from __future__ import annotations
from pathlib import Path
from typing import Dict, Tuple, Optional

import json
import fiona
from fiona.transform import transform_geom

from .base import BaseIngestor, IngestError
from .provenance import Provenance
from .stac_writer import StacWriter


class VectorIngestor(BaseIngestor):
    """Vector → GeoJSON (EPSG:4326), with SHA256 + STAC dict."""

    def __init__(
        self,
        src_path: str | Path,
        out_dir: str | Path | None = "data/processed",
        dst_crs: str = "EPSG:4326",
        indent: int = 2,
        stac_collection: Optional[str] = None,
        stac_items_dir: str | Path = "stac/items",
        layer: Optional[str] = None,  # for GPKG: "path.gpkg:layer_name" alternative
    ):
        super().__init__(src_path, out_dir, dst_crs)
        self.indent = indent
        self.layer = layer
        self.stac_collection = stac_collection
        self.stac_items_dir = Path(stac_items_dir)

    def _default_out_dir(self) -> Path:
        return Path("data/processed")

    def _target_path(self) -> Path:
        name = self.src_path.stem + ".json"
        return self.out_dir / name

    def _open_src(self):
        if self.layer:
            return fiona.open(self.src_path, layer=self.layer)
        return fiona.open(self.src_path)

    def run(self) -> Tuple[Path, Dict]:
        out_path = self._target_path()
        out_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with self._open_src() as src:
                src_crs = src.crs_wkt or src.crs
                if not src_crs:
                    raise IngestError(f"Vector has no CRS: {self.src_path}")

                features = []
                bbox_union = None

                for feat in src:
                    geom = feat.get("geometry")
                    if geom:
                        geom = transform_geom(src_crs, self.dst_crs, geom, antimeridian_cutting=True, precision=9)
                    feat["geometry"] = geom
                    features.append(feat)

                    # BBox union (simple per-feature bbox)
                    if geom and "coordinates" in geom:
                        try:
                            from shapely.geometry import shape
                            from shapely.ops import unary_union
                            # For speed, approximate bbox union using per-geom bounds
                            g = shape(geom)
                            if bbox_union is None:
                                bbox_union = g.bounds
                            else:
                                l, b, r, t = bbox_union
                                l2, b2, r2, t2 = g.bounds
                                bbox_union = [min(l, l2), min(b, b2), max(r, r2), max(t, t2)]
                        except Exception:
                            pass

                collection = {
                    "type": "FeatureCollection",
                    "name": self.src_path.stem,
                    "features": features,
                }
                out_path.write_text(json.dumps(collection, ensure_ascii=False, indent=self.indent), encoding="utf-8")

        except fiona.errors.DriverError as e:
            raise IngestError(str(e)) from e

        digest = Provenance.sha256_file(out_path)
        Provenance.write_sha256_sidecar(out_path, digest)

        bbox = bbox_union
        geometry = None
        if bbox:
            l, b, r, t = bbox
            geometry = {
                "type": "Polygon",
                "coordinates": [[[l, b], [r, b], [r, t], [l, t], [l, b]]],
            }

        props = {
            "kfm:ingest": "vector",
            "kfm:sha256": digest,
            "kfm:src": str(self.src_path.as_posix()),
            "proj:epsg": int(self.dst_crs.split(":")[1]) if ":" in self.dst_crs else None,
            "feature:count": len(collection["features"]),
        }
        extra = self.extra_properties() or {}
        props.update(extra)

        item = StacWriter.mk_item(
            id_=out_path.stem,
            source_path=self.src_path,
            out_path=out_path,
            bbox=bbox if bbox else None,
            geometry=geometry,
            properties=props,
            asset_media_type="application/geo+json",
            collection=self.stac_collection,
        )
        StacWriter.write_item(item, self.stac_items_dir)

        return out_path, item
