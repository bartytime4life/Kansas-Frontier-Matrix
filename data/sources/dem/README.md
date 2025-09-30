<div align="center">

# 🏔️ Kansas Geo Timeline — DEM & Elevation Sources (`data/sources/dem/`)

**Mission:** Provide **Digital Elevation Models (DEMs)** and derivatives (hillshade, slope, aspect, contours)  
as the foundation for Kansas Frontier Matrix terrain, hydrology, and historical analyses.  

📌 Descriptors follow [`schema.source.json`](../schema.source.json)  
📌 Drive `make fetch` → `make cogs` → `make stac` workflows  
📌 Guarantee **traceability, reproducibility, and STAC compliance**  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

## 🎯 Purpose

- 🌍 Supply **baseline statewide and county DEMs**.  
- 🖼️ Support **derivatives** (hillshade, slope, aspect, roughness).  
- 📜 Enable **historical comparisons** (e.g., pre-dam vs modern).  
- 🔬 Integrate **LiDAR & USGS 3DEP** for high-resolution terrain.  
- 🧾 Maintain **checksums + provenance** for MCP reproducibility.  

---

## 📂 Directory layout

[data/sources/dem/]
├── ks_dem_1m.json          # Statewide 1-m DEM (DASC / USGS 3DEP)
├── ks_lidar_county.json    # Example LiDAR tile index
├── usgs_3dep_index.json    # USGS 3DEP coverage metadata
├── ks_hillshade.json       # Derived hillshade config
├── processed/              # Processed derivatives (hillshade, slope, aspect)
└── README.md

🔒 **Note:** Raw GeoTIFFs, LiDAR tiles, and large COGs live in `data/raw/**` (ignored) or tracked via LFS/DVC.  
Only descriptors, metadata, and sidecars are committed to git.  

---

## 🧭 Metadata requirements

Each DEM descriptor must comply with the **KFM Source Descriptor schema**.  

Example:

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

Rules:
	•	bbox in EPSG:4326 (lon/lat).
	•	urls[] may list multiple tiles (fanned by make fetch).
	•	Always include license + provenance.
	•	period must map directly to STAC temporal extent.

⸻

🌍 Recommended sources
	•	Kansas DASC → 1-m statewide DEM, LiDAR services.
	•	USGS 3DEP → official LiDAR & DEM coverage.
	•	FEMA / USACE → watershed & county surveys.
	•	Kansas Geological Survey (KGS) → historical elevation/surveys.

⸻

🔗 Integration notes
	•	🗜️ All DEMs → converted to COGs (make cogs).
	•	🖼️ Derivatives (hillshade, slope, aspect) → written to processed/ and published as STAC Items.
	•	🔗 Linked to knowledge graph via Place nodes (counties, watersheds).
	•	⚠️ Document confidence for void-filled or artifacted DEMs.
	•	✅ CI enforces schema + COG structure validation.

⸻

📝 Best practices
	•	🧾 Maintain .sha256 checksums + provenance timestamps.
	•	📦 Keep raw LiDAR tiles in data/raw/dem/ (ignored by git).
	•	🗺️ Store raw DEMs in original CRS, normalize processed outputs to EPSG:4326.
	•	⚙️ Automate builds with Make:

make dem        # statewide DEM COGs
make hillshade  # hillshades
make terrain    # slope/aspect/roughness


	•	🗂️ Each artifact requires a _meta.json lineage sidecar.

⸻

🔍 Debugging & validation
	•	make validate-sources → JSON schema validation.
	•	make validate-cogs → check tiling, overviews, compression.
	•	make checksums → regenerate .sha256.
	•	make stac && make validate-stac → ensure STAC compliance.

⸻

📚 References
	•	USGS 3DEP — LiDAR/DEM program.
	•	Kansas DASC — LiDAR & DEM portal.
	•	Data Resource Analysis Report — DEM/LiDAR gaps (/docs/reports/).
	•	MCP Templates — Scientific Method logs (/docs/mcp/).

⸻

📝 TL;DR
	•	data/sources/dem/ = blueprints for Kansas DEMs.
	•	Each descriptor must include provenance, license, bbox, and temporal coverage.
	•	Pipeline = raw → processed/COG → STAC → Knowledge Graph.
	•	Ensures Kansas elevation layers are traceable, reproducible, MCP-grade auditable.

✅ If it shapes Kansas terrain → it belongs here.