# Cloud-Optimized GeoTIFFs (COGs)

This directory holds **final, publishable rasters** for the Kansas-Frontier-Matrix / Kansas Geo Timeline.
They are optimized for **HTTP range reads**, **reproducible builds**, and **clear provenance**.

**Each raster must have:**
- COG layout (internal tiling + overviews)
- WGS84 **EPSG:4326** unless a workflow explicitly requires another CRS
- A **`.tif.sha256`** sidecar (GNU format)
- (Recommended) A **STAC Item** in `stac/items/` describing the asset

> Adding a new dataset? See the **Checklist** at the end of this file.

---

## Layout (by convention)

```

data/
└─ cogs/
├─ dem/
│  ├─ ks_1m_dem_2018_2020.tif
│  └─ ks_1m_dem_2018_2020.tif.sha256
├─ hillshade/
│  ├─ ks_hillshade_2018_2020.tif
│  └─ ks_hillshade_2018_2020.tif.sha256
└─ overlays/
├─ usgs_topo_larned_1894.tif
└─ usgs_topo_larned_1894.tif.sha256

```

> Keep **metadata** in STAC (`stac/items/**`). A lightweight `.meta.json` is optional if you need local,
non-STAC notes, but STAC is the source of truth.

---

## Naming

Use clear, sortable names:

```

<region_or_theme>*<detail>*<temporal>.tif

````

Examples:
- `ks_1m_dem_2018_2020.tif`
- `ks_hillshade_2018_2020.tif`
- `usgs_topo_larned_1894.tif`

If there are multiple styles of the same product, suffix with the style:
`ks_hillshade_2018_2020_multidir.tif`.

---

## Create / Convert

### Fast path (project script)

**Raster → COG (lossless, deflate):**
```bash
python scripts/convert.py raster-to-cog \
  data/raw/maps/usgs_topo_larned_1894_raw.tif \
  data/cogs/overlays/usgs_topo_larned_1894.tif
````

**Raster → COG (photographic scans, smaller, WebP profile):**

```bash
python scripts/convert.py raster-to-cog \
  --web-optimized \
  data/raw/scans/relief_tint_1938.tif \
  data/cogs/overlays/relief_tint_ks_1938.tif
```

The script will:

* reproject to **EPSG:4326** if needed,
* build overviews (auto),
* and write a `.sha256` sidecar.

### GDAL (canonical options)

**DEM (float32, lossless):**

```bash
gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  <input_dem_wgs84.tif> data/cogs/dem/ks_1m_dem_2018_2020.tif
```

**Hillshade (uint8, lossless):**

```bash
gdaldem hillshade -alt 45 -az 315 -compute_edges \
  data/cogs/dem/ks_1m_dem_2018_2020.tif /tmp/ks_hillshade_2018_2020.tif

gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/ks_hillshade_2018_2020.tif data/cogs/hillshade/ks_hillshade_2018_2020.tif
```

**Historic map overlays (RGB, JPEG-in-COG):**

```bash
# 1) Reproject to EPSG:4326 (keep alpha for cutlines)
gdalwarp -t_srs EPSG:4326 -r cubic -dstalpha \
  <source_georef.tif> /tmp/usgs_topo_larned_1894_wgs84.tif

# 2) Convert to COG with JPEG/YCBCR
gdal_translate -of COG \
  -co COMPRESS=JPEG -co QUALITY=85 -co PHOTOMETRIC=YCBCR \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/usgs_topo_larned_1894_wgs84.tif data/cogs/overlays/usgs_topo_larned_1894.tif
```

---

## CRS guidance

* Web overlays default to **EPSG:4326** for viewer compatibility.
* For source processing, Kansas DEM/LiDAR often uses **UTM 14N**

  * EPSG: **26914** (NAD83) or **6344** (NAD83(2011))
* If you reproject, document it in STAC properties (processing notes).

---

## STAC registration

Emit a STAC Item for every COG:

**Python API:**

```python
from kansas_geo_timeline.ingest import ingest_raster
out, item = ingest_raster("data/raw/scans/usgs_topo_larned_1894.tif",
                          out_dir="data/cogs/overlays",
                          profile="deflate",
                          stac_items_dir="stac/items",
                          stac_collection="kfm-overlays")
print(out, item["id"])
```

**Or via Make:**

```bash
make stac stac-validate-items
```

STAC items live under `stac/items/**` and include bbox, file stats, and SHA-256.

---

## Web integration

COGs are best served as **tiles** (PNG/JPEG) or **PMTiles**. Add your layer to `web/data/*.json` or generate from STAC.

Example (raster overlay):

```json
{
  "id": "usgs_topo_larned_1894",
  "title": "USGS Topo (Larned, 1894)",
  "type": "raster",
  "data": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "category": "cartography",
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "opacity": 0.8,
  "visible": false,
  "attribution": "USGS (Public Domain)"
}
```

> If you’re using a tiler, reference the tile URL(s) instead of the raw COG.
> For PMTiles, use a `pmtiles://…` URL and ensure the protocol handler is registered.

---

## Validation & QA

```bash
# Verify checksum sidecars
find data/cogs -name "*.tif.sha256" -print0 | xargs -0 -I{} sha256sum -c {}

# Quick gdalinfo checks
gdalinfo data/cogs/dem/ks_1m_dem_2018_2020.tif | head -n 40

# Optional: COG structure validation (rio-cogeo)
rio cogeo validate data/cogs/overlays/usgs_topo_larned_1894.tif
```

---

## Troubleshooting

* **Jagged at small scales** → ensure overviews exist (reconvert).
* **Washed out colors** → prefer `DEFLATE` for line art/labels; JPEG/WebP for photos only.
* **Huge file** → `--web-optimized` (script) or `COMPRESS=JPEG QUALITY=80–85`.
* **Seams/misalignment** → verify georeferencing before COG conversion.

---

## Checklist (add a new raster)

1. Convert to **COG** in `data/cogs/<subdir>/<name>.tif` (use script or GDAL).
2. Write **checksum** → `<name>.tif.sha256`.
3. Generate **STAC Item** in `stac/items/**` (`ingest_raster` or `make stac`).
4. (If web) Expose tiles or PMTiles and add a layer config under `web/data/`.
5. Run validation (`sha256sum -c`, `gdalinfo`, optional `rio cogeo validate`).
6. Commit — CI will validate and publish.

---

## Notes for maintainers

* Large rasters: track with **Git LFS or DVC**; only checksums + STAC in git.
* Prefer **tile size 512**; it performs better for large rasters.
* For continuous rasters: **DEFLATE + PREDICTOR=2**.
  For photographic scans: **JPEG/YCBCR** (quality ~85) or the script’s **WebP** profile.

```
```
