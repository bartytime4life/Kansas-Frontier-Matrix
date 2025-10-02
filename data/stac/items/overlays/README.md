<div align="center">

# 🗺️ Kansas-Frontier-Matrix — STAC Items (Overlays)  
`data/stac/items/overlays/`

**Mission:** Curate **overlay STAC Items** for Kansas — derivative and styled layers built on top of DEMs, maps, and other sources.  
Examples: hillshade, slope, aspect, roughness, styled rasters, composite map overlays.  

📌 Each Item = **one overlay instance** (e.g., hillshade from 2018 DEM, styled soils raster).  
📌 Items link **up** to the `overlays.json` Collection and the **root catalog**.  
📌 Items link **out** to processed rasters in `data/processed/` or COGs in `data/cogs/overlays/`.  
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
data/stac/items/overlays/
├── ks_1m_dem_2018_hillshade.json     # Hillshade derived from 2018 DEM
├── ks_1m_dem_2018_slope.json         # Slope overlay derived from 2018 DEM
├── usgs_topo_larned_1894.json        # Historic topo sheet styled overlay
└── README.md


⸻

🧾 Authoring Checklist (Overlays)
	1.	STAC compliance
	•	Must conform to STAC 1.0.0.
	•	Required header:

{ "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }


	2.	IDs
	•	Lowercase, underscores, unique.
	•	Examples: ks_1m_dem_2018_hillshade, usgs_topo_larned_1894.
	3.	Datetime
	•	Derived overlays inherit the acquisition/publication year of their source DEM or map.
	•	Example: "datetime": "2018-12-31T00:00:00Z".
	4.	Geometry + BBox
	•	Must include both geometry and bbox.
	•	CRS: EPSG:4326.
	5.	Assets
	•	Raster COGs: image/tiff; application=geotiff; profile=cloud-optimized.
	•	Styled maps: image/tiff or application/vnd.mapbox-vector-tile if tiled.
	•	Thumbnails: image/png.
	•	Must include roles, title, and checksum:sha256.
	6.	Links
	•	Must link to parent Collection (overlays.json).
	•	Should link to provenance (registry.json).
	•	Optionally link to source DEM/Map Item with rel: derived_from.

⸻

📑 Example Item — Hillshade Overlay

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_hillshade",
  "collection": "overlays",
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
    "overlay": {
      "href": "../../../../data/processed/overlays/ks_1m_dem_2018_hillshade.tif",
      "title": "Hillshade Overlay (DEM 2018)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["visual"],
      "checksum:sha256": "<sha256sum>"
    },
    "thumbnail": {
      "href": "../../../../media/thumbnails/ks_1m_dem_2018_hillshade.png",
      "title": "Hillshade Thumbnail",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/overlays.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../items/dem/ks_1m_dem_2018.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#ks_1m_dem_2018", "type": "application/json" }
  ]
}


⸻

🔗 Integration Notes
	•	Collections: All overlay Items belong to overlays.json.
	•	Derived From: Must reference the DEM or topo Item they were generated from.
	•	Web Viewer: Overlays used as styled layers in MapLibre and Google Earth exports.
	•	Provenance: Each overlay links to lineage in data/provenance/registry.json.
	•	Experiments: MCP logs cite overlay IDs when used in terrain/hazard modeling.

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
	•	❌ Forgetting to link overlay back to source DEM/map Item.
	•	❌ Missing checksum:sha256.
	•	❌ Wrong MIME types for styled rasters.
	•	❌ Inconsistent bbox and geometry.
	•	❌ Overlays not aligned to EPSG:4326.

⸻

✦ Summary

data/stac/items/overlays/ contains STAC Items for derivative and styled layers — hillshade, slope, aspect, topo overlays.
They are time-aware, provenance-tracked, and STAC-compliant, ensuring overlays are discoverable and reproducible,
powering interactive maps, the STAC catalog, and the Frontier-Matrix knowledge graph.