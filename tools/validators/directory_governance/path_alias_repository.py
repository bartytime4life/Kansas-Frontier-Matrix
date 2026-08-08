"""Repository parity checks for accepted compatibility paths."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from .path_alias_io import array, git_blob_sha1, sha256
from .path_alias_model import ADR_PATH, REPO_ROOT, Finding


def safe_repo_path(root: Path, raw: str) -> Path | None:
    if not raw or raw.startswith("/") or "\\" in raw:
        return None
    pure = PurePosixPath(raw)
    if str(pure) != raw or any(part in {".", ".."} for part in pure.parts):
        return None
    candidate = root.joinpath(*pure.parts)
    try:
        resolved_root = root.resolve(strict=True)
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(resolved_root)
    except (OSError, ValueError):
        return None
    return resolved


def repository_findings(candidate: Mapping[str, Any], repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        if repo_root.is_symlink() or not repo_root.is_dir():
            return [Finding("REPO_ROOT_INVALID", "/repo_root")]
        repo_root.resolve(strict=True)
    except OSError:
        return [Finding("REPO_ROOT_UNAVAILABLE", "/repo_root")]

    try:
        adr_text = (repo_root / ADR_PATH.relative_to(REPO_ROOT)).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        findings.append(Finding("DECISION_EVIDENCE_MISSING", "/doctrine/decision_ref"))
    else:
        if "status: accepted" not in adr_text and "**Status** | `accepted`" not in adr_text:
            findings.append(Finding("DECISION_EVIDENCE_MISSING", "/doctrine/decision_ref"))

    for index, raw in enumerate(array(candidate.get("aliases"))):
        if not isinstance(raw, Mapping):
            continue
        base = f"/aliases/{index}"
        old = safe_repo_path(repo_root, str(raw.get("old_path", "")))
        target = safe_repo_path(repo_root, str(raw.get("canonical_target", "")))
        if old is None or not old.is_file():
            findings.append(Finding("ALIAS_PATH_MISSING", f"{base}/old_path"))
        if target is None or not target.is_file():
            findings.append(Finding("CANONICAL_TARGET_MISSING", f"{base}/canonical_target"))
        if old is None or target is None or not old.is_file() or not target.is_file():
            continue
        if old == target:
            findings.append(Finding("ALIAS_SELF_TARGET", f"{base}/canonical_target"))
        legacy_blob = raw.get("legacy_git_blob")
        if isinstance(legacy_blob, str):
            try:
                actual_blob = git_blob_sha1(old)
            except OSError:
                findings.append(Finding("ALIAS_PATH_UNREADABLE", f"{base}/old_path"))
            else:
                if actual_blob != legacy_blob:
                    findings.append(Finding("LEGACY_BLOB_MISMATCH", f"{base}/legacy_git_blob"))
        canonical_digest = raw.get("canonical_sha256")
        if isinstance(canonical_digest, str):
            try:
                actual_digest = f"sha256:{sha256(target)}"
            except OSError:
                findings.append(Finding("CANONICAL_TARGET_UNREADABLE", f"{base}/canonical_target"))
            else:
                if actual_digest != canonical_digest:
                    findings.append(Finding("CANONICAL_DIGEST_MISMATCH", f"{base}/canonical_sha256"))
        if raw.get("body_mode") == "tombstone":
            try:
                size = old.stat().st_size
            except OSError:
                findings.append(Finding("ALIAS_PATH_UNREADABLE", f"{base}/old_path"))
            else:
                if size > 32 * 1024:
                    findings.append(Finding("TOMBSTONE_LIVE_COPY_SUSPECTED", f"{base}/body_mode"))
    return findings
