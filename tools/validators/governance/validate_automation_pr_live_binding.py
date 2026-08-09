#!/usr/bin/env python3
"""Validate a write-eligible AutomationPrProposal against live local Git refs.

This validator is deliberately non-mutating and no-network. The caller must fetch the
trusted base and proposed head refs before invoking it. It proves only that the local
refs and candidate bytes match the declaration that was already admitted by the
AutomationPrProposal validator.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROPOSAL_VALIDATOR_PATH = HERE / "validate_automation_pr_proposal.py"


def _load_proposal_validator():
    spec = importlib.util.spec_from_file_location(
        "kfm_automation_pr_proposal_validator", PROPOSAL_VALIDATOR_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load AutomationPrProposal validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git(repo_root: Path, *args: str, binary: bool = False) -> bytes | str:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if binary:
        return completed.stdout
    return completed.stdout.decode("utf-8", errors="strict").strip()


def _live_changes(repo_root: Path, base_ref: str, head_ref: str) -> list[tuple[str, str]]:
    raw = _git(
        repo_root,
        "diff",
        "--name-status",
        "--no-renames",
        "-z",
        f"{base_ref}..{head_ref}",
        binary=True,
    )
    assert isinstance(raw, bytes)
    parts = raw.split(b"\0")
    if parts and parts[-1] == b"":
        parts.pop()
    if len(parts) % 2:
        raise RuntimeError("unexpected git --name-status -z output")
    changes: list[tuple[str, str]] = []
    for index in range(0, len(parts), 2):
        status = parts[index].decode("utf-8", errors="strict")
        path = parts[index + 1].decode("utf-8", errors="strict")
        changes.append((status, path))
    return changes


def _blob_mode(repo_root: Path, head_ref: str, path: str) -> str | None:
    raw = _git(repo_root, "ls-tree", "-z", head_ref, "--", path, binary=True)
    assert isinstance(raw, bytes)
    if not raw:
        return None
    record = raw.rstrip(b"\0").decode("utf-8", errors="strict")
    metadata, _, actual_path = record.partition("\t")
    if actual_path != path:
        return None
    fields = metadata.split()
    return fields[0] if len(fields) >= 3 else None


def validate_live_binding(
    payload: Any,
    *,
    repo_root: Path,
    base_ref: str,
    head_ref: str,
) -> dict[str, Any]:
    reasons: set[str] = set()
    try:
        proposal_validator = _load_proposal_validator()
        proposal_result = proposal_validator.validate(payload)
    except Exception:
        return {
            "outcome": "ERROR",
            "write_eligible": False,
            "reason_codes": ["PROPOSAL_VALIDATOR_ERROR"],
        }

    if proposal_result.get("outcome") != "PASS" or not proposal_result.get(
        "write_eligible"
    ):
        return {
            "outcome": "ERROR",
            "write_eligible": False,
            "reason_codes": ["PROPOSAL_NOT_WRITE_ELIGIBLE"],
        }

    assert isinstance(payload, dict)
    try:
        base_sha = str(_git(repo_root, "rev-parse", "--verify", f"{base_ref}^{{commit}}"))
        head_sha = str(_git(repo_root, "rev-parse", "--verify", f"{head_ref}^{{commit}}"))
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError):
        return {
            "outcome": "ERROR",
            "write_eligible": False,
            "reason_codes": ["MISSING_GIT_REF"],
        }

    if base_sha != payload["base_sha"]:
        reasons.add("BASE_SHA_MISMATCH")

    try:
        merge_base = str(_git(repo_root, "merge-base", base_ref, head_ref))
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        merge_base = ""
        reasons.add("MERGE_BASE_ERROR")
    if merge_base and merge_base != base_sha:
        reasons.add("HEAD_NOT_BASED_ON_CURRENT_MAIN")

    try:
        changes = _live_changes(repo_root, base_ref, head_ref)
    except (subprocess.CalledProcessError, UnicodeDecodeError, RuntimeError):
        return {
            "outcome": "ERROR",
            "write_eligible": False,
            "reason_codes": sorted(reasons | {"LIVE_DIFF_ERROR"}),
            "base_sha": base_sha,
            "head_sha": head_sha,
        }

    live_paths = [path for _, path in changes]
    if set(live_paths) != set(payload["changed_paths"]) or len(live_paths) != len(
        payload["changed_paths"]
    ):
        reasons.add("LIVE_CHANGED_PATH_MISMATCH")

    for status, path in changes:
        if status not in {"A", "M"}:
            reasons.add("UNSAFE_LIVE_CHANGE_TYPE")
        if not proposal_validator.safe_candidate_path(path):
            reasons.add("UNSAFE_LIVE_CHANGED_PATH")

    artifact_digests = {
        artifact["path"]: artifact["sha256"] for artifact in payload["artifacts"]
    }
    for path in payload["changed_paths"]:
        if path not in live_paths:
            continue
        try:
            mode = _blob_mode(repo_root, head_ref, path)
            if mode != "100644":
                reasons.add("UNSAFE_CANDIDATE_BLOB_MODE")
                continue
            blob = _git(repo_root, "show", f"{head_ref}:{path}", binary=True)
            assert isinstance(blob, bytes)
        except (subprocess.CalledProcessError, UnicodeDecodeError):
            reasons.add("CANDIDATE_BLOB_UNREADABLE")
            continue
        actual = "sha256:" + hashlib.sha256(blob).hexdigest()
        if actual != artifact_digests.get(path):
            reasons.add("ARTIFACT_DIGEST_MISMATCH")

    write_eligible = not reasons
    return {
        "outcome": "PASS" if write_eligible else "ERROR",
        "write_eligible": write_eligible,
        "reason_codes": sorted(reasons),
        "base_sha": base_sha,
        "head_sha": head_sha,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("proposal")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--head-ref", required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(
            json.dumps(
                {
                    "outcome": "ERROR",
                    "write_eligible": False,
                    "reason_codes": ["INVALID_JSON"],
                    "detail": str(exc),
                },
                sort_keys=True,
            )
        )
        return 2

    result = validate_live_binding(
        payload,
        repo_root=Path(args.repo_root).resolve(),
        base_ref=args.base_ref,
        head_ref=args.head_ref,
    )
    print(json.dumps(result, sort_keys=True))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
