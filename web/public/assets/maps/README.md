<div align="center">

# 🗺️ Kansas Frontier Matrix — Public Map Overlays  
`web/public/assets/maps/`

**Historic Maps · Overlays · Geospatial Rasters**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/public/assets/maps/` directory contains **static geospatial raster and vector overlays**  
used by the **MapView** and **LayerControls** components of the Kansas Frontier Matrix web application.  
These map assets include **historic USGS topographic maps**, **treaty boundary outlines**,  
**hydrology layers**, and other specialized visualizations that support Kansas’s spatial and temporal storytelling.

All map overlays correspond to **STAC Items** defined under `data/stac/`, and are accessible  
through both the **interactive web map** and the **Google Earth export pipeline** (KML/KMZ).

Each raster and vector file in this directory has been optimized for **fast web delivery**,  
georeferenced to **EPSG:4326 (WGS84)**, and compressed for browser rendering via MapLibre GL JS.

---

## 🧱 Directory Structure

```text
web/public/assets/maps/
├── topo_1894_overlay.png          # Historic USGS topographic scan (Larned, 1894)
├── topo_1905_overlay.png          # Historic USGS map (Fort Hays, 1905)
├── treaty_boundaries_outline.svg  # Vector outline of tribal treaty areas
├── hydrology_network_light.svg    # Simplified river and stream network overlay
├── soil_survey_1967.png           # NRCS Soil Survey raster overlay (1967)
├── floodplain_zones_1975.png      # Historical floodplain mapping (Kansas River)
├── drought_index_1936.png         # Dust Bowl drought index visualization
├── legend_treaty.png              # Legend graphic for treaty map
├── legend_topo.png                # Legend for topographic overlay
└── README.md                      # This documentation file


⸻

🧩 Asset Types

File Type	Description	Format	Use Case
Raster Overlay	Georeferenced image (e.g., scanned map, DEM hillshade).	PNG / GeoTIFF	Map background layer
Vector Overlay	Scalable thematic data (boundaries, hydrology).	SVG / GeoJSON	Outline overlays
Legend Image	Supporting graphic for data interpretation.	PNG	LayerControls panel
Composite Map	Blended image combining multiple datasets.	WebP	Base thematic rendering


⸻

🌍 Geospatial Standards
	•	Projection: WGS84 (EPSG:4326)
	•	Resolution: Optimized for 1–10 m/px web zoom levels
	•	Compression: PNG (lossless, 8-bit) or WebP (85% quality)
	•	Tile Size: 256×256 px (for tiled display when applicable)
	•	Alignment: All overlays aligned to the modern Kansas state grid and verified in QGIS

Example metadata (topo_1894_overlay.json):

{
  "id": "topo_1894_overlay",
  "title": "USGS Topographic Map (Larned, 1894)",
  "type": "raster",
  "crs": "EPSG:4326",
  "spatial_extent": [-99.3, 38.1, -98.8, 38.5],
  "temporal_extent": { "start": "1894-01-01", "end": "1894-12-31" },
  "license": "Public Domain",
  "source": "USGS Historical Topographic Map Collection"
}


⸻

🗺️ Example Integration (MapLibre)

map.addSource("topo1894", {
  type: "raster",
  tiles: ["/assets/maps/topo_1894_overlay.png"],
  tileSize: 256
});

map.addLayer({
  id: "topo1894-layer",
  type: "raster",
  source: "topo1894",
  paint: { "raster-opacity": 0.8 }
});

The map overlays are auto-registered in LayerControls from the corresponding STAC metadata.

⸻

🧮 Optimization & Provenance

Tool	Purpose
GDAL	Georeferencing and coordinate reprojection
rio-cogeo	Conversion to Cloud-Optimized GeoTIFFs (COGs)
MapTiler	Tile generation for large rasters
pngquant / cwebp	Raster compression
SVGO	Vector simplification and optimization
SHA256 Checksums	Integrity tracking for all assets

Every overlay includes a checksum (.sha256) and a metadata JSON descriptor
for reproducibility and linkage to its original data source.

⸻

♿ Accessibility and Thematic Design
	•	Colorblind-friendly palettes for maps and legends (tested with Deuteranopia/Protanopia filters).
	•	Descriptive titles and metadata exposed in tooltips and LayerControls.
	•	Legend graphics labeled with large sans-serif fonts (≥ 12pt).
	•	High-contrast outlines ensure visibility on light/dark basemaps.
	•	ARIA labeling for map legends and descriptions when displayed in the UI.

⸻

🧾 Licensing & Attribution

Map Overlay	Source	License	Attribution
topo_1894_overlay.png	USGS Historical Topographic Map Collection	Public Domain	U.S. Geological Survey
treaty_boundaries_outline.svg	Kansas Frontier Matrix (digitized)	CC-BY 4.0	KFM Team
soil_survey_1967.png	USDA NRCS	Public Domain	NRCS Archive
floodplain_zones_1975.png	FEMA Map Archive	Public Domain	FEMA
drought_index_1936.png	NOAA / NCEI	Public Domain	NOAA Data Center
hydrology_network_light.svg	Derived from USGS NHD	CC-BY 4.0	Kansas Frontier Matrix

All derivative work is cited with dataset DOI or repository link in STAC metadata.
Where possible, the overlays are cross-referenced to official open government sources.

⸻

🧪 Validation Workflow (CI/CD)
	•	Validate all map overlays against STAC schema using JSON Schema validator.
	•	Ensure file naming matches dataset IDs in data/stac/items/.
	•	Run checksum comparison to detect changes in underlying rasters.
	•	Generate quick-look previews (128×128 px) for documentation and LayerControls.
	•	Publish validation logs in CI build artifacts for transparency.

⸻

🔗 Related Documentation
	•	LayerControls Component
	•	MapView Component
	•	STAC Catalog Overview
	•	Design Mockups — Map
	•	Web UI Architecture

⸻

📜 License

All map overlays and derivative visualizations created by the
Kansas Frontier Matrix Team are released under the MIT License unless otherwise specified.
Historic maps and datasets sourced from federal archives remain Public Domain.

© 2025 Kansas Frontier Matrix — Produced under the Master Coder Protocol (MCP)
for traceable, reproducible, and educational geospatial visualization.

“Maps are memory etched on the land — these overlays reveal Kansas’s stories through time and terrain.”

