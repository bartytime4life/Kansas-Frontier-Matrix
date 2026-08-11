#!/usr/bin/env python3
"""Validate fixture-only CountyYearPanel records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/data/county_year_panel.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/data/county_year_panel/cases.json"
PREFIX = "kfm:county-year-panel:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
OBSERVATION_KINDS = ["ACCESS", "AGRICULTURE", "ECONOMIC", "POPULATION"]
REQUIRED_LIMITS = {
    "AGGREGATE_ONLY",
    "NO_CROSSWALK_INFERENCE",
    "NO_FRONTIER_CLASSIFICATION",
    "NO_PUBLICATION_AUTHORITY",
    "OBSERVATIONS_REFERENCED_NOT_RESOLVED",
    "SOURCE_ROLES_PRESERVED",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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
            return None, (Finding("COUNTY_YEAR_PANEL_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("COUNTY_YEAR_PANEL_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("COUNTY_YEAR_PANEL_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("COUNTY_YEAR_PANEL_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("COUNTY_YEAR_PANEL_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("COUNTY_YEAR_PANEL_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("COUNTY_YEAR_PANEL_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("COUNTY_YEAR_PANEL_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("panel_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _expected_summary(observations: Sequence[Mapping[str, Any]]) -> tuple[str, str, list[str]]:
    available = sum(
        item["availability"] == "AVAILABLE"
        and item["geography_alignment"] != "UNRESOLVED"
        for item in observations
    )
    suppressed = any(item["availability"] == "SUPPRESSED" for item in observations)
    unresolved = any(item["geography_alignment"] == "UNRESOLVED" for item in observations)
    if available == len(OBSERVATION_KINDS):
        return "COMPLETE", "REVIEW_CANDIDATE", ["ALL_REQUIRED_OBSERVATIONS_AVAILABLE"]
    reasons = [
        "OBSERVATION_GAPS_PRESENT" if available else "NO_OBSERVATIONS_AVAILABLE"
    ]
    if suppressed:
        reasons.append("SUPPRESSED_OBSERVATION_PRESENT")
    if unresolved:
        reasons.append("UNRESOLVED_GEOGRAPHY_ALIGNMENT")
    return ("PARTIAL" if available else "INSUFFICIENT", "HOLD", sorted(reasons))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    panel_geography = value["panel_scope"]["geography_version_ref"]
    observations = value["observations"]
    summary = value["summary"]
    support = value["support"]
    disclosure = value["disclosure"]

    kinds = [item["observation_kind"] for item in observations]
    if set(kinds) != set(OBSERVATION_KINDS) or len(kinds) != len(set(kinds)):
        findings.add(
            Finding("COUNTY_YEAR_PANEL_OBSERVATION_KIND_SET_INVALID", "/observations")
        )
    elif kinds != OBSERVATION_KINDS:
        findings.add(Finding("COUNTY_YEAR_PANEL_OBSERVATION_ORDER_INVALID", "/observations"))

    indicators = [item["indicator_definition_ref"] for item in observations]
    if len(indicators) != len(set(indicators)):
        findings.add(Finding("COUNTY_YEAR_PANEL_INDICATOR_DUPLICATE", "/observations"))

    for index, item in enumerate(observations):
        path = f"/observations/{index}"
        evidence_refs = item["evidence_refs"]
        if evidence_refs != sorted(evidence_refs):
            findings.add(
                Finding("COUNTY_YEAR_PANEL_OBSERVATION_EVIDENCE_ORDER_INVALID", f"{path}/evidence_refs")
            )

        alignment = item["geography_alignment"]
        observation_geography = item["observation_geography_version_ref"]
        crosswalk_ref = item["geography_crosswalk_ref"]
        if alignment == "SAME_VERSION":
            if observation_geography != panel_geography or crosswalk_ref is not None:
                findings.add(
                    Finding("COUNTY_YEAR_PANEL_SAME_VERSION_ALIGNMENT_INVALID", path)
                )
        elif alignment == "CROSSWALK_REFERENCED":
            if observation_geography == panel_geography or crosswalk_ref is None:
                findings.add(
                    Finding("COUNTY_YEAR_PANEL_CROSSWALK_ALIGNMENT_INVALID", path)
                )
        else:
            if observation_geography == panel_geography or crosswalk_ref is not None:
                findings.add(
                    Finding("COUNTY_YEAR_PANEL_UNRESOLVED_ALIGNMENT_INVALID", path)
                )
            if item["availability"] == "AVAILABLE":
                findings.add(
                    Finding("COUNTY_YEAR_PANEL_UNRESOLVED_AVAILABLE_INVALID", path)
                )

        availability = item["availability"]
        observation_ref = item["observation_ref"]
        uncertainty_ref = item["uncertainty_ref"]
        reason = item["reason_code"]
        if availability == "AVAILABLE":
            if not (observation_ref and uncertainty_ref and evidence_refs and reason == "NONE"):
                findings.add(Finding("COUNTY_YEAR_PANEL_AVAILABLE_SHAPE_INVALID", path))
        elif availability == "MISSING":
            if not (
                observation_ref is None
                and uncertainty_ref is None
                and not evidence_refs
                and reason in {"SOURCE_MISSING", "GEOGRAPHY_ALIGNMENT_UNRESOLVED"}
            ):
                findings.add(Finding("COUNTY_YEAR_PANEL_MISSING_SHAPE_INVALID", path))
        elif availability == "SUPPRESSED":
            if not (
                observation_ref is None
                and uncertainty_ref is None
                and evidence_refs
                and reason == "POLICY_SUPPRESSED"
            ):
                findings.add(Finding("COUNTY_YEAR_PANEL_SUPPRESSED_SHAPE_INVALID", path))
        elif not (
            observation_ref is None
            and uncertainty_ref is None
            and not evidence_refs
            and reason == "OUT_OF_SCOPE"
        ):
            findings.add(Finding("COUNTY_YEAR_PANEL_NOT_APPLICABLE_SHAPE_INVALID", path))

    expected_state, expected_decision, expected_reasons = _expected_summary(observations)
    if summary["panel_state"] != expected_state:
        findings.add(
            Finding("COUNTY_YEAR_PANEL_SUMMARY_STATE_MISMATCH", "/summary/panel_state")
        )
    if summary["decision"] != expected_decision:
        findings.add(
            Finding("COUNTY_YEAR_PANEL_SUMMARY_DECISION_MISMATCH", "/summary/decision")
        )
    if summary["reason_codes"] != expected_reasons:
        findings.add(
            Finding("COUNTY_YEAR_PANEL_SUMMARY_REASON_MISMATCH", "/summary/reason_codes")
        )

    if support["panel_evidence_refs"] != sorted(support["panel_evidence_refs"]):
        findings.add(
            Finding("COUNTY_YEAR_PANEL_EVIDENCE_ORDER_INVALID", "/support/panel_evidence_refs")
        )
    if support["assumption_refs"] != sorted(support["assumption_refs"]):
        findings.add(
            Finding("COUNTY_YEAR_PANEL_ASSUMPTION_ORDER_INVALID", "/support/assumption_refs")
        )
    limits = disclosure["interpretation_limits"]
    if limits != sorted(limits):
        findings.add(
            Finding("COUNTY_YEAR_PANEL_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits")
        )
    if not REQUIRED_LIMITS.issubset(set(limits)):
        findings.add(
            Finding("COUNTY_YEAR_PANEL_REQUIRED_LIMIT_MISSING", "/disclosure/interpretation_limits")
        )

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("COUNTY_YEAR_PANEL_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("COUNTY_YEAR_PANEL_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["panel_id"] != identifier:
            findings.add(Finding("COUNTY_YEAR_PANEL_ID_MISMATCH", "/panel_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    return Result("DENY", semantic_findings) if semantic_findings else Result("PASS", ())


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in manifest["variants"][case["base"]]:
        _replace(document, mutation["path"], mutation.get("value"))
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["panel_id"] = case.get("panel_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_network",
                "no_observation_loading_or_value_computation",
                "no_geography_or_crosswalk_resolution",
                "no_evidence_resolution",
                "no_frontier_classification",
                "no_policy_or_review_approval",
                "no_promotion_or_release",
                "no_public_use_or_publication",
            ],
            "outcome": result.outcome,
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
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
