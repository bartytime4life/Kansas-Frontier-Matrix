# src/kansas_geo_timeline/ingest/stac_writer.py
from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path
from typing import Dict, Optional

from .provenance import Provenance


_SLUG_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def _safe_id(s: str) -> str:
    """Conservative STAC item id sanitizer."""
    s = s.strip()
    s = _SLUG_RE.sub("-", s)
    return s.strip("-") or "item"


def _norm_datetime(properties: dict) -> str:
    """Normalize to RFC3339 UTC ('Z') if present, else now."""
    dt = properties.get("datetime")
    if isinstance(dt, str) and dt:
        # Light normalization; trust user string if it already contains 'Z' or offset
        if dt.endswith("Z") or ("+" in dt and ":" in dt.split("+", 1)[-1]):
            return dt
    return Provenance.now_iso()


def _ensure_bbox_geom(bbox: Optional[list[float]], geometry: Optional[dict]) -> tuple[Optional[list[float]], Optional[dict]]:
    """If missing bbox but geometry provided (or vice versa), use the other.
    For simplicity, we only ensure bbox from geometry when polygon provided.
    """
    if bbox and geometry:
        return bbox, geometry
    if geometry and geometry.get("type") == "Polygon":
        try:
            coords = geometry["coordinates"][0]
            xs = [c[0] for c in coords]
            ys = [c[1] for c in coords]
            return [min(xs), min(ys), max(xs), max(ys)], geometry
        except Exception:
            pass
    # If only bbox is present, keep geometry None — valid STAC.
    return bbox, geometry


class StacWriter:
    """Tiny STAC item emitter (JSON dict) with checksums, roles, and atomic writes."""

    @staticmethod
    def mk_item(
        id_: str,
        source_path: Path,
        out_path: Path,
        bbox: Optional[list[float]],
        geometry: Optional[dict],
        properties: dict,
        asset_media_type: str,
        collection: Optional[str] = None,
        roles: Optional[list[str]] = None,
        add_checksum: bool = True,
    ) -> Dict:
        # Normalize inputs
        item_id = _safe_id(id_)
        props = {**properties}
        props["datetime"] = _norm_datetime(properties)

        bbox, geometry = _ensure_bbox_geom(bbox, geometry)

        # Compute checksum & file stats for asset
        checksum = Provenance.sha256_file(out_path) if add_checksum else None
        stats = Provenance.file_stats(out_path)

        # Media-type fallback (be defensive)
        media_type = asset_media_type or Provenance.inferred_media_type(out_path)

        assets: Dict[str, Dict] = {
            "data": {
                **Provenance.basic_asset(out_path, media_type),
                "roles": roles or ["data"],
                "file:size": stats["size"],
            }
        }
        if checksum:
            # STAC Checksum Extension (common pattern)
            assets["data"]["checksum:sha256"] = checksum

        # include a 'source' asset for traceability
        assets["source"] = {
            **Provenance.basic_asset(source_path, "application/octet-stream"),
            "roles": ["source"],
        }

        item: Dict = {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": item_id,
            "bbox": bbox,
            "geometry": geometry,
            "properties": props,
            "assets": assets,
        }

        # Lightweight links: self + optional collection (caller can post-process catalogs)
        links = []
        # 'self' link will be completed in write_item when we know the actual filename
        if collection:
            item["collection"] = collection
            links.append({"rel": "collection", "href": f"../collections/{collection}.json"})
        if links:
            item["links"] = links

        return item

    @staticmethod
    def write_item(item: Dict, out_dir: Path, filename: Optional[str] = None) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        # If the caller passed a filename, trust it; else use `<id>.json`.
        name = filename or f"{item['id']}.json"
        path = (out_dir / name)

        # Add/refresh 'self' link relative to the items directory
        href_self = path.name
        # Ensure links field exists
        links = item.get("links", [])
        # Remove any prior 'self'
        links = [lnk for lnk in links if lnk.get("rel") != "self"]
        links.append({"rel": "self", "href": href_self})
        item["links"] = links

        # Atomic write
        payload = json.dumps(item, ensure_ascii=False, indent=2)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=out_dir) as tmp:
            tmp.write(payload)
            tmp_path = Path(tmp.name)
        os.replace(tmp_path, path)

        return path
