#!/usr/bin/env python3
"""Render a deterministic, non-authoritative review handoff from stable diff data.

The output is a derived QA artifact. It binds exact inputs for later human
review but does not create a ReviewRecord, approve a change, evaluate policy,
promote, release, deploy, or publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_FIELDS = 2_000
MAX_TEXT = 720
SHA256_REF = re.compile(r"^(?:urn:|kfm://)[^\s@]+@sha256:[0-9a-f]{64}$")
IDENTIFIER = re.compile(r"^[a-z][a-z0-9_.:-]{2,160}$")
ROLE_VALUES = frozenset({"steward", "reviewer", "auditor"})
DIFF_STATUS_VALUES = frozenset({"same", "changed"})
TOOL_NAME = "kfm-diff-review-handoff"
SCHEMA_VERSION = "1.0.0"
REVIEW_SCHEMA_REF = "schemas/contracts/v1/governance/review_record.schema.json"
ALLOWED_DECISIONS = ("approve", "reject", "request_changes")


class HandoffInputError(ValueError):
    """Finite input or contract error."""


class DuplicateKeyError(ValueError):
    """JSON object repeated a key."""


class NonFiniteNumberError(ValueError):
    """JSON contained NaN or infinity."""


def _reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> dict[str, object]:
    """Load one bounded regular JSON object without following symlinks."""

    try:
        if path.is_symlink():
            raise HandoffInputError("INPUT_SYMLINK_DENIED")
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(path, flags)
        try:
            file_stat = os.fstat(fd)
            if not stat.S_ISREG(file_stat.st_mode):
                raise HandoffInputError("INPUT_NOT_FILE")
            with os.fdopen(fd, "rb") as stream:
                fd = -1
                raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if fd >= 0:
                os.close(fd)
    except FileNotFoundError as exc:
        raise HandoffInputError("INPUT_NOT_FILE") from exc
    except OSError as exc:
        raise HandoffInputError("INPUT_READ_ERROR") from exc

    if len(raw) > MAX_JSON_BYTES:
        raise HandoffInputError("INPUT_TOO_LARGE")
    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicates,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except UnicodeDecodeError as exc:
        raise HandoffInputError("JSON_INVALID_UTF8") from exc
    except DuplicateKeyError as exc:
        raise HandoffInputError("JSON_DUPLICATE_KEY") from exc
    except NonFiniteNumberError as exc:
        raise HandoffInputError("JSON_NONFINITE_NUMBER") from exc
    except (json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise HandoffInputError("JSON_INVALID") from exc
    if not isinstance(value, dict):
        raise HandoffInputError("JSON_ROOT_NOT_OBJECT")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return "sha256:" + digest.hexdigest()


def _bounded_string(value: object, code: str) -> str:
    if not isinstance(value, str) or not value or len(value) > MAX_TEXT or any(
        character.isspace() for character in value
    ):
        raise HandoffInputError(code)
    return value


def _string_list(value: object, code: str) -> list[str]:
    if (
        not isinstance(value, list)
        or len(value) > MAX_FIELDS
        or any(not isinstance(item, str) or not item or len(item) > 160 for item in value)
    ):
        raise HandoffInputError(code)
    normalized = sorted(set(value))
    if normalized != value:
        raise HandoffInputError(code + "_NOT_CANONICAL")
    return normalized


@dataclass(frozen=True)
class DiffData:
    status: str
    added: tuple[str, ...]
    removed: tuple[str, ...]
    changed: tuple[str, ...]

    @property
    def affected(self) -> tuple[str, ...]:
        return tuple(sorted(set((*self.added, *self.removed, *self.changed))))


def validate_diff_report(value: Mapping[str, object]) -> DiffData:
    if value.get("tool") != "stable-diff":
        raise HandoffInputError("DIFF_TOOL_INVALID")
    status = value.get("status")
    if status not in DIFF_STATUS_VALUES:
        raise HandoffInputError("DIFF_STATUS_INVALID")
    summary = value.get("summary")
    if not isinstance(summary, dict):
        raise HandoffInputError("DIFF_SUMMARY_INVALID")
    added = _string_list(summary.get("added"), "DIFF_ADDED_INVALID")
    removed = _string_list(summary.get("removed"), "DIFF_REMOVED_INVALID")
    changed = _string_list(summary.get("changed"), "DIFF_CHANGED_INVALID")
    if len(set((*added, *removed, *changed))) != len(added) + len(removed) + len(changed):
        raise HandoffInputError("DIFF_FIELD_SETS_OVERLAP")
    if status == "same" and any((added, removed, changed)):
        raise HandoffInputError("DIFF_SAME_HAS_CHANGES")
    if status == "changed" and not any((added, removed, changed)):
        raise HandoffInputError("DIFF_CHANGED_EMPTY")
    return DiffData(status, tuple(added), tuple(removed), tuple(changed))


def validate_context(value: Mapping[str, object]) -> dict[str, object]:
    expected = {
        "handoff_id",
        "left_artifact_ref",
        "right_artifact_ref",
        "review_scope",
        "required_reviewer_roles",
        "source_card_refs",
    }
    if set(value) != expected:
        raise HandoffInputError("CONTEXT_FIELDS_INVALID")

    handoff_id = value.get("handoff_id")
    if not isinstance(handoff_id, str) or IDENTIFIER.fullmatch(handoff_id) is None:
        raise HandoffInputError("CONTEXT_HANDOFF_ID_INVALID")

    left_ref = _bounded_string(value.get("left_artifact_ref"), "CONTEXT_LEFT_REF_INVALID")
    right_ref = _bounded_string(value.get("right_artifact_ref"), "CONTEXT_RIGHT_REF_INVALID")
    if SHA256_REF.fullmatch(left_ref) is None or SHA256_REF.fullmatch(right_ref) is None:
        raise HandoffInputError("CONTEXT_ARTIFACT_REF_NOT_DIGEST_BOUND")

    review_scope = value.get("review_scope")
    if not isinstance(review_scope, str) or IDENTIFIER.fullmatch(review_scope) is None:
        raise HandoffInputError("CONTEXT_REVIEW_SCOPE_INVALID")

    roles = _string_list(value.get("required_reviewer_roles"), "CONTEXT_ROLES_INVALID")
    if not roles or set(roles) - ROLE_VALUES:
        raise HandoffInputError("CONTEXT_ROLES_INVALID")
    source_cards = _string_list(value.get("source_card_refs"), "CONTEXT_SOURCE_CARDS_INVALID")

    return {
        "handoff_id": handoff_id,
        "left_artifact_ref": left_ref,
        "right_artifact_ref": right_ref,
        "review_scope": review_scope,
        "required_reviewer_roles": roles,
        "source_card_refs": source_cards,
    }


def validate_policy_map(value: Mapping[str, object]) -> dict[str, list[str]]:
    if set(value) != {"field_policy_map"}:
        raise HandoffInputError("POLICY_MAP_FIELDS_INVALID")
    field_map = value.get("field_policy_map")
    if not isinstance(field_map, dict) or len(field_map) > MAX_FIELDS:
        raise HandoffInputError("POLICY_MAP_INVALID")

    result: dict[str, list[str]] = {}
    for field in sorted(field_map):
        if not isinstance(field, str) or not field or len(field) > 160:
            raise HandoffInputError("POLICY_MAP_FIELD_INVALID")
        families = _string_list(field_map[field], "POLICY_MAP_FAMILY_INVALID")
        if not families:
            raise HandoffInputError("POLICY_MAP_FAMILY_EMPTY")
        result[field] = families
    return result


def _canonical_digest(value: Mapping[str, object]) -> str:
    encoded = json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def build_handoff(
    diff: DiffData,
    context: Mapping[str, object],
    field_policy_map: Mapping[str, list[str]],
    *,
    diff_sha256: str,
    context_sha256: str,
    policy_map_sha256: str | None,
) -> dict[str, object]:
    affected = list(diff.affected)
    policy_families = sorted(
        {
            family
            for field in affected
            for family in field_policy_map.get(field, [])
        }
    )
    unmapped = sorted(field for field in affected if field not in field_policy_map)
    requires_policy_review = bool(policy_families or unmapped)

    if diff.status == "same":
        handoff_state = "NO_CHANGE"
    elif unmapped:
        handoff_state = "HOLD_UNMAPPED_POLICY_IMPACT"
    else:
        handoff_state = "READY_FOR_REVIEW"

    bundle_summary = {
        "diff_status": diff.status,
        "added_fields": list(diff.added),
        "removed_fields": list(diff.removed),
        "changed_fields": list(diff.changed),
        "total_changes": len(affected),
    }
    policy_impact = {
        "affected_fields": affected,
        "policy_families": policy_families,
        "unmapped_changed_fields": unmapped,
        "requires_policy_review": requires_policy_review,
    }
    binding = {
        "handoff_id": context["handoff_id"],
        "left_artifact_ref": context["left_artifact_ref"],
        "right_artifact_ref": context["right_artifact_ref"],
        "review_scope": context["review_scope"],
        "required_reviewer_roles": context["required_reviewer_roles"],
        "source_card_refs": context["source_card_refs"],
        "diff_report_sha256": diff_sha256,
        "context_sha256": context_sha256,
        "policy_map_sha256": policy_map_sha256,
        "bundle_summary": bundle_summary,
        "policy_impact": policy_impact,
    }
    binding_digest = _canonical_digest(binding)
    subject_ref = "urn:kfm:diff-review-handoff:" + binding_digest

    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_NAME,
        "handoff_state": handoff_state,
        "bundle_summary": bundle_summary,
        "policy_impact": policy_impact,
        "review_handoff": {
            "handoff_id": context["handoff_id"],
            "subject_ref": subject_ref,
            "left_artifact_ref": context["left_artifact_ref"],
            "right_artifact_ref": context["right_artifact_ref"],
            "review_scope": context["review_scope"],
            "required_reviewer_roles": context["required_reviewer_roles"],
            "source_card_refs": context["source_card_refs"],
            "input_digests": {
                "diff_report": diff_sha256,
                "context": context_sha256,
                "policy_map": policy_map_sha256,
                "binding": binding_digest,
            },
            "review_record_schema_ref": REVIEW_SCHEMA_REF,
            "allowed_decisions": list(ALLOWED_DECISIONS),
        },
        "authority_boundary": (
            "This derived handoff binds review inputs but is not a ReviewRecord, "
            "PolicyDecision, approval, promotion, release, deployment, or publication."
        ),
    }


def json_text(value: Mapping[str, object]) -> str:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"


def _code(value: object) -> str:
    return "`" + str(value).replace("`", "") + "`"


def markdown_text(value: Mapping[str, object]) -> str:
    summary = value["bundle_summary"]
    impact = value["policy_impact"]
    handoff = value["review_handoff"]
    assert isinstance(summary, dict)
    assert isinstance(impact, dict)
    assert isinstance(handoff, dict)

    def items(values: object) -> str:
        if not isinstance(values, list) or not values:
            return "_none_"
        return ", ".join(_code(item) for item in values)

    return "\n".join(
        [
            "# KFM diff review handoff",
            "",
            f"**State:** {_code(value['handoff_state'])}",
            "",
            "## Bundle summary",
            "",
            f"- Added fields: {items(summary['added_fields'])}",
            f"- Removed fields: {items(summary['removed_fields'])}",
            f"- Changed fields: {items(summary['changed_fields'])}",
            f"- Total changes: {summary['total_changes']}",
            "",
            "## Policy impact",
            "",
            f"- Affected fields: {items(impact['affected_fields'])}",
            f"- Policy families: {items(impact['policy_families'])}",
            f"- Unmapped fields: {items(impact['unmapped_changed_fields'])}",
            "",
            "## Review binding",
            "",
            f"- Subject: {_code(handoff['subject_ref'])}",
            f"- Left artifact: {_code(handoff['left_artifact_ref'])}",
            f"- Right artifact: {_code(handoff['right_artifact_ref'])}",
            f"- Required roles: {items(handoff['required_reviewer_roles'])}",
            f"- Allowed decisions: {items(handoff['allowed_decisions'])}",
            "",
            f"> {value['authority_boundary']}",
            "",
        ]
    )


def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        delete=False,
    ) as stream:
        stream.write(content)
        temporary = Path(stream.name)
    temporary.replace(path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diff-report", required=True, type=Path)
    parser.add_argument("--context", required=True, type=Path)
    parser.add_argument("--policy-map", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--fail-on-unmapped-impact", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        diff_value = load_json_object(args.diff_report)
        context_value = load_json_object(args.context)
        policy_value = (
            load_json_object(args.policy_map)
            if args.policy_map is not None
            else {"field_policy_map": {}}
        )
        diff = validate_diff_report(diff_value)
        context = validate_context(context_value)
        field_policy_map = validate_policy_map(policy_value)
        output = build_handoff(
            diff,
            context,
            field_policy_map,
            diff_sha256=_sha256(args.diff_report),
            context_sha256=_sha256(args.context),
            policy_map_sha256=_sha256(args.policy_map) if args.policy_map else None,
        )
        rendered = json_text(output) if args.format == "json" else markdown_text(output)
        if args.output is not None:
            _write_atomic(args.output, rendered)
        print(rendered, end="")
        impact = output["policy_impact"]
        assert isinstance(impact, dict)
        if args.fail_on_unmapped_impact and impact["unmapped_changed_fields"]:
            return 1
        return 0
    except HandoffInputError as exc:
        print(
            json_text(
                {
                    "schema_version": SCHEMA_VERSION,
                    "tool": TOOL_NAME,
                    "handoff_state": "ERROR",
                    "error": {"code": str(exc)},
                    "authority_boundary": (
                        "No review, policy, promotion, release, deployment, or "
                        "publication authority was created."
                    ),
                }
            ),
            end="",
        )
        return 2
    except OSError:
        print(
            json_text(
                {
                    "schema_version": SCHEMA_VERSION,
                    "tool": TOOL_NAME,
                    "handoff_state": "ERROR",
                    "error": {"code": "OUTPUT_WRITE_ERROR"},
                    "authority_boundary": (
                        "No review, policy, promotion, release, deployment, or "
                        "publication authority was created."
                    ),
                }
            ),
            end="",
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
