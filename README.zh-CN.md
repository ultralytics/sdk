<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

[English](README.md) | [简体中文](README.zh-CN.md)

# 🔌 Ultralytics SDKs

[![Ultralytics Actions](https://github.com/ultralytics/sdk/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/format.yml)
[![CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/sdk/actions/workflows/ci.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics-platform?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics-platform/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics-platform)](https://clickpy.clickhouse.com/dashboard/ultralytics-platform) [![Python >=3.11](https://img.shields.io/badge/python-%E2%89%A53.11-blue?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics-platform/)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

[Ultralytics Platform API](https://platform.ultralytics.com) 的类型化 SDK，使用 [Ultralytics OpenAPI](https://github.com/ultralytics/openapi) 从固定版本的契约生成。[交互式 API 参考](https://platform.ultralytics.com/api/docs)直接呈现实时契约，并包含 Python SDK 示例。

| 输出 | 状态 |
| --- | --- |
| [交互式 API 参考](https://platform.ultralytics.com/api/docs) | 已可用 |
| [Python SDK](https://pypi.org/project/ultralytics-platform/) | 已可用 |
| TypeScript SDK | 即将推出 |
| Go SDK | 即将推出 |
| Java SDK | 即将推出 |

## 🐍 Python

在 [**Python >=3.11**](https://www.python.org/) 环境中从 PyPI 安装 [`ultralytics-platform`](https://pypi.org/project/ultralytics-platform/)：

```bash
uv pip install ultralytics-platform
```

如下所示，您可以直接传递 [Platform API 密钥](https://platform.ultralytics.com/settings?tab=api-keys)。或者，设置 `ULTRALYTICS_API_KEY` 并省略 `api_key` 参数。

```python
from ultralytics_platform import Platform

with Platform(api_key="YOUR_API_KEY") as client:
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
    async with AsyncPlatform(api_key="YOUR_API_KEY") as client:
        datasets = await client.datasets.list()


asyncio.run(main())
```

该包包含类型化响应、多部分上传、临时故障重试、结构化 API 错误、自定义 HTTP 客户端以及上下文管理器清理功能。它需要 Python 3.11 或更高版本。

## 🧩 一份契约，多种输出

[Ultralytics Platform](https://platform.ultralytics.com) 拥有 API 契约。此仓库固定契约快照的版本，并将其与生成的派生文件一起提交：

```text
Platform OpenAPI 契约
    ├── openapi.json      # 版本化的契约快照
    ├── README.python.md  # Python 软件包 README 源文件
    └── sdk/
        ├── python/     # ultralytics-platform
        ├── typescript/（即将推出）
        ├── go/        （即将推出）
        └── java/      （即将推出）
```

`openapi.config.json` 包含产品和软件包配置，包括 `README.python.md` 的源文件路径。`openapi.json` 和 `openapi.sha256` 固定所使用契约的确切版本。切勿手动编辑生成的文件；请更新契约快照、配置、软件包 README 源文件或生成器，然后重新生成。

## 🛠️ 验证

[CI](https://github.com/ultralytics/sdk/actions/workflows/ci.yml) 使用版本化的契约和 [Ultralytics OpenAPI](https://github.com/ultralytics/openapi) 的 `main` 分支重新生成 Python SDK，并在契约不匹配或生成内容漂移时失败。计划任务和手动运行会检测上游契约变更，而不会中断无关的拉取请求。CI 还会格式化和检查 Python、编译软件包、构建 wheel、通过 Git 子目录边界进行安装，并使用模拟传输测试具有代表性的同步和异步请求。`main` 上的版本更新会通过可信发布将 [`ultralytics-platform`](https://pypi.org/project/ultralytics-platform/) 发布到 PyPI。

## 💡 贡献

Ultralytics 因社区协作而蓬勃发展，我们非常重视您的贡献！请参阅[贡献指南](https://docs.ultralytics.com/zh/help/contributing)，了解参与方式。我们也欢迎您通过[问卷调查](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey)分享反馈。衷心感谢 🙏 所有贡献者！

API 结构变更应在 Platform OpenAPI 契约中完成；不应直接编辑此仓库中的生成文件。

[![Ultralytics 开源贡献者](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/sdk/graphs/contributors)

## 📄 许可证

- **AGPL-3.0 许可证**：生成的 SDK 采用 [AGPL-3.0 许可证](LICENSE)。
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
