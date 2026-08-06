#!/usr/bin/env python3
"""Validate bounded KFM documentation metadata blocks without network access.

The validator inspects explicitly supplied Markdown files, validates the
``KFM_META_BLOCK_V2`` envelope and a conservative structural field profile,
and can compare valid identities with the existing machine document registry.
It emits a review-only registry delta; it never edits documentation or the
registry and never decides doctrine, evidence, policy, review, release, or
publication authority.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, replace
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

MAX_MARKDOWN_BYTES = 5_000_000
MAX_DOCUMENTS = 20_000
MAX_REPORT_DOCUMENTS = 5_000
MAX_FINDINGS = 2_000
MARKDOWN_SUFFIXES = frozenset({".md", ".markdown"})
PROFILE_PRESENT = "present"
PROFILE_REQUIRED = "required"
SEVERITY_FAIL = "FAIL"
SEVERITY_WARN = "WARN"
SEVERITY_INFO = "INFO"
SEVERITY_ORDER = {
    SEVERITY_FAIL: 0,
    SEVERITY_WARN: 1,
    SEVERITY_INFO: 2,
}
GIT_DIFF_RE = re.compile(
    r"^[0-9a-fA-F]{7,40}\.\.\.(?:HEAD|[0-9a-fA-F]{7,40})$"
)
META_BLOCK_RE = re.compile(
    r"<!--\s*\[KFM_META_BLOCK_V2\]\s*(.*?)\s*"
    r"\[/KFM_META_BLOCK_V2\]\s*-->",
    re.DOTALL | re.IGNORECASE,
)
LEGACY_BLOCK_RE = re.compile(
    r"<!--\s*KFM_DOCUMENT_CONTROL\s*(.*?)-->",
    re.DOTALL | re.IGNORECASE,
)
KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")
DOC_ID_RE = re.compile(r"^kfm://[A-Za-z0-9][A-Za-z0-9._~:/-]{2,255}$")
TYPE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,95}$")
ROOT_RE = re.compile(r"^(?:repository-root|[A-Za-z0-9_.-]+/)$")
KNOWN_TRUTH_MARKERS = (
    "confirmed",
    "proposed",
    "unknown",
    "needs verification",
    "cite-or-abstain",
    "cite or abstain",
)
ROOT_PREFIXES = frozenset(
    {
        ".github", "apps", "artifacts", "catalog", "configs", "connectors",
        "contracts", "control_plane", "data", "docs", "examples", "fixtures",
        "infra", "jsonschema", "migrations", "packages", "pipeline_specs",
        "pipelines", "policies", "policy", "release", "runtime", "schemas",
        "scripts", "src", "styles", "tests", "tools", "ui",
        "viewer_templates", "web",
    }
)
REQUIRED_FIELDS = (
    "doc_id",
    "title",
    "type",
    "version",
    "status",
    "created",
    "updated",
    "policy_label",
    "owning_root",
    "responsibility",
    "truth_posture",
)


class MetaBlockError(RuntimeError):
    """A bounded metadata validation operation could not complete safely."""


@dataclass(frozen=True, order=True)
class Finding:
    severity: str
    code: str
    path: str
    field: str
    detail: str
    related_paths: tuple[str, ...] = ()
    historical: bool = False


@dataclass(frozen=True, order=True)
class RegistryEntry:
    doc_id: str
    path: str
    kind: str | None = None
    status: str | None = None
    authority: str | None = None


@dataclass(frozen=True, order=True)
class RegistryDelta:
    action: str
    doc_id: str
    path: str
    reason_code: str
    proposed_fields: tuple[tuple[str, str], ...]
    unresolved_fields: tuple[str, ...]

    def to_payload(self) -> dict[str, object]:
        return {
            "action": self.action,
            "doc_id": self.doc_id,
            "path": self.path,
            "reason_code": self.reason_code,
            "proposed_fields": dict(self.proposed_fields),
            "unresolved_fields": list(self.unresolved_fields),
        }


def _owner_values(metadata: Mapping[str, object]) -> tuple[str, ...]:
    """Return normalized owner/owners values without interpreting identity."""

    owner = metadata.get("owner")
    owners = metadata.get("owners")
    values: list[str] = []
    if isinstance(owner, str) and owner.strip():
        values.append(owner.strip())
    if isinstance(owners, list):
        values.extend(str(item).strip() for item in owners if str(item).strip())
    elif isinstance(owners, str) and owners.strip():
        values.append(owners.strip())
    return tuple(values)


@dataclass(frozen=True)
class DocumentRecord:
    path: str
    meta_block_state: str
    metadata: Mapping[str, object]
    metadata_digest: str | None
    first_line: int | None
    registry_state: str

    def to_payload(self) -> dict[str, object]:
        payload: dict[str, object] = {
            "path": self.path,
            "meta_block_state": self.meta_block_state,
            "metadata_digest": self.metadata_digest,
            "first_line": self.first_line,
            "registry_state": self.registry_state,
        }
        for key in (
            "doc_id",
            "title",
            "type",
            "version",
            "status",
            "policy_label",
            "owning_root",
            "truth_posture",
        ):
            value = self.metadata.get(key)
            if isinstance(value, str):
                payload[key] = value
        owner = _owner_values(self.metadata)
        if owner:
            payload["owners"] = list(owner)
        return payload


@dataclass(frozen=True)
class MetaBlockResult:
    outcome: str
    scope: str
    profile: str
    report_digest: str
    changed_documents: tuple[str, ...]
    documents: tuple[DocumentRecord, ...]
    findings: tuple[Finding, ...]
    registry_delta: tuple[RegistryDelta, ...]
    counts: Mapping[str, int]
    limitations: tuple[str, ...]

    @property
    def exit_code(self) -> int:
        if self.outcome == "ERROR":
            return 2
        if self.outcome == "DOC_META_BLOCK_FAIL":
            return 1
        return 0

    def to_payload(self) -> dict[str, object]:
        return {
            "profile": "kfm.docs.meta-block.v1",
            "outcome": self.outcome,
            "scope": self.scope,
            "validation_profile": self.profile,
            "report_digest": self.report_digest,
            "changed_documents": list(self.changed_documents),
            "counts": dict(sorted(self.counts.items())),
            "documents": [item.to_payload() for item in self.documents],
            "findings": [asdict(item) for item in self.findings],
            "registry_delta": [item.to_payload() for item in self.registry_delta],
            "limitations": list(self.limitations),
        }

    def to_json(self) -> str:
        return json.dumps(
            self.to_payload(),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )

    def to_text(self) -> str:
        lines = [
            self.outcome,
            f"scope={self.scope}",
            f"profile={self.profile}",
            f"report_digest={self.report_digest}",
            " ".join(
                f"{key}={value}" for key, value in sorted(self.counts.items())
            ),
        ]
        lines.extend(
            f"{item.severity}{' historical' if item.historical else ''} "
            f"{item.code} {item.path} {item.field}"
            for item in self.findings
        )
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = [
            "# KFM Documentation Metadata Workbench",
            "",
            f"**Outcome:** `{self.outcome}`  ",
            f"**Scope:** `{_escape(self.scope)}`  ",
            f"**Profile:** `{self.profile}`  ",
            f"**Report digest:** `{self.report_digest}`",
            "",
            "> This is deterministic documentation QA. It is not doctrine, evidence",
            "> closure, source admission, policy approval, human review, release,",
            "> publication, or a Directory Rules exception.",
            "",
            "## Summary",
            "",
            "| Measure | Count |",
            "|---|---:|",
        ]
        for key in (
            "documents",
            "metadata_blocks",
            "missing_metadata_blocks",
            "valid_metadata_blocks",
            "invalid_metadata_blocks",
            "registered_documents",
            "registry_add_candidates",
            "registry_conflicts",
            "fail_findings",
            "warn_findings",
            "info_findings",
        ):
            lines.append(f"| `{key}` | {self.counts.get(key, 0)} |")

        lines.extend(["", "## Review-only document-registry delta", ""])
        if not self.registry_delta:
            lines.append("No registry delta was emitted for the current review scope.")
        else:
            lines.extend(
                [
                    "| Action | Document ID | Path | Reason | Unresolved |",
                    "|---|---|---|---|---|",
                ]
            )
            for item in self.registry_delta[:300]:
                unresolved = ", ".join(item.unresolved_fields) or "—"
                lines.append(
                    f"| `{item.action}` | `{_table(item.doc_id)}` | "
                    f"`{_table(item.path)}` | `{item.reason_code}` | "
                    f"{_table(unresolved)} |"
                )
        lines.extend(
            [
                "",
                "> The delta is a review candidate only. The validator never writes or",
                "> authorizes `control_plane/document_registry.yaml`.",
                "",
                "## Findings",
                "",
            ]
        )
        if not self.findings:
            lines.append("No configured metadata finding was emitted.")
        else:
            lines.extend(
                [
                    "| Severity | Code | Path | Field | Historical |",
                    "|---|---|---|---|:---:|",
                ]
            )
            for item in self.findings[:300]:
                lines.append(
                    f"| {item.severity} | `{item.code}` | `{_table(item.path)}` | "
                    f"`{_table(item.field)}` | "
                    f"{'yes' if item.historical else 'no'} |"
                )
        lines.extend(["", "## Limits", ""])
        lines.extend(f"- {_escape(item)}" for item in self.limitations)
        return "\n".join(lines) + "\n"

    def registry_delta_json(self) -> str:
        payload = {
            "profile": "kfm.docs.document-registry-delta.v1",
            "source_report_digest": self.report_digest,
            "scope": self.scope,
            "review_only": True,
            "mutates_registry": False,
            "entries": [item.to_payload() for item in self.registry_delta],
        }
        payload["delta_digest"] = _digest(payload)
        return json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("`", "\\`")


def _table(value: str) -> str:
    return _escape(value.replace("|", "\\|").replace("\n", " "))[:240]


def _digest(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


