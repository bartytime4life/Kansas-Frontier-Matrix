#!/usr/bin/env python3
"""Validate additive ClaimEnvelope-to-CatalogMatrix non-overstatement closure.

PASS proves local, deterministic consistency only. It does not resolve evidence,
decide policy, authenticate review, release, publish, or authorize public use.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker
from referencing.exceptions import Unresolvable

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.validators._common.local_resolver import build_registry
from tools.validators import validate_catalog_matrix_closure as CATALOG_VALIDATOR
from tools.validators import validate_claim_envelope as CLAIM_VALIDATOR

SCHEMA = ROOT / "schemas/contracts/v1/data/catalog_matrix_claim_closure_profile.schema.json"
FIXTURES = ROOT / "fixtures/data/catalog_matrix/claim_closure"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_BYTES = 512 * 1024
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "MANIFEST_INVALID",
    "CLAIM_ENVELOPE_SCHEMA_UNAVAILABLE",
    "CATALOG_MATRIX_SCHEMA_UNAVAILABLE",
}
TERMINAL_DENIAL_STATES = {
    ("support_state", "DENIED"),
    ("policy_state", "DENY"),
    ("review_state", "REJECTED"),
    ("review_state", "SUPERSEDED"),
    ("release_state", "WITHDRAWN"),
    ("release_state", "SUPERSEDED"),
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(finding.code in ERROR_CODES for finding in self.findings)

    @property
    def outcome(self) -> str:
        return "PASS" if self.ok else ("ERROR" if self.error else "FAIL")


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _constant(_value: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    fd: int | None = None
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/", "symbolic links are denied")]
        fd = os.open(
            path,
            os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0),
        )
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            return None, [Finding("FILE_NOT_FOUND", "/", "input is not a regular file")]
        if info.st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds 512 KiB")]
        with os.fdopen(fd, "rb") as stream:
            fd = None
            raw = stream.read(MAX_BYTES + 1)
        value = json.loads(
            raw.decode(),
            object_pairs_hook=_pairs,
            parse_constant=_constant,
            parse_float=_float,
        )
    except FileNotFoundError:
        return None, [Finding("FILE_NOT_FOUND", "/", "input file was not found")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate members are denied")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/", "numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/", "input is not valid JSON")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("FILE_READ_ERROR", "/", "input could not be read safely")]
    finally:
        if fd is not None:
            os.close(fd)
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/", "JSON root must be an object")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, object]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            registry=build_registry(ROOT),
            format_checker=FormatChecker(),
        )
        errors = sorted(
            validator.iter_errors(value),
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError, Unresolvable):
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema graph could not be loaded safely")]
    return [
        Finding(
            "SCHEMA_INVALID",
            _pointer(error.absolute_path),
            f"schema constraint failed: {error.validator}",
        )
        for error in errors[:50]
    ]


def _prefixed_findings(prefix: str, code_prefix: str, findings: Iterable[object]) -> list[Finding]:
    output: list[Finding] = []
    for finding in findings:
        field = getattr(finding, "field", "/")
        joined = prefix if field == "/" else prefix + field
        output.append(
            Finding(
                f"{code_prefix}_{getattr(finding, 'code', 'INVALID')}",
                joined,
                f"embedded {code_prefix.lower().replace('_', ' ')} validation failed",
            )
        )
    return output


def _integration_findings(value: Mapping[str, object]) -> list[Finding]:
    claim = value["claim_envelope"]
    catalog = value["catalog_matrix_closure"]
    assert isinstance(claim, dict)
    assert isinstance(catalog, dict)

    findings: list[Finding] = []

    claim_evidence = set(claim["evidence_refs"])
    catalog_evidence = set(catalog["evidence_refs"])
    if not catalog_evidence.issubset(claim_evidence):
        findings.append(
            Finding(
                "CATALOG_EVIDENCE_REFS_OVERSTATE_CLAIM",
                "/catalog_matrix_closure/evidence_refs",
                "catalog evidence references must be a subset of claim evidence references",
            )
        )

    claim_sources = set(claim["source_refs"])
    catalog_sources = set(catalog["source_refs"])
    if not catalog_sources.issubset(claim_sources):
        findings.append(
            Finding(
                "CATALOG_SOURCE_REFS_OVERSTATE_CLAIM",
                "/catalog_matrix_closure/source_refs",
                "catalog source references must be a subset of claim source references",
            )
        )

    artifact = catalog["artifact"]
    assert isinstance(artifact, dict)
    if artifact["release_ref"] != claim["release_ref"]:
        findings.append(
            Finding(
                "CATALOG_RELEASE_REF_OVERSTATES_CLAIM",
                "/catalog_matrix_closure/artifact/release_ref",
                "catalog and claim release references must match",
            )
        )
    if catalog["correction_path_ref"] != claim["correction_path_ref"]:
        findings.append(
            Finding(
                "CATALOG_CORRECTION_REF_OVERSTATES_CLAIM",
                "/catalog_matrix_closure/correction_path_ref",
                "catalog and claim correction references must match",
            )
        )
    if catalog["rollback_ref"] != claim["rollback_ref"]:
        findings.append(
            Finding(
                "CATALOG_ROLLBACK_REF_OVERSTATES_CLAIM",
                "/catalog_matrix_closure/rollback_ref",
                "catalog and claim rollback references must match",
            )
        )

    if catalog["decision"] == "READY":
        ready_rules = [
            (claim["support_state"] != "SUPPORTED", "CATALOG_READY_SUPPORT_OVERSTATEMENT", "/claim_envelope/support_state"),
            (claim["policy_state"] != "ALLOW", "CATALOG_READY_POLICY_OVERSTATEMENT", "/claim_envelope/policy_state"),
            (claim["review_state"] != "APPROVED", "CATALOG_READY_REVIEW_OVERSTATEMENT", "/claim_envelope/review_state"),
            (claim["release_state"] not in {"CANDIDATE", "PUBLISHED"}, "CATALOG_READY_RELEASE_OVERSTATEMENT", "/claim_envelope/release_state"),
        ]
        findings.extend(
            Finding(code, field, "catalog READY would strengthen claim posture")
            for failed, code, field in ready_rules
            if failed
        )

    terminal_denial = any(claim[field] == state for field, state in TERMINAL_DENIAL_STATES)
    if terminal_denial and catalog["decision"] != "DENY":
        findings.append(
            Finding(
                "CATALOG_DECISION_UNDERSTATES_CLAIM_DENIAL",
                "/catalog_matrix_closure/decision",
                "terminal negative claim posture requires catalog DENY",
            )
        )

    if value["catalog_publication_state"] == "PUBLISHED" and not (
        claim["release_state"] == "PUBLISHED" and catalog["decision"] == "READY"
    ):
        findings.append(
            Finding(
                "CATALOG_PUBLICATION_OVERSTATEMENT",
                "/catalog_publication_state",
                "catalog publication projection exceeds claim or catalog posture",
            )
        )

    return sorted(set(findings))


def validate_value(value: Mapping[str, object]) -> ValidationResult:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return ValidationResult(tuple(sorted(set(schema_findings))))

    claim = value["claim_envelope"]
    catalog = value["catalog_matrix_closure"]
    assert isinstance(claim, dict)
    assert isinstance(catalog, dict)

    claim_result = CLAIM_VALIDATOR.validate_value(claim)
    catalog_result = CATALOG_VALIDATOR.validate_value(catalog)
    embedded = _prefixed_findings(
        "/claim_envelope", "CLAIM_ENVELOPE", claim_result.findings
    ) + _prefixed_findings(
        "/catalog_matrix_closure", "CATALOG_MATRIX", catalog_result.findings
    )
    if embedded:
        return ValidationResult(tuple(sorted(set(embedded))))

    return ValidationResult(tuple(_integration_findings(value)))


def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None:
        return ValidationResult(tuple(findings))
    return validate_value(value)


def run_fixtures() -> int:
    manifest, findings = _read(MANIFEST)
    if manifest is None or findings or not isinstance(manifest.get("cases"), list):
        print("CATALOG_MATRIX_CLAIM_CLOSURE_FIXTURES_ERROR code=MANIFEST_INVALID")
        return 2

    failures: list[str] = []
    cases = manifest["cases"]
    for case in cases:
        result = validate(FIXTURES / case["path"])
        actual = sorted({finding.code for finding in result.findings})
        if (
            result.outcome != case["expected_outcome"]
            or actual != sorted(case["expected_findings"])
        ):
            failures.append(case["case_id"])
        print(
            "CATALOG_MATRIX_CLAIM_CLOSURE_FIXTURE "
            f"case={case['case_id']} outcome={result.outcome} "
            f"findings={','.join(actual) if actual else '-'}"
        )

    if failures:
        for case_id in failures:
            print(f"CATALOG_MATRIX_CLAIM_CLOSURE_FIXTURE_MISMATCH case={case_id}")
        return 1

    print(
        "CATALOG_MATRIX_CLAIM_CLOSURE_FIXTURES_VALID "
        f"cases={len(cases)} no_network=true authority=local-non-overstatement-only"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        return run_fixtures()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")

    result = validate(args.path)
    for finding in result.findings:
        print(
            f"CATALOG_MATRIX_CLAIM_CLOSURE_{result.outcome} "
            f"code={finding.code} field={finding.field} detail={finding.detail}"
        )
    if result.ok:
        print(
            "CATALOG_MATRIX_CLAIM_CLOSURE_PASS "
            f"path={args.path} authority=local-non-overstatement-only"
        )
        return 0
    return 2 if result.error else 1


if __name__ == "__main__":
    raise SystemExit(main())
