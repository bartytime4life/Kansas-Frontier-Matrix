#!/usr/bin/env python3
"""Deterministic, no-network rollback/withdrawal rehearsal for synthetic roots only.

The helper refuses roots without ``.kfm-synthetic-rollback-rehearsal`` and refuses
scenarios without ``synthetic: true``. Reports are rehearsal evidence, never release,
policy, review, rollback, or publication authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Mapping

MARKER = ".kfm-synthetic-rollback-rehearsal"
REPORT_SCHEMA = "kfm.synthetic_rollback_rehearsal_report.v1"
INVALIDATIONS = tuple(sorted({
    "API_CACHE", "CDN", "TILES", "CATALOG", "TRIPLETS", "SEARCH_INDEX",
    "VECTOR_INDEX", "AI_CACHE", "DOWNSTREAM_DERIVATIVES",
}))


class RehearsalError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest_bytes(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def read_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RehearsalError("REQUIRED_FILE_MISSING", f"missing {path}") from exc
    except json.JSONDecodeError as exc:
        raise RehearsalError("INVALID_JSON", f"invalid JSON in {path}") from exc
    if not isinstance(value, dict):
        raise RehearsalError("INVALID_OBJECT", f"expected object in {path}")
    return value


def safe(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise RehearsalError("UNSAFE_PATH", relative)
    path = root / rel
    resolved = path.resolve(strict=False)
    if root != resolved and root not in resolved.parents:
        raise RehearsalError("UNSAFE_PATH", relative)
    cursor = root
    for part in rel.parts:
        cursor /= part
        if cursor.exists() and cursor.is_symlink():
            raise RehearsalError("UNSAFE_SYMLINK", relative)
    return path


def verify_root(root: Path) -> Path:
    try:
        root = root.resolve(strict=True)
    except FileNotFoundError as exc:
        raise RehearsalError("WORKSPACE_MISSING", str(root)) from exc
    marker = root / MARKER
    if not marker.is_file() or marker.is_symlink():
        raise RehearsalError("SYNTHETIC_MARKER_MISSING", MARKER)
    if marker.read_text(encoding="utf-8") != "synthetic-only\n":
        raise RehearsalError("SYNTHETIC_MARKER_INVALID", MARKER)
    return root


def require_text(obj: Mapping[str, Any], key: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value:
        raise RehearsalError("SCENARIO_INVALID", f"{key} must be text")
    return value


def validate_scenario(s: Mapping[str, Any]) -> None:
    keys = {"scenario_id", "synthetic", "operation", "affected_release_id",
            "target_release_id", "correction", "invalidations", "expected"}
    if set(s) != keys:
        raise RehearsalError("SCENARIO_INVALID", "scenario fields differ from contract")
    if s["synthetic"] is not True:
        raise RehearsalError("NON_SYNTHETIC_INPUT_DENIED", "synthetic must be true")
    require_text(s, "scenario_id")
    require_text(s, "affected_release_id")
    operation = s["operation"]
    target = s["target_release_id"]
    if operation not in {"ROLLBACK", "WITHDRAWAL"}:
        raise RehearsalError("SCENARIO_INVALID", "unsupported operation")
    if operation == "ROLLBACK" and not isinstance(target, str):
        raise RehearsalError("TARGET_REQUIRED", "rollback target missing")
    if operation == "WITHDRAWAL" and target is not None:
        raise RehearsalError("WITHDRAWAL_TARGET_FORBIDDEN", "withdrawal target must be null")
    correction = s["correction"]
    if not isinstance(correction, dict):
        raise RehearsalError("CORRECTION_REQUIRED", "correction object missing")
    for key in ("correction_id", "reason_code", "decided_at"):
        require_text(correction, key)
    invalidations = s["invalidations"]
    if not isinstance(invalidations, list) or tuple(sorted(set(invalidations))) != INVALIDATIONS:
        raise RehearsalError("INVALIDATION_SET_INCOMPLETE", "all carrier invalidations are required")
    expected = s["expected"]
    if not isinstance(expected, dict) or set(expected) != {
        "current_alias_digest", "affected_manifest_digest", "target_manifest_digest"
    }:
        raise RehearsalError("SCENARIO_INVALID", "expected digests missing")


def verify_release(root: Path, release_id: str) -> tuple[dict[str, Any], str, dict[str, str]]:
    manifest = read_object(safe(root, f"releases/{release_id}/manifest.json"))
    if manifest.get("release_id") != release_id:
        raise RehearsalError("RELEASE_ID_MISMATCH", release_id)
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise RehearsalError("MANIFEST_INVALID", release_id)
    actual: dict[str, str] = {}
    for item in artifacts:
        if not isinstance(item, dict) or set(item) != {"path", "digest"}:
            raise RehearsalError("MANIFEST_INVALID", release_id)
        relative, declared = item["path"], item["digest"]
        if not isinstance(relative, str) or relative in actual:
            raise RehearsalError("MANIFEST_INVALID", release_id)
        found = digest_bytes(safe(root, f"releases/{release_id}/{relative}").read_bytes())
        if found != declared:
            raise RehearsalError("ARTIFACT_DIGEST_MISMATCH", relative)
        actual[relative] = found
    return manifest, digest_bytes(canonical(manifest)), dict(sorted(actual.items()))


def verify(root: Path, s: Mapping[str, Any]) -> dict[str, Any]:
    root = verify_root(root)
    validate_scenario(s)
    affected = s["affected_release_id"]
    alias = read_object(safe(root, "published/current.json"))
    alias_digest = digest_bytes(canonical(alias))
    if alias != {"status": "ACTIVE", "release_id": affected}:
        raise RehearsalError("AFFECTED_RELEASE_NOT_CURRENT", affected)
    if alias_digest != s["expected"]["current_alias_digest"]:
        raise RehearsalError("CURRENT_ALIAS_DIGEST_MISMATCH", affected)
    am, amd, aa = verify_release(root, affected)
    if amd != s["expected"]["affected_manifest_digest"]:
        raise RehearsalError("AFFECTED_MANIFEST_DIGEST_MISMATCH", affected)
    tm = tmd = None
    ta: dict[str, str] = {}
    if s["operation"] == "ROLLBACK":
        target = s["target_release_id"]
        if target == affected:
            raise RehearsalError("TARGET_EQUALS_AFFECTED", target)
        tm, tmd, ta = verify_release(root, target)
        if tmd != s["expected"]["target_manifest_digest"]:
            raise RehearsalError("TARGET_MANIFEST_DIGEST_MISMATCH", target)
    return {"alias": alias, "alias_digest": alias_digest, "affected_manifest": am,
            "affected_manifest_digest": amd, "affected_artifacts": aa,
            "target_manifest": tm, "target_manifest_digest": tmd, "target_artifacts": ta}


def write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def rehearse(root: Path, s: Mapping[str, Any], *, apply: bool = False) -> dict[str, Any]:
    root = verify_root(root)
    state = verify(root, s)
    after = ({"status": "ACTIVE", "release_id": s["target_release_id"],
              "supersedes_release_id": s["affected_release_id"],
              "correction_ref": s["correction"]["correction_id"]}
             if s["operation"] == "ROLLBACK" else
             {"status": "WITHDRAWN", "release_id": None,
              "supersedes_release_id": s["affected_release_id"],
              "correction_ref": s["correction"]["correction_id"]})
    report = {
        "schema": REPORT_SCHEMA, "scenario_id": s["scenario_id"], "synthetic": True,
        "mode": "APPLY" if apply else "PLAN", "operation": s["operation"], "outcome": "PASS",
        "reason_code": "SYNTHETIC_REHEARSAL_APPLIED" if apply else "SYNTHETIC_REHEARSAL_PLANNED",
        "before": {"current_alias": state["alias"], "current_alias_digest": state["alias_digest"],
                   "affected_manifest_digest": state["affected_manifest_digest"],
                   "affected_artifact_digests": state["affected_artifacts"]},
        "after": {"current_alias": after, "current_alias_digest": digest_bytes(canonical(after)),
                  "target_manifest_digest": state["target_manifest_digest"],
                  "target_artifact_digests": state["target_artifacts"]},
        "correction": s["correction"], "invalidations": list(INVALIDATIONS),
        "preservation": {"affected_manifest_retained": True, "affected_artifacts_retained": True,
                         "append_only_correction": True},
        "governance": {"authority_created": False, "policy_evaluated": False,
                       "review_completed": False, "release_authorized": False,
                       "publication_authorized": False, "public_state_mutated": False,
                       "synthetic_workspace_only": True},
    }
    if not apply:
        return report
    affected = s["affected_release_id"]
    history = {"manifest": digest_bytes(safe(root, f"releases/{affected}/manifest.json").read_bytes()),
               **{p: digest_bytes(safe(root, f"releases/{affected}/{p}").read_bytes())
                  for p in state["affected_artifacts"]}}
    write_json(safe(root, "published/current.json"), after)
    write_json(safe(root, f"corrections/{s['correction']['correction_id']}.json"),
               {**s["correction"], "affected_release_id": affected, "operation": s["operation"],
                "target_release_id": s["target_release_id"], "synthetic": True})
    write_json(safe(root, f"invalidations/{s['scenario_id']}.json"),
               {"scenario_id": s["scenario_id"], "affected_release_id": affected,
                "invalidations": list(INVALIDATIONS), "synthetic": True})
    current = {"manifest": digest_bytes(safe(root, f"releases/{affected}/manifest.json").read_bytes()),
               **{p: digest_bytes(safe(root, f"releases/{affected}/{p}").read_bytes())
                  for p in state["affected_artifacts"]}}
    if current != history:
        raise RehearsalError("HISTORY_MUTATED", affected)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--scenario", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        result = rehearse(args.workspace, read_object(args.scenario), apply=args.apply)
        code = 0
    except RehearsalError as exc:
        result = {"schema": REPORT_SCHEMA, "outcome": "HOLD", "reason_code": exc.code,
                  "message": str(exc), "governance": {"authority_created": False,
                  "public_state_mutated": False, "synthetic_workspace_only": True}}
        code = 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    if args.report:
        write_json(args.report, result)
    return code


if __name__ == "__main__":
    sys.exit(main())
