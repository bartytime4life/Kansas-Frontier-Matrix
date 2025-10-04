<div align="center">

# 📊 Kansas Frontier Matrix — Tabular Checksums  
`data/processed/checksums/tabular/`

**Mission:** Ensure the **integrity, provenance, and reproducibility** of all processed tabular datasets  
within Kansas Frontier Matrix — protecting structured data such as census, agricultural, and economic tables  
from corruption and guaranteeing consistent analytical outputs.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum files (`.sha256`)** for all processed **tabular datasets**  
in the Kansas Frontier Matrix (KFM).  

Checksums provide cryptographic verification that CSV and Parquet files have not been altered since processing,  
linking the data to its provenance chain and guaranteeing reproducibility across environments.

All checksum files are generated automatically during the **tabular ETL pipeline** (`make tabular`)  
and validated continuously through GitHub Actions.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/tabular/
├── README.md
├── census_population_1860_2020.parquet.sha256
├── agricultural_production_1870_2020.parquet.sha256
└── economic_indicators_1900_2025.parquet.sha256
````

> **Note:** Each `.sha256` file represents a verified SHA-256 hash for its matching dataset
> in `data/processed/tabular/` and is automatically re-checked during CI builds.

---

## 🔐 Purpose of Checksums

| Objective                  | Description                                                        |
| :------------------------- | :----------------------------------------------------------------- |
| **Integrity Verification** | Detects any change or corruption in structured tabular files.      |
| **Reproducibility**        | Confirms that ETL outputs are identical across runs and systems.   |
| **Provenance Tracking**    | Links each hash to its metadata and STAC entry for transparency.   |
| **Automation in CI**       | GitHub Actions re-hash all tabular datasets to prevent divergence. |

---

## 🧮 Example `.sha256` File

```bash
# File: census_population_1860_2020.parquet.sha256
0d1e13dbde8fca82e7bc2184c23a7e231eb5b74b6e38e72df47f60bde8e54ccf  census_population_1860_2020.parquet
```

This file verifies the authenticity of
`data/processed/tabular/census_population_1860_2020.parquet`.

---

## ⚙️ Checksum Generation Workflow

Checksums are produced as part of the tabular ETL process.

**Makefile target:**

```bash
make tabular-checksums
```

**Equivalent Python command:**

```bash
python src/utils/generate_checksums.py data/processed/tabular/ --algo sha256
```

**Workflow Steps:**

1. Locate all processed tabular outputs (`.csv`, `.parquet`).
2. Compute SHA-256 hashes using Python’s `hashlib` library.
3. Write each hash to `<filename>.sha256` within this folder.
4. Validate automatically in CI/CD pipelines.

---

## 🧰 CI/CD Validation

Checksum verification runs on every build and deployment.

```bash
sha256sum -c data/processed/checksums/tabular/*.sha256
```

If a mismatch is detected, the pipeline halts and flags the dataset
for re-processing to maintain MCP reproducibility guarantees.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                       |
| :------------------------------------------ | :------------------------------------------------------------ |
| `data/processed/metadata/tabular/`          | Metadata JSON files reference checksums in their STAC assets  |
| `src/pipelines/tabular/tabular_pipeline.py` | Handles checksum generation and re-validation                 |
| `.github/workflows/stac-validate.yml`       | Runs checksum and STAC validation as part of CI               |
| `data/stac/tabular/`                        | STAC catalog contains hash provenance for tabular collections |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                               |
| :---------------------- | :----------------------------------------------------------- |
| **Documentation-first** | Each dataset includes README and `.sha256` record            |
| **Reproducibility**     | Deterministic ETL + verified hashes ensure identical results |
| **Open Standards**      | SHA-256 (FIPS 180-4) algorithm for all checksum operations   |
| **Provenance**          | Hashes tied to STAC and metadata lineage                     |
| **Auditability**        | CI logs all validations, creating a traceable audit trail    |

---

## 📅 Version History

| Version | Date       | Summary                                                          |
| :------ | :--------- | :--------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of tabular checksum documentation and hash files |

---

<div align="center">

**Kansas Frontier Matrix** — *“Verifying Every Figure: Integrity in the Numbers.”*
📍 [`data/processed/checksums/tabular/`](.) · Linked to the **Tabular STAC Collection**

</div>
