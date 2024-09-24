from enum import Enum
from typing import Any

from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Environment(str, Enum):
    LOCAL = "LOCAL"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self) -> bool:
        return self in (self.LOCAL, self.TESTING)

    @property
    def is_deployed(self) -> bool:
        return self == self.PRODUCTION


class Config(BaseSettings):
    DATABASE_URL: str

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENVIRONMENT: Environment = Environment.LOCAL

    CORS_ORIGINS: list[str] = ["*"]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str] = ["*"]

    class Config:
        env_file = (BASE_DIR / ".env.local", BASE_DIR / ".env")
        env_file_encoding = "utf-8"
        extra = "allow"


configs = Config()
app_configs: dict[str, Any] = {
    "title": "Agustina's App",
    "description": "My FastAPI application",
    "version": "0.1",
}

if not configs.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None
    app_configs["redoc_url"] = None
