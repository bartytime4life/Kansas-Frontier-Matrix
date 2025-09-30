<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Web Map Tiles (`data/tiles/`)

**Mission:** Provide **ephemeral, build-from-source tile outputs** (raster + vector)  
for local preview or staging before publishing.  

📌 This directory is **ignored by Git** (see `data/.gitignore`)  
📌 Final reproducible tiles → store in `data/derivatives/tiles/` or `web/tiles/` via **Git LFS**  
📌 Guarantees **traceability + reproducibility** by requiring provenance sidecars for published tiles  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.pre-commit-config.yaml)

</div>

---

## 🎯 Purpose

- 🗺️ Hold **temporary tile pyramids** (z/x/y or PMTiles) for local map previews.  
- 🔄 Support quick testing of raster & vector layers before final publishing.  
- 🚫 **Do not version raw tiles here** → move to derivatives or `web/tiles/` for LFS-tracked publishing.  

---

## 📂 Directory Layout

```text
[data/tiles/]
├── <layer>/            # z/x/y pyramid for local preview
│   └── {z}/{x}/{y}.png
└── <layer>.pmtiles     # single-file alternative (preferred for publishing)

Examples:
	•	hillshade_2018_2020/…
	•	usgs_topo_larned_1894/…
	•	railroads_1900.pmtiles

⸻

🔧 Build Recipes

1️⃣ Raster → z/x/y PNG/JPEG (preview)

gdal2tiles.py \
  -z 5-14 \
  -r bilinear \
  -s EPSG:3857 \
  -w none \
  data/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif \
  data/tiles/hillshade_2018

Tips:
	•	For COGs, GDAL uses internal overviews efficiently.
	•	Limit zoom levels (-z) to avoid disk bloat.

⸻

2️⃣ Raster → PMTiles (portable, preferred)

# Requires rio-pmtiles
pip install pmtiles rio-pmtiles

rio pmtiles create \
  data/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif \
  data/tiles/hillshade_2018.pmtiles \
  --minzoom 5 --maxzoom 14


⸻

3️⃣ Vector → MBTiles / PMTiles (Tippecanoe)

tippecanoe \
  -o data/tiles/railroads_1900.mbtiles \
  -zg -Z5 -B5 \
  --layer=railroads_1900 \
  data/processed/vectors/ks_railroads.json

pmtiles convert data/tiles/railroads_1900.mbtiles data/tiles/railroads_1900.pmtiles

Or export as z/x/y:

mb-util --image_format=pbf data/tiles/railroads_1900.mbtiles data/tiles/railroads_1900/


⸻

🧾 Metadata & Provenance

Even though this directory is ignored by Git:
	•	📝 Create metadata sidecars (*_meta.json) under processed sources.
	•	🔒 Store checksums for published PMTiles in data/provenance/registry.json.

Example:

sha256sum data/tiles/railroads_1900.pmtiles > data/tiles/railroads_1900.pmtiles.sha256

When publishing, move .pmtiles + .sha256 to LFS-tracked paths.

⸻

🌐 Serving Locally

Static z/x/y tiles

python -m http.server --directory data/tiles 8000
# → http://localhost:8000/<layer>/{z}/{x}/{y}.png

PMTiles (preferred)

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

📦 Git / LFS Policy
	•	data/tiles/** is ignored.
	•	Committable artifacts → place in:
	•	data/derivatives/tiles/*.pmtiles
	•	web/tiles/*.pmtiles

.gitattributes routes *.pmtiles, *.mbtiles, *.pbf → Git LFS.

⸻

🚀 Publishing
	•	Web app: move .pmtiles → web/tiles/ and reference in MapLibre configs (pmtiles:// URLs).
	•	GitHub Releases: attach .pmtiles + .sha256 as immutable assets.
	•	Cloud storage (S3/GCS): upload and reference with HTTPS URLs.
	•	STAC Items should include links to PMTiles artifacts as "roles": ["tiles"].

⸻

🛠 Suggested Makefile Targets

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

⚠️ Notes & Gotchas
	•	Keep Kansas-wide datasets ≤ z14 unless heavily simplified.
	•	Always set --layer in Tippecanoe for stable MapLibre configs.
	•	Ensure reproducibility → STAC Items & provenance registry must link source dataset → published .pmtiles.

⸻

✅ This folder is for temporary tile builds only.
Final distributable tiles belong in data/derivatives/tiles/ or web/tiles/, tracked with LFS and registered in STAC.