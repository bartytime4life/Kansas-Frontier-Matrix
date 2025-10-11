<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain Checksums  
`data/processed/terrain/checksums/`

**Mission:** Maintain and verify the **integrity, reproducibility, and provenance**  
of all processed terrain datasets in Kansas Frontier Matrix — ensuring that every elevation, hillshade,  
and derivative raster is cryptographically validated across builds and environments.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum files (`.sha256`)**  
for all processed **terrain datasets** within the Kansas Frontier Matrix (KFM).  

Checksums provide:
- 🔒 **Integrity** — Guarantee no terrain raster is corrupted or modified.  
- 🔁 **Reproducibility** — Validate identical ETL outputs across environments.  
- 🧩 **Provenance** — Link datasets, metadata, and STAC assets via cryptographic fingerprinting.  
- 🧠 **Auditability** — Enable automated verification in continuous-integration pipelines.

All `.sha256` files are produced during the **terrain ETL pipeline** (`make terrain`)  
and validated in GitHub Actions workflows (`stac-validate.yml`).

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Terrain Rasters\n(data/processed/terrain/*.tif)"] --> B["Checksum Generator\n(src/utils/generate_checksums.py)"]
  B --> C["Checksum Files\n(data/processed/terrain/checksums/*.sha256)"]
  C --> D["STAC Metadata Linkage\n(data/processed/terrain/metadata/*.json)"]
  D --> E["CI Validation\n(.github/workflows/stac-validate.yml)"]
  E --> F["Verified Terrain Catalog\n(data/stac/terrain/)"]
  %% END OF MERMAID
````

---

## 🗂️ Directory Layout

```bash
data/processed/terrain/checksums/
├── README.md
├── ks_1m_dem_2018_2020.tif.sha256
├── ks_hillshade_2018_2020.tif.sha256
└── slope_aspect_2018_2020.tif.sha256
```

> **Note:**
> Each `.sha256` corresponds to a processed raster in
> `data/processed/terrain/` and is automatically verified using
> `sha256sum -c` during CI/CD validation.

---

## 🔐 Purpose & Principles

| Objective            | Description                                                   |
| :------------------- | :------------------------------------------------------------ |
| **Data Integrity**   | Detects file corruption or unauthorized modification.         |
| **Reproducibility**  | Confirms identical ETL outputs across compute environments.   |
| **Provenance Chain** | Embeds dataset fingerprints within metadata and STAC assets.  |
| **CI Enforcement**   | CI pipelines fail automatically when mismatches are detected. |

---

## 🧮 Example `.sha256` File

```bash
# File: ks_1m_dem_2018_2020.tif.sha256
f3c0b929a38ef47c7b41138dd726abf84a65a03b8b24e8e12db2fa89a5740c42  ks_1m_dem_2018_2020.tif
```

This checksum certifies the file integrity of
`data/processed/terrain/ks_1m_dem_2018_2020.tif`.

---

## ⚙️ Checksum Generation Workflow

**Makefile target**

```bash
make terrain-checksums
```

**Python command**

```bash
python src/utils/generate_checksums.py data/processed/terrain/ --algo sha256
```

**Steps**

1. Identify all terrain rasters (`.tif`, `.cog`, `.geojson`).
2. Compute SHA-256 hashes using Python’s `hashlib`.
3. Save `<filename>.sha256` under this directory.
4. Validate hashes during CI/CD workflows after ETL runs.
5. Embed hash references in STAC JSON metadata assets.

---

## 🧰 CI/CD Validation

Checksum validation runs automatically in KFM’s **GitHub Actions** pipelines.

**Validation Command**

```bash
sha256sum -c data/processed/terrain/checksums/*.sha256
```

If any mismatch is detected:

* The build fails immediately.
* Logs identify the affected dataset.
* The CI prevents unverified files from propagating to STAC or deployment stages.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Function                                                       |
| :------------------------------------------ | :------------------------------------------------------------- |
| `data/processed/terrain/metadata/*.json`    | References checksum via STAC `"assets.checksum:sha256"` fields |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates + verifies hashes during ETL                         |
| `.github/workflows/stac-validate.yml`       | Automates hash validation across environments                  |
| `data/stac/terrain/`                        | Stores final verified STAC items linked to hashes              |

---

## 🤖 AI & Automation Integration

* **Automated Detection:** The AI pipeline flags anomalies (checksum drift, size change, or missing `.sha256`).
* **Predictive Provenance:** Machine logic compares hash lineage to source manifests for anomaly detection.
* **Self-Healing:** On verified regeneration, new checksums are committed with provenance delta logs in `data/audit/terrain/`.
* **Human Oversight:** All AI-generated integrity reports require curator confirmation before merge.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                 |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | Each dataset includes `.sha256` documentation and linkage      |
| **Reproducibility**     | Deterministic checksum validation ensures identical outputs    |
| **Open Standards**      | Uses SHA-256 (FIPS-180-4) cryptographic standard               |
| **Provenance**          | Checksum stored in STAC metadata, pipeline logs, and manifests |
| **Auditability**        | CI logs + automated re-validation in every build               |

---

## 🧾 Version History

| Version   | Date       | Summary                                                                                            |
| :-------- | :--------- | :------------------------------------------------------------------------------------------------- |
| **1.2.0** | 2025-10-11 | Added front-matter metadata, Mermaid system diagram, AI audit integration, and cross-STAC linking. |
| 1.1.0     | 2025-10-05 | Improved CI validation references and reproducibility table.                                       |
| 1.0.0     | 2025-10-04 | Initial release: checksum generation for DEM, hillshade, slope/aspect datasets.                    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity in Elevation: Every Surface Verified.”*
📍 [`data/processed/terrain/checksums/`](.) · Linked to the **Terrain STAC Collection**

</div>
```
