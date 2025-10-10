<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain Checksums  
`data/processed/checksums/terrain/`

**Mission:** Guarantee the **integrity, provenance, and reproducibility** of all processed **terrain datasets**  
by implementing SHA-256 checksum validation, ensuring trustworthy geospatial data lineage and reproducible ETL results  
across the Kansas Frontier Matrix (KFM) scientific ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **SHA-256 checksum files (`.sha256`)** that validate all processed **terrain datasets** in KFM.  
Checksums provide a cryptographic fingerprint that ensures the authenticity and integrity of datasets such as **DEMs**, **hillshades**, and **slope rasters**,  
forming a verifiable link between source inputs, ETL processes, and published STAC metadata.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/terrain/
├── README.md
├── ks_1m_dem_2018_2020.tif.sha256
├── ks_hillshade_2018_2020.tif.sha256
├── slope_aspect_2018_2020.tif.sha256
└── usgs_topo_larned_1894.tif.sha256

Each .sha256 file corresponds 1:1 to its processed dataset in data/processed/terrain/.
These are automatically regenerated and verified in CI/CD workflows for reproducibility and compliance.

⸻

🎯 Purpose

Objective	Description
Integrity Verification	Detects corruption or tampering in raster outputs (COG, GeoTIFF).
Reproducibility	Confirms that ETL processes yield identical artifacts given identical inputs.
Traceability	Links outputs to their STAC and metadata records for full provenance.
CI Enforcement	Enforced via automated GitHub workflows (stac-validate.yml, integrity-check.yml).


⸻

🧮 Example .sha256 File

# File: ks_1m_dem_2018_2020.tif.sha256
b8494ab6a3219c6a51e3de22804b329872c10f39ff8a4cf18ad4b3b61cb6ac8d  ks_1m_dem_2018_2020.tif

This checksum verifies the file data/processed/terrain/ks_1m_dem_2018_2020.tif
is bit-for-bit identical to its previously validated version.

⸻

⚙️ Checksum Generation

Checksums are generated automatically at the end of each terrain ETL run.

Makefile target

make terrain-checksums

Equivalent Python utility

python src/utils/generate_checksums.py data/processed/terrain/ --algo sha256

Workflow Steps
	1.	Locate all processed terrain outputs (.tif, .geojson, .json).
	2.	Compute the SHA-256 digest for each file in binary mode.
	3.	Store digests as <filename>.sha256 in this directory.
	4.	Validate against the stored reference during continuous integration.

💡 Prefer sha256sum --binary (GNU Coreutils) or the provided Python utility to ensure cross-platform consistency.

⸻

🔎 CI/CD Validation

Checksum verification runs automatically in STAC Validation and Build & Deploy workflows.

Example CI validation command:

sha256sum -c data/processed/checksums/terrain/*.sha256

If any mismatch occurs, the CI job fails, blocking merges or releases until the dataset is reprocessed and re-hashed.
This automated enforcement guarantees pipeline trust and data immutability.

⸻

🧩 Integration with Metadata & STAC

Linked Component	Purpose
data/processed/metadata/terrain/	STAC Items include checksum references for validation.
src/pipelines/terrain/terrain_pipeline.py	Handles checksum generation and verification post-processing.
.github/workflows/stac-validate.yml	Re-hashes and verifies checksum integrity in CI/CD.
data/stac/terrain/	STAC catalog embeds the checksum hash in assets.checksum:sha256.

Together, these create a seamless source → process → verification → publication chain.

⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	Each dataset has an accompanying .sha256 and metadata file.
Reproducibility	Deterministic pipeline outputs validated through hashes.
Open Standards	SHA-256 (FIPS 180-4) compliance and JSON Schema validation.
Provenance	SHA digests link datasets across ETL, STAC, and metadata layers.
Auditability	CI workflows log checksum validation results for long-term traceability.


⸻

🧮 Maintenance & Best Practices
	•	🔄 Checksum Updates: Always regenerate checksums after modifying or reprocessing terrain data.
	•	🧩 Naming Consistency: Ensure checksum filenames mirror their associated dataset filenames.
	•	🧪 Bulk Validation: Use _manifest_all.sha256 for multi-file batch verification during releases.
	•	🧰 Version Control: Record all checksum updates in PR descriptions and STAC changelogs.
	•	⚙️ Automation Tip: Implement pre-commit hooks to detect outdated or missing .sha256 files.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded documentation for CI workflows, MCP compliance, and reproducibility standards.
1.0.0	2025-10-04	Initial release of terrain checksum documentation and validation manifests.


⸻

📖 References
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC 1.0 Specification: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards: ../../../../docs/standards/
	•	Data Provenance in Open Science: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


Kansas Frontier Matrix — “Integrity in Every Pixel: Verifying the Ground Truth.”
📍 data/processed/checksums/terrain/ · Linked to the Terrain STAC Collection

</div>
```