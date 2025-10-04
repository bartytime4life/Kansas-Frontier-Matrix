<div align="center">

# 🔐 Kansas-Frontier-Matrix — Processed Data Checksums (`data/processed/checksums/`)

**Mission:** Store and manage **checksum files (`.sha256`)** for all processed datasets,  
ensuring data integrity, provenance, and reproducibility across the Kansas Frontier Matrix ecosystem.

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

## 📚 Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Directory Layout](#directory-layout)
- [Checksum Generation](#checksum-generation)
- [Verification Workflow](#verification-workflow)
- [Integration with MCP & STAC](#integration-with-mcp--stac)
- [Adding or Updating Checksums](#adding-or-updating-checksums)
- [References](#references)

---

## 🧠 Overview

This directory contains **SHA-256 checksum files** that verify the integrity of all  
processed datasets stored under `data/processed/`.  

Checksums ensure that data files have not been modified, corrupted, or replaced since  
their last generation, allowing for **reproducible science** and traceable lineage —  
core tenets of the **Master Coder Protocol (MCP)**.

Each checksum file corresponds 1:1 to a data asset, whether raster, vector, tabular, or text.

---

## 🎯 Purpose

- **Integrity Assurance:** Guarantee that processed files remain unchanged post-validation.  
- **Reproducibility:** Allow independent users to verify data consistency using hash checks.  
- **Automation:** Enable CI/CD pipelines to confirm checksum validity during build and deploy stages.  
- **Linkage:** Tie each checksum to its associated `mcp_provenance` field in metadata and STAC catalogs.  

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
````

Each `.sha256` file contains a single 64-character hexadecimal hash representing the
unique fingerprint of the dataset it validates.

---

## 🔐 Checksum Generation

Checksums are automatically generated using `sha256sum` during ETL or processing stages.
Manual creation (for local validation) is also supported:

```bash
# Generate checksum for a single file
sha256sum dem_1m_ks_filled.tif > checksums/terrain/dem_1m_ks_filled.tif.sha256

# Generate all checksums recursively
find data/processed -type f \( -name "*.tif" -o -name "*.csv" -o -name "*.jsonl" \) \
  -exec sha256sum {} \; > data/processed/checksums/_manifest_all.sha256
```

All hashes are computed in **binary mode** (`--binary`) to ensure cross-platform consistency.

---

## 🔎 Verification Workflow

Checksum validation can be performed manually or automatically during continuous integration.

```bash
# Verify all checksums in a directory
sha256sum -c checksums/terrain/*.sha256

# Verify a single file
sha256sum -c data/processed/checksums/climate/precip_total_annual_1895_2024.tif.sha256
```

### Automated CI Validation

The GitHub Action `.github/workflows/stac-validate.yml` executes checksum verification
for every push or pull request, ensuring that no file changes go unnoticed.

---

## 🧩 Integration with MCP & STAC

Checksums are directly referenced in two metadata systems:

1. **MCP Provenance Chains**

   * Each metadata JSON includes an `mcp_provenance` field (e.g. `"sha256:abc123…"`) linking to the file hash.
2. **STAC Catalog**

   * Each STAC item’s `properties` section contains the same hash for auditability.

This dual-record ensures that checksum verification is part of both
scientific reproducibility and catalog integrity workflows.

---

## 🧮 Adding or Updating Checksums

1. Run checksum generation:

   ```bash
   sha256sum <file> > data/processed/checksums/<path>/<file>.sha256
   ```
2. Confirm with:

   ```bash
   sha256sum -c data/processed/checksums/<path>/<file>.sha256
   ```
3. Commit both the data file and its `.sha256` pair.
4. Push changes — CI/CD will verify integrity automatically.
5. If a file changes intentionally (e.g., reprocessed dataset), **update its checksum** and
   increment its version in the corresponding metadata JSON under `mcp_provenance`.

---

## 📖 References

* **GNU Coreutils SHA256SUM:** [https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **JSON Schema Specification:** [https://json-schema.org](https://json-schema.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../docs/standards/)
* **Data Provenance in Open Science:** [https://www.nature.com/articles/s41597-019-0193-2](https://www.nature.com/articles/s41597-019-0193-2)

---

<div align="center">

*“Every verified checksum is a promise — that Kansas’s digital frontier remains consistent, transparent, and trusted.”*

</div>
```

