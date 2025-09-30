<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Tile Layer (`data/tiles/layer/`)

**Mission:** Temporary build space for **ephemeral tile artifacts**  
(raster pyramids or vector PMTiles) for a **single map layer**.  
Supports **local preview & staging** before publishing reproducible outputs.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 **Ignored by Git** (`.gitignore`), except this `README.md`.  
📌 Final, reproducible tiles must move to  
`data/derivatives/tiles/` or `web/tiles/` under **Git LFS**.  
📌 Guarantees **traceability + reproducibility** (metadata + checksums).  

</div>

---

## 🎯 Purpose

- 🗺️ Hold **z/x/y raster pyramids** or a single `.pmtiles` for one layer.  
- 🔄 Enable quick **local preview** before publishing.  
- 🚫 Raw pyramids are temporary; only final `.pmtiles` go to LFS paths.  

---

## 📂 Directory Layout

```text
data/tiles/layer/
├── {z}/{x}/{y}.png        # optional raster pyramid (preview only)
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

pmtiles convert \
  data/tiles/layer/layer.mbtiles \
  data/tiles/layer/layer.pmtiles


⸻

🧾 Metadata & Provenance
	•	Create a sidecar _meta.json in data/processed/ for the source.
	•	Always store checksums when publishing:

sha256sum data/tiles/layer/layer.pmtiles \
  > data/tiles/layer/layer.pmtiles.sha256


⸻

🌐 Local Preview

Static pyramid

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
	•	data/tiles/layer/** → ignored.
	•	Final artifacts → move .pmtiles + .sha256 to:
	•	data/derivatives/tiles/
	•	web/tiles/

⸻

🚀 Publishing
	•	Reference PMTiles in MapLibre configs via pmtiles:// URLs.
	•	Attach .pmtiles + .sha256 to GitHub Releases or cloud storage.
	•	STAC Items must reference the published .pmtiles with:

"roles": ["tiles"]


⸻

🔄 Lifecycle (MCP Workflow)

flowchart TD
  A["Processed data\n(data/processed/*.tif|.json)"] --> B["Build tiles\n(rio pmtiles / tippecanoe)"]
  B --> C["Ephemeral output\n(data/tiles/layer/)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["Final artifacts\n(data/derivatives/tiles/ or web/tiles/)"]
  E --> F["STAC Items\n(stac/items/*.json)"]
  F --> G["Web Viewer\n(MapLibre + pmtiles:// URLs)"]
  G --> H["Preview & Publish\n(local or cloud)"]

<!-- END OF MERMAID -->



⸻

✅ Summary:
This folder = temporary build space for one layer.
Final reproducible artifacts → LFS-tracked data/derivatives/tiles/ or web/tiles/.