from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "URL Shortener"
    BASE_URL: str = "http://localhost:8000"
    DATABASE_URL: str = os.environ.get("DATABASE_URL_NEW") or os.environ.get(
        "DATABASE_URL", ""
    ).replace("postgres://", "postgresql://")

    class Config:
        env_file = ".env"


settings = Settings()
