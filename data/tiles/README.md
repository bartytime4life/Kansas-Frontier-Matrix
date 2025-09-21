# `data/tile/` — Web Map Tiles (Raster & Vector)

> Ephemeral, build-from-source outputs. This folder is **ignored by Git** (see `data/.gitignore`) except for this README (and any `.gitkeep` you add). Use it for local previews or staging before publishing tiles as versioned artifacts elsewhere (e.g., `web/`, releases, or object storage).

## What goes here

- **Raster tiles**: pyramids from COG/GeoTIFF (e.g., hillshade, scanned topo mosaics)
  - Layouts: `/{z}/{x}/{y}.png` (or `.jpg`), or single-file **PMTiles** (`.pmtiles`)
- **Vector tiles**: `pbf` sets or single-file **PMTiles** built from GeoJSON/GeoPackage

> For long-term storage and CI reproducibility, prefer single-file **PMTiles** or **MBTiles** committed via **Git LFS** outside this folder (e.g., `data/derivatives/tiles/` or `web/tiles/`).

---

## Naming

```

data/tile/
├── <layer>*<period>/           # z/x/y pyramid for quick local preview
│   └── {z}/{x}/{y}.png
└── <layer>*<period>.pmtiles    # single-file alternative for publishing

````

Examples:
- `hillshade_2018_2020/…`
- `usgs_topo_larned_1894/…`
- `roads_1930s.pmtiles`

---

## Build recipes

### 1) Raster → z/x/y PNG/JPEG (quick preview)

Using `gdal2tiles.py`:

```bash
gdal2tiles.py \
  -z 5-14 \
  -r bilinear \
  -s EPSG:3857 \
  -w none \
  data/processed/hillshade/ks_hillshade_2018_2020.tif \
  data/tile/hillshade_2018_2020
````

Tips:

* For COGs, GDAL will read overviews efficiently.
* Use `-z` to cap zoom levels; deeper zooms explode disk usage.

### 2) Raster → PMTiles (single file)

Using `rio pmtiles` (rasterio-pmtiles) or `cog2pmtiles`:

```bash
# rasterio-pmtiles (install: pip install pmtiles rio-pmtiles)
rio pmtiles create \
  data/processed/hillshade/ks_hillshade_2018_2020.tif \
  data/tile/hillshade_2018_2020.pmtiles \
  --minzoom 5 --maxzoom 14
```

### 3) Vector (GeoJSON) → PBF (z/x/y) with tippecanoe

```bash
tippecanoe \
  -o data/tile/roads_1930s.mbtiles \
  -zg -Z5 -B5 \
  --coalesce --drop-densest-as-needed \
  --layer=roads_1930s \
  data/processed/vectors/roads_1930s.geojson
```

Convert MBTiles → PMTiles (optional):

```bash
pmtiles convert data/tile/roads_1930s.mbtiles data/tile/roads_1930s.pmtiles
```

Or export z/x/y:

```bash
mb-util --image_format=pbf data/tile/roads_1930s.mbtiles data/tile/roads_1930s/
```

---

## Metadata & checksums

Even though this folder is ignored, you should still produce side metadata for provenance:

* `*_meta.json` alongside the source artifacts in `data/processed/**`
* `*.sha256` for any published PMTiles/MBTiles (usually stored **outside** `data/tile/`)

Example checksum:

```bash
sha256sum data/tile/roads_1930s.pmtiles > data/tile/roads_1930s.pmtiles.sha256
```

(For committed artifacts, move both files to your LFS-tracked path before committing.)

---

## Serving locally

### Static z/x/y directory

Any static file server works:

```bash
python -m http.server --directory data/tile 8000
# tiles at: http://localhost:8000/<layer>_<period>/{z}/{x}/{y}.png
```

### PMTiles (no server needed)

MapLibre can read `.pmtiles` directly via the PMTiles plugin.

```html
<script src="https://unpkg.com/pmtiles@3/dist/pmtiles.js"></script>
<script>
  const protocol = new pmtiles.Protocol();
  maplibregl.addProtocol("pmtiles", protocol.tile);
  const url = "pmtiles://data/tile/roads_1930s.pmtiles";

  map.addSource("roads", {
    type: "vector",
    url,                    // PMTiles vector source
  });
  map.addLayer({
    id: "roads-line",
    type: "line",
    source: "roads",
    "source-layer": "roads_1930s",   // tippecanoe layer name
    paint: { "line-width": 1.2 }
  });
</script>
```

For raster PMTiles:

```javascript
map.addSource("hillshade", {
  type: "raster",
  tiles: ["pmtiles://data/tile/hillshade_2018_2020.pmtiles"],
  tileSize: 256
});
map.addLayer({ id: "hillshade", type: "raster", source: "hillshade", paint: { "raster-opacity": 0.75 }});
```

---

## Git/LFS policy

* `data/tile/**` is **ignored** to keep the repo light and CI fast.
* If you need to commit distributable single-file tiles, place them in an **LFS-tracked** path such as:

  * `data/derivatives/tiles/*.pmtiles` or
  * `web/tiles/*.pmtiles`
* `.gitattributes` already routes `*.pmtiles`, `*.mbtiles`, and `*.pbf` to **Git LFS**.

---

## Publishing

* **GitHub Pages / web app**: move `.pmtiles` to `web/tiles/` (LFS) and reference with `pmtiles://` URLs in your MapLibre config.
* **Releases**: attach `.pmtiles`/`.mbtiles` plus `*.sha256` to a GitHub Release for immutable distribution.
* **Object storage (S3/GCS)**: upload and reference via `https://…/roads_1930s.pmtiles` (use `pmtiles://` custom protocol mapping if desired).

---

## Make targets (suggested)

Add to your `Makefile`:

```makefile
tile-raster:
\tgdal2tiles.py -z 5-14 -r bilinear -s EPSG:3857 -w none \\
\t\tdata/processed/hillshade/ks_hillshade_2018_2020.tif \\
\t\tdata/tile/hillshade_2018_2020

tile-vector:
\ttippecanoe -o data/tile/roads_1930s.mbtiles -zg -Z5 -B5 --layer=roads_1930s \\
\t\tdata/processed/vectors/roads_1930s.geojson
\tpmtiles convert data/tile/roads_1930s.mbtiles data/tile/roads_1930s.pmtiles

tile-clean:
\trm -rf data/tile/*

.PHONY: tile-raster tile-vector tile-clean
```

---

### Notes & gotchas

* Deep zoom levels (`z>=16`) grow fast; keep Kansas-wide layers to \~`z<=14` unless heavily generalized.
* Prefer **PMTiles** for portability and easier hosting; keep raw z/x/y only for quick local checks.
* Ensure vector layers declare a stable **layer name** (`--layer`) so your style JSONs remain consistent.

```
```

