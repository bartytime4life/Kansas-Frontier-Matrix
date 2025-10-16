<div align="center">

# 🧰 Kansas Frontier Matrix — **Tools & Utilities**  
`tools/utils/`

**Automation · Integrity · Reproducibility**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Test)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blueviolet)](../../../.github/workflows/stac-validate.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-yellow)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Tools & Utilities (tools/utils/)"
version: "v1.1.0"
last_updated: "2025-10-16"
owners: ["@kfm-architecture", "@kfm-data"]
tags: ["tools","scripts","utilities","etl","devops","automation","mcp"]
license: "MIT"
semantic_alignment:
  - MCP-DL v6.2 Reproducibility
  - STAC 1.0 Asset Validation
  - JSON Schema Compliance
  - DCAT 2.0 Metadata Alignment
---
```

---

## 🧭 Overview

The `tools/utils/` directory provides **shared command-line utilities and automation scripts**  
that keep the **Kansas Frontier Matrix (KFM)** monorepo reproducible, auditable, and verifiable.  

These tools ensure **end-to-end traceability** across ETL pipelines, CI/CD workflows, and dataset versioning.  
Every script adheres to the **Master Coder Protocol (MCP-DL v6.2)** — meaning each operation is  
**documented, reproducible, and leaves a verifiable digital fingerprint.**

> *Automation with Integrity — every byte tells a story.*

---

## 🧱 Directory Structure

```text
tools/utils/
├── checksum.py           # Compute / verify SHA-256 hashes
├── convert_geojson.py    # Convert Shapefile ↔ GeoJSON ↔ COG pipeline
├── generate_stac.py      # Build and validate STAC catalog items
├── validate_json.py      # JSON Schema and DCAT validation
├── lint_markdown.sh      # Markdown + link linting for CI
├── fetch_remote.py       # Robust HTTP/API data fetcher with logging
├── summarize_logs.py     # Summarize CI and pipeline runs
├── requirements.txt      # Python dependencies for CLI tools
└── README.md             # This documentation file
```

---

## 🧩 Purpose & Key Functions

| Utility / Script | Core Purpose | Typical Use Case |
| :---------------- | :------------ | :--------------- |
| **checksum.py** | Compute and verify SHA-256 hashes for files | Verify dataset integrity before merge |
| **convert_geojson.py** | Reproject and convert geospatial layers to open formats | Transform Shapefile → GeoJSON → COG |
| **generate_stac.py** | Create STAC Item and Collection metadata | Register processed assets in `data/stac/` |
| **validate_json.py** | Validate JSON and STAC against schemas | CI metadata checks before deployment |
| **lint_markdown.sh** | Run Markdown lint + link checker | Documentation quality gate in CI |
| **fetch_remote.py** | Automate data downloads and API fetches | Pull NOAA / USGS feeds into `data/raw/` |
| **summarize_logs.py** | Aggregate and analyze pipeline logs | Generate provenance summaries for audits |

Each script is **CLI-driven**, self-documented (`--help` flag), and writes  
structured logs to `/logs/utils/` for provenance tracking and CI auditing.

---

## ⚙️ Environment Setup

### 🧩 Installation

```bash
# Create environment
conda create -n kfm-tools python=3.11 -y
conda activate kfm-tools

# Install requirements
pip install -r tools/utils/requirements.txt
```

**Example `requirements.txt`:**

```txt
jsonschema
pystac
pystac-client
requests
urllib3
markdownlint
linkchecker
```

---

## 🧮 Integration with MCP Pipelines

| MCP Stage | Automated Utility | Output Artifact |
| :--------- | :---------------- | :-------------- |
| **Provenance Logging** | `checksum.py`, `summarize_logs.py` | `logs/provenance.log` |
| **Data Validation** | `validate_json.py`, `generate_stac.py` | Validated metadata JSON |
| **Reproducibility Check** | `checksum.py` | Verified SHA-256 digests |
| **Documentation QA** | `lint_markdown.sh` | CI lint reports |
| **Automation Hooks** | `fetch_remote.py` | Synced `data/raw/` sources |

These utilities integrate directly with:
- `.github/workflows/ci.yml`
- `.github/workflows/stac-validate.yml`
- Makefile automation targets (`make validate`, `make fetch`, `make stac`)

---

## 🧠 Usage Examples

```bash
# Validate all source metadata
python tools/utils/validate_json.py data/sources/

# Generate a STAC catalog from processed assets
python tools/utils/generate_stac.py --input data/processed/ --output data/stac/

# Verify hash integrity of raw files
python tools/utils/checksum.py verify --dir data/raw/

# Run Markdown lint and link checks
bash tools/utils/lint_markdown.sh
```

---

## 📦 Dependencies Summary

| Category | Library / Tool | Purpose |
| :-------- | :-------------- | :-------- |
| **Python 3.11+** | `jsonschema`, `pystac` | Metadata validation / STAC creation |
|  | `requests`, `urllib3` | Remote fetch & API support |
| **CLI Tools** | `make`, `jq`, `bash` | Build automation / JSON filtering |
| **QA Tools** | `markdownlint`, `linkchecker` | Documentation validation |

---

## 🧾 Provenance & Logging Standard

Every execution appends to `logs/provenance.log` in a standard MCP format:

```
[YYYY-MM-DD HH:MM:SS] [user] [tool] [target] [status] [commit-sha]
```

These logs form the **chain of custody** for all ETL and verification activities  
and are periodically summarized via `summarize_logs.py` for auditing.

---

## 🧩 Development Workflow

1. 🧱 **Add Tool** → create a new script under `tools/utils/`  
2. 🧾 **Header Metadata**  
   ```python
   # Tool: fetch_remote.py
   # Version: 1.3.0
   # Author: @kfm-architecture
   # Last Updated: 2025-10-16
   # License: MIT
   ```
3. ⚙️ Implement CLI (using `argparse` or `click`)  
4. ✅ Add Unit Tests → `tests/tools/test_utils.py`  
5. 🧮 Update Makefile target and this README  
6. 🔐 Commit with `Signed-off-by:` and append provenance record  

---

## 🧾 MCP Compliance Checklist

| MCP Principle | Implementation |
| :------------- | :-------------- |
| **Documentation-First** | YAML headers + inline docstrings |
| **Reproducibility** | Deterministic CLI output + hash checks |
| **Provenance** | Logged execution chain + commit trace |
| **Open Standards** | STAC 1.0 · JSON Schema · DCAT 2.0 |
| **Auditability** | CI validation · automated reports |
| **Accessibility** | Clear help text · color-safe CLI output |

---

## 🔗 Related Documentation

* **Tools Index** — `tools/README.md`  
* **ETL Pipelines** — `src/pipelines/README.md`  
* **Data Architecture** — `docs/architecture/data-architecture.md`  
* **MCP Standards** — `docs/standards/markdown_rules.md`  
* **STAC Catalog Guide** — `data/stac/README.md`

---

## 📜 License

All utilities are released under the **MIT License**.  
© 2025 *Kansas Frontier Matrix* — developed under **MCP-DL v6.2** for open, auditable, and reproducible research.

> *“Automation with Integrity — because every byte tells a story.”*