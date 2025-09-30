<div align="center">

# 🔁 Kansas-Frontier-Matrix — Change Detection & Time-Series Derivatives  
`data/derivatives/change/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

**Mission:** Store **time-aware, analysis-ready change layers** derived from canonical inputs  
(`data/cogs/`, `data/sources/`) to quantify how **Kansas landscapes, waters, and communities changed** —  
with **provenance, uncertainty, and STAC compliance**.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Inputs\nCOGs & Vectors\n(data/cogs, data/sources)"] --> B["Normalize\nCRS, masks, time-index"]
  B --> C["Pairing\nperiod-to-period\n(t0,t1,...,tn)"]
  C --> D["Metrics\nΔ, %Δ, indices,\nclassification"]
  D --> E["Uncertainty\nerror budget,\nconf intervals"]
  E --> F["Publish\n(data/derivatives/change)"]
  F --> G["STAC items\n(stac/items)"]
  G --> H["Validate\n(stac-validate)"]
  F --> I["Tiles/PMTiles\n(web/tiles)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/
└─ derivatives/
   └─ change/
      ├─ raster/                 # GeoTIFF/COG outputs
      │  ├─ dem/
      │  ├─ landcover/
      │  ├─ vegetation/
      │  ├─ fire/
      │  └─ hydro/
      ├─ vector/                 # GeoJSON / PMTiles
      │  ├─ channels/
      │  ├─ boundaries/
      │  └─ hazards/
      ├─ qc/                     # QA reports, masks, residuals
      └─ README.md


⸻

✅ What Belongs Here
	•	Raster change products → DEM of Difference (DoD), landcover transitions, NDVI change, burn severity, flood extent diffs.
	•	Vector change products → channel migration, shoreline/wetland deltas, road/rail expansion, treaty/parcel transitions, hazard perimeters.
	•	Time-series summaries → recurrence maps, trends, decade snapshots.

🚫 Does Not Belong
	•	Raw sources (data/sources/)
	•	Single-date COGs (data/cogs/)
	•	Ephemeral tiles (scratch → data/tiles/, published → web/tiles/)

⸻

🛠 Supported Products

Theme	Inputs	Outputs (examples)
DEM Δ	LiDAR/DEM epochs	dod_2012_2020.tif, residuals, masks
Hydrology	Flood outlines, NHD, gauges	flood_extent_diff_1951_2007.tif, channel shift vectors
Landcover	NLCD 1992–2021	nlcd_change_2001_2021.tif, per-class transitions
Vegetation	Landsat/Sentinel NDVI	ndvi_delta_1986_2020.tif, trends, anomalies
Fire	NIFC perimeters, pre/post NBR	dnbr_2000_2024.tif, severity classes
Hazards	NOAA SPC, Storm Events	Tornado decadal PMTiles, density grids
Admin	Treaties, parcels, PLSS	boundary transition vectors


⸻

📜 Naming & Metadata

Filename pattern

<topic>_<spatial>_<metric>_<t0>_<t1>[_v<semver>].tif|geojson|pmtiles

STAC requirements
	•	properties.start_datetime / end_datetime
	•	proj:epsg = 4326 for published outputs
	•	kfm:method = recipe id (with params)
	•	kfm:uncertainty = RMSE / CI method
	•	kfm:lineage = source ids + commit ref

⸻

⚙️ Workflow & Make Targets

# Fetch & prep
make fetch cogs terrain

# Change products
make change-dod       # DEM of Difference
make change-nlcd      # Landcover transitions
make change-ndvi      # NDVI Δ and trends
make change-fire      # Burn severity
make change-hazards   # SPC/Storm Events decadal layers

# Catalog & validate
make stac stac-validate

# Web publishing
make tiles


⸻

🔬 Method Notes
	•	DoD (DEM Δ): coregister DEMs, propagate vertical RMSE, mask unstable ground.
	•	Flood diffs: union polygons, rasterize, compute loss/gain.
	•	Landcover: harmonize legends, output per-class + net-change rasters.
	•	NDVI: seasonal composites, Δ or Sen’s slope trend.
	•	Fire: dNBR pre/post composites → severity classes.
	•	Hazards: decadal tornado/wind/hail layers + kernel density.
	•	Admin change: diff polygons; attributes {from,to,year,confidence}.

⸻

🧪 QA & Uncertainty
	•	Coregistration checks → tie points, RMSE reports.
	•	Stable masks → ground/water for DEMs; cloud/shadow for imagery.
	•	Error budgets → propagate sensor + processing errors.
	•	Cross-checks → gauges, FEMA DFIRMs, USGS reports.
	•	Review status → qa:status = draft | provisional | verified.

⸻

🚀 Publishing
	•	Rasters → COG (with overviews, compression).
	•	Vectors → PMTiles (for efficient web use).
	•	Register as STAC Items in stac/items/ under collection change.json.
	•	Validate in CI (stac-validate).

⸻

👩‍💻 Contributor Notes
	•	Add recipes under scripts/change/ + doc in docs/methods/.
	•	Always update STAC items + viewer configs.
	•	Prefer open formats + EPSG:4326 for public outputs.
	•	Use MCP templates for experiments and SOPs.