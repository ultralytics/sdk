<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🔌 Ultralytics Platform API Python SDK

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics) [![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com) [![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

Typed synchronous and asynchronous Python clients generated from the [Ultralytics Platform API](https://platform.ultralytics.com) contract with [Ultralytics OpenAPI](https://github.com/ultralytics/openapi). The [interactive API reference](https://platform.ultralytics.com/api/docs) documents every resource and includes Python examples.

## 🐍 Python

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics-platform?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics-platform/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics-platform)](https://clickpy.clickhouse.com/dashboard/ultralytics-platform) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics-platform?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics-platform/)

Install [`ultralytics-platform`](https://pypi.org/project/ultralytics-platform/) from PyPI in a [**Python >=3.11**](https://www.python.org/) environment:

```bash
uv pip install ultralytics-platform
```

Pass your [API key](https://platform.ultralytics.com/settings?tab=api-keys) directly as shown below. Alternatively, set `ULTRALYTICS_API_KEY` and omit the `api_key` argument.

```python
from ultralytics_platform import Platform

with Platform(api_key="YOUR_API_KEY") as client:
    response = client.datasets.list()
```

The asynchronous client exposes the same resource tree:

```python
import asyncio

from ultralytics_platform import AsyncPlatform


async def main():
    async with AsyncPlatform(api_key="YOUR_API_KEY") as client:
        response = await client.datasets.list()


asyncio.run(main())
```

The package includes typed responses, multipart uploads, retries for temporary failures, structured API errors, custom HTTP clients, and context-manager cleanup.

## 🧩 One Contract, Typed Python

The [Ultralytics Platform API](https://platform.ultralytics.com) contract is the single source of truth for the generated client:

```text
OpenAPI contract
    └── Python SDK # ultralytics-platform
```

The [source repository](https://github.com/ultralytics/sdk) pins the consumed contract and generated output so API changes remain deterministic and reviewable. Generated SDK files should never be edited manually; update the contract, consumer configuration, [package README source](https://github.com/ultralytics/sdk/blob/main/README.python.md), or [generator](https://github.com/ultralytics/openapi) and regenerate.

## 🛠️ Validation

[CI](https://github.com/ultralytics/sdk/actions) regenerates the Python SDK to detect contract mismatch or generated drift. It also formats and lints Python, compiles the package, builds its wheel, installs it through the package boundary, and exercises representative synchronous and asynchronous requests.

## 💡 Contribute

[Ultralytics](https://www.ultralytics.com/) thrives on community collaboration, and we deeply value your contributions! Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for details on how you can get involved. We also encourage you to share your feedback through our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge thank you 🙏 to all our contributors!

API shape changes belong in the service OpenAPI contract; generated files should not be edited directly.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/sdk/graphs/contributors)

## 📄 License

- **AGPL-3.0 License**: The generated SDK is licensed under the [AGPL-3.0 License](https://spdx.org/licenses/AGPL-3.0-only.html).
- **Enterprise License**: Commercial licensing is available separately through [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📫 Contact

For bug reports or feature suggestions related to this SDK, please submit an issue via [GitHub Issues](https://github.com/ultralytics/sdk/issues). Join our [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), or [Community Forums](https://community.ultralytics.com/) for discussions and support!

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
