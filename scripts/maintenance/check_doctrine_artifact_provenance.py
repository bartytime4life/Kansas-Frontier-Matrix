#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _cli_errors import emit_structured_error

ALLOWED_STATUS = {"pending", "verified"}


def parse_entries(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_block = False
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("required_doctrine_artifact_provenance:"):
            in_block = True
            continue
        if not in_block:
            continue
        if line.startswith("- filename:"):
            if current:
                entries.append(current)
            current = {"filename": line.split(":", 1)[1].strip()}
        elif current is not None and ":" in line:
            k, v = line.split(":", 1)
            current[k.strip()] = v.strip()

    if current:
        entries.append(current)
    if not in_block:
        raise ValueError("missing required_doctrine_artifact_provenance block")
    if not entries:
        raise ValueError("required_doctrine_artifact_provenance block has no entries")
    return entries


def run(path: Path, output: Path | None) -> int:
    entries = parse_entries(path)
    invalid_urls = []
    invalid_status = []
    missing_fields = []
    for e in entries:
        for f in ("filename", "doc_id", "source_url", "status"):
            if not e.get(f):
                missing_fields.append({"filename": e.get("filename", "<unknown>"), "field": f})
        if e.get("source_url", "").startswith(("http://", "https://")) is False:
            invalid_urls.append(e.get("filename", "<unknown>"))
        if e.get("status") not in ALLOWED_STATUS:
            invalid_status.append({"filename": e.get("filename", "<unknown>"), "status": e.get("status")})

    result = {
        "check": "required_doctrine_artifact_provenance",
        "registry": str(path),
        "entry_count": len(entries),
        "invalid_urls": invalid_urls,
        "invalid_status": invalid_status,
        "missing_fields": missing_fields,
        "result": "pass" if not invalid_urls and not invalid_status and not missing_fields else "fail",
    }
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload + "\n", encoding="utf-8")
    return 0 if result["result"] == "pass" else 1


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=root / "control_plane" / "doctrine_artifact_provenance_sources.yaml")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    try:
        return run(args.registry, args.output)
    except (OSError, ValueError) as exc:
        return emit_structured_error("required_doctrine_artifact_provenance", exc)


if __name__ == "__main__":
    raise SystemExit(main())
