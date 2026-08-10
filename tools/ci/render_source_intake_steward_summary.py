#!/usr/bin/env python3
"""Render a deterministic steward-facing Markdown summary from SourceIntakeRecord.

This is a presentation-only projection. It validates one local intake record,
performs no network access, and creates no evidence, policy, review, promotion,
release, notification, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators import validate_source_intake_record as intake_validator

SUMMARY_TITLE = "Source Intake Steward Summary"
SCOPE = "source-intake-steward-summary-presentation-only-v1"
MARKDOWN_META = re.compile(r"([\\`*_{}\[\]()<>#+\-.!|>])")


@dataclass(frozen=True)
class SummaryRenderResult:
    markdown: str
    status: str
    blocking: bool
    exit_code: int
    source_record_sha256: str


class SummaryRenderError(ValueError):
    """Value-free deterministic failure for invalid input or output handling."""

    def __init__(self, code: str, field: str) -> None:
        super().__init__(code)
        self.code = code
        self.field = field


def _escape_text(value: str) -> str:
    return MARKDOWN_META.sub(r"\\\1", value)


def _code(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|")
    return f"`{escaped}`"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
    except OSError as exc:
        raise SummaryRenderError("INPUT_READ_ERROR", "/") from exc
    return "sha256:" + digest.hexdigest()


def _validated_record(path: Path) -> dict[str, Any]:
    result = intake_validator.validate(path)
    if not result.ok:
        first = result.findings[0] if result.findings else None
        code = first.code if first is not None else "SOURCE_INTAKE_INVALID"
        field = first.field if first is not None else "/"
        raise SummaryRenderError(code, field)
    value, findings = intake_validator._read(path)
    if value is None or findings:
        first = findings[0] if findings else intake_validator.Finding("SOURCE_INTAKE_INVALID", "/")
        raise SummaryRenderError(first.code, first.field)
    return value


def _policy_implications(record: Mapping[str, Any], drift: Mapping[str, Any]) -> list[str]:
    implications = ["PROMOTION_REQUIRED"]
    if record.get("evidence_bundle_resolved") is not True:
        implications.append("EVIDENCE_BUNDLE_UNRESOLVED")
    if record.get("policy_review_required") is True:
        implications.append("POLICY_REVIEW_REQUIRED")
    sensitivity = drift.get("sensitive_implication")
    if isinstance(sensitivity, str) and sensitivity != "NONE":
        implications.append("SENSITIVITY_" + sensitivity)
    if drift.get("public_detail_allowed") is not True:
        implications.append("PUBLIC_DETAIL_DENIED")
    return sorted(set(implications))


def _status_and_actions(record: Mapping[str, Any], drift: Mapping[str, Any]) -> tuple[str, bool, list[str]]:
    disposition = record.get("disposition")
    rollback_declared = isinstance(drift.get("prior_identity_ref"), str)
    if disposition == "NO_MATERIAL_CHANGE":
        return "NO_ACTION", False, ["NO_ACTION", "REQUEST_EXPANSION"]
    if disposition == "PROPOSED_WORK_RECORD" and rollback_declared:
        return "READY_FOR_REVIEW", False, [
            "DENY", "ESCALATE", "REQUEST_EXPANSION", "REVIEW_FOR_PROCESSED"
        ]
    if disposition == "PROPOSED_WORK_RECORD":
        return "HOLD", True, ["DENY", "ESCALATE", "REQUEST_EXPANSION"]
    if disposition == "QUARANTINED":
        return "HOLD", True, ["DENY", "ESCALATE", "REQUEST_EXPANSION"]
    return "HOLD", True, ["ESCALATE", "REQUEST_EXPANSION"]


def _code_list(values: object) -> str:
    if not isinstance(values, list) or not values:
        return "—"
    return ", ".join(_code(str(value)) for value in values)


def render_source_intake_steward_summary(path: Path, output_path: Path | None = None) -> SummaryRenderResult:
    """Validate one SourceIntakeRecord and render its bounded Markdown projection."""

    record = _validated_record(path)
    drift = record["drift_summary"]
    status, blocking, actions = _status_and_actions(record, drift)
    digest = _sha256(path)
    sensitive = drift.get("sensitive_implication") != "NONE" or drift.get("public_detail_allowed") is not True
    rollback_target = drift.get("prior_identity_ref")

    lines = [
        f"# {SUMMARY_TITLE}",
        "",
        f"- **Status:** {_code(status)}",
        f"- **Blocking:** {_code('true' if blocking else 'false')}",
        f"- **Source record digest:** {_code(digest)}",
        f"- **Intake:** {_code(str(record['intake_id']))}",
        f"- **Source:** {_code(str(record['source_descriptor_ref']))}",
        f"- **Disposition:** {_code(str(record['disposition']))}",
        f"- **Drift kind:** {_code(str(drift['drift_kind']))}",
        f"- **Materiality:** {_code(str(drift['materiality']))}",
        "",
        "## What changed",
        "",
    ]
    if sensitive:
        lines.append("Sensitive or non-public drift detail is redacted from this summary.")
        lines.append("")
        lines.append(f"- **Change codes:** {_code_list(drift.get('change_codes'))}")
        lines.append("- **Changed fields:** `REDACTED`")
    else:
        lines.append(_escape_text(str(drift["summary"])))
        lines.append("")
        lines.append(f"- **Change codes:** {_code_list(drift.get('change_codes'))}")
        lines.append(f"- **Changed fields:** {_code_list(drift.get('changed_fields'))}")

    lines.extend([
        "",
        "## Materiality reason",
        "",
        f"- **Reason codes:** {_code_list(record.get('reason_codes'))}",
        f"- **Policy implications:** {_code_list(_policy_implications(record, drift))}",
        "",
        "## Rollback posture",
        "",
        f"- **Rollback target:** {_code(str(rollback_target)) if isinstance(rollback_target, str) else '`NOT_DECLARED`'}",
    ])
    if not isinstance(rollback_target, str):
        lines.append("- **Hold reason:** `ROLLBACK_TARGET_NOT_DECLARED`")

    lines.extend([
        "",
        "## Next-action options",
        "",
    ])
    lines.extend(f"- {_code(action)}" for action in actions)
    lines.extend([
        "",
        "## Boundary",
        "",
        "This deterministic Markdown is a presentation-only projection of one validated "
        "`SourceIntakeRecord`. It does not fetch a source, expose restricted details, "
        "resolve evidence, decide policy, approve review, mutate a candidate, notify, "
        "promote, release, publish, or authorize public use.",
        "",
    ])
    markdown = "\n".join(lines)
    if output_path is not None:
        try:
            if output_path.is_symlink():
                raise SummaryRenderError("OUTPUT_SYMLINK_DENIED", "/output")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown, encoding="utf-8", newline="\n")
        except SummaryRenderError:
            raise
        except OSError as exc:
            raise SummaryRenderError("OUTPUT_WRITE_ERROR", "/output") from exc
    return SummaryRenderResult(
        markdown=markdown,
        status=status,
        blocking=blocking,
        exit_code=1 if blocking else 0,
        source_record_sha256=digest,
    )


def _error_payload(error: SummaryRenderError) -> str:
    return json.dumps({
        "object_type": "SourceIntakeStewardSummaryRenderError",
        "outcome": "ERROR",
        "code": error.code,
        "field": error.field,
        "scope": SCOPE,
        "authority_created": False,
    }, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a steward summary from one validated SourceIntakeRecord.")
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = render_source_intake_steward_summary(args.record, args.output)
    except SummaryRenderError as error:
        print(_error_payload(error))
        return 2
    if args.output is None:
        print(result.markdown, end="")
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
