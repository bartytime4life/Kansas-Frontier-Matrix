# Kansas Geo Timeline — **Time · Terrain · History**

A minimal **Google Earth + Web (GitHub Pages)** mapping system for Kansas elevation and historical layers.

- **Earth deliverables**: regionated **KML/KMZ** (progressive loading via NetworkLinks)
- **Web app**: lightweight **MapLibre** viewer with a **time slider**
- **Catalog**: **STAC 1.0.0** (Catalog → Collections → Items) for clean provenance
- **Pipelines**: `Makefile` targets to **fetch → COG → derivatives (slope/aspect/hillshade) → KML → site**
- **CLI**: `kgt` (Kansas Geo Timeline) for STAC validation, listing, and web-config rendering

> Created 2025-09-18. Keep sources/STAC small at first (one county), then scale out.

---

## Table of contents
- [Quickstart](#quickstart)
- [Repository layout](#repository-layout)
- [Install](#install)
- [Make targets](#make-targets)
- [Data sources (examples)](#data-sources-examples)
- [STAC structure](#stac-structure)
- [CLI (kgt) usage](#cli-kgt-usage)
- [Web viewer (MapLibre + time)](#web-viewer-maplibre--time)
- [Google Earth (KML/KMZ)](#google-earth-kmlkmz)
- [Checks & reproducibility](#checks--reproducibility)
- [CI: GitHub Pages publish](#ci-github-pages-publish)
- [Troubleshooting](#troubleshooting)

---

## Quickstart

```bash
# Python env (3.10+ recommended)
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# 1) Configure sources (edit data/sources/*.json)
# 2) Build a tiny slice end-to-end
make fetch
make cogs
make terrain
make stac
make kml
make site

# 3) Serve the viewer locally
python -m http.server -d web 8080

# 4) Validate STAC + render viewer config
kgt validate-stac stac/items/*.json
kgt render-config --stac stac/items --output web/app.config.json --pretty
````

---

## Repository layout

```
data/                        # inputs/outputs (COGs, KMZ, JSON metadata)
  sources/                   # source descriptors (endpoints, CRS, bounds, license)
  processed/                 # generated COGs/tiles and artifacts
stac/                        # STAC 1.0.0: catalog + collections + items
  catalog.json
  collections/
    elevation.json
  items/
    ks_1m_dem_2018_2020.json
scripts/                     # small, dependency-light tools (Python/bash)
web/                         # static site (MapLibre) for GitHub Pages
docker/                      # optional container environment (reproducible build)
mcp/                         # optional SOPs/experiments/model cards (reproducibility)
```

---

## Install

```bash
pip install -r requirements.txt
# optional extras for CLI features
pip install "jsonschema>=4.0" "jinja2>=3.1"
```

Expose the CLI (already wired in `pyproject.toml` if present):

```toml
[project.scripts]
kgt = "kansas_geo_timeline.cli:main"
```

---

## Make targets

```bash
make help               # show all tasks
make fetch              # download/input prep via data/sources/*.json
make cogs               # convert rasters to Cloud Optimized GeoTIFFs (COGs)
make terrain            # derive hillshade/slope/aspect from DEMs
make stac               # (re)generate/refresh stac/*.json (items/links/checks)
make kml                # regionate overlays; emit KML/KMZ with NetworkLinks
make site               # build static web viewer (web/) + manifest
make check              # jsonlint + STAC validate + CRS/bbox/time sanity
make reproducibility    # smoke-test a tiny pipeline slice end-to-end
make clean              # remove intermediates
```

> Tip: run `make check` before committing. It catches most wiring mistakes.

---

## Data sources (examples)

Create a source descriptor in `data/sources/ks_dem.json`:

```json
{
  "id": "ks_dem_1m",
  "title": "Kansas DEM (1 m)",
  "type": "raster-dem",
  "endpoint": {
    "type": "arcgis",
    "url": "https://tiles.kansasgis.org/arcgis/rest/services/Elevation/KS_1m_DEM/ImageServer"
  },
  "spatial": { "bbox": [-102.10, 36.99, -94.60, 40.00], "crs": "EPSG:4326" },
  "temporal": { "start": "2018-01-01", "end": "2020-12-31" },
  "license": "CC-BY-4.0",
  "provenance": {
    "attribution": "KARS / State of Kansas",
    "retrieved": "2025-09-18T01:50:00Z"
  },
  "outputs": {
    "cog": "data/cogs/dem/ks_1m_dem_2018_2020.tif",
    "hillshade": "data/cogs/hillshade/ks_hillshade_2018_2020.tif"
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
      "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/USGS_15x15_1894_Larned_Geo.tif"
    ]
  },
  "temporal": { "start": "1894-01-01", "end": "1950-12-31" },
  "spatial": { "bbox": [-100.10, 37.90, -98.80, 38.60], "crs": "EPSG:4326" },
  "license": "USGS-PD",
  "provenance": { "attribution": "USGS Historical Topographic Maps" },
  "style": { "opacity": 0.8 }
}
```

---

## STAC structure

**Root catalog:** `stac/catalog.json` (links to collections)

**Elevation collection:** `stac/collections/elevation.json` (DEM derivatives; includes `item_assets` and `links`)

**DEM item:** `stac/items/ks_1m_dem_2018_2020.json` (time range, geometry, assets, checksums)

* Uses STAC extensions: `projection`, `checksum`, (optionally) `raster`, `version`
* `links.rel=collection` → `../collections/elevation.json`
* `links.rel=parent`/`root` set accordingly

Validate:

```bash
kgt validate-stac stac/items/*.json
```

List:

```bash
kgt list-stac stac/items --format table
```

---

## CLI (`kgt`) usage

```bash
# STAC validation (strict if jsonschema installed)
kgt validate-stac stac/items --report-json build/stac_report.json

# Render the viewer manifest (web/app.config.json) from Items (+optional context JSON)
kgt render-config \
  --stac stac/items \
  --context configs/render_context.json \
  --output web/app.config.json \
  --pretty

# Summarize items
kgt list-stac stac/items --format csv --output build/items.csv
```

Environment overrides if you keep templates/schemas elsewhere:

```bash
export KGT_SCHEMAS_DIR=src/kansas_geo_timeline/schemas
export KGT_TEMPLATES_DIR=src/kansas_geo_timeline/templates
```

---

## Web viewer (MapLibre + time)

Static `web/` serves tiles/overlays and filters by year range.

`web/app.config.json` (generated via `kgt render-config`):

```json
{
  "title": "Kansas Geo Timeline",
  "subtitle": "Historical + geological layers over time",
  "stac_items": [ /* auto-populated */ ]
}
```

The template (`templates/app.config.json.j2`) receives:

* `stac_items` with `properties._year` injected for convenience
* any extra context merged from `--context` / `--ctx`

Serve locally:

```bash
python -m http.server -d web 8080
```

---

## Google Earth (KML/KMZ)

`make kml` emits:

```
earth/
  Kansas_Terrain.kmz
  networklinks/
    ks_1m_hillshade.kml
    usgs_topo_1894.kml
  doc.kml
```

Tips:

* Use **Region**/**Lod** for large rasters (progressive loading).
* Group decades into folders for quick toggling.

---

## Checks & reproducibility

* **Validation**: `make check` runs JSON lint, STAC checks, CRS/bbox/time sanity.
* **Provenance**: each artifact gets `_meta.json` (origin, command, timestamp, hash).
* **Hashes**: fill `checksum:sha256` for assets (COGs) via a small script or Make rule.

Example checksum filler (concept):

```bash
python - <<'PY'
from pathlib import Path
import json, hashlib
p = Path("stac/items/ks_1m_dem_2018_2020.json")
d = json.loads(p.read_text())
for k in ("dem","hillshade"):
    href = d["assets"][k]["href"]
    h = hashlib.sha256(Path(href).read_bytes()).hexdigest()
    d["assets"][k]["checksum:sha256"] = h
p.write_text(json.dumps(d, indent=2))
print("updated checksums")
PY
```

---

## CI: GitHub Pages publish

`.github/workflows/site.yml`:

```yaml
name: Publish site
on:
  push:
    branches: [ main ]
permissions:
  pages: write
  id-token: write
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt "jsonschema>=4.0" "jinja2>=3.1"
      - run: make check site
      - uses: actions/upload-pages-artifact@v3
        with: { path: web }
      - uses: actions/deploy-pages@v4
```

---

## Troubleshooting

* **`kgt render-config` says Jinja2 missing** → `pip install jinja2`.
* **Validation warns `jsonschema` missing** → `pip install jsonschema` or run with `--no-strict`.
* **Blank map** → check `web/app.config.json` exists and layers’ URLs are reachable (HTTP Range for COGs).
* **ArcGIS source reprojects oddly** → ensure `spatial.crs` and COG target CRS (`EPSG:4326`) match your pipeline.

---

### Requirements

```
rasterio
rio-cogeo
pyproj
shapely
pystac
jsonschema           # optional but recommended (CLI validation)
jinja2               # optional but recommended (CLI rendering)
Pillow
```

---

### Roadmap (near-term)

1. **Data**: historic topo, statewide hillshade, treaty/railroad vectors; 1930s Dust Bowl land-use.
2. **Time slider v1**: year filter; opacity & blend controls.
3. **Earth polish**: per-decade folders; per-county regionation.
4. **Provenance**: auto `_meta.json` + STAC refresh in `make stac`.
5. **CI**: publish `web/` on `main` and run `make check` in PRs.
6. **Story stub**: “Santa Fe Trail” page toggling prewired layers.
7. **Stretch**: optional **CesiumJS** 3D if terrain tiles available.

---
