from __future__ import annotations

import threading
import time
from pathlib import Path

from .utils import atomic_write_json, read_json


class TokenBucketStore:
    def __init__(self, state_path: str | Path):
        self.state_path = Path(state_path)
        self._lock = threading.Lock()

    def try_consume(self, source_id: str, rate_per_minute: float, burst: int, cost: float = 1.0) -> bool:
        if burst <= 0:
            return False
        if rate_per_minute < 0:
            rate_per_minute = 0
        with self._lock:
            state = read_json(self.state_path, default={}) or {}
            now = time.time()
            entry = state.get(source_id) or {"tokens": float(burst), "updated_at": now}
            tokens = float(entry.get("tokens", burst))
            updated_at = float(entry.get("updated_at", now))
            elapsed = max(0.0, now - updated_at)
            tokens = min(float(burst), tokens + elapsed * (rate_per_minute / 60.0))
            allowed = tokens >= cost
            if allowed:
                tokens -= cost
            state[source_id] = {"tokens": tokens, "updated_at": now}
            atomic_write_json(self.state_path, state)
            return allowed
