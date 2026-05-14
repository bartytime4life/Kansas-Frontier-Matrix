#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_STATUS = {"validated", "pending", "blocked"}
REQUIRED_FIELDS = ("consumer", "owner", "status", "validated_utc", "evidence", "notes")


def parse_entries(path: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_block = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("normalized_summary_consumers:"):
            in_block = True
            continue
        if not in_block:
            continue
        if line.startswith("- consumer:"):
            if current:
                entries.append(current)
            current = {"consumer": line.split(":", 1)[1].strip()}
        elif current is not None and ":" in line:
            k, v = line.split(":", 1)
            current[k.strip()] = v.strip()
    if current:
        entries.append(current)
    if not in_block:
        raise ValueError("missing normalized_summary_consumers block")
    return entries


def run(path: Path, require_all_validated: bool = False) -> int:
    entries = parse_entries(path)
    errors: list[str] = []
    seen: set[str] = set()
    for e in entries:
        for f in REQUIRED_FIELDS:
            if not e.get(f):
                errors.append(f"missing field {f} for consumer {e.get('consumer','<unknown>')}")
        c = e.get("consumer", "")
        if c in seen:
            errors.append(f"duplicate consumer {c}")
        seen.add(c)
        if e.get("status") not in ALLOWED_STATUS:
            errors.append(f"invalid status {e.get('status')} for consumer {c}")

    if require_all_validated:
        non_validated = [e.get("consumer", "<unknown>") for e in entries if e.get("status") != "validated"]
        if non_validated:
            errors.append("non-validated consumers present: " + ",".join(sorted(non_validated)))
    payload = {
        "check": "normalized_summary_consumer_readiness",
        "registry": str(path),
        "consumer_count": len(entries),
        "result": "pass" if not errors else "fail",
        "errors": errors,
        "require_all_validated": require_all_validated,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not errors else 1


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=root / "control_plane" / "normalized_summary_consumer_readiness.yaml")
    parser.add_argument("--require-all-validated", action="store_true")
    args = parser.parse_args()
    return run(args.registry, args.require_all_validated)


if __name__ == "__main__":
    raise SystemExit(main())
