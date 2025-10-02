<div align="center">

# 🧩 Kansas-Frontier-Matrix — STAC Items (Vectors)  
`data/stac/items/vectors/`

**Mission:** Curate **vector STAC Items** — treaties, trails, towns, railroads, hydrology lines, parcels, soils —  
ensuring they are **traceable, reproducible, and discoverable** in the STAC catalog.  

📌 Each Item = **one vector dataset instance** (e.g., `ks_treaties.json`, `ks_railroads.json`).  
📌 Items link **up** to the `vectors.json` Collection and the **root catalog**.  
📌 Items link **out** to GeoJSON, Shapefiles, or vector tiles.  
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
data/stac/items/vectors/
├── ks_treaties.json         # Treaty & land transfer polygons
├── ks_railroads.json        # Historic railroad lines
├── ks_towns.json            # Townsite polygons/points
├── ks_trails.json           # Santa Fe, Oregon, other historic trails
├── ks_parcels.json          # Cadastral parcels
└── README.md


⸻

🧾 Authoring Checklist (Vector Items)
	1.	STAC compliance
	•	Must conform to STAC 1.0.0.
	•	Required header:

{ "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }


	2.	IDs
	•	Lowercase, underscores, unique.
	•	Examples: ks_treaties, ks_railroads_1900.
	3.	Datetime
	•	Use date of dataset validity (survey, treaty signing, publication).
	•	Example: "datetime": "1854-05-30T00:00:00Z".
	•	If multi-year → use start_datetime / end_datetime.
	4.	Geometry + BBox
	•	Must include both geometry and bbox.
	•	CRS: EPSG:4326.
	•	Simplify geometries if very complex.
	5.	Assets
	•	GeoJSON: application/geo+json, roles ["data"].
	•	Shapefile / GPKG: application/zip (zipped shapefile) or application/geopackage+sqlite3.
	•	Vector tiles: application/vnd.mapbox-vector-tile.
	•	Thumbnail: image/png.
	•	Every asset must include roles, title, and checksum:sha256.
	6.	Links
	•	Must link to parent Collection (vectors.json).
	•	Preferably link to provenance (registry.json).

⸻

📑 Example Item — Treaty Vectors

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_treaties",
  "collection": "vectors",
  "properties": {
    "datetime": "1854-05-30T00:00:00Z",
    "license": "public-domain"
  },
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-94.61, 36.99],
      [-94.61, 40.00],
      [-102.05, 40.00],
      [-102.05, 36.99]
    ]]
  },
  "assets": {
    "geojson": {
      "href": "../../../../data/processed/vectors/ks_treaties.geojson",
      "title": "Kansas Treaty and Land Cession Boundaries",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    },
    "thumbnail": {
      "href": "../../../../media/thumbnails/ks_treaties.png",
      "title": "Treaty Boundaries Thumbnail",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#ks_treaties", "type": "application/json" }
  ]
}


⸻

🔗 Integration Notes
	•	Collections: Every vector Item belongs to vectors.json.
	•	Provenance: Must reference lineage in data/provenance/registry.json.
	•	Web Viewer: Vectors power interactive layers (treaties, trails, towns).
	•	Experiments: MCP logs cite vector Item IDs in analysis.
	•	Cross-links:
	•	Treaty → Event & Document Items.
	•	Railroads → Settlement & economy layers.
	•	Trails → Hydrology + terrain layers.

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
	•	❌ Missing checksum:sha256.
	•	❌ Wrong CRS (must be EPSG:4326).
	•	❌ Inconsistent bbox and geometry.
	•	❌ Not linking to Collection.
	•	❌ Complex geometries without simplification → huge file sizes.

⸻

✦ Summary

data/stac/items/vectors/ contains STAC Items for vector datasets — treaties, trails, towns, railroads, parcels.
Each Item is schema-compliant, provenance-linked, and time-aware, powering the STAC catalog, knowledge graph, and interactive map viewer.
These Items ensure Kansas’s vector data is discoverable, reproducible, and cross-linked with documents, DEMs, and overlays.