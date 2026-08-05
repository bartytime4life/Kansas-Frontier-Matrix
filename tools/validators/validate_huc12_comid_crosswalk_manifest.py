#!/usr/bin/env python3
"""Validate the bounded synthetic HUC12-COMID crosswalk manifest profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    validate_fixture_file,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hydrology/huc12_comid_crosswalk_manifest.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/domains/hydrology/huc12_comid_crosswalk_manifest"
SCOPE = "hydrology.huc12_comid_crosswalk_manifest"
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_VALIDATOR = Draft202012Validator(SCHEMA)
ZERO_HASH = "sha256:" + ("0" * 64)
FORBIDDEN_LIFECYCLE_FRAGMENTS = (
    "/raw/",
    "/work/",
    "/quarantine/",
    "data/raw/",
    "data/work/",
    "data/quarantine/",
)


def serialize_outcome(path: Path, findings: list[Finding], *, status: str | None = None) -> str:
    payload = {
        "file": str(path),
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in sorted(findings)
        ],
        "scope": SCOPE,
        "status": status or ("FAIL" if findings else "PASS"),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def canonical_spec_hash(document: dict[str, object]) -> str:
    """Hash every declared field except spec_hash using canonical JSON."""

    identity_document = {key: value for key, value in document.items() if key != "spec_hash"}
    canonical = json.dumps(
        identity_document,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _json_path(error_path: Sequence[object]) -> str:
    result = "$"
    for part in error_path:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.removesuffix("Z") + "+00:00")


def validate_document(candidate: object) -> list[Finding]:
    """Validate closed shape, deterministic identity, references, and time."""

    findings: set[Finding] = set()
    schema_errors = sorted(
        SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "HUC12_COMID_MANIFEST_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    if candidate["spec_hash"] == ZERO_HASH or candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(findings, "HUC12_COMID_MANIFEST_HASH_MISMATCH", "$.spec_hash")

    if candidate["crosswalk_digest"] == ZERO_HASH:
        add_finding(findings, "HUC12_COMID_CROSSWALK_DIGEST_PLACEHOLDER", "$.crosswalk_digest")

    expected_manifest_id = (
        "kfm://manifest/hydrology/huc12-comid/"
        f"{candidate['huc12']}/{candidate['wbd_snapshot_id']}/{candidate['valid_from'][:10]}"
    )
    if candidate["manifest_id"] != expected_manifest_id:
        add_finding(findings, "HUC12_COMID_MANIFEST_ID_MISMATCH", "$.manifest_id")

    if not candidate["crosswalk_ref"].endswith("@" + candidate["crosswalk_digest"]):
        add_finding(findings, "HUC12_COMID_CROSSWALK_REF_DIGEST_MISMATCH", "$.crosswalk_ref")

    if candidate["comid_count"] > candidate["row_count"]:
        add_finding(findings, "HUC12_COMID_COUNT_EXCEEDS_ROWS", "$.comid_count")

    try:
        valid_from = _parse_utc(candidate["valid_from"])
        valid_to = _parse_utc(candidate["valid_to"])
    except ValueError:
        add_finding(findings, "HUC12_COMID_TIME_INVALID", "$.valid_from")
    else:
        if valid_from >= valid_to:
            add_finding(findings, "HUC12_COMID_TIME_ORDER_INVALID", "$.valid_to")

    for field in ("crosswalk_ref", "run_receipt_ref", "evidence_bundle_ref"):
        value = candidate[field].lower()
        if any(fragment in value for fragment in FORBIDDEN_LIFECYCLE_FRAGMENTS):
            add_finding(findings, "HUC12_COMID_INTERNAL_LIFECYCLE_REF_DENIED", f"$.{field}")

    return sorted(findings)


def validate_manifest_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def assess_change(previous: object, candidate: object) -> tuple[str, list[Finding]]:
    """Return PASS, HOLD, or DENY for one append-only manifest transition."""

    findings: set[Finding] = set(validate_document(previous))
    findings.update(validate_document(candidate))
    if findings or not isinstance(previous, dict) or not isinstance(candidate, dict):
        return "DENY", sorted(findings)

    if previous["huc12"] != candidate["huc12"]:
        add_finding(findings, "HUC12_COMID_CHANGE_SCOPE_MISMATCH", "$.huc12")
    try:
        previous_to = _parse_utc(previous["valid_to"])
        candidate_from = _parse_utc(candidate["valid_from"])
    except ValueError:
        add_finding(findings, "HUC12_COMID_TIME_INVALID", "$.valid_from")
    else:
        if candidate_from <= previous_to:
            add_finding(findings, "HUC12_COMID_TIME_WINDOW_OVERLAP", "$.valid_from")
    if findings:
        return "DENY", sorted(findings)

    holds: set[Finding] = set()
    if previous["nhd_snapshot_id"] != candidate["nhd_snapshot_id"]:
        add_finding(holds, "HUC12_COMID_NHD_SNAPSHOT_CHANGED", "$.nhd_snapshot_id")
    if previous["crosswalk_digest"] != candidate["crosswalk_digest"]:
        add_finding(holds, "HUC12_COMID_CROSSWALK_DIGEST_CHANGED", "$.crosswalk_digest")
    return ("HOLD", sorted(holds)) if holds else ("PASS", [])


def _fixture_suite() -> int:
    ok = True
    for expected_valid, directory in (
        (True, FIXTURES_ROOT / "valid"),
        (False, FIXTURES_ROOT / "invalid"),
    ):
        files = sorted(directory.glob("*.json"))
        if not files:
            print(f"FAIL {directory}: no JSON fixtures found")
            ok = False
            continue
        for path in files:
            findings = validate_manifest_file(path)
            accepted = not findings
            if accepted == expected_valid:
                print(f"{'OK' if expected_valid else 'EXPECTED_FAIL'} {path}")
            else:
                print(serialize_outcome(path, findings))
                ok = False

    hold_root = FIXTURES_ROOT / "hold"
    previous_path = hold_root / "previous.json"
    for candidate_name, expected_code in (
        ("candidate_nhd_changed.json", "HUC12_COMID_NHD_SNAPSHOT_CHANGED"),
        ("candidate_crosswalk_changed.json", "HUC12_COMID_CROSSWALK_DIGEST_CHANGED"),
    ):
        previous = json.loads(previous_path.read_text(encoding="utf-8"))
        candidate = json.loads((hold_root / candidate_name).read_text(encoding="utf-8"))
        status, findings = assess_change(previous, candidate)
        if status == "HOLD" and expected_code in {finding.code for finding in findings}:
            print(f"EXPECTED_HOLD {hold_root / candidate_name}")
        else:
            print(serialize_outcome(hold_root / candidate_name, findings, status=status))
            ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a synthetic HUC12-COMID crosswalk manifest and optional prior slice."
    )
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))

    if args.fixtures:
        if args.candidate is not None or args.previous is not None:
            print("--fixtures cannot be combined with candidate or --previous", file=sys.stderr)
            return 2
        return _fixture_suite()
    if args.candidate is None:
        print("candidate manifest is required", file=sys.stderr)
        return 2

    candidate_findings = validate_manifest_file(args.candidate)
    if args.previous is None:
        print(serialize_outcome(args.candidate, candidate_findings))
        return 1 if candidate_findings else 0

    previous_findings = validate_manifest_file(args.previous)
    if previous_findings or candidate_findings:
        findings = sorted({*previous_findings, *candidate_findings})
        print(serialize_outcome(args.candidate, findings, status="DENY"))
        return 1

    previous = json.loads(args.previous.read_text(encoding="utf-8"))
    candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
    status, findings = assess_change(previous, candidate)
    print(serialize_outcome(args.candidate, findings, status=status))
    if status == "PASS":
        return 0
    if status == "HOLD":
        return 3
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
