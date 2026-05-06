from __future__ import annotations

from pathlib import Path

FORBIDDEN_PATH_TOKENS = (
    "data/raw",
    "/raw/",
    "data/work",
    "/work/",
    "data/quarantine",
    "/quarantine/",
)


def test_governed_api_server_avoids_raw_work_quarantine_paths() -> None:
    server_source = Path("apps/governed_api/server.py").read_text(encoding="utf-8").lower()

    assert all(token not in server_source for token in FORBIDDEN_PATH_TOKENS)
