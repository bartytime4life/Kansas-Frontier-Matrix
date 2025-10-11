<div align="center">

# 🧱 Kansas Frontier Matrix — Data Architecture  
`data/ARCHITECTURE.md`

**Mission:** Define the **end-to-end data architecture** of the Kansas Frontier Matrix (KFM) —  
detailing how raw inputs are transformed, validated, documented, and visualized within a **reproducible**,  
**STAC-compliant**, and **MCP-governed** data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix Data Architecture** governs how data moves through the repository —  
from acquisition and transformation to metadata generation, validation, and visualization.  
It ensures that every layer of data is:

- **Traceable** — from its source manifest to its published STAC Item.  
- **Reproducible** — deterministic ETL and validation workflows.  
- **Auditable** — via checksums, provenance logs, and MCP documentation.  
- **Open** — using transparent, standards-based formats for maximum interoperability.  

This document serves as the **blueprint** for the KFM data subsystem — defining its lifecycle,  
governance model, and automated verification pipeline.

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

| Stage                       | Directory                                | Purpose                                                   | Key Artifacts                     |
| :-------------------------- | :--------------------------------------- | :-------------------------------------------------------- | :-------------------------------- |
| **1. Source Registration**  | `data/sources/`                          | Defines dataset origins, access methods, and licensing.   | JSON manifests (`*.json`)         |
| **2. Raw Acquisition**      | `data/raw/`                              | Immutable snapshots of ingested data.                     | GeoTIFF, CSV, NetCDF, JSON        |
| **3. ETL Processing**       | `src/pipelines/`                         | Cleans, transforms, and standardizes inputs.              | Python scripts, ETL logs          |
| **4. Processed Data**       | `data/processed/`                        | Validated outputs ready for analysis or visualization.    | GeoJSON, COG, CSV                 |
| **5. Metadata & STAC**      | `data/processed/metadata/`, `data/stac/` | Records structure, provenance, spatial/temporal coverage. | STAC Items & Collections          |
| **6. Integrity Validation** | `data/checksums/`                        | Verifies integrity through deterministic hashing.         | `.sha256` files                   |
| **7. Visualization**        | `data/tiles/`, `web/config/`             | Powers map and timeline interfaces.                       | Raster/vector tiles, JSON configs |

---

## ⚙️ ETL Pipeline Architecture

The ETL subsystem is a **modular, deterministic pipeline** orchestrated by Makefiles
and executed through Python scripts within `src/pipelines/`.

### 🔧 Domain Pipelines

| Domain        | Pipeline Script         | Output Directory            | Description                                 |
| :------------ | :---------------------- | :-------------------------- | :------------------------------------------ |
| **Terrain**   | `terrain_pipeline.py`   | `data/processed/terrain/`   | DEMs, hillshades, slope/aspect layers       |
| **Hydrology** | `hydrology_pipeline.py` | `data/processed/hydrology/` | Rivers, watersheds, flood polygons          |
| **Landcover** | `landcover_pipeline.py` | `data/processed/landcover/` | Vegetation, land use, NLCD                  |
| **Climate**   | `climate_pipeline.py`   | `data/processed/climate/`   | Precipitation, temperature, drought indices |
| **Hazards**   | `hazards_pipeline.py`   | `data/processed/hazards/`   | Tornado, wildfire, flood events             |
| **Tabular**   | `tabular_pipeline.py`   | `data/processed/tabular/`   | Census, agricultural, economic stats        |
| **Text**      | `text_pipeline.py`      | `data/processed/text/`      | OCR and NLP outputs (treaties, newspapers)  |

Each pipeline:

* Pulls sources from `data/sources/`.
* Logs transformations to `data/work/logs/`.
* Writes intermediates to `data/work/tmp/`.
* Generates checksums in `data/checksums/`.
* Outputs metadata under `data/processed/metadata/`.

---

## 🧮 Validation & Integrity Architecture

| Component                  | Function                                                   | Tooling                            |
| :------------------------- | :--------------------------------------------------------- | :--------------------------------- |
| **Checksums**              | Verifies binary integrity via SHA-256.                     | `hashlib`, Make targets            |
| **Schema Validation**      | Confirms JSON/STAC schema conformance.                     | `jsonschema`, `stac-validator`     |
| **STAC Compliance**        | Ensures catalog consistency and references.                | GitHub Action: `stac-validate.yml` |
| **Continuous Integration** | Runs validation on every push or PR.                       | GitHub Actions                     |
| **Peer Review**            | Applies MCP’s scientific peer protocol for major datasets. | Manual review, change log          |

All validation artifacts are versioned and archived in `data/checksums/`
and `data/work/logs/` for audit reproducibility.

---

## 🧠 Provenance Tracking

Provenance follows a **linear, inspectable chain**:

`Source → Raw → Processed → Metadata → Visualization`

| Artifact Type       | Example Path                              | Purpose                                         |
| :------------------ | :---------------------------------------- | :---------------------------------------------- |
| **Source Manifest** | `data/sources/usgs_dem.json`              | Defines original dataset endpoint & license.    |
| **Checksum File**   | `data/checksums/terrain/ks_dem_1m.sha256` | Verifies output integrity.                      |
| **STAC Item**       | `data/stac/terrain/ks_dem_1m.json`        | Describes dataset metadata and access links.    |
| **Processing Log**  | `data/work/logs/terrain_2025-10.log`      | Records transformation and validation results.  |
| **ETL Script**      | `src/pipelines/terrain_pipeline.py`       | Reconstructs transformations deterministically. |

Each dataset’s lineage can be traced entirely from its source manifest to its published layer.

---

## 🔒 CI/CD Data Governance

Automated **GitHub Actions** enforce the MCP data governance model.

| Workflow            | Purpose                                           | Trigger             |
| :------------------ | :------------------------------------------------ | :------------------ |
| `fetch.yml`         | Fetch raw datasets defined in manifests.          | Manual or scheduled |
| `stac-validate.yml` | Validate STAC schema and links.                   | Push / PR           |
| `checksums.yml`     | Recompute and verify SHA-256 hashes.              | Data updates        |
| `codeql.yml`        | Analyze ETL and validation code.                  | Push / PR           |
| `site.yml`          | Build documentation and deploy site.              | Merge to `main`     |
| `trivy.yml`         | Scan images and dependencies for vulnerabilities. | Nightly             |

All workflows log results to `data/work/logs/` and surface status badges on project READMEs.

---

## 🧩 Integration with the MCP Framework

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-First** | Every data folder includes a README and STAC example.                  |
| **Reproducibility**     | Deterministic ETL with logs, hashes, and pinned dependencies.          |
| **Open Standards**      | Uses STAC 1.0, GeoTIFF (COG), GeoJSON, Parquet, CSVW, NetCDF.          |
| **Provenance**          | Chain of manifests, logs, checksums, and metadata ensure full lineage. |
| **Auditability**        | Automated + human validation provide continuous assurance.             |

---

## 🧱 Architectural Philosophy

1. **Transparency** — Every dataset has an explicit, inspectable lineage.
2. **Reproducibility** — Every transformation is deterministic and scriptable.
3. **Interoperability** — Every format and schema is open and standard-compliant.
4. **Extensibility** — Pipelines and metadata schemas can evolve without breaking legacy data.

---

## 📎 Related Documentation

| Path                     | Description                                  |
| :----------------------- | :------------------------------------------- |
| `data/README.md`         | High-level overview of all data directories. |
| `data/sources/README.md` | Source manifests and provenance registry.    |
| `data/stac/README.md`    | STAC catalog structure and validation rules. |
| `docs/architecture/`     | Global system and integration architecture.  |
| `src/pipelines/`         | Domain ETL modules and transformation logic. |

---

## 🧾 Version History

| Version    | Date       | Summary                                                                                         |
| :--------- | :--------- | :---------------------------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial data architecture documentation (source → visualization flow).                          |
| **v1.1.0** | 2025-10-10 | Upgraded per MCP Framework: added CodeQL/Trivy workflows, extended provenance + CI/CD sections. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Data Without Mystery: Every Byte Proven, Every Layer Reproducible.”*
📍 [`data/ARCHITECTURE.md`](.) · Blueprint for the Kansas Frontier Matrix data subsystem.

</div>
