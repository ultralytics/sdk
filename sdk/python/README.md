# Ultralytics Platform API Python SDK

Typed synchronous and asynchronous Python clients generated from the Ultralytics Platform API OpenAPI contract.

## Installation

```bash
uv pip install ultralytics-platform
```

## Usage

Set `ULTRALYTICS_API_KEY`, then create one client with grouped API resources:

```python
from ultralytics_platform import Platform

client = Platform()
```

Every resource is also available through the asynchronous client:

```python
from ultralytics_platform import AsyncPlatform

client = AsyncPlatform()
```

The clients include typed responses, multipart uploads, retries for temporary failures, and structured API errors.
