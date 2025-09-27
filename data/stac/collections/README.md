# STAC Collections — Kansas Frontier Matrix

This folder contains **STAC Collection JSON files** — groupings of related STAC Items under the 
Kansas Frontier Matrix catalog.  
Each collection defines metadata shared across its Items (spatial/temporal extent, keywords, providers, license).

---

## Structure

```

data/stac/collections/
dem.json          # Digital Elevation Models
topo.json         # Historic topographic maps
overlays.json     # Scanned map overlays, soils, etc.
vectors.json      # Vector layers (treaties, trails, towns, railroads…)

````

- **`catalog.json`** (in `../`) references these collections.  
- **`items/`** holds the individual STAC Item JSON files that belong to each collection.  
- **Collection files** must end in `.json` and follow the [STAC 1.0.0 Collection spec](https://stacspec.org/).

---

## Authoring Rules

1. **STAC Compliance**  
   - `"stac_version": "1.0.0"`  
   - `"type": "Collection"`

2. **IDs**  
   - Short, lowercase, descriptive (e.g., `dem`, `topo`, `overlays`, `vectors`).

3. **Extent**  
   - Each collection must define a **spatial extent** (`bbox` in WGS84) and **temporal extent** (`interval`).  
   - Use the union of all Items in the collection.

4. **Keywords**  
   - Provide thematic tags for search (e.g., `"keywords": ["DEM", "LiDAR", "elevation", "Kansas"]`).

5. **Providers**  
   - Credit original data sources (USGS, NOAA, Kansas GIS Hub, KGS, etc.).  
   - Example:  
     ```json
     "providers": [
       {
         "name": "USGS",
         "roles": ["producer", "licensor"],
         "url": "https://www.usgs.gov/"
       }
     ]
     ```

6. **License**  
   - Use SPDX identifiers where possible (e.g., `"license": "PDDL-1.0"` or `"license": "CC-BY-4.0"`).  
   - If public domain (e.g., USGS), mark `"license": "public-domain"`.

7. **Links**  
   - Each collection must link back to the root catalog and forward to its items.  

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
    { "rel": "item", "href": "../items/dem/ks_1m_dem_2018.json", "type": "application/geo+json" }
  ]
}
````

---

## Validation

* Run pre-commit hook:

  ```bash
  pre-commit run stac-validate --all-files
  ```
* Or manually with [`kgt`](https://github.com/bartytime4life/kgt):

  ```bash
  kgt validate-stac data/stac/collections --no-strict
  ```
* CI runs `.github/workflows/.pre-commit-config.yaml` to enforce validity.

---

✅ Each Collection ensures its Items are **discoverable, grouped, and properly attributed** within the Kansas Frontier Matrix STAC catalog.

```
