#!/usr/bin/env python3
"""Validate bindings and render a deterministic implementation review packet.

The packet joins one validated ImplementationChangeContext with zero or more
validated ImplementationDecisionRecord documents. It reads declared fields only:
no diff hunks or changed-file contents are inspected, no rationale is inferred,
and no result creates evidence, policy, review approval, repository mutation,
promotion, release, deployment, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.implementation_change_context_model import (
    Evaluation as ContextEvaluation,
    evaluate_document as evaluate_context_document,
    evaluate_path as evaluate_context_path,
    load_json,
)
from tools.validators.governance.validate_implementation_decision_record import (
    Evaluation as DecisionEvaluation,
    evaluate_document as evaluate_decision_document,
    evaluate_paths as evaluate_decision_paths,
)

FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/implementation_review_packet/cases.json"
)
MAX_DECISIONS = 256
RECORD_ID_PATTERN = re.compile(
    r"^kfm:implementation-decision:[a-z0-9][a-z0-9-]{2,63}:[0-9]{4}$"
)
CONTEXT_ID_PATTERN = re.compile(r"^kfm:implementation-change-context:[0-9a-f]{64}$")
GIT_SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
EXIT_READY = 0
EXIT_ERROR = 2
EXIT_HOLD = 3
EXIT = {"READY": EXIT_READY, "ERROR": EXIT_ERROR, "HOLD": EXIT_HOLD}


@dataclass(frozen=True, order=True)
class Finding:
    """One value-minimized packet finding."""

    code: str
    field: str


@dataclass(frozen=True)
class Evaluation:
    """Finite packet outcome."""

    outcome: str
    findings: tuple[Finding, ...]


DecisionRow = tuple[Path, Mapping[str, object], DecisionEvaluation]


@dataclass(frozen=True)
class ReviewPacket:
    """Validated inputs plus their cross-object packet evaluation."""

    context_path: Path
    context: Mapping[str, object]
    context_evaluation: ContextEvaluation
    decision_rows: tuple[DecisionRow, ...]
    evaluation: Evaluation


def _source_finding(prefix: str, finding: object, source: str = "") -> Finding:
    code = getattr(finding, "code", "INPUT_INVALID")
    field = getattr(finding, "field", "$")
    rendered_field = f"{source}:{field}" if source else str(field)
    return Finding(f"{prefix}_{code}", rendered_field)


def _changed_paths(context: Mapping[str, object]) -> set[str]:
    paths: set[str] = set()
    files = context.get("files")
    if not isinstance(files, list):
        return paths
    for item in files:
        if not isinstance(item, dict):
            continue
        path = item.get("path")
        previous = item.get("previous_path")
        if isinstance(path, str):
            paths.add(path)
        if isinstance(previous, str):
            paths.add(previous)
    return paths


def _scope_paths(document: Mapping[str, object]) -> list[str]:
    scope = document.get("scope")
    paths = scope.get("paths") if isinstance(scope, dict) else None
    if not isinstance(paths, list):
        return []
    return [item for item in paths if isinstance(item, str)]


def evaluate_bound_documents(
    context: Mapping[str, object],
    context_evaluation: ContextEvaluation,
    decision_rows: Sequence[DecisionRow],
    *,
    pre_errors: Sequence[Finding] = (),
) -> Evaluation:
    """Evaluate input outcomes and exact context-to-decision bindings."""

    errors = list(pre_errors)
    holds: list[Finding] = []

    target = errors if context_evaluation.outcome == "ERROR" else holds
    if context_evaluation.outcome in {"ERROR", "HOLD"}:
        target.extend(
            _source_finding("CONTEXT", finding)
            for finding in context_evaluation.findings
        )

    for index, (_path, document, evaluation) in enumerate(decision_rows):
        target = errors if evaluation.outcome == "ERROR" else holds
        if evaluation.outcome in {"ERROR", "HOLD"}:
            record_id = document.get("record_id")
            source = (
                record_id
                if isinstance(record_id, str)
                and RECORD_ID_PATTERN.fullmatch(record_id) is not None
                else f"decision[{index}]"
            )
            target.extend(
                _source_finding("DECISION", finding, source)
                for finding in evaluation.findings
            )

    input_error = context_evaluation.outcome == "ERROR" or any(
        row[2].outcome == "ERROR" for row in decision_rows
    )
    if not input_error and not pre_errors:
        references = context.get("implementation_decision_refs")
        expected = set(references) if isinstance(references, list) else set()
        supplied = {
            record_id
            for _, document, _ in decision_rows
            if isinstance((record_id := document.get("record_id")), str)
        }
        if expected != supplied:
            errors.append(
                Finding(
                    "DECISION_REFERENCE_SET_MISMATCH",
                    "$.implementation_decision_refs",
                )
            )

        context_id = context.get("context_id")
        admitted_paths = _changed_paths(context)
        for _path, document, _evaluation in decision_rows:
            record_id = document.get("record_id")
            record_field = (
                f"$.decisions[{record_id}]"
                if isinstance(record_id, str)
                else "$.decisions[unknown]"
            )
            if document.get("change_ref") != context_id:
                errors.append(
                    Finding(
                        "DECISION_CHANGE_REF_MISMATCH",
                        f"{record_field}.change_ref",
                    )
                )
            for scope_path in _scope_paths(document):
                if scope_path not in admitted_paths:
                    errors.append(
                        Finding(
                            "DECISION_PATH_OUTSIDE_CHANGE",
                            f"{record_field}.scope.paths",
                        )
                    )

    if errors:
        return Evaluation("ERROR", tuple(sorted(set(errors))))
    if holds:
        return Evaluation("HOLD", tuple(sorted(set(holds))))
    return Evaluation("READY", ())


def evaluate_paths(
    context_path: Path,
    decision_paths: Sequence[Path],
) -> ReviewPacket:
    """Load, validate, bind, and classify packet inputs."""

    context, context_evaluation = evaluate_context_path(context_path)
    context = context or {}
    pre_errors: list[Finding] = []
    if len(decision_paths) > MAX_DECISIONS:
        pre_errors.append(Finding("DECISION_LIMIT_EXCEEDED", "$.decisions"))
        rows: list[DecisionRow] = []
    elif decision_paths:
        _payload, loaded_rows = evaluate_decision_paths(decision_paths)
        rows = list(loaded_rows)
    else:
        rows = []

    evaluation = evaluate_bound_documents(
        context,
        context_evaluation,
        rows,
        pre_errors=pre_errors,
    )
    return ReviewPacket(
        context_path=context_path,
        context=context,
        context_evaluation=context_evaluation,
        decision_rows=tuple(rows),
        evaluation=evaluation,
    )


def _plain(value: object) -> str:
    return " ".join(str(value if value is not None else "").replace("\x00", "").split())


def _code(value: object) -> str:
    normalized = _plain(value).replace("`", "'")
    return f"`{normalized}`"


def _safe_match(value: object, pattern: re.Pattern[str]) -> str | None:
    return value if isinstance(value, str) and pattern.fullmatch(value) else None


def _safe_record_id(document: Mapping[str, object], index: int) -> str:
    record_id = _safe_match(document.get("record_id"), RECORD_ID_PATTERN)
    return record_id if record_id is not None else f"decision[{index}]"


def _table(value: object) -> str:
    return _plain(value).replace("|", "\\|")


def _decision_order(row: DecisionRow) -> tuple[int, int, str]:
    _path, document, evaluation = row
    governance = document.get("governance")
    truth = governance.get("truth_label") if isinstance(governance, dict) else None
    outcome_rank = {"HOLD": 0, "READY": 1, "ERROR": 2}
    truth_rank = {"UNKNOWN": 0, "NEEDS_VERIFICATION": 1, "PROPOSED": 2, "CONFIRMED": 3}
    return (
        outcome_rank.get(evaluation.outcome, 9),
        truth_rank.get(str(truth), 9),
        str(document.get("record_id", "")),
    )


def _coverage(packet: ReviewPacket) -> tuple[list[str], list[str]]:
    changed = sorted(
        str(item.get("path"))
        for item in packet.context.get("files", [])
        if isinstance(item, dict) and isinstance(item.get("path"), str)
    )
    covered = {
        path
        for _source, document, _evaluation in packet.decision_rows
        for path in _scope_paths(document)
    }
    return sorted(set(changed) & covered), sorted(set(changed) - covered)


def payload(packet: ReviewPacket) -> dict[str, object]:
    """Return a bounded machine-readable packet summary."""

    covered, uncovered = _coverage(packet)
    return {
        "authority": "NONE",
        "outcome": packet.evaluation.outcome,
        "renderable": packet.evaluation.outcome != "ERROR",
        "context_id": _safe_match(packet.context.get("context_id"), CONTEXT_ID_PATTERN),
        "base_sha": _safe_match(packet.context.get("base_sha"), GIT_SHA_PATTERN),
        "head_sha": _safe_match(packet.context.get("head_sha"), GIT_SHA_PATTERN),
        "context_outcome": packet.context_evaluation.outcome,
        "decision_count": len(packet.decision_rows),
        "covered_path_count": len(covered),
        "uncovered_path_count": len(uncovered),
        "findings": [
            {"code": finding.code, "field": finding.field}
            for finding in packet.evaluation.findings
        ],
        "records": [
            {
                "record_id": _safe_record_id(document, index),
                "outcome": evaluation.outcome,
                "findings": [
                    {"code": finding.code, "field": finding.field}
                    for finding in evaluation.findings
                ],
            }
            for index, (_path, document, evaluation) in enumerate(
                sorted(packet.decision_rows, key=_decision_order)
            )
        ],
        "permissions": {
            "may_approve_review": False,
            "may_mutate_repository": False,
            "may_change_policy": False,
            "may_promote": False,
            "may_release": False,
            "may_publish": False,
        },
    }


def render_markdown(packet: ReviewPacket) -> str:
    """Render one deterministic reviewer view from validated declared fields."""

    if packet.evaluation.outcome == "ERROR":
        raise ValueError("ERROR packets are not renderable")

    context = packet.context
    summary = context.get("summary") if isinstance(context.get("summary"), dict) else {}
    files = [item for item in context.get("files", []) if isinstance(item, dict)]
    files.sort(
        key=lambda item: (
            str(item.get("path", "")),
            str(item.get("status", "")),
            str(item.get("previous_path") or ""),
        )
    )
    rows = sorted(packet.decision_rows, key=_decision_order)
    covered, uncovered = _coverage(packet)

    lines = [
        "# Implementation review packet",
        "",
        (
            f"_Mechanically assembled from one validated change context and "
            f"{len(rows)} validated decision record(s). It reads no diff hunks or "
            "changed-file contents, infers no rationale, and creates no evidence, "
            "policy, approval, mutation, promotion, release, deployment, or "
            "publication authority._"
        ),
        "",
        "## Review outcome",
        "",
        f"- **Packet:** `{packet.evaluation.outcome}`",
        f"- **Context:** `{packet.context_evaluation.outcome}`",
        f"- **Repository:** {_code(context.get('repository'))}",
        f"- **Range:** {_code(context.get('base_sha'))} → {_code(context.get('head_sha'))}",
        f"- **Context ID:** {_code(context.get('context_id'))}",
        f"- **Generated at:** {_code(context.get('generated_at'))}",
        "",
        "## Mechanical change summary",
        "",
        f"- **Files:** `{_plain(summary.get('file_count'))}`",
        f"- **Text additions/deletions:** `{_plain(summary.get('additions'))}` / `{_plain(summary.get('deletions'))}`",
        f"- **Binary files:** `{_plain(summary.get('binary_file_count'))}`",
        "- **Top-level roots:** "
        + (", ".join(_code(item) for item in summary.get("top_level_roots", [])) or "_none_"),
        "- **Signals:** "
        + (", ".join(_code(item) for item in summary.get("signal_codes", [])) or "_none_"),
        f"- **Signal score:** `{_plain(summary.get('signal_score'))}`",
        f"- **Decision capture recommended:** `{str(summary.get('decision_capture_recommended')).lower()}`",
        f"- **Decision-covered destination paths:** `{len(covered)}` / `{len(files)}`",
        "",
        "## Review attention",
        "",
    ]
    if packet.evaluation.findings:
        lines.extend(
            f"- `{finding.code}` at {_code(finding.field)}"
            for finding in packet.evaluation.findings
        )
    else:
        lines.append("- No mechanical hold or binding finding.")

    lines += [
        "",
        "## Changed paths",
        "",
        "| Status | Path | Previous path | Additions | Deletions | Binary |",
        "|---|---|---|---:|---:|:---:|",
    ]
    for item in files:
        additions = "—" if item.get("additions") is None else _table(item.get("additions"))
        deletions = "—" if item.get("deletions") is None else _table(item.get("deletions"))
        previous = _table(item.get("previous_path")) or "—"
        lines.append(
            "| "
            + " | ".join(
                (
                    _table(item.get("status")),
                    _code(item.get("path")),
                    _code(previous) if previous != "—" else "—",
                    additions,
                    deletions,
                    "yes" if item.get("binary") is True else "no",
                )
            )
            + " |"
        )

    lines += ["", "## Decision coverage", ""]
    if rows:
        lines += [
            "| Outcome | Record | Truth | Significance | Scope paths |",
            "|---|---|---|---|---|",
        ]
        for _path, document, evaluation in rows:
            governance = document.get("governance") if isinstance(document.get("governance"), dict) else {}
            paths = ", ".join(_code(item) for item in _scope_paths(document))
            lines.append(
                "| "
                + " | ".join(
                    (
                        f"`{evaluation.outcome}`",
                        _code(document.get("record_id")),
                        f"`{_table(governance.get('truth_label'))}`",
                        f"`{_table(governance.get('significance'))}`",
                        paths,
                    )
                )
                + " |"
            )
    else:
        lines.append(
            "_No decision record was supplied; the validated context did not bind one._"
        )

    lines += ["", "### Uncovered destination paths", ""]
    if uncovered:
        lines.extend(f"- {_code(path)}" for path in uncovered)
        lines += [
            "",
            "_Uncovered paths are informational. A decision record explains a material choice; it is not required to enumerate every changed file._",
        ]
    else:
        lines.append("- None.")

    for _path, document, evaluation in rows:
        scope = document.get("scope") if isinstance(document.get("scope"), dict) else {}
        decision = document.get("decision") if isinstance(document.get("decision"), dict) else {}
        governance = document.get("governance") if isinstance(document.get("governance"), dict) else {}
        rollback = document.get("rollback") if isinstance(document.get("rollback"), dict) else {}
        lines += [
            "",
            "---",
            "",
            f"## {_plain(document.get('record_id'))} — {_plain(document.get('title'))}",
            "",
            f"- **Outcome:** `{evaluation.outcome}`",
            f"- **Change binding:** {_code(document.get('change_ref'))}",
            f"- **Status:** `{_plain(document.get('status'))}`",
            f"- **Truth label:** `{_plain(governance.get('truth_label'))}`",
            f"- **Significance:** `{_plain(governance.get('significance'))}`",
            f"- **Behavior:** {_plain(scope.get('behavior'))}",
            "- **Paths:** " + ", ".join(_code(item) for item in _scope_paths(document)),
        ]
        if evaluation.findings:
            lines.append(
                "- **Record findings:** "
                + ", ".join(f"`{item.code}`" for item in evaluation.findings)
            )
        lines += [
            "",
            "### Chosen mechanism",
            "",
            f"**Option:** {_plain(decision.get('chosen_option'))}",
            "",
            _plain(decision.get("mechanism")),
            "",
            "### Rationale",
            "",
            _plain(decision.get("rationale")),
            "",
            "### Alternatives",
            "",
        ]
        for alternative in decision.get("alternatives", []):
            if isinstance(alternative, dict):
                lines.append(
                    f"- **{_plain(alternative.get('disposition'))} — {_plain(alternative.get('option'))}:** {_plain(alternative.get('reason'))}"
                )
        lines += ["", "### Reviewer questions", ""]
        lines.extend(
            f"- {_plain(item)}" for item in decision.get("reviewer_questions", [])
        )
        lines += [
            "",
            "### Support and rollback",
            "",
            "- **Evidence:** "
            + (", ".join(_code(item) for item in document.get("evidence_refs", [])) or "_none declared_"),
            "- **Validation:** "
            + (", ".join(_code(item) for item in document.get("validation_refs", [])) or "_none declared_"),
            f"- **Rollback strategy:** {_plain(rollback.get('strategy'))}",
            f"- **Rollback target:** {_code(rollback.get('target_ref'))}",
        ]
        for label, key in (
            ("ADR", "adr_ref"),
            ("Decision log", "decision_log_ref"),
            ("Review record", "review_record_ref"),
            ("Generated receipt", "generated_receipt_ref"),
        ):
            value = governance.get(key)
            lines.append(
                f"- **{label}:** {_code(value) if value else '_not declared_'}"
            )

    questions = sorted(
        {
            (str(document.get("record_id", "")), _plain(question))
            for _path, document, _evaluation in rows
            for question in (
                document.get("decision", {}).get("reviewer_questions", [])
                if isinstance(document.get("decision"), dict)
                else []
            )
        }
    )
    lines += ["", "## Consolidated reviewer questions", ""]
    if questions:
        lines.extend(f"- {_code(record_id)}: {question}" for record_id, question in questions)
    else:
        lines.append("- None declared.")

    lines += [
        "",
        "## Trust boundary",
        "",
        "This packet is review support only. A `READY` result means the supplied records are internally valid and exactly bound to the declared committed range. It does not authenticate evidence references, prove the rationale, approve the change, authorize merge, or replace KFM ReviewRecord, ADR, promotion, release, rollback, or publication controls.",
        "",
    ]
    return "\n".join(lines)


def _decode_pointer_part(part: str) -> str:
    decoded = part.replace("~1", "/").replace("~0", "~")
    if "~" in decoded and "~" in part.replace("~0", "").replace("~1", ""):
        raise ValueError("invalid fixture JSON pointer escape")
    return decoded


def _apply_overrides(target: object, overrides: object) -> None:
    if overrides is None:
        return
    if not isinstance(overrides, dict):
        raise ValueError("fixture overrides must be an object")
    for pointer in sorted(overrides):
        if not isinstance(pointer, str) or not pointer.startswith("/"):
            raise ValueError("fixture override must use an absolute JSON pointer")
        parts = [_decode_pointer_part(part) for part in pointer[1:].split("/")]
        current = target
        for part in parts[:-1]:
            if isinstance(current, dict):
                if part not in current:
                    raise ValueError("fixture override traverses an unknown object key")
                current = current[part]
            elif isinstance(current, list):
                if not part.isdigit() or int(part) >= len(current):
                    raise ValueError("fixture override traverses an invalid array index")
                current = current[int(part)]
            else:
                raise ValueError("fixture override traverses a scalar")
        leaf = parts[-1]
        value = copy.deepcopy(overrides[pointer])
        if isinstance(current, dict):
            if leaf not in current:
                raise ValueError("fixture override targets an unknown object key")
            current[leaf] = value
        elif isinstance(current, list):
            if not leaf.isdigit() or int(leaf) >= len(current):
                raise ValueError("fixture override targets an invalid array index")
            current[int(leaf)] = value
        else:
            raise ValueError("fixture override targets a scalar")


def load_fixture_cases() -> list[dict[str, object]]:
    """Expand compact base-plus-override fixtures into exact input documents."""

    manifest = load_json(FIXTURE_PATH)
    if manifest.get("profile") != "kfm.governance.implementation-review-packet.fixture-cases.v1":
        raise ValueError("unexpected fixture profile")
    base = manifest.get("base")
    scenarios = manifest.get("cases")
    if not isinstance(base, dict) or not isinstance(scenarios, list):
        raise ValueError("fixture base and cases are required")
    base_context = base.get("context")
    base_decisions = base.get("decisions")
    if not isinstance(base_context, dict) or not isinstance(base_decisions, list):
        raise ValueError("fixture base inputs are invalid")
    if len(scenarios) > 64 or len(base_decisions) > 16:
        raise ValueError("fixture manifest exceeds configured bounds")

    admitted = {
        "name",
        "expected_outcome",
        "expected_findings",
        "include_decisions",
        "context_overrides",
        "decision_overrides",
    }
    cases: list[dict[str, object]] = []
    for scenario in scenarios:
        if not isinstance(scenario, dict) or set(scenario) - admitted:
            raise ValueError("fixture scenario is invalid")
        name = scenario.get("name")
        expected = scenario.get("expected_outcome")
        findings = scenario.get("expected_findings")
        if not isinstance(name, str) or expected not in EXIT or not isinstance(findings, list):
            raise ValueError("fixture scenario metadata is invalid")
        context = copy.deepcopy(base_context)
        decisions = (
            copy.deepcopy(base_decisions)
            if scenario.get("include_decisions", True) is True
            else []
        )
        _apply_overrides(context, scenario.get("context_overrides", {}))
        _apply_overrides(decisions, scenario.get("decision_overrides", {}))
        cases.append(
            {
                "name": name,
                "expected_outcome": expected,
                "expected_findings": copy.deepcopy(findings),
                "context": context,
                "decisions": decisions,
            }
        )
    return cases


def run_cases() -> tuple[bool, dict[str, object]]:
    """Run exact fixture polarity without network access."""

    try:
        cases = load_fixture_cases()
    except Exception:
        return False, {
            "authority": "NONE",
            "outcome": "ERROR",
            "cases": 0,
            "mismatches": ["FIXTURE_INPUT_INVALID"],
        }

    mismatches: list[dict[str, object]] = []
    for case in cases:
        if not isinstance(case, dict):
            mismatches.append(
                {"case": "<invalid>", "expected": "<unknown>", "actual": "ERROR"}
            )
            continue
        context = case.get("context")
        decisions = case.get("decisions")
        if not isinstance(context, dict) or not isinstance(decisions, list) or not all(
            isinstance(item, dict) for item in decisions
        ):
            actual = "ERROR"
            codes = ["FIXTURE_CASE_INVALID"]
        else:
            context_evaluation = evaluate_context_document(context)
            rows = [
                (
                    Path(f"fixture-{index:03d}.json"),
                    document,
                    evaluate_decision_document(document),
                )
                for index, document in enumerate(decisions)
            ]
            evaluation = evaluate_bound_documents(context, context_evaluation, rows)
            actual = evaluation.outcome
            codes = [finding.code for finding in evaluation.findings]
        expected = case.get("expected_outcome")
        expected_codes = case.get("expected_findings", [])
        if actual != expected or codes != expected_codes:
            mismatches.append(
                {
                    "case": case.get("name"),
                    "expected": expected,
                    "actual": actual,
                    "expected_findings": expected_codes,
                    "actual_findings": codes,
                }
            )

    return not mismatches, {
        "authority": "NONE",
        "outcome": "PASS" if not mismatches else "FAIL",
        "cases": len(cases),
        "mismatches": mismatches,
    }


run_fixture_suite = run_cases


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context", nargs="?", type=Path)
    parser.add_argument("decisions", nargs="*", type=Path)
    parser.add_argument("--cases", action="store_true")
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args(argv)

    if args.cases:
        if args.context or args.decisions or args.render:
            parser.error("--cases cannot be combined with packet inputs or --render")
        ok, result = run_cases()
        print(json.dumps(result, indent=2, sort_keys=True))
        return EXIT_READY if ok else EXIT_ERROR
    if args.context is None:
        parser.error("provide one context file or use --cases")

    packet = evaluate_paths(args.context, args.decisions)
    if args.render and packet.evaluation.outcome != "ERROR":
        print(render_markdown(packet), end="")
    else:
        print(json.dumps(payload(packet), indent=2, sort_keys=True))
    return EXIT[packet.evaluation.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
