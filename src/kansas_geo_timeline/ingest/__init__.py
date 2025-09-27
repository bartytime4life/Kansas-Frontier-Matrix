# src/kansas_geo_timeline/ingest/__init__.py
"""Kansas Geo Timeline — ingest package.

Entry points for the ingestion layer:
- RasterIngestor  → Raster → COG (EPSG:4326), SHA256 sidecar, STAC item
- VectorIngestor  → Vector → GeoJSON (EPSG:4326), SHA256 sidecar, STAC item
- StacWriter      → Minimal STAC item builder/writer
- Provenance      → Hashing + sidecar utilities

Quickstart
----------
from kansas_geo_timeline.ingest import ingest_raster, ingest_vector
out, item = ingest_raster("data/raw/topo_1938.tif")
out, item = ingest_vector("data/raw/towns.shp")
"""
from __future__ import annotations

from pathlib import Path
from typing import Tuple, Dict, Optional

try:
    # Prefer canonical name; fall back to module name if packaged differently.
    try:
        from importlib.metadata import version, PackageNotFoundError  # py>=3.8
    except Exception:  # pragma: no cover
        from importlib_metadata import version, PackageNotFoundError  # type: ignore
    try:
        __version__ = version("kansas-geo-timeline")
    except PackageNotFoundError:
        try:
            __version__ = version("kansas_geo_timeline")
        except PackageNotFoundError:
            __version__ = "0.0.0"
except Exception:  # pragma: no cover
    __version__ = "0.0.0"

from .raster_ingest import RasterIngestor
from .vector_ingest import VectorIngestor
from .stac_writer import StacWriter
from .provenance import Provenance

# Common default locations (kept here so downstream code can import from one place)
DEFAULT_PROCESSED_DIR: Path = Path("data/processed")
DEFAULT_STAC_ITEMS_DIR: Path = Path("stac/items")

def ingest_raster(
    src_path: str | Path,
    out_dir: str | Path | None = DEFAULT_PROCESSED_DIR,
    *,
    dst_crs: str = "EPSG:4326",
    profile: str = "deflate",             # or "webp"
    overview_level: Optional[int] = None, # auto if None
    resampling: str = "bilinear",
    nodata: Optional[float] = None,
    stac_collection: Optional[str] = None,
    stac_items_dir: str | Path = DEFAULT_STAC_ITEMS_DIR,
) -> Tuple[Path, Dict]:
    """One-call raster ingest → (output_path, stac_item_dict)."""
    ing = RasterIngestor(
        src_path=src_path,
        out_dir=out_dir,
        dst_crs=dst_crs,
        profile=profile,
        overview_level=overview_level,
        resampling=resampling,
        nodata=nodata,
        stac_collection=stac_collection,
        stac_items_dir=stac_items_dir,
    )
    return ing.run()

def ingest_vector(
    src_path: str | Path,
    out_dir: str | Path | None = DEFAULT_PROCESSED_DIR,
    *,
    dst_crs: str = "EPSG:4326",
    indent: int = 2,
    stac_collection: Optional[str] = None,
    stac_items_dir: str | Path = DEFAULT_STAC_ITEMS_DIR,
    layer: Optional[str] = None,
) -> Tuple[Path, Dict]:
    """One-call vector ingest → (output_path, stac_item_dict)."""
    ing = VectorIngestor(
        src_path=src_path,
        out_dir=out_dir,
        dst_crs=dst_crs,
        indent=indent,
        stac_collection=stac_collection,
        stac_items_dir=stac_items_dir,
        layer=layer,
    )
    return ing.run()

__all__ = (
    "RasterIngestor",
    "VectorIngestor",
    "StacWriter",
    "Provenance",
    "DEFAULT_PROCESSED_DIR",
    "DEFAULT_STAC_ITEMS_DIR",
    "ingest_raster",
    "ingest_vector",
    "__version__",
)
