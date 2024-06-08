from typing import Any

from src.config import BaseConfig

settings = BaseConfig()

app_configs: dict[str, Any] = {
    "title": "Conversion App API",
}

if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
