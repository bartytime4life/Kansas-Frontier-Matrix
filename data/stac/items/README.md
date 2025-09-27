# STAC Items — Kansas Frontier Matrix

This folder holds the **STAC Item JSON files** — the atomic metadata records that describe individual
datasets (raster COGs, vector GeoJSON, scanned maps, overlays, etc.).  
Each Item links to a parent `collection` under `../collections/` and ultimately to the root `catalog.json`.

---

## Structure

```

data/stac/items/
dem/
ks_1m_dem_2018.json
ks_1m_dem_2020.json
overlays/
usgs_topo_larned_1894.json
vectors/
ks_treaties.json
ks_railroads.json

````

- **Subfolders** (`dem`, `overlays`, `vectors`, etc.) mirror the collection IDs.  
- **Item files** (`*.json`) describe one dataset instance (a specific DEM year, topo sheet, treaty vector).

---

## Authoring Rules

1. **Spec compliance**  
   - Use [STAC 1.0.0](https://stacspec.org/) (JSON Schema).  
   - Each file is `type: "Feature"` with `stac_version` and `id`.

2. **IDs**  
   - Lowercase with underscores, unique within project.  
   - Example: `ks_1m_dem_2018`, `usgs_topo_larned_1894`.

3. **Datetime**  
   - Use survey/acquisition/publication date if known.  
   - If approximate, use year start: `"1854-01-01T00:00:00Z"`.

4. **Geometry + BBox**  
   - Always include bounding box and footprint geometry in WGS84 (EPSG:4326).  
   - Simplify polygons where appropriate.

5. **Assets**  
   - **Raster COG**:  
     ```json
     "type": "image/tiff; application=geotiff; profile=cloud-optimized"
     ```
   - **Vector GeoJSON**:  
     ```json
     "type": "application/geo+json"
     ```
   - Include `roles: ["data"]` and `checksum:sha256`.

6. **Links**  
   - Each item must link to its collection:  
     ```json
     { "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" }
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
    "datetime": "2018-01-01T00:00:00Z"
  },
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.0, 36.9, -94.6, 40.0],
  "assets": {
    "data": {
      "href": "../../../cogs/dem/ks_1m_dem_2018.tif",
      "title": "Kansas 1m DEM (2018)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/dem.json", "type": "application/json" }
  ]
}
````

---

## Validation

* Run locally:

  ```bash
  pre-commit run stac-validate --all-files
  ```
* CI runs `.github/workflows/.pre-commit-config.yaml` to enforce STAC validity.
* Use `make stac` to regenerate `catalog.json` and run validators.

---

✅ Every file under `data/stac/items/` must be a **valid STAC Item**, link to its collection, and include
complete metadata (datetime, bbox, geometry, assets, checksum, license).

```
