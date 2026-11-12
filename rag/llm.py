"""One small interface over the LLM provider, so switching provider is a one-file change."""

from typing import Protocol


class LLMClient(Protocol):
    def complete(self, system: str, user: str, *, model: str | None = None) -> str: ...


def get_llm_client() -> LLMClient:
    """Return a client for settings.llm_provider (Azure OpenAI, Bedrock, OpenAI or Anthropic)."""
    raise NotImplementedError("Week 0: implement for your chosen provider")
