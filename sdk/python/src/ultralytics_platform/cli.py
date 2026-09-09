# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Unified Ultralytics CLI: local YOLO commands and Platform SDK operations discovered from the SDK itself."""

from __future__ import annotations

import importlib.util
import inspect
import json
import os
import sys
import types
import typing
from collections.abc import Sequence
from contextlib import ExitStack
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, BinaryIO, Literal, get_args, get_origin, get_type_hints

from . import APIConnectionError, APIError, NotGiven, Platform
from ._cli_metadata import MULTIPART_FILES

JSON_TYPES = {type(None): "null", bool: "boolean", int: "integer", float: "number", str: "string", list: "array"}
JSON_TYPES |= {dict: "object", Sequence: "array"}


def kinds(annotation: Any) -> tuple[set[str], list | None]:
    """Map a generated SDK annotation to JSON kinds and literal choices; empty kinds accept any JSON value."""
    if annotation is Any:
        return set(), None
    if annotation is BinaryIO:
        return {"binary"}, None
    origin = get_origin(annotation)
    if origin is Literal:
        values = list(get_args(annotation))
        return {JSON_TYPES[type(value)] for value in values}, values
    if origin in {types.UnionType, typing.Union}:
        members = [member for member in get_args(annotation) if member is not NotGiven]
        parts = [kinds(member) for member in members]
        if any(not part[0] for part in parts):
            return set(), None
        literal = all(get_origin(member) is Literal or member is type(None) for member in members)
        return set().union(*(part[0] for part in parts)), [
            v for _, c in parts for v in c or [None]
        ] if literal else None
    return {JSON_TYPES[origin or annotation]}, None


def describe(method) -> dict[str, dict]:
    """Argument descriptors from the SDK signature: positional parameters are path parameters."""
    hints = get_type_hints(method)
    result = {}
    for parameter in inspect.signature(method).parameters.values():
        if parameter.name in {"timeout", "extra_headers"}:
            continue
        types_, choices = kinds(hints[parameter.name])
        result[parameter.name] = {
            "types": types_,
            "choices": choices,
            "required": parameter.default is parameter.empty,
            "path": parameter.kind is parameter.POSITIONAL_OR_KEYWORD,
        }
    return result


def assignments(tokens: list[str]) -> dict[str, str | None]:
    """Allow spaces before '=' while preserving empty values and subsequent shell arguments."""
    result = {}
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if i + 1 < len(tokens) and tokens[i + 1].startswith("=") and "=" not in token:
            i += 1
            token += tokens[i]
        key, separator, value = token.partition("=")
        i += 1
        if (key.startswith("-") and token not in {"--help", "-h"}) or not key:
            raise ValueError("Use key=value arguments, not --key value")
        if key in result:
            raise ValueError(f"duplicate argument: {key}")
        result[key] = value if separator else None
    return result


def parse(raw: dict[str, str | None], arguments: dict[str, dict]) -> dict:
    """Convert supplied arguments using the SDK signature; only supplied values reach the SDK."""
    result = {}
    stdin_used = False
    for name, text in raw.items():
        if name not in arguments:
            raise ValueError(f"unknown argument: {name}")
        arg = arguments[name]
        kinds_ = {"string"} if "binary" in arg["types"] else arg["types"]
        if text is None:
            if kinds_ - {"null"} != {"boolean"}:
                raise ValueError(f"{name} requires a value; only booleans may be bare")
            text = "True"
        if text.startswith("@") and (not kinds_ or kinds_ & {"object", "array"}):
            if text == "@-":
                if stdin_used:
                    raise ValueError("stdin can supply only one input")
                stdin_used = True
                text = sys.stdin.read()
            else:
                try:
                    text = Path(text[1:]).read_text(encoding="utf-8")
                except OSError as error:
                    raise ValueError(f"{name}: cannot read JSON input file") from error
        expected = "|".join(sorted(kinds_)) or "JSON"
        try:
            if text.lower() in {"null", "none"} and (not kinds_ or "null" in kinds_):
                value = None
            elif kinds_ - {"null"} == {"string"}:
                value = text
            elif "boolean" in kinds_ and text.lower() in {"true", "false"}:
                value = text.lower() == "true"
            elif kinds_ - {"null"} == {"integer"}:
                value = int(text)
            elif kinds_ - {"null"} == {"number"}:
                value = float(text)
            else:
                value = json.loads(text)
            json.dumps(value, allow_nan=False)  # Reject non-finite numbers at any depth.
        except ValueError as error:
            raise ValueError(f"{name}: expected {expected}; objects and arrays require valid JSON") from error
        actual = JSON_TYPES.get(type(value))
        if kinds_ and actual not in kinds_ and not (actual == "integer" and "number" in kinds_):
            raise ValueError(f"{name}: expected {expected}")
        if arg["choices"] is not None and value not in arg["choices"]:
            raise ValueError(f"{name}: choose one of {json.dumps(arg['choices'])}")
        result[name] = value
    missing = [
        n for n, a in arguments.items() if a["required"] and n not in result and not (a["path"] and n == "owner")
    ]
    if missing:
        raise ValueError(f"missing arguments: {', '.join(missing)}")
    return result


def open_inputs(values: dict, arguments: dict[str, dict], files: list[str], stack: ExitStack) -> dict:
    """Open binary arguments and the multipart body fields the generator identified as binary."""
    fields = [(values, name) for name, arg in arguments.items() if "binary" in arg["types"] and name in values]
    fields += [
        (values["body"], field) for field in files if isinstance(values.get("body"), dict) and field in values["body"]
    ]
    for container, key in fields:
        value = container[key]
        if not isinstance(value, str) or not value.startswith("@") or value == "@-":
            raise ValueError(f"{key}: binary inputs require @path (not stdin)")
        container[key] = stack.enter_context(open(value[1:], "rb"))  # noqa: SIM115 - caller owns the ExitStack
    return values


def output(value) -> None:
    """Write one complete SDK response to stdout; never fetch additional pages."""
    if isinstance(value, bytes):
        sys.stdout.buffer.write(value)
    elif isinstance(value, str):
        print(value)
    else:
        print(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False))


def defaults(methods: dict[str, Any]) -> dict[str, list[str]]:
    """Implicit verbs: bare `list`, and `retrieve` when its extra path identifiers are supplied."""
    if "list" not in methods:
        return {}
    result = {"list": []}
    if "retrieve" in methods:
        parents = {name for name, arg in describe(methods["list"]).items() if arg["path"]}
        identifiers = [
            name for name, arg in describe(methods["retrieve"]).items() if arg["path"] and name not in parents
        ]
        if identifiers:
            result["retrieve"] = identifiers
    return result


def dispatch(tokens: list[str]) -> int:
    """Execute one SDK operation, inferring only a missing resource-path owner."""
    tokens = list(tokens)
    with ExitStack() as stack:
        client = stack.enter_context(
            Platform(base_url=os.getenv("ULTRALYTICS_PLATFORM_URL", "https://platform.ultralytics.com"))
        )
        resources = {
            name.replace("_", "-"): {
                method.replace("_", "-"): member
                for method, member in inspect.getmembers(resource, inspect.ismethod)
                if not method.startswith("_")
            }
            for name, resource in vars(client).items()
            if not name.startswith("_")
        }
        resource = tokens.pop(0) if tokens and tokens[0] not in {"help", "--help", "-h"} else None
        if resource is not None and resource not in resources:
            raise ValueError("Unknown command; use --help to list API operations")
        methods = resources[resource] if resource is not None else {}
        implicit = defaults(methods)
        method = tokens.pop(0) if tokens and tokens[0] in methods else None
        raw = assignments(tokens)
        help_requested = any(key in {"help", "--help", "-h"} and value is None for key, value in raw.items())
        if resource is not None and method is None and not help_requested:
            method = next((name for name, keys in implicit.items() if keys and any(key in raw for key in keys)), None)
            method = method or ("list" if "list" in implicit else None)
        if method is None and tokens and not help_requested:
            raise ValueError("Choose a resource operation before supplying arguments")
        if method is None or help_requested:
            print("<resource> [operation] key=value ... (path owner defaults to the logged-in username)")
            listing = {resource: {method: methods[method]} if method else methods} if resource else resources
            for resource_name, members in listing.items():
                for method_name, member in members.items():
                    doc = inspect.getdoc(member) or ""
                    print(f"  {resource_name} {method_name}: {doc.partition(chr(10))[0].rstrip('.')}")
                    if method is not None:
                        for line in doc.splitlines()[1:]:
                            if not line.startswith(("    timeout (", "    extra_headers (")):
                                print(line)
            return 0
        arguments = describe(methods[method])
        values = parse(raw, arguments)
        key = f"{resource.replace('-', '_')}.{method.replace('-', '_')}"
        open_inputs(values, arguments, MULTIPART_FILES.get(key, []), stack)
        if "owner" not in values and arguments.get("owner", {}).get("path"):
            username = client.account.summary().get("username")
            if not isinstance(username, str) or not username:
                raise ValueError("Could not infer owner; supply owner= explicitly")
            values["owner"] = username
        output(methods[method](**values))
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the unified CLI and translate SDK errors into process exit codes."""
    args = list(sys.argv[1:] if argv is None else argv)
    try:
        if not args or args in (["help"], ["--help"], ["-h"]):
            print(
                "ul login API_KEY | logout | version\n"
                "ul train|val|predict|export|track|benchmark key=value ...\n"
                "ul settings|checks|cfg|copy-cfg|solutions ...\n"
                "ul cloud <resource> [operation] key=value ...\n"
                "Login/logout and local commands require ultralytics. Use ul cloud --help to list API commands.\n"
                "Omitted path owners default to the logged-in username. No --key value options."
            )
            return 0
        if args in (["version"], ["--version"]):
            print(f"ultralytics-platform {version('ultralytics-platform')}")
            try:
                print(f"ultralytics {version('ultralytics')}")
            except PackageNotFoundError:
                print("ultralytics not installed")
            return 0
        if args[0] == "cloud":
            return dispatch(args[1:])
        if importlib.util.find_spec("ultralytics") is None:
            raise ValueError(
                "This command requires ultralytics. Install it in this environment: pip install ultralytics"
            )
        original = sys.argv[:]
        try:
            # YOLO aliases sys.argv as ARGV and recognizes its executable name in prediction paths.
            sys.argv[:] = ["yolo", *args]
            from ultralytics.cfg import entrypoint

            entrypoint()
        finally:
            sys.argv[:] = original
        return 0
    except APIError as error:
        body = error.json
        detail = body.get("error") if isinstance(body, dict) else None
        print(
            f"API request failed (HTTP {error.status_code}){f': {detail}' if isinstance(detail, str) else '.'}",
            file=sys.stderr,
        )
        return 1
    except APIConnectionError:
        print("Could not connect to API.", file=sys.stderr)
        return 1
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
