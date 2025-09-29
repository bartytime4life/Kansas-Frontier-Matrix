# Kansas-Frontier-Matrix — Earth Network Links

This directory contains **network-linked Earth datasets** used by the Kansas Frontier Matrix.  
Whereas `data/earth/sources/` lists **static source descriptors** (files, COGs, GeoJSON),  
this directory documents **remote or live feeds** that can be consumed directly via network links:  

- 🌐 **OGC services** (WMS, WMTS, WCS, WFS)  
- 🔗 **ArcGIS REST endpoints** (ImageServer / FeatureServer)  
- 📡 **Tiled basemaps** (XYZ, PMTiles, TileJSON)  
- 🛰️ **Live hazard feeds** (NASA FIRMS, USGS ShakeMap, NOAA storm tracks)  

These links provide **dynamic Earth context layers** — global basemaps, live environmental data, and hazard overlays —  
which can be pulled into the web viewer or into GIS workflows without storing large raster/vector files locally.

---

## Purpose

- Supply **global Earth reference data** via remote services.  
- Allow the **web viewer** to connect directly to live feeds (time-aware layers, hazards).  
- Complement Kansas-specific static datasets with **planetary context**.  
- Document provenance and service endpoints for **reproducibility** [oai_citation:0‡Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf](file-service://file-XygDDSfCPa5gz3jmjRV81b) [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).  

---

## Directory Layout

data/earth/networklinks/
├── basemaps.json        # Global basemaps (Blue Marble, Natural Earth, OSM, etc.)
├── climate.json         # Live climate & reanalysis feeds (NOAA, Copernicus, ERA5 APIs)
├── hazards.json         # Earthquake, wildfire, storm feeds (USGS, NASA FIRMS, NOAA SPC)
├── tectonics.json       # Global faults, seismic hazard services (USGS, GEM, OneGeology)
├── water.json           # Global hydrography, oceans, wetlands (HydroSHEDS, NHDPlus HR WMS)
└── README.md            # This file

---

## Example Network Links

### 🌍 Basemaps
- **NASA Blue Marble / GIBS** — WMTS service, monthly global mosaics.  
- **Natural Earth tiles** — PMTiles or XYZ raster tiles.  
- **OpenStreetMap (OSM)** — XYZ/WMTS basemap.  

### 🌡️ Climate
- **Copernicus ERA5 (ECMWF)** — API for global reanalysis.  
- **NASA Daymet WCS** — 1 km daily climate for North America [oai_citation:2‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).  
- **WorldClim WMS** — long-term climate normals.  

### ⚠️ Hazards
- **NASA FIRMS Fire Data** — live wildfire detections (WMS/GeoJSON feed).  
- **USGS ShakeMap / Earthquake Feeds** — global seismic events (GeoJSON/WMS).  
- **NOAA SPC Tornado / Severe Weather Tracks** — GIS endpoints [oai_citation:3‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).  

### 🌐 Tectonics
- **USGS Global Faults WMS**.  
- **GEM Seismic Hazard Map** — global raster hazard intensity.  
- **OneGeology services** — lithology and tectonic frameworks.  

### 🌊 Water
- **HydroSHEDS (WWF)** — rivers/basins (WMS/WFS).  
- **NHDPlus HR (USGS)** — high-resolution hydrography, ArcGIS REST.  
- **NASA OceanColor / MODIS Aqua** — WMS services.  

---

## Integration

- Each `.json` descriptor follows the **networklinks schema**:  
  ```json
  {
    "id": "fao_globallandcover",
    "title": "FAO Global Land Cover WMS",
    "type": "wms",
    "endpoint": "https://example.org/geoserver/wms",
    "layers": ["landcover:global"],
    "attribution": "FAO / UN",
    "license": "CC-BY-4.0"
  }

	•	These descriptors can be loaded by the web viewer alongside local sources.
	•	STAC items in stac/items/earth/ may reference these network links instead of local assets ￼.

⸻

Notes
	•	Use network links when:
	•	Data volume is too large to host locally.
	•	A dataset is updated frequently (e.g., near real-time hazards).
	•	The provider’s service is authoritative and persistent.
	•	For reproducibility, always record:
	•	Service URL and layer name(s).
	•	Access date (if snapshots are taken).
	•	License/usage constraints.

⸻

See Also
	•	data/earth/sources/README.md — static global Earth datasets.
	•	data/stac/README.md — STAC catalog and how network links fit into the item model.
	•	docs/ — MCP documentation on reproducibility and experiment logging.

---