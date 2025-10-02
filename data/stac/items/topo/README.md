<div align="center">

# 🏔️ Kansas-Frontier-Matrix — STAC Items (Topographic & Elevation)  
`data/stac/items/topo/`

**Mission:** Curate **STAC Items for topographic maps and elevation products** —  
historic USGS topo sheets, DEM-derived contours, survey maps, and styled elevation layers.  

📌 Each Item = **one topo/elevation dataset instance** (e.g., `usgs_topo_larned_1894.json`).  
📌 Items link **up** to the `topo.json` Collection and the **root catalog**.  
📌 Items link **out** to scanned maps, digitized contours, and DEM derivatives.  
📌 Items link **back** to provenance (`data/provenance/registry.json`).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)  

</div>

---

## 📂 Directory Layout

```text
data/stac/items/topo/
├── usgs_topo_larned_1894.json   # Historic USGS topo quad (Larned, 1894)
├── contours_10m.json            # Derived 10 m contours from DEM
├── slope_aspect.json            # DEM-derived slope/aspect overlay
└── README.md


⸻

🧾 Authoring Checklist (Topo Items)
	1.	STAC compliance
	•	Must conform to STAC 1.0.0.
	•	Required header:

{ "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }


	2.	IDs
	•	Lowercase, underscores, unique.
	•	Examples: usgs_topo_larned_1894, contours_10m.
	3.	Datetime
	•	Topo maps → survey/publication year.
	•	DEM-derived → acquisition year of source DEM.
	•	Example: "datetime": "1894-01-01T00:00:00Z".
	4.	Geometry + BBox
	•	Must include both geometry and bbox.
	•	CRS: EPSG:4326.
	•	Simplify geometry footprints for performance.
	5.	Assets
	•	Scans (GeoTIFF/MrSID/PDF): image/tiff, application/pdf.
	•	Derived contours/slopes: application/geo+json or COG.
	•	Thumbnail: image/png.
	•	Must include roles, title, and checksum:sha256.
	6.	Links
	•	Must link to parent Collection (topo.json).
	•	Preferably link to provenance (registry.json).
	•	Optionally link to DEM source with rel: derived_from.

⸻

📑 Example Item — Historic Topo Map

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "usgs_topo_larned_1894",
  "collection": "topo",
  "properties": {
    "datetime": "1894-01-01T00:00:00Z",
    "license": "public-domain"
  },
  "bbox": [-99.3, 38.0, -98.5, 38.5],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-99.3, 38.0],
      [-98.5, 38.0],
      [-98.5, 38.5],
      [-99.3, 38.5],
      [-99.3, 38.0]
    ]]
  },
  "assets": {
    "scan": {
      "href": "../../../../data/cogs/topo/usgs_topo_larned_1894.tif",
      "title": "USGS Topo Map — Larned, 1894",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    },
    "thumbnail": {
      "href": "../../../../media/thumbnails/usgs_topo_larned_1894.png",
      "title": "Topo Map Thumbnail (Larned 1894)",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/topo.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#usgs_topo_larned_1894", "type": "application/json" }
  ]
}


⸻

🔗 Integration Notes
	•	Collections: Every topo Item belongs to topo.json.
	•	Provenance: Link to lineage in data/provenance/registry.json.
	•	Web Viewer: Used as basemap layers or overlays in MapLibre.
	•	Cross-links:
	•	Trails, towns, railroads → aligned against topo maps.
	•	Hazards (floods, Dust Bowl) → visualized against terrain.
	•	DEM derivatives (contours, slope) → tie to hydrology/erosion analysis.

⸻

✅ Validation

Local

pre-commit run stac-validate --all-files

Makefile

make stac
make stac-validate

CI
	•	.github/workflows/stac-validate.yml blocks merges if invalid.

⸻

⚠️ Common Pitfalls
	•	❌ Missing checksum:sha256 → always generate with sha256sum.
	•	❌ Wrong CRS (must be EPSG:4326).
	•	❌ Misaligned bbox vs geometry.
	•	❌ Not linking to Collection.
	•	❌ Scans not converted to COGs → convert with rio cogeo create --web-optimized.

⸻

✦ Summary

data/stac/items/topo/ contains STAC Items for topographic maps and elevation layers — historic quads, DEM-derived contours, styled slope/aspect.
Each Item is schema-compliant, provenance-linked, and time-aware, ensuring topo datasets are discoverable, reproducible, and cross-linked in the Frontier-Matrix catalog, knowledge graph, and web viewer.