Here it is, rebuilt clean so it renders in GitHub (no smart separators, proper fences, working Mermaid, plain ASCII labels).

<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Data (`/data/`)

**Mission:** Store, organize, and version-control all datasets powering the  
Kansas Frontier Matrix knowledge hub — maps, rasters, vectors, documents, and tables.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)

</div>

---

## Purpose

- Central hub for all project data assets  
- Ensures reproducibility (Makefile-driven ETL)  
- Enforces provenance rules (checksums, metadata, schemas)  
- Feeds the map, timeline, and knowledge graph

---

## Layout

```bash
data/
├── sources/       # JSON manifests for external datasets (URLs, metadata, licenses)
├── raw/           # Fetched raw files (Git LFS/DVC pointers only, never pushed)
├── processed/     # Normalized open formats (GeoJSON, COGs, CSVs)
├── stac/          # STAC catalog (collections & items JSON)
├── derivatives/   # Computed layers (hillshade, slope, mosaics, stats)
├── tiles/         # Ephemeral web tiles (PMTiles, MBTiles)
├── work/          # Scratch/workspace for pipelines
└── tmp/           # Build leftovers, ignored by Git


⸻

Data Lifecycle

flowchart TD
  A[SOURCES manifests and APIs] --> B[RAW data/raw]
  B --> C[ETL data/processed]
  C --> D[STAC data/stac]
  D --> E[DERIVATIVES data/derivatives tiles]
  E --> F[WEB and Knowledge Graph]

	•	Sources → JSON manifests (data/sources/*.json) define IDs, URLs, metadata
	•	Raw → Downloaded via make fetch; never committed directly (LFS/DVC pointers only)
	•	Processed → Open formats (GeoJSON, COG GeoTIFF, CSV); reproducible via ETL scripts
	•	STAC → Indexed collections and items with spatial/temporal metadata
	•	Derivatives → Hillshades, slope/aspect, mosaics, statistics
	•	Tiles → Build-only tiles (z/x/y pyramids, PMTiles) for web/app previews

⸻

Standards
	•	Vectors → GeoJSON (EPSG:4326 WGS84)
	•	Rasters → Cloud-Optimized GeoTIFF (COG)
	•	Catalogs → STAC 1.0.0
	•	Metadata → JSON Schema, DCAT-compatible
	•	Integrity → .sha256 for every artifact

⸻

Provenance Rules

Every dataset must include:
	•	Manifest → data/sources/{id}.json (title, URL, license, extent, temporal)
	•	Checksum → .sha256 for raw and processed artifacts
	•	STAC Item → in data/stac/ with links to processed outputs
	•	Explicit license (MIT, CC-BY, Public Domain, etc.)
	•	Docs updated (README.md, changelog)

If it cannot be verified, reproduced, or cited → it does not go in main/.

⸻

Example Manifest

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

Example Domains
	•	Land and Soils → SSURGO, STATSGO, historic soil maps
	•	Terrain → LiDAR DEMs, USGS 3DEP, slope/aspect
	•	Hydrology → USGS NWIS, Kansas River floods
	•	Hazards → NOAA Storm Events, FEMA disasters
	•	Cultural and History → Kansas Memory, treaties, newspapers
	•	Indigenous Data → Oral histories, land cessions

⸻

Notes
	•	Large files → use Git LFS or DVC; do not commit binaries
	•	Tiles → ephemeral, always rebuilt
	•	work/ and tmp/ → ignored by Git

⸻


If you want, I’ll apply the same “safe Mermaid” fix across your other docs so you don’t hit this again anywhere.
