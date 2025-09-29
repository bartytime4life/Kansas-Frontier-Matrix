# Kansas-Frontier-Matrix — STAC Collections

This folder contains **STAC Collection JSON files** — groupings of related STAC Items under the  
Kansas Frontier Matrix catalog.  

Each Collection defines **shared metadata** across its Items (spatial/temporal extent, keywords, providers, license)  
and ensures datasets are discoverable and properly attributed.  

---

## Structure

data/stac/collections/
├── dem.json          # Digital Elevation Models
├── topo.json         # Historic topographic maps
├── overlays.json     # DEM/map overlays, soils, styled rasters
└── vectors.json      # Vectors (treaties, trails, towns, railroads…)

- **`catalog.json`** (in `../`) → root catalog referencing these collections.  
- **`items/`** → holds the individual STAC Item JSON files for each collection.  
- **Collection files** → must end in `.json` and comply with the [STAC 1.0.0 Collection spec](https://stacspec.org/).  

---

## Authoring Rules

1. **STAC Compliance**  
   - Required fields:  
     ```json
     "stac_version": "1.0.0",
     "type": "Collection"
     ```

2. **IDs**  
   - Short, lowercase, descriptive.  
   - Examples: `dem`, `topo`, `overlays`, `vectors`.

3. **Extent**  
   - Define both **spatial extent** (`bbox` in WGS84) and **temporal extent** (`interval`).  
   - Use the **union of all Items** in the collection.  

4. **Keywords**  
   - Add thematic tags for search.  
   - Example: `"keywords": ["DEM", "LiDAR", "elevation", "Kansas"]`

5. **Providers**  
   - Credit upstream sources (e.g., USGS, NOAA, Kansas GIS Hub, KGS).  
   - Example:  
     ```json
     "providers": [
       { "name": "USGS", "roles": ["producer", "licensor"], "url": "https://www.usgs.gov/" }
     ]
     ```

6. **License**  
   - Use SPDX identifiers when possible:  
     - `"CC-BY-4.0"` (attribution)  
     - `"PDDL-1.0"` (public domain dedication)  
   - Or `"public-domain"` for USGS/NOAA data.

7. **Links**  
   - Each Collection must:  
     - Link back to `../catalog.json` (`rel: root`).  
     - Link forward to all STAC Items it groups (`rel: item`).  
     - Optionally link to related docs or provenance (`rel: derived_from`).

---

## Example STAC Collection (DEM)

```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [],
  "type": "Collection",
  "id": "dem",
  "title": "Digital Elevation Models (Kansas)",
  "description": "DEM datasets for Kansas including 1m LiDAR-derived surfaces.",
  "license": "public-domain",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.59, 40.00]] },
    "temporal": { "interval": [["2018-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]] }
  },
  "providers": [
    {
      "name": "USGS",
      "roles": ["producer", "licensor"],
      "url": "https://www.usgs.gov/"
    }
  ],
  "keywords": ["DEM", "elevation", "LiDAR", "Kansas"],
  "links": [
    { "rel": "root", "href": "../catalog.json", "type": "application/json" },
    { "rel": "item", "href": "../items/dem/ks_1m_dem_2018.json", "type": "application/geo+json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#ks_1m_dem_2018", "type": "application/json" }
  ]
}


⸻

Integration
	•	Provenance → Each Collection links back to data/provenance/registry.json for lineage ￼.
	•	Web Viewer → Collections inform how layers are grouped in web/config/layers.schema.json.
	•	Makefile → make stac and make stac-validate build, update, and check collections.
	•	Experiments → MCP logs in experiments/** must cite STAC collection IDs when using grouped datasets.

⸻

Validation

Pre-commit hook

pre-commit run stac-validate --all-files

Manual with kgt

kgt validate-stac data/stac/collections --no-strict

CI
	•	.github/workflows/stac-validate.yml enforces schema compliance.
	•	Failures block merges until collections and items validate.

⸻

✅ Each Collection ensures its Items are discoverable, grouped, attributed, and reproducible within the Kansas Frontier Matrix STAC catalog.

---