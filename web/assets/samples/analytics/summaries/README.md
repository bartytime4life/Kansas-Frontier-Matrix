# 📊 Analytics Summary Samples (Web UI Fixtures)

![KFM](https://img.shields.io/badge/KFM-Analytics-2b6cb0) ![Samples](https://img.shields.io/badge/assets-samples-555) ![Format](https://img.shields.io/badge/format-JSON-f39c12) ![Provenance](https://img.shields.io/badge/provenance-first-2ecc71) ![UI](https://img.shields.io/badge/target-Web%20UI-9cf)

> **Purpose:** This folder contains **small, static “analytics summary” fixtures** used by the **Web UI** for demos, local/offline development, and repeatable UI testing 🧪  
> In production, summaries should come from the governed API—these files are intentionally lightweight and *front-end friendly*.

---

## 📍 You are here

```text
web/
  assets/
    samples/
      analytics/
        summaries/   👈 you are here
```

---

## 🧠 How summaries fit the KFM architecture

KFM treats analytics as **interpretability glue**: turning query results into **quick stats + chart-ready series** so users can understand a layer without exporting data.

**Rule of thumb:** summaries are *UI-ready artifacts* that should reflect the platform’s contract-first + provenance-first approach.

```mermaid
flowchart LR
  ETL[ETL Pipelines ⚙️] --> CAT[Catalogs (STAC/DCAT/PROV) 🗂️]
  CAT --> GRAPH[Knowledge Graph (Neo4j) 🧠]
  GRAPH --> API[Governed API (src/server) 🔌]
  API --> UI[Web UI 🌐]
  UI --> STORY[Story Nodes 🧾]
  STORY --> FOCUS[Focus Mode AI 🎯]
```

✅ **These sample JSON files live on the “UI side”** (static assets) and are meant to **mimic** what the governed API would return for analytics endpoints.

---

## ✅ What an “analytics summary” is

A summary is a compact JSON document that answers:

- **What was summarized?** (dataset + scope: place/time + filters) 🗺️🕰️  
- **What are the headline stats?** (min/max/mean/count, etc.) 📈  
- **What can the UI chart instantly?** (small time series / categories) 📉  
- **Where did it come from?** (catalog/provenance pointers) 🧾  
- **Is it safe to display?** (classification + redaction notes) 🔒

---

## 🧾 Summary contract (recommended)

These samples are not “raw data.” They are **presentation-friendly** outputs. Keep them:

- **small** (fast to fetch + render)
- **deterministic** (same inputs → same outputs)
- **traceable** (include provenance pointers)
- **safe** (no secrets, no sensitive data)

<details>
<summary><strong>📦 Minimal contract (JSON) — recommended fields</strong></summary>

```json
{
  "schemaVersion": "1.0",
  "id": "rainfall--county--johnson--1895-2020",
  "title": "Rainfall Summary — Johnson County (1895–2020)",
  "description": "Quick statistics and a chart-ready annual series for rainfall in Johnson County.",
  "isSample": true,

  "scope": {
    "place": {
      "type": "county",
      "name": "Johnson County, KS",
      "geoId": "kfm:place:us-ks-county-johnson"
    },
    "time": {
      "start": "1895-01-01",
      "end": "2020-12-31",
      "resolution": "year"
    },
    "filters": [
      { "field": "measure", "op": "=", "value": "rainfall" }
    ]
  },

  "dataset": {
    "catalogId": "kfm:dataset:climate-rainfall-stations",
    "label": "Rainfall (Stations)",
    "license": "see catalog",
    "source": "see catalog"
  },

  "metrics": {
    "count": 126,
    "min": 18.2,
    "max": 62.9,
    "mean": 38.7,
    "units": "in/yr"
  },

  "series": {
    "annual": [
      { "t": "1895", "v": 31.2 },
      { "t": "1896", "v": 28.9 }
    ]
  },

  "charts": [
    {
      "type": "line",
      "title": "Annual Rainfall",
      "x": { "field": "t", "label": "Year" },
      "y": { "field": "v", "label": "Rainfall (in/yr)" }
    }
  ],

  "provenance": {
    "stac": "kfm:stac:collection:climate-rainfall",
    "prov": "kfm:prov:run:2026-01-18T01-35-00Z",
    "inputs": [
      "kfm:source:example-manifest-or-station-feed"
    ],
    "notes": [
      "Summary values are derived from cataloged processed datasets. See dataset catalog entry for authoritative details."
    ]
  },

  "classification": {
    "level": "public",
    "redactionsApplied": false
  },

  "generatedAt": "2026-01-18T01:35:00Z"
}
```
</details>

### 🧩 Field tips (UI-friendly)

- Use **ISO-8601** timestamps where possible (`generatedAt`, scope time bounds).
- Prefer **stable IDs** for graph/cat references (e.g., `kfm:dataset:*`, `kfm:place:*`) 🔗
- Keep numeric values as numbers (not strings), and include **units** explicitly.
- If a summary is **synthetic** (for demos), mark it clearly (`isSample: true`) ✅

---

## 🏷️ File naming conventions (recommended)

Use consistent, grep-friendly names:

```text
<domain>--<metric>--<region>--<time-range>.summary.json
```

Examples:
- `climate--rainfall--johnson-county--1895-2020.summary.json`
- `hazards--tornadoes--kansas--1950-2024.summary.json`
- `agriculture--crop-yield--statewide--1990-2022.summary.json`

---

## ➕ Adding a new summary (checklist)

- [ ] Keep the file **small** (prefer summaries over raw arrays; truncate series if needed) 🪶  
- [ ] Include `schemaVersion`, `id`, and a **clear title** 🏷️  
- [ ] Include `dataset.catalogId` and provenance pointers (`provenance.stac` / `provenance.prov`) 🧾  
- [ ] Include `classification.level` (`public` by default for anything shipped in `web/assets/`) 🔒  
- [ ] Prefer chart-ready data (small `series`) + headline stats (`metrics`) 📈  
- [ ] If you reference people/places/events, use **stable graph IDs** (not just names) 🔗  
- [ ] Never include credentials, tokens, private URLs, or sensitive coordinates 🚫

---

## 🔒 Safety + governance notes

Because these files ship to the browser:

- ✅ Treat everything here as **public** by default.
- 🚫 Do **not** include secrets, API keys, private endpoints, or non-public datasets.
- 🧭 If a source is restricted, **do not** create a public sample that “leaks” detail; use redactions/generalization.

---

## 🔗 Related docs (recommended reading)

- `../../../../../docs/MASTER_GUIDE_v13.md` 📘  
- `../../../../../docs/data/contracts/examples/README.md` 🧾  
- `../../../../../README.md` 🏠  
- (If present) API contracts & schema validators under `src/server/` 🔌

---

## 🧼 Philosophy (why we’re strict here)

KFM’s core promise is that anything shown in the UI (and anything used for AI features) should be **traceable, reproducible, and governed**. These samples should reinforce that mindset—even when they’re “just fixtures.” ✅
