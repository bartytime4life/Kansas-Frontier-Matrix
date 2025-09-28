# `data/sources/dem/tile_indexes/` — DEM & LiDAR Tile Indexes

This directory contains **tile index descriptors** for Digital Elevation Models (DEM)  
and LiDAR collections. Indexes define how to fetch, mosaic, and manage tiled elevation data  
(county-level LiDAR, USGS 3DEP, FEMA/USACE surveys, etc.) before conversion into statewide  
Cloud-Optimized GeoTIFFs (COGs).

---

## Purpose

- Store **curated descriptors** (`*.json`, `*.yml`) for tile indexes (shapefiles, GeoJSON, REST services).  
- Enable reproducible **fetch + mosaic** workflows in the Makefile pipeline.  
- Document provenance for each LiDAR/DEM collection (publisher, coverage, period, license).  
- Provide spatial footprints for STAC Items & Collections.

---

## Typical Contents

```

data/sources/dem/tile_indexes/
├── ks_lidar_county_index.json   # County-based LiDAR tile index descriptor
├── usgs_3dep_index.json         # USGS 3DEP nationwide tile index (subset: Kansas)
├── fema_flood_lidar.json        # FEMA/USACE project-level LiDAR indexes
└── README.md                    # This file

````

---

## Descriptor Schema

Tile index descriptors must follow the **KFM Source Descriptor schema**  
(`data/sources/schema.source.json`). Example:

```json
{
  "id": "ks_lidar_county",
  "title": "Kansas County LiDAR Tile Index",
  "type": "vector",
  "period": "2012-2020",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://data.kansasgis.org/lidar/ks_county_index.geojson"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.kansasgis.org/"
  },
  "provenance": {
    "attribution": "Kansas DASC",
    "retrieved": "2025-09-27T00:00:00Z"
  },
  "keywords": ["DEM", "LiDAR", "Kansas", "tile index"]
}
````

---

## Workflow

1. **Add/edit a descriptor** here (`*_index.json`).
2. **Validate** with:

   ```bash
   make validate-sources
   ```
3. **Fetch** the tile index:

   ```bash
   make fetch
   ```

   → downloads to `data/raw/dem/tile_indexes/` (ignored by git).
4. Use `make dem` or `make mosaic` targets to:

   * Fetch referenced DEM/LiDAR tiles.
   * Mosaic into statewide/region COGs.
   * Generate `_meta.json` and `*.sha256` sidecars.
5. **Catalog**:

   ```bash
   make stac
   ```

   → builds STAC Items for each index and mosaic.

---

## Integration Notes

* Always convert raw DEMs to **COGs** (`make cogs`).
* Keep raw LiDAR LAS/LAZ in `data/raw/` — only publish mosaics.
* Normalize CRS to **EPSG:4326** for viewer, but keep original CRS recorded in `_meta.json`.
* STAC items should include:

  * `geometry` footprint of the index.
  * `kfm:tile_count` for QA.
  * `proj:epsg` for CRS.

---

## Best Practices

* Maintain **checksums** (`*.sha256`) for both index and derived mosaics.
* Record `retrieved` datetime each time an index is updated.
* Use **confidence flags** if index coverage is incomplete.
* Group multi-project indexes logically (e.g., by watershed, county, or FEMA project).

---

✦ **Summary:**
`data/sources/dem/tile_indexes/` is the **blueprint for tiled DEM/LiDAR collections**.
It ensures that raw elevation tiles can be consistently located, mosaicked, and published
as reproducible COGs with full provenance.

```
