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
├── ks\_dem\_1m.json             # Statewide 1-m DEM (Kansas DASC / USGS 3DEP)
├── ks\_lidar\_county.json       # Example LiDAR tile index for county-level fetch
├── ks\_hillshade.json          # Derived hillshade (example config)
├── usgs\_3dep\_index.json       # 3DEP coverage metadata
├── processed/                 # Derived COGs (hillshade, slope, aspect)
└── README.md                  # This file

````

---

## Metadata Requirements

Each DEM source config (`.json` or `.yml`) must follow the **STAC-like schema**:

```json
{
  "id": "ks_dem_1m",
  "title": "Kansas Statewide DEM (1-m resolution)",
  "type": "raster",
  "version": "1.0.0",
  "description": "1-m DEM mosaic from Kansas DASC / USGS 3DEP program.",
  "temporal": {
    "start": "2012-01-01",
    "end": "2020-12-31"
  },
  "spatial": {
    "bbox": [-102.05, 36.99, -94.61, 40.00]
  },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://prd-tnm.s3.amazonaws.com/Lidar/KS/DEM_1m_2020.tif"
      ]
    }
  ],
  "lineage": [
    "Fetched from USGS TNM S3",
    "Converted to Cloud-Optimized GeoTIFF",
    "Tile pyramids built for MapLibre viewer"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123abc…",
    "filesize_bytes": null
  },
  "keywords": ["DEM", "elevation", "Kansas", "LiDAR", "terrain"]
}
````

---

## Recommended Sources

* **Kansas Data Access & Support Center (DASC)** — 1-m statewide DEM, LiDAR tile services.
* **USGS 3D Elevation Program (3DEP)** — LiDAR & DEM coverage for Kansas.
* **FEMA / USACE** — selected LiDAR collections (county or watershed).
* **Kansas Geological Survey (KGS)** — historical elevation & survey data.

---

## Integration Notes

* All DEMs should be converted to **Cloud-Optimized GeoTIFFs (COGs)**.
* Derivatives (hillshade, slope, aspect) stored in `processed/` with **STAC Items**.
* Link to **knowledge graph** via `Place` nodes (counties, watersheds).
* Document uncertainty: use **confidence flags** if DEMs contain voids or artifacts.

---

## Best Practices

* Maintain **checksums** and record fetch dates in `data/provenance/`.
* Keep **raw LiDAR tiles** in `data/raw/` and only serve mosaicked COGs here.
* Align DEM CRS with EPSG:4326 for web viewer, but retain original projection in raw storage.
* Use **Makefile targets** (`make dem`, `make hillshade`) for automated processing.

---

## References

* [USGS 3DEP](https://www.usgs.gov/3d-elevation-program)
* [Kansas DASC LiDAR & DEM](https://www.kansasgis.org/)
* [Kansas Frontier Matrix Design: Environmental & Terrain Layers]: contentReference[oaicite:0]{index=0}
* [Data Resource Analysis Report — DEM/LiDAR gaps]: contentReference[oaicite:1]{index=1}
* [MCP Scientific Method Templates]: contentReference[oaicite:2]{index=2}

---

```
