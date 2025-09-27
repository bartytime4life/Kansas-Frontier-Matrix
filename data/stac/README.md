# STAC Catalog — Kansas Frontier Matrix

This folder holds the **SpatioTemporal Asset Catalog (STAC)** that organizes all geospatial and historical datasets
used in the Kansas Frontier Matrix.  
It is the **single source of truth** for dataset metadata, provenance, spatial/temporal extents, and links to
data artifacts under `data/`.

---

## Structure

```

data/stac/
catalog.json               # Root STAC catalog
collections/               # Groupings of related datasets
dem.json                 # Digital Elevation Models
topo.json                # Historic topographic maps
overlays.json            # Scanned map overlays, soil surveys, etc.
vectors.json             # Vector layers (treaties, trails, towns, railroads…)
items/                     # Individual datasets with metadata
dem/ks_1m_dem_2018.json
overlays/usgs_topo_larned_1894.json
vectors/ks_treaties.json
vectors/ks_railroads.json

````

- **`catalog.json`** — Root catalog, references all collections.
- **`collections/*.json`** — Each logical grouping (DEM, topo, overlays, vectors, etc.).
- **`items/<collection>/*.json`** — STAC Items describing individual assets (COGs, GeoJSON, etc.).

---

## STAC Version

- **Spec:** [STAC 1.0.0](https://stacspec.org/)  
- **Extensions:** may include `proj`, `eo`, `raster`, `version`, `checksum`, depending on dataset.

---

## Conventions

- **IDs**  
  Use lowercase with underscores, e.g. `ks_1m_dem_2018`, `usgs_topo_larned_1894`.

- **Datetime**  
  - For maps/surveys: use publication year or survey range.  
  - For rasters (DEM, NLCD, etc.): use acquisition year(s).

- **Assets**  
  - Rasters: `COG` (Cloud-Optimized GeoTIFF) under `data/cogs/`.  
  - Vectors: GeoJSON under `data/processed/`.  
  - Use media types:  
    - `image/tiff; application=geotiff; profile=cloud-optimized`  
    - `application/geo+json`

- **Provenance**  
  Always include `license`, `providers`, `created`, `updated`, and `checksum:sha256`.

---

## How to Add a New Dataset

1. **Prepare data**  
   - Convert rasters → COG (see `rio cogeo create`).  
   - Convert vectors → GeoJSON (`ogr2ogr -f GeoJSON -t_srs EPSG:4326`).

2. **Place artifact**  
   - Save in `data/cogs/` (raster) or `data/processed/` (vector).  
   - Compute SHA-256: `scripts/gen_sha256.sh path/to/file`.

3. **Create STAC Item**  
   - Copy an existing item JSON from `items/<collection>/`.  
   - Update `id`, `properties.datetime`, `bbox`, `geometry`, and `assets`.

4. **Link to collection**  
   - Add the item to the relevant `collections/*.json`.  

5. **Validate**  
   - Run:  
     ```bash
     pre-commit run stac-validate --all-files
     ```
   - Or manually:  
     ```bash
     kgt validate-stac data/stac/items --no-strict
     ```

---

## Example STAC Item (Vector)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_treaties",
  "collection": "vectors",
  "properties": {
    "datetime": "1854-01-01T00:00:00Z"
  },
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.0, 36.9, -94.6, 40.0],
  "assets": {
    "data": {
      "href": "../../processed/ks_treaties.json",
      "title": "Kansas Treaties (GeoJSON)",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" }
  ]
}
````

---

## Validation & CI

* **Pre-commit hook**: `stac-validate` runs automatically on `stac/items/*.json`.
* **CI**: `.github/workflows/.pre-commit-config.yaml` enforces validation in GitHub Actions.
* **Local**: run `make stac` to regenerate and validate catalogs.

---

✅ The STAC catalog ensures all Kansas Frontier Matrix datasets are **discoverable, linkable, and reproducible**.

```
