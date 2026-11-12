# Architecture

```
            ingestion path (weeks 5 to 6)
 EDGAR ──> Go poller ──> Kafka: filings.new ──> Python worker ──> Postgres + pgvector
                                                    │                     ▲
                                                    └─> filings.indexed   │
                                                                          │
            query path                                                    │
 Streamlit ──> FastAPI /ask ──> RAG chain (weeks 1 to 3) ─────────────────┤
                            └─> LangGraph agent (week 4) ──> tools ───────┘
                                   planner → tool loop → writer → verifier
                                                    │
                                                    └─> Langfuse traces, audit_log
```

Until the Kafka path exists, `make ingest` runs `ingest/pipeline.py` and writes to pgvector directly.
