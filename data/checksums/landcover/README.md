<div align="center">

# 🌾 Kansas Frontier Matrix — Land Cover Checksums  
`data/checksums/landcover/`

**Mission:** Verify, preserve, and document the **integrity, reproducibility, and provenance**  
of all processed **land cover datasets** — including vegetation, NLCD, crop distribution, and land use change —  
ensuring transparent, auditable, and MCP-compliant results across the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../../.github/workflows/trivy.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `data/checksums/landcover/` directory holds **SHA-256 checksum manifests**  
for every **processed land cover dataset** in KFM — from historic vegetation reconstructions  
to recent NLCD mosaics and crop distribution analyses.  

These checksums act as the **digital fingerprint** ensuring every land cover layer  
remains reproducible, authentic, and verifiable through its lifecycle.

**Guarantees provided:**
- 🌾 **Integrity** — Detects corruption or unauthorized edits.  
- 🔁 **Reproducibility** — Confirms byte-for-byte identical ETL results.  
- 🔗 **Provenance** — Links all land cover products to metadata, STAC Items, and sources.  
- 🧩 **Auditability** — CI/CD continuously validates and logs data integrity.  

All `.sha256` files are produced via the **Landcover ETL pipeline (`make landcover`)**  
and verified automatically during each GitHub Actions build.

---

## 🧭 Land Cover Integrity Workflow

```mermaid
flowchart LR
  S["data/sources/landcover/*.json\nSource Manifests"] --> R["data/raw/landcover/**\nNLCD · Crops · Vegetation"]
  R --> P["src/pipelines/landcover_pipeline.py\nETL · Harmonize · Derive"]
  P --> O["data/processed/landcover/**\nCOG · GeoJSON · CSV"]
  O --> C["data/checksums/landcover/*.sha256\nIntegrity Proofs"]
  O --> T["data/stac/landcover/**.json\nSTAC Items (checksum:sha256)"]
  C --> V["CI Validation\nsha256sum -c + STAC parity"]
%% END OF MERMAID
````

<!-- END OF MERMAID -->

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
```

> Each `.sha256` references a dataset under `data/processed/landcover/`
> and is validated during CI via `sha256sum -c`.

---

## 🧮 Example `.sha256` File

```bash
# File: nlcd_1992_2021.tif.sha256
1e8a2a99ef45f582f821a4b8ac3adcc48f0c52b7c1d7ce1f92f4cb045c54cc54  nlcd_1992_2021.tif
```

This manifest certifies the integrity of
`data/processed/landcover/nlcd_1992_2021.tif`
and confirms its reproducibility across all builds and platforms.

---

## ⚙️ Generation Workflow

**Makefile target**

```bash
make landcover-checksums
```

**Python command**

```bash
python src/utils/generate_checksums.py data/processed/landcover/ --algo sha256
```

**Workflow Steps**

1. Scan `data/processed/landcover/` for `.tif`, `.geojson`, `.csv`.
2. Compute SHA-256 hashes with Python’s `hashlib` or `sha256sum`.
3. Save `<filename>.sha256` in this directory.
4. CI validates all hashes automatically.
5. Logs archived under `data/work/logs/landcover_checksums.log`.

---

## 🧰 CI/CD Validation

**Validation command**

```bash
sha256sum -c data/checksums/landcover/*.sha256
```

| Result         | Behavior                                                  |
| :------------- | :-------------------------------------------------------- |
| ✅ **Verified** | Integrity confirmed; build proceeds.                      |
| ❌ **Failed**   | Pipeline halts; dataset must be reprocessed and rehashed. |
| 🧾 **Logs**    | Stored in `data/work/logs/` for MCP audit traceability.   |

> This process runs within the **STAC validation workflow** (`.github/workflows/stac-validate.yml`)
> ensuring checksum–metadata parity before deployment.

---

## 🔗 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                      |
| :------------------------------------ | :----------------------------------------------------------- |
| `data/stac/landcover/**.json`         | STAC Items include `"checksum:sha256"` for each dataset.     |
| `data/processed/metadata/landcover/`  | Mirrors checksum and provenance details for non-STAC layers. |
| `src/pipelines/landcover_pipeline.py` | Generates, verifies, and logs checksum events.               |
| `.github/workflows/stac-validate.yml` | Validates checksum–STAC consistency in CI/CD.                |
| `data/checksums/manifest.sha256`      | Global registry aggregating all landcover digests.           |

---

## 🧩 Troubleshooting & Maintenance

| Issue                        | Likely Cause                             | Resolution                                             |
| :--------------------------- | :--------------------------------------- | :----------------------------------------------------- |
| CI fails checksum validation | File changed or re-exported post-ETL     | Run `make landcover-checksums` and recommit hashes.    |
| Missing `.sha256`            | New dataset added without checksum       | Execute generator manually and add file.               |
| STAC mismatch                | STAC entry out of sync with checksum     | Run `make stac` or sync via CI validator.              |
| Non-deterministic TIFFs      | Metadata timestamps or compression drift | Use `SOURCE_DATE_EPOCH`, pin GDAL compression options. |

---

## 🧠 MCP Compliance Matrix

| MCP Principle           | Implementation                                      |
| :---------------------- | :-------------------------------------------------- |
| **Documentation-first** | Every dataset includes README + checksum record.    |
| **Reproducibility**     | SHA-256 hashing ensures deterministic verification. |
| **Open Standards**      | FIPS 180-4, STAC Checksum extension, UTF-8 paths.   |
| **Provenance**          | ETL outputs tied to metadata and STAC items.        |
| **Auditability**        | CI/CD gates, logs, and retention policies applied.  |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                                         |
| :------- | :--------- | :-------------------------------------------------------------------------------------------------------------- |
| **v1.2** | 2025-10-11 | Protocol v1.1 upgrade: front-matter, Mermaid workflow, CI parity enforcement, compression determinism guidance. |
| **v1.1** | 2025-10-10 | Added canopy cover dataset, improved CI logs, STAC linkage.                                                     |
| **v1.0** | 2025-10-04 | Initial land cover checksum documentation — NLCD, vegetation, crop, and land use datasets verified.             |

---

<div align="center">

**Kansas Frontier Matrix** — *Every Pixel Proven: Verifying the Living Surface of Kansas.*
📍 [`data/checksums/landcover/`](.) · Linked to the **Land Cover STAC Collection** and **Global Manifest Registry**.

</div>
```
