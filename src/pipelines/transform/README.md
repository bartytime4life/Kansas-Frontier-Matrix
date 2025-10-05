<div align="center">

# 🔄 Kansas Frontier Matrix — Data Transformation Pipelines  
`src/pipelines/transform/README.md`

**Standardization · Geospatial Processing · Temporal Normalization**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/pipelines/transform/`** directory contains all **data transformation, normalization, and conversion** utilities used in the **Kansas Frontier Matrix (KFM)** pipeline.  

After data is fetched and validated in `fetch/`, this stage converts raw assets into **open, interoperable formats** such as **GeoJSON**, **COG GeoTIFF**, **CSV**, and **Parquet**, and prepares them for semantic ingestion into the **Knowledge Graph** and **STAC catalog**.  

Transformation scripts follow the **Master Coder Protocol (MCP)** to ensure **transparency, reproducibility, and scientific traceability**.

---

## 🏗 Pipeline Role in the System

```mermaid
flowchart TD
    A["data/raw/<source>/*"] --> B["Transform Scripts<br/>normalize, reproject, clean, extract"]
    B --> C["data/processed/<layer>/*.<geojson|tif|csv>"]
    C --> D["data/stac/<collection>.json<br/>metadata + provenance"]
    D --> E["Knowledge Graph (Neo4j)"]
````

<!-- END OF MERMAID -->

This layer standardizes the structure, CRS (Coordinate Reference System), and temporal fields for all datasets, ensuring consistency across:

* **Spatial Data** (GIS rasters, shapefiles, DEMs)
* **Tabular Data** (census, water tables, weather records)
* **Text-Derived Data** (OCR-extracted entities from documents)

---

## 📂 Directory Layout

```
src/pipelines/transform/
├── __init__.py
├── geocode_utils.py         # Geocoding + GNIS integration
├── raster_to_cog.py         # Convert rasters to Cloud-Optimized GeoTIFFs
├── vector_to_geojson.py     # Convert shapefiles to GeoJSON (EPSG:4326)
├── csv_cleaner.py           # Normalize tabular and time-series data
├── text_cleaner.py          # Preprocess OCR text (remove noise, detect language)
├── date_normalizer.py       # Convert inconsistent date formats to ISO 8601
├── schema_validator.py      # Validate processed files against JSON Schemas
└── README.md                # (this file)
```

Each script performs a single, atomic operation, enabling modular testing and reproducibility.

For example:
`raster_to_cog.py` takes TIFF or MrSID files and produces COGs with pyramidal overviews and WGS84 projection.
`vector_to_geojson.py` simplifies shapefiles and adds metadata for STAC ingestion.

---

## ⚙️ Common Workflow

1. **Reproject Spatial Data**

   * All layers are reprojected to **EPSG:4326 (WGS84)** for web mapping compatibility.
   * Uses `gdalwarp` or `rasterio.warp` for rasters, and `ogr2ogr` for vector layers.

2. **Convert Raster Formats**

   * Legacy TIFFs or MrSID imagery are converted to **Cloud-Optimized GeoTIFF (COG)** using `rio-cogeo`.
   * Adds internal overviews and tiled structure for fast map loading.

   ```bash
   rio cogeo create input.tif output_cog.tif --overview-level=5 --web-optimized
   ```

3. **Convert Vector Formats**

   * Converts `.shp` or `.gdb` to GeoJSON:

     ```bash
     ogr2ogr -f GeoJSON -t_srs EPSG:4326 output.json input.shp
     ```
   * Ensures attributes are simplified and topology errors fixed.

4. **Clean and Normalize Tables**

   * Strip null values, rename inconsistent columns, unify time fields:

     ```python
     df['date'] = pd.to_datetime(df['date'], errors='coerce')
     df.to_csv('cleaned.csv', index=False)
     ```

5. **Geocode & Spatial Join**

   * Resolve place names to coordinates via **USGS GNIS** or **OpenStreetMap Nominatim**.
   * Merge with county boundaries or hydrology polygons for context.

6. **Temporal Normalization**

   * Converts vague time references into ISO intervals (e.g., “Spring 1857” → `1857-03-01/1857-06-01`).
   * Aligns with **OWL-Time** and **PeriodO** for semantic time interoperability.

7. **Validate Outputs**

   * Uses `schema_validator.py` to check GeoJSON and CSVs against project schemas.
   * Enforces presence of: `id`, `title`, `license`, `spatial`, `temporal`, `provenance`.

---

## 🧱 Example Usage

```bash
# Convert all shapefiles to GeoJSON
python src/pipelines/transform/vector_to_geojson.py --input data/raw/usgs --output data/processed/vectors

# Create COGs from DEM rasters
python src/pipelines/transform/raster_to_cog.py --input data/raw/dem --output data/processed/rasters

# Geocode place names from a CSV
python src/pipelines/transform/geocode_utils.py --file data/raw/settlements.csv --out data/processed/geocoded.csv

# Run full transformation sequence
make transform
```

---

## 🧮 Script Template for New Transforms

```python
#!/usr/bin/env python3
"""
@MCP-LOG Kansas Frontier Matrix – Transformation Script Template
Purpose: Clean and standardize a dataset for STAC + Graph ingestion.
"""
import pandas as pd, os, json
from datetime import datetime

def transform(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df.columns = [c.strip().lower() for c in df.columns]
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    meta = {
        "id": os.path.basename(output_path),
        "processed": datetime.now().isoformat(),
        "source": input_path,
        "license": "Open Data / Public Domain"
    }
    json.dump(meta, open(output_path + ".meta.json", "w"), indent=2)
    print(f"✅ Transformed {input_path} → {output_path}")

if __name__ == "__main__":
    transform("data/raw/example.csv", "data/processed/example_clean.csv")
```

---

## 🧾 Standards & Conventions

| Type         | Standard                      | Description                          |
| :----------- | :---------------------------- | :----------------------------------- |
| Spatial Data | EPSG:4326                     | Geographic WGS84 projection          |
| Raster       | COG (Cloud-Optimized GeoTIFF) | Web-optimized tiled raster format    |
| Vector       | GeoJSON                       | Open JSON-based GIS standard         |
| Temporal     | ISO 8601 / OWL-Time           | Standard date/time intervals         |
| Metadata     | STAC 1.0                      | Spatiotemporal asset catalog entries |
| Validation   | JSON Schema                   | Enforces structure + completeness    |

---

## 🧰 Logging & Provenance

All transformation steps log metadata to `logs/pipelines/transform.log`:

```
[2025-10-05 10:32:11] vector_to_geojson | kansas_trails.shp → kansas_trails.geojson | OK
[2025-10-05 10:35:07] raster_to_cog | ks_1m_dem.tif → ks_1m_dem_cog.tif | SHA256=afe2b...
[2025-10-05 10:41:22] geocode_utils | 125 entries resolved via GNIS | 4 unresolved
```

---

## 🧩 Integration with Other Pipelines

* **Upstream:** `fetch/` provides raw inputs from source manifests.
* **Downstream:** Outputs feed `enrich/` (AI/NLP) and `load/` (graph + STAC ingestion).
* **Automation:** `Makefile` target `make transform` runs all steps sequentially.

---

## 📚 References

* [Kansas Frontier Matrix – File & Data Architecture](../../../docs/architecture.md)
* [AI System Developer Documentation](../../../docs/ai-system.md)
* [Scientific Modeling & Simulation Guide](../../../docs/standards/README.md)
* [Integrating Historical & Geological Research (MCP Reference)](../../../docs/integration/README.md)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Open Science · Open Data · Reproducible History*

</div>

