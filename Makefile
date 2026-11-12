COMPOSE = docker compose -f infra/docker-compose.yml

.PHONY: up down ingest eval test lint api ui smoke

up:      ## Start Postgres + pgvector and Langfuse
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

ingest:  ## Download, parse, chunk and embed filings (Python path)
	uv run python -m ingest.pipeline

eval:    ## Run the eval set and save a run under eval/runs/
	uv run python -m eval.run_eval

test:
	uv run pytest

lint:
	uv run ruff check . && uv run ruff format --check . && uv run mypy app rag agent ingest

api:
	uv run uvicorn app.main:app --reload

ui:
	uv run streamlit run ui/streamlit_app.py

smoke:   ## Week 0: embed, store, retrieve, call the LLM, check Langfuse
	uv run python scripts/smoke_test.py
