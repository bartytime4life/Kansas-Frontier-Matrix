<div align="center">

# ⚙️ Kansas Frontier Matrix — Work Directory  
`data/work/`

**Mission:** Provide a **sandboxed, temporary workspace** for intermediate artifacts, debug outputs,  
and validation caches generated during ETL, STAC, and testing workflows within the **Kansas Frontier Matrix (KFM)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/` directory acts as the **volatile workspace** for all Kansas Frontier Matrix data pipelines.  
It holds **temporary files**, **debug data**, and **intermediate results** that appear during ETL, testing,  
checksum computation, and validation processes.  

This directory is **not version-controlled for data** — only structure, configuration, and documentation are tracked.  
It is intended solely for **short-term, reproducible operations**, not for persistent storage.

### Typical Uses
- ETL transformations and temporary joins  
- Raster reprojections or clipping previews  
- STAC pre-validation and draft metadata generation  
- Thumbnail rendering and checksum staging  
- Logging, QA/QC testing, or experimental data prep  

All contents are **ephemeral** and can be safely deleted or regenerated at any time.

---

## 🗂️ Directory Layout

```bash
data/work/
├── README.md
├── tmp/                  # Temporary ETL artifacts and working data
├── cache/                # Cached validation, model, or preview results
├── staging/              # Transitional outputs prior to commit into processed/
└── logs/                 # Runtime and debugging logs for QA/QC
````

> **Note:** `.gitignore` ensures all subdirectory contents are excluded from version control
> to avoid committing large or transient files. Only this README and structure persist.

---

## ⚠️ Policies & Guidelines

| Rule                    | Description                                                             |
| :---------------------- | :---------------------------------------------------------------------- |
| **Ephemeral Storage**   | Files here may be deleted, replaced, or regenerated at any time.        |
| **No Persistent Data**  | Final data products must reside in `data/processed/`.                   |
| **Version Control**     | Only directory structure and metadata documentation are tracked.        |
| **CI/CD Safety**        | Work files are ignored by CI except when used for test outputs or logs. |
| **Sandbox Environment** | This directory is isolated from published datasets for safety.          |

---

## ⚙️ Common Use Cases

| Task                         | Example                                                         |
| :--------------------------- | :-------------------------------------------------------------- |
| **Pipeline Debugging**       | Temporary raster slices or extracted tables during ETL testing. |
| **Checksum Validation**      | Intermediate SHA-256 staging before global manifest generation. |
| **Thumbnail Generation**     | Temporary image previews and compressions.                      |
| **STAC Validation Tests**    | Pre-deployment metadata validation.                             |
| **Machine Learning Staging** | Short-lived feature tables or tokenized text datasets.          |

---

## 🧰 Maintenance Procedures

This directory should remain **clean and disposable**.
Stale files can accumulate during iterative runs, so automated and manual cleanup are both supported.

### 🔁 Automated Cleanup (Preferred)

Run the Make target:

```bash
make clean-work
```

### 🧹 Manual Cleanup (Developer)

Remove files manually from each transient subdirectory:

```bash
rm -rf data/work/tmp/* data/work/cache/* data/work/staging/* data/work/logs/*
```

**Safety:** All critical datasets are reproducible via domain-specific rebuild targets
(e.g., `make terrain`, `make hydrology`, `make landcover`, etc.).

---

## 🔒 Integration with CI/CD and MCP

| Component            | Description                                                               |
| :------------------- | :------------------------------------------------------------------------ |
| `.github/workflows/` | CI workflows may output logs or metrics here during validation runs.      |
| `src/pipelines/*`    | ETL scripts use this workspace for in-memory or on-disk intermediates.    |
| `data/checksums/`    | Hash computation results are temporarily staged here before publication.  |
| `data/stac/`         | Draft STAC Items may be generated and validated here before finalization. |
| `Makefile`           | Defines `clean-work` and related utility tasks to manage this directory.  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                            |
| :---------------------- | :------------------------------------------------------------------------ |
| **Documentation-first** | This README documents structure, retention policy, and workflow usage.    |
| **Reproducibility**     | Ensures all transient steps can be cleanly rerun from source inputs.      |
| **Open Standards**      | Uses open, human-readable, non-proprietary intermediate formats.          |
| **Provenance**          | Each artifact corresponds to a deterministic pipeline step and log entry. |
| **Auditability**        | Logs under `data/work/logs/` provide complete traceability of ETL events. |

---

## 🧩 Related Directories

| Path              | Purpose                                                    |
| :---------------- | :--------------------------------------------------------- |
| `data/raw/`       | Immutable source data snapshots.                           |
| `data/processed/` | Cleaned and validated dataset outputs.                     |
| `data/checksums/` | SHA-256 manifests for all processed data.                  |
| `data/stac/`      | STAC catalog and collection metadata for public discovery. |

---

## 📅 Version History

| Version    | Date       | Summary                                                          |
| :--------- | :--------- | :--------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial creation of the work directory documentation.            |
| **v1.1.0** | 2025-10-10 | Expanded MCP integration, CI/CD context, and maintenance policy. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Work Fast. Validate Often. Keep It Clean.”*
📍 [`data/work/`](.) · Temporary workspace for intermediate and transient files under MCP governance.

</div>
```
