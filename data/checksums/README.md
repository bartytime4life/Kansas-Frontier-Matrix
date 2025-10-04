<div align="center">

# 🔐 Kansas Frontier Matrix — Global Data Checksums  
`data/checksums/`

**Mission:** Ensure **project-wide data integrity, reproducibility, and provenance**  
for all datasets within the Kansas Frontier Matrix (KFM) through comprehensive SHA-256 checksum tracking and validation.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/checksums/` directory serves as the **central verification registry**  
for all SHA-256 checksum manifests used across the Kansas Frontier Matrix.  

These checksum files guarantee:
- **Data integrity** across all datasets (raw, processed, tabular, spatial, text).  
- **Reproducibility** of ETL pipelines across environments and versions.  
- **Provenance tracking** through immutable hash references.  
- **Auditability** for every dataset committed to the repository.  

Every subdirectory under `data/processed/**/checksums/` contributes its hash records to this master catalog.

---

## 🗂️ Directory Layout

```bash
data/checksums/
├── README.md
├── terrain/manifest.sha256
├── hydrology/manifest.sha256
├── landcover/manifest.sha256
├── climate/manifest.sha256
├── hazards/manifest.sha256
├── tabular/manifest.sha256
└── text/manifest.sha256
````

> **Note:** Each `manifest.sha256` consolidates the verified hashes from its domain
> (e.g., terrain, hydrology, landcover).
> These manifests are regenerated during pipeline runs and validated in CI/CD workflows.

---

## 🧾 Manifest Description

| Manifest File               | Description                                                                          |
| :-------------------------- | :----------------------------------------------------------------------------------- |
| `terrain/manifest.sha256`   | Aggregated checksums for DEMs, hillshades, slope/aspect rasters.                     |
| `hydrology/manifest.sha256` | Hashes for hydrologic datasets: rivers, watersheds, groundwater, flood zones.        |
| `landcover/manifest.sha256` | Checksums for vegetation, NLCD, crop distribution, and land use change layers.       |
| `climate/manifest.sha256`   | Validation hashes for temperature, precipitation, and drought rasters.               |
| `hazards/manifest.sha256`   | Hashes for tornado, flood, wildfire, and drought hazard data.                        |
| `tabular/manifest.sha256`   | CSV/Parquet checksum records for structured data (population, agriculture, economy). |
| `text/manifest.sha256`      | Verifies OCR and NLP text files (newspapers, oral histories, treaties).              |

---

## ⚙️ Checksum Generation Workflow

All manifests are generated automatically during the build process.

**Makefile target:**

```bash
make checksums
```

**Python command:**

```bash
python src/utils/generate_global_checksums.py data/ --algo sha256
```

**Steps:**

1. Traverse all subdirectories of `data/processed/`.
2. Compute SHA-256 hashes for every dataset (`.tif`, `.geojson`, `.csv`, `.parquet`, `.jsonl`).
3. Consolidate hashes by domain into manifest files under `data/checksums/`.
4. Validate manifests via CI/CD (using `sha256sum -c`).

---

## 🧮 Example `manifest.sha256` Entry

```bash
# File: terrain/manifest.sha256
f3c0b929a38ef47c7b41138dd726abf84a65a03b8b24e8e12db2fa89a5740c42  data/processed/terrain/ks_1m_dem_2018_2020.tif
b84b732cc9a2c62f1430b43e813cf7768e2f3452a5de003bfcbf7a72962290a4  data/processed/terrain/ks_hillshade_2018_2020.tif
fe91df2adf373b9cfcd23a9a6cc3a219ae56c92e728c4fcb8333abfa08c48a02  data/processed/terrain/slope_aspect_2018_2020.tif
```

---

## 🧰 CI/CD Validation

Checksum verification is part of the **STAC validation and deployment pipelines**.

**CI Command:**

```bash
sha256sum -c data/checksums/**/*.sha256
```

**Behavior:**

* CI fails on any mismatch between the computed and stored hash values.
* Prevents deployment or publication of modified/unverified data.
* Logs validation results for transparency and auditability.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                         | Purpose                                                                    |
| :--------------------------------------- | :------------------------------------------------------------------------- |
| `data/processed/**/metadata/`            | Metadata JSON includes hash values via `"checksum:sha256"` in STAC assets. |
| `src/utils/generate_global_checksums.py` | Aggregates subdirectory hashes into global manifests.                      |
| `.github/workflows/stac-validate.yml`    | Validates integrity of all datasets and STAC references.                   |
| `data/stac/`                             | STAC catalog references manifest checksums for global reproducibility.     |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                    |
| :---------------------- | :---------------------------------------------------------------- |
| **Documentation-first** | Global checksum manifest documented in this README.               |
| **Reproducibility**     | Hashes ensure consistent dataset integrity across environments.   |
| **Open Standards**      | SHA-256 (FIPS 180-4) cryptographic algorithm used for all checks. |
| **Provenance**          | Manifest provides dataset-level lineage and traceable validation. |
| **Auditability**        | Automated CI/CD checks prevent divergence from validated data.    |

---

## 📅 Version History

| Version | Date       | Summary                                                                   |
| :------ | :--------- | :------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial creation of global checksum manifests for all dataset categories. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity Across Time and Terrain.”*
📍 [`data/checksums/`](.) · Global registry for dataset integrity and provenance validation.

</div>
