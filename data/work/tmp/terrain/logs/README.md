<div align="center">

# 🧾 Kansas Frontier Matrix — **Terrain ETL Logs**  
`data/work/tmp/terrain/logs/`

**Mission:** Record, track, and manage **temporary logs** generated during terrain ETL, validation, and QA operations —  
ensuring **reproducibility, transparency, and auditability** across all elevation-related data workflows  
in the **Kansas Frontier Matrix (KFM)** project.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Terrain ETL Logs (data/work/tmp/terrain/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-architecture"]
tags: ["terrain","logs","etl","validation","hillshade","slope","aspect","cog","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - Cloud-Optimized GeoTIFF (COG)
  - FAIR Principles (Transparent & Reusable Workflows)
---
```

---

## 📚 Overview

The `data/work/tmp/terrain/logs/` directory contains **temporary ETL and QA logs** created during terrain data processing and validation.  
These logs document the complete lifecycle of terrain ETL activities:

- DEM reprojection, tiling, mosaicking  
- Hillshade, slope, aspect derivation and QA  
- Raster alignment and geospatial transformation testing  
- Checksum validation, schema compliance, and STAC verification  

All files are **ephemeral**, **excluded from version control**, and regenerated per run.  
They serve as **human-readable diagnostics** for developers and **machine-parsable evidence** for CI/CD.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/terrain/logs/
├── README.md
├── terrain_etl_debug.log          # High-level pipeline trace (start/end, timings, statuses)
├── terrain_projection_test.log    # CRS conversions, resampling metadata, GCP/transform checks
├── terrain_validation_report.log  # Checksum, schema, COG profile & overviews verification
└── qa_metrics_summary.log         # RMSE, pixel-variance, nodata fill %, void detection
```

> **Note:** Filenames rotate or overwrite per run; exact names may vary based on active ETL tasks.

---

## ⚙️ Logging Schema & Standards

All logs follow a **structured, timestamped** line format for grep-ability and audit trails.

**Standard Line Schema**

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 ... message="free text"
```

**Examples**

```text
2025-10-16T03:11:08Z INFO terrain.etl stage="start" run_id="2025-10-16T03:11Z" message="terrain pipeline init"
2025-10-16T03:11:29Z INFO terrain.projection src_epsg=26914 dst_epsg=4326 resample="bilinear" message="reproject DEM tile"
2025-10-16T03:11:57Z WARNING terrain.alignment tile_id=47 offset_px=1.0 message="minor edge misalignment"
2025-10-16T03:12:14Z INFO terrain.hillshade azimuth=315 altitude=35 outfile="data/work/tmp/terrain/hillshade_preview.tif"
2025-10-16T03:12:38Z INFO terrain.cog check="overviews" levels=5 result="ok" message="cog profile valid"
2025-10-16T03:12:44Z INFO terrain.checksum file="slope_aspect_test_area.tif" sha256="c7a07a..." result="match"
2025-10-16T03:12:50Z INFO terrain.etl stage="end" status="SUCCESS" duration_s=102.4
```

**Policy**

- UTF-8 **plain text** (no ANSI colors); single-line entries; newline-terminated  
- Include **component names** (`terrain.projection`, `terrain.hillshade`, `terrain.cog`)  
- Record **CRS**, **resampling**, **nodata**, and **overview** details where relevant

---

## 🧾 Log Types & Purposes

| Log Type                            | Purpose                                                                                         |
| :---------------------------------- | :---------------------------------------------------------------------------------------------- |
| **`terrain_etl_debug.log`**         | Complete ETL trace (stages, timings, statuses, error handling).                                 |
| **`terrain_projection_test.log`**   | CRS conversions, resampling method, pixelsize, alignment/transform checks.                      |
| **`terrain_validation_report.log`** | COG profile checks (tiling/overviews), schema and checksum verification outcomes.               |
| **`qa_metrics_summary.log`**        | QA aggregates: RMSE to baseline, nodata/skew stats, void detection, histogram sanity.           |

---

## 🔧 Logging Framework

KFM uses **Python `logging`** with rotational handlers for both **readability** and **machine parsing**.

**YAML Config (example)**

```yaml
version: 1
formatters:
  line:
    format: "%(asctime)s %(levelname)s %(name)s %(message)s"
handlers:
  terrain_rotating:
    class: logging.handlers.RotatingFileHandler
    filename: data/work/tmp/terrain/logs/terrain_etl_debug.log
    maxBytes: 2097152   # 2 MB
    backupCount: 3
    encoding: utf-8
    formatter: line
loggers:
  kfm.terrain:
    level: INFO
    handlers: [terrain_rotating]
    propagate: no
root:
  level: WARNING
  handlers: [terrain_rotating]
```

**Python Emission (snippet)**

```python
import logging, logging.config, json
with open("config/logging_terrain.yaml") as f:
    logging.config.dictConfig(json.load(open("config/logging_terrain.json")))  # or yaml.safe_load(f)
log = logging.getLogger("kfm.terrain")

log.info('stage="start" run_id="2025-10-16T03:11Z" message="terrain pipeline init"')
# ...
log.warning('tile_id=47 offset_px=1.0 message="minor edge misalignment"')
log.info('check="overviews" result="ok" message="cog profile valid"')
log.info('stage="end" status="SUCCESS" duration_s=102.4')
```

---

## 🧩 Log Management Workflow

**Makefile Target**

```bash
make terrain
```

**Python CLI**

```bash
python src/pipelines/terrain/terrain_pipeline.py \
  --log data/work/tmp/terrain/logs/terrain_etl_debug.log
```

**Lifecycle**

1. Initialize log with timestamp, run ID, commit SHA, and env hash.  
2. Append structured entries for each stage (reproject → derive → validate).  
3. Flag anomalies with `WARNING`/`ERROR`, include corrective action or retry info.  
4. Summarize counts, duration, and final status (`SUCCESS`/`FAIL`).  
5. Rotate/purge per retention policy.

---

## 🧹 Cleanup Policy

Logs are **purged** between pipeline executions to avoid retention of obsolete artifacts.

**Automated**

```bash
make clean-logs
```

**Manual**

```bash
rm -rf data/work/tmp/terrain/logs/*
```

**Permanent Outputs**

- `data/processed/terrain/` — Final DEMs, slopes, hillshades  
- `data/checksums/terrain/` — SHA-256 integrity manifests  
- `data/processed/metadata/terrain/` — STAC-compliant provenance metadata

---

## 🔒 Security & Retention Policy

| Rule                   | Implementation                                                                 |
| :--------------------- | :------------------------------------------------------------------------------ |
| **Retention Duration** | Logs persist only for active pipeline cycles or current CI job; default ≤ 7 days.|
| **Sensitive Data**     | Do not log raw pixel windows or confidential coordinates beyond QA context.     |
| **Access Scope**       | Local-only artifacts; not uploaded to remote storage or version control.         |
| **Minimize Content**   | Record parameters/metrics; avoid large content dumps or binary traces.          |

---

## 🧰 CI/CD & Metadata Integration

| Linked Component                              | Purpose                                                   |
| :-------------------------------------------- | :-------------------------------------------------------- |
| `src/pipelines/terrain/terrain_pipeline.py`   | Emits ETL, QA, and error logs; manages rotation/purge.    |
| `.github/workflows/stac-validate.yml`         | Consumes logs for checksum and STAC validation context.   |
| `data/work/tmp/terrain/`                      | Parent scratch space for terrain intermediates.           |
| `data/processed/terrain/`                     | Destination for finalized terrain datasets.               |
| `data/checksums/terrain/`                     | Hosts integrity checks for published assets.              |
| `data/processed/metadata/terrain/`            | Persists STAC Items/Collections linked to terrain inputs. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README documents structure, lifecycle, and retention policies.              |
| **Reproducibility**     | Logs deterministically mirror ETL/QA actions and outcomes.                  |
| **Open Standards**      | UTF-8 text lines; consistent naming; optional JSON sidecar summaries.       |
| **Provenance**          | Entries reference run ID, commit SHA, inputs, and transformation stages.    |
| **Auditability**        | Grep-friendly, structured lines + CI consumption for transparent QA.        |

---

## 📎 Related Directories

| Path                               | Description                                                  |
| :--------------------------------- | :----------------------------------------------------------- |
| `data/work/tmp/terrain/`           | Temporary workspace for terrain ETL and QA intermediates.    |
| `data/processed/terrain/`          | Final processed terrain datasets (DEMs, hillshades, slopes). |
| `data/checksums/terrain/`          | Hash manifests for reproducibility verification.             |
| `data/processed/metadata/terrain/` | STAC metadata entries for terrain datasets.                  |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                  |
| :------- | :--------- | :--------------------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation for terrain ETL logging.                                           |
| **v1.1.0** | 2025-10-10 | Added schema examples, retention policy, and CI/CD integration details.                  |
| **v1.2.0** | 2025-10-16 | Alignment pass: YAML front matter, line schema, rotation config, and security updates.   |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Elevation Has a Story — and Every Process Leaves a Log.”*  
📍 [`data/work/tmp/terrain/logs/`](.) · Temporary ETL logging hub for terrain processing, validation, and QA.

</div>
