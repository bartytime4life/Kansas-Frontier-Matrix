#!/usr/bin/env python3
"""Run ecology validator suite against a descriptor bundle JSON file."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


VALIDATORS = (
    "validate_ecology_bundle.py",
    "validate_source_descriptors.py",
    "validate_taxa.py",
    "validate_occurrences.py",
    "validate_habitat_surfaces.py",
    "validate_habitat_assignments.py",
    "validate_sensitivity.py",
    "validate_catalog_closure.py",
    "validate_release_bundle.py",
    "validate_runtime_envelope.py",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all ecology validators")
    parser.add_argument("--bundle", required=True, help="Candidate ecology bundle JSON")
    parser.add_argument("--json", action="store_true", help="Print machine-readable summary")
    args = parser.parse_args()

    base = Path(__file__).parent
    results: list[dict[str, object]] = []

    for validator in VALIDATORS:
        if validator == "validate_ecology_bundle.py":
            cmd = [sys.executable, str(base / validator), "--bundle", args.bundle, "--json"]
        else:
            cmd = [sys.executable, str(base / validator), args.bundle, "--json"]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        payload: dict[str, object]
        try:
            payload = json.loads(proc.stdout) if proc.stdout.strip() else {"decision": "fail", "errors": ["empty_output"]}
        except json.JSONDecodeError:
            payload = {"decision": "fail", "errors": ["invalid_json_output"], "stdout": proc.stdout.strip()}
        payload["validator"] = validator
        payload["exit_code"] = proc.returncode
        results.append(payload)

    failed = [r for r in results if r.get("decision") != "pass" or r.get("exit_code") != 0]
    summary = {"decision": "pass" if not failed else "fail", "bundle": args.bundle, "results": results}

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(f"decision={summary['decision']}")
        for item in results:
            print(f"{item['validator']}: {item.get('decision')} (exit={item.get('exit_code')})")

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
