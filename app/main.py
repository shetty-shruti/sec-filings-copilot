"""FastAPI entry point. Run with: make api"""

from fastapi import FastAPI, HTTPException

from app.schemas import AskRequest, AskResponse

app = FastAPI(title="SEC Filings Research Copilot", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    # Week 1: call rag.chain.answer(); week 4: swap in agent.graph.run().
    raise HTTPException(status_code=501, detail="Not implemented yet (week 1)")
