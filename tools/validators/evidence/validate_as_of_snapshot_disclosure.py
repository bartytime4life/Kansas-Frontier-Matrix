"""Validate inactive AsOfSnapshotDisclosureCandidate fixtures without a network."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONTRACT = REPO_ROOT / "contracts/evidence/as_of_snapshot_disclosure.md"
DEFAULT_SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/as_of_snapshot_disclosure.schema.json"
DEFAULT_FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/as_of_snapshot_disclosure/cases.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
OUTCOME_RANK = {"PASS": 0, "ABSTAIN": 1, "DENY": 2, "ERROR": 3}


class DuplicateKeyError(ValueError):
    pass


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError("non-finite JSON number")
    return parsed


def load_json(path: Path) -> Any:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"unsafe JSON input: {path}")
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError(f"JSON input exceeds {MAX_JSON_BYTES} bytes: {path}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)), parse_float=_finite)


def _pointer(path: object) -> str:
    parts = [str(item).replace("~", "~0").replace("/", "~1") for item in path]
    return "/" + "/".join(parts) if parts else "/"


def _parse_utc(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if value.endswith("Z") and parsed.utcoffset().total_seconds() == 0 else None
    except (AttributeError, TypeError, ValueError):
        return None


def _finding(code: str, outcome: str, path: str) -> dict[str, str]:
    return {"code": code, "outcome": outcome, "path": path}


def validate_candidate(candidate: Mapping[str, Any], schema: Mapping[str, Any], contract_bytes: bytes) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(candidate), key=lambda item: (_pointer(item.absolute_path), str(item.validator))):
        findings.append(_finding("SCHEMA_INVALID", "ERROR", _pointer(error.absolute_path)))
    if findings:
        return {"outcome": "ERROR", "findings": findings}

    if candidate["profile_spec_hash"] != hashlib.sha256(contract_bytes).hexdigest():
        findings.append(_finding("PROFILE_SPEC_HASH_MISMATCH", "ERROR", "/profile_spec_hash"))

    timestamp_paths = {
        "/observed_at": candidate["observed_at"],
        "/claim_valid_time/start": candidate["claim_valid_time"]["start"],
        "/claim_valid_time/end": candidate["claim_valid_time"]["end"],
        "/snapshot/as_of": candidate["snapshot"]["as_of"],
        "/corrections/included_through": candidate["corrections"]["included_through"],
    }
    parsed: dict[str, datetime] = {}
    for path, value in timestamp_paths.items():
        item = _parse_utc(value)
        if item is None:
            findings.append(_finding("TIMESTAMP_NOT_UTC", "ERROR", path))
        else:
            parsed[path] = item
    for index, source in enumerate(candidate["source_snapshots"]):
        item = _parse_utc(source["source_as_of"])
        path = f"/source_snapshots/{index}/source_as_of"
        if item is None:
            findings.append(_finding("TIMESTAMP_NOT_UTC", "ERROR", path))
        else:
            parsed[path] = item
    if any(item["outcome"] == "ERROR" for item in findings):
        return {"outcome": "ERROR", "findings": sorted(findings, key=lambda item: (item["path"], item["code"]))}

    if parsed["/claim_valid_time/start"] >= parsed["/claim_valid_time/end"]:
        findings.append(_finding("VALID_TIME_ORDER_INVALID", "DENY", "/claim_valid_time"))

    snapshot = candidate["snapshot"]
    mode = snapshot["mode"]
    release_ref = snapshot["release_manifest_ref"]
    transaction_ref = snapshot["transaction_snapshot_ref"]
    mode_ok = (
        (mode == "RELEASE_SNAPSHOT" and release_ref is not None and transaction_ref is None)
        or (mode == "TRANSACTION_SNAPSHOT" and release_ref is None and transaction_ref is not None)
        or (mode == "BITEMPORAL_SNAPSHOT" and release_ref is not None and transaction_ref is not None)
    )
    if not mode_ok:
        findings.append(_finding("SNAPSHOT_MODE_REFERENCE_CONFLICT", "DENY", "/snapshot"))

    if candidate["claim_scope"]["resolution"] == "UNRESOLVED" or snapshot["resolution"] == "UNRESOLVED":
        findings.append(_finding("SNAPSHOT_PREREQUISITE_UNRESOLVED", "ABSTAIN", "/snapshot"))

    sources = candidate["source_snapshots"]
    source_ids = [source["source_id"] for source in sources]
    if source_ids != sorted(source_ids) or len(source_ids) != len(set(source_ids)):
        findings.append(_finding("SOURCE_SNAPSHOT_ORDER_NONCANONICAL", "DENY", "/source_snapshots"))
    for index, source in enumerate(sources):
        if source["resolution"] == "UNRESOLVED":
            findings.append(_finding("SOURCE_SNAPSHOT_UNRESOLVED", "ABSTAIN", f"/source_snapshots/{index}"))
        if parsed[f"/source_snapshots/{index}/source_as_of"] > parsed["/snapshot/as_of"]:
            findings.append(_finding("SOURCE_SNAPSHOT_AFTER_AS_OF", "DENY", f"/source_snapshots/{index}/source_as_of"))

    corrections = candidate["corrections"]
    if parsed["/corrections/included_through"] > parsed["/snapshot/as_of"]:
        findings.append(_finding("CORRECTION_CUTOFF_AFTER_AS_OF", "DENY", "/corrections/included_through"))
    if corrections["later_corrections_behavior"] == "UNKNOWN":
        findings.append(_finding("LATER_CORRECTION_POSTURE_UNKNOWN", "ABSTAIN", "/corrections/later_corrections_behavior"))

    disclosure = candidate["disclosure"]
    if disclosure["valid_time_label"].strip().casefold() == disclosure["as_of_label"].strip().casefold():
        findings.append(_finding("TIME_AXIS_LABELS_COLLAPSED", "DENY", "/disclosure"))
    for path, values in (
        ("/corrections/correction_refs", corrections["correction_refs"]),
        ("/disclosure/review_record_refs", disclosure["review_record_refs"]),
        ("/evidence_refs", candidate["evidence_refs"]),
    ):
        if values != sorted(values):
            findings.append(_finding("REFERENCE_ORDER_NONCANONICAL", "DENY", path))
    if disclosure["intended_use"] == "PUBLIC_CANDIDATE":
        if not disclosure["review_record_refs"]:
            findings.append(_finding("PUBLIC_REVIEW_REF_MISSING", "DENY", "/disclosure/review_record_refs"))
        if disclosure["release_manifest_ref"] is None:
            findings.append(_finding("PUBLIC_RELEASE_REF_MISSING", "DENY", "/disclosure/release_manifest_ref"))
    if release_ref is not None and disclosure["release_manifest_ref"] != release_ref:
        findings.append(_finding("RELEASE_REFERENCE_MISMATCH", "DENY", "/disclosure/release_manifest_ref"))

    conclusion = candidate["conclusion"]
    if conclusion["completeness"] != "COMPLETE":
        findings.append(_finding("DISCLOSURE_INCOMPLETE", "ABSTAIN", "/conclusion"))

    preliminary = max((item["outcome"] for item in findings), key=lambda value: OUTCOME_RANK[value], default="PASS")
    expected = "DENY" if preliminary == "DENY" else "HOLD" if preliminary == "ABSTAIN" else "READY_FOR_REVIEW"
    if conclusion["declared_outcome"] != expected:
        findings.append(_finding("DECLARED_OUTCOME_INCOHERENT", "DENY", "/conclusion/declared_outcome"))
    outcome = max((item["outcome"] for item in findings), key=lambda value: OUTCOME_RANK[value], default="PASS")
    return {"outcome": outcome, "findings": sorted(findings, key=lambda item: (item["path"], item["code"]))}


def _set_pointer(document: Any, pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.strip("/").split("/") if part]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    if isinstance(target, list):
        target[int(parts[-1])] = value
    else:
        target[parts[-1]] = value


def _delete_pointer(document: Any, pointer: str) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.strip("/").split("/") if part]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    if isinstance(target, list):
        del target[int(parts[-1])]
    else:
        del target[parts[-1]]


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    for pointer, value in case.get("set", {}).items():
        _set_pointer(candidate, pointer, value)
    for pointer in case.get("delete", []):
        _delete_pointer(candidate, pointer)
    return candidate


def validate_fixture_manifest(manifest: Mapping[str, Any], schema: Mapping[str, Any], contract_bytes: bytes) -> list[dict[str, Any]]:
    results = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_case(manifest, case), schema, contract_bytes)
        result.update({"case_id": case["case_id"], "expected_outcome": case["expected_outcome"]})
        results.append(result)
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--fixtures", nargs="?", const=DEFAULT_FIXTURES, type=Path)
    parser.add_argument("--candidate", type=Path)
    args = parser.parse_args(argv)
    if bool(args.fixtures) == bool(args.candidate):
        parser.error("select exactly one of --fixtures or --candidate")
    schema = load_json(args.schema)
    contract_bytes = args.contract.read_bytes()
    if args.fixtures:
        manifest = load_json(args.fixtures)
        results = validate_fixture_manifest(manifest, schema, contract_bytes)
        mismatches = [item for item in results if item["outcome"] != item["expected_outcome"]]
        print(json.dumps({"profile": manifest["profile"], "case_count": len(results), "mismatch_count": len(mismatches), "results": results}, sort_keys=True))
        return 1 if mismatches else 0
    result = validate_candidate(load_json(args.candidate), schema, contract_bytes)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
