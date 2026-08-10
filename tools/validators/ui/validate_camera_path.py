#!/usr/bin/env python3
"""Validate fixture-only CameraPath candidates without executing motion."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import date
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/ui/camera_path.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/ui/camera_path/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:camera-path:"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("CAMERA_PATH_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("CAMERA_PATH_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("CAMERA_PATH_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("CAMERA_PATH_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("CAMERA_PATH_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("CAMERA_PATH_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("CAMERA_PATH_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("CAMERA_PATH_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"camera_path_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("CAMERA_PATH_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("CAMERA_PATH_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("CAMERA_PATH_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    states = value["view_states"]
    if states[0]["t_ms"] != 0:
        findings.add(Finding("CAMERA_PATH_FIRST_TIMESTAMP_INVALID", "/view_states/0/t_ms"))
    prior = states[0]["t_ms"]
    for index, state in enumerate(states[1:], start=1):
        if state["t_ms"] <= prior:
            findings.add(
                Finding(
                    "CAMERA_PATH_TIMESTAMP_NOT_STRICTLY_INCREASING",
                    f"/view_states/{index}/t_ms",
                )
            )
        prior = state["t_ms"]
    if states[-1]["t_ms"] != value["playback"]["duration_ms"]:
        findings.add(Finding("CAMERA_PATH_DURATION_MISMATCH", "/playback/duration_ms"))

    anchor = value["temporal_anchor"]
    try:
        valid_from = date.fromisoformat(anchor["valid_from"])
        valid_to = date.fromisoformat(anchor["valid_to"])
    except ValueError:
        findings.add(Finding("CAMERA_PATH_TEMPORAL_ANCHOR_INVALID", "/temporal_anchor"))
    else:
        if valid_from > valid_to:
            findings.add(Finding("CAMERA_PATH_TEMPORAL_ANCHOR_INVALID", "/temporal_anchor"))

    evidence_refs = value["evidence_refs"]
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("CAMERA_PATH_EVIDENCE_ORDER_INVALID", "/evidence_refs"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)

    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("CAMERA_PATH_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("CAMERA_PATH_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["camera_path_id"] != expected_id:
            findings.add(Finding("CAMERA_PATH_ID_MISMATCH", "/camera_path_id"))
    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    document["spec_hash"], document["camera_path_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "camera_path_id_override" in case:
        document["camera_path_id"] = case["camera_path_id_override"]
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.state != case["expected_state"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_state": case["expected_state"],
                    "actual_state": result.state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "executes_motion": False,
                "resolves_scene": False,
                "resolves_evidence": False,
                "evaluates_policy": False,
                "authorizes_admission": False,
                "authorizes_release": False,
                "deploys": False,
                "publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "path": item.path} for item in result.findings
            ],
            "outcome": result.outcome,
            "state": result.state,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
