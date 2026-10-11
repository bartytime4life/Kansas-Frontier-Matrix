#!/usr/bin/env python3
"""Owner-run release steps for the GHCN-Daily weather layer.

``prepare`` turns a validated WORK candidate into an immutable weather snapshot
(with the admitted license only when ``--admitted-source`` is given).
``decide`` writes a kfm.weather-release-decision/v1 record only when the
weather serving gate (ADR-0045) answers ELIGIBLE for it. Nothing here fetches
source data, stages, activates or publishes; serving is a separate step.
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
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, store_lock
from tools.local_data.water_pilot import immutable

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
    args = parser.parse_args(argv)
    try:
        root = external_root(args.root)
        if args.command == "prepare":
            result = prepare(root, args.candidate_id, rollback_target=args.rollback_target, admitted_source=args.admitted_source)
        else:
            result = decide(root, args.package_id, reviewer=args.reviewer, releaser=args.releaser,
                            valid_days=args.valid_days, now=datetime.now(timezone.utc))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) and CODE.fullmatch(str(exc)) else "WEATHER_RELEASE_STEP_FAILED"
        print(canonical_bytes({"outcome": "ERROR", "reason_code": reason}).decode())
        return 1
    print(canonical_bytes(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
