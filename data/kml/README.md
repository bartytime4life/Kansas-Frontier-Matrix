# KML / KMZ Exports

This folder holds **Google Earth–ready** exports of our rasters and vectors:
- Regionated KML/KMZ “super-overlays” of big rasters (DEM-derived hillshade, historic topos).
- Lightweight KMLs for vectors (treaties, railroads, trails).
- Small JSON sidecars (`*.meta.json`) to keep provenance + traceability (MCP-style).

> Tip: Use **KMZ** (zipped KML + assets) for distribution; keep individual files < ~100–200 MB when possible.

---

## What belongs here
- `*.kmz`  — regionated raster super-overlays for Google Earth.
- `*.kml`  — simple vector layers (or small rasters).
- `*.meta.json` — optional per-export metadata (who/when/how generated, source paths, checksums).
- `README.md` — this doc.

We **do not** stage raw/processed COGs or GeoJSON here; those live under `data/processed/**`. This directory is strictly for **Earth viewer** exports.

---

## Conventions

**CRS**
- Google Earth renders in geographic WGS84. Export tools will reproject as needed.
- Source rasters/vectors can be any CRS, but record it in the meta.

**Naming**
```

<topic>\[\_<year-or-range>].kmz
e.g., ks\_hillshade\_2018\_2020.kmz
usgs\_topo\_larned\_1894.kmz
treaties.kml
railroads\_1900.kml

````

**Metadata (optional but recommended)**
Create a `*.meta.json` alongside the KML/KMZ:
```json
{
  "id": "usgs_topo_larned_1894_kmz",
  "title": "USGS Topo – Larned (1894), KMZ Super-Overlay",
  "source_raster": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "export_tool": "gdal_translate -of KMLSUPEROVERLAY",
  "processing": "Auto-regionated; internal tiling",
  "rms_georef_m": 8.6,
  "license": "CC-BY-4.0",
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
  data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  data/kml/ks_hillshade_2018_2020.kmz
```

This creates a regionated tile pyramid inside a KMZ suitable for smooth zooming in Google Earth.

**Alternative (explicit KML tree):**

```bash
gdal_translate -of KMLSUPEROVERLAY input.tif out_folder   # emits .kml + tiles folder
zip -r data/kml/out.kmz out_folder
```

### B) Vector (GeoJSON/GeoPackage/SHP) → **KML**

```bash
ogr2ogr -f KML data/kml/treaties.kml data/processed/dem/vectors/treaties.geojson
ogr2ogr -f KML data/kml/railroads_1900.kml data/processed/dem/vectors/railroads_1900.geojson
```

### C) Color-relief or styled rasters

If you need a color ramp before exporting:

```bash
gdaldem color-relief \
  data/processed/dem/ks_1m_dem.tif \
  configs/colorramps/hillshade.txt \
  /tmp/ks_hillshade_rgba.tif

gdal_translate -of KMLSUPEROVERLAY /tmp/ks_hillshade_rgba.tif data/kml/ks_hillshade_2018_2020.kmz
```

---

## Makefile snippets (drop into your project `Makefile`)

```make
KML_DIR := data/kml

$(KML_DIR)/%.kmz: data/cogs/hillshade/%.tif
	@mkdir -p $(KML_DIR)
	gdal_translate -of KMLSUPEROVERLAY $< $@

$(KML_DIR)/%.kml: data/processed/dem/vectors/%.geojson
	@mkdir -p $(KML_DIR)
	ogr2ogr -f KML $@ $<
```

Usage:

```bash
make data/kml/ks_hillshade_2018_2020.kmz
make data/kml/treaties.kml
```

---

## Quality & troubleshooting

* **Huge KMZ?** Crop to AOI or downsample before export:

  ```bash
  gdalwarp -te <minx> <miny> <maxx> <maxy> -r bilinear in.tif /tmp/crop.tif
  ```
* **Seams/blur at certain zooms?** Re-export at full native resolution; avoid pre-pyramids in the source.
* **Transparency missing?** Ensure your source contains an alpha band or a nodata value before export.
* **Label clutter (vectors)?** Pre-simplify and filter attributes:

  ```bash
  ogr2ogr -simplify 0.0005 -select id,name,year -f KML out.kml src.geojson
  ```

---

## Checklist before committing

* ✅ File opens cleanly in **Google Earth** (desktop).
* ✅ Reasonable size (prefer **KMZ**).
* ✅ `*.meta.json` present (provenance, tool/version, dates).
* ✅ Title and description make sense for non-dev users.
* ✅ If derived from a source raster/vector, paths recorded in meta.

---

## Examples to stage next

* `ks_hillshade_2018_2020.kmz` — DEM hillshade super-overlay.
* `usgs_topo_larned_1894.kmz` — georef’d historic topo super-overlay.
* `treaties.kml` — treaty/reservation polygons.
* `railroads_1900.kml` — generalized 1900 lines for time-slider demos.

```
