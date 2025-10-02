<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Tile Layer  
`data/tiles/layer/`

**Mission:** Temporary build space for **ephemeral tile artifacts**  
(raster pyramids or vector PMTiles) for a **single map layer**.  
Supports **local preview & staging** before publishing reproducible outputs.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)  

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

✦ Summary

data/tiles/layer/ is a temporary build space for one map layer.
Final reproducible artifacts must move to LFS-tracked data/derivatives/tiles/ or web/tiles/,
ensuring tiles are previewed locally, published reproducibly, and registered in STAC.