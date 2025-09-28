# `data/sources/climate/` — Climate & Weather Data Sources

This folder holds **curated JSON descriptors** for climate, weather, and drought
datasets that support the Kansas-Frontier-Matrix project.  
Descriptors here are validated against the global [`schema.source.json`](../schema.source.json)
and drive `make fetch` → `make stac` workflows.

---

## Purpose

- Capture **metadata + provenance** for climate-related datasets.
- Provide reproducible recipes for fetching long-term weather records,
  gridded climate surfaces, drought monitors, and hazard archives.
- Feed into the `processed/` and `cogs/` pipelines to produce analysis-ready
  artifacts and STAC catalogs.

---

## Typical Datasets

Examples of datasets described here (see [integration guide](../../README.md)):

| Dataset                              | Coverage                 | Format(s)      | Notes                                   |
|--------------------------------------|--------------------------|----------------|-----------------------------------------|
| NOAA NCEI GHCN-Daily                 | Station obs 1880s–today | CSV, TXT, API  | Precip, temp, snow at KS stations       |
| NASA Daymet (V4)                     | 1980–today, 1 km grid   | NetCDF, WMS    | Daily gridded min/max temp, precip, etc |
| NOAA Climate Normals (1991–2020)     | 30-year averages        | CSV, GeoTIFF   | Baseline reference climatology           |
| US Drought Monitor                   | 2000–today, weekly      | Shapefile, GeoJSON | D0–D4 drought polygons per week   |
| NOAA Storm Events (multi-hazard)     | 1950–today              | CSV, SQL       | Tornadoes, floods, wildfires, etc.       |

---

## Workflow

1. **Add/Edit descriptor** (e.g. `ghcn_daily.json`).
2. **Validate schema**:
   ```bash
   make validate-sources
````

3. **Fetch data**:

   ```bash
   make fetch
   ```

   → downloads to `data/raw/climate/` (ignored by git).
4. **Process**:

   * `make cogs` → convert rasters (e.g. gridded NetCDF → GeoTIFF/COG).
   * `make vectors` → normalize drought polygons.
5. **Catalog**:

   ```bash
   make stac
   ```

   → builds/updates `data/stac/items/climate_*.json`.

---

## Conventions

* IDs: `climate_<dataset>_<period>` (lowercase, underscore).

  * Example: `climate_daymet_1980_2025`
* Periods: `YYYY`, `YYYY-YYYY`, `1990s`, `late-19c`.
* Spatial reference: normalize to `EPSG:4326` unless strong reason otherwise.
* Each descriptor should include:

  * `license` with `name` and `url`
  * `provenance` attribution (agency, program, DOI if available)
  * `retrieved` datetime

---

## Git Policy

* JSON descriptors here are **always tracked**.
* Raw downloaded files live under `data/raw/climate/` (ignored).
* Processed outputs (`data/processed/climate/**`, `data/cogs/climate/**`)
  go to LFS if large, with `*_meta.json` + `*.sha256` sidecars in git.

---

✦ **Summary:**
`data/sources/climate/` contains the **blueprints for climate + hazard datasets**.
These descriptors guarantee traceability from NOAA/NASA sources → reproducible
artifacts → discoverable STAC metadata.

```
