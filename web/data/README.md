Kansas-Frontier-Matrix — web/data/ (Layers & Map Data)

This folder contains the layer configs and map-ready data references used by the web viewer (MapLibre + time slider). Each JSON file here is either:
	•	a layer spec the viewer reads (id, title, type, format, time, attribution, legend, style), or
	•	a data pointer the layer consumes (GeoJSON/PMTiles/COG endpoints, service URLs, etc.).

This directory is the bridge between the project’s ETL/STAC pipeline and the interactive map UI (timeline + toggles).  ￼  ￼  ￼

⸻

What lives here (at a glance)

web/
└─ data/
   ├─ layers.json                 # main layer index consumed by the UI
   ├─ categories.json             # optional grouping (e.g., basemap, environment, hazards, movement, sovereignty, culture)
   ├─ *.layer.json                # per-layer specs (split files recommended for large sets)
   ├─ legends/                    # legend presets (ramp, fill, line)
   ├─ styles/                     # optional style presets shared by layers
   ├─ templates/                  # example snippets for new layers
   └─ docs/                       # optional layer notes (provenance, QA results)

The actual data artifacts (COGs, PMTiles, GeoJSON) are generated/managed by the ETL and referenced from here—do not check large binaries into web/data/. Prefer COG for rasters and PMTiles for large vectors for web performance.  ￼

⸻

Layer spec (schema)

Each layer file follows a minimal canonical shape; the viewer merges these into UI controls and the time slider.

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
	•	attribution, license (don’t ship anything without these)
	•	Time: Add either a layer-level time range or per-feature timeProperty (see below).

Optional keys
	•	bounds, minzoom/maxzoom, visible, opacity
	•	legend, style, popup, timeFormat, timePrecision, provenance

Our time-aware UI expects either a global time range (static slice) or a timeProperty on features to filter/animate across years/decades. Keep time metadata precise and machine-parsable; it powers the historical narrative, confidence overlays, and story mode.  ￼  ￼

⸻

Data formats & performance (strongly recommended)
	•	Vectors
	•	Small → GeoJSON
	•	Medium/large or statewide/long-time series → PMTiles (single-file tiles, CDN-friendly)
	•	Rasters
	•	COG (Cloud-Optimized GeoTIFF) with internal overviews; serve via HTTP range requests
	•	XYZ/WMTS can be referenced when hosted elsewhere
	•	DEM
	•	type: "raster-dem" with COG hillshade or terrain tiles as backends

These choices align with the project’s ETL/COG and tiling patterns and keep the viewer fast. Use the pipeline convertors (rio-cogeo, gdal/ogr, tippecanoe/pmtiles) from the Makefile targets.  ￼  ￼

⸻

Time support (how the slider reads your layer)
	1.	Static time window (layer-level)

"time": { "start": "1894-01-01", "end": "1894-12-31" }

Use for a single historic map or a particular survey year.

	2.	Per-feature time (dynamic)

"timeProperty": "year",
"timeFormat": "year",
"timePrecision": "year"

The viewer filters features as the slider moves (e.g., year within current interval). Works for hazard events, rail expansion by year, drought polygons by week, etc.  ￼

When time is approximate (e.g., “spring 1850s”), normalize to a best-effort machine value and (optionally) add a _confidence field for the popup; uncertainty is first-class in the hub.  ￼  ￼

⸻

Categories (suggested)
	•	basemap (terrain/DEM, hillshade, historic topographic sheets)
	•	environment (landcover, soils, vegetation, wetlands)
	•	hazards (tornado tracks, floods, wildfire perimeters, drought polygons)
	•	movement (trails, railroads by year, road milestones)
	•	sovereignty (treaties/reservations, counties by era)
	•	culture (settlements, forts, cemeteries, oral histories, POIs)

These map to UI groupings and storytelling lanes.  ￼  ￼

⸻

Examples (snippets you can copy)

1) Historic topo (raster, single year)

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

Use COG derived from archive MrSID/TIFF; keep datum and georeferencing clean in ETL.  ￼

2) Tornado tracks (vector PMTiles, 1950-present)

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

Source SPC tracks + attributes (date, EF, path); tile and compress for performance.  ￼

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

Weekly shapefiles → PMTiles; slider scrubs week date.  ￼

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

Include year_end and accuracy for uncertainty transparency.  ￼

⸻

Attribution, license, provenance (non-negotiable)
	•	Every layer must declare attribution, license, and a traceable provenance link (STAC item, source descriptor).
	•	When integrating external services (ArcGIS, WMS), mirror the provider’s attribution and terms.
	•	For compiled layers, enumerate source blend and date of synthesis in STAC.
These rules uphold reproducibility and credit, and enable QA back-tracing from the UI to raw inputs.  ￼  ￼

⸻

How to add a new layer (checklist)
	1.	Create/convert data artifact
	•	Vector → GeoJSON (small) or PMTiles (large); Raster → COG.
	•	Normalize to WGS84 (EPSG:4326). Add overviews (COG).  ￼
	2.	STAC + source descriptor
	•	Write a STAC Item under stac/items/ with assets pointing to the artifact (media types: image/tiff; application=geotiff; profile=cloud-optimized, application/vnd.pmtiles).
	•	Ensure bounding box, time extents, licensing, and providers are filled.  ￼
	3.	Author the layer spec
	•	Add a new .layer.json (or append to layers.json) with the schema above.
	•	Include time metadata, category, legend/style, popup fields.
	4.	Validate
	•	Run schema validation & lints (make config-validate, CI hooks) and open the layer locally (dev viewer).
	•	Check attribute names used in popup/timeProperty.  ￼
	5.	Performance sanity
	•	Inspect size & load behavior; tile if necessary; reduce geometry noise; add simplification/overviews.
	6.	Document
	•	Add a short note in web/data/docs/ (edge cases, caveats, uncertainty, source anomalies).

⸻

Conventions & tips
	•	IDs: snake_case, stable, no spaces (used in state & bookmarks).
	•	Fields: keep popup fields concise; consider human vs machine names (ef_scale + EF Scale).
	•	Legends: prefer explicit classes for reproducibility (no magic in code).
	•	Bounds: set to layer bbox; used to auto-zoom when toggled.
	•	Uncertainty: add _confidence or accuracy per feature when relevant; surface in popup.  ￼

⸻

Example categories to prioritize (starter set)
	•	Basemaps: Hillshade/DEM (COG), 1890s–1950s USGS quads (COG)  ￼
	•	Hazards: Tornado tracks (SPC), floods/FEMA declarations, drought (USDM), wildfire perimeters (NIFC)  ￼
	•	Sovereignty: Treaties/reservations, historical counties by year
	•	Movement: Trails, rail buildout by year
	•	Environment: Landcover (NLCD timeslices), soils/SSURGO, wetlands (NWI)
	•	Culture: Forts/settlements by era, cemeteries, oral histories POIs

These layers support the story-forward, time-aware exploration that’s central to the hub’s design.  ￼

⸻

Why this design
	•	Keeps UI configuration declarative & testable and decoupled from data pipelines.
	•	Aligns with open, reproducible geospatial publishing (COG/PMTiles, STAC, explicit legends).
	•	Supports timeline narrative, uncertainty expression, and provenance-centric QA required by the broader KFM architecture.  ￼  ￼

⸻

References (internal)
	•	System/Viewer design (timeline, toggles, story mode): Kansas-Frontier-Matrix Hub Design.  ￼
	•	Design audit (story maps, uncertainty, analytics): Design Audit – Gaps & Enhancements.  ￼
	•	ETL → COG/PMTiles → STAC (archive integration): GIS Archive & Deeds Integration Guide.  ￼
	•	Backend/graph & API contracts (provenance, time): Developer Documentation.  ￼
	•	Hazards & climate datasets (KS-focused catalog): Historical Dataset Integration.  ￼
	•	Knowledge/uncertainty semantics (MCP alignment): Data Resources & MCP.  ￼

⸻

Ready to ship: drop your new .layer.json here, reference data from STAC, pass config-validate, and you’re live in the viewer with time, legends, and popups wired—no code changes needed.
