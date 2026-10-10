#!/usr/bin/env python3
"""Prepare/inspect an immutable water snapshot; no activation or review writes."""
from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors_core.captured_json import canonical_bytes, decode_object
from pipelines.domains.hydrology.admission import load_admission
from pipelines.domains.hydrology.package import prepare_water_package
from release.core import DIGEST, validate_snapshot
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, store_lock
from tools.local_data.water_pilot import immutable


def prepare(root: Path, candidate_id: str, *, rollback_target=None, admitted_source=False) -> dict:
    if not DIGEST.fullmatch(candidate_id):
        raise ValueError("INVALID_CANDIDATE_ID")
    candidate = decode_object(read_regular(root / "data/work/hydrology/usgs-nwis" / candidate_id.split(":")[1] / "candidate.json", 8*1024*1024), limit=8*1024*1024)
    if candidate.get("candidate_id") != candidate_id:
        raise ValueError("CANDIDATE_PATH_ID_MISMATCH")
    admission = load_admission() if admitted_source else None
    package = prepare_water_package(candidate, rollback_target=rollback_target, admission=admission)
    raw = canonical_bytes(package)
    manifest, _ = validate_snapshot(raw)
    with store_lock(root):
        immutable(root / "release/candidates/hydrology" / manifest["package_id"].split(":")[1] / "snapshot.json", raw)
    return {"profile": "kfm.water-package-preparation/v1", "package_id": manifest["package_id"], "candidate_id": candidate_id,
            "outcome": "PREPARED", "reason_code": "RELEASE_DECISION_REQUIRED" if admission else "REVIEW_REQUIRED",
            "admitted_source": admission["source_ref"] if admission else None, "activated": False, "published": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--rollback-target")
    parser.add_argument("--admitted-source", action="store_true",
                        help="carry the admitted license and public sensitivity from data/registry/sources/hydrology/usgs_nwis.yaml")
    args = parser.parse_args(argv)
    try:
        result = prepare(external_root(args.root), args.candidate_id, rollback_target=args.rollback_target,
                         admitted_source=args.admitted_source)
    except (ValueError, OSError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"PACKAGE_PREPARATION_FAILED"}')
        return 1
    print(canonical_bytes(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
