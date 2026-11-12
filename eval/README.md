# Eval

`dataset.jsonl` holds one question per line:

```json
{"id": "q001", "type": "single_fact", "question": "What was BAC's CET1 ratio in FY2024?", "expected_answer": "...", "ticker": "BAC", "fiscal_year": 2024, "section": "Item 7"}
```

Types: `single_fact`, `cross_year`, `cross_bank`, `unanswerable`, `multi_step`.
