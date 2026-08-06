#!/usr/bin/env python3
"""Validate fixture-only SourceIngestionPlanCandidate records."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_ingestion_plan.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_ingestion_plan"
MAX_FILE_BYTES = 1_048_576
SCOPE = "source.ingestion_plan"
SECRET_RE = re.compile(r"(?i)(password|passwd|secret|api[_-]?key|access[_-]?token|authorization|bearer)")
EMAIL_RE = re.compile(r"(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}")
INTERNAL_PATH_MARKERS = ("data/raw/", "data/work/", "data/quarantine/", "/data/raw/", "/data/work/", "/data/quarantine/")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def _canonical_hash(candidate: Mapping[str, Any]) -> str:
    identity = json.loads(json.dumps(candidate))
    identity.pop("plan_id", None)
    determinism = identity.get("determinism")
    if isinstance(determinism, dict):
        determinism.pop("spec_hash", None)
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _scan(value: Any) -> list[Finding]:
    findings: set[Finding] = set()
    pending: list[tuple[Any, str]] = [(value, "/")]
    while pending:
        current, path = pending.pop()
        if isinstance(current, dict):
            for key, item in current.items():
                child = f"{path.rstrip('/')}/{key}"
                if SECRET_RE.search(key):
                    findings.add(Finding("SECRET_FIELD_DENIED", child))
                pending.append((item, child))
        elif isinstance(current, list):
            for index, item in enumerate(current):
                pending.append((item, f"{path.rstrip('/')}/{index}"))
        elif isinstance(current, str):
            if SECRET_RE.search(current) or EMAIL_RE.search(current):
                findings.add(Finding("SECRET_OR_PII_VALUE_DENIED", path))
            if any(marker in current.lower() for marker in INTERNAL_PATH_MARKERS):
                findings.add(Finding("INTERNAL_LIFECYCLE_REFERENCE_DENIED", path))
    return sorted(findings)


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema)
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in validator.iter_errors(candidate)]


def _sorted_unique_strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set(_scan(candidate))
    source = candidate["source"]
    selection = candidate["selection"]
    determinism = candidate["determinism"]
    lane = candidate["lane"]
    governance = candidate["governance"]

    expected_hash = _canonical_hash(candidate)
    if determinism["spec_hash"] != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/determinism/spec_hash"))
    expected_id = f"kfm://candidate/source-ingestion/{source['source_id']}/{expected_hash.split(':', 1)[1]}"
    if candidate["plan_id"] != expected_id:
        findings.add(Finding("PLAN_ID_MISMATCH", "/plan_id"))

    if not _sorted_unique_strings(selection["reason_codes"]):
        findings.add(Finding("REASON_CODES_NOT_CANONICAL", "/selection/reason_codes"))
    if not _sorted_unique_strings(determinism["partition_keys"]):
        findings.add(Finding("PARTITION_KEYS_NOT_CANONICAL", "/determinism/partition_keys"))
    if selection["mode"] != lane["kind"]:
        findings.add(Finding("MODE_LANE_MISMATCH", "/selection/mode"))

    expected_mode = {
        "REMOTE_HTTP": "HTTP_CONDITIONAL",
        "CONTROLLED_TRANSACTIONAL_DATABASE": "EVENT_CDC",
        "BULK_CORPUS": "SCHEDULED_ETL",
    }[source["control_class"]]
    if selection["mode"] != expected_mode:
        findings.add(Finding("MODE_SOURCE_CONTROL_MISMATCH", "/source/control_class"))

    if lane["kind"] == "HTTP_CONDITIONAL":
        validators = lane["validators"]
        if not validators["etag"] and not validators["last_modified"]:
            findings.add(Finding("HTTP_VALIDATOR_REQUIRED", "/lane/validators"))
        if selection["latency_target"] == "NEAR_REAL_TIME":
            findings.add(Finding("HTTP_LATENCY_OVERCLAIM", "/selection/latency_target"))
    elif lane["kind"] == "EVENT_CDC":
        if lane["offset_store"] != "DURABLE":
            findings.add(Finding("CDC_DURABLE_OFFSET_REQUIRED", "/lane/offset_store"))
        if lane["schema_compatibility"] == "NONE":
            findings.add(Finding("CDC_SCHEMA_COMPATIBILITY_REQUIRED", "/lane/schema_compatibility"))
        if lane["replay_drill_required"] is not True:
            findings.add(Finding("CDC_REPLAY_DRILL_REQUIRED", "/lane/replay_drill_required"))
        if lane["exactly_once_claimed"] is not False:
            findings.add(Finding("CDC_EXACTLY_ONCE_OVERCLAIM", "/lane/exactly_once_claimed"))
        if selection["full_refresh_allowed"] is not False:
            findings.add(Finding("CDC_FULL_REFRESH_MISMATCH", "/selection/full_refresh_allowed"))
    elif lane["kind"] == "SCHEDULED_ETL":
        plan = lane["partition_plan"]
        if plan["partial_rerun"] is not True:
            findings.add(Finding("ETL_PARTIAL_RERUN_REQUIRED", "/lane/partition_plan/partial_rerun"))
        if lane["checkpointing"] is not True:
            findings.add(Finding("ETL_CHECKPOINT_REQUIRED", "/lane/checkpointing"))
        if lane["resumable_temp_artifacts"] is not True:
            findings.add(Finding("ETL_RESUMABLE_TEMP_REQUIRED", "/lane/resumable_temp_artifacts"))

    if any(governance[field] is not False for field in (
        "authority_created",
        "source_activation_allowed",
        "network_execution_authorized",
        "promotion_authorized",
        "public_use_allowed",
    )) or governance["release_state"] != "HOLD":
        findings.add(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return sorted(findings)


def validate_document(candidate: Any) -> list[Finding]:
    scan_findings = _scan(candidate)
    schema_findings = _schema_findings(candidate) if isinstance(candidate, dict) else [Finding("ROOT_NOT_OBJECT", "/")]
    if schema_findings:
        return sorted(set(scan_findings + schema_findings))
    return _semantic_findings(candidate)


def validate_file(path: Path | str) -> ValidationResult:
    candidate, findings = _read_object(Path(path))
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(validate_document(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps({
        "file": path.as_posix(),
        "findings": [{"code": item.code, "field": item.field} for item in result.findings],
        "outcome": "PASS" if result.ok else "FAIL",
        "scope": SCOPE,
    }, sort_keys=True, separators=(",", ":"))


def _manifest() -> dict[str, list[str]]:
    try:
        value = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixtures() -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    expected = _manifest()
    ok = bool(valid and invalid and set(expected) == {path.name for path in invalid})
    for path in valid:
        result = validate_file(path)
        print(_serialize(path, result))
        ok = ok and result.ok
    for path in invalid:
        result = validate_file(path)
        print(_serialize(path, result))
        actual = sorted({item.code for item in result.findings})
        wanted = sorted(expected.get(path.name, []))
        if result.ok or actual != wanted:
            ok = False
            print(json.dumps({"actual": actual, "expected": wanted, "file": path.as_posix(), "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    if not args.files:
        parser.error("provide files or use --fixtures")
    failed = False
    for path in sorted(args.files):
        result = validate_file(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
