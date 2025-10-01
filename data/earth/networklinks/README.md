<div align="center">

# 🌐 Kansas-Frontier-Matrix — Earth Network Links  
`data/earth/networklinks/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Document **network-linked Earth datasets** consumed by the Frontier Matrix.  

Unlike `data/earth/sources/` (static file descriptors),  
this directory catalogs **remote or live feeds** accessed directly over the network:  

- 🛰️ OGC services (WMS, WMTS, WCS, WFS)  
- 🔗 ArcGIS REST endpoints (ImageServer / FeatureServer)  
- 🗺️ Tiled basemaps (XYZ, PMTiles, TileJSON)  
- ⚠️ Live hazard feeds (NASA FIRMS, USGS ShakeMap, NOAA storm tracks)  

These provide **dynamic Earth context layers** — global basemaps, live environmental data, and hazard overlays —  
for use in the MapLibre viewer and GIS workflows, without storing bulky rasters/vectors locally.  

</div>

---

## 📈 Lifecycle

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
	•	Allow the web viewer to consume near real-time feeds (hazards, climate, time-aware overlays).
	•	Complement Kansas static layers with planetary context.
	•	Document provenance and endpoints for scientific reproducibility (MCP).

⸻

📂 Directory Layout

data/earth/networklinks/
├── basemaps.json    # Global basemaps (Blue Marble, Natural Earth, OSM)
├── climate.json     # Live climate & reanalysis feeds (NOAA, Copernicus, ERA5 APIs)
├── hazards.json     # Earthquake, wildfire, storm feeds (USGS, NASA FIRMS, NOAA SPC)
├── tectonics.json   # Faults, seismic hazard services (USGS, GEM, OneGeology)
├── water.json       # Hydrography, oceans, wetlands (HydroSHEDS, NHDPlus HR)
└── README.md

	•	Each .json follows the networklinks.schema.json.
	•	Defines service type, endpoint, layers, attribution, and license.

⸻

🌍 Example Network Links

Basemaps
	•	NASA Blue Marble / GIBS → WMTS mosaics.
	•	Natural Earth → PMTiles / XYZ tiles.
	•	OpenStreetMap → XYZ or WMTS basemaps.

Climate
	•	Copernicus ERA5 → global reanalysis API.
	•	NASA Daymet WCS → 1 km daily climate (North America).
	•	WorldClim WMS → long-term climate normals.

Hazards
	•	NASA FIRMS → live wildfire detections (WMS/GeoJSON).
	•	USGS ShakeMap & Earthquake Feeds → global seismic events.
	•	NOAA SPC → tornado & severe weather tracks.

Tectonics
	•	USGS Global Faults WMS.
	•	GEM Seismic Hazard Map → raster hazard intensity.
	•	OneGeology → lithology & tectonic services.

Water
	•	HydroSHEDS → global rivers/basins (WMS/WFS).
	•	NHDPlus HR (USGS) → ArcGIS REST high-resolution hydrography.
	•	NASA OceanColor / MODIS Aqua → WMS services.

⸻

🛠️ Integration

Schema example for a network link descriptor (hazards.json entry):

{
  "id": "nasa_firms_fires",
  "title": "NASA FIRMS — Active Fire Data",
  "type": "wms",
  "endpoint": "https://firms.modaps.eosdis.nasa.gov/wms/",
  "layers": ["fires_viirs"],
  "attribution": "NASA FIRMS",
  "license": "Free and open (NASA EarthData policy)"
}

	•	.json descriptors are consumed by the web viewer alongside local layers.
	•	STAC Items in stac/items/earth/ may reference network services instead of local files.

⸻

📑 Example STAC Item (NASA FIRMS — Active Fire WMS)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "earth_firms_fire_wms",
  "properties": {
    "title": "NASA FIRMS — Active Fire Data (WMS)",
    "description": "Near real-time global fire detections from NASA FIRMS, exposed as an OGC WMS feed.",
    "start_datetime": "2025-09-01T00:00:00Z",
    "end_datetime": null,
    "kfm:method": "WMS service consumption",
    "kfm:lineage": [
      "https://firms.modaps.eosdis.nasa.gov/wms/"
    ],
    "qa:status": "live"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-180, -90],
      [-180, 90],
      [180, 90],
      [180, -90],
      [-180, -90]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/earth.json"
    }
  ],
  "assets": {
    "wms": {
      "href": "https://firms.modaps.eosdis.nasa.gov/wms/",
      "title": "NASA FIRMS Active Fire (WMS)",
      "type": "application/xml",
      "roles": ["data", "service"]
    }
  }
}


⸻

📝 Notes

Use network links when:
	•	Data is too large to store locally.
	•	Dataset updates frequently (e.g., real-time hazards).
	•	Provider is authoritative and persistent.

Always record:
	•	Service URL + layer name(s).
	•	Access date (if snapshot taken).
	•	License / usage constraints.

⸻

📚 See Also
	•	data/earth/sources/README.md → static Earth datasets.
	•	data/stac/README.md → STAC catalog & item registry.
	•	docs/ → MCP guides on reproducibility and experiment logging.

⸻

✅ Mission Principle

Network links must be documented, reproducible, and STAC-referenced.
If a service can’t be validated or cited, it doesn’t belong here.