#!/usr/bin/env python3
"""Validate fixture-only vegetation connectivity gate assessments."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from hashing import compute_spec_hash
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/agriculture/vegetation_connectivity_gate.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/domains/agriculture/vegetation_connectivity_gate/cases.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "fixture-only-vegetation-connectivity-gate"


class DuplicateKeyError(ValueError):
    """Raised when an object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for non-standard NaN or Infinity tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        return "PASS" if self.ok else "DENY"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_payload(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(payload: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    ordered = sorted(
        errors,
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in ordered]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _basis_points(present: int, total: int) -> int:
    """Round 10,000 * present / total to nearest integer, halves upward."""

    return (present * 10000 + total // 2) // total


def _component_expected(
    component: Mapping[str, Any],
    observation_count: int,
    thresholds: Mapping[str, Any],
) -> tuple[int, bool]:
    present = len(component["present_observation_ids"])
    persistence = _basis_points(present, observation_count)
    qualifies = (
        int(component["area_m2"]) >= int(thresholds["min_component_area_m2"])
        and present >= int(thresholds["min_persistent_observations"])
        and persistence >= int(thresholds["min_persistence_basis_points"])
    )
    return persistence, qualifies


def _expected_summary(
    components: Sequence[Mapping[str, Any]],
    observation_count: int,
    thresholds: Mapping[str, Any],
) -> dict[str, int]:
    qualifying_areas = [
        int(component["area_m2"])
        for component in components
        if _component_expected(component, observation_count, thresholds)[1]
    ]
    return {
        "component_count": len(components),
        "qualifying_component_count": len(qualifying_areas),
        "qualifying_area_m2": sum(qualifying_areas),
        "largest_qualifying_component_area_m2": max(qualifying_areas, default=0),
    }


def _expected_reasons(payload: Mapping[str, Any]) -> list[str]:
    thresholds = payload["thresholds"]
    components = payload["components"]
    observation_count = len(payload["observation_ids"])
    reasons: set[str] = set()

    if any(item["receipt_state"] != "RESOLVED" for item in payload["inputs"]):
        reasons.add("INPUT_RECEIPT_UNRESOLVED")

    area_qualified = [
        component
        for component in components
        if int(component["area_m2"]) >= int(thresholds["min_component_area_m2"])
    ]
    fully_qualified = [
        component
        for component in components
        if _component_expected(component, observation_count, thresholds)[1]
    ]
    if not area_qualified:
        reasons.add("AREA_THRESHOLD_NOT_MET")
    elif not fully_qualified:
        reasons.add("PERSISTENCE_THRESHOLD_NOT_MET")
    elif len(fully_qualified) < int(thresholds["min_qualifying_component_count"]):
        reasons.add("QUALIFYING_COMPONENT_COUNT_NOT_MET")
    return sorted(reasons)


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    hash_subject = {key: value for key, value in payload.items() if key != "spec_hash"}
    if payload["spec_hash"] != compute_spec_hash(hash_subject):
        findings.append(Finding("VEGETATION_CONNECTIVITY_SPEC_HASH_MISMATCH", "/spec_hash"))

    observation_ids = payload["observation_ids"]
    if observation_ids != sorted(observation_ids) or len(observation_ids) != len(set(observation_ids)):
        findings.append(Finding("OBSERVATIONS_NOT_CANONICAL", "/observation_ids"))
    observation_set = set(observation_ids)

    inputs = payload["inputs"]
    input_refs = [item["artifact_ref"] for item in inputs]
    if input_refs != sorted(input_refs) or len(input_refs) != len(set(input_refs)):
        findings.append(Finding("INPUTS_NOT_CANONICAL", "/inputs"))

    components = payload["components"]
    component_ids = [component["component_id"] for component in components]
    if component_ids != sorted(component_ids) or len(component_ids) != len(set(component_ids)):
        findings.append(Finding("COMPONENTS_NOT_CANONICAL", "/components"))

    thresholds = payload["thresholds"]
    observation_count = len(observation_ids)
    for index, component in enumerate(components):
        present_ids = component["present_observation_ids"]
        base_path = f"/components/{index}"
        if present_ids != sorted(present_ids) or len(present_ids) != len(set(present_ids)):
            findings.append(Finding("COMPONENT_OBSERVATIONS_NOT_CANONICAL", f"{base_path}/present_observation_ids"))
        if any(item not in observation_set for item in present_ids):
            findings.append(Finding("COMPONENT_OBSERVATION_UNKNOWN", f"{base_path}/present_observation_ids"))
        expected_persistence, expected_qualifies = _component_expected(
            component, observation_count, thresholds
        )
        if int(component["persistence_basis_points"]) != expected_persistence:
            findings.append(Finding("COMPONENT_PERSISTENCE_MISMATCH", f"{base_path}/persistence_basis_points"))
        if component["qualifies"] is not expected_qualifies:
            findings.append(Finding("COMPONENT_QUALIFICATION_MISMATCH", f"{base_path}/qualifies"))

    expected_summary = _expected_summary(components, observation_count, thresholds)
    if payload["summary"] != expected_summary:
        findings.append(Finding("SUMMARY_MISMATCH", "/summary"))

    expected_reasons = _expected_reasons(payload)
    if payload["outcome"]["reasons"] != expected_reasons:
        findings.append(Finding("DECISION_REASONS_MISMATCH", "/outcome/reasons"))
    expected_status = "PROPOSED_INDICATOR_CANDIDATE" if not expected_reasons else "HOLD"
    if payload["outcome"]["status"] != expected_status:
        findings.append(Finding("DECISION_OUTCOME_MISMATCH", "/outcome/status"))

    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    """Validate parsed shape, deterministic identity, and semantic closure."""

    findings = _schema_findings(payload)
    if not findings:
        findings.extend(_semantic_findings(payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    payload, findings = _load_payload(path)
    if payload is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_payload(payload)


def load_fixture_manifest() -> dict[str, Any]:
    value = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("bases"), dict) or not isinstance(value.get("cases"), list):
        raise ValueError("fixture manifest is invalid")
    return value


def _replace_pointer(payload: dict[str, Any], path: str, value: Any) -> None:
    if not path.startswith("/"):
        raise ValueError("mutation path must be a JSON pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in path.split("/")[1:]]
    if not parts:
        raise ValueError("root replacement is denied")
    cursor: Any = payload
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = copy.deepcopy(value)
    elif isinstance(cursor, dict) and final in cursor:
        cursor[final] = copy.deepcopy(value)
    else:
        raise ValueError("mutation path is invalid")


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    bases = manifest["bases"]
    base_id = case["base"]
    if base_id not in bases or not isinstance(bases[base_id], dict):
        raise ValueError("fixture base is invalid")
    payload = copy.deepcopy(bases[base_id])
    for mutation in case.get("mutations", []):
        if not isinstance(mutation, dict) or mutation.get("op") != "replace":
            raise ValueError("only deterministic replace mutations are supported")
        _replace_pointer(payload, mutation["path"], mutation.get("value"))
    hash_subject = {key: value for key, value in payload.items() if key != "spec_hash"}
    payload["spec_hash"] = case.get("spec_hash_override") or compute_spec_hash(hash_subject)
    return payload


def run_fixtures() -> int:
    try:
        manifest = load_fixture_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return 2
    passed = True
    for case in manifest["cases"]:
        try:
            result = validate_payload(materialize_case(manifest, case))
        except (KeyError, TypeError, ValueError):
            result = ValidationResult((Finding("FIXTURE_PAYLOAD_INVALID", "/payload"),))
        actual_findings = [
            {"code": finding.code, "path": finding.path} for finding in result.findings
        ]
        matches = (
            result.outcome == case["expected_outcome"]
            and actual_findings == case["expected_findings"]
        )
        print(json.dumps({
            "case_id": case["case_id"],
            "outcome": result.outcome,
            "findings": actual_findings,
            "suite_match": matches,
        }, sort_keys=True, separators=(",", ":")))
        passed = passed and matches
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-only vegetation connectivity gate assessment."
    )
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            raise SystemExit("--fixtures cannot be combined with a path")
        return run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(json.dumps({
        "ok": result.ok,
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "path": finding.path} for finding in result.findings
        ],
        "scope": SCOPE,
        "authority": {
            "source_activation": False,
            "raw_admission": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
