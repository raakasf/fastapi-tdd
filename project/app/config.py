import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")
class Settings(BaseSettings):
    environment: str = os.getenv("Environment", "dev")
    testing: bool = os.getenv("Testing", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
