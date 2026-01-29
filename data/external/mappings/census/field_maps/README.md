# 🧭 Census Field Maps (Schema Translation Layer)

![Status](https://img.shields.io/badge/status-active-success)
![Scope](https://img.shields.io/badge/scope-census%20mappings-blue)
![Artifacts](https://img.shields.io/badge/artifacts-YAML%20%7C%20JSON-orange)
![ETL](https://img.shields.io/badge/ETL-deterministic-important)

> **What this folder is:** a **version-controlled “translation layer”** that maps *external Census fields* (columns, codes, table IDs) into the **Kansas Frontier Matrix (KFM)** canonical schema.  
> **What this folder is not:** a place for processed outputs, ad-hoc cleanup scripts, or one-off transforms.

---

## ✨ Why this exists

Census sources change across:
- **time** (vintages / decades / ACS releases),
- **geographies** (state/county/tract/block group/block),
- **tables** (naming, codes, definitions),
- **formats** (CSV, fixed-width, shapefile/GeoPackage attributes, API extracts).

Field maps keep those differences **explicit, reviewable, and reproducible** so ingestion pipelines can stay deterministic and “audit-friendly” (raw → processed → catalog/provenance → DB → API → UI). :contentReference[oaicite:0]{index=0}

---

## 🧱 Where Field Maps sit in the KFM data flow

```mermaid
flowchart LR
  A[📥 data/raw/<source>/] --> B[🧪 pipelines/* import + clean]
  B --> C[📦 data/processed/census/]
  C --> D[🧾 data/catalog/ (STAC-ish metadata)]
  C --> E[🧬 data/provenance/ (lineage logs)]
  D --> F[(🗄️ Database)]
  E --> F
  F --> G[🔌 API]
  G --> H[🗺️ UI]
```

**Field maps are consumed in step B** (“import + clean”) to rename fields, cast types, normalize units, and document meaning **without hiding changes inside code-only logic**. Deterministic pipelines and the canonical order above are required for KFM-style workflows. :contentReference[oaicite:1]{index=1}

---

## 📁 Folder layout

> (Your exact contents may evolve, but keep the *intent* consistent: small, diffable mapping artifacts.)

```text
📦 data/
└─ 📂 external/
   └─ 📂 mappings/
      └─ 📂 census/
         └─ 📂 field_maps/
            ├─ 📄 README.md  👈 you are here
            ├─ 📄 <dataset>__<vintage>__<geo>__<table>.yml
            ├─ 📄 <dataset>__<vintage>__<geo>__<table>.json
            ├─ 📂 examples/
            │  └─ 📄 demo__1900__county__population.yml
            └─ 📂 schemas/
               └─ 📄 field_map.schema.json
```

---

## 🧾 What a “Field Map” should describe

A field map should be able to answer:

- **What is the source?** (provider, table IDs, download URL or citation)
- **What vintage?** (year / release / edition)
- **What geography level?** (county, tract, block group…)
- **How do source columns become canonical columns?**
- **What type/unit transformations happen?**
- **What derived fields exist (if any), and how are they computed?**
- **What QA rules apply?** (ranges, required fields, null handling)
- **What privacy/sensitivity constraints apply?**

> 📌 Good field maps make “hidden assumptions” impossible.

---

## 🧩 Suggested Field Map schema (human-readable)

You can represent field maps as **YAML** (preferred for editing) or **JSON** (preferred for tooling).

### ✅ Recommended top-level keys

| Key | Type | Why it matters |
|---|---:|---|
| `id` | string | Stable identifier (used by pipelines) |
| `title` | string | Human name for reviews / UI |
| `vintage` | int/string | Year or release label |
| `source` | object | Provenance + citation |
| `geography` | object | Geo level + GEOID rules + CRS |
| `fields` | list | Core mapping: source → canonical |
| `derivations` | list | Optional computed fields |
| `quality` | object | Validation + constraints |
| `privacy` | object | Suppression flags + notes |
| `notes` | string | Anything reviewers should know |

---

## 🧪 Example Field Map (YAML)

> This is an illustrative template; replace with real dataset details.

```yaml
id: decennial__1900__county__population
title: "US Decennial Census 1900 — County Population (Kansas focus)"
vintage: 1900

source:
  provider: "US Census / secondary distributor (e.g., NHGIS)"
  table: "POPULATION_TOTAL"
  license: "Public domain (verify per source)"
  citation: "Fill in a real citation / dataset landing page"
  retrieved_at: "YYYY-MM-DD"

geography:
  level: "county"
  canonical_geoid: "GEOID"              # what KFM expects downstream
  geoid_components: ["STATEFP", "COUNTYFP"]
  crs: "EPSG:4326"                      # normalize early; avoid CRS drift
  notes: "Convert/validate if source CRS differs."

fields:
  - source: "STATEFP"
    target: "state_fips"
    type: "string"
    required: true

  - source: "COUNTYFP"
    target: "county_fips"
    type: "string"
    required: true

  - source: "POP_TOT"
    target: "population_total"
    type: "int"
    units: "persons"
    required: true

  - source: "NAME"
    target: "county_name"
    type: "string"
    required: false

derivations:
  - target: "geoid"
    type: "string"
    formula: "state_fips + county_fips"
    description: "Compose canonical GEOID for county-level joins."

quality:
  null_values: ["", "NA", "N/A", "NULL"]
  constraints:
    population_total:
      min: 0

privacy:
  sensitivity: "low"
  notes: >
    Aggregated county-level counts are generally public, but still validate small-cell policies
    if joining with other sensitive attributes.
```

---

## 🔧 How pipelines should use Field Maps

**Rule of thumb:** pipelines do the *work*, field maps define the *contract*.

### Typical ingestion steps (KFM-style)

1. **Read inputs from `data/raw/`**
2. **Process & clean** using this field map (rename/cast/normalize)
3. **Write outputs to `data/processed/`** (ready-to-use, correct CRS/columns)
4. **Update `data/catalog/` + `data/provenance/`** (hard requirement)
5. Load to DB → API → UI

This “Raw → Processed → Catalog/Prov → Database → API → UI” sequence is considered canonical. :contentReference[oaicite:2]{index=2}

### Pseudocode pattern

```python
raw_df = read_raw("data/raw/census_1900/census_1900.csv")

field_map = load_field_map("decennial__1900__county__population")  # from this folder
df = apply_field_map(raw_df, field_map)                             # rename, cast, derive, validate

write_processed(df, "data/processed/census/1900_population.parquet")

update_catalog_and_provenance(
  dataset_id=field_map["id"],
  outputs=["data/processed/census/1900_population.parquet"],
  inputs=["data/raw/census_1900/census_1900.csv"],
)
```

> ✅ Pipelines should be deterministic: same inputs/config → byte-identical outputs, no interactive prompts, no manual “fix it by hand” steps. :contentReference[oaicite:3]{index=3}

---

## 🧷 Naming conventions

Use filenames that sort well and tell the truth:

```text
<dataset>__<vintage>__<geo_level>__<table_or_theme>.yml
```

Examples:
- `decennial__1900__county__population.yml`
- `acs__2022_5yr__tract__income.yml`
- `tiger__2020__block_group__boundaries.yml`

---

## ✅ QA checklist (PR-ready)

Before merging a new/updated field map:

- [ ] **Unique `id`** (never reuse an `id` for different semantics)
- [ ] **All required fields present**
- [ ] **Types are explicit** (`int`, `float`, `string`, `bool`, `date`)
- [ ] **Units are documented** (especially rates vs totals)
- [ ] **Geography keys are unambiguous** (GEOID rules clear)
- [ ] **CRS normalization stated** (and enforced in pipeline)
- [ ] **Constraints declared** (min/max/allowed values where known)
- [ ] **Privacy notes included** (see below)
- [ ] **Pipeline + provenance updated** (raw → processed → metadata logs)

---

## 🔐 Privacy & ethics notes (Census data is not “free-for-all”)

Even when data is public, **how you map/aggregate it matters**.

- The Census counts people at addresses, but address-level detail is withheld to protect privacy; we typically work with **aggregated units** (block group / tract / county) and respect suppression norms. :contentReference[oaicite:4]{index=4}  
- Aggregation can **change the story** (boundaries, skew, and misinterpretation). Field maps should clearly declare whether a field is a **total**, **rate**, or **derived statistic**, and what geographic unit it belongs to. :contentReference[oaicite:5]{index=5}

> ⚠️ If a map risks identifying individuals (tiny cells, sensitive attributes), add a `privacy.sensitivity` flag and document suppression/rounding expectations.

---

## 🧠 Design philosophy (keep it boring, keep it true)

Field maps should be:
- **Small** 🪶 (diff-friendly)
- **Explicit** 🧾 (no hidden transforms)
- **Reusable** ♻️ (pipelines can share logic)
- **Auditable** 🔎 (source + definitions + constraints)
- **Deterministic** 🧪 (repeatable every run) :contentReference[oaicite:6]{index=6}

---

## 📚 References (Project grounding)

- Kansas Frontier Matrix (KFM) — Comprehensive Technical Blueprint :contentReference[oaicite:7]{index=7}  
- *Making Maps: A Visual Guide to Map Design for GIS* (notes on census aggregation + privacy) :contentReference[oaicite:8]{index=8}

