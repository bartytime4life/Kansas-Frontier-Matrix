<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate Checksums  
`data/processed/checksums/climate/`

**Mission:** Guarantee the **integrity, reproducibility, and provenance** of all processed **climate datasets** —  
ensuring temperature, precipitation, and drought products remain verifiable across KFM’s full temporal and spatial range.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder holds **SHA-256 checksum files (`.sha256`)** for all processed **climate datasets** under `data/processed/climate/`.  
Checksums create a **verifiable link** between raw inputs → processed outputs → published STAC metadata, ensuring **reproducibility** and **auditability**.

All hashes are produced automatically by the climate ETL (`make climate`) and validated in CI/CD to detect drift, corruption, or accidental edits.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/climate/
├── README.md
├── daymet_1980_2024.tif.sha256
├── noaa_normals_1991_2020.geojson.sha256
└── drought_monitor_2000_2025.tif.sha256

Each .sha256 contains the verified SHA-256 digest for its sibling product in data/processed/climate/.
CI workflows (stac-validate.yml) recompute and compare these digests on every build.

⸻

🎯 Purpose

Objective	Description
Integrity Assurance	Detects changes or corruption in raster/vector climate datasets.
Reproducibility	Confirms deterministic pipeline outputs when rerun with identical inputs.
Provenance Chain	Links artifacts to metadata and STAC Items by hash.
CI Enforcement	Enforced in GitHub Actions (build blocks on mismatch).


⸻

🧮 Example .sha256 File

# File: daymet_1980_2024.tif.sha256
a7f9132dfe5b16c9783f3f0ec4a2f4da8a9bb5e7b739c3477325dcb0df836f41  daymet_1980_2024.tif

This fingerprint validates data/processed/climate/daymet_1980_2024.tif.

⸻

⚙️ Checksum Generation

Checksums are created during/after the ETL for climate data.

Makefile target:

make climate-checksums

Equivalent Python utility:

python src/utils/generate_checksums.py data/processed/climate/ --algo sha256

Steps performed:
	1.	Scan outputs (.tif, .geojson, .csv, .jsonl, …).
	2.	Compute SHA-256 (hashlib) in binary mode.
	3.	Write <filename>.sha256 into this folder.
	4.	Validate digests in CI/CD.

💡 For cross-platform consistency, prefer sha256sum --binary (GNU coreutils) or the Python tool above.

⸻

🔎 Verification Workflow

Manual:

# Verify all in folder
sha256sum -c data/processed/checksums/climate/*.sha256

# Verify one file
sha256sum -c data/processed/checksums/climate/daymet_1980_2024.tif.sha256

CI/CD (automatic):
.github/workflows/stac-validate.yml re-hashes targeted artifacts and fails on mismatch, halting deploy until corrected.

⸻

🧩 Integration with Metadata & STAC

Linked Component	Purpose
data/processed/metadata/climate/	Metadata JSONs reference the file’s checksum (mcp_provenance: "sha256:<digest>").
src/pipelines/climate/climate_pipeline.py	Orchestrates digest generation and validation in the ETL.
.github/workflows/stac-validate.yml	Automates STAC + integrity checks in CI/CD.
data/stac/climate/	STAC Items include the same digest in properties for cross-verification.

This dual registration (MCP + STAC) guarantees a single source of truth for integrity across science and catalog layers.

⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	Every dataset is paired with a .sha256 and metadata record.
Reproducibility	Deterministic hashes validate identical outputs on reruns.
Open Standards	SHA-256 (FIPS 180-4), STAC 1.0, JSON Schema.
Provenance	Digest embedded in MCP metadata and STAC Items.
Auditability	CI/CD verification + artifact logs provide an auditable trail.


⸻

🧮 Tips & Best Practices
	•	Always regenerate checksums after intentional data changes, and bump dataset version in metadata.
	•	Store only the <hex>  <filename> line (no extra whitespace) in each .sha256.
	•	Avoid renaming data without updating the paired checksum filename and references.
	•	Keep a rolling _manifest_all.sha256 when bulk-auditing releases.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README, MCP/STAC linkage, CI notes, best-practice guidance.
1.0.0	2025-10-04	Initial release of climate checksum docs and digests.


⸻

📖 References
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC Specification 1.0: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards (KFM): ../../../../docs/standards/
	•	Data Provenance in Open Science: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


Kansas Frontier Matrix — “Climate Integrity: Verifying Every Degree and Drop.”
📍 data/processed/checksums/climate/

</div>
```
