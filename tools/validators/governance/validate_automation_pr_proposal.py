#!/usr/bin/env python3
"""Validate the bounded Pass 12 AutomationPrProposal profile."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import PurePosixPath
from typing import Any

PROFILE = "kfm.automation.pr-proposal.v1"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
PROPOSAL_ID = re.compile(r"^[a-z0-9][a-z0-9._-]{2,63}$")
BRANCH = re.compile(r"^automation/[A-Za-z0-9._/-]{3,100}$")
REASON = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
ALLOWED_KEYS = {
    "profile", "proposal_id", "base_ref", "base_sha", "head_branch", "title",
    "changed_paths", "artifacts", "receipt_ref", "policy_outcome", "policy_reasons",
    "draft", "merge_allowed", "release_allowed", "deploy_allowed", "promote_allowed",
    "publish_allowed",
}


def safe_candidate_path(value: Any) -> bool:
    if not isinstance(value, str) or not value.startswith("data/work/automation/"):
        return False
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "." in path.parts:
        return False
    return all(not part.startswith(".") for part in path.parts)


def validate(payload: Any) -> dict[str, Any]:
    reasons: set[str] = set()
    if not isinstance(payload, dict):
        return {"outcome": "ERROR", "write_eligible": False, "reason_codes": ["INVALID_OBJECT"]}

    if set(payload) != ALLOWED_KEYS:
        reasons.add("INVALID_FIELD_SET")
    if payload.get("profile") != PROFILE:
        reasons.add("INVALID_PROFILE")
    if not isinstance(payload.get("proposal_id"), str) or not PROPOSAL_ID.fullmatch(payload["proposal_id"]):
        reasons.add("INVALID_PROPOSAL_ID")
    if payload.get("base_ref") != "main":
        reasons.add("INVALID_BASE_REF")
    if not isinstance(payload.get("base_sha"), str) or not SHA40.fullmatch(payload["base_sha"]):
        reasons.add("INVALID_BASE_SHA")
    if not isinstance(payload.get("head_branch"), str) or not BRANCH.fullmatch(payload["head_branch"]):
        reasons.add("INVALID_HEAD_BRANCH")
    if ".." in str(payload.get("head_branch", "")).split("/"):
        reasons.add("UNSAFE_HEAD_BRANCH")
    title = payload.get("title")
    if not isinstance(title, str) or not (1 <= len(title) <= 120):
        reasons.add("INVALID_TITLE")

    changed = payload.get("changed_paths")
    if not isinstance(changed, list) or not (1 <= len(changed) <= 8) or len(changed) != len(set(changed or [])):
        reasons.add("INVALID_CHANGED_PATHS")
        changed_set: set[str] = set()
    else:
        changed_set = set(changed)
        if not all(safe_candidate_path(path) for path in changed):
            reasons.add("UNSAFE_CHANGED_PATH")

    artifacts = payload.get("artifacts")
    artifact_paths: set[str] = set()
    if not isinstance(artifacts, list) or not (1 <= len(artifacts) <= 8):
        reasons.add("INVALID_ARTIFACTS")
    else:
        for artifact in artifacts:
            if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
                reasons.add("INVALID_ARTIFACT")
                continue
            path = artifact.get("path")
            digest = artifact.get("sha256")
            if not safe_candidate_path(path):
                reasons.add("UNSAFE_ARTIFACT_PATH")
            elif path in artifact_paths:
                reasons.add("DUPLICATE_ARTIFACT_PATH")
            else:
                artifact_paths.add(path)
            if not isinstance(digest, str) or not SHA256.fullmatch(digest):
                reasons.add("INVALID_ARTIFACT_DIGEST")
        if changed_set and artifact_paths != changed_set:
            reasons.add("ARTIFACT_PATH_BINDING_MISMATCH")

    receipt_ref = payload.get("receipt_ref")
    if not isinstance(receipt_ref, str) or not (1 <= len(receipt_ref) <= 200):
        reasons.add("MISSING_RECEIPT_REF")

    policy = payload.get("policy_outcome")
    if policy not in {"PASS", "HOLD", "DENY", "ERROR"}:
        reasons.add("INVALID_POLICY_OUTCOME")
    policy_reasons = payload.get("policy_reasons")
    if not isinstance(policy_reasons, list) or len(policy_reasons) > 16 or len(policy_reasons) != len(set(policy_reasons or [])):
        reasons.add("INVALID_POLICY_REASONS")
    elif not all(isinstance(item, str) and REASON.fullmatch(item) for item in policy_reasons):
        reasons.add("INVALID_POLICY_REASON")
    if policy != "PASS" and isinstance(policy_reasons, list) and not policy_reasons:
        reasons.add("MISSING_POLICY_REASON")

    if payload.get("draft") is not True:
        reasons.add("DRAFT_REQUIRED")
    for field, reason in (
        ("merge_allowed", "MERGE_MUST_BE_FALSE"),
        ("release_allowed", "RELEASE_MUST_BE_FALSE"),
        ("deploy_allowed", "DEPLOY_MUST_BE_FALSE"),
        ("promote_allowed", "PROMOTE_MUST_BE_FALSE"),
        ("publish_allowed", "PUBLISH_MUST_BE_FALSE"),
    ):
        if payload.get(field) is not False:
            reasons.add(reason)

    structural_error = bool(reasons)
    write_eligible = not structural_error and policy == "PASS"
    outcome = "PASS" if write_eligible else ("HOLD" if not structural_error else "ERROR")
    if not structural_error and policy != "PASS":
        reasons.add(f"POLICY_{policy}")
    return {"outcome": outcome, "write_eligible": write_eligible, "reason_codes": sorted(reasons)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    try:
        with open(args.path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"outcome": "ERROR", "write_eligible": False, "reason_codes": ["INVALID_JSON"], "detail": str(exc)}, sort_keys=True))
        return 2
    result = validate(payload)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["outcome"] in {"PASS", "HOLD"} else 1


if __name__ == "__main__":
    sys.exit(main())
