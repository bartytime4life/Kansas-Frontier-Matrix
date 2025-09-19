# Kansas Geo Timeline — **Time · Terrain · History**

A minimal **Google Earth + Web (GitHub Pages)** mapping system for Kansas elevation and historical layers.

* **Earth deliverables**: regionated **KML/KMZ** (progressive loading via NetworkLinks)
* **Web app**: lightweight **MapLibre** viewer with a **time slider**
* **Data model**: **STAC-like JSON** for sources, spatial/temporal extents, provenance & license
* **Pipelines**: `Makefile` targets to **fetch → COG → derivatives (slope/aspect/hillshade) → KML → site**

> Created 2025-09-18 01:38:08 UTC.
> Fill in the ArcGIS/USGS endpoints in `data/sources/*.json` (examples below), then run `make help`.

---

## Quickstart

```bash
# Python env
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# 1) Configure sources (edit data/sources/*.json)
# 2) Fetch & convert
make fetch
make cogs
make terrain

# 3) Build Earth package (KMZ) + simple web viewer
make kml
make site

# 4) Serve locally (web viewer)
python -m http.server -d web 8080
```

---

## Repository layout

```
data/          # inputs/outputs (COGs, KMZ, STAC items, JSON metadata)
  sources/     # source descriptors (endpoints, CRS, bounds, license)
  processed/   # generated COGs/tiles and artifacts
stac/          # static catalog of items & collections (time-indexed)
scripts/       # small, dependency-light tools (Python/bash)
web/           # static site (MapLibre) for GitHub Pages
docker/        # optional container environment (reproducible build)
mcp/           # (optional) experiments/, sops/, model_cards/ for rigor
```

---

## Make targets (concise)

```bash
make help               # show all tasks
make fetch              # pull raw rasters/vectors via endpoints in data/sources/*.json
make cogs               # convert rasters to Cloud Optimized GeoTIFFs (COGs)
make terrain            # derive hillshade/slope/aspect from DEMs
make stac               # (re)generate stac/*.json with time/space/provenance
make kml                # regionate overlays; emit KML/KMZ with NetworkLinks
make site               # build static web viewer (web/) + layer manifest
make clean              # remove intermediates
make check              # validate JSON/STAC, ensure CRS/extent consistency
make reproducibility    # smoke-test a tiny pipeline slice end-to-end
```

---

## Data sources (examples)

Create a source descriptor (edit as needed) in `data/sources/ks_dem.json`:

```json
{
  "id": "ks_dem_1m",
  "title": "Kansas DEM (1 m)",
  "type": "raster-dem",
  "endpoint": {
    "type": "arcgis",
    "url": "https://tiles.kansasgis.org/arcgis/rest/services/Elevation/KS_1m_DEM/ImageServer"
  },
  "spatial": { "bbox": [-102.1, 36.99, -94.6, 40.00], "crs": "EPSG:3857" },
  "temporal": { "start": "2018-01-01", "end": "2020-12-31" },
  "license": "CC-BY-4.0",
  "provenance": {
    "attribution": "KARS / State of Kansas",
    "retrieved": "2025-09-18T01:50:00Z"
  },
  "outputs": {
    "cog": "data/processed/dem/ks_1m_dem.tif",
    "hillshade": "data/processed/dem/ks_1m_hillshade.tif"
  }
}
```

Historic topo (USGS) in `data/sources/usgs_historic_topo.json`:

```json
{
  "id": "usgs_topo_1894_1950",
  "type": "raster",
  "endpoint": {
    "type": "http",
    "urls": [
      "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/USGS_15x15_1894_Larned_Geo.tif",
      "https://... more ..."
    ]
  },
  "temporal": { "start": "1894-01-01", "end": "1950-12-31" },
  "spatial": { "bbox": [-100.1, 37.9, -98.8, 38.6], "crs": "EPSG:4326" },
  "license": "USGS-PD",
  "provenance": { "attribution": "USGS Historical Topographic Maps" },
  "style": { "opacity": 0.8 }
}
```

---

## STAC item (minimal pattern)

`stac/items/ks_1m_dem.json`:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_1m_dem",
  "properties": {
    "datetime": "2019-06-30T00:00:00Z",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z"
  },
  "geometry": { "type": "Polygon", "coordinates": [[[...]]] },
  "bbox": [-102.1, 36.99, -94.6, 40.0],
  "assets": {
    "cog": {
      "href": "../data/processed/dem/ks_1m_dem.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "hillshade": {
      "href": "../data/processed/dem/ks_1m_hillshade.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["derived"]
    }
  },
  "links": [{ "rel": "collection", "href": "../collections/elevation.json" }]
}
```

---

## Web viewer (MapLibre + time)

* Static `web/` renders COG/tiles and dated overlays.
* Time slider filters layers whose `start/end` bracket the slider year.
* Works from **GitHub Pages** (no server).

`web/app.config.json` (tiny manifest the JS reads):

```json
{
  "title": "Kansas Geo Timeline",
  "layers": [
    { "id": "ks_1m_hillshade", "type": "raster", "url": "./tiles/ks_1m_hillshade/{z}/{x}/{y}.png", "start": 2018, "end": 2020, "opacity": 0.9 },
    { "id": "usgs_topo_1894",  "type": "image",  "url": "./overlays/usgs_1894_larned.tif",               "start": 1894, "end": 1894, "opacity": 0.7 }
  ]
}
```

---

## Google Earth (KML/KMZ)

The `make kml` task emits:

```
earth/
  Kansas_Terrain.kmz
  networklinks/
    ks_1m_hillshade.kml  # regionated GroundOverlays with <Region><Lod> for progressive loading
    usgs_topo_1894.kml
  doc.kml                # master with <NetworkLink> per layer + <Folder> per decade
```

Tips:

* Prefer **Regionation** + **Lod** for large rasters.
* Break long time ranges into **per-decade** folders for quick toggling.

---

## Uncertainty & provenance (built-in)

* Every source JSON includes **license, attribution, retrieved**, CRS, bbox.
* The pipeline stamps artifacts with a **`_meta.json`** (origin, command, timestamp, hash).
* The web UI can optionally show **confidence** (e.g., lower opacity or “± meters” tooltip) if you add `confidence` to layer configs.
* `make check` validates CRS consistency, STAC schema, and that time spans are sane (start ≤ end).

---

## Roadmap (near-term)

1. **Data**: add **historic topo**, **DEM hillshade statewide**, **treaty/railroad** vectors, and one **new**: 1930s Dust Bowl land-use.
2. **Time slider v1**: filter layers by year range; expose **opacity** & **blend** controls.
3. **Earth polish**: per-decade folders, per-county regionation for big overlays.
4. **Provenance**: auto-write `_meta.json` for each output + STAC refresh in `make stac`.
5. **CI**: GitHub Action to run `make check` on PRs and publish `web/` to Pages on `main`.
6. **Story stub**: a single “Santa Fe Trail” story page that toggles prewired layers.
7. **Stretch**: optional **CesiumJS** 3D with time-dynamic hillshade (if terrain tiles available).

---

## Contributing / MCP (optional but nice)

If you want NASA-grade reproducibility:

* `mcp/sops/…` — short SOPs: “Add a map”, “Add a DEM”, “Publish Pages”.
* `mcp/experiments/…` — tiny experiment logs for non-trivial changes (e.g., comparing two hillshade params).
* `mcp/model_cards/…` — if you add ML (e.g., OCR or geocoding), document limits & training data.

---

## Requirements

* **Python 3.10+**, GDAL stack (installed via `requirements.txt` or docker).
* No external accounts required; **Google Earth** is optional for 3D viewing.

---

## Notes & tips

* Set explicit **CRS** and **bounds** in each `data/sources/*.json` to avoid reprojection surprises.
* For very large rasters, host COGs in cloud storage with **HTTP Range Requests**; MapLibre can read via tiles, Google Earth via **GroundOverlay**/**Regionation**.
* Start small: one county end-to-end, then scale out.

---

### Appendices

**A) Minimal `requirements.txt`**

```
rasterio
rio-cogeo
pyproj
shapely
pystac
jsonschema
Pillow
```

**B) GitHub Pages workflow (`.github/workflows/site.yml`)**

```yaml
name: Publish site
on:
  push:
    branches: [ main ]
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt
      - run: make check site
      - uses: actions/upload-pages-artifact@v3
        with: { path: web }
      - uses: actions/deploy-pages@v4
```

**C) `make help` (what users see)**

```make
help:
\t@echo "fetch | cogs | terrain | stac | kml | site | check | reproducibility | clean"
```

---
