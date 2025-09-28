# Kansas-Frontier-Matrix — DEM & Elevation Sources

This directory contains **Digital Elevation Models (DEM)** and related derivatives  
(hillshade, slope, aspect, contours) for Kansas. These datasets form the **terrain layer**  
of the Kansas-Frontier-Matrix knowledge hub and are central to geological, hydrological,  
and historical analyses.

---

## Purpose

- Provide **baseline elevation models** (statewide and county-level).  
- Support **derivative products**: hillshade, slope, aspect rasters.  
- Enable **historical comparisons** with pre-dam and historical survey elevations.  
- Integrate **LiDAR & 3DEP** high-resolution data where available.  
- Document **provenance, checksums, and lineage** for reproducibility.

---

## Directory Layout

```

data/sources/dem/
├── ks_dem_1m.json          # Statewide 1-m DEM (Kansas DASC / USGS 3DEP)
├── ks_lidar_county.json    # Example LiDAR tile index for county-level fetch
├── usgs_3dep_index.json    # 3DEP coverage metadata
├── ks_hillshade.json       # Example config for derived hillshade layer
├── processed/              # Derived COGs (hillshade, slope, aspect)
└── README.md               # This file

````

> **Note:** Large binaries (GeoTIFFs, COGs, LiDAR tiles) are not tracked directly —  
> they go to **Git LFS** or `data/raw/` (ignored). Only descriptors, sidecars, and metadata live in git.

---

## Metadata Requirements

Each DEM source config (`.json` or `.yml`) must follow the **KFM Source Descriptor schema**  
(`data/sources/schema.source.json`). Example:

```json
{
  "id": "ks_dem_1m",
  "title": "Kansas Statewide DEM (1-m resolution)",
  "type": "raster",
  "description": "1-m DEM mosaic from Kansas DASC / USGS 3DEP program.",
  "period": "2012-2020",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://prd-tnm.s3.amazonaws.com/Lidar/KS/DEM_1m_2020.tif"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.usgs.gov/faqs/data-policy"
  },
  "provenance": {
    "attribution": "USGS 3DEP / Kansas DASC",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["DEM", "elevation", "Kansas", "LiDAR", "terrain"]
}
````

Key rules:

* `bbox` must be in EPSG:4326 (WGS84 lon/lat).
* `urls[]` may list multiple tiles; `make fetch` will fan-out.
* Always include `license` and `provenance`.
* Use `period` to link with time slider and STAC temporal fields.

---

## Recommended Sources

* **Kansas Data Access & Support Center (DASC)** — 1-m statewide DEM, LiDAR tile services.
* **USGS 3D Elevation Program (3DEP)** — LiDAR & DEM coverage for Kansas.
* **FEMA / USACE** — selected LiDAR collections (county or watershed).
* **Kansas Geological Survey (KGS)** — historical elevation & survey data.

---

## Integration Notes

* All DEMs should be converted to **Cloud-Optimized GeoTIFFs (COGs)** (`make cogs`).
* Derivatives (hillshade, slope, aspect) stored in `processed/` with **STAC Items**.
* Link to **knowledge graph** via `Place` nodes (counties, watersheds).
* Document uncertainty: use `confidence` if DEMs contain voids or artifacts.
* CI validates COG structure (`make validate-cogs`) and schema compliance.

---

## Best Practices

* Maintain **checksums** (`*.sha256`) and record fetch dates in `provenance`.
* Keep **raw LiDAR tiles** in `data/raw/dem/` (ignored by git).
* Use original CRS in raw storage, but normalize to **EPSG:4326** for web viewer.
* Automate builds:

  ```bash
  make dem        # build statewide DEM COGs
  make hillshade  # hillshade derivatives
  make terrain    # slope/aspect/roughness stack
  ```
* Ensure each artifact has a sidecar `_meta.json` with lineage + stats.

---

## Debugging & Validation

* `make validate-sources` → check JSON descriptors against schema.
* `make validate-cogs` → verify COG tiling, compression, and overviews.
* `make checksums` → refresh `.sha256` sidecars.
* Check STAC compliance:

  ```bash
  make stac
  make validate-stac
  ```

---

## References

* [USGS 3DEP](https://www.usgs.gov/3d-elevation-program)
* [Kansas DASC LiDAR & DEM](https://www.kansasgis.org/)
* Data Resource Analysis Report — DEM/LiDAR gaps (see `/docs/reports/`)
* MCP Scientific Method Templates (`/docs/mcp/`)

---

✦ **Summary:**
`data/sources/dem/` contains descriptors for Kansas DEM sources and processing configs.
They guarantee that elevation products are **traceable**, **reproducible**, and **integrated** into the
STAC catalog, CI validation, and downstream terrain analysis.

```
