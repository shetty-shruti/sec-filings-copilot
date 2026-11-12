# Ingestion service (Go)

Polls EDGAR for new 10-K filings from the configured tickers, saves them to
storage and publishes `filings.new`. The Python worker (`../ingest/worker.py`)
consumes those events and indexes the filings.

Built in weeks 5 to 6. Until then, `make ingest` runs the Python pipeline directly.

```bash
go run ./cmd/poller
```

Update the module path in `go.mod` once the GitHub repo exists.
