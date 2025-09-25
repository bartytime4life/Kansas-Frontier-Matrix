# Kansas-Frontier-Matrix — Badge System (`scripts/badges/`)

This folder contains the **badge generation pipeline** for the **Data Source Status** table in the main [`README.md`](../../README.md).

---

## 📌 Purpose

Badges in the main README show the **live validation status** (✔ / ⚠ / ❌) of each data source, based on **STAC validation** in CI.

- ✔ **brightgreen** → clean STAC validation (no errors/warnings)  
- ⚠ **orange** → STAC validation succeeded but had warnings  
- ❌ **red** → validation failed, no items mapped, or missing assets  

The badge JSONs are published under `web/badges/*.json` and read by [shields.io endpoint badges](https://shields.io/endpoint).

---

## ⚙️ Components

### 1. `write_badges.sh`
A Bash script run in CI to:
- Collect source IDs from `data/sources/*.json`
- Default all to ❌ (red)
- Parse the STAC validation report (`build/stac_report.json`)
- Roll up validation results per source
- Write badge JSON files to `web/badges/*.json`

> See [`.github/workflows/stac-badges.yml`](../../.github/workflows/stac-badges.yml) for how it’s invoked.

### 2. `source_map.json`
Explicit mapping from **source IDs → STAC Item paths**.  
Example:

```json
{
  "ks_dem_1m": [
    "stac/items/ks_1m_dem_2018_2020.json"
  ],
  "usgs_topo_1894_1950": [
    "stac/items/overlays/usgs_topo_larned_1894.json"
  ],
  "ks_treaties": [
    "stac/items/vectors/ks_treaties.json"
  ],
  "ks_railroads": [
    "stac/items/vectors/ks_railroads.json"
  ],
  "schema.source": []
}
