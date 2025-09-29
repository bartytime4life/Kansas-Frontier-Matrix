# Kansas-Frontier-Matrix — STAC Catalog

This directory holds the **SpatioTemporal Asset Catalog (STAC)** that organizes all geospatial and historical datasets  
used in the Kansas Frontier Matrix.  

The STAC catalog is the **single source of truth** for dataset metadata, provenance, spatial/temporal extents, and links to  
artifacts stored in `data/raw/`, `data/processed/`, `data/cogs/`, and `data/kml/`.

---

## Structure

data/stac/
├── catalog.json                # Root STAC catalog (entry point)
├── collections/                # Groupings of related datasets
│   ├── dem.json                # Digital Elevation Models
│   ├── topo.json               # Historic topographic maps
│   ├── overlays.json           # Map overlays, soil surveys, styled rasters
│   └── vectors.json            # Vector datasets (treaties, trails, towns, railroads…)
└── items/                      # Individual datasets
├── dem/ks_1m_dem_2018.json
├── overlays/usgs_topo_larned_1894.json
├── vectors/ks_treaties.json
└── vectors/ks_railroads.json

- **`catalog.json`** → Root catalog referencing all collections.  
- **`collections/*.json`** → Logical groupings (DEM, topo, overlays, vectors, etc.).  
- **`items/<collection>/*.json`** → STAC Items describing individual datasets (COGs, GeoJSON, KMZ).  

---

## STAC Version

- **Specification:** [STAC 1.0.0](https://stacspec.org/)  
- **Extensions supported:**  
  - `proj` → CRS, grid definition  
  - `eo` → earth observation (bands, acquisition)  
  - `raster` → raster metadata (resolution, nodata)  
  - `version` → dataset versioning  
  - `checksum` → integrity validation  

---

## Conventions

### IDs
- Use lowercase with underscores.  
- Examples: `ks_1m_dem_2018`, `usgs_topo_larned_1894`, `ks_treaties`.

### Datetime
- **Maps/surveys:** publication year or survey range.  
- **Rasters (DEM, NLCD, etc.):** acquisition year(s).  
- **Documents/events:** treaty signing date, flood year, etc.

### Assets
- **Rasters:** COGs under `data/cogs/`.  
- **Vectors:** GeoJSON under `data/processed/`.  
- **Overlays:** styled COGs or color-reliefs under `data/processed/dem/overlays/`.  
- **Earth exports:** KML/KMZ in `data/kml/`.  

Media types:
- `image/tiff; application=geotiff; profile=cloud-optimized`  
- `application/geo+json`  
- `application/vnd.google-earth.kmz`  

### Provenance
- Always include:  
  - `license`  
  - `providers` (name, roles, URLs)  
  - `created` / `updated`  
  - `checksum:sha256` (matches `.sha256` sidecars in `data/raw/` / `data/processed/`) [oai_citation:0‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P)  
- Link back to `data/provenance/registry.json` for lineage [oai_citation:1‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468).  

---

## How to Add a New Dataset

1. **Prepare data**  
   - Raster → COG (`rio cogeo create`).  
   - Vector → GeoJSON (`ogr2ogr -f GeoJSON -t_srs EPSG:4326`).  

2. **Place artifact**  
   - `data/cogs/` for rasters, `data/processed/` for vectors.  
   - Compute SHA-256:  
     ```bash
     scripts/gen_sha256.sh path/to/file
     ```

3. **Create STAC Item**  
   - Copy an example from `items/<collection>/`.  
   - Update `id`, `datetime`, `bbox`, `geometry`, `assets`.  
   - Ensure `checksum:sha256` matches the generated value.  

4. **Link to collection**  
   - Add the item reference to the relevant `collections/*.json`.  
   - Verify `catalog.json` points to the updated collection.  

5. **Validate**  
   ```bash
   make stac-validate
   pre-commit run stac-validate --all-files


⸻

Example STAC Item (Vector)

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_treaties",
  "collection": "vectors",
  "properties": {
    "datetime": "1854-01-01T00:00:00Z",
    "license": "CC-BY-4.0"
  },
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.0, 36.9, -94.6, 40.0],
  "assets": {
    "data": {
      "href": "../../../processed/ks_treaties.json",
      "title": "Kansas Treaties (GeoJSON)",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#ks_treaties", "type": "application/json" }
  ]
}


⸻

Integration
	•	Provenance → data/provenance/registry.json links IDs to raw → processed → STAC lineage.
	•	Web Viewer → Layers in web/data/*.json must reference STAC IDs to stay consistent.
	•	Makefile → Targets (make stac, make stac-validate) update and verify catalog.
	•	Experiments → MCP logs in experiments/**/experiment.md must cite STAC item IDs.
	•	KML exports → KML/KMZ in data/kml/ must reference source STAC item(s).

⸻

Validation & CI
	•	Pre-commit → stac-validate runs automatically on stac/items/*.json.
	•	CI workflows → .github/workflows/stac-validate.yml enforces schema compliance.
	•	Local →

make stac
make stac-validate
kgt validate-stac data/stac/items



⸻

✅ The STAC catalog ensures all Kansas Frontier Matrix datasets are discoverable, linkable, reproducible, and compliant with MCP reproducibility and web viewer integration.

---