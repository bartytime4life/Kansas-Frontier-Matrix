# `ingest/` — Data Ingestion & Conversion Layer

This module is the **entry point** for pulling raw datasets (maps, shapefiles, rasters, deeds, hydrology, etc.)
into the **Kansas Geo Timeline** pipeline.  
It ensures **format normalization, reprojection (EPSG:4326), provenance tracking, and STAC registration.**

---

## Design Goals

- **Single source of truth**: All raw → processed transformations pass through here.
- **Reproducible**: Scripts are deterministic, with SHA256 sidecars for each artifact.
- **Web-ready outputs**: Rasters → COG (Cloud Optimized GeoTIFF), Vectors → GeoJSON.
- **STAC-aware**: Every converted artifact gets a STAC Item for discovery and metadata lineage.
- **Idempotent**: Safe to re-run; outputs overwrite only when hashes change.

---

## Directory Layout

```

src/kansas_geo_timeline/ingest/
├── **init**.py
├── base.py              # Abstract base classes for Ingestors
├── raster_ingest.py     # Raster → COG pipeline
├── vector_ingest.py     # Vector → GeoJSON pipeline
├── stac_writer.py       # Helper to emit STAC Item JSON
├── provenance.py        # Hashing, metadata, sidecar utilities
└── README.md            # This file

````

---

## Workflow

```mermaid
flowchart TD
  A["Raw Data\n(data/raw/*.tif, *.shp, *.gpkg)"] --> B["Ingest Scripts\n(raster_ingest.py,\nvector_ingest.py)"]
  B --> C["Processed Artifacts\n(data/processed/*.tif, *.geojson)"]
  C --> D["STAC Items\n(stac/items/*.json)"]
  D --> E["Viewer Config\n(web/config/*.json)"]
````

* **Input**: Raw datasets (`data/raw/`)
* **Process**: Conversion + reprojection + metadata (via `scripts/convert.py` and ingest classes)
* **Output**:

  * `data/processed/…` (COG/GeoJSON)
  * `stac/items/…` (with checksum + provenance)
  * `web/config/…` (viewer config regeneration)

---

## Usage

### CLI (via `scripts/convert.py`)

```bash
# Raster → COG
python scripts/convert.py raster-to-cog data/raw/topo_1938.tif data/processed/dem/topo_1938.tif

# Vector → GeoJSON
python scripts/convert.py vector-to-geojson data/raw/towns.shp data/processed/towns_points.json
```

### Python API

```python
from kansas_geo_timeline.ingest.raster_ingest import RasterIngestor
from kansas_geo_timeline.ingest.vector_ingest import VectorIngestor

r = RasterIngestor("data/raw/topo_1938.tif")
cog_path, stac_item = r.run()

v = VectorIngestor("data/raw/towns.shp")
geojson_path, stac_item = v.run()
```

---

## Dependencies

* **Raster I/O**: [`rasterio`](https://rasterio.readthedocs.io/), [`rio-cogeo`](https://github.com/cogeotiff/rio-cogeo)
* **Vector I/O**: [`fiona`](https://fiona.readthedocs.io/), [`pyproj`](https://pyproj4.github.io/pyproj/stable/)
* **STAC**: [`pystac`](https://pystac.readthedocs.io/)
* **CLI**: [`click`](https://click.palletsprojects.com/)

All bundled in `pyproject.toml`.

---

## Notes

* Always reproject to **EPSG:4326** for consistency with MapLibre & time slider.
* Each artifact gets a `.sha256` sidecar for integrity checks.
* Ingestion scripts should be wired into **Makefile** targets (`make cogs`, `make vectors`, `make stac`).
* If adding a new data source, update:

  * `data/sources/*.json` (descriptor)
  * `scripts/convert.py` (if new format needs handling)
  * `stac/collections/*.json` (for catalog registration)

---

✅ **Mission-grade principle**: every dataset entering this repo must pass through this ingestion layer.
This ensures traceability from **raw source → processed artifact → STAC → web viewer**.

```
