"""Agent tools (week 4)."""


def search_filings(
    query: str, ticker: str | None = None, year: int | None = None, section: str | None = None
) -> list[dict]:
    """Wraps the best retriever from weeks 2 to 3."""
    raise NotImplementedError("Week 4")


def get_financial_fact(ticker: str, concept: str, year: int) -> float | None:
    """Exact numbers from data.sec.gov/api/xbrl/companyfacts, cached in Postgres."""
    raise NotImplementedError("Week 4")


def calculate(expression: str) -> float:
    """Safe arithmetic for YoY change and ratios (no eval())."""
    raise NotImplementedError("Week 4")
