#!/usr/bin/env python3
"""Validate proposed SourceNativeQualityTranslation records without network access.

A passing result proves bounded schema shape, deterministic fixture hashing, and
local separation of source-native quality mapping, operational health, and
observation validity. It does not admit a source, resolve evidence, evaluate
policy, authorize promotion, release, deployment, publication, or public use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/common/source_native_quality_translation.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/common/source_native_quality_translation"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source-native-quality-translation-and-health-separation-only"
ZERO_DIGEST = "sha256:" + ("0" * 64)

MAPPING_OUTCOMES = {"MAPPED", "UNMAPPED", "AMBIGUOUS", "NOT_APPLICABLE"}
HEALTH_STATES = {"ONLINE", "DEGRADED", "OFFLINE", "UNKNOWN", "NOT_APPLICABLE"}
VALIDITY_STATES = {"VALID", "SUSPECT", "INVALID", "MISSING", "NOT_ASSESSED"}
ASSESSED_VALIDITY_STATES = {"VALID", "SUSPECT", "INVALID"}


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

    @property
    def error(self) -> bool:
        return any(
            finding.code
            in {
                "FILE_NOT_FOUND",
                "FILE_READ_ERROR",
                "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED",
                "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY",
                "JSON_INVALID",
                "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8",
                "ROOT_NOT_OBJECT",
                "SCHEMA_UNAVAILABLE",
            }
            for finding in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
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
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
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
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    source = _mapping(candidate.get("source"))
    mapping = _mapping(candidate.get("mapping"))
    health = _mapping(candidate.get("operational_health"))
    validity = _mapping(candidate.get("observation_validity"))
    separation = _mapping(candidate.get("separation"))
    provenance = _mapping(candidate.get("provenance"))
    governance = _mapping(candidate.get("governance"))

    for field, value in (
        ("/spec_hash", candidate.get("spec_hash")),
        ("/source/vocabulary_digest", source.get("vocabulary_digest")),
        ("/mapping/profile_digest", mapping.get("profile_digest")),
    ):
        if value == ZERO_DIGEST:
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    supplied_hash = candidate.get("spec_hash")
    if isinstance(supplied_hash, str):
        try:
            expected_hash = _canonical_spec_hash(candidate)
        except (TypeError, ValueError, RecursionError):
            expected_hash = None
        if expected_hash is not None and supplied_hash != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    canonical_arrays = (
        ("/mapping/reason_codes", _array(mapping.get("reason_codes"))),
        ("/operational_health/reason_codes", _array(health.get("reason_codes"))),
        ("/operational_health/evidence_refs", _array(health.get("evidence_refs"))),
        ("/observation_validity/reason_codes", _array(validity.get("reason_codes"))),
        ("/observation_validity/evidence_refs", _array(validity.get("evidence_refs"))),
        ("/provenance/input_refs", _array(provenance.get("input_refs"))),
    )
    for field, values in canonical_arrays:
        if not _sorted_unique_strings(values):
            findings.append(Finding("REFS_OR_REASONS_NOT_CANONICAL", field))

    vocabulary_fields = (
        source.get("vocabulary_id"),
        source.get("vocabulary_version"),
        source.get("vocabulary_digest"),
        source.get("native_code"),
    )
    if not all(isinstance(value, str) and value.strip() for value in vocabulary_fields):
        findings.append(
            Finding(
                "NATIVE_VOCABULARY_IDENTITY_INCOMPLETE",
                "/source",
            )
        )

    outcome = mapping.get("outcome")
    normalized_quality = mapping.get("normalized_quality")
    semantic_loss = mapping.get("semantic_loss")
    unmapped_state = mapping.get("unmapped_state")
    review_required = mapping.get("review_required")

    if outcome == "MAPPED":
        if (
            normalized_quality in {"UNKNOWN", "NOT_APPLICABLE"}
            or unmapped_state != "NOT_UNMAPPED"
            or semantic_loss == "UNKNOWN"
        ):
            findings.append(Finding("MAPPED_NORMALIZATION_INCONSISTENT", "/mapping"))
        if semantic_loss in {"PARTIAL", "MATERIAL"} and review_required is not True:
            findings.append(Finding("SEMANTIC_LOSS_REVIEW_MISSING", "/mapping"))
    elif outcome == "UNMAPPED":
        if (
            normalized_quality != "UNKNOWN"
            or unmapped_state != "UNMAPPED_PRESERVED"
            or semantic_loss not in {"MATERIAL", "UNKNOWN"}
        ):
            findings.append(
                Finding("UNMAPPED_NORMALIZATION_COLLAPSE", "/mapping")
            )
        if review_required is not True:
            findings.append(
                Finding("UNMAPPED_MAPPING_REVIEW_MISSING", "/mapping/review_required")
            )
    elif outcome == "AMBIGUOUS":
        if normalized_quality not in {"UNKNOWN", "SUSPECT"} or unmapped_state != "AMBIGUOUS_PRESERVED":
            findings.append(Finding("AMBIGUOUS_NORMALIZATION_INCONSISTENT", "/mapping"))
        if semantic_loss == "NONE":
            findings.append(Finding("SEMANTIC_LOSS_INCONSISTENT", "/mapping/semantic_loss"))
        if review_required is not True:
            findings.append(
                Finding(
                    "AMBIGUOUS_MAPPING_REVIEW_MISSING",
                    "/mapping/review_required",
                )
            )
    elif outcome == "NOT_APPLICABLE":
        if (
            normalized_quality != "NOT_APPLICABLE"
            or unmapped_state != "NOT_APPLICABLE"
            or semantic_loss != "NONE"
            or review_required is not False
        ):
            findings.append(Finding("NOT_APPLICABLE_MAPPING_INCONSISTENT", "/mapping"))

    health_state = health.get("state")
    validity_state = validity.get("state")
    affects_availability = health.get("affects_current_observation_availability")
    if health_state == "OFFLINE" and affects_availability is not True:
        findings.append(
            Finding(
                "HEALTH_AVAILABILITY_INCONSISTENT",
                "/operational_health/affects_current_observation_availability",
            )
        )
    if health_state in {"ONLINE", "NOT_APPLICABLE"} and affects_availability is not False:
        findings.append(
            Finding(
                "HEALTH_AVAILABILITY_INCONSISTENT",
                "/operational_health/affects_current_observation_availability",
            )
        )

    if validity_state in HEALTH_STATES and validity_state not in VALIDITY_STATES:
        findings.append(
            Finding(
                "HEALTH_VALIDITY_VOCABULARY_COLLAPSE",
                "/observation_validity/state",
            )
        )

    if (
        health.get("observation_validity_decided") is not False
        or validity.get("derived_from_operational_health") is not False
    ):
        findings.append(
            Finding(
                "HEALTH_VALIDITY_CAUSAL_COLLAPSE",
                "/observation_validity/derived_from_operational_health",
            )
        )

    if any(
        separation.get(field) is not True
        for field in (
            "health_and_validity_independent",
            "offline_does_not_invalidate_prior_observations",
            "no_data_is_not_environmental_condition",
            "source_quality_is_not_source_authority",
        )
    ):
        findings.append(Finding("SEPARATION_BOUNDARY_VIOLATION", "/separation"))

    observation_ref = validity.get("observation_ref")
    assessed_at = validity.get("assessed_at")
    if validity_state in ASSESSED_VALIDITY_STATES and (
        observation_ref is None or assessed_at is None
    ):
        findings.append(
            Finding("OBSERVATION_SUPPORT_MISSING", "/observation_validity")
        )
    if validity_state == "MISSING" and (observation_ref is not None or assessed_at is None):
        findings.append(
            Finding("MISSING_OBSERVATION_STATE_INCONSISTENT", "/observation_validity")
        )
    if validity_state == "NOT_ASSESSED" and assessed_at is not None:
        findings.append(
            Finding("NOT_ASSESSED_STATE_INCONSISTENT", "/observation_validity/assessed_at")
        )

    if health.get("assessment_id") == validity.get("assessment_id"):
        findings.append(
            Finding("ASSESSMENT_IDENTITY_COLLAPSE", "/observation_validity/assessment_id")
        )

    recorded_at = _parse_time(provenance.get("recorded_at"))
    health_observed_at = _parse_time(health.get("observed_at"))
    validity_assessed_at = _parse_time(validity.get("assessed_at"))
    if recorded_at and health_observed_at and health_observed_at > recorded_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/operational_health/observed_at"))
    if recorded_at and validity_assessed_at and validity_assessed_at > recorded_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/observation_validity/assessed_at"))

    governance_flags = (
        "authority_created",
        "source_admitted",
        "evidence_closure_claimed",
        "policy_evaluated",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
        "public_use_allowed",
    )
    if (
        any(governance.get(field) is not False for field in governance_flags)
        or governance.get("release_ref") is not None
    ):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_translation(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [
                {"code": item.code, "field": item.field}
                for item in result.findings
            ],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(directory.glob(f"{prefix}*.json"), key=lambda path: path.as_posix())


def _expected_manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads(
            (directory / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = _fixture_files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _fixture_files(FIXTURE_ROOT / "invalid", "invalid_")
    manifest = _expected_manifest(FIXTURE_ROOT / "invalid")
    if not valid_files or not invalid_files:
        return 1

    passed = True
    for path in valid_files:
        result = validate_translation(path)
        print(_serialize(path, result))
        passed = passed and result.ok

    for path in invalid_files:
        result = validate_translation(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": expected,
                        "file": _display_path(path),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )

    expected_names = {path.name for path in invalid_files}
    if set(manifest) != expected_names:
        passed = False
        print(
            json.dumps(
                {
                    "actual": sorted(manifest),
                    "expected": sorted(expected_names),
                    "outcome": "FIXTURE_MANIFEST_INVENTORY_ERROR",
                },
                sort_keys=True,
                separators=(",", ":"),
            ),
            file=sys.stderr,
        )
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate SourceNativeQualityTranslation records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="Run the repository valid/invalid fixture profile.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files:
            print("--fixtures cannot be combined with file arguments", file=sys.stderr)
            return 2
        return run_fixture_profile()
    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2

    exit_code = 0
    for path in args.files:
        result = validate_translation(path)
        print(_serialize(path, result))
        if result.error:
            exit_code = max(exit_code, 2)
        elif not result.ok:
            exit_code = max(exit_code, 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
