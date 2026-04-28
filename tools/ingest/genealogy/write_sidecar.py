#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
from typing import Any


def _iter_ndjson(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _pseudonymous_key(person_id: str, repo_salt: str) -> str:
    return hashlib.sha256(f"{repo_salt}|{person_id}".encode("utf-8")).hexdigest()


def _encode_payload(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True).encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("ascii")


def build_sidecar(rows: list[dict[str, Any]], repo_salt: str, kek_id: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in rows:
        person_id = str(row.get("person_id", ""))
        if not person_id or person_id in seen:
            continue
        seen.add(person_id)

        payload = {
            "person_id": person_id,
            "source_line": row.get("source_line"),
        }
        out.append(
            {
                "person_key": _pseudonymous_key(person_id, repo_salt),
                "kek_id": kek_id,
                "ciphertext": _encode_payload(payload),
            }
        )
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write restricted genealogy sidecar mapping rows.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repo-salt", required=True)
    parser.add_argument("--kek-id", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sidecar_rows = build_sidecar(_iter_ndjson(args.input), args.repo_salt, args.kek_id)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for row in sidecar_rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    print(f"WROTE: {len(sidecar_rows)} sidecar rows -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
