#!/usr/bin/env python3
"""Regenerate the declared synthetic water fixtures in isolated output only."""
from pathlib import Path
import argparse
import json
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes
from pipelines.domains.hydrology.admission import load_admission
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.package import prepare_water_package
from hashing import compute_spec_hash
from release.water_projection import project
from tools.local_data.file_io import read_regular, write_new

PROFILE = ROOT / "control_plane/readiness/fixture-regeneration-manifest.json"


def generated(profile):
    raw = read_regular(ROOT / profile["input_path"], 512 * 1024)
    if digest_bytes(raw) != profile["input_digest"]:
        raise ValueError("FIXTURE_INPUT_DIGEST_MISMATCH")
    source = decode_object(raw, limit=512 * 1024)
    if source["posture"] != "SYNTHETIC_TEST_ONLY":
        raise ValueError("SYNTHETIC_INPUT_REQUIRED")
    candidate = normalize_capture(source["manifest"], {key: text.encode() for key, text in source["objects"].items()})
    held = prepare_water_package(candidate)
    snapshot = json.loads(json.dumps(held))
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        bundle["sensitivity"] = {"level": "public", "reason": "SYNTHETIC TEST ONLY", "applied_at": profile["evaluated_at"]}
        bundle["rights"] = {"license": "SYNTHETIC TEST ONLY - no real rights grant"}
        bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
    snapshot["artifacts"]["evidence.json"] = canonical_bytes(evidence).decode()
    snapshot["manifest"]["artifacts"]["evidence.json"] = digest_bytes(snapshot["artifacts"]["evidence.json"].encode())
    snapshot["manifest"]["package_id"] = compute_spec_hash({k: v for k, v in snapshot["manifest"].items() if k != "package_id"})
    decision = {"profile": "kfm.water-release-decision/v1", "package_id": snapshot["manifest"]["package_id"],
                "decision": "APPROVED", "reviewed_at": "2026-09-30T18:30:00Z", "released_at": "2026-09-30T18:45:00Z", "expires_at": "2026-10-01T00:00:00Z",
                "correction_state": "ACTIVE", "correction_ref": None, "reviewer": "synthetic-reviewer", "releaser": "synthetic-releaser"}
    for name in ("source_admission", "rights", "sensitivity", "policy", "review", "release"):
        decision[name + "_ref"] = "kfm://synthetic/" + name
    # ADR-0044: the admitted license on synthetic input, released by one person.
    admitted = prepare_water_package(candidate, admission=load_admission())
    owner_decision = dict(decision, package_id=admitted["manifest"]["package_id"],
                          reviewer="synthetic-owner", releaser="synthetic-owner")
    values = {"snapshot.json": snapshot, "held-snapshot.json": held, "decision.json": decision,
              "admitted-snapshot.json": admitted, "owner-decision.json": owner_decision}
    for view in ("bootstrap", "layers", "evidence"):
        values[view + ".json"] = project(canonical_bytes(snapshot), decision, view=view, now=profile["evaluated_at"])
    return {name: canonical_bytes(value) for name, value in values.items()}


def regenerate(output: Path, *, check=True):
    if output.is_symlink() or output.exists() and any(output.iterdir()) or output.resolve().is_relative_to(ROOT):
        raise ValueError("ISOLATED_EMPTY_OUTPUT_REQUIRED")
    profile = json.loads(PROFILE.read_text())
    if profile["posture"] != "SYNTHETIC_TEST_ONLY" or profile["profile"] != "kfm.water-fixture-regeneration/v1":
        raise ValueError("PROFILE_INVALID")
    values = generated(profile)
    if set(values) != set(profile["outputs"]):
        raise ValueError("FIXTURE_OUTPUT_CLOSURE")
    for name, raw in values.items():
        if check and (digest_bytes(raw) != profile["outputs"][name] or read_regular(ROOT / profile["reviewed_root"] / name, 512*1024) != raw):
            raise ValueError("FIXTURE_DRIFT")
        write_new(output / name, raw)
    return {"outcome": "PASS", "generated": len(values), "authority": "synthetic_only", "reviewed_files_overwritten": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir")
    args = parser.parse_args(argv)
    try:
        if args.output_dir:
            result = regenerate(Path(args.output_dir))
        else:
            with tempfile.TemporaryDirectory(prefix="kfm-fixtures-") as directory:
                result = regenerate(Path(directory))
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"FAIL","reason_code":"FIXTURE_REGENERATION_FAILED"}')
        return 1
    print(json.dumps(result)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
