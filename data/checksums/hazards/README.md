<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards Checksums  
`data/checksums/hazards/`

**Mission:** Guarantee **integrity, reproducibility, and provenance** of all processed **natural hazard datasets** —  
including tornado tracks, floods, wildfires, drought indices, and disaster declarations — through **SHA-256 validation**  
and continuous CI/CD verification within the Kansas Frontier Matrix (KFM) ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **SHA-256 checksum files (`.sha256`)** for all **hazard datasets**  
processed within the Kansas Frontier Matrix (KFM).  

These cryptographic fingerprints verify that hazard data — from tornado paths to drought layers — remain  
unaltered, reproducible, and transparent across the full MCP-compliant data lifecycle.

**Checksums enforce:**

- 🧱 **Integrity** — Detects corruption or unauthorized file changes.  
- 🔁 **Reproducibility** — Ensures deterministic ETL outputs across rebuilds.  
- 🧩 **Provenance** — Links each asset directly to metadata and STAC references.  
- 🔍 **Auditability** — Enables automated validation and historical tracking through CI/CD logs.  

All `.sha256` files are automatically generated during the **Hazards ETL process (`make hazards`)**  
and validated continuously during GitHub Action workflows.

---

## 🗂️ Directory Layout

```bash
data/checksums/hazards/
├── README.md
├── tornado_tracks_1950_2024.geojson.sha256
├── flood_events_1900_2025.geojson.sha256
├── wildfire_perimeters_2000_2024.geojson.sha256
├── drought_index_2000_2025.tif.sha256
└── fema_disaster_declarations_1953_2025.csv.sha256
````

> **Note:** Each `.sha256` file corresponds to a dataset in
> `data/processed/hazards/` and is verified via `sha256sum -c` in CI/CD validation jobs.

---

## 🔐 Checksum Purpose and Role

| Objective              | Description                                                                                  |
| :--------------------- | :------------------------------------------------------------------------------------------- |
| **Integrity Check**    | Detects accidental corruption, missing bytes, or unauthorized edits to hazard data.          |
| **Reproducibility**    | Confirms consistent ETL output when pipelines re-run under identical conditions.             |
| **Provenance Linkage** | Maintains verifiable connection between datasets, STAC metadata, and checksum registry.      |
| **Automation**         | Continuous verification ensures early detection of data drift or processing errors.          |
| **Transparency**       | Promotes scientific and operational accountability for hazard datasets used in public tools. |

---

## 🧮 Example `.sha256` File

```bash
# File: tornado_tracks_1950_2024.geojson.sha256
8fb29cda3d0e44182f26c7bceff74b2c81b83e742d47d836b33151f871bb69d1  tornado_tracks_1950_2024.geojson
```

The above verifies that the **Tornado Tracks** layer
(`data/processed/hazards/tornado_tracks_1950_2024.geojson`) matches its canonical hash.

---

## ⚙️ Checksum Generation Workflow

Checksums are produced automatically during pipeline execution or can be manually triggered.

**Makefile target:**

```bash
make hazards-checksums
```

**Python CLI:**

```bash
python src/utils/generate_checksums.py data/processed/hazards/ --algo sha256
```

**Workflow Steps:**

1. Identify all processed hazard outputs (`.geojson`, `.tif`, `.csv`).
2. Compute SHA-256 hashes using Python’s `hashlib` for deterministic output.
3. Write `<filename>.sha256` files to this directory.
4. Verify all checksums via `sha256sum -c` in CI/CD pipelines.
5. Log validation results in `data/work/logs/hazards_checksums.log`.

---

## 🧰 CI/CD Validation

Checksum validation is enforced in the **KFM automated workflows** to prevent propagation of corrupted or outdated data.

**Command executed in CI:**

```bash
sha256sum -c data/checksums/hazards/*.sha256
```

**Validation behavior:**

* ❌ A failed hash triggers a workflow error and blocks deployment.
* 🔁 Datasets must be regenerated (`make hazards`) and checksums recomputed.
* 📜 Validation logs are archived in `data/work/logs/` for reproducibility and peer review.

---

## 🔗 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                                 |
| :------------------------------------ | :---------------------------------------------------------------------- |
| `data/processed/metadata/hazards/`    | Embeds `"checksum:sha256"` values in STAC assets.                       |
| `src/pipelines/hazards_pipeline.py`   | Automates checksum generation post-processing.                          |
| `.github/workflows/stac-validate.yml` | Revalidates STAC + checksum consistency in every PR or push.            |
| `data/stac/hazards/`                  | STAC catalog stores checksum links for discovery and integrity tracing. |
| `data/checksums/manifest.sha256`      | Global manifest references domain-level checksums for full validation.  |

---

## 🧩 Troubleshooting & Common Issues

| Issue                        | Likely Cause                                             | Resolution                                                        |
| :--------------------------- | :------------------------------------------------------- | :---------------------------------------------------------------- |
| **CI fails on mismatch**     | Dataset modified or rebuilt without updating hash.       | Re-run `make hazards-checksums` and commit regenerated checksums. |
| **File missing in manifest** | New hazard dataset added but checksum not yet generated. | Add checksum via `python src/utils/generate_checksums.py`.        |
| **Checksum drift from STAC** | STAC metadata not refreshed after reprocessing.          | Run `make stac` to sync hashes with STAC Items.                   |
| **Inconsistent file paths**  | Relative path formatting inconsistency (`\` vs `/`).     | Normalize paths to POSIX in `.sha256` files.                      |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | Each dataset includes an accompanying `.sha256` record and README. |
| **Reproducibility**     | Deterministic SHA-256 ensures identical outputs across rebuilds.   |
| **Open Standards**      | Employs FIPS 180-4 SHA-256 hashing, integrated with STAC schema.   |
| **Provenance**          | Connects data lineage across ETL, metadata, and STAC catalogs.     |
| **Auditability**        | CI/CD workflows log and enforce checksum verification globally.    |

---

## 📅 Version History

| Version | Date       | Summary                                                                                           |
| :------ | :--------- | :------------------------------------------------------------------------------------------------ |
| v1.0.0  | 2025-10-04 | Initial hazards checksum documentation — tornado, flood, wildfire, and drought datasets verified. |
| v1.1.0  | 2025-10-10 | Added FEMA disaster checksums, enhanced CI/STAC integration, troubleshooting, and log references. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Storm Verified: Integrity Through Time.”*
📍 [`data/checksums/hazards/`](.) · Linked to the **Hazards STAC Collection** and Global Manifest Registry.

</div>
```
