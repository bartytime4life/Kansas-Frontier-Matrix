#!/usr/bin/env python3
"""Bind a stable-diff report and its rendered summary into a review handoff.

The handoff is a deterministic CI/reviewer aid. It recomputes the existing
``stable-diff`` report from the supplied artifact bytes and recomputes the
existing Markdown projection before binding hashes. It does not interpret
policy, authenticate reviewers, approve a ReviewRecord, promote, release, or
publish.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.ci.render_stable_diff_summary import (  # noqa: E402
    SummaryRenderError,
    render_stable_diff_summary,
)
from tools.diff.stable_diff import compare_paths  # noqa: E402

CONTEXT_SCHEMA_VERSION = "kfm.stable-diff-review-context.v1"
HANDOFF_SCHEMA_VERSION = "1.0.0"
MAX_JSON_BYTES = 256 * 1024
MAX_ARTIFACT_BYTES = 16 * 1024 * 1024
MAX_SUMMARY_BYTES = 1024 * 1024
SAFE_REF_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]{1,639}$")
ROLE_RE = re.compile(r"^[a-z][a-z0-9_:-]{2,63}$")
REVIEW_SCOPES = {
    "ai",
    "contract",
    "cross-cutting",
    "data",
    "docs",
    "domain",
    "evidence",
    "governance",
    "policy",
    "release",
    "schema",
    "sensitivity",
    "source",
    "ui",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class HandoffError(ValueError):
    def __init__(self, code: str, field: str) -> None:
        super().__init__(code)
        self.code = code
        self.field = field


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_json(path: Path, *, field: str) -> tuple[dict[str, Any], bytes]:
    try:
        if path.is_symlink():
            raise HandoffError("INPUT_SYMLINK_DENIED", field)
        if not path.is_file():
            raise HandoffError("INPUT_NOT_FILE", field)
        if path.stat().st_size > MAX_JSON_BYTES:
            raise HandoffError("INPUT_TOO_LARGE", field)
        raw = path.read_bytes()
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except HandoffError:
        raise
    except UnicodeDecodeError as exc:
        raise HandoffError("JSON_NOT_UTF8", field) from exc
    except DuplicateKeyError as exc:
        raise HandoffError("JSON_DUPLICATE_KEY", f"{field}/{exc.args[0]}") from exc
    except NonFiniteNumberError as exc:
        raise HandoffError("JSON_NONFINITE_NUMBER", field) from exc
    except json.JSONDecodeError as exc:
        raise HandoffError("JSON_INVALID", field) from exc
    except OSError as exc:
        raise HandoffError("INPUT_READ_ERROR", field) from exc
    if not isinstance(value, dict):
        raise HandoffError("ROOT_NOT_OBJECT", field)
    return value, raw


def _read_bytes(path: Path, *, field: str, maximum: int) -> bytes:
    try:
        if path.is_symlink():
            raise HandoffError("INPUT_SYMLINK_DENIED", field)
        if not path.is_file():
            raise HandoffError("INPUT_NOT_FILE", field)
        if path.stat().st_size > maximum:
            raise HandoffError("INPUT_TOO_LARGE", field)
        return path.read_bytes()
    except HandoffError:
        raise
    except OSError as exc:
        raise HandoffError("INPUT_READ_ERROR", field) from exc


def _sha256(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _repo_path(value: str, *, field: str) -> str:
    if not value or "\\" in value or any(ord(char) < 32 for char in value):
        raise HandoffError("PATH_INVALID", field)
    parsed = PurePosixPath(value)
    if parsed.is_absolute() or "." in parsed.parts or ".." in parsed.parts:
        raise HandoffError("PATH_INVALID", field)
    normalized = parsed.as_posix()
    if normalized != value:
        raise HandoffError("PATH_INVALID", field)
    return value


def _exact_keys(
    value: Mapping[str, Any],
    *,
    required: frozenset[str],
    optional: frozenset[str] = frozenset(),
    field: str,
) -> None:
    keys = frozenset(value)
    if not required <= keys or not keys <= required | optional:
        raise HandoffError("CONTEXT_SHAPE_INVALID", field)


def _safe_ref(value: Any, *, field: str, nullable: bool = False) -> str | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str) or not SAFE_REF_RE.fullmatch(value):
        raise HandoffError("REF_INVALID", field)
    return value


def _canonical_strings(
    value: Any,
    *,
    field: str,
    maximum: int,
    pattern: re.Pattern[str] | None = None,
    allow_empty: bool = True,
) -> list[str]:
    if not isinstance(value, list) or len(value) > maximum:
        raise HandoffError("ARRAY_INVALID", field)
    if not allow_empty and not value:
        raise HandoffError("ARRAY_INVALID", field)
    for item in value:
        if not isinstance(item, str) or not item or len(item) > 640:
            raise HandoffError("ARRAY_INVALID", field)
        if any(ord(char) < 32 for char in item):
            raise HandoffError("ARRAY_INVALID", field)
        if pattern is not None and not pattern.fullmatch(item):
            raise HandoffError("ARRAY_INVALID", field)
    if value != sorted(set(value)):
        raise HandoffError("ARRAY_NOT_CANONICAL", field)
    return list(value)


def _load_context(path: Path) -> tuple[dict[str, Any], bytes]:
    value, raw = _read_json(path, field="/context")
    required = frozenset(
        {
            "schema_version",
            "candidate_ref",
            "author_ref",
            "review_scope",
            "evidence_refs",
            "basis_refs",
            "policy_relevant_keys",
            "required_reviewer_roles",
            "rollback_target_ref",
        }
    )
    _exact_keys(value, required=required, field="/context")
    if value["schema_version"] != CONTEXT_SCHEMA_VERSION:
        raise HandoffError("CONTEXT_VERSION_INVALID", "/context/schema_version")
    candidate_ref = _safe_ref(value["candidate_ref"], field="/context/candidate_ref")
    author_ref = _safe_ref(value["author_ref"], field="/context/author_ref")
    scope = value["review_scope"]
    if scope not in REVIEW_SCOPES:
        raise HandoffError("REVIEW_SCOPE_INVALID", "/context/review_scope")
    evidence_refs = _canonical_strings(
        value["evidence_refs"], field="/context/evidence_refs", maximum=128
    )
    basis_refs = _canonical_strings(
        value["basis_refs"], field="/context/basis_refs", maximum=128
    )
    for index, ref in enumerate(evidence_refs):
        _safe_ref(ref, field=f"/context/evidence_refs/{index}")
    for index, ref in enumerate(basis_refs):
        _safe_ref(ref, field=f"/context/basis_refs/{index}")
    policy_keys = _canonical_strings(
        value["policy_relevant_keys"],
        field="/context/policy_relevant_keys",
        maximum=256,
    )
    roles = _canonical_strings(
        value["required_reviewer_roles"],
        field="/context/required_reviewer_roles",
        maximum=32,
        pattern=ROLE_RE,
        allow_empty=False,
    )
    rollback = _safe_ref(
        value["rollback_target_ref"],
        field="/context/rollback_target_ref",
        nullable=True,
    )
    normalized = {
        "schema_version": CONTEXT_SCHEMA_VERSION,
        "candidate_ref": candidate_ref,
        "author_ref": author_ref,
        "review_scope": scope,
        "evidence_refs": evidence_refs,
        "basis_refs": basis_refs,
        "policy_relevant_keys": policy_keys,
        "required_reviewer_roles": roles,
        "rollback_target_ref": rollback,
    }
    return normalized, raw


def _validate_report_paths(report: Mapping[str, Any], left: str, right: str) -> None:
    report_left = report.get("left")
    report_right = report.get("right")
    if report_left != left:
        raise HandoffError("REPORT_LEFT_PATH_MISMATCH", "/report/left")
    if report_right != right:
        raise HandoffError("REPORT_RIGHT_PATH_MISMATCH", "/report/right")


def _policy_impact(changed_keys: list[str], declared_keys: list[str]) -> dict[str, Any]:
    impacted = sorted(set(changed_keys) & set(declared_keys))
    if not changed_keys:
        classification = "NONE"
    elif not declared_keys:
        classification = "UNKNOWN"
    elif impacted:
        classification = "POTENTIAL"
    else:
        classification = "NO_DECLARED_IMPACT"
    return {
        "classification": classification,
        "declared_policy_relevant_keys": declared_keys,
        "impacted_keys": impacted,
        "authority_created": False,
    }


def build_review_handoff(
    *,
    left_path: Path,
    right_path: Path,
    report_path: Path,
    summary_path: Path,
    context_path: Path,
    output_path: Path | None = None,
) -> tuple[dict[str, Any], int]:
    left_ref = _repo_path(left_path.as_posix(), field="/left")
    right_ref = _repo_path(right_path.as_posix(), field="/right")
    report_ref = _repo_path(report_path.as_posix(), field="/report")
    summary_ref = _repo_path(summary_path.as_posix(), field="/summary")
    context_ref = _repo_path(context_path.as_posix(), field="/context")

    left_raw = _read_bytes(left_path, field="/left", maximum=MAX_ARTIFACT_BYTES)
    right_raw = _read_bytes(right_path, field="/right", maximum=MAX_ARTIFACT_BYTES)
    report, report_raw = _read_json(report_path, field="/report")
    summary_raw = _read_bytes(summary_path, field="/summary", maximum=MAX_SUMMARY_BYTES)
    context, context_raw = _load_context(context_path)

    _validate_report_paths(report, left_ref, right_ref)
    blocking = report.get("blocking")
    if not isinstance(blocking, bool):
        raise HandoffError("REPORT_BLOCKING_INVALID", "/report/blocking")
    if report.get("status") == "error":
        raise HandoffError("DIFF_REPORT_ERROR", "/report/status")
    recomputed_report, recomputed_exit = compare_paths(
        left_path, right_path, fail_on_change=blocking
    )
    if report != recomputed_report:
        raise HandoffError("REPORT_ARTIFACT_BINDING_MISMATCH", "/report")
    if recomputed_exit == 2:
        raise HandoffError("DIFF_REPORT_ERROR", "/report/status")

    try:
        expected_summary = render_stable_diff_summary(report_path).markdown.encode("utf-8")
    except SummaryRenderError as exc:
        raise HandoffError("SUMMARY_RENDER_ERROR", f"/summary/{exc.code}") from exc
    if summary_raw != expected_summary:
        raise HandoffError("SUMMARY_REPORT_BINDING_MISMATCH", "/summary")

    diff_summary = report["summary"]
    changed_keys = sorted(
        diff_summary["added"] + diff_summary["removed"] + diff_summary["changed"]
    )
    status = report["status"]
    disposition = (
        "NO_CHANGE"
        if status == "same"
        else "HOLD"
        if blocking
        else "REVIEW_REQUIRED"
    )
    core: dict[str, Any] = {
        "object_type": "StableDiffReviewHandoff",
        "schema_version": HANDOFF_SCHEMA_VERSION,
        "authority_created": False,
        "disposition": disposition,
        "candidate_ref": context["candidate_ref"],
        "input_binding": {
            "left": {"path": left_ref, "sha256": _sha256(left_raw)},
            "right": {"path": right_ref, "sha256": _sha256(right_raw)},
            "report": {"path": report_ref, "sha256": _sha256(report_raw)},
            "summary": {"path": summary_ref, "sha256": _sha256(summary_raw)},
            "context": {"path": context_ref, "sha256": _sha256(context_raw)},
        },
        "bundle_summary": {
            "status": status,
            "blocking": blocking,
            "total_changed_keys": len(changed_keys),
            "added": diff_summary["added"],
            "removed": diff_summary["removed"],
            "changed": diff_summary["changed"],
        },
        "policy_impact": _policy_impact(
            changed_keys, context["policy_relevant_keys"]
        ),
        "review_binding": {
            "candidate_ref": context["candidate_ref"],
            "author_ref": context["author_ref"],
            "review_scope": context["review_scope"],
            "evidence_refs": context["evidence_refs"],
            "basis_refs": context["basis_refs"],
            "required_reviewer_roles": context["required_reviewer_roles"],
            "rollback_target_ref": context["rollback_target_ref"],
            "review_record_contract_ref": "contracts/governance/ReviewRecord.md",
            "exact_input_binding_required": True,
        },
        "trust_boundary": {
            "evidence_resolved": False,
            "policy_decided": False,
            "review_authenticated": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
        },
    }
    # The digest covers the handoff core before the self-derived subject_ref is
    # inserted. Verification removes handoff_id, handoff_sha256, and
    # review_binding.subject_ref before recomputing this digest.
    digest = _sha256(_canonical_bytes(core))
    handoff = {
        **core,
        "handoff_id": "kfm:stable-diff-review-handoff:" + digest.removeprefix("sha256:"),
        "handoff_sha256": digest,
    }
    handoff["review_binding"]["subject_ref"] = handoff["handoff_id"]
    serialized = json.dumps(
        handoff, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
    ) + "\n"
    if output_path is not None:
        _write_output(output_path, serialized)
    return handoff, 1 if disposition == "HOLD" else 0


def _write_output(path: Path, text: str) -> None:
    try:
        if path.exists() and path.is_symlink():
            raise HandoffError("OUTPUT_SYMLINK_DENIED", "/output")
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name + ".tmp")
        if temporary.exists() and temporary.is_symlink():
            raise HandoffError("OUTPUT_SYMLINK_DENIED", "/output")
        temporary.write_text(text, encoding="utf-8", newline="\n")
        os.replace(temporary, path)
    except HandoffError:
        raise
    except OSError as exc:
        raise HandoffError("OUTPUT_WRITE_ERROR", "/output") from exc


def _error_payload(error: HandoffError) -> str:
    return json.dumps(
        {
            "object_type": "StableDiffReviewHandoffError",
            "outcome": "ERROR",
            "code": error.code,
            "field": error.field,
            "authority_created": False,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--left", required=True, type=Path)
    parser.add_argument("--right", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--context", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        handoff, exit_code = build_review_handoff(
            left_path=args.left,
            right_path=args.right,
            report_path=args.report,
            summary_path=args.summary,
            context_path=args.context,
            output_path=args.output,
        )
    except HandoffError as error:
        print(_error_payload(error))
        return 2
    if args.output is None:
        print(json.dumps(handoff, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
