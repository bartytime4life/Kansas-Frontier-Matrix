# 📊 Chart Export Data (UI‑Ready)  
> **Path:** `web/assets/charts/exports/data/`  
> **Role:** lightweight, static data exports optimized for charts in the `web/` frontend.

![scope](https://img.shields.io/badge/scope-web%20UI-blue)
![format](https://img.shields.io/badge/format-JSON%20%7C%20CSV-informational)
![governance](https://img.shields.io/badge/governance-provenance%20required-brightgreen)
![contract](https://img.shields.io/badge/contract-schema%20backed-success)

---

## ✨ What this folder is

This directory contains **chart-ready exports** that the frontend can load **without heavy processing**. Think of these files as **UI assets**: small, structured, deterministic, and safe to ship with the app.

Typical use-cases:
- 📈 Time-series charts in popups/side panels
- 🧭 “Focus Mode” panels where charts must be fast + traceable
- 🧩 Demo datasets / “starter” visualizations for offline-ish browsing

---

## 🚫 What this folder is NOT

- **Not canonical data.** This is *downstream* UI packaging. Canonical sources live in `data/` and must be cataloged/validated there first.
- **Not a dumping ground.** If a chart can’t explain *where it came from*, it doesn’t belong here.
- **Not for huge datasets.** If it’s big, it probably belongs behind the API (or in `data/processed/` with a proper contract + provenance), not inside bundled web assets.

---

## 🧬 Golden rules (KFM invariants, applied to charts)

1. **🧾 Provenance-first:** Anything shown in UI must be traceable back to cataloged sources (and governed processing).
2. **📜 Contract-first:** Every export has an explicit schema (or a referenced schema) and stable meaning over time.
3. **🧭 No leapfrogging:** Exports here are *downstream* artifacts. They should be generated from validated outputs, not handcrafted.
4. **🛡️ No sensitive leakage:** If content could reveal sensitive locations or restricted info, it must be generalized/redacted before it ever reaches the UI export stage.

---

## 🗂️ Recommended folder layout

> ✅ You can use folders-per-export (preferred) or flat files for very small projects.  
> **Folders-per-export** scales better and keeps metadata/provenance co-located.

```text
web/assets/charts/exports/data/
├─ 📌 index.json                         # Optional: registry of available exports (generated)
├─ 📁 population_county_1860_2020/
│  ├─ data.json                          # The chart payload (series/points)
│  ├─ meta.json                          # Human + machine-readable metadata (data contract)
│  ├─ prov.json                          # Provenance/lineage reference
│  └─ schema.json                        # Optional: JSON Schema or schema reference wrapper
├─ 📁 precipitation_station_daily/
│  ├─ data.json
│  ├─ meta.json
│  └─ prov.json
└─ README.md
```

---

## 🏷️ Naming conventions

### Export IDs
Use **kebab_case OR snake_case** consistently across the web app (pick one convention for the repo; don’t mix).
- ✅ `population_county_1860_2020`
- ✅ `precipitation_station_daily`
- ❌ `PopulationCounty` / `pop county`

### Versioning
When the **meaning** of a dataset changes (not just new rows), bump a version:
- Folder name suffix: `__v1`, `__v2`  
  Example: `population_county_1860_2020__v2/`
- Or use semantic version in `meta.json` (`export_version: "2.0.0"`)

### Determinism
Exports should be reproducible:
- Same inputs + same pipeline version ⇒ same output bytes (or at least the same semantic content + checksum recorded in metadata)

---

## 📦 Supported formats

### ✅ JSON (default)
Preferred for UI shipping. Fast to parse, compresses well over the wire.

**Good for:**
- time series
- categorical breakdowns
- small multipanel datasets

### ✅ CSV (debug-friendly)
Allowed for quick inspection or intermediary steps, but **prefer JSON for runtime**.

### ❌ Avoid
- Big Parquet in the frontend bundle
- Huge GeoJSON (unless aggressively simplified and truly necessary)
- Anything that requires a “special reader” in the browser without strong reason

---

## 🧱 Data shape: recommended “chart-series@1” contract

Use a compact, predictable structure. Keep strings minimal, keep numbers numeric.

### `data.json` example (time-series)
```json
{
  "schema_version": "chart-series@1",
  "x": ["1860-01-01", "1870-01-01", "1880-01-01"],
  "series": [
    {
      "id": "population_total",
      "label": "Population",
      "unit": "people",
      "y": [107206, 364399, 996096]
    }
  ]
}
```

### Optional: categorical / grouped series
```json
{
  "schema_version": "chart-series@1",
  "x": ["2024-01", "2024-02", "2024-03"],
  "series": [
    { "id": "rainfall_mm", "label": "Rainfall", "unit": "mm", "y": [12.4, 8.1, 15.0] },
    { "id": "snow_cm", "label": "Snow", "unit": "cm", "y": [2.0, 0.0, 1.2] }
  ]
}
```

### Data rules (practical)
- Use **ISO 8601** for time keys unless your chart explicitly uses numeric bins.
- Missing values: use `null` (not `"NaN"`, not empty string).
- Never change the meaning of a field without bumping the export version.

---

## 🧾 `meta.json` contract (required)

`meta.json` makes these exports **self-describing** and supports UI attribution + traceability.

### Required fields (minimum viable)
```json
{
  "export_id": "population_county_1860_2020",
  "export_version": "1.0.0",
  "title": "Kansas County Population (1860–2020)",
  "description": "County-level population totals by census year.",
  "tags": ["demographics", "time-series"],

  "ui": {
    "default_chart": "line",
    "x_label": "Year",
    "y_label": "Population"
  },

  "data_contract": {
    "schema_version": "chart-series@1",
    "x_type": "date",
    "y_type": "integer",
    "units": {
      "population_total": "people"
    }
  },

  "source": {
    "catalog_dataset_ids": ["urn:kfm:dataset:population:county:1860-2020"],
    "source_urls": [],
    "license": "Public Domain",
    "attribution": [
      "Original providers credited in the canonical catalog entry."
    ]
  },

  "build": {
    "generated_at": "2026-01-15T00:00:00Z",
    "generator": "src/pipelines/<domain>/export_charts.*",
    "commit_sha": "<git sha>",
    "checksum_sha256": "sha256:<hash-of-data.json>"
  }
}
```

> 💡 **Tip:** Keep canonical attribution + licensing in the **catalog**, and repeat only what the UI needs here (or reference the catalog IDs so the UI can fetch full attribution from the API).

---

## 🧾 `prov.json` (required)

This file is the **lineage pointer** that proves “this chart came from those sources, via that process”.

### Lightweight provenance (pragmatic)
```json
{
  "prov_version": "1",
  "derived_from": [
    "urn:kfm:dataset:population:county:1860-2020"
  ],
  "activity": {
    "type": "export",
    "pipeline": "src/pipelines/population/export_charts.py",
    "run_id": "run-2026-01-15T00:00:00Z",
    "tool": "kfm-pipeline",
    "parameters": {
      "aggregation": "sum",
      "group_by": ["county_id", "year"]
    }
  },
  "agent": {
    "type": "software",
    "name": "kfm-pipeline",
    "version": "v13"
  }
}
```

### If you’re using PROV‑O formally
You can store or reference a PROV‑O JSON-LD graph instead. The key is: **UI exports must link back to governed provenance**.

---

## ✅ Validation expectations

Before an export is considered “shippable”:

- ✅ `data.json` validates against the referenced schema (`chart-series@1` or project schema)
- ✅ `meta.json` contains required fields (title, license, catalog IDs, checksum, etc.)
- ✅ `prov.json` points to catalog IDs and identifies a pipeline/tool/run
- ✅ License is acceptable and attribution is not missing
- ✅ No sensitive values are accidentally shipped (especially location-like fields)

---

## ⚡ Performance & size guidelines

Keeping exports fast is part of the “UI contract”.

- Prefer **few files** per export (usually `data.json + meta.json + prov.json`)
- Prefer **arrays** over verbose objects when rendering performance matters
- Keep exports **small enough to ship** with the frontend  
  If a dataset grows, move it behind the API and fetch on-demand.

---

## ➕ Adding a new export (workflow)

1. **Start from cataloged data** (canonical datasets first)
2. Add/extend a pipeline step that produces the chart-friendly structure
3. Output into a new folder under `web/assets/charts/exports/data/<export_id>/`
4. Generate:
   - `data.json`
   - `meta.json`
   - `prov.json`
5. Validate schemas + licenses + sensitivity checks
6. Wire the export into the UI (chart config points to `export_id`)
7. Confirm rendering in the map UI / Focus Mode

---

## ✅ Definition of Done (DoD) checklist 🧩

- [ ] Export has `data.json`, `meta.json`, and `prov.json`
- [ ] `meta.json.source.catalog_dataset_ids` is present and correct
- [ ] `meta.json.build.checksum_sha256` matches `data.json`
- [ ] Schema validation passes
- [ ] Chart renders correctly in the UI
- [ ] No sensitive/restricted content is exposed
- [ ] Naming/versioning follows conventions

---

## 🧯 Common pitfalls

- **“Just one quick chart”**: hand-editing data here creates drift. Use a pipeline.
- **Missing license/attribution**: the UI must be able to show credits.
- **Unstable timestamps**: if your “x” is time, ensure consistent timezone handling (prefer UTC).
- **Exporting too much**: a single export that balloons can slow builds, loads, and reviews.

---

## 🔍 Quick glossary

- **Export**: a UI-ready artifact derived from canonical datasets
- **Contract**: the schema + metadata requirements that make the export safe to consume
- **Provenance**: the lineage showing how this artifact was produced from sources
- **Catalog dataset ID**: stable identifier that points to governed dataset metadata

---

🧭 **If you’re unsure whether something belongs here:**  
Default to **putting it in canonical data + catalogs** and exposing it via the API. This folder is for **fast, traceable, UI-ready** slices—not the system of record.