<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Tile Layer (`data/tiles/layer/`)

**Mission:** Hold **ephemeral build artifacts** (raster/vector tiles) for a  
**single map layer** — used for local preview or staging prior to publishing.  

📌 Ephemeral only → ignored by Git (except this README).  
📌 Final reproducible tiles must be published via LFS in  
`data/derivatives/tiles/` or `web/tiles/`.  
📌 Guarantees **traceability + reproducibility** via metadata + checksums.  

</div>

---

## 🎯 Purpose

- 🗺️ Store the **z/x/y tile pyramid** or single-file `.pmtiles` for this layer.  
- 🔄 Allow quick **local preview** before publishing.  
- 🚫 Do not track raw tiles here — only final `.pmtiles` are moved to LFS paths.  

---

## 📂 Directory Layout

```text
[data/tiles/layer/]
├── {z}/{x}/{y}.png        # raster pyramid (optional, preview only)
├── layer.pmtiles          # single-file portable tileset (preferred)
└── README.md


⸻

🔧 Build Recipes

Raster → PMTiles

rio pmtiles create \
  data/processed/<source>.tif \
  data/tiles/layer/layer.pmtiles \
  --minzoom 5 --maxzoom 14

Vector → PMTiles

tippecanoe \
  -o data/tiles/layer/layer.mbtiles \
  -zg -Z5 -B5 --layer=layer \
  data/processed/<source>.json

pmtiles convert data/tiles/layer/layer.mbtiles data/tiles/layer/layer.pmtiles


⸻

🧾 Metadata & Provenance
	•	Create a sidecar _meta.json in data/processed/ for the source.
	•	Store checksums when publishing:

sha256sum data/tiles/layer/layer.pmtiles > data/tiles/layer/layer.pmtiles.sha256


⸻

🌐 Local Preview

Static z/x/y pyramid

python -m http.server --directory data/tiles/layer 8000
# → http://localhost:8000/{z}/{x}/{y}.png

PMTiles (preferred)

map.addSource("layer", {
  type: "vector",   // or "raster"
  tiles: ["pmtiles://data/tiles/layer/layer.pmtiles"],
  tileSize: 256
});
map.addLayer({ id: "layer", type: "line", source: "layer" });


⸻

📦 Git / LFS Policy
	•	data/tiles/layer/** is ignored.
	•	Final artifacts → move .pmtiles + .sha256 to:
	•	data/derivatives/tiles/
	•	web/tiles/

⸻

🚀 Publishing
	•	Reference PMTiles in MapLibre configs via pmtiles:// URLs.
	•	Attach .pmtiles + .sha256 to GitHub Releases or upload to cloud storage.
	•	STAC Items should reference the published .pmtiles with:

"roles": ["tiles"]


⸻

✅ This folder = temporary build space for one layer.
Final reproducible artifacts → LFS-tracked data/derivatives/tiles/ or web/tiles/.