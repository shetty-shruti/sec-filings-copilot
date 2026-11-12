"""Chunking strategies. Week 1 baseline is fixed-size; weeks 2 to 3 compare alternatives."""

from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    ticker: str
    fiscal_year: int
    section: str
    source_url: str


def chunk_fixed(text: str, size_tokens: int = 800, overlap_tokens: int = 100) -> list[str]:
    raise NotImplementedError("Week 1 baseline")


def chunk_section_aware(text: str) -> list[str]:
    raise NotImplementedError("Weeks 2 to 3 experiment")
