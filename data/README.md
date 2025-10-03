<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Data Directory (`/data/`)

**Mission:** Organize, validate, and track all geospatial & historical datasets  
that power the Kansas Frontier Matrix interactive map, timeline, and knowledge graph.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)  
[![MCP Protocol](https://img.shields.io/badge/Docs-MCP%20Aligned-green)](../docs/)  

</div>

---

## 📚 Purpose

This directory holds all **data references, metadata, and derived products** used in the project.  
It is designed for **reproducibility, provenance, and STAC-driven discoverability**:

- 🔗 **Manifests** describe external sources (no raw bulk in Git).  
- 🛠️ **Pipelines** fetch, process, and validate data into open formats.  
- 📜 **Provenance** is tracked with checksums, schema validation, and metadata.  
- 🌐 **Outputs** power the timeline map, knowledge graph, and Google Earth exports.  

---

## 📂 Layout

```bash
data/
├── sources/      # JSON/YAML manifests describing external datasets
├── raw/          # Local cache of fetched raw data (Git LFS/DVC pointers only)
├── processed/    # Clean, normalized outputs (GeoJSON, COGs, CSVs)
├── stac/         # SpatioTemporal Asset Catalog (collections & items in JSON)
├── derivatives/  # Computed products (hillshades, contours, mosaics, stats)
├── tiles/        # Ephemeral raster/vector tiles (PMTiles, MBTiles for previews)
├── work/         # Scratch space for pipelines, ephemeral only
└── tmp/          # Build leftovers, ignored by Git


⸻

🧰 Data Lifecycle

flowchart TD
A[“Sources\n(manifests, APIs)”] –> B[“Raw Fetch\n(data/raw)”]
B –> C[“Processing & ETL\n(data/processed)”]
C –> D[“STAC Catalog\n(data/stac)”]
D –> E[“Derivatives\n(data/derivatives, tiles)”]
E –> F[“Web & Knowledge Graph\n(MapLibre, Neo4j, Google Earth)”]

<!-- END OF MERMAID -->


	•	Sources → JSON manifests (data/sources/*.json) define IDs, URLs, metadata ￼.
	•	Raw → Downloaded via make fetch; never committed directly (LFS/DVC pointers only).
	•	Processed → Open formats (GeoJSON, COG GeoTIFF, CSV); reproducible via ETL scripts.
	•	STAC → Indexed collections & items with spatial/temporal metadata ￼.
	•	Derivatives → Hillshades, slope/aspect, mosaics, statistical summaries.
	•	Tiles → Build-only tiles (z/x/y pyramids, PMTiles) for web/app previews ￼.

⸻

📦 Data Standards
	•	🌍 Vectors → GeoJSON (EPSG:4326 WGS84)
	•	🏔️ Rasters → Cloud-Optimized GeoTIFF (COG)
	•	⏳ Catalogs → STAC 1.0.0 (JSON) ￼
	•	📑 Metadata → JSON Schema validated, DCAT-compatible
	•	🔐 Integrity → .sha256 sidecars for all fetched & processed data

⸻

📜 Provenance & MCP Rules

Every dataset must include:
	•	✅ Manifest → data/sources/{id}.json with title, URL, license, spatial extent, temporal coverage.
	•	✅ Checksum → .sha256 file for every raw/processed artifact.
	•	✅ STAC Item → in data/stac/ with links to processed outputs.
	•	✅ License → Explicit license field in metadata (MIT, CC-BY, PD, etc.) ￼.
	•	✅ Docs → Contribution must update relevant README.md + changelog.

Rule: If it cannot be verified, reproduced, or cited → it does not belong in main/.

⸻

🔍 Example: Source Descriptor

{
  "id": "usgs_topo_larned_1894",
  "title": "USGS Historic Topographic Map — Larned (1894)",
  "type": "raster",
  "endpoint": {
    "type": "http",
    "urls": [
      "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/KS/Larned_1894.tif"
    ]
  },
  "spatial": { "bbox": [-99.25, 38.1, -98.75, 38.5], "crs": "EPSG:4326" },
  "temporal": { "start": "1894-01-01", "end": "1894-12-31" },
  "license": "Public Domain",
  "outputs": {
    "cog": "data/processed/overlays/usgs_topo_larned_1894.tif"
  }
}


⸻

🏛 Example Domains
	•	🌾 Land & Soils — SSURGO/STATSGO surveys, historic soil maps.
	•	🏔️ Terrain — LiDAR DEMs, USGS 3DEP, hillshades, slope/aspect.
	•	🌊 Hydrology — USGS NWIS streams, Kansas River flood maps.
	•	🌪️ Hazards — NOAA Storm Events, FEMA disaster declarations.
	•	📜 Cultural & History — Kansas Memory archives, treaties, newspapers ￼.
	•	🏹 Indigenous Data — Oral histories, land cession boundaries.

(See data/sources/ for full manifest set.)

⸻

⚠️ Notes
	•	Large files → managed via Git LFS or DVC; never checked into GitHub directly ￼.
	•	Ephemeral tiles → always rebuilt, never version-controlled (data/tiles/).
	•	Work & tmp → ignored by .gitignore; promote only important products.

⸻


<div align="center">


✅ In short: /data/ is the heart of the Kansas Frontier Matrix,
turning fragmented archives into traceable, reproducible, open science datasets.

</div>
```
