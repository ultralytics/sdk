<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

[English](README.md) | [简体中文](README.zh-CN.md)

# 🔌 Ultralytics SDKs

[![Ultralytics Actions](https://github.com/ultralytics/sdk/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/format.yml)
[![CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/ci.yml)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

Typed SDKs for the Ultralytics Platform API, generated from a pinned contract with [Ultralytics OpenAPI](https://github.com/ultralytics/openapi). The [interactive API reference](https://platform.ultralytics.com/api/docs) renders the live contract directly and includes Python SDK examples.

| Output                        | Status      |
| ----------------------------- | ----------- |
| [Interactive API reference](https://platform.ultralytics.com/api/docs) | Available   |
| Python SDK                    | Available   |
| TypeScript SDK                | Coming soon |
| Go SDK                        | Coming soon |
| Java SDK                      | Coming soon |

## 🐍 Python

Install directly from this repository while the first release is being validated:

```bash
uv pip install "git+https://github.com/ultralytics/sdk.git#subdirectory=sdk/python"
```

Pass your API key directly to the synchronous client:

```python
from ultralytics_platform import Platform

with Platform(api_key="YOUR_API_KEY") as client:
    datasets = client.datasets.list()
    training = client.training.start(model_id="model_id", train_args={"epochs": 10})
    model = client.models.retrieve("model_id")
    export = client.exports.create(model_id="model_id", format="onnx")
    deployment = client.deployments.create(model_id="model_id", name="production", region="us-central1")
```

The asynchronous client exposes the same resource tree:

```python
import asyncio

from ultralytics_platform import AsyncPlatform


async def main():
    async with AsyncPlatform(api_key="YOUR_API_KEY") as client:
        datasets = await client.datasets.list()


asyncio.run(main())
```

The package includes typed responses, multipart uploads, retries for temporary failures, structured API errors, custom HTTP clients, and context-manager cleanup. It requires Python 3.11 or newer.

## 🧩 One Contract, Multiple Outputs

Platform owns the API contract. This repository pins that contract and commits only generated descendants:

```text
Platform OpenAPI contract
    └── sdk/
        ├── python/     # ultralytics-platform
        ├── typescript/ # coming soon
        ├── go/         # coming soon
        └── java/       # coming soon
```

`openapi.config.json` contains product and package configuration. `openapi.sha256` pins the exact consumed contract. Generated files are never edited manually; update the contract, configuration, or generator and regenerate.

## 🛠️ Validation

CI regenerates the Python SDK with a pinned generator revision, then fails on contract mismatch or generated drift. It also formats and lints Python, compiles the package, builds its wheel, installs through the Git subdirectory boundary, and exercises representative sync and async requests against a mock transport. No package is published to PyPI yet.

## 💡 Contribute

Ultralytics thrives on community collaboration, and we deeply value your contributions! Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for details on how you can get involved. We also encourage you to share your feedback through our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge thank you 🙏 to all our contributors!

API shape changes belong in the Platform OpenAPI contract; generated files in this repository should not be edited directly.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/sdk/graphs/contributors)

## 📄 License

- **AGPL-3.0 License**: The generated SDKs are licensed under the [AGPL-3.0 License](LICENSE).
- **Enterprise License**: Commercial licensing is available separately through [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📫 Contact

For bug reports or feature suggestions related to Ultralytics SDKs, please submit an issue via [GitHub Issues](https://github.com/ultralytics/sdk/issues). Join our [Discord](https://discord.com/invite/ultralytics) community for discussions and support!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.youtube.com/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
