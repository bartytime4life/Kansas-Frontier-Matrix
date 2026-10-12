#!/usr/bin/env python3
"""Run the bounded connector output-path scan; source admission stays held."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.connector_gate.output_paths import (  # noqa: E402
    iter_connector_source_files,
    legacy_publish_target_violations,
    scan_connector_file,
)


def scan_repository() -> dict[str, object]:
    try:
        sources = iter_connector_source_files(ROOT)
        findings = sum(len(scan_connector_file(path, ROOT)) for path in sources)
        findings += len(legacy_publish_target_violations(ROOT))
    except (OSError, UnicodeError):
        return {
            "authority": "NONE",
            "finding_count": 0,
            "outcome": "ERROR",
            "reason": "CONNECTOR_SOURCE_SCAN_UNAVAILABLE",
            "scope": "static_connector_output_paths_only",
            "source_count": 0,
        }
    if not sources:
        return {
            "authority": "NONE",
            "finding_count": 0,
            "outcome": "ERROR",
            "reason": "CONNECTOR_SOURCE_INVENTORY_EMPTY",
            "scope": "static_connector_output_paths_only",
            "source_count": 0,
        }
    return {
        "authority": "NONE",
        "finding_count": findings,
        "outcome": "DENY" if findings else "PASS",
        "scope": "static_connector_output_paths_only",
        "source_count": len(sources),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan-repository", action="store_true", required=True)
    parser.parse_args(argv)
    result = scan_repository()
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
