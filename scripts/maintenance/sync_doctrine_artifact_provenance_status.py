#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from check_doctrine_artifact_provenance import parse_entries


def _render(entries: list[dict[str, str]]) -> str:
    lines = ["required_doctrine_artifact_provenance:"]
    for e in entries:
        lines.append(f"  - filename: {e['filename']}")
        lines.append(f"    doc_id: {e['doc_id']}")
        lines.append(f"    source_url: {e['source_url']}")
        lines.append(f"    status: {e['status']}")
        if e.get("verified_at"):
            lines.append(f"    verified_at: {e['verified_at']}")
    return "\n".join(lines) + "\n"


def run(registry_path: Path, artifacts_dir: Path, write: bool = False) -> int:
    entries = parse_entries(registry_path)
    changed = []
    for e in entries:
        artifact = artifacts_dir / e["filename"]
        if artifact.exists() and e.get("status") != "verified":
            e["status"] = "verified"
            e["verified_at"] = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
            changed.append(e["filename"])

    payload = {
        "check": "sync_doctrine_artifact_provenance_status",
        "registry": str(registry_path),
        "artifacts_dir": str(artifacts_dir),
        "changed": changed,
        "changed_count": len(changed),
        "result": "changed" if changed else "no_change",
        "write": write,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))

    if write and changed:
        registry_path.write_text(_render(entries), encoding="utf-8")

    return 0


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=root / "control_plane" / "doctrine_artifact_provenance_sources.yaml")
    parser.add_argument("--artifacts-dir", type=Path, default=root / "docs" / "doctrine" / "artifacts")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    return run(args.registry, args.artifacts_dir, args.write)


if __name__ == "__main__":
    raise SystemExit(main())
