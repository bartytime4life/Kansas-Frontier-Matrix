# 📊 Chart Sources (Raw) — `web/assets/media/charts/raw/source/`

![KFM](https://img.shields.io/badge/KFM-living_atlas-2ea44f)
![Evidence-first](https://img.shields.io/badge/evidence-first-blue)
![Deterministic](https://img.shields.io/badge/pipeline-deterministic-orange)
![API%20Boundary](https://img.shields.io/badge/UI-via_governed_API-critical)

> **Purpose:** Keep **reproducible chart “recipes”** (specs + scripts + *tiny* fixtures) that can generate chart media consistently — without sneaking governed data into the UI layer.

---

## 🧾 Policy Metadata

| Field | Value |
|---|---|
| **File** | `web/assets/media/charts/raw/source/README.md` |
| **Status** | ✅ Active |
| **Last updated** | 2026-01-18 |
| **Scope** | Source assets for charts (specs/scripts/fixtures), used at build-time or for design/test |
| **Primary principle** | **Evidence-first + API-boundary**: UI doesn’t ship hidden datasets; governed artifacts flow through catalogs → API → UI |
| **Canonical references** | Master Guide v13 (pipeline invariants), KFM Technical Docs (web app structure) |

---

## 🧭 Where this folder sits (context)

KFM’s frontend lives under `web/` and includes reusable UI components (including **charts**) and an `assets/` area for static media. This directory is one small piece of that frontend surface. [^kfm-web]

At the same time, KFM’s **non‑negotiable pipeline** is:

> **ETL → STAC/DCAT/PROV catalogs → Graph → API → UI → Story Nodes → Focus Mode** [^kfm-pipeline]

So: this folder is **not** a shortcut around catalogs/provenance/API governance. It’s for **presentation-layer sources**, not for smuggling “data products” into production UI bundles. [^kfm-invariants] [^kfm-ui-no-hidden-data]

---

## ✅ Golden Rules

> [!IMPORTANT]
> If your chart communicates **governed evidence** (not just decoration), treat it like an **evidence artifact**: store in `data/processed`, register STAC/DCAT, trace in PROV, and expose it via the governed API — **do not hardcode/ship it from the UI**. [^kfm-evidence-artifacts]

### 1) 🚫 No hidden datasets in the UI
- The UI **must not contain hidden data files** that become the “real source of truth.” The frontend consumes what the API returns. [^kfm-ui-no-hidden-data]

### 2) 🧬 Provenance-first, always
- Anything promoted beyond “local dev/test asset” needs **traceable lineage**: STAC/DCAT/PROV exists *before* it’s referenced in UI/narratives. [^kfm-boundary-artifacts] [^kfm-invariants]

### 3) 🔁 Deterministic builds
- Charts should be reproducible: same inputs ⇒ same outputs (idempotent, config-driven, logged). [^kfm-invariants]

### 4) 🔒 Classification propagation
- **No output is less restricted than its inputs.** If an input is restricted/sensitive, it does *not* belong in web-shipped assets unless explicitly redacted/approved. [^kfm-invariants]

### 5) 🧩 Separate “source” vs “rendered”
- `raw/source/` is for **inputs/specs/scripts**.
- Rendered outputs belong in a **rendered/dist sibling directory** (and/or in governed data storage if evidence-grade).

---

## 🗂️ Suggested layout (per chart package)

> [!NOTE]
> This is a *recommended* convention for clarity + governance. If the repo already has a chart manifest convention, follow that.

```text
📦 web/assets/media/charts/
└─ 🧪 raw/
   ├─ 🧾 source/                     👈 you are here
   │  ├─ kfm__<domain>__<chart-slug>/
   │  │  ├─ chart.yaml               # manifest + metadata (required)
   │  │  ├─ spec/                    # vega-lite / echarts / d3 configs (recommended)
   │  │  │  └─ chart.vl.json
   │  │  ├─ inputs/                  # tiny fixtures ONLY (optional)
   │  │  │  └─ sample.csv
   │  │  ├─ render/                  # scripts to build outputs (recommended)
   │  │  │  └─ render.ts
   │  │  ├─ prov/                    # provenance pointers (recommended)
   │  │  │  └─ prov.jsonld
   │  │  └─ README.md                # per-chart notes (optional but helpful)
   │  └─ _shared/                    # shared themes/fonts/helpers (optional)
   └─ 🖼️ rendered/                   # generated outputs (SVG/PNG) (recommended)
```

---

## 📦 Minimum “Chart Package” contract

### Required
- **`chart.yaml`** (or `chart.json`) manifest with:
  - chart identity + title
  - intended use (decorative vs evidence-grade)
  - source-of-truth pointers (dataset IDs / API endpoints / STAC/DCAT refs)
  - license + attribution
  - classification (public/internal/restricted) + propagation notes
  - build/render instructions (or links)

### Recommended
- **`spec/`** containing a machine-readable chart spec (e.g., Vega-Lite)
- **`render/`** script or documented command
- **`prov/`** with PROV JSON-LD pointer/bundle if the chart is promoted beyond a dev fixture [^kfm-evidence-artifacts]
- **`README.md`** per chart with assumptions + notes

---

## 🧾 Example `chart.yaml` (manifest)

```yaml
chart_id: kfm.weather.station_recent_readings
title: "Recent Weather Station Readings"
description: "UI preview chart for the weather-station popup (7-day window)."

intent:
  tier: "ui-preview"     # ui-preview | decorative | evidence-grade
  shipped_to_prod: false # if true, confirm governance + approvals

source_of_truth:
  # Prefer API / catalog references (not inline data files)
  api_endpoint: "/api/weather/stations/{station_id}/timeseries?range=P7D"
  datasets:
    - stac_item_id: "stac://kfm/.../weather_stations_timeseries"
    - dcat_dataset_id: "dcat://kfm/.../weather-stations"

governance:
  classification: "public"
  propagation_note: "No restricted inputs; safe for public UI preview assets."

license:
  spdx: "CC-BY-4.0"
  attribution: "KFM + upstream provider (see dataset metadata)"

render:
  engine: "vega-lite"
  spec_path: "./spec/chart.vl.json"
  output_targets:
    - "../../rendered/kfm.weather.station_recent_readings.svg"
  deterministic:
    timezone: "UTC"
    locale: "en-US"
    rounding: 2
    sort: "stable"
```

---

## 🧬 Provenance & Catalog alignment

If a chart crosses the line from “UI fixture” → “published evidence,” it must follow the **catalog + PROV path**:

- **STAC / DCAT / PROV are boundary artifacts** produced before something is “fully published” downstream. [^kfm-boundary-artifacts]
- Evidence artifacts must be stored under **`data/processed/...`**, cataloged, and traced in PROV. [^kfm-evidence-artifacts]
- Anything accessible in the UI should be served via the **governed API** so redaction/classification rules can be enforced. [^kfm-evidence-artifacts]

---

## 🎨 Output guidance: prefer SVG for charts

When shipping static charts, prefer **SVG** where practical:
- more resolution-independent
- often smaller than bitmap formats
- well-suited to charts/line art [^svg]

---

## 🛠️ Adding a new chart source (workflow)

1) **Decide the intent**
- `ui-preview` (storybook/visual regression)
- `decorative` (branding/illustrative, not evidence)
- `evidence-grade` (must route through catalogs + API)

2) **Create a chart package folder**
- `kfm__<domain>__<chart-slug>/` (kebab-case slug)

3) **Write `chart.yaml`**
- Include *explicit* API/catalog pointers (avoid committing “truth data” into `web/`).

4) **Add spec + render script**
- Keep rendering deterministic (timezone/locale/rounding/sort).

5) **If evidence-grade: publish properly**
- Put the artifact in `data/processed/...`
- Create STAC/DCAT entries + PROV lineage bundle [^kfm-boundary-artifacts] [^kfm-evidence-artifacts]

6) **Wire into UI via API**
- UI consumes governed endpoints; no direct “secret” data files. [^kfm-ui-no-hidden-data]

---

## ✅ PR Checklist (quick)

- [ ] `chart.yaml` exists and is complete (intent, attribution, classification)
- [ ] No restricted/sensitive data committed under `web/assets/...` [^kfm-invariants]
- [ ] Rendering is deterministic (timezone/locale/rounding stable) [^kfm-invariants]
- [ ] If evidence-grade: STAC/DCAT/PROV are created and linked [^kfm-boundary-artifacts]
- [ ] UI usage (if any) flows through API boundary [^kfm-invariants]

---

## 📚 References (project-grounded)

[^kfm-web]: KFM technical documentation describes `web/` as the React frontend (components include charts/map overlays) and `assets/` as static assets like icons/images.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^kfm-pipeline]: Master Guide v13 defines KFM’s canonical pipeline ordering (ETL → catalogs → graph → API → UI → narratives).  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^kfm-invariants]: Master Guide v13 lists invariants: absolute pipeline ordering, API boundary, provenance-first, deterministic ETL, and classification propagation.  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^kfm-ui-no-hidden-data]: Master Guide v13: UI should not contain hidden data files; it relies on the API.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^kfm-boundary-artifacts]: Master Guide v13: STAC/DCAT/PROV “boundary artifacts” are required before data is considered published and consumed downstream.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^kfm-evidence-artifacts]: Master Guide v13: evidence artifacts must be stored in `data/processed`, cataloged (STAC/DCAT), traced in PROV, and exposed via governed APIs (no hard-coding in UI).  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^svg]: Responsive web design reference: SVG provides resolution independence and can be smaller than raster formats; suitable for charts.  [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
