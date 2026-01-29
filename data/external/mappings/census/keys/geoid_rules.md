# 🗝️ Census GEOID Rules (US Census / TIGER) 🇺🇸

![Spec](https://img.shields.io/badge/spec-GEOID_rules-2ea44f)
![Scope](https://img.shields.io/badge/scope-US_Census_TIGER%2FLine-blue)
![KFM](https://img.shields.io/badge/KFM-data%20keys-orange)

> **Purpose:** Define **canonical rules** for creating, storing, validating, and joining **Census GEOIDs** across KFM pipelines (raw ➜ processed ➜ API/UI).  
> This keeps joins deterministic, reproducible, and reviewable. 🔁✅

---

## 📌 Where this file lives

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 📦 census/                                  🧮 Census/TIGER mapping packs + key registries
         └─ 🔑 keys/                                 🗝️ canonical IDs, dictionaries, and crosswalks
            └─ 🗝️ geoid_rules.md                      👈 you are here (GEOID composition, padding, validation)
```

---

## 🧠 Definitions (don’t mix these up)

| Term | What it is | Typical source |
|---|---|---|
| `GEOID` | The **standard geographic identifier** used in TIGER/Line (usually a **numeric string**, fixed-width, no separators). | TIGER/Line shapefiles / cartographic boundary files |
| `GEO_ID` / `GEO.ID` | A **fully qualified** identifier used in **data.census.gov downloads** that includes a **prefix** (summary level + variant/component + `US`) before the underlying GEOID. | data.census.gov CSV downloads |
| `GEOIDFQ` | “**Fully qualified GEOID**” field available in **newer** TIGER/Line vintages; intended to match data.census.gov-style identifiers. | TIGER/Line 2023+ (and newer) |
| `AFFGEOID` | Legacy fully-qualified identifier used historically (American FactFinder era); now retired/renamed in newer downloads. | Older cartographic boundary files / shapefiles |

> ⚠️ **Not geodesy:** this file is about *Census GEOIDs*, not the “geoid” (Earth gravity model). 🌍

---

## 🥇 Golden Rules (KFM canon)

1. **Always store GEOIDs as strings** (never integers).  
   - Reason: **leading zeros are meaningful** and must not be lost.  
2. **Never add separators** (`-`, spaces, etc.). Use **plain concatenation**.
3. **Normalize via left-zero-padding** to the official widths (see table below).
4. **Keep both forms when available**:
   - `geoid` (plain TIGER-style)
   - `geoidfq` (data.census.gov-style / fully-qualified)
5. **Never “guess” geography from length alone** in production joins.  
   - Store a `geography` / `summary_level` / dataset metadata alongside the key.

---

## 🧱 KFM pipeline touchpoints (why keys matter here)

KFM pipelines are expected to turn raw artifacts into **processed, ready-to-use datasets** (and keep them reproducible).  
A canonical example output from the project blueprint is:

```text
data/processed/census/1900_population.geojson
```

To keep this deterministic and reviewable:

- ✅ Put canonical join keys like `geoid` (and optionally `geoidfq`) directly in processed outputs.
- ✅ Record dataset geography + vintage (e.g., `tract`, TIGER 2024, ACS 2019–2023 5-year).
- ✅ Update the matching **metadata + provenance** alongside the dataset (`data/catalog/` + `data/provenance/`) so joins are explainable and auditable.

> TL;DR: If the key isn't stable + documented, the map is a lie. 😅🗺️

---

## 🧩 GEOID anatomy by geography

All components are **concatenated** in a fixed order and width.

> ✅ “Nestable” geographies embed their parents (e.g., tract contains state+county).  
> ✅ Tracts/block groups/blocks nest within **state + county**.

### 📋 Common TIGER/Line GEOID structures

| Geography | GEOID structure | Digits | Regex (practical) | Example |
|---|---:|---:|---|---|
| State | `STATE` | 2 | `^\d{2}$` | `48` |
| County | `STATE + COUNTY` | 5 | `^\d{5}$` | `48201` |
| County Subdivision | `STATE + COUNTY + COUSUB` | 10 | `^\d{10}$` | `4820192975` |
| Place | `STATE + PLACE` | 7 | `^\d{7}$` | `4835000` |
| Census Tract | `STATE + COUNTY + TRACT` | 11 | `^\d{11}$` | `48201223100` |
| Block Group | `STATE + COUNTY + TRACT + BLKGRP` | 12 | `^\d{12}$` | `482012231001` |
| Census Block | `STATE + COUNTY + TRACT + BLOCK` | 15 | `^\d{15}[A-Z]?$` | `482012231001050` |
| Congressional District | `STATE + CD` | 4 | `^\d{4}$` | `0902` |
| State Legislative District (Upper) | `STATE + SLDU` | 5 | `^\d{5}$` | `09033` |
| State Legislative District (Lower) | `STATE + SLDL` | 5 | `^\d{5}$` | `09147` |
| ZCTA | `ZCTA` | 5 | `^\d{5}$` | `20746` |

**Block note:** A block GEOID omits the block-group digit explicitly because **the first digit of the 4-digit block code represents the block group**. Some blocks may include a **1-character suffix** (e.g., `A`, `B`, `C`). 🧱

---

## 🔄 “Plain GEOID” vs “Fully Qualified GEOID” (joins that won’t bite you later)

### 1) TIGER/Line / Cartographic boundary files (spatial boundaries)

- **Primary join key**: `GEOID`
- **Preferred join key for data.census.gov tables (2023+)**: `GEOIDFQ`
- **Legacy key**: `AFFGEOID` (older vintages)

> 🧩 Practical rule:  
> If a TIGER/Line vintage has **`GEOIDFQ`**, use it for table joins. Otherwise, fall back to `GEOID` + normalization.

---

### 2) data.census.gov downloads (tabular data)

Downloads often include `GEO_ID` (or `GEO.ID`) shaped like:

```text
0500000US48201
^^^^^^^^^  ^^^^^
prefix     plain GEOID
```

**Prefix meaning (conceptual):**
- 3-digit summary level
- 2-digit geographic variant
- 2-digit geographic component
- literal `US`

✅ Net effect: `GEO_ID` is typically **9 characters longer** than the plain TIGER GEOID for the same feature.

---

## 🧪 Normalization & join recipes

### ✅ Recipe A: TIGER/Line 2023+ (or newer) ↔ data.census.gov

**Join:** `data.GEO_ID == tiger.GEOIDFQ`

This is the cleanest path. ✨

---

### ✅ Recipe B: TIGER/Line 2022 or older ↔ data.census.gov

Older TIGER/Line vintages may not include `GEOIDFQ`.  
In that case, **strip the first 9 characters** from `GEO_ID` to recover the plain GEOID:

```text
plain_geoid = GEO_ID[9:]   # keep from the 10th character onward
```

**Join:** `plain_geoid == tiger.GEOID`

---

## 🛠️ Implementation snippets (copy/paste friendly)

### 🐍 Python: normalize + validate

```python
import re

RE = {
    "state": re.compile(r"^\d{2}$"),
    "county": re.compile(r"^\d{5}$"),
    "cousub": re.compile(r"^\d{10}$"),
    "place": re.compile(r"^\d{7}$"),
    "tract": re.compile(r"^\d{11}$"),
    "bg": re.compile(r"^\d{12}$"),
    "block": re.compile(r"^\d{15}[A-Z]?$"),
    "zcta": re.compile(r"^\d{5}$"),
}

def zpad(value: str | int, width: int) -> str:
    return str(value).strip().zfill(width)

def build_geoid_county(statefp: str | int, countyfp: str | int) -> str:
    return zpad(statefp, 2) + zpad(countyfp, 3)

def strip_data_census_prefix(geo_id: str) -> str:
    """
    Converts data.census.gov GEO_ID / GEO.ID like '0500000US48201'
    into '48201' by stripping the first 9 characters.
    """
    s = str(geo_id).strip()
    return s[9:] if len(s) > 9 else s

def validate(kind: str, geoid: str) -> bool:
    return bool(RE[kind].match(geoid))
```

---

### 🐘 Postgres: strip prefix for older TIGER vintages

```sql
-- GEO_ID like '0500000US48201'  ->  '48201'
SUBSTRING(geo_id FROM 10)
```

---

### 🧠 Earth Engine (GEE): keeping `GEOID` as the unique ID

When you pull TIGER boundaries into Earth Engine, use `GEOID` as the stable identifier and
rename it explicitly (helps avoid collisions in joins/export). 🛰️

```javascript
var countiesAll = ee.FeatureCollection('TIGER/2018/Counties');

var countiesSelected = countiesAll
  .filter(ee.Filter.inList('STATEFP', ['20']))   // Kansas = 20 (example)
  .select({
    propertySelectors: ['GEOID'],
    newProperties: ['uniqueID']
  });
```

---

## ✅ Pipeline expectations (KFM)

When a pipeline writes any *Census-derived* processed dataset (GeoJSON/Parquet/etc.), include:

- `geoid` (**string**, normalized)
- `geography` (e.g., `county`, `tract`, `block_group`, `block`, `place`, `zcta`)
- optional: `geoidfq` (if upstream source provides it)

> 📦 Reminder: processed outputs should be “ready-to-use” with stable keys for joins.  
> Also update **catalog/provenance** alongside the dataset so we can trace raw ➜ processed lineage.

---

## 😬 Gotchas (the stuff that breaks joins)

- **Leading zeros**: a missing `0` changes the entity. Treat IDs as strings.
- **ZCTAs** are *not* hierarchical like state/county/tract.
- **Blocks can have a suffix letter** in some cases.
- **Vintage mismatches**: boundaries + codes can change over time. Always record:
  - TIGER vintage (year)
  - dataset vintage (ACS 5-year, Decennial year, etc.)
- **Old field names**: some TIGER vintages use `GEOID10`, `GEOID20`, or `AFFGEOID`.

---

## 🔗 References (authoritative)

- Understanding Geographic Identifiers (GEOIDs): https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html  
- How to match GEOID (data.census.gov ↔ TIGER/Line): https://www.census.gov/data/what-is-data-census-gov/guidance-for-data-users/frequently-asked-questions/how-can-i-match-the-GEOID.html  
- TIGER/Line Shapefiles hub: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html  
- Cartographic Boundary Files (notes on `GEOIDFQ` / `AFFGEOID`): https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html

