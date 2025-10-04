<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Checksums  
`data/processed/checksums/hydrology/`

**Mission:** Verify and preserve the **integrity and reproducibility** of all processed hydrology datasets  
through SHA-256 checksums, ensuring consistent data lineage and provenance within the Kansas Frontier Matrix.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **SHA-256 checksum files (`.sha256`)**  
for all processed hydrology datasets in Kansas Frontier Matrix (KFM).  

Checksums guarantee:
- **Integrity:** Detect accidental corruption or unauthorized modification  
- **Reproducibility:** Confirm that generated outputs match expected pipeline artifacts  
- **Traceability:** Provide a verifiable audit trail for hydrology layers across ETL stages  

All hashes are generated automatically by the hydrology ETL pipeline (`make hydrology`)  
and verified during CI/CD workflows.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/hydrology/
├── README.md
├── nhd_flowlines_ks.geojson.sha256
├── watersheds_huc12_ks.geojson.sha256
├── fema_nfhl_ks.geojson.sha256
├── groundwater_levels_ks.geojson.sha256
└── flood_events_ks.geojson.sha256
````

> **Note:** Each checksum corresponds to a data file in
> `data/processed/hydrology/` and is validated automatically in CI via `sha256sum -c`.

---

## 🔐 Purpose of Checksums

| Objective               | Description                                                                          |
| :---------------------- | :----------------------------------------------------------------------------------- |
| **Data Integrity**      | Confirms that GeoJSON and COG outputs remain unaltered after generation.             |
| **Reproducibility**     | Ensures identical outputs are regenerated from the same ETL inputs.                  |
| **Provenance Tracking** | Connects each checksum with its dataset’s STAC metadata and source descriptor.       |
| **CI Enforcement**      | GitHub Actions re-hash files during `stac-validate.yml` and stop merges on mismatch. |

---

## 🧮 Example `.sha256` File

```bash
# File: watersheds_huc12_ks.geojson.sha256
d2a9e4b1f97c3aa923f9025b2cf2058c477f01e8c024a07f68b992b04d789e5f  watersheds_huc12_ks.geojson
```

This file represents the hash for
`data/processed/hydrology/watersheds_huc12_ks.geojson`.

---

## ⚙️ Checksum Generation Workflow

Checksums are created automatically at the end of each hydrology ETL run.

**Makefile target:**

```bash
make hydrology-checksums
```

**Equivalent Python command:**

```bash
python src/utils/generate_checksums.py data/processed/hydrology/ --algo sha256
```

**Steps:**

1. Locate processed hydrology datasets (`.geojson`, `.tif`, `.csv`).
2. Compute SHA-256 hash for each file.
3. Save `<filename>.sha256` in this folder.
4. Validate hashes during CI/CD builds.

---

## 🧰 Validation in CI/CD

Checksum validation occurs automatically in GitHub Actions:

```bash
sha256sum -c data/processed/checksums/hydrology/*.sha256
```

If a mismatch occurs, the workflow fails — preventing merge or deployment
until the affected data is re-processed and re-hashed.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                                | Purpose                                                          |
| :---------------------------------------------- | :--------------------------------------------------------------- |
| `data/processed/metadata/hydrology/`            | STAC items reference these checksums for integrity verification  |
| `src/pipelines/hydrology/hydrology_pipeline.py` | Generates and validates SHA-256 hashes post-processing           |
| `.github/workflows/stac-validate.yml`           | CI job verifying that current file hashes match stored checksums |
| `data/stac/hydrology/`                          | Metadata cross-references checksum files in asset properties     |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                           |
| :---------------------- | :------------------------------------------------------- |
| **Documentation-first** | Every hydrology output has a checksum and metadata entry |
| **Reproducibility**     | Hash validation ensures deterministic ETL results        |
| **Open Standards**      | Uses FIPS-approved SHA-256 hashing algorithm             |
| **Provenance**          | Hashes linked to dataset STAC items and source configs   |
| **Auditability**        | CI validation logs checksum matches for every artifact   |

---

## 📅 Version History

| Version | Date       | Summary                                                               |
| :------ | :--------- | :-------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of hydrology checksum documentation and SHA-256 files |

---

<div align="center">

**Kansas Frontier Matrix** — *“Flowing Data, Verified Integrity.”*
📍 [`data/processed/checksums/hydrology/`](.) · Linked to the **Hydrology STAC Collection**

</div>
