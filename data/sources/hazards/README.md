<div align="center">

# 🌪 Kansas-Frontier-Matrix — Hazards & Disasters STAC Items  
`stac/items/hazards/`

**Mission:** Provide **time-aware STAC Item descriptors** for Kansas hazard datasets,  
ensuring tornadoes, floods, droughts, wildfires, and FEMA disasters are  
**auditable, reproducible, and linked** into the Frontier-Matrix knowledge hub.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)  

</div>

---

## 🎯 Purpose

- Define **STAC Item JSONs** for each hazard dataset  
- Guarantee **traceability, provenance, and licensing**  
- Enable **timeline + map viewer** integration  
- Support **knowledge graph linking** (Event ↔ Place ↔ Document)  

---

## 📂 Directory Layout

```text
stac/items/hazards/
├── tornado_tracks_1950_2024.json
├── drought_monitor_2000_present.json
├── wildfire_perimeters_2000_present.json
└── README.md


⸻

🌪 Tornado Tracks (1950–2024)

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tornado_tracks_1950_2024",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "properties": {
    "title": "NOAA SPC Tornado Tracks (1950–2024)",
    "description": "Tornado tracks across Kansas with EF scale, path width, fatalities, and damage estimates.",
    "start_datetime": "1950-01-01T00:00:00Z",
    "end_datetime": "2024-12-31T23:59:59Z",
    "license": "public-domain",
    "providers": [
      {
        "name": "NOAA Storm Prediction Center",
        "roles": ["producer", "licensor"],
        "url": "https://www.spc.noaa.gov/gis/svrgis/"
      }
    ],
    "keywords": ["tornado", "hazard", "Kansas", "SPC", "severe weather"]
  },
  "assets": {
    "data": {
      "href": "https://www.spc.noaa.gov/gis/svrgis/Tornado/1950-2024_tornado_tracks.shp.zip",
      "type": "application/zip",
      "roles": ["data"]
    },
    "geojson": {
      "href": "../../data/processed/hazards/tornado_tracks_1950_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "self", "href": "./tornado_tracks_1950_2024.json" },
    { "rel": "collection", "href": "../collections/hazards.json" }
  ]
}


⸻

🌵 Drought Monitor (2000–present)

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "drought_monitor_2000_present",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "properties": {
    "title": "U.S. Drought Monitor (2000–present)",
    "description": "Weekly drought polygons (D0–D4 categories) for Kansas.",
    "start_datetime": "2000-01-01T00:00:00Z",
    "end_datetime": null,
    "license": "public-domain",
    "providers": [
      {
        "name": "NOAA / USDA / NDMC",
        "roles": ["producer", "licensor"],
        "url": "https://droughtmonitor.unl.edu/"
      }
    ],
    "keywords": ["drought", "hazard", "Kansas", "NDMC", "time series"]
  },
  "assets": {
    "data": {
      "href": "https://droughtmonitor.unl.edu/data/shapefiles_m/USDM_20250121_M.zip",
      "type": "application/zip",
      "roles": ["data"]
    },
    "timeseries": {
      "href": "../../data/processed/hazards/drought_monitor_timeseries.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "self", "href": "./drought_monitor_2000_present.json" },
    { "rel": "collection", "href": "../collections/hazards.json" }
  ]
}


⸻

🔥 Wildfire Perimeters (2000–present)

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "wildfire_perimeters_2000_present",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "properties": {
    "title": "Wildfire Perimeters (2000–present)",
    "description": "Large wildfire perimeters across Kansas, with fire name, ignition date, and acres burned.",
    "start_datetime": "2000-01-01T00:00:00Z",
    "end_datetime": null,
    "license": "public-domain",
    "providers": [
      {
        "name": "NIFC + Kansas Forest Service",
        "roles": ["producer", "licensor"],
        "url": "https://data-nifc.opendata.arcgis.com/"
      }
    ],
    "keywords": ["wildfire", "hazard", "Kansas", "NIFC", "Kansas Forest Service"]
  },
  "assets": {
    "data": {
      "href": "https://data-nifc.opendata.arcgis.com/datasets/wildfire-perimeters-2000-present.zip",
      "type": "application/zip",
      "roles": ["data"]
    },
    "geojson": {
      "href": "../../data/processed/hazards/wildfire_perimeters_2000_present.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "self", "href": "./wildfire_perimeters_2000_present.json" },
    { "rel": "collection", "href": "../collections/hazards.json" }
  ]
}


⸻

🔗 Integration Notes
	•	Each Item belongs to stac/collections/hazards.json
	•	Assets include raw shapefiles/archives + processed GeoJSONs
	•	Temporal extent drives timeline slider in MapLibre UI
	•	Keywords & providers support search & provenance

⸻

✅ Best Practices
	•	Maintain .sha256 checksums for all assets
	•	Normalize CRS → EPSG:4326 (record original in _meta.json)
	•	Add thumbnail assets when available for map previews
	•	Update retrieved timestamps whenever refreshed

⸻

✦ Summary

These STAC Items define Kansas hazard & disaster layers in a machine-readable,
STAC 1.0.0-compliant format. They ensure tornadoes, droughts, and wildfires
are fully documented, reproducible, and integrated into the Kansas-Frontier-Matrix
knowledge graph, catalog, and interactive timeline viewer.