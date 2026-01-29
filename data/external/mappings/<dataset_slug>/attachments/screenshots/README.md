# 📸 Screenshot Attachments — `"<dataset_slug>"`

![Attachments](https://img.shields.io/badge/attachments-screenshots-2ea44f?style=flat-square)
![Purpose](https://img.shields.io/badge/purpose-evidence%20%26%20QA-blue?style=flat-square)
![Policy](https://img.shields.io/badge/policy-provenance--friendly-orange?style=flat-square)
![Formats](https://img.shields.io/badge/formats-.png%20%7C%20.webp-lightgrey?style=flat-square)

> [!NOTE]
> This directory holds **visual evidence** (QA, previews, diffs) for the mapping dataset **`<dataset_slug>`**.  
> Screenshots support trust & review — they are **not** the canonical data source for processing pipelines.

---

## 📍 Location

`data/external/mappings/<dataset_slug>/attachments/screenshots/`

Quick links:
- ↩️ Dataset root: `../../README.md` (recommended to exist)
- 📎 Attachments root: `../`
- 🧾 (Optional) Screenshot index: `./index.md` or `./index.csv`

---

## 🎯 What belongs here

✅ Put screenshots here when they help humans verify something **fast**:

- 🗺️ **Layer previews** (styling, symbology, labeling, scale behavior)
- 🧪 **QA evidence** (alignment, reprojection, clipping, topology, join correctness)
- 🔁 **Before/After comparisons** (pipeline changes, schema updates, new source versions)
- 🧭 **UI previews** (web map states, popups, filters, legends)
- 📤 **Layout exports** (print-style map outputs used in docs or reports)

---

## 🚫 What does *not* belong here

❌ Don’t use this folder as a dumping ground:

- Raw datasets (put those in `raw/` or the correct ingestion folder)
- Processed outputs that the pipeline depends on
- Screenshots containing **sensitive/PII** or restricted layers without permission
- Unlicensed/attribution-missing basemap tiles or proprietary cartography exports

---

## 🗂️ Suggested subfolders (optional but helpful)

If the folder grows, organize it like this:

```text
📁 screenshots/
├── 🧭 ui/               # web app / viewer screenshots
├── 🧪 qa/               # QA proof (geometry, joins, alignment, topology)
├── 🔁 diffs/            # before/after pairs
├── 🗺️ layouts/          # print/export layouts
└── 🧾 index.md|index.csv # registry of what’s here + why
```

> [!TIP]
> Keep the structure **boring and predictable**. The best folder is the one reviewers can scan in 10 seconds.

---

## 🏷️ Filename convention

### ✅ Recommended (human-readable + sortable)

Use double underscores `__` to keep names parseable:

`YYYYMMDD__<dataset_slug>__<kind>__<area_or_feature>__z<zoom_or_scale>__crs-<epsg>__v<rev>.png`

**Examples**
- `20260129__kansas_roads__qa__douglas_county__z12__crs-3857__v01.png`
- `20260129__kansas_roads__diff_before__lawrence__z13__crs-3857__v01.png`
- `20260129__kansas_roads__diff_after__lawrence__z13__crs-3857__v01.png`
- `20260129__kansas_roads__layout__statewide__scale-1-250k__crs-4326__v03.png`

### Allowed “kind” values (pick one)

- `ui`
- `qa`
- `diff_before`
- `diff_after`
- `layout`
- `preview`
- `debug`

> [!NOTE]
> If you don’t know the CRS/zoom, use `crs-unknown` / `zNA` **but** add details in the sidecar metadata (below).

---

## 🧾 Sidecar metadata (highly recommended)

For screenshots that matter (QA, diffs, publishable layouts), add a tiny companion file:

- `20260129__...__v01.png`
- `20260129__...__v01.md`  ← preferred (easy review)
  - or `20260129__...__v01.json`

### Sidecar template (`.md`)

```markdown
---
id: "20260129__<dataset_slug>__qa__<area>__z12__crs-3857__v01"
captured_at: "2026-01-29"
captured_by: "<your_name_or_handle>"
tool: "qgis|arcgis|maplibre|browser|script"
purpose: "QA evidence for <what changed/validated>"
source_dataset: "<dataset_slug>"
layer_or_view: "<layer_name / view route / endpoint>"
bbox_or_center: "<lon,lat or xmin,ymin,xmax,ymax>"
crs: "EPSG:####"
zoom_or_scale: "z12 | 1:250k"
commit_or_run_id: "<git_sha | pipeline_run_id>"
notes: |
  - What should a reviewer look for?
  - Any caveats?
credits: |
  - Data source(s):
  - Basemap (if any):
  - License/attribution notes:
---
```

> [!TIP]
> The sidecar is where you store *context* (commit hash, tool, exact view) so the screenshot stays useful months later.

---

## 🧭 Capture checklist

### Minimum (QA / debugging screenshots)

- ✅ Make the **issue visible** (turn on outlines, highlight selections, show boundaries)
- ✅ Include **enough context** to orient the viewer (place label, county name, etc.)
- ✅ If comparing, capture **same extent** for before/after
- ✅ If relevant, show **coordinates / CRS** somewhere (UI status bar or map annotation)
- ✅ Add a sidecar if the screenshot supports a decision or a merge

### Publication-style (layouts / narrative / docs)

Include the standard map elements when applicable:

- 📏 **Scale** (scale bar or clear numeric scale)
- 🧾 **Legend** (if symbols/colors aren’t self-evident)
- 🧭 **Directional indicator** (north arrow) when orientation isn’t obvious
- 🧱 **Neatline/border** if it improves readability
- 🏷️ **Sources / credits / date** (and projection/CRS if the map is analytical)

> [!NOTE]
> If the screenshot is meant to be cited or shared externally, treat it like a *map product* — include credits + date + projection notes.

---

## 🔒 Licensing, attribution, and sensitive content

Before committing:

- ✅ Verify you’re allowed to store/share what’s visible (data license + basemap terms)
- ✅ Include required attribution in the screenshot *or* the sidecar `credits:` block
- ✅ Avoid PII (names/addresses) unless explicitly allowed and necessary
- ✅ If redaction is required, redact before commit (blur boxes are fine)

---

## 🧹 Git hygiene (keep the repo lean)

- Prefer `.webp` for UI screenshots when quality is acceptable ✅
- Use `.png` for crisp linework / labels / cartographic exports ✅
- Don’t commit duplicates — replace or version intentionally (`v02`, `v03`, etc.)
- If a screenshot must be large, consider Git LFS (or store externally + checksum pointer)

---

## 🧾 Optional: screenshot index

If you have more than ~10 screenshots, add an `index.md` (human-friendly) or `index.csv` (machine-friendly).

### `index.md` starter

| 🖼️ Screenshot | Kind | Area | Why it exists | Linked work |
|---|---:|---|---|---|
| `20260129__<dataset_slug>__qa__example__z12__crs-3857__v01.png` | `qa` | Example Area | Validates reprojection + snapping | Issue/PR: `<link>` |
| `20260129__<dataset_slug>__diff_after__example__z12__crs-3857__v01.png` | `diff_after` | Example Area | Shows fixed alignment | Issue/PR: `<link>` |

---

## ⚡ “Add a screenshot in 60 seconds” recipe

1) Capture the screenshot (same extent if it’s a diff) 🖼️  
2) Rename using the convention 🏷️  
3) Add a sidecar (`.md`) if it’s important 🧾  
4) Update `index.md` if present 📋  
5) Commit with a clear message, e.g. `docs(screenshots): add QA proof for <dataset_slug>` ✅

---

