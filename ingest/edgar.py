"""SEC EDGAR client. Sends the required User-Agent and stays under 10 requests/second."""

SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"


def list_10k_filings(cik: int, years: int = 3) -> list[dict]:
    raise NotImplementedError("Week 1")


def download_filing(url: str, dest_path: str) -> None:
    """Save raw HTML under data/raw/{ticker}/{year}.html"""
    raise NotImplementedError("Week 1")
