# 📈 Time Series PNG Chart Exports

![Asset Type](https://img.shields.io/badge/asset-PNG-blue)
![Chart Type](https://img.shields.io/badge/chart-time--series-8a2be2)
![Usage](https://img.shields.io/badge/usage-web%20UI%20%2B%20stories-brightgreen)
![Governance](https://img.shields.io/badge/provenance-required-critical)

📍 **You are here:** `web/assets/charts/exports/png/timeseries/`

This folder contains **raster (PNG) exports** of **time-series charts** used by the KFM web experience (UI panels, Story Nodes, thumbnails, share cards, and other non-interactive contexts).

> [!IMPORTANT]
> **Exports are not evidence by themselves.** Every PNG in here must be traceable to a governed dataset + metadata trail (STAC/DCAT/PROV) and a deterministic generation process. No “mystery charts.” 🧬

---

## 🧭 Quick links

- [What belongs here](#-what-belongs-here)
- [Folder contract](#-folder-contract)
- [File layout](#-file-layout)
- [Naming convention](#-naming-convention)
- [Sidecar metadata](#-sidecar-metadata-required)
- [Add or update an export](#-add-or-update-an-export)
- [Quality gates](#-quality-gates)
- [Troubleshooting](#-troubleshooting)

---

## ✅ What belongs here

**✅ Yes**
- PNG images that render **time-series** data (single metric, multiple metrics, anomalies, cumulative series, seasonal bands, etc.).
- PNGs intended for:
  - Story Node media
  - UI fallbacks (when interactive charts aren’t appropriate)
  - Thumbnails / preview cards
  - Social/OG share images

**❌ No**
- Raw time-series values (those belong in `data/processed/**` and the API).
- Ad-hoc charts without a provenance trail.
- Screenshots of dashboards unless they’re governed story assets **and** have citations.

---

## 🔒 Folder contract

This directory is treated as a **build output surface** for the front-end:

1. **Do not hand-edit** exported images (unless explicitly marked as a “manual story illustration” and reviewed).
2. **Every PNG must have a sidecar metadata file** with the same basename:  
   `my-chart.png` → `my-chart.meta.json`
3. Each export must link back to:
   - the **source dataset(s)** (dataset IDs / catalog IDs)
   - the **time range** and **aggregation rules**
   - the **generation method** (script/tool + run id / commit)
   - the **license/attribution** inherited from source data

> [!NOTE]
> If you only need a chart inside a Story Node, still follow the same rule: **evidence-first** (data → catalogs → narrative). Story media should never become “floating truth.” 🧾

---

## 🗂️ File layout

```text
web/
└── 📁 assets/
    └── 📁 charts/
        └── 📁 exports/
            └── 📁 png/
                └── 📁 timeseries/
                    ├── 📄 README.md                👈 you are here
                    ├── 🖼️  <chart-slug>.png
                    ├── 🧾  <chart-slug>.meta.json
                    └── 🗃️  (optional) index.json   # machine-discovery (if used)
```

---

## 🏷️ Naming convention

Keep names **stable, searchable, and diff-friendly**.

### Recommended pattern

```text
<domain>__<dataset>__<metric>__<geo_or_scope>__<start>--<end>__<grain>__v<semver>.png
```

### Examples

```text
climate__uscrn__temp_c__ks_station_ks001__2000-01-01--2025-12-31__daily__v1.0.0.png
hydrology__usgs_nwis__discharge_cfs__arkansas_river__1980-01-01--2020-12-31__monthly__v1.1.0.png
land__fire_history__burned_area_pct__flint_hills__1984-01-01--2024-12-31__annual__v2.0.0.png
```

### Rules of thumb
- ✅ lowercase
- ✅ `__` as major separators (easy parsing)
- ✅ ISO dates (`YYYY-MM-DD`)
- ✅ include `v<semver>` when the chart definition changes
- ❌ spaces
- ❌ “final_final2.png” 😅

---

## 🧾 Sidecar metadata (required)

For each `*.png` export, include a matching `*.meta.json`.

### Minimum required fields

```json
{
  "id": "kfm:chart:timeseries:<slug>",
  "title": "Human-readable title",
  "description": "What the chart shows and why it exists.",
  "sources": [
    {
      "dataset_id": "kfm:dataset:<id>",
      "stac_item": "data/stac/items/<path>.json",
      "dcat_dataset": "data/catalog/dcat/<path>.jsonld"
    }
  ],
  "time": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD",
    "grain": "daily|monthly|annual|..."
  },
  "metrics": [
    { "name": "metric_name", "unit": "unit", "aggregation": "mean|sum|..." }
  ],
  "render": {
    "width": 1600,
    "height": 900,
    "dpi_scale": 2,
    "theme": "kfm-light|kfm-dark|print"
  },
  "provenance": {
    "pipeline": "src/pipelines/<...> or tools/<...>",
    "run_id": "optional-but-strongly-recommended",
    "commit": "git sha strongly recommended",
    "generated_at": "ISO-8601 timestamp",
    "prov_bundle": "data/prov/<path>.json"
  },
  "license": "SPDX identifier or explicit license text",
  "attribution": "Required attribution string(s)"
}
```

> [!TIP]
> If you’re generating these charts from multiple datasets (e.g., “precipitation + burned area”), include **multiple entries** in `sources[]` and explicitly document join/alignment logic in `description`.

---

## 🔁 Add or update an export

<details>
<summary><strong>Step-by-step checklist</strong> (click to expand)</summary>

1. **Start from governed data**
   - Confirm the underlying dataset exists in `data/processed/**`
   - Confirm catalogs exist/are planned: `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`

2. **Define the chart**
   - Ensure the chart definition (metric, filters, aggregation, time grain) is explicit and repeatable.
   - If a chart definition file/spec exists in your pipeline, update it there (preferred).

3. **Generate PNG**
   - Export at the intended target size(s) (e.g., hero vs thumbnail).
   - Keep the design consistent: labels, units, time axis, missing-data handling.

4. **Write the sidecar**
   - Create `*.meta.json` with the minimum fields above.
   - Copy attribution/license requirements from the source dataset metadata (do not invent).

5. **(Optional) Update index**
   - If the UI uses `index.json` for discovery, add the new entry there.

6. **Open a PR**
   - Include the PNG + meta + any pipeline/spec changes
   - Ensure reviewers can trace the asset back to evidence and catalogs

</details>

---

## ✅ Quality gates

### Visual + UX
- [ ] Title/axis labels are readable at intended display size
- [ ] Units are present (`mm`, `°C`, `cfs`, `%`, etc.)
- [ ] Missing data is visible/handled (gaps, annotations, or explicit note)
- [ ] Colors are accessible (avoid “only red vs green” semantics)

### Governance + provenance
- [ ] `*.meta.json` exists and validates
- [ ] `sources[]` points to dataset IDs and catalog paths
- [ ] `license` + `attribution` present and correct
- [ ] `provenance.commit` set (or a `run_id` equivalent)

### Performance
- [ ] PNG size is reasonable for the web (target: small enough to ship fast)
- [ ] Avoid unnecessary transparency / gigantic dimensions

> [!WARNING]
> If an export is used in the UI but cannot be traced to a dataset + catalogs + provenance, it should be treated as **untrusted** and must not ship. 🚫

---

## 🧩 How the UI typically uses these

Common patterns:
- **Story Nodes:** embedded as media with captions/citations
- **Catalog previews:** small “sparkline-style” thumbnails
- **Fallback panels:** when interactive charting is disabled or unavailable

If you need **interactive** time navigation (hover, select ranges, drill down), that should be implemented in `web/components/` (chart components) using **API-backed data**, with PNGs only as optional fallback visuals.

---

## 🛠️ Troubleshooting

**“I don’t know what dataset this PNG came from.”**  
→ It should not be here. Add provenance + sidecar (or remove the file).

**“The chart looks different across machines.”**  
→ Ensure deterministic generation: pinned dependencies, fixed fonts, and a scripted export path.

**“I need multiple sizes.”**  
→ Export multiple files with explicit size suffixes (e.g., `__w800`, `__w1600`) and declare `render.width/height` per file in each `.meta.json`.

---

## 📚 Related docs (repo)

- `docs/MASTER_GUIDE_v13.md` 📘
- `docs/standards/KFM_STAC_PROFILE.md` 🌐
- `docs/standards/KFM_DCAT_PROFILE.md` 🧾
- `docs/standards/KFM_PROV_PROFILE.md` 🧬
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` 🎬
