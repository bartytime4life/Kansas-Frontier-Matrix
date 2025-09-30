<div align="center">

# 📂 Kansas Geo Timeline — Processed Data

This directory contains **derived, cleaned, and ready-for-use geospatial + historical datasets**.  

All files are **pipeline outputs** (ETL workflows, experiments, or transformations) and  
every artifact is referenced in the **STAC catalog** (`data/stac/items/`).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw data\n(data/raw/**)"] --> B["ETL / Cleaning\n(scripts, notebooks)"]
  B --> C["Processed outputs\n(data/processed/**)"]
  C --> D["Provenance sidecars\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/**)"]
  E --> F["Validate\n(stac-validate · schema)"]
  F --> G["Web viewer layers\n(web/config/**)"]

<!-- END OF MERMAID -->



⸻

🧭 Principles
	•	Immutable inputs, reproducible outputs
	•	Raw data lives in data/raw/.
	•	Outputs here must be reproducible from scripts + configs + GCPs.
	•	Nothing in this directory is hand-edited.
	•	STAC integration
	•	Every file here links to a STAC Item in data/stac/items/.
	•	Each item records: datetime, bbox, checksum, license, provenance.
	•	Items are grouped into STAC Collections (data/stac/collections/).
	•	Lightweight storage
	•	Large rasters tracked with Git LFS or DVC.
	•	Vectors & tables stored as GeoJSON, CSV, Parquet.
	•	Holds only current, published outputs (not archives).
	•	MCP reproducibility
	•	Each dataset traces back to an experiment, config, or Makefile step.
	•	Provenance sidecars (.sha256, .meta.json) required.
	•	Outputs treated as experiment results with full lineage.

⸻

📂 Typical contents

data/processed/
├── towns_points.json          # Settlements (GeoJSON)
├── ks_treaties.json           # Treaty boundaries (historic polygons)
├── ks_railroads.json          # Railroad lines (historic)
├── hydrology.json             # Rivers and waterbodies
├── landcover_timeslices.json  # NLCD 1992–2021 snapshots
├── dem/
│   ├── ks_1m_hillshade.tif
│   ├── ks_slope.tif
│   └── vectors/contours.json
├── hydrology/                 # Subsets (Kansas River, floodplains)
└── oral_histories.csv         # Oral history index (structured)

Formats
	•	Vectors → GeoJSON (*.json, *.geojson)
	•	Tables → CSV (*.csv), Parquet (*.parquet)
	•	Rasters → GeoTIFF/COG (*.tif)
	•	Metadata → JSON (*.meta.json)

Schemas align with web/config/layers.schema.json for seamless viewer integration.

⸻

🔄 Workflow
	1.	Fetch raw data → data/raw/

make fetch


	2.	Transform / clean → scripts or notebooks (experiments/*/)
	•	Reproject, clip to Kansas extent, normalize fields.
	3.	Save outputs → data/processed/ in open formats.
	4.	Generate checksums

scripts/gen_sha256.sh data/processed/<file>


	5.	Update STAC Item → data/stac/items/
	•	Ensure href, checksum, and links are correct.
	6.	Validate → schema + STAC

make stac-validate
pre-commit run --all-files



⸻

📑 Example entries

Vector GeoJSON
	•	File: data/processed/ks_treaties.json
	•	STAC: data/stac/items/vectors/ks_treaties.json
	•	Viewer: web/data/treaties.json

Raster COG
	•	File: data/processed/dem/ks_1m_hillshade.tif
	•	STAC: data/stac/items/topo/ks_1m_hillshade.json
	•	Viewer: web/data/hillshade.json
	•	Export: data/kml/ks_hillshade_2018_2020.kmz

⸻

📝 Notes
	•	❌ Do not manually edit files here — regenerate via pipeline.
	•	✅ Document provenance (configs, scripts, GCPs).
	•	🔗 Keep filenames stable for references (STAC, Makefile, configs).
	•	🗂️ Use collections (data/stac/collections/) to group datasets (e.g., treaties, DEM, landcover).
	•	📦 Use make clean to clear rasters when rebuilding experiments.

⸻

📚 See also
	•	data/raw/ — raw acquisitions.
	•	data/cogs/ — cloud-optimized mission-final rasters.
	•	data/stac/ — STAC items & collections.
	•	web/data/ — configs for the web viewer.
	•	data/kml/ — KML/KMZ Earth exports.
	•	experiments/ — MCP-style experiment logs.

⸻

✅ Mission-grade principle: Processed datasets must be consistent, versioned, STAC-compliant, and reproducible across pipelines, experiments, and web layers.

