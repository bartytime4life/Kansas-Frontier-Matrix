<div align="center">

# 🗺️ Kansas-Frontier-Matrix — DEM & LiDAR Tile Indexes  
`data/sources/dem/tile_indexes/`

**Mission:** Curate descriptors for **DEM & LiDAR tile indexes** (county LiDAR, USGS 3DEP, FEMA/USACE surveys, etc.)  
to enable reproducible **fetch → mosaic → COG conversion** pipelines across Kansas.

📌 Validated against [`schema.source.json`](../../schema.source.json)  
📌 Workflow: `make fetch` → `make mosaic` → `make stac`  
📌 Guarantee **traceability, provenance, and spatial footprints** for tiled elevation data  

---

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../.github/workflows/automerge.yml)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)  

</div>

---

## 🎯 Purpose

- 📖 Store **descriptor JSON/YAML** files for DEM & LiDAR tile indexes (GeoJSON, Shapefile, REST services).  
- 🔄 Enable reproducible **fetch + mosaic workflows** in the Makefile pipeline.  
- 🧾 Document provenance (publisher, coverage, time period, license).  
- 🌍 Provide **spatial footprints** for STAC Items & Collections.  

---

## 📂 Directory Layout

```text
[data/sources/dem/tile_indexes/]
├── ks_lidar_county_index.json   # County-based LiDAR tile index descriptor
├── usgs_3dep_index.json         # USGS 3DEP nationwide tile index (Kansas subset)
├── fema_flood_lidar.json        # FEMA/USACE project-level LiDAR indexes
└── README.md

⚠️ Large binaries (LAS/LAZ/GeoTIFF tiles) → stored in data/raw/** and tracked with Git LFS/DVC.  
✅ Only descriptors, metadata, and sidecars are committed to git.


⸻

🧭 Descriptor Schema

Each tile index descriptor must follow the KFM Source Descriptor schema.
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

Rules:
	•	bbox in EPSG:4326 (lon/lat).
	•	urls[] may list multiple tiles (expanded by make fetch).
	•	Always include license + provenance.
	•	period must map directly to STAC temporal extent.

⸻

🔄 Workflow

flowchart TD
  A["Add/Edit Descriptor\n(data/sources/dem/tile_indexes/*.json)"] --> B["Validate\nmake validate-sources"]
  B --> C["Fetch Tile Index\nmake fetch → data/raw/dem/tile_indexes/**"]
  C --> D["Fetch Tiles + Mosaic\nmake dem / make mosaic"]
  D --> E["Convert to COGs\nmake cogs → data/cogs/dem/**"]
  E --> F["Catalog\nmake stac → data/stac/items/**"]

<!-- END OF MERMAID -->



⸻

🔗 Integration Notes
	•	🗜️ All mosaicked DEMs → COGs (make cogs).
	•	📦 Raw LiDAR LAS/LAZ → data/raw/** (ignored by git).
	•	🌐 Normalize CRS to EPSG:4326 for web viewer; preserve original CRS in _meta.json.
	•	STAC Items must include:
	•	geometry footprint of the index
	•	kfm:tile_count for QA
	•	proj:epsg CRS metadata

⸻

📝 Best Practices
	•	🧾 Maintain .sha256 checksums for both indexes and mosaics.
	•	⏱️ Record retrieved datetime whenever an index is updated.
	•	⚠️ Use confidence flags for partial/incomplete coverage.
	•	📑 Group multi-project indexes logically (county, watershed, FEMA project).

⸻

🔍 Debugging & Validation

# Validate descriptors
make validate-sources

# Verify COGs
make validate-cogs

# Rebuild STAC
make stac
make validate-stac


⸻

✦ Summary

data/sources/dem/tile_indexes/ contains blueprints for tiled DEM/LiDAR collections.
They ensure raw elevation tiles can be consistently located, mosaicked, and published as reproducible COGs,
with complete provenance and STAC discoverability.

✅ If it indexes Kansas terrain tiles → it belongs here.