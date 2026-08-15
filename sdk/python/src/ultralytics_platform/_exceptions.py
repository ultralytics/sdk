# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import json
from typing import Any


class APIError(Exception):
    """Error returned by the API."""

    def __init__(self, status_code: int, body: str, request_id: str | None = None) -> None:
        self.status_code = status_code
        self.body = body
        self.request_id = request_id
        super().__init__(f"API request failed with status {status_code}: {body}")

    @property
    def json(self) -> Any:
        """Parsed JSON body, or None when the body is not JSON."""
        try:
            return json.loads(self.body)
        except ValueError:
            return None


class APIConnectionError(Exception):
    """Network error raised while contacting the API."""
