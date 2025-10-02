<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Processed Vectors  
`data/processed/vectors/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/vectors/)

**Mission:** Hold **processed vector datasets** that are cleaned, derived, or aggregated from raw acquisitions in `data/raw/` and published in open formats (GeoJSON, CSV).  
All outputs here are **pipeline results** (no manual edits), **registered in the STAC catalog** (`stac/items/vectors/`), and validated against the web viewer schema for seamless integration.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw vectors & scans\n(data/raw/**)"] --> B["Process / Clean\n(reproject · simplify · normalize)"]
  B --> C["Processed vectors\n(data/processed/vectors/**)"]
  C --> D["Checksums + metadata\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(stac/items/vectors/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]
  G --> H["Knowledge Hub links\n(people · places · events)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Structure

data/processed/vectors/
├── treaties.json            # Treaty & reservation boundaries
├── railroads_1900.json      # Historic railroads circa 1900
├── trails.json              # Overland & migration trails
├── towns_points.json        # Historic settlement locations (points)
├── counties_1855.json       # Territorial county boundaries
└── README.md

Common themes
	•	Political / Legal → treaties, reservations, territorial & county boundaries
	•	Infrastructure → railroads, roads, trails, telegraph lines
	•	Settlements → towns, forts, trading posts, agencies
	•	Environmental → floodplains (vectorized), fire perimeters, soils & landcover polygons

⸻

🧭 File Conventions
	•	Canonical vector format → GeoJSON (.json / .geojson)
	•	Tabular → CSV (.csv) for attribute tables / crosswalks
	•	Projection → EPSG:4326 (WGS84 lat/long) for all outputs
	•	Naming → <theme>_<year>.json or <theme>_<params>.json
	•	Examples: railroads_1900.json, counties_1855.json, trails_prairie_santa_fe.json

⸻

🔧 Schema (recommended core fields)

Field	Type	Description
id	string	Stable identifier (UUID or canonical slug)
name	string	Feature name / label
type	string	Category (e.g., treaty, railroad, trail)
year	integer	Primary year (or earliest year)
start_year	integer	Optional start year (temporal range)
end_year	integer	Optional end year (temporal range)
source	string	Short source label (archive, map, dataset)
notes	string	Free-text notes (curation, ambiguity, etc.)

Keep rich provenance in STAC properties.kfm:* and assets, while GeoJSON carries light-weight display attributes.

⸻

🔄 Workflow
	1.	Fetch raw data → data/raw/
	•	Scanned maps, shapefiles, GeoPackage, GeoJSON, CSVs
	2.	Process

	•	Reproject → EPSG:4326
	•	Clean attributes; dissolve/simplify geometries (scale-aware)
	•	Normalize schema fields (id, name, type, year, …)

	3.	Export → data/processed/vectors/*.json (canonical GeoJSON)
	4.	Checksums

scripts/gen_sha256.sh data/processed/vectors/*.json

	5.	STAC registration

	•	Add/update Item JSON under stac/items/vectors/
	•	Include roles: ["data"] and checksum:sha256

	6.	Validation

make stac-validate
pre-commit run --all-files


⸻

🧪 Suggested Make Targets

vectors: vectors-process vectors-stac vectors-validate

vectors-process:
\t# run your vector cleaning/simplification/normalization pipeline

vectors-stac:
\t# write or patch STAC Items/Collections for new/updated vectors

vectors-validate:
\tmake stac-validate
\tpre-commit run --all-files


⸻

✅ QA Checklist
	•	EPSG:4326 confirmed for all outputs
	•	Canonical GeoJSON exported and .sha256 created
	•	STAC Item created/updated with correct href, roles, and checksum
	•	Attributes normalized to the core schema (see table above)
	•	web/config/layers.json entries added/updated (and pass schema)
	•	Large files tracked with Git LFS or DVC
	•	Provenance recorded in STAC + experiments/

⸻

📑 Example STAC Items

Treaty Boundaries (vector, GeoJSON)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_treaties",
  "properties": {
    "title": "Kansas Treaty Boundaries",
    "description": "Historic treaty and reservation boundaries digitized for Kansas.",
    "datetime": "1854-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Digitized from archival maps and normalized",
    "kfm:lineage": ["data/raw/vectors/treaty_scans/*.tif"],
    "qa:status": "provisional"
  },
  "links": [
    { "rel": "collection", "href": "../../../stac/collections/vectors.json" }
  ],
  "assets": {
    "geojson": {
      "href": "../../../data/processed/vectors/treaties.json",
      "title": "Kansas Treaty Boundaries",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}

Railroads (1900, vector, GeoJSON)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_railroads_1900",
  "properties": {
    "title": "Kansas Railroads (1900)",
    "description": "Digitized historic railroads across Kansas, circa 1900.",
    "datetime": "1900-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Digitized and generalized from 1900 railroad index maps",
    "kfm:lineage": ["data/raw/vectors/railroads_1900_scan.tif"],
    "qa:status": "verified"
  },
  "links": [
    { "rel": "collection", "href": "../../../stac/collections/vectors.json" }
  ],
  "assets": {
    "geojson": {
      "href": "../../../data/processed/vectors/railroads_1900.json",
      "title": "Kansas Railroads (1900)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}


⸻

🔗 Integration
	•	STAC catalog → discoverable via stac/items/vectors/
	•	Web viewer → layers wired into web/config/layers.json
	•	KML exports → selected vectors exported to data/kml/ for Google Earth
	•	Knowledge Hub → link to people, places, events; enable timeline & narrative queries
	•	Experiments → treaty-land overlays, settlement studies, archaeology, hazard analysis

⸻

📝 Notes
	•	Canonical format = GeoJSON (retain original raw sources in data/raw/)
	•	For very large datasets → tile or convert to MBTiles/PMTiles (but keep canonical GeoJSON here)
	•	Keep filenames stable → <theme>_<year>.json or <theme>_<params>.json
	•	Document processing steps & decisions in experiments/<ID>_*/experiment.md

⸻

📚 See Also
	•	../dem/vectors/ → DEM-derived vectors (contours, watersheds, streams)
	•	../hydrology/ → processed hydrology datasets
	•	../../stac/items/vectors/ → STAC Items for processed vectors
	•	../../kml/ → KML/KMZ Earth-ready exports
	•	experiments/ → MCP notebooks + logs for vector processing

⸻


<div align="center">


✅ Mission Principle
Processed vectors must be clean, reproducible, STAC-linked, and schema-validated, ready for integration into the Kansas Frontier Matrix web mapping system.

</div>
```
