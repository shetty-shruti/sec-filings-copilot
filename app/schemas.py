"""Request and response models for the API."""

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)
    ticker: str | None = None
    year: int | None = None


class Citation(BaseModel):
    id: int
    ticker: str
    fiscal_year: int
    section: str
    url: str
    snippet: str


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation] = []
    confidence: str = "unknown"  # high | partial | not_found
