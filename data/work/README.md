<div align="center">

# ⚙️ Kansas Frontier Matrix — Work Directory  
`data/work/`

**Mission:** Provide a **sandboxed, ephemeral workspace** for intermediate artifacts,  
debug outputs, and cache data generated during **ETL, STAC validation, ML preprocessing,  
and CI/CD workflows** within the **Kansas Frontier Matrix (KFM)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/` directory serves as KFM’s **volatile, developer-centric workspace**,  
intended exclusively for **temporary and regenerable artifacts** created during  
data transformation, testing, and validation.

This area supports **real-time pipeline debugging**, **checksum staging**, and  
**draft STAC item validation**—while maintaining the core MCP principle of  
reproducibility.  

> **Important:** This directory’s contents are **not version-controlled**.  
> Only structure and documentation persist. All data here can be safely deleted  
> and rebuilt using `make` or ETL pipeline scripts.

---

## 🗂️ Directory Layout

```bash
data/work/
├── README.md
├── tmp/                  # On-the-fly ETL artifacts and working data
├── cache/                # Validation, model, and preview caches
├── staging/              # Transitional data outputs prior to publishing
└── logs/                 # Debug, validation, and runtime logs
````

> The `.gitignore` file ensures subdirectory contents are **excluded from version control**,
> preventing accidental commits of transient artifacts.

---

## ⚠️ Usage Policies

| Policy             | Description                                                              |
| :----------------- | :----------------------------------------------------------------------- |
| **Ephemeral**      | Contents are temporary and may be deleted or replaced at any time.       |
| **Non-persistent** | Final outputs belong in `data/processed/` or domain directories.         |
| **MCP-compliant**  | Every temporary artifact must be reproducible via documented workflow.   |
| **CI-safe**        | Used for automated testing, validation, and artifact caching in CI runs. |
| **Isolated**       | Not referenced by public-facing APIs, maps, or published STAC catalogs.  |

---

## ⚙️ Common Use Cases

| Workflow Stage           | Example Output                                           |
| ------------------------ | -------------------------------------------------------- |
| **ETL Testing**          | Temporary CSV joins or clipped GeoTIFFs.                 |
| **Checksum Validation**  | SHA-256 staging before inclusion in manifest.            |
| **Thumbnail Generation** | Intermediate visual renderings prior to optimization.    |
| **STAC Validation**      | Draft item JSONs before catalog inclusion.               |
| **ML Staging**           | Feature tables, tokenized corpora, or validation splits. |

---

## 🧰 Maintenance Procedures

The `data/work/` directory should remain **clean, reproducible, and disposable**.
Automated and manual cleanup are both supported.

### 🔁 Automated Cleanup

```bash
make clean-work
```

### 🧹 Manual Cleanup

```bash
rm -rf data/work/tmp/* data/work/cache/* data/work/staging/* data/work/logs/*
```

> **Safety:** All data stored here is temporary and can be regenerated
> from `data/raw/` or `data/processed/` using Make targets or ETL scripts.

---

## 🔒 Integration with CI/CD & MCP

| Component             | Function                                                                     |
| :-------------------- | :--------------------------------------------------------------------------- |
| `.github/workflows/*` | CI logs, test metrics, or validation reports may be temporarily stored here. |
| `src/pipelines/*`     | ETL tasks may stream intermediates to this workspace.                        |
| `data/checksums/`     | Intermediate checksum computations are staged here.                          |
| `data/stac/`          | Draft STAC Items are generated here before publication.                      |
| `Makefile`            | Provides cleanup and utility tasks for managing `data/work/`.                |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | README defines lifecycle, structure, and reproducibility.           |
| **Reproducibility**     | All files regenerable from upstream inputs and Make targets.        |
| **Open Standards**      | Uses CSV, JSON, GeoJSON, Parquet, or COG for interoperability.      |
| **Provenance**          | Each artifact is tied to a logged or scripted pipeline step.        |
| **Auditability**        | `data/work/logs/` preserves process-level records for traceability. |

---

## 🧩 Related Directories

| Path              | Description                                           |
| ----------------- | ----------------------------------------------------- |
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
| **v1.2.0** | 2025-10-12 | Enhanced reproducibility framework and linked subdirectory governance. |

---

<div align="center">

**Kansas Frontier Matrix**
⚙️ *“Work Fast. Validate Often. Keep It Clean.”*
📍 [`data/work/`](.) — transient workspace governed by MCP reproducibility and open-data policy.

</div>
```
