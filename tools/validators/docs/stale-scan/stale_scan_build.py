from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Mapping, Sequence

from stale_scan_core import (
    Finding,
    StaleScanError,
    StaleScanResult,
    changed_paths_from_git,
    ratchet_findings,
    result_from_parts,
)
from stale_scan_parse import (
    collect_markdown_paths,
    owner_is_placeholder,
    owner_text,
    parse_meta_block,
    read_utf8,
    scalar,
    temporal_marker_values,
)


LIMITATIONS = (
    "Freshness is a review signal, not proof that a document or claim is true, false, current, adopted, or authoritative.",
    "The scanner reads a bounded top-level metadata subset and delegates full metadata conformance to the meta-block validator.",
    "Exact local link, fragment, case, and path resolution remains owned by the link-check validator.",
    "Implementation-claim findings request review; they do not infer the actual implementation state.",
    "The scanner never edits Markdown, registries, doctrine, policy, review, release, or publication state.",
)

IMPLEMENTATION_MARKERS = (
    "implemented",
    "bounded-executable",
    "production",
    "active",
    "published",
    "current behavior",
    "confirmed implementation",
)


def parse_iso_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def parse_type_windows(raw_values: Sequence[str]) -> dict[str, int]:
    windows: dict[str, int] = {}
    for raw in raw_values:
        if "=" not in raw:
            raise StaleScanError("type window must use <type>=<days>")
        document_type, days_text = raw.split("=", 1)
        document_type = document_type.strip().lower()
        try:
            days = int(days_text)
        except ValueError as exc:
            raise StaleScanError("type window days must be an integer") from exc
        if not document_type or days < 1:
            raise StaleScanError("type window requires a non-empty type and positive days")
        windows[document_type] = days
    return windows


def _claim_review_due(metadata: Mapping[str, object], text: str) -> bool:
    values = (
        scalar(metadata, "status") or "",
        scalar(metadata, "truth_posture") or "",
        scalar(metadata, "responsibility") or "",
        text[:1500],
    )
    combined = " ".join(values).lower()
    return any(marker in combined for marker in IMPLEMENTATION_MARKERS)


def _verification_debt_due(metadata: Mapping[str, object]) -> bool:
    posture = (scalar(metadata, "truth_posture") or "").upper()
    return "NEEDS VERIFICATION" in posture or "UNKNOWN" in posture


def scan_stale_docs(
    *,
    repo_root: Path,
    inputs: Sequence[str],
    as_of: date,
    profile: str = "advisory",
    review_window_days: int = 365,
    placeholder_grace_days: int = 90,
    type_windows: Mapping[str, int] | None = None,
    git_diff: str | None = None,
    warnings_as_errors: bool = False,
) -> StaleScanResult:
    if profile not in {"advisory", "bounded-required"}:
        raise StaleScanError("unsupported stale-scan profile")
    if review_window_days < 1 or placeholder_grace_days < 1:
        raise StaleScanError("freshness thresholds must be positive integers")

    root = repo_root.resolve()
    windows = {key.lower(): value for key, value in (type_windows or {}).items()}
    paths = collect_markdown_paths(root, inputs)
    findings: list[Finding] = []
    documents: list[dict[str, object]] = []

    for file_path in paths:
        relative = file_path.relative_to(root).as_posix()
        text = read_utf8(file_path)
        parsed = parse_meta_block(text, relative)
        findings.extend(parsed.findings)
        metadata = parsed.metadata
        document_type = (scalar(metadata, "type") or "unknown").lower()
        window = windows.get(document_type, review_window_days)
        created_raw = scalar(metadata, "created")
        reviewed_raw = scalar(metadata, "last_reviewed", "reviewed", "updated")
        created = parse_iso_date(created_raw) if created_raw else None
        reviewed = parse_iso_date(reviewed_raw) if reviewed_raw else None
        owner = owner_text(metadata)
        placeholder = owner_is_placeholder(owner)
        age_days: int | None = None

        if not parsed.has_block:
            if profile == "bounded-required" and not parsed.findings:
                findings.append(
                    Finding(
                        "DELEGATE_TO_META_BLOCK",
                        "fail",
                        relative,
                        "The bounded-required stale profile needs a metadata block; structural enforcement belongs to the meta-block validator.",
                    )
                )
        else:
            if created_raw and created is None:
                findings.append(
                    Finding(
                        "CREATED_DATE_INVALID",
                        "fail",
                        relative,
                        f"Created date '{created_raw}' is not an ISO calendar date.",
                    )
                )
            if reviewed_raw and reviewed is None:
                findings.append(
                    Finding(
                        "REVIEW_DATE_INVALID",
                        "fail",
                        relative,
                        f"Review date '{reviewed_raw}' is not an ISO calendar date.",
                    )
                )
            if reviewed is None and reviewed_raw is None:
                severity = "fail" if profile == "bounded-required" else "warn"
                findings.append(
                    Finding(
                        "REVIEW_DATE_MISSING",
                        severity,
                        relative,
                        "No last_reviewed, reviewed, or updated date is available for freshness assessment.",
                    )
                )
            if created and reviewed and created > reviewed:
                findings.append(
                    Finding(
                        "DATE_ORDER_INVALID",
                        "fail",
                        relative,
                        f"Created date {created.isoformat()} is later than review date {reviewed.isoformat()}.",
                    )
                )
            if reviewed:
                age_days = (as_of - reviewed).days
                if age_days < 0:
                    findings.append(
                        Finding(
                            "FUTURE_REVIEW_DATE",
                            "fail",
                            relative,
                            f"Review date {reviewed.isoformat()} is {abs(age_days)} day(s) after the as-of date.",
                        )
                    )
                elif age_days > window:
                    findings.append(
                        Finding(
                            "REVIEW_WINDOW_EXPIRED",
                            "warn",
                            relative,
                            f"Review age is {age_days} days, exceeding the configured {window}-day window.",
                        )
                    )
                    if _claim_review_due(metadata, text):
                        findings.append(
                            Finding(
                                "IMPLEMENTATION_CLAIM_REVIEW_DUE",
                                "warn",
                                relative,
                                "The document carries implementation/current-state language and its review window has expired; actual behavior must be reverified.",
                            )
                        )
                    if _verification_debt_due(metadata):
                        findings.append(
                            Finding(
                                "VERIFICATION_DEBT_REVIEW_DUE",
                                "warn",
                                relative,
                                "The document retains unresolved verification posture beyond the configured review window.",
                            )
                        )

            age_for_owner = age_days
            if age_for_owner is None and created:
                age_for_owner = (as_of - created).days
            if placeholder and age_for_owner is not None and age_for_owner > placeholder_grace_days:
                findings.append(
                    Finding(
                        "OWNER_PLACEHOLDER_STALE",
                        "warn",
                        relative,
                        f"Owner placeholder remains after {age_for_owner} days; route to the owning steward rather than inventing an owner.",
                    )
                )

            for key, raw_value in temporal_marker_values(metadata):
                marker_date = parse_iso_date(raw_value)
                if marker_date is None:
                    findings.append(
                        Finding(
                            "TEMPORARY_MARKER_DATE_INVALID",
                            "fail",
                            relative,
                            f"Metadata field '{key}' value '{raw_value}' is not an ISO calendar date.",
                        )
                    )
                elif marker_date < as_of:
                    findings.append(
                        Finding(
                            "TEMPORARY_MARKER_EXPIRED",
                            "warn",
                            relative,
                            f"Metadata field '{key}' expired on {marker_date.isoformat()} and requires steward review.",
                        )
                    )

        documents.append(
            {
                "path": relative,
                "doc_id": scalar(metadata, "doc_id", "document_id"),
                "title": scalar(metadata, "title"),
                "type": document_type,
                "status": scalar(metadata, "status"),
                "owner": owner,
                "has_metadata": parsed.has_block,
                "review_date": reviewed.isoformat() if reviewed else None,
                "age_days": age_days,
                "review_window_days": window,
                "owner_placeholder": placeholder,
                "current": True,
            }
        )

    changed_paths = changed_paths_from_git(root, git_diff) if git_diff else None
    ratcheted = ratchet_findings(
        findings,
        changed_paths=changed_paths,
        warnings_as_errors=warnings_as_errors,
    )
    if changed_paths is not None:
        documents = [
            {**document, "current": str(document["path"]) in changed_paths}
            for document in documents
        ]

    return result_from_parts(
        profile=profile,
        as_of=as_of.isoformat(),
        review_window_days=review_window_days,
        placeholder_grace_days=placeholder_grace_days,
        documents=documents,
        findings=ratcheted,
        warnings_as_errors=warnings_as_errors,
        limitations=LIMITATIONS,
    )
