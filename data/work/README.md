<div align="center">

# ⚙️ Kansas Frontier Matrix — **Work Directory**  
`data/work/`

**Mission:** Provide a **sandboxed, ephemeral workspace** for intermediate artifacts,  
debug outputs, and cache data generated during **ETL, STAC validation, ML preprocessing,  
and CI/CD workflows** within the **Kansas Frontier Matrix (KFM)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Work Directory (data/work/)"
version: "v1.3.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-architecture"]
tags: ["work","tmp","cache","staging","logs","etl","stac","mcp","ci-cd"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Draft validation staging)
  - FAIR Principles (Findable, Accessible, Interoperable, Reusable)
---
```

---

## 📚 Overview

The `data/work/` directory is KFM’s **volatile, developer-centric workspace**, intended **only** for **temporary and regenerable artifacts** created during data transformation, testing, and validation.

It supports **real-time pipeline debugging**, **checksum staging**, and **draft STAC validation** while preserving the MCP tenets of **reproducibility** and **traceability**.

> **Important:** Contents are **not version-controlled**. Only structure and documentation persist.  
> Everything here can be safely deleted and rebuilt using `make` targets or ETL pipeline scripts.

---

## 🗂️ Directory Layout

```bash
data/work/
├── README.md
├── tmp/                  # On-the-fly ETL intermediates and working data
├── cache/                # Validation caches, model caches, preview tiles/thumbnails
├── staging/              # Transitional outputs prior to publishing
└── logs/                 # Debug, validation, and runtime logs
```

> `.gitignore` excludes **all contents** of these subfolders to prevent accidental commits of transient artifacts.

---

## ⚠️ Usage Policies

| Policy             | Description                                                              |
| :----------------- | :----------------------------------------------------------------------- |
| **Ephemeral**      | Contents are temporary and may be deleted or replaced at any time.       |
| **Non-persistent** | Final outputs belong in `data/processed/` or domain directories.         |
| **MCP-compliant**  | Every temporary artifact must be reproducible via documented workflow.   |
| **CI-safe**        | Used for automated testing, validation, and artifact caching in CI runs. |
| **Isolated**       | Not referenced by public APIs, maps, or published STAC catalogs.         |

---

## ⚙️ Common Use Cases

| Workflow Stage           | Example Output                                                     |
| :----------------------- | :----------------------------------------------------------------- |
| **ETL Testing**          | Temporary CSV joins, clipped GeoTIFFs, reprojection scratch files. |
| **Checksum Validation**  | SHA-256 staging before inclusion in checksums manifests.            |
| **Thumbnail Generation** | Intermediate thumbnails prior to optimization and publish.          |
| **STAC Validation**      | Draft Item/Collection JSON for pre-catalog checks.                  |
| **ML Staging**           | Feature tables, tokenized corpora, validation/train/test splits.     |

---

## 🧰 Maintenance Procedures

The `data/work/` area should remain **clean, reproducible, and disposable**.

### 🔁 Automated Cleanup

```bash
make clean-work
```

### 🧹 Manual Cleanup

```bash
rm -rf data/work/tmp/* data/work/cache/* data/work/staging/* data/work/logs/*
```

> **Safety:** All data here is temporary and can be regenerated from `data/raw/` or `data/processed/` using Make targets or ETL scripts.

---

## 🔒 Integration with CI/CD & MCP

| Component               | Function                                                                       |
| :---------------------- | :------------------------------------------------------------------------------ |
| `.github/workflows/*`   | CI logs, test metrics, and validation reports may be stored here temporarily.  |
| `src/pipelines/*`       | ETL tasks may stream intermediates to this workspace.                          |
| `data/checksums/`       | Intermediate checksum computations are staged here before manifest updates.    |
| `data/stac/`            | Draft STAC Items/Collections are generated here before catalog publication.     |
| `Makefile`              | Provides cleanup and helper tasks for managing `data/work/`.                   |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | README defines lifecycle, structure, and reproducibility.           |
| **Reproducibility**     | All files regenerable from upstream inputs and Make targets.        |
| **Open Standards**      | Prefer CSV, JSON, GeoJSON, Parquet, or COG for interoperability.    |
| **Provenance**          | Each artifact tied to a logged/scriped pipeline step in `logs/`.     |
| **Auditability**        | `data/work/logs/` preserves process-level records for traceability. |

---

## 🔗 Related Directories

| Path              | Description                                           |
| :---------------- | :---------------------------------------------------- |
| `data/raw/`       | Immutable source datasets.                            |
| `data/processed/` | Cleaned, validated, and structured outputs.           |
| `data/checksums/` | SHA-256 manifests for verified assets.                |
| `data/stac/`      | Published STAC metadata for global catalog discovery. |

---

## 📅 Version History

| Version    | Date       | Summary                                                                |
| :--------- | :--------- | :--------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial creation of the work directory and documentation.              |
| **v1.1.0** | 2025-10-10 | Added MCP integration, CI/CD policies, and cleanup procedures.         |
| **v1.3.0** | 2025-10-16 | Alignment pass: YAML front matter, tables, policies, maintenance ops.  |

---

<div align="center">

**Kansas Frontier Matrix**  
⚙️ *“Work Fast. Validate Often. Keep It Clean.”*  
📍 [`data/work/`](.) — transient workspace governed by MCP reproducibility and open-data policy.

</div>