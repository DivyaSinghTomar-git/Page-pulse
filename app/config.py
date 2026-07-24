from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Page Pulse"

    CACHE_TTL: int = 300

    REQUEST_TIMEOUT: int = 10

    MAX_CONCURRENT_REQUESTS: int = 20

    RATE_LIMIT: str = "20/minute"

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()