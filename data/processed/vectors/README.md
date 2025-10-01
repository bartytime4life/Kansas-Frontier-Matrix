<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Processed Vectors  
`data/processed/vectors/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Hold **processed vector datasets**  
that are cleaned, derived, or aggregated from raw acquisitions in `data/raw/`  
and published in open formats (GeoJSON, CSV).  

All outputs here are **pipeline results** (no manual edits),  
**referenced in the STAC catalog** (`data/stac/items/vectors/`),  
and validated against `web/config/layers.schema.json` for seamless use in the web viewer.  

</div>

---

## 📈 Lifecycle

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

📂 Typical Contents

data/processed/vectors/
├── treaties.json            # Treaty & reservation boundaries
├── railroads_1900.json      # Historic railroads circa 1900
├── trails.json              # Overland & migration trails
├── towns_points.json        # Historic settlement locations
├── counties_1855.json       # Territorial county boundaries
└── README.md

Common vector themes
	•	Political / Legal → treaties, reservations, county boundaries
	•	Infrastructure → railroads, roads, trails
	•	Settlements → towns, forts, posts
	•	Environmental → floodplains, fire perimeters, soils (vectorized)

⸻

🔄 Workflow
	1.	Fetch raw data → data/raw/ (scanned maps, shapefiles, GeoJSON)
	2.	Process
	•	Reproject → EPSG:4326 (WGS84)
	•	Clean attributes, dissolve/simplify geometries
	•	Normalize schema fields (id, name, year, type)
	3.	Export → data/processed/vectors/*.json (canonical GeoJSON)
	4.	Checksums

scripts/gen_sha256.sh data/processed/vectors/*.json


	5.	STAC registration
	•	Add/update Item JSON under data/stac/items/vectors/
	•	Include roles: ["data"] and checksum:sha256
	6.	Validate

make stac-validate
pre-commit run --all-files



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
    "kfm:lineage": [
      "data/raw/vectors/treaty_scans/*.tif"
    ],
    "qa:status": "provisional"
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/vectors.json"
    }
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
    "kfm:lineage": [
      "data/raw/vectors/railroads_1900_scan.tif"
    ],
    "qa:status": "verified"
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/vectors.json"
    }
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
	•	STAC catalog → discoverable in data/stac/items/vectors/
	•	Web viewer → layers wired into web/config/layers.json
	•	KML exports → selected vectors exported to data/kml/ for Google Earth
	•	Experiments → used in treaty-land overlays, settlement studies, archaeology, hazard analysis

⸻

📝 Notes
	•	Canonical format = GeoJSON (.json)
	•	For very large datasets, tile or convert to MBTiles/PMTiles (but keep canonical GeoJSON here)
	•	Track large files with Git LFS / DVC
	•	Follow naming convention: <theme>_<year>.json or <theme>_<params>.json
	•	Examples: railroads_1900.json, treaties.json
	•	Document processing steps in experiments/<ID>_.../experiment.md

⸻

📚 See Also
	•	../dem/vectors/ → DEM-derived vector products (contours, watersheds, streams)
	•	../hydrology/ → processed hydrology datasets
	•	../../stac/items/vectors/ → STAC items for processed vectors
	•	../../kml/ → KML/KMZ Earth-ready exports
	•	experiments/ → MCP notebooks + logs for vector processing

⸻

✅ Mission Principle

Processed vectors must be clean, reproducible, STAC-linked, and schema-validated,
ready for integration into the Kansas Frontier Matrix web mapping system.