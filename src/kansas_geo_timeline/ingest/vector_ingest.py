# src/kansas_geo_timeline/ingest/vector_ingest.py
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Dict, Tuple, Optional, Iterable

import fiona
from fiona.errors import DriverError
from fiona.transform import transform_geom

from .base import BaseIngestor, IngestError
from .provenance import Provenance
from .stac_writer import StacWriter


def _split_path_layer(path_or_layer: str | Path, explicit_layer: Optional[str]) -> tuple[Path, Optional[str]]:
    """Support 'path.gpkg:layer' shorthand; explicit layer overrides shorthand."""
    p = Path(str(path_or_layer))
    if explicit_layer:
        return p, explicit_layer
    # Only parse if string contains ':', avoid Windows drive letters by checking suffix
    s = str(path_or_layer)
    if ":" in s and Path(s.split(":", 1)[0]).exists():
        ds, lyr = s.split(":", 1)
        return Path(ds), (lyr or None)
    return p, None


def _iter_feature_bboxes(features: Iterable[dict]) -> Iterable[tuple[float, float, float, float]]:
    """Yield per-feature bbox (minx, miny, maxx, maxy). Uses Shapely if present, else quick manual bbox for Points/Lines/Polygons."""
    try:
        from shapely.geometry import shape  # type: ignore
        use_shapely = True
    except Exception:
        use_shapely = False

    def _bbox_coords(coords):
        xs, ys = [], []
        stack = [coords]
        while stack:
            c = stack.pop()
            if isinstance(c, (list, tuple)) and c and isinstance(c[0], (list, tuple)):
                # nested
                for item in c:
                    stack.append(item)
            else:
                # assume coordinate pair
                try:
                    x, y = c[:2]
                    xs.append(float(x)); ys.append(float(y))
                except Exception:
                    pass
        if xs and ys:
            return (min(xs), min(ys), max(xs), max(ys))
        return None

    for ft in features:
        geom = ft.get("geometry")
        if not geom:
            continue
        if use_shapely:
            try:
                g = shape(geom)
                if not g.is_empty:
                    minx, miny, maxx, maxy = g.bounds
                    yield (minx, miny, maxx, maxy)
                    continue
            except Exception:
                pass
        # Fallback manual bbox
        try:
            typ = geom.get("type")
            coords = geom.get("coordinates")
            if typ in {"Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"} and coords is not None:
                bb = _bbox_coords(coords)
                if bb:
                    yield bb
        except Exception:
            continue


def _union_bbox(bboxes: Iterable[tuple[float, float, float, float]]) -> Optional[list[float]]:
    minx = miny = float("inf")
    maxx = maxy = float("-inf")
    found = False
    for (l, b, r, t) in bboxes:
        found = True
        minx = min(minx, l)
        miny = min(miny, b)
        maxx = max(maxx, r)
        maxy = max(maxy, t)
    if not found:
        return None
    return [minx, miny, maxx, maxy]


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
        self.indent = int(indent)
        self.layer = layer
        self.stac_collection = stac_collection
        self.stac_items_dir = Path(stac_items_dir)

    # ------------------------- internals -------------------------

    def _default_out_dir(self) -> Path:
        return Path("data/processed").resolve()

    def _target_path(self) -> Path:
        name = self.src_path.stem + ".json"
        return (self.out_dir / name).resolve()

    def _open_src(self) -> fiona.Collection:
        ds_path, lyr = _split_path_layer(self.src_path, self.layer)
        try:
            col = fiona.open(ds_path, layer=lyr) if lyr else fiona.open(ds_path)
        except DriverError as e:
            raise IngestError(str(e)) from e
        if lyr and col.name != lyr:
            # If Fiona resolved a different layer, error out to avoid silent mistakes
            raise IngestError(f"Requested layer '{lyr}' not found in {ds_path}. Found: {col.name}")
        return col

    # --------------------------- main API --------------------------

    def run(self) -> Tuple[Path, Dict]:
        out_path = self._target_path()
        out_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with self._open_src() as src:
                src_crs = src.crs_wkt or src.crs
                if not src_crs:
                    raise IngestError(f"Vector has no CRS: {self.src_path}")

                features: list[dict] = []
                # Transform → dst crs, collect feature bboxes
                for feat in src:
                    geom = feat.get("geometry")
                    if geom:
                        try:
                            geom = transform_geom(src_crs, self.dst_crs, geom, antimeridian_cutting=True, precision=9)
                        except Exception as e:
                            # Skip broken geometry but keep ingest robust
                            self.logger.warning("Geometry transform failed (skipping feature): %s", e)
                            geom = None
                    feat["geometry"] = geom
                    features.append(feat)

                # Compute union bbox on transformed features
                bbox = _union_bbox(_iter_feature_bboxes(features))

                # Atomic write GeoJSON
                fc = {"type": "FeatureCollection", "name": self.src_path.stem, "features": features}
                payload = json.dumps(fc, ensure_ascii=False, indent=self.indent)
                with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=out_path.parent) as tmp:
                    tmp.write(payload)
                    tmp_path = Path(tmp.name)
                os.replace(tmp_path, out_path)

        except IngestError:
            raise
        except Exception as e:
            raise IngestError(f"Vector ingest failed for {self.src_path}: {e}") from e

        # Hash & sidecar
        digest = Provenance.digest_and_sidecar(out_path)

        # STAC geometry polygon from bbox (optional but nice)
        geometry = None
        if bbox:
            l, b, r, t = bbox
            geometry = {"type": "Polygon", "coordinates": [[[l, b], [r, b], [r, t], [l, t], [l, b]]]}

        # Properties
        props = {
            "kfm:ingest": "vector",
            "kfm:sha256": digest,
            "kfm:src": self.relpath(self.src_path),
            "file:meta": Provenance.file_stats(out_path),
            "proj:epsg": int(self.dst_crs.split(":")[1]) if ":" in self.dst_crs else None,
            "feature:count": len(fc["features"]),
        }
        extra = self.extra_properties() or {}
        props.update(extra)

        media_type = Provenance.inferred_media_type(out_path) or "application/geo+json"

        item = StacWriter.mk_item(
            id_=out_path.stem,
            source_path=self.src_path,
            out_path=out_path,
            bbox=bbox if bbox else None,
            geometry=geometry,
            properties=props,
            asset_media_type=media_type,
            collection=self.stac_collection,
        )
        StacWriter.write_item(item, self.stac_items_dir)

        return out_path, item
