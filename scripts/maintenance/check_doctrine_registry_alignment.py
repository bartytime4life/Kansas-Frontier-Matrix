#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _doctrine_registry import parse_required_entries
from check_doctrine_artifact_provenance import parse_entries as parse_provenance_entries


def run(required_registry: Path, provenance_registry: Path) -> int:
    required = {e["filename"] for e in parse_required_entries(required_registry)}
    provenance = {e["filename"] for e in parse_provenance_entries(provenance_registry)}

    missing_in_provenance = sorted(required - provenance)
    extra_in_provenance = sorted(provenance - required)

    result = {
        "check": "doctrine_registry_alignment",
        "required_registry": str(required_registry),
        "provenance_registry": str(provenance_registry),
        "required_count": len(required),
        "provenance_count": len(provenance),
        "missing_in_provenance": missing_in_provenance,
        "extra_in_provenance": extra_in_provenance,
        "result": "pass" if not missing_in_provenance and not extra_in_provenance else "fail",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "pass" else 1


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--required-registry", type=Path, default=root / "control_plane" / "document_registry_doctrine_required.yaml")
    parser.add_argument("--provenance-registry", type=Path, default=root / "control_plane" / "doctrine_artifact_provenance_sources.yaml")
    args = parser.parse_args()
    return run(args.required_registry, args.provenance_registry)


if __name__ == "__main__":
    raise SystemExit(main())
