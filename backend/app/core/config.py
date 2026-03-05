from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    project_name: str = "AI Trading OS"
    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/ai_trading_os"
    redis_url: str = "redis://redis:6379/0"
    openai_api_key: str = "change-me"


settings = Settings()
