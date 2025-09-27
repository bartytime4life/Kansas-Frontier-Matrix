from __future__ import annotations
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
        profile: str = "deflate",  # or "webp"
        overview_level: Optional[int] = None,
        resampling: str = "bilinear",
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

    def _default_out_dir(self) -> Path:
        return Path("data/processed")

    def _target_path(self) -> Path:
        # Preserve basename, force .tif under out_dir
        name = self.src_path.stem + ".tif"
        return (self.out_dir / "dem" / name) if "dem" in self.src_path.as_posix().lower() else (self.out_dir / name)

    def _infer_overview_level(self, w: int, h: int) -> int:
        lvl, W, H = 0, w, h
        while max(W, H) > 512:
            lvl += 1
            W //= 2
            H //= 2
        return max(lvl, 1)

    def _reproject_to_tmp(self, src_ds: rasterio.io.DatasetReader) -> Path:
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
        tmp = Path(".tmp") / f"_reproj_{self.src_path.stem}.tif"
        tmp.parent.mkdir(parents=True, exist_ok=True)
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

    def run(self) -> Tuple[Path, Dict]:
        out_path = self._target_path()
        out_path.parent.mkdir(parents=True, exist_ok=True)

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

                profile = cog_profiles.get(self.profile)
                nodata_value = self.nodata if self.nodata is not None else reproj.nodata

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

        digest = Provenance.sha256_file(out_path)
        Provenance.write_sha256_sidecar(out_path, digest)

        # Simple bbox/geom (read from output)
        with rasterio.open(out_path) as ds:
            left, bottom, right, top = ds.bounds
            bbox = [left, bottom, right, top]
            geometry = {
                "type": "Polygon",
                "coordinates": [[
                    [left, bottom], [right, bottom], [right, top], [left, top], [left, bottom]
                ]],
            }

        props = {
            "kfm:ingest": "raster",
            "kfm:sha256": digest,
            "kfm:src": str(self.src_path.as_posix()),
            "proj:epsg": int(self.dst_crs.split(":")[1]) if ":" in self.dst_crs else None,
        }
        extra = self.extra_properties() or {}
        props.update(extra)

        item = StacWriter.mk_item(
            id_=out_path.stem,
            source_path=self.src_path,
            out_path=out_path,
            bbox=bbox,
            geometry=geometry,
            properties=props,
            asset_media_type="image/tiff; application=geotiff; profile=cloud-optimized",
            collection=self.stac_collection,
        )

        # Persist STAC item next to global items dir (optional)
        StacWriter.write_item(item, self.stac_items_dir)

        return out_path, item
