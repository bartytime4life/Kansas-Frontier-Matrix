"""Read-only review of a device-local, unadmitted curation package."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from tools.local_data import review_curation


BUNDLE = "kfm-store-reconciliation-20260925"
PRISM = "kfm-prism-review-20260925T140241Z"
IDS = [
    "kdot_county_future_functional_class_candidates",
    "kdot_urban_future_functional_class_candidates",
    "kdot_bridge_label_search_anchors",
    "historic_map_sheet_geometry_review",
    "prism_completed_grid_review",
]


def write_json(root: Path, relative: str, value: dict) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def checksums(root: Path) -> None:
    entries = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != "checksums.sha256":
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            entries.append(f"{digest}  {path.relative_to(root).as_posix()}")
    (root / "checksums.sha256").write_text("\n".join(entries) + "\n", encoding="utf-8")


@pytest.fixture
def package(tmp_path: Path) -> tuple[Path, Path, Path]:
    root = tmp_path / "KFM-data"
    processed = root / "data/processed"
    bundle = processed / BUNDLE
    prism = processed / PRISM
    bundle.mkdir(parents=True)
    prism.mkdir(parents=True)
    for relative in ["maps/county.geojson.gz", "maps/urban.geojson.gz",
                     "maps/bridge.geojson", "maps/georef.csv"]:
        path = bundle / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"candidate")
    (prism / "grid_catalog.csv.gz").write_bytes(b"model snapshot")
    write_json(bundle, "validation.json", {
        "passed": True,
        "source_inventory": {"passed": True, "all_collections_accounted": True,
                             "all_nonmutable_files_hashed": True,
                             "all_prior_maps_present": True,
                             "source_files": 20},
        "county_clipped_fragments": 10, "urban_vector_lines": 20,
    })
    write_json(bundle, "inventory/summary.json", {
        "files": 20, "collections": {name: {} for name in review_curation.COLLECTIONS},
        "completed_utc": "2026-09-25T14:21:45Z",
    })
    write_json(bundle, "maps/georeference_review.json", {"map_sheets": 5})
    write_json(bundle, "cleanup_plan.json", {
        "source_deletions_in_this_run": 0, "approved_for_deletion": [],
    })
    artifacts = ["maps/county.geojson.gz", "maps/urban.geojson.gz",
                 "maps/bridge.geojson", "maps/georef.csv", f"../{PRISM}/grid_catalog.csv.gz"]
    write_json(bundle, "layers/layer_manifest.json", {
        "schema": review_curation.SCHEMA,
        "layers": [{"id": identity, "artifact": artifact,
                    "domain": "roads_rail_trade", "geometry": "LineString",
                    "time_mode": "sheet_edition", "claim_limit": "Review only",
                    "status": "review_queue" if identity == IDS[3] else "local_unadmitted_candidate"}
                   for identity, artifact in zip(IDS, artifacts)],
    })
    checksums(bundle)
    checksums(prism)
    return root, bundle, prism


def test_verified_candidate_package_is_only_a_local_review(package) -> None:
    root, _, _ = package
    before = {str(path): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    report = review_curation.inspect(root, BUNDLE)
    after = {str(path): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    assert report["status"] == "LOCAL_CANDIDATE_REVIEW"
    assert report["source_files_at_snapshot"] == 20
    assert {layer["id"] for layer in report["layers"]} == set(IDS)
    assert before == after


def test_changed_candidate_bytes_hold(package) -> None:
    root, bundle, _ = package
    (bundle / "maps/county.geojson.gz").write_bytes(b"changed")
    with pytest.raises(review_curation.Held, match="CHECKSUM_MISMATCH"):
        review_curation.inspect(root, BUNDLE)


def test_changed_linked_prism_bytes_hold(package) -> None:
    root, _, prism = package
    (prism / "grid_catalog.csv.gz").write_bytes(b"changed")
    with pytest.raises(review_curation.Held, match="CHECKSUM_MISMATCH"):
        review_curation.inspect(root, BUNDLE)


def test_admitted_claim_and_deletion_claim_hold(package) -> None:
    root, bundle, _ = package
    manifest_path = bundle / "layers/layer_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["layers"][0]["status"] = "admitted"
    write_json(bundle, "layers/layer_manifest.json", manifest)
    checksums(bundle)
    with pytest.raises(review_curation.Held, match="INVALID_LAYER_STATUS"):
        review_curation.inspect(root, BUNDLE)
    manifest["layers"][0]["status"] = "local_unadmitted_candidate"
    write_json(bundle, "layers/layer_manifest.json", manifest)
    write_json(bundle, "cleanup_plan.json", {
        "source_deletions_in_this_run": 1, "approved_for_deletion": ["raw/map.pdf"],
    })
    checksums(bundle)
    with pytest.raises(review_curation.Held, match="UNREVIEWED_SOURCE_DELETION"):
        review_curation.inspect(root, BUNDLE)


def test_artifact_cannot_escape_processed_root(package, tmp_path: Path) -> None:
    root, bundle, _ = package
    outside = tmp_path / "outside.geojson"
    outside.write_bytes(b"unrelated")
    manifest_path = bundle / "layers/layer_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["layers"][0]["artifact"] = "../../../../outside.geojson"
    write_json(bundle, "layers/layer_manifest.json", manifest)
    checksums(bundle)
    with pytest.raises(review_curation.Held, match="UNSAFE_ARTIFACT_PATH"):
        review_curation.inspect(root, BUNDLE)
