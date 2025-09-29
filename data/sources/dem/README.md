<div align="center">

# 🏔️ Kansas-Frontier-Matrix — **DEM & Elevation Sources** (`data/sources/dem/`)

**Mission:** Provide **Digital Elevation Models (DEMs)** and their derivatives (hillshade, slope, aspect, contours)  
as the foundation for Kansas Frontier Matrix’s terrain, hydrology, and historical analyses.  

📌 Descriptors follow [`schema.source.json`](../schema.source.json)  
📌 Drive `make fetch` → `make cogs` → `make stac` workflows  
📌 Guarantee **traceability, reproducibility, and STAC compliance**  

</div>

---

## Purpose

- 🌍 Supply **baseline statewide and county DEMs**.  
- 🖼️ Support **derivative products**: hillshade, slope, aspect, roughness.  
- 📜 Enable **historical comparisons** (pre-dam vs modern).  
- 🔬 Integrate **LiDAR & USGS 3DEP** for high resolution.  
- 🧾 Ensure **provenance + checksums** for MCP-grade reproducibility.  

---

## Directory Layout

```text
data/sources/dem/
├── ks_dem_1m.json          # Statewide 1-m DEM (DASC / USGS 3DEP)
├── ks_lidar_county.json    # Example LiDAR tile index for county fetch
├── usgs_3dep_index.json    # USGS 3DEP coverage metadata
├── ks_hillshade.json       # Config for derived hillshade layer
├── processed/              # Derived DEM products (hillshade, slope, aspect)
└── README.md               # This file

🔒 Note: Raw GeoTIFFs, LiDAR tiles, and large COGs are tracked via Git LFS/DVC or data/raw/** (ignored).
Only descriptors, metadata, and sidecars live in git.

⸻

Metadata Requirements

Each DEM descriptor must comply with the KFM Source Descriptor schema.
Example:

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
	•	urls[] may list multiple tiles (auto-fanned by make fetch).
	•	Always include license + provenance.
	•	period links directly with STAC temporal extent.

⸻

Recommended Sources
	•	Kansas Data Access & Support Center (DASC) — 1-m statewide DEM, LiDAR services.
	•	USGS 3D Elevation Program (3DEP) — official LiDAR & DEM coverage.
	•	FEMA / USACE — watershed/county LiDAR surveys.
	•	Kansas Geological Survey (KGS) — historical elevation & survey data.

⸻

Integration Notes
	•	🗜️ All DEMs → Cloud-Optimized GeoTIFFs (COGs) (make cogs).
	•	🖼️ Derivatives (hillshade, slope, aspect) → processed/ + published as STAC Items.
	•	🔗 Link into knowledge graph via Place nodes (counties, watersheds).
	•	⚠️ Document uncertainty with confidence when DEMs contain voids or artifacts.
	•	✅ CI enforces schema + COG structure validation.

⸻

Best Practices
	•	🧾 Maintain .sha256 checksums + provenance dates.
	•	📦 Keep raw LiDAR tiles in data/raw/dem/ (ignored by git).
	•	🗺️ Raw = original CRS; processed = normalized to EPSG:4326.
	•	⚙️ Automate builds:

make dem        # build statewide DEM COGs
make hillshade  # derive hillshades
make terrain    # slope/aspect/roughness stack


	•	🗂️ Every artifact gets a _meta.json lineage sidecar.

⸻

Debugging & Validation
	•	make validate-sources → JSON schema validation.
	•	make validate-cogs → check COG overviews, tiling, compression.
	•	make checksums → regenerate .sha256 sidecars.
	•	make stac && make validate-stac → ensure STAC compliance.

⸻

References
	•	USGS 3DEP
	•	Kansas DASC LiDAR & DEM
	•	Internal: Data Resource Analysis Report — DEM/LiDAR gaps (/docs/reports/)
	•	MCP Scientific Method Templates (/docs/mcp/)

⸻

TL;DR
	•	data/sources/dem/ = blueprints for Kansas DEMs.
	•	Every descriptor has provenance, license, bbox, period.
	•	Pipeline = raw → processed/COG → STAC Item → Knowledge Graph.
	•	Ensures Kansas elevation layers are traceable, reproducible, and MCP-grade auditable.

✅ If it shapes Kansas’s terrain, it belongs here.

