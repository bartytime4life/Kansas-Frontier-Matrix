#!/usr/bin/env python3
"""Validate fixture-first SourceProbeEnvelope profiles."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/contracts/v1/source/source_probe_envelope.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/source/source_probe_envelope"
MAX_BYTES = 2 * 1024 * 1024


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


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


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
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique, parse_constant=_reject_nonfinite)
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


def canonical_hash(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("spec_hash", None)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    profile = value.get("profile")
    data = _mapping(value.get("profile_data"))
    material = _mapping(value.get("materiality"))
    scope = _mapping(value.get("scope"))

    if value.get("spec_hash") != canonical_hash(value):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    if profile == "NASS_AGGREGATE":
        required = {"source_role", "row_count", "canonical_rows_sha256", "field_level_claim"}
        if set(data) != required:
            findings.append(Finding("NASS_PROFILE_SHAPE_INVALID", "/profile_data"))
        if data.get("source_role") != "aggregate":
            findings.append(Finding("NASS_SOURCE_ROLE_INVALID", "/profile_data/source_role"))
        if scope.get("geography_level") not in {"NATIONAL", "STATE", "COUNTY"}:
            findings.append(Finding("NASS_GEOGRAPHY_TOO_PRECISE", "/scope/geography_level"))
        if data.get("field_level_claim") is not False:
            findings.append(Finding("NASS_FIELD_LEVEL_CLAIM_DENIED", "/profile_data/field_level_claim"))
        row_count = data.get("row_count")
        if isinstance(row_count, bool) or not isinstance(row_count, int) or row_count < 0:
            findings.append(Finding("NASS_ROW_COUNT_INVALID", "/profile_data/row_count"))
        digest = data.get("canonical_rows_sha256")
        if not isinstance(digest, str) or not digest.startswith("sha256:") or len(digest) != 71:
            findings.append(Finding("NASS_CONTENT_DIGEST_MISSING", "/profile_data/canonical_rows_sha256"))

    elif profile == "EDNA_MONITORING":
        required = {"source_role", "chain_of_custody_complete", "controls", "interpretation", "population_status_claim"}
        if set(data) != required:
            findings.append(Finding("EDNA_PROFILE_SHAPE_INVALID", "/profile_data"))
        if data.get("source_role") != "observed":
            findings.append(Finding("EDNA_SOURCE_ROLE_INVALID", "/profile_data/source_role"))
        controls = _mapping(data.get("controls"))
        if set(controls) != {"positive_control", "negative_control"} or any(controls.get(key) not in {"PASS", "FAIL", "UNKNOWN"} for key in controls):
            findings.append(Finding("EDNA_CONTROLS_INVALID", "/profile_data/controls"))
        if data.get("population_status_claim") is not None:
            findings.append(Finding("EDNA_POPULATION_INFERENCE_DENIED", "/profile_data/population_status_claim"))
        interpretation = data.get("interpretation")
        if interpretation not in {"DETECTION_SIGNAL", "NO_DETECTION", "INCONCLUSIVE"}:
            findings.append(Finding("EDNA_INTERPRETATION_INVALID", "/profile_data/interpretation"))
        control_values = set(controls.values())
        expected = "DENY" if "FAIL" in control_values else "HOLD" if (data.get("chain_of_custody_complete") is not True or "UNKNOWN" in control_values or interpretation == "INCONCLUSIVE") else material.get("status")
        if "FAIL" in control_values and material.get("status") != "DENY":
            findings.append(Finding("EDNA_FAILED_CONTROL_NOT_DENIED", "/materiality/status"))
        if expected == "HOLD" and material.get("status") != "HOLD":
            findings.append(Finding("EDNA_INCOMPLETE_EVIDENCE_NOT_HELD", "/materiality/status"))

    elif profile == "KGS_GEOLOGY":
        required = {"source_role", "geology_kind", "unit_vocabulary", "resource_inference", "regulatory_inference"}
        if set(data) != required:
            findings.append(Finding("KGS_PROFILE_SHAPE_INVALID", "/profile_data"))
        if data.get("source_role") != "modeled":
            findings.append(Finding("KGS_SOURCE_ROLE_INVALID", "/profile_data/source_role"))
        if data.get("geology_kind") not in {"BEDROCK", "SURFICIAL"}:
            findings.append(Finding("KGS_GEOLOGY_KIND_INVALID", "/profile_data/geology_kind"))
        vocab = data.get("unit_vocabulary")
        if not isinstance(vocab, list) or not vocab or not all(isinstance(item, str) and item for item in vocab):
            findings.append(Finding("KGS_UNIT_VOCABULARY_MISSING", "/profile_data/unit_vocabulary"))
        if data.get("resource_inference") is not False:
            findings.append(Finding("KGS_RESOURCE_INFERENCE_DENIED", "/profile_data/resource_inference"))
        if data.get("regulatory_inference") is not False:
            findings.append(Finding("KGS_REGULATORY_INFERENCE_DENIED", "/profile_data/regulatory_inference"))

    elif profile == "LOC_CHRONICLING_AMERICA":
        required = {"source_role", "family_decision", "rights_state", "care_review", "source_activation"}
        if set(data) != required:
            findings.append(Finding("LOC_PROFILE_SHAPE_INVALID", "/profile_data"))
        if data.get("source_role") != "candidate":
            findings.append(Finding("LOC_SOURCE_ROLE_INVALID", "/profile_data/source_role"))
        if data.get("family_decision") != "DEFERRED_OPEN_DSC_10":
            findings.append(Finding("LOC_FAMILY_DECISION_UNRESOLVED", "/profile_data/family_decision"))
        if data.get("rights_state") not in {"UNKNOWN", "NEEDS_REVIEW"} or data.get("care_review") != "PENDING":
            findings.append(Finding("LOC_RIGHTS_CARE_NOT_HELD", "/profile_data"))
        if data.get("source_activation") is not False:
            findings.append(Finding("LOC_ACTIVATION_DENIED", "/profile_data/source_activation"))
        if material.get("status") != "HOLD":
            findings.append(Finding("LOC_PROFILE_MUST_HOLD", "/materiality/status"))

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
    return json.dumps({"file": display, "findings": [{"code": item.code, "path": item.path} for item in result.findings], "outcome": "PASS" if result.ok else "FAIL", "scope": "source-probe-envelope-fixture-only"}, sort_keys=True, separators=(",", ":"))


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
