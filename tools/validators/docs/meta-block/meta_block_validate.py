"""Structural validation for parsed KFM documentation metadata blocks."""

from __future__ import annotations

from datetime import date
from pathlib import Path, PurePosixPath
from typing import Mapping

from meta_block_core import (
    DOC_ID_RE, KNOWN_TRUTH_MARKERS, LEGACY_BLOCK_RE, META_BLOCK_RE,
    PROFILE_REQUIRED, REQUIRED_FIELDS, ROOT_PREFIXES, ROOT_RE, TYPE_RE,
    DocumentRecord, Finding, SEVERITY_FAIL, SEVERITY_WARN, _digest, _relative,
)
from meta_block_parse import _parse_meta_body, _read_text

def _owner_values(metadata: Mapping[str, object]) -> tuple[str, ...]:
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


def _string(metadata: Mapping[str, object], key: str) -> str | None:
    value = metadata.get(key)
    return value.strip() if isinstance(value, str) and value.strip() else None


def _expected_owning_root(path: str) -> str:
    parts = PurePosixPath(path).parts
    return f"{parts[0]}/" if len(parts) > 1 else "repository-root"


def _normalize_related_path(source_path: str, related: str) -> str | None:
    parts = PurePosixPath(related).parts
    if parts and parts[0] in ROOT_PREFIXES:
        combined = parts
    else:
        combined = PurePosixPath(source_path).parent.parts + parts
    normalized: list[str] = []
    for part in combined:
        if part in {"", "."}:
            continue
        if part == "..":
            if not normalized:
                return None
            normalized.pop()
            continue
        normalized.append(part)
    return "/".join(normalized)


def _validate_related(
    metadata: Mapping[str, object], path: str
) -> list[Finding]:
    value = metadata.get("related")
    if value is None:
        return []
    if not isinstance(value, list):
        return [
            Finding(
                SEVERITY_FAIL,
                "FIELD_VALUE_INVALID",
                path,
                "/related",
                "related must be a sequence of strings",
            )
        ]
    findings: list[Finding] = []
    seen: set[str] = set()
    for item in value:
        if not isinstance(item, str) or not item.strip():
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "FIELD_VALUE_INVALID",
                    path,
                    "/related",
                    "related entries must be non-empty strings",
                )
            )
            continue
        related = item.strip()
        if related in seen:
            findings.append(
                Finding(
                    SEVERITY_WARN,
                    "RELATED_ENTRY_DUPLICATE",
                    path,
                    "/related",
                    "related entries should be unique",
                )
            )
        seen.add(related)
        if related.startswith("kfm://"):
            continue
        if "://" in related or related.startswith("mailto:"):
            continue
        if "\\" in related or related.startswith("/") or "\x00" in related:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "RELATED_ENTRY_INVALID",
                    path,
                    "/related",
                    "related path is outside the portable repository-path profile",
                )
            )
            continue
        if _normalize_related_path(path, related) is None:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "RELATED_PATH_ESCAPE",
                    path,
                    "/related",
                    "related path must not escape the repository root",
                )
            )
    return findings


def _validate_metadata(
    metadata: Mapping[str, object],
    path: str,
    *,
    profile: str,
) -> list[Finding]:
    findings: list[Finding] = []
    for field in REQUIRED_FIELDS:
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "REQUIRED_FIELD_MISSING",
                    path,
                    f"/{field}",
                    "required metadata field is missing or empty",
                )
            )
    owner_present = "owner" in metadata
    owners_present = "owners" in metadata
    if owner_present and owners_present:
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "OWNER_FIELDS_CONFLICT",
                path,
                "/owner",
                "use owner or owners, not both",
            )
        )
    if not _owner_values(metadata):
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "REQUIRED_FIELD_MISSING",
                path,
                "/owner",
                "owner or owners is required",
            )
        )

    doc_id = _string(metadata, "doc_id")
    if doc_id is not None and not DOC_ID_RE.fullmatch(doc_id):
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "DOC_ID_INVALID",
                path,
                "/doc_id",
                "doc_id must use the bounded kfm:// identity grammar",
            )
        )
    document_type = _string(metadata, "type")
    if document_type is not None and not TYPE_RE.fullmatch(document_type):
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "FIELD_VALUE_INVALID",
                path,
                "/type",
                "type is outside the bounded token grammar",
            )
        )
    owning_root = _string(metadata, "owning_root")
    if owning_root is not None:
        if not ROOT_RE.fullmatch(owning_root):
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "FIELD_VALUE_INVALID",
                    path,
                    "/owning_root",
                    "owning_root must be a responsibility-root token",
                )
            )
        elif owning_root != _expected_owning_root(path):
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "OWNING_ROOT_PATH_MISMATCH",
                    path,
                    "/owning_root",
                    "owning_root must match the document's top-level responsibility root",
                )
            )

    created = _string(metadata, "created")
    updated = _string(metadata, "updated")
    created_date: date | None = None
    updated_date: date | None = None
    for field, value in (("created", created), ("updated", updated)):
        if value is None:
            continue
        try:
            parsed = date.fromisoformat(value)
        except ValueError:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "DATE_INVALID",
                    path,
                    f"/{field}",
                    "date fields must use the ISO calendar-date form",
                )
            )
        else:
            if field == "created":
                created_date = parsed
            else:
                updated_date = parsed
    if created_date and updated_date and updated_date < created_date:
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "DATE_ORDER_INVALID",
                path,
                "/updated",
                "updated must not precede created",
            )
        )

    truth_posture = _string(metadata, "truth_posture")
    if truth_posture is not None and not any(
        marker in truth_posture.casefold() for marker in KNOWN_TRUTH_MARKERS
    ):
        findings.append(
            Finding(
                SEVERITY_WARN,
                "TRUTH_POSTURE_UNRECOGNIZED",
                path,
                "/truth_posture",
                "truth_posture does not expose a recognized evidence marker",
            )
        )

    for field in ("title", "version", "status", "policy_label", "responsibility"):
        value = _string(metadata, field)
        if value is not None and len(value) > 1_024:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "FIELD_VALUE_TOO_LONG",
                    path,
                    f"/{field}",
                    "metadata value exceeds the bounded field limit",
                )
            )
    findings.extend(_validate_related(metadata, path))
    return findings


def _extract_record(
    root: Path,
    path: Path,
    *,
    profile: str,
) -> tuple[DocumentRecord, list[Finding]]:
    relative = _relative(path, root)
    text = _read_text(path)
    findings: list[Finding] = []
    matches = tuple(META_BLOCK_RE.finditer(text))
    legacy_matches = tuple(LEGACY_BLOCK_RE.finditer(text))
    open_count = text.casefold().count("[kfm_meta_block_v2]")
    close_count = text.casefold().count("[/kfm_meta_block_v2]")

    if not matches:
        if open_count or close_count:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "META_BLOCK_MALFORMED",
                    relative,
                    "/",
                    "metadata block delimiters do not form one complete envelope",
                )
            )
            state = "malformed"
        elif legacy_matches:
            findings.append(
                Finding(
                    SEVERITY_WARN,
                    "LEGACY_META_BLOCK_PRESENT",
                    relative,
                    "/",
                    "legacy metadata is visible but outside the v2 conformance profile",
                )
            )
            state = "legacy"
        elif profile == PROFILE_REQUIRED:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "META_BLOCK_MISSING",
                    relative,
                    "/",
                    "the selected profile requires KFM_META_BLOCK_V2",
                )
            )
            state = "missing"
        else:
            state = "missing"
        return DocumentRecord(relative, state, {}, None, None, "not_evaluated"), findings

    if len(matches) > 1:
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "META_BLOCK_DUPLICATE",
                relative,
                "/",
                "a document must not contain multiple v2 metadata blocks",
            )
        )
    if legacy_matches:
        findings.append(
            Finding(
                SEVERITY_FAIL,
                "META_BLOCK_PROFILE_CONFLICT",
                relative,
                "/",
                "v2 and legacy metadata envelopes must not coexist",
            )
        )
    match = matches[0]
    first_line = text.count("\n", 0, match.start()) + 1
    if text[: match.start()].strip("\ufeff \t\r\n"):
        findings.append(
            Finding(
                SEVERITY_WARN,
                "META_BLOCK_NOT_FIRST",
                relative,
                "/",
                "metadata block should precede document content",
            )
        )
    metadata, parse_findings = _parse_meta_body(match.group(1), relative)
    findings.extend(parse_findings)
    findings.extend(_validate_metadata(metadata, relative, profile=profile))
    digest = _digest(metadata)
    state = "valid" if not any(item.severity == SEVERITY_FAIL for item in findings) else "invalid"
    return DocumentRecord(relative, state, metadata, digest, first_line, "not_evaluated"), findings


