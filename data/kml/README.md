# KML / KMZ Exports

This folder holds **Google Earth–ready** exports of our rasters and vectors:
- Regionated KML/KMZ **super-overlays** of large rasters (DEM hillshade, georef’d historic topos).
- Lightweight KMLs for vectors (treaties, railroads, trails).
- Small JSON sidecars (`*.meta.json`) for provenance + traceability (MCP-style).

> Tip: Prefer **KMZ** (zipped KML + assets) for distribution; aim to keep each file < ~100–200 MB.

---

## What belongs here

- `*.kmz` — regionated raster super-overlays for Google Earth.
- `*.kml` — vectors (and very small rasters).
- `*.meta.json` — optional per-export metadata (who/when/how, inputs, checksums).
- `README.md` — this doc.

We **do not** stage raw/processed COGs or GeoJSON here; those live under `data/cogs/**` and `data/processed/**`.  
This directory is strictly for **Earth viewer** exports.

---

## Conventions

### CRS
- Google Earth renders in geographic WGS84. Export tools will reproject as needed.
- Sources may be any CRS; record the source CRS in the meta.

### Naming
```

<topic>\[\_<year-or-range>].kmz
e.g.,
ks\_hillshade\_2018\_2020.kmz
usgs\_topo\_larned\_1894.kmz
treaties.kml
railroads\_1900.kml

````

### Metadata (optional but recommended)
Create a `*.meta.json` alongside the KML/KMZ:
```json
{
  "id": "usgs_topo_larned_1894_kmz",
  "title": "USGS Topo – Larned (1894), KMZ Super-Overlay",
  "source_raster": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "export_tool": "gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG",
  "processing": "Auto-regionated pyramid inside KMZ",
  "rms_georef_m": 8.6,
  "license": "Public Domain (USGS)",
  "created": "2025-09-19T20:30:00Z",
  "sha256": "<optional checksum of KMZ>"
}
````

---

## How to generate

### A) Raster → **KMZ super-overlay** (recommended for large rasters)

**GDAL translate (one-liner):**

```bash
gdal_translate -of KMLSUPEROVERLAY \
  -co FORMAT=PNG \                    # PNG preserves transparency; use JPEG for photos
  data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  data/kml/ks_hillshade_2018_2020.kmz
```

**Alternative (explicit KML tree → zip yourself):**

```bash
gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG input.tif out_folder   # writes out_folder/doc.kml + tiles/
zip -r data/kml/out.kmz out_folder
```

> Notes:
>
> * Use `FORMAT=PNG` for overlays with transparency (hillshade, historic map collars).
> * Use `FORMAT=JPEG` for photographic rasters without transparency (smaller KMZ).

### B) Vector (GeoJSON/GeoPackage/SHP) → **KML**

```bash
# Treaties (polygon)
ogr2ogr -f KML data/kml/treaties.kml data/processed/vectors/treaties.geojson \
  -dsco NameField=name -select id,name,year

# Railroads circa 1900 (line)
ogr2ogr -f KML data/kml/railroads_1900.kml data/processed/vectors/railroads_1900.geojson \
  -nlt PROMOTE_TO_MULTI -select id,name,year
```

### C) Color-relief or styled rasters (optional pre-step)

```bash
gdaldem color-relief \
  data/processed/dem/ks_1m_dem.tif \
  configs/colorramps/hillshade.txt \
  /tmp/ks_hillshade_rgba.tif

gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG \
  /tmp/ks_hillshade_rgba.tif data/kml/ks_hillshade_2018_2020.kmz
```

---

## Makefile snippets (drop into project `Makefile`)

```make
KML_DIR := data/kml

# --- Raster → KMZ (expects COGs or processed GeoTIFFs) -----------------
$(KML_DIR)/%.kmz: data/cogs/hillshade/%.tif
	@mkdir -p $(KML_DIR)
	gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG $< $@

# Historic topo overlays
$(KML_DIR)/usgs_topo_%.kmz: data/cogs/overlays/usgs_topo_%.tif
	@mkdir -p $(KML_DIR)
	gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG $< $@

# --- Vectors → KML -----------------------------------------------------
$(KML_DIR)/%.kml: data/processed/vectors/%.geojson
	@mkdir -p $(KML_DIR)
	ogr2ogr -f KML $@ $<

.PHONY: kml-all
kml-all: \
	$(KML_DIR)/ks_hillshade_2018_2020.kmz \
	$(KML_DIR)/treaties.kml \
	$(KML_DIR)/railroads_1900.kml
```

Usage:

```bash
make data/kml/ks_hillshade_2018_2020.kmz
make data/kml/treaties.kml
```

---

## Quality & troubleshooting

* **KMZ too large?** Crop or downsample first:

  ```bash
  gdalwarp -te <minx> <miny> <maxx> <maxy> -r bilinear in.tif /tmp/crop.tif
  ```
* **Seams/blur at certain zooms?** Export from the highest-resolution source; avoid pre-pyramids in the input TIFF.
* **Transparency missing?** Ensure the source has an alpha band or a proper `NODATA` set before export; prefer `-co FORMAT=PNG`.
* **Label clutter (vectors)?** Simplify/trim attributes:

  ```bash
  ogr2ogr -simplify 0.0005 -select id,name,year -f KML out.kml src.geojson
  ```
* **Wrong layer names?** Use `-dsco NameField=<field>` (dataset name) or `-lco NameField=<field>` (layer name) with `ogr2ogr`.

---

## Checklist before committing

* ✅ Opens cleanly in **Google Earth Pro** (desktop).
* ✅ Reasonable size (prefer **KMZ**).
* ✅ `*.meta.json` present (provenance, tool/version, dates).
* ✅ Titles/descriptions are non-developer friendly.
* ✅ If derived from project data, input paths recorded in meta.

---

## Examples to stage next

* `ks_hillshade_2018_2020.kmz` — DEM hillshade super-overlay.
* `usgs_topo_larned_1894.kmz` — georef’d historic topo super-overlay.
* `treaties.kml` — treaty/reservation polygons.
* `railroads_1900.kml` — 1900 lines for time-slider demos.

```
