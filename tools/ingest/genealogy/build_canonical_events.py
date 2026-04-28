#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def _stable_person_key(person_id: str, repo_salt: str) -> str:
    material = f"{repo_salt}|{person_id}".encode("utf-8")
    return hashlib.sha256(material).hexdigest()


def _iter_ndjson(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def build_rows(rows: list[dict[str, Any]], bundle_id: str, evidence_ref: str, repo_salt: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        person_id = str(row.get("person_id", "UNKNOWN"))
        pseudonymous_key = _stable_person_key(person_id, repo_salt)
        out.append(
            {
                "event_id": f"{bundle_id}:{index}",
                "bundle_id": bundle_id,
                "evidence_ref": evidence_ref,
                "person_key": pseudonymous_key,
                "event_type": row.get("event_type"),
                "event_date": row.get("event_date"),
                "place": row.get("place"),
                "source_line": row.get("source_line"),
            }
        )
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build canonical genealogy events from normalized/raw rows.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bundle-id", required=True)
    parser.add_argument("--evidence-ref", required=True)
    parser.add_argument("--repo-salt", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_rows = _iter_ndjson(args.input)
    output_rows = build_rows(input_rows, args.bundle_id, args.evidence_ref, args.repo_salt)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for row in output_rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")

    print(f"WROTE: {len(output_rows)} canonical events -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
