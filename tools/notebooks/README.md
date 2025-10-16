<div align="center">

# 🧰 Kansas Frontier Matrix — **Tools & Utilities**  
`tools/utils/`

**Automation · Integrity · Reproducibility**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Test)](../../../.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-yellow)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Tools & Utilities (tools/utils/)"
version: "v1.0.0"
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

The `tools/utils/` directory provides **lightweight, reusable automation scripts** and **DevOps helpers**  
for maintaining reproducibility, provenance, and auditability across the **Kansas Frontier Matrix (KFM)** project.

Each utility is designed as a **modular, CLI-based microtool** aligned with **MCP-DL v6.2** —  
meaning every execution is logged, validated, and traceable.

> *“Automation with integrity — every byte tells a story.”*

---

## 🧱 Directory Structure

```text
tools/utils/
├── checksum.py           # Compute / verify SHA-256 file integrity
├── convert_geojson.py    # Convert shapefiles and CSVs to GeoJSON / COG
├── generate_stac.py      # Create & validate STAC items and collections
├── validate_json.py      # Validate JSON files against schemas
├── lint_markdown.sh      # Lint markdowns + check links (docs QA)
├── fetch_remote.py       # Download remote datasets / API data
├── summarize_logs.py     # Summarize provenance & CI logs
├── requirements.txt      # Python dependencies for utilities
└── README.md             # This documentation file
```

---

## 🧩 Purpose & Use Cases

| Utility / Script             | Focus                                                       | Tools / Libraries               |
| :---------------------------- | :---------------------------------------------------------- | :------------------------------ |
| **checksum.py**              | Compute and verify SHA-256 hashes for data integrity        | `hashlib`, `argparse`           |
| **convert_geojson.py**       | Reproject, simplify, and convert vector / raster datasets   | `geopandas`, `rasterio`, `gdal` |
| **generate_stac.py**         | Build and validate STAC Collections & Items                 | `pystac`, `jsonschema`          |
| **validate_json.py**         | Validate JSON and DCAT metadata structures                 | `jsonschema`, `json`            |
| **lint_markdown.sh**         | Run markdown and link-check linting for docs                | `markdownlint`, `linkchecker`   |
| **fetch_remote.py**          | Fetch and sync datasets from APIs (NOAA, USGS, FEMA)       | `requests`, `urllib3`           |
| **summarize_logs.py**        | Aggregate and summarize CI or ETL log files                | `json`, `datetime`, `logging`   |

Each script is **CLI-executable**, self-documented (`--help` flag), and  
logs all actions to `/logs/provenance.log` for MCP compliance.

---

## ⚙️ Environment Setup

### 🧩 Installation

```bash
# Create environment
conda create -n kfm-tools python=3.11 -y
conda activate kfm-tools

# Install dependencies
pip install -r tools/utils/requirements.txt
```

**Example `requirements.txt`:**

```txt
jsonschema
pystac
pystac-client
requests
urllib3
geopandas
rasterio
markdownlint
linkchecker
```

---

## 🧠 Workflow Integration

| Workflow Stage       | Automated Tool(s)                       | Output Artifact / Purpose                      |
| :-------------------- | :-------------------------------------- | :--------------------------------------------- |
| **Data Integrity**    | `checksum.py`                           | SHA-256 verified datasets                      |
| **Metadata QA**       | `validate_json.py`, `generate_stac.py`  | STAC-compliant JSON & metadata validation logs |
| **Documentation QA**  | `lint_markdown.sh`                      | Markdown link & format reports                 |
| **Data Syncing**      | `fetch_remote.py`                       | Fetched API datasets (e.g., NOAA, USGS)        |
| **Provenance Review** | `summarize_logs.py`                     | Log summaries & hash provenance tables         |

Each execution adds a line to the project-wide provenance ledger:  

```
[YYYY-MM-DD HH:MM:SS] [user] [tool] [target] [status] [commit-SHA]
```

---

## 🧩 Example Commands

```bash
# Validate all JSON sources
python tools/utils/validate_json.py data/sources/

# Generate a STAC catalog
python tools/utils/generate_stac.py --input data/processed/ --output data/stac/

# Verify checksums
python tools/utils/checksum.py verify --dir data/raw/

# Lint documentation
bash tools/utils/lint_markdown.sh
```

---

## 🧾 Development Standards

| Requirement            | Description / Expectation                                                  |
| :--------------------- | :------------------------------------------------------------------------ |
| **Naming**             | Use `verb_noun.py` convention for new tools                               |
| **Docstring Header**   | Include tool name, version, author, license, last update                   |
| **CLI Interface**      | Must include `--help` and argument validation                              |
| **Logging**            | Write to `/logs/utils/` and append to `provenance.log`                    |
| **Testing**            | Add or update tests in `tests/tools/test_utils.py`                        |
| **Formatting**         | Use `black`, `ruff`, and `mypy` for style & type consistency               |
| **Docs Update**        | Update this README when adding or editing utilities                       |

Example header:

```python
# Tool: fetch_remote.py
# Version: 1.2.0
# Author: @kfm-architecture
# License: MIT
# Last Updated: 2025-10-16
```

---

## 🧩 MCP Compliance Matrix

| MCP Principle       | Implementation Example                                 |
| :------------------ | :----------------------------------------------------- |
| **Documentation-first** | Inline metadata and YAML-style script headers         |
| **Reproducibility**     | Deterministic CLI with checksum verification          |
| **Provenance**          | Log chains and hash-based audit trails                |
| **Open Standards**      | STAC 1.0 · JSON Schema · DCAT 2.0                     |
| **Auditability**        | CI validation via `.github/workflows/`                |
| **Accessibility**       | CLI help text and color-safe outputs                  |

---

## 🔗 Related Documentation

* **Tools Index** — `tools/README.md`  
* **ETL Pipelines** — `src/pipelines/README.md`  
* **Data Architecture** — `docs/architecture/data-architecture.md`  
* **MCP Markdown Rules** — `docs/standards/markdown_rules.md`  
* **STAC Catalog Guide** — `data/stac/README.md`

---

## 📜 License

All utilities are released under the **MIT License**.  
© 2025 *Kansas Frontier Matrix* — developed under **MCP-DL v6.2** for transparent and reproducible research.

> *“Automation is the handwriting of reproducibility — make every action traceable.”*