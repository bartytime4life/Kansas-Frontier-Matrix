# 📊 Analytics Samples — Comparisons  
`web/assets/samples/analytics/comparisons/`

![KFM v13](https://img.shields.io/badge/KFM-v13.0.0--draft-1f6feb)
![sample](https://img.shields.io/badge/sample-analytics%2Fcomparisons-8250df)
![governance](https://img.shields.io/badge/governance-provenance--first-2da44e)
![rule](https://img.shields.io/badge/rule-API%20boundary-critical)
![data](https://img.shields.io/badge/data-config--first%20%7C%20synthetic-lightgrey)

> [!IMPORTANT]  
> **These samples must not become a “side-channel” around KFM governance.**  
> In KFM v13, the pipeline ordering is strict (ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode) and the **frontend must not query the graph directly**—all access goes through the API layer.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🎯 What this folder is

A small library of **comparison “packs”** used by the **KFM web app (`web/`)** to demo, develop, and test analytics UI patterns like:

- side-by-side metric charts (A vs B)  
- delta / percent-change summaries  
- cohort comparisons (place vs place / time vs time / version vs version)  
- “evidence-aware” comparisons that keep provenance visible

The `web/` directory is the frontend home in the v13 repo layout.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ What belongs here (and what doesn’t)

### ✅ Good fits
- **Config-first** comparison manifests (what to compare, how to render, what to cite)
- **Preview images** (lightweight, non-sensitive)
- **Synthetic fixtures** *only when needed* for Storybook / offline UI tests (explicitly labeled)

### 🚫 Not allowed
- Any **authoritative dataset** or “real” production data embedded in the frontend  
- Anything that bypasses the governed API boundary (no direct graph access)  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Anything that violates sovereignty/classification propagation (outputs can’t be less restricted than inputs)  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!NOTE]  
> KFM’s UI contract expectations include things like **layer registry config**, **accessibility audits**, and **usage analytics hooks**—samples in this folder should exercise those pathways instead of inventing new ones.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧱 Non‑negotiables this folder must respect (KFM v13)

### 1) Canonical pipeline ordering (inviolable)
Samples here should **only reference** artifacts that exist downstream of the canonical pipeline:
ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) API boundary rule
The web UI **must never** query Neo4j directly; comparisons should call API endpoints (or use explicitly synthetic fixtures for offline rendering).  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) Provenance-first
Any comparison that presents results as “real” should point back to **cataloged evidence** (STAC/DCAT + PROV lineage) before it’s used in UI/story contexts.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 4) Evidence-first UX (especially in “inspect” / “why” affordances)
KFM’s design intent is that users can inspect sources and citations for layers/analyses. Comparisons should keep that affordance intact (e.g., “Evidence” drawer per series). 

### 5) Auditability & telemetry signals
Where sensitivity/redaction is relevant, emit telemetry events so governance can answer **“who saw what and why.”** (Example event: `focus_mode_redaction_notice_shown`.)  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Suggested layout

> This repo may evolve—treat the following as the **recommended** structure for comparison samples.

```text
📁 web/assets/samples/analytics/comparisons/
├── 📄 README.md
├── 📄 index.json                       # registry of available comparison packs (recommended)
└── 📁 packs/
    └── 📁 <comparison_id>/
        ├── 📄 manifest.json            # comparison definition (config-first)
        ├── 🖼️ preview.png              # optional
        └── 📄 fixture.response.json    # optional; synthetic-only; for Storybook/tests
```

---

## 🧾 Comparison Pack Manifest (contract-first)

A “comparison pack” is **a UI-friendly contract** describing:

- **what** is being compared (series A/B/…)  
- **how** the UI should render the comparison  
- **where** evidence comes from (STAC/DCAT/PROV references)  
- **what** telemetry should fire (for governance + analytics)

<details>
<summary><b>📦 Example <code>manifest.json</code></b> (config-first; API-backed)</summary>

```json
{
  "id": "compare__hydrology__streamflow_vs_precip__1900_1950",
  "title": "Streamflow vs Precipitation (1900–1950)",
  "summary": "Side-by-side time series with delta + correlation summary.",
  "kind": "timeseries",
  "mode": "api",
  "classification": {
    "level": "public",
    "notes": "No sensitive locations; derived metrics are aggregated."
  },
  "series": [
    {
      "seriesId": "streamflow",
      "label": "Streamflow",
      "api": {
        "endpoint": "/analytics/timeseries",
        "params": { "metric": "streamflow", "timeRange": "1900-01-01/1950-12-31" }
      },
      "evidence": {
        "stacItemIds": ["stac:item:..."],
        "dcatDatasetIds": ["dcat:dataset:..."],
        "provBundleIds": ["prov:bundle:..."]
      }
    },
    {
      "seriesId": "precip",
      "label": "Precipitation",
      "api": {
        "endpoint": "/analytics/timeseries",
        "params": { "metric": "precip", "timeRange": "1900-01-01/1950-12-31" }
      },
      "evidence": {
        "stacItemIds": ["stac:item:..."],
        "dcatDatasetIds": ["dcat:dataset:..."],
        "provBundleIds": ["prov:bundle:..."]
      }
    }
  ],
  "comparison": {
    "derived": [
      { "id": "delta", "label": "Δ (A − B)" },
      { "id": "pct_change", "label": "% change vs baseline" },
      { "id": "corr", "label": "Correlation (Pearson)" }
    ]
  },
  "viz": {
    "defaultView": "lines",
    "units": { "streamflow": "cfs", "precip": "in" },
    "a11y": { "requiresTableView": true }
  },
  "telemetry": {
    "onOpen": "comparison_opened",
    "onRun": "comparison_run_started",
    "onComplete": "comparison_run_completed",
    "onExport": "comparison_export_clicked"
  }
}
```
</details>

### Manifest principles
- **`mode: "api"` is the default.** It respects the API boundary rule by design.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Evidence is not optional** for anything that might be treated as “real.” KFM is explicitly provenance-first and evidence-first.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Classification is explicit** to prevent accidental “leak-by-UI.” Outputs cannot be less restricted than inputs.  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔌 How the web UI should use these samples

```mermaid
flowchart LR
  P[📦 Comparison Pack<br/>(manifest + evidence)] --> UI[🌐 Web UI<br/>(web/)]
  UI -->|governed requests| API[🧱 API Layer<br/>(src/server)]
  API --> G[🕸️ Graph]
  API --> C[📚 Catalogs<br/>STAC/DCAT/PROV]
  UI --> T[📡 Telemetry<br/>(events + audit trails)]
```

### Expected runtime behavior
1. UI loads `index.json` (or equivalent registry)  
2. User selects a comparison → UI loads `packs/<id>/manifest.json`  
3. UI runs API queries described in the manifest (**never** direct graph calls)  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
4. UI renders:
   - side-by-side chart(s)
   - derived metrics (delta, % change, etc.)
   - evidence panel per series (STAC/DCAT/PROV links)
5. UI emits telemetry events (open/run/complete/export + any redaction notices)  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ♿ Accessibility expectations (don’t skip)

Comparisons should be usable in multiple modalities:

- keyboard navigation (no mouse required)
- “table view” fallback for charts (screen reader friendly)
- clear labeling of units and baselines (what’s A? what’s B?)
- avoid color-only meaning

These samples should help exercise **accessibility audit hooks** as part of the UI contract surface.  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Using these samples for QA

Comparison packs are great fixtures for:
- Storybook states (stable UI snapshots)
- integration tests that validate API → UI rendering
- end-to-end flows (select → run → inspect evidence → export)

KFM’s QA strategy includes unit/integration/E2E testing and mentions tools such as **pytest** and **Cypress**.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ Contribution checklist

Before adding/editing a comparison pack:

- [ ] **API-boundary compliant** (no direct graph calls)  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] **Provenance referenced** (STAC/DCAT/PROV IDs or links where applicable)  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] **Classification declared** and consistent with inputs  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] **No real sensitive data** embedded in the frontend  
- [ ] **Telemetry hooks named** (open/run/complete/export + redaction events if relevant)  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] **A11y fallback** exists (table view / labels / baselines)  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] If fixtures exist: they are **synthetic**, deterministic, and clearly labeled

---

## ✍️ Adding a new comparison pack (recipe)

1. **Choose an ID**  
   Convention suggestion:  
   `compare__<domain>__<metricA>_vs_<metricB>__<time_or_scope>`

2. **Create pack directory**  
   `web/assets/samples/analytics/comparisons/packs/<comparison_id>/`

3. **Write `manifest.json`**  
   - define series and API queries  
   - include evidence pointers  
   - define default viz + telemetry event names

4. **(Optional) Add `preview.png`**  
   Keep it small + non-sensitive.

5. **(Optional) Add `fixture.response.json`**  
   Only if you truly need offline rendering; must be synthetic.

6. **Register in `index.json`**  
   So UI pickers can discover it.

---

## 📚 References (project sources)

- KFM v13 directory layout + canonical subsystem locations (including `web/`).  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- KFM v13 invariants: pipeline ordering, API boundary, provenance-first, classification propagation, validation gates.  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Audit trail / telemetry example for redaction notices.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- KFM transparency intent: users should be able to inspect layer sources/citations.   
- Testing/QA toolchain mentions (unit/integration/E2E; pytest/Cypress).  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
