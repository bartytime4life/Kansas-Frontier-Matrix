<div align="center">

# 📂 Kansas-Frontier-Matrix — Processed Data  
`data/processed/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/)  

**Mission:** Hold **derived, cleaned, and ready-for-use geospatial + historical datasets**.  
All files here are **pipeline outputs** (ETL workflows, experiments, transformations).  
Every artifact is referenced in the **STAC catalog** (`data/stac/items/`) and validated against schemas for seamless integration into the web viewer.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw data\n(data/raw/**)"] --> B["ETL / Cleaning\n(scripts · notebooks · configs)"]
  B --> C["Processed outputs\n(data/processed/**)"]
  C --> D["Provenance sidecars\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/**)"]
  E --> F["Validate\n(make stac-validate · schema checks)"]
  F --> G["Web viewer integration\n(web/config/**)"]
  G --> H["Knowledge Hub links\n(cross-domain integration)"]

<!-- END OF MERMAID -->



⸻

🧭 Principles
	•	Immutable inputs, reproducible outputs
	•	Raw data lives in data/raw/
	•	Outputs here must be reproducible from scripts + configs + GCPs
	•	❌ Nothing here is hand-edited
	•	STAC integration
	•	Every file here links to a STAC Item in data/stac/items/
	•	Each item records: datetime, bbox, checksum, license, provenance
	•	Items are grouped into Collections (data/stac/collections/)
	•	Lightweight storage
	•	Large rasters tracked with Git LFS or DVC
	•	Vectors & tables → GeoJSON, CSV, Parquet
	•	Holds only current, published outputs (not archives)
	•	MCP reproducibility
	•	Each dataset traces back to an experiment, config, or Makefile step
	•	Provenance sidecars (.sha256, .meta.json) required
	•	Outputs treated as experiment results with full lineage

⸻

📂 Directory Structure

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

Formats:
	•	Vectors → GeoJSON (.json, .geojson)
	•	Tables → CSV (.csv), Parquet (.parquet)
	•	Rasters → GeoTIFF/COG (.tif)
	•	Metadata → JSON (.meta.json)

⸻

🔄 Workflow
	1.	Fetch raw data → data/raw/

make fetch

	2.	Transform / clean → scripts or notebooks (experiments/*/)
	•	Reproject to EPSG:4326
	•	Clip to Kansas extent
	•	Normalize schema fields
	3.	Save outputs → data/processed/ in open formats
	4.	Generate checksums

scripts/gen_sha256.sh data/processed/<file>

	5.	Update STAC Items → data/stac/items/
	•	Ensure href, checksum, and links are correct
	6.	Validate → schema + STAC

make stac-validate
pre-commit run --all-files


⸻

📑 Example STAC Items

Vector (Treaty Boundaries, GeoJSON)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_treaties",
  "properties": {
    "title": "Kansas Treaty Boundaries",
    "description": "Historic treaty boundaries digitized for Kansas.",
    "datetime": "1854-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Digitized from historic maps",
    "kfm:lineage": [
      "data/raw/treaties/treaty_maps_scan.tif",
      "data/processed/ks_treaties.json"
    ],
    "qa:status": "provisional"
  },
  "links": [
    { "rel": "collection", "href": "../../stac/collections/vectors.json" }
  ],
  "assets": {
    "geojson": {
      "href": "../../data/processed/ks_treaties.json",
      "title": "Treaty Boundaries (Kansas)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}

Raster (DEM Hillshade, COG)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_1m_hillshade",
  "properties": {
    "title": "Kansas Hillshade (1m DEM)",
    "description": "Hillshade generated from Kansas 1m DEM mosaics.",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "GDAL hillshade",
    "kfm:lineage": [
      "data/cogs/dem/ks_1m_2018.tif",
      "data/cogs/dem/ks_1m_2020.tif"
    ],
    "qa:status": "verified"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-102.05, 40.00],
      [-94.59, 40.00],
      [-94.59, 36.99],
      [-102.05, 36.99]
    ]]
  },
  "links": [
    { "rel": "collection", "href": "../../stac/collections/terrain.json" }
  ],
  "assets": {
    "cog": {
      "href": "../../data/processed/dem/ks_1m_hillshade.tif",
      "title": "Hillshade (Kansas DEM, 1m)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    }
  }
}


⸻

✅ QA Checklist
	•	All outputs reprojected to EPSG:4326
	•	Checksums generated (.sha256)
	•	STAC Items updated with correct href, roles, and checksums
	•	Filenames stable for STAC + Makefile references
	•	Large files tracked with Git LFS or DVC
	•	Provenance documented in experiments/

⸻

📝 Notes
	•	❌ Do not manually edit files here — always regenerate via pipeline
	•	✅ Document provenance (configs, scripts, GCPs)
	•	🔗 Keep filenames stable for references (STAC, Makefile, configs)
	•	🗂️ Use data/stac/collections/ to group datasets (treaties, DEM, landcover)
	•	📦 Use make clean to clear rasters when rebuilding experiments

⸻

📚 See Also
	•	data/raw/ → raw acquisitions
	•	data/cogs/ → cloud-optimized mission-final rasters
	•	data/stac/ → STAC items & collections
	•	web/data/ → configs for the web viewer
	•	data/kml/ → KML/KMZ Earth exports
	•	experiments/ → MCP-style experiment logs

⸻


<div align="center">


✅ Mission Principle
Processed datasets must be consistent, versioned, STAC-compliant, and reproducible across pipelines, experiments, and web layers.

</div>
```
