<div align="center">

# 🗺️ Kansas-Frontier-Matrix — DEM-Derived Vectors  
`data/processed/dem/vectors/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Store **vector products derived from DEMs**.  
These are extracted or modeled from rasters in `../` and `../overlays/`,  
stored as **GeoJSON** for maximum interoperability.  

All vector layers must be:  
- **Reproducible** from DEM inputs (no manual edits)  
- **Linked to provenance** in the STAC catalog (`data/stac/items/dem/*.json`)  
- **Schema-validated** against `web/config/layers.schema.json`  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Processed DEMs\n(data/processed/dem/**)"] --> B["Generate vectors\n(contours · watersheds · streams)"]
  B --> C["GeoJSON outputs\n(data/processed/dem/vectors/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/dem/**)"]
  E --> F["Validate\n(stac-validate · schema)"]
  F --> G["Web viewer\n(web/config/layers.json)"]
  F --> H["Earth exports\n(data/kml/**)"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

data/processed/dem/vectors/
├── ks_1m_dem_2018_contours_10m.json       # 10 m interval contours
├── ks_1m_dem_2018_watersheds_huc12.json   # watershed polygons
├── ks_1m_dem_2018_stream_network.json     # extracted stream lines
└── ks_1m_dem_2020_contours_5m.json        # alternate contour interval

Common types
	•	Contours → elevation isolines at fixed intervals
	•	Watersheds / Basins → polygons derived from flow accumulation
	•	Stream networks → centerlines from flow routing thresholds
	•	Landform classes → slope/aspect zones, geomorph classes

⸻

🔄 Workflow
	1.	Source DEM
	•	Must exist as a COG in data/processed/dem/
	•	Example: ks_1m_dem_2018.tif
	2.	Generate vectors

Contours (10m)

gdal_contour -a elev -i 10 \
  data/processed/dem/ks_1m_dem_2018.tif \
  /tmp/ks_1m_dem_2018_contours_10m.shp

ogr2ogr -f GeoJSON -t_srs EPSG:4326 \
  data/processed/dem/vectors/ks_1m_dem_2018_contours_10m.json \
  /tmp/ks_1m_dem_2018_contours_10m.shp

Watersheds (HUC12 equivalent)
	•	Tools: TauDEM, WhiteboxTools, GRASS GIS
	•	Workflow: flow direction → flow accumulation → stream & basin delineation

Stream networks

wbt_breach_depressions --dem=ks_1m_dem_2018.tif --output=/tmp/filled.tif
wbt_d8_flow_accumulation --dem=/tmp/filled.tif --out_type=catchment-area --output=/tmp/accum.tif
wbt_extract_streams --flow_accum=/tmp/accum.tif --threshold=1000 --output=/tmp/streams.tif
gdal_polygonize.py /tmp/streams.tif -f GeoJSON \
  data/processed/dem/vectors/ks_1m_dem_2018_stream_network.json

	3.	Reproject → always EPSG:4326 (WGS84 lat/long)
	4.	Checksums

scripts/gen_sha256.sh data/processed/dem/vectors/*.json

	5.	Update STAC Items → add vector assets to parent DEM

"contours_10m": {
  "href": "../../../processed/dem/vectors/ks_1m_dem_2018_contours_10m.json",
  "title": "DEM Contours 10m (2018)",
  "type": "application/geo+json",
  "roles": ["data"],
  "checksum:sha256": "<sha256sum>"
}


⸻

📑 Example STAC Item (DEM 10m Contours)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_1m_contours_10m_2018",
  "properties": {
    "title": "Kansas DEM Contours 10m (2018)",
    "description": "10m contour lines derived from the 2018 Kansas 1m DEM mosaic.",
    "datetime": "2018-06-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "gdal_contour -i 10",
    "kfm:lineage": [
      "data/processed/dem/ks_1m_dem_2018.tif"
    ],
    "qa:status": "provisional"
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../../stac/collections/terrain.json"
    }
  ],
  "assets": {
    "geojson": {
      "href": "../../../../data/processed/dem/vectors/ks_1m_dem_2018_contours_10m.json",
      "title": "Contours (10m, 2018 DEM)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}


⸻

🔗 Integration
	•	STAC catalog → ensures discoverability (contours, watersheds, streams)
	•	Web viewer → layers referenced in web/config/layers.json
	•	KML exports → selected DEM vectors exported under data/kml/
	•	Experiments → used in terrain analysis, archaeology, hydrology, flood modeling
	•	Reproducibility → regenerate outputs via pipelines; never hand-edit

⸻

📝 Notes
	•	Canonical format = GeoJSON (.json)
	•	For very large sets, tile or convert to MBTiles/PMTiles (but keep canonical GeoJSON here)
	•	Track large files with Git LFS or DVC
	•	Document exact tools/parameters in experiments/*/experiment.md
	•	Naming convention: <dem_id>_<layer>_<parameters>.json
	•	Example: ks_1m_dem_2018_contours_10m.json

⸻

📚 See Also
	•	../ → Base processed DEMs
	•	../overlays/ → Raster derivatives (hillshade, slope, aspect)
	•	../../stac/items/dem/ → STAC items linking DEMs and vector derivatives
	•	../../kml/ → KML/KMZ exports
	•	experiments/ → MCP logs + configs for vector derivation

⸻

✅ Mission Principle

DEM-derived vectors must be clean, reproducible, STAC-linked, and ready for integration
in Kansas Frontier Matrix workflows and web mapping.