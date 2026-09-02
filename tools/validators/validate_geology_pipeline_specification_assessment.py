#!/usr/bin/env python3
"""Validate fixture-only Geology pipeline specification assessment candidates.

The validator reads declarations only. It does not execute specifications, contact
sources, resolve references, inspect geometry, infer geology, classify resources,
move lifecycle objects, decide policy/review, release, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/geology/geology_pipeline_specification_assessment.schema.json"
FIXTURE_PATH = ROOT / "fixtures/contracts/v1/domains/geology/geology_pipeline_specification_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:geology:pipeline-specification-assessment:"


class DuplicateKeyError(ValueError):
    """Raised when JSON repeats an object key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-finite number token."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return [finding.code for finding in self.findings]


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_identity(candidate: Mapping[str, object]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("spec_hash", None)
    subject.pop("assessment_id", None)
    spec_hash = canonical_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate)
    )
    return [] if not errors else [Finding("SCHEMA_INVALID")]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _integrity_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash, expected_id = compute_identity(candidate)
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED"))

    source = candidate["source_bindings"]
    semantics = candidate["domain_semantics"]
    assert isinstance(source, Mapping)
    assert isinstance(semantics, Mapping)
    arrays = (
        source["source_descriptor_refs"],
        source["source_roles"],
        semantics["object_roles"],
        semantics["knowledge_characters"],
        semantics["anti_collapse_assertions"],
    )
    if not all(_canonical_strings(value) for value in arrays):
        findings.add(Finding("REFERENCE_OR_VOCABULARY_ARRAY_NOT_CANONICAL"))
    return sorted(findings)


PROFILE_RULES: dict[str, dict[str, object]] = {
    "BEDROCK_UNITS": {
        "role": "GeologicUnit",
        "support": "MAP_UNIT_POLYGON",
        "knowledge_any": {"INTERPRETED"},
        "assertion": "MAP_UNIT_NOT_POINT_TRUTH",
        "resource": "NONE",
        "scale": True,
    },
    "SURFICIAL_UNITS": {
        "role": "SurficialUnit",
        "support": "MAP_UNIT_POLYGON",
        "knowledge_any": {"INTERPRETED"},
        "assertion": "MAP_UNIT_NOT_POINT_TRUTH",
        "resource": "NONE",
        "scale": True,
    },
    "BOREHOLES": {
        "role": "BoreholeReference",
        "support": "BOREHOLE_POINT",
        "knowledge_any": {"OBSERVED"},
        "assertion": "GENERALIZED_GEOMETRY_NOT_PUBLIC_APPROVAL",
        "resource": "NONE",
        "depth": True,
        "controlled": True,
    },
    "WELL_LOGS": {
        "role": "WellLogReference",
        "support": "WELL_LOG_INTERVAL",
        "knowledge_any": {"MEASURED", "OBSERVED"},
        "assertion": "GENERALIZED_GEOMETRY_NOT_PUBLIC_APPROVAL",
        "resource": "NONE",
        "depth": True,
        "vertical": True,
        "controlled": True,
    },
    "CROSS_SECTIONS": {
        "role": "CrossSection",
        "support": "CROSS_SECTION_2D",
        "knowledge_any": {"INTERPRETED", "MODELED"},
        "assertion": "INTERPRETATION_NOT_OBSERVATION",
        "resource": "NONE",
        "scale": True,
        "depth": True,
        "vertical": True,
    },
    "MINERAL_OCCURRENCES": {
        "role": "MineralOccurrence",
        "support": "OCCURRENCE_POINT_OR_AREA",
        "knowledge_any": {"INTERPRETED", "OBSERVED"},
        "assertion": "OCCURRENCE_NOT_DEPOSIT_OR_ESTIMATE",
        "resource": "OCCURRENCE",
    },
}


def _coherence_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    specification = candidate["specification"]
    source = candidate["source_bindings"]
    semantics = candidate["domain_semantics"]
    spatial = candidate["spatial_temporal"]
    lifecycle = candidate["lifecycle"]
    reviews = candidate["review_requirements"]
    assert isinstance(specification, Mapping)
    assert isinstance(source, Mapping)
    assert isinstance(semantics, Mapping)
    assert isinstance(spatial, Mapping)
    assert isinstance(lifecycle, Mapping)
    assert isinstance(reviews, Mapping)

    family = str(specification["specification_family"])
    rule = PROFILE_RULES[family]
    roles = set(semantics["object_roles"])
    knowledge = set(semantics["knowledge_characters"])
    assertions = set(semantics["anti_collapse_assertions"])

    if roles != {rule["role"]}:
        findings.add(Finding("PROFILE_OBJECT_ROLE_MISMATCH"))
    if spatial["support_kind"] != rule["support"]:
        findings.add(Finding("PROFILE_SPATIAL_SUPPORT_MISMATCH"))
    if not knowledge.intersection(rule["knowledge_any"]):
        findings.add(Finding("PROFILE_KNOWLEDGE_CHARACTER_MISMATCH"))
    if rule["assertion"] not in assertions:
        findings.add(Finding("PROFILE_ANTI_COLLAPSE_ASSERTION_MISSING"))
    if semantics["resource_claim_class"] != rule["resource"]:
        findings.add(Finding("PROFILE_RESOURCE_CLASS_MISMATCH"))

    if source["rights_state"] == "DENIED":
        findings.add(Finding("SOURCE_RIGHTS_DENIED"))
    if rule.get("controlled") and spatial["sensitivity_state"] != "CONTROLLED":
        findings.add(Finding("SENSITIVE_SUBSURFACE_CONTROL_REQUIRED"))
    if rule.get("scale") and spatial["map_scale_denominator"] is None:
        findings.add(Finding("MAP_SCALE_REQUIRED"))
    if rule.get("depth") and spatial["depth_reference_ref"] is None:
        findings.add(Finding("DEPTH_REFERENCE_REQUIRED"))
    if rule.get("vertical") and spatial["vertical_datum_ref"] is None:
        findings.add(Finding("VERTICAL_DATUM_REQUIRED"))

    if "ADMINISTRATIVE" in knowledge and "ADMINISTRATIVE_RECORD_NOT_PHYSICAL_GEOLOGY" not in assertions:
        findings.add(Finding("ADMINISTRATIVE_ANTI_COLLAPSE_ASSERTION_MISSING"))
    if knowledge.intersection({"INTERPRETED", "MODELED"}) and "INTERPRETATION_NOT_OBSERVATION" not in assertions:
        if family not in {"BEDROCK_UNITS", "SURFICIAL_UNITS"}:
            findings.add(Finding("INTERPRETATION_ANTI_COLLAPSE_ASSERTION_MISSING"))

    if specification["assessment_state"] == "COMPLETE":
        closure = [
            specification["parser_ref"],
            specification["consumer_ref"],
            semantics["claim_scope_statement"],
            spatial["horizontal_crs_ref"],
            spatial["source_vintage"],
            spatial["temporal_scope_ref"],
            spatial["uncertainty_ref"],
            lifecycle["validation_profile_ref"],
            lifecycle["evidence_requirements_ref"],
            lifecycle["correction_ref"],
            lifecycle["rollback_ref"],
            reviews["source_rights_review_ref"],
            reviews["sensitivity_review_ref"],
            reviews["geology_review_ref"],
            reviews["validation_review_ref"],
        ]
        if any(value is None for value in closure):
            findings.add(Finding("COMPLETE_ASSESSMENT_CLOSURE_REQUIRED"))
    return sorted(findings)


def _abstain_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    specification = candidate["specification"]
    source = candidate["source_bindings"]
    spatial = candidate["spatial_temporal"]
    assert isinstance(specification, Mapping)
    assert isinstance(source, Mapping)
    assert isinstance(spatial, Mapping)

    state = specification["assessment_state"]
    if state in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"ASSESSMENT_{state}"))
    if specification["parser_ref"] is None or specification["consumer_ref"] is None:
        findings.add(Finding("PARSER_OR_CONSUMER_UNRESOLVED"))
    if source["rights_state"] == "UNRESOLVED":
        findings.add(Finding("SOURCE_RIGHTS_UNRESOLVED"))
    if spatial["sensitivity_state"] == "UNRESOLVED":
        findings.add(Finding("SENSITIVITY_UNRESOLVED"))
    return sorted(findings)


def validate_candidate(candidate: Mapping[str, object]) -> Result:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("DENY", tuple(schema_findings))
    integrity = _integrity_findings(candidate)
    if integrity:
        return Result("DENY", tuple(integrity))
    specification = candidate["specification"]
    assert isinstance(specification, Mapping)
    if specification["assessment_state"] == "ERROR":
        return Result("ERROR", (Finding("GEOLOGY_PIPELINE_SPECIFICATION_ASSESSMENT_ERROR"),))
    coherence = _coherence_findings(candidate)
    if coherence:
        return Result("DENY", tuple(coherence))
    abstain = _abstain_findings(candidate)
    return Result("ABSTAIN", tuple(abstain)) if abstain else Result("PASS", ())


def _merge(base: object, overlay: object) -> object:
    if isinstance(base, dict) and isinstance(overlay, dict):
        merged = copy.deepcopy(base)
        for key, value in overlay.items():
            merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    return copy.deepcopy(overlay)


def _resolve_base(manifest: Mapping[str, object], name: str) -> dict[str, object]:
    bases = manifest["bases"]
    assert isinstance(bases, Mapping)
    raw = copy.deepcopy(bases[name])
    assert isinstance(raw, dict)
    parent = raw.pop("extends", None)
    if parent is None:
        return raw
    assert isinstance(parent, str)
    resolved = _merge(_resolve_base(manifest, parent), raw)
    assert isinstance(resolved, dict)
    return resolved


def _replace(document: object, pointer: str, value: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_fixture_case(manifest: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    candidate = _resolve_base(manifest, str(case["base"]))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    spec_hash, assessment_id = compute_identity(candidate)
    candidate["spec_hash"] = case.get("spec_hash_override", spec_hash)
    candidate["assessment_id"] = case.get("assessment_id_override", assessment_id)
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "outcome": "ERROR",
            "findings": [finding.code for finding in findings],
            "ok": False,
        }]
    results: list[dict[str, object]] = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_fixture_case(manifest, case))
        results.append({
            "name": case["name"],
            "outcome": result.outcome,
            "findings": result.codes,
            "ok": result.outcome == case["expected_outcome"] and result.codes == case["expected_findings"],
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    arguments = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(arguments)
    if args.fixtures:
        if arguments != ["--fixtures"]:
            parser.error("--fixtures must be used as the only argument")
        results = validate_fixture_manifest()
        for result in results:
            print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0 if all(result["ok"] for result in results) else 1
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = load_json_object(args.input)
    result = Result("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
    print(json.dumps({
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "outcome": result.outcome,
        "findings": result.codes,
    }, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
