#!/usr/bin/env python3
"""Stage private lab refresh candidates from exact provider captures, with no network access."""
import argparse
from datetime import date, datetime
from hashlib import sha256
import json
from pathlib import Path
import re
from runpy import run_path
import shutil
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
LANES = {
    "weather": ("prepare-daily-climate.py", ("heat-and-rain",)),
    "land": ("prepare-drought-and-soil.py", ("county-drought", "soil-profile")),
    "air": ("prepare-daily-air-quality.py", ("daily-air-quality",)),
    "sunlight": ("prepare-sunlight.py", ("sunlight-and-sky",)),
}
MANIFEST = "app/labs/{}/snapshot-manifest.json"
OBSERVATION_KEYS = {"records", "counties", "dates", "weeks"}


def load_inputs(value):
    """Use captured provider objects only. Source references are never fetched."""
    if not isinstance(value, dict) or not isinstance(value.get("sources", {}), (dict, list)):
        raise ValueError("INVALID_SOURCE_RECORD")
    if {"url", "sha256", "capturedAt"} <= value.keys():
        return {value["url"]: (value["sha256"], datetime.fromisoformat(value["capturedAt"]))}
    sources = {}
    for item in value.values():
        if isinstance(item, dict):
            sources.update(load_inputs(item))
        elif isinstance(item, list):
            for entry in item:
                if isinstance(entry, dict):
                    sources.update(load_inputs(entry))
    return sources


def read_layer(root, lab):
    manifest_path = root / MANIFEST.format(lab)
    manifest = json.loads(manifest_path.read_bytes())
    assets = manifest.get("stations", manifest.get("points", [manifest.get("snapshot")]))
    records = {}
    for asset in assets:
        url = asset["url"]
        if not re.fullmatch(r"/science-data/[a-z-]+/[a-z0-9-]+\.json", url):
            raise ValueError("INVALID_SNAPSHOT_PATH")
        raw = (root / "public" / url.lstrip("/")).read_bytes()
        if len(raw) != asset["bytes"] or sha256(raw).hexdigest() != asset["sha256"]:
            raise ValueError("SNAPSHOT_INTEGRITY_MISMATCH")
        data = json.loads(raw)
        if data["period"] != manifest["period"] or asset["id"] in records:
            raise ValueError("SNAPSHOT_SCOPE_MISMATCH")
        records[asset["id"]] = {key: data[key] for key in OBSERVATION_KEYS if key in data}
    sources = load_inputs(manifest)
    if not records or not sources or manifest["scope"] != "provider-context":
        raise ValueError("INCOMPLETE_MANIFEST")
    return manifest, records, sources


def assess(current_root, draft_root, lab):
    old, old_records, old_sources = read_layer(current_root, lab)
    new, new_records, new_sources = read_layer(draft_root, lab)
    before, after = old["period"], new["period"]
    if (old["schema"], old["provider"]) != (new["schema"], new["provider"]) or old_records.keys() != new_records.keys():
        raise ValueError("SNAPSHOT_SCOPE_CHANGED")
    if date.fromisoformat(after["from"]) > date.fromisoformat(before["from"]) or date.fromisoformat(after["to"]) < date.fromisoformat(before["to"]):
        raise ValueError("COVERAGE_WINDOW_REGRESSION")
    if old_sources.keys() - new_sources.keys():
        raise ValueError("PROVIDER_SOURCE_REMOVED")
    changed = [url for url, (digest, _) in new_sources.items() if url not in old_sources or digest != old_sources[url][0]]
    if any(url in old_sources and new_sources[url][1] < old_sources[url][1] for url in changed):
        raise ValueError("OLDER_SOURCE_CAPTURE")
    changed_records = old_records != new_records
    return {"lab": lab, "coverage": after, "changedSourceObjects": len(changed), "observationsChanged": changed_records}


def stage(captures, destination, baseline=ROOT):
    destination = destination.resolve()
    if destination.is_relative_to(baseline.resolve()):
        raise ValueError("STAGE_OUTSIDE_APPLICATION")
    destination.mkdir(mode=0o700)
    results = {}
    for lane, capture in captures.items():
        script, labs = LANES[lane]
        if not capture.is_dir():
            results[lane] = {"state": "waiting-for-capture"}
            continue
        if capture.resolve().is_relative_to(ROOT):
            results[lane] = {"state": "hold", "reason": "CAPTURE_MUST_STAY_PRIVATE"}
            continue
        with TemporaryDirectory(dir=destination) as directory:
            draft = Path(directory) / "output"
            try:
                prepare = run_path(str(ROOT / "scripts" / script))["prepare"]
                prepare(capture, output_root=draft)
            except (OSError, ValueError, KeyError, TypeError):
                results[lane] = {"state": "hold", "reason": "CAPTURE_OR_BUILD_INVALID"}
                continue
            try:
                checks = [assess(baseline, draft, lab) for lab in labs]
            except (OSError, ValueError, KeyError, TypeError) as exc:
                reason = str(exc)
                results[lane] = {"state": "hold", "reason": reason if re.fullmatch("[A-Z_]+", reason) else "SNAPSHOT_VERIFICATION_FAILED"}
                continue
            wrote_candidate = any(check["changedSourceObjects"] or check["observationsChanged"] for check in checks)
            if wrote_candidate:
                shutil.move(draft, destination / lane)
            results[lane] = {"state": "review-required" if wrote_candidate else "unchanged", "checks": checks}
    report = {"schema": "kfm.science-refresh-candidate/v1", "lanes": results}
    (destination / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for lane in LANES:
        parser.add_argument(f"--{lane}", type=Path, help="Existing private capture directory for this lane.")
    parser.add_argument("--stage-dir", type=Path, required=True, help="New directory outside the application.")
    args = parser.parse_args()
    captures = {lane: getattr(args, lane) for lane in LANES if getattr(args, lane) is not None}
    if not captures:
        parser.error("choose at least one capture lane")
    report = stage(captures, args.stage_dir)
    return 2 if any(lane["state"] in {"waiting-for-capture", "hold"} for lane in report["lanes"].values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
