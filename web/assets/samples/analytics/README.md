# 📊 Analytics Samples

![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Fsamples%2Fanalytics-blue)
![Data](https://img.shields.io/badge/data-JSON%20%7C%20GeoJSON%20%7C%20CSV-informational)
![Policy](https://img.shields.io/badge/policy-provenance--first-success)
![Telemetry](https://img.shields.io/badge/telemetry-audit--ready-important)

Static **sample analytics fixtures** for the KFM Web UI: charts, summaries, model outputs, and telemetry events you can use for **dev previews, Storybook-style demos, and UI tests**.

> 🔒 **Safety & Governance:** Only commit **synthetic / anonymized** data here. Never commit raw user telemetry, PII, secrets, or sensitive locations.

---

## 🧭 Quick navigation

- [🎯 Purpose](#-purpose)
- [📦 What belongs here](#-what-belongs-here)
- [🗂️ Suggested layout](#️-suggested-layout)
- [🧩 Payload contracts](#-payload-contracts)
- [🧪 How to use these samples](#-how-to-use-these-samples)
- [✅ Adding a new sample](#-adding-a-new-sample)
- [🔗 Related (repo) references](#-related-repo-references)

---

## 🎯 Purpose

KFM’s UI supports analytics-heavy interactions (summaries, charts, comparisons, model outputs, “Focus Mode” evidence panels, etc.). This folder provides **drop-in fixtures** that:

- ✅ unblock UI work before the full API is ready
- ✅ keep UI behavior stable via regression tests
- ✅ document “shape expectations” for analytics responses
- ✅ support governance-ready telemetry demos (audit + compliance dashboards)

---

## 📦 What belongs here

### ✅ Good candidates
- 📈 **Chart payloads**: time series, histograms, distributions, summary stats  
- 🧮 **Computed analytics results**: trend lines, percent changes, z-scores, aggregates
- 🤖 **Model outputs** (safe + explainable): regression coefficients, feature importance, evaluation summaries
- 🧾 **Telemetry fixtures**: UI interaction events + “governance signals” (redaction notices, blocked publication attempts, etc.)
- 🗺️ **Comparative analysis configs**: swipe/compare UI state, “difference map” metadata (not huge rasters)

### 🚫 Not allowed here
- ❌ real user/session telemetry
- ❌ API keys, tokens, credentials
- ❌ sensitive coordinates (unless intentionally generalized and clearly labeled)
- ❌ large binary dumps (COGs/tiles/etc. belong in data pipelines + catalogs, not web assets)

---

## 🗂️ Suggested layout

> This is a **recommended** structure. Adjust to your UI components, but keep things tidy and predictable.

```text
web/assets/samples/analytics/
├── 📄 README.md                         # 📘 What analytics samples exist, size limits, and “demo-only” governance rules
├── 📊 charts/                           # Small chart-ready payloads (JSON/CSV) for UI components + tests
│   ├── 📈📄 timeseries__demo.json        # Timeseries example (deterministic, tiny, safe to ship)
│   └── 📊📄 histogram__demo.json         # Histogram example (bins/counts or raw points per contract)
├── 🧾 summaries/                        # Quick stats + computed rollups (used by summary panels/cards)
│   └── 📊🧾 stats__demo.json             # Example summary metrics payload (mean/median/ranges/etc.)
├── 🧪 regression/                       # Model-style outputs (coefficients, metrics) for derived-results rendering
│   └── 🧮📄 linear_regression__demo.json # Regression demo (coeffs, R², residual stats, metadata)
├── 🔁 comparisons/                      # Compare/swap/diff “state” fixtures (before/after, swipe, side-by-side)
│   └── ↔️📄 swipe_compare__demo.json     # Comparison fixture (two states + labels + UI hints)
├── 📡 telemetry/                        # UI events + governance signals (audit-ready sample payloads)
│   ├── 🧭📄 ui_event__layer_toggle.json  # Example UI event (layer toggled on/off with safe context)
│   └── 🛡️📄 governance__redaction_notice.json # Example governance event (what was redacted + why)
└── 🧩 dashboards/                       # Optional: layout configs for analytics panels/dashboards
    └── 🧩📄 dashboard__demo.json         # Demo dashboard layout (widgets, positions, data bindings)
```

---

## 🧩 Payload contracts

Even as “samples”, these files should feel like **real API responses** and follow KFM’s governance principles:

### 1) Always include **metadata**
Use a `meta` object for: `id`, `title`, `description`, `created_at`, `units`, and display hints.

### 2) Always include **provenance hooks**
Add a `provenance` object that can point back to cataloged records (STAC/DCAT/PROV).  
Even if you don’t have the full IDs yet, include placeholders like `stac_items: []`.

### 3) Include **classification / sensitivity**
If a payload is derived from sensitive sources, the **sample must reflect that** (and/or be generalized).

### 4) Keep it **small + deterministic**
Samples should be stable fixtures—no random numbers unless seeded and documented.

---

## 📎 Example payloads

<details>
  <summary><strong>📈 Time series chart payload (JSON)</strong></summary>

```json
{
  "meta": {
    "id": "timeseries__demo__rainfall_county",
    "title": "Demo: Annual Rainfall (Synthetic)",
    "description": "Synthetic example for testing time-series chart rendering.",
    "created_at": "2026-01-15T00:00:00Z",
    "units": "in/yr"
  },
  "data": {
    "series": [
      { "t": "2016", "value": 32.1 },
      { "t": "2017", "value": 28.4 },
      { "t": "2018", "value": 30.0 },
      { "t": "2019", "value": 34.2 },
      { "t": "2020", "value": 31.7 }
    ],
    "summary": {
      "min": 28.4,
      "max": 34.2,
      "mean": 31.28
    }
  },
  "provenance": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": [],
    "notes": "Demo fixture only. Replace with real catalog references when wiring to API."
  },
  "classification": {
    "level": "public",
    "reason": "synthetic"
  }
}
```
</details>

<details>
  <summary><strong>🧮 Regression output payload (JSON)</strong></summary>

```json
{
  "meta": {
    "id": "linear_regression__demo__yield_vs_rain",
    "title": "Demo: Linear Regression Output",
    "description": "Synthetic regression result payload for coefficient + metrics UI widgets.",
    "created_at": "2026-01-15T00:00:00Z",
    "model_type": "linear_regression"
  },
  "data": {
    "target": "yield_bu_acre",
    "features": ["rainfall_in", "avg_temp_f"],
    "coefficients": [
      { "name": "intercept", "value": 12.4 },
      { "name": "rainfall_in", "value": 1.85 },
      { "name": "avg_temp_f", "value": -0.22 }
    ],
    "metrics": {
      "r2": 0.71,
      "rmse": 5.3
    }
  },
  "provenance": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": [],
    "notes": "Model output is synthetic; used to validate rendering + formatting."
  },
  "classification": {
    "level": "public",
    "reason": "synthetic"
  }
}
```
</details>

<details>
  <summary><strong>🧾 Telemetry event fixture (JSON)</strong></summary>

```json
{
  "event_name": "ui.layer_toggled",
  "timestamp": "2026-01-15T12:34:56Z",
  "actor": {
    "role": "viewer",
    "id": "synthetic_user_001"
  },
  "context": {
    "page": "map",
    "session_id": "synthetic_session_abc",
    "app_version": "dev"
  },
  "payload": {
    "layer_id": "hydrology__streams__demo",
    "enabled": true
  },
  "classification": {
    "level": "public",
    "reason": "synthetic"
  }
}
```
</details>

---

## 🧪 How to use these samples

Common patterns (choose what fits your frontend setup):

- 🧩 **Component fixtures:** import JSON directly into chart components for local rendering.
- 🧪 **UI tests:** load fixtures as deterministic inputs for snapshot / interaction tests.
- 🧰 **Mock API mode:** serve these files as stand-ins for `/api/analytics/*` endpoints (dev-only).

> 💡 Tip: Keep the “sample” payload shape aligned with whatever the governed API will return so swapping from fixtures → real data is painless.

---

## ✅ Adding a new sample

### Checklist ✔️
- [ ] file lives in the correct bucket (charts / summaries / regression / telemetry / dashboards)
- [ ] includes `meta` + `provenance` (+ `classification` when applicable)
- [ ] uses deterministic values (or clearly documents randomness)
- [ ] contains **no** PII, secrets, or sensitive coordinates
- [ ] small enough to ship as a web asset (prefer KBs, not MBs)

### Naming convention 🏷️
Use clear, grep-friendly names:

- `timeseries__<topic>__<scope>.json`
- `stats__<topic>__<scope>.json`
- `linear_regression__<topic>__<scope>.json`
- `ui_event__<action>.json`
- `governance__<signal>.json`

---

## 🔗 Related (repo) references

If present in the repo, these are the “north star” docs for how analytics + telemetry should behave:

- 📘 `docs/MASTER_GUIDE_v13.md` (pipeline ordering, contracts, governance)
- 🧾 `schemas/telemetry/` (telemetry event validation)
- 🧩 `schemas/ui/` (UI config + payload validation)
- 🧱 `src/server/` (API boundary; governance + redaction enforcement)
- 🌐 `web/` (React/Map UI implementation)

---

### 🧠 Philosophy (why we’re strict about this)

KFM is a provenance-first, evidence-first system: analytics are only trustworthy when outputs are traceable, classified correctly, and safe to display. Samples should reflect that culture—**even when they’re “just mocks.”**
