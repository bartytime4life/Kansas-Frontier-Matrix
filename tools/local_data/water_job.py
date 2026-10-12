#!/usr/bin/env python3
"""One bounded hourly acquisition and candidate preparation; no serving-store writes."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors.usgs.water_data.pilot_capture import capture
from connectors_core.captured_json import canonical_bytes
from tools.local_data.manage import external_root, init_store
from tools.local_data.water_pilot import stage
from tools.release.water_snapshot import prepare


def run(root, *, now=None, acquire=capture):
    root = external_root(str(root))
    current = datetime.now(timezone.utc) if now is None else now
    if not isinstance(current, datetime) or current.tzinfo is None or current.utcoffset() is None:
        raise ValueError("WATER_JOB_NOW_NOT_TIMEZONE_AWARE")
    end = current.astimezone(timezone.utc).replace(minute=0, second=0, microsecond=0)
    init_store(root)
    stamp = lambda t: t.strftime("%Y-%m-%dT%H:%M:%SZ")
    receipt = stage(root, acquire(stamp(end - timedelta(hours=24)), stamp(end)))
    if receipt["outcome"] != "CANDIDATE_READY":
        return receipt
    return {**receipt, "package": prepare(root, receipt["candidate_id"]), "authority": "CANDIDATE_ONLY"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    args = parser.parse_args(argv)
    try:
        result = run(args.root)
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"WATER_JOB_FAILED","authority":"CANDIDATE_ONLY"}')
        return 1
    print(canonical_bytes(result).decode())
    return 0 if result["outcome"] == "CANDIDATE_READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
