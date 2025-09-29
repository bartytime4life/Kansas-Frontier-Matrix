<div align="center">

# 🗂️ Kansas-Frontier-Matrix — **STAC Items** (`data/stac/items/`)

**Role:** The **atomic units** of the STAC catalog.  
Each Item is a **JSON Feature** that describes **one dataset instance** — DEMs, historic maps, treaty vectors, scanned documents, overlays, tiles, etc.  

📌 Items link **upward** → their **Collection** (`../collections/*.json`) and the **root** `../catalog.json`.  
📌 Items link **outward** → actual data files (`data/cogs/`, `data/processed/`, `data/docs/`, `data/kml/`).  
📌 Items link **backward** → provenance (`../provenance/registry.json`).

</div>

---

## Structure

```text
data/stac/items/
├── dem/
│   ├── ks_1m_dem_2018.json
│   └── ks_1m_dem_2020.json
├── overlays/
│   └── usgs_topo_larned_1894.json
├── vectors/
│   ├── ks_treaties.json
│   └── ks_railroads.json
└── docs/
    └── treaty_osage_1825.json

	•	Subfolders mirror Collection IDs (dem, overlays, vectors, docs, …).
	•	Item files describe a single dataset instance.

⸻

Authoring Checklist
	1.	STAC compliance
	•	Must conform to STAC 1.0.0.
	•	Minimum header:

{ "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }


	2.	IDs
	•	Lowercase, underscores, unique.
	•	Examples: ks_1m_dem_2018, usgs_larned_1894, treaty_osage_1825.
	3.	Datetime
	•	DEM / imagery → acquisition date.
	•	Maps / surveys → publication/survey year.
	•	Treaties / docs → signing/publication date.
	•	Approximate? Use "YYYY-01-01T00:00:00Z".
	4.	Geometry + BBox
	•	Include both geometry and bbox.
	•	CRS: WGS84 (EPSG:4326).
	•	Simplify footprints when possible.
	5.	Assets (every asset must include roles, title, license, and checksum:sha256)
	•	Raster COG → image/tiff; application=geotiff; profile=cloud-optimized
	•	Vector → application/geo+json
	•	Document → application/pdf
	•	Tiles → application/vnd.mapbox-vector-tile (or vendor type)
	•	Thumbnail → image/png
	6.	Links
	•	Always link to parent Collection:

{ "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" }


	•	Preferably link to provenance:

{ "rel": "derived_from", "href": "../../provenance/registry.json#ks_treaties", "type": "application/json" }



⸻

Example Item — Raster DEM

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018",
  "collection": "dem",
  "properties": {
    "datetime": "2018-12-31T00:00:00Z",
    "license": "Public Domain"
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": { "type": "Polygon", "coordinates": [...] },
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

Integration Points
	•	Collections → every Item must belong to a parent Collection (../collections/*.json).
	•	Provenance → Items should link to lineage in ../provenance/registry.json.
	•	Web Viewer → web/data/*.json config references Item IDs.
	•	Makefile → make stac and make stac-validate auto-build and check Items.
	•	Experiments (MCP) → experiment logs cite Item IDs.
	•	Earth exports → Items may include application/vnd.google-earth.kmz assets for KMZ overlays.

⸻

Validation

Local

pre-commit run stac-validate --all-files

Makefile

make stac
make stac-validate

CI
	•	.github/workflows/stac-validate.yml blocks merges if Items are invalid.

⸻

Common Pitfalls
	•	❌ Both datetime and start/end_datetime → pick one.
	•	❌ Missing checksum:sha256 → generate with sha256sum + copy into Item.
	•	❌ Relative paths wrong → assets must point to ../../../../data/....
	•	❌ Vectors not EPSG:4326 → reproject before publishing.
	•	❌ DEM COGs missing tiling/overviews → reprocess with rio cogeo create --web-optimized.
	•	❌ bbox mismatch with geometry → recompute extents.

⸻

TL;DR
	•	Every file in data/stac/items/ is a STAC Item.
	•	Must link to its Collection, include time + space + assets + provenance.
	•	If in doubt: copy a template, update fields, run validation, then open a PR.

