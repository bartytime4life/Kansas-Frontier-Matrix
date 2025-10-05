<div align="center">

# 🛠️ Kansas Frontier Matrix — Tools (`/tools/`)

**Mission:** Provide **utility scripts and helper tools** that support  
data ingestion, processing, validation, and deployment workflows  
across the Kansas Frontier Matrix (KFM) project.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../.github/workflows/tests.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)

</div>

---

## 🎯 Purpose

The `/tools/` directory contains **scripts, utilities, and helper programs**  
that are not part of the deployed production stack but are **essential** for:

- 🗂️ **Data management** — fetching, converting, validating datasets.  
- 🧪 **Testing & validation** — schema checks, STAC compliance, CI helpers.  
- 🚀 **Automation** — build/deploy utilities and Makefile helpers.  
- 🧭 **Exploration** — Jupyter notebooks or quick-analysis scripts.  

> All utilities follow the **Master Coder Protocol (MCP)** — every operation is reproducible, documented, and provenance-logged.

---

## 📚 Structure

```text
tools/
├── fetch_data.py       # Fetch raw datasets from data/sources/*.json
├── convert_gis.py      # Convert shapefiles/rasters → GeoJSON/COG GeoTIFF
├── validate_stac.py    # Validate STAC collections/items via JSON Schema
├── checksum.py         # Generate / verify SHA-256 provenance sidecars
├── migrate_graph.py    # Load ETL outputs into Neo4j (batch Cypher inserts)
├── build_config.py     # Regenerate app.config.json & layers.json for web UI
├── notebooks/          # Jupyter notebooks (exploration / prototypes)
└── utils/              # Shared helper modules (logging, config, etc.)
````

---

## ⚙️ Key Tools

### `fetch_data.py`

* Reads `data/sources/*.json` manifests.
* Downloads referenced files (HTTP, REST, ArcGIS API).
* Writes raw outputs to `data/raw/`.

### `convert_gis.py`

* Converts GIS datasets to open formats:

  * Vector → **GeoJSON**
  * Raster → **COG GeoTIFF**
* Reprojects to **WGS84 (EPSG:4326)** for consistency.

### `validate_stac.py`

* Runs JSON Schema + STAC 1.0 validation.
* Ensures every STAC Item in `data/stac/` passes compliance checks.

### `checksum.py`

* Generates `.sha256` files for all raw/processed assets.
* Verifies integrity before ingestion or publish.

### `migrate_graph.py`

* Loads processed ETL outputs into the **Neo4j knowledge graph**.
* Uses batched Cypher transactions; skips duplicate entities via alias matching.

### `build_config.py`

* Rebuilds `app.config.json` and `layers.json` for the web app.
* Pulls metadata from the STAC catalog; keeps the UI in sync with datasets.

---

## 🚀 Usage

Typical workflows are orchestrated via **Makefile** targets.

```bash
# Fetch all external datasets
make fetch

# Convert raw GIS → open formats
make convert

# Validate STAC catalog
make stac-validate

# Verify checksums
make checksums

# Migrate data into Neo4j
make graph-migrate

# Rebuild web UI configs
make site-config
```

For ad-hoc runs:

```bash
python tools/fetch_data.py --source data/sources/usgs_topo.json
python tools/convert_gis.py input.shp output.json
python tools/validate_stac.py data/stac/items/*
```

---

## 🧭 Development Guidelines

Every tool must:

1. Include **inline docstrings** and CLI help (`-h/--help`).
2. **Log** actions to stdout and optional provenance logs.
3. Use open, well-maintained libraries (`requests`, `rasterio`, `pyproj`, `pystac`, `GDAL`).
4. Remain **importable** as a module (`from tools import ...`) for pipeline reuse.
5. Follow MCP structure → clear inputs / outputs, deterministic results.
6. Large or experimental workflows → keep under `notebooks/` until production-ready.

---

## 🧩 Integration Points

| Stage              | Consumes              | Produces            | Downstream         |
| ------------------ | --------------------- | ------------------- | ------------------ |
| `fetch_data.py`    | `data/sources/*.json` | `data/raw/`         | `convert_gis.py`   |
| `convert_gis.py`   | raw files             | `data/processed/`   | `validate_stac.py` |
| `validate_stac.py` | processed files       | validation logs     | CI checks / build  |
| `checksum.py`      | raw + processed       | `.sha256`           | provenance audits  |
| `migrate_graph.py` | processed CSV/JSON    | Neo4j nodes/edges   | API / frontend     |
| `build_config.py`  | `data/stac/`          | `web/config/*.json` | Web UI             |

---

## 🧪 Testing & CI Hooks

* **Unit tests:** under `tests/tools/`, executed by `pytest`.
* **Pre-commit hooks:** lint (ruff/black), YAML schema checks.
* **CI:** each tool exercised in GitHub Actions (`tests.yml`) with sample manifests.
* **Logs:** CI artifacts include validation and checksum reports.

---

## 🧱 Example Workflow (End-to-End)

```bash
# 1. Fetch & verify data
make fetch checksums

# 2. Convert → COG / GeoJSON
make convert

# 3. Validate STAC metadata
make stac-validate

# 4. Migrate graph + rebuild configs
make graph-migrate site-config
```

All steps are traceable via generated `.sha256` and STAC provenance.

---

<div align="center">

🧩 *Tools are not throwaways — they are first-class, documented, and reproducible under MCP standards.*
✨ *Automation with integrity — every helper leaves a trail.* ✨

</div>
