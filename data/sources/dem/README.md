<div align="center">

# 🏔️ Kansas-Frontier-Matrix — DEM & Elevation Sources  
`data/sources/dem/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/dem/)  

**Mission:** Provide **Digital Elevation Models (DEMs)** and derivatives (hillshade, slope, aspect, contours)  
as the foundation for Kansas Frontier Matrix terrain, hydrology, and historical analyses.  

📌 Descriptors follow [`schema.source.json`](../schema.source.json)  
📌 Lifecycle: `make fetch` → `make cogs` → `make stac`  
📌 Guarantee **traceability, reproducibility, and STAC compliance**  

</div>

---

## 🎯 Purpose

- 🌍 Supply **baseline statewide and county DEMs**.  
- 🖼️ Support **derivatives** (hillshade, slope, aspect, roughness).  
- 📜 Enable **historical comparisons** (e.g., pre-dam vs. modern).  
- 🔬 Integrate **LiDAR & USGS 3DEP** for high-resolution terrain.  
- 🧾 Maintain **checksums + provenance** for MCP reproducibility.  

---

## 📂 Directory Layout

data/sources/dem/
├── ks_dem_1m.json          # Statewide 1-m DEM (DASC / USGS 3DEP)
├── ks_lidar_county.json    # Example LiDAR tile index
├── usgs_3dep_index.json    # USGS 3DEP coverage metadata
├── ks_hillshade.json       # Derived hillshade config
├── processed/              # Processed derivatives (hillshade, slope, aspect)
└── README.md

🔒 **Note:** Raw GeoTIFFs, LiDAR tiles, and large COGs live in `data/raw/**` (ignored) or tracked via Git LFS/DVC.  
Only descriptors, metadata, and sidecars are committed to git.  

---

## 🧭 Metadata Requirements

Every DEM descriptor must comply with `schema.source.json`.

**Example Descriptor**

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

Rules
	•	bbox must be EPSG:4326 (lon/lat).
	•	urls[] may list multiple tiles (expanded by make fetch).
	•	Always include license + provenance.
	•	period must map directly to STAC temporal extent.

⸻

🌍 Recommended Sources
	•	Kansas DASC → 1-m statewide DEM, LiDAR services.
	•	USGS 3DEP → official LiDAR & DEM coverage.
	•	FEMA / USACE → watershed & county surveys.
	•	Kansas Geological Survey (KGS) → historical elevation/surveys.

⸻

🔗 Integration Notes
	•	🗜️ All DEMs → converted to COGs (make cogs).
	•	🖼️ Derivatives (hillshade, slope, aspect) → written to processed/ and published as STAC Items.
	•	🔗 Linked to the Knowledge Graph via Place nodes (counties, watersheds).
	•	⚠️ Document confidence for void-filled or artifacted DEMs.
	•	✅ CI enforces schema + COG structure validation.

⸻

📝 Best Practices
	•	🧾 Maintain .sha256 checksums + provenance timestamps.
	•	📦 Keep raw LiDAR tiles in data/raw/dem/ (ignored by git).
	•	🗺️ Store raw DEMs in original CRS; normalize processed outputs to EPSG:4326.
	•	⚙️ Automate builds with Makefile targets:

make dem        # statewide DEM COGs
make hillshade  # hillshades
make terrain    # slope/aspect/roughness

	•	🗂️ Each artifact requires a _meta.json lineage sidecar.

⸻

🔍 Debugging & Validation

make validate-sources   # JSON Schema validation
make validate-cogs      # check COG tiling, overviews, compression
make checksums          # regenerate .sha256
make stac && make validate-stac   # ensure STAC compliance


⸻

📚 References
	•	USGS 3DEP — LiDAR/DEM program
	•	Kansas DASC — LiDAR & DEM portal
	•	Data Resource Analysis Report — DEM/LiDAR gaps (/docs/reports/)
	•	MCP Templates — Scientific Method logs (/docs/mcp/)

⸻

✅ QA Checklist
	•	Descriptors validated against schema
	•	License + provenance explicitly recorded
	•	Raw payloads stored in data/raw/ with .sha256 checksum
	•	COGs built + validated with internal overviews/compression
	•	STAC Items generated + linked to descriptors
	•	Large files tracked with LFS/DVC

⸻

📝 TL;DR
	•	data/sources/dem/ = blueprints for Kansas DEMs.
	•	Each descriptor must include provenance, license, bbox, and temporal coverage.
	•	Pipeline = raw → processed/COG → STAC → Knowledge Graph.
	•	Ensures Kansas elevation layers are traceable, reproducible, MCP-grade auditable.

<div align="center">


✅ If it shapes Kansas terrain → it belongs here.

</div>
```
