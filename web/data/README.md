Kansas-Frontier-Matrix — Web Data

This folder contains layer configs and map data references used by the web viewer (web/).
Each *.json here is either:
	•	a layer spec (id, title, type, style, time, attribution) the viewer reads, or
	•	a data file (GeoJSON/JSON/COG references) used by that layer.

This directory is the bridge between archival data (STAC, COGs, GeoJSON) and the interactive map UI.

⸻

How Layers Work (Schema)

Your configs should conform to web/config/layers.schema.json (validated in CI).
Minimal canonical shape:

{
  "id": "unique_layer_id",
  "title": "Layer Title",
  "type": "vector | raster | image | raster-dem",
  "format": "geojson | xyz | cog | pmtiles",
  "data": "web/data/<file>.geojson | .json | data/processed/<artifact>.tif",
  "category": "reference | environment | hazards | movement | sovereignty | culture",
  "time": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD or null" },
  "timeProperty": "feature field (e.g., 'year' or 'active')",
  "popup": ["field1", "field2"],
  "style": {},
  "visible": true,
  "attribution": "Source / License"
}

Notes
	•	Time supports global windows or per-feature year / year_end (or similar).
	•	Vectors are GeoJSON (typed properties).
	•	Rasters are typically COGs (Cloud-Optimized GeoTIFFs) or XYZ tiles.
	•	UI is driven by app.js, which reads these configs, applies the time slider, and attaches popups.

⸻

Quick Templates (copy-paste)

Vector (GeoJSON points)

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
  "attribution": "Curated from territorial gazetteers",
  "license": "CC-BY-4.0",
  "connections": {
    "stac_item": "stac/items/towns.json",
    "related_layers": ["web/data/railroads.json"]
  }
}

Raster (XYZ basemap)

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


⸻

Connections (wiring to STAC & siblings)

Each layer can declare helpful cross-links:

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

	•	stac_item: canonical metadata/provenance entry.
	•	related_layers: peer configs to toggle in the UI.
	•	preferred_overlay_order: draw order guidance for the viewer.

⸻

Complete File Index

Reference & Base
	•	basemap.json — Basemap configuration (OSM or other).
	•	counties.json — Kansas county boundaries (static).
	•	counties_timeslices.json — Historical county slices (time-aware).
	•	kansas_counties.geojson — Raw county geometries.
	•	elevation.json — DEM/terrain layers and derivatives.
	•	plss_sections.json — PLSS township/section index.
	•	historic_parcels.json — Historic parcels / deeds.

Environment & Climate
	•	climate_normals.json — Climate normals (layer spec).
	•	climate_normals_ks.json — Climate normals (Kansas FeatureCollection).
	•	drought.json — Drought indices.
	•	drought_weekly.json — Weekly drought snapshots.
	•	soil_surveys.json — Soil survey data.
	•	hydrology.json — Rivers, streams, and waterbodies.
	•	landcover.json — Land cover (spec).
	•	landcover_timeslices.json — NLCD time slices (1992–2021).

Hazards
	•	fema_disasters.json / fema_disasters_ks.json
	•	storm_events.json / storm_events_ks.json
	•	tornado_tracks.json / tornado_tracks_ks.json
	•	wildfire_perimeters.json

Movement & Infrastructure
	•	railroads.json / railroads_lines.json
	•	trails.json / trails_lines.json
	•	usgs_topo.json — Historic topo COG overlays.

Sovereignty & Treaties
	•	treaties.json — Layer spec.
	•	treaties_polygons.json — Treaty/reservation polygons (GeoJSON).

Culture, Documents & Stories
	•	oral_histories.json / oral_histories_points.json
	•	documents.json / documents_points.json
	•	stories.json

Towns & Demo
	•	towns.json / towns_points.json
	•	demo_entities.json / demo_events.json
	•	timeline.json — Global timeline feed.

Cartography Tokens
	•	legend.json — Central symbol/color definitions.
	•	style_tokens.json — Shared UI/cartography tokens.

⸻

Data Flow Overview

flowchart TD
  A["STAC Items\n(stac/items/*.json)"] --> B["Processed Data\n(data/processed/*.json|.geojson|.tif)"]
  B --> C["Layer Configs\n(web/data/*.json)"]
  C --> D["Web Viewer Logic\n(web/app.js)"]
  D --> E["MapLibre UI\n(Time Slider, Sidebar, Popups)"]

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


⸻

Thematic Organization of Files

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
    railroads["railroads.json"]
    railroads_lines["railroads_lines.json"]
    trails["trails.json"]
    trails_lines["trails_lines.json"]
    usgs_topo["usgs_topo.json"]
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

Conventions & QA
	•	Keep configs lean; heavy data belongs in data/processed/ and is referenced via STAC.
	•	Reuse colors/widths from legend.json and tokens from style_tokens.json.
	•	Always include attribution and, when possible, license and provenance.
	•	Add connections.stac_item for authoritative metadata; use related_layers for UX.

Validation (before commit)

# JSON sanity
jq . web/data/*.json >/dev/null

# Repo tests (if configured)
pytest -k web_configs

# Schema check (example)
python -m scripts.validate_config web/data --schema web/config/layers.schema.json

Common Pitfalls
	•	Comments in JSON: Don’t use // or /* */.
	•	Bounds: Use Web Mercator vertical limit ±85.0511 when global.
	•	Paths: Prefer web/data/... or data/processed/... consistently.
	•	Time: If per-feature dates exist, set timeProperty (e.g., year, year_end).

⸻

📌 Key concept: web/data/ is the UI wiring layer—it translates structured archives (STAC, processed GeoJSON/COGs) into an interactive timeline + map experience with clear provenance and reproducibility.
