"""Application settings, loaded from environment variables and .env."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: str = "azure_openai"
    llm_model_large: str = ""
    llm_model_small: str = ""

    embedding_model: str = "BAAI/bge-small-en-v1.5"
    embedding_dim: int = 384

    database_url: str = "postgresql+psycopg://copilot:copilot@localhost:5432/copilot"

    langfuse_host: str = "http://localhost:3000"
    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""

    sec_user_agent: str = ""
    tickers: str = "JPM,BAC,C,WFC,GS,MS,USB,PNC,TFC,COF"
    filing_years: int = 3

    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic_new: str = "filings.new"
    kafka_topic_indexed: str = "filings.indexed"
    kafka_topic_dlq: str = "filings.dlq"

    agent_max_steps: int = 8
    agent_token_budget: int = 20000

    @property
    def ticker_list(self) -> list[str]:
        return [t.strip() for t in self.tickers.split(",") if t.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
