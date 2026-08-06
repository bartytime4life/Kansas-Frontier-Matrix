"""Shared models and deterministic rendering for KFM documentation graph QA."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from dataclasses import asdict, dataclass, replace
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping

MAX_BYTES = 5_000_000
MAX_DOCS = 20_000
MAX_REPORT_DOCS = 5_000
MAX_FINDINGS = 1_000
MARKDOWN_SUFFIXES = frozenset({".md", ".markdown"})
FAIL, WARN, INFO = "FAIL", "WARN", "INFO"
SEVERITY_ORDER = {FAIL: 0, WARN: 1, INFO: 2}
RELATION_KEYS = ("related", "supersedes", "superseded_by")


class DocumentGraphError(RuntimeError):
    """A bounded graph operation could not complete safely."""


@dataclass(frozen=True, order=True)
class Edge:
    source: str
    target: str
    relation: str
    line: int


@dataclass(frozen=True, order=True)
class Finding:
    severity: str
    code: str
    path: str
    related_paths: tuple[str, ...]
    detail: str
    historical: bool = False


@dataclass(frozen=True)
class Metadata:
    source_kind: str | None
    doc_id: str | None
    title: str | None
    document_type: str | None
    status: str | None
    owner: str | None
    policy_label: str | None
    related: tuple[str, ...]
    supersedes: tuple[str, ...]
    superseded_by: tuple[str, ...]
    warnings: tuple[str, ...]


@dataclass(frozen=True)
class RegistryEntry:
    doc_id: str
    path: str


@dataclass(frozen=True)
class GraphResult:
    outcome: str
    scope: str
    graph_digest: str
    entrypoints: tuple[str, ...]
    changed_documents: tuple[str, ...]
    documents: tuple[Mapping[str, object], ...]
    edges: tuple[Edge, ...]
    findings: tuple[Finding, ...]
    counts: Mapping[str, int]
    limitations: tuple[str, ...]

    @property
    def exit_code(self) -> int:
        return 2 if self.outcome == "ERROR" else 1 if self.outcome == "DOC_GRAPH_FAIL" else 0

    def to_payload(self) -> dict[str, object]:
        return {
            "profile": "kfm.docs.document-graph.v1",
            "outcome": self.outcome,
            "scope": self.scope,
            "graph_digest": self.graph_digest,
            "entrypoints": list(self.entrypoints),
            "changed_documents": list(self.changed_documents),
            "counts": dict(sorted(self.counts.items())),
            "documents": list(self.documents),
            "edges": [asdict(edge) for edge in self.edges],
            "findings": [asdict(finding) for finding in self.findings],
            "limitations": list(self.limitations),
        }

    def to_json(self) -> str:
        return json.dumps(
            self.to_payload(), sort_keys=True, separators=(",", ":"), ensure_ascii=False
        )

    def to_text(self) -> str:
        lines = [
            self.outcome,
            f"scope={self.scope}",
            f"graph_digest={self.graph_digest}",
            " ".join(f"{key}={value}" for key, value in sorted(self.counts.items())),
        ]
        lines.extend(
            f"{finding.severity}{' historical' if finding.historical else ''} "
            f"{finding.code} {finding.path}"
            for finding in self.findings
        )
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = [
            "# KFM Documentation Graph Workbench", "",
            f"**Outcome:** `{self.outcome}`  ",
            f"**Scope:** `{_escape(self.scope)}`  ",
            f"**Graph digest:** `{self.graph_digest}`", "",
            "> This is a deterministic documentation-QA projection. It is not doctrine,",
            "> evidence closure, policy approval, review, release, publication, or a",
            "> Directory Rules exception.", "", "## Summary", "",
            "| Measure | Count |", "|---|---:|",
        ]
        for key in (
            "documents", "edges", "reachable_documents", "unreachable_documents",
            "orphan_documents", "documents_with_doc_id",
            "registered_markdown_documents", "fail_findings", "warn_findings",
            "info_findings",
        ):
            lines.append(f"| `{key}` | {self.counts.get(key, 0)} |")
        lines.extend(["", "## Entrypoints", ""])
        lines.extend(
            f"- [`{_escape(path)}`]({_quote(path)})" for path in self.entrypoints
        )
        if not self.entrypoints:
            lines.append("- None")

        groups: dict[str, list[Mapping[str, object]]] = defaultdict(list)
        for document in self.documents:
            groups[_group(str(document["path"]))].append(document)
        lines.extend(["", "## Generated Maps of Content", ""])
        for group in sorted(groups):
            lines.extend(
                [
                    f"### `{_escape(group)}`", "",
                    "| Document | Title | In | Out | Reachable | Registry |",
                    "|---|---|---:|---:|:---:|---|",
                ]
            )
            for document in sorted(groups[group], key=lambda item: str(item["path"])):
                path = str(document["path"])
                lines.append(
                    f"| [`{_escape(path)}`]({_quote(path)}) | "
                    f"{_table(str(document.get('title') or ''))} | "
                    f"{document['inbound_count']} | {document['outbound_count']} | "
                    f"{'yes' if document['reachable'] else 'no'} | "
                    f"{_table(str(document['registry_state']))} |"
                )
            lines.append("")

        lines.extend(["## Backlink Index", ""])
        backlink_docs = [item for item in self.documents if item.get("backlinks")]
        if not backlink_docs:
            lines.append("No inbound documentation relationship was found.")
        for document in sorted(
            backlink_docs, key=lambda item: (-int(item["inbound_count"]), str(item["path"]))
        )[:200]:
            path = str(document["path"])
            lines.extend([f"### [`{_escape(path)}`]({_quote(path)})", ""])
            lines.extend(
                f"- [`{_escape(str(backlink))}`]({_quote(str(backlink))})"
                for backlink in document["backlinks"]
            )
            lines.append("")

        lines.extend(["## Findings", ""])
        if not self.findings:
            lines.append("No configured document-graph finding was emitted.")
        else:
            lines.extend(
                ["| Severity | Code | Path | Historical |", "|---|---|---|:---:|"]
            )
            for finding in self.findings[:300]:
                lines.append(
                    f"| {finding.severity} | `{finding.code}` | "
                    f"`{_table(finding.path)}` | "
                    f"{'yes' if finding.historical else 'no'} |"
                )
        lines.extend(["", "## Limits", ""])
        lines.extend(f"- {_escape(value)}" for value in self.limitations)
        return "\n".join(lines) + "\n"


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("`", "\\`")


def _table(value: str) -> str:
    return _escape(value.replace("|", "\\|").replace("\n", " "))[:200]


def _quote(path: str) -> str:
    return path.replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def _digest(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _sort_finding(finding: Finding) -> tuple[object, ...]:
    return (
        SEVERITY_ORDER.get(finding.severity, 99), finding.code, finding.path,
        finding.related_paths, finding.historical,
    )


def _ratchet_findings(
    findings: Iterable[Finding], changed: frozenset[str], *, git_diff_active: bool
) -> tuple[Finding, ...]:
    adjusted: list[Finding] = []
    for finding in findings:
        if not git_diff_active or finding.path in changed or any(
            path in changed for path in finding.related_paths
        ):
            adjusted.append(finding)
        elif finding.code not in {"DOC_ORPHANED", "DOC_UNREACHABLE", "DOC_ID_MISSING"}:
            adjusted.append(replace(finding, severity=WARN, historical=True))
    return tuple(sorted(adjusted, key=_sort_finding))


def _group(path: str) -> str:
    parts = PurePosixPath(path).parts
    if len(parts) == 1:
        return "repository-root"
    if len(parts) >= 2 and parts[0] == "docs":
        return "/".join(parts[:2])
    if len(parts) >= 3 and parts[:3] == ("tools", "validators", "docs"):
        return "/".join(parts[:4]) if len(parts) >= 4 else "/".join(parts)
    return parts[0] if parts else "."
