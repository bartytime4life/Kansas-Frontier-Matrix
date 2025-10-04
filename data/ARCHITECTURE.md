<div align="center">

# 🧱 Kansas Frontier Matrix — Data Architecture  
`data/ARCHITECTURE.md`

**Mission:** Define the **end-to-end data architecture** of the Kansas Frontier Matrix (KFM) —  
detailing how raw inputs are transformed, validated, documented, and visualized within a fully reproducible,  
STAC-compliant, and MCP-governed data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix Data Architecture** governs the structure, flow,  
and governance of all data within the repository — from acquisition and validation  
to metadata generation and web visualization.

It ensures that every dataset:
- Is **traceable** from its source manifest to its STAC metadata.  
- Follows **reproducible** ETL and validation workflows.  
- Is **auditable** through checksums, provenance logs, and MCP documentation.  
- Adheres to **open standards** for interoperability and accessibility.  

This document provides a **high-level blueprint** of the data subsystem and its lifecycle within KFM.

---

## 🗺️ Data Architecture Overview

```mermaid
flowchart TD
  A["🌐 External Sources\n(data/sources/)"] --> B["📦 Raw Data\n(data/raw/)"]
  B --> C["⚙️ ETL Processing & Cleaning\n(src/pipelines/)"]
  C --> D["✅ Processed Data\n(data/processed/)"]
  D --> E["🧩 Metadata & STAC\n(data/processed/metadata/, data/stac/)"]
  E --> F["🧾 Checksums & Validation\n(data/checksums/)"]
  F --> G["🌎 Web & Visualization Layers\n(data/tiles/, web/config/, web/app.js)"]

  style A fill:#f8f9fa,stroke:#888
  style B fill:#f0f8ff,stroke:#0088cc
  style C fill:#fff0f5,stroke:#cc0088
  style D fill:#e8fff0,stroke:#33aa33
  style E fill:#faf5e6,stroke:#e8a500
  style F fill:#f0e8ff,stroke:#7d33aa
  style G fill:#f7f7f7,stroke:#333
````

<!-- END OF MERMAID -->

---

## 🧩 Data Lifecycle Stages

| Stage                       | Directory                                | Purpose                                                         | Key Artifacts                     |
| :-------------------------- | :--------------------------------------- | :-------------------------------------------------------------- | :-------------------------------- |
| **1. Source Registration**  | `data/sources/`                          | Defines dataset origins, access methods, and licensing.         | JSON manifests (`*.json`)         |
| **2. Raw Acquisition**      | `data/raw/`                              | Stores unmodified data as acquired from sources.                | Raw files (COGs, CSVs, NetCDFs)   |
| **3. ETL Processing**       | `src/pipelines/`                         | Transforms, cleans, and standardizes data for analysis.         | Python scripts, logs              |
| **4. Processed Data**       | `data/processed/`                        | Houses validated and cleaned data, ready for publication.       | GeoTIFF, GeoJSON, CSV, JSONL      |
| **5. Metadata & STAC**      | `data/processed/metadata/`, `data/stac/` | Describes dataset provenance, structure, and temporal coverage. | STAC Items & Collections          |
| **6. Integrity Validation** | `data/checksums/`                        | Provides SHA-256 hashes for reproducibility verification.       | `.sha256` hash files              |
| **7. Visualization**        | `data/tiles/`, `web/config/`             | Hosts pre-rendered tiles and viewer configurations.             | Raster/vector tiles, JSON configs |

---

## ⚙️ ETL Pipeline Architecture

The KFM ETL (Extract, Transform, Load) system operates as a **deterministic, domain-driven pipeline**
powered by Makefiles and modular Python scripts under `src/pipelines/`.

### 🧱 Pipeline Modules

| Domain        | Pipeline Script         | Output Directory            | Description                                 |
| :------------ | :---------------------- | :-------------------------- | :------------------------------------------ |
| **Terrain**   | `terrain_pipeline.py`   | `data/processed/terrain/`   | DEM, hillshade, slope/aspect generation     |
| **Hydrology** | `hydrology_pipeline.py` | `data/processed/hydrology/` | River, watershed, flood modeling            |
| **Landcover** | `landcover_pipeline.py` | `data/processed/landcover/` | NLCD, vegetation, land use                  |
| **Climate**   | `climate_pipeline.py`   | `data/processed/climate/`   | Precipitation, temperature, drought indices |
| **Hazards**   | `hazards_pipeline.py`   | `data/processed/hazards/`   | Tornado, wildfire, and flood layers         |
| **Tabular**   | `tabular_pipeline.py`   | `data/processed/tabular/`   | Census, agricultural, and economic data     |
| **Text**      | `text_pipeline.py`      | `data/processed/text/`      | OCR, NLP, and transcript datasets           |

Each pipeline:

* Fetches data from `data/sources/`
* Logs all processing steps to `data/work/logs/`
* Writes intermediate artifacts to `data/work/tmp/`
* Generates checksums in `data/checksums/`
* Produces metadata in `data/processed/metadata/`

---

## 🧮 Validation & Integrity Architecture

Validation ensures that **all data products** meet reproducibility and consistency standards.

| Component             | Function                                                             | Tooling                            |
| :-------------------- | :------------------------------------------------------------------- | :--------------------------------- |
| **Checksums**         | SHA-256 hashes verify file integrity across rebuilds.                | `hashlib`, Makefile tasks          |
| **Schema Validation** | JSON Schema ensures metadata and source manifests meet requirements. | `jsonschema`, `stac-validator`     |
| **STAC Compliance**   | Ensures catalog structure follows STAC 1.0.0 specification.          | GitHub Action: `stac-validate.yml` |
| **CI/CD Workflows**   | Automated validation for every dataset addition or modification.     | GitHub Actions                     |
| **Manual Review**     | Peer verification for critical datasets or major updates.            | MCP peer review protocol           |

---

## 🧠 Provenance Tracking

Provenance in KFM follows a **source → raw → processed → metadata → visualization** chain.

Each dataset is tracked by:

* **Source Manifest** (`data/sources/*.json`)
* **Checksum File** (`data/checksums/<domain>/*.sha256`)
* **STAC Item** (`data/stac/<domain>/*.json`)
* **Processing Log** (`data/work/logs/*.log`)
* **ETL Script Reference** (`src/pipelines/<domain>_pipeline.py`)

Together, these ensure that every product is **auditable, reproducible, and transparent**.

---

## 🧩 Integration with the MCP Framework

KFM’s data architecture fully adheres to **Master Coder Protocol (MCP)** standards:

| MCP Principle           | Implementation                                                                |
| :---------------------- | :---------------------------------------------------------------------------- |
| **Documentation-first** | Every data stage includes a README and structured metadata.                   |
| **Reproducibility**     | Deterministic ETL and checksum validation ensure consistency.                 |
| **Open Standards**      | STAC 1.0.0, GeoTIFF (COG), GeoJSON, NetCDF, CSV.                              |
| **Provenance**          | Source manifests, STAC links, and logs document full lineage.                 |
| **Auditability**        | CI/CD logging, peer validation, and hash verification guarantee transparency. |

---

## 🧩 CI/CD Data Governance

GitHub Actions workflows automate validation, documentation, and reproducibility checks:

| Workflow            | Purpose                                            | Trigger             |
| :------------------ | :------------------------------------------------- | :------------------ |
| `fetch.yml`         | Downloads new raw data based on source manifests.  | On push or schedule |
| `stac-validate.yml` | Validates STAC catalog structure and links.        | On PR or commit     |
| `checksums.yml`     | Recomputes and verifies all SHA-256 checksums.     | On data update      |
| `site.yml`          | Builds documentation and deploys data viewer site. | On main branch push |

Logs for these workflows are stored under `data/work/logs/`.

---

## 🧱 Architectural Philosophy

KFM’s architecture is built on three principles:

1. **Transparency:**
   Every dataset must have a clear, documented lineage — from acquisition to publication.

2. **Reproducibility:**
   Every data transformation is deterministic and scriptable, ensuring consistent rebuilds.

3. **Interoperability:**
   Every file format, metadata schema, and workflow must comply with open standards.

---

## 📎 Related Documentation

| Path                     | Description                               |
| :----------------------- | :---------------------------------------- |
| `data/README.md`         | General overview of all data directories. |
| `data/sources/README.md` | Source manifests and provenance registry. |
| `data/stac/README.md`    | STAC catalog and metadata integration.    |
| `docs/architecture/`     | High-level project architecture overview. |
| `src/pipelines/`         | ETL and transformation pipelines.         |

---

## 📅 Version History

| Version | Date       | Summary                                                                        |
| :------ | :--------- | :----------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial data architecture documentation covering source-to-visualization flow. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Data Without Mystery: Every Byte Proven, Every Layer Reproducible.”*
📍 [`data/ARCHITECTURE.md`](.) · Blueprint for the data subsystem within the Kansas Frontier Matrix.

</div>
