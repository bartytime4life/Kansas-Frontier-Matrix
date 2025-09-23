# Kansas Geo Timeline — Hillshade COGs

This folder contains **hillshade raster tiles** for the  
**Kansas Geo Timeline / Kansas-Frontier-Matrix** stack.

Hillshade rasters are derived from the **1-m Kansas DEM (2018–2020)** [oai_citation:0‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).  
They provide shaded-relief visualizations of terrain and are published as  
**Cloud-Optimized GeoTIFFs (COGs)** for efficient streaming in GIS and web maps.

---

## Directory Layout

data/cogs/hillshade/
├── ks_hillshade_2018_2020.tif        # main COG
├── ks_hillshade_2018_2020.meta.json  # metadata (extent, CRS, pixel size)
├── ks_hillshade_2018_2020.sha256     # checksum
└── README.md                         # (this file)

---

## Source & Processing

- **Source DEM**: Kansas 1-m bare-earth DEM (2018–2020), published via KS GIS Hub [oai_citation:1‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).  
- **Derivatives**: Processed into hillshade using GDAL’s `gdaldem hillshade`.  
- **CRS**: EPSG:4326 (WGS84) for web distribution; local UTM zones recommended for reprojection.  
- **COG conversion**: Internal tiling, overviews, and DEFLATE compression for fast access.  
- **Checksums**: Every `.tif` has a matching `.sha256` for reproducibility.

---

## Usage

### GIS Desktop
- Open the `.tif` in **QGIS / ArcGIS**.
- Layer blends well with **historic topographic scans** and **vector features** (railroads, trails).

### Web / MapLibre
- Exposed via `app.config.json` → `MapLibre raster` source.
- Tiles auto-stream from the COG (no need to generate XYZ tiles).

Example snippet:

```jsonc
{
  "id": "hillshade",
  "type": "raster",
  "url": "data/cogs/hillshade/ks_hillshade_2018_2020.tif",
  "opacity": 0.6
}


⸻

Integration

Hillshade rasters complement:
	•	Slope / aspect COGs in data/cogs/dem/.
	•	Historic map overlays (data/cogs/overlays/).
	•	Hydrology / soils layers still under integration ￼.

The goal is to provide a time-aware base terrain that underpins both
modern DEMs and historic cartography in the Frontier Matrix system.

⸻

Notes
	•	Resolution: 1 m grid (resampled for web at lower zoom levels).
	•	Extent: Full Kansas coverage.
	•	Limitations: Does not capture vegetation or built environment; terrain only.
	•	Future: Explore integration of county-level LiDAR hillshades (higher res) ￼.

⸻

📌 All rasters here are COGs: directly usable in cloud-native workflows,
STAC-described in stac/items/.

---
