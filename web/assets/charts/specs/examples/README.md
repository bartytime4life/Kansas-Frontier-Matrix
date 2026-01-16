---
title: "KFM Web UI — Chart Spec Examples 📊"
path: "web/assets/charts/specs/examples/README.md"
version: "v0.1.0"
status: "draft"
last_updated: "2026-01-16"
doc_kind: "README"
license: "CC-BY-4.0"
owner: "web-ui"
tags: ["charts", "specs", "examples", "provenance-first", "contract-first"]
doc_uuid: "urn:kfm:doc:web:charts:specs:examples:v0.1.0"
---

# 📊 Chart Spec Examples

![Status](https://img.shields.io/badge/status-draft-yellow)
![Scope](https://img.shields.io/badge/scope-web%20ui-blue)
![Principle](https://img.shields.io/badge/contract--first-yes-success)
![Principle](https://img.shields.io/badge/provenance--first-yes-success)

> 🎯 **Purpose:** This folder holds **example chart specs** that demonstrate how KFM charts should be authored: **declarative**, **reproducible**, **API-governed**, and **provenance-linked**.

---

## 📦 What lives here?

These example specs are meant to be used as:

- ✅ Reference patterns for building **pop-up mini-graphs** (sparklines), **details-sidebars**, and **Story/Focus** visuals  
- ✅ Regression fixtures for chart rendering (when we add/maintain a chart renderer + CI validation)  
- ✅ A “known good” cookbook of chart patterns (line, bar, histogram, etc.)

---

## 🗂️ Folder context

```text
web/
└─ 📁 assets/
   └─ 📈 charts/
      └─ 🧪📐 specs/
         └─ 🧪 examples/
            ├─ 📄 README.md             # 👈 you are here 📌
            ├─ 🧾 *.json                # (example chart specs)
            ├─ 📝 *.md                  # (optional: narrative notes per example)
            ├─ 🧩 data/                 # (optional: tiny fixture datasets, if used)
            └─ 🖼️ *.png                 # (optional: golden screenshots for review/CI)
```

---

## 🧭 KFM chart rules (non-negotiables)

### 1) 🔌 API boundary (no direct graph access)
Chart specs **must assume data comes from the governed API layer** (REST/GraphQL), not from direct database/graph calls inside the UI.

> 🧱 If a chart needs something “clever,” that logic belongs upstream (ETL/API), not as ad-hoc UI scraping.

### 2) 🧾 Provenance-first (charts must be explainable)
Every chart shown to users should be able to answer:
- **What dataset is this from?**
- **What transformations happened?**
- **What time/space subset is shown?**
- **Where can I click to verify?**

Practical implication: **specs should carry a `caption` + `citations` (or provenance pointers)**.

### 3) 🧠 Evidence-first narrative (no unsourced interpretation)
If an example includes narrative text (caption, annotations), it must stay **factual** and **sourced**.

### 4) 🔒 Classification + sovereignty propagate
Specs must never encourage leaking sensitive data (e.g., exact locations / identifying details).  
If a dataset is restricted, downstream visualizations must remain **equally or more restricted** (or redacted/aggregated).

### 5) ♿ Accessibility is a feature, not an afterthought
Examples must demonstrate:
- clear labels (axes, legend)
- keyboard-friendly interactions (where applicable)
- screen-reader text / ARIA labeling for chart containers
- captions that explain what the chart means in plain language

---

## 🗺️ How a chart spec fits in KFM (mental model)

```mermaid
flowchart LR
  A[📦 Cataloged Data<br/>STAC/DCAT/PROV] --> B[🔌 Governed API<br/>REST / GraphQL]
  B --> C[📊 Chart Spec<br/>(declarative)]
  C --> D[🖥️ Web UI Renderer<br/>Popup / Sidebar / Story]
  C --> E[🧾 Caption + Citations]
  E --> D
```

---

## 🧩 Recommended chart spec shape

We keep this intentionally **library-agnostic**. If the project uses Vega-Lite (or another engine), treat this as a thin wrapper around that engine’s spec.

### ✅ Minimum fields an example should include

- `meta` — title, id, version, tags
- `data` — how data is obtained (API query or inline fixture)
- `spec` — the chart definition (engine-specific or KFM-native)
- `caption` — user-facing summary
- `citations` — links/refs to datasets + provenance

---

## 🧪 Example spec template (copy/paste)

<details>
<summary><strong>📄 Template: <code>*.json</code> (click to expand)</strong></summary>

```json
{
  "$schema": "../schema/chart-spec.schema.json",
  "meta": {
    "id": "line__sparkline__example__v1",
    "title": "Example Sparkline (10-year trend)",
    "description": "Small time-series chart suitable for popups and compact panels.",
    "version": "v1",
    "tags": ["sparkline", "timeseries", "popup"],
    "owner": "web-ui"
  },

  "governance": {
    "classification": "open",
    "care_label": "Public",
    "notes": "If this chart is ever used with restricted datasets, add redaction rules and review triggers."
  },

  "data": {
    "mode": "api",
    "endpoint": "/api/v1/metrics/timeseries",
    "params": {
      "entity_type": "weather_station",
      "entity_id": "STATION_ID_HERE",
      "metric": "precip_in",
      "window": "P10Y",
      "interval": "P1Y"
    },
    "contract_ref": "docs/contracts/api/metrics_timeseries.v1.json",
    "expected_fields": [
      { "name": "t", "type": "date" },
      { "name": "value", "type": "number" }
    ]
  },

  "spec": {
    "engine": "vega-lite",
    "definition": {
      "mark": { "type": "line" },
      "encoding": {
        "x": { "field": "t", "type": "temporal", "title": "Year" },
        "y": { "field": "value", "type": "quantitative", "title": "Precipitation (in)" }
      }
    }
  },

  "a11y": {
    "ariaLabel": "Line chart showing precipitation trend over the last 10 years.",
    "longDescription": "Values are annual totals; hover or focus to inspect exact values."
  },

  "caption": "Annual precipitation totals for the last 10 years (station-level summary).",
  "citations": [
    {
      "label": "Dataset",
      "kind": "DCAT",
      "ref": "data/catalog/dcat/weather_precipitation.jsonld"
    },
    {
      "label": "Lineage",
      "kind": "PROV",
      "ref": "data/prov/weather_precipitation__prov.json"
    }
  ]
}
```
</details>

---

## 🏷️ Naming conventions

Keep filenames predictable so we can build an examples gallery later 👇

**Suggested pattern**

```text
<chartType>__<useCase>__<domain_or_dataset>__v<major>.json
```

**Examples**
- `line__sparkline__weather_station__v1.json`
- `bar__topn__county_population__v1.json`
- `hist__distribution__soil_ph__v1.json`

> 💡 Use `__v2` only when the example changes meaningfully (breaking behavior, different fields, new engine structure).

---

## 🧰 Example catalog (add as you go)

| ✅ | Example file | Pattern | Intended UI surface | Notes |
|---:|---|---|---|---|
| ⬜ | `line__sparkline__...__v1.json` | Line | Popup | compact; fast |
| ⬜ | `bar__topn__...__v1.json` | Bar | Details panel | sortable, labeled |
| ⬜ | `area__stacked__...__v1.json` | Stacked area | Story step | narrative-friendly |
| ⬜ | `hist__distribution__...__v1.json` | Histogram | Data QA | bins defined |
| ⬜ | `scatter__...__v1.json` | Scatter | Analysis | include trendline only if sourced |

---

## 🧭 Authoring guidelines (practical)

### ✅ Do
- ✅ Keep example data **small** (or use server-side aggregation)
- ✅ Prefer **deterministic** outputs (no randomness unless seeded and justified)
- ✅ Include a **caption + citations**
- ✅ Include `a11y` text fields
- ✅ Prefer **clear defaults**: axis titles, units, and time windows

### ❌ Don’t
- ❌ Hard-code secrets, tokens, internal hostnames
- ❌ Point examples at unstable/ephemeral endpoints without a fallback fixture
- ❌ Encode “interpretation” in text without citations (“X caused Y”)
- ❌ Load raw, high-volume data into the browser for simple charts

---

## 🔍 Validation checklist (Definition of Done ✅)

When adding a new example, make sure:

- [ ] Spec is valid JSON and follows the schema (if present)
- [ ] `meta.id`, filename, and version match (no drift)
- [ ] Data mode is clear: `api` or `inline`
- [ ] Includes `caption` + `citations` (or provenance refs)
- [ ] Includes `a11y` fields (at least `ariaLabel`)
- [ ] No sensitive details are exposed (classification respected)
- [ ] Renders legibly at small sizes (popup-friendly)
- [ ] (Optional) Add `*.png` screenshot for golden review

---

## 🧠 FAQ

### Why “spec files” instead of writing charts directly in code?
Because chart specs are **portable** and **reviewable**: they behave like UI contracts and can be audited like any other governed artifact.

### Why do we keep citations with charts?
KFM’s UI philosophy is to expose the **“map behind the map”**—users should always be able to trace visuals back to source datasets and lineage.

---

## 🧩 Next improvements (nice-to-have)
- 📌 Add `../schema/chart-spec.schema.json` (Ajv-valid JSON Schema)
- 🧪 Add a lightweight “Chart Gallery” dev page that loads everything in `examples/`
- 🖼️ Add screenshot-based regression tests for example specs
- 🧷 Add a `examples/index.json` registry for stable ordering + tags
