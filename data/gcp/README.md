<div align="center">

# 📍 Kansas Geo Timeline — Ground Control Points (GCP)

This directory stores **Ground Control Points (GCPs)** and tie point files  
for georeferencing scanned maps, aerial photos, and historic imagery  
in the **Kansas Frontier Matrix**.  

GCPs transform **raw historical scans** into spatially referenced layers  
(GeoTIFFs / COGs) that align with modern coordinate systems.  
They are essential for **accuracy, reproducibility, and cross-dataset integration**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

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
	•	Support reproducible workflows — every rectified map cites its GCP file.
	•	Enable cross-checking accuracy (residuals, RMS error stats).
	•	Maintain an archive of stable reference features (PLSS corners, survey benchmarks, river confluences).
	•	Link GCPs to STAC items for provenance and time-aware usage.

⸻

📂 Directory layout

data/gcp/
├── README.md
├── kansas_topos/           # topo map GCPs
│   ├── 1894_ellsworth.gcp
│   └── 1937_salina.gcp
├── aerials/                # aerial photo GCPs (1930s–1950s)
├── plats/                  # county plat/cadastral sheets
└── shared_benchmarks.json  # common PLSS corners & benchmarks


⸻

🗂️ File formats

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
	•	CSV (.csv) — bulk import/export.
	•	JSON (.json) — structured sets, often linked to STAC metadata.

Each file should include:
	•	Source scan name + date
	•	Target CRS (EPSG:4326 or EPSG:3857 typical)
	•	Number of points + RMS error
	•	Notes on feature choice (e.g., “church spire”, “railroad junction”)

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
	•	Follow MCP reproducibility: each georeferencing step must reference the exact GCP file used.

⸻

📚 See also
	•	data/earth/sources/README.md — global basemaps for alignment checks.
	•	data/cogs/overlays/README.md — raster overlays generated after rectification.
	•	stac/items/ — STAC metadata linking imagery to its GCPs.

⸻

✅ Mission-grade principle: GCPs must be archived, cited, and reproducible.
No georeferenced map is valid without its documented GCP inputs.

