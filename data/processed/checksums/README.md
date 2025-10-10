<div align="center">

# 🔐 Kansas Frontier Matrix — Processed Data Checksums  
`data/processed/checksums/`

**Mission:** Safeguard the integrity and traceability of all processed datasets through reproducible  
**SHA-256 checksums**, ensuring scientific verifiability, provenance, and reproducibility across the Kansas Frontier Matrix ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Directory Layout](#directory-layout)
- [Checksum Generation](#checksum-generation)
- [Verification Workflow](#verification-workflow)
- [Integration with MCP & STAC](#integration-with-mcp--stac)
- [Adding or Updating Checksums](#adding-or-updating-checksums)
- [References](#references)

---

## 🧠 Overview

This directory contains **SHA-256 checksum manifests** that validate every dataset stored under  
`data/processed/`.  

Checksums ensure that no file has been modified, corrupted, or replaced since its last verified state,  
enforcing **reproducible data workflows** and **verifiable lineage** across the entire MCP-compliant data pipeline.

Each `.sha256` file provides a cryptographic fingerprint uniquely identifying its corresponding dataset —  
whether raster, vector, tabular, or text.

---

## 🎯 Purpose

| Objective | Description |
|:--|:--|
| 🧩 **Integrity Assurance** | Guarantees that processed files remain unchanged post-validation. |
| 🔁 **Reproducibility** | Enables independent verification of dataset consistency. |
| ⚙️ **Automation** | Powers CI/CD checksum validation during builds and deployments. |
| 🔗 **Linkage** | Connects `mcp_provenance` fields in metadata and STAC Items directly to verified hashes. |

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── checksums/
        ├── terrain/
        │   ├── dem_1m_ks_filled.tif.sha256
        │   ├── dem_30m_ned_ks.tif.sha256
        ├── hydrology/
        │   ├── flow_dir_d8_1m_ks.tif.sha256
        │   ├── watermask_ks.tif.sha256
        ├── landcover/
        │   ├── nlcd_2021_ks.tif.sha256
        │   ├── vegetation_mask_ks.tif.sha256
        ├── climate/
        │   ├── precip_total_annual_1895_2024.tif.sha256
        │   ├── drought_spi12_1895_2024.tif.sha256
        ├── hazards/
        │   ├── tornado_tracks_1950_2024.geojson.sha256
        │   ├── fema_disasters_1953_2024.geojson.sha256
        ├── tabular/
        │   ├── tornado_counts_1950_2024.csv.sha256
        │   ├── county_population_1850_2020.csv.sha256
        ├── text/
        │   ├── newspapers_1854_1925_cleaned.jsonl.sha256
        │   ├── nlp_entities_extracted.json.sha256
        └── README.md

Each .sha256 contains a single 64-character hexadecimal digest verifying a data asset’s byte-level integrity.

⸻

🔐 Checksum Generation

Checksums are generated automatically during ETL or manual validation using GNU Coreutils or equivalent.

# ✅ Generate checksum for one file
sha256sum dem_1m_ks_filled.tif > checksums/terrain/dem_1m_ks_filled.tif.sha256

# 🔁 Generate all checksums recursively
find data/processed -type f $begin:math:text$ -name "*.tif" -o -name "*.csv" -o -name "*.jsonl" $end:math:text$ \
  -exec sha256sum {} \; > data/processed/checksums/_manifest_all.sha256

💡 Use --binary mode (sha256sum --binary) for platform-independent consistency.

⸻

🔎 Verification Workflow

Validation ensures dataset fidelity before release or publication.

# Verify all checksums in a subdirectory
sha256sum -c checksums/terrain/*.sha256

# Verify a single file
sha256sum -c data/processed/checksums/climate/precip_total_annual_1895_2024.tif.sha256

🔄 Automated CI/CD Integration

Checksum validation runs automatically via
.github/workflows/stac-validate.yml, triggered on every push or pull request.
If a checksum mismatch occurs, the pipeline fails, preventing invalid data merges.

⸻

🧩 Integration with MCP & STAC

Checksums are woven into KFM’s dual provenance architecture:

Layer	Integration
MCP Provenance	Each metadata JSON includes an mcp_provenance field, e.g. "sha256:abc123…".
STAC Catalog	Each STAC Item embeds the same digest in its properties for cross-verification.

This ensures consistent, end-to-end validation across both the scientific provenance chain
and the geospatial catalog layer.

⸻

🧮 Adding or Updating Checksums
	1.	Generate checksum:

sha256sum <file> > data/processed/checksums/<path>/<file>.sha256


	2.	Validate:

sha256sum -c data/processed/checksums/<path>/<file>.sha256


	3.	Commit both the data and checksum pair.
	4.	Push and let CI validate automatically.
	5.	If the dataset changes intentionally, update its checksum and increment
the corresponding version field in its metadata JSON (mcp_provenance).

⸻

🧠 Best Practices

Category	Guideline
✅ Completeness	Every processed dataset must include a corresponding .sha256.
🔄 Update Policy	Always update checksums after dataset modification.
🧾 Schema Compliance	Validate JSON metadata against the STAC/MCP schemas.
🧪 CI Enforcement	Use automated checks to prevent mismatched hashes.
🧰 Transparency	Log checksum manifests (_manifest_all.sha256) for batch audits.


⸻

📖 References
	•	🔗 GNU Coreutils SHA Utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	🌐 STAC Specification 1.0: https://stacspec.org
	•	🧩 JSON Schema: https://json-schema.org
	•	📘 Master Coder Protocol: docs/standards/
	•	🧭 Data Provenance in Open Science: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


“Every verified checksum is a promise — Kansas’s digital frontier remains consistent, transparent, and trusted.”

</div>