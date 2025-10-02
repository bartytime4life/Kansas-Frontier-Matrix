<div align="center">

# 🌦️ Kansas Geo Timeline — Climate & Weather Sources  
`data/sources/climate/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/climate/)  

**Mission:** This folder holds **curated JSON descriptors** for climate, weather, and drought datasets powering the Kansas Frontier Matrix.  

📌 Validated against [`schema.source.json`](../schema.source.json)  
📌 Drive **`make fetch` → `make stac`** workflows  
📌 Guarantee **traceability** from NOAA/NASA sources → reproducible artifacts → discoverable STAC Items  

</div>

---

## 🎯 Purpose

- 📖 Capture **metadata + provenance** for climate datasets.  
- 🔄 Provide reproducible recipes for fetching station records, gridded surfaces, drought monitors, and hazards.  
- ⚙️ Feed into `processed/` and `cogs/` pipelines for analysis-ready outputs.  
- 🌐 Ensure datasets are discoverable in the **STAC catalog**.  

---

## 📂 Typical Datasets

| Dataset                              | Coverage                  | Format(s)          | Notes                                       |
|--------------------------------------|---------------------------|--------------------|---------------------------------------------|
| **NOAA NCEI GHCN-Daily**             | 1880s–present, stations   | CSV, TXT, API      | Daily precip/temp/snow at KS stations       |
| **NASA Daymet (V4)**                 | 1980–present, 1 km grid   | NetCDF, WMS/WCS    | Daily gridded weather variables             |
| **NOAA Climate Normals (1991–2020)** | 30-year averages          | CSV, GeoTIFF       | Baseline climatology                        |
| **US Drought Monitor**               | 2000–present, weekly      | Shapefile, GeoJSON | Weekly drought polygons (D0–D4 categories)  |
| **NOAA Storm Events (multi-hazard)** | 1950–present              | CSV, SQL           | Tornadoes, floods, drought, wildfires, etc. |

---

## 📈 Workflow

```mermaid
flowchart TD
  A["Add/Edit Descriptor\n(data/sources/climate/*.json)"] --> B["Validate\n(make validate-sources)"]
  B --> C["Fetch Raw Data\n(make fetch → data/raw/climate/**)"]
  C --> D["Process\n(make cogs / make vectors → data/processed/**, data/cogs/**)"]
  D --> E["Build STAC\n(make stac → data/stac/items/climate_*.json)"]
  E --> F["Viewer integration\n(web/config/layers.json)"]

<!-- END OF MERMAID -->



⸻

🧭 Conventions
	•	IDs → climate_<dataset>_<period> (lowercase, underscores).
	•	Example: climate_daymet_1980_2025
	•	Periods → YYYY, YYYY-YYYY, 1990s, late-19c
	•	CRS → normalize to EPSG:4326 unless strong reason otherwise
	•	Each descriptor must include:
	•	license → name + URL
	•	provenance → attribution, program, DOI if available
	•	retrieved → ISO 8601 datetime

⸻

🔐 Git Policy
	•	✅ JSON descriptors in data/sources/climate/ are tracked
	•	🚫 Raw downloads → data/raw/climate/** ignored by git
	•	📦 Processed outputs:
	•	data/processed/climate/**, data/cogs/climate/**
	•	Large files → Git LFS
	•	Sidecars (*.meta.json, *.sha256) committed to git

⸻

🚀 Quickstart

# 1. Add/Edit descriptor
$EDITOR data/sources/climate/ghcn_daily.json

# 2. Validate schema
make validate-sources

# 3. Fetch raw data
make fetch    # saves to data/raw/climate/

# 4. Process into analysis-ready outputs
make cogs     # e.g., NetCDF → COG
make vectors  # e.g., drought polygons

# 5. Build STAC catalog entries
make stac     # updates data/stac/items/climate_*.json


⸻

✅ QA Checklist
	•	Descriptor schema validated (schema.source.json)
	•	License and provenance explicitly recorded
	•	Raw payloads downloaded into data/raw/climate/ with .sha256 sidecar
	•	All downstream outputs (processed/COGs) trace back to descriptor ID
	•	STAC Items generated and validated

⸻

📝 TL;DR
	•	data/sources/climate/ = blueprints for climate + hazard datasets
	•	Ensures traceability: NOAA/NASA → raw → processed → STAC
	•	Supports reproducible pipelines and discoverable metadata

<div align="center">


✅ If it tracks Kansas climate, drought, or weather history → it belongs here.

</div>
```
