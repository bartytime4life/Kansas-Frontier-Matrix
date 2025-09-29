# Kansas-Frontier-Matrix — Processed Data

This directory contains **derived, cleaned, and ready-for-use geospatial and historical datasets**.  
All files here are **pipeline outputs** (ETL workflows, experiments, or transformations),  
and every artifact is referenced in the **STAC catalog** (`data/stac/items/`).

---

## Principles

- **Immutable inputs, reproducible outputs**  
  - Raw data lives under `data/raw/` or is fetched from authoritative sources.  
  - Processed data here must be **reproducible** from scripts + configs + GCPs.  
  - Nothing in this directory is hand-edited.

- **STAC integration**  
  - Every file here should map to a **STAC Item** (`data/stac/items/**.json`).  
  - Each item must record: datetime, bbox, checksum, license, provenance.  
  - Items are grouped into thematic STAC collections (`data/stac/collections/`).

- **Lightweight storage**  
  - Large rasters are tracked with **Git LFS** or **DVC**.  
  - Vectors and tables should be optimized (GeoJSON, Parquet).  
  - This folder is not an archive; it holds only **current, published outputs** for  
    experiments, the web viewer, and reproducible analysis.

- **MCP reproducibility** [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:1‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P)  
  - Each dataset must trace back to its experiment, config, or Makefile step.  
  - Provenance sidecars (`.sha256`, `.meta.json`) are required.  
  - Outputs are treated as experiment results with documented lineage.

---

## Typical Contents

data/processed/
├── towns_points.json          # Settlement points (GeoJSON)
├── ks_treaties.json           # Treaty polygons (historic boundaries)
├── ks_railroads.json          # Historic railroad lines
├── hydrology.json             # Rivers and waterbodies (vectorized)
├── landcover_timeslices.json  # Land cover snapshots (NLCD, 1992–2021)
├── dem/                       # Processed DEMs and terrain derivatives
│   ├── ks_1m_hillshade.tif
│   ├── ks_slope.tif
│   └── vectors/contours.json
├── hydrology/                 # Hydrology subdatasets (e.g. Kansas River, floodplains)
└── oral_histories.csv         # Structured oral history index

Formats:
- **Vector datasets** → GeoJSON (`*.json`, `*.geojson`)  
- **Tabular data** → CSV (`*.csv`) or Parquet (`*.parquet`)  
- **Derived rasters** (small to medium) → GeoTIFF/COG (`*.tif`)  
- **Metadata** → JSON sidecars (`*.meta.json`)  

Schemas should match `web/config/layers.schema.json` so web layers load seamlessly.

---

## Workflow

1. **Fetch raw data** → `data/raw/`  
   ```bash
   make fetch

	2.	Transform / clean → using scripts in scripts/ or notebooks in experiments/*/
	•	Examples: reproject, clip to Kansas extent, normalize fields.
	3.	Save outputs → data/processed/ in open, web-friendly formats (GeoJSON, CSV, COG).
	4.	Generate checksum + provenance

scripts/gen_sha256.sh data/processed/<file>


	5.	Update STAC Item → under data/stac/items/
	•	Each processed file must have a STAC item with correct href, checksum, and links.
	6.	Validate → JSON schema + STAC validation

make stac-validate
pre-commit run --all-files



⸻

Example Entries

Vector GeoJSON
	•	File: data/processed/ks_treaties.json
	•	STAC Item: data/stac/items/vectors/ks_treaties.json
	•	Linked Layer: web/data/treaties.json

Raster COG
	•	File: data/processed/dem/ks_1m_hillshade.tif
	•	STAC Item: data/stac/items/topo/ks_1m_hillshade.json
	•	Linked Layer: web/data/hillshade.json
	•	Exported KML/KMZ: data/kml/ks_hillshade_2018_2020.kmz ￼

⸻

Notes
	•	❌ Do not manually edit files in this directory. Always regenerate via pipelines.
	•	✅ Document provenance — configs, GCPs, scripts must be linked in metadata.
	•	🔗 Keep filenames stable so references in STAC, Makefile, and web configs remain valid.
	•	🗂️ Use collections (data/stac/collections/) to group related processed data (e.g. landcover, treaties, DEM).
	•	📦 Use make clean to clear processed rasters when rebuilding experiments.

⸻

See Also
	•	data/raw/ — raw, unaltered acquisitions.
	•	data/cogs/ — cloud-optimized GeoTIFFs (mission-final rasters).
	•	data/stac/ — STAC items and collections for catalog integration.
	•	web/data/ — JSON layer configs consumed by the web viewer.
	•	data/kml/ — KML/KMZ exports for Google Earth.
	•	experiments/ — MCP-style experiment logs and notebooks that produce these files.

⸻

✅ This directory ensures Kansas Frontier Matrix datasets are consistent, versioned, STAC-compliant, and reproducible across experiments, pipelines, and web viewer layers.

----