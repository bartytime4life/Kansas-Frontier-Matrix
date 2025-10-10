<div align="center">

# ⚙️ Kansas Frontier Matrix — Work Directory  
`data/work/`

**Mission:** Provide a **temporary, sandboxed workspace** for intermediate files,  
debug outputs, and transient artifacts created during ETL, validation, and testing  
within the Kansas Frontier Matrix (KFM) data pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/` directory serves as a **volatile working area** for data engineers and automated processes  
running Kansas Frontier Matrix pipelines. It is **not version-controlled** for data content (only structure and documentation)  
and is intended exclusively for temporary use during:

- ETL and data transformation workflows  
- STAC catalog generation and validation runs  
- Thumbnail creation and checksum computation  
- Experimental data processing and QA/QC checks  

All files stored here are **ephemeral** and can be safely deleted or regenerated at any time.

---

## 🗂️ Directory Layout

```bash
data/work/
├── README.md
├── tmp/                  # Transient data used during ETL processing
├── cache/                # Cached intermediate data or validation results
├── staging/              # Temporary outputs awaiting integration into processed/
└── logs/                 # Runtime logs for debugging and testing
````

> **Note:** The contents of this directory are excluded via `.gitignore`
> to prevent accidental commits of large or temporary files.

---

## ⚠️ Policy

| Rule                   | Description                                               |
| :--------------------- | :-------------------------------------------------------- |
| **Ephemeral Storage**  | Files here may be deleted or overwritten at any time.     |
| **No Persistent Data** | Long-term datasets belong under `data/processed/`.        |
| **CI/CD Safety**       | Work data is ignored by CI except for validation outputs. |
| **Version Control**    | Only structure, configs, and this README are tracked.     |

---

## ⚙️ Typical Use Cases

| Task                    | Example                                                         |
| :---------------------- | :-------------------------------------------------------------- |
| **Pipeline Debugging**  | Temporary raster subsets or vector slices during ETL runs.      |
| **Checksum Validation** | Hash generation and revalidation staging.                       |
| **Thumbnail Rendering** | Intermediate images before compression/export.                  |
| **STAC Testing**        | Draft STAC validation before commit to `data/stac/`.            |
| **Model Training Prep** | Transient tables used for ML preprocessing or NLP tokenization. |

---

## 🧰 Maintenance

**This folder should remain clean.**

* Old or unused files should be purged automatically via scheduled maintenance.
* Developers may manually clear contents using the provided Make target:

```bash
make clean-work
```

Or directly from the CLI:

```bash
rm -rf data/work/tmp/* data/work/cache/* data/work/staging/* data/work/logs/*
```

All critical outputs are **regenerated automatically** by domain-specific targets such as
`make terrain`, `make hydrology`, `make landcover`, etc.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | README defines directory purpose, retention, and safety rules.     |
| **Reproducibility**     | Ensures transient processes can be re-run cleanly.                 |
| **Open Standards**      | No proprietary formats; all temporary data mirror KFM conventions. |
| **Provenance**          | Work artifacts trace back to deterministic pipeline inputs.        |
| **Auditability**        | Logs and caches provide transparent intermediate records.          |

---

## 📎 Related Directories

| Path              | Description                            |
| :---------------- | :------------------------------------- |
| `data/raw/`       | Immutable original datasets.           |
| `data/processed/` | Finalized and validated outputs.       |
| `data/checksums/` | Integrity tracking for validated data. |
| `data/stac/`      | Published metadata catalog.            |

---

## 📅 Version History

| Version    | Date       | Summary                                                  |
| :--------- | :--------- | :------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial creation of the working directory documentation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Work Fast. Validate Often. Keep It Clean.”*
📍 [`data/work/`](.) · Temporary workspace for intermediate and transient files.

</div>
