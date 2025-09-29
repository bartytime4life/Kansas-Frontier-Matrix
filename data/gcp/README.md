# Kansas-Frontier-Matrix — Ground Control Points (GCP)

This directory stores **Ground Control Points (GCPs)** and related tie point files  
used to georeference scanned maps, aerial photos, and other imagery in the  
Kansas Frontier Matrix.  

GCPs are the foundation for turning **raw historical scans** into spatially  
referenced layers (GeoTIFFs / COGs) that align with modern coordinate systems.  
They are essential for reproducibility, accuracy, and integration across  
historical datasets.

---

## Purpose

- Provide **documented control points** for georeferencing historic imagery.  
- Support reproducible workflows: every rectified map cites its GCP file.  
- Enable **cross-checking accuracy** (residuals, error statistics).  
- Maintain an archive of **reference locations** (courthouses, section corners,  
  survey benchmarks, river confluences, etc.) across Kansas.  
- Link GCP sets to **STAC items** for provenance and time-aware usage [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:1‡Kansas Frontier Matrix – GIS Archive & Deeds Data Integration Guide.pdf](file-service://file-A8GiBPZM1dWsKG68SXPHjE).  

---

## Directory Layout

data/gcp/
├── README.md               # This file
├── kansas_topos/           # GCPs for historical topo maps
│   ├── 1894_ellsworth.gcp   # tie points for 1894 Ellsworth quad
│   └── 1937_salina.gcp      # tie points for 1937 Salina quad
├── aerials/                # GCPs for aerial photographs (county-level, 1930s–1950s)
├── plats/                  # GCPs for county plats / cadastral sheets
└── shared_benchmarks.json  # Common control locations (PLSS corners, benchmarks)

---

## GCP File Formats

- **Plaintext (`.gcp`)** — common in GDAL/QGIS:  

pixel_x, pixel_y, lon, lat
1340, 2250, -98.1234, 38.7654
2075, 310,  -98.2000, 38.8901

- **GeoJSON (`.geojson`)** — points with properties:  
```json
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

	•	CSV (.csv) — tabular for bulk import/export.
	•	JSON (.json) — structured control point sets, linked to STAC metadata.

Each file should include:
	•	source scan name + date
	•	projection (target CRS, usually EPSG:4326 or EPSG:3857)
	•	number of points + RMS error
	•	notes on point selection (e.g., “church spire”, “railroad junction”).

⸻

Integration
	•	Referenced in data/sources/ descriptors for scanned maps.
	•	Used by make rectified or make cogs targets in the Makefile to warp rasters ￼.
	•	Residuals/errors documented in provenance sidecars.
	•	STAC items in stac/items/topo/ or stac/items/plat/ cite the associated GCP file.

⸻

Notes
	•	Prefer stable features (river confluences, PLSS intersections) over transient ones (fence lines).
	•	Include at least 4–6 points well spread across the map. More points improve warp quality.
	•	Store raw + refined versions if iterations are done.
	•	Follow MCP reproducibility: every georeferencing step must reference its exact GCP input ￼ ￼.

⸻

See Also
	•	data/earth/sources/README.md — global basemaps used for checking alignment.
	•	data/processed/dem/overlays/README.md — raster overlays generated after georeferencing.
	•	stac/items/ — STAC metadata linking imagery to its GCP files.

---