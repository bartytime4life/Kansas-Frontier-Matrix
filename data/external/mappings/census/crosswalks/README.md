# 🧬 Census Crosswalks (Geography + Vintage Translation Tables)

![KFM](https://img.shields.io/badge/KFM-Data%20Lake%20%2B%20Pipelines-1f6feb?style=for-the-badge)
![Census](https://img.shields.io/badge/Census-Mappings%20%2F%20Crosswalks-0b7285?style=for-the-badge)
![Format](https://img.shields.io/badge/Formats-CSV%20%7C%20Parquet-495057?style=for-the-badge)
![Policy](https://img.shields.io/badge/Policy-Documented%20%2B%20Reproducible-2b8a3e?style=for-the-badge)

📍 **Path:** `data/external/mappings/census/crosswalks/`

Crosswalks are **translation tables** that map identifiers between **Census geographies** and/or **Census vintages** (e.g., **2010 Tracts → 2020 Tracts**, **ZCTA → County**, **Place → Tract**, etc.).  
They’re the glue that lets KFM do longitudinal analysis when boundaries and codes inevitably change over time. 🧩

> ⚠️ **Important:** A crosswalk fixes *geography alignment*, not *variable definition drift*.  
> If a question changes (“household” vs “housing unit”) or definitions change across releases, you still need semantic harmonization upstream/downstream.

---

## 🧭 Quick Navigation

- [✅ Directory Contract](#-directory-contract)
- [🗂️ Recommended Layout](#️-recommended-layout)
- [🏷️ File Naming Convention](#️-file-naming-convention)
- [📐 Crosswalk Schema](#-crosswalk-schema)
- [⚖️ Weight Semantics](#️-weight-semantics)
- [🧪 Validation Rules](#-validation-rules)
- [🧰 How to Use](#-how-to-use)
- [➕ Adding / Updating Crosswalks](#-adding--updating-crosswalks)
- [🧾 Metadata & Provenance](#-metadata--provenance)
- [📚 Sources](#-sources)

---

## ✅ Directory Contract

### ✅ What belongs here
- 📦 **Authoritative / third-party crosswalks** (Census Bureau, IPUMS/NHGIS, Geocorr, etc.) used as *inputs*.
- 🧊 “Vendor drop” files stored **as-is** (or with minimal packaging changes like compression).
- 🧷 Supporting assets needed to interpret the crosswalk (field docs, provider notes, codebooks).

### 🚫 What does **not** belong here
- 🧪 **Derived crosswalks** produced by KFM (e.g., spatial overlays we compute).  
  Those should be generated deterministically by a pipeline and stored under a **processed** location (then cataloged/provenanced).
- ✍️ Manually edited “quick fixes.” If something must change, **encode it as code** in a pipeline so it’s repeatable.
- 🕵️ Anything without clear **license/attribution** and a paper trail (see metadata section).

---

## 🗂️ Recommended Layout

We keep crosswalks organized by provider, then by geography level and “direction” (source → target).

```text
📁 data/external/mappings/census/crosswalks/
├─ 📄 README.md
├─ 📄 _index.yml                👈 optional but recommended (human + machine friendly)
├─ 📄 checksums.sha256          👈 optional but recommended for “vendor drop” integrity
│
├─ 📁 census_bureau/            🇺🇸 official / TIGER-adjacent releases
│  ├─ 📁 tract/
│  ├─ 📁 block_group/
│  └─ 📁 zcta/
│
├─ 📁 nhgis_ipums/              🧭 NHGIS / IPUMS crosswalk distributions
│  ├─ 📁 county/
│  └─ 📁 tract/
│
├─ 📁 geocorr/                  🧱 MABLE/Geocorr style crosswalks
│  └─ 📁 zcta_to_tract/
│
└─ 📁 local_vendor/             🏛️ state / university / special-purpose providers
```

> 🧠 **Rule of thumb:** Keep “external” clean and provenance-heavy.  
> Anything that smells like transformation belongs in pipelines + processed outputs.

---

## 🏷️ File Naming Convention

**Goal:** You should be able to understand a crosswalk **without opening it**.

### ✅ Recommended pattern

```text
<provider>__<source_geo>_<source_vintage>__to__<target_geo>_<target_vintage>__<weighting>__v<YYYYMMDD>.<ext>
```

Where:
- `provider`: `census_bureau`, `nhgis_ipums`, `geocorr`, `local_vendor`, etc.
- `source_geo` / `target_geo`: `tract`, `bg` (block_group), `county`, `place`, `zcta`, `puma`, etc.
- `vintage`: usually census year (`2000`, `2010`, `2020`) or provider vintage tag
- `weighting`:
  - `unweighted` (1:1 or many:many without weights)
  - `areawt` (area weights)
  - `popwt` (population weights)
  - `multiwt` (multiple weight columns provided)
- `ext`: `parquet` preferred for large; `csv` acceptable for small

### 📌 Examples
- `census_bureau__tract_2010__to__tract_2020__popwt__v20240115.parquet`
- `geocorr__zcta_2020__to__county_2020__areawt__v20231201.csv`
- `nhgis_ipums__county_1990__to__county_2020__unweighted__v20231010.csv`

---

## 📐 Crosswalk Schema

This repo treats crosswalks as **tables** with a predictable schema. If a provider’s native schema differs, we either:
- keep the “vendor drop” intact **and** document it in metadata, or
- generate a standardized derivative in processed data (preferred for heavy usage).

### ✅ Minimum required columns (standardized)

| Column | Type | Required | Meaning |
|---|---:|:---:|---|
| `source_geoid` | string | ✅ | ID on the **source** side (keep leading zeros!) |
| `target_geoid` | string | ✅ | ID on the **target** side |
| `source_geo` | string | ✅ | e.g., `tract`, `county`, `zcta` |
| `target_geo` | string | ✅ | e.g., `tract`, `county`, `zcta` |
| `source_vintage` | int/string | ✅ | e.g., `2010` |
| `target_vintage` | int/string | ✅ | e.g., `2020` |
| `direction` | string | ✅ | usually `source_to_target` |
| `method` | string | ✅ | e.g., `official`, `spatial_overlay`, `provider_tabular` |
| `provider` | string | ✅ | redundant but helpful for lineage |

### ⚖️ Weight columns (optional)
Choose one of these patterns:

**A) Single weight column**
- `weight` (float64) + `weight_type` (`pop`, `area`, `housing`, etc.)

**B) Multiple explicit weight columns**
- `wt_pop` (float64)
- `wt_area` (float64)
- `wt_hu` (float64) *(housing units; optional)*

> ✅ Preferred: **multiple explicit weight columns** when available (it prevents ambiguity).

### 🧼 Strong recommendations
- Always store GEOIDs as **strings**.
- Use **UTF-8**, **LF** line endings, and avoid “smart quotes.”
- Keep types stable across releases (`weight` as float64, ids as string).
- For Parquet: prefer **snappy** compression and stable sorting for deterministic diffs.

---

## ⚖️ Weight Semantics

### 🎛️ Direction
In KFM, “source” means **what your dataset currently uses** and “target” means **what you want to re-aggregate into**.

- `source_geoid` → `target_geoid`
- weights represent *how much of the source unit contributes to the target unit*

### ✅ Sum-to-one expectation (default)
Unless metadata states otherwise:

- For each `source_geoid`, weights across all rows sharing that source should sum to **~1.0** (per weight type).

Why? Because it makes re-aggregation deterministic:

- **Counts** (population, households, events): `count_target = Σ(count_source × weight)`
- **Rates**: aggregate numerator + denominator separately (don’t average rates directly unless you have the correct denominator weights)

### 🧠 Choosing weights
- 👥 Use **population weights** (`wt_pop`) for person-based measures.
- 🗺️ Use **area weights** (`wt_area`) for area-based phenomena (land cover, rainfall, etc.).
- 🏠 Use **housing weights** (`wt_hu`) for housing-based measures if you have them.

> ⚠️ If your variable is a **rate** (e.g., “% unemployed”), never “just weight the rate” unless the weight matches the rate’s denominator.

---

## 🧪 Validation Rules

Crosswalks are notorious for silent failure (wrong join keys = wrong history). We validate aggressively. 🛡️

### ✅ Required checks (for standardized crosswalks)
- 🔑 `source_geoid` and `target_geoid` are **non-null** strings
- 🧾 no unexpected whitespace (trimmed IDs)
- 🧮 weights are in `[0, 1]` (unless explicitly documented)
- 🎯 `sum(weights by source_geoid)` ≈ `1.0` within tolerance (e.g., `±1e-6`)
- 🧷 uniqueness sanity: duplicates are allowed, but must be intentional (many:many)
- 🧊 deterministic sort order (stable diffs):  
  `ORDER BY source_geoid, target_geoid`

### 🔍 Recommended checks
- 🧱 coverage report: `% of sources with complete mapping`
- 🧯 orphan detection:
  - source IDs present in data but missing in crosswalk
  - target IDs in crosswalk that don’t exist in target boundary layer

### 🎛️ Tolerances
Floating weights can drift if rounded.  
**Store full precision**; tolerate tiny errors at validation time.

---

## 🧰 How to Use

### 🐍 Python (counts → counts)

```python
import pandas as pd

# Example: re-aggregate a count measure from source geoid → target geoid
xw = pd.read_parquet("census_bureau__tract_2010__to__tract_2020__popwt__v20240115.parquet")
df = pd.read_parquet("my_dataset.parquet")  # columns: geoid (2010 tract), pop_count

out = (
    df.merge(xw, left_on="geoid", right_on="source_geoid", how="left")
      .assign(pop_count_target=lambda d: d["pop_count"] * d["wt_pop"])
      .groupby("target_geoid", as_index=False)["pop_count_target"].sum()
      .rename(columns={"target_geoid": "geoid", "pop_count_target": "pop_count"})
)

out.to_parquet("my_dataset_tract2020.parquet", index=False)
```

### 🐍 Python (rates → rates, the safe way)

If you have a rate like `unemployment_rate = unemployed / labor_force`:

```python
import pandas as pd

xw = pd.read_parquet("...popwt...parquet")
df = pd.read_parquet("...")  # columns: geoid, unemployed, labor_force

out = (
    df.merge(xw, left_on="geoid", right_on="source_geoid", how="left")
      .assign(
          unemployed_t=lambda d: d["unemployed"] * d["wt_pop"],
          labor_force_t=lambda d: d["labor_force"] * d["wt_pop"],
      )
      .groupby("target_geoid", as_index=False)[["unemployed_t","labor_force_t"]].sum()
      .assign(unemployment_rate=lambda d: d["unemployed_t"] / d["labor_force_t"])
)
```

### 🧮 SQL pattern (Postgres)

```sql
-- Counts: sum(value * weight) into target
SELECT
  x.target_geoid,
  SUM(d.value * x.wt_pop) AS value_target
FROM my_data d
JOIN crosswalk x
  ON d.geoid = x.source_geoid
GROUP BY x.target_geoid;
```

---

## ➕ Adding / Updating Crosswalks

### ✅ Contribution checklist (PR-ready)
1. 📥 **Acquire** the crosswalk from an authoritative source (save “vendor drop” here).
2. 🧾 Record **license + attribution** (provider + terms).
3. 🧷 Add **checksums** if the file is large or externally hosted.
4. 🧪 If standardizing:
   - generate standardized output via a deterministic pipeline
   - validate (sum-to-one, nulls, types)
5. 🧾 Publish/update **metadata + provenance** (see below).
6. 🔗 Update `_index.yml` (if used) so discoverability stays high.

### 🧠 PR rule
If the crosswalk is used by downstream pipelines, **don’t ship it without a validation step** (or a small validation report).

---

## 🧾 Metadata & Provenance

KFM treats crosswalks as first-class “data artifacts,” even when they’re external.  
At minimum, every crosswalk should have:

- 🧾 **Metadata**: title, description, vintages, geography levels, license, provider
- 🧬 **Provenance**: where it came from, when fetched, and if transformed, how/with what pipeline version

### 🧩 Suggested registry entry (`_index.yml`)
```yaml
# _index.yml (optional)
- id: census_bureau__tract_2010__to__tract_2020__popwt__v20240115
  path: census_bureau/tract/census_bureau__tract_2010__to__tract_2020__popwt__v20240115.parquet
  source_geo: tract
  target_geo: tract
  source_vintage: 2010
  target_vintage: 2020
  weights: [pop]
  provider: census_bureau
  license: public_domain
  notes: "Use for person-based allocations; weights sum to 1 by source_geoid."
```

> 🧠 Tip: Keep registry entries short, then rely on STAC/DCAT/PROV (or your project’s catalog system) for the full story.

---

## 📚 Sources

Common crosswalk providers we expect to see referenced here (depending on the dataset/task):

- 🇺🇸 **U.S. Census Bureau** (TIGER/Line related geography products)
- 🧭 **IPUMS NHGIS** (harmonized boundary and tabular tools; may include crosswalk products)
- 🧱 **MABLE/Geocorr** (ZCTA ↔ Tract/County/Place style correspondences)
- 🏛️ **State / University / Historical GIS** providers (domain-specific boundary reconciliation)

> 📌 Always document *exact* release/vintage and the licensing terms in metadata/provenance.

---

<details>
<summary>🧠 Glossary (click to expand)</summary>

- **GEOID**: Geographic Identifier (string; often includes leading zeros)
- **Vintage**: The reference year/version of a geography definition (e.g., 2010 vs 2020 tracts)
- **Crosswalk**: A mapping table translating geographies and/or vintages, optionally with weights
- **Weight**: A fractional allocation coefficient (often population- or area-based)

</details>

