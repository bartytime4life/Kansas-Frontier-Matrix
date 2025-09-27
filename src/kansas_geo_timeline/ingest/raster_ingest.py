# src/kansas_geo_timeline/ingest/raster_ingest.py
from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, Tuple, Optional

import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject
from rio_cogeo.cogeo import cog_translate
from rio_cogeo.profiles import cog_profiles

from .base import BaseIngestor, IngestError
from .provenance import Provenance
from .stac_writer import StacWriter


class RasterIngestor(BaseIngestor):
    """Raster → COG, EPSG:4326 by default, with SHA256 + STAC dict."""

    def __init__(
        self,
        src_path: str | Path,
        out_dir: str | Path | None = "data/processed",
        dst_crs: str = "EPSG:4326",
        profile: str = "deflate",                  # or "webp"
        overview_level: Optional[int] = None,      # auto if None
        resampling: str = "bilinear",              # matches rasterio.enums.Resampling names
        nodata: Optional[float] = None,
        stac_collection: Optional[str] = None,
        stac_items_dir: str | Path = "stac/items",
    ):
        super().__init__(src_path, out_dir, dst_crs)
        self.profile = profile
        self.overview_level = overview_level
        self.resampling = resampling
        self.nodata = nodata
        self.stac_collection = stac_collection
        self.stac_items_dir = Path(stac_items_dir)

        if self.profile not in cog_profiles:
            raise IngestError(f"Unknown COG profile '{self.profile}'. Options: {', '.join(sorted(cog_profiles.keys()))}")

        try:
            # Validate resampling up-front (raises KeyError if invalid)
            _ = Resampling[self.resampling]
        except KeyError as e:
            raise IngestError(f"Unknown resampling '{self.resampling}'.") from e

    # ------------------------- internals -------------------------

    def _default_out_dir(self) -> Path:
        return Path("data/processed").resolve()

    def _target_path(self) -> Path:
        """Derive output COG path. Keep filename, force .tif extension."""
        name = self.src_path.stem + ".tif"
        # Heuristic: tuck DEMs into data/processed/dem/
        sub = "dem" if "dem" in self.src_path.as_posix().lower() else ""
        return (self.out_dir / sub / name).resolve() if sub else (self.out_dir / name).resolve()

    def _infer_overview_level(self, w: int, h: int) -> int:
        lvl, W, H = 0, w, h
        while max(W, H) > 512:
            lvl += 1
            W //= 2
            H //= 2
        return max(lvl, 1)

    def _reproject_to_tmp(self, src_ds: rasterio.io.DatasetReader) -> Path:
        """Reproject to self.dst_crs into a temporary tiled GTiff."""
        transform, width, height = calculate_default_transform(
            src_ds.crs, self.dst_crs, src_ds.width, src_ds.height, *src_ds.bounds
        )
        meta = src_ds.meta.copy()
        meta.update({
            "driver": "GTiff",
            "crs": self.dst_crs,
            "transform": transform,
            "width": width,
            "height": height,
            "tiled": True,
            "blockxsize": 512,
            "blockysize": 512,
            "compress": "DEFLATE",
            "predictor": 2 if meta.get("count", 1) == 1 else 3,
        })
        tmp = Path(".tmp") / f"_reproj_{self.src_path.stem}_{os.getpid()}.tif"
        tmp.parent.mkdir(parents=True, exist_ok=True)

        self.logger.info("Reprojecting %s → %s", self.src_path.name, self.dst_crs)
        with rasterio.open(tmp, "w", **meta) as dst:
            for b in range(1, src_ds.count + 1):
                reproject(
                    rasterio.band(src_ds, b),
                    rasterio.band(dst, b),
                    src_transform=src_ds.transform,
                    src_crs=src_ds.crs,
                    dst_transform=transform,
                    dst_crs=self.dst_crs,
                    resampling=Resampling[self.resampling],
                )
        return tmp

    # --------------------------- main API --------------------------

    def run(self) -> Tuple[Path, Dict]:
        out_path = self._target_path()
        out_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with rasterio.open(self.src_path) as src:
                if not src.crs:
                    raise IngestError(f"Raster has no CRS: {self.src_path}")

                # Reproject if needed
                if src.crs.to_string().upper() != self.dst_crs.upper():
                    reproj_path = self._reproject_to_tmp(src)
                    reproj = rasterio.open(reproj_path)
                    cleanup_tmp = True
                else:
                    reproj = src
                    cleanup_tmp = False

                try:
                    # Overviews
                    if self.overview_level is None:
                        self.overview_level = self._infer_overview_level(reproj.width, reproj.height)
                    self.overview_level = max(1, int(self.overview_level))

                    # nodata handling
                    nodata_value = self.nodata if self.nodata is not None else reproj.nodata

                    # COG translate
                    profile = cog_profiles[self.profile]
                    self.logger.info(
                        "COG translate → %s (profile=%s, overviews=%d, resampling=%s)",
                        out_path, self.profile, self.overview_level, self.resampling
                    )

                    cog_translate(
                        reproj,
                        str(out_path),
                        profile,
                        nodata=nodata_value,
                        overview_level=self.overview_level,
                        overview_resampling=Resampling[self.resampling],
                        web_optimized=False,
                        config={
                            "GDAL_TIFF_INTERNAL_MASK": "YES",
                            "GDAL_NUM_THREADS": "ALL_CPUS",
                        },
                    )
                finally:
                    if cleanup_tmp:
                        reproj.close()
                        Path(reproj.name).unlink(missing_ok=True)

            # Hash & sidecar
            digest = Provenance.digest_and_sidecar(out_path)

            # Inspect final product for STAC geometry/meta
            with rasterio.open(out_path) as ds:
                left, bottom, right, top = ds.bounds
                bbox = [left, bottom, right, top]
                geometry = {
                    "type": "Polygon",
                    "coordinates": [[[left, bottom], [right, bottom], [right, top], [left, top], [left, bottom]]],
                }
                props = {
                    "kfm:ingest": "raster",
                    "kfm:sha256": digest,
                    "kfm:src": self.relpath(self.src_path),
                    "file:meta": Provenance.file_stats(out_path),
                    "raster:width": ds.width,
                    "raster:height": ds.height,
                    "raster:count": ds.count,
                    "raster:dtype": str(ds.dtypes[0]) if ds.count else None,
                    "proj:epsg": int(self.dst_crs.split(":")[1]) if ":" in self.dst_crs else None,
                    "proj:shape": [ds.height, ds.width],
                    "proj:transform": list(ds.transform)[:6],  # affine (a, b, d, e, xoff, yoff)
                }

            extra = self.extra_properties() or {}
            props.update(extra)

            media_type = Provenance.inferred_media_type(out_path)
            if "geotiff" in media_type and "profile=cloud-optimized" not in media_type:
                media_type += "; profile=cloud-optimized"

            item = StacWriter.mk_item(
                id_=out_path.stem,
                source_path=self.src_path,
                out_path=out_path,
                bbox=bbox,
                geometry=geometry,
                properties=props,
                asset_media_type=media_type,
                collection=self.stac_collection,
            )

            # Persist STAC item
            StacWriter.write_item(item, self.stac_items_dir)

            return out_path, item

        except IngestError:
            raise
        except Exception as e:
            # Convert unexpected issues into IngestError with context.
            raise IngestError(f"Raster ingest failed for {self.src_path}: {e}") from e
