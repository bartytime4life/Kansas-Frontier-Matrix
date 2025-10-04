<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain Checksums  
`data/processed/terrain/checksums/`

**Mission:** Maintain and verify the **integrity, reproducibility, and provenance**  
of all processed terrain datasets in Kansas Frontier Matrix — ensuring that every elevation, hillshade,  
and derivative raster is cryptographically validated across builds and environments.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum files (`.sha256`)**  
for all processed **terrain datasets** under Kansas Frontier Matrix (KFM).  

Checksums ensure:
- **Integrity** — No corruption or unauthorized modification of raster datasets.  
- **Reproducibility** — Identical ETL outputs across processing environments.  
- **Provenance** — Verified linkage between processed files, metadata, and STAC items.  
- **Auditability** — Automatic verification through continuous integration (CI/CD) workflows.  

All checksum files are generated during the terrain ETL pipeline (`make terrain`)  
and validated automatically via GitHub Actions (`stac-validate.yml`).

---

## 🗂️ Directory Layout

```bash
data/processed/terrain/checksums/
├── README.md
├── ks_1m_dem_2018_2020.tif.sha256
├── ks_hillshade_2018_2020.tif.sha256
└── slope_aspect_2018_2020.tif.sha256
````

> **Note:** Each `.sha256` file corresponds to a raster dataset in
> `data/processed/terrain/` and is checked automatically via `sha256sum -c` in CI.

---

## 🔐 Purpose of Checksums

| Objective            | Description                                                          |
| :------------------- | :------------------------------------------------------------------- |
| **Data Integrity**   | Confirms no terrain raster has been corrupted, altered, or replaced. |
| **Reproducibility**  | Ensures ETL processes produce identical raster hashes.               |
| **Provenance Chain** | Links datasets to metadata, STAC, and source lineage.                |
| **CI Enforcement**   | Builds fail automatically when checksum mismatches occur.            |

---

## 🧮 Example `.sha256` File

```bash
# File: ks_1m_dem_2018_2020.tif.sha256
f3c0b929a38ef47c7b41138dd726abf84a65a03b8b24e8e12db2fa89a5740c42  ks_1m_dem_2018_2020.tif
```

This verifies the integrity of the DEM file
`data/processed/terrain/ks_1m_dem_2018_2020.tif`.

---

## ⚙️ Checksum Generation Workflow

Checksums are generated automatically by the terrain ETL pipeline.

**Makefile target:**

```bash
make terrain-checksums
```

**Python command:**

```bash
python src/utils/generate_checksums.py data/processed/terrain/ --algo sha256
```

**Steps:**

1. Identify raster files (`.tif`, `.cog`, `.geojson`).
2. Compute SHA-256 hashes via Python’s `hashlib`.
3. Save `<filename>.sha256` to this directory.
4. Validate integrity in CI/CD workflows after each pipeline run.

---

## 🧰 CI/CD Validation

Checksum validation occurs automatically in GitHub Actions workflows.

**Example validation command:**

```bash
sha256sum -c data/processed/terrain/checksums/*.sha256
```

If any mismatch is detected, the build fails — enforcing full dataset reproducibility
and preventing propagation of unverified raster files.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                              |
| :------------------------------------------ | :------------------------------------------------------------------- |
| `data/processed/terrain/metadata/`          | Metadata JSON files link to checksums via STAC `"assets"`            |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates and verifies hashes during ETL runs                        |
| `.github/workflows/stac-validate.yml`       | Automates checksum and STAC validation                               |
| `data/stac/terrain/`                        | STAC items embed checksum info for catalog-level provenance tracking |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                 |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | README and `.sha256` for every dataset                         |
| **Reproducibility**     | Identical terrain outputs validated via checksum comparison    |
| **Open Standards**      | SHA-256 (FIPS 180-4) cryptographic algorithm                   |
| **Provenance**          | Checksum forms part of dataset’s documented lineage            |
| **Auditability**        | CI verification logs and checksum tracking ensure transparency |

---

## 📅 Version History

| Version | Date       | Summary                                                                                      |
| :------ | :--------- | :------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial terrain checksum documentation — DEM, hillshade, and slope/aspect datasets verified. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity in Elevation: Every Surface Verified.”*
📍 [`data/processed/terrain/checksums/`](.) · Linked to the **Terrain STAC Collection**

</div>
