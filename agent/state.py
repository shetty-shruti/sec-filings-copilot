"""LangGraph state for the research agent (week 4)."""

from typing import TypedDict


class AgentState(TypedDict, total=False):
    question: str
    sub_questions: list[str]
    tool_results: list[dict]
    draft: str
    verified: bool
    steps: int
