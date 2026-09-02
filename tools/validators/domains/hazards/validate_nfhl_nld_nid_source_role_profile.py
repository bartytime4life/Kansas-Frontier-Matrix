#!/usr/bin/env python3
"""Validate the fixture-only FEMA NFHL / USACE NLD / NID source-role profile."""
from __future__ import annotations

import argparse
import copy
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

SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/domains/hazards/"
    "nfhl_nld_nid_source_role_profile.schema.json"
)
FIXTURE_PATH = (
    ROOT
    / "fixtures/contracts/v1/domains/hazards/"
    "nfhl_nld_nid_source_role_profile/cases.json"
)
PROFILE = "kfm.hazards.nfhl-nld-nid-source-role-profile.v1"
ASSESSMENT_PREFIX = "kfm:hazards:nfhl-nld-nid:"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100

EXPECTED_SOURCES: dict[str, tuple[str, str, str, str, str]] = {
    "nfhl": (
        "NFHL",
        "FEMA_NFHL",
        "REGULATORY_FLOOD_HAZARD_BASELINE",
        "kfm://source/fema/nfhl",
        "PUBLIC_REGULATORY_GEOMETRY",
    ),
    "nld": (
        "NLD",
        "USACE_NLD",
        "LEVEE_INVENTORY_REFERENCE",
        "kfm://source/usace/nld",
        "GENERALIZED_LINEAR_REFERENCE",
    ),
    "nid": (
        "NID",
        "USACE_NID",
        "DAM_INVENTORY_REFERENCE",
        "kfm://source/usace/nid",
        "GENERALIZED_POINT_REFERENCE",
    ),
}


class DuplicateKeyError(ValueError):
    """Raised when JSON contains a duplicate object key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or an infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


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


def _reject_constant(_value: str) -> None:
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
            parse_constant=_reject_constant,
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
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
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
        Finding(
            "HAZARD_SOURCE_ROLE_SCHEMA_INVALID",
            _pointer(error.absolute_path),
        )
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _identity_payload(value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: copy.deepcopy(value[key])
        for key in (
            "profile",
            "status",
            "execution_mode",
            "sources",
            "relations",
            "claims",
        )
        if key in value
    }


def _semantic_findings(
    value: Mapping[str, Any],
) -> tuple[list[Finding], list[Finding]]:
    deny: list[Finding] = []
    abstain: list[Finding] = []

    expected_hash = compute_spec_hash(_identity_payload(value))
    if value.get("spec_hash") != expected_hash:
        deny.append(
            Finding(
                "HAZARD_SOURCE_ROLE_SPEC_HASH_MISMATCH",
                "/spec_hash",
            )
        )
    if value.get("assessment_id") != ASSESSMENT_PREFIX + expected_hash:
        deny.append(
            Finding(
                "HAZARD_SOURCE_ROLE_ASSESSMENT_ID_MISMATCH",
                "/assessment_id",
            )
        )

    sources = value.get("sources")
    all_evidence: set[str] = set()
    native_hashes: list[str] = []
    if isinstance(sources, Mapping):
        for lane, expected in EXPECTED_SOURCES.items():
            source = sources.get(lane)
            if not isinstance(source, Mapping):
                continue

            actual = (
                source.get("source_key"),
                source.get("source_family"),
                source.get("source_role"),
                source.get("source_descriptor_ref"),
                (
                    source.get("public_geometry", {}).get("precision_class")
                    if isinstance(source.get("public_geometry"), Mapping)
                    else None
                ),
            )
            if actual != expected:
                deny.append(
                    Finding(
                        "HAZARD_SOURCE_ROLE_COLLAPSE",
                        f"/sources/{lane}/source_role",
                    )
                )

            native_hash = source.get("native_identity_hash")
            if isinstance(native_hash, str):
                native_hashes.append(native_hash)

            evidence_refs = source.get("evidence_refs")
            if isinstance(evidence_refs, list):
                if evidence_refs != sorted(set(evidence_refs)):
                    deny.append(
                        Finding(
                            "HAZARD_SOURCE_EVIDENCE_REFS_NOT_CANONICAL",
                            f"/sources/{lane}/evidence_refs",
                        )
                    )
                all_evidence.update(
                    item for item in evidence_refs if isinstance(item, str)
                )

            state = source.get("data_state")
            source_key = expected[0]
            if state == "NO_DATA":
                abstain.append(
                    Finding(
                        f"{source_key}_NO_DATA",
                        f"/sources/{lane}/data_state",
                    )
                )
            elif state in {"POPULATED", "EMPTY"} and evidence_refs == []:
                abstain.append(
                    Finding(
                        f"{source_key}_EVIDENCE_UNRESOLVED",
                        f"/sources/{lane}/evidence_refs",
                    )
                )

            time_value = source.get("time")
            if isinstance(time_value, Mapping):
                effective = _parse_time(time_value.get("source_effective_at"))
                updated = _parse_time(time_value.get("source_updated_at"))
                retrieved = _parse_time(time_value.get("retrieved_at"))
                if (
                    effective is None
                    or updated is None
                    or retrieved is None
                    or not (effective <= updated <= retrieved)
                ):
                    deny.append(
                        Finding(
                            "HAZARD_SOURCE_TIME_ORDER_INVALID",
                            f"/sources/{lane}/time",
                        )
                    )

            geometry = source.get("public_geometry")
            if isinstance(geometry, Mapping):
                if geometry.get("exact_operational_detail_present") is not False:
                    deny.append(
                        Finding(
                            "HAZARD_OPERATIONAL_DETAIL_DENIED",
                            f"/sources/{lane}/public_geometry/"
                            "exact_operational_detail_present",
                        )
                    )
                if geometry.get("restricted_attribute_present") is not False:
                    deny.append(
                        Finding(
                            "HAZARD_RESTRICTED_ATTRIBUTE_DENIED",
                            f"/sources/{lane}/public_geometry/"
                            "restricted_attribute_present",
                        )
                    )

                transform_ref = geometry.get("public_safe_transform_ref")
                if lane == "nfhl" and transform_ref is not None:
                    deny.append(
                        Finding(
                            "NFHL_TRANSFORM_REF_UNEXPECTED",
                            f"/sources/{lane}/public_geometry/"
                            "public_safe_transform_ref",
                        )
                    )
                if lane in {"nld", "nid"} and state == "POPULATED":
                    if not isinstance(transform_ref, str):
                        deny.append(
                            Finding(
                                "INFRASTRUCTURE_GENERALIZATION_REQUIRED",
                                f"/sources/{lane}/public_geometry/"
                                "public_safe_transform_ref",
                            )
                        )

    if len(native_hashes) != len(set(native_hashes)):
        deny.append(
            Finding(
                "HAZARD_NATIVE_IDENTITY_COLLISION",
                "/sources",
            )
        )

    relations = value.get("relations")
    relation_ids: list[str] = []
    if isinstance(relations, list):
        for index, relation in enumerate(relations):
            if not isinstance(relation, Mapping):
                continue
            relation_id = relation.get("relation_id")
            if isinstance(relation_id, str):
                relation_ids.append(relation_id)
            if relation.get("from_source") == relation.get("to_source"):
                deny.append(
                    Finding(
                        "HAZARD_SELF_RELATION_DENIED",
                        f"/relations/{index}",
                    )
                )
            refs = relation.get("evidence_refs")
            if isinstance(refs, list):
                if refs != sorted(set(refs)):
                    deny.append(
                        Finding(
                            "HAZARD_RELATION_EVIDENCE_NOT_CANONICAL",
                            f"/relations/{index}/evidence_refs",
                        )
                    )
                if not set(
                    item for item in refs if isinstance(item, str)
                ).issubset(all_evidence):
                    abstain.append(
                        Finding(
                            "HAZARD_RELATION_EVIDENCE_UNRESOLVED",
                            f"/relations/{index}/evidence_refs",
                        )
                    )
        if relation_ids != sorted(set(relation_ids)):
            deny.append(
                Finding(
                    "HAZARD_RELATIONS_NOT_CANONICAL",
                    "/relations",
                )
            )

    claims = value.get("claims")
    if isinstance(claims, Mapping):
        claim_codes = {
            "observed_flood_extent_claimed":
                "NFHL_OBSERVED_FLOOD_COLLAPSE_DENIED",
            "forecast_or_current_inundation_claimed":
                "NFHL_FORECAST_COLLAPSE_DENIED",
            "levee_operational_condition_claimed":
                "NLD_OPERATIONAL_CONDITION_DENIED",
            "dam_operational_condition_claimed":
                "NID_OPERATIONAL_CONDITION_DENIED",
            "engineering_safety_claimed":
                "HAZARD_ENGINEERING_SAFETY_CLAIM_DENIED",
        }
        for key, code in claim_codes.items():
            if claims.get(key) is not False:
                deny.append(Finding(code, f"/claims/{key}"))
        authority_keys = (
            "source_admission_authorized",
            "evidence_resolved",
            "policy_approved",
            "promotion_authorized",
            "release_authorized",
            "publication_authorized",
        )
        if any(claims.get(key) is not False for key in authority_keys):
            deny.append(
                Finding(
                    "HAZARD_SOURCE_ROLE_AUTHORITY_OVERREACH",
                    "/claims",
                )
            )

    return sorted(set(deny)), sorted(set(abstain))


def validate_document(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", tuple(sorted(set(schema_findings))))
    deny, abstain = _semantic_findings(value)
    if deny:
        return Result("DENY", tuple(deny))
    if abstain:
        return Result("ABSTAIN", tuple(abstain))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, operational_findings = _read(path)
    if value is None:
        return Result("ERROR", tuple(sorted(set(operational_findings))))
    return validate_document(value)


def load_fixture_cases() -> tuple[list[dict[str, Any]], list[Finding]]:
    value, findings = _read(FIXTURE_PATH)
    if value is None:
        return [], findings
    bases = value.get("bases")
    cases = value.get("cases")
    if not isinstance(bases, dict) or not isinstance(cases, list):
        return [], [Finding("FIXTURE_MANIFEST_INVALID", "/")]
    materialized: list[dict[str, Any]] = []
    try:
        for case in cases:
            if not isinstance(case, dict):
                raise ValueError
            base_id = case.get("base")
            if not isinstance(base_id, str) or not isinstance(bases.get(base_id), dict):
                raise ValueError
            document = copy.deepcopy(bases[base_id])
            base_hash = compute_spec_hash(_identity_payload(document))
            mutations = case.get("mutations", [])
            if not isinstance(mutations, list):
                raise ValueError
            for mutation in mutations:
                if not isinstance(mutation, dict):
                    raise ValueError
                _apply_mutation(document, mutation)
            selected_hash = (
                base_hash
                if case.get("preserve_identity") is True
                else compute_spec_hash(_identity_payload(document))
            )
            document["spec_hash"] = selected_hash
            document["assessment_id"] = ASSESSMENT_PREFIX + selected_hash
            materialized.append({**case, "document": document})
    except (KeyError, TypeError, ValueError):
        return [], [Finding("FIXTURE_MANIFEST_INVALID", "/")]
    return materialized, []


def _parts(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        raise ValueError
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.split("/")[1:]
    ]


def _apply_mutation(document: dict[str, Any], mutation: Mapping[str, Any]) -> None:
    op = mutation.get("op")
    pointer = mutation.get("path")
    if op not in {"replace", "remove"} or not isinstance(pointer, str):
        raise ValueError
    parts = _parts(pointer)
    if not parts:
        raise ValueError
    cursor: Any = document
    for part in parts[:-1]:
        if isinstance(cursor, list):
            cursor = cursor[int(part)]
        elif isinstance(cursor, dict):
            cursor = cursor[part]
        else:
            raise ValueError
    last = parts[-1]
    if isinstance(cursor, list):
        index = int(last)
        if op == "replace":
            cursor[index] = copy.deepcopy(mutation.get("value"))
        else:
            del cursor[index]
    elif isinstance(cursor, dict):
        if op == "replace":
            if last not in cursor:
                raise ValueError
            cursor[last] = copy.deepcopy(mutation.get("value"))
        else:
            del cursor[last]
    else:
        raise ValueError


def run_fixture_suite() -> tuple[bool, dict[str, Any]]:
    cases, findings = load_fixture_cases()
    if findings:
        return False, {
            "outcome": "ERROR",
            "findings": [
                {"code": item.code, "path": item.path}
                for item in findings
            ],
        }

    counts = {"PASS": 0, "ABSTAIN": 0, "DENY": 0, "ERROR": 0}
    results: list[dict[str, Any]] = []
    ok = True
    for case in cases:
        result = validate_document(case["document"])
        actual = [
            {"code": item.code, "path": item.path}
            for item in result.findings
        ]
        expected = case.get("expected_findings")
        matched = (
            result.outcome == case.get("expected_outcome")
            and actual == expected
        )
        counts[result.outcome] += 1
        ok = ok and matched
        results.append(
            {
                "case_id": case["case_id"],
                "outcome": result.outcome,
                "findings": actual,
                "suite_match": matched,
            }
        )
    return ok, {
        "outcome": "PASS" if ok else "ERROR",
        "cases": len(cases),
        "counts": counts,
        "authority": "NONE",
        "non_effects": [
            "no_live_source_access",
            "no_raw_or_lifecycle_write",
            "no_source_admission_or_evidence_resolution",
            "no_policy_review_promotion_release_or_publication",
        ],
        "results": results,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 2

    exit_code = 0
    for path in args.files:
        result = validate_file(path)
        print(
            json.dumps(
                {
                    "file": path.as_posix(),
                    "outcome": result.outcome,
                    "findings": [
                        {"code": item.code, "path": item.path}
                        for item in result.findings
                    ],
                    "scope": PROFILE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        if result.outcome == "ERROR":
            exit_code = max(exit_code, 2)
        elif result.outcome == "ABSTAIN":
            exit_code = max(exit_code, 3)
        elif result.outcome == "DENY":
            exit_code = max(exit_code, 1)
    if not args.files:
        parser.error("provide at least one file or use --fixtures")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
