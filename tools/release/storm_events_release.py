#!/usr/bin/env python3
"""Owner-run release steps for the NOAA Storm Events layer.

``prepare`` turns a validated WORK candidate into an immutable storm events
snapshot (with the admitted license only when ``--admitted-source`` is given).
``decide`` writes a kfm.storm-events-release-decision/v1 record only when the
storm events serving gate (ADR-0047) answers ELIGIBLE for it and every evidence
bundle replays. ``stage``/``activate``/``rollback`` operate the storm events
tables of a local serving store (the one ``KFM_RELEASE_STORE`` points
kfm-governed-api at, which serves /v1/storm-events/*). ``stage-hosted`` uploads
a package to the Site's storm events staging route; it cannot activate.
``cycle`` runs capture through decision (and hosted staging) in one step for the
owner. Only ``cycle`` fetches source data; nothing here activates on the Site.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors_core.captured_json import canonical_bytes, decode_object
from pipelines.domains.hazards.storm_events_admission import SOURCE_REF, load_admission
from pipelines.domains.hazards.storm_events_normalize import normalize_capture
from pipelines.domains.hazards.storm_events_package import prepare_storm_events_package
from pipelines.domains.hazards.storm_events_validate import validate_candidate
from policy_runtime.core import STORM_EVENTS_DECISION_PROFILE, STORM_EVENTS_SELF_RELEASE_LICENSES, serving_gate
from release.core import DIGEST, STORM_EVENTS, validate_snapshot
from release.local_admin import activate, stage
from release.water_projection import replay_evidence
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, init_store, store_lock
from tools.local_data import storm_events_pilot
from tools.local_data.storm_events_pilot import LANE
from tools.local_data.water_pilot import immutable
from tools.release.water_release import _site_call, _site_origin
from connectors.noaa.src.noaa.storm_events_capture import capture

MAX_SNAPSHOT_BYTES = 8 * 1024 * 1024
MAX_VALID_DAYS = 30
CODE = re.compile(r"^[A-Z][A-Z0-9_:]{0,80}$")
CANDIDATES = Path("data/work/hazards") / LANE
SNAPSHOTS = Path("release/candidates/storm-events")
DECISIONS = Path("release/decisions/storm-events")


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
    snapshot = prepare_storm_events_package(candidate, rollback_target=rollback_target, admission=admission)
    package_id = snapshot["manifest"]["package_id"]
    with store_lock(root):
        immutable(root / SNAPSHOTS / package_id.split(":")[1] / "snapshot.json", canonical_bytes(snapshot))
    return {"profile": "kfm.storm-events-package-preparation/v1", "package_id": package_id, "candidate_id": candidate_id,
            "outcome": "PREPARED", "reason_code": "RELEASE_DECISION_REQUIRED" if admission else "REVIEW_REQUIRED",
            "admitted_source": admission["source_ref"] if admission else None, "activated": False, "published": False}


def _snapshot(root: Path, package_id: str) -> tuple[dict, dict]:
    raw = read_regular(root / SNAPSHOTS / _short(package_id, "PACKAGE_ID_INVALID") / "snapshot.json", MAX_SNAPSHOT_BYTES)
    manifest, values = validate_snapshot(raw, profile=STORM_EVENTS)
    if manifest["package_id"] != package_id:
        raise ValueError("PACKAGE_PATH_ID_MISMATCH")
    # validate_snapshot checks hashes and bindings only; a resealed package must also
    # pass the domain validator and carry exactly the receipt it produces.
    if validate_candidate(values["candidate.json"]) != values["validation.json"]:
        raise ValueError("VALIDATION_RECEIPT_MISMATCH")
    # Provenance: the candidate must be exactly what the immutable capture it names normalizes to.
    try:
        capture = storm_events_pilot.load_capture(root, values["candidate.json"]["capture_id"])
    except FileNotFoundError:
        raise ValueError("CAPTURE_NOT_IN_STORE") from None
    except ValueError as exc:
        if str(exc) == "DIRECTORY_MISSING":
            raise ValueError("CAPTURE_NOT_IN_STORE") from None
        raise
    if normalize_capture(capture.manifest, capture.objects) != values["candidate.json"]:
        raise ValueError("CANDIDATE_CAPTURE_MISMATCH")
    # Evidence: bundle rights, sensitivity and hashes are unkeyed, so the package must be exactly
    # what the trusted builder makes from this candidate, either on hold or under the current admission.
    builds = [prepare_storm_events_package(values["candidate.json"], rollback_target=manifest["rollback_target"], admission=None)]
    try:
        admission = load_admission()
    except ValueError:
        admission = None
    if admission is not None:
        builds.append(prepare_storm_events_package(values["candidate.json"], rollback_target=manifest["rollback_target"],
                                                   admission=admission))
    if all(canonical_bytes(build) != raw for build in builds):
        raise ValueError("PACKAGE_NOT_REPRODUCIBLE")
    return manifest, values


def build_decision(package_id: str, *, reviewer: str, releaser: str, now: datetime, valid_days: int) -> dict:
    if not 1 <= valid_days <= MAX_VALID_DAYS:
        raise ValueError("VALID_DAYS_OUT_OF_RANGE")
    short = package_id.split(":")[1][:16]
    stamp = _utc(now)
    return {"profile": STORM_EVENTS_DECISION_PROFILE, "package_id": package_id, "decision": "APPROVED",
            "reviewed_at": stamp, "released_at": stamp, "expires_at": _utc(now + timedelta(days=valid_days)),
            "correction_state": "ACTIVE", "correction_ref": None, "reviewer": reviewer, "releaser": releaser,
            "source_admission_ref": SOURCE_REF, "rights_ref": SOURCE_REF + "/rights",
            "sensitivity_ref": SOURCE_REF + "/sensitivity",
            "policy_ref": "kfm://adr/0047" if reviewer == releaser else "kfm://policy/storm-events-serving-gate/v1",
            "review_ref": "kfm://review/storm-events/" + short, "release_ref": "kfm://release/storm-events/" + short}


def decide(root: Path, package_id: str, *, reviewer: str, releaser: str, valid_days: int, now: datetime) -> dict:
    manifest, values = _snapshot(root, package_id)
    decision = build_decision(package_id, reviewer=reviewer, releaser=releaser, now=now, valid_days=valid_days)
    outcome = serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"],
                           decision_profile=STORM_EVENTS_DECISION_PROFILE, licenses=STORM_EVENTS_SELF_RELEASE_LICENSES)
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
    return {"profile": "kfm.storm-events-release-decision-written/v1", "outcome": "DECIDED", "package_id": package_id,
            "decision_path": relative.as_posix(), "expires_at": decision["expires_at"], "activated": False}


def hosted_active(site_url: str, *, opener=None) -> str | None:
    """The storm events package the Site is serving now; a replacement must name it as its rollback target."""
    body = _site_call(_site_origin(site_url), "status", opener=opener, admin="storm-events-admin")
    active = body.get("active_package_id")
    if active is not None and not (isinstance(active, str) and DIGEST.fullmatch(active)):
        raise ValueError("HOSTED_UNEXPECTED_RESPONSE")
    return active


def stage_hosted(root: Path, package_id: str, site_url: str, *, opener=None) -> dict:
    """Upload a prepared storm events package to the Site's staging route; activation stays owner-only there."""
    netloc = _site_origin(site_url)
    # The same checks as decide: carrier, domain revalidation, the stored capture and a reproducible package.
    _snapshot(root, package_id)
    raw = read_regular(root / SNAPSHOTS / _short(package_id, "PACKAGE_ID_INVALID") / "snapshot.json", MAX_SNAPSHOT_BYTES)
    body = _site_call(netloc, "stage", data=raw, opener=opener, admin="storm-events-admin")
    if body.get("package_id") != package_id or body.get("state") != "STAGED" or body.get("activated") is not False:
        raise ValueError("HOSTED_STAGING_UNEXPECTED_RESPONSE")
    return {"outcome": "STAGED_HOSTED", "package_id": package_id, "site": netloc, "activated": False}


def cycle(root: Path, *, year: int, owner: str, valid_days: int, clock=None,
          site_url: str | None = None, rollback_target: str | None = None, acquire=None, opener=None) -> dict:
    """Capture -> candidate -> admitted package -> decision [-> hosted staging]. Never activates.

    With ``site_url`` the rollback target is read from the Site before capturing, so the
    package binds to whatever storm events package is active there now.
    """
    if site_url and rollback_target is not None:
        raise ValueError("ROLLBACK_TARGET_FROM_SITE")
    if rollback_target is not None and not DIGEST.fullmatch(rollback_target):
        raise ValueError("ROLLBACK_TARGET_INVALID")
    if not 1 <= valid_days <= MAX_VALID_DAYS:
        raise ValueError("VALID_DAYS_OUT_OF_RANGE")
    if site_url:
        rollback_target = hosted_active(site_url, opener=opener)
    run = storm_events_pilot.stage(root, (acquire or capture)(year))
    if run["outcome"] != "CANDIDATE_READY":
        raise ValueError("CAPTURE_NOT_READY")
    package = prepare(root, run["candidate_id"], rollback_target=rollback_target, admitted_source=True)
    # The package carries the capture's retrieval time and the gate requires created_at <= reviewed_at,
    # so the decision time is read only after capture.
    now = (clock or (lambda: datetime.now(timezone.utc)))()
    decided = decide(root, package["package_id"], reviewer=owner, releaser=owner, valid_days=valid_days, now=now)
    result = {"profile": "kfm.storm-events-release-cycle/v1", "outcome": "DECIDED", "data_year": year,
              "capture_id": run["capture_id"], "candidate_id": run["candidate_id"], "package_id": package["package_id"],
              "rollback_target": rollback_target, "decision_path": decided["decision_path"],
              "expires_at": decided["expires_at"], "staged_hosted": False, "activated": False}
    if site_url:
        stage_hosted(root, package["package_id"], site_url, opener=opener)
        result |= {"outcome": "STAGED_HOSTED", "staged_hosted": True,
                   "next": f"https://{_site_origin(site_url)}/governed/storm-events-release"}
    return result


def _decision(path: Path) -> dict:
    decision = decode_object(read_regular(path, 64 * 1024), limit=64 * 1024)
    if decision.get("profile") != STORM_EVENTS_DECISION_PROFILE:
        raise ValueError("DECISION_PROFILE_INVALID")
    return decision


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    make = commands.add_parser("prepare", help="build an immutable storm events snapshot from a WORK candidate")
    make.add_argument("--root", required=True, help="private acquisition/candidate store")
    make.add_argument("--candidate-id", required=True)
    make.add_argument("--rollback-target")
    make.add_argument("--admitted-source", action="store_true",
                      help="carry the admitted license and public sensitivity from data/registry/sources/hazards/noaa.storm_events.yaml")
    rule = commands.add_parser("decide", help="write a release decision if the storm events gate would serve it")
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
    refresh.add_argument("--year", required=True, type=int, help="data year; the newest details file NCEI lists for it is captured")
    refresh.add_argument("--owner", required=True, help="reviewer and releaser under ADR-0047")
    refresh.add_argument("--valid-days", type=int, default=7)
    target = refresh.add_mutually_exclusive_group()
    target.add_argument("--site-url", help="https origin of the KFM Site; reads the rollback target from it and stages there")
    target.add_argument("--rollback-target", help="active storm events package id for a local-only cycle")
    for name in ("stage", "activate", "rollback"):
        sub = commands.add_parser(name)
        sub.add_argument("--root", required=True, help="private acquisition/candidate store")
        sub.add_argument("--store", required=True, help="private serving store (KFM_RELEASE_STORE)")
        if name == "stage":
            sub.add_argument("--package-id", required=True)
            sub.add_argument("--actor", required=True)
        else:
            sub.add_argument("--decision", required=True, help="decision path relative to --root")
            sub.add_argument("--expected-active", required=True, help="currently active storm events package id, or 'none'")
    args = parser.parse_args(argv)
    now = datetime.now(timezone.utc)
    try:
        root = external_root(args.root)
        if args.command in ("cycle", "stage-hosted"):
            if args.command == "cycle":
                init_store(root)
                result = cycle(root, year=args.year, owner=args.owner, valid_days=args.valid_days,
                               site_url=args.site_url, rollback_target=args.rollback_target)
            else:
                result = stage_hosted(root, args.package_id, args.site_url)
            print(canonical_bytes(result).decode())
            return 0
        if args.command == "stage":
            # The same checks as decide: carrier, domain revalidation, stored capture and reproducibility.
            _snapshot(root, args.package_id)
            raw = read_regular(root / SNAPSHOTS / _short(args.package_id, "PACKAGE_ID_INVALID") / "snapshot.json", MAX_SNAPSHOT_BYTES)
            package_id = stage(external_root(args.store), raw, actor=args.actor, now=_utc(now),
                               validator=validate_candidate, family="storm_events")
            print(canonical_bytes({"outcome": "STAGED", "package_id": package_id, "activated": False}).decode())
            return 0
        if args.command in ("activate", "rollback"):
            decision = _decision(root / args.decision)
            expected = None if args.expected_active == "none" else args.expected_active
            result = activate(external_root(args.store), decision["package_id"], decision, expected_active=expected, now=_utc(now),
                              validator=validate_candidate, rollback=args.command == "rollback", family="storm_events")
            print(canonical_bytes({"outcome": "ROLLED_BACK" if args.command == "rollback" else "ACTIVATED", **result}).decode())
            return 0
        if args.command == "prepare":
            result = prepare(root, args.candidate_id, rollback_target=args.rollback_target, admitted_source=args.admitted_source)
        else:
            result = decide(root, args.package_id, reviewer=args.reviewer, releaser=args.releaser,
                            valid_days=args.valid_days, now=now)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) and CODE.fullmatch(str(exc)) else "STORM_EVENTS_RELEASE_STEP_FAILED"
        print(canonical_bytes({"outcome": "ERROR", "reason_code": reason}).decode())
        return 1
    print(canonical_bytes(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
