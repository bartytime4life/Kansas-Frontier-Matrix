<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Data (`/data/`)

**Mission:** Store, organize, and version-control all datasets powering the  
Kansas Frontier Matrix knowledge hub — maps, rasters, vectors, documents, and tables.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)  
[![MCP Protocol](https://img.shields.io/badge/Docs-MCP%20Aligned-green)](../docs/)  

</div>

---

## 📚 Purpose

- Central hub for **all project data assets**.  
- Ensures **reproducibility** (Makefile-driven ETL).  
- Enforces **MCP provenance rules** (checksums, metadata, schemas).  
- Feeds the **map + timeline + knowledge graph**.  

---

## 📂 Layout

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

🧰 Data Lifecycle

flowchart TD
  A["Sources<br/>manifests & APIs"] --> B["Raw<br/>(data/raw)"]
  B --> C["Processing & ETL<br/>(data/processed)"]
  C --> D["STAC Catalog<br/>(data/stac)"]
  D --> E["Derivatives<br/>(data/derivatives, tiles)"]
  E --> F["Web and Knowledge Graph"]

	•	Sources → JSON manifests (data/sources/*.json) define IDs, URLs, metadata.
	•	Raw → Downloaded via make fetch; never committed directly (LFS/DVC pointers only).
	•	Processed → Open formats (GeoJSON, COG GeoTIFF, CSV); reproducible via ETL scripts.
	•	STAC → Indexed collections & items with spatial/temporal metadata.
	•	Derivatives → Hillshades, slope/aspect, mosaics, statistical summaries.
	•	Tiles → Build-only tiles (z/x/y pyramids, PMTiles) for web/app previews.

⸻

📦 Standards
	•	🌍 Vectors → GeoJSON (EPSG:4326 WGS84)
	•	🏔️ Rasters → Cloud-Optimized GeoTIFF (COG)
	•	⏳ Catalogs → STAC 1.0.0
	•	📑 Metadata → JSON Schema, DCAT-compatible
	•	🔐 Integrity → .sha256 for every artifact

⸻

📜 Provenance Rules

Every dataset must include:
	•	✅ Manifest → data/sources/{id}.json (title, URL, license, extent, temporal).
	•	✅ Checksum → .sha256 for raw + processed.
	•	✅ STAC Item → in data/stac/.
	•	✅ Explicit license (MIT, CC-BY, PD, etc.).
	•	✅ Docs updated (README.md, changelog).

If it can’t be verified, reproduced, or cited → it does not go in main/.

⸻

🔍 Example Manifest

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
	•	🌾 Land & Soils → SSURGO, STATSGO, historic soil maps
	•	🏔️ Terrain → LiDAR DEMs, USGS 3DEP, slope/aspect
	•	🌊 Hydrology → USGS NWIS, Kansas River floods
	•	🌪️ Hazards → NOAA Storm Events, FEMA disasters
	•	📜 Cultural & History → Kansas Memory, treaties, newspapers
	•	🏹 Indigenous Data → Oral histories, land cessions

⸻

⚠️ Notes
	•	Large files → use Git LFS / DVC, never commit binaries.
	•	Tiles → ephemeral, always rebuilt.
	•	work/ + tmp/ → ignored by Git.

⸻


<div align="center">


✅ /data/ is the engine room of Kansas Frontier Matrix —
turning scattered archives into traceable, reproducible, open datasets.

</div>
```
