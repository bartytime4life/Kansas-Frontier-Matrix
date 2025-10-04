<div align="center">

# 🗂️ Kansas Frontier Matrix — File & Directory Architecture  
`docs/architecture/file-architecture.md`

**Mission:** Define the **complete directory structure, file standards, and lineage design**  
of the Kansas Frontier Matrix (KFM) repository — ensuring that every file, folder,  
and artifact is **traceable**, **documented**, and **reproducible** in alignment with the  
**Master Coder Protocol (MCP)** and **open data governance** standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The **file architecture** of the Kansas Frontier Matrix repository is designed for  
**clarity, transparency, and reproducibility** — ensuring that every dataset, metadata file,  
and workflow artifact can be located, validated, and reprocessed deterministically.

Each directory has:
- 📘 **README.md** explaining purpose and usage  
- 🧩 **Schema / manifest files** for validation  
- 🧾 **Checksums** to ensure integrity  
- 🧠 **Traceable lineage** from raw to processed outputs  

---

## 🗃️ Top-Level Repository Layout

```bash
Kansas-Frontier-Matrix/
├── data/                      # Core data management system
│   ├── sources/               # JSON manifests for all raw data sources
│   ├── raw/                   # Immutable original datasets
│   ├── processed/             # Cleaned, validated, standardized data
│   ├── checksums/             # SHA-256 hashes for reproducibility
│   ├── tiles/                 # Raster and vector map tiles for web display
│   ├── stac/                  # STAC catalog (metadata + asset registry)
│   ├── work/                  # Temporary, staging, and logging directories
│   └── ARCHITECTURE.md        # Data-specific architectural documentation
│
├── docs/                      # Documentation system (Markdown + architecture guides)
│   ├── architecture/          # Architecture subfolder
│   │   ├── architecture.md    # System-level architecture
│   │   ├── data-architecture.md
│   │   └── file-architecture.md
│   └── standards/             # Style, schema, and reproducibility standards
│
├── src/                       # ETL + processing pipelines
│   ├── pipelines/             # Domain-specific ETL scripts
│   ├── utils/                 # Shared helper scripts and validation utilities
│   └── tests/                 # Unit and integration tests for pipelines
│
├── web/                       # Static web app and configuration
│   ├── config/                # JSON-based configuration for MapLibre + UI
│   ├── assets/                # Logos, icons, and UI images
│   └── index.html             # Web interface root
│
├── .github/                   # GitHub automation, CI/CD, and issue templates
│   ├── workflows/             # YAML workflows for build, test, and validation
│   └── ISSUE_TEMPLATE/        # Standardized templates for community contributions
│
├── Makefile                   # Task automation for ETL, validation, and deployment
├── LICENSE                    # Code and data license (MIT + CC-BY 4.0)
└── README.md                  # Repository overview and quick start
````

---

## 🧱 Data Subsystem Hierarchy

```bash
data/
├── sources/             # Registry of data origins (JSON manifests)
├── raw/                 # Immutable raw data (untouched)
├── processed/           # Cleaned and standardized datasets
│   ├── terrain/         # DEM, slope, hillshade
│   ├── hydrology/       # Rivers, basins, floods
│   ├── landcover/       # Vegetation, NLCD, crop cover
│   ├── climate/         # Temperature, precipitation, drought
│   ├── hazards/         # Tornado, wildfire, flood events
│   ├── tabular/         # Census, agriculture, economy
│   └── text/            # Historical text & OCR data
│
├── processed/metadata/  # STAC-linked metadata and thumbnails
├── checksums/           # File integrity and reproducibility records
├── stac/                # Catalog of metadata + asset references
├── tiles/               # Web-friendly map tile assets (raster/vector)
└── work/                # Transient workspace (logs, tmp, cache, staging)
```

Each data domain (`terrain/`, `hydrology/`, etc.) contains:

* `README.md` — domain-specific documentation
* `metadata/` — STAC items + schema files
* `thumbnails/` — visualization previews
* `checksums/` — `.sha256` verification files

---

## 🧩 Workspaces & Their Roles

| Directory            | Purpose                                                          | Lifecycle       | Retention Policy                   |
| :------------------- | :--------------------------------------------------------------- | :-------------- | :--------------------------------- |
| `data/work/tmp/`     | Temporary intermediate files during ETL runs.                    | Ephemeral       | Auto-cleaned via `make clean-tmp`  |
| `data/work/cache/`   | Caching layer for reused intermediates.                          | Semi-persistent | Clean monthly                      |
| `data/work/staging/` | Pre-validation staging area before final commit to `processed/`. | Transitional    | Promoted or purged post-validation |
| `data/work/logs/`    | Pipeline and CI/CD logs for reproducibility and audit.           | Continuous      | Retained for one build cycle       |

---

## 🧾 File Naming Conventions

KFM follows **deterministic and descriptive** file naming for all data products.

| Category             | Format                                | Example                          |
| :------------------- | :------------------------------------ | :------------------------------- |
| **Datasets**         | `<region>_<topic>_<year-range>.<ext>` | `ks_1m_dem_2018_2020.tif`        |
| **Metadata**         | `<dataset>.json`                      | `ks_1m_dem_2018_2020.json`       |
| **Checksum**         | `<dataset>.<ext>.sha256`              | `ks_1m_dem_2018_2020.tif.sha256` |
| **Thumbnail**        | `<dataset>.png`                       | `ks_1m_dem_2018_2020.png`        |
| **Source Manifests** | `<provider>_<dataset>.json`           | `usgs_3dep_dem.json`             |
| **Logs**             | `<domain>_etl_debug.log`              | `terrain_etl_debug.log`          |

All files use **lowercase with underscores**, ensuring cross-platform compatibility and predictability in automation.

---

## 🔗 Provenance Chain (File Relationships)

```text
data/sources/<domain>/<source>.json
    ↓ (fetch)
data/raw/<domain>/<dataset>.<ext>
    ↓ (ETL)
data/processed/<domain>/<dataset>.<ext>
    ↓ (checksum)
data/checksums/<domain>/<dataset>.<ext>.sha256
    ↓ (metadata)
data/stac/<domain>/<dataset>.json
    ↓ (visualization)
data/tiles/<domain>/<dataset>/{z}/{x}/{y}.png
```

Each stage is **linked by relative path**, and all references are validated by STAC and checksum workflows.

---

## 🧠 Reproducibility Design

| Layer                        | Mechanism                 | Tooling                            |
| :--------------------------- | :------------------------ | :--------------------------------- |
| **Integrity**                | SHA-256 checksums         | `hashlib`, Makefile targets        |
| **Metadata Validation**      | JSON Schema enforcement   | `jsonschema`, `stac-validator`     |
| **Pipeline Reproducibility** | Deterministic ETL scripts | `src/pipelines/*.py`               |
| **CI/CD Enforcement**        | Workflow automation       | `.github/workflows/*`              |
| **Human Verification**       | Peer review checklist     | `.github/PULL_REQUEST_TEMPLATE.md` |

All validations and logs are stored temporarily in `data/work/logs/` and summarized in CI artifacts.

---

## 🧩 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | Every directory and subdomain contains README.md.                  |
| **Reproducibility**     | File structure enforces deterministic rebuilds.                    |
| **Open Standards**      | GeoTIFF, GeoJSON, NetCDF, STAC, CSV, JSON Schema.                  |
| **Provenance**          | Each file links backward through manifest, metadata, and checksum. |
| **Auditability**        | Structure validated automatically by CI/CD and checksum workflows. |

---

## 🧱 Design Goals

1. **Transparency** — Every file is traceable from acquisition to publication.
2. **Modularity** — Independent directories for each data domain and workflow.
3. **Reproducibility** — Checksums, metadata, and Makefiles guarantee consistent results.
4. **Interoperability** — Compatible with STAC 1.0.0, GeoTIFF (COG), and web mapping standards.
5. **Automation** — Fully integrated with GitHub Actions for validation and deployment.

---

## 📎 Related Documentation

| File                                     | Description                                 |
| :--------------------------------------- | :------------------------------------------ |
| `docs/architecture/architecture.md`      | Full system architecture overview.          |
| `docs/architecture/data-architecture.md` | Data flow, lineage, and validation systems. |
| `data/ARCHITECTURE.md`                   | Implementation details for data management. |
| `.github/workflows/README.md`            | CI/CD automation and data governance.       |

---

## 📅 Version History

| Version | Date       | Summary                                                                                |
| :------ | :--------- | :------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial file architecture documentation with directory hierarchy and provenance chain. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every File Has a Purpose. Every Path Has a Provenance.”*
📍 [`docs/architecture/file-architecture.md`](.) · Complete directory and file-level architecture of the Kansas Frontier Matrix.

</div>

