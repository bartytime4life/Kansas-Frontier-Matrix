from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.flora.usda_plants_dataset_validator import validate_dataset

SOURCE_URI = "https://plants.sc.egov.usda.gov/downloads"


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _spec_hash_for_dataset(dataset: dict[str, Any]) -> str:
    base = deepcopy(dataset)
    base.pop("spec_hash", None)
    props = base.get("properties")
    if isinstance(props, dict):
        props.pop("kfm:spec_hash", None)
    digest = hashlib.sha256(_canonical_json_bytes(base)).hexdigest()
    return f"sha256:{digest}"


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _split_growth_habit(raw: str) -> list[str]:
    if not raw:
        return []
    return [part.strip() for part in raw.replace(";", "|").split("|") if part.strip()]


def load_usda_plants_fixtures(checklist: Path, states: Path, counties: Path, snapshot_date: str, out_dir: Path) -> dict[str, Path]:
    with checklist.open("r", encoding="utf-8", newline="") as f:
        checklist_rows = list(csv.DictReader(f))
    with states.open("r", encoding="utf-8", newline="") as f:
        state_rows = list(csv.DictReader(f))
    with counties.open("r", encoding="utf-8", newline="") as f:
        county_rows = list(csv.DictReader(f))

    state_by_symbol: dict[str, list[dict[str, str]]] = {}
    for row in state_rows:
        state_by_symbol.setdefault(row["symbol"].strip(), []).append({"state": row["state"].strip(), "presence": row["presence"].strip()})

    county_by_symbol: dict[str, list[dict[str, Any]]] = {}
    for row in county_rows:
        county_by_symbol.setdefault(row["symbol"].strip(), []).append(
            {"fips": row["fips"].strip(), "presence": row["presence"].strip(), "first_observed": None}
        )

    processed_dir = out_dir / "processed/flora/usda_plants"
    receipt_dir = out_dir / "receipts/flora/usda_plants"
    proof_dir = out_dir / "proofs/flora/usda_plants"
    processed_dir.mkdir(parents=True, exist_ok=True)
    receipt_dir.mkdir(parents=True, exist_ok=True)
    proof_dir.mkdir(parents=True, exist_ok=True)

    output_refs: list[str] = []
    validation_results: list[dict[str, Any]] = []
    dataset_paths: list[Path] = []

    for row in sorted(checklist_rows, key=lambda r: r["symbol"].strip()):
        symbol = row["symbol"].strip()
        dataset: dict[str, Any] = {
            "schema_version": "1.0.0",
            "object_type": "usda_plants_dataset",
            "id": f"kfm.dataset.flora.usda_plants.{symbol}",
            "domain": "flora",
            "spec_hash": "",
            "source": {
                "source_id": "usda_plants",
                "source_type": "usda_plants_bulk",
                "source_name": "USDA PLANTS Database",
                "source_descriptor_ref": "data/registry/flora/sources.yaml#usda_plants",
                "source_uri": SOURCE_URI,
            },
            "properties": {
                "plants:symbol": symbol,
                "scientificName": row["scientificName"].strip(),
                "nationalCommonName": row["nationalCommonName"].strip(),
                "family": row["family"].strip(),
                "nativeStatus": row["nativeStatus"].strip(),
                "growthHabit": _split_growth_habit(row["growthHabit"].strip()),
                "wetlandStatus": row["wetlandStatus"].strip(),
                "license": "USDA / U.S. Public Domain",
                "rightsHolder": "United States Department of Agriculture",
                "datasetID": "USDA_PLANTS",
                "policy_label": "public",
                "kfm:spec_hash": "",
            },
            "distributions": {
                "state": sorted(state_by_symbol.get(symbol, []), key=lambda i: i["state"]),
                "county": sorted(county_by_symbol.get(symbol, []), key=lambda i: i["fips"]),
            },
            "provenance": {
                "source_uri": SOURCE_URI,
                "snapshot_date": snapshot_date,
                "raw_refs": [str(checklist), str(states), str(counties)],
                "receipt_refs": [
                    "receipts/flora/usda_plants/ingest_receipt.json",
                    "receipts/flora/usda_plants/validation_receipt.json",
                ],
            },
            "validation": {
                "validator_id": "usda_plants_dataset_validator@v1",
                "result": "pass",
                "reason_codes": [],
            },
        }
        spec_hash = _spec_hash_for_dataset(dataset)
        dataset["spec_hash"] = spec_hash
        dataset["properties"]["kfm:spec_hash"] = spec_hash

        path = processed_dir / f"{symbol}.json"
        _write_json(path, dataset)
        dataset_paths.append(path)
        output_refs.append(str(path.relative_to(out_dir)))

        result = validate_dataset(dataset)
        validation_results.append({"path": str(path.relative_to(out_dir)), "result": result["result"], "reason_codes": result["reason_codes"]})

    pass_count = sum(1 for r in validation_results if r["result"] == "pass")
    fail_count = len(validation_results) - pass_count

    ingest_receipt = {
        "schema_version": "1.0.0",
        "object_type": "usda_plants_ingest_receipt",
        "receipt_id": "kfm.receipt.flora.usda_plants.ingest.v1",
        "generated_at": _utc_now_iso(),
        "snapshot_date": snapshot_date,
        "source_id": "usda_plants",
        "source_uri": SOURCE_URI,
        "input_refs": [str(checklist), str(states), str(counties)],
        "output_refs": sorted(output_refs),
        "record_counts": {
            "checklist_rows": len(checklist_rows),
            "state_distribution_rows": len(state_rows),
            "county_distribution_rows": len(county_rows),
            "emitted_datasets": len(output_refs),
        },
        "status": "pass" if fail_count == 0 else "fail",
        "reason_codes": [] if fail_count == 0 else ["VALIDATION_FAILED"],
    }

    validation_receipt = {
        "schema_version": "1.0.0",
        "object_type": "usda_plants_validation_receipt",
        "receipt_id": "kfm.receipt.flora.usda_plants.validation.v1",
        "generated_at": _utc_now_iso(),
        "validator_id": "usda_plants_dataset_validator@v1",
        "validated_refs": sorted(output_refs),
        "results": sorted(validation_results, key=lambda i: i["path"]),
        "summary": {"pass_count": pass_count, "fail_count": fail_count},
        "status": "pass" if fail_count == 0 else "fail",
    }

    _write_json(receipt_dir / "ingest_receipt.json", ingest_receipt)
    _write_json(receipt_dir / "validation_receipt.json", validation_receipt)

    return {
        "processed_dir": processed_dir,
        "ingest_receipt": receipt_dir / "ingest_receipt.json",
        "validation_receipt": receipt_dir / "validation_receipt.json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Load USDA PLANTS fixture CSVs into deterministic dataset JSON artifacts")
    parser.add_argument("--checklist", required=True, type=Path)
    parser.add_argument("--states", required=True, type=Path)
    parser.add_argument("--counties", required=True, type=Path)
    parser.add_argument("--snapshot-date", required=True)
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()
    load_usda_plants_fixtures(args.checklist, args.states, args.counties, args.snapshot_date, args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
