<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Derivative Checksums  
`data/derivatives/hydrology/checksums/`

**Purpose:** Maintain verifiable **SHA-256 integrity manifests** for all hydrology derivative datasets  
(e.g., streamflow rasters, floodplain maps, aquifer grids, watershed boundaries) produced by the ETL pipeline.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **SHA-256 checksum files (`.sha256`)** for all processed hydrology derivative outputs under  
`data/derivatives/hydrology/`.  

Checksums ensure:
- **File integrity** of derivative products  
- **Reproducibility** across ETL and CI runs  
- **Trustable linkage** with the STAC catalog and knowledge graph  

Artifacts covered include:
- Streamflow and discharge composites  
- Floodplain raster grids (COG)  
- Watershed boundary polygons  
- Groundwater and aquifer elevation models  

---

## 🧭 Checksum Generation Flow

```mermaid
flowchart TD
  A["Hydrology Sources\nUSGS · FEMA · NOAA · KDHE"] --> B["ETL\nExtract · Normalize · Derive"]
  B --> C["Hydrology Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Compute SHA-256\nGenerate *.sha256 manifests"]
  D --> E["STAC Items\nAttach checksum references"]
  E --> F["Knowledge Graph\nIntegrate checksum properties"]
  F --> G["API & Web UI\nserve verified layers and metadata"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

checksums/
├── streamflow_monthly_1990_2025_cog.tif.sha256
├── floodplain_extent_2020_cog.tif.sha256
├── aquifer_depth_ks_cog.tif.sha256
├── watershed_boundaries_huc8.geojson.sha256
└── README.md

Each .sha256 file contains a one-line hexadecimal digest and the associated filename,
matching artifacts stored in the parent hydrology directory.

⸻

🧾 File Format

Property	Description
Algorithm	SHA-256 (hex digest)
Format	<HEX_DIGEST>  <filename>
Line Endings	LF (\n)
Scope	Computed against each hydrology artifact (COG, GeoJSON, Parquet, CSV)
Purpose	Used by CI and STAC validation to ensure dataset immutability


⸻

🛠️ Generate & Verify

Generate Checksums

cd data/derivatives/hydrology
for f in *.tif *.geojson *.parquet *.csv; do
  [ -f "$f" ] || continue
  shasum -a 256 "$f" > "checksums/${f}.sha256"
done

Verify Checksums

cd data/derivatives/hydrology
for c in checksums/*.sha256; do
  base=$(basename "$c" .sha256)
  sha256sum -c "checksums/${base}.sha256"
done

✅ Supports both sha256sum (Linux) and shasum -a 256 (macOS).

⸻

🔗 STAC Integration (Provenance)

STAC Field	Example
assets.<key>.href	"floodplain_extent_2020_cog.tif"
assets.<key>.checksum:sha256	"c7b3a3ef3d9eac9b8a6e42b2d98…" 
properties['kfm:provenance']	"data/sources/fema_flood_zones.json"

Checksums are referenced directly within STAC items, enabling CI and user-side validation of file authenticity.

⸻

🧩 Knowledge Graph & API Use
	•	The Neo4j graph stores checksum_sha256 attributes on asset nodes, preserving auditability.
	•	API endpoint GET /api/hydrology/{id}/checksum exposes digests for verification in external apps.
	•	Frontend displays checksum status in asset details (e.g., ✅ Verified | ⚠️ Pending).

⸻

🧱 Naming Conventions

Pattern	Example	Notes
<dataset>_<years>_cog.tif.sha256	streamflow_monthly_1990_2025_cog.tif.sha256	COG rasters
<dataset>_<year>_cog.tif.sha256	floodplain_extent_2020_cog.tif.sha256	Single-year rasters
<dataset>_<region>.geojson.sha256	watershed_boundaries_huc8.geojson.sha256	Vector boundaries
<dataset>_<region>.parquet.sha256	aquifer_depth_ks.parquet.sha256	Tabular or gridded data


⸻

✅ Policy

1️⃣ All hydrology derivatives must include matching .sha256 manifests.
2️⃣ Checksums must be regenerated after file edits or reprocessing.
3️⃣ CI (stac-validate.yml) will fail if hashes mismatch STAC checksum:sha256 records.
4️⃣ All pull requests modifying derivative data must include updated checksum files.

⸻

🔒 Reproducibility & MCP Alignment

These manifests support KFM’s reproducibility, provenance, and transparency goals:
	•	Checksum creation is part of every ETL → STAC workflow.
	•	Validation in CI ensures files are immutable and trustworthy.
	•	Checksums provide the evidential chain required by the Master Coder Protocol.

⸻

🧱 Related Documentation
	•	data/derivatives/hydrology/metadata/README.md — metadata definitions and relationships
	•	data/stac/README.md — STAC catalog schema and integration
	•	docs/architecture.md — ETL and integrity workflow overview
	•	data/sources/README.md — hydrology source manifest standards

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial hydrology checksum manifest documentation and examples.