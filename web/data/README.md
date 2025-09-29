Kansas-Frontier-Matrix — web/data/ (Rebuilt)

This folder is the UI wiring layer between our archival assets (STAC, COGs, GeoJSON, PMTiles) and the interactive MapLibre/Google-Earth viewer. Each JSON file here is either:
	•	a layer spec the viewer reads (id, title, type, format, time, style, attribution), or
	•	a data file (GeoJSON/JSON/PMTiles/COG references) used by that layer.

Design goals: compact, explicit, time-aware, and reproducible across CI and local dev.

⸻

How layers work (contract)

All layer JSONs must validate against web/config/layers.schema.json in CI. Minimal canonical shape:

{
  "id": "unique_layer_id",
  "title": "Layer Title",
  "type": "vector | raster | image | raster-dem",
  "format": "geojson | pmtiles | cog | xyz | image",
  "data": "web/data/<file>.geojson | data/processed/<artifact>.pmtiles | data/cogs/<raster>.tif",
  "category": "reference | environment | hazards | movement | sovereignty | culture",
  "time": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD or null" },
  "timeProperty": "per-feature date field (e.g., 'year' or 'valid_from')",
  "popup": ["field1", "field2"],
  "style": {},
  "visible": false,
  "attribution": "Source / License"
}

Notes
	•	Time can be global via time.start/end or per-feature via timeProperty (e.g., year, year_end).
	•	Vectors are typically GeoJSON (UTF-8, WGS84). Heavy vectors should use PMTiles.
	•	Rasters are COGs or XYZ; DEMs are raster-dem.
	•	The viewer (MapLibre + app code) reads these specs, applies the time slider, and attaches popups.

⸻

Quick templates

1) Vector (GeoJSON points)

{
  "id": "towns",
  "title": "Towns & Posts",
  "type": "vector",
  "format": "geojson",
  "data": "web/data/towns_points.geojson",
  "category": "reference",
  "time": { "start": null, "end": null },
  "minzoom": 5,
  "maxzoom": 19,
  "visible": false,
  "popup": ["name", "year_founded", "source"],
  "style": {
    "renderer": "circle",
    "circleColor": "#1f77b4",
    "circleRadius": 4,
    "circleStrokeColor": "#ffffff",
    "circleStrokeWidth": 0.6
  },
  "attribution": "Curated frontier gazetteers (see STAC item)",
  "license": "CC-BY-4.0",
  "connections": {
    "stac_item": "stac/items/towns.json",
    "related_layers": ["web/data/railroads.json"]
  }
}

2) Raster (XYZ basemap)

{
  "id": "basemap_osm",
  "title": "Basemap — OpenStreetMap (Standard)",
  "type": "raster",
  "format": "xyz",
  "tile_format": "png",
  "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
  "category": "reference",
  "time": { "start": null, "end": null },
  "bounds": [-180.0, -85.0511, 180.0, 85.0511],
  "minzoom": 0,
  "maxzoom": 19,
  "tileSize": 256,
  "visible": true,
  "opacity": 1.0,
  "style": { "renderer": "raster", "rasterOpacity": 1.0 },
  "attribution": "© OpenStreetMap contributors",
  "license": "ODbL-1.0"
}

3) Raster overlay (COG)

{
  "id": "ks_hillshade",
  "title": "Hillshade (LiDAR 1 m)",
  "type": "raster",
  "format": "cog",
  "data": "data/cogs/overlays/ks_lidar_hillshade.tif",
  "category": "reference",
  "time": { "start": null, "end": null },
  "minzoom": 5,
  "maxzoom": 18,
  "visible": false,
  "opacity": 0.7,
  "style": { "renderer": "raster", "rasterOpacity": 0.7 },
  "attribution": "KARS / USGS 3DEP (public domain)",
  "license": "Public Domain",
  "connections": {
    "stac_item": "stac/items/ks_hillshade.json"
  }
}

Use COG/GeoJSON/PMTiles to stay fast and web-friendly; convert upstream with the ETL recipes (COG via rio-cogeo, vectors to GeoJSON, or PMTiles for large sets).

⸻

Connections (wiring to STAC & siblings)

{
  "connections": {
    "stac_item": "stac/items/<layer>.json",
    "related_layers": [
      "web/data/hillshade.json",
      "web/data/landcover.json"
    ],
    "preferred_overlay_order": ["hillshade", "contours", "terrain", "landcover"]
  }
}

	•	stac_item: authoritative metadata/provenance.
	•	related_layers: peer configs to toggle together.
	•	preferred_overlay_order: viewer draw-order guidance.
Tie every map layer to a STAC Item for provenance and reproducibility in CI.

⸻

Complete file index (suggested baseline)

Reference & Base
	•	basemap.json — Basemap configuration(s)
	•	counties.json — Kansas county boundaries (static)
	•	counties_timeslices.json — Historical county slices (time-aware)
	•	kansas_counties.geojson — County geometries (data)
	•	elevation.json — DEM/terrain layers & derivatives
	•	plss_sections.json — PLSS township/section index
	•	historic_parcels.json — Historic parcels/deeds overview

Environment & Climate
	•	climate_normals.json — Layer spec for normals
	•	climate_normals_ks.json — Kansas stations FC
	•	drought.json / drought_weekly.json — U.S. Drought Monitor (weekly time slices)
	•	soil_surveys.json — SSURGO/STATSGO references
	•	hydrology.json — Rivers, streams, waterbodies
	•	landcover.json — NLCD specs
	•	landcover_timeslices.json — NLCD 1992–2021 snapshots

Hazards
	•	fema_disasters.json / _ks.json
	•	storm_events.json / _ks.json
	•	tornado_tracks.json / _ks.json
	•	wildfire_perimeters.json

Movement & Infrastructure
	•	railroads.json / railroads_lines.json
	•	trails.json / trails_lines.json
	•	usgs_topo.json — Historic topo COG/tiles

Sovereignty & Treaties
	•	treaties.json — Layer spec
	•	treaties_polygons.json — Treaty/reservation polygons (GeoJSON)

Culture, Documents & Stories
	•	oral_histories.json / _points.json
	•	documents.json / _points.json
	•	stories.json

Towns & Demo
	•	towns.json / towns_points.json
	•	demo_entities.json / demo_events.json
	•	timeline.json — Global timeline feed

Cartography Tokens
	•	legend.json — Central symbology
	•	style_tokens.json — Shared UI tokens

Hazard, drought, tornado, FEMA, and wildfire layers should point to official sources (NCEI Storm Events, SPC GIS, FEMA OpenFEMA, USDM, NIFC), time-indexed for the slider.

⸻

Data flow (visual)

flowchart TD
  A["STAC Items\n(stac/items/*.json)"] --> B["Processed Data\n(data/processed/*.json|.geojson|.pmtiles|.tif)"]
  B --> C["Layer Configs\n(web/data/*.json)"]
  C --> D["Web Viewer Logic\n(web/app.js)"]
  D --> E["MapLibre UI\n(Time Slider,\nSidebar,\nPopups)"]

  classDef stac fill:#FFD166,stroke:#333,stroke-width:1px;
  classDef processed fill:#06D6A0,stroke:#333,stroke-width:1px;
  classDef webdata fill:#118AB2,stroke:#fff,stroke-width:1px;
  classDef viewer fill:#073B4C,stroke:#fff,stroke-width:1px;
  classDef ui fill:#EF476F,stroke:#fff,stroke-width:1px;

  class A stac;
  class B processed;
  class C webdata;
  class D viewer;
  class E ui;

The pipeline is STAC-first, ETL generates COG/PMTiles/GeoJSON, layer JSONs reference those artifacts, and the viewer composes time-aware maps.

⸻

Thematic organization (visual)

flowchart LR
  subgraph Ref["Reference & Base"]
    basemap["basemap.json"]
    counties["counties.json"]
    counties_ts["counties_timeslices.json"]
    kc_geo["kansas_counties.geojson"]
    elevation["elevation.json"]
    plss["plss_sections.json"]
    parcels["historic_parcels.json"]
  end
  subgraph Env["Environment & Climate"]
    climate_normals["climate_normals.json"]
    climate_normals_ks["climate_normals_ks.json"]
    drought["drought.json"]
    drought_weekly["drought_weekly.json"]
    soils["soil_surveys.json"]
    hydro["hydrology.json"]
    landcover["landcover.json"]
    landcover_ts["landcover_timeslices.json"]
  end
  subgraph Haz["Hazards"]
    fema["fema_disasters.json"]
    fema_ks["fema_disasters_ks.json"]
    storm["storm_events.json"]
    storm_ks["storm_events_ks.json"]
    tornado["tornado_tracks.json"]
    tornado_ks["tornado_tracks_ks.json"]
    wildfire["wildfire_perimeters.json"]
  end
  subgraph Move["Movement & Infrastructure"]
    rail["railroads.json"]
    rail_lines["railroads_lines.json"]
    trails["trails.json"]
    trails_lines["trails_lines.json"]
    topo["usgs_topo.json"]
  end
  subgraph Sov["Sovereignty & Treaties"]
    treaties["treaties.json"]
    treaties_poly["treaties_polygons.json"]
  end
  subgraph Cult["Culture, Docs & Stories"]
    oral["oral_histories.json"]
    oral_pts["oral_histories_points.json"]
    docs["documents.json"]
    docs_pts["documents_points.json"]
    stories["stories.json"]
  end
  subgraph Demo["Towns & Demo"]
    towns["towns.json"]
    towns_pts["towns_points.json"]
    demo_entities["demo_entities.json"]
    demo_events["demo_events.json"]
    timeline["timeline.json"]
  end
  subgraph Carto["Cartography Tokens"]
    legend["legend.json"]
    style_tokens["style_tokens.json"]
  end


⸻

Conventions
	•	Keep configs lean; heavy geometry and rasters live under data/processed/ or data/cogs/, with STAC pointing to originals, checksums, and lineage.
	•	Reuse legend colors and style_tokens for consistency.
	•	Always include attribution, license, and provenance (as connections.stac_item).
	•	Prefer PMTiles for large vectors; COGs for rasters; WGS84 (EPSG:4326) throughout the web stack.
	•	Time semantics: if features have year or valid_from/valid_to, set timeProperty and keep global time for layer’s overall extent.

⸻

Validation & QA

JSON sanity

jq . web/data/*.json >/dev/null

Schema check

python -m scripts.validate_config web/data --schema web/config/layers.schema.json

Repo tests (if configured)

pytest -k web_configs

Common pitfalls
	•	JSON comments: don’t use // or /* */.
	•	Bounds: global rasters must respect Web-Mercator vertical limit ±85.0511.
	•	Paths: use web/data/..., data/processed/..., or data/cogs/... consistently.
	•	Time: set either global time or timeProperty (or both) appropriately; don’t contradict STAC item dates.

⸻

Ingest & formats (field-ready tips)
	•	Convert rasters to COG (rio cogeo create … --web-optimized) and vectors to GeoJSON (or PMTiles) in WGS84.
	•	When sourcing historic maps (MrSID, scanned PDFs), georeference to GeoTIFF, then COG; record year for the time slider; index sheets in STAC.
	•	For hazards and climate:
	•	NCEI Storm Events (CSV by state/year) for multi-hazard timelines,
	•	SPC Tornado/Hail/Wind GIS for paths/points (annual rolls),
	•	US Drought Monitor weekly polygons (shp/geojson/WMS),
	•	NIFC wildfire perimeters (2000+) and KFS state perimeters.
Attach each to STAC, then wire a lean layer JSON here.

⸻

Why this shape?
	•	It keeps the viewer config small and declarative, while STAC carries full lineage and licensing.
	•	It aligns with our ETL/AI + graph + viewer architecture and CI reproducibility targets.
	•	It leaves room for analytics (time-aware hazards, climate, sovereignty layers) without bloating the UI config.

⸻

References (project design & ingestion guides):
Architecture & viewer contract  • Integration gaps & analytics focus  • GIS archive ingestion & formats (COG/GeoJSON/PMTiles)  • Hazard/climate datasets and timelines
