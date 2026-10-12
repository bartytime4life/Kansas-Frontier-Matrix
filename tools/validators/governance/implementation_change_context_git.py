"""Safe local Git metadata builder for ImplementationChangeContext."""
from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from tools.validators.governance.implementation_change_context_model import (
    GitContextError,
    MAX_FILES,
    STATUS_MAP,
    _file_sort_key,
    expected_context_id,
    expected_summary,
)

def _git_bytes(repo_root: Path, *args: str) -> bytes:
    environment = dict(os.environ)
    environment.update(
        {
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_OPTIONAL_LOCKS": "0",
            "LC_ALL": "C.UTF-8",
        }
    )
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo_root), *args],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise GitContextError("local git metadata command failed") from exc
    if completed.returncode != 0:
        raise GitContextError("local git metadata command failed")
    return completed.stdout


def _git_text(repo_root: Path, *args: str) -> str:
    try:
        return _git_bytes(repo_root, *args).decode("utf-8", errors="strict").strip()
    except UnicodeError as exc:
        raise GitContextError("git metadata is not UTF-8") from exc


def _resolve_commit(repo_root: Path, ref: str) -> str:
    if not ref or ref.startswith("-") or any(ord(char) < 32 for char in ref):
        raise GitContextError("unsafe git ref")
    resolved = _git_text(repo_root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")
    if not re.fullmatch(r"[0-9a-f]{40}", resolved):
        raise GitContextError("git ref did not resolve to a full commit SHA")
    return resolved


def _parse_name_status(raw: bytes) -> list[dict[str, object]]:
    try:
        tokens = [token.decode("utf-8", errors="strict") for token in raw.split(b"\0") if token]
    except UnicodeError as exc:
        raise GitContextError("changed path metadata is not UTF-8") from exc
    rows: list[dict[str, object]] = []
    index = 0
    while index < len(tokens):
        raw_status = tokens[index]
        index += 1
        code = raw_status[:1]
        status = STATUS_MAP.get(code)
        if status is None:
            raise GitContextError("unsupported git name-status code")
        if code in {"R", "C"}:
            if index + 1 >= len(tokens):
                raise GitContextError("truncated rename/copy metadata")
            previous_path, path = tokens[index], tokens[index + 1]
            index += 2
        else:
            if index >= len(tokens):
                raise GitContextError("truncated path metadata")
            path = tokens[index]
            previous_path = None
            index += 1
        rows.append(
            {
                "path": path,
                "previous_path": previous_path,
                "status": status,
            }
        )
    return rows


def _parse_numstat(raw: bytes) -> dict[str, tuple[int | None, int | None, bool]]:
    parts = raw.split(b"\0")
    stats: dict[str, tuple[int | None, int | None, bool]] = {}
    index = 0
    while index < len(parts):
        token = parts[index]
        index += 1
        if not token:
            continue
        try:
            text = token.decode("utf-8", errors="strict")
        except UnicodeError as exc:
            raise GitContextError("numstat metadata is not UTF-8") from exc
        fields = text.split("\t", 2)
        if len(fields) != 3:
            raise GitContextError("invalid numstat record")
        add_raw, delete_raw, path = fields
        if path:
            destination = path
        else:
            if index + 1 >= len(parts):
                raise GitContextError("truncated renamed numstat record")
            try:
                _previous = parts[index].decode("utf-8", errors="strict")
                destination = parts[index + 1].decode("utf-8", errors="strict")
            except UnicodeError as exc:
                raise GitContextError("renamed numstat path is not UTF-8") from exc
            index += 2
        binary = add_raw == "-" or delete_raw == "-"
        if binary:
            additions = deletions = None
        else:
            try:
                additions = int(add_raw)
                deletions = int(delete_raw)
            except ValueError as exc:
                raise GitContextError("invalid numeric numstat value") from exc
        if destination in stats:
            raise GitContextError("duplicate numstat destination")
        stats[destination] = (additions, deletions, binary)
    return stats


def _utc_timestamp(value: str) -> str:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError
        normalized = parsed.astimezone(timezone.utc).replace(microsecond=0)
    except ValueError as exc:
        raise GitContextError("invalid commit timestamp") from exc
    return normalized.isoformat().replace("+00:00", "Z")


def build_from_git(
    repo_root: Path,
    *,
    repository: str,
    base_ref: str,
    head_ref: str,
    status: str = "DRAFT",
    implementation_decision_refs: Sequence[str] = (),
) -> dict[str, object]:
    if repo_root.is_symlink() or not repo_root.is_dir():
        raise GitContextError("repository root must be a real directory")
    try:
        resolved_root = repo_root.resolve(strict=True)
    except OSError as exc:
        raise GitContextError("repository root could not be resolved") from exc
    top_level = Path(_git_text(resolved_root, "rev-parse", "--show-toplevel")).resolve(strict=True)
    if top_level != resolved_root:
        raise GitContextError("repository root must be the git top-level directory")

    base_sha = _resolve_commit(resolved_root, base_ref)
    head_sha = _resolve_commit(resolved_root, head_ref)
    ancestor = subprocess.run(
        ["git", "-C", str(resolved_root), "merge-base", "--is-ancestor", base_sha, head_sha],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env={**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_OPTIONAL_LOCKS": "0"},
        timeout=30,
    )
    if ancestor.returncode != 0:
        raise GitContextError("base commit is not an ancestor of head commit")

    names = _parse_name_status(
        _git_bytes(
            resolved_root,
            "diff",
            "--no-ext-diff",
            "--no-textconv",
            "--name-status",
            "-z",
            "--find-renames=50%",
            base_sha,
            head_sha,
            "--",
        )
    )
    if not names:
        raise GitContextError("commit range contains no changed files")
    if len(names) > MAX_FILES:
        raise GitContextError("commit range exceeds the 1000-file profile limit")
    stats = _parse_numstat(
        _git_bytes(
            resolved_root,
            "diff",
            "--no-ext-diff",
            "--no-textconv",
            "--numstat",
            "-z",
            "--find-renames=50%",
            base_sha,
            head_sha,
            "--",
        )
    )

    files: list[dict[str, object]] = []
    for row in names:
        path = str(row["path"])
        if path not in stats:
            raise GitContextError("name-status and numstat path sets differ")
        additions, deletions, binary = stats[path]
        files.append(
            {
                "path": path,
                "previous_path": row["previous_path"],
                "status": row["status"],
                "additions": additions,
                "deletions": deletions,
                "binary": binary,
            }
        )
    if set(stats) != {str(item["path"]) for item in files}:
        raise GitContextError("name-status and numstat path sets differ")
    files.sort(key=_file_sort_key)

    timestamp = _utc_timestamp(_git_text(resolved_root, "show", "-s", "--format=%cI", head_sha))
    document: dict[str, object] = {
        "schema_version": "1.0.0",
        "profile": "kfm.governance.implementation-change-context.v1",
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "LOCAL_GIT_METADATA_ONLY",
        "authority": "NONE",
        "context_id": "",
        "repository": repository,
        "base_sha": base_sha,
        "head_sha": head_sha,
        "generated_at": timestamp,
        "status": status,
        "files": files,
        "summary": expected_summary(files),
        "implementation_decision_refs": sorted(set(implementation_decision_refs)),
        "content_boundary": {
            "value_minimized": True,
            "raw_diff_included": False,
            "file_content_included": False,
            "private_reasoning_included": False,
        },
        "permissions": {
            "may_approve_review": False,
            "may_mutate_repository": False,
            "may_change_policy": False,
            "may_promote": False,
            "may_release": False,
            "may_publish": False,
        },
        "non_effects": [
            "no_evidence_creation_or_resolution",
            "no_policy_or_review_approval",
            "no_repository_mutation_authority",
            "no_promotion_release_deployment_or_publication",
            "no_raw_diff_file_content_person_profile_or_hidden_reasoning",
        ],
    }
    document["context_id"] = expected_context_id(document)
    return document
