<div align="center">

# 🛠️ Kansas Frontier Matrix — **Tools**  
`/tools/`

**Utility Scripts · Data Pipelines · Validation & Deployment Helpers**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../.github/workflows/tests.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../docs/)

</div>

---

```yaml
---
title: "KFM • Tools (tools/)"
version: "v1.5.0"
last_updated: "2025-10-14"
owners: ["@kfm-data", "@kfm-engineering"]
tags: ["tools","scripts","automation","validation","stac","neo4j","mcp"]
license: "MIT"
semantic_alignment:
  - STAC 1.0
  - PROV-O (Provenance Tracking)
  - FAIR Principles (Data Reproducibility)
---
````

---

## 🎯 Mission

The `/tools/` directory provides **scripts, utilities, and helper programs** that automate and validate core workflows across the **Kansas Frontier Matrix (KFM)** project.

These tools are **not production dependencies**, but they are **mission-critical for reproducibility** — enabling data ingestion, processing, validation, and deployment under **Master Coder Protocol (MCP-DL v6.2)** principles.

> **Guiding Principle:** Every helper is deterministic, documented, and leaves a provenance trail.

---

## 🧱 Directory Structure

```text
tools/
├── fetch_data.py         # Fetch raw datasets from data/sources/*.json manifests
├── convert_gis.py        # Convert shapefiles/rasters → GeoJSON / COG GeoTIFF
├── validate_stac.py      # Validate STAC collections/items via JSON Schema
├── checksum.py           # Generate/verify SHA-256 provenance sidecars
├── migrate_graph.py      # Load ETL outputs into Neo4j (batched Cypher inserts)
├── build_config.py       # Regenerate web/config/*.json from STAC metadata
├── notebooks/            # Jupyter notebooks (prototyping, exploratory analysis)
└── utils/                # Shared helper modules (logging, config, constants)
```

---

## ⚙️ Core Utilities

### `fetch_data.py`

* Reads dataset manifests (`data/sources/*.json`)
* Fetches remote data via HTTP, REST, or ArcGIS APIs
* Stores outputs in `data/raw/`
* Logs provenance (URL, timestamp, checksum)

### `convert_gis.py`

* Converts raw GIS data into open formats:

  * Vector → **GeoJSON**
  * Raster → **COG GeoTIFF**
* Reprojects to **EPSG:4326 (WGS84)**
* Uses **GDAL / rasterio / pyproj**

### `validate_stac.py`

* Validates **STAC 1.0 Items** and Collections
* Ensures metadata completeness and schema compliance
* Outputs CI validation reports and JSON summaries

### `checksum.py`

* Computes and verifies **SHA-256** integrity checks for all raw and processed files
* Used for provenance assurance and reproducible builds

### `migrate_graph.py`

* Imports processed datasets into the **Neo4j knowledge graph**
* Uses batch Cypher inserts
* De-duplicates entities via alias matching and provenance links

### `build_config.py`

* Regenerates `web/config/app.config.json` and `web/config/layers.json`
* Extracts STAC metadata for direct use by the frontend web UI
* Guarantees synchronization between data backend and visualization layers

---

## 🚀 Usage

All workflows can be executed directly or orchestrated via the **Makefile**.

```bash
# Fetch external datasets
make fetch

# Convert raw GIS to open formats
make convert

# Validate STAC metadata
make stac-validate

# Verify checksums
make checksums

# Load data into Neo4j
make graph-migrate

# Rebuild web configurations
make site-config
```

**Direct CLI Usage Example:**

```bash
python tools/fetch_data.py --source data/sources/usgs_topo.json
python tools/convert_gis.py input.shp output.geojson
python tools/validate_stac.py data/stac/items/*
```

---

## 🧩 Integration Workflow

| Stage              | Consumes              | Produces            | Downstream          |
| :----------------- | :-------------------- | :------------------ | :------------------ |
| `fetch_data.py`    | `data/sources/*.json` | `data/raw/`         | `convert_gis.py`    |
| `convert_gis.py`   | Raw files             | `data/processed/`   | `validate_stac.py`  |
| `validate_stac.py` | Processed files       | Validation reports  | CI / Build Pipeline |
| `checksum.py`      | Raw + Processed       | `.sha256` files     | Provenance Audits   |
| `migrate_graph.py` | Processed data        | Neo4j nodes/edges   | API / Frontend      |
| `build_config.py`  | STAC metadata         | Web UI config JSONs | `web/config/`       |

---

## 🧪 Testing & CI Integration

* **Unit Tests:** `tests/tools/` executed via **pytest**
* **Pre-commit Hooks:** Enforce linting (`ruff`, `black`), YAML/JSON schema validation
* **CI Workflows:** Each tool exercised in `tests.yml` with fixture datasets
* **Artifacts:** Validation reports and checksum logs stored in CI build artifacts

All tools support `--dry-run`, `--verbose`, and `--output` flags for safe experimentation.

---

## 🧱 Example End-to-End Workflow

```bash
# 1. Fetch & verify source data
make fetch checksums

# 2. Convert GIS formats (COG, GeoJSON)
make convert

# 3. Validate STAC compliance
make stac-validate

# 4. Load to knowledge graph and rebuild configs
make graph-migrate site-config
```

Each stage emits structured logs and SHA-verified artifacts for traceable, reproducible processing.

---

## 🧠 Development Guidelines

Every script must:

1. Include a clear **docstring** and CLI help (`-h` / `--help`).
2. **Log all actions** with timestamps and output summaries.
3. Use **only open-source, actively maintained libraries** (`requests`, `rasterio`, `pystac`, `GDAL`, etc.).
4. Be **modular** — importable as a library for pipelines (`from tools import ...`).
5. Produce **deterministic outputs**; identical inputs must yield identical hashes.
6. Write **structured logs** to `logs/{tool_name}.log` for provenance tracking.

> Larger or experimental workflows must first live in `/tools/notebooks/` before production inclusion.

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                    |
| :--------------- | :------------------------------------------------------------- |
| **Inputs**       | Dataset manifests, raw data files, STAC metadata               |
| **Outputs**      | Processed datasets, provenance checksums, config JSONs         |
| **Dependencies** | Python 3.11+, GDAL, rasterio, pystac, neo4j-driver             |
| **Integrity**    | Verified through CI logs, STAC validation, and checksum audits |
| **Traceability** | Each execution stores operation logs and SHA256 signatures     |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                           |
| :------------------ | :------------------------------------------------------- |
| Documentation-first | Every tool documented with docstrings + README reference |
| Reproducibility     | Deterministic execution verified via checksum validation |
| Provenance          | Input/output tracking with SHA-256 sidecars              |
| Open Standards      | STAC 1.0, GeoJSON, EPSG:4326                             |
| Auditability        | CI workflows archive validation and checksum logs        |
| Accessibility       | CLI help, verbose logging, and config-driven operation   |

---

## 🔗 Related Documentation

* **Data Ingestion Pipeline** — `data/README.md`
* **STAC Catalog Overview** — `data/stac/README.md`
* **Web Configuration** — `web/config/README.md`
* **Monorepo Repository Design** — `docs/monorepo/README.md`

---

## 📜 License

Released under the **MIT License**.
© 2025 Kansas Frontier Matrix — developed under **MCP-DL v6.2** for traceable, automated, and reproducible data engineering.

> *“Tools are not throwaways — they are first-class citizens of reproducibility.”*
> *Automation with integrity — every helper leaves a trail.*

```
```
