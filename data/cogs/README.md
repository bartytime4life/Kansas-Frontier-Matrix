# Cloud-Optimized GeoTIFFs (COGs)

This directory holds **final, publishable rasters** used by the Kansas-Frontier-Matrix.
- Mission: fast HTTP range-reads, reproducible derivations, and clean provenance.
- Each raster ships with **metadata sidecars** (`*.meta.json`, `*.tif.sha256`) and, optionally, a **STAC Item**.

> Adding a new dataset? Follow the **Checklist** and copy a template below.

---

## Directory layout

```

data/
└─ cogs/
├─ dem/
│  ├─ ks\_1m\_dem\_2018\_2020.tif
│  ├─ ks\_1m\_dem\_2018\_2020.meta.json
│  └─ ks\_1m\_dem\_2018\_2020.tif.sha256
├─ hillshade/
│  ├─ ks\_hillshade\_2018\_2020.tif
│  ├─ ks\_hillshade\_2018\_2020.meta.json
│  └─ ks\_hillshade\_2018\_2020.tif.sha256
└─ overlays/
├─ usgs\_topo\_larned\_1894.tif
├─ usgs\_topo\_larned\_1894.meta.json
└─ usgs\_topo\_larned\_1894.tif.sha256

````

---

## Naming conventions

- **Filename**: `{region_or_theme}_{detail}_{temporal}.tif`  
  Examples: `ks_1m_dem_2018_2020.tif`, `ks_hillshade_2018_2020.tif`, `usgs_topo_larned_1894.tif`
- **Sidecars**: same stem with `.meta.json`, `.tif.sha256`
- **Preview** (optional): `{stem}_preview.png`

---

## Required sidecars

### 1) SHA-256

```bash
sha256sum data/cogs/<subdir>/<name>.tif \
  | awk '{print $1"  "$2}' \
  > data/cogs/<subdir>/<name>.tif.sha256
````

Validate later with `sha256sum -c`.

### 2) `.meta.json` (compact, non-STAC)

Include:

* `id`, `type`, `title`, `description`, `collection`
* `spatial` (bbox, resolution, `proj.epsg`)
* `temporal` (start/end)
* `files` (local path, optional remote, size\_bytes?, sha256 path)
* `processing` (software, commands, COG profile)
* `validation` checks
* `providers`, `license`, `keywords`
* Optional links to a **STAC** item

See examples in:

* `dem/ks_1m_dem_2018_2020.meta.json`
* `hillshade/ks_hillshade_2018_2020.meta.json`
* `overlays/usgs_topo_larned_1894.meta.json`

---

## COG profiles (canonical commands)

### DEM (float32, lossless)

```bash
gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  <input_dem.tif> data/cogs/dem/ks_1m_dem_2018_2020.tif
```

### Hillshade (uint8, lossless)

```bash
# Derive hillshade (robust defaults), then COG
gdaldem hillshade -alt 45 -az 315 -compute_edges \
  data/cogs/dem/ks_1m_dem_2018_2020.tif /tmp/ks_hillshade_2018_2020.tif

gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/ks_hillshade_2018_2020.tif data/cogs/hillshade/ks_hillshade_2018_2020.tif
```

> Prefer `-multidirectional` for softer statewide visuals (slower).

### Historical map overlays (RGB, JPEG-in-COG)

```bash
# Warp scanned sheet (GCP/TPS recommended) to EPSG:4326 for web overlay
gdalwarp -t_srs EPSG:4326 -r cubic -dstalpha \
  <source_georef.tif> /tmp/usgs_topo_larned_1894_wgs84.tif

# COG with JPEG/YCBCR (small & fast)
gdal_translate -of COG \
  -co COMPRESS=JPEG -co QUALITY=85 \
  -co PHOTOMETRIC=YCBCR \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/usgs_topo_larned_1894_wgs84.tif data/cogs/overlays/usgs_topo_larned_1894.tif
```

---

## CRS guidance

* Web overlays: **EPSG:4326** (or 3857 if tiling that way).
* LiDAR/DEM work in Kansas commonly uses **UTM 14N**:

  * EPSG: **26914** (NAD83) or **6344** (NAD83(2011))
* Record actual CRS in each `.meta.json` under `spatial.proj.epsg`.
* If reprojected, document the warp in `processing.commands`.

---

## Validation & QA

```bash
# JSON sidecars
find data/cogs -name "*.meta.json" -print0 | xargs -0 -I{} jq -e 'type=="object"' {}

# Checksums
find data/cogs -name "*.tif.sha256" -print0 | xargs -0 -I{} sha256sum -c {}

# Quick gdalinfo spot checks
gdalinfo data/cogs/dem/ks_1m_dem_2018_2020.tif | head -n 40
gdalinfo data/cogs/hillshade/ks_hillshade_2018_2020.tif | head -n 40
gdalinfo data/cogs/overlays/usgs_topo_larned_1894.tif | head -n 40
```

> CI also validates STAC under `data/stac/` and enforces sidecar presence.

---

## (Optional) STAC items

Place items under `data/stac/items/<theme>/<item>.json` and link from the meta:

* `items/dem/ks_1m_dem_2018_2020.json`
* `items/hillshade/ks_hillshade_2018_2020.json`
* `items/overlays/usgs_topo_larned_1894.json`

Use STAC extensions: **projection**, **raster**, **file**, **processing**.
Populate `assets.roles`, `raster:bands`, and `file:checksum` (sha256).

---

## MapLibre / web integration (tiler-backed)

COGs are containers; serve tiles (PNG/JPEG or PMTiles) for web maps.

```json
// web/sources/ks_hillshade_2018_2020.json
{
  "id": "ks_hillshade_2018_2020",
  "type": "raster",
  "tiles": ["https://<tiler>/raster/ks_hillshade_2018_2020/{z}/{x}/{y}.png"],
  "tileSize": 256,
  "maxzoom": 14,
  "attribution": "USGS 3DEP, Kansas DASC (Public Domain)"
}
```

```json
// web/sources/ks_1m_dem_2018_2020.json
{
  "id": "ks_1m_dem_2018_2020",
  "type": "raster-dem",
  "encoding": "terrarium",
  "tiles": ["https://<tiler>/terrain/ks_1m_dem_2018_2020/{z}/{x}/{y}.png"],
  "tileSize": 256,
  "maxzoom": 14,
  "attribution": "USGS 3DEP, Kansas DASC (Public Domain)"
}
```

For **PMTiles**, reference `pmtiles://…` and ensure a PMTiles protocol handler is registered.

---

## Checklist (add a new raster)

1. **Write COG** to `data/cogs/<subdir>/<name>.tif` using the correct profile.
2. **Create checksum** → `<name>.tif.sha256`.
3. **Create `.meta.json`** (copy a template and edit).
4. (Optional) **Create STAC item** in `data/stac/items/**` and link it.
5. (If web) **Expose tiles** or PMTiles and add a `web/sources/*.json`.
6. **Run validation** (jq, sha256sum, gdalinfo).
7. **Commit** — CI validates and publishes.

---

## Notes for maintainers

* Large rasters must be tracked with **Git LFS / DVC**; git stores **checksums + meta** only.
* `.gitattributes` should mark common raster formats as binary and set LFS filters for `data/cogs/**`.
* Prefer **tile size 512** for big rasters (better range-read behavior).
* Use **DEFLATE+PREDICTOR=2** for continuous rasters; **JPEG/YCBCR (Q≈85)** for scanned RGB overlays.

```
```
