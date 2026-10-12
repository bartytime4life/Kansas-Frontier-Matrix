#!/usr/bin/env python3
"""Validate fixture-only SSURGO/gNATSGO yearly-diff profiles."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError:
    def compute_spec_hash(value: Any) -> str:
        raw = json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
        return "sha256:" + hashlib.sha256(raw).hexdigest()

PROFILE = ROOT / "pipeline_specs/soil/ssurgo_yearly_diff_profile.v1.json"
SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/ssurgo_yearly_diff_profile.schema.json"
CASES = ROOT / "fixtures/domains/soil/yearly_diff/cases.json"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "soil-ssurgo-gnatsgo-yearly-diff-fixture-only"

SOURCE_PROFILES = {
    "GNATSGO": (
        "GRIDDED_DERIVATIVE_SOIL",
        "GNATSGO_GRID_METADATA_DIFF_V1",
        "data/registry/sources/soil/nrcs-gnatsgo.yaml",
    ),
    "SSURGO": (
        "AUTHORITATIVE_STATIC_SOIL_SURVEY",
        "SSURGO_KEYED_RECORD_DIFF_V1",
        "data/registry/sources/soil/nrcs-ssurgo.yaml",
    ),
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Result:
    outcome: str
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


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                ).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    errors = sorted(
        errors,
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    declared = value.get("spec_hash")
    candidate = {key: item for key, item in value.items() if key != "spec_hash"}
    if isinstance(declared, str) and declared != compute_spec_hash(candidate):
        findings.append(Finding("SOIL_YEARLY_SPEC_HASH_MISMATCH", "/spec_hash"))

    family = value.get("source_family")
    expected = SOURCE_PROFILES.get(family)
    actual = (
        value.get("support_type"),
        (value.get("diff") or {}).get("computation_profile")
        if isinstance(value.get("diff"), dict)
        else None,
        value.get("source_descriptor_ref"),
    )
    if expected is None or actual != expected:
        findings.append(Finding("SOIL_YEARLY_SOURCE_ROLE_INVALID", "/support_type"))

    previous = value.get("previous_snapshot")
    current = value.get("current_snapshot")
    if isinstance(previous, dict) and isinstance(current, dict):
        previous_year = previous.get("dataset_year")
        current_year = current.get("dataset_year")
        if (
            not isinstance(previous_year, int)
            or not isinstance(current_year, int)
            or current_year != previous_year + 1
        ):
            findings.append(
                Finding(
                    "SOIL_YEARLY_YEAR_SEQUENCE_INVALID",
                    "/current_snapshot/dataset_year",
                )
            )

    normalization = value.get("normalization")
    if isinstance(normalization, dict):
        changed = normalization.get("geometry_changed") is True or normalization.get("attributes_changed") is True
        receipts = normalization.get("transform_receipt_refs")
        if isinstance(receipts, list):
            if receipts != sorted(set(receipts)):
                findings.append(
                    Finding(
                        "SOIL_YEARLY_TRANSFORM_RECEIPTS_NOT_CANONICAL",
                        "/normalization/transform_receipt_refs",
                    )
                )
            if changed and not receipts:
                findings.append(
                    Finding(
                        "SOIL_YEARLY_TRANSFORM_RECEIPT_REQUIRED",
                        "/normalization/transform_receipt_refs",
                    )
                )
            if not changed and receipts:
                findings.append(
                    Finding(
                        "SOIL_YEARLY_TRANSFORM_RECEIPT_UNEXPECTED",
                        "/normalization/transform_receipt_refs",
                    )
                )

    diff = value.get("diff")
    if isinstance(diff, dict):
        properties = diff.get("changed_property_names")
        if isinstance(properties, list) and properties != sorted(set(properties)):
            findings.append(
                Finding(
                    "SOIL_YEARLY_CHANGED_PROPERTIES_NOT_CANONICAL",
                    "/diff/changed_property_names",
                )
            )
        if diff.get("observed_property_relabelled") is True:
            findings.append(
                Finding(
                    "SOIL_YEARLY_OBSERVED_PROPERTY_RELABEL_DENIED",
                    "/diff/observed_property_relabelled",
                )
            )
        counts = [
            diff.get("added_records"),
            diff.get("removed_records"),
            diff.get("modified_records"),
        ]
        if all(isinstance(item, int) for item in counts):
            total = sum(counts)
            if total == 0 and properties:
                findings.append(
                    Finding(
                        "SOIL_YEARLY_DIFF_SUMMARY_INCOHERENT",
                        "/diff/changed_property_names",
                    )
                )
            if diff.get("modified_records") == 0 and properties:
                findings.append(
                    Finding(
                        "SOIL_YEARLY_DIFF_SUMMARY_INCOHERENT",
                        "/diff/changed_property_names",
                    )
                )

    governance = value.get("governance")
    if isinstance(governance, dict) and any(item is not False for item in governance.values()):
        findings.append(Finding("SOIL_YEARLY_AUTHORITY_OVERREACH", "/governance"))

    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", tuple(sorted(set(schema_findings))))
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", tuple(sorted(set(semantic_findings))))
    return Result("PASS", ())


def validate(path: Path) -> Result:
    value, operational_findings = _read(path)
    if value is None:
        return Result("ERROR", tuple(sorted(set(operational_findings))))
    return validate_payload(value)


def load_fixture_manifest() -> dict[str, Any]:
    value = json.loads(CASES.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("bases"), dict) or not isinstance(value.get("cases"), list):
        raise ValueError("fixture manifest must contain bases and cases")
    return value


def _pointer_parts(path: str) -> list[str]:
    if not path.startswith("/"):
        raise ValueError("mutation path must be a JSON pointer")
    return [part.replace("~1", "/").replace("~0", "~") for part in path.split("/")[1:]]


def _apply_mutation(payload: dict[str, Any], mutation: Mapping[str, Any]) -> None:
    if mutation.get("op") != "replace" or not isinstance(mutation.get("path"), str):
        raise ValueError("only deterministic replace mutations are supported")
    parts = _pointer_parts(mutation["path"])
    if not parts:
        raise ValueError("root replacement is denied")
    cursor: Any = payload
    for part in parts[:-1]:
        if not isinstance(cursor, dict) or part not in cursor:
            raise ValueError("mutation path is missing")
        cursor = cursor[part]
    if not isinstance(cursor, dict) or parts[-1] not in cursor:
        raise ValueError("mutation path is missing")
    cursor[parts[-1]] = copy.deepcopy(mutation.get("value"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    bases = manifest.get("bases")
    base_id = case.get("base")
    if not isinstance(bases, dict) or not isinstance(base_id, str) or not isinstance(bases.get(base_id), dict):
        raise ValueError("fixture base is invalid")
    payload = copy.deepcopy(bases[base_id])
    mutations = case.get("mutations", [])
    if not isinstance(mutations, list):
        raise ValueError("fixture mutations must be an array")
    for mutation in mutations:
        if not isinstance(mutation, dict):
            raise ValueError("fixture mutation must be an object")
        _apply_mutation(payload, mutation)
    if case.get("preserve_spec_hash") is True:
        override = case.get("spec_hash_override")
        if not isinstance(override, str):
            raise ValueError("preserved spec_hash requires an override")
        payload["spec_hash"] = override
    else:
        payload["spec_hash"] = compute_spec_hash(payload)
    return payload


def run_fixtures() -> int:
    try:
        manifest = load_fixture_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return 2
    passed = True
    for case in manifest["cases"]:
        try:
            payload = materialize_case(manifest, case)
            result = validate_payload(payload)
        except (KeyError, TypeError, ValueError):
            result = Result("ERROR", (Finding("FIXTURE_PAYLOAD_INVALID", "/payload"),))
        actual_findings = [
            {"code": item.code, "field": item.field}
            for item in result.findings
        ]
        match = (
            result.outcome == case["expected_outcome"]
            and actual_findings == case["expected_findings"]
        )
        print(
            json.dumps(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": actual_findings,
                    "suite_match": match,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and match
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only SSURGO/gNATSGO yearly-diff profiles."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()

    exit_code = 0
    for path in args.files or [PROFILE]:
        result = validate(path)
        print(
            json.dumps(
                {
                    "file": path.as_posix(),
                    "outcome": result.outcome,
                    "findings": [
                        {"code": item.code, "field": item.field}
                        for item in result.findings
                    ],
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        if result.outcome == "ERROR":
            exit_code = max(exit_code, 2)
        elif result.outcome == "DENY":
            exit_code = max(exit_code, 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
