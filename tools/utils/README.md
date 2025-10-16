<div align="center">

# 🧰 Kansas Frontier Matrix — **Tools & Utilities**  
`/tools/utils/`

**Helper Scripts · DevOps Automation · Data ETL Utilities**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)
[![Build & Test](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Test)](../../.github/workflows/ci.yml)
[![Validated](https://img.shields.io/badge/STAC-Validated-blueviolet.svg)](../../.github/workflows/stac-validate.yml)

</div>

---

## 🧭 Overview

The `/tools/utils/` directory houses shared command-line utilities, helper scripts, and developer tools that automate core operations across the **Kansas Frontier Matrix (KFM)** monorepo.  

These scripts support the project’s **Master Coder Protocol (MCP)** principles — documentation-first, reproducibility, and open standards — by enabling repeatable data and environment tasks such as:

- Fetching and verifying external data sources  
- Running integrity checks and computing SHA-256 digests  
- Converting GIS layers to open formats (GeoJSON, Cloud-Optimized GeoTIFF)  
- Performing STAC validation and JSON Schema checks  
- Automating builds, tests, and provenance logging  
- Simplifying developer setup and environment synchronization  

Every utility in this directory is fully documented, version-controlled, and designed to be reproducible across environments (Linux / macOS / Windows WSL).

---

## ⚙️ Structure

```bash
tools/
├── utils/
│   ├── checksum.py           # Compute & verify SHA-256 hashes for data integrity
│   ├── convert_geojson.py    # Convert shapefiles or CSVs to GeoJSON
│   ├── generate_stac.py      # Build STAC catalogs for processed assets
│   ├── validate_json.py      # Validate JSON files against schemas
│   ├── lint_markdown.sh      # Run markdown & link-checking linters
│   ├── fetch_remote.py       # Generic URL / API fetcher with logging
│   ├── summarize_logs.py     # Summarize CI or pipeline logs for review
│   ├── __init__.py
│   └── README.md             # (this file)
└── ...

Each script follows a consistent pattern:
	1.	CLI entrypoint (via argparse or click)
	2.	Inline documentation (usage + examples)
	3.	Configurable logging & error handling
	4.	Integration hooks for CI/CD or Makefile targets

⸻

🧩 Usage

Run utilities directly or through the project’s make commands:

# Validate all JSON sources against schemas
python tools/utils/validate_json.py data/sources/

# Generate a STAC catalog for processed layers
python tools/utils/generate_stac.py --input data/processed/ --output data/stac/

# Verify dataset integrity
python tools/utils/checksum.py verify --dir data/raw/

# Lint documentation and check links
bash tools/utils/lint_markdown.sh

These commands can also be invoked automatically in CI workflows or via scheduled pipelines (.github/workflows/ci.yml, Makefile).

⸻

🧱 Dependencies

Category	Library / Tool	Purpose
Python 3.11+	jsonschema	Validate JSON & STAC metadata
	requests, urllib3	HTTP fetching & API integration
	pystac, pystac-client	Build and validate STAC catalogs
	hashlib, argparse	Core system modules for hashing & CLI
CLI / System	make, bash, jq	Build automation & JSON parsing
Linting	markdownlint, linkcheck	Documentation quality gates

Install all Python dependencies with:

pip install -r requirements.txt


⸻

🧮 Integration with MCP Workflows

Each utility contributes to MCP verification chains:
	•	Provenance Logging: Every operation appends an entry to /logs/provenance.log, capturing timestamp, user, commit ID, and hash.
	•	Reproducibility: Output directories are deterministic; identical inputs yield identical hashes.
	•	Validation: Utilities double-check schema conformance (STAC 1.0, DCAT 2.0, GeoJSON).
	•	Automation Hooks: All utilities are callable from CI workflows (pre-commit, validate.yml, stac-validate.yml) ensuring the repo’s continuous auditability.

⸻

🧠 Best Practices
	•	Write all new scripts as stateless, idempotent CLI tools.
	•	Include a --help flag with examples.
	•	Store configuration in config.yaml or environment variables — avoid hard-coding paths.
	•	Log to stdout and /logs/utils/ using the MCP logging format:

[YYYY-MM-DD HH:MM:SS] [user] [action] [target] [status]


	•	Follow PEP 8 / Black style guidelines and include type hints.
	•	Add a short usage example to each script’s docstring.

⸻

🧾 Contributing

When adding a new utility:
	1.	Place it under /tools/utils/ with a descriptive name (verb_noun.py).
	2.	Include an inline docstring (purpose, arguments, examples).
	3.	Add an entry in this README under the Structure section.
	4.	Create or update unit tests in tests/tools/test_utils.py.
	5.	Update the Makefile and CI workflow if integration is needed.
	6.	Document provenance & version in the script header:

# Tool: fetch_remote.py
# Version: 1.2.0  |  Last updated: 2025-10-16
# Author: @kfm-architecture
# License: MIT



All contributions are reviewed for reproducibility, clarity, and MCP compliance before merge.

⸻

📚 References
	•	KFM Architecture Overview
	•	Data & File Architecture
	•	MCP Documentation Guide
	•	STAC Specification 1.0.0
	•	DCAT 2.0 Recommendation (W3C)

⸻

🧾 Version History

Version	Date	Author	Notes
v1.0.0	2025-10-16	@kfm-architecture	Initial release of Tools & Utilities README
v1.0.1	—	—	—


⸻


<div align="center">


✅ “Every Tool Leaves a Trace — Every Trace Ensures Reproducibility.”

</div>
