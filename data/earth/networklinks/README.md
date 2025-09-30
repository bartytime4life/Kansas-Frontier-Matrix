<div align="center">

# 🌐 Kansas Geo Timeline — Earth Network Links

**Network-linked Earth datasets** used by the **Kansas Frontier Matrix**.  

Unlike `data/earth/sources/` (static file descriptors),  
this directory documents **remote or live feeds** consumed directly via network links:  

- 🛰️ OGC services (WMS, WMTS, WCS, WFS)  
- 🔗 ArcGIS REST endpoints (ImageServer / FeatureServer)  
- 🗺️ Tiled basemaps (XYZ, PMTiles, TileJSON)  
- ⚠️ Live hazard feeds (NASA FIRMS, USGS ShakeMap, NOAA storm tracks)  

These provide **dynamic Earth context layers** — global basemaps, live environmental data, and hazard overlays —  
for use in the MapLibre viewer and GIS workflows, without storing bulky rasters/vectors locally.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Network services\n(WMS · WMTS · WCS · REST)"] --> B["JSON descriptors\n(data/earth/networklinks/*.json)"]
  B --> C["Web Viewer\n(live overlays)"]
  B --> D["STAC Items\n(stac/items/earth)"]
  D --> E["Validate\n(stac-validate)"]
  E --> F["Reproducible provenance\n(MCP logging)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Provide global Earth reference data via live services.
	•	Allow the web viewer to consume near real-time feeds (hazards, time-aware climate).
	•	Complement Kansas-specific static layers with planetary context.
	•	Document provenance and endpoints for reproducibility  .

⸻

📂 Directory layout

data/earth/networklinks/
├── basemaps.json    # Global basemaps (Blue Marble, Natural Earth, OSM)
├── climate.json     # Live climate & reanalysis feeds (NOAA, Copernicus, ERA5 APIs)
├── hazards.json     # Earthquake, wildfire, storm feeds (USGS, NASA FIRMS, NOAA SPC)
├── tectonics.json   # Faults, seismic hazard services (USGS, GEM, OneGeology)
├── water.json       # Hydrography, oceans, wetlands (HydroSHEDS, NHDPlus HR)
└── README.md

Each .json file lists services following the networklinks schema.

⸻

🌍 Example network links

Basemaps
	•	NASA Blue Marble / GIBS — WMTS mosaics.
	•	Natural Earth tiles — PMTiles / XYZ raster tiles.
	•	OpenStreetMap — XYZ or WMTS basemap.

Climate
	•	Copernicus ERA5 — global reanalysis API.
	•	NASA Daymet WCS — 1 km daily climate for North America .
	•	WorldClim WMS — long-term climate normals.

Hazards
	•	NASA FIRMS Fire Data — live wildfire detections (WMS/GeoJSON).
	•	USGS ShakeMap / Earthquake Feeds — global seismic events.
	•	NOAA SPC Tornado & Severe Weather Tracks — GIS endpoints .

Tectonics
	•	USGS Global Faults WMS.
	•	GEM Seismic Hazard Map — global raster hazard intensity.
	•	OneGeology — lithology & tectonic services.

Water
	•	HydroSHEDS — global rivers/basins (WMS/WFS).
	•	NHDPlus HR (USGS) — high-resolution hydrography, ArcGIS REST.
	•	NASA OceanColor / MODIS Aqua — WMS services.

⸻

🛠️ Integration

Schema example:

{
  "id": "fao_globallandcover",
  "title": "FAO Global Land Cover WMS",
  "type": "wms",
  "endpoint": "https://example.org/geoserver/wms",
  "layers": ["landcover:global"],
  "attribution": "FAO / UN",
  "license": "CC-BY-4.0"
}

	•	These .json descriptors are consumed by the web viewer alongside local layers.
	•	STAC Items in stac/items/earth/ may reference network links instead of local files.

⸻

📝 Notes

Use network links when:
	•	Data volume is too large to host locally.
	•	Dataset updates frequently (e.g. real-time hazards).
	•	Provider service is authoritative and persistent.

Always record:
	•	Service URL + layer name(s).
	•	Access date (if snapshot taken).
	•	License / usage constraints.

⸻

📚 See also
	•	data/earth/sources/README.md — static Earth datasets.
	•	data/stac/README.md — STAC catalog & item model.
	•	docs/ — MCP guides on reproducibility and experiment logging.

⸻

✅ Mission-grade principle: Network links must be documented, reproducible, and STAC-referenced.
If the service can’t be validated or cited, it doesn’t belong here.

