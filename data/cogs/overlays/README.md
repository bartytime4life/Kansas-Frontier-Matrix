<div align="center">

# 🖼️ Kansas Geo Timeline — Overlay COGs

**Web-ready Cloud-Optimized GeoTIFFs (COGs)** used as  
map overlays in the **Kansas Frontier Matrix / Kansas Geo Timeline** viewer.  

Overlays include historic scans, terrain renderings, wildfire rasters, treaty boundaries,  
and other cartographic textures used to enrich the timeline + map.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart LR
  A["Raw scans / rasters\n(data/raw/**)"] --> B["Georeference & Reproject\n(gdalwarp → EPSG:4326)"]
  B --> C["Convert to COG\n(data/cogs/overlays/**)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  C --> F["Web Viewer\n(MapLibre overlays)"]
  E --> G["Validate\n(stac validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory layout

data/cogs/overlays/
├── hillshade_1m_ks_2018-2020.tif
├── relief_tint_ks_1938.tif
├── usgs_quad_1894_larned.tif
├── treaty_boundaries_1854.tif
└── <name>.tif

Everything here must be:
• Cloud-Optimized GeoTIFF
• EPSG:4326 (WGS84)
• Mask/NoData set correctly
• .sha256 sidecar
• Registered in STAC

⸻

🧭 What belongs here?
	•	🗺️ Scanned historic maps (georeferenced)
	•	🏔️ Terrain derivatives (hillshade, slope/aspect renderings)
	•	🔥 Rasterized events (e.g., wildfire perimeters per date)
	•	🧭 Cartographic textures (hachures, stipple masks, relief tints)

❌ Vector data (trails, hydrology, settlements) lives in data/processed/ as GeoJSON.

⸻

🏷 Naming convention

<theme>*<resolution|scale>*<region>_<year-or-range>.tif

Examples:
	•	usgs_quad_1894_larned.tif
	•	hillshade_1m_ks_2018-2020.tif

⸻

⚙️ COG specs (house standard)

Property	Value / Guidance
CRS	EPSG:4326 (WGS84)
Tiling	512×512 internal tiles
Overviews	Down to ~512 px min dimension
Compression	deflate (lossless) or webp (lossy, for photo-like scans)
Mask / NoData	Internal mask; set nodata explicitly if applicable
Bit depth	Prefer 8-bit (Byte)
Checksums	Write <file>.tif.sha256 (GNU format)


⸻

🛠️ Create / Convert

Option A — Project script

Lossless (deflate):

python scripts/convert.py raster-to-cog \
  data/raw/maps/usgs_quad_1894_larned_raw.tif \
  data/cogs/overlays/usgs_quad_1894_larned.tif

Web-optimized (photo scans, webp):

python scripts/convert.py raster-to-cog \
  --web-optimized \
  data/raw/scans/relief_tint_1938.tif \
  data/cogs/overlays/relief_tint_ks_1938.tif

Option B — Python API

from kansas_geo_timeline.ingest import ingest_raster
out, item = ingest_raster(
    "data/raw/scans/usgs_quad_1894_larned.tif",
    out_dir="data/cogs/overlays",
    profile="deflate"
)
print(out, item["id"])


⸻

📌 Georeferencing notes
	•	If the scan is not georeferenced, apply GCPs + gdalwarp to EPSG:4326 before conversion.
	•	Crop/deskew before COG; trim borders to improve compression.
	•	For line art / labels → prefer deflate (avoid lossy artifacts).

⸻

📇 STAC registration
	•	Automatic when using ingest_raster() above.
	•	Or regenerate with Make:

make stac stac-validate-items

Each STAC item includes bbox, checksum, file stats, and media type
(image/tiff; application=geotiff; profile=cloud-optimized).

⸻

🗺️ Web viewer wiring

Add a layer entry in web/config/*.json:

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

Keep legends in web/config/legend.json; use relative paths so GitHub Pages can serve.

⸻

🧪 QA / validation

# Quick metadata check
gdalinfo -checksum data/cogs/overlays/<file>.tif | less

# Validate COG structure
rio cogeo validate data/cogs/overlays/<file>.tif

# Verify checksum
sha256sum -c data/cogs/overlays/<file>.tif.sha256


⸻

⚖️ Attribution & licensing
	•	Add source, citation, and license to the layer’s STAC properties & viewer attribution.
	•	Do not include restricted scans; prefer open licenses (CC-BY / CC0 / Public Domain).

⸻

🐛 Troubleshooting
	•	Jagged edges at small scales → rebuild with overviews.
	•	Colors washed out → preserve 8-bit, avoid implicit scaling.
	•	File too large → use --web-optimized (webp) for photo scans.
	•	Misalignment → fix georeferencing before COG conversion.

⸻

✅ Mission-grade principle: Overlay COGs must be clean, verifiable, and traceable via STAC.
If it’s not reproducible and fast in the viewer, it doesn’t ship here.

