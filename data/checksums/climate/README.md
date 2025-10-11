<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate Checksums  
`data/checksums/climate/`

**Mission:** Guarantee **integrity, reproducibility, and provenance** for all processed climate datasets —  
temperature, precipitation, drought indices, and atmospheric anomalies — across the KFM ecosystem.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../../.github/workflows/trivy.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

`data/checksums/climate/` maintains **SHA-256 checksum manifests (`.sha256`)**  
for every processed climate dataset in KFM. These immutable digests guarantee:

- 🔒 **Integrity** — detect corruption or unauthorized modification  
- 🔁 **Reproducibility** — confirm deterministic ETL outputs over time  
- 🔗 **Provenance** — bind derived assets to sources and **STAC** metadata  
- 🧾 **Auditability** — enable end-to-end CI/CD validation and logging

All `.sha256` files are produced by the **Climate ETL** (`make climate`) and revalidated on every commit.

---

## 🧭 Climate Integrity Workflow

```mermaid
flowchart LR
  S["data/sources/climate/*.json\nSource Manifests"] --> R["data/raw/climate/**\nDaymet · PRISM · NOAA"]
  R --> P["src/pipelines/climate_pipeline.py\nETL · Resample · Derive"]
  P --> O["data/processed/climate/**\nCOG · GeoJSON · CSV · Parquet"]
  O --> C["data/checksums/climate/*.sha256\nPer-asset digests"]
  O --> T["data/stac/climate/**.json\nSTAC Items (checksum:sha256)"]
  C --> V["CI Validation\nsha256sum -c + STAC parity"]
%% END OF MERMAID
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/checksums/climate/
├── README.md
├── daymet_1980_2024.tif.sha256
├── noaa_normals_1991_2020.geojson.sha256
├── drought_monitor_2000_2025.tif.sha256
└── prism_temp_anomaly_1895_2024.tif.sha256
```

> Each `.sha256` corresponds to an asset in `data/processed/climate/` and is verified in CI with `sha256sum -c`.

---

## 🔐 Checksum Governance

| Objective           | Description                                                 |
| :------------------ | :---------------------------------------------------------- |
| **Data Integrity**  | Detects accidental or malicious changes in rasters/vectors. |
| **Reproducibility** | Ensures consistent ETL outputs across machines and time.    |
| **Provenance**      | Maintains verifiable linkage among raw → processed → STAC.  |
| **Automation**      | CI/CD continuously validates all digests and blocks drift.  |

---

## 🧮 Example `.sha256` File

```bash
# File: daymet_1980_2024.tif.sha256
a7f9132dfe5b16c9783f3f0ec4a2f4da8a9bb5e7b739c3477325dcb0df836f41  daymet_1980_2024.tif
```

This proves `data/processed/climate/daymet_1980_2024.tif` matches the last validated build.

---

## ⚙️ Generation & Verification

**Make targets**

```bash
make climate-checksums          # generate checksums
make climate-checksums-verify   # verify checksums (used by CI)
```

**Python CLI**

```bash
python src/utils/generate_checksums.py data/processed/climate/ --algo sha256
```

**Steps**

1. Traverse `data/processed/climate/` for `.tif`, `.geojson`, `.csv`, `.parquet`.
2. Compute SHA-256 (Python `hashlib` or `sha256sum`).
3. Write `<filename>.sha256` into `data/checksums/climate/`.
4. CI runs `sha256sum -c data/checksums/climate/*.sha256`; logs → `data/work/logs/climate_checksums.log`.

---

## 🧰 CI/CD Validation

**Command executed by CI**

```bash
sha256sum -c data/checksums/climate/*.sha256
```

**Behavior**

* ✅ **Pass:** hashes match; build proceeds.
* ❌ **Fail:** pipeline halts; reprocess and regenerate digests.
* 🧾 **Logs:** archived under `data/work/logs/` for MCP auditability.

Integrated with **`.github/workflows/stac-validate.yml`** to enforce checksum–metadata parity.

---

## 🔗 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                |
| :------------------------------------ | :----------------------------------------------------- |
| `data/stac/climate/**.json`           | STAC Items embed `"checksum:sha256"` for each asset.   |
| `data/processed/metadata/climate/`    | Mirrors checksum/provenance for non-STAC artifacts.    |
| `src/pipelines/climate_pipeline.py`   | Generates/validates checksums; emits audit logs.       |
| `.github/workflows/stac-validate.yml` | Revalidates checksum and STAC schema on every PR.      |
| `data/checksums/manifest.sha256`      | Global roll-up manifest for cross-domain verification. |

---

## 🔄 Cross-Domain Integrity

Climate checksums participate in the **global registry** (`data/checksums/`) enabling whole-repo checks:

```bash
sha256sum -c data/checksums/**/*.sha256
```

* ✅ All OK → repository integrity verified
* ❌ Any failure → deployment blocked until resolved

---

## 🧩 Troubleshooting

| Issue                     | Cause                                    | Resolution                                                  |
| :------------------------ | :--------------------------------------- | :---------------------------------------------------------- |
| CI mismatch               | File modified or truncated post-build    | Re-run ETL (`make climate`), then `make climate-checksums`. |
| Missing `.sha256`         | New asset not hashed                     | Run generator and commit the sidecar.                       |
| STAC drift                | STAC not refreshed after checksum change | `make stac` to sync Items.                                  |
| Non-deterministic rasters | Compression/timestamps vary              | Pin libs, set `SOURCE_DATE_EPOCH`, normalize GDAL options.  |

---

## 🧠 MCP Compliance Matrix

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | README defines policy, structure, commands, CI hooks.            |
| **Reproducibility**     | Deterministic SHA-256 hashing + enforced CI validation.          |
| **Open Standards**      | FIPS 180-4 SHA-256; STAC checksum extension; UTF-8, POSIX paths. |
| **Provenance**          | Checksums + STAC Items bind assets to immutable identities.      |
| **Auditability**        | CI failure gates; logs retained for review.                      |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                        |
| :------- | :--------- | :--------------------------------------------------------------------------------------------- |
| **v1.2** | 2025-10-11 | Protocol v1.1 upgrade: front-matter, Mermaid flow, CI parity, cross-domain verification notes. |
| **v1.1** | 2025-10-10 | Added PRISM anomaly dataset; CI/STAC integration and whole-repo check guidance.                |
| **v1.0** | 2025-10-04 | Initial checksums for Daymet, NOAA Normals, Drought Monitor datasets.                          |

---

<div align="center">

**Kansas Frontier Matrix** — *Integrity in Every Forecast: Verifying the Climate of Record.*
📍 [`data/checksums/climate/`](.) · Linked to **Climate STAC Collection** and **Global Checksum Registry**.

</div>
```
