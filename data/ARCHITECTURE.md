<div align="center">

# 🧱 Kansas Frontier Matrix — Data Architecture  
`data/ARCHITECTURE.md`

**Mission:** Define the **end-to-end data architecture** of the Kansas Frontier Matrix (KFM) —  
detailing how raw inputs are transformed, validated, documented, and visualized within a **reproducible**,  
**STAC-compliant**, and **MCP-governed** data ecosystem.

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
- Is **auditable** via checksums, provenance logs, and MCP documentation.  
- Adheres to **open standards** for interoperability and accessibility.  

This document provides a **high-level blueprint** of the data subsystem and its lifecycle within KFM.

---

## 🗺️ Data Architecture Overview

```mermaid
flowchart TD
  A["🌐 External Sources\n(data/sources/)"] --> B["📦 Raw Data\n(data/raw/)"]
  B --> C["⚙️ ETL Processing & Cleaning\n(src/pipelines/)"]
  C --> D["✅ Processed Data\n(data/processed/)"]
  D --> E["🧩 Metadata & STAC\n(data/processed/metadata/ · data/stac/)"]
  E --> F["🧾 Checksums & Validation\n(data/checksums/)"]
  F --> G["🌎 Web & Visualization Layers\n(data/tiles/ · web/config/)"]

  style A fill:#f8f9fa,stroke:#888;
  style B fill:#f0f8ff,stroke:#0088cc;
  style C fill:#fff0f5,stroke:#cc0088;
  style D fill:#e8fff0,stroke:#33aa33;
  style E fill:#faf5e6,stroke:#e8a500;
  style F fill:#f0e8ff,stroke:#7d33aa;
  style G fill:#f7f7f7,stroke:#333;
%% END OF MERMAID
````

---

## 🧩 Data Lifecycle Stages

| Stage                       | Directory                                | Purpose                                                 | Key Artifacts                          |
| :-------------------------- | :--------------------------------------- | :------------------------------------------------------ | :------------------------------------- |
| **1. Source Registration**  | `data/sources/`                          | Defines dataset origins, access methods, and licensing. | JSON manifests (`*.json`)              |
| **2. Raw Acquisition**      | `data/raw/`                              | Immutable snapshots of ingested source data.            | Raw files (e.g., GeoTIFF, CSV, NetCDF) |
| **3. ETL Processing**       | `src/pipelines/`                         | Transforms, cleans, and standardizes data for analysis. | Python scripts, ETL logs               |
| **4. Processed Data**       | `data/processed/`                        | Validated & cleaned data ready for publication.         | GeoTIFF (COG), GeoJSON, CSV, JSONL     |
| **5. Metadata & STAC**      | `data/processed/metadata/`, `data/stac/` | Provenance, structure, spatial/temporal coverage.       | STAC Items & Collections               |
| **6. Integrity Validation** | `data/checksums/`                        | SHA-256 hashes for reproducibility verification.        | `.sha256` files                        |
| **7. Visualization**        | `data/tiles/`, `web/config/`             | Pre-rendered tiles and viewer configuration.            | Raster/vector tiles, JSON configs      |

---

## ⚙️ ETL Pipeline Architecture

The KFM ETL system operates as a **deterministic, domain-driven pipeline**
powered by Makefiles and modular Python scripts in `src/pipelines/`.

### 🧱 Pipeline Modules

| Domain        | Pipeline Script         | Output Directory            | Description                         |
| :------------ | :---------------------- | :-------------------------- | :---------------------------------- |
| **Terrain**   | `terrain_pipeline.py`   | `data/processed/terrain/`   | DEM, hillshade, slope/aspect        |
| **Hydrology** | `hydrology_pipeline.py` | `data/processed/hydrology/` | Rivers, watersheds, flood layers    |
| **Landcover** | `landcover_pipeline.py` | `data/processed/landcover/` | NLCD, vegetation, land use          |
| **Climate**   | `climate_pipeline.py`   | `data/processed/climate/`   | Precipitation, temperature, drought |
| **Hazards**   | `hazards_pipeline.py`   | `data/processed/hazards/`   | Tornado, wildfire, flood events     |
| **Tabular**   | `tabular_pipeline.py`   | `data/processed/tabular/`   | Census, agriculture, economics      |
| **Text**      | `text_pipeline.py`      | `data/processed/text/`      | OCR, NLP, and transcript datasets   |

Each pipeline:

* Fetches data from `data/sources/`
* Logs processing steps to `data/work/logs/`
* Writes intermediates to `data/work/tmp/`
* Generates checksums in `data/checksums/`
* Produces metadata in `data/processed/metadata/`

---

## 🧮 Validation & Integrity Architecture

Validation ensures that **all data products** meet reproducibility and consistency standards.

| Component             | Function                                         | Tooling                           |
| :-------------------- | :----------------------------------------------- | :-------------------------------- |
| **Checksums**         | SHA-256 verifies file integrity across rebuilds. | `hashlib`, Make targets           |
| **Schema Validation** | JSON Schema validates manifests and metadata.    | `jsonschema`, `stac-validator`    |
| **STAC Compliance**   | Catalog structure follows STAC 1.0.0.            | GitHub Action `stac-validate.yml` |
| **CI/CD Workflows**   | Automated validation for any data change.        | GitHub Actions                    |
| **Manual Review**     | Peer verification for critical updates.          | MCP peer-review protocol          |

---

## 🧠 Provenance Tracking

Provenance follows a **source → raw → processed → metadata → visualization** chain.

Artifacts per dataset:

* **Source Manifest** — `data/sources/*.json`
* **Checksum File** — `data/checksums/<domain>/*.sha256`
* **STAC Item** — `data/stac/<domain>/*.json`
* **Processing Log** — `data/work/logs/*.log`
* **ETL Script** — `src/pipelines/<domain>_pipeline.py`

Together, these guarantee **auditability, reproducibility, and transparency**.

---

## 🧩 Integration with the MCP Framework

KFM’s data architecture adheres to **Master Coder Protocol (MCP)** principles:

| MCP Principle           | Implementation                                                |
| :---------------------- | :------------------------------------------------------------ |
| **Documentation-first** | Every data stage includes a README and structured metadata.   |
| **Reproducibility**     | Deterministic ETL and checksum validation ensure consistency. |
| **Open Standards**      | STAC 1.0.0, GeoTIFF (COG), GeoJSON, NetCDF, CSV.              |
| **Provenance**          | Source manifests, STAC links, and logs document full lineage. |
| **Auditability**        | CI/CD logging, peer validation, and hash verification.        |

---

## 🧩 CI/CD Data Governance

Automated **GitHub Actions** enforce data governance:

| Workflow            | Purpose                                     | Trigger          |
| :------------------ | :------------------------------------------ | :--------------- |
| `fetch.yml`         | Download raw data from manifests.           | Push or schedule |
| `stac-validate.yml` | Validate catalog structure and links.       | PR or commit     |
| `checksums.yml`     | Recompute and verify all SHA-256 checksums. | On data update   |
| `site.yml`          | Build docs and deploy the data viewer site. | Push to `main`   |

Workflow logs are archived under `data/work/logs/`.

---

## 🧱 Architectural Philosophy

1. **Transparency** — Every dataset must have a clear, documented lineage.
2. **Reproducibility** — Every transformation is deterministic and scriptable.
3. **Interoperability** — All formats and schemas are open and standards-compliant.

---

## 📎 Related Documentation

| Path                     | Description                             |
| :----------------------- | :-------------------------------------- |
| `data/README.md`         | Overview of all data directories.       |
| `data/sources/README.md` | Source manifests & provenance registry. |
| `data/stac/README.md`    | STAC catalog & metadata integration.    |
| `docs/architecture/`     | High-level project architecture.        |
| `src/pipelines/`         | ETL & transformation pipelines.         |

---

## 📅 Version History

| Version | Date       | Summary                                                                |
| :------ | :--------- | :--------------------------------------------------------------------- |
| v1.0.0  | 2025-10-04 | Initial data architecture documentation (source → visualization flow). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Data Without Mystery: Every Byte Proven, Every Layer Reproducible.”*
📍 [`data/ARCHITECTURE.md`](.) · Blueprint for the data subsystem within the Kansas Frontier Matrix.

</div>
