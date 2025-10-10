<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards Checksums  
`data/processed/checksums/hazards/`

**Mission:** Maintain and verify the **integrity, provenance, and reproducibility** of all processed **natural hazard datasets** —  
including tornadoes, floods, wildfires, and drought layers — ensuring confidence in the Kansas Frontier Matrix (KFM)  
geospatial and temporal record of extreme events.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **SHA-256 checksum files (`.sha256`)** that serve as verifiable digital signatures for all processed **hazard datasets**  
within the Kansas Frontier Matrix (KFM).  

Each checksum acts as a cryptographic fingerprint, confirming:
- 🧩 **Data integrity** — ensures data is untampered and bit-for-bit identical to its validated state.  
- 🔁 **Reproducibility** — verifies ETL re-runs generate identical outputs from identical inputs.  
- 🔗 **Provenance** — embeds linkages to metadata, STAC Items, and source records.  
- 🔒 **Auditability** — provides transparent, CI-enforced verification for open science compliance.  

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/hazards/
├── README.md
├── tornado_tracks_1950_2024.geojson.sha256
├── flood_events_1900_2025.geojson.sha256
├── wildfire_perimeters_2000_2024.geojson.sha256
└── drought_index_2000_2025.tif.sha256

Each .sha256 corresponds 1:1 to its dataset in data/processed/hazards/.
CI workflows (stac-validate.yml) automatically verify these checksums at every commit and deployment.

⸻

🎯 Purpose

Objective	Description
Integrity Verification	Detects data corruption or unauthorized changes post-processing.
Reproducibility	Confirms ETL pipeline outputs remain deterministic across executions.
Provenance	Establishes traceable linkage between data, metadata, and STAC assets.
CI Enforcement	Automates verification through GitHub Actions; mismatches fail validation.


⸻

🧮 Example .sha256 Manifest

# File: tornado_tracks_1950_2024.geojson.sha256
8fb29cda3d0e44182f26c7bceff74b2c81b83e742d47d836b33151f871bb69d1  tornado_tracks_1950_2024.geojson

This digest confirms the authenticity and byte-level fidelity of
data/processed/hazards/tornado_tracks_1950_2024.geojson.

⸻

⚙️ Checksum Generation Workflow

Checksums are created automatically by the hazards ETL pipeline, triggered during dataset post-processing.

Makefile target:

make hazards-checksums

Equivalent Python utility:

python src/utils/generate_checksums.py data/processed/hazards/ --algo sha256

Workflow Steps:
	1.	Scan all processed hazard files (.geojson, .tif, .csv, etc.).
	2.	Compute SHA-256 hash via Python’s hashlib or GNU sha256sum.
	3.	Output corresponding .sha256 manifests into this directory.
	4.	Validate checksums within CI/CD pipelines.

💡 For deterministic hashes across platforms, use sha256sum --binary.

⸻

🧰 CI/CD Validation

Checksum verification runs automatically in GitHub Actions workflows to protect dataset integrity.

Example validation command:

sha256sum -c data/processed/checksums/hazards/*.sha256

Any mismatch halts the pipeline, preventing deployment until the affected dataset is reprocessed and re-hashed.
Logs from the workflow are archived for audit trail compliance under MCP governance.

⸻

🧩 Integration with Metadata & STAC

Linked Component	Purpose
data/processed/metadata/hazards/	STAC Items include corresponding checksums for data verification.
src/pipelines/hazards/hazards_pipeline.py	Automates checksum creation and verification within ETL.
.github/workflows/stac-validate.yml	CI job validates checksums and STAC metadata across commits.
data/stac/hazards/	STAC catalog integrates SHA-256 values for provenance in assets.checksum:sha256.

Together, these ensure end-to-end synchronization between the checksum system, metadata registry, and catalog layer.

⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	Every hazard dataset includes .sha256 and STAC records for transparency.
Reproducibility	Deterministic ETL ensures identical outputs verified via SHA-256.
Open Standards	Uses SHA-256 (FIPS 180-4) and JSON Schema-compliant STAC metadata.
Provenance	Ties together source → processed → STAC metadata with hashes.
Auditability	CI/CD pipelines validate hashes; audit logs recorded automatically.


⸻

🧮 Maintenance & Best Practices
	•	🔄 Update Policy: Recompute checksums after intentional dataset updates or reprocessing.
	•	🧩 Manifest Control: Keep _manifest_all.sha256 for bulk audits when publishing releases.
	•	⚙️ Consistency: Ensure dataset filenames and .sha256 names match exactly.
	•	📜 Transparency: Document all checksum updates in pull request descriptions and STAC changelogs.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README with CI workflow details and MCP compliance expansion.
1.0.0	2025-10-04	Initial hazards checksum release for tornado, flood, wildfire, drought datasets.


⸻

📖 References
	•	GNU Coreutils SHA Utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC Specification 1.0: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards: docs/standards/
	•	Provenance in Open Data: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


Kansas Frontier Matrix — “Every Storm Verified: Data Integrity for a Changing Kansas.”
📍 data/processed/checksums/hazards/ · Linked to the Hazards STAC Collection

</div>
```