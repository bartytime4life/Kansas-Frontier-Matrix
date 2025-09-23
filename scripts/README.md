# Kansas-Frontier-Matrix — Scripts

This directory contains helper scripts that automate data ingestion, validation, and
site-building tasks for the **Kansas-Frontier-Matrix** stack.  
Scripts are designed to be **CLI-first**, modular, and reproducible — consistent with
the MCP Scientific Method templates [oai_citation:2‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6) and Knowledge Hub pipeline design [oai_citation:3‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## Objectives

- Automate **data ingestion** from external sources (TopoView, NOAA, USGS, etc.).
- Convert raw inputs (e.g., scanned maps, CSVs, shapefiles) into **structured STAC items**.
- Provide **quality checks** (checksums, schema validation).
- Support **reproducibility** in CI/CD (GitHub Actions, Makefile pipelines).
- Enable **multi-modal integration**: maps, hydrology, texts, oral histories [oai_citation:4‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).

---

## Layout

scripts/
├── topoview_fetch.py        # Fetches historic topo maps from USGS TopoView API
├── sync-roadmap.py          # Sync roadmap.yaml → GitHub Issues/Milestones
├── stac_validate.py         # STAC schema + MCP conformance checks
├── generate_checksums.sh    # SHA256/MD5 file integrity checks
├── ingest_texts.py          # (planned) OCR + NLP for historic texts
├── ingest_vectors.py        # (planned) Process treaty boundaries, trails, railroads
└── utils/                   # Shared helpers (logging, JSON, YAML parsers)

---

## Key Scripts

### `topoview_fetch.py`
- Reads a JSON source file (e.g. `data/sources/usgs_topoview.json`).
- Queries USGS TopoView API for historic topo maps within bbox/year range.
- Downloads TIFFs into `data/raw/`.
- Writes `README_topoview.txt` index + optional STAC items.

### `stac_validate.py`
- Runs schema validation for `catalog.json`, `collections/*.json`, `items/*.json`.
- Ensures IDs, bbox, datetime, and assets meet **STAC 1.0.0** rules.
- Integrates with **pytest** (`tests/test_stac.py`) for automated QA.

### `sync-roadmap.py`
- Pushes `.github/roadmap/roadmap.yaml` milestones/issues to GitHub.
- Ensures repo roadmap ↔ GitHub Projects stay in sync.

### `generate_checksums.sh`
- Produces `.sha256` and `.md5` files for large assets.
- Used in CI to verify downloads and processed outputs.

---

## Planned Scripts

- **`ingest_texts.py`** — OCR + NLP extraction from scanned diaries, letters, newspapers.
- **`ingest_vectors.py`** — ETL for treaty boundaries, PLSS grids, railroads, hydrology [oai_citation:5‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).
- **`ingest_hazards.py`** — Parse NOAA/FEMA datasets for floods, droughts, tornadoes [oai_citation:6‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).
- **`graph_linker.py`** — Link extracted entities/events into the Knowledge Graph [oai_citation:7‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## Usage

All scripts are CLI-friendly. From repo root:

```bash
# Fetch TopoView data
python scripts/topoview_fetch.py --source data/sources/usgs_topoview.json

# Validate STAC
python scripts/stac_validate.py stac/catalog.json

# Generate checksums
bash scripts/generate_checksums.sh data/cogs/dem/*.tif


⸻

Integration
	•	Makefile: Wraps common script tasks (e.g., make stac-validate, make fetch-topo).
	•	GitHub Actions: CI jobs call scripts for validation and site-builds.
	•	Knowledge Hub: Outputs (STAC, JSON, CSV) are ingested into the historical knowledge graph ￼.
	•	Google Earth / Web UI: Validated STAC items feed into MapLibre/KML time sliders.

⸻

Notes
	•	Keep dependencies minimal (stdlib + requests, pandas, pyyaml, shapely).
	•	Prefer Python for ingestion/ETL, Bash for small utilities.
	•	Follow MCP reproducibility: log outputs, checksums, metadata.
	•	Scripts should fail fast with clear error messages, and skip gracefully when inputs are absent.

⸻
