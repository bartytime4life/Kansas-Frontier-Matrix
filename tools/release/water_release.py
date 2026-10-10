#!/usr/bin/env python3
"""Owner-run release steps for a prepared water package.

``decide`` writes a kfm.water-release-decision/v1 record only after the serving
gate answers for it. ``stage``/``activate``/``rollback`` operate a local
serving store (the one ``KFM_RELEASE_STORE`` points kfm-governed-api at).
``stage-hosted`` uploads the package to the Site for owner activation there; it
cannot activate. Nothing here fetches source data or approves on its own.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse
import json
import os
import re
import sys
from urllib.parse import urlsplit
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors_core.captured_json import canonical_bytes, decode_object
from pipelines.domains.hydrology.admission import SOURCE_REF
from pipelines.domains.hydrology.validate import validate_candidate
from release.core import DIGEST, validate_snapshot
from release.local_admin import activate, stage
from release.water_projection import project
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, store_lock
from tools.local_data.water_pilot import immutable

MAX_SNAPSHOT_BYTES = 8 * 1024 * 1024
MAX_VALID_DAYS = 30
CODE = re.compile(r"^[A-Z][A-Z0-9_:]{0,80}$")


def _utc(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _snapshot(root: Path, package_id: str) -> bytes:
    if not DIGEST.fullmatch(package_id):
        raise ValueError("PACKAGE_ID_INVALID")
    raw = read_regular(root / "release/candidates/hydrology" / package_id.split(":")[1] / "snapshot.json", MAX_SNAPSHOT_BYTES)
    manifest, _ = validate_snapshot(raw)
    if manifest["package_id"] != package_id:
        raise ValueError("PACKAGE_PATH_ID_MISMATCH")
    return raw


def build_decision(package_id: str, *, reviewer: str, releaser: str, now: datetime, valid_days: int) -> dict:
    if not 1 <= valid_days <= MAX_VALID_DAYS:
        raise ValueError("VALID_DAYS_OUT_OF_RANGE")
    short = package_id.split(":")[1][:16]
    stamp = _utc(now)
    return {"profile": "kfm.water-release-decision/v1", "package_id": package_id, "decision": "APPROVED",
            "reviewed_at": stamp, "released_at": stamp, "expires_at": _utc(now + timedelta(days=valid_days)),
            "correction_state": "ACTIVE", "correction_ref": None, "reviewer": reviewer, "releaser": releaser,
            "source_admission_ref": SOURCE_REF, "rights_ref": SOURCE_REF + "/rights",
            "sensitivity_ref": SOURCE_REF + "/sensitivity",
            "policy_ref": "kfm://adr/0044" if reviewer == releaser else "kfm://policy/water-serving-gate/v1",
            "review_ref": "kfm://review/water/" + short, "release_ref": "kfm://release/water/" + short}


def decide(root: Path, package_id: str, *, reviewer: str, releaser: str, valid_days: int, now: datetime) -> dict:
    raw = _snapshot(root, package_id)
    decision = build_decision(package_id, reviewer=reviewer, releaser=releaser, now=now, valid_days=valid_days)
    response = project(raw, decision, view="layers", now=decision["released_at"])
    if response["envelope"]["outcome"] != "ANSWER":
        raise ValueError(response["envelope"]["reason_code"])
    relative = Path("release/decisions/hydrology") / package_id.split(":")[1] / (decision["released_at"].replace(":", "") + ".json")
    with store_lock(root):
        immutable(root / relative, canonical_bytes(decision))
    return {"profile": "kfm.water-release-decision-written/v1", "outcome": "DECIDED", "package_id": package_id,
            "decision_path": relative.as_posix(), "expires_at": decision["expires_at"], "activated": False}


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *_args):
        return None


def stage_hosted(root: Path, package_id: str, site_url: str, *, opener=None) -> dict:
    """Upload a prepared package to the Site's staging route; activation stays owner-only on the Site."""
    parts = urlsplit(site_url)
    if parts.scheme != "https" or not parts.hostname or parts.path not in ("", "/") or parts.query or parts.fragment:
        raise ValueError("SITE_URL_INVALID")
    token = os.environ.get("KFM_WATER_WORKER_TOKEN", "")
    if len(token) < 32:
        raise ValueError("WATER_WORKER_TOKEN_REQUIRED")
    raw = _snapshot(root, package_id)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"}
    bypass = os.environ.get("KFM_SITES_BYPASS_TOKEN")
    if bypass:
        headers["OAI-Sites-Authorization"] = f"Bearer {bypass}"
    request = Request(f"https://{parts.netloc}/api/governed/water-admin/stage", data=raw, headers=headers, method="POST")
    try:
        with (opener or build_opener(_NoRedirect())).open(request, timeout=60) as response:
            body = json.loads(response.read(64 * 1024))
    except HTTPError as error:
        try:
            reason = json.loads(error.read(4096)).get("reason_code", "")
        except ValueError:
            reason = ""
        raise ValueError(reason if CODE.fullmatch(str(reason)) else "HOSTED_STAGING_REFUSED") from None
    if body.get("package_id") != package_id or body.get("state") != "STAGED" or body.get("activated") is not False:
        raise ValueError("HOSTED_STAGING_UNEXPECTED_RESPONSE")
    return {"outcome": "STAGED_HOSTED", "package_id": package_id, "site": parts.netloc, "activated": False}


def _decision(path: Path) -> dict:
    decision = decode_object(read_regular(path, 64 * 1024), limit=64 * 1024)
    if decision.get("profile") != "kfm.water-release-decision/v1":
        raise ValueError("DECISION_PROFILE_INVALID")
    return decision


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("decide", "stage", "activate", "rollback", "stage-hosted"):
        sub = commands.add_parser(name)
        sub.add_argument("--root", required=True, help="private acquisition/candidate store")
        if name in ("stage", "activate", "rollback"):
            sub.add_argument("--store", required=True, help="private serving store (KFM_RELEASE_STORE)")
        if name in ("decide", "stage", "stage-hosted"):
            sub.add_argument("--package-id", required=True)
        if name == "stage-hosted":
            sub.add_argument("--site-url", required=True, help="https origin of the KFM Site")
        if name == "decide":
            sub.add_argument("--reviewer", required=True)
            sub.add_argument("--releaser", required=True)
            sub.add_argument("--valid-days", type=int, default=7)
        if name == "stage":
            sub.add_argument("--actor", required=True)
        if name in ("activate", "rollback"):
            sub.add_argument("--decision", required=True, help="decision path relative to --root")
            sub.add_argument("--expected-active", required=True, help="currently active package id, or 'none'")
    args = parser.parse_args(argv)
    now = datetime.now(timezone.utc)
    try:
        root = external_root(args.root)
        if args.command == "decide":
            result = decide(root, args.package_id, reviewer=args.reviewer, releaser=args.releaser,
                            valid_days=args.valid_days, now=now)
        elif args.command == "stage-hosted":
            result = stage_hosted(root, args.package_id, args.site_url)
        elif args.command == "stage":
            package_id = stage(external_root(args.store), _snapshot(root, args.package_id), actor=args.actor,
                               now=_utc(now), validator=validate_candidate)
            result = {"outcome": "STAGED", "package_id": package_id, "activated": False}
        else:
            decision = _decision(root / args.decision)
            expected = None if args.expected_active == "none" else args.expected_active
            result = activate(external_root(args.store), decision["package_id"], decision, expected_active=expected,
                              now=_utc(now), validator=validate_candidate, rollback=args.command == "rollback")
            result = {"outcome": "ROLLED_BACK" if args.command == "rollback" else "ACTIVATED", **result}
    except (ValueError, OSError, KeyError, TypeError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) and CODE.fullmatch(str(exc)) else "WATER_RELEASE_STEP_FAILED"
        print(canonical_bytes({"outcome": "ERROR", "reason_code": reason}).decode())
        return 1
    print(canonical_bytes(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
