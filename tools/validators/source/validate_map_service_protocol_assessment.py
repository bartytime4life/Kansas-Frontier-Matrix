#!/usr/bin/env python3
"""Validate fixture-only, no-network map service protocol assessments."""

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

from hashing import CanonicalizationFailure, compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/source/map_service_protocol_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/map_service_protocol_assessment/cases.json"
PREFIX = "kfm:map-service-protocol:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
EXPECTED_LIMITATIONS = [
    "fixture_only",
    "no_network_or_remote_verification",
    "no_source_or_rights_authority",
    "no_cache_or_layer_mutation",
    "no_release_publication_or_public_use",
]
EXPECTED_SURFACE = {
    "PMTILES": "LOCAL_IMMUTABLE_ARTIFACT",
    "XYZ": "REMOTE_TILE_TEMPLATE",
    "WMTS": "REMOTE_CAPABILITIES_SERVICE",
    "WMS": "REMOTE_CAPABILITIES_SERVICE",
}
EXPECTED_EVIDENCE = {
    "PMTILES": "PMTILES_HEADER_ASSESSMENT",
    "XYZ": "XYZ_TEMPLATE_ASSESSMENT",
    "WMTS": "WMTS_CAPABILITIES_ASSESSMENT",
    "WMS": "WMS_CAPABILITIES_ASSESSMENT",
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
            raise DuplicateKeyError(key)
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
            return None, (Finding("MAP_PROTOCOL_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("MAP_PROTOCOL_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("MAP_PROTOCOL_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("MAP_PROTOCOL_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("MAP_PROTOCOL_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("MAP_PROTOCOL_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("MAP_PROTOCOL_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def _decision(outcome: str, recommendation: str, reason: str) -> dict[str, Any]:
    return {
        "outcome": outcome,
        "recommendation": recommendation,
        "reason_codes": [reason],
        "review_required": True,
        "execution_authorized": False,
    }


def _declaration_coherent(value: Mapping[str, Any]) -> bool:
    declaration = value["declaration"]
    controls = value["controls"]
    protocol = declaration["protocol_class"]
    digest = declaration["artifact_digest"]
    if protocol == "PMTILES":
        return (
            declaration["source_use_role"] == "VERSIONED_ARTIFACT"
            and declaration["immutable"] is True
            and digest is not None
            and set(digest.removeprefix("sha256:")) != {"0"}
            and controls["cache_policy"] in {"IMMUTABLE_VERSIONED", "UNKNOWN"}
            and controls["freshness_policy_ref"] is None
            and controls["source_health_ref"] is None
            and controls["source_health_state"] == "NOT_APPLICABLE"
        )
    return (
        declaration["source_use_role"] == "CONTEXT_ONLY"
        and declaration["immutable"] is False
        and digest is None
        and controls["cache_policy"] in {"REVALIDATE", "NO_STORE", "UNKNOWN"}
        and controls["freshness_policy_ref"] is not None
        and controls["source_health_ref"] is not None
        and controls["source_health_state"] != "NOT_APPLICABLE"
    )


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return _decision("ERROR", "VALIDATOR_ERROR", "VALIDATOR_ERROR")

    declaration = value["declaration"]
    controls = value["controls"]
    protocol = declaration["protocol_class"]
    if declaration["access_surface"] != EXPECTED_SURFACE[protocol]:
        return _decision("DENY", "REJECT", "PROTOCOL_TRANSPORT_MISMATCH")
    if declaration["protocol_evidence_kind"] != EXPECTED_EVIDENCE[protocol]:
        return _decision("DENY", "REJECT", "PROTOCOL_EVIDENCE_MISMATCH")
    if not _declaration_coherent(value):
        return _decision("DENY", "REJECT", "DECLARATION_INCOHERENT")
    if controls["attribution_required"] and controls["attribution_text"] is None:
        return _decision("DENY", "REJECT", "ATTRIBUTION_INCOMPLETE")
    if controls["rights_assessment_state"] == "BLOCKED":
        return _decision("DENY", "REJECT", "RIGHTS_BLOCKED")
    if controls["source_health_state"] in {"STALE", "UNAVAILABLE"}:
        return _decision("DENY", "REJECT", "SOURCE_STALE_OR_UNAVAILABLE")
    if controls["rights_assessment_state"] == "REVIEW_DUE":
        return _decision("ABSTAIN", "HOLD_FOR_REVIEW", "RIGHTS_REVIEW_DUE")
    if controls["rights_assessment_state"] == "UNRESOLVED":
        return _decision("ABSTAIN", "HOLD_FOR_REVIEW", "RIGHTS_UNRESOLVED")
    if controls["cache_policy"] == "UNKNOWN":
        return _decision("ABSTAIN", "HOLD_FOR_REVIEW", "CACHE_POLICY_UNRESOLVED")
    if controls["source_health_state"] == "UNKNOWN":
        return _decision("ABSTAIN", "HOLD_FOR_REVIEW", "SOURCE_HEALTH_UNRESOLVED")
    if controls["source_health_state"] == "DEGRADED":
        return _decision("ABSTAIN", "HOLD_FOR_REVIEW", "SOURCE_HEALTH_DEGRADED")
    return _decision("PASS", "READY_FOR_REVIEW", "PROTOCOL_CONTROLS_COHERENT")


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("MAP_PROTOCOL_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("MAP_PROTOCOL_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("MAP_PROTOCOL_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("MAP_PROTOCOL_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("MAP_PROTOCOL_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("MAP_PROTOCOL_ID_MISMATCH", "/assessment_id"))
    if value["source_descriptor_ref"] != f"kfm://source/{value['source_id']}":
        findings.add(
            Finding("MAP_PROTOCOL_SOURCE_REF_MISMATCH", "/source_descriptor_ref")
        )
    if value["limitations"] != EXPECTED_LIMITATIONS:
        findings.add(Finding("MAP_PROTOCOL_LIMITATIONS_INVALID", "/limitations"))
    if value["decision"] != recompute_decision(value):
        findings.add(Finding("MAP_PROTOCOL_DECISION_MISMATCH", "/decision"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    decision = recompute_decision(value)
    if decision["outcome"] == "PASS":
        return Result("PASS", ())
    return Result(
        decision["outcome"],
        tuple(
            Finding(code, "/decision/reason_codes")
            for code in decision["reason_codes"]
        ),
    )


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", findings)
    return validate_payload(value)


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]
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


def materialize_case(
    manifest: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["decision"] = copy.deepcopy(
        case.get("decision_override", recompute_decision(document))
    )
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["assessment_id"] = case.get("assessment_id_override", identifier)
    return document


def validate_fixture_manifest() -> list[dict[str, Any]]:
    manifest = load_fixtures()
    results: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        results.append(
            {
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_findings": case["expected_findings"],
                "actual_findings": actual,
                "ok": (
                    result.outcome == case["expected_outcome"]
                    and actual == case["expected_findings"]
                ),
            }
        )
    return results


def run_fixtures() -> int:
    results = validate_fixture_manifest()
    for result in results:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if all(result["ok"] for result in results) else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
            "file": path.as_posix() if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": [
                "no_network_or_remote_byte_verification",
                "no_source_activation_or_fetch",
                "no_rights_or_evidence_authority",
                "no_cache_or_layer_mutation",
                "no_release_publication_or_public_use",
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
    result = validate_file(args.input)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
