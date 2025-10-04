<div align="center">

# 🧱 Kansas Frontier Matrix — Data Architecture  
`docs/architecture/data-architecture.md`

**Mission:** Describe the full **data subsystem architecture** of the Kansas Frontier Matrix (KFM) —  
detailing how datasets flow through acquisition, transformation, validation, cataloging, and visualization  
in a fully reproducible, provenance-tracked, and open-standard framework.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The **data architecture** of the Kansas Frontier Matrix (KFM) defines how **scientific, historical, and spatial data**  
are stored, versioned, validated, and published under the **Master Coder Protocol (MCP)**.

This subsystem ensures that every dataset is:

- 📜 **Documented** — every directory includes a README and manifest  
- 🔁 **Reproducible** — deterministic pipelines recreate identical outputs  
- 🧾 **Auditable** — integrity verified by automated checksums and STAC validation  
- 🧠 **Provenant** — each product traceable to its source manifest  
- 🌍 **Interoperable** — compliant with STAC 1.0.0 and open geospatial standards  

Together, these principles make KFM a **self-verifying data ecosystem**.

---

## 🧩 Data System Layers

```mermaid
flowchart TD
  A["🌐 External Data Sources\n(data/sources/)"] --> B["📦 Raw Data Storage\n(data/raw/)"]
  B --> C["⚙️ ETL & Transformation\n(src/pipelines/)"]
  C --> D["✅ Processed Datasets\n(data/processed/)"]
  D --> E["🧩 Metadata & STAC Records\n(data/processed/metadata/, data/stac/)"]
  E --> F["🔐 Checksum Verification\n(data/checksums/)"]
  F --> G["🌎 Visualization & Publication\n(data/tiles/, web/, docs/)"]
````

<!-- END OF MERMAID -->

---

## 🧱 Data Architecture Components

| Layer                       | Directory                                | Description                                                                      | Standards                          |
| :-------------------------- | :--------------------------------------- | :------------------------------------------------------------------------------- | :--------------------------------- |
| **Source Registry**         | `data/sources/`                          | JSON manifests describing dataset origin, licensing, and access methods.         | JSON Schema                        |
| **Raw Data Archive**        | `data/raw/`                              | Immutable copies of original datasets for traceability.                          | Original file formats              |
| **ETL Pipelines**           | `src/pipelines/`                         | Python modules and Makefile targets for extraction, transformation, and loading. | MCP Workflow Spec                  |
| **Processed Data Store**    | `data/processed/`                        | Cleaned and validated datasets ready for downstream integration.                 | GeoTIFF, GeoJSON, CSV, JSONL       |
| **Metadata & STAC Catalog** | `data/stac/`, `data/processed/metadata/` | STAC 1.0.0 Items & Collections describing data assets and provenance.            | STAC, JSON Schema                  |
| **Checksum Verification**   | `data/checksums/`                        | SHA-256 files ensuring reproducibility and data immutability.                    | FIPS 180-4 SHA-2                   |
| **Web Visualization**       | `data/tiles/`, `web/`                    | Raster and vector tiles served to web viewers for interactive exploration.       | Mapbox Vector Tile, COG, EPSG:3857 |

---

## ⚙️ Data Flow Summary

| Stage                        | Input                       | Output                     | Key Process                                | Validation                        |
| :--------------------------- | :-------------------------- | :------------------------- | :----------------------------------------- | :-------------------------------- |
| **1️⃣ Acquisition**          | `data/sources/`             | `data/raw/`                | Fetch via API, FTP, or static download     | License and schema validation     |
| **2️⃣ ETL Transformation**   | `data/raw/`                 | `data/processed/`          | Cleaning, reprojection, subsetting         | Pipeline logs (`data/work/logs/`) |
| **3️⃣ Metadata Generation**  | `data/processed/`           | `data/processed/metadata/` | Create STAC items and provenance JSON      | STAC JSON Schema                  |
| **4️⃣ Integrity Validation** | `data/processed/`           | `data/checksums/`          | Compute SHA-256 hashes                     | Automated checksum comparison     |
| **5️⃣ Publication**          | `data/stac/`, `data/tiles/` | `web/`, `docs/`            | Render maps, dashboards, and documentation | CI/CD deployment logs             |

---

## 🧮 Domain Data Model (Collections)

| Domain        | Primary Datasets                            | Format           | Temporal Scope | Spatial Scope          |
| :------------ | :------------------------------------------ | :--------------- | :------------- | :--------------------- |
| **Terrain**   | DEM, hillshade, slope/aspect                | GeoTIFF (COG)    | 2018–2020      | Statewide              |
| **Hydrology** | NHD flowlines, watersheds, flood zones      | GeoJSON          | 1900–2025      | Major river basins     |
| **Landcover** | NLCD, vegetation, crop data                 | GeoTIFF          | 1992–2021      | Statewide              |
| **Climate**   | Temperature, precipitation, drought indices | NetCDF, GeoTIFF  | 1980–2025      | Statewide              |
| **Hazards**   | Tornado, flood, wildfire datasets           | GeoJSON, GeoTIFF | 1950–2025      | Kansas and regional    |
| **Tabular**   | Census, economic, agricultural stats        | CSV, Parquet     | 1860–2025      | County and state level |
| **Text**      | OCR text, oral histories, treaties          | JSONL, TXT       | 1800–present   | Historical archives    |

---

## 🧾 STAC & Metadata Linkage

Each processed dataset has a **one-to-one** relationship between:

1. **Source Manifest** — `data/sources/<domain>/<dataset>.json`
2. **Processed Dataset** — `data/processed/<domain>/<dataset>.<ext>`
3. **Checksum Record** — `data/checksums/<domain>/<dataset>.<ext>.sha256`
4. **STAC Item** — `data/stac/<domain>/<dataset>.json`
5. **Thumbnail / Preview** — `data/processed/metadata/<domain>/thumbnails/<dataset>.png`

This ensures full **traceability** and **data lineage**.

---

## 🔐 Data Integrity & Validation Layers

| Mechanism               | Description                                        | Enforcement                    |
| :---------------------- | :------------------------------------------------- | :----------------------------- |
| **Checksum Validation** | All processed files have `.sha256` signatures.     | GitHub CI/CD (`checksums.yml`) |
| **Schema Validation**   | Metadata verified using JSON Schema.               | Python `jsonschema` library    |
| **STAC Validation**     | STAC Items/Collections validated automatically.    | `stac-validate.yml` workflow   |
| **Data QA/QC**          | Manual and automated checks for spatial integrity. | `make validate` target         |
| **CI/CD Enforcement**   | PRs blocked unless all validations succeed.        | `.github/workflows/*`          |

---

## 🌐 Data Publication Pipeline

The **publication workflow** transforms processed datasets and STAC metadata
into web-accessible assets for visualization.

```mermaid
graph LR
  A["data/processed/"] --> B["data/stac/"]
  B --> C["data/tiles/"]
  C --> D["web/config/layers.json"]
  D --> E["🌎 MapLibre Web App"]
```

<!-- END OF MERMAID -->

This allows users to:

* Browse datasets via STAC collections
* Toggle layers interactively on maps
* View provenance metadata and thumbnails

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                |
| :---------------------- | :------------------------------------------------------------ |
| **Documentation-first** | Every directory includes README + metadata.                   |
| **Reproducibility**     | Deterministic ETL and checksum workflows.                     |
| **Open Standards**      | STAC 1.0.0, GeoTIFF (COG), GeoJSON, NetCDF, CSV, JSON Schema. |
| **Provenance**          | Linked manifests and checksums for every dataset.             |
| **Auditability**        | Automated CI/CD validation and full data lineage logs.        |

---

## 📎 Related Documentation

| Path                                   | Description                                          |
| :------------------------------------- | :--------------------------------------------------- |
| `data/ARCHITECTURE.md`                 | In-depth description of the overall data pipeline.   |
| `docs/architecture/architecture.md`    | System-wide overview (data + CI/CD + visualization). |
| `docs/architecture/system_overview.md` | Optional visual summary of the entire KFM stack.     |
| `.github/workflows/stac-validate.yml`  | Workflow enforcing STAC metadata validation.         |

---

## 📅 Version History

| Version | Date       | Summary                                                                                       |
| :------ | :--------- | :-------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial data architecture documentation — detailing full data lifecycle and provenance model. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Proven. Every Process Reproducible.”*
📍 [`docs/architecture/data-architecture.md`](.) · Technical documentation of the Kansas Frontier Matrix data architecture.

</div>
