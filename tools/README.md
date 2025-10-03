<div align="center">

# 🛠️ Kansas Frontier Matrix — Tools (`/tools/`)

**Mission:** Provide **utility scripts and helper tools** that support  
data ingestion, processing, validation, and deployment workflows  
across the Kansas Frontier Matrix (KFM) project.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../.github/workflows/tests.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)  

</div>

---

## 🎯 Purpose

The `/tools/` directory contains **scripts, utilities, and helper programs**  
that are not part of the deployed core system but are essential for:  

- 🗂️ **Data management** — fetching, converting, and validating datasets.  
- 🧪 **Testing & validation** — schema checks, STAC compliance, and CI helpers.  
- 🚀 **Automation** — build/deploy utilities and Makefile helpers.  
- 🧭 **Exploration** — quick analysis, Jupyter notebooks, or migration helpers.  

All tools follow **Master Coder Protocol (MCP)**: documented, reproducible, and transparent.  

---

## 📚 Structure

```text
tools/
├── fetch_data.py         # Fetch raw datasets using source descriptors
├── convert_gis.py        # Convert shapefiles/rasters → GeoJSON/COG GeoTIFF
├── validate_stac.py      # Validate STAC collections/items against schemas
├── checksum.py           # Generate/verify SHA-256 provenance sidecars
├── migrate_graph.py      # Load/update entities in Neo4j from ETL outputs
├── build_config.py       # Regenerate app.config.json and layers.json
├── notebooks/            # Jupyter notebooks for exploration / prototyping
└── utils/                # Shared Python utilities (logging, config, helpers)


⸻

⚙️ Key Tools

fetch_data.py
	•	Reads data/sources/*.json manifests.
	•	Downloads referenced files (via HTTP, API, or ArcGIS REST).
	•	Stores raw files in data/raw/.

convert_gis.py
	•	Converts GIS datasets to open formats:
	•	Vector → GeoJSON
	•	Raster → Cloud-Optimized GeoTIFF (COG)
	•	Reprojects to WGS84 (EPSG:4326) for consistency.

validate_stac.py
	•	Runs JSON Schema + STAC 1.0.0 validation.
	•	Ensures every item in data/stac/ is compliant before CI/CD passes.

checksum.py
	•	Creates .sha256 files for all raw and processed data.
	•	Verifies checksums to guarantee provenance integrity.

migrate_graph.py
	•	Loads processed ETL outputs into the Neo4j knowledge graph.
	•	Uses Cypher transactions for batch inserts.
	•	Prevents duplicate entities by fuzzy-matching names/aliases.

build_config.py
	•	Rebuilds frontend configs (app.config.json, layers.json).
	•	Sources metadata from data/stac/ collections.
	•	Ensures web UI stays synchronized with the latest datasets.

⸻

🚀 Usage

Typical workflows are orchestrated via Makefile targets.

# Fetch all external datasets
make fetch

# Convert raw GIS → open formats
make convert

# Validate STAC catalog compliance
make stac-validate

# Verify checksums
make checksums

# Migrate data into Neo4j graph
make graph-migrate

# Rebuild web UI configs
make site-config

For ad-hoc usage, run tools directly:

python tools/fetch_data.py --source data/sources/usgs_topo.json
python tools/convert_gis.py input.shp output.json
python tools/validate_stac.py data/stac/items/*


⸻

🧭 Guidelines
	•	Every tool must:
	•	Be documented with inline comments.
	•	Support CLI help (-h/--help).
	•	Log actions to stdout (and optionally to a provenance log).
	•	Prefer open libraries (GDAL, rasterio, pyproj, pystac).
	•	Small, reusable modules → importable by other scripts.
	•	Long-term or experimental workflows → put in notebooks/ and migrate later.

⸻


<div align="center">


🔗 Tools are not throwaways — they are first-class,
documented, and reproducible under MCP standards.

</div>
```