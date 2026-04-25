#!/usr/bin/env python3
"""
Tests for pipelines/kansas_biodiversity_etl/catalog/validate_catalog.py.

These tests prove fail-closed catalog validation behavior for:
- valid STAC/DCAT/PROV closure
- missing STAC collection
- missing STAC items
- STAC item spec_hash mismatch
- DCAT spec_hash mismatch
- PROV missing spec_hash
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict


SPEC_HASH = "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validator_path() -> Path:
    return Path(__file__).resolve().parents[1] / "validate_catalog.py"


def build_valid_catalog(root: Path) -> Dict[str, Path]:
    metadata = root / "metadata.json"
    stac_root = root / "stac"
    dcat = root / "dcat.json"
    prov = root / "prov.json"

    write_json(
        metadata,
        {
            "dataset_id": "kfm:kansas_biodiversity_occurrences",
            "spec_hash": SPEC_HASH,
            "records": 2,
            "format": "parquet_partitioned",
        },
    )

    write_json(
        stac_root / "collection.json",
        {
            "type": "Collection",
            "stac_version": "1.0.0",
            "id": "kfm:kansas_biodiversity_occurrences",
            "summaries": {
                "kfm:spec_hash": [SPEC_HASH],
            },
        },
    )

    write_json(
        stac_root / "year=2026-month=04.item.json",
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": "kfm-kansas-biodiversity-occurrences-year=2026-month=04",
            "properties": {
                "kfm:spec_hash": SPEC_HASH,
                "kfm:partition_year": "2026",
                "kfm:partition_month": "04",
            },
            "geometry": None,
            "bbox": None,
        },
    )

    write_json(
        dcat,
        {
            "@type": "dcat:Dataset",
            "@id": "kfm:kansas_biodiversity_occurrences",
            "kfm:spec_hash": SPEC_HASH,
        },
    )

    write_json(
        prov,
        {
            "entity": {
                "dataset": {
                    "prov:type": "kfm:PartitionedParquetDataset",
                    "kfm:spec_hash": SPEC_HASH,
                }
            }
        },
    )

    return {
        "metadata": metadata,
        "stac_root": stac_root,
        "dcat": dcat,
        "prov": prov,
    }


def run_validator(paths: Dict[str, Path]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(validator_path()),
            "--metadata",
            str(paths["metadata"]),
            "--stac-root",
            str(paths["stac_root"]),
            "--dcat",
            str(paths["dcat"]),
            "--prov",
            str(paths["prov"]),
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def parse_stdout(result: subprocess.CompletedProcess[str]) -> Dict[str, Any]:
    assert result.stdout.strip(), result.stderr
    return json.loads(result.stdout)


def test_valid_catalog_passes(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 0
    assert payload["decision"] == "PASS"
    assert payload["spec_hash"] == SPEC_HASH
    assert payload["stac_items"] == 1


def test_missing_collection_fails(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)
    (paths["stac_root"] / "collection.json").unlink()

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 1
    assert payload == {
        "decision": "FAIL",
        "reason": "stac_collection_missing",
    }


def test_no_stac_items_fails(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)

    for item in paths["stac_root"].glob("*.item.json"):
        item.unlink()

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 1
    assert payload == {
        "decision": "FAIL",
        "reason": "no_stac_items_found",
    }


def test_stac_item_hash_mismatch_fails(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)
    item_path = paths["stac_root"] / "year=2026-month=04.item.json"

    item = json.loads(item_path.read_text(encoding="utf-8"))
    item["properties"]["kfm:spec_hash"] = "sha256:bad"
    write_json(item_path, item)

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 1
    assert payload == {
        "decision": "FAIL",
        "reason": "stac_item_spec_hash_mismatch:year=2026-month=04.item.json",
    }


def test_dcat_hash_mismatch_fails(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)

    dcat = json.loads(paths["dcat"].read_text(encoding="utf-8"))
    dcat["kfm:spec_hash"] = "sha256:bad"
    write_json(paths["dcat"], dcat)

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 1
    assert payload == {
        "decision": "FAIL",
        "reason": "dcat_spec_hash_mismatch",
    }


def test_prov_missing_spec_hash_fails(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)

    prov = json.loads(paths["prov"].read_text(encoding="utf-8"))
    del prov["entity"]["dataset"]["kfm:spec_hash"]
    write_json(paths["prov"], prov)

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 1
    assert payload == {
        "decision": "FAIL",
        "reason": "prov_missing_spec_hash",
    }


def test_stac_root_missing_fails(tmp_path: Path) -> None:
    paths = build_valid_catalog(tmp_path)
    shutil.rmtree(paths["stac_root"])

    result = run_validator(paths)
    payload = parse_stdout(result)

    assert result.returncode == 1
    assert payload == {
        "decision": "FAIL",
        "reason": "stac_root_missing",
    }
