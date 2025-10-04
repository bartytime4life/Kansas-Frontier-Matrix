<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate Checksums  
`data/checksums/climate/`

**Mission:** Guarantee the **integrity, reproducibility, and provenance** of all processed climate datasets —  
including temperature, precipitation, and drought indices — across the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory holds **SHA-256 checksum files (`.sha256`)**  
for all processed **climate datasets** within the Kansas Frontier Matrix.  

Checksums serve as cryptographic fingerprints, ensuring:
- **Integrity** — Each dataset remains unaltered post-processing.  
- **Reproducibility** — The same ETL process yields identical results.  
- **Provenance** — Datasets can be traced through their metadata and STAC references.  
- **Auditability** — Every file is verified during CI/CD validation workflows.  

All checksum files are generated automatically during the climate ETL process (`make climate`)  
and re-validated through GitHub Actions.

---

## 🗂️ Directory Layout

```bash
data/checksums/climate/
├── README.md
├── daymet_1980_2024.tif.sha256
├── noaa_normals_1991_2020.geojson.sha256
└── drought_monitor_2000_2025.tif.sha256
````

> **Note:** Each `.sha256` file corresponds to its dataset in
> `data/processed/climate/` and is validated automatically via `sha256sum -c` in CI.

---

## 🔐 Purpose of Checksums

| Objective           | Description                                                                 |
| :------------------ | :-------------------------------------------------------------------------- |
| **Data Integrity**  | Detects any accidental corruption or tampering of raster or vector data.    |
| **Reproducibility** | Confirms that pipeline re-runs produce identical datasets.                  |
| **Provenance**      | Maintains a verifiable lineage between raw data, metadata, and STAC assets. |
| **Automation**      | CI/CD workflows continuously validate hashes for every dataset.             |

---

## 🧮 Example `.sha256` File

```bash
# File: daymet_1980_2024.tif.sha256
a7f9132dfe5b16c9783f3f0ec4a2f4da8a9bb5e7b739c3477325dcb0df836f41  daymet_1980_2024.tif
```

This file verifies the integrity of
`data/processed/climate/daymet_1980_2024.tif`.

---

## ⚙️ Checksum Generation Workflow

Checksums are created automatically as part of the ETL pipeline.

**Makefile target:**

```bash
make climate-checksums
```

**Python command:**

```bash
python src/utils/generate_checksums.py data/processed/climate/ --algo sha256
```

**Workflow Steps:**

1. Locate processed climate outputs (`.tif`, `.geojson`).
2. Compute SHA-256 hashes using Python’s `hashlib`.
3. Write `<filename>.sha256` files to this directory.
4. Validate checksums during CI/CD runs.

---

## 🧰 CI/CD Validation

Checksum verification is integrated into the project’s automated validation workflows.

**Command used in CI:**

```bash
sha256sum -c data/checksums/climate/*.sha256
```

**Behavior:**

* If any file hash fails, CI stops immediately.
* Maintainers must regenerate the dataset and its checksum before merging.
* Logs capture all verification events for reproducibility tracking.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                             |
| :------------------------------------------ | :------------------------------------------------------------------ |
| `data/processed/metadata/climate/`          | STAC items reference checksums for validation.                      |
| `src/pipelines/climate/climate_pipeline.py` | Generates and verifies SHA-256 hashes during ETL.                   |
| `.github/workflows/stac-validate.yml`       | CI job that re-validates climate dataset integrity.                 |
| `data/stac/climate/`                        | STAC catalog embeds checksum references for global reproducibility. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                          |
| :---------------------- | :------------------------------------------------------ |
| **Documentation-first** | Each dataset has an accompanying `.sha256` and README.  |
| **Reproducibility**     | Deterministic ETL outputs verified via SHA-256.         |
| **Open Standards**      | Uses SHA-256 (FIPS 180-4) cryptographic hashing.        |
| **Provenance**          | Checksum connects raw data → processed data → metadata. |
| **Auditability**        | CI/CD pipelines log verification for every dataset.     |

---

## 📅 Version History

| Version | Date       | Summary                                                                                               |
| :------ | :--------- | :---------------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial climate checksum documentation — Daymet, NOAA Normals, and Drought Monitor datasets verified. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity in Every Forecast: Verifying the Climate of Record.”*
📍 [`data/checksums/climate/`](.) · Linked to the **Climate STAC Collection**

</div>
