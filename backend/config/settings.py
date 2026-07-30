from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Ticket Platform API"
    database_url: str = "postgresql://postgres:postgres@postgres:5432/tickets"
    redis_url: str = "redis://redis:6379/0"
    jwt_secret: str = "change-me"
    cors_origins: str = "*"

    class Config:
        env_file = ".env"


settings = Settings()
