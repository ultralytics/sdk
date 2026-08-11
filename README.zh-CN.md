<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

[English](README.md) | [简体中文](README.zh-CN.md)

# 🔌 Ultralytics SDKs

[![Ultralytics Actions](https://github.com/ultralytics/sdk/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/format.yml)
[![CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/ci.yml)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

Ultralytics Platform API 的类型化 SDK 和交互式文档。所有输出均使用 [Ultralytics OpenAPI](https://github.com/ultralytics/openapi)，从同一份固定版本的 OpenAPI 契约生成。

| 输出 | 状态 |
| --- | --- |
| 交互式 API 文档 | 已可用 |
| Python SDK | 已可用 |
| TypeScript SDK | 即将推出 |
| Go SDK | 即将推出 |
| Java SDK | 即将推出 |

## 🐍 Python

首个版本验证期间，可直接从此仓库安装：

```bash
uv pip install "git+https://github.com/ultralytics/sdk.git#subdirectory=sdk/python"
```

设置 `ULTRALYTICS_API_KEY`，然后使用同步客户端：

```python
from ultralytics_platform import Platform

with Platform() as client:
    datasets = client.datasets.list()
    training = client.training.start(model_id="model_id", train_args={"epochs": 10})
    model = client.models.retrieve("model_id")
    export = client.exports.create(model_id="model_id", format="onnx")
    deployment = client.deployments.create(model_id="model_id", name="production", region="us-central1")
```

异步客户端提供相同的资源树：

```python
import asyncio

from ultralytics_platform import AsyncPlatform


async def main():
    async with AsyncPlatform() as client:
        datasets = await client.datasets.list()


asyncio.run(main())
```

该包包含类型化响应、多部分上传、临时故障重试、结构化 API 错误、自定义 HTTP 客户端以及上下文管理器清理功能。它需要 Python 3.11 或更高版本。

## 🧩 一份契约，多种输出

Platform 拥有 API 契约。此仓库固定该契约的版本，并仅提交生成的派生文件：

```text
Platform OpenAPI 契约
    ├── docs/          # 静态交互式 API 参考
    └── sdk/
        ├── python/     # ultralytics-platform
        ├── typescript/（即将推出）
        ├── go/        （即将推出）
        └── java/      （即将推出）
```

`openapi.config.json` 包含产品和软件包配置。`openapi.sha256` 固定所使用契约的确切版本。切勿手动编辑生成的文件；请更新契约、配置或生成器，然后重新生成。

## 🛠️ 验证

CI 使用固定版本的生成器重新生成文档和 Python SDK，并在契约不匹配或生成内容漂移时失败。它还会格式化和检查 Python、编译软件包、构建 wheel、通过 Git 子目录边界进行安装，并使用模拟传输测试具有代表性的同步和异步请求。目前尚未向 PyPI 发布任何软件包。

## 💡 贡献

Ultralytics 因社区协作而蓬勃发展，我们非常重视您的贡献！请参阅[贡献指南](https://docs.ultralytics.com/zh/help/contributing)，了解参与方式。我们也欢迎您通过[问卷调查](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey)分享反馈。衷心感谢 🙏 所有贡献者！

API 结构变更应在 Platform OpenAPI 契约中完成；不应直接编辑此仓库中的生成文件。

[![Ultralytics 开源贡献者](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/sdk/graphs/contributors)

## 📄 许可证

- **AGPL-3.0 许可证**：生成的 SDK 和文档采用 [AGPL-3.0 许可证](LICENSE)。
- **企业许可证**：商业许可证可通过 [Ultralytics Licensing](https://www.ultralytics.com/license) 单独获取。

## 📫 联系我们

如需报告与 Ultralytics SDK 相关的错误或提出功能建议，请通过 [GitHub Issues](https://github.com/ultralytics/sdk/issues) 提交。欢迎加入我们的 [Discord](https://discord.com/invite/ultralytics) 社区参与讨论并获取支持！

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
