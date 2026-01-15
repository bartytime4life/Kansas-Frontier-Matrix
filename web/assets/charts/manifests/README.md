According to a document from 2026-01-14, KFM is **contract-first** + **provenance-first**: anything shown in the UI must be traceable to **sources, licenses, and processing steps**.

# Chart Manifests 🧾📈

![Governance](https://img.shields.io/badge/governance-provenance--first-brightgreen)
![Contracts](https://img.shields.io/badge/contracts-schema--validated-blue)
![Catalogs](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![UI](https://img.shields.io/badge/UI-responsive%20%2B%20accessible-purple)
![Perf](https://img.shields.io/badge/perf-cache%20%2B%20downsample-yellow)

Declarative **JSON manifests** that power how charts are **discovered, attributed, validated, rendered, and audited** in the KFM web UI.

> ⚠️ **No “mystery charts.”** If it can be rendered, it must be attributable. If it’s attributable, it must be catalog-linked. ✅

---

<details>
<summary><strong>📌 Table of Contents</strong></summary>

- [What lives in this folder](#what-lives-in-this-folder-)
- [Why manifests exist](#why-manifests-exist-)
- [Non-negotiable principles](#non-negotiable-principles-)
- [Folder layout](#folder-layout-)
- [Naming and IDs](#naming-and-ids-)
- [Manifest schema](#manifest-schema-)
- [Provenance and data contracts](#provenance-and-data-contracts-)
- [Chart configuration](#chart-configuration-)
- [Models, uncertainty, and claims](#models-uncertainty-and-claims-)
- [Geo + 3D charts](#geo--3d-charts-)
- [Performance](#performance-)
- [Accessibility](#accessibility-)
- [Security](#security-)
- [Validation and CI](#validation-and-ci-)
- [Examples](#examples-)
- [Contribution workflow](#contribution-workflow-)
- [Project library that shaped this spec](#project-library-that-shaped-this-spec-)

</details>

---

## What lives in this folder 🗂️

This folder contains **chart manifest files** — small, readable JSON documents that define:

- **What** the chart is (title, description, tags, domain)
- **Where** the data comes from (STAC/DCAT/PROV references + asset pointers)
- **How** the data was produced (pipeline references, transforms, versions)
- **How** it should render (chart type, encodings, defaults, interactions)
- **How** it should be trusted (citations, uncertainty, limitations, disclaimers)
- **How** it should be shipped (validation, caching hints, performance caps)

✅ **Manifests are UI-facing contracts**  
🚫 Manifests are **not** raw datasets, and they should not contain secrets, inline executable code, or “magic” undocumented assumptions.

---

## Why manifests exist 🧠

KFM treats charts like “boundary artifacts” in the same spirit as datasets:

- **Front-end components can stay generic** (render whatever the manifest declares)
- **Back-end/API can enforce governance** (schemas, redaction, attribution)
- **Focus Mode can cite evidence** (chart → provenance → catalog → sources)
- **Review becomes tractable** (diff a manifest; don’t diff a mystery UI)

---

## Non-negotiable principles 🔒

### 1) Provenance-first 🧬
Every chart must contain enough metadata to explain **where it came from** and **how it was produced**.

### 2) Contract-first 🧩
Manifests must validate against a **versioned schema**. If you add a field, you add it via schema evolution (not ad-hoc).

### 3) Deterministic by default 🎯
A chart should render the *same way* given the same inputs. Prefer reproducible pipelines and pinned versions.

### 4) Human-centered + evidence-first 🧑‍🤝‍🧑
If a chart implies interpretation (trend, causal claim, prediction), encode:
- limitations
- uncertainty
- “what this does/does not mean”

### 5) Responsive + accessible 📱♿
Manifests must carry a11y metadata (summary/caption/table fallback) so charts remain usable across devices and assistive tech.

### 6) Secure-by-default 🛡️
Manifests are data — treat them as untrusted input. Validate and sanitize everything.

---

## Folder layout 📁

A recommended shape (you can evolve it, but keep it tidy and discoverable):

```text
web/
└─ 🌐🧩 assets/
   └─ 📈 charts/
      └─ 🧾 manifests/
         ├─ 📄 README.md
         ├─ 📐 schema/
         │  └─ 📐🧾 chart-manifest.schema.json
         ├─ 🧪 examples/
         │  ├─ 📈🧪 timeseries.line.v1.json
         │  └─ 🗺️📊🧪 geo.choropleth.v1.json
         └─ 🧭 domains/
            ├─ 🌾 agriculture/
            │  └─ 🌾📊 crop_yield_by_county.v1.json
            ├─ 🌧️ climate/
            │  └─ 🌧️📊 precip_monthly_by_county.v1.json
            └─ 🏛️ history/
               └─ 🏛️📈 treaty_signings_over_time.v1.json
```

> ✅ Tip: keep manifests small and composable. If you need “logic,” reference a pipeline artifact — don’t embed code blobs.

---

## Naming and IDs 🏷️

### File naming
- **kebab_case** or **snake_case** is fine, but be consistent per domain.
- Include a version suffix for stability:
  - `precip_monthly_by_county.v1.json`
  - `precip_monthly_by_county.v2.json`

### `id` format
Use a stable, globally unique ID string:

- Recommended: `kfm.chart.<domain>.<name>`
  - `kfm.chart.climate.precip_monthly_by_county`

### `slug`
Optional, URL-safe UI route helper:
- `climate/precip-monthly-by-county`

---

## Manifest schema 🧬

Manifests should be JSON and follow a versioned schema. A pragmatic v1 shape:

### Top-level fields (v1)

| Field | Type | Required | Purpose |
|------|------|----------|---------|
| `$schema` | string | ✅ | Points to the JSON Schema used for validation |
| `kind` | string | ✅ | `"chart"` (future-proofing for other manifest types) |
| `manifestVersion` | string | ✅ | Schema version (SemVer) |
| `id` | string | ✅ | Stable chart ID |
| `title` | string | ✅ | Human readable name |
| `description` | string | ✅ | What the user is looking at |
| `domain` | string | ✅ | e.g. `climate`, `history`, `agriculture` |
| `status` | string | ✅ | `draft` \| `review` \| `published` \| `deprecated` |
| `tags` | string[] | ⛳ | Search + filtering in UI |
| `provenance` | object | ✅ | Links to STAC/DCAT/PROV + licensing + attribution |
| `data` | object | ✅ | Where the data asset lives, format, fields |
| `chart` | object | ✅ | Chart type + encodings + UX |
| `performance` | object | ⛳ | Limits/caching hints |
| `accessibility` | object | ✅ | Summary/caption/table fallback |
| `security` | object | ⛳ | Allowed origins, sanitization rules |
| `model` | object | ⛳ | Model card-like metadata (if inferred/predicted) |

⛳ = optional but strongly recommended

---

## Provenance and data contracts 🧾

A manifest must connect to KFM’s catalog standards:

- 🛰️ **STAC**: assets & spatiotemporal descriptors (when geo)
- 🧠 **DCAT**: dataset discovery & distribution links
- 🧬 **PROV**: lineage bundles (inputs → steps → outputs)

### Provenance block (minimum)

- **license**: what users are allowed to do
- **attribution**: who gets credit
- **catalog links**: pointers to STAC/DCAT/PROV artifacts
- **method note**: short “how this was built” for humans

---

## Chart configuration 🎛️

Manifests should be library-agnostic where possible, but must specify enough for a renderer:

- `type`: line, bar, scatter, area, histogram, boxplot, heatmap, etc.
- `encoding`: x/y fields, series, color grouping, tooltip fields
- `defaults`: initial filters (county, year, category)
- `interactions`: hover, brush, zoom, click → inspect
- `thumbnail`: optional icon/preview asset (SVG preferred)

---

## Models, uncertainty, and claims 📉🧪

If a chart represents **inference** (regression line, forecast, classification, clustering), the manifest must declare:

- **what model was used**
- **training/evaluation scope**
- **metrics**
- **uncertainty representation**
- **limitations / non-claims**

Suggested pattern:

- `model` → “model card lite”
- `uncertainty` → intervals/bands, method, confidence level
- `claims` → what is OK to say, what is not OK to say

---

## Geo + 3D charts 🗺️🧊

For geospatial charts (choropleths, point maps, tiles, 3D terrain):

Include:

- `crs` (EPSG code)
- `bbox` and/or `spatialExtent`
- `geometryType` (point/line/polygon/raster/tile)
- tile source metadata (vector tiles vs raster)
- `lod` hints for 3D (levels of detail), if applicable

> ✅ If it’s streamed 3D (e.g., 3D Tiles), the manifest should explicitly declare it so performance budgets can be enforced.

---

## Performance ⚡

Manifests can set guardrails:

- `maxPoints`: cap client-side rendering load
- `downsample`: `none` \| `lttb` \| `bin` \| `aggregate`
- `cache`:
  - `strategy`: `etag` \| `immutable` \| `ttl`
  - `ttlSeconds`: e.g., 86400
- `preAggregated`: true/false (prefer true for big data)

---

## Accessibility ♿

Every manifest must include:

- `summary`: 1–3 sentence description for screen readers
- `caption`: short human caption
- `tableFallback`: whether to provide a tabular view
- `keyboardInteractions`: documented controls if relevant

> ✅ Accessibility metadata belongs *with the chart spec*, not buried in UI code.

---

## Security 🛡️

Recommended manifest-level security knobs:

- `allowedDataOrigins`: allowlist of origins/domains (or `localOnly: true`)
- `sanitize`: how to treat labels/markdown/HTML (prefer plain text)
- `pii`: true/false + redaction note (if chart is derived from sensitive inputs)

> 🚫 Never allow manifests to point to arbitrary third-party script execution.

---

## Validation and CI ✅

At minimum, CI should:

- JSON Schema validate all manifests
- verify referenced assets exist (when local)
- verify referenced catalog artifacts exist (STAC/DCAT/PROV pointers)
- lint IDs (uniqueness, formatting)
- (optional) run screenshot/regression tests for critical charts

---

## Examples ✅

### Example 1: Time series line chart (v1)

```json
{
  "$schema": "./schema/chart-manifest.schema.json",
  "kind": "chart",
  "manifestVersion": "1.0.0",
  "id": "kfm.chart.climate.precip_monthly_by_county",
  "slug": "climate/precip-monthly-by-county",
  "title": "Monthly precipitation by county",
  "description": "Monthly precipitation (mm) aggregated by Kansas county. Use filters to compare counties over time.",
  "domain": "climate",
  "status": "published",
  "z
  "tags": ["climate", "precipitation", "time-series", "county"],

  "provenance": {
    "license": "CC-BY-4.0",
    "attribution": "Source: NOAA (or relevant provider). Processing: KFM climate pipeline.",
    "dcat": "data/catalog/dcat/climate_precipitation.jsonld",
    "stac": {
      "collection": "data/stac/collections/climate_precipitation.json",
      "items": [
        "data/stac/items/climate/precip_monthly_2020_2025.json"
      ]
    },
    "prov": "data/prov/climate/precip_monthly/prov.json",
    "method": "Monthly aggregation from daily observations; spatial join to county boundaries."
  },

  "data": {
    "asset": "data/processed/climate/precip_monthly_by_county.parquet",
    "format": "parquet",
    "primaryKey": ["month", "county_fips"],
    "fields": [
      { "name": "month", "type": "date" },
      { "name": "county_fips", "type": "string" },
      { "name": "county_name", "type": "string" },
      { "name": "precip_mm", "type": "number", "unit": "mm" }
    ]
  },

  "chart": {
    "renderer": "generic",
    "type": "line",
    "encoding": {
      "x": { "field": "month", "type": "temporal", "label": "Month" },
      "y": { "field": "precip_mm", "type": "quantitative", "label": "Precipitation (mm)" },
      "series": { "field": "county_name", "type": "nominal", "label": "County" },
      "tooltip": ["month", "county_name", "precip_mm"]
    },
    "defaults": {
      "filters": { "county_fips": "20173" }
    },
    "thumbnail": "web/assets/charts/thumbnails/precip_monthly_by_county.svg"
  },

  "performance": {
    "maxPoints": 5000,
    "downsample": "lttb",
    "cache": { "strategy": "etag" }
  },

  "accessibility": {
    "summary": "A line chart showing monthly precipitation over time for a selected county, with optional comparison across counties.",
    "caption": "Monthly precipitation (mm) by county over time.",
    "tableFallback": true
  }
}
```

> 📝 Note: `renderer: "generic"` intentionally avoids locking us to a single chart library. The UI adapter chooses the implementation.

---

### Example 2: Choropleth (county-level) 🗺️

```json
{
  "$schema": "./schema/chart-manifest.schema.json",
  "kind": "chart",
  "manifestVersion": "1.0.0",
  "id": "kfm.chart.agriculture.crop_yield_by_county_2024",
  "slug": "agriculture/crop-yield-by-county-2024",
  "title": "Crop yield by county (2024)",
  "description": "County choropleth of crop yield for the selected crop in 2024.",
  "domain": "agriculture",
  "status": "review",
  "tags": ["agriculture", "county", "choropleth"],

  "provenance": {
    "license": "TBD",
    "attribution": "Source: USDA (or relevant provider). Processing: KFM agriculture pipeline.",
    "dcat": "data/catalog/dcat/usda_crop_yield.jsonld",
    "stac": {
      "collection": "data/stac/collections/usda_crop_yield.json",
      "items": ["data/stac/items/agriculture/crop_yield_2024.json"]
    },
    "prov": "data/prov/agriculture/crop_yield_2024/prov.json",
    "method": "Normalized units, joined to county polygons; missing values encoded as null."
  },

  "data": {
    "asset": "data/processed/agriculture/crop_yield_by_county_2024.geojson",
    "format": "geojson",
    "crs": "EPSG:4326",
    "fields": [
      { "name": "county_name", "type": "string" },
      { "name": "county_fips", "type": "string" },
      { "name": "crop", "type": "string" },
      { "name": "yield", "type": "number", "unit": "bu/acre" }
    ]
  },

  "chart": {
    "renderer": "map",
    "type": "choropleth",
    "encoding": {
      "geometry": { "field": "geometry" },
      "color": { "field": "yield", "type": "quantitative", "label": "Yield (bu/acre)" },
      "tooltip": ["county_name", "crop", "yield"]
    },
    "defaults": {
      "filters": { "crop": "corn" }
    },
    "legend": {
      "format": "quantize",
      "missingLabel": "No data"
    }
  },

  "accessibility": {
    "summary": "A county-level map showing crop yield intensity across Kansas for a selected crop in 2024.",
    "caption": "County choropleth of crop yield (2024).",
    "tableFallback": true
  },

  "security": {
    "localOnly": true
  }
}
```

---

## Contribution workflow 🧑‍💻

1) Pick a domain folder under `domains/` (or create one). 📂  
2) Duplicate an example manifest and rename it to `*.v1.json`. 🧾  
3) Fill in **provenance** first (license + attribution + catalog refs). 🧬  
4) Point `data.asset` to an existing, published artifact (or add the pipeline that publishes it). 📦  
5) Run validations (schema + link checks). ✅  
6) Add/refresh `thumbnail` (SVG preferred). 🖼️  
7) PR with a short “what changed + why” and include screenshots for UI review. 🔎  

---

## Project library that shaped this spec 📚

<details>
<summary><strong>📚 Click to expand the full library map</strong></summary>

### 🧭 Core KFM Docs (governance + pipeline invariants)
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** — provenance-first, contract-first, clean architecture, UI composition
- **MARKDOWN_GUIDE_v13.md.gdoc** — governed pipeline ordering + STAC/DCAT/PROV alignment rules
- **Scientific Method _ Research _ Master Coder Protocol Documentation.pdf** — dataset docs, experiment rigor, model cards, reproducibility patterns
- **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf** — system vision + cross-subsystem boundaries

### 🌐 Web + Visualization
- **responsive-web-design-with-html5-and-css3.pdf** — responsive assets (SVG is ideal for sharp chart thumbnails/icons) 📱
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** — 3D rendering budgets + WebGL mental model 🧊
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** — choosing PNG/JPEG/GIF for previews and exports 🖼️

### 🗺️ GIS + Mapping + Remote Sensing
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf** — cartographic clarity, legends, and encoding choices 🗺️
- **python-geospatial-analysis-cookbook.pdf** — GeoJSON/PostGIS pipelines, spatial joins, export patterns 🧰
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** — projections, bands, pixel scale, viz parameters 🛰️
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** — mobile UX + mapping in context 📍
- **Archaeological 3D GIS_26_01_12_17_53_09.pdf** — temporal/3D GIS narratives + evidence visualization 🏺

### 📊 Statistics + Data Science + Modeling
- **Understanding Statistics & Experimental Design.pdf** — uncertainty, experimental rigor, interpretation guardrails 🧪
- **regression-analysis-with-python.pdf** — performance/scaling + regression reporting patterns 📈
- **Regression analysis using Python - slides-linear-regression.pdf** — compact regression references 🧾
- **think-bayes-bayesian-statistics-in-python.pdf** — credible intervals and uncertainty communication 🎲
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** — units, simulation traceability, verification/validation 🧑‍🚀
- **Generalized Topology Optimization for Structural Design.pdf** — simulation outputs + parameterized runs 🧱
- **Spectral Geometry of Graphs.pdf** — graph metrics and network visualization foundations 🕸️

### 🧠 Data Platforms + Performance + Databases
- **Scalable Data Management for Future Hardware.pdf** — streaming + windowing + heterogeneous acceleration ⚡
- **Database Performance at Scale.pdf** — indexing, caching, query discipline 🗄️
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** — SQL/Postgres fundamentals 🐘
- **Data Spaces.pdf** — reference architectures + cross-cutting concerns (standards, security, trust) 🧩
- **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** — real-time thinking for streaming dashboards ⏱️

### 🔐 Security + Safety + Governance
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** — threat models for external sources + ingestion 🛡️
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** — secure coding mindset & attack surface awareness 🧯
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** — transparency + legal framing for ML outputs ⚖️

### 🧑‍🤝‍🧑 Human-centered + Ethics
- **Introduction to Digital Humanism.pdf** — accountability, transparency, human-in-the-loop principles 🤝
- **Principles of Biological Autonomy - book_9780262381833.pdf** — system “closure” as a metaphor for strong contracts/guards 🧬

### 🧰 General Engineering Library Bundles (language + systems breadth)
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** — model training and evaluation discipline (for charts backed by ML) 🧠

</details>
