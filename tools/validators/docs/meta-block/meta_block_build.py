"""Compose bounded KFM documentation metadata validation results."""

from __future__ import annotations

from dataclasses import asdict, replace
from pathlib import Path
from typing import Sequence

from meta_block_core import (
    MAX_FINDINGS, MAX_REPORT_DOCUMENTS, PROFILE_PRESENT, PROFILE_REQUIRED,
    SEVERITY_FAIL, SEVERITY_INFO, SEVERITY_WARN, Finding, MetaBlockError,
    MetaBlockResult, RegistryDelta, RegistryEntry, _digest, _inside,
)
from meta_block_parse import _changed_documents, _collect_documents
from meta_block_validate import _extract_record
from meta_block_registry import (
    _duplicate_identity_findings, _parse_registry, _ratchet_findings,
    _registry_comparison, _sort_finding,
)

def _error_result(profile: str = PROFILE_PRESENT) -> MetaBlockResult:
    finding = Finding(
        SEVERITY_FAIL,
        "ERROR",
        "<scope>",
        "/",
        "metadata validation could not complete safely",
    )
    material = {
        "outcome": "ERROR",
        "profile": profile,
        "findings": [asdict(finding)],
    }
    return MetaBlockResult(
        outcome="ERROR",
        scope="error",
        profile=profile,
        report_digest=_digest(material),
        changed_documents=(),
        documents=(),
        findings=(finding,),
        registry_delta=(),
        counts={
            "documents": 0,
            "metadata_blocks": 0,
            "missing_metadata_blocks": 0,
            "valid_metadata_blocks": 0,
            "invalid_metadata_blocks": 0,
            "registered_documents": 0,
            "registry_add_candidates": 0,
            "registry_conflicts": 0,
            "fail_findings": 1,
            "warn_findings": 0,
            "info_findings": 0,
        },
        limitations=(
            "The error result intentionally omits untrusted input details.",
        ),
    )


def validate_meta_blocks(
    *,
    repo_root: Path,
    inputs: Sequence[str],
    profile: str = PROFILE_PRESENT,
    registry_path: str | None = None,
    git_diff: str | None = None,
    warnings_as_errors: bool = False,
) -> MetaBlockResult:
    root = repo_root.resolve(strict=True)
    if not root.is_dir():
        raise MetaBlockError("repository root is not a directory")
    if profile not in {PROFILE_PRESENT, PROFILE_REQUIRED}:
        raise MetaBlockError("unsupported validation profile")
    paths = _collect_documents(root, inputs)
    changed = _changed_documents(root, git_diff)
    findings: list[Finding] = []
    records: list[DocumentRecord] = []
    for path in paths:
        record, record_findings = _extract_record(root, path, profile=profile)
        records.append(record)
        findings.extend(record_findings)
    findings.extend(_duplicate_identity_findings(records))

    registry_entries: tuple[RegistryEntry, ...] = ()
    registry_delta: tuple[RegistryDelta, ...] = ()
    if registry_path:
        candidate = (root / registry_path).resolve(strict=False)
        if not _inside(candidate, root):
            raise MetaBlockError("registry path escapes repository root")
        registry_entries, registry_findings = _parse_registry(candidate)
        findings.extend(registry_findings)
        review_paths = changed if git_diff is not None else None
        records_tuple, comparison_findings, registry_delta = _registry_comparison(
            records, registry_entries, review_paths
        )
        records = list(records_tuple)
        findings.extend(comparison_findings)

    ratcheted = list(
        _ratchet_findings(findings, changed, active=git_diff is not None)
    )
    if warnings_as_errors:
        ratcheted = [
            replace(item, severity=SEVERITY_FAIL)
            if item.severity == SEVERITY_WARN and not item.historical
            else item
            for item in ratcheted
        ]
        ratcheted.sort(key=_sort_finding)

    fail_count = sum(item.severity == SEVERITY_FAIL for item in ratcheted)
    warn_count = sum(item.severity == SEVERITY_WARN for item in ratcheted)
    info_count = sum(item.severity == SEVERITY_INFO for item in ratcheted)
    if fail_count:
        outcome = "DOC_META_BLOCK_FAIL"
    elif warn_count or info_count:
        outcome = "DOC_META_BLOCK_WARN"
    else:
        outcome = "DOC_META_BLOCK_PASS"

    metadata_blocks = sum(
        item.meta_block_state in {"valid", "invalid"} for item in records
    )
    counts = {
        "documents": len(records),
        "metadata_blocks": metadata_blocks,
        "missing_metadata_blocks": sum(
            item.meta_block_state == "missing" for item in records
        ),
        "valid_metadata_blocks": sum(
            item.meta_block_state == "valid" for item in records
        ),
        "invalid_metadata_blocks": sum(
            item.meta_block_state in {"invalid", "malformed", "legacy"}
            for item in records
        ),
        "registered_documents": sum(
            item.registry_state == "registered" for item in records
        ),
        "registry_add_candidates": sum(
            item.action == "ADD_REVIEW" for item in registry_delta
        ),
        "registry_conflicts": sum(
            item.action == "HOLD_CONFLICT" for item in registry_delta
        ),
        "fail_findings": fail_count,
        "warn_findings": warn_count,
        "info_findings": info_count,
    }
    scope = ",".join(inputs)
    report_documents = tuple(records[:MAX_REPORT_DOCUMENTS])
    material = {
        "profile": profile,
        "scope": scope,
        "changed_documents": sorted(changed),
        "documents": [item.to_payload() for item in report_documents],
        "findings": [asdict(item) for item in ratcheted],
        "registry_delta": [item.to_payload() for item in registry_delta],
        "counts": counts,
    }
    limitations = (
        "The parser validates a bounded top-level metadata subset, not general YAML.",
        "Structural metadata conformance does not establish truth, authority, rights, policy, review, release, or publication state.",
        "Exact local target, fragment, case, and path resolution remains delegated to the link-check validator.",
        "Registry additions are review-only candidates and leave authority unresolved.",
        "Evidence-based status-overclaim detection remains outside this first executable profile.",
    )
    return MetaBlockResult(
        outcome=outcome,
        scope=scope,
        profile=profile,
        report_digest=_digest(material),
        changed_documents=tuple(sorted(changed)),
        documents=report_documents,
        findings=tuple(ratcheted),
        registry_delta=registry_delta,
        counts=counts,
        limitations=limitations,
    )


