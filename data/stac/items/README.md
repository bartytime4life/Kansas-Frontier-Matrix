# Kansas-Frontier-Matrix — STAC Items

This folder holds the **STAC Item JSON files** — the atomic metadata records that describe individual datasets  
(raster COGs, vector GeoJSON, scanned maps, overlays, documents, etc.).  

Each Item links to a **parent Collection** under `../collections/` and ultimately to the **root `catalog.json`**.  
Items are the **granular building blocks** of the Kansas Frontier Matrix STAC ecosystem.

---

## Structure

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

- **Subfolders** (`dem`, `overlays`, `vectors`, `docs`, etc.) mirror collection IDs.  
- **Item files** (`*.json`) describe one dataset instance (a DEM mosaic, a topo sheet, a treaty vector, a document scan).  

---

## Authoring Rules

1. **STAC compliance**  
   - Use [STAC 1.0.0](https://stacspec.org/) JSON Schema.  
   - Each file must be:  
     ```json
     { "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }
     ```

2. **IDs**  
   - Lowercase, underscores, unique.  
   - Examples: `ks_1m_dem_2018`, `usgs_topo_larned_1894`, `treaty_osage_1825`.

3. **Datetime**  
   - **DEM / imagery:** acquisition date.  
   - **Maps / surveys:** publication or survey year.  
   - **Treaties / documents:** signing or publication date.  
   - If approximate → use year start, e.g. `"1854-01-01T00:00:00Z"`.

4. **Geometry + BBox**  
   - Must include **bounding box** and **footprint geometry** in WGS84 (EPSG:4326).  
   - Simplify polygons if complex.

5. **Assets**  
   - **Raster COGs:**  
     ```json
     "type": "image/tiff; application=geotiff; profile=cloud-optimized"
     ```
   - **Vector GeoJSON:**  
     ```json
     "type": "application/geo+json"
     ```
   - **Documents (PDF):**  
     ```json
     "type": "application/pdf"
     ```
   - Always include:  
     - `roles: ["data"]`  
     - `checksum:sha256`  
     - `title` and `license`.

6. **Links**  
   - Must link to parent collection:  
     ```json
     { "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" }
     ```
   - Optionally link to provenance registry:  
     ```json
     { "rel": "derived_from", "href": "../../provenance/registry.json#ks_treaties" }
     ```

---

## Example STAC Item (Raster DEM)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018",
  "collection": "dem",
  "properties": {
    "datetime": "2018-01-01T00:00:00Z",
    "license": "public-domain"
  },
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "assets": {
    "data": {
      "href": "../../../cogs/dem/ks_1m_dem_2018.tif",
      "title": "Kansas 1m DEM (2018)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    },
    "hillshade": {
      "href": "../../../processed/dem/overlays/ks_1m_dem_2018_hillshade.tif",
      "title": "Hillshade overlay (derived from DEM 2018)",
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

Integration
	•	Collections → Each Item belongs to a collections/*.json file.
	•	Provenance → Each Item must link back to provenance entries (data/provenance/registry.json) ￼.
	•	Web Viewer → Web configs (web/data/*.json) reference STAC Item IDs to load data layers.
	•	Makefile → make stac auto-builds catalog references and runs validation.
	•	Experiments → MCP experiment logs must cite STAC Item IDs for datasets used.
	•	KML exports → Items may include links to derived KMZ overlays (data/kml/).

⸻

Validation

Local

pre-commit run stac-validate --all-files

Makefile

make stac
make stac-validate

CI
	•	.github/workflows/stac-validate.yml enforces validation.
	•	Pull requests cannot merge unless all STAC Items are valid.

⸻

✅ Every file under data/stac/items/ must be a valid STAC Item, link to its collection, and include
complete metadata (datetime, bbox, geometry, assets, checksum, license, provenance).

---