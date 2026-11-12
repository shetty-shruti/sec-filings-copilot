# SEC Filings Research Copilot

A cited Q&A copilot over US bank SEC 10-K filings. Ask a question such as
"How did JPMorgan's provision for credit losses change from FY2023 to FY2025,
and what reasons did management give?" and get the number, the change, and
links to the exact 10-K sections it came from.

> Status: scaffolding only (week 0). Modules are stubs that raise
> `NotImplementedError` until their week in the build plan.

## Why this project

A hands-on way to learn the building blocks of LLM applications end to end:
retrieval-augmented generation, evaluation, agents, tracing and production
concerns. Each concept has its own folder, and each module's docstring says
which week it gets built.

## Concept map

| Concept | Where to look |
|---|---|
| Document ingestion and parsing | `ingest/edgar.py`, `ingest/parse.py` |
| Chunking strategies | `rag/chunking.py` |
| Embeddings | `rag/embeddings.py` |
| Vector store (pgvector, HNSW) | `db/init.sql` |
| Retrieval, hybrid search, reranking | `rag/retrieval.py` |
| Prompting, grounding, structured output | `rag/prompts.py`, `rag/chain.py`, `app/schemas.py` |
| Provider abstraction and fallbacks | `rag/llm.py` |
| Evaluation (retrieval and generation metrics) | `eval/` |
| Agents, tools, self-verification | `agent/` |
| Tracing and cost tracking | Langfuse in `infra/docker-compose.yml` |
| Prompt injection and audit trail | `rag/prompts.py`, `audit_log` in `db/init.sql` |
| Event-driven ingestion | `ingestion-service/` (Go), `ingest/worker.py` |
| Deployment and CI quality gate | `docker/`, `infra/`, `.github/workflows/` |

Notes on what you learn along the way go in [docs/learning-notes.md](docs/learning-notes.md).

## Architecture

Two paths share one Postgres database:

- **Ingestion path:** a Go service (`ingestion-service/`) polls EDGAR and
  publishes `filings.new` to Kafka. A Python worker (`ingest/`) parses,
  chunks, embeds, writes to pgvector and publishes `filings.indexed`.
  Until weeks 5 to 6, `make ingest` runs the Python pipeline directly.
- **Query path:** FastAPI (`app/`) receives `POST /ask`. Weeks 1 to 3 use a
  plain retrieve-then-answer chain (`rag/`); from week 4 a LangGraph agent
  (`agent/`) plans, calls tools, writes and verifies the cited answer.

See [docs/architecture.md](docs/architecture.md).

## Layout

| Path | What lives there |
|---|---|
| `app/` | FastAPI service, settings, request and response schemas |
| `rag/` | Chunking, embeddings, retrieval, prompts, LLM client |
| `agent/` | LangGraph state, tools and graph (week 4) |
| `ingest/` | Python EDGAR download, parsing and indexing worker |
| `ingestion-service/` | Go EDGAR poller that publishes to Kafka (weeks 5 to 6) |
| `eval/` | Eval dataset, harness, run outputs and `RESULTS.md` |
| `ui/` | Streamlit front end |
| `db/` | Database schema (pgvector, filings, chunks, audit log) |
| `infra/` | Docker Compose stack and IaC (Terraform or Bicep) |
| `docker/` | Dockerfiles for the API and worker |
| `scripts/` | One-off scripts such as the week 0 smoke test |
| `tests/` | Unit tests |
| `data/raw/` | Downloaded filings (git-ignored) |

## Quick start

```bash
cp .env.example .env        # fill in your LLM key and EDGAR User-Agent
uv sync                     # install Python deps (Python 3.12)
make up                     # Postgres + pgvector, Langfuse
make smoke                  # embed, store, retrieve, call the LLM
make api                    # http://localhost:8000/docs
```

On Windows, run the `make` targets from Git Bash or WSL, or run the commands
inside the `Makefile` directly.

## Results

Filled in during weeks 2 to 3. See [eval/RESULTS.md](eval/RESULTS.md).

## Built with

Python, FastAPI, LangGraph, Postgres with pgvector, Langfuse, RAGAS or
DeepEval, Streamlit, Kafka, Go, Docker, GitHub Actions. Developed with an AI
coding assistant (Claude Code).
