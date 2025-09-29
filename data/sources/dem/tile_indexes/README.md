<div align="center">

# 🗺️ Kansas-Frontier-Matrix — **DEM & LiDAR Tile Indexes** (`data/sources/dem/tile_indexes/`)

**Mission:** Provide curated descriptors for **DEM & LiDAR tile indexes** (county LiDAR, USGS 3DEP, FEMA/USACE surveys, etc.),  
enabling reproducible **fetch → mosaic → COG conversion** pipelines.  

📌 Validated against [`schema.source.json`](../../schema.source.json)  
📌 Drive **`make fetch` → `make mosaic` → `make stac`** workflows  
📌 Guarantee **traceability, provenance, and spatial footprints** for tiled elevation data  

</div>

---

## Purpose

- 📖 Store **descriptor JSON/YAML** files for DEM & LiDAR tile indexes (GeoJSON, Shapefile, REST services).  
- 🔄 Enable reproducible **fetch + mosaic workflows** in the Makefile pipeline.  
- 🧾 Document provenance: publisher, coverage, time period, license.  
- 🌍 Provide **spatial footprints** for STAC Items & Collections.  

---

## Directory Layout

```text
data/sources/dem/tile_indexes/
├── ks_lidar_county_index.json   # County-based LiDAR tile index descriptor
├── usgs_3dep_index.json         # USGS 3DEP nationwide tile index (subset: Kansas)
├── fema_flood_lidar.json        # FEMA/USACE project-level LiDAR indexes
└── README.md                    # This file

⚠️ Large binaries (LAS/LAZ/GeoTIFF tiles) → stored in data/raw/** and tracked with Git LFS/DVC.
✅ Only descriptors, metadata, and sidecars live in git.

⸻

Descriptor Schema

Tile index descriptors must follow the KFM Source Descriptor schema.
Example:

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


⸻

Workflow

flowchart TD
  A[Add/Edit Descriptor<br/>data/sources/dem/tile_indexes/*.json] --> B[Validate<br/>make validate-sources]
  B --> C[Fetch Tile Index<br/>make fetch → data/raw/dem/tile_indexes/**]
  C --> D[Fetch Tiles + Mosaic<br/>make dem / make mosaic]
  D --> E[Convert to COGs<br/>make cogs → data/cogs/dem/**]
  E --> F[Catalog<br/>make stac → data/stac/items/**]

<!-- END OF MERMAID -->



⸻

Integration Notes
	•	🗜️ All mosaicked DEMs → COGs (make cogs).
	•	📦 Raw LiDAR LAS/LAZ → data/raw/** (ignored by git).
	•	🌐 Normalize CRS to EPSG:4326 for web viewer, but preserve original CRS in _meta.json.
	•	STAC Items should include:
	•	geometry footprint of the index
	•	kfm:tile_count for QA
	•	proj:epsg CRS metadata

⸻

Best Practices
	•	🧾 Maintain checksums (*.sha256) for both indexes and mosaics.
	•	⏱️ Record retrieved datetime each time an index is updated.
	•	⚠️ Use confidence flags for partial/incomplete coverage.
	•	📑 Group multi-project indexes logically (county, watershed, FEMA project).

⸻

Debugging & Validation
	•	Validate descriptors:

make validate-sources


	•	Verify COGs:

make validate-cogs


	•	Rebuild STAC:

make stac
make validate-stac



⸻

✦ Summary:
data/sources/dem/tile_indexes/ contains blueprints for tiled DEM/LiDAR collections.
They ensure raw elevation tiles can be consistently located, mosaicked, and published as reproducible COGs
with complete provenance and STAC discoverability.

