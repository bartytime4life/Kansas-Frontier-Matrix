<div align="center">

# 🧰 Kansas Frontier Matrix — **Tools & Utilities**  
`tools/utils/`

**Automation · Integrity · Reproducibility**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Test)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blueviolet)](../../../.github/workflows/stac-validate.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-yellow)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)

</div>

---

## 🧭 Overview

`tools/utils/` contains the **shared command-line utilities and helper scripts** that power reproducible workflows across the **Kansas Frontier Matrix (KFM)** ecosystem.  
Each script implements **MCP-DL v6.3** reproducibility, ensuring verifiable provenance, deterministic outputs, and standardized logging for ETL, CI/CD, and data versioning.

> *“Automation with integrity — every byte tells a story.”*

---

## 🧱 Directory Structure

```text
tools/utils/
├── checksum.py           # Compute/verify SHA-256 hashes for provenance tracking
├── convert_geojson.py    # Reproject & convert GIS formats (Shapefile ↔ GeoJSON ↔ COG)
├── generate_stac.py      # Build & validate STAC Items and Collections
├── validate_json.py      # Validate JSON metadata using JSON Schema + DCAT
├── lint_markdown.sh      # Markdown & link linting for documentation QA
├── fetch_remote.py       # Robust HTTP/API downloader with provenance logging
├── summarize_logs.py     # Summarize & analyze CI pipeline and provenance logs
├── requirements.txt      # Python dependencies for utils
└── README.md
```

---

## 🧩 Core Functions

| Script | Purpose | Common Use |
| :------| :--------| :----------|
| `checksum.py` | Generate & verify **SHA-256** hashes for data integrity | Audit raw/processed datasets |
| `convert_geojson.py` | Convert GIS layers between open formats (EPSG:4326) | Transform raw shapefiles |
| `generate_stac.py` | Build STAC-compliant metadata entries | Register processed assets |
| `validate_json.py` | Validate STAC/DCAT/JSON Schema compliance | Metadata quality control |
| `lint_markdown.sh` | Check Markdown formatting & broken links | Docs CI quality gate |
| `fetch_remote.py` | Download & log datasets from APIs or archives | Fetch NOAA/USGS/KHS feeds |
| `summarize_logs.py` | Aggregate structured logs from pipelines | Generate audit summaries |

Each script provides `--help` flags and writes structured logs to `/logs/utils/`.

---

## ⚙️ Environment Setup

```bash
conda create -n kfm-utils python=3.11 -y
conda activate kfm-utils
pip install -r tools/utils/requirements.txt
```

**Requirements Example:**
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

| Pipeline Stage | Utility Used | Output |
| :--------------| :------------| :------|
| Data Provenance | `checksum.py`, `summarize_logs.py` | Logs + checksums |
| Data Validation | `validate_json.py`, `generate_stac.py` | Valid JSON metadata |
| Documentation QA | `lint_markdown.sh` | CI lint reports |
| Automation Hooks | `fetch_remote.py` | Synced raw datasets |
| Geo Conversion | `convert_geojson.py` | COG + GeoJSON outputs |

These utilities run automatically via:
- `make validate`
- `.github/workflows/stac-validate.yml`
- `.github/workflows/ci.yml`

---

## 🧠 Example Usage

```bash
# Validate JSON metadata
python tools/utils/validate_json.py data/sources/

# Generate STAC entries from processed assets
python tools/utils/generate_stac.py --input data/processed/ --output data/stac/

# Verify dataset integrity
python tools/utils/checksum.py verify --dir data/raw/

# Lint documentation
bash tools/utils/lint_markdown.sh
```

---

## 📦 Dependencies

| Type | Tool | Purpose |
| :----| :----| :-------|
| **Python** | `jsonschema`, `pystac`, `requests` | Validation, STAC creation, HTTP |
| **CLI** | `make`, `jq`, `bash` | Pipeline orchestration |
| **QA** | `markdownlint`, `linkchecker` | Docs linting and link validation |

---

## 🧾 Provenance & Logging

Every execution appends an entry to `logs/provenance.log` in structured format:

```
[YYYY-MM-DD HH:MM:SS] [user] [tool] [target] [status] [commit-sha]
```

Log summaries can be compiled via:
```bash
python tools/utils/summarize_logs.py --input logs/ --report reports/provenance_summary.json
```

---

## 🧩 Development Workflow

1. Add a new script under `tools/utils/`.
2. Include header metadata:
   ```python
   # Tool: fetch_remote.py
   # Version: 1.3.1
   # Author: @kfm-architecture
   # Last Updated: 2025-10-17
   # License: MIT
   ```
3. Implement CLI (`argparse` / `click`), write structured logs.
4. Add tests under `tests/tools/test_utils.py`.
5. Update Makefile targets and README.md.
6. Run `make validate` before committing.

> Prototype new ideas in `/tools/notebooks/` before merging into production utilities.

---

## 🧠 MCP Compliance Checklist

| Principle           | Implementation Example |
| :------------------ | :--------------------- |
| **Documentation-First** | YAML headers, inline docstrings, and usage examples |
| **Reproducibility** | Deterministic CLI + consistent hashes |
| **Provenance** | SHA-256 checks + log lineage per run |
| **Open Standards** | STAC 1.0 · JSON Schema · DCAT 2.0 |
| **Auditability** | CI validation + structured logs |
| **Accessibility** | CLI help text, readable outputs, WCAG-safe colors |

---

## 🔗 Related Documentation

- **Main Tools Index** — `tools/README.md`  
- **ETL Pipelines** — `src/pipelines/README.md`  
- **Data Architecture** — `docs/architecture/data-architecture.md`  
- **MCP Standards** — `docs/standards/README.md`  
- **STAC Catalog Guide** — `data/stac/README.md`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.2.0` |
| **Codename** | *Deterministic CLI Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-data · @kfm-architecture |
| **License** | MIT |
| **Alignment** | STAC 1.0 · JSON Schema · DCAT 2.0 · MCP-DL v6.3 |
| **Maturity** | Stable / Production |

---

## 📜 License

All utilities are released under **MIT License**.  
© 2025 Kansas Frontier Matrix — built under **MCP-DL v6.3** for auditable, deterministic, and open automation.

> *“Automation with integrity — every tool leaves a verifiable fingerprint.”*
