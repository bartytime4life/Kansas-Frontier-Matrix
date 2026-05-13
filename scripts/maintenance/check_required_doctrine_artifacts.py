#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _cli_errors import emit_structured_error
from _doctrine_registry import parse_required_entries

def run(registry_path: Path, artifacts_dir: Path, output_path: Path | None = None) -> int:
    entries = parse_required_entries(registry_path)
    required = [entry["filename"] for entry in entries]
    expected_status = {entry["filename"]: entry.get("status", "unknown") for entry in entries}
    present = {f: (artifacts_dir / f).exists() for f in required}
    missing = [f for f, ok in present.items() if not ok]
    status_mismatches = [
        f
        for f in required
        if (expected_status[f] == "missing" and present[f]) or (expected_status[f] == "present" and not present[f])
    ]

    result = {
        "check": "required_doctrine_artifacts",
        "registry": str(registry_path),
        "artifacts_dir": str(artifacts_dir),
        "required_count": len(required),
        "missing_count": len(missing),
        "missing": missing,
        "present": present,
        "status_mismatches": status_mismatches,
        "result": "pass" if not missing and not status_mismatches else "fail",
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")

    return 0 if not missing and not status_mismatches else 1


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        type=Path,
        default=root / "control_plane" / "document_registry_doctrine_required.yaml",
        help="Path to doctrine-required registry yaml",
    )
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=root / "docs" / "doctrine" / "artifacts",
        help="Directory containing doctrine artifact files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional JSON receipt output path",
    )
    args = parser.parse_args()

    try:
        return run(args.registry, args.artifacts_dir, args.output)
    except (ValueError, OSError) as exc:
        return emit_structured_error("required_doctrine_artifacts", exc)


if __name__ == "__main__":
    raise SystemExit(main())
