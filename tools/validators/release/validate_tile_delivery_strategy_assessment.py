#!/usr/bin/env python3
"""Validate fixture-only, no-network tile delivery strategy assessments."""

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

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/release/"
    "tile_delivery_strategy_assessment.schema.json"
)
FIXTURES = (
    ROOT
    / "fixtures/contracts/v1/release/"
    "tile_delivery_strategy_assessment/cases.json"
)
PREFIX = "kfm:tile-delivery-strategy:"
MAX_BYTES = 2 * 1024 * 1024
MAX_FINDINGS = 100
EXPECTED_LIMITATIONS = [
    "fixture_only",
    "no_network_artifact_service_or_database_verification",
    "no_rights_sensitivity_policy_or_review_authority",
    "no_hosting_cache_release_or_deployment_effect",
    "no_publication_or_public_use",
]


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
            return None, (Finding("TILE_STRATEGY_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("TILE_STRATEGY_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("TILE_STRATEGY_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("TILE_STRATEGY_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("TILE_STRATEGY_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("TILE_STRATEGY_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("TILE_STRATEGY_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def _assessment(
    outcome: str,
    recommended_strategy: str | None,
    reason: str,
) -> dict[str, Any]:
    return {
        "outcome": outcome,
        "recommended_strategy": recommended_strategy,
        "reason_codes": [reason],
        "review_required": True,
        "execution_authorized": False,
    }


def recommend_strategy(value: Mapping[str, Any]) -> str | None:
    declaration = value["declaration"]
    if declaration["audience"] == "LOCAL" and declaration["offline_required"]:
        return "MBTILES_LOCAL"
    if (
        declaration["update_pattern"] == "DYNAMIC_QUERY"
        or declaration["server_mediation_required"]
        or declaration["postgis_slicing_required"]
        or declaration["access_control_required"]
    ):
        return "MARTIN_POSTGIS"
    if (
        declaration["update_pattern"] == "PARTIAL_MUTATION"
        or declaration["per_tile_invalidation_required"]
    ):
        return "XYZ_SERVICE"
    if (
        declaration["update_pattern"]
        in {"IMMUTABLE_SNAPSHOT", "APPEND_ONLY_VERSIONED"}
        and declaration["immutable_versioned_artifact"]
        and declaration["range_hosting_ready"]
    ):
        return "PMTILES_ARCHIVE"
    return None


def recompute_assessment(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return _assessment("ERROR", None, "VALIDATOR_ERROR")

    declaration = value["declaration"]
    controls = value["controls"]
    selected = declaration["selected_strategy"]
    recommended = recommend_strategy(value)

    if declaration["audience"] == "PUBLIC" and not declaration["public_safe_input"]:
        return _assessment("DENY", recommended, "PUBLIC_UNSAFE_INPUT_DENIED")
    if selected == "MBTILES_LOCAL" and declaration["audience"] == "PUBLIC":
        return _assessment(
            "DENY", recommended, "MBTILES_PUBLIC_DELIVERY_DENIED"
        )
    if (
        declaration["audience"] == "PUBLIC"
        and declaration["access_control_required"]
    ):
        return _assessment(
            "DENY", recommended, "PUBLIC_ACCESS_CONTROL_CONFLICT"
        )
    if selected in {"PMTILES_ARCHIVE", "XYZ_SERVICE"} and (
        declaration["server_mediation_required"]
        or declaration["postgis_slicing_required"]
        or declaration["access_control_required"]
    ):
        return _assessment(
            "DENY", recommended, "STATIC_DELIVERY_BYPASSES_MEDIATION"
        )

    if selected == "PMTILES_ARCHIVE":
        if controls["tile_artifact_manifest_ref"] is None:
            return _assessment(
                "HOLD", recommended, "TILE_ARTIFACT_MANIFEST_REQUIRED"
            )
        if controls["cache_policy_ref"] is None:
            return _assessment("HOLD", recommended, "CACHE_POLICY_REF_REQUIRED")
        if not declaration["range_hosting_ready"]:
            return _assessment(
                "HOLD", recommended, "PMTILES_RANGE_HOSTING_UNREADY"
            )
        if (
            not declaration["immutable_versioned_artifact"]
            or declaration["update_pattern"]
            not in {"IMMUTABLE_SNAPSHOT", "APPEND_ONLY_VERSIONED"}
            or declaration["per_tile_invalidation_required"]
            or declaration["offline_required"]
        ):
            return _assessment(
                "HOLD", recommended, "PMTILES_IMMUTABILITY_REQUIRED"
            )

    if selected == "XYZ_SERVICE":
        if controls["map_service_protocol_assessment_ref"] is None:
            return _assessment(
                "HOLD", recommended, "SERVICE_PROTOCOL_ASSESSMENT_REQUIRED"
            )
        if controls["cache_policy_ref"] is None:
            return _assessment("HOLD", recommended, "CACHE_POLICY_REF_REQUIRED")
        if (
            declaration["update_pattern"] != "PARTIAL_MUTATION"
            or not declaration["per_tile_invalidation_required"]
        ):
            return _assessment(
                "HOLD", recommended, "XYZ_INVALIDATION_REQUIREMENT_MISSING"
            )

    if selected == "MARTIN_POSTGIS":
        if controls["map_service_protocol_assessment_ref"] is None:
            return _assessment(
                "HOLD", recommended, "SERVICE_PROTOCOL_ASSESSMENT_REQUIRED"
            )
        if not (
            declaration["update_pattern"] == "DYNAMIC_QUERY"
            or declaration["server_mediation_required"]
            or declaration["postgis_slicing_required"]
            or declaration["access_control_required"]
        ):
            return _assessment(
                "HOLD", recommended, "MARTIN_MEDIATION_NEED_REQUIRED"
            )

    if selected == "MBTILES_LOCAL":
        if (
            declaration["audience"] != "LOCAL"
            or not declaration["offline_required"]
        ):
            return _assessment(
                "HOLD", recommended, "MBTILES_LOCAL_REQUIREMENTS_MISSING"
            )
        if controls["tile_artifact_manifest_ref"] is None:
            return _assessment(
                "HOLD", recommended, "TILE_ARTIFACT_MANIFEST_REQUIRED"
            )

    if recommended is None:
        return _assessment("HOLD", None, "STRATEGY_UNRESOLVED")
    if selected != recommended:
        return _assessment("HOLD", recommended, "STRATEGY_MISMATCH")
    return _assessment("PASS", recommended, "STRATEGY_COHERENT")


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
        return (Finding("TILE_STRATEGY_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("TILE_STRATEGY_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("TILE_STRATEGY_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("TILE_STRATEGY_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(
                Finding("TILE_STRATEGY_SPEC_HASH_MISMATCH", "/spec_hash")
            )
        if value["assessment_id"] != expected_id:
            findings.add(Finding("TILE_STRATEGY_ID_MISMATCH", "/assessment_id"))
    if value["limitations"] != EXPECTED_LIMITATIONS:
        findings.add(
            Finding("TILE_STRATEGY_LIMITATIONS_INVALID", "/limitations")
        )
    if value["assessment"] != recompute_assessment(value):
        findings.add(
            Finding("TILE_STRATEGY_ASSESSMENT_MISMATCH", "/assessment")
        )
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    assessment = recompute_assessment(value)
    if assessment["outcome"] == "PASS":
        return Result("PASS", ())
    return Result(
        assessment["outcome"],
        (
            Finding(
                assessment["reason_codes"][0],
                "/assessment/reason_codes",
            ),
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
    manifest: Mapping[str, Any],
    case: Mapping[str, Any],
) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["assessment"] = copy.deepcopy(
        case.get("assessment_override", recompute_assessment(document))
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
            "file": str(path) if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "profile": "kfm.release.tile-delivery-strategy.fixture.v1",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate inactive tile delivery strategy assessments."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with file arguments")
        return run_fixtures()
    if not args.files:
        print(serialize(None, Result("ERROR", (Finding("NO_INPUT", "/"),))))
        return 2

    failed = False
    for path in sorted(args.files, key=lambda item: str(item)):
        result = validate_file(path)
        print(serialize(path, result))
        failed = failed or result.outcome != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
