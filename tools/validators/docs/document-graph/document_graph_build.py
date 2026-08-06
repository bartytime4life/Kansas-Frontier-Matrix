"""Graph construction and finite QA outcomes for KFM documentation graph QA."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import asdict, replace
from pathlib import Path, PurePosixPath
from typing import Mapping, Sequence

from document_graph_core import (
    FAIL,
    INFO,
    MAX_FINDINGS,
    MAX_REPORT_DOCS,
    MARKDOWN_SUFFIXES,
    RELATION_KEYS,
    WARN,
    DocumentGraphError,
    Edge,
    Finding,
    GraphResult,
    _digest,
    _inside,
    _ratchet_findings,
    _relative,
    _sort_finding,
)
from document_graph_parse import (
    _changed,
    _collect,
    _first_heading,
    _read,
    _registry,
    _target,
    extract_links,
    parse_metadata,
)

def build_document_graph(
    *, repo_root: Path, inputs: Sequence[str], entrypoints: Sequence[str],
    registry_path: str | None = None, git_diff: str | None = None,
    warnings_as_errors: bool = False,
) -> GraphResult:
    root = repo_root.resolve()
    paths, changed = _collect(root, inputs), _changed(root, git_diff)
    texts = {_relative(path, root): _read(path) for path in paths}
    metadata = {path: parse_metadata(text) for path, text in texts.items()}
    nodes: dict[str, dict[str, object]] = {}
    findings: list[Finding] = []
    for path, text in texts.items():
        meta = metadata[path]
        nodes[path] = {
            "path": path, "doc_id": meta.doc_id,
            "title": meta.title or _first_heading(text) or PurePosixPath(path).name,
            "document_type": meta.document_type, "status": meta.status,
            "owner": meta.owner, "policy_label": meta.policy_label,
            "metadata_source": meta.source_kind,
        }
        findings.extend(
            Finding(WARN, warning, path, (), "bounded metadata construct not interpreted")
            for warning in meta.warnings
        )
        if meta.source_kind and not meta.doc_id:
            findings.append(Finding(WARN, "DOC_ID_MISSING", path, (), "metadata-bearing document has no stable identity"))

    id_index: dict[str, list[str]] = defaultdict(list)
    for path, node in nodes.items():
        if node["doc_id"]:
            id_index[str(node["doc_id"])].append(path)
    for members in id_index.values():
        if len(members) > 1:
            findings.append(Finding(FAIL, "DUPLICATE_DOC_ID", members[0], tuple(members[1:]), "stable identity is duplicated"))

    edges: set[Edge] = set()
    outside_scope = external = 0
    for path, text in texts.items():
        source = root / path
        for line, raw_target in extract_links(text):
            target, kind = _target(root, source, raw_target)
            if kind == "external":
                external += 1
            elif kind == "escape":
                findings.append(Finding(FAIL, "PATH_ESCAPE", path, (), "Markdown relationship escapes repository root"))
            elif target is not None:
                relative = _relative(target, root)
                if relative in nodes and relative != path:
                    edges.add(Edge(path, relative, "markdown_link", line))
                elif target.is_file() and target.suffix.casefold() in MARKDOWN_SUFFIXES:
                    outside_scope += 1
        meta = metadata[path]
        for relation in RELATION_KEYS:
            for value in getattr(meta, relation):
                if value.startswith("kfm://"):
                    matches = id_index.get(value, [])
                    if len(matches) == 1:
                        edges.add(Edge(path, matches[0], f"metadata_{relation}", 0))
                    elif not matches:
                        findings.append(Finding(FAIL, "RELATED_DOC_ID_MISSING", path, (), "declared document identity has no in-scope target"))
                    continue
                target, kind = _target(root, source, value)
                if kind == "external":
                    external += 1
                elif kind == "escape":
                    findings.append(Finding(FAIL, "PATH_ESCAPE", path, (), "metadata relationship escapes repository root"))
                elif target is None or not target.exists():
                    findings.append(Finding(FAIL, "RELATED_TARGET_MISSING", path, (), "declared relationship target does not exist"))
                else:
                    relative = _relative(target, root)
                    if relative in nodes and relative != path:
                        edges.add(Edge(path, relative, f"metadata_{relation}", 0))
                    elif target.suffix.casefold() in MARKDOWN_SUFFIXES:
                        outside_scope += 1

    registry_state = {path: "not_checked" for path in nodes}
    registered_markdown = 0
    if registry_path:
        registry_file = (root / registry_path).resolve(strict=False)
        if not _inside(registry_file, root):
            raise DocumentGraphError("registry path escapes repository root")
        entries, warnings = _registry(registry_file)
        registry_relative = _relative(registry_file, root)
        findings.extend(Finding(WARN, warning, registry_relative, (), "bounded registry construct not interpreted") for warning in warnings)
        seen_ids: dict[str, str] = {}
        seen_paths: dict[str, str] = {}
        for entry in entries:
            if entry.doc_id in seen_ids:
                findings.append(Finding(FAIL, "REGISTRY_DOC_ID_DUPLICATE", registry_relative, (seen_ids[entry.doc_id], entry.path), "registry identity is duplicated"))
            seen_ids.setdefault(entry.doc_id, entry.path)
            if entry.path in seen_paths:
                findings.append(Finding(FAIL, "REGISTRY_PATH_DUPLICATE", registry_relative, (entry.path,), "registry path is duplicated"))
            seen_paths.setdefault(entry.path, entry.doc_id)
            if PurePosixPath(entry.path).suffix.casefold() not in MARKDOWN_SUFFIXES:
                continue
            registered_markdown += 1
            target = (root / entry.path).resolve(strict=False)
            if not _inside(target, root) or not target.is_file():
                findings.append(Finding(FAIL, "REGISTRY_TARGET_MISSING", registry_relative, (entry.path,), "registered Markdown target does not exist"))
            elif entry.path not in nodes:
                outside_scope += 1
            else:
                registry_state[entry.path] = "registered"
                node_id = nodes[entry.path]["doc_id"]
                if not node_id:
                    registry_state[entry.path] = "registered_unbound"
                    findings.append(Finding(WARN, "REGISTRY_DOC_ID_UNBOUND", entry.path, (registry_relative,), "registered document declares no identity"))
                elif node_id != entry.doc_id:
                    registry_state[entry.path] = "mismatch"
                    findings.append(Finding(FAIL, "REGISTRY_DOC_ID_MISMATCH", entry.path, (registry_relative,), "registry and document identities differ"))
        for path, node in nodes.items():
            if node["doc_id"] and registry_state[path] == "not_checked":
                registry_state[path] = "unregistered"

    resolved_entries: list[str] = []
    for raw in entrypoints:
        candidate = (root / raw).resolve(strict=False)
        if not _inside(candidate, root):
            raise DocumentGraphError("entrypoint escapes repository root")
        if candidate.is_dir():
            candidate /= "README.md"
        relative = _relative(candidate, root)
        if relative not in nodes:
            raise DocumentGraphError("entrypoint is outside supplied graph scope")
        resolved_entries.append(relative)
    if not resolved_entries:
        resolved_entries = [path for path in ("README.md", "docs/README.md") if path in nodes]
    if not resolved_entries:
        raise DocumentGraphError("no graph entrypoint is available")

    outgoing = {path: set() for path in nodes}
    incoming = {path: set() for path in nodes}
    for edge in edges:
        outgoing[edge.source].add(edge.target)
        incoming[edge.target].add(edge.source)
    reachable: set[str] = set()
    queue = deque(sorted(set(resolved_entries)))
    while queue:
        current = queue.popleft()
        if current in reachable:
            continue
        reachable.add(current)
        queue.extend(sorted(outgoing[current] - reachable))
    entry_set = set(resolved_entries)
    for path in sorted(nodes):
        if path not in entry_set and not incoming[path]:
            findings.append(Finding(WARN, "DOC_ORPHANED", path, (), "document has no inbound graph edge"))
        if path not in reachable:
            findings.append(Finding(WARN, "DOC_UNREACHABLE", path, (), "document is not reachable from an entrypoint"))

    adjusted = list(_ratchet_findings(findings, changed, git_diff_active=git_diff is not None))
    if warnings_as_errors:
        adjusted = [replace(item, severity=FAIL) if item.severity == WARN and not item.historical else item for item in adjusted]
        adjusted.sort(key=_sort_finding)
    if len(adjusted) > MAX_FINDINGS:
        adjusted = adjusted[: MAX_FINDINGS - 1] + [Finding(WARN, "FINDINGS_TRUNCATED", ".", (), "findings exceeded bounded output")]

    documents: list[Mapping[str, object]] = []
    for path in sorted(nodes):
        documents.append({
            **nodes[path], "reachable": path in reachable, "entrypoint": path in entry_set,
            "inbound_count": len(incoming[path]), "outbound_count": len(outgoing[path]),
            "backlinks": sorted(incoming[path]), "outgoing": sorted(outgoing[path]),
            "registry_state": registry_state[path],
        })
    if len(documents) > MAX_REPORT_DOCS:
        raise DocumentGraphError("document report exceeds bounded output")

    fail_count = sum(item.severity == FAIL for item in adjusted)
    warn_count = sum(item.severity == WARN for item in adjusted)
    info_count = sum(item.severity == INFO for item in adjusted)
    outcome = "DOC_GRAPH_FAIL" if fail_count else "DOC_GRAPH_WARN" if warn_count else "DOC_GRAPH_PASS"
    counts = {
        "documents": len(nodes), "edges": len(edges),
        "reachable_documents": len(reachable),
        "unreachable_documents": len(nodes) - len(reachable),
        "orphan_documents": sum(path not in entry_set and not incoming[path] for path in nodes),
        "documents_with_doc_id": sum(bool(node["doc_id"]) for node in nodes.values()),
        "registered_markdown_documents": registered_markdown,
        "changed_documents": sum(path in changed for path in nodes),
        "outside_scope_markdown_targets": outside_scope,
        "external_targets_unverified": external,
        "fail_findings": fail_count, "warn_findings": warn_count,
        "info_findings": info_count,
    }
    graph_material = {
        "entrypoints": sorted(entry_set),
        "documents": [
            {"path": item["path"], "doc_id": item["doc_id"], "outgoing": item["outgoing"]}
            for item in documents
        ],
        "edges": [asdict(edge) for edge in sorted(edges)],
    }
    limitations = (
        "Reachability and orphan status are bounded to supplied Markdown scope and entrypoints.",
        "The existing link-check lane remains responsible for target, fragment, case, and path QA.",
        "Only top-level identity and relationship metadata fields are consumed.",
        "Registry comparison is limited to entries carrying doc_id and path.",
        "A passing report does not establish truth, policy, review, release, publication, or maturity.",
    )
    return GraphResult(
        outcome, git_diff or "full_supplied_scope", _digest(graph_material),
        tuple(sorted(entry_set)), tuple(sorted(path for path in nodes if path in changed)),
        tuple(documents), tuple(sorted(edges)), tuple(adjusted), counts, limitations,
    )


def _error_result() -> GraphResult:
    finding = Finding(FAIL, "ERROR", ".", (), "bounded document-graph operation failed")
    counts = {
        "documents": 0, "edges": 0, "reachable_documents": 0,
        "unreachable_documents": 0, "orphan_documents": 0,
        "documents_with_doc_id": 0, "registered_markdown_documents": 0,
        "changed_documents": 0, "outside_scope_markdown_targets": 0,
        "external_targets_unverified": 0, "fail_findings": 1,
        "warn_findings": 0, "info_findings": 0,
    }
    return GraphResult(
        "ERROR", "error", "sha256:" + "0" * 64, (), (), (), (), (finding,),
        counts, ("The document graph could not be computed safely.",),
    )

