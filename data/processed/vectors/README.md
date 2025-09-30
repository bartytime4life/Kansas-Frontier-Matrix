<div align="center">

# 🗺️ Kansas Geo Timeline — Processed Vectors

This directory contains **processed vector datasets**  
that are cleaned, derived, or aggregated from raw acquisitions in `data/raw/`  
and published in open formats (GeoJSON, CSV).  

All outputs here are **pipeline results** (no manual edits),  
**referenced in the STAC catalog** (`data/stac/items/vectors/`),  
and validated against `web/config/layers.schema.json` for seamless use in the web viewer.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw vectors & scans\n(data/raw/**)"] --> B["Process / Clean\n(reproject · simplify · normalize)"]
  B --> C["Processed vectors\n(data/processed/vectors/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/vectors/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]

<!-- END OF MERMAID -->



⸻

📂 Typical contents

data/processed/vectors/
├── treaties.json            # Treaty & reservation boundaries
├── railroads_1900.json      # Historic railroads circa 1900
├── trails.json              # Overland & migration trails
├── towns_points.json        # Historic settlement locations
├── counties_1855.json       # Territorial county boundaries
└── README.md

Common vector themes
	•	Political / Legal → treaties, reservations, county boundaries.
	•	Infrastructure → railroads, roads, trails.
	•	Settlements → towns, forts, posts.
	•	Environmental → floodplains, fire perimeters, soils (vectorized).

⸻

🔄 Workflow
	1.	Fetch raw data → data/raw/ (scanned maps, shapefiles, GeoJSON).
	2.	Process
	•	Reproject → EPSG:4326 (WGS84).
	•	Clean attributes, dissolve/simplify geometries.
	•	Normalize schema fields (id, name, year, type).
	3.	Export → data/processed/vectors/*.json (canonical GeoJSON).
	4.	Checksums

scripts/gen_sha256.sh data/processed/vectors/*.json


	5.	STAC registration
	•	Add/update Item JSON under data/stac/items/vectors/.
	•	Include roles: ["data"] and checksum:sha256.
	6.	Validate

make stac-validate
pre-commit run --all-files



⸻

🔗 Integration
	•	STAC catalog → discoverable in data/stac/items/vectors/.
	•	Web viewer → wired into web/config/layers.json.
	•	KML exports → selected vectors exported to data/kml/ for Google Earth.
	•	Experiments → used in treaty-land overlays, settlement studies, archaeology, hazard analysis.

⸻

📝 Notes
	•	Canonical format = GeoJSON (.json).
	•	For very large datasets, tile or convert to MBTiles/PMTiles — but keep canonical GeoJSON here.
	•	Track large files with Git LFS / DVC.
	•	Follow naming convention: <theme>_<year>.json or <theme>_<params>.json.
	•	Examples: railroads_1900.json, treaties.json.
	•	Document processing steps in experiments/<ID>_.../experiment.md.

⸻

📚 See also
	•	../dem/vectors/ → DEM-derived vector products (contours, watersheds, streams).
	•	../hydrology/ → processed hydrology datasets.
	•	../../stac/items/vectors/ → STAC items for processed vectors.
	•	../../kml/ → KML/KMZ Earth-ready exports.
	•	experiments/ → MCP notebooks + logs for vector processing.

⸻

✅ Mission-grade principle: Processed vectors must be clean, reproducible, STAC-linked, and schema-validated for integration into the Kansas Frontier Matrix.

