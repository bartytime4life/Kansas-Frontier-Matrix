from __future__ import annotations

from pathlib import Path

DIRECT_MODEL_TOKENS = (
    "openai",
    "anthropic",
    "ollama",
    "localhost:11434",
    "/v1/chat",
    "/v1/responses",
)


def test_governed_api_server_has_no_direct_model_client_references() -> None:
    server_source = Path("apps/governed_api/server.py").read_text(encoding="utf-8").lower()

    assert all(token not in server_source for token in DIRECT_MODEL_TOKENS)
