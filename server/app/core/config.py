from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "URL Shortener"
    BASE_URL: str = "http://localhost:8000"
    DATABASE_URL_NEW: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
