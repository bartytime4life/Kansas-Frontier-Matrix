# `data/cogs/overlays/` — Cloud-Optimized Raster Overlays

This folder stores **web-ready COGs (Cloud-Optimized GeoTIFFs)** used as
map overlays in the Kansas Frontier Matrix / Kansas Geo Timeline viewer
(e.g., historic scans, hillshade, slope classes, fire perimeters,
newspaper map insets, treaty boundary rasters).

**Everything here must be:**
- **COG** (internal tiling + overviews)
- **EPSG:4326 (WGS84)**
- Have **nodata/mask** set correctly
- Have a **`.sha256` sidecar**
- Registered in **STAC** (`stac/items/`)

---

## What belongs here?

- 🗺️ **Scanned historic maps** that you’ve georeferenced
- 🏔️ **Terrain derivatives** (hillshade, slope/aspect renditions)
- 🔥 **Rasterized events** (e.g., wildfire perimeters per date)
- 🧭 **Cartographic textures** (hachures, stipple masks, relief tint)

> Vector data (trails, hydrology lines/polygons, settlements) **does not**
> live here. Keep vectors as GeoJSON in `data/processed/`.

---

## Layout & Naming

```

data/cogs/overlays/
├── hillshade_1m_ks_2018-2020.tif
├── relief_tint_ks_1938.tif
├── usgs_quad_1894_larned.tif
├── treaty_boundaries_1854.tif
└── <name>.tif

```

**Naming convention (recommended):**
```

<theme>*<resolution|scale>*<region>_<year-or-range>.tif

````
Examples: `usgs_quad_1894_larned.tif`, `hillshade_1m_ks_2018-2020.tif`.

---

## COG Specs (house standard)

| Property                | Value / Guidance                                              |
|-------------------------|---------------------------------------------------------------|
| CRS                    | `EPSG:4326`                                                   |
| Tiling                 | 512×512 internal tiles                                        |
| Overviews              | Down to ~512 px min dimension (auto)                          |
| Compression            | `deflate` (lossless) or `webp` (lossy, for photo-like scans)  |
| Mask / NoData          | Internal mask; set `nodata` where appropriate                 |
| Bit depth              | Prefer 8-bit (Byte). Convert if the source allows             |
| Checksums              | Write `<file>.tif.sha256` (GNU format)                        |

---

## Create / Convert

### Option A — Use the project script (recommended)

**Raster → COG (lossless, deflate):**
```bash
python scripts/convert.py raster-to-cog \
  data/raw/maps/usgs_quad_1894_larned_raw.tif \
  data/cogs/overlays/usgs_quad_1894_larned.tif
````

**Raster → COG (photo scans, smaller, webp):**

```bash
python scripts/convert.py raster-to-cog \
  --web-optimized \
  data/raw/scans/relief_tint_1938.tif \
  data/cogs/overlays/relief_tint_ks_1938.tif
```

> The script will reproject to **EPSG:4326**, build overviews, and emit a
> `.sha256` sidecar automatically.

### Option B — Python API (ingest module)

```python
from kansas_geo_timeline.ingest import ingest_raster
out, item = ingest_raster("data/raw/scans/usgs_quad_1894_larned.tif",
                          out_dir="data/cogs/overlays",
                          profile="deflate")
print(out, item["id"])
```

---

## Georeferencing notes

* If your scan is **not** georeferenced yet, use `gdal_translate` with GCPs
  then `gdalwarp` to WGS84 first, **then** convert to COG.
* Crop/deskew before conversion; trim white borders to improve compression.
* For line art / labels, prefer **deflate** to avoid lossy artifacts.

---

## STAC registration

Every overlay COG needs a STAC Item:

* **Automatic** when using `ingest_raster()` (above).
* Or regenerate via Make:

  ```bash
  make stac stac-validate-items
  ```

STAC items appear under `stac/items/`. Each includes bbox, checksum,
file stats, and media type (`image/tiff; application=geotiff; profile=cloud-optimized`).

---

## Wiring to the web viewer

Add/adjust a layer config in `web/data/*.json` (or in your generator):

```json
{
  "id": "relief_tint_1938",
  "title": "Relief Tint (1938)",
  "type": "raster",
  "data": "data/cogs/overlays/relief_tint_ks_1938.tif",
  "category": "terrain",
  "time": { "start": "1938-01-01", "end": "1938-12-31" },
  "opacity": 0.6,
  "visible": false,
  "attribution": "Source: …"
}
```

> Keep legend colors/symbols in `web/config/legend.json` and ensure the file
> path is **relative** so GitHub Pages can serve it.

---

## QA / Validation

* Quick check:

  ```bash
  gdalinfo -checksum data/cogs/overlays/<file>.tif | less
  ```
* Validate COG structure (optional, if `rio-cogeo` CLI available):

  ```bash
  rio cogeo validate data/cogs/overlays/<file>.tif
  ```
* Verify sidecar:

  ```bash
  sha256sum -c data/cogs/overlays/<file>.tif.sha256
  ```

---

## Attribution & Licensing

* Include source, citation, and license in the layer’s **STAC properties** and
  **viewer attribution** field.
* Do **not** include restricted scans. Favor open licenses (CC-BY/CC0).

---

## Troubleshooting

* **Edges look jagged at small scales** → ensure overviews exist; reconvert.
* **Colors washed out** → avoid implicit scaling; keep 8-bit; prefer `deflate`.
* **Heavy file** → try `--web-optimized` (webp) for photographic content.
* **Misaligned** → confirm the scan’s georeferencing before COG conversion.

---

✅ **Mission-grade principle:** Overlays are **clean, verifiable COGs**
with clear provenance. If it’s not reproducible and fast in the viewer,
it doesn’t ship here.

```
```
