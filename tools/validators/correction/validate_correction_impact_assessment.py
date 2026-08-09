#!/usr/bin/env python3
"""Validate fixture-only CorrectionImpactAssessment records."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/correction/correction_impact_assessment.schema.json"
MAX_JSON_BYTES = 512 * 1024
MAX_FINDINGS = 100
CARRIERS = (
    "CATALOG", "API", "MAP", "TILE", "SEARCH",
    "GRAPH", "EXPORT", "AI", "CACHE", "DOCUMENTATION",
)
UTC_SECOND = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]
    payload: Mapping[str, object] | None
    outcome: str

    @property
    def ok(self) -> bool:
        return not self.findings and self.payload is not None


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _canonical(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def canonical_assessment_payload(assessment: Mapping[str, object]) -> dict[str, object]:
    return {
        key: assessment[key]
        for key in sorted(assessment)
        if key not in {"assessment_id", "assessment_digest"}
    }


def compute_assessment_digest(assessment: Mapping[str, object]) -> str:
    encoded = _canonical(canonical_assessment_payload(assessment)).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def compute_assessment_id(assessment: Mapping[str, object]) -> str:
    return (
        "kfm:correction-impact:"
        + compute_assessment_digest(assessment).split(":", 1)[1][:16]
    )


def _load(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except (OSError, UnicodeError):
        return None, [Finding("INPUT_UNREADABLE", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/")]
    return value, []


def _schema_findings(assessment: Mapping[str, object]) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = list(
        islice(
            Draft202012Validator(schema).iter_errors(assessment),
            MAX_FINDINGS + 1,
        )
    )
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic(assessment: Mapping[str, object]) -> tuple[list[Finding], str]:
    findings: list[Finding] = []
    carriers_raw = assessment.get("carriers")
    if not isinstance(carriers_raw, list):
        return [Finding("PROFILE_INCOMPLETE", "/carriers")], "ERROR"

    carriers = [item for item in carriers_raw if isinstance(item, Mapping)]
    names = [str(item.get("carrier")) for item in carriers]
    if names != list(CARRIERS):
        findings.append(Finding("CARRIER_INVENTORY_MISMATCH", "/carriers"))
    if len(names) != len(set(names)):
        findings.append(Finding("CARRIER_DUPLICATE", "/carriers"))

    for index, item in enumerate(carriers):
        affected = item.get("affected")
        action = item.get("action")
        reasons = item.get("reason_codes")
        refs = item.get("artifact_refs")
        if not isinstance(reasons, list) or not isinstance(refs, list):
            findings.append(Finding("CARRIER_PROFILE_INCOMPLETE", f"/carriers/{index}"))
            continue

        if affected is True:
            if action == "NO_ACTION":
                findings.append(Finding("AFFECTED_ACTION_REQUIRED", f"/carriers/{index}/action"))
            if not refs:
                findings.append(Finding("AFFECTED_ARTIFACT_REF_REQUIRED", f"/carriers/{index}/artifact_refs"))
        elif affected is False:
            if action != "NO_ACTION":
                findings.append(Finding("UNAFFECTED_ACTION_INVALID", f"/carriers/{index}/action"))
            if refs:
                findings.append(Finding("UNAFFECTED_ARTIFACT_REF_FORBIDDEN", f"/carriers/{index}/artifact_refs"))
            if "NOT_APPLICABLE_CONFIRMED" not in reasons:
                findings.append(Finding("UNAFFECTED_REASON_REQUIRED", f"/carriers/{index}/reason_codes"))

        if item.get("carrier") == "CACHE" and affected is True:
            if action != "INVALIDATE":
                findings.append(Finding("CACHE_ACTION_INVALID", f"/carriers/{index}/action"))
            if "CACHE_INVALIDATION_REQUIRED" not in reasons:
                findings.append(Finding("CACHE_REASON_REQUIRED", f"/carriers/{index}/reason_codes"))

        if item.get("carrier") == "AI" and affected is True:
            if action not in {"REVALIDATE", "WITHDRAW", "SUPERSEDE"}:
                findings.append(Finding("AI_ACTION_INVALID", f"/carriers/{index}/action"))
            if "CITATIONS_REVALIDATE" not in reasons:
                findings.append(Finding("AI_CITATION_REVALIDATION_REQUIRED", f"/carriers/{index}/reason_codes"))

    if not UTC_SECOND.fullmatch(str(assessment.get("assessed_at", ""))):
        findings.append(Finding("ASSESSED_AT_NOT_CANONICAL", "/assessed_at"))

    if assessment.get("assessment_digest") != compute_assessment_digest(assessment):
        findings.append(Finding("ASSESSMENT_DIGEST_MISMATCH", "/assessment_digest"))
    if assessment.get("assessment_id") != compute_assessment_id(assessment):
        findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    complete = (
        assessment.get("review_state") == "APPROVED"
        and isinstance(assessment.get("policy_decision_ref"), str)
        and bool(assessment.get("policy_decision_ref"))
        and isinstance(assessment.get("rollback_target_ref"), str)
        and bool(assessment.get("rollback_target_ref"))
    )
    computed_outcome = "COMPLETE" if complete else "HOLD"

    if findings:
        return findings, "ERROR"
    return [], computed_outcome


def validate(path: Path) -> Result:
    assessment, load_findings = _load(path)
    if assessment is None:
        return Result(tuple(sorted(load_findings)), None, "ERROR")

    schema_findings = _schema_findings(assessment)
    if schema_findings:
        return Result(tuple(sorted(schema_findings)), None, "ERROR")

    semantic_findings, computed = _semantic(assessment)
    if semantic_findings:
        return Result(tuple(sorted(semantic_findings)), None, "ERROR")
    if assessment.get("outcome") != computed:
        return Result((Finding("OUTCOME_MISMATCH", "/outcome"),), None, "ERROR")
    return Result((), assessment, computed)


def report(result: Result) -> dict[str, object]:
    return {
        "authority_created": False,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "outcome": result.outcome,
        "publication_authorized": False,
        "repository_mutation_allowed": False,
        "scope": "correction-impact-assessment",
        "status": "FAIL" if result.outcome == "ERROR" else "PASS",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only CorrectionImpactAssessment records."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    reports = [
        report(validate(path))
        for path in sorted(args.files, key=lambda item: item.as_posix())
    ]
    print(_canonical(reports))
    return 1 if any(item["status"] == "FAIL" for item in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
