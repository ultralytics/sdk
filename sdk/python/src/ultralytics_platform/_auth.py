# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import json
import os
import stat
import sys
import tempfile
from pathlib import Path


def get_api_key() -> str | None:
    """Read the Platform key saved by yolo login without importing the ML package."""
    if config_dir := os.environ.get("YOLO_CONFIG_DIR"):
        directory = Path(config_dir).expanduser() / "Ultralytics"
    elif sys.platform == "linux":
        directory = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "Ultralytics"
    elif sys.platform == "win32":
        directory = Path.home() / "AppData" / "Roaming" / "Ultralytics"
    elif sys.platform == "darwin":
        directory = Path.home() / "Library" / "Application Support" / "Ultralytics"
    else:
        return None
    # Select the same directory as the settings writer; never revive a key from another location after logout.
    try:
        if not directory.is_dir():  # the writer falls back to a private temp directory when it cannot create this one
            windows = sys.platform == "win32"
            directory = Path(tempfile.gettempdir()) / ("Ultralytics" if windows else f"Ultralytics-{os.getuid()}")
            st = directory.lstat()
            if not (stat.S_ISDIR(st.st_mode) and (windows or (st.st_uid, st.st_mode & 0o777) == (os.getuid(), 0o700))):
                return None  # the writer never uses a foreign, shared or symlinked directory
        settings = json.loads((directory / "settings.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    api_key = settings.get("api_key") if isinstance(settings, dict) else None
    return api_key if isinstance(api_key, str) else None
