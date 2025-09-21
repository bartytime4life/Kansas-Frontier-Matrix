# Cloud-Optimized GeoTIFFs (COGs)

This directory holds **final, publishable rasters** used by the Kansas-Frontier-Matrix:
- Mission: fast HTTP range-reads, reproducible derivations, and clean provenance.
- Each raster has **metadata sidecars** (`*.meta.json`, `*.sha256`) and an optional **STAC Item**.

> If you’re adding a new dataset, follow the **Checklist** below and copy one of the templates.

---

## Directory Layout

```

data/
└─ cogs/
├─ dem/
│  ├─ ks\_1m\_dem\_2018\_2020.tif
│  ├─ ks\_1m\_dem\_2018\_2020.meta.json
│  └─ ks\_1m\_dem\_2018\_2020.sha256
├─ hillshade/
│  ├─ ks\_hillshade\_2018\_2020.tif
│  ├─ ks\_hillshade\_2018\_2020.meta.json
│  └─ ks\_hillshade\_2018\_2020.sha256
└─ overlays/
├─ usgs\_topo\_larned\_1894.tif
├─ usgs\_topo\_larned\_1894.meta.json
└─ usgs\_topo\_larned\_1894.sha256

````

---

## Naming Conventions

- **Filename**: `{region_or_theme}_{detail}_{temporal}.tif`
  - Examples: `ks_1m_dem_2018_2020.tif`, `ks_hillshade_2018_2020.tif`, `usgs_topo_larned_1894.tif`
- **Metadata sidecar**: same stem, `.meta.json`
- **Checksum**: same stem, `.sha256`
- **Preview/thumbnail** (optional): `{stem}_preview.png`

---

## Required Sidecars

### 1) SHA-256 checksum

Create after writing the COG:

```bash
sha256sum data/cogs/<subdir>/<name>.tif \
  | awk '{print $1"  " $2}' \
  > data/cogs/<subdir>/<name>.sha256
````

CI runs `sha256sum -c` against this file.

### 2) `.meta.json` (non-STAC)

A compact, pipeline-friendly metadata document that captures:

* `id`, `type`, `title`, `description`, `collection`
* `spatial` (bbox, resolution, `proj.epsg`)
* `temporal` (start/end)
* `files` (local path, s3 path, size\_bytes?, sha256 path)
* `processing` (software, commands, COG profile)
* `validation` checks
* `providers`, `license`, `keywords`
* Optional links to **STAC** item(s)

See examples already in the repo:

* `dem/ks_1m_dem_2018_2020.meta.json`
* `hillshade/ks_hillshade_2018_2020.meta.json`
* `overlays/usgs_topo_larned_1894.meta.json`

---

## COG Profiles

### DEM (float32, lossless)

```bash
gdal_translate \
  -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=YES \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  <input_dem.tif> data/cogs/dem/ks_1m_dem_2018_2020.tif
```

### Hillshade (uint8, lossless)

```bash
# Derive hillshade, then COG
gdaldem hillshade -alt 45 -az 315 \
  data/cogs/dem/ks_1m_dem_2018_2020.tif /tmp/ks_hillshade_2018_2020.tif

gdal_translate \
  -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=YES \
  -co OVERVIEW_RESAMPLING=NEAREST \
  /tmp/ks_hillshade_2018_2020.tif data/cogs/hillshade/ks_hillshade_2018_2020.tif
```

### Historical map overlays (RGB, JPEG-in-COG)

```bash
# Warp scanned sheet to EPSG:4326 for web overlay
gdalwarp -t_srs EPSG:4326 -r cubic -dstalpha -overwrite \
  <source_scan.tif> /tmp/usgs_topo_larned_1894_wgs84.tif

# COG with JPEG compression (smaller, fast)
gdal_translate \
  -of COG \
  -co COMPRESS=JPEG -co QUALITY=85 \
  -co PHOTOMETRIC=YCBCR \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/usgs_topo_larned_1894_wgs84.tif data/cogs/overlays/usgs_topo_larned_1894.tif
```

> Tile/block size: prefer **512×512** for large rasters (better for HTTP range reads).

---

## CRS Guidance

* Web overlays commonly use **EPSG:4326** or **EPSG:3857**.
* LiDAR-derived products in Kansas are often in **UTM Zone 14N**:

  * EPSG: **26914** (NAD83), or **6344** (NAD83(2011))
* Record the actual CRS in `*.meta.json` under `spatial.proj.epsg`.
* If you reproject, document warp parameters in `processing.commands`.

---

## Validation & QA

Run these locally before pushing:

```bash
# JSON sidecars must be valid objects
find data/cogs -name "*.meta.json" -print0 | xargs -0 -I{} jq -e 'type=="object"' {}

# Checksums
find data/cogs -name "*.sha256" -print0 | xargs -0 -I{} sha256sum -c {}

# Quick gdalinfo sanity
gdalinfo data/cogs/dem/ks_1m_dem_2018_2020.tif | head -n 40
gdalinfo data/cogs/hillshade/ks_hillshade_2018_2020.tif | head -n 40
gdalinfo data/cogs/overlays/usgs_topo_larned_1894.tif | head -n 40
```

> CI also validates JSON in `data/stac/` and `data/sources/` and deploys the static site.

---

## (Optional) STAC Items

For discoverability, place matching STAC Items in `data/stac/` and link to them from the sidecar:

* `data/stac/ks_1m_dem_2018_2020.json`
* `data/stac/ks_hillshade_2018_2020.json`
* `data/stac/usgs_topo_larned_1894.json`

STAC Items should use:

* `projection`, `raster`, `file`, `processing` extensions
* Proper `assets.roles`, `raster:bands`, and `file:checksum` (sha256)

---

## MapLibre / Web Integration

COGs are **data containers**; for web maps you’ll typically serve **tiles**:

* **Raster terrain (DEM)** → raster-dem tiles (e.g., Terrarium/Mapzen encoding) or PMTiles
* **Visual layers (hillshade/overlay)** → raster PNG/JPEG tiles or PMTiles

Example source stubs (if using a tiler):

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

> If you use **PMTiles**, reference `pmtiles://…` and ensure a PMTiles protocol handler is registered.

---

## Checklist (add a new raster)

1. **Write raster** to `data/cogs/<subdir>/<name>.tif` using the correct COG profile.
2. **Generate checksum** → `<name>.sha256`.
3. **Create `.meta.json`** (copy an existing one as a template; update fields).
4. (Optional) **Generate STAC Item** in `data/stac/` and link from the meta.
5. (If web) **Expose tiles** or PMTiles and add a `web/sources/*.json` stub.
6. **Run validation** (jq, sha256sum, gdalinfo).
7. **Commit & push** — CI will validate and deploy the site.

---

## Troubleshooting

* **Link checker fails in CI**: ensure `web/` references only deployed paths or absolute URLs.
* **Tiles look blurry**: adjust overview resampling (`AVERAGE` for photos, `NEAREST` for masks/labels).
* **Large downloads**: consider JPEG-in-COG for RGB scans; keep DEM/hillshade lossless.
* **CRS mismatch**: reproject inputs; set `spatial.proj.epsg` correctly and document warp steps.

---

## Templates

Short, copy-paste skeletons for a new dataset:

<details>
<summary><strong>Minimal DEM .meta.json</strong></summary>

```json
{
  "id": "ks_1m_dem_YYYY_YYYY",
  "version": "1.0.0",
  "type": "raster-dem",
  "title": "Kansas 1-Meter DEM (YYYY–YYYY)",
  "description": "Statewide 1 m DEM …",
  "collection": "ks_dem",
  "spatial": { "bbox": [-102.05, 36.99, -94.60, 40.00], "resolution_m": 1.0, "proj": { "epsg": 26914 } },
  "temporal": { "start": "YYYY-01-01", "end": "YYYY-12-31" },
  "files": {
    "cog": {
      "path": "data/cogs/dem/ks_1m_dem_YYYY_YYYY.tif",
      "s3": "s3://…/ks_1m_dem_YYYY_YYYY.tif",
      "media_type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "size_bytes": null,
      "sha256": "data/cogs/dem/ks_1m_dem_YYYY_YYYY.sha256"
    }
  },
  "processing": { "software": { "gdal": "3.6+" }, "commands": [], "cog_profile": { "compress": "DEFLATE", "predictor": 2, "tile_width": 512, "tile_height": 512 } },
  "validation": { "checks": ["jq -e 'type==\"object\"' data/cogs/dem/ks_1m_dem_YYYY_YYYY.meta.json", "sha256sum -c data/cogs/dem/ks_1m_dem_YYYY_YYYY.sha256"] },
  "license": "Public Domain (USGS)",
  "keywords": ["Kansas","DEM"],
  "mcp": { "experiment_id": "EXP-DEM-…", "traceability": { "source_data": "…", "processing": "…", "git_commit": "<commit-hash>" } }
}
```

</details>

<details>
<summary><strong>Minimal Overlay .meta.json</strong></summary>

```json
{
  "id": "usgs_topo_<place>_<year>",
  "version": "1.0.0",
  "type": "raster-map",
  "title": "USGS Topographic Map – <Place> (<Year>)",
  "collection": "usgs_historical_topos",
  "spatial": { "bbox": [minx, miny, maxx, maxy], "proj": { "epsg": 4326 } },
  "temporal": { "start": "<year>-01-01", "end": "<year>-12-31" },
  "files": {
    "cog": {
      "path": "data/cogs/overlays/usgs_topo_<place>_<year>.tif",
      "s3": "s3://…/usgs_topo_<place>_<year>.tif",
      "media_type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "sha256": "data/cogs/overlays/usgs_topo_<place>_<year>.sha256"
    }
  },
  "processing": { "software": { "gdal": "3.6+" }, "commands": [], "cog_profile": { "compress": "JPEG", "quality": 85, "tile_width": 512, "tile_height": 512 } },
  "validation": { "checks": ["jq -e 'type==\"object\"' data/cogs/overlays/usgs_topo_<place>_<year>.meta.json", "sha256sum -c data/cogs/overlays/usgs_topo_<place>_<year>.sha256"] },
  "license": "Public Domain (USGS)",
  "keywords": ["Kansas","topographic map","overlay"],
  "mcp": { "experiment_id": "EXP-USGS-…", "traceability": { "source_data": "…", "processing": "…", "git_commit": "<commit-hash>" } }
}
```

</details>

---

**Owner**: Data Engineering / MCP
**PR label**: `data:cog`

```
```

