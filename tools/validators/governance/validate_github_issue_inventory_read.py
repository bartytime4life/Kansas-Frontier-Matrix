#!/usr/bin/env python3
"""Validate a stored GitHubIssueInventoryRead receipt for briefing routing.

This validator never performs network access. It verifies the closed schema,
deterministic digest/receipt identity, freshness at an explicit as-of time, and
all-false trust-bearing effects before a receipt may be used as read-only
routing input.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/github_issue_inventory_read.schema.json"


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    payload: Mapping[str, object] | None

    @property
    def ok(self) -> bool:
        return not self.findings and self.payload is not None


def _canon(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _parse(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def compute_digest(record: Mapping[str, object]) -> str:
    payload = {k: v for k, v in record.items() if k not in {"receipt_id", "response_digest"}}
    return "sha256:" + hashlib.sha256(_canon(payload).encode("utf-8")).hexdigest()


def compute_receipt_id(record: Mapping[str, object]) -> str:
    return "kfm:github-issue-read:" + compute_digest(record).removeprefix("sha256:")[:24]


def validate_record(path: Path, *, as_of: str) -> ValidationResult:
    findings: list[Finding] = []
    try:
        if path.is_symlink() or not path.is_file():
            return ValidationResult((Finding("INPUT_NOT_REGULAR_FILE", "/"),), None)
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ValidationResult((Finding("INPUT_INVALID", "/"),), None)
    if not isinstance(record, dict):
        return ValidationResult((Finding("ROOT_NOT_OBJECT", "/"),), None)

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(record), key=lambda e: tuple(e.absolute_path)):
        path_text = "/" + "/".join(str(p) for p in error.absolute_path) if error.absolute_path else "/"
        findings.append(Finding("SCHEMA_INVALID", path_text))
    if findings:
        return ValidationResult(tuple(sorted(set(findings))), None)

    if record.get("response_digest") != compute_digest(record):
        findings.append(Finding("RESPONSE_DIGEST_MISMATCH", "/response_digest"))
    if record.get("receipt_id") != compute_receipt_id(record):
        findings.append(Finding("RECEIPT_ID_MISMATCH", "/receipt_id"))
    requested = record.get("requested_issue_ids")
    issues = record.get("issues")
    if isinstance(requested, list) and requested != sorted(set(requested)):
        findings.append(Finding("REQUESTED_ISSUES_NOT_SORTED_UNIQUE", "/requested_issue_ids"))
    if isinstance(issues, list):
        numbers = [row.get("number") for row in issues if isinstance(row, Mapping)]
        if numbers != sorted(numbers) or numbers != requested:
            findings.append(Finding("ISSUE_SET_MISMATCH", "/issues"))

    if record.get("outcome") != "FRESH":
        findings.append(Finding("LIVE_READ_NOT_FRESH", "/outcome"))
    try:
        if _parse(as_of) > _parse(str(record["stale_at"])):
            findings.append(Finding("LIVE_READ_STALE_AT_AS_OF", "/stale_at"))
        if _parse(as_of) < _parse(str(record["retrieved_at"])):
            findings.append(Finding("AS_OF_PRECEDES_RETRIEVAL", "/retrieved_at"))
    except (ValueError, TypeError, KeyError):
        findings.append(Finding("AS_OF_INVALID", "/"))

    return ValidationResult(tuple(sorted(set(findings))), record if not findings else None)


def summary(record: Mapping[str, object]) -> dict[str, object]:
    return {
        "profile": "github-live-read-v1",
        "receipt_id": record.get("receipt_id"),
        "repository": record.get("repository"),
        "repository_id": record.get("repository_id"),
        "default_branch": record.get("default_branch"),
        "default_branch_head_sha": record.get("default_branch_head_sha"),
        "retrieved_at": record.get("retrieved_at"),
        "stale_at": record.get("stale_at"),
        "authority_created": False,
        "repository_mutation_allowed": False,
    }
