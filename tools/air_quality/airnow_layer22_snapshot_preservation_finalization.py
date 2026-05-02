"""CLI runner for AirNow Layer 22 snapshot preservation finalization."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from kfm.air_quality.airnow.snapshot_preservation_finalization.run_snapshot_preservation_finalization import (
    run_snapshot_preservation_finalization,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--created-at", required=True)
    args = parser.parse_args()

    receipt = run_snapshot_preservation_finalization(
        args.manifest,
        args.out_dir,
        args.created_at,
    )
    print(json.dumps(receipt, indent=2, sort_keys=True))
    is_pass = receipt.get("validation_outcome") == "PASS" and receipt.get("finite_outcome") == "ANSWER"
    return 0 if is_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
