#!/usr/bin/env python3
"""Validate and render non-authoritative ImplementationDecisionRecord inputs.

READY means only that a record is internally review-ready. HOLD and ERROR fail
closed. No result creates evidence, policy, approval, repository mutation,
promotion, release, deployment, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/contracts/v1/governance/implementation_decision_record.schema.json"
CASES = REPO_ROOT / "fixtures/contracts/v1/governance/implementation_decision_record/cases.json"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
EXIT_READY = 0
EXIT_ERROR = 2
EXIT_HOLD = 3
EXIT = {"READY": EXIT_READY, "ERROR": EXIT_ERROR, "HOLD": EXIT_HOLD}
SCHEMA_PATH = SCHEMA
FIXTURE_PATH = CASES


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Evaluation:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def _constant(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json(path: Path) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular non-symlink file")
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("input exceeds 2 MiB")
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_pairs,
        parse_constant=_constant,
        parse_float=_float,
    )
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _pointer(parts: Iterable[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(document: Mapping[str, object]) -> list[Finding]:
    errors = list(islice(_validator().iter_errors(document), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda e: (_pointer(e.absolute_path), str(e.validator)))
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return findings


def _sorted_unique(value: object) -> bool:
    return isinstance(value, list) and value == sorted(value) and len(value) == len(set(value))


def _roots(paths: Sequence[object]) -> set[str]:
    return {PurePosixPath(item).parts[0] for item in paths if isinstance(item, str)}


def _semantic_errors(document: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    scope = document.get("scope")
    governance = document.get("governance")
    decision = document.get("decision")
    rollback = document.get("rollback")
    if not all(isinstance(item, dict) for item in (scope, governance, decision, rollback)):
        return findings

    ordered = (
        (scope.get("paths"), "$.scope.paths"),
        (scope.get("object_families"), "$.scope.object_families"),
        (document.get("evidence_refs"), "$.evidence_refs"),
        (document.get("validation_refs"), "$.validation_refs"),
    )
    for value, field in ordered:
        if not _sorted_unique(value):
            findings.append(Finding("CANONICAL_ORDER_REQUIRED", field))

    paths = scope.get("paths")
    if isinstance(paths, list):
        for index, value in enumerate(paths):
            if not isinstance(value, str):
                continue
            path = PurePosixPath(value)
            if (
                value.startswith("/") or "\\" in value or str(path) != value
                or any(part in {"", ".", ".."} for part in path.parts)
                or path.parts[0] in {".git", ".env", "secrets"}
            ):
                findings.append(Finding("REPOSITORY_PATH_UNSAFE", f"$.scope.paths[{index}]"))
        if governance.get("significance") == "CROSS_COMPONENT" and len(_roots(paths)) < 2:
            findings.append(Finding("SIGNIFICANCE_SCOPE_MISMATCH", "$.governance.significance"))

    forbidden = re.compile(
        r"(?:chain[- ]of[- ]thought|hidden reasoning|competence (?:score|profile)|"
        r"developer skill level|personal calibration profile)", re.IGNORECASE
    )

    def scan(value: object, field: str) -> None:
        if isinstance(value, str) and forbidden.search(value):
            findings.append(Finding("PRIVATE_REASONING_OR_PROFILE_DENIED", field))

    scan(scope.get("behavior"), "$.scope.behavior")
    for key in ("chosen_option", "mechanism", "rationale"):
        scan(decision.get(key), f"$.decision.{key}")
    for index, alternative in enumerate(decision.get("alternatives", [])):
        if isinstance(alternative, dict):
            scan(alternative.get("option"), f"$.decision.alternatives[{index}].option")
            scan(alternative.get("reason"), f"$.decision.alternatives[{index}].reason")
    for index, question in enumerate(decision.get("reviewer_questions", [])):
        scan(question, f"$.decision.reviewer_questions[{index}]")
    scan(rollback.get("strategy"), "$.rollback.strategy")
    return findings


def _hold_findings(document: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    governance = document.get("governance")
    if document.get("status") == "DRAFT":
        findings.append(Finding("RECORD_DRAFT", "$.status"))
    if isinstance(governance, dict):
        if governance.get("truth_label") == "UNKNOWN":
            findings.append(Finding("TRUTH_UNKNOWN", "$.governance.truth_label"))
        if governance.get("significance") == "AUTHORITY_SIGNIFICANT" and not governance.get("adr_ref"):
            findings.append(Finding("ADR_REQUIRED", "$.governance.adr_ref"))
    if document.get("status") == "READY_FOR_REVIEW" and not document.get("validation_refs"):
        findings.append(Finding("VALIDATION_REQUIRED", "$.validation_refs"))
    return findings


def evaluate_document(document: Mapping[str, object]) -> Evaluation:
    errors = sorted(set(_schema_findings(document) + _semantic_errors(document)))
    if errors:
        return Evaluation("ERROR", tuple(errors))
    holds = tuple(sorted(set(_hold_findings(document))))
    return Evaluation("HOLD" if holds else "READY", holds)


def evaluate_path(path: Path) -> tuple[dict[str, object] | None, Evaluation]:
    try:
        return (document := load_json(path)), evaluate_document(document)
    except (json.JSONDecodeError, DuplicateKeyError, NonFiniteNumberError):
        return None, Evaluation("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return None, Evaluation("ERROR", (Finding("INPUT_INVALID", "$"),))


def evaluate_paths(paths: Sequence[Path]) -> tuple[dict[str, object], list[tuple[Path, Mapping[str, object], Evaluation]]]:
    rows: list[tuple[Path, Mapping[str, object], Evaluation]] = []
    ids: dict[str, int] = {}
    for path in paths:
        document, evaluation = evaluate_path(path)
        document = document or {}
        record_id = document.get("record_id")
        if isinstance(record_id, str):
            if record_id in ids:
                evaluation = Evaluation("ERROR", tuple(sorted(set(evaluation.findings + (Finding("DUPLICATE_RECORD_ID", "$.record_id"),)))))
                old_path, old_doc, old_eval = rows[ids[record_id]]
                rows[ids[record_id]] = (old_path, old_doc, Evaluation("ERROR", tuple(sorted(set(old_eval.findings + (Finding("DUPLICATE_RECORD_ID", "$.record_id"),))))))
            else:
                ids[record_id] = len(rows)
        rows.append((path, document, evaluation))
    rows.sort(key=lambda row: (str(row[1].get("record_id", "")), row[0].as_posix()))
    rank = {"READY": 0, "HOLD": 1, "ERROR": 2}
    overall = max((row[2].outcome for row in rows), key=rank.get, default="ERROR")
    payload = {
        "authority": "NONE",
        "outcome": overall,
        "findings": [{"code": code} for code in sorted({finding.code for row in rows for finding in row[2].findings})],
        "records": [
            {
                "path": row[0].as_posix(),
                "record_id": row[1].get("record_id"),
                "outcome": row[2].outcome,
                "findings": [{"code": finding.code, "field": finding.field} for finding in row[2].findings],
            }
            for row in rows
        ],
    }
    return payload, rows


def _plain(value: object) -> str:
    return " ".join(str(value).replace("\x00", "").split())


def _code(value: object) -> str:
    return f"`{_plain(value).replace('`', "'")}`"


def render_markdown(rows: Sequence[tuple[Path, Mapping[str, object], Evaluation]]) -> str:
    lines = [
        "# Implementation decision review", "",
        f"_{len(rows)} mechanically rendered record(s). This view creates no evidence, policy, review approval, repository mutation, promotion, release, deployment, or publication authority._", "",
    ]
    for _, doc, evaluation in rows:
        scope = doc.get("scope", {}) if isinstance(doc.get("scope"), dict) else {}
        decision = doc.get("decision", {}) if isinstance(doc.get("decision"), dict) else {}
        governance = doc.get("governance", {}) if isinstance(doc.get("governance"), dict) else {}
        rollback = doc.get("rollback", {}) if isinstance(doc.get("rollback"), dict) else {}
        lines += [
            f"## {_plain(doc.get('record_id'))} — {_plain(doc.get('title'))}", "",
            f"- **Outcome:** `{evaluation.outcome}`",
            f"- **Change:** {_code(doc.get('change_ref'))}",
            f"- **Status:** `{_plain(doc.get('status'))}`",
            f"- **Behavior:** {_plain(scope.get('behavior'))}",
            "- **Paths:** " + ", ".join(_code(item) for item in scope.get("paths", [])),
        ]
        if evaluation.findings:
            lines.append("- **Hold/error reasons:** " + ", ".join(f"`{item.code}`" for item in evaluation.findings))
        lines += ["", "### Chosen mechanism", "", f"**Option:** {_plain(decision.get('chosen_option'))}", "", _plain(decision.get("mechanism")), "", "### Rationale", "", _plain(decision.get("rationale")), "", "### Alternatives", ""]
        for alternative in decision.get("alternatives", []):
            if isinstance(alternative, dict):
                lines.append(f"- **{_plain(alternative.get('disposition'))} — {_plain(alternative.get('option'))}:** {_plain(alternative.get('reason'))}")
        lines += ["", "### Reviewer questions", ""]
        lines += [f"- {_plain(item)}" for item in decision.get("reviewer_questions", [])]
        lines += ["", "### Support and governance", "", "- **Evidence:** " + ", ".join(_code(item) for item in doc.get("evidence_refs", [])), "- **Validation:** " + (", ".join(_code(item) for item in doc.get("validation_refs", [])) or "_none declared_"), f"- **Truth label:** `{_plain(governance.get('truth_label'))}`", f"- **Significance:** `{_plain(governance.get('significance'))}`"]
        for label, key in (("ADR", "adr_ref"), ("Decision log", "decision_log_ref"), ("Review record", "review_record_ref"), ("Generated receipt", "generated_receipt_ref")):
            value = governance.get(key)
            lines.append(f"- **{label}:** {_code(value) if value else '_not declared_'}")
        lines += ["", "### Rollback", "", f"- **Strategy:** {_plain(rollback.get('strategy'))}", f"- **Target:** {_code(rollback.get('target_ref'))}", "", "---", ""]
    return "\n".join(lines).rstrip() + "\n"


def run_cases() -> tuple[bool, dict[str, object]]:
    try:
        cases = load_json(CASES).get("cases")
    except Exception:
        return False, {"outcome": "ERROR", "cases": 0, "mismatches": ["FIXTURE_INPUT_INVALID"]}
    if not isinstance(cases, list):
        return False, {"outcome": "ERROR", "cases": 0, "mismatches": ["FIXTURE_CASES_INVALID"]}
    mismatches = []
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("document"), dict):
            mismatches.append({"case": "<invalid>", "expected": "<unknown>", "actual": "ERROR"})
            continue
        actual = evaluate_document(case["document"]).outcome
        if actual != case.get("expected_outcome"):
            mismatches.append({"case": case.get("name"), "expected": case.get("expected_outcome"), "actual": actual})
    return not mismatches, {"authority": "NONE", "outcome": "PASS" if not mismatches else "FAIL", "cases": len(cases), "mismatches": mismatches}


run_fixture_suite = run_cases


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="*", type=Path)
    parser.add_argument("--cases", action="store_true")
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args(argv)
    if args.cases:
        if args.records or args.render:
            parser.error("--cases cannot be combined with records or --render")
        ok, payload = run_cases()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if ok else 2
    if not args.records:
        parser.error("provide at least one record or use --cases")
    payload, rows = evaluate_paths(args.records)
    print(render_markdown(rows) if args.render and payload["outcome"] != "ERROR" else json.dumps(payload, indent=2, sort_keys=True), end="" if args.render and payload["outcome"] != "ERROR" else "\n")
    return EXIT[str(payload["outcome"])]


if __name__ == "__main__":
    raise SystemExit(main())
