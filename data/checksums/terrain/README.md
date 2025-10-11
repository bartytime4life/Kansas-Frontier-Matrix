<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Checksums  
`data/checksums/terrain/`

**Mission:** Guarantee **integrity, reproducibility, and provenance** for all terrain and elevation datasets  
within the Kansas Frontier Matrix (KFM). Every Digital Elevation Model (DEM), hillshade, slope/aspect raster,  
and terrain vector product is **cryptographically verified**, **reproducible**, and **linked via STAC metadata**  
for transparent provenance and lifecycle traceability.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../../.github/workflows/trivy.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `data/checksums/terrain/` directory stores **SHA-256 checksum manifests** for all processed terrain datasets  
within the Kansas Frontier Matrix (KFM).  

Checksums form the foundation of **scientific reproducibility and data assurance**, verifying that all terrain assets —  
from statewide LiDAR DEM mosaics to derivative slope and contour layers — remain **unaltered, reproducible, and traceable**.

**Checksum guarantees:**
- 🧱 **Integrity** — Detects corruption or unauthorized modification.  
- 🔁 **Reproducibility** — Ensures deterministic ETL outputs on every build.  
- 🔗 **Provenance** — Links terrain products to their STAC metadata and source lineage.  
- ⚙️ **Automation** — Integrated into CI/CD validation pipelines for continuous verification.  

---

## 🧭 Terrain Integrity Workflow

```mermaid
flowchart LR
  S["data/sources/terrain/*.json\nSource Manifests"] --> R["data/raw/terrain/**\nLiDAR · DEM Tiles"]
  R --> P["src/pipelines/terrain_pipeline.py\nETL · Mosaicking · Derivatives"]
  P --> O["data/processed/terrain/**\nCOGs · GeoJSON"]
  O --> C["data/checksums/terrain/*.sha256\nIntegrity Hashes"]
  O --> T["data/stac/terrain/**.json\nSTAC Items (checksum:sha256)"]
  C --> V["CI Validation\nsha256sum -c + STAC parity check"]
%% END OF MERMAID
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/checksums/terrain/
├── README.md
├── ks_1m_dem_2018_2020.tif.sha256
├── ks_hillshade_2018_2020.tif.sha256
├── slope_aspect_2018_2020.tif.sha256
└── contour_lines_10m_ks.geojson.sha256
```

> Each `.sha256` corresponds to its dataset in `data/processed/terrain/`
> and is automatically validated during CI/CD.

---

## 🧮 Example `.sha256` Manifest

```bash
# File: ks_1m_dem_2018_2020.tif.sha256
f3c0b929a38ef47c7b41138dd726abf84a65a03b8b24e8e12db2fa89a5740c42  ks_1m_dem_2018_2020.tif
```

This checksum certifies the integrity of
`data/processed/terrain/ks_1m_dem_2018_2020.tif`
and validates that all ETL outputs remain byte-for-byte identical across environments.

---

## ⚙️ Generation & Verification

**Makefile targets**

```bash
make terrain-checksums        # generate all terrain checksums
make terrain-checksums-verify # verify during CI/CD
```

**Python equivalent**

```bash
python src/utils/generate_checksums.py data/processed/terrain/ --algo sha256
```

**Workflow Steps**

1. Scan `data/processed/terrain/` for `.tif`, `.cog`, `.geojson` files.
2. Compute SHA-256 using Python’s `hashlib` or system `sha256sum`.
3. Output results as `<filename>.sha256` to `data/checksums/terrain/`.
4. Validate in CI/CD; logs stored in `data/work/logs/terrain_checksums.log`.

---

## 🧰 CI/CD Validation

**Command executed by CI**

```bash
sha256sum -c data/checksums/terrain/*.sha256
```

| Outcome     | Behavior                                                  |
| :---------- | :-------------------------------------------------------- |
| ✅ **Pass**  | Integrity confirmed, STAC Items verified.                 |
| ❌ **Fail**  | Pipeline halts; dataset must be reprocessed and rehashed. |
| 🧾 **Logs** | Written to `data/work/logs/` for MCP audit retention.     |

---

## 🔗 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                           |
| :------------------------------------ | :---------------------------------------------------------------- |
| `data/stac/terrain/**.json`           | STAC Items include `"checksum:sha256"` for every terrain asset.   |
| `src/pipelines/terrain_pipeline.py`   | Automates checksum creation and validation.                       |
| `.github/workflows/stac-validate.yml` | Verifies parity between STAC checksum fields and `.sha256` files. |
| `data/checksums/manifest.sha256`      | Global manifest referencing all terrain checksum files.           |

---

## 🧩 Troubleshooting & Maintenance

| Issue                     | Likely Cause                       | Resolution                                        |
| :------------------------ | :--------------------------------- | :------------------------------------------------ |
| CI validation fails       | File changed or truncated post-ETL | Run `make terrain-checksums` and recommit hashes. |
| Missing checksum          | New raster added without checksum  | Re-run generator or Python command.               |
| STAC mismatch             | STAC checksum not updated          | Run `make stac` to rebuild metadata.              |
| Non-deterministic results | Timestamps or compression drift    | Pin GDAL options, set `SOURCE_DATE_EPOCH`.        |

---

## 🧠 MCP Compliance Matrix

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | Each dataset includes README and `.sha256` manifest.        |
| **Reproducibility**     | Deterministic hashing with CI verification.                 |
| **Open Standards**      | SHA-256 (FIPS 180-4), STAC checksum extension, POSIX paths. |
| **Provenance**          | Linked via STAC, metadata, and checksum chain.              |
| **Auditability**        | Logs and validation stored under MCP retention policy.      |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                          |
| :------- | :--------- | :----------------------------------------------------------------------------------------------- |
| **v1.2** | 2025-10-11 | Protocol v1.1 upgrade: added front-matter, workflow diagram, CI refinements, metadata alignment. |
| **v1.1** | 2025-10-10 | Added contour datasets, CI logging, troubleshooting, and global manifest references.             |
| **v1.0** | 2025-10-04 | Initial terrain checksum docs for DEM, hillshade, slope/aspect.                                  |

---

<div align="center">

**Kansas Frontier Matrix** — *Elevation Verified, Integrity Preserved.*
📍 [`data/checksums/terrain/`](.) · Linked to **Terrain STAC Collection** and **Global Checksum Registry**.

</div>
```
