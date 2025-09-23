Kansas Geo Timeline — Time · Terrain · History

A minimal Google Earth + Web (GitHub Pages) mapping system for Kansas elevation and historical layers.
	•	Earth deliverables: regionated KML/KMZ (progressive loading via NetworkLinks)
	•	Web app: lightweight MapLibre viewer with a time slider
	•	Catalog: STAC 1.0.0 (Catalog → Collections → Items) for clean provenance
	•	Pipelines: Makefile targets to fetch → COG → derivatives (slope/aspect/hillshade) → site
	•	CLI: kgt for STAC validation/listing and viewer-config rendering

Start small (one county), then scale out. Keep STAC tight and versioned.

⸻

Table of contents
	•	Quickstart
	•	Repository layout
	•	Install
	•	Make targets
	•	Data sources (examples)
	•	STAC structure
	•	CLI (kgt) usage
	•	Web viewer (MapLibre + time)
	•	Google Earth (KML/KMZ)
	•	Checks & reproducibility
	•	CI: GitHub Pages publish
	•	Troubleshooting
	•	Roadmap

⸻

Quickstart

# Python env (3.10+ recommended)
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# 1) Configure sources (edit data/sources/*.json)
# 2) Build a tiny slice end-to-end
make fetch
make cogs
make terrain
make stac

# 3) Validate STAC + render viewer config
kgt validate-stac stac/items --no-strict
kgt render-config --stac stac/items --output web/app.config.json --pretty

# 4) Serve the viewer locally
python -m http.server -d web 8080

Prefer make stac-validate if you’re using the repo’s validator scripts.

⸻

Repository layout

data/                        # inputs/outputs (COGs, JSON metadata)
  sources/                   # source descriptors (endpoints, CRS, bounds, license)
  processed/                 # generated COGs/tiles and artifacts
stac/                        # STAC 1.0.0: catalog + collections + items
  catalog.json
  collections/
    elevation.json           # elevation/terrain collection
    historic_topo.json       # historical topo overlays collection
  items/
    ks_1m_dem_2018_2020.json                 # DEM item
    overlays/
      usgs_topo_larned_1894.json             # overlay map item
scripts/                     # small, dependency-light tools (Python/bash)
web/                         # static site (MapLibre) for GitHub Pages
docker/                      # container env (reproducible build)
mcp/                         # SOPs/experiments/model cards (reproducibility)


⸻

Install

pip install -r requirements.txt
# optional extras for CLI features
pip install "jsonschema>=4.0" "jinja2>=3.1"

Expose the CLI (already wired via pyproject.toml):

[project.scripts]
kgt = "kansas_geo_timeline.cli:main"


⸻

Make targets

make help               # show all tasks
make fetch              # download/input prep via data/sources/*.json
make cogs               # convert rasters to Cloud Optimized GeoTIFFs (COGs)
make terrain            # derive hillshade/slope/aspect from DEMs
make stac               # (re)generate stac/{items,collections}
make stac-validate      # validate sources + STAC (uses scripts/ or kgt fallback)
make site               # write a simple web/layers.json (always available)
make site-config        # render web/app.config.json via kgt + Jinja2 (if template present)
make clean              # remove intermediates (keeps ./stac)

Tip: run make stac-validate before committing. It catches most wiring mistakes.

⸻

Data sources (examples)

Create data/sources/ks_dem.json:

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

Historic topo in data/sources/usgs_historic_topo.json:

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


⸻

STAC structure

Root catalog: stac/catalog.json
Collections:
	•	Elevation → stac/collections/elevation.json
	•	Historic topo overlays → stac/collections/historic_topo.json

Items (examples):
	•	DEM → stac/items/ks_1m_dem_2018_2020.json
	•	Overlay (Larned 1894) → stac/items/overlays/usgs_topo_larned_1894.json

Extensions typically used: projection, checksum (optionally raster, version).

Item link rules:
	•	collection → ../collections/<collection>.json
	•	parent → catalog or collection (your pattern is collection)
	•	root → ../catalog.json
	•	self → the item filename

Validate:

kgt validate-stac stac/items --no-strict

List:

kgt list-stac stac/items --format table


⸻

CLI (kgt) usage

# STAC validation (strict if jsonschema installed)
kgt validate-stac stac/items --report-json build/stac_report.json

# Render viewer manifest (web/app.config.json) from Items (+ optional context JSON)
kgt render-config \
  --stac stac/items \
  --context configs/render_context.json \
  --output web/app.config.json \
  --pretty

# Summarize items
kgt list-stac stac/items --format csv --output build/items.csv

Environment overrides if you keep templates/schemas elsewhere:

export KGT_SCHEMAS_DIR=src/kansas_geo_timeline/schemas
export KGT_TEMPLATES_DIR=src/kansas_geo_timeline/templates


⸻

Web viewer (MapLibre + time)

web/app.config.json (generated via kgt render-config) looks like:

{
  "title": "Kansas Geo Timeline",
  "subtitle": "Historical + geological layers over time",
  "stac_items": [ /* auto-populated */ ]
}

Serve locally:

python -m http.server -d web 8080

The viewer will toggle Items and honor their datetime / start_datetime–end_datetime to filter by year.

⸻

Google Earth (KML/KMZ)

If you maintain regionation scripts, make kml can export:

earth/
  Kansas_Terrain.kmz
  networklinks/
    ks_1m_hillshade.kml
    usgs_topo_1894.kml
  doc.kml

Tips: Region/Lod for large rasters; group decades for quick toggling.

⸻

Checks & reproducibility

Validation
	•	make stac-validate (sources + STAC)
	•	kgt validate-stac stac/items --no-strict (or strict with jsonschema)

Provenance
	•	pipelines stamp _meta.json (origin, command, timestamp, hash)

Hashes
	•	fill checksum:sha256 on assets (e.g., COGs)

Checksum filler (concept):

python - <<'PY'
from pathlib import Path
import json, hashlib
p = Path("stac/items/ks_1m_dem_2018_2020.json")
d = json.loads(p.read_text())
for key in ("dem","hillshade"):
    href = Path(d["assets"][key]["href"])
    if href.exists():
        h = hashlib.sha256(href.read_bytes()).hexdigest()
        d["assets"][key]["checksum:sha256"] = h
p.write_text(json.dumps(d, indent=2))
print("updated checksums")
PY


⸻

CI: GitHub Pages publish

.github/workflows/site.yml:

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
      - run: make stac-validate site
      - uses: actions/upload-pages-artifact@v3
        with: { path: web }
      - uses: actions/deploy-pages@v4


⸻

Troubleshooting
	•	kgt render-config says Jinja2 missing → pip install jinja2.
	•	Validation warns jsonschema missing → pip install jsonschema or run with --no-strict.
	•	Blank map → ensure web/app.config.json exists and assets[*].href are correct; COGs must support HTTP Range.
	•	ArcGIS reprojection oddities → confirm spatial.crs in data/sources/*.json and the COG target CRS (EPSG:4326) match your pipeline.
	•	Item link errors → verify links.collection points at ../collections/<name>.json and links.root is the catalog.

⸻

Roadmap
	1.	Data: historic topo (USGS), statewide hillshade, treaty/railroad vectors; 1930s Dust Bowl land-use.
	2.	Time slider v1: year filter; opacity & blend controls.
	3.	Earth polish: per-decade folders; per-county regionation.
	4.	Provenance: auto _meta.json + STAC refresh in make stac.
	5.	CI: publish web/ on main; run validation on PRs.
	6.	Story stub: “Santa Fe Trail” page toggling prewired layers.
	7.	Stretch: optional CesiumJS 3D if terrain tiles available.

⸻

Requirements

rasterio
rio-cogeo
pyproj
shapely
pystac
jsonschema           # optional but recommended (CLI validation)
jinja2               # optional but recommended (CLI rendering)
Pillow


⸻

Status snapshot

Layer	STAC Item	Asset
DEM (1 m, 2018–2020)	stac/items/ks_1m_dem_2018_2020.json	data/cogs/dem/ks_1m_dem_2018_2020.tif
Hillshade (derived)	same Item (assets.hillshade)	data/cogs/hillshade/ks_hillshade_2018_2020.tif
Historic Topo (Larned 1894)	stac/items/overlays/usgs_topo_larned_1894.json	data/cogs/overlays/usgs_topo_larned_1894.tif

PRs welcome: stick to STAC 1.0.0, keep links relative, and validate before commit.

⸻
