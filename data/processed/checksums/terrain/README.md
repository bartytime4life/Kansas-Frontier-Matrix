<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain Checksums  
`data/processed/checksums/terrain/`

**Mission:** Ensure **integrity and reproducibility** of all processed terrain datasets  
through SHA-256 checksum tracking and validation — in accordance with MCP provenance standards.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **checksum files (`.sha256`)** for every processed **terrain dataset**  
in Kansas Frontier Matrix (KFM).  

Checksums ensure:
- **Data integrity:** Detect accidental or unauthorized file modifications  
- **Reproducibility:** Verify outputs match the expected pipeline results  
- **Traceability:** Maintain a cryptographic audit trail between source, transform, and output  

Checksums are generated automatically by the ETL pipeline (`make terrain`) and validated in CI workflows.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/terrain/
├── README.md
├── ks_1m_dem_2018_2020.tif.sha256
├── ks_hillshade_2018_2020.tif.sha256
├── slope_aspect_2018_2020.tif.sha256
└── usgs_topo_larned_1894.tif.sha256
````

> **Note:** Each `.sha256` file stores the SHA-256 hash for its corresponding raster in
> `data/processed/terrain/`. These are verified during continuous integration (CI) checks.

---

## 🔐 Purpose of Checksums

| Objective                  | Description                                                                                        |
| :------------------------- | :------------------------------------------------------------------------------------------------- |
| **Integrity Verification** | Confirms that processed outputs (COGs, GeoJSONs) have not been altered or corrupted.               |
| **Reproducibility**        | Ensures identical outputs are generated from the same input and configuration.                     |
| **Traceability**           | Links every artifact to its corresponding STAC item and metadata entry.                            |
| **CI Enforcement**         | GitHub Actions (`stac-validate.yml`, `integrity-check.yml`) automatically verify checksum matches. |

---

## 🧮 Example `.sha256` File

```bash
# File: ks_1m_dem_2018_2020.tif.sha256
b8494ab6a3219c6a51e3de22804b329872c10f39ff8a4cf18ad4b3b61cb6ac8d  ks_1m_dem_2018_2020.tif
```

This file represents the SHA-256 hash for
`data/processed/terrain/ks_1m_dem_2018_2020.tif`.

---

## ⚙️ Checksum Generation Workflow

Checksums are created automatically after each ETL run using a Makefile target:

```bash
make terrain-checksums
```

Equivalent Python command:

```bash
python src/utils/generate_checksums.py data/processed/terrain/ --algo sha256
```

**Steps:**

1. Locate all terrain data outputs (`.tif`, `.json`, `.geojson`).
2. Compute SHA-256 hashes using the Python `hashlib` module.
3. Save results as `<filename>.sha256` in this folder.
4. Cross-validate against stored checksums during CI runs.

---

## 🧰 Validation in CI/CD

Checksum validation is built into the **STAC validation** and **Build & Deploy** workflows.

Example command from CI:

```bash
sha256sum -c data/processed/checksums/terrain/*.sha256
```

If any file hash fails verification, the workflow exits with an error, preventing merge or deploy.
This guarantees **data immutability** and **pipeline trust**.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                             |
| :------------------------------------------ | :-------------------------------------------------- |
| `data/processed/metadata/terrain/`          | Each STAC item references its checksum file         |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates and verifies hashes post-processing       |
| `.github/workflows/stac-validate.yml`       | CI job that re-hashes files and validates integrity |
| `data/stac/terrain/`                        | Metadata cross-reference to checksum filenames      |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                            |
| :---------------------- | :------------------------------------------------------------------------ |
| **Documentation-first** | Every terrain output has an associated `.sha256` file and metadata record |
| **Reproducibility**     | Checksums confirm deterministic ETL outputs                               |
| **Open Standards**      | SHA-256 cryptographic hash algorithm (FIPS 180-4)                         |
| **Provenance**          | Source → Processed → Checksum → STAC linkage                              |
| **Auditability**        | Continuous checksum validation in CI/CD pipelines                         |

---

## 📅 Version History

| Version | Date       | Summary                                                     |
| :------ | :--------- | :---------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of terrain checksum documentation and files |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity in Every Pixel: Verifying the Ground Truth.”*
📍 [`data/processed/checksums/terrain/`](.) · Linked to the **Terrain STAC Collection**

</div>
