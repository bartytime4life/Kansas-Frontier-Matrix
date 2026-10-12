#!/usr/bin/env python3
"""Build and validate deterministic fixture-only STAC/DCAT/PROV release closure."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
HASH_SRC = ROOT / "packages/hashing/src"
for path in (HERE, HASH_SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from hashing import canonicalize_json
from _synthetic_release_catalog_closure_common import (
    Finding, Result, candidate_findings, read_object,
)
from _synthetic_release_catalog_closure_projection import (
    build_projections, finish_validation,
)

FIXTURES = ROOT / "fixtures/contracts/v1/data/synthetic_release_catalog_closure_profile"
CASES = FIXTURES / "cases.json"


def validate_candidate(candidate: Mapping[str, Any]) -> Result:
    findings = candidate_findings(candidate)
    if findings:
        return Result("DENY", tuple(sorted(findings)))
    return finish_validation(candidate)


def validate_file(path: Path) -> Result:
    value, findings = read_object(path)
    if value is None:
        return Result("ERROR", findings)
    return validate_candidate(value)


def _parts(pointer: str) -> list[str]:
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = _parts(pointer)
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    if isinstance(cursor, list):
        cursor[int(parts[-1])] = replacement
    else:
        cursor[parts[-1]] = replacement


def _remove_pointer(document: dict[str, Any], pointer: str) -> None:
    parts = _parts(pointer)
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    if isinstance(cursor, list):
        del cursor[int(parts[-1])]
    else:
        cursor.pop(parts[-1], None)


def materialize_case(
    manifest: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    for mutation in case.get("mutations", []):
        if mutation.get("op", "set") == "remove":
            _remove_pointer(candidate, mutation["path"])
        else:
            _set_pointer(candidate, mutation["path"], mutation.get("value"))
    if case.get("provide_generated_projections"):
        candidate["provided_projections"] = build_projections(candidate)
        for mutation in case.get("projection_mutations", []):
            _set_pointer(
                candidate["provided_projections"],
                mutation["path"],
                mutation.get("value"),
            )
    if "expected_spec_hash_override" in case:
        candidate["expected_spec_hash"] = case["expected_spec_hash_override"]
    return candidate


def load_cases() -> dict[str, Any]:
    value, findings = read_object(CASES)
    if value is None or findings:
        raise ValueError("fixture manifest could not be loaded")
    return value


def canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return canonicalize_json(value)


def run_fixtures() -> int:
    manifest = load_cases()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_case(manifest, case))
        actual_codes = sorted({item.code for item in result.findings})
        expected_codes = sorted(case["expected_reason_codes"])
        if (
            result.outcome != case["expected_outcome"]
            or actual_codes != expected_codes
        ):
            failures.append({
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_reason_codes": expected_codes,
                "actual_reason_codes": actual_codes,
            })
        expected_hash = case.get("expected_packet_spec_hash")
        if expected_hash and (
            result.packet is None or result.packet.get("spec_hash") != expected_hash
        ):
            failures.append({
                "case_id": case["case_id"],
                "error": "EXPECTED_PACKET_SPEC_HASH_MISMATCH",
                "expected_spec_hash": expected_hash,
                "actual_spec_hash": (
                    None if result.packet is None else result.packet.get("spec_hash")
                ),
            })
        print(
            f"SYNTHETIC_RELEASE_CATALOG_CLOSURE_FIXTURE case={case['case_id']} "
            f"outcome={result.outcome} "
            f"findings={','.join(actual_codes) if actual_codes else '-'}"
        )
    if failures:
        print(json.dumps(
            {"suite_match": False, "failures": failures},
            sort_keys=True,
            separators=(",", ":"),
        ))
        return 1
    print(
        f"SYNTHETIC_RELEASE_CATALOG_CLOSURE_FIXTURES_VALID "
        f"cases={len(manifest['cases'])} no_network=true "
        "writes_lifecycle=false publishes=false"
    )
    return 0


def _serialize(result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "resolves_evidence": False,
                "decides_policy": False,
                "approves_review": False,
                "authorizes_release": False,
                "writes_lifecycle": False,
                "serves_or_publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "findings": [
                {"code": item.code, "path": item.path}
                for item in result.findings
            ],
            "outcome": result.outcome,
            "packet": result.packet,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument(
        "--write-packet",
        type=Path,
        help="write one canonical packet to an explicit temporary path",
    )
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    if args.write_packet is not None:
        if result.packet is None:
            print(_serialize(result))
            return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]
        if args.write_packet.exists() and args.write_packet.is_symlink():
            print(json.dumps({
                "outcome": "ERROR",
                "findings": [{"code": "OUTPUT_SYMLINK_DENIED", "path": "/"}],
            }))
            return 2
        args.write_packet.parent.mkdir(parents=True, exist_ok=True)
        args.write_packet.write_bytes(canonical_bytes(result.packet))
    print(_serialize(result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
