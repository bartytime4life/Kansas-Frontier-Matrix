<div align="center">

# 🖼️ Kansas-Frontier-Matrix — Overlay COGs (`data/cogs/overlays/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)

**Mission:** Store **web-ready Cloud-Optimized GeoTIFFs (COGs)** used as overlays in  
the Kansas Frontier Matrix / Kansas Geo Timeline viewer.  

Overlays include historic scans, terrain renderings, wildfire rasters, treaty boundaries,  
and other cartographic textures that enrich the timeline + map.  

</div>

---

## 🔄 Overlay Lifecycle

```mermaid
flowchart LR
  A["Raw scans / rasters\n(data/raw/**)"] --> B["Georeference & Reproject\n(gdalwarp → EPSG:4326)"]
  B --> C["Convert to COG\n(data/cogs/overlays/**)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  C --> F["Web viewer\n(MapLibre overlays)"]
  E --> G["Validate\n(stac-validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/cogs/overlays/
├── hillshade_1m_ks_2018-2020.tif
├── relief_tint_ks_1938.tif
├── usgs_quad_1894_larned.tif
├── treaty_boundaries_1854.tif
└── <name>.tif

Everything here must be:
	•	Cloud-Optimized GeoTIFF
	•	EPSG:4326 (WGS84)
	•	Mask/NoData set correctly
	•	.sha256 sidecar present
	•	Registered in STAC

⸻

🧭 What Belongs Here?
	•	🗺️ Scanned historic maps (georeferenced)
	•	🏔️ Terrain derivatives (hillshade, slope/aspect renderings)
	•	🔥 Rasterized events (e.g., wildfire perimeters by date)
	•	🧭 Cartographic textures (hachures, stipple masks, relief tints)

❌ Vector data (trails, hydrology, settlements) → data/processed/ as GeoJSON.

⸻

🏷 Naming Convention

<theme>*<resolution|scale>*<region>_<year-or-range>.tif

Examples:
	•	usgs_quad_1894_larned.tif
	•	hillshade_1m_ks_2018-2020.tif

⸻

⚙️ COG Specs (House Standard)

Property	Value / Guidance
CRS	EPSG:4326 (WGS84)
Tiling	512×512 internal tiles
Overviews	Down to ~512 px minimum dimension
Compression	deflate (lossless) or webp (lossy, photo-like scans)
Mask/NoData	Internal mask; set nodata explicitly if applicable
Bit depth	Prefer 8-bit (Byte)
Checksums	Write <file>.tif.sha256 (GNU format)


⸻

🛠️ Create / Convert

Option A — Project Script

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

📌 Georeferencing Notes
	•	If the scan is not georeferenced, apply GCPs + gdalwarp -t_srs EPSG:4326 before conversion
	•	Crop/deskew before COG; trim borders to improve compression
	•	For line art/labels → prefer deflate (avoid lossy artifacts)

⸻

📇 STAC Registration
	•	Automatic when using ingest_raster()
	•	Or regenerate via Make:

make stac stac-validate-items

Each STAC Item includes bbox, checksum, file stats, and media type:
image/tiff; application=geotiff; profile=cloud-optimized

⸻

🗺️ Web Viewer Wiring

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

Keep legends in web/config/legend.json; use relative paths for GitHub Pages serving.

⸻

🧪 QA / Validation

# Quick metadata check
gdalinfo -checksum data/cogs/overlays/<file>.tif | less

# Validate COG structure
rio cogeo validate data/cogs/overlays/<file>.tif

# Verify checksum
sha256sum -c data/cogs/overlays/<file>.tif.sha256


⸻

⚖️ Attribution & Licensing
	•	Add source, citation, and license to the layer’s STAC properties + viewer attribution
	•	Do not include restricted scans; prefer open licenses (CC-BY / CC0 / Public Domain)

⸻

🐛 Troubleshooting
	•	Jagged edges at small scales → rebuild with overviews
	•	Colors washed out → preserve 8-bit, avoid implicit scaling
	•	File too large → use --web-optimized (webp) for photo scans
	•	Misalignment → fix georeferencing before COG conversion

⸻

✅ Summary

Mission-grade principle: Overlay COGs must be clean, verifiable, and traceable via STAC.
If it’s not reproducible and fast in the viewer, it does not ship here.