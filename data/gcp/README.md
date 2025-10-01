<div align="center">

# 📍 Kansas-Frontier-Matrix — Ground Control Points (GCP)  
`data/gcp/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Store and maintain **Ground Control Points (GCPs)** and tie point files  
for georeferencing scanned maps, aerial photos, and historic imagery  
in the **Kansas Frontier Matrix**.  

GCPs transform **raw historical scans** into spatially referenced layers  
(GeoTIFFs / COGs) that align with modern coordinate systems.  
They are essential for **accuracy, reproducibility, and cross-dataset integration**.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw scans\n(data/raw/maps/**)"] --> B["Ground Control Points\n(data/gcp/**)"]
  B --> C["Rectified rasters\n(make rectified / gdalwarp)"]
  C --> D["COGs / Overlays\n(data/cogs/overlays/**)"]
  D --> E["STAC Items\n(stac/items/topo | plat)"]
  E --> F["Validate\n(stac-validate)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Provide documented control points for georeferencing historic imagery.
	•	Support reproducible workflows → every rectified map cites its GCP file.
	•	Enable cross-checking accuracy (residuals, RMS error stats).
	•	Maintain an archive of stable reference features (PLSS corners, survey benchmarks, river confluences).
	•	Link GCPs to STAC items for provenance and time-aware usage.

⸻

📂 Directory Layout

data/gcp/
├── README.md
├── kansas_topos/           # topo map GCPs
│   ├── 1894_ellsworth.gcp
│   └── 1937_salina.gcp
├── aerials/                # aerial photo GCPs (1930s–1950s)
├── plats/                  # county plat/cadastral sheets
└── shared_benchmarks.json  # common PLSS corners & benchmarks


⸻

🗂️ File Formats

Plaintext (.gcp) — GDAL/QGIS convention:

pixel_x, pixel_y, lon, lat
1340, 2250, -98.1234, 38.7654
2075,  310, -98.2000, 38.8901

GeoJSON (.geojson) — structured points with metadata:

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Point", "coordinates": [-98.1234, 38.7654] },
      "properties": { "pixel": [1340,2250], "map": "Ellsworth 1894" }
    }
  ]
}

Other formats:
	•	CSV (.csv) → bulk import/export.
	•	JSON (.json) → structured sets, often linked to STAC metadata.

Each file should include:
	•	Source scan name + date
	•	Target CRS (EPSG:4326 or EPSG:3857 typical)
	•	Number of points + RMS error
	•	Notes on feature choice (e.g., “church spire”, “railroad junction”)

⸻

📑 Example STAC Item (Rectified Topo Map with GCP Reference)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "topo_ellsworth_1894_rectified",
  "properties": {
    "title": "Ellsworth County Topo Map (1894, rectified)",
    "description": "Georeferenced 1894 Ellsworth topo sheet using documented GCPs.",
    "datetime": "1894-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "gdalwarp polynomial warp (order=2)",
    "kfm:lineage": [
      "data/raw/maps/topos/1894_ellsworth_scan.tif",
      "data/gcp/kansas_topos/1894_ellsworth.gcp"
    ],
    "qa:rms_error": 3.2,
    "qa:status": "verified"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-99.0, 38.5],
      [-99.0, 39.0],
      [-98.0, 39.0],
      [-98.0, 38.5],
      [-99.0, 38.5]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/topo.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../../data/cogs/overlays/topos/1894_ellsworth_rectified.tif",
      "title": "Rectified Topo Map (Ellsworth 1894)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    },
    "gcp": {
      "href": "../../../data/gcp/kansas_topos/1894_ellsworth.gcp",
      "title": "Ground Control Points (Ellsworth 1894)",
      "type": "text/plain",
      "roles": ["metadata", "provenance"]
    }
  }
}


⸻

📑 GCP Templates

Template .gcp file

# Example GCP file (GDAL/QGIS format)
# pixel_x, pixel_y, lon, lat
100, 200, -98.5000, 38.8000
500, 800, -98.7000, 38.9500
900, 1200, -98.6000, 38.7000
1200, 1500, -98.8000, 38.8500

Equivalent GeoJSON representation

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Point", "coordinates": [-98.5000, 38.8000] },
      "properties": { "pixel": [100,200], "map": "Example Map" }
    },
    {
      "type": "Feature",
      "geometry": { "type": "Point", "coordinates": [-98.7000, 38.9500] },
      "properties": { "pixel": [500,800], "map": "Example Map" }
    }
  ]
}


⸻

🔗 Integration
	•	Referenced in data/sources/*.json descriptors for scanned maps.
	•	Consumed by make rectified / make cogs to warp rasters.
	•	Residuals & errors logged in provenance sidecars.
	•	Cited by STAC items (stac/items/topo/, stac/items/plat/).

⸻

📝 Notes
	•	Prefer stable features (river confluences, PLSS intersections) over transient ones (fence lines).
	•	Include at least 4–6 well-spread points; more improves warp accuracy.
	•	Store raw + refined versions if iterative corrections are made.
	•	Follow MCP reproducibility → every georeferencing step must cite the exact GCP file used.

⸻

📚 See Also
	•	data/earth/sources/README.md → global basemaps for alignment checks.
	•	data/cogs/overlays/README.md → raster overlays generated after rectification.
	•	stac/items/ → STAC metadata linking imagery to its GCPs.

⸻

✅ Mission Principle

GCPs must be archived, cited, and reproducible.
No georeferenced map is valid without its documented GCP inputs.