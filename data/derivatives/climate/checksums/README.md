<div align="center">

# 🧾 Kansas Frontier Matrix — Climate Derivative Checksums  
`data/derivatives/climate/checksums/`

**Purpose:** Provide reproducible, machine-verifiable integrity for climate-derivative artifacts  
(COG · GeoJSON · Parquet · CSV) produced by the ETL pipeline.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-brightgreen)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum manifests** for all climate-derivative outputs under  
`data/derivatives/climate/ …`.  
Checksums function as **integrity anchors** across KFM’s full chain — **ETL → STAC → Knowledge Graph → API → Web UI** — ensuring that every artifact used in research or visualization can be independently verified and reproduced.

---

## 🧭 When and where checksums are created

```mermaid
flowchart TD
  A["Sources\nNOAA · Daymet · Normals"] --> B["ETL\nnormalize · reproject · derive"]
  B --> C["Climate Derivatives\nCOGs · GeoJSON · Parquet"]
  C --> D["Compute SHA-256\n*.sha256 files"]
  D --> E["STAC Items\nlink assets + checksum"]
  E --> F["Graph Load\nprovenance + asset refs"]
  F --> G["API & Web UI\nserve verified assets"]
  click E "_blank" "Indexed in data/stac/"
  click C "_blank" "data/derivatives/climate/"
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂 Directory layout

data/derivatives/climate/
├── # derived climate products (COGs, GeoJSON, Parquet, CSV)
└── checksums/
    ├── 1991_2020_normals_prcp_cog.tif.sha256
    ├── daymet_1980_2024_tmin_ks_cog.tif.sha256
    ├── drought_index_annual_ks.parquet.sha256
    ├── station_normals_points.geojson.sha256
    └── README.md

Only .sha256 files reside here; binaries live one level up in data/derivatives/climate/.

⸻

🧪 Algorithm & File Format

Property	Value/Explanation
Algorithm	SHA-256 (hex digest)
Format	<HEX_DIGEST>  <filename> (one line per file)
Line Endings	LF (\n)
Scope	Hashes are computed over raw binary files (not symlinks)
Why SHA-256	Collision-resistant and portable across toolchains (sha256sum, shasum -a 256, openssl dgst)


⸻

🛠️ Generate & Verify

Generate

cd data/derivatives/climate
for f in *.tif *.parquet *.geojson *.csv; do
  [ -f "$f" ] || continue
  shasum -a 256 "$f" > "checksums/${f}.sha256"
done

Verify

cd data/derivatives/climate
for c in checksums/*.sha256; do
  base=$(basename "$c" .sha256)
  sha256sum -c "checksums/${base}.sha256"
done


⸻

🔗 STAC Integration (Provenance)

Each climate asset’s STAC item includes its digest for traceability:

Key	Example
assets.<key>.href	data/derivatives/climate/daymet_1980_2024_tmin_ks_cog.tif
assets.<key>.checksum:sha256	fa9c…​3b2d
properties['kfm:provenance']	data/sources/daymet.json

Checksums act as CI validation gates in the stac-validate workflow.

⸻

🧩 Knowledge Graph & API Usage
	•	checksum_sha256 properties attach to asset nodes in Neo4j for evidential provenance.
	•	API route GET /api/assets/{id}/checksum returns the digest for client-side validation.

⸻

🧱 Naming Conventions

Pattern	Example	Notes
<dataset>_<temporal>_<var>_ks_cog.tif.sha256	daymet_1980_2024_tmin_ks_cog.tif.sha256	Year range + KS suffix
<dataset>_<period>_<name>.parquet.sha256	drought_index_annual_ks.parquet.sha256	Tabular derivative
<dataset>_<layer>.geojson.sha256	station_normals_points.geojson.sha256	Vector layer naming
<dataset>_<period>_<var>.csv.sha256	normals_1991_2020_prcp.csv.sha256	Small CSV outputs


⸻

✅ Policy

1️⃣ Every derivative file must have a matching .sha256 before publication.
2️⃣ Never edit digests by hand — recompute after any modification.
3️⃣ CI fails if hash ≠ STAC record.
4️⃣ All PRs touching derivatives must include updated checksums.

⸻

🔒 Reproducibility & MCP Alignment

Checksums embody KFM’s Master Coder Protocol principles — verifiable data integrity, traceable provenance, and container-reproducible ETL runs across data/sources/, data/processed/, and data/stac/.

⸻

🧱 Related Docs
	•	docs/architecture.md · docs/data-architecture.md
	•	data/stac/catalog.json (STAC entries with checksum:sha256)
	•	Monorepo Design → Integrity Gates section

⸻

🗓 Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial checksum policy and examples