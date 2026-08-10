<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🔌 Ultralytics SDKs

[![Ultralytics Actions](https://github.com/ultralytics/sdk/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/format.yml)
[![CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/ci.yml)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

Typed SDKs and interactive documentation for the Ultralytics Platform API. Every output is generated from the same pinned OpenAPI contract with [Ultralytics OpenAPI](https://github.com/ultralytics/openapi).

| Output                        | Status      |
| ----------------------------- | ----------- |
| Interactive API documentation | Available   |
| Python SDK                    | Available   |
| TypeScript SDK                | Coming soon |
| Go SDK                        | Coming soon |
| Java SDK                      | Coming soon |

## 🐍 Python

Install directly from this repository while the first release is being validated:

```bash
uv pip install "git+https://github.com/ultralytics/sdk.git#subdirectory=sdk/python"
```

Set `ULTRALYTICS_API_KEY`, then use the synchronous client:

```python
from ultralytics_platform import Platform

with Platform() as client:
    datasets = client.datasets.list()
    training = client.training.start(model_id="model_id", train_args={"epochs": 10})
    model = client.models.retrieve("model_id")
    export = client.exports.create(model_id="model_id", format="onnx")
    deployment = client.deployments.create(model_id="model_id", name="production", region="us-central1")
```

The asynchronous client exposes the same resource tree:

```python
from ultralytics_platform import AsyncPlatform

async with AsyncPlatform() as client:
    datasets = await client.datasets.list()
```

The package includes typed responses, multipart uploads, retries for temporary failures, structured API errors, custom HTTP clients, and context-manager cleanup. It requires Python 3.11 or newer.

## 🧩 One Contract, Multiple Outputs

Platform owns the API contract. This repository pins that contract and commits only generated descendants:

```text
Platform OpenAPI contract
    ├── docs/          # Static interactive API reference
    └── sdk/
        ├── python/  # ultralytics-platform
        ├── typescript/ (coming soon)
        ├── go/         (coming soon)
        └── java/       (coming soon)
```

`openapi.config.json` contains product and package configuration. `openapi.sha256` pins the exact consumed contract. Generated files are never edited manually; update the contract, configuration, or generator and regenerate.

## 🛠️ Validation

CI regenerates the docs and Python SDK with a pinned generator revision, then fails on contract mismatch or generated drift. It also formats and lints Python, compiles the package, builds its wheel, installs through the Git subdirectory boundary, and exercises representative sync and async requests against a mock transport. No package is published to PyPI yet.

## 💡 Contribute

Bug reports and focused feature proposals are welcome in [GitHub Issues](https://github.com/ultralytics/sdk/issues). API shape changes belong in the Platform OpenAPI contract; generated files in this repository should not be edited directly.

## 📄 License

The generated SDKs and documentation are licensed under the [AGPL-3.0 License](LICENSE). For commercial licensing, contact [Ultralytics Licensing](https://www.ultralytics.com/license).
