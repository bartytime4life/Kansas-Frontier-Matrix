#!/usr/bin/env python3
"""Validate fixture-only STAC/DCAT/PROV distribution mapping candidates.

PASS proves bounded local carrier alignment only. The validator does not read
the network, emit catalogs, activate OCI/ORAS, resolve evidence, decide policy,
approve review, authorize release, publish, or authorize public use.
"""
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

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/data/catalog_distribution_mapping_profile.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/data/catalog_distribution_mapping_profile/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:catalog-distribution-mapping:"


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
    outcome: str
    profile_state: str | None
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


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("CATALOG_MAPPING_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("CATALOG_MAPPING_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("CATALOG_MAPPING_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("CATALOG_MAPPING_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("CATALOG_MAPPING_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("CATALOG_MAPPING_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("CATALOG_MAPPING_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("CATALOG_MAPPING_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"candidate_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def expected_alignment(value: Mapping[str, Any]) -> dict[str, Any]:
    artifact = value["artifact"]
    carriers = value["carriers"]
    stac = carriers["stac"]
    dcat = carriers["dcat"]
    prov = carriers["prov"]
    return {
        "locator_match": all(
            candidate == artifact["locator"]
            for candidate in (stac["href"], dcat["access_url"], prov["location"])
        ),
        "digest_match": all(
            candidate == artifact["digest"]
            for candidate in (stac["checksum"], dcat["checksum"], prov["checksum"])
        ),
        "media_type_match": all(
            candidate == artifact["media_type"]
            for candidate in (stac["media_type"], dcat["media_type"], prov["media_type"])
        ),
        "role_match": (
            stac["roles"] == [artifact["asset_role"]]
            and dcat["role"] == artifact["asset_role"]
            and prov["role"] == artifact["asset_role"]
        ),
        "locator_digest_bound": artifact["locator"].endswith("@" + artifact["digest"]),
        "prov_generation_bound": prov["generated_entity_ref"] == prov["entity_ref"],
        "profile_state": "REVIEW_REQUIRED",
        "catalog_records_emitted": False,
        "publication_authorized": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("CATALOG_MAPPING_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("CATALOG_MAPPING_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("CATALOG_MAPPING_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    expected = expected_alignment(value)
    if value["alignment"] != expected:
        findings.add(Finding("CATALOG_MAPPING_ALIGNMENT_SUMMARY_MISMATCH", "/alignment"))
    if not expected["locator_match"]:
        findings.add(Finding("CATALOG_MAPPING_LOCATOR_MISMATCH", "/carriers"))
    if not expected["digest_match"]:
        findings.add(Finding("CATALOG_MAPPING_DIGEST_MISMATCH", "/carriers"))
    if not expected["media_type_match"]:
        findings.add(Finding("CATALOG_MAPPING_MEDIA_TYPE_MISMATCH", "/carriers"))
    if not expected["role_match"]:
        findings.add(Finding("CATALOG_MAPPING_ROLE_MISMATCH", "/carriers"))
    if not expected["locator_digest_bound"]:
        findings.add(
            Finding("CATALOG_MAPPING_DIGEST_URI_MISMATCH", "/artifact/locator")
        )
    if not expected["prov_generation_bound"]:
        findings.add(
            Finding(
                "CATALOG_MAPPING_PROV_GENERATION_MISMATCH",
                "/carriers/prov/generated_entity_ref",
            )
        )
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)

    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("CATALOG_MAPPING_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("CATALOG_MAPPING_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["candidate_id"] != expected_id:
            findings.add(Finding("CATALOG_MAPPING_ID_MISMATCH", "/candidate_id"))

    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if not case.get("preserve_alignment", False):
        document["alignment"] = expected_alignment(document)
    document["spec_hash"], document["candidate_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "candidate_id_override" in case:
        document["candidate_id"] = case["candidate_id_override"]
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.profile_state != case["expected_profile_state"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_profile_state": case["expected_profile_state"],
                    "actual_profile_state": result.profile_state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "writes_catalogs": False,
                "activates_oci_or_oras": False,
                "resolves_evidence": False,
                "decides_policy": False,
                "approves_review": False,
                "authorizes_release": False,
                "publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "path": item.path} for item in result.findings
            ],
            "outcome": result.outcome,
            "profile_state": result.profile_state,
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
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
