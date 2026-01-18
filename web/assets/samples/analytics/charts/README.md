<!-- 📍 Path: web/assets/samples/analytics/charts/README.md -->

# 📊 Analytics Charts Samples (KFM)

A small, practical sandbox of chart examples for the **KFM web UI** (dashboards, map-adjacent analytics, and evidence-facing UI widgets). These samples exist to help us ship *consistent*, *traceable*, and *re-usable* visuals—without breaking KFM’s “evidence-first / provenance-first” rules. 🧾✅

> 🧭 KFM reminder: the UI is downstream of the canonical pipeline and must only visualize **governed outputs** (cataloged + provenance-backed, delivered through the API boundary). [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🏷️ Quick “badge” facts

| 🧪 Status | 🎯 Purpose | 🔒 Data Access | 🧾 Provenance |
|---|---|---|---|
| Sample assets | UI patterns + dev reference | **API-only** (no graph direct) | Required for anything “real” |

---

## 🎯 What this folder is for

Use these samples to:

- Prototype chart layouts fast (axes, legends, tooltips, brushing, etc.) ✨  
- Establish **a consistent “Chart Contract”** (inputs/outputs + metadata) across the UI 🧩  
- Ensure every chart can be tied back to governed datasets (STAC/DCAT) and lineage (PROV) 🧾  
- Provide “copy/paste starters” for Story Nodes / Focus Mode visuals—**without** sneaking in unsourced claims 🧠📌 [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

KFM is designed so that **every narrative claim** (and by extension, every analytic annotation) can be traced back to versioned evidence. [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Suggested folder structure

> If your current sample set differs, treat this as the target shape and adjust incrementally.

```text
📁 web/
  📁 assets/
    📁 samples/
      📁 analytics/
        📁 charts/
          📄 README.md  👈 you are here
          📁 _shared/
            📄 chart-contract.schema.json
            📄 theme.css
            📄 sample-utils.js
          📁 line-timeseries/
            📄 index.html
            📄 chart.spec.json
            📄 data.sample.json
          📁 bars-stacked/
            📄 index.html
            📄 chart.spec.json
            📄 data.sample.json
          📁 scatter-brush/
            📄 index.html
            📄 chart.spec.json
            📄 data.sample.json
          📁 heatmap/
            📄 index.html
            📄 chart.spec.json
            📄 data.sample.json
          📁 _images/
            📄 thumbnails.md
            🖼️ line-timeseries.png
            🖼️ scatter-brush.png
```

---

## 🔒 Non‑negotiables (KFM rules that apply to charts)

### 1) Pipeline ordering is absolute
Charts are *UI output*, and must not “invent” data upstream. KFM’s pipeline ordering is inviolable (ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode). [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) API boundary rule
The UI **must never query Neo4j directly**. All chart data must come through the governed API layer (or offline sample JSON that represents an API response shape). [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) Provenance-first visualization
No dataset (and no derived “evidence artifact”) should appear in charts unless it has:
- Catalog metadata (STAC/DCAT where appropriate), and  
- A PROV lineage record  
as prerequisites to graph/UI use. [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 4) Evidence artifacts are first-class
If a chart uses computed results (aggregation, model output, NLP extraction, etc.), those outputs must be treated as first-class datasets: stored as processed outputs, cataloged, and traced in PROV—**and exposed via governed APIs** (not hard-coded into the UI). [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🌐 How charts should receive data

KFM’s web UI is intended to be usable via standard web tech in a browser, and the repo design emphasizes open libraries and public data sources (no proprietary services required). [oai_citation:10‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

The `web/` folder is described as the home for the front-end viewer (index.html, JS/CSS, and precomputed JSON as needed). [oai_citation:11‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

### Recommended flow (UI perspective)

```mermaid
flowchart LR
  A[📦 ETL Outputs] --> B[🗂️ STAC / DCAT / PROV]
  B --> C[🧠 Graph (Neo4j)]
  C --> D[🔒 Governed APIs]
  D --> E[🌐 UI Chart Components]
  E --> F[🧾 Story Nodes / Focus Mode]
```

- Our samples should mimic **API response shapes** and include enough metadata to support traceability.
- If a sample chart is fed from local JSON, treat it as a **fixture** (not a “real dataset”) unless it’s cataloged.

---

## 📐 Chart Contract (recommended)

We want every chart to be portable and testable. A simple contract makes samples reusable across dashboard widgets and story visuals.

### ✅ Minimum `chart.spec.json` fields

```json
{
  "id": "line-timeseries__ingest_volume",
  "title": "Ingest Volume Over Time",
  "description": "Example time series showing a metric across a timeline.",
  "data": {
    "source": "api",
    "endpoint": "/api/analytics/metrics/time-series",
    "params": { "metric": "ingest_volume", "grain": "year" }
  },
  "encoding": {
    "x": { "field": "year", "type": "temporal" },
    "y": { "field": "value", "type": "quantitative", "unit": "items" }
  },
  "provenance": {
    "dcat_dataset_id": "dcat:…",
    "stac_item_id": "stac:…",
    "prov_activity_id": "prov:…",
    "notes": "IDs must resolve to governed metadata when this becomes a real chart."
  },
  "accessibility": {
    "ariaLabel": "Line chart of ingest volume by year",
    "tableFallback": true
  }
}
```

> 📌 Why: KFM treats analytics + derived artifacts as governed evidence, requiring lineage and careful API exposure. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Sample data guidelines

### ✅ Allowed
- Small synthetic fixtures (clearly labeled as synthetic)
- Public domain / public datasets with attribution
- Snippets derived from governed outputs (when they’re already cataloged)

### 🚫 Not allowed
- Sensitive data
- “Mystery JSON” with no source story
- Any analytics output used in UI without a provenance plan

KFM’s documentation standards emphasize that data work should be documented with pipeline details and recorded EDA; visualization outputs should include context and data source. (These rules apply even when we “just add a chart”.) [oai_citation:13‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🛠️ Adding a new chart sample (checklist)

Create a new folder: `📁 <chart-name>/` and include:

- [ ] `index.html` (or equivalent demo entry)  
- [ ] `chart.spec.json` (contract)  
- [ ] `data.sample.json` (fixture)  
- [ ] `README.md` (1–2 paragraphs: intent + how to run + caveats)  
- [ ] Thumbnail in `/_images/` (optional but encouraged) 🖼️  

**Design checklist**
- [ ] Clear title + caption-like description (what does it show and why?) [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Axes labeled with units when quantitative
- [ ] Tooltips don’t imply claims without evidence links
- [ ] If any derived metric: note the transform and planned PROV activity pointer [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ♿ Accessibility baseline

Make charts usable in KFM’s “public browser” context:

- Provide an ARIA label and readable title
- Ensure keyboard focus targets for legends/toggles
- Add a **table fallback** or “download data” in future UI wiring
- Avoid encoding meaning *only* via color (use shapes/labels/patterns where feasible)

---

## 🚀 Performance notes (pragmatic)

- Keep fixtures tiny (prefer ≤ 50–200 points for demos)
- If the “real” version will be large, plan:
  - server-side aggregation via API
  - binning / downsampling
  - incremental rendering for time sliders / brushing

---

## 🔁 Reproducibility & build philosophy

Project design favors reproducible environments, versioned data relationships, and CI checks (e.g., validating catalogs, ensuring expected outputs). Consider adding lightweight validations for chart fixtures/specs over time. [oai_citation:16‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

For large data artifacts (outside this folder), the project design includes using DVC to avoid bloating Git while tracking code↔data version relationships. [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 📚 Governing references (why these rules exist)

- **KFM pipeline ordering + evidence-first design** [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **API boundary (UI must not query Neo4j directly)** [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Evidence artifacts are first-class (catalog + PROV + API exposure)** [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Data science & visualization documentation expectations** (EDA recorded, pipeline documented, charts explained with sources) [oai_citation:22‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- **Web UI philosophy (browser-first, open libraries, static web folder)** [oai_citation:23‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA) [oai_citation:24‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## ✅ Next “good” upgrades (when convenient)

<details>
<summary>📌 Click to expand</summary>

- Add `chart-contract.schema.json` and validate `chart.spec.json` in CI  
- Add a tiny `index.json` registry of samples for a gallery view  
- Generate thumbnails automatically (or maintain a curated set in `_images/`)  
- Add a “provenance widget” stub (shows dataset IDs and links once wired)  
- Add a `CONTRIBUTING` note for chart samples (naming, metadata, accessibility checks)

</details>
