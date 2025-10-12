<div align="center">

# 🔐 Kansas Frontier Matrix — Processed Data Checksums

`data/processed/checksums/`

**Mission:** Safeguard the integrity and traceability of all processed datasets through reproducible
**SHA-256 checksums**, ensuring **scientific verifiability**, **data provenance**, and **end-to-end reproducibility** across the Kansas Frontier Matrix (KFM) ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 🧩 Versioning

| Field            | Value                                    |
| :--------------- | :--------------------------------------- |
| **Version**      | `v1.4.0`                                 |
| **Status**       | Stable                                   |
| **Maintainers**  | KFM Data Engineering Team                |
| **Last Updated** | 2025-10-12                               |
| **Applies To**   | All datasets in `data/processed/`        |
| **Provenance**   | MCP v1.0 • STAC 1.0.0 • SHA-256 Verified |

---

## 📚 Table of Contents

* [Overview](#overview)
* [Purpose](#purpose)
* [Directory Layout](#directory-layout)
* [Checksum Generation](#checksum-generation)
* [Verification Workflow](#verification-workflow)
* [Integration with MCP & STAC](#integration-with-mcp--stac)
* [Adding or Updating Checksums](#adding-or-updating-checksums)
* [Best Practices](#best-practices)
* [Mermaid Data Flow](#mermaid-data-flow)
* [Change Log](#change-log)
* [References](#references)

---

## 🧠 Overview

This directory houses **cryptographic checksum manifests (`.sha256`)** validating the byte-level integrity of all
processed datasets within `data/processed/`.

Checksums provide tamper detection, reproducibility validation, and traceable data lineage across every processing stage.
Each 64-character digest uniquely represents a dataset version and integrates directly into the
**MCP Provenance** and **STAC Catalog** metadata structures.

---

## 🎯 Purpose

| Objective                  | Description                                                                   |
| :------------------------- | :---------------------------------------------------------------------------- |
| 🧩 **Integrity Assurance** | Ensures that processed datasets remain unmodified post-validation.            |
| 🔁 **Reproducibility**     | Enables deterministic, verifiable reconstruction of results.                  |
| ⚙️ **Automation**          | Supports CI/CD checksum validation workflows.                                 |
| 🔗 **Provenance Linkage**  | Ties `mcp_provenance` fields in metadata and STAC Items to verifiable hashes. |

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── checksums/
        ├── terrain/
        │   ├── dem_1m_ks_filled.tif.sha256
        │   ├── dem_30m_ned_ks.tif.sha256
        ├── hydrology/
        │   ├── flow_dir_d8_1m_ks.tif.sha256
        │   ├── watermask_ks.tif.sha256
        ├── landcover/
        │   ├── nlcd_2021_ks.tif.sha256
        │   ├── vegetation_mask_ks.tif.sha256
        ├── climate/
        │   ├── precip_total_annual_1895_2024.tif.sha256
        │   ├── drought_spi12_1895_2024.tif.sha256
        ├── hazards/
        │   ├── tornado_tracks_1950_2024.geojson.sha256
        │   ├── fema_disasters_1953_2024.geojson.sha256
        ├── tabular/
        │   ├── tornado_counts_1950_2024.csv.sha256
        │   ├── county_population_1850_2020.csv.sha256
        ├── text/
        │   ├── newspapers_1854_1925_cleaned.jsonl.sha256
        │   ├── nlp_entities_extracted.json.sha256
        └── README.md
```

Each file stores a 64-character SHA-256 digest ensuring byte-for-byte identity across all environments.

---

## ⚙️ Checksum Generation

Checksums are generated automatically during ETL or manually when verifying datasets.

```bash
# ✅ Generate checksum for one file
sha256sum dem_1m_ks_filled.tif > checksums/terrain/dem_1m_ks_filled.tif.sha256

# 🔁 Generate checksums recursively
find data/processed -type f \( -name "*.tif" -o -name "*.csv" -o -name "*.jsonl" \) \
  -exec sha256sum {} \; > data/processed/checksums/_manifest_all.sha256
```

💡 Use `--binary` mode (`sha256sum --binary`) for cross-platform consistency.

---

## 🧪 Verification Workflow

```bash
# Verify all checksums in a subdirectory
sha256sum -c checksums/terrain/*.sha256

# Verify a specific file
sha256sum -c data/processed/checksums/climate/precip_total_annual_1895_2024.tif.sha256
```

**Automated CI/CD Integration**
Validation runs in `.github/workflows/stac-validate.yml` for every push or pull request.
Any checksum mismatch halts the pipeline, ensuring no altered or corrupted data enters production.

---

## 🧩 Integration with MCP & STAC

| Layer              | Integration Mechanism                                                                         |
| :----------------- | :-------------------------------------------------------------------------------------------- |
| **MCP Provenance** | Metadata JSON contains `"mcp_provenance": "sha256:<digest>"`.                                 |
| **STAC Catalog**   | STAC Item property `properties.checksum:sha256` mirrors the same digest for cross-validation. |
| **Data Lineage**   | Links checksum → STAC Item → metadata → dataset → CI logs.                                    |

This creates a **verifiable, multi-layer integrity chain** across both the **scientific** and **geospatial** domains.

---

## 🧮 Adding or Updating Checksums

1. **Generate**

   ```bash
   sha256sum <file> > data/processed/checksums/<path>/<file>.sha256
   ```
2. **Validate**

   ```bash
   sha256sum -c data/processed/checksums/<path>/<file>.sha256
   ```
3. **Commit**
   Add both the data and checksum files to Git.
4. **Push**
   CI/CD auto-verifies checksums.
5. **Update Provenance**
   If data changes, refresh checksum and increment `version` + `mcp_provenance` in metadata.

---

## 🧠 Best Practices

| Category                 | Guideline                                                  |
| :----------------------- | :--------------------------------------------------------- |
| ✅ **Completeness**       | Every processed dataset must include a matching `.sha256`. |
| 🔄 **Update Policy**     | Always regenerate checksums after any file change.         |
| 🧾 **Schema Compliance** | Ensure metadata JSON validates against MCP/STAC schemas.   |
| 🧪 **CI Enforcement**    | Automated tests must reject mismatched hashes.             |
| 🧰 **Transparency**      | Maintain `_manifest_all.sha256` for full dataset audits.   |

---

## 🧭 Mermaid Data Flow

```mermaid
flowchart TD
  A["Data Sources<br/>raw scans · rasters · vectors"] --> B["ETL Process<br/>normalize · clean · export"]
  B --> C["Processed Data<br/>COGs · CSVs · JSONL"]
  C --> D["Checksum Generation<br/>sha256sum per file"]
  D --> E["Verification<br/>CI/CD · local validation"]
  E --> F["Catalog & Provenance<br/>STAC · MCP metadata"]
  F --> G["Public Access<br/>GitHub · Data Hub · Google Earth"]
<!-- END OF MERMAID -->
```

---

## 🧾 Change Log

| Version    | Date       | Type      | Description                                                 | Author     |
| :--------- | :--------- | :-------- | :---------------------------------------------------------- | :--------- |
| **v1.4.0** | 2025-10-12 | 🔧 Update | Full revision with versioning, Mermaid, and best-practices. | Andy Barta |
| **v1.3.2** | 2025-09-28 | 🧩 Add    | Added checksum integration with STAC validation.            | KFM Core   |
| **v1.2.0** | 2025-08-15 | ✨ Feature | Introduced `_manifest_all.sha256` batch audits.             | Data Ops   |
| **v1.0.0** | 2025-06-01 | 🚀 Launch | Initial checksum repository for processed data.             | MCP Team   |

---

## 📖 References

* 🔗 [GNU Coreutils SHA Utilities](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
* 🌐 [STAC Specification 1.0](https://stacspec.org)
* 🧩 [JSON Schema](https://json-schema.org)
* 📘 [Master Coder Protocol Standards](../../../docs/standards/)
* 🧭 [Data Provenance in Open Science](https://www.nature.com/articles/s41597-019-0193-2)

---

<div align="center">

> “Every verified checksum is a promise —
> Kansas’s digital frontier remains consistent, transparent, and trusted.”

**— Kansas Frontier Matrix · Integrity First**

</div>
