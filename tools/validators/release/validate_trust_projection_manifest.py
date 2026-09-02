#!/usr/bin/env python3
"""Validate fixture-first release trust projection manifests."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/contracts/v1/release/trust_projection_manifest.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/release/trust_projection_manifest"
MAX_BYTES = 2 * 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _pointer(parts: Iterable[object]) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("spec_hash", None)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00").astimezone(timezone.utc)
    except ValueError:
        return None


def schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if value.get("spec_hash") != canonical_hash(value):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    kind = value.get("object_type")

    if kind == "AssetIntegrityResult":
        expected = value.get("expected_sha256")
        observed = value.get("observed_sha256")
        outcome = value.get("outcome")
        derived = "MISSING_DECLARATION" if expected is None else "INTERRUPTED" if observed is None else "VERIFIED" if expected == observed else "MISMATCH"
        if outcome in {"VERIFIED", "MISMATCH", "MISSING_DECLARATION", "INTERRUPTED"} and outcome != derived:
            findings.append(Finding("ASSET_INTEGRITY_OUTCOME_MISMATCH", "/outcome"))
        if outcome == "VERIFIED" and value.get("byte_length") is None:
            findings.append(Finding("ASSET_VERIFIED_LENGTH_MISSING", "/byte_length"))

    elif kind == "TimeSliceManifest":
        interval = value.get("valid_time", {})
        start = _time(interval.get("start") if isinstance(interval, dict) else None)
        end = _time(interval.get("end") if isinstance(interval, dict) else None)
        if start is None or end is None or start > end:
            findings.append(Finding("TIME_SLICE_INTERVAL_INVALID", "/valid_time"))
        assets = value.get("assets")
        if isinstance(assets, list):
            refs = [item.get("asset_ref") for item in assets if isinstance(item, dict)]
            if len(refs) != len(set(refs)):
                findings.append(Finding("TIME_SLICE_ASSET_DUPLICATE", "/assets"))
        if value.get("status") in {"CORRECTED", "WITHDRAWN"} and value.get("correction_ref") is None:
            findings.append(Finding("TIME_SLICE_CORRECTION_REQUIRED", "/correction_ref"))
        if not value.get("rollback_ref"):
            findings.append(Finding("TIME_SLICE_ROLLBACK_REQUIRED", "/rollback_ref"))

    elif kind == "ReviewPacketReference":
        issued = _time(value.get("issued_at"))
        expires = _time(value.get("expires_at"))
        evaluated = _time(value.get("evaluated_at"))
        revoked = _time(value.get("revoked_at")) if value.get("revoked_at") is not None else None
        if None in {issued, expires, evaluated} or issued >= expires:
            findings.append(Finding("REVIEW_PACKET_TIME_INVALID", "/"))
        else:
            assert issued and expires and evaluated
            expected = "REVOKED" if revoked is not None and revoked <= evaluated else "EXPIRED" if evaluated >= expires else "ACTIVE"
            if value.get("status") != expected:
                findings.append(Finding("REVIEW_PACKET_STATUS_MISMATCH", "/status"))
            if evaluated < issued:
                findings.append(Finding("REVIEW_PACKET_NOT_YET_ISSUED", "/evaluated_at"))
        if value.get("approval_authority") is not False or value.get("access_mode") != "READ_ONLY":
            findings.append(Finding("REVIEW_PACKET_AUTHORITY_DENIED", "/approval_authority"))

    elif kind == "GovernanceChangeRecord":
        event = value.get("event_type")
        decision_refs = value.get("decision_refs")
        if event in {"POLICY_UPDATED", "VOCABULARY_UPDATED", "WAIVER_ISSUED", "WAIVER_REVOKED"} and (not isinstance(decision_refs, list) or not decision_refs):
            findings.append(Finding("GOVERNANCE_DECISION_REF_REQUIRED", "/decision_refs"))
        if value.get("append_only") is not True:
            findings.append(Finding("GOVERNANCE_APPEND_ONLY_REQUIRED", "/append_only"))
        if not value.get("rollback_refs"):
            findings.append(Finding("GOVERNANCE_ROLLBACK_REQUIRED", "/rollback_refs"))

    return findings


def validate(path: Path) -> Result:
    value, findings = read(path)
    if value is None:
        return Result(tuple(sorted(set(findings))))
    findings.extend(schema_findings(value))
    if not findings:
        findings.extend(semantic_findings(value))
    return Result(tuple(sorted(set(findings))))


def serialize(path: Path, result: Result) -> str:
    try:
        display = path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        display = path.name
    return json.dumps({"file": display, "findings": [{"code": item.code, "path": item.path} for item in result.findings], "outcome": "PASS" if result.ok else "FAIL", "scope": "release-trust-projection-fixture-only"}, sort_keys=True, separators=(",", ":"))


def fixture_profile() -> int:
    valid = sorted((FIXTURES / "valid").glob("*.json"))
    invalid = sorted((FIXTURES / "invalid").glob("*.json"))
    if not valid or not invalid:
        return 1
    ok = True
    for path in valid:
        result = validate(path)
        print(serialize(path, result))
        ok = result.ok and ok
    for path in invalid:
        result = validate(path)
        print(serialize(path, result))
        ok = (not result.ok) and ok
    return 0 if ok else 1


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate(path)
        print(serialize(path, result))
        rc = max(rc, 0 if result.ok else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
