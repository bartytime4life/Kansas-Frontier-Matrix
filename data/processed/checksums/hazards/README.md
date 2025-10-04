<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards Checksums  
`data/processed/checksums/hazards/`

**Mission:** Maintain and verify the **integrity, provenance, and reproducibility**  
of all processed natural hazard datasets — including tornadoes, floods, wildfires, and drought layers —  
within the Kansas Frontier Matrix data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum files (`.sha256`)**  
for all processed **hazard datasets** in Kansas Frontier Matrix (KFM).  

Checksums serve as cryptographic fingerprints that ensure:
- **Data integrity** — confirming no corruption or tampering has occurred.  
- **Reproducibility** — verifying that ETL outputs are identical across runs.  
- **Provenance** — linking each hazard dataset to its metadata and STAC record.  
- **Auditability** — providing traceable verification within continuous integration workflows.  

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/hazards/
├── README.md
├── tornado_tracks_1950_2024.geojson.sha256
├── flood_events_1900_2025.geojson.sha256
├── wildfire_perimeters_2000_2024.geojson.sha256
└── drought_index_2000_2025.tif.sha256
````

> **Note:** Each `.sha256` file corresponds directly to its dataset in
> `data/processed/hazards/` and is automatically validated in CI workflows via `sha256sum -c`.

---

## 🔐 Purpose of Checksums

| Objective                  | Description                                                              |
| :------------------------- | :----------------------------------------------------------------------- |
| **Integrity Verification** | Detects data corruption or modification post-processing.                 |
| **Reproducibility**        | Ensures ETL pipeline outputs are consistent and deterministic.           |
| **Provenance**             | Connects each dataset to its metadata, STAC entry, and source reference. |
| **CI Enforcement**         | Integrated into GitHub Actions; builds fail on checksum mismatches.      |

---

## 🧮 Example `.sha256` File

```bash
# File: tornado_tracks_1950_2024.geojson.sha256
8fb29cda3d0e44182f26c7bceff74b2c81b83e742d47d836b33151f871bb69d1  tornado_tracks_1950_2024.geojson
```

This checksum authenticates the dataset
`data/processed/hazards/tornado_tracks_1950_2024.geojson`.

---

## ⚙️ Checksum Generation Workflow

Checksums are generated automatically as part of the hazards ETL process.

**Makefile target:**

```bash
make hazards-checksums
```

**Equivalent Python command:**

```bash
python src/utils/generate_checksums.py data/processed/hazards/ --algo sha256
```

**Steps:**

1. Identify all processed hazard files (`.geojson`, `.tif`, `.csv`).
2. Compute their SHA-256 hashes using the `hashlib` library.
3. Output `<filename>.sha256` files into this directory.
4. Validate these hashes as part of CI/CD pipelines.

---

## 🧰 CI/CD Validation

Checksum validation runs automatically in GitHub Actions workflows.

**Example validation command:**

```bash
sha256sum -c data/processed/checksums/hazards/*.sha256
```

If any hash mismatch is detected, the workflow fails — halting commits or deploys
until the affected dataset is rebuilt and re-hashed.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                              |
| :------------------------------------------ | :------------------------------------------------------------------- |
| `data/processed/metadata/hazards/`          | STAC items reference checksum files for data verification            |
| `src/pipelines/hazards/hazards_pipeline.py` | Handles generation and validation of hashes                          |
| `.github/workflows/stac-validate.yml`       | CI job re-verifying all hashes automatically                         |
| `data/stac/hazards/`                        | STAC catalog embeds checksum references in each asset metadata entry |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | Each hazard dataset has an accompanying checksum and STAC record |
| **Reproducibility**     | Deterministic ETL outputs verified via hashes                    |
| **Open Standards**      | Uses SHA-256 (FIPS 180-4 compliant cryptographic algorithm)      |
| **Provenance**          | Checksum links connect source → processed → metadata             |
| **Auditability**        | CI pipelines verify every checksum during validation             |

---

## 📅 Version History

| Version | Date       | Summary                                                                                    |
| :------ | :--------- | :----------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hazards checksum release — includes tornado, flood, wildfire, and drought datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Storm Verified: Data Integrity for a Changing Kansas.”*
📍 [`data/processed/checksums/hazards/`](.) · Linked to the **Hazards STAC Collection**

</div>
