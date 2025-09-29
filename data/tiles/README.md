# Kansas-Frontier-Matrix — Web Map Tiles

This directory (`data/tiles/`) is for **ephemeral, build-from-source outputs** — raster and vector tiles  
used for local previews or staging before publishing.  

> ⚠️ **Ignored by Git** (`data/.gitignore`), except this README and any `.gitkeep`.  
> For versioned or distributable tiles, use **Git LFS** in `data/derivatives/tiles/` or `web/tiles/`.

---

## What Goes Here

- **Raster tiles** → pyramids built from COG/GeoTIFF (hillshade, scanned topo mosaics).  
  - Layouts: `/{z}/{x}/{y}.png` (or `.jpg`)  
  - Or single-file **PMTiles** (`.pmtiles`)  

- **Vector tiles** → `pbf` z/x/y sets or **PMTiles** from GeoJSON/GeoPackage.  

> ✅ For long-term reproducibility and CI integration → prefer **PMTiles** (or MBTiles)  
> tracked via Git LFS outside this folder (`data/derivatives/tiles/`, `web/tiles/`).  

---

## Layout & Naming

data/tiles/
├── /           # z/x/y pyramid for local preview
│   └── {z}/{x}/{y}.png
└── .pmtiles    # single-file alternative (preferred for publishing)

Examples:
- `hillshade_2018_2020/…`  
- `usgs_topo_larned_1894/…`  
- `railroads_1900.pmtiles`  

---

## Build Recipes

### 1) Raster → z/x/y PNG/JPEG (quick preview)

```bash
gdal2tiles.py \
  -z 5-14 \
  -r bilinear \
  -s EPSG:3857 \
  -w none \
  data/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif \
  data/tiles/hillshade_2018

Tips:
	•	For COGs, GDAL will use internal overviews efficiently.
	•	Limit zoom levels (-z) to prevent disk bloat.

⸻

2) Raster → PMTiles (single file, portable)

# Requires rio-pmtiles (pip install pmtiles rio-pmtiles)
rio pmtiles create \
  data/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif \
  data/tiles/hillshade_2018.pmtiles \
  --minzoom 5 --maxzoom 14


⸻

3) Vector → MBTiles/PMTiles with Tippecanoe

tippecanoe \
  -o data/tiles/railroads_1900.mbtiles \
  -zg -Z5 -B5 \
  --layer=railroads_1900 \
  data/processed/vectors/ks_railroads.json

pmtiles convert data/tiles/railroads_1900.mbtiles data/tiles/railroads_1900.pmtiles

Or export z/x/y:

mb-util --image_format=pbf data/tiles/railroads_1900.mbtiles data/tiles/railroads_1900/


⸻

Metadata & Provenance

Even if tiles here are ignored, provenance must be preserved:
	•	Create side metadata (*_meta.json) under processed sources.
	•	Store checksums for published PMTiles in data/provenance/registry.json ￼.

Example checksum:

sha256sum data/tiles/railroads_1900.pmtiles > data/tiles/railroads_1900.pmtiles.sha256

When publishing, move .pmtiles + .sha256 to an LFS-tracked path.

⸻

Serving Locally

Static z/x/y tiles

python -m http.server --directory data/tiles 8000
# Access: http://localhost:8000/<layer>_{period}/{z}/{x}/{y}.png

PMTiles (preferred)

MapLibre can read .pmtiles directly:

<script src="https://unpkg.com/pmtiles@3/dist/pmtiles.js"></script>
<script>
  const protocol = new pmtiles.Protocol();
  maplibregl.addProtocol("pmtiles", protocol.tile);

  map.addSource("hillshade", {
    type: "raster",
    tiles: ["pmtiles://data/tiles/hillshade_2018.pmtiles"],
    tileSize: 256
  });
  map.addLayer({ id: "hillshade", type: "raster", source: "hillshade" });
</script>


⸻

Git / LFS Policy
	•	data/tiles/** is ignored.
	•	Committable artifacts → place in:
	•	data/derivatives/tiles/*.pmtiles
	•	web/tiles/*.pmtiles

.gitattributes routes *.pmtiles, *.mbtiles, *.pbf to Git LFS.

⸻

Publishing
	•	Web app → move .pmtiles to web/tiles/ and reference in MapLibre configs (pmtiles:// URLs).
	•	GitHub Releases → attach .pmtiles + .sha256 as immutable assets.
	•	Cloud storage (S3/GCS) → upload and reference with HTTPS URLs.

STAC Items should include links to PMTiles artifacts as "roles": ["tiles"] ￼.

⸻

Suggested Makefile Targets

tile-raster:
\tgdal2tiles.py -z 5-14 -r bilinear -s EPSG:3857 -w none \
\t\tdata/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif \
\t\tdata/tiles/hillshade_2018

tile-vector:
\ttippecanoe -o data/tiles/railroads_1900.mbtiles -zg -Z5 -B5 --layer=railroads_1900 \
\t\tdata/processed/vectors/ks_railroads.json
\tpmtiles convert data/tiles/railroads_1900.mbtiles data/tiles/railroads_1900.pmtiles

tile-clean:
\trm -rf data/tiles/*

.PHONY: tile-raster tile-vector tile-clean


⸻

Notes & Gotchas
	•	Zoom levels → Keep Kansas-wide datasets ≤ z14 unless heavily simplified.
	•	Vector consistency → Always set --layer name in Tippecanoe for stable MapLibre configs.
	•	Reproducibility → STAC Items and provenance registry must point to the source dataset and link to the published .pmtiles.

⸻

✅ This folder is for temporary tile builds only.
Final distributable tiles belong in data/derivatives/tiles/ or web/tiles/, tracked with LFS, linked in STAC, and referenced in the web viewer.

---