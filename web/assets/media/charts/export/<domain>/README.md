---
title: "📊 Chart Exports — <domain>"
path: "web/assets/media/charts/export/<domain>/README.md"
version: "v0.1.0"
status: "draft"
doc_kind: "Asset README"
last_updated: "2026-01-18"
license: "TBD"

# Governance / ethics (align with KFM)
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"
---

# 📊 Chart Exports — `<domain>`

![contract-first](https://img.shields.io/badge/contract--first-✅-informational)
![provenance-first](https://img.shields.io/badge/provenance--first-✅-informational)
![svg-preferred](https://img.shields.io/badge/format-SVG%20preferred-blue)
![no-mystery-assets](https://img.shields.io/badge/policy-no%20mystery%20assets-critical)

> **What this is:** UI-friendly, versioned **export artifacts** (SVG/PNG + metadata) for the `<domain>` domain.  
> **What this is NOT:** a place to stash “random charts” without sources, lineage, or licensing.

---

## 🧭 Quick navigation

- [🎯 Purpose](#-purpose)
- [🗂️ Folder layout](#️-folder-layout)
- [🧾 Chart Export Contract](#-chart-export-contract)
- [🔗 Provenance rules](#-provenance-rules)
- [🖼️ Formats](#️-formats)
- [♿ Accessibility](#-accessibility)
- [✅ Definition of Done](#-definition-of-done)
- [🧩 How the web app uses these](#-how-the-web-app-uses-these)
- [📚 Related KFM docs](#-related-kfm-docs)

---

## 🎯 Purpose

This directory holds **static exports** of charts used by the web UI and documentation surfaces (e.g., story panels, popups, summaries, thumbnails). The goal is to keep chart media:

- **Fast to load** (static assets, cacheable)
- **Reproducible** (derived from deterministic pipelines)
- **Traceable** (every chart has source + license + lineage references)
- **Auditable** (no surprises in what we show to users)

> 🧠 Rule of thumb: if a chart can’t explain *where its data came from*, it doesn’t belong here.

---

## 🗂️ Folder layout

Recommended structure (one folder per chart export):

```text
web/assets/media/charts/export/<domain>/
├── README.md
├── manifest.json                        # optional, domain-level index (recommended)
└── <chart_id>/                          # kebab-case stable chart id (ex: "water-station-trend")
    ├── chart.svg                        # ✅ preferred
    ├── chart.png                        # optional raster fallback
    ├── thumb.png                        # optional for grids/cards
    ├── chart.meta.json                  # ✅ REQUIRED (contract + provenance pointers)
    ├── chart.spec.json                  # optional (vega/plotly/etc spec snapshot)
    └── chart.data.sample.csv            # optional (small sample only; never sensitive)
```

### ✅ Naming rules

- `<domain>`: kebab-case, matches the **data domain** name (ex: `air-quality`, `land-treaties`, `soils-sda`).
- `<chart_id>`: kebab-case, **stable** identifier (do not bake dates into the ID).
- If you need variants, keep the ID stable and suffix the file name:
  - `chart.dark.svg`, `chart.light.svg`
  - `chart.sm.png`, `chart.lg.png`

---

## 🧾 Chart Export Contract

Every chart folder **must** include `chart.meta.json`. This is the “mini-contract” that makes the asset governable.

### Minimal required fields

```json
{
  "id": "water-station-trend",
  "domain": "<domain>",
  "title": "Station readings over time",
  "description": "Short explanation of what the chart shows (1–2 sentences).",

  "created_at": "2026-01-18",
  "created_by": ["TBD"],

  "formats": {
    "svg": "chart.svg",
    "png": "chart.png"
  },

  "sources": {
    "stac": ["urn:kfm:stac:collection:..."],
    "dcat": ["urn:kfm:dcat:dataset:..."],
    "prov": ["urn:kfm:prov:bundle:..."]
  },

  "license": {
    "spdx": "TBD",
    "attribution": "TBD"
  },

  "accessibility": {
    "alt": "Alt text describing the key takeaway of the chart."
  }
}
```

### Strongly recommended fields (make it *actually* reproducible)

Add these when you can:

- `time_extent`, `spatial_extent`
- `units`, `stat_method`, `aggregation`
- `parameters` (anything that changes the output: smoothing, bin size, filters)
- `generator` (script path + commit SHA or pipeline run ID)
- `checksums` (sha256 for exported files)

<details>
  <summary>📦 Extended <code>chart.meta.json</code> template</summary>

```json
{
  "id": "water-station-trend",
  "domain": "<domain>",
  "version": "v1",
  "title": "Station readings over time",
  "description": "Shows monthly mean readings with a rolling average overlay.",

  "created_at": "2026-01-18",
  "updated_at": "2026-01-18",
  "created_by": ["<name-or-team>"],

  "chart_type": "line",
  "dimensions": { "width": 1200, "height": 675, "dpi": 144 },

  "time_extent": { "start": "1950-01-01", "end": "2025-12-31" },
  "spatial_extent": { "type": "bbox", "bbox": [-102.05, 36.99, -94.60, 40.00] },

  "metrics": [
    { "name": "reading_value", "unit": "TBD", "aggregation": "monthly_mean" }
  ],

  "formats": {
    "svg": "chart.svg",
    "png": "chart.png",
    "thumb": "thumb.png"
  },

  "sources": {
    "stac": ["urn:kfm:stac:collection:<...>", "urn:kfm:stac:item:<...>"],
    "dcat": ["urn:kfm:dcat:dataset:<...>"],
    "prov": ["urn:kfm:prov:bundle:<...>"],
    "notes": [
      "All sources must be cataloged; no ad-hoc spreadsheets or screenshots."
    ]
  },

  "generator": {
    "pipeline": "src/pipelines/<domain>/",
    "script": "TBD",
    "commit_sha": "TBD",
    "run_id": "TBD",
    "parameters": { "rolling_window_days": 30 }
  },

  "license": {
    "spdx": "TBD",
    "attribution": "TBD",
    "third_party_assets": [
      { "name": "TBD", "license": "TBD", "notes": "TBD" }
    ]
  },

  "accessibility": {
    "alt": "Monthly station readings trend upward after 2000 with seasonal peaks.",
    "notes": "Avoid red/green-only distinctions; ensure contrast on light/dark."
  },

  "checksums": {
    "chart.svg": "sha256:TBD",
    "chart.png": "sha256:TBD"
  }
}
```

</details>

---

## 🔗 Provenance rules

This directory follows KFM’s evidence-first and provenance-first guardrails:

1. **No “mystery exports.”**  
   If you can’t point to cataloged sources + lineage, don’t add the chart.

2. **Do not bypass the pipeline.**  
   Canonical data lives in governed outputs (ETL → catalogs → graph → API).  
   This folder only stores **rendered media** derived from those outputs.

3. **Charts are evidence artifacts.**  
   Treat them like published results: version, methods, parameters, and provenance must be explicit.

4. **Sensitive data must be handled carefully.**  
   If there’s any chance a chart reveals sensitive location or personal info, aggregate/redact and document the decision in `chart.meta.json`.

---

## 🖼️ Formats

### ✅ SVG (preferred)

Use SVG whenever possible:

- stays sharp at any zoom level (great for charts and linework)
- usually smaller than bitmap images for the same visual complexity
- can be optimized/minified

### 🧷 PNG (fallback)

Provide PNG when:

- the SVG would be too heavy
- the chart includes raster imagery (satellite basemaps, etc.)
- you need a stable fallback for environments that don’t render SVG well

Recommended conventions:

- `chart.png` at 2× baseline resolution (so it looks crisp on high-DPI screens)
- keep `thumb.png` small (for list/grid views)

### 📎 Specs + data samples

If you include a spec or data:

- `chart.spec.json`: chart grammar snapshot (Vega, Plotly JSON, etc.)
- `chart.data.sample.csv`: **small sample only** (never dump large or sensitive data in web assets)

> ✅ The “truth” should remain in governed datasets and catalogs; samples here are just for debugging and UI previews.

---

## ♿ Accessibility

Every chart export must support accessibility:

- Provide meaningful `accessibility.alt` in `chart.meta.json`
- Avoid color-only encodings (use labels, dashes, markers)
- Ensure readable font sizes at typical embedding widths
- Prefer “takeaway-first” alt text (what the chart *means*, not just what it *contains*)

---

## ✅ Definition of Done

Use this checklist before committing chart exports:

- [ ] Chart folder uses **kebab-case** and stable `<chart_id>`
- [ ] `chart.meta.json` exists and includes:
  - [ ] `sources.{stac,dcat,prov}` pointers
  - [ ] `license` + attribution
  - [ ] `accessibility.alt`
- [ ] SVG is present **or** a documented reason why only PNG exists
- [ ] No sensitive data is exposed (or redaction/aggregation is documented)
- [ ] File sizes are reasonable (optimized; no “accidental megabytes”)
- [ ] If used by the UI, `manifest.json` updated (if applicable)

---

## 🧩 How the web app uses these

This folder is under the front-end `web/` static assets area. Typical uses include:

- chart thumbnails in catalog cards
- inline images in story narratives
- popup/side-panel charts when a user clicks a feature (station, county, event, etc.)
- “known-good” snapshots for offline docs and reviews

### 🧬 Pipeline placement (mental model)

```mermaid
flowchart LR
  A[data/processed + STAC/DCAT/PROV] --> B[src/server APIs]
  B --> C[web/ React UI]
  A --> D[chart generator (deterministic)]
  D --> E[web/assets/media/charts/export/<domain>]
  E --> C
```

---

## 📚 Related KFM docs

- `docs/standards/` — STAC/DCAT/PROV profiles and governance policies
- `docs/templates/` — document + story node templates
- `docs/reports/story_nodes/` — narrative content that may embed these exports
- `src/pipelines/` — deterministic transformations that should generate reproducible outputs
- `web/` — React UI codebase (charts, overlays, story UI)

---

## 🧷 Optional: domain manifest

If the UI needs a simple index, add `manifest.json`:

```json
{
  "domain": "<domain>",
  "charts": [
    { "id": "water-station-trend", "path": "water-station-trend/chart.meta.json" },
    { "id": "county-summary-bars", "path": "county-summary-bars/chart.meta.json" }
  ]
}
```

> Keep it boring and predictable — a manifest should be easy to diff and review ✅
