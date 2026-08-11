<div align="center">
  <a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🔌 Ultralytics Platform API Python SDK

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics-platform?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics-platform/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics-platform?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics-platform/)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com)

</div>

Typed synchronous and asynchronous Python clients generated from the Ultralytics Platform API contract.

## 🐍 Installation

```bash
uv pip install ultralytics-platform
```

## 🔑 Authentication

Pass your API key directly when creating a client:

```python
from ultralytics_platform import Platform

client = Platform(api_key="YOUR_API_KEY")
```

Alternatively, set `ULTRALYTICS_API_KEY` and omit the `api_key` argument.

## 🚀 Usage

Resources are grouped under one client and support context-manager cleanup:

```python
from ultralytics_platform import Platform

with Platform() as client:
    response = client.datasets.list()
```

Every resource is also available through the asynchronous client:

```python
import asyncio

from ultralytics_platform import AsyncPlatform


async def main():
    async with AsyncPlatform() as client:
        response = await client.datasets.list()


asyncio.run(main())
```

## ✨ Features

- Typed synchronous and asynchronous resource clients
- Multipart uploads and custom HTTP clients
- Automatic retries for temporary failures
- Structured API and connection errors
- Context-manager cleanup

## 📄 License

This SDK is licensed under the [AGPL-3.0 License](LICENSE). Commercial licensing is available through [Ultralytics Licensing](https://www.ultralytics.com/license).

## 🤝 Community

For help and feedback, join the [Ultralytics community](https://community.ultralytics.com/) or [Discord](https://discord.com/invite/ultralytics).
