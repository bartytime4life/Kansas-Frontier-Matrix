<div align="center">

# 🌾 Kansas Frontier Matrix — Landcover Derivative Checksums  
`data/derivatives/landcover/checksums/`

**Purpose:** Maintain verified **SHA-256 integrity manifests** for all **landcover derivative datasets**  
(e.g., NLCD layers, vegetation rasters, canopy composites, and historical land-use grids) generated through the ETL pipeline.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **SHA-256 checksum files** (`.sha256`) for all processed landcover derivative outputs stored in  
`data/derivatives/landcover/`.  

Checksums are used across the KFM **ETL → STAC → Graph → API** workflow to:
- Verify file integrity for landcover datasets (COG, GeoJSON, Parquet, CSV).  
- Guarantee reproducibility and cross-validation between builds.  
- Maintain data lineage consistency for historical vegetation and land-use layers.

Typical datasets include:  
🌱 Historical vegetation cover maps, 🛰️ NLCD raster layers, 🌾 cropland/grassland extent composites, and 🪵 canopy-height grids.

---

## 🧭 Checksum Generation Flow

```mermaid
flowchart TD
  A["Landcover Sources\nUSGS NLCD · KARS · USDA NRCS"] --> B["ETL\nExtract · Normalize · Derive"]
  B --> C["Landcover Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Compute SHA-256\nGenerate *.sha256 manifests"]
  D --> E["STAC Items\nAttach checksum and provenance"]
  E --> F["Knowledge Graph\nChecksum nodes and asset relations"]
  F --> G["API & Web UI\nserve verified landcover layers"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

checksums/
├── nlcd_1992_2021_cog.tif.sha256
├── landuse_1900_2000_composite_cog.tif.sha256
├── vegetation_zones_1850_ks.geojson.sha256
├── prairie_extent_2020_cog.tif.sha256
└── README.md

Each .sha256 file corresponds to a processed artifact in the parent directory
and records a single-line SHA-256 digest for provenance validation.

⸻

🧾 File Format

Property	Description
Algorithm	SHA-256 (hexadecimal digest)
Format	<HEX_DIGEST>  <filename>
Line Endings	LF (\n)
Scope	Hash calculated over artifact binary data (not symlinks)
Purpose	CI integrity verification and STAC compliance validation


⸻

🛠️ Generate & Verify

Generate Checksums

cd data/derivatives/landcover
for f in *.tif *.geojson *.parquet *.csv; do
  [ -f "$f" ] || continue
  shasum -a 256 "$f" > "checksums/${f}.sha256"
done

Verify Checksums

cd data/derivatives/landcover
for c in checksums/*.sha256; do
  base=$(basename "$c" .sha256)
  sha256sum -c "checksums/${base}.sha256"
done

✅ Use sha256sum (Linux) or shasum -a 256 (macOS); both produce identical hex digests.

⸻

🔗 STAC Integration (Provenance)

STAC Field	Example
assets.<key>.href	"nlcd_1992_2021_cog.tif"
assets.<key>.checksum:sha256	"edb8a2c1ff34a27dfb1f6c2c7e2b8..."
properties['kfm:provenance']	"data/sources/usgs_nlcd.json"

Checksums are embedded in STAC metadata to guarantee dataset authenticity and to synchronize with KFM’s validation pipeline.

⸻

🧩 Knowledge Graph & API Use
	•	Each asset node in Neo4j includes its checksum_sha256 property.
	•	API endpoint GET /api/landcover/{id}/checksum provides digests for client verification.
	•	The web UI’s layer panel reflects checksum status: ✅ verified / ⚠️ out-of-date.

⸻

🧱 Naming Conventions

Pattern	Example	Notes
<dataset>_<years>_cog.tif.sha256	nlcd_1992_2021_cog.tif.sha256	Multiyear COG raster
<dataset>_<range>_composite_cog.tif.sha256	landuse_1900_2000_composite_cog.tif.sha256	Historical composites
<dataset>_<region>.geojson.sha256	vegetation_zones_1850_ks.geojson.sha256	Vector polygons
<dataset>_<year>_cog.tif.sha256	prairie_extent_2020_cog.tif.sha256	Single-epoch raster


⸻

✅ Policy

1️⃣ Every landcover derivative must include a matching .sha256 checksum before publication.
2️⃣ Recompute digests after any file modification or re-projection.
3️⃣ CI (stac-validate.yml) fails if digests mismatch the STAC item.
4️⃣ All PRs involving derivative updates must include revised .sha256 files.

⸻

🔒 Reproducibility & MCP Alignment

Checksums uphold MCP’s reproducibility standards by:
	•	Documenting artifact integrity through transparent, auditable hashes.
	•	Ensuring pipeline determinism across environments.
	•	Providing verifiable evidence of data lineage across ETL → STAC → Graph → UI.

These manifests safeguard Kansas Frontier Matrix’s landcover and vegetation datasets as trusted scientific references.

⸻

🧱 Related Documentation
	•	data/derivatives/landcover/metadata/README.md — metadata schema and linkage
	•	data/stac/README.md — STAC item and catalog structure
	•	docs/architecture.md — ETL, STAC, and provenance architecture
	•	data/sources/README.md — landcover source manifest guidelines

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial landcover checksum policy and examples.