"""Machine document-registry comparison and changed-file ratcheting."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from typing import Iterable, Sequence

from meta_block_core import (
    MAX_FINDINGS, SEVERITY_FAIL, SEVERITY_INFO, SEVERITY_ORDER, SEVERITY_WARN,
    DocumentRecord, Finding, MetaBlockError, RegistryDelta, RegistryEntry,
)
from meta_block_parse import _scalar
from meta_block_validate import _string

def _parse_registry(path: Path) -> tuple[tuple[RegistryEntry, ...], list[Finding]]:
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 2_000_000:
            raise MetaBlockError("document registry is not a bounded regular file")
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        raise MetaBlockError("document registry could not be read") from error

    in_entries = False
    current: dict[str, str] | None = None
    raw_entries: list[dict[str, str]] = []
    findings: list[Finding] = []

    def flush() -> None:
        nonlocal current
        if current is not None:
            raw_entries.append(current)
        current = None

    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not in_entries:
            in_entries = stripped == "entries:"
            continue
        if not raw.startswith(" "):
            flush()
            break
        if raw.startswith("  - "):
            flush()
            current = {}
            fragment = raw[4:].strip()
        elif raw.startswith("    ") and current is not None:
            fragment = stripped
        else:
            findings.append(
                Finding(
                    SEVERITY_WARN,
                    "REGISTRY_UNSUPPORTED_NESTING",
                    "control_plane/document_registry.yaml",
                    "/entries",
                    "registry syntax is outside the bounded entry profile",
                )
            )
            continue
        if not fragment:
            continue
        if ":" not in fragment:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_ENTRY_MALFORMED",
                    "control_plane/document_registry.yaml",
                    "/entries",
                    "registry entry line is missing a key separator",
                )
            )
            continue
        key, raw_value = fragment.split(":", 1)
        key = key.strip()
        if key in current:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_DUPLICATE_KEY",
                    "control_plane/document_registry.yaml",
                    f"/entries/{key}",
                    "registry entry fields must not repeat",
                )
            )
        current[key] = _scalar(raw_value)
    flush()

    entries: list[RegistryEntry] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for item in raw_entries:
        doc_id = item.get("doc_id", "").strip()
        target = item.get("path", "").strip()
        if not doc_id or not target:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_ENTRY_INCOMPLETE",
                    "control_plane/document_registry.yaml",
                    "/entries",
                    "registry entry requires doc_id and path",
                )
            )
            continue
        if doc_id in seen_ids:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_DUPLICATE_DOC_ID",
                    "control_plane/document_registry.yaml",
                    "/entries/doc_id",
                    "registry document identities must be unique",
                )
            )
        if target in seen_paths:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_DUPLICATE_PATH",
                    "control_plane/document_registry.yaml",
                    "/entries/path",
                    "registry document paths must be unique",
                )
            )
        seen_ids.add(doc_id)
        seen_paths.add(target)
        entries.append(
            RegistryEntry(
                doc_id=doc_id,
                path=target,
                kind=item.get("kind") or None,
                status=item.get("status") or None,
                authority=item.get("authority") or None,
            )
        )
    return tuple(entries), findings


def _registry_comparison(
    records: Sequence[DocumentRecord],
    entries: Sequence[RegistryEntry],
    review_paths: frozenset[str] | None,
) -> tuple[tuple[DocumentRecord, ...], list[Finding], tuple[RegistryDelta, ...]]:
    by_id = {item.doc_id: item for item in entries}
    by_path = {item.path: item for item in entries}
    updated_records: list[DocumentRecord] = []
    findings: list[Finding] = []
    delta: list[RegistryDelta] = []
    for record in records:
        doc_id = _string(record.metadata, "doc_id")
        if record.meta_block_state != "valid" or doc_id is None:
            updated_records.append(record)
            continue
        entry_by_id = by_id.get(doc_id)
        entry_by_path = by_path.get(record.path)
        should_emit = review_paths is None or record.path in review_paths
        state = "unregistered"
        if entry_by_id and entry_by_id.path == record.path:
            state = "registered"
        elif entry_by_id is not None:
            state = "conflict"
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_DOC_ID_PATH_CONFLICT",
                    record.path,
                    "/doc_id",
                    "document identity is registered to a different path",
                    related_paths=(entry_by_id.path,),
                )
            )
            if should_emit:
                delta.append(
                    RegistryDelta(
                        "HOLD_CONFLICT",
                        doc_id,
                        record.path,
                        "REGISTRY_DOC_ID_PATH_CONFLICT",
                        (),
                        ("authority_resolution", "migration_or_correction_decision"),
                    )
                )
        elif entry_by_path is not None:
            state = "conflict"
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REGISTRY_PATH_DOC_ID_CONFLICT",
                    record.path,
                    "/doc_id",
                    "document path is registered to a different identity",
                )
            )
            if should_emit:
                delta.append(
                    RegistryDelta(
                        "HOLD_CONFLICT",
                        doc_id,
                        record.path,
                        "REGISTRY_PATH_DOC_ID_CONFLICT",
                        (),
                        ("authority_resolution", "identity_correction_decision"),
                    )
                )
        else:
            findings.append(
                Finding(
                    SEVERITY_WARN,
                    "REGISTRY_ENTRY_MISSING",
                    record.path,
                    "/doc_id",
                    "valid metadata identity is not present in the machine registry",
                )
            )
            if should_emit:
                proposed_fields = tuple(
                    sorted(
                        (
                            ("kind", _string(record.metadata, "type") or "document"),
                            ("status", _string(record.metadata, "status") or "unknown"),
                            (
                                "policy_label",
                                _string(record.metadata, "policy_label") or "unknown",
                            ),
                        )
                    )
                )
                delta.append(
                    RegistryDelta(
                        "ADD_REVIEW",
                        doc_id,
                        record.path,
                        "REGISTRY_ENTRY_MISSING",
                        proposed_fields,
                        ("authority",),
                    )
                )
        updated_records.append(replace(record, registry_state=state))
    return tuple(updated_records), findings, tuple(sorted(delta))


def _duplicate_identity_findings(
    records: Sequence[DocumentRecord],
) -> list[Finding]:
    by_id: dict[str, list[str]] = {}
    for record in records:
        doc_id = _string(record.metadata, "doc_id")
        if doc_id is not None:
            by_id.setdefault(doc_id, []).append(record.path)
    findings: list[Finding] = []
    for paths in by_id.values():
        unique_paths = sorted(set(paths))
        if len(unique_paths) < 2:
            continue
        for path in unique_paths:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "DUPLICATE_DOC_ID",
                    path,
                    "/doc_id",
                    "document identity is repeated in the scan scope",
                    related_paths=tuple(item for item in unique_paths if item != path),
                )
            )
    return findings


def _sort_finding(item: Finding) -> tuple[object, ...]:
    return (
        SEVERITY_ORDER.get(item.severity, 99),
        item.code,
        item.path,
        item.field,
        item.related_paths,
        item.historical,
    )


def _ratchet_findings(
    findings: Iterable[Finding],
    changed: frozenset[str],
    *,
    active: bool,
) -> tuple[Finding, ...]:
    adjusted: list[Finding] = []
    for item in findings:
        touches_change = item.path in changed or any(
            path in changed for path in item.related_paths
        )
        if not active or touches_change:
            adjusted.append(item)
            continue
        if item.severity == SEVERITY_FAIL:
            adjusted.append(
                replace(item, severity=SEVERITY_WARN, historical=True)
            )
        # Historical warnings and information are intentionally omitted from the
        # pull-request ratchet to keep the first deployment reviewable.
    return tuple(sorted(adjusted[:MAX_FINDINGS], key=_sort_finding))


