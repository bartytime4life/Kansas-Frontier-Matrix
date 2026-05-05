from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .utils import atomic_write_text, parse_utc, utc_now


class JsonlQueue:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def append(self, item: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n")

    def append_many(self, items: list[dict[str, Any]]) -> None:
        if not items:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            for item in items:
                fh.write(json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n")

    def read_all(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        items: list[dict[str, Any]] = []
        with self.path.open("r", encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    items.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(f"invalid JSONL at {self.path}:{line_no}: {exc}") from exc
        return items

    def replace_all(self, items: list[dict[str, Any]]) -> None:
        text = "".join(json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n" for item in items)
        atomic_write_text(self.path, text)

    def drain_ready(self, max_items: int) -> list[dict[str, Any]]:
        now = datetime.now(timezone.utc)
        ready: list[dict[str, Any]] = []
        deferred: list[dict[str, Any]] = []
        for item in self.read_all():
            available_at = parse_utc(item.get("available_at"))
            is_ready = available_at is None or available_at <= now
            if is_ready and len(ready) < max_items:
                ready.append(item)
            else:
                deferred.append(item)
        self.replace_all(deferred)
        return ready
