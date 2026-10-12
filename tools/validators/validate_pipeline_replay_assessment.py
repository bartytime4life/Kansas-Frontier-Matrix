#!/usr/bin/env python3
"""Validate fixture-only pipeline replay assessment declarations."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/validation/pipeline_replay_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/validation/pipeline_replay_assessment/cases.json"
MAX_JSON_BYTES = 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputSymlinkError(ValueError):
    pass


class InputTooLargeError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    replay_outcome: str | None
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    return f"kfm:pipeline-replay-assessment:{spec_hash.removeprefix('sha256:')[:24]}"


def _canonical(values: Sequence[Mapping[str, Any]], key: str) -> bool:
    identifiers = [item[key] for item in values]
    return identifiers == sorted(set(identifiers))


def expected_report(document: Mapping[str, Any]) -> dict[str, Any]:
    expected = document["replay_profile"]
    observed = document["replay_observation"]
    codes: set[str] = set()
    if expected["sources"] != observed["sources"]:
        codes.add("SOURCE_SNAPSHOT_DRIFT")
    if expected["transform_parameters_digest"] != observed["transform_parameters_digest"]:
        codes.add("TRANSFORM_PARAMETERS_DRIFT")
    if expected["model_identity"] != observed["model_identity"]:
        codes.add("MODEL_IDENTITY_DRIFT")
    if expected["validators"] != observed["validators"]:
        codes.add("VALIDATOR_SET_DRIFT")
    if expected["expected_output_digest"] != observed["observed_output_digest"]:
        codes.add("OUTPUT_DRIFT")
    drift_codes = sorted(codes)
    return {
        "outcome": "FAIL" if drift_codes else "PASS",
        "drift_codes": drift_codes,
        "replay_execution_claimed": False,
        "replay_equivalence_authoritative": False,
        "separate_review_required": True,
    }


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _deny(code: str, path: str, replay_outcome: str | None = None) -> ValidationResult:
    return ValidationResult("DENY", replay_outcome, (Finding(code, path),))


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return _deny("PIPELINE_REPLAY_SCHEMA_INVALID", _pointer(errors[0].absolute_path))

    expected = document["replay_profile"]
    observed = document["replay_observation"]
    if observed["profile_ref"] != expected["profile_ref"]:
        return _deny("PIPELINE_REPLAY_PROFILE_BINDING_MISMATCH", "/replay_observation/profile_ref")
    for root_name, record in (("replay_profile", expected), ("replay_observation", observed)):
        if not _canonical(record["sources"], "source_ref"):
            return _deny("PIPELINE_REPLAY_SOURCES_NOT_CANONICAL", f"/{root_name}/sources")
        if not _canonical(record["validators"], "validator_ref"):
            return _deny("PIPELINE_REPLAY_VALIDATORS_NOT_CANONICAL", f"/{root_name}/validators")

    report = expected_report(document)
    if document["report"] != report:
        return _deny("PIPELINE_REPLAY_REPORT_MISMATCH", "/report", report["outcome"])
    spec_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], spec_hash):
        return _deny("PIPELINE_REPLAY_SPEC_HASH_MISMATCH", "/spec_hash")
    assessment_id = expected_assessment_id(spec_hash)
    if not hmac.compare_digest(document["assessment_id"], assessment_id):
        return _deny("PIPELINE_REPLAY_ID_MISMATCH", "/assessment_id")
    return ValidationResult("PASS", report["outcome"], ())


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = value
    else:
        cursor[final] = value


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest root must be an object")
    return value


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if case.get("recompute_report"):
        document["report"] = expected_report(document)
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def _load_document(path: Path) -> Mapping[str, Any]:
    if path.is_symlink():
        raise InputSymlinkError
    if not path.is_file():
        raise OSError
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InputTooLargeError
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream, object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.status != case["expected_status"]
            or result.replay_outcome != case["expected_replay_outcome"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append({"case_id": case["case_id"], "actual_status": result.status, "actual_replay_outcome": result.replay_outcome, "actual_findings": actual_findings})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    try:
        result = validate_payload(_load_document(args.path))
    except DuplicateKeyError:
        result = ValidationResult("ERROR", None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        result = ValidationResult("ERROR", None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except InputSymlinkError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),))
    except InputTooLargeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_TOO_LARGE", "/"),))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_INVALID", "/"),))
    print(json.dumps({"status": result.status, "replay_outcome": result.replay_outcome, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
