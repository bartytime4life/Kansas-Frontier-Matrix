<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazard Derivative Checksums  
`data/derivatives/hazards/checksums/`

**Purpose:** Provide verifiable, machine-readable **SHA-256 integrity manifests**  
for all hazard-related derivative datasets (e.g. tornado tracks, flood rasters, drought indices, disaster maps)  
produced by the KFM ETL pipeline.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum manifests** for all hazard derivative outputs under  
`data/derivatives/hazards/`. These files ensure reproducible validation of data integrity for hazard models and layers such as:  
- Tornado, hail, and wind track vectors (NOAA SPC)  
- Flood and drought raster composites (FEMA, USGS, NOAA)  
- Historical disaster intensity layers or event summaries  

Checksums verify that derivative artifacts remain **bit-for-bit identical** across ETL runs and serve as validation gates in the KFM CI/STAC workflow.

---

## 🧭 Checksum generation flow

```mermaid
flowchart TD
  A["Hazard Sources\nNOAA SPC · FEMA · USGS · NCEI Storm Events"] --> B["ETL\nExtract · Normalize · Derive"]
  B --> C["Hazard Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Compute SHA-256\nCreate *.sha256 manifests"]
  D --> E["STAC Items\nLink assets + checksums"]
  E --> F["Knowledge Graph\nattach provenance nodes"]
  F --> G["API & Web UI\nserve verified hazard layers"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

checksums/
├── tornado_tracks_1950_2024.geojson.sha256
├── flood_zones_1990_2025_cog.tif.sha256
├── drought_index_annual_ks.parquet.sha256
├── severe_storm_reports_1955_2024.csv.sha256
└── README.md

Each .sha256 file contains a single line of hex digest followed by its associated filename.

⸻

🧾 File Format

Property	Description
Algorithm	SHA-256 (hex digest)
Format	<HEX_DIGEST>  <filename>
Line Endings	LF (\n)
Relative Path	Calculated from data/derivatives/hazards/ directory
Validation	Used by CI and stac-validate workflows


⸻

🛠️ Generate & Verify

Generate checksums

cd data/derivatives/hazards
for f in *.tif *.geojson *.parquet *.csv; do
  [ -f "$f" ] || continue
  shasum -a 256 "$f" > "checksums/${f}.sha256"
done

Verify checksums

cd data/derivatives/hazards
for c in checksums/*.sha256; do
  base=$(basename "$c" .sha256)
  sha256sum -c "checksums/${base}.sha256"
done

✅ Either sha256sum (Linux) or shasum -a 256 (macOS) is acceptable — both yield consistent digests.

⸻

🔗 STAC Integration (Provenance)

Each hazard layer is referenced in its STAC Item with a matching checksum:

STAC Key	Example
assets.<key>.href	"flood_zones_1990_2025_cog.tif"
assets.<key>.checksum:sha256	"b4a9e91…d37b"
properties['kfm:provenance']	"data/sources/noaa_spc.json"

Checksums are verified automatically during CI STAC validation to prevent broken lineage or tampered data.

⸻

🧩 Knowledge Graph & API Use
	•	During graph ingestion, checksum values attach to asset nodes and relations for evidential provenance.
	•	API endpoint GET /api/hazards/{id}/checksum returns the SHA-256 digest for client-side integrity checks.
	•	Frontend tools can display checksum validation status (e.g., ✅ Verified or ⚠️ Mismatch).

⸻

🧱 Naming Conventions

Pattern	Example	Notes
<dataset>_<years>.geojson.sha256	tornado_tracks_1950_2024.geojson.sha256	Tornado, hail, or storm vectors
<dataset>_<period>_cog.tif.sha256	flood_zones_1990_2025_cog.tif.sha256	Raster hazard maps (COG format)
<dataset>_<interval>.parquet.sha256	drought_index_annual_ks.parquet.sha256	Tabular indices
<dataset>_<range>.csv.sha256	severe_storm_reports_1955_2024.csv.sha256	Flat tabular derivatives


⸻

✅ Policy

1️⃣ All hazard derivatives must include a matching .sha256 file before publication.
2️⃣ Recompute checksums after any modification or regeneration of artifacts.
3️⃣ CI will fail if digests do not match STAC metadata.
4️⃣ Include updated .sha256 files in every pull request affecting hazard derivatives.

⸻

🔒 Reproducibility & MCP Alignment

These manifests align with MCP’s reproducibility and provenance principles:
	•	Transparent, auditable verification of data artifacts.
	•	Clear linkage between ETL outputs, STAC assets, and graph entities.
	•	Secure, checksum-based validation in CI workflows.

They guarantee that each hazard dataset (e.g., storm tracks, flood rasters) can be independently verified as authentic and unchanged.

⸻

🧱 Related Docs
	•	data/derivatives/hazards/metadata/README.md — metadata schema & relationships
	•	data/derivatives/climate/checksums/README.md — parallel checksum policy
	•	data/stac/README.md — STAC catalog design
	•	docs/architecture.md — ETL and validation workflow

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial hazard checksum specification and examples