---
title: "🧰 Kansas Frontier Matrix — Tools & Utilities Suite"
path: "tools/utils/README.md"
version: "v1.4.2"
last_updated: "2025-10-22"
review_cycle: "Quarterly"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v1.4.2/sbom.spdx.json"
manifest_ref: "releases/v1.4.2/manifest.zip"
doc_id: "KFM-TOOLS-UTILS-RMD-v1.4.2"
maintainers: ["@kfm-data", "@kfm-architecture"]
approvers: ["@kfm-qa", "@kfm-security"]
ci_required_checks: ["docs-validate", "code-lint", "stac-validate", "checksum-verify"]
license: "MIT"
design_stage: "Operational / Maintenance"
mcp_version: "MCP-DL v6.3"
alignment: ["STAC 1.0", "DCAT 3.0", "FAIR", "CIDOC CRM", "OWL-Time"]
status: "Platinum+ / Stable"
tags: ["automation", "etl", "provenance", "stac", "dcat", "fair", "ai-focus", "markdown-qa"]
---

<div align="center">

# 🧰 Kansas Frontier Matrix — **Tools & Utilities Suite**  
`tools/utils/README.md`

**Automation · Provenance · Validation · Reproducibility**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Test)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blueviolet)](../../../.github/workflows/stac-validate.yml)
[![Checksum Verify](https://img.shields.io/badge/Checksums-Verified-success)](../../../.github/workflows/checksum.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-yellow)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Data%20Ethics-blue)](https://www.go-fair.org/fair-principles/)

</div>

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Directory Structure](#️-directory-structure)
- [Core Functions](#-core-functions)
- [Environment Setup](#️-environment-setup)
- [Integration with Workflows](#-integration-with-workflows)
- [Example Usage](#-example-usage)
- [Dependencies](#-dependencies)
- [Provenance & Logging](#-provenance--logging)
- [Development Workflow](#-development-workflow)
- [AI & Focus Mode Support](#-ai--focus-mode-support)
- [Security & Integrity](#-security--integrity)
- [MCP Compliance Checklist](#-mcp-compliance-checklist)
- [Related Documentation](#-related-documentation)
- [Versioning & Metadata](#-versioning--metadata)
- [License](#-license)
- [Version History](#-version-history)

---

## 📚 Overview

`tools/utils/` contains the shared **command-line utilities and helper scripts** that power reproducible workflows across the **Kansas Frontier Matrix (KFM)** ecosystem.  
Each utility adheres to **MCP-DL v6.3**, ensuring **verifiable provenance**, deterministic outputs, and standardized logging across ETL, CI/CD, and data versioning pipelines.

> *“Automation with integrity — every byte leaves a verifiable fingerprint.”*

These utilities implement reproducibility protocols, integrating directly with `Makefile` targets and CI workflows to maintain FAIR-compliant, CIDOC CRM–aligned data processing.

---

## 🗂️ Directory Structure

```text
tools/utils/
├── checksum.py           # Compute/verify SHA-256 hashes for provenance tracking
├── convert_geojson.py    # Reproject & convert GIS formats (Shapefile ↔ GeoJSON ↔ COG)
├── generate_stac.py      # Build & validate STAC Items and Collections
├── validate_json.py      # Validate JSON metadata (STAC/DCAT/Schema)
├── fetch_remote.py       # Fetch & log external datasets with provenance entries
├── lint_markdown.sh      # Markdown & link linting for documentation QA
├── summarize_logs.py     # Aggregate & summarize ETL/CI provenance logs
├── requirements.txt      # Python dependencies for utils
└── README.md
```

Each script is self-documented (`--help`), versioned, and verified via CI (`.github/workflows/`).

---

## 🧩 Core Functions

| Script | Purpose | Common Use |
| :------| :--------| :----------|
| `checksum.py` | Generate & verify **SHA-256** hashes | Dataset integrity verification |
| `convert_geojson.py` | Convert GIS layers between formats (EPSG:4326) | Transform archival shapefiles |
| `generate_stac.py` | Build STAC-compliant Items/Collections | Register processed datasets |
| `validate_json.py` | Validate metadata schemas (STAC/DCAT/JSON) | Metadata quality assurance |
| `fetch_remote.py` | Download & log data from APIs or archives | NOAA/USGS/KHS data ingestion |
| `lint_markdown.sh` | Lint Markdown & check links | Docs CI compliance |
| `summarize_logs.py` | Aggregate structured logs from pipelines | Provenance summaries & metrics |

All outputs are logged to `/logs/utils/` for audit and reproducibility.

---

## ⚙️ Environment Setup

```bash
conda create -n kfm-utils python=3.11 -y
conda activate kfm-utils
pip install -r tools/utils/requirements.txt
```

**requirements.txt**
```txt
jsonschema
pystac
requests
urllib3
markdownlint
linkchecker
rasterio
```

---

## 🧮 Integration with Workflows

| Stage | Utility | Output |
| :---- | :-------| :------|
| Provenance | `checksum.py`, `summarize_logs.py` | Logs + checksums |
| Data Validation | `validate_json.py`, `generate_stac.py` | Valid JSON metadata |
| Docs QA | `lint_markdown.sh` | Markdown/Link validation |
| Automation | `fetch_remote.py` | Synced datasets |
| Geo Conversion | `convert_geojson.py` | GeoJSON/COG artifacts |

Run through unified automation:

```makefile
make setup          # installs dependencies
make data           # runs ETL pipeline
make validate       # executes all validation gates
make stac-validate  # STAC/DCAT compliance check
make docs-validate  # Lint Markdown & metadata
```

---

## 🧠 Example Usage

```bash
# Validate metadata
python tools/utils/validate_json.py data/sources/

# Generate STAC entries
python tools/utils/generate_stac.py --input data/processed/ --output data/stac/

# Verify dataset integrity
python tools/utils/checksum.py verify --dir data/raw/

# Lint Markdown
bash tools/utils/lint_markdown.sh
```

> **Tip:** Run `make validate` to execute the entire validation pipeline end-to-end.

---

## 📦 Dependencies

| Type | Tool | Function |
| :----| :----| :--------|
| **Python** | `jsonschema`, `pystac`, `requests` | Validation, STAC creation |
| **CLI** | `make`, `jq`, `bash` | Orchestration, parsing |
| **QA** | `markdownlint`, `linkchecker` | Documentation integrity |

---

## 🧾 Provenance & Logging

Each utility logs standardized records in `logs/provenance.log`:

```
[YYYY-MM-DD HH:MM:SS] [user] [tool] [target] [status] [commit-sha]
```

Summarize provenance reports:

```bash
python tools/utils/summarize_logs.py --input logs/ --report reports/provenance_summary.json
```

These records form the foundation for reproducibility validation and AI cross-referencing within Focus Mode.

---

## 🧩 Development Workflow

1. Add or update a script under `tools/utils/`
2. Include metadata header:
   ```python
   # Tool: fetch_remote.py
   # Version: 1.4.2
   # Author: @kfm-architecture
   # Last Updated: 2025-10-22
   # License: MIT
   ```
3. Implement CLI (`argparse` or `click`)
4. Write structured logs
5. Add test under `tests/tools/test_utils.py`
6. Update Makefile + README
7. Run `make validate` before committing

> **Note:** Prototype new ideas under `/tools/notebooks/` before merging into production.

---

## 🤖 AI & Focus Mode Support

Utilities such as `summarize_logs.py` and `generate_stac.py` feed metadata directly into **AI Focus Mode**, providing structured summaries, confidence metrics, and provenance trails for the frontend assistant.  
These enable queries like “show all validated datasets with checksum errors since last build” and provide Focus Mode analytics on ETL performance over time.

---

## 🔐 Security & Integrity

- Utilities **must not** alter source data in-place — all operations create new immutable outputs.  
- Sensitive credentials are loaded from `.env` or sealed configuration, never hard-coded.  
- Checksum validation via `checksum.py` is required before dataset publication or release.  
- CI enforces integrity gates (`checksum-verify`) before merges to main.

---

## 🧠 MCP Compliance Checklist

| Principle | Implementation |
| :---------| :--------------|
| **Documentation-First** | YAML headers + inline docstrings |
| **Reproducibility** | Deterministic CLIs + consistent hashing |
| **Provenance** | SHA-256 validation + structured logs |
| **Open Standards** | STAC 1.0 · DCAT 3.0 · FAIR metadata |
| **Auditability** | CI gates + machine-validated STAC items |
| **Accessibility** | CLI help text, ARIA-safe outputs |

---

## 🔗 Related Documentation

- **Main Tools Index** — `tools/README.md`  
- **ETL Pipelines** — `src/pipelines/README.md`  
- **Data Architecture** — `docs/architecture/data-architecture.md`  
- **MCP Standards** — `docs/standards/README.md`  
- **STAC Catalog Guide** — `data/stac/README.md`  
- **Focus Mode (AI Assistant)** — `docs/features/focus-mode.md`  

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.4.2` |
| **Codename** | *Focus Integration + Ethics Upgrade* |
| **Last Updated** | 2025-10-22 |
| **Maintainers** | @kfm-data · @kfm-architecture |
| **License** | MIT |
| **Alignment** | STAC 1.0 · DCAT 3.0 · FAIR · CIDOC CRM · OWL-Time |
| **Maturity** | Platinum+ / Stable |
| **Design Stage** | Operational / Maintenance |

---

## 📜 License

Released under **MIT License**.  
© 2025 Kansas Frontier Matrix — Built under **MCP-DL v6.3** for deterministic, auditable automation.

> *“Integrity by design — reproducibility by default.”*

---

## 🧩 Version History

| Version | Date | Author | Change Summary |
| :------ | :---- | :------ | :-------------- |
| v1.4.2 | 2025-10-22 | @kfm-architecture | Added footer badges, checksum badge, security section |
| v1.4.1 | 2025-10-22 | @kfm-architecture | Added FAIR badge + Focus Mode linkage |
| v1.4.0 | 2025-10-22 | @kfm-data | Full Platinum README alignment |
| v1.3.0 | 2025-10-21 | @kfm-architecture | STAC/DCAT integration finalized |
| v1.2.0 | 2025-10-17 | @kfm-architecture | Initial MCP-DL v6.3 compliance pass |

---

<div align="center">

[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=CI%20Build)](../../../.github/workflows/ci.yml)
[![Docs Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validate)](../../../.github/workflows/docs-validate.yml)
[![Checksum Verify](https://img.shields.io/badge/Checksums-Verified-success)](../../../.github/workflows/checksum.yml)
[![STAC/DCAT](https://img.shields.io/badge/STAC%2FDCAT-Compliant-blueviolet)](../../../data/stac/)
[![FAIR+CARE Principles](https://img.shields.io/badge/FAIR%20%2B%20CARE-Data%20Ethics-blue)](https://www.go-fair.org/fair-principles/)
[![Status: Platinum+](https://img.shields.io/badge/Status-Platinum%2B-brightgreen)]()

</div>