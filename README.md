# Kansas Geo Timeline — Time · Terrain · History

This repo is a minimal, **Google Earth + Web (GitHub Pages)** mapping system for Kansas elevation and historical layers.

- **Earth deliverables**: regionated KML/KMZ (progressive loading via NetworkLinks)
- **Web app**: lightweight MapLibre viewer served by GitHub Pages
- **Data model**: STAC-like JSON for sources and time spans
- **Pipelines**: Makefile targets to fetch → COG → derivatives (slope/aspect/hillshade) → KML → site

> Created 2025-09-18 01:38:08 UTC. Fill in the ArcGIS/USGS endpoints in `data/sources/*.json` (examples included).
> Then run `make help` for the workflow.

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

## Folders

```
data/          # inputs/outputs (COGs, KMZ, JSON metadata)
scripts/       # small, dependency-light tools
web/           # static site (MapLibre) for GitHub Pages
stac/          # static catalog of layers with time metadata
docker/        # optional container environment
```

## Notes

- **No external accounts required**; Earth Engine optional later.
- Set explicit CRS and bounds in source JSON to avoid surprises.
- For very large rasters, host COGs in cloud storage with range requests enabled; MapLibre can read via tile endpoints, Google Earth via GroundOverlay/Regionation.
