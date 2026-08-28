"""Validate fixture-only environmental-indicator EvidenceBundle profiles.

The profile binds a derived environmental indicator to the repository's existing
EvidenceBundle contract. A PASS proves only local schema shape, deterministic
identity, internal reference closure, and the explicit no-authority boundary for
synthetic fixtures. It performs no network access, source activation, evidence
resolution, policy evaluation, lifecycle write, release, publication, or public
use.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing.exceptions import Unresolvable

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import (
    JsonInputError,
    load_json_file,
)
from tools.validators._common.local_resolver import build_registry
from tools.validators.environmental_indicator_evidence_bundle_profile_support import (
    FIXTURE_PATH,
    load_fixture_cases,
)
from tools.validators.environmental_indicator_evidence_bundle_profile_semantics import (
    Finding,
    semantic_findings as _semantic_findings,
)

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "evidence"
    / "environmental_indicator_evidence_bundle_profile.schema.json"
)
MAX_SCHEMA_FINDINGS = 100
SCOPE = "evidence.environmental_indicator_evidence_bundle_profile"
NON_EFFECTS = (
    "no_live_source_access",
    "no_observation_authority",
    "no_evidence_resolution_claim",
    "no_policy_or_review_creation",
    "no_lifecycle_write",
    "no_promotion_release_deployment_or_publication",
)


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    analysis_id: str | None = None
    indicator_spec_hash: str | None = None
    bundle_spec_hash: str | None = None


def _json_pointer(parts: Sequence[object], prefix: str = "") -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    suffix = "/" + "/".join(escaped) if escaped else ""
    return prefix + suffix or "/"


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(
        schema,
        registry=build_registry(REPO_ROOT),
        format_checker=FormatChecker(),
    )


def _schema_findings(candidate: Mapping[str, object]) -> set[Finding]:
    try:
        validator = _load_schema_validator()
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (
        OSError,
        UnicodeError,
        ValueError,
        RecursionError,
        Unresolvable,
    ):
        return {Finding("ENV_PROFILE_SCHEMA_UNAVAILABLE", "/")}

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (
            _json_pointer(tuple(error.absolute_path)),
            str(error.validator or "schema"),
        ),
    )
    findings = {
        Finding(
            "ENV_PROFILE_SCHEMA_INVALID",
            _json_pointer(tuple(error.absolute_path)),
        )
        for error in errors
    }
    if truncated:
        findings.add(Finding("ENV_PROFILE_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def validate_document(candidate: object) -> ValidationResult:
    if not isinstance(candidate, Mapping):
        return ValidationResult("DENY", (Finding("ROOT_TYPE", "/"),))

    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult(
            "DENY",
            tuple(sorted(schema_findings)),
            analysis_id=(
                candidate.get("analysis_id")
                if isinstance(candidate.get("analysis_id"), str)
                else None
            ),
        )

    findings, indicator_hash, bundle_hash = _semantic_findings(candidate)
    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        analysis_id=(
            candidate.get("analysis_id")
            if isinstance(candidate.get("analysis_id"), str)
            else None
        ),
        indicator_spec_hash=indicator_hash,
        bundle_spec_hash=bundle_hash,
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        candidate = load_json_file(path)
    except JsonInputError:
        return ValidationResult("ERROR", (Finding("INPUT_READ_ERROR", "/"),))
    return validate_document(candidate)


def _serialize(path: Path | None, result: ValidationResult) -> str:
    return json.dumps(
        {
            "analysis_id": result.analysis_id,
            "authority": "NONE",
            "bundle_spec_hash": result.bundle_spec_hash,
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path is not None else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "indicator_spec_hash": result.indicator_spec_hash,
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    cases, suite_findings = load_fixture_cases()
    mismatches: list[dict[str, object]] = []
    counts = {"PASS": 0, "DENY": 0, "ERROR": 0}

    for case in cases:
        case_id = str(case["case_id"])
        result = validate_document(case.get("document"))
        counts[result.outcome] = counts.get(result.outcome, 0) + 1
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if (
            result.outcome != case.get("expected_outcome")
            or actual_findings != case.get("expected_findings")
        ):
            mismatches.append(
                {
                    "case_id": case_id,
                    "expected_outcome": case.get("expected_outcome"),
                    "actual_outcome": result.outcome,
                    "expected_findings": case.get("expected_findings"),
                    "actual_findings": actual_findings,
                }
            )

    ok = bool(cases) and not suite_findings and not mismatches
    payload: dict[str, object] = {
        "authority": "NONE",
        "cases": len(cases),
        "counts": counts,
        "execution_mode": "FIXTURE_ONLY",
        "findings": suite_findings,
        "mismatches": mismatches,
        "non_effects": NON_EFFECTS,
        "outcome": "PASS" if ok else "ERROR",
        "scope": SCOPE,
    }
    return ok, payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only environmental indicator EvidenceBundle profiles."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 2

    if not args.files:
        parser.error("provide at least one JSON file or --fixtures")

    exit_code = 0
    for path in args.files:
        result = validate_file(path)
        print(_serialize(path, result))
        if result.outcome == "ERROR":
            exit_code = 2
        elif result.outcome == "DENY" and exit_code == 0:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
