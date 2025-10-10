<div align="center">

# 📊 Kansas Frontier Matrix — Tabular Checksums  
`data/processed/checksums/tabular/`

**Mission:** Safeguard the **integrity, provenance, and reproducibility** of all processed **tabular datasets** —  
including census, agricultural, demographic, and economic data — within the Kansas Frontier Matrix (KFM) system.  
By maintaining SHA-256 checksums, this directory ensures analytical trust and reproducible scientific outcomes.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **SHA-256 checksum files (`.sha256`)** for all processed **tabular datasets** in KFM.  
Checksums act as **cryptographic verifiers**, confirming that CSV, Parquet, or JSONL files have not changed since validation,  
preserving **data lineage**, **ETL reproducibility**, and **transparency** across research environments.

All `.sha256` files are created automatically by the **tabular ETL pipeline** (`make tabular`)  
and revalidated in CI/CD during every build, merge, or release.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/tabular/
├── README.md
├── census_population_1860_2020.parquet.sha256
├── agricultural_production_1870_2020.parquet.sha256
└── economic_indicators_1900_2025.parquet.sha256

Each .sha256 corresponds 1:1 with its dataset in data/processed/tabular/.
CI workflows (stac-validate.yml) automatically recompute and verify each checksum.

⸻

🎯 Purpose

Objective	Description
Integrity Verification	Detects data corruption, tampering, or incomplete transfers.
Reproducibility	Ensures identical outputs from deterministic ETL processes.
Provenance Tracking	Ties each dataset’s lineage through STAC, metadata, and checksum.
Automation in CI	Continuous validation prevents version drift or data mismatch.


⸻

🧮 Example .sha256 File

# File: census_population_1860_2020.parquet.sha256
0d1e13dbde8fca82e7bc2184c23a7e231eb5b74b6e38e72df47f60bde8e54ccf  census_population_1860_2020.parquet

This checksum authenticates data/processed/tabular/census_population_1860_2020.parquet,
verifying byte-level integrity and alignment with recorded provenance.

⸻

⚙️ Checksum Generation

Checksums are generated as a post-processing step in the tabular ETL workflow.

Makefile target

make tabular-checksums

Equivalent Python utility

python src/utils/generate_checksums.py data/processed/tabular/ --algo sha256

Workflow Steps
	1.	Identify all tabular outputs (.csv, .parquet, .jsonl).
	2.	Compute SHA-256 hash via Python’s hashlib or GNU sha256sum --binary.
	3.	Write <filename>.sha256 into this directory.
	4.	Revalidate in CI/CD and raise alerts if mismatched.

💡 Store checksums in binary-safe mode for cross-platform consistency.

⸻

🔎 CI/CD Validation

GitHub Actions automatically re-verify tabular dataset integrity at every commit and release.

Command executed in CI:

sha256sum -c data/processed/checksums/tabular/*.sha256

A single mismatch fails the workflow, ensuring immediate detection and mitigation of checksum drift.
Logs are preserved to maintain a complete MCP audit trail for reproducibility.

⸻

🧩 Integration with Metadata & STAC

Linked Component	Purpose
data/processed/metadata/tabular/	STAC and metadata JSONs embed SHA-256 checksums for validation.
src/pipelines/tabular/tabular_pipeline.py	Handles hash generation and verification within ETL.
.github/workflows/stac-validate.yml	CI job confirming checksum integrity on each push or pull request.
data/stac/tabular/	STAC catalog stores hash provenance in assets and properties fields.


⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	Every tabular dataset includes a .sha256 and metadata documentation.
Reproducibility	Deterministic ETL validated through hash equivalence.
Open Standards	SHA-256 (FIPS 180-4) compliance ensures interoperability.
Provenance	Hashes link the complete data lineage (source → ETL → STAC).
Auditability	CI/CD validation provides a transparent, reviewable verification trail.


⸻

🧮 Maintenance & Best Practices
	•	🔄 After data updates: Recalculate checksums and increment metadata version numbers.
	•	🧾 File pairing: Checksum filenames must match their datasets exactly.
	•	📜 Bulk audits: Maintain a _manifest_all.sha256 for multi-file verification during releases.
	•	🧪 Pre-commit hooks: Optionally enforce checksum updates before staging modified tabular data.
	•	🧰 Metadata sync: Ensure STAC and metadata entries reflect the latest SHA-256 hash values.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Enhanced CI integration, MCP documentation, and validation workflow details.
1.0.0	2025-10-04	Initial release of tabular checksum documentation and hash manifests.


⸻

📖 References
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC 1.0 Specification: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards (KFM): ../../../../docs/standards/
	•	Data Provenance in Open Science: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


Kansas Frontier Matrix — “Verifying Every Figure: Integrity in the Numbers.”
📍 data/processed/checksums/tabular/

</div>
```