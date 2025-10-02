<div align="center">

# 🏔️ Kansas-Frontier-Matrix — STAC Items (DEM)  
`data/stac/items/dem/`

**Mission:** Curate **Digital Elevation Model (DEM) Items** for Kansas, including 1m LiDAR, 10m USGS NED,  
and their **derivatives** (hillshade, slope, aspect, contours).  

📌 Each Item = **one DEM dataset instance** (e.g., `ks_1m_dem_2018.json`).  
📌 Items link **up** to the `dem.json` Collection and the **root catalog**.  
📌 Items link **out** to COGs, processed rasters, and derivative products.  
📌 Items link **back** to provenance in `data/provenance/registry.json`.  

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
data/stac/items/dem/
├── ks_1m_dem_2018.json      # 1 m DEM (LiDAR, 2018)
├── ks_1m_dem_2020.json      # 1 m DEM (LiDAR, 2020)
└── README.md


⸻

🧾 Authoring Checklist (DEM Items)
	1.	STAC compliance
	•	Must conform to STAC 1.0.0.
	•	Required header:

{ "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }


	2.	IDs
	•	Format: lowercase + underscores.
	•	Example: ks_1m_dem_2018.
	3.	Datetime
	•	Acquisition year → "YYYY-12-31T00:00:00Z" if annual.
	•	Example: "datetime": "2018-12-31T00:00:00Z".
	4.	Geometry + BBox
	•	Must include both geometry and bbox.
	•	CRS: EPSG:4326.
	5.	Assets (must include roles, title, and checksum:sha256)
	•	DEM (COG):
	•	type: image/tiff; application=geotiff; profile=cloud-optimized
	•	roles: ["data"]
	•	Hillshade (COG):
	•	roles: ["visual"]
	•	Optional: slope, aspect, thumbnail
	6.	Links
	•	Must link to parent Collection and provenance.

⸻

📑 Example Item — DEM

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018",
  "collection": "dem",
  "properties": {
    "datetime": "2018-12-31T00:00:00Z",
    "license": "public-domain"
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-94.59, 36.99],
      [-94.59, 40.00],
      [-102.05, 40.00],
      [-102.05, 36.99]
    ]]
  },
  "assets": {
    "data": {
      "href": "../../../../data/cogs/dem/ks_1m_dem_2018.tif",
      "title": "Kansas 1 m DEM (2018)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    },
    "hillshade": {
      "href": "../../../../data/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif",
      "title": "Hillshade (derived from DEM 2018)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["visual"],
      "checksum:sha256": "<sha256sum>"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/dem.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#ks_1m_dem_2018", "type": "application/json" }
  ]
}


⸻

🔗 Integration Notes
	•	Collections: Every DEM Item belongs to dem.json.
	•	Provenance: Link to lineage in data/provenance/registry.json.
	•	Derivatives: Include hillshade, slope, aspect when available.
	•	Web Viewer: MapLibre reads Item IDs for DEM + hillshade layers.
	•	Makefile: make stac and make stac-validate auto-build and validate DEM Items.

⸻

✅ Validation

Local

pre-commit run stac-validate --all-files

Makefile

make stac
make stac-validate

CI
	•	.github/workflows/stac-validate.yml blocks merges if Items are invalid.

⸻

⚠️ Common Pitfalls
	•	❌ Missing checksum:sha256 → always generate with sha256sum.
	•	❌ DEMs not COG-optimized → reprocess with rio cogeo create --web-optimized.
	•	❌ Incorrect CRS → must be EPSG:4326 for STAC Items.
	•	❌ Inconsistent bbox and geometry → recompute extents.
	•	❌ Items missing derivative layers → include hillshade at minimum.

⸻

✦ Summary

data/stac/items/dem/ contains STAC Items for Kansas DEM datasets.
Each Item describes one DEM instance (LiDAR, NED) with links to raw COGs, derivative products, provenance, and metadata.
They ensure DEM layers are time-aware, reproducible, and discoverable, powering the STAC catalog, knowledge graph, and interactive viewer.