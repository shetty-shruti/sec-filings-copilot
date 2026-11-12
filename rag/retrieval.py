"""Retrieval: vector search (week 1), then hybrid + rerank experiments (weeks 2 to 3)."""

from rag.chunking import Chunk


def vector_search(
    query: str, k: int = 5, ticker: str | None = None, year: int | None = None
) -> list[Chunk]:
    raise NotImplementedError("Week 1")


def hybrid_search(
    query: str, k: int = 5, ticker: str | None = None, year: int | None = None
) -> list[Chunk]:
    """Postgres full-text + vector, merged with reciprocal rank fusion."""
    raise NotImplementedError("Weeks 2 to 3")


def rerank(query: str, chunks: list[Chunk], top_n: int = 5) -> list[Chunk]:
    """Cross-encoder rerank, e.g. BAAI/bge-reranker-base."""
    raise NotImplementedError("Weeks 2 to 3")
