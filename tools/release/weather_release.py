#!/usr/bin/env python3
"""Owner-run release steps for the GHCN-Daily weather layer.

``prepare`` turns a validated WORK candidate into an immutable weather snapshot
(with the admitted license only when ``--admitted-source`` is given).
``decide`` writes a kfm.weather-release-decision/v1 record only when the
weather serving gate (ADR-0045) answers ELIGIBLE for it. ``stage``/``activate``/
``rollback`` operate the weather tables of a local serving store (the one
``KFM_RELEASE_STORE`` points kfm-governed-api at). ``stage-hosted`` uploads a
package to the Site's weather staging route; it cannot activate. ``cycle`` runs
capture through decision (and hosted staging) in one step for the owner. Only
``cycle`` fetches source data; nothing here activates on the Site.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors_core.captured_json import canonical_bytes, decode_object
from pipelines.domains.atmosphere.ghcnd_daily_admission import SOURCE_REF, load_admission
from pipelines.domains.atmosphere.ghcnd_daily_package import prepare_weather_package
from policy_runtime.core import WEATHER_DECISION_PROFILE, WEATHER_SELF_RELEASE_LICENSES, serving_gate
from release.core import DIGEST, WEATHER, validate_snapshot
from release.water_projection import replay_evidence
from release.local_admin import activate, stage
from pipelines.domains.atmosphere.ghcnd_daily_validate import validate_candidate
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, init_store, store_lock
from tools.local_data.water_pilot import immutable
from tools.local_data import ghcnd_daily_pilot
from tools.release.water_release import _site_call, _site_origin
from connectors.noaa.src.noaa.ghcnd_daily_capture import capture

MAX_SNAPSHOT_BYTES = 8 * 1024 * 1024
MAX_VALID_DAYS = 30
CODE = re.compile(r"^[A-Z][A-Z0-9_:]{0,80}$")
CANDIDATES = Path("data/work/atmosphere/noaa-ghcnd-daily")
SNAPSHOTS = Path("release/candidates/atmosphere")
DECISIONS = Path("release/decisions/atmosphere")


def _utc(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _short(digest: str, code: str) -> str:
    if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
        raise ValueError(code)
    return digest.split(":")[1]


def prepare(root: Path, candidate_id: str, *, rollback_target=None, admitted_source=False) -> dict:
    raw = read_regular(root / CANDIDATES / _short(candidate_id, "INVALID_CANDIDATE_ID") / "candidate.json", MAX_SNAPSHOT_BYTES)
    candidate = decode_object(raw, limit=MAX_SNAPSHOT_BYTES)
    if candidate.get("candidate_id") != candidate_id:
        raise ValueError("CANDIDATE_PATH_ID_MISMATCH")
    admission = load_admission() if admitted_source else None
    snapshot = prepare_weather_package(candidate, rollback_target=rollback_target, admission=admission)
    package_id = snapshot["manifest"]["package_id"]
    with store_lock(root):
        immutable(root / SNAPSHOTS / package_id.split(":")[1] / "snapshot.json", canonical_bytes(snapshot))
    return {"profile": "kfm.weather-package-preparation/v1", "package_id": package_id, "candidate_id": candidate_id,
            "outcome": "PREPARED", "reason_code": "RELEASE_DECISION_REQUIRED" if admission else "REVIEW_REQUIRED",
            "admitted_source": admission["source_ref"] if admission else None, "activated": False, "published": False}


def _snapshot(root: Path, package_id: str) -> tuple[dict, dict]:
    raw = read_regular(root / SNAPSHOTS / _short(package_id, "PACKAGE_ID_INVALID") / "snapshot.json", MAX_SNAPSHOT_BYTES)
    manifest, values = validate_snapshot(raw, profile=WEATHER)
    if manifest["package_id"] != package_id:
        raise ValueError("PACKAGE_PATH_ID_MISMATCH")
    return manifest, values


def build_decision(package_id: str, *, reviewer: str, releaser: str, now: datetime, valid_days: int) -> dict:
    if not 1 <= valid_days <= MAX_VALID_DAYS:
        raise ValueError("VALID_DAYS_OUT_OF_RANGE")
    short = package_id.split(":")[1][:16]
    stamp = _utc(now)
    return {"profile": WEATHER_DECISION_PROFILE, "package_id": package_id, "decision": "APPROVED",
            "reviewed_at": stamp, "released_at": stamp, "expires_at": _utc(now + timedelta(days=valid_days)),
            "correction_state": "ACTIVE", "correction_ref": None, "reviewer": reviewer, "releaser": releaser,
            "source_admission_ref": SOURCE_REF, "rights_ref": SOURCE_REF + "/rights",
            "sensitivity_ref": SOURCE_REF + "/sensitivity",
            "policy_ref": "kfm://adr/0045" if reviewer == releaser else "kfm://policy/weather-serving-gate/v1",
            "review_ref": "kfm://review/weather/" + short, "release_ref": "kfm://release/weather/" + short}


def decide(root: Path, package_id: str, *, reviewer: str, releaser: str, valid_days: int, now: datetime) -> dict:
    manifest, values = _snapshot(root, package_id)
    decision = build_decision(package_id, reviewer=reviewer, releaser=releaser, now=now, valid_days=valid_days)
    outcome = serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"],
                           decision_profile=WEATHER_DECISION_PROFILE, licenses=WEATHER_SELF_RELEASE_LICENSES)
    if outcome != "ELIGIBLE":
        raise ValueError(outcome)
    # The gate checks release metadata, rights and sensitivity; serving also replays
    # every bundle's integrity and resolution, so a decision is written only if it would.
    failure = replay_evidence(values["evidence.json"]["entries"], decision, decision["released_at"])
    if failure:
        raise ValueError(failure[0])
    relative = DECISIONS / package_id.split(":")[1] / (decision["released_at"].replace(":", "") + ".json")
    with store_lock(root):
        immutable(root / relative, canonical_bytes(decision))
    return {"profile": "kfm.weather-release-decision-written/v1", "outcome": "DECIDED", "package_id": package_id,
            "decision_path": relative.as_posix(), "expires_at": decision["expires_at"], "activated": False}


def hosted_active(site_url: str, *, opener=None) -> str | None:
    """The weather package the Site is serving now; a replacement must name it as its rollback target."""
    body = _site_call(_site_origin(site_url), "status", opener=opener, admin="weather-admin")
    active = body.get("active_package_id")
    if active is not None and not (isinstance(active, str) and DIGEST.fullmatch(active)):
        raise ValueError("HOSTED_UNEXPECTED_RESPONSE")
    return active


def stage_hosted(root: Path, package_id: str, site_url: str, *, opener=None) -> dict:
    """Upload a prepared weather package to the Site's staging route; activation stays owner-only there."""
    netloc = _site_origin(site_url)
    raw = read_regular(root / SNAPSHOTS / _short(package_id, "PACKAGE_ID_INVALID") / "snapshot.json", MAX_SNAPSHOT_BYTES)
    if validate_snapshot(raw, profile=WEATHER)[0]["package_id"] != package_id:
        raise ValueError("PACKAGE_PATH_ID_MISMATCH")
    body = _site_call(netloc, "stage", data=raw, opener=opener, admin="weather-admin")
    if body.get("package_id") != package_id or body.get("state") != "STAGED" or body.get("activated") is not False:
        raise ValueError("HOSTED_STAGING_UNEXPECTED_RESPONSE")
    return {"outcome": "STAGED_HOSTED", "package_id": package_id, "site": netloc, "activated": False}


def cycle(root: Path, *, end_date: str, owner: str, valid_days: int, clock=None,
          site_url: str | None = None, rollback_target: str | None = None, acquire=None, opener=None) -> dict:
    """Capture -> candidate -> admitted package -> decision [-> hosted staging]. Never activates.

    With ``site_url`` the rollback target is read from the Site before capturing, so the
    package binds to whatever weather package is active there now.
    """
    if site_url and rollback_target is not None:
        raise ValueError("ROLLBACK_TARGET_FROM_SITE")
    if rollback_target is not None and not DIGEST.fullmatch(rollback_target):
        raise ValueError("ROLLBACK_TARGET_INVALID")
    if not 1 <= valid_days <= MAX_VALID_DAYS:
        raise ValueError("VALID_DAYS_OUT_OF_RANGE")
    if site_url:
        rollback_target = hosted_active(site_url, opener=opener)
    run = ghcnd_daily_pilot.stage(root, (acquire or capture)(end_date))
    if run["outcome"] != "CANDIDATE_READY":
        raise ValueError("CAPTURE_NOT_READY")
    package = prepare(root, run["candidate_id"], rollback_target=rollback_target, admitted_source=True)
    # The package carries the capture's retrieval time and the gate requires created_at <= reviewed_at,
    # so the decision time is read only after capture.
    now = (clock or (lambda: datetime.now(timezone.utc)))()
    decided = decide(root, package["package_id"], reviewer=owner, releaser=owner, valid_days=valid_days, now=now)
    result = {"profile": "kfm.weather-release-cycle/v1", "outcome": "DECIDED", "end_date": end_date,
              "capture_id": run["capture_id"], "candidate_id": run["candidate_id"], "package_id": package["package_id"],
              "rollback_target": rollback_target, "decision_path": decided["decision_path"],
              "expires_at": decided["expires_at"], "staged_hosted": False, "activated": False}
    if site_url:
        stage_hosted(root, package["package_id"], site_url, opener=opener)
        result |= {"outcome": "STAGED_HOSTED", "staged_hosted": True,
                   "next": f"https://{_site_origin(site_url)}/governed/weather-release"}
    return result


def _decision(path: Path) -> dict:
    decision = decode_object(read_regular(path, 64 * 1024), limit=64 * 1024)
    if decision.get("profile") != WEATHER_DECISION_PROFILE:
        raise ValueError("DECISION_PROFILE_INVALID")
    return decision


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    make = commands.add_parser("prepare", help="build an immutable weather snapshot from a WORK candidate")
    make.add_argument("--root", required=True, help="private acquisition/candidate store")
    make.add_argument("--candidate-id", required=True)
    make.add_argument("--rollback-target")
    make.add_argument("--admitted-source", action="store_true",
                      help="carry the admitted license and public sensitivity from data/registry/sources/atmosphere/noaa_ghcnd.yaml")
    rule = commands.add_parser("decide", help="write a release decision if the weather gate would serve it")
    rule.add_argument("--root", required=True)
    rule.add_argument("--package-id", required=True)
    rule.add_argument("--reviewer", required=True)
    rule.add_argument("--releaser", required=True)
    rule.add_argument("--valid-days", type=int, default=7)
    hosted = commands.add_parser("stage-hosted", help="upload a prepared package to the Site; never activates")
    hosted.add_argument("--root", required=True)
    hosted.add_argument("--package-id", required=True)
    hosted.add_argument("--site-url", required=True, help="https origin of the KFM Site")
    refresh = commands.add_parser("cycle", help="capture, package, decide and (with --site-url) stage; never activates")
    refresh.add_argument("--root", required=True, help="private acquisition/candidate store")
    refresh.add_argument("--end-date", help="last observation day, YYYY-MM-DD (default: yesterday, UTC)")
    refresh.add_argument("--owner", required=True, help="reviewer and releaser under ADR-0045")
    refresh.add_argument("--valid-days", type=int, default=7)
    target = refresh.add_mutually_exclusive_group()
    target.add_argument("--site-url", help="https origin of the KFM Site; reads the rollback target from it and stages there")
    target.add_argument("--rollback-target", help="active weather package id for a local-only cycle")
    for name in ("stage", "activate", "rollback"):
        sub = commands.add_parser(name)
        sub.add_argument("--root", required=True, help="private acquisition/candidate store")
        sub.add_argument("--store", required=True, help="private serving store (KFM_RELEASE_STORE)")
        if name == "stage":
            sub.add_argument("--package-id", required=True)
            sub.add_argument("--actor", required=True)
        else:
            sub.add_argument("--decision", required=True, help="decision path relative to --root")
            sub.add_argument("--expected-active", required=True, help="currently active weather package id, or 'none'")
    args = parser.parse_args(argv)
    now = datetime.now(timezone.utc)
    try:
        root = external_root(args.root)
        if args.command in ("cycle", "stage-hosted"):
            if args.command == "cycle":
                init_store(root)
                end_date = args.end_date or (now - timedelta(days=1)).date().isoformat()
                result = cycle(root, end_date=end_date, owner=args.owner, valid_days=args.valid_days,
                               site_url=args.site_url, rollback_target=args.rollback_target)
            else:
                result = stage_hosted(root, args.package_id, args.site_url)
            print(canonical_bytes(result).decode())
            return 0
        if args.command == "stage":
            raw = read_regular(root / SNAPSHOTS / _short(args.package_id, "PACKAGE_ID_INVALID") / "snapshot.json", MAX_SNAPSHOT_BYTES)
            package_id = stage(external_root(args.store), raw, actor=args.actor, now=_utc(now),
                               validator=validate_candidate, family="weather")
            print(canonical_bytes({"outcome": "STAGED", "package_id": package_id, "activated": False}).decode())
            return 0
        if args.command in ("activate", "rollback"):
            decision = _decision(root / args.decision)
            expected = None if args.expected_active == "none" else args.expected_active
            result = activate(external_root(args.store), decision["package_id"], decision, expected_active=expected, now=_utc(now),
                              validator=validate_candidate, rollback=args.command == "rollback", family="weather")
            print(canonical_bytes({"outcome": "ROLLED_BACK" if args.command == "rollback" else "ACTIVATED", **result}).decode())
            return 0
        if args.command == "prepare":
            result = prepare(root, args.candidate_id, rollback_target=args.rollback_target, admitted_source=args.admitted_source)
        else:
            result = decide(root, args.package_id, reviewer=args.reviewer, releaser=args.releaser,
                            valid_days=args.valid_days, now=now)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) and CODE.fullmatch(str(exc)) else "WEATHER_RELEASE_STEP_FAILED"
        print(canonical_bytes({"outcome": "ERROR", "reason_code": reason}).decode())
        return 1
    print(canonical_bytes(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
