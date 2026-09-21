# AGENTS.md

Repository guidance for coding agents. `CLAUDE.md` is a symlink to this file.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## API and SDK versioning (CRITICAL)

**One version, one owner: `ultralytics/portal` → `scripts/generate-openapi.ts` → Alpha's `info.version`. The Python SDK package version MUST equal the API contract version it contains.** This SDK repository consumes the deployed contract through automation; it does not choose release versions.

- NEVER set `python.version` in `openapi.config.json`, independently bump the SDK patch, or edit versions in generated files. Do not restore automatic patch bumps or `max(API version, SDK version)` logic. A newer SDK number is a mismatch, not successful coordination.
- This also applies to SDK-only CLI/help/auth fixes and generator improvements. Merge the source fix, bump Alpha's contract version in Portal, deploy it, then let SDK contract synchronization regenerate and publish that same version. Do not manually repair the snapshot or generated descendants to manufacture a release.
- Before updating a consumer's minimum SDK requirement, verify the published wheel contains the required behavior and its version matches the deployed API. A successful install or green CI alone does not prove this.
- If SDK versions have already been published ahead of the API, advance the Portal-owned API version beyond every published SDK version, then synchronize. Never downgrade the SDK, reuse a published version, or claim the offset will self-heal. API `0.1.50` with SDK `0.1.52` is INVALID; both at `0.1.52` is valid.

Contract snapshots keep upstream samples until Portal deploys its rebuilt OpenAPI output and automation synchronizes it. Keep both READMEs aligned with `.github/workflows/ci.yml`.

## Commands and validation

```bash
uv venv --python 3.11
source .venv/bin/activate
uv pip install pytest jsonschema referencing -e ./sdk/python

sha256sum --check openapi.sha256
if [ -d .generator ]; then
  git -C .generator switch main
  git -C .generator pull --ff-only origin main
else
  git clone --branch main https://github.com/ultralytics/openapi.git .generator
fi
export OPENAPI_CONFIG="$PWD/openapi.config.json"
(cd .generator && bun install --frozen-lockfile && bun run generate)
diff --recursive --unified sdk/python .generator/generated/python

pytest tests -v
uvx ruff@0.16.2 format --check --line-length 120 sdk/python tests cli.py auth.py
uvx ruff@0.16.2 check sdk/python tests cli.py auth.py
```

Use the generator's `main` branch, never a pinned SHA or tag; update an existing `.generator` checkout before regenerating. Check drift before running tests/builds, which leave ignored artifacts in the generated tree. After intentional source changes, inspect the diff, then copy with `rsync --archive --delete .generator/generated/python/ sdk/python/`. Never repair generated files by hand. Install the package in the same interpreter that runs pytest. Use `python -m ultralytics_platform.cli` if the system `ul` command shadows the console script.

## Where to look

- CLI and credential customization → `cli.py`, `auth.py`.
- Generator configuration and README template → `openapi.config.json`, `README.python.md`.
- Pinned contract → `openapi.json`, `openapi.sha256`.
- Generated package → `sdk/python/`.
- Regeneration and contract sync → `.github/workflows/ci.yml`.
- Release rules → `.github/workflows/publish.yml`, `README.md`.

## Conventions

- Ultralytics-owned PyPI packages use `MAJOR.MINOR.PATCH` versions only; no suffixes.
- License headers (`# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license`) are added automatically by Ultralytics Actions — don't add or revert them manually. Generated files receive the same header from the generator (`header` in `openapi.config.json`).
- Google-style docstrings, `from __future__ import annotations` for modern type hints, line length 120; formatting is checked by `ci.yml` with the pinned `uvx ruff@0.16.2` (`format.yml` runs with `python: false`, so nothing reformats Python on PR branches) and the generator formats its own output.

## Pitfalls

- `tests/live_readonly.py` is not read-only and is not collected by pytest. It needs `ULTRALYTICS_API_KEY`, runs against production, creates and deletes `sdk-ci-<timestamp>` projects/datasets/models, uploads `coco32.zip` from `ultralytics/assets`, and paces requests at 0.75s. Its response hook validates successful responses that declare a JSON schema against `openapi.json`, rejects 401/5xx and undocumented statuses, and checks the exact error message of any 403 against `EXPECTED_FORBIDDEN`. Operations that cannot succeed on the canary account (training start, export, deployment create, ...) are wrapped in `expected_error(...)` and must fail; the final gate fails when the set of error-only operations drifts from those classifications. It exercises explicit scenarios, not every operation (e.g. `models.find_similar_training_images` is not called). Run it only deliberately.
- `ULTRALYTICS_API_KEY=""` (empty) does not disable auth — `_resolve_api_key` treats an empty environment value as unset and falls through to the saved `yolo login` key (that is how `tests/test_cli.py` forces the settings path). Only an explicit `Platform(api_key="")` disables the header.
- Shell quoting: JSON arguments need single quotes (`'train_args={"epochs":1}'`), `@-` may be used by at most one argument per invocation, and binary fields must be `@path` (never stdin) even when nested inside a multipart `body` JSON.
- `format.yml` will not reformat Python or Markdown for you here (`python: false`, `prettier: false`); run the pinned `uvx ruff@0.16.2 format --line-length 120` on `cli.py`, `auth.py`, and `tests/` yourself before pushing.
