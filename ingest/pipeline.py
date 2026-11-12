"""Python ingestion path used by `make ingest` until the Kafka path exists."""


def main() -> None:
    # download -> parse -> chunk -> embed -> write to pgvector
    raise NotImplementedError("Week 1")


if __name__ == "__main__":
    main()
