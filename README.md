<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

[English](README.md) | [简体中文](README.zh-CN.md)

# 🔌 Ultralytics SDKs

[![Ultralytics Actions](https://github.com/ultralytics/sdk/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/format.yml)
[![CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/ci.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://www.reddit.com/r/ultralytics/)

Typed SDKs for the [Ultralytics Platform API](https://platform.ultralytics.com), generated from a pinned contract with [Ultralytics OpenAPI](https://github.com/ultralytics/openapi). The [interactive API reference](https://platform.ultralytics.com/api/docs) renders the live contract directly and includes Python SDK examples.

| Output                        | Status      |
| ----------------------------- | ----------- |
| [Interactive API reference](https://platform.ultralytics.com/api/docs) | Available   |
| [Python SDK](https://pypi.org/project/ultralytics-platform/) | Available   |
| TypeScript SDK                | Coming soon |
| Go SDK                        | Coming soon |
| Java SDK                      | Coming soon |

## 🐍 Python

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics-platform?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics-platform/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics-platform)](https://clickpy.clickhouse.com/dashboard/ultralytics-platform) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics-platform?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics-platform/)

Install the standalone [`ultralytics-platform`](https://pypi.org/project/ultralytics-platform/) package from PyPI in a [**Python >=3.11**](https://www.python.org/) environment. It has one lightweight runtime dependency (`httpx`) and does not install the larger `ultralytics` package:

```bash
uv pip install ultralytics-platform
```

Pass your [Platform API key](https://platform.ultralytics.com/settings?tab=api-keys) directly as shown below. Alternatively, set `ULTRALYTICS_API_KEY` and omit the `api_key` argument.

```python
from ultralytics_platform import Platform

with Platform(api_key="YOUR_API_KEY") as client:
    datasets = client.datasets.list("your_username")
    training = client.training.start(model_id="model_id", train_args={"epochs": 10})
    model = client.models.retrieve("your_username", "project", "model")
    export = client.exports.create("your_username", "project", "model", format="onnx")
    deployment = client.deployments.create(
        "your_username",
        project="project",
        model="model",
        deployment="production",
        name="Production",
        region="us-central1",
    )
```

The asynchronous client exposes the same resource tree:

```python
import asyncio

from ultralytics_platform import AsyncPlatform


async def main():
    async with AsyncPlatform(api_key="YOUR_API_KEY") as client:
        datasets = await client.datasets.list("your_username")


asyncio.run(main())
```

The package includes typed responses, multipart uploads, retries for temporary failures, structured API errors, custom HTTP clients, and context-manager cleanup. It requires Python 3.11 or newer.

## 🧩 One Contract, Multiple Outputs

[Ultralytics Platform](https://platform.ultralytics.com) owns the API contract. This repository pins a versioned snapshot with its generated descendants:

```text
Platform OpenAPI contract
    ├── openapi.json      # Versioned contract snapshot
    ├── README.python.md  # Python package README source
    └── sdk/
        ├── python/     # ultralytics-platform
        ├── typescript/ # coming soon
        ├── go/         # coming soon
        └── java/       # coming soon
```

`openapi.config.json` contains product and package configuration, including the source path for `README.python.md`. `openapi.json` and `openapi.sha256` pin the exact consumed contract. Generated files are never edited manually; update the contract snapshot, configuration, package README source, or generator and regenerate.

## 🛠️ Validation

[CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml) regenerates the Python SDK from the versioned contract with the `main` branch of [Ultralytics OpenAPI](https://github.com/ultralytics/openapi), then fails on contract mismatch or generated drift. Pushes to `main`, scheduled runs, and manual runs detect upstream contract changes without breaking unrelated pull requests. CI also formats and lints Python, compiles the package, builds its wheel, installs through the Git subdirectory boundary, and exercises representative sync and async requests against a mock transport. The package version is the contract's `info.version`, so a contract version bump reaching `main` publishes [`ultralytics-platform`](https://pypi.org/project/ultralytics-platform/) to PyPI through trusted publishing.

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
