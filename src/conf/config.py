from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:022709@localhost:5432/book_app"

    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )


settings = Settings()
