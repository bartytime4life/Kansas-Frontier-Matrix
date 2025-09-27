from __future__ import annotations
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict


class Provenance:
    """Utilities for hashing and sidecars."""

    @staticmethod
    def sha256_file(path: Path, chunk: int = 8192) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for b in iter(lambda: f.read(chunk), b""):
                h.update(b)
        return h.hexdigest()

    @staticmethod
    def write_sha256_sidecar(path: Path, digest: str) -> Path:
        side = path.with_suffix(path.suffix + ".sha256")
        side.write_text(f"{digest}  {path.name}\n", encoding="utf-8")
        return side

    @staticmethod
    def now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def basic_asset(path: Path, media_type: str) -> Dict:
        return {
            "href": str(path.as_posix()),
            "type": media_type,
            "title": path.name,
        }
