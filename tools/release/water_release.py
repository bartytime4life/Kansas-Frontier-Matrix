#!/usr/bin/env python3
"""Owner-run release steps for a prepared water package.

``decide`` writes a kfm.water-release-decision/v1 record only after the serving
gate answers for it. ``stage``/``activate``/``rollback`` operate a local
serving store (the one ``KFM_RELEASE_STORE`` points kfm-governed-api at).
``stage-hosted`` uploads the package to the Site for owner activation there; it
cannot activate. ``cycle`` runs capture through decision (and hosted staging) in
one step for the owner. Only ``cycle`` fetches source data; nothing here
activates on the Site.
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
from connectors.usgs.water_data.pilot_capture import capture
from connectors_core.captured_json import canonical_bytes, decode_object
from pipelines.domains.hydrology.admission import SOURCE_REF, load_admission
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.package import prepare_water_package
from pipelines.domains.hydrology.validate import validate_candidate
from release.core import DIGEST, validate_snapshot
from release.local_admin import activate, stage
from release.water_projection import project
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, init_store, store_lock
from tools.local_data.water_pilot import immutable, load_capture, stage as stage_capture
from tools.release.water_snapshot import prepare

MAX_SNAPSHOT_BYTES = 8 * 1024 * 1024
MAX_VALID_DAYS = 30
CODE = re.compile(r"^[A-Z][A-Z0-9_:]{0,80}$")


def _utc(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _snapshot(root: Path, package_id: str) -> bytes:
    if not DIGEST.fullmatch(package_id):
        raise ValueError("PACKAGE_ID_INVALID")
    raw = read_regular(root / "release/candidates/hydrology" / package_id.split(":")[1] / "snapshot.json", MAX_SNAPSHOT_BYTES)
    manifest, values = validate_snapshot(raw)
    if manifest["package_id"] != package_id:
        raise ValueError("PACKAGE_PATH_ID_MISMATCH")
    # validate_snapshot checks hashes and bindings only; a resealed package must also
    # pass the domain validator and carry exactly the receipt it produces.
    candidate = values["candidate.json"]
    if validate_candidate(candidate) != values["validation.json"]:
        raise ValueError("VALIDATION_RECEIPT_MISMATCH")
    # Provenance: the candidate must be exactly what the immutable capture it names normalizes to.
    try:
        capture = load_capture(root, candidate["capture_id"])
    except FileNotFoundError:
        raise ValueError("CAPTURE_NOT_IN_STORE") from None
    except ValueError as exc:
        if str(exc) == "DIRECTORY_MISSING":
            raise ValueError("CAPTURE_NOT_IN_STORE") from None
        raise
    if normalize_capture(capture.manifest, capture.objects, stale_after_seconds=candidate["stale_after_seconds"]) != candidate:
        raise ValueError("CANDIDATE_CAPTURE_MISMATCH")
    # Evidence: bundle rights, sensitivity and hashes are unkeyed, so the package must be exactly
    # what the trusted builder makes from this candidate, either on hold or under the current admission.
    builds = [prepare_water_package(candidate, rollback_target=manifest["rollback_target"], admission=None)]
    try:
        admission = load_admission()
    except ValueError:
        admission = None
    if admission is not None:
        builds.append(prepare_water_package(candidate, rollback_target=manifest["rollback_target"], admission=admission))
    if all(canonical_bytes(build) != raw for build in builds):
        raise ValueError("PACKAGE_NOT_REPRODUCIBLE")
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


def _site_origin(site_url: str) -> str:
    parts = urlsplit(site_url)
    if parts.scheme != "https" or not parts.hostname or parts.path not in ("", "/") or parts.query or parts.fragment:
        raise ValueError("SITE_URL_INVALID")
    return parts.netloc


def _site_call(netloc: str, path: str, *, data: bytes | None = None, opener=None, admin: str = "water-admin") -> dict:
    """One bounded request to a release-admin route with the staging token; no redirects followed.

    ``admin`` names the family's route prefix (``water-admin``, ``weather-admin`` or ``soil-admin``); the Site holds
    one staging token, and each family's routes accept only that family's package profile.
    """
    if admin not in ("water-admin", "weather-admin", "soil-admin"):
        raise ValueError("ADMIN_ROUTE_INVALID")
    token = os.environ.get("KFM_WATER_WORKER_TOKEN", "")
    if len(token) < 32:
        raise ValueError("WATER_WORKER_TOKEN_REQUIRED")
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    bypass = os.environ.get("KFM_SITES_BYPASS_TOKEN")
    if bypass:
        headers["OAI-Sites-Authorization"] = f"Bearer {bypass}"
    request = Request(f"https://{netloc}/api/governed/{admin}/{path}", data=data, headers=headers,
                      method="GET" if data is None else "POST")
    try:
        with (opener or build_opener(_NoRedirect())).open(request, timeout=60) as response:
            body = json.loads(response.read(64 * 1024))
    except HTTPError as error:
        try:
            reason = json.loads(error.read(4096)).get("reason_code", "")
        except ValueError:
            reason = ""
        raise ValueError(reason if CODE.fullmatch(str(reason)) else "HOSTED_REQUEST_REFUSED") from None
    if not isinstance(body, dict):
        raise ValueError("HOSTED_UNEXPECTED_RESPONSE")
    return body


def hosted_active(site_url: str, *, opener=None) -> str | None:
    """The package the Site is serving now; a replacement must name it as its rollback target."""
    body = _site_call(_site_origin(site_url), "status", opener=opener)
    active = body.get("active_package_id")
    if active is not None and not (isinstance(active, str) and DIGEST.fullmatch(active)):
        raise ValueError("HOSTED_UNEXPECTED_RESPONSE")
    return active


def stage_hosted(root: Path, package_id: str, site_url: str, *, opener=None) -> dict:
    """Upload a prepared package to the Site's staging route; activation stays owner-only on the Site."""
    netloc = _site_origin(site_url)
    body = _site_call(netloc, "stage", data=_snapshot(root, package_id), opener=opener)
    if body.get("package_id") != package_id or body.get("state") != "STAGED" or body.get("activated") is not False:
        raise ValueError("HOSTED_STAGING_UNEXPECTED_RESPONSE")
    return {"outcome": "STAGED_HOSTED", "package_id": package_id, "site": netloc, "activated": False}


def cycle(root: Path, *, start: str, end: str, owner: str, valid_days: int, clock=None,
          site_url: str | None = None, rollback_target: str | None = None, acquire=None, opener=None) -> dict:
    """Capture -> candidate -> admitted package -> decision [-> hosted staging]. Never activates.

    With ``site_url`` the rollback target is read from the Site, so the package binds to
    whatever is active there now; activation still happens on the Site's release page.
    """
    if site_url and rollback_target is not None:
        raise ValueError("ROLLBACK_TARGET_FROM_SITE")
    if rollback_target is not None and not DIGEST.fullmatch(rollback_target):
        raise ValueError("ROLLBACK_TARGET_INVALID")
    if not 1 <= valid_days <= MAX_VALID_DAYS:
        raise ValueError("VALID_DAYS_OUT_OF_RANGE")
    if site_url:
        rollback_target = hosted_active(site_url, opener=opener)
    acquired = (acquire or capture)(start, end)
    run = stage_capture(root, acquired)
    if run["outcome"] != "CANDIDATE_READY":
        raise ValueError("CAPTURE_NOT_READY")
    package = prepare(root, run["candidate_id"], rollback_target=rollback_target, admitted_source=True)
    # The package is stamped with the capture's retrieval time, and the gate requires
    # created_at <= reviewed_at, so the decision time is read only after capture.
    now = (clock or (lambda: datetime.now(timezone.utc)))()
    decided = decide(root, package["package_id"], reviewer=owner, releaser=owner, valid_days=valid_days, now=now)
    result = {"profile": "kfm.water-release-cycle/v1", "outcome": "DECIDED", "start": start, "end": end, "capture_id": run["capture_id"],
              "candidate_id": run["candidate_id"], "package_id": package["package_id"], "rollback_target": rollback_target,
              "decision_path": decided["decision_path"], "expires_at": decided["expires_at"],
              "staged_hosted": False, "activated": False}
    if site_url:
        stage_hosted(root, package["package_id"], site_url, opener=opener)
        result |= {"outcome": "STAGED_HOSTED", "staged_hosted": True,
                   "next": f"https://{_site_origin(site_url)}/governed/water-release"}
    return result


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
    refresh = commands.add_parser("cycle", help="capture, package, decide and (with --site-url) stage; never activates")
    refresh.add_argument("--root", required=True, help="private acquisition/candidate store")
    refresh.add_argument("--start", help="UTC start; with --end, at most 24 hours (default: the 24 hours before --end)")
    refresh.add_argument("--end", help="UTC end (default: the current hour)")
    refresh.add_argument("--owner", required=True, help="reviewer and releaser under ADR-0044")
    refresh.add_argument("--valid-days", type=int, default=7)
    target = refresh.add_mutually_exclusive_group()
    target.add_argument("--site-url", help="https origin of the KFM Site; reads the rollback target from it and stages there")
    target.add_argument("--rollback-target", help="active package id for a local-only cycle")
    args = parser.parse_args(argv)
    now = datetime.now(timezone.utc)
    try:
        root = external_root(args.root)
        if args.command == "cycle":
            init_store(root)
            end = args.end or _utc(now.replace(minute=0, second=0, microsecond=0))
            start = args.start or _utc(datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) - timedelta(hours=24))
            result = cycle(root, start=start, end=end, owner=args.owner, valid_days=args.valid_days,
                           site_url=args.site_url, rollback_target=args.rollback_target)
        elif args.command == "decide":
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
