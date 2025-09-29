<div align="center">

# 🌦️ Kansas-Frontier-Matrix — **Climate & Weather Sources** (`data/sources/climate/`)

**Mission:** This folder holds **curated JSON descriptors** for climate, weather, and drought datasets  
that power the Kansas Frontier Matrix.  

📌 Validated against [`schema.source.json`](../schema.source.json)  
📌 Drive **`make fetch` → `make stac`** workflows  
📌 Guarantee **traceability** from NOAA/NASA sources → reproducible artifacts → discoverable STAC Items  

</div>

---

## Purpose

- 📖 Capture **metadata + provenance** for climate-related datasets.  
- 🔄 Provide reproducible recipes for fetching station records, gridded surfaces, drought monitors, and hazards.  
- ⚙️ Feed into the `processed/` and `cogs/` pipelines for analysis-ready outputs.  
- 🌐 Ensure datasets are discoverable in the **STAC catalog**.  

---

## Typical Datasets

| Dataset                          | Coverage                  | Format(s)         | Notes                                   |
|----------------------------------|---------------------------|-------------------|-----------------------------------------|
| **NOAA NCEI GHCN-Daily**         | 1880s–today, station obs  | CSV, TXT, API     | Precip, temp, snow at KS stations       |
| **NASA Daymet (V4)**             | 1980–today, 1 km grid     | NetCDF, WMS/WCS   | Daily gridded min/max temp, precip, etc |
| **NOAA Climate Normals (1991–2020)** | 30-year averages         | CSV, GeoTIFF      | Baseline reference climatology           |
| **US Drought Monitor**           | 2000–today, weekly        | Shapefile, GeoJSON | Weekly drought polygons (D0–D4)        |
| **NOAA Storm Events (multi-hazard)** | 1950–today              | CSV, SQL          | Tornadoes, floods, wildfires, etc.      |

> See [integration guide](../../README.md) for details on how these fit into the larger pipeline.

---

## Workflow

```mermaid
flowchart TD
  A[Add/Edit Descriptor<br/>data/sources/climate/*.json] --> B[Validate<br/>make validate-sources]
  B --> C[Fetch Raw Data<br/>make fetch → data/raw/climate/**]
  C --> D[Process<br/>make cogs / make vectors<br/>→ data/processed/**, data/cogs/**]
  D --> E[Catalog<br/>make stac → data/stac/items/climate_*.json]

<!-- END OF MERMAID -->



⸻

Conventions
	•	IDs: climate_<dataset>_<period> (lowercase, underscores).
	•	Example: climate_daymet_1980_2025
	•	Periods: YYYY, YYYY-YYYY, 1990s, late-19c.
	•	CRS: normalize to EPSG:4326 unless strong reason otherwise.
	•	Each descriptor must include:
	•	license → name + URL
	•	provenance → attribution, program, DOI if available
	•	retrieved → ISO 8601 datetime

⸻

Git Policy
	•	✅ JSON descriptors in data/sources/climate/ are always tracked.
	•	🚫 Raw downloads → data/raw/climate/** (ignored by git).
	•	📦 Processed outputs (data/processed/climate/**, data/cogs/climate/**):
	•	Large files → tracked via Git LFS.
	•	Each output has *_meta.json + *.sha256 sidecars committed to git.

⸻

Quickstart
	1.	Add/Edit descriptor

$ $EDITOR data/sources/climate/ghcn_daily.json


	2.	Validate schema

make validate-sources


	3.	Fetch data

make fetch

→ downloads to data/raw/climate/

	4.	Process

make cogs    # e.g., NetCDF → COG
make vectors # e.g., drought polygons


	5.	Catalog

make stac

→ updates data/stac/items/climate_*.json

⸻

TL;DR
	•	data/sources/climate/ = blueprints for climate + hazard datasets.
	•	Ensures traceability: source (NOAA/NASA) → raw → processed → STAC.
	•	Supports reproducible pipelines and discoverable metadata.

✅ If it tracks Kansas climate, drought, or weather history, it belongs here.

