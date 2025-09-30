<div align="center">


🔁 Kansas-Frontier-Matrix — Change Detection & Time-Series Derivatives (data/derivatives/change/)

Mission: hold time-aware, analysis-ready change layers derived from canonical inputs (data/cogs/, data/sources/) to quantify how Kansas changed — terrain, water, vegetation, hazards, parcels/treaties, and built networks — with provenance, uncertainty, and STAC.  ￼  ￼

</div>



⸻

Lifecycle

flowchart TD
  A["Inputs\nCOGs & vectors\n(data/cogs, data/sources)"] --> B["Normalize\nCRS, masks, time-index"]
  B --> C["Pairing\nperiod-to-period\n(t0,t1,...,tn)"]
  C --> D["Metrics\nΔ, %Δ, indices,\nclassification"]
  D --> E["Uncertainty\nerror budget,\nconf intervals"]
  E --> F["Publish\n(data/derivatives/change)"]
  F --> G["STAC items\n(stac/items)"]
  G --> H["Validate\n(stac-validate)"]
  F --> I["Tiles/PMTiles\n(web/tiles)"]

<!-- END OF MERMAID -->


Built MCP-style: documentation-first, reproducible, and cross-domain (history + cartography + geology).  ￼

⸻

What belongs here (and what doesn’t)

✅ Belongs
	•	Raster change products: elevation Δ (DoD), slope/roughness change, inundation differencing, landcover transitions, NDVI/greenness change, burn severity (dNBR/RdNBR), drought class frequency, soil moisture anomalies.
	•	Vector change products: channel centerline shift, shoreline/wetland polygon deltas, road/rail expansion by decade, parcel/treaty boundary evolution, hazard footprints (tornado, wildfire, flood) by period.
	•	Time-series summaries: recurrence maps, trend rasters, turn-of-decade snapshots, event heatmaps.

🚫 Doesn’t
	•	Raw sources (put in data/sources/) or single-date COGs (go in data/cogs/).
	•	Ephemeral web tiles (use data/tiles/ for scratch; publish to web/tiles/ when versioned).

⸻

Directory layout

data/
└─ derivatives/
   └─ change/
      ├─ raster/                 # GeoTIFF/COG outputs
      │  ├─ dem/
      │  │  └─ dod_1m_2012_2020.tif
      │  ├─ landcover/
      │  │  └─ nlcd_change_2001_2021.tif
      │  ├─ vegetation/
      │  │  └─ ndvi_delta_1986_2020_seasmean.tif
      │  ├─ fire/
      │  │  └─ dnbr_2000_2024_kansas.tif
      │  └─ hydro/
      │     └─ flood_extent_diff_1951_2007.tif
      ├─ vector/                 # GeoJSON/Parquet/PMTiles
      │  ├─ channels/
      │  │  └─ kansas_river_centerline_shift_1954_2020.geojson
      │  ├─ boundaries/
      │  │  ├─ treaty_transitions_1854_1871.geojson
      │  │  └─ parcels_change_1900_1935.geojson
      │  └─ hazards/
      │     └─ tornado_tracks_decadal_1950_2020.pmtiles
      ├─ qc/                     # reports, masks, residuals
      │  └─ dod_1m_2012_2020_residuals.tif
      └─ README.md


⸻

Supported change products (recipes)

Theme	Inputs	Output (examples)
DoD: DEM of Difference	LiDAR/DEM epochs	dod_*_t0_t1.tif (Δm), residuals, masks, 95% CI
Hydro	Historic flood outlines, NHD, gauge extents	flood_extent_diff_YYYY_YYYY.tif, channel shift vectors
Landcover	NLCD/CCDC	nlcd_change_2001_2021.tif, per-class transitions
Vegetation	Landsat/Sentinel NDVI	ndvi_delta_*, trend rasters, anomaly maps
Fire	NIFC perimeters, dNBR from pre/post	dnbr_*.tif, severity classes
Hazards	NOAA SPC, Storm Events	decadal tornado/wind/hail layers, density grids
Admin/Property	Treaties, PLSS, parcels	treaty/parcel state-change vectors by year

Dataset anchors: NOAA Storm Events & SPC, FEMA declarations, NIFC wildfire perimeters, NLCD 1992–2021, LiDAR/DEM (1-m), historic topographic scans.

⸻

Naming & metadata conventions

File pattern

<topic>_<spatial>_<metric>_<t0>_<t1>[_v<semver>].tif|geojson|pmtiles

STAC Item required keys
	•	properties.datetime or start_datetime/end_datetime (paired/interval)
	•	proj:epsg (=4326 for published)
	•	kfm:method (short recipe id + params)
	•	kfm:uncertainty (RMSE/σ, CI method)
	•	kfm:lineage (source ids + commit)
	•	processing:software (versions, container tag)

Keep MCP traceability: keep method notes + checksums; every output cites inputs + code rev.   ￼

⸻

Workflow & Make targets

Common flow:

# 0) Fetch sources and build COGs (DEM, NLCD, imagery)
make fetch cogs

# 1) Create masks & co-registration (hillshade for QA as needed)
make terrain align

# 2) Change products
make change-dod             # DEM of Difference (pairs file)
make change-nlcd            # Landcover transitions
make change-ndvi            # NDVI Δ and trends
make change-fire            # dNBR from pre/post composites
make change-hazards         # SPC/Storm Events decadal layers

# 3) STAC + validation
make stac stac-validate

# 4) Tiles/PMTiles for web
make tiles

Pairing strategy (pairs.yaml) defines epochs and masks (stable ground/water). Batch jobs run containerized for reproducibility.

⸻

Method notes (condensed)
	•	DoD (DEM→Δ): coregister (NCC/ICP), propagate vertical RMSE to cellwise CI, mask low-confidence; output Δm + residuals.
	•	Hydro diffs: union historic flood polygons; rasterize to 0/1; Δ = post - pre → loss/gain; track channel centerline migration (MNDWI assist).
	•	Landcover transitions: harmonize legends; confusion matrix; per-class change and net-change rasters.
	•	NDVI change/trends: per-pixel seasonal composites, Δ or Sen’s slope; drought overlays from US Drought Monitor.
	•	Fire severity (dNBR): pre/post NBR, Δ and class thresholds; clip by NIFC perimeters, export severity map.
	•	Hazards: SPC line/point → per-decade PMTiles + kernel density; Storm Events → county counts/time-series.
	•	Admin change: diff treaty/parcel polygons over time; encode attributes {from,to,year,confidence}.

Where applicable, quantify uncertainty and expose it (bands or sidecars). Follow NASA-grade V&V concepts (credibility, assumptions, parameters).

⸻

QA/QC & uncertainty
	•	Co-registration tests (pre/post): tie points, residuals, report RMSE.
	•	Masks: stable ground/water masks for DoD; cloud/shadow masks for optical.
	•	Error budget: propagate sensor & processing error; include CI band or kfm:uncertainty.
	•	Cross-checks: compare change against independent references (gauges, FEMA DFIRMs, field notes, USGS reports).
	•	Reviews: mark outputs with qa:status = draft|provisional|verified.

MCP requires transparent assumptions + peer-style notes alongside code and data.  ￼

⸻

Performance & publishing
	•	Publish rasters as COG (internal overviews, deflate/lzw); vectors as PMTiles for the web.
	•	Large vectors: tile or partition by county/decade; consider TopoJSON for static overlays.
	•	Add STAC Items in stac/items/ and link into thematic collection (e.g., stac/collections/change.json).
	•	Validate in CI (stac-validate workflow) and ship to viewer config.

⸻

Examples

1) DEM of Difference (2012 → 2020)

# pairs.yaml example
- id: ks_dod_1m_2012_2020
  t0: data/cogs/dem/ks_1m_2012.tif
  t1: data/cogs/dem/ks_1m_2020.tif
  mask: data/processed/masks/stable_ground.tif
  out: data/derivatives/change/raster/dem/dod_1m_2012_2020.tif

make change-dod
make stac stac-validate

2) NLCD transitions (2001 → 2021)

make change-nlcd NLCD_T0=2001 NLCD_T1=2021 OUT=data/derivatives/change/raster/landcover/nlcd_change_2001_2021.tif

3) Tornado decadal tiles

make change-hazards SPC_TORNADO_SHP=data/sources/hazards/spc_tornado_1950_2024.shp
# outputs PMTiles per decade under vector/hazards/

4) Treaty boundary evolution

python scripts/change/diff_polygons.py \
  --t0 data/sources/treaties/1854.geojson \
  --t1 data/sources/treaties/1871.geojson \
  --out data/derivatives/change/vector/boundaries/treaty_transitions_1854_1871.geojson


⸻

References & anchors
	•	Hazards & climate: NOAA Storm Events, SPC GIS, US Drought Monitor, FEMA Declarations, NIFC perimeters.
	•	Topography & historical maps: USGS topo (Topoview/PCL), KS LiDAR/DEM & hillshade.
	•	GIS archive integration & COG/GeoJSON/PMTiles guidance.
	•	MCP/architecture & knowledge graph linkage for time-aware layers.   ￼

⸻

Notes for contributors
	•	Add/extend recipes under scripts/change/ with clear params + defaults, write a short docs/methods/<recipe>.md.
	•	Always update STAC items and viewer config; keep provenance (commit, container tag) in item properties.
	•	Prefer open formats (COG, GeoJSON, PMTiles) and EPSG:4326 for published layers.
	•	If unsure, follow MCP templates for experiment/method and sop.  ￼

— end —