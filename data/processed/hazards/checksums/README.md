<div align="center">

# ⚠️ Kansas Frontier Matrix — Processed Hazards Checksums  
`data/processed/hazards/checksums/`

**Mission:** Maintain **checksum files (`.sha256`)** verifying the integrity of all processed hazard datasets —  
drought indices, tornado tracks, flood polygons, wildfire detections, and FEMA disaster summaries —  
ensuring **scientific reproducibility, authenticity, and transparent provenance** for Kansas hazard data.

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

## 🌪️ Overview

This directory stores **SHA-256 checksum files** for all processed hazard datasets under `data/processed/hazards/`.  
These digests ensure hazard products (**tornado**, **flood**, **drought**, **wildfire**, and **FEMA** datasets) remain **unaltered** from their validated versions and provide a verifiable, cryptographic link in the MCP provenance chain.  
Each checksum corresponds directly to a dataset and its metadata entry in `data/processed/hazards/metadata/`.

---

## 🎯 Purpose

- **Integrity Validation:** Detect any post-build or post-transfer change in GeoJSON/COG artifacts.  
- **Transparency:** Publish verifiable hashes cross-referenced in STAC and MCP records.  
- **Reproducibility:** Enable independent re-checks by downstream researchers and apps.  
- **Automation:** Power CI/CD gates that block merges/releases on checksum mismatch.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hazards/
        └── checksums/
            ├── tornado_tracks_1950_2024.geojson.sha256
            ├── fema_disasters_1953_2024.geojson.sha256
            ├── drought_spi12_1950_2024.tif.sha256
            ├── wildfire_points_2000_2023.geojson.sha256
            ├── flood_events_1900_2020.geojson.sha256
            └── README.md

Each .sha256 is a single-line digest referencing its dataset (GNU Coreutils format):

1b5a7f129bc0cde23c18da63b32b17e6b12a926a9b92b57975db5ef938c3f142  tornado_tracks_1950_2024.geojson


⸻

🧩 Checksum Standards

Property	Value
Algorithm	SHA-256 (Secure Hash Algorithm, 256-bit)
Format	GNU sha256sum: <hash>␠␠<filename>
Mode	Binary (--binary) for OS-independent hashes
Purpose	Reproducible fingerprint proving immutability

Hashes are verifiable on Linux/macOS/Windows (WSL/PowerShell equivalents).

⸻

🔍 Verification Workflow

Manual Verification

# Verify one dataset
sha256sum -c data/processed/hazards/checksums/tornado_tracks_1950_2024.geojson.sha256

# Verify all hazards checksums
find data/processed/hazards/checksums -name "*.sha256" -exec sha256sum -c {} \;

Expected output:

tornado_tracks_1950_2024.geojson: OK
flood_events_1900_2020.geojson: OK
drought_spi12_1950_2024.tif: OK

On mismatch:

fema_disasters_1953_2024.geojson: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match

Automated CI Verification

GitHub Actions (.github/workflows/stac-validate.yml) automatically re-hash and validate checksums on every commit/PR.

⸻

🌐 Integration with MCP & STAC

Checksums are the cryptographic glue linking file integrity to semantic metadata:
	1.	MCP Provenance — Each metadata JSON includes the hash:

"mcp_provenance": "sha256:1b5a7f129bc0cde23c18da63b32b17e6b12a926a9b92b57975db5ef938c3f142"

	2.	STAC Linkage — STAC Items in data/stac/items/hazards_* reference the same digest
(e.g., in properties or assets.checksum:sha256) for cross-layer verification.

Together, these provide end-to-end verification across the KFM data architecture.

⸻

⚙️ Adding or Updating Checksums
	1.	Generate checksum for a new/updated dataset:

sha256sum <dataset> > data/processed/hazards/checksums/<dataset>.sha256


	2.	Validate locally:

sha256sum -c data/processed/hazards/checksums/<dataset>.sha256


	3.	Sync metadata: update mcp_provenance in the dataset’s metadata and STAC Item.
	4.	Commit data + .sha256 together.
	5.	Validate:

make validate-hazards


	6.	Open a PR — CI will re-verify all digests.

⸻

🛠️ Maintenance & Best Practices
	•	🔄 After reprocessing: Regenerate checksums and update metadata/STAC digests.
	•	🧾 Filename parity: Checksum filenames must match dataset names exactly.
	•	📜 Bulk audits: Maintain a _manifest_all.sha256 for release-wide verification.
	•	🧪 Pre-commit hook (optional): Block commits with stale/missing .sha256 files.
	•	🧠 Doc sync: Record digest changes in PR descriptions and STAC changelogs.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README with MCP front matter, CI workflow details, and maintenance guidance.
1.0.0	2025-10-04	Initial hazards checksum documentation and SHA-256 manifests.


⸻

📖 References
	•	NOAA Storm Events: https://www.ncei.noaa.gov/stormevents/
	•	FEMA Declarations (OpenFEMA): https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2
	•	NASA FIRMS: https://firms.modaps.eosdis.nasa.gov/
	•	U.S. Drought Monitor: https://droughtmonitor.unl.edu/
	•	USGS Flood Science: https://www.usgs.gov/mission-areas/water-resources/science/floods
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC 1.0: https://stacspec.org
	•	MCP Standards: ../../../../docs/standards/

⸻


<div align="center">


“Every storm, every fire, every flood — these checksums ensure the history of Kansas hazards remains untampered and true.”
📍 data/processed/hazards/checksums/

</div>
```