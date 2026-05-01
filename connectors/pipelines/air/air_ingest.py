#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def deterministic_example():
    return {
        "aggregation": {"averaging_window": "nowcast_hourly", "parameter": "pm25", "units": "ug_m3"},
        "aqs_flags_summary": {"hard_denial_rows_in_baseline": 0},
        "decision": "candidate",
        "flags": {
            "evidence_bundle_ref": "data/processed/air/evidence_bundle.example.json",
            "run_receipt_ref": "data/receipts/air/run_receipt.example.json",
        },
        "metrics": {"nowcast_max": 21.0, "nowcast_vs_baseline_sigma": 1.5, "station_coverage_pct": 82.0},
        "schema_version": "v1",
        "source": {"dataset": "no_network_stub", "provider": "kfm_air_pipeline"},
        "time_window": {"end": "2026-05-01T01:00:00Z", "start": "2026-05-01T00:00:00Z"},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", help="Optional QA summary fixture JSON path")
    args = parser.parse_args()

    out_summary = Path("data/processed/air/qa_summary.example.json")
    out_receipt = Path("data/receipts/air/run_receipt.example.json")
    out_summary.parent.mkdir(parents=True, exist_ok=True)
    out_receipt.parent.mkdir(parents=True, exist_ok=True)

    if args.fixture:
        payload = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    else:
        payload = deterministic_example()

    receipt = {
        "schema_version": "v1",
        "run_id": "air-ingest-no-network-2026-05-01T01:00:00Z",
        "pipeline": "connectors/pipelines/air/air_ingest.py",
        "network_access": "disabled",
        "outputs": [str(out_summary)],
        "status": "completed",
    }

    out_summary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    out_receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"WROTE {out_summary}")
    print(f"WROTE {out_receipt}")


if __name__ == "__main__":
    main()
