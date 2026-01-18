# 📊 Raw Chart Assets Spec (KFM)

![Spec](https://img.shields.io/badge/spec-v1.0.0-blue) ![Status](https://img.shields.io/badge/status-draft-yellow) ![Contract--first](https://img.shields.io/badge/contract--first-yes-success) ![Provenance](https://img.shields.io/badge/provenance-required-orange) ![UI](https://img.shields.io/badge/scope-web%20assets-8A2BE2)

> **Folder:** `web/assets/media/charts/raw/`  
> **This doc:** `web/assets/media/charts/raw/spec/README.md` ✅  
> **Goal:** Keep charts **consistent**, **traceable**, and **UI-friendly** (pop-ups, side panels, Story Nodes, Focus Mode). 🧭

---

## ✨ What “raw charts” means here

Raw chart assets are the **editable source-of-truth** inputs for charts used by the web UI:

- 🧾 **A chart contract (manifest)** describing *what the chart is* + *where its data comes from* + *how it’s rendered*
- 📦 Optional **small static data** for demos/mocks (only when explicitly allowed)
- 🖼️ Optional **preview media** (SVG/PNG) for catalogs, docs, or Story Node thumbnails

**Important principle:** KFM is **contract-first** and **provenance-first**.  
Charts used as “evidence” in narratives must be **traceable** back to cataloged sources (STAC/DCAT) with lineage (PROV). 🔗

---

## ✅ Non-goals (what this folder is NOT for)

🚫 Do **not** treat `web/assets/...` as a hidden data lake.

- ❌ No large datasets here (use `data/<domain>/...` + catalogs + API)
- ❌ No “mystery charts” with unknown origins
- ❌ No chart images used in Focus Mode / Story Nodes without provenance metadata
- ❌ No direct database dumps, personal data, or sensitive-location leakage

---

## 🗂️ Recommended directory layout

> This is the recommended shape; adjust if the repo’s exact structure differs, but keep the same semantics.

```text
web/assets/media/charts/
├── raw/
│   ├── spec/                         🧾 This spec + examples
│   │   ├── README.md                 📘 (you are here)
│   │   └── examples/
│   │       ├── sparkline.manifest.json
│   │       └── county_rainfall.manifest.json
│   ├── charts/
│   │   └── <chart_id>/               📌 One folder per chart (recommended)
│   │       ├── manifest.json         🧾 REQUIRED (chart contract)
│   │       ├── preview.svg           🖼️ Optional (preferred)
│   │       ├── preview.png           🖼️ Optional fallback
│   │       └── data.csv              📦 Optional (ONLY allowed for demo/mocks)
│   └── _registry.json                🗃️ Optional index for quick discovery
└── (optimized|dist)/                 ⚡ Build outputs (if used by toolchain)
```

---

## 🔁 Asset lifecycle (how charts should flow)

```mermaid
flowchart LR
  A[📦 Cataloged data<br/>STAC/DCAT/PROV] -->|API query / pipeline| B[📈 Chart data]
  B --> C[🧾 Chart manifest<br/>contract artifact]
  C --> D[🖥️ Web UI chart component<br/>(pop-up / sidebar / story)]
  C --> E[🖼️ Optional static render<br/>(SVG/PNG)]
```

**Rule of thumb:**
- If it’s **interactive** → UI fetches from **API** using manifest instructions.
- If it’s **evidence** (Story Node / Focus Mode) → it must be **catalog-registered** (and the manifest must point to that).

---

## 🧾 The Chart Manifest (contract artifact)

Each chart **MUST** have a `manifest.json` (or `*.manifest.json`) that is:

- ✅ machine-readable
- ✅ versioned
- ✅ provenance-linked
- ✅ renderable by the UI (directly or via a renderer adapter)

This manifest is considered a **contract artifact** (similar to schema/API contracts), so:
- **No breaking changes** without a **version bump**. 🔧

### Manifest file naming

✅ Preferred:
- `web/assets/media/charts/raw/charts/<chart_id>/manifest.json`

✅ Also allowed:
- `web/assets/media/charts/raw/spec/examples/<chart_id>.manifest.json` (examples only)

---

## 📌 Chart ID rules

**MUST:**
- `kebab-case`
- stable over time
- globally unique within the repo

✅ Examples:
- `weather-station-sparkline`
- `county-rainfall-timeseries`
- `landcover-change-summary`

---

## 🧩 Manifest schema (v1.0.0)

> Canonical schema should live under `schemas/ui/` (per Master Guide). This folder documents the spec and keeps examples.

### Required fields

| Field | Type | Purpose |
|------|------|---------|
| `schema_version` | string | Manifest schema version (e.g. `1.0.0`) |
| `id` | string | Chart ID (`kebab-case`) |
| `title` | string | Human label |
| `summary` | string | One-liner for UI tooltips |
| `chart_type` | string | `line`, `bar`, `area`, `scatter`, `histogram`, `sparkline`, … |
| `context` | array | Where it’s used: `popup`, `details_panel`, `story_node`, `focus_mode`, `docs` |
| `data` | object | Where data comes from (API/file/inline) |
| `encoding` | object | How to map fields to axes/series |
| `provenance` | object | Sources + license + catalog references |
| `accessibility` | object | Alt text + non-visual description |

### Strongly recommended fields

- `units` (per metric/series)
- `time` (time range + timezone)
- `style` (palette + semantics)
- `sensitivity` (classification tags)
- `ui` (preferred size + formatting hints)

---

## 🧾 Example manifest (API-backed sparkline)

```json
{
  "schema_version": "1.0.0",
  "id": "weather-station-sparkline",
  "title": "Weather station trend (last 10 years)",
  "summary": "Sparkline used in station pop-ups",
  "chart_type": "sparkline",
  "context": ["popup", "details_panel"],

  "data": {
    "kind": "api",
    "ref": {
      "endpoint": "/api/v1/series/weather-station/{station_id}",
      "method": "GET",
      "params": {
        "metric": "precip_mm",
        "range": "10y",
        "interval": "monthly"
      }
    },
    "format": "json",
    "shape": "long"
  },

  "encoding": {
    "x": { "field": "date", "type": "temporal" },
    "y": { "field": "value", "type": "quantitative" }
  },

  "units": {
    "value": "mm"
  },

  "time": {
    "timezone": "UTC",
    "display": "month",
    "label_required": true
  },

  "style": {
    "palette": "colorblind-safe",
    "avoid_pairs": ["red-green"],
    "semantic_rules": {
      "precip": "blue-ish",
      "temperature": "warm-scale"
    }
  },

  "accessibility": {
    "alt": "Sparkline showing monthly precipitation trend for the last 10 years.",
    "long_description": "A compact line chart for quick trend reading. Exact values are available via tooltip and table view."
  },

  "provenance": {
    "catalog_refs": {
      "stac_items": ["stac:item:climate:noaa:precip:station-timeseries"],
      "dcat_datasets": ["dcat:dataset:noaa:climate-observations"],
      "prov_bundles": ["prov:run:2024-09-18_weather_station_series_build"]
    },
    "sources": [
      {
        "title": "NOAA Climate Observations",
        "type": "dataset",
        "citation": "See DCAT record for formal citation text",
        "url": "https://example.invalid/replace-with-dcat-link"
      }
    ],
    "license": "CC-BY-4.0",
    "attribution": "NOAA (via KFM processing pipeline)"
  },

  "sensitivity": {
    "classification": "public",
    "notes": "No sensitive locations; station ids are public."
  },

  "ui": {
    "preferred_size_px": { "width": 220, "height": 48 },
    "show_gridlines": false,
    "show_points": false,
    "tooltip": "on-hover",
    "fallback": "table"
  }
}
```

---

## 📦 Data rules (API vs file vs inline)

### 1) `data.kind = "api"` ✅ (preferred)
Use when the chart is driven by:
- dynamic user selection (clicked feature, selected county, time slider)
- large or frequently updated datasets
- anything “evidence-like”

**MUST:**
- reference an API endpoint, not a raw DB/table name
- include required params + defaults
- keep payloads small (pre-aggregate server-side if needed)

### 2) `data.kind = "file"` ⚠️ (limited)
Allowed only for:
- UI demos / design mocks
- tiny static reference charts used in docs (with provenance)

**MUST NOT:**
- ship large data files
- bypass catalog governance for Story Nodes / Focus Mode evidence

### 3) `data.kind = "inline"` 🚫 (discouraged)
Allowed only for minimal examples (like 5–10 points) in `spec/examples/`.

---

## 📐 Data shape conventions

To keep chart adapters simple, use one of these shapes:

### ✅ Long (tidy) format (preferred)
One row = one observation.

| date | series | value |
|------|--------|-------|
| 2020-01-01 | precip_mm | 12.4 |

### ✅ Wide format (allowed)
Use if it’s significantly smaller/cleaner.

| date | precip_mm | temp_c |
|------|-----------|--------|

**Time fields MUST:**
- be ISO-8601 strings (`YYYY-MM-DD` or full timestamp)
- declare timezone if ambiguous

---

## 🎨 Visual + labeling conventions (chart hygiene)

Borrowing from KFM’s broader visualization conventions:

**MUST:**
- include **units** in axis labels or legend (`mm`, `°C`, `people`, etc.)
- label **time context** clearly (especially for exported images)
- use **colorblind-friendly palettes**
- avoid classic red/green ambiguity
- keep symbology consistent across similar metrics (don’t reinvent temperature colors)

**SHOULD:**
- use sparklines in pop-ups for quick trend read
- provide a table fallback for exact values (accessibility + verification)

---

## ♿ Accessibility rules

**Every chart MUST provide:**
- `accessibility.alt` (short)
- `accessibility.long_description` (when chart is non-trivial)

**Interactive charts SHOULD:**
- be keyboard navigable
- expose values to screen readers (or provide an accessible table view)
- avoid “color-only” encoding (use symbols/labels when needed)

---

## 🛡️ Governance + sensitivity

If any input data is restricted/sensitive, the chart output **inherits the strictest classification**.

**MUST:**
- set `sensitivity.classification` correctly (`public`, `restricted`, `sensitive`)
- never publish precise sensitive locations if governance forbids it
- avoid embedding personal data or re-identification vectors

---

## ⚡ Performance rules (web-friendly charts)

**MUST:**
- keep pop-up charts lightweight (think “sparkline”, not “dashboard”)
- prefer server-side aggregation/downsampling for long time series
- avoid shipping massive CSVs/JSON blobs in `web/assets/`

**SHOULD:**
- lazy-load chart data on demand (click/open panel)
- cache results by query key (client or edge)
- compress/optimize preview images (SVG preferred; PNG only when needed)

---

## ✅ Review checklist (add / change a chart)

Before opening a PR:

- [ ] 📌 Chart has a stable `id` (`kebab-case`)
- [ ] 🧾 `manifest.json` exists and validates against the UI chart schema
- [ ] 🔗 `provenance` includes **license + attribution** and **catalog refs** when applicable
- [ ] 📏 Units + time labeling are present
- [ ] ♿ `accessibility.alt` is written (and `long_description` when needed)
- [ ] 🛡️ Sensitivity classification is correct
- [ ] ⚡ Payload/perf is reasonable (no giant static data files in web assets)

---

## 🔗 Related standards & project docs

- 📘 Master pipeline & repo structure: `docs/MASTER_GUIDE_v13.md`
- 🧾 Contract-first + evidence rules: `docs/MASTER_GUIDE_v13.md` + `docs/governance/REVIEW_GATES.md`
- 🗂️ Metadata catalogs (profiles):  
  - `docs/standards/KFM_STAC_PROFILE.md`  
  - `docs/standards/KFM_DCAT_PROFILE.md`  
  - `docs/standards/KFM_PROV_PROFILE.md`
- 🧩 Schemas live under: `schemas/ui/` (UI contracts)

---

## 🧪 Appendix: Minimal example (file-backed mock)

```json
{
  "schema_version": "1.0.0",
  "id": "demo-county-population-mini",
  "title": "Demo: County population (toy data)",
  "summary": "Mock chart for UI layout testing",
  "chart_type": "bar",
  "context": ["docs"],

  "data": {
    "kind": "file",
    "ref": "../charts/demo-county-population-mini/data.csv",
    "format": "csv",
    "shape": "wide"
  },

  "encoding": {
    "x": { "field": "county", "type": "nominal" },
    "y": { "field": "population", "type": "quantitative" }
  },

  "units": { "population": "people" },

  "accessibility": {
    "alt": "Bar chart comparing population across three demo counties.",
    "long_description": "Toy dataset for layout only; not used for analysis."
  },

  "provenance": {
    "sources": [],
    "license": "CC0-1.0",
    "attribution": "KFM demo asset"
  },

  "sensitivity": { "classification": "public" }
}
```
