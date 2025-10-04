<div align="center">

# 🧾 Kansas Frontier Matrix — Tabular Checksums  
`data/processed/tabular/checksums/`

**Mission:** Ensure **data integrity, reproducibility, and provenance** for all processed tabular datasets  
in the Kansas Frontier Matrix — including historical census, agricultural, and economic time-series —  
by maintaining SHA-256 checksums for every file under version control and continuous validation.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder stores **SHA-256 checksum files (`.sha256`)**  
for all tabular datasets processed within the Kansas Frontier Matrix (KFM).

Checksums provide a cryptographic fingerprint for each structured dataset, enabling:
- **Integrity verification** — ensuring no accidental or unauthorized file modification.  
- **Reproducibility** — validating that identical results are generated across ETL environments.  
- **Provenance tracking** — linking data artifacts to their metadata and STAC entries.  
- **Automated CI enforcement** — guaranteeing that datasets are immutable once validated.

Checksums are generated automatically by the **tabular ETL pipeline** (`make tabular`)  
and verified during GitHub Actions CI workflows.

---

## 🗂️ Directory Layout

```bash
data/processed/tabular/checksums/
├── README.md
├── census_population_1860_2020.parquet.sha256
├── agricultural_production_1870_2020.parquet.sha256
└── economic_indicators_1900_2025.parquet.sha256
````

> **Note:** Each `.sha256` file records the SHA-256 hash for a corresponding dataset in
> `data/processed/tabular/` and is automatically validated during each CI build.

---

## 🔐 Purpose of Checksums

| Objective            | Description                                                           |
| :------------------- | :-------------------------------------------------------------------- |
| **Data Integrity**   | Detects file corruption, unauthorized modification, or version drift. |
| **Reproducibility**  | Confirms that identical results are produced by the ETL pipeline.     |
| **Provenance Chain** | Connects each dataset to its metadata and STAC records.               |
| **Automation in CI** | GitHub Actions automatically verify checksum validity on every run.   |

---

## 🧮 Example `.sha256` File

```bash
# File: census_population_1860_2020.parquet.sha256
ca03d2fb389314a0ee43525a0eac0b422518a329c8a6f4c482c6c0a12cbb6aa7  census_population_1860_2020.parquet
```

This hash verifies the integrity of
`data/processed/tabular/census_population_1860_2020.parquet`.

---

## ⚙️ Checksum Generation Workflow

Checksums are created as part of the tabular ETL process or can be regenerated manually.

**Makefile target:**

```bash
make tabular-checksums
```

**Python command:**

```bash
python src/utils/generate_checksums.py data/processed/tabular/ --algo sha256
```

**Workflow Steps:**

1. Locate tabular outputs (`.csv`, `.parquet`, `.json`).
2. Compute SHA-256 hashes using `hashlib`.
3. Save each hash to a file in this directory.
4. Validate hashes automatically during CI/CD builds.

---

## 🧰 CI/CD Validation

Checksum verification is enforced via continuous integration pipelines.

**Validation command:**

```bash
sha256sum -c data/processed/tabular/checksums/*.sha256
```

If any hash mismatch is detected, the workflow fails —
ensuring that data artifacts are immutable and reproducible.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                          |
| :------------------------------------------ | :--------------------------------------------------------------- |
| `data/processed/tabular/metadata/`          | Metadata JSON files reference these checksum files.              |
| `src/pipelines/tabular/tabular_pipeline.py` | Generates and verifies checksum values during ETL.               |
| `.github/workflows/stac-validate.yml`       | CI workflow that revalidates hashes and metadata integrity.      |
| `data/stac/tabular/`                        | STAC catalog embeds checksum references for provenance tracking. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | Every dataset includes a checksum and metadata file.                    |
| **Reproducibility**     | Deterministic ETL process ensures stable output hashes.                 |
| **Open Standards**      | SHA-256 (FIPS 180-4) for cryptographic verification.                    |
| **Provenance**          | Hashes form an immutable link between data, metadata, and STAC records. |
| **Auditability**        | Automated CI/CD verification logs ensure accountability.                |

---

## 📅 Version History

| Version | Date       | Summary                                                                             |
| :------ | :--------- | :---------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial tabular checksum release — population, agricultural, and economic datasets. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity in Every Record: Verifying Data Through Time.”*
📍 [`data/processed/tabular/checksums/`](.) · Linked to the **Tabular STAC Collection**

</div>
