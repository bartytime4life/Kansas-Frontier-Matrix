<div align="center">

# 🧰 Kansas Frontier Matrix — **Tools & Utilities**  
`/tools/utils/`

**Automation · Integrity · Reproducibility**  
*“Every Tool Leaves a Trace — Every Trace Ensures Reproducibility.”*

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Test)](../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blueviolet.svg)](../../.github/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)
[![Maturity: Production](https://img.shields.io/badge/Maturity-Production-orange)](../../docs/)

</div>

---

## 🧭 Overview

The `/tools/utils/` directory contains **shared command-line utilities** and **automation scripts** used throughout the **Kansas Frontier Matrix (KFM)** project.  

These tools uphold the **Master Coder Protocol (MCP)** — emphasizing **documentation-first**, **reproducibility**, and **traceability** — by automating data validation, provenance logging, and pipeline reproducibility.

Key functions include:

- 🔐 **Checksum validation** (SHA-256 integrity verification)  
- 🌎 **Geospatial conversions** (Shapefile → GeoJSON / COG)  
- 🧩 **STAC & JSON Schema validation**  
- ⚙️ **Data fetching, cleaning, and transformation**  
- 🧮 **Provenance logging and trace audits**  
- 🧹 **Linting & documentation checks for CI/CD pipelines**

Each utility script is self-contained, idempotent, and versioned — every action leaves an auditable trace in the project’s provenance log.

---

## 🗂️ Directory Layout

```bash
tools/
├── utils/
│   ├── checksum.py           # Compute & verify SHA-256 hashes
│   ├── convert_geojson.py    # Convert shapefiles or CSVs to GeoJSON
│   ├── generate_stac.py      # Build & validate STAC catalogs
│   ├── validate_json.py      # Validate JSON files against schemas
│   ├── lint_markdown.sh      # Run markdown linting & link checks
│   ├── fetch_remote.py       # Download or fetch from APIs w/ logging
│   ├── summarize_logs.py     # Summarize CI / pipeline logs
│   ├── __init__.py
│   └── README.md             # (this file)
└── ...

Each script follows the MCP-DL protocol:
	1.	🧾 Docstring header — author, version, date, purpose
	2.	⚙️ CLI entrypoint using argparse or click
	3.	🧱 Logging and error handling (logs → /logs/utils/)
	4.	📜 Provenance entry (timestamp, commit ID, result)
	5.	🧪 Unit tests in tests/tools/test_utils.py

⸻

⚙️ Usage Examples

Run utilities individually or through the Makefile:

# ✅ Validate all source JSON manifests
python tools/utils/validate_json.py data/sources/

# 🌎 Generate STAC catalog from processed data
python tools/utils/generate_stac.py --input data/processed/ --output data/stac/

# 🔐 Verify data integrity
python tools/utils/checksum.py verify --dir data/raw/

# 🧹 Lint and check Markdown docs
bash tools/utils/lint_markdown.sh

These scripts integrate with CI/CD workflows:
	•	.github/workflows/ci.yml
	•	.github/workflows/stac-validate.yml
	•	Makefile → make validate, make checksums, make stac

⸻

🧮 Dependencies

Category	Library / Tool	Purpose
Python 3.11+	jsonschema	Validate metadata & STAC files
	requests, urllib3	Fetch APIs / remote datasets
	pystac, pystac-client	STAC indexing and validation
	hashlib, argparse	Core CLI / hashing / logging
System	make, jq, bash	Command automation & parsing
Linting	markdownlint, linkcheck	CI documentation QA

Install dependencies via:

pip install -r requirements.txt


⸻

🧱 Integration with MCP Workflows

All utilities contribute to MCP verification chains:
	•	🪶 Provenance Logging → Every operation records [timestamp, user, commit, action]
	•	🔄 Reproducibility → Deterministic outputs, verifiable hashes
	•	🧩 Validation → STAC 1.0, DCAT 2.0, GeoJSON schema checks
	•	🔔 Automation Hooks → Triggered via pre-commit, CI workflows, or scheduled jobs

This ensures full auditability of all data operations — every fetch, hash, or conversion can be retraced through commit history and log archives.

⸻

🧠 Best Practices
	•	Keep utilities stateless and idempotent.
	•	Include --help and example usage in every CLI.
	•	Never hardcode paths — use relative or config variables.
	•	Log all results to /logs/provenance.log.
	•	Follow PEP 8 + Black formatting + type hints.
	•	Document each new utility in this README under Directory Layout.
	•	Add unit tests for every tool added or modified.

⸻

🧾 Contribution Workflow

When adding a new tool:
	1.	Create the script in /tools/utils/ (verb_noun.py convention).
	2.	Add inline header:

# Tool: fetch_remote.py
# Version: 1.3.0
# Author: @kfm-architecture
# License: MIT
# Last Updated: 2025-10-16


	3.	Write unit tests → tests/tools/test_utils.py.
	4.	Update this README (under Layout).
	5.	Add Makefile target or CI trigger if applicable.
	6.	Ensure provenance logging works.
	7.	Commit with Signed-off-by: and include Docs: Updated tools/utils/README.md.

⸻

🧾 Version History

Version	Date	Author	Description
v1.0.0	2025-10-16	@kfm-architecture	Initial release — baseline utilities doc
v1.1.0	—	—	—


⸻

📚 References
	•	🧭 Architecture Overview
	•	🗂️ Data & File Architecture
	•	📘 MCP Markdown Standards
	•	🛰️ STAC Specification 1.0
	•	📖 W3C DCAT 2.0 Recommendation

⸻


<div align="center">


🏗️ Kansas Frontier Matrix — A Living Atlas of Time · Terrain · History
Maintained under the Master Coder Protocol v6.2

</div>
```