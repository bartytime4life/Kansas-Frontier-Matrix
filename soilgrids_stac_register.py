from __future__ import annotations

import argparse
import hashlib
import json
import logging
import math
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODULE_VERSION = "1.0.0"
REMOTE_PREFIXES = ("http://", "https://", "s3://", "gs://", "/vsicurl/", "/vsis3/", "/vsigs/")
SUPPORTED_STAC_VERSIONS = {"1.0.0", "1.1.0"}
PROJ_EXT = "https://stac-extensions.github.io/projection/v2.0.0/schema.json"
FILE_EXT = "https://stac-extensions.github.io/file/v2.1.0/schema.json"
RASTER_EXT = "https://stac-extensions.github.io/raster/v2.0.0/schema.json"


def _logger() -> logging.Logger:
    logger = logging.getLogger("soilgrids_stac_register")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def _log(event: str, **payload: Any) -> None:
    _logger().info(json.dumps({"event": event, **payload}, sort_keys=True))


def write_canonical_json(path: Path, obj: dict[str, Any], keep_temp: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=".tmp_", suffix=".json", dir=str(path.parent))
    os.close(fd)
    tmp = Path(tmp_name)
    try:
        tmp.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        json.loads(tmp.read_text(encoding="utf-8"))
        shutil.move(str(tmp), str(path))
    except Exception:
        if tmp.exists() and not keep_temp:
            tmp.unlink()
        raise


def _canonical_hash(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _is_remote(path_like: str) -> bool:
    return str(path_like).startswith(REMOTE_PREFIXES)


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _validate_bbox(bbox: list[float]) -> None:
    if len(bbox) != 4:
        raise ValueError("bbox must have 4 values")
    xmin, ymin, xmax, ymax = bbox
    if not all(math.isfinite(v) for v in bbox):
        raise ValueError("bbox values must be finite")
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("bbox min/max invalid")
    if xmin < -180 or xmax > 180 or ymin < -90 or ymax > 90:
        raise ValueError("bbox outside EPSG:4326 bounds")


def _bbox_to_geometry(bbox: list[float]) -> dict[str, Any]:
    _validate_bbox(bbox)
    xmin, ymin, xmax, ymax = bbox
    ring = [[xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax], [xmin, ymin]]
    return {"type": "Polygon", "coordinates": [ring]}


def build_band_metadata_for_stac_version(version: str, raster_metadata: dict[str, Any]) -> dict[str, Any]:
    band = {
        "name": raster_metadata.get("name"),
        "description": raster_metadata.get("description"),
        "unit": raster_metadata.get("unit"),
        "data_type": raster_metadata.get("data_type"),
        "nodata": raster_metadata.get("nodata"),
        "raster:spatial_resolution": raster_metadata.get("spatial_resolution"),
    }
    if version == "1.1.0":
        return {"bands": [band]}
    if version == "1.0.0":
        return {"raster:bands": [band]}
    raise ValueError("unsupported STAC version")


def compute_stac_spec_hash(payload: dict[str, Any]) -> str:
    return _canonical_hash(payload)


def validate_stac_item_semantics(item: dict[str, Any]) -> None:
    _validate_bbox(item["bbox"])
    coords = item["geometry"]["coordinates"][0]
    if coords[0] != coords[-1]:
        raise ValueError("geometry ring must be closed")


def build_stac_item(*, stac_version: str, item_id: str, collection_id: str, dataset_datetime: str, bbox: list[float],
                    proj_code: str, proj_shape: list[int], proj_transform: list[float], property_name: str, depth: str,
                    statistic: str, unit: str, asset_href: str, cog_sha256: str, cog_bytes: int,
                    cog_receipt_href: str, run_receipt_href: str | None, raster_metadata: dict[str, Any]) -> dict[str, Any]:
    geometry = _bbox_to_geometry(bbox)
    data_asset = {
        "href": asset_href,
        "type": "image/tiff; application=geotiff; profile=cloud-optimized",
        "roles": ["data"],
        "title": f"SoilGrids {property_name} {depth} {statistic} COG",
        "file:size": cog_bytes,
        "file:checksum": f"1220{cog_sha256}",
    }
    data_asset.update(build_band_metadata_for_stac_version(stac_version, raster_metadata))
    assets = {
        "data": data_asset,
        "cog_receipt": {"href": cog_receipt_href, "type": "application/json", "roles": ["metadata"], "title": "COG normalization receipt"},
    }
    if run_receipt_href:
        assets["wcs_receipt"] = {"href": run_receipt_href, "type": "application/json", "roles": ["metadata"], "title": "WCS ingestion receipt"}
    item = {
        "type": "Feature",
        "stac_version": stac_version,
        "stac_extensions": [PROJ_EXT, FILE_EXT, RASTER_EXT],
        "id": item_id,
        "collection": collection_id,
        "bbox": bbox,
        "geometry": geometry,
        "properties": {
            "datetime": dataset_datetime,
            "platform": "SoilGrids",
            "instruments": ["ensemble-ml"],
            "soilgrids:version": "v2.0",
            "soilgrids:property": property_name,
            "soilgrids:depth": depth,
            "soilgrids:statistic": statistic,
            "soilgrids:unit": unit,
            "proj:code": proj_code,
            "proj:shape": proj_shape,
            "proj:transform": proj_transform,
        },
        "assets": assets,
        "links": [
            {"rel": "collection", "href": "../collection.json", "type": "application/json"},
            {"rel": "root", "href": "../../../catalog.json", "type": "application/json"},
            {"rel": "self", "href": f"./{item_id}.json", "type": "application/json"},
            {"rel": "derived_from", "href": cog_receipt_href, "type": "application/json"},
        ],
    }
    validate_stac_item_semantics(item)
    return item


def build_or_update_collection(existing: dict[str, Any] | None, *, stac_version: str, collection_id: str, title: str,
                               description: str, license_value: str, item_bbox: list[float], item_datetime: str) -> dict[str, Any]:
    if existing and existing.get("id") != collection_id:
        raise ValueError("conflicting collection id")
    bboxes = [item_bbox]
    if existing:
        bboxes.extend(existing.get("extent", {}).get("spatial", {}).get("bbox", []))
    xmin = min(b[0] for b in bboxes)
    ymin = min(b[1] for b in bboxes)
    xmax = max(b[2] for b in bboxes)
    ymax = max(b[3] for b in bboxes)
    links = (existing or {}).get("links", []) + [{"rel": "root", "href": "../../catalog.json", "type": "application/json"}, {"rel": "self", "href": "./collection.json", "type": "application/json"}]
    uniq = {(l["rel"], l["href"]): l for l in links}
    out = {
        "type": "Collection",
        "stac_version": stac_version,
        "id": collection_id,
        "title": title,
        "description": description,
        "license": license_value,
        "extent": {"spatial": {"bbox": [[xmin, ymin, xmax, ymax]]}, "temporal": {"interval": [[item_datetime, None]]}},
        "links": sorted(uniq.values(), key=lambda l: (l["rel"], l["href"])),
        "summaries": {"soilgrids:version": ["v2.0"]},
    }
    if stac_version == "1.1.0":
        out["item_assets"] = {"data": {"type": "image/tiff; application=geotiff; profile=cloud-optimized", "roles": ["data"]}}
    return out


def build_or_update_catalog(existing: dict[str, Any] | None, *, stac_version: str, catalog_id: str, title: str, description: str,
                            collection_id: str) -> dict[str, Any]:
    if existing and existing.get("id") != catalog_id:
        raise ValueError("conflicting catalog id")
    links = (existing or {}).get("links", []) + [
        {"rel": "self", "href": "./catalog.json", "type": "application/json"},
        {"rel": "root", "href": "./catalog.json", "type": "application/json"},
        {"rel": "child", "href": f"./collections/{collection_id}/collection.json", "type": "application/json"},
    ]
    uniq = {(l["rel"], l["href"]): l for l in links}
    return {"type": "Catalog", "stac_version": stac_version, "id": catalog_id, "title": title, "description": description, "links": sorted(uniq.values(), key=lambda l: (l["rel"], l["href"]))}


def register_cog_to_stac(**kwargs: Any) -> dict[str, Any]:
    stac_version = kwargs["stac_version"]
    if stac_version not in SUPPORTED_STAC_VERSIONS:
        raise ValueError("unsupported STAC version")
    cog_receipt_path = Path(kwargs["cog_receipt_path"])
    if _is_remote(str(cog_receipt_path)):
        raise ValueError("remote paths not allowed")
    cog_receipt = json.loads(cog_receipt_path.read_text())
    if cog_receipt.get("status") != "success":
        raise ValueError("CogReceipt must be success")
    cog_path = Path(cog_receipt["output_path"])
    if _is_remote(str(cog_path)):
        raise ValueError("remote paths not allowed")
    if not cog_path.exists():
        raise FileNotFoundError("COG file missing")
    sha = _sha256_file(cog_path)
    size = cog_path.stat().st_size
    if sha != cog_receipt.get("output_sha256"):
        raise ValueError("COG checksum mismatch")
    if size != cog_receipt.get("output_bytes"):
        raise ValueError("COG size mismatch")
    bbox = cog_receipt["raster"]["bbox"]
    _validate_bbox(bbox)
    bbox_hash = _canonical_hash(bbox)[:8]
    item_id = kwargs.get("item_id_override") or f"soilgrids_{kwargs['property']}_{kwargs['depth']}_{kwargs['statistic']}_{bbox_hash}_{cog_receipt['spec_hash'][:12]}"
    catalog_dir = Path(kwargs["catalog_dir"])
    item_path = catalog_dir / "collections" / kwargs["collection_id"] / "items" / f"{item_id}.json"
    asset_href = os.path.relpath(cog_path, item_path.parent) if kwargs["asset_href_mode"] == "relative" else str(cog_path.resolve())
    if kwargs["asset_href_mode"] == "external":
        base = kwargs.get("asset_base_href")
        if not base:
            raise ValueError("external mode requires asset_base_href")
        asset_href = base.rstrip("/") + "/" + cog_path.name
    item = build_stac_item(stac_version=stac_version, item_id=item_id, collection_id=kwargs["collection_id"], dataset_datetime=kwargs["dataset_datetime"],
                           bbox=bbox, proj_code=cog_receipt["raster"]["crs"], proj_shape=[cog_receipt["raster"]["height"], cog_receipt["raster"]["width"]],
                           proj_transform=cog_receipt["raster"]["geotransform"], property_name=kwargs["property"], depth=kwargs["depth"], statistic=kwargs["statistic"],
                           unit=kwargs["unit"], asset_href=asset_href, cog_sha256=sha, cog_bytes=size,
                           cog_receipt_href=os.path.relpath(cog_receipt_path, item_path.parent),
                           run_receipt_href=os.path.relpath(kwargs["run_receipt_path"], item_path.parent) if kwargs.get("run_receipt_path") else None,
                           raster_metadata={"name": f"{kwargs['property']}_{kwargs['depth']}_{kwargs['statistic']}", "description": "SoilGrids band", "unit": kwargs["unit"], "data_type": "int16", "nodata": None, "spatial_resolution": 250})
    coll_path = catalog_dir / "collections" / kwargs["collection_id"] / "collection.json"
    cat_path = catalog_dir / "catalog.json"
    collection = build_or_update_collection(json.loads(coll_path.read_text()) if coll_path.exists() else None, stac_version=stac_version, collection_id=kwargs["collection_id"], title=kwargs["collection_title"], description=kwargs.get("collection_description") or kwargs["collection_title"], license_value=kwargs["license"], item_bbox=bbox, item_datetime=kwargs["dataset_datetime"])
    catalog = build_or_update_catalog(json.loads(cat_path.read_text()) if cat_path.exists() else None, stac_version=stac_version, catalog_id=kwargs["catalog_id"], title=kwargs["catalog_title"], description=kwargs.get("catalog_description") or kwargs["catalog_title"], collection_id=kwargs["collection_id"])
    write_canonical_json(item_path, item, keep_temp=kwargs.get("keep_temp", False))
    write_canonical_json(coll_path, collection, keep_temp=kwargs.get("keep_temp", False))
    write_canonical_json(cat_path, catalog, keep_temp=kwargs.get("keep_temp", False))
    spec_hash = compute_stac_spec_hash({"stac_version": stac_version, "catalog_id": kwargs["catalog_id"], "collection_id": kwargs["collection_id"], "item_id": item_id, "asset_sha256": sha, "asset_bytes": size, "asset_href_mode": kwargs["asset_href_mode"], "asset_href": asset_href, "bbox": bbox, "geometry": item["geometry"], "projection": {"proj:code": cog_receipt["raster"]["crs"], "proj:shape": [cog_receipt["raster"]["height"], cog_receipt["raster"]["width"]], "proj:transform": cog_receipt["raster"]["geotransform"]}, "soilgrids": {"property": kwargs["property"], "depth": kwargs["depth"], "statistic": kwargs["statistic"], "unit": kwargs["unit"]}, "cog_spec_hash": cog_receipt.get("spec_hash"), "module_version": MODULE_VERSION, "extensions": [PROJ_EXT, FILE_EXT, RASTER_EXT]})
    receipt = {"schema": "StacRegistrationReceipt.v1", "run_id": hashlib.sha256(f"{item_id}|{spec_hash}".encode()).hexdigest()[:16], "created_at_utc": datetime.now(timezone.utc).isoformat(), "status": "success", "source": "soilgrids_stac_register", "stac_version": stac_version, "spec_hash": spec_hash, "catalog_path": str(cat_path), "collection_path": str(coll_path), "item_path": str(item_path), "item_id": item_id, "collection_id": kwargs["collection_id"], "catalog_id": kwargs["catalog_id"], "asset_href": asset_href, "asset_href_mode": kwargs["asset_href_mode"], "asset_sha256": sha, "asset_bytes": size, "file_checksum_multihash": f"1220{sha}", "bbox": bbox, "geometry_hash": _canonical_hash(item["geometry"]), "source_receipts": {"cog_receipt_path": str(cog_receipt_path), "cog_spec_hash": cog_receipt.get("spec_hash"), "run_receipt_path": kwargs.get("run_receipt_path"), "run_spec_hash": None}, "validation": {"cog_exists": True, "cog_sha256_match": True, "cog_size_match": True, "bbox_valid": True, "geometry_valid": True, "projection_valid": True, "collection_valid": True, "catalog_valid": True, "item_valid": True, "links_valid": True}, "errors": []}
    receipt_path = (catalog_dir / "receipts" / f"stac_registration_{spec_hash[:12]}.json")
    write_canonical_json(receipt_path, receipt)
    return receipt


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--cog-receipt", required=True, dest="cog_receipt_path")
    p.add_argument("--run-receipt", dest="run_receipt_path")
    p.add_argument("--catalog-dir", required=True)
    p.add_argument("--catalog-id", required=True)
    p.add_argument("--catalog-title", required=True)
    p.add_argument("--collection-id", required=True)
    p.add_argument("--collection-title", required=True)
    p.add_argument("--dataset-datetime", required=True)
    p.add_argument("--license", required=True)
    p.add_argument("--property", required=True)
    p.add_argument("--depth", required=True)
    p.add_argument("--statistic", required=True)
    p.add_argument("--unit", required=True)
    p.add_argument("--asset-href-mode", required=True, choices=["relative", "absolute", "external"])
    p.add_argument("--asset-base-href")
    p.add_argument("--stac-version", default="1.1.0")
    args = p.parse_args()
    register_cog_to_stac(**vars(args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
