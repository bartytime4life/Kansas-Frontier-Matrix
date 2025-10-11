<div align="center">

# 🌾 Kansas Frontier Matrix — Land Cover Checksums  
`data/checksums/landcover/`

**Mission:** Verify, preserve, and document the **integrity, reproducibility, and provenance**  
of all processed **land cover datasets** — including vegetation, NLCD, crop distribution, and land use change —  
to ensure transparent and auditable results across the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `data/checksums/landcover/` directory contains **SHA-256 cryptographic checksum files (`.sha256`)**  
for every **land cover dataset** processed within the Kansas Frontier Matrix (KFM).  

These checksums certify that data representing Kansas’s **vegetation, cropland, and surface change history**  
remains consistent, reproducible, and traceable through every stage of the MCP-governed data lifecycle.

**Guarantees provided:**
- 🌾 **Integrity** — Prevents silent data corruption or tampering.  
- 🔁 **Reproducibility** — Ensures deterministic ETL results across environments.  
- 🔗 **Provenance** — Connects every dataset to its metadata, STAC record, and source manifest.  
- 🧩 **Auditability** — Enables CI/CD workflows to verify and log dataset integrity automatically.  

All `.sha256` files are generated via the **landcover ETL pipeline (`make landcover`)**  
and validated during each continuous integration (CI) run.

---

## 🗂️ Directory Layout

```bash
data/checksums/landcover/
├── README.md
├── nlcd_1992_2021.tif.sha256
├── kansas_vegetation_1850s.tif.sha256
├── landcover_change_1992_2021.geojson.sha256
├── crop_distribution_2020.geojson.sha256
└── canopy_cover_2016.tif.sha256
````

> **Note:** Each `.sha256` file corresponds to its dataset in
> `data/processed/landcover/` and is validated automatically through CI using `sha256sum -c`.

---

## 🔐 Role of Checksums

| Objective                  | Description                                                                  |
| :------------------------- | :--------------------------------------------------------------------------- |
| **Integrity Verification** | Detects corruption or unauthorized alteration of land cover files.           |
| **Reproducibility**        | Confirms that re-running the ETL pipeline yields byte-identical results.     |
| **Provenance**             | Links processed layers to their metadata and STAC asset references.          |
| **Automation**             | CI/CD pipelines verify all hashes on every push, merge, and release build.   |
| **Transparency**           | Promotes open, scientific accountability through MCP-governed documentation. |

---

## 🧮 Example `.sha256` File

```bash
# File: nlcd_1992_2021.tif.sha256
1e8a2a99ef45f582f821a4b8ac3adcc48f0c52b7c1d7ce1f92f4cb045c54cc54  nlcd_1992_2021.tif
```

This file certifies the integrity of
`data/processed/landcover/nlcd_1992_2021.tif`
and ensures it matches the canonical version tracked in the repository.

---

## ⚙️ Generation Workflow

Checksums are created automatically upon ETL completion or can be executed manually.

**Makefile target:**

```bash
make landcover-checksums
```

**Python command:**

```bash
python src/utils/generate_checksums.py data/processed/landcover/ --algo sha256
```

**Workflow Steps:**

1. Identify all outputs in `data/processed/landcover/` (`.tif`, `.geojson`, `.csv`).
2. Compute SHA-256 digests using Python’s `hashlib`.
3. Write `<filename>.sha256` files into this directory.
4. Validate hashes during CI/CD workflows (`sha256sum -c`).
5. Archive logs to `data/work/logs/landcover_checksums.log` for peer audit.

---

## 🧰 CI/CD Validation

**CI command:**

```bash
sha256sum -c data/checksums/landcover/*.sha256
```

**Behavior:**

* ✅ Verified: All hashes match recorded values — dataset integrity confirmed.
* ❌ Failed: CI halts, logs failure, and blocks deployment until checksums are regenerated.
* 🧾 Logs: Validation details retained under `data/work/logs/` for reproducibility and compliance tracking.

These checks are tied to the **STAC validation workflow** (`.github/workflows/stac-validate.yml`)
to guarantee metadata and checksum parity.

---

## 🔗 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                              |
| :------------------------------------ | :------------------------------------------------------------------- |
| `data/processed/metadata/landcover/`  | STAC Items embed `"checksum:sha256"` per asset for validation.       |
| `src/pipelines/landcover_pipeline.py` | Generates, validates, and logs hashes as part of the ETL routine.    |
| `.github/workflows/stac-validate.yml` | Automates checksum and STAC validation across branches.              |
| `data/stac/landcover/`                | Catalog includes checksum values for global reproducibility.         |
| `data/checksums/manifest.sha256`      | Global manifest linking domain checksums across all data categories. |

---

## 🧩 Troubleshooting & Maintenance

| Issue                         | Likely Cause                                           | Resolution                                                    |
| :---------------------------- | :----------------------------------------------------- | :------------------------------------------------------------ |
| CI fails on checksum mismatch | Dataset modified without updated hash.                 | Run `make landcover-checksums` and recommit `.sha256` files.  |
| File missing from directory   | New dataset added but no checksum generated.           | Execute `python src/utils/generate_checksums.py`.             |
| STAC mismatch                 | STAC `checksum:sha256` value out of sync.              | Run `make stac` to refresh STAC metadata.                     |
| Non-deterministic output      | Randomized compression or timestamps in TIFF metadata. | Enforce deterministic GDAL settings; set `SOURCE_DATE_EPOCH`. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | Each dataset includes README and `.sha256` verification record.        |
| **Reproducibility**     | SHA-256 ensures deterministic validation across systems.               |
| **Open Standards**      | Employs SHA-256 (FIPS 180-4) and STAC Checksum extension.              |
| **Provenance**          | Links ETL outputs with metadata and STAC collections for traceability. |
| **Auditability**        | Continuous CI/CD validation with log retention ensures transparency.   |

---

## 📅 Version History

| Version | Date       | Summary                                                                                          |
| :------ | :--------- | :----------------------------------------------------------------------------------------------- |
| v1.0.0  | 2025-10-04 | Initial checksum documentation — NLCD, vegetation, crop, and land use change datasets verified.  |
| v1.1.0  | 2025-10-10 | Added canopy cover dataset, improved CI log integration, troubleshooting, and metadata linkages. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Pixel Proven: Verifying the Living Surface of Kansas.”*
📍 [`data/checksums/landcover/`](.) · Linked to the **Land Cover STAC Collection** and Global Manifest Registry.

</div>
```
