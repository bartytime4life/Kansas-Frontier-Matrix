<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate Checksums  
`data/checksums/climate/`

**Mission:** Guarantee **integrity, reproducibility, and provenance** for all processed climate datasets —  
including temperature, precipitation, drought indices, and atmospheric anomalies — across the  
Kansas Frontier Matrix (KFM) data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `data/checksums/climate/` directory maintains **cryptographic SHA-256 signatures**  
for every processed climate dataset in the KFM repository.  

These checksums function as immutable digital fingerprints that guarantee:

- **Integrity** — Detects data corruption or unauthorized modification.  
- **Reproducibility** — Confirms deterministic ETL output across time and systems.  
- **Provenance** — Links derived assets back to raw sources and STAC metadata.  
- **Auditability** — Enables end-to-end validation during CI/CD workflows.  

All `.sha256` files are generated automatically by the **climate ETL pipeline** (`make climate`)  
and revalidated via GitHub Actions during every commit and pull request.

---

## 🗂️ Directory Layout

```bash
data/checksums/climate/
├── README.md
├── daymet_1980_2024.tif.sha256
├── noaa_normals_1991_2020.geojson.sha256
├── drought_monitor_2000_2025.tif.sha256
└── prism_temp_anomaly_1895_2024.tif.sha256
````

> **Note:** Each `.sha256` file corresponds directly to a dataset under
> `data/processed/climate/` and is validated automatically using `sha256sum -c`.

---

## 🔐 Checksum Governance

| Objective           | Description                                                                 |
| :------------------ | :-------------------------------------------------------------------------- |
| **Data Integrity**  | Detects accidental or malicious corruption in raster or vector files.       |
| **Reproducibility** | Ensures ETL pipeline output consistency across builds and environments.     |
| **Provenance**      | Establishes verifiable linkage between raw → processed → STAC metadata.     |
| **Automation**      | CI/CD workflows continuously validate all hashes for consistency and trust. |

---

## 🧮 Example `.sha256` File

```bash
# File: daymet_1980_2024.tif.sha256
a7f9132dfe5b16c9783f3f0ec4a2f4da8a9bb5e7b739c3477325dcb0df836f41  daymet_1980_2024.tif
```

The above verifies that
`data/processed/climate/daymet_1980_2024.tif` is identical to its validated version in the repository.

---

## ⚙️ Generation Workflow

Checksums are created automatically within the ETL process or can be triggered manually.

**Makefile target:**

```bash
make climate-checksums
```

**Python command:**

```bash
python src/utils/generate_checksums.py data/processed/climate/ --algo sha256
```

**Workflow Steps:**

1. Traverse all outputs in `data/processed/climate/`.
2. Compute SHA-256 for `.tif`, `.geojson`, `.csv`, or `.parquet` files.
3. Write `<filename>.sha256` files to this directory.
4. Validate during CI/CD (`sha256sum -c`) and report to workflow logs.

---

## 🧰 CI/CD Validation

All checksums are automatically verified in continuous integration workflows.

**Command executed in CI:**

```bash
sha256sum -c data/checksums/climate/*.sha256
```

**Behavior:**

* A single mismatch **fails CI** immediately.
* Maintainers must reprocess the data and regenerate checksums before merging.
* Validation logs are archived under `data/work/logs/` for long-term auditability.
* STAC validation (`.github/workflows/stac-validate.yml`) crosschecks hash references.

---

## 🔗 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                                |
| :------------------------------------ | :--------------------------------------------------------------------- |
| `data/processed/metadata/climate/`    | STAC items embed `"checksum:sha256"` for reproducibility validation.   |
| `src/pipelines/climate_pipeline.py`   | Generates and validates hashes as part of ETL processing.              |
| `.github/workflows/stac-validate.yml` | Performs automated re-validation of hashes and metadata references.    |
| `data/stac/climate/`                  | STAC Catalog includes checksums as part of its metadata specification. |

> **Tip:** STAC and manifest hashes must always match.
> Run `make stac` after updating any checksum to refresh all linked STAC metadata.

---

## 🔄 Cross-Domain Integration

Climate checksums are part of the **global checksum registry** under `data/checksums/`.
They integrate with other domain manifests (e.g., terrain, hydrology) to enable
whole-repository integrity checks via `make checksums-verify`.

**Command:**

```bash
sha256sum -c data/checksums/**/*.sha256
```

**Outputs:**

* ✅ Verified hashes print “OK” with relative path confirmation.
* ❌ Invalid or missing files trigger error logs and block deployment.

---

## 🧩 Troubleshooting

| Issue                           | Cause                                                | Resolution                                             |
| :------------------------------ | :--------------------------------------------------- | :----------------------------------------------------- |
| CI fails on checksum mismatch   | File modified or truncated post-build.               | Rerun ETL (`make climate`), regenerate hashes.         |
| File missing from manifest      | New asset not captured in ETL output.                | Run `make climate-checksums` to rebuild manifests.     |
| Hash differs from STAC metadata | Drift between data and STAC reference.               | Update STAC entries (`make stac`).                     |
| Random validation errors        | Non-deterministic compression or timestamp metadata. | Reprocess with fixed seeds and normalized compression. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | Every dataset includes `.sha256` and README documentation.       |
| **Reproducibility**     | SHA-256 ensures deterministic output validation.                 |
| **Open Standards**      | Uses SHA-256 (FIPS 180-4) per STAC Checksum extension.           |
| **Provenance**          | Links dataset lineage across ETL, metadata, and STAC references. |
| **Auditability**        | Continuous verification in CI/CD with logs archived for review.  |

---

## 📅 Version History

| Version | Date       | Summary                                                                                           |
| :------ | :--------- | :------------------------------------------------------------------------------------------------ |
| v1.0.0  | 2025-10-04 | Initial checksum documentation for Daymet, NOAA Normals, Drought Monitor datasets.                |
| v1.1.0  | 2025-10-10 | Added PRISM anomaly dataset, CI/STAC integration section, and cross-domain verification workflow. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Integrity in Every Forecast: Verifying the Climate of Record.”*
📍 [`data/checksums/climate/`](.) · Linked to the **Climate STAC Collection** and global checksum registry.

</div>
```
