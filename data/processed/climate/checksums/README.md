<div align="center">

# 🌦️ Kansas Frontier Matrix — Processed Climate Checksums  
`data/processed/climate/checksums/`

**Mission:** Maintain **checksum files (`.sha256`)** verifying the integrity of all processed climate datasets —  
gridded temperature, precipitation, and drought indices — ensuring **long-term reproducibility, authenticity,**  
and **provenance** for Kansas Frontier Matrix climate archives.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Directory Layout](#directory-layout)
- [Checksum Standards](#checksum-standards)
- [Verification Workflow](#verification-workflow)
- [Integration with MCP & STAC](#integration-with-mcp--stac)
- [Adding or Updating Checksums](#adding-or-updating-checksums)
- [Maintenance & Best Practices](#maintenance--best-practices)
- [Version History](#version-history)
- [References](#references)

---

## 🧠 Overview

This directory contains **SHA-256 checksum files** used to verify the **integrity and authenticity**  
of all processed climate products stored in `data/processed/climate/`.

Checksums ensure each temperature, precipitation, or drought raster/table remains **unchanged** since creation,  
supporting **reproducibility**, **scientific transparency**, and **long-term validation** under the **Master Coder Protocol (MCP)**.

Each checksum file corresponds directly to a processed climate asset and its metadata entry in  
`data/processed/climate/metadata/`.

---

## 🎯 Purpose

- **Integrity Verification:** Detect accidental/unauthorized data modification.  
- **Reproducibility Assurance:** Confirm analyses reproduce exact results from published artifacts.  
- **Provenance Linking:** Tie file hashes to `mcp_provenance` fields in metadata and STAC Items.  
- **Automation:** Allow CI/CD to perform automated hash checks during build and release cycles.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── climate/
        └── checksums/
            ├── temp_mean_annual_1895_2024.tif.sha256
            ├── precip_total_annual_1895_2024.tif.sha256
            ├── drought_spi12_1895_2024.tif.sha256
            ├── climate_normals_1991_2020.parquet.sha256
            └── README.md

Each .sha256 contains a single SHA-256 line referencing its dataset (GNU Coreutils format):

9c1a24e3374e6dbfcd3ef11a8a9a5568c4f5f7f2b6c77714569e34138ab7f91b  temp_mean_annual_1895_2024.tif


⸻

🧩 Checksum Standards

Standard	Algorithm	Output	Description
SHA-256	256-bit hash	64 char hexadecimal string	Cryptographic fingerprint for file identity
Format	GNU sha256sum	<hash>␠␠<filename>	Human- & machine-readable
Mode	--binary	Platform-consistent hashing	Avoids EOL/newline discrepancies

Hashes can be generated/verified on Linux, macOS, or Windows (WSL/PowerShell equivalents).

⸻

🔍 Verification Workflow

Validate locally or in CI:

# Verify a single file
sha256sum -c data/processed/climate/checksums/temp_mean_annual_1895_2024.tif.sha256

# Verify all checksums
find data/processed/climate/checksums -name "*.sha256" -exec sha256sum -c {} \;

Expected:

temp_mean_annual_1895_2024.tif: OK
precip_total_annual_1895_2024.tif: OK

On mismatch:

drought_spi12_1895_2024.tif: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match


⸻

🌐 Integration with MCP & STAC

1) MCP Provenance
Each metadata JSON includes an mcp_provenance field:

"mcp_provenance": "sha256:9c1a24e3374e6dbfcd3ef11a8a9a5568c4f5f7f2b6c77714569e34138ab7f91b"

2) STAC Catalog
STAC Items in data/stac/items/climate_* embed the same SHA-256 hash (e.g., in properties or assets.checksum:sha256)
for cross-layer verification and catalog integrity tracking.

⸻

⚙️ Adding or Updating Checksums
	1.	Generate checksum for a new/updated dataset:

sha256sum <dataset> > data/processed/climate/checksums/<dataset>.sha256


	2.	Validate locally:

sha256sum -c data/processed/climate/checksums/<dataset>.sha256


	3.	Update metadata: replace the mcp_provenance digest in the dataset’s STAC/metadata JSON.
	4.	Commit together: include both the dataset and checksum; push your branch.
	5.	Open a PR: CI will rerun verification (failing on mismatch).

⸻

🛠️ Verification in CI/CD

GitHub Actions re-hash datasets and validate checksums in:
	•	.github/workflows/stac-validate.yml
	•	(optional) .github/workflows/integrity-check.yml

CI command (example):

sha256sum -c data/processed/climate/checksums/*.sha256

If any digest fails, the workflow blocks merge/deploy until the dataset is corrected and re-hashed.

⸻

🧰 Maintenance & Best Practices
	•	🔄 After updates: Recompute checksums whenever a climate dataset changes.
	•	🧾 Filename parity: Checksum filenames must exactly match their datasets.
	•	📜 Bulk audits: Maintain a _manifest_all.sha256 to verify releases at scale.
	•	🧪 Pre-commit hook (optional): Reject commits with stale/missing checksums.
	•	🧠 Metadata sync: Ensure mcp_provenance in STAC/metadata reflects the latest digest.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README with MCP front matter, CI integration, and best-practice guidance.
1.0.0	2025-10-04	Initial processed climate checksum documentation and hash files.


⸻

📖 References
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC 1.0 Specification: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards: ../../../../docs/standards/
	•	NOAA NCEI: https://www.ncei.noaa.gov/
	•	PRISM Climate Group: https://prism.oregonstate.edu/

⸻


<div align="center">


“Every climate grid, every anomaly — these checksums preserve the integrity of Kansas’s atmospheric memory.”

</div>
```