<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Web Data (Layers & Map Data)  
`web/data/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Provide **layer specs** and **map-ready data references** for the MapLibre viewer  
(timeline + toggles). Each JSON here is either a **layer spec** (id, title, type, time, legend, style)  
or a **data pointer** (GeoJSON/PMTiles/COG/XYZ/WMS).

This directory is the **bridge** between the project’s **ETL/STAC pipeline** and the **interactive map UI**.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["ETL / Derivatives\n(data/processed/** · data/derivatives/**)"] --> B["STAC Items\n(stac/items/**)"]
  B --> C["Config Render\n(kgt render-config → web/config/app.config.json)"]
  C --> D["Layer Specs & Data Pointers\n(web/data/**)"]
  D --> E["MapLibre Viewer\n(web/index.html + app.js)"]

<!-- END OF MERMAID -->



⸻

📂 What lives here

web/
└─ data/
   ├─ layers.json                 # main layer index consumed by the UI
   ├─ categories.json             # optional grouping (e.g., basemap, environment, hazards, movement, sovereignty, culture)
   ├─ *.layer.json                # per-layer specs (recommended for large sets)
   ├─ legends/                    # legend presets (ramp, fill, line)
   ├─ styles/                     # optional style presets shared by layers
   ├─ templates/                  # example snippets for new layers
   └─ docs/                       # optional layer notes (provenance, QA results)

Data artifacts (COGs, PMTiles, GeoJSON) are produced by ETL and referenced here.
Do not check large binaries into web/data/. Prefer COG for rasters and PMTiles for large vectors.

⸻

🧩 Layer spec (canonical shape)

Each layer file follows a minimal shape; the viewer merges these into UI controls and the timeline.

{
  "id": "unique_layer_id",
  "title": "Human-readable Layer Title",
  "category": "basemap | environment | hazards | movement | sovereignty | culture",
  "type": "vector | raster | image | raster-dem",
  "format": "geojson | pmtiles | cog | xyz | wms",
  "data": "relative/or/absolute/url/to/data",
  "bounds": [-102.051, 36.993, -94.588, 40.003],
  "minzoom": 5,
  "maxzoom": 19,
  "visible": false,
  "opacity": 1.0,

  "time": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" },
  "timeProperty": "optional_property_on_features_for_time",
  "timeFormat": "iso-date | year | year-month | ordinal",
  "timePrecision": "day | month | year",

  "popup": ["field_a", "field_b", "field_c"],

  "legend": {
    "type": "fill | line | ramp | gradient",
    "label": "Legend Title",
    "classes": [
      { "label": "class name", "fill": "#hex", "stroke": "#hex", "value": 1 }
    ]
  },

  "style": {
    "lineColor": "#3A86FF",
    "lineWidth": 1.5,
    "fillColor": "#A0C4FF",
    "fillOpacity": 0.8,
    "circleColor": "#FF006E",
    "circleRadius": 3
  },

  "attribution": "Source | Org | Year",
  "license": "license string or URL",
  "provenance": "link to STAC item or source descriptor"
}

Required keys
	•	id, title, category, type, format, data
	•	attribution, license
	•	Time: either a layer-level time range or timeProperty (per-feature)

Optional keys
	•	bounds, minzoom, maxzoom, visible, opacity
	•	legend, style, popup, timeFormat, timePrecision, provenance

⸻

🕰️ Time support (how the slider reads your layer)

1) Static window (layer-level)

"time": { "start": "1894-01-01", "end": "1894-12-31" }

Use for a single historic map or a survey year.

2) Per-feature time (dynamic)

"timeProperty": "year",
"timeFormat": "year",
"timePrecision": "year"

The viewer filters features as the slider moves (e.g., events by year).
For approximate time (e.g., “spring 1850s”), normalize to a machine value and add an _confidence field for popups.

⸻

💾 Data formats & performance (recommended)
	•	Vectors
	•	Small → GeoJSON
	•	Medium/large or statewide/time-series → PMTiles (single-file, CDN-friendly)
	•	Rasters
	•	COG with internal overviews (HTTP ranged reads)
	•	XYZ/WMTS only if hosted elsewhere
	•	DEM
	•	type: "raster-dem"; serve tile sources for terrain/hillshade

Align with pipeline converters (rio-cogeo, GDAL/OGR, tippecanoe/pmtiles) from Makefile targets.

⸻

🧭 Categories (suggested)
	•	basemap (terrain/DEM, hillshade, historic USGS sheets)
	•	environment (landcover, soils, vegetation, wetlands)
	•	hazards (tornado tracks, floods, wildfire perimeters, drought)
	•	movement (trails, railroads by year, roads)
	•	sovereignty (treaties/reservations, counties by era)
	•	culture (settlements, forts, cemeteries, oral histories)

These map to sidebar groupings and storytelling lanes.

⸻

✅ Examples (snippets to copy)

1) Historic topo (raster COG, single year)

{
  "id": "topo_1894_pawnee",
  "title": "USGS Topographic Map — Pawnee (1894)",
  "category": "basemap",
  "type": "raster",
  "format": "cog",
  "data": "data/cogs/topo/pawnee_1894.tif",
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "opacity": 0.85,
  "attribution": "USGS Historical Topographic Map Collection",
  "license": "Public Domain",
  "provenance": "stac/items/topo_1894_pawnee.json"
}

2) Tornado tracks (vector PMTiles, 1950–present)

{
  "id": "tornado_tracks",
  "title": "Tornado Tracks (1950–Present)",
  "category": "hazards",
  "type": "vector",
  "format": "pmtiles",
  "data": "https://cdn.example.org/ks_tornado_tracks.pmtiles",
  "timeProperty": "yr",
  "timeFormat": "year",
  "style": { "lineColor": "#D83C3C", "lineWidth": 1.2, "opacity": 0.9 },
  "popup": ["date", "ef_scale", "length_km", "fatalities"],
  "attribution": "NOAA SPC",
  "license": "Public Domain",
  "provenance": "stac/items/haz_tornado_tracks.json"
}

3) Drought (weekly polygons)

{
  "id": "drought_usdm",
  "title": "U.S. Drought Monitor (Weekly)",
  "category": "hazards",
  "type": "vector",
  "format": "pmtiles",
  "data": "https://cdn.example.org/usdm_weekly.pmtiles",
  "timeProperty": "week_iso",
  "timeFormat": "iso-date",
  "legend": {
    "type": "ramp",
    "label": "Drought Category",
    "classes": [
      { "label": "D0 Abnormally Dry", "fill": "#ffffb2", "value": 0 },
      { "label": "D1 Moderate",        "fill": "#fecc5c", "value": 1 },
      { "label": "D2 Severe",          "fill": "#fd8d3c", "value": 2 },
      { "label": "D3 Extreme",         "fill": "#f03b20", "value": 3 },
      { "label": "D4 Exceptional",     "fill": "#bd0026", "value": 4 }
    ]
  },
  "attribution": "USDM (NOAA/USDA/NDMC)",
  "license": "Public Domain",
  "provenance": "stac/items/haz_usdm_weekly.json"
}

4) Treaties & reservations (polygons with eras)

{
  "id": "treaties_reservations",
  "title": "Treaties & Reservations (Historical)",
  "category": "sovereignty",
  "type": "vector",
  "format": "geojson",
  "data": "data/processed/sovereignty/treaties_reservations.geojson",
  "timeProperty": "year",
  "legend": { "type": "fill", "label": "Status", "classes": [
    { "label": "Reservation", "fill": "#4C78A8" },
    { "label": "Treaty Area", "fill": "#9EC1CF" }
  ]},
  "popup": ["name", "tribe", "year", "year_end", "accuracy", "source"],
  "attribution": "Compiled from historical sources",
  "license": "Open (see feature properties)",
  "provenance": "stac/items/sovereignty_treaties.json"
}


⸻

🧾 Attribution, license, provenance (non-negotiable)
	•	Every layer must declare attribution, license, and a traceable provenance link (STAC item or source descriptor).
	•	For external services (ArcGIS, WMS), mirror the provider’s attribution & terms.
	•	For compiled layers, enumerate source blend and synthesis date in STAC.

⸻

🧪 How to add a new layer (checklist)
	1.	Create/convert the artifact

	•	Vector → GeoJSON (small) or PMTiles (large)
	•	Raster → COG with overviews
	•	Normalize to EPSG:4326

	2.	STAC + source descriptor

	•	Write a STAC Item under stac/items/ with assets pointing to the artifact
	•	Include bbox, time, licensing, providers

	3.	Author the layer spec

	•	Add *.layer.json (or append layers.json) with schema above
	•	Include time metadata, category, legend/style, popup fields

	4.	Validate

make config-validate

	•	Open locally in the dev viewer; verify popup fields & time attributes

	5.	Performance sanity

	•	Tile if necessary; simplify dense geometry; confirm overviews

	6.	Document

	•	Add a short note in web/data/docs/ (edge cases, uncertainty, source anomalies)

⸻

🧭 Conventions & tips
	•	IDs: snake_case, stable, no spaces (usgs_topo_1894_larned)
	•	Fields: keep popups concise; consider human vs machine names (ef_scale vs “EF Scale”)
	•	Legends: prefer explicit classes for reproducibility (no hidden magic)
	•	Bounds: set to layer bbox; used for auto-zoom on toggle
	•	Uncertainty: add _confidence / accuracy per feature when relevant and surface in popups

⸻

📚 Example categories to prioritize
	•	Basemaps: Hillshade/DEM (COG), 1890s–1950s USGS quads (COG)
	•	Hazards: Tornado tracks (SPC), floods/FEMA, drought (USDM), wildfire perimeters (NIFC)
	•	Sovereignty: Treaties/reservations, historical counties by year
	•	Movement: Trails, rail build-out by year
	•	Environment: Landcover (NLCD timeslices), soils/SSURGO, wetlands (NWI)
	•	Culture: Forts/settlements by era, cemeteries, oral histories POIs

⸻

🔗 See also
	•	web/config/ — viewer-wide config, categories & legend schemas
	•	stac/items/ — authoritative metadata & asset links
	•	data/processed/ · data/derivatives/ — generated artifacts referenced here

⸻

✅ Mission Principle

Keep the UI configuration declarative & testable, aligned with COG/PMTiles and STAC.
Do the work in pipelines, declare it here, validate, and ship — no code changes required.

⸻


