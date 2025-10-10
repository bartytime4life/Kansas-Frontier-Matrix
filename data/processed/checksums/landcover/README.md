<div align="center">

# 🌾 Kansas Frontier Matrix — Land Cover Checksums  
`data/processed/checksums/landcover/`

**Mission:** Verify, preserve, and document the **integrity and reproducibility** of all processed **land cover datasets**  
using SHA-256 checksums — ensuring **consistency, transparency, and auditability** across the KFM spatiotemporal system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **SHA-256 checksum files (`.sha256`)** for all processed **land cover datasets** in KFM.  
Checksums provide a **cryptographic fingerprint** for each artifact, enabling:

- ✅ **Integrity verification** — detect accidental corruption or tampering  
- 🔁 **Reproducibility** — confirm identical ETL outputs across platforms/environments  
- 🧭 **Provenance** — link output artifacts with STAC Items, metadata, and source descriptors  
- 🔒 **Auditability** — CI pipelines re-validate hashes on every commit and release

All hashes are generated automatically by the **land cover ETL pipeline** (`make landcover`) and validated in CI/CD.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/landcover/
├── README.md
├── nlcd_1992_2021.tif.sha256
├── kansas_vegetation_1850s.tif.sha256
├── landcover_change_1992_2021.geojson.sha256
└── crop_distribution_2020.geojson.sha256

Each .sha256 maps 1:1 to its dataset in data/processed/landcover/ and is re-verified via sha256sum -c in CI.

⸻

🎯 Purpose

Objective	Description
Integrity	Detects file corruption or unauthorized modification between versions/transfers.
Reproducibility	Guarantees deterministic ETL outputs from the same inputs and parameters.
Provenance	Connects artifacts to metadata, STAC entries, and source references by digest.
CI Enforcement	GitHub Actions fail on mismatches to prevent invalid merges/deploys.


⸻

🧮 Example .sha256 File

# File: nlcd_1992_2021.tif.sha256
1e8a2a99ef45f582f821a4b8ac3adcc48f0c52b7c1d7ce1f92f4cb045c54cc54  nlcd_1992_2021.tif

This digest validates data/processed/landcover/nlcd_1992_2021.tif against the last verified state.

⸻

⚙️ Checksum Generation

Checksums are generated as the final step in the ETL pipeline.

Makefile target

make landcover-checksums

Equivalent Python utility

python src/utils/generate_checksums.py data/processed/landcover/ --algo sha256

Workflow Steps
	1.	Scan data/processed/landcover/ for rasters/vectors (e.g., .tif, .geojson, .csv).
	2.	Compute SHA-256 in binary mode for cross-platform consistency.
	3.	Save results as <filename>.sha256 in this directory.
	4.	Re-validate in CI/CD (stac-validate.yml and any integrity checks).

💡 Prefer sha256sum --binary (GNU Coreutils) or the Python tool to avoid line-ending discrepancies.

⸻

🔎 CI/CD Validation

During GitHub Actions runs, checksums are re-verified:

sha256sum -c data/processed/checksums/landcover/*.sha256

Any mismatch fails the workflow, blocking merges/deploys until the dataset is reprocessed and re-hashed.
Validation logs are retained for MCP audit trail compliance.

⸻

🧩 Integration with Metadata & STAC

Linked Component	Purpose
data/processed/metadata/landcover/	Metadata/STAC Items embed the artifact’s SHA-256 for verification.
src/pipelines/landcover/landcover_pipeline.py	Automates digest generation & verification during ETL.
.github/workflows/stac-validate.yml	CI job re-checking hashes and STAC compliance on each PR/push.
data/stac/landcover/	STAC catalog references SHA-256 in assets or properties for provenance.


⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	Every land cover product has a .sha256 and metadata record.
Reproducibility	Deterministic ETL outputs verified via SHA-256 digests.
Open Standards	Uses SHA-256 (FIPS 180-4), STAC 1.0, JSON Schema-aligned metadata.
Provenance	Hash links source → processed → catalog (STAC) for full lineage.
Auditability	CI/CD verification logs provide transparent, reviewable records.


⸻

🧮 Maintenance & Best Practices
	•	🔄 After updates: Recompute checksums after intentional data changes and bump dataset version in metadata.
	•	🧩 Naming: Ensure checksum filenames match the data filenames exactly.
	•	📝 Manifests: Maintain _manifest_all.sha256 for batch audits during releases.
	•	🧪 Pre-commit (optional): Add a local hook to block commits when checksum pairs are stale or missing.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README with CI, maintenance practices, and MCP/STAC linkage clarifications.
1.0.0	2025-10-04	Initial land cover checksum documentation and SHA-256 files.


⸻

📖 References
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC 1.0 Specification: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards (KFM): ../../../../docs/standards/
	•	Open Data Provenance: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


Kansas Frontier Matrix — “Every Pixel Proven: Verifying the Surface of Change.”
📍 data/processed/checksums/landcover/

</div>
```