"""Kafka consumer for filings.new (weeks 5 to 6).

Idempotent on accession number; publishes filings.indexed, sends failures to filings.dlq.
"""


def main() -> None:
    raise NotImplementedError("Weeks 5 to 6")


if __name__ == "__main__":
    main()
