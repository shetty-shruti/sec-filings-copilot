-- Runs once when the Postgres container is first created.
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS filings (
    id               SERIAL PRIMARY KEY,
    ticker           TEXT NOT NULL,
    cik              INTEGER NOT NULL,
    accession_number TEXT UNIQUE NOT NULL,
    fiscal_year      INTEGER NOT NULL,
    filing_date      DATE,
    source_url       TEXT NOT NULL,
    created_at       TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS sections (
    id         SERIAL PRIMARY KEY,
    filing_id  INTEGER REFERENCES filings(id) ON DELETE CASCADE,
    section    TEXT NOT NULL,          -- e.g. 'Item 1A', 'Item 7', 'Item 8'
    text       TEXT NOT NULL
);

-- 384 dimensions matches BAAI/bge-small-en-v1.5; change if you switch models.
CREATE TABLE IF NOT EXISTS chunks (
    id          SERIAL PRIMARY KEY,
    section_id  INTEGER REFERENCES sections(id) ON DELETE CASCADE,
    ticker      TEXT NOT NULL,
    fiscal_year INTEGER NOT NULL,
    section     TEXT NOT NULL,
    source_url  TEXT NOT NULL,
    content     TEXT NOT NULL,
    embedding   vector(384),
    tsv         tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED
);
CREATE INDEX IF NOT EXISTS chunks_embedding_hnsw ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS chunks_tsv_gin ON chunks USING gin (tsv);
CREATE INDEX IF NOT EXISTS chunks_filters ON chunks (ticker, fiscal_year);

CREATE TABLE IF NOT EXISTS xbrl_cache (
    cik        INTEGER PRIMARY KEY,
    payload    JSONB NOT NULL,
    fetched_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS audit_log (
    id                  BIGSERIAL PRIMARY KEY,
    user_id             TEXT,
    question            TEXT NOT NULL,
    retrieved_chunk_ids INTEGER[],
    tool_calls          JSONB,
    answer              TEXT,
    model               TEXT,
    cost_usd            NUMERIC(10, 6),
    low_confidence      BOOLEAN DEFAULT false,
    created_at          TIMESTAMPTZ DEFAULT now()
);
