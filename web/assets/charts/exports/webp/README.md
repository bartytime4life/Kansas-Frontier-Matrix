# 📊 WebP Chart Exports (Web UI)

![format](https://img.shields.io/badge/format-.webp-0B7285)
![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fcharts-1F6FEB)
![governance](https://img.shields.io/badge/rule-provenance--first-2EA44F)

> **Folder:** `web/assets/charts/exports/webp/`  
> **Role:** Optimized, **static** chart images for the KFM web front-end (React), Story Nodes, and Focus Mode.

---

## 🧭 What lives here (and what doesn’t)

### ✅ Put these here
- Final, web-optimized **`.webp`** chart images meant to be shipped with the web app
- **Deterministic** exports generated from a script/spec (repeatable build)
- Charts that need to be embedded in:
  - UI panels / popups / docs-like screens
  - Story Nodes (narratives)
  - Focus Mode evidence views

### ❌ Don’t put these here
- Raw working files (e.g., `.psd`, `.ai`, `.xcf`)
- “One-off” screenshots with unclear provenance
- Duplicate exports with different names (reuse / version instead)
- Anything that leaks sensitive locations or private data (see **🔒 Governance**)

---

## 🧬 Provenance-first rule (non-negotiable)

KFM’s UI content is **evidence-driven**: if a chart appears in the UI or Focus Mode, it must be **traceable** to cataloged sources and a reproducible process.

That means every WebP in this folder must have:
1. **A sidecar metadata file** (required) 🧾  
2. A **clear link to its inputs + generation steps** (required) 🔁  
3. A **pointer to catalog/provenance identifiers** when used in Story Nodes / Focus Mode (required) 🧷  

---

## 📁 Folder layout

```text
web/
└─ assets/
   └─ charts/
      └─ exports/
         └─ webp/          👈 you are here
            ├─ README.md
            ├─ <chart>.webp
            └─ <chart>.webp.json   (required sidecar)
```

---

## 🏷️ Naming convention

We want names that are:
- **Readable** (humans can understand what it is)
- **Stable** (good caching)
- **Deterministic** (regenerating doesn’t invent new names)
- **Versioned** (don’t overwrite old meaning)

### Pattern

```text
<topic>-<metric>-<scope>--<variant>--v<NNN>@<width>w.webp
```

### Examples
- `climate-precip-kansas--annual--v003@1600w.webp`
- `hazards-tornado-counts--by-decade--v001@1280w.webp`
- `water-ogallala-levels--timeseries--v006@1600w.webp`

### Notes
- Use **kebab-case** only (`a-z`, `0-9`, `-`)  
- Bump `vNNN` when pixels meaningfully change (data window, method, styling, binning, etc.)  
- `@<width>w` enables responsive rendering patterns and avoids “mystery sizes”

---

## 🧾 Required sidecar metadata

For every file:
- `X.webp` must have `X.webp.json`

### Minimal schema (recommended)

```json
{
  "id": "climate-precip-kansas--annual--v003@1600w",
  "title": "Kansas Annual Precipitation (1895–2024)",
  "alt": "Line chart of annual precipitation in Kansas from 1895 to 2024 with a visible upward trend after 1980.",
  "caption": "Annual precipitation totals aggregated statewide. See sources and method for details.",
  "license": "CC-BY-4.0",
  "sources": [
    {
      "type": "catalog",
      "ref": "dcat:dataset/noaa-climate-kansas-1895-2024"
    }
  ],
  "provenance": {
    "generated_by": "scripts/charts/build_precip_timeseries.py",
    "params": {
      "region": "kansas",
      "aggregation": "annual",
      "range": "1895-01-01..2024-12-31"
    },
    "git": {
      "commit": "<sha>",
      "repo": "Kansas-Frontier-Matrix"
    },
    "created_utc": "2026-01-15T00:00:00Z"
  },
  "render": {
    "format": "webp",
    "width": 1600,
    "height": 900,
    "density": 2
  },
  "governance": {
    "sensitivity": "public",
    "notes": "Aggregated statewide; no sensitive coordinates."
  }
}
```

### Why we do this
- Enables **automated attribution** and method tracing
- Prevents “mystery assets”
- Gives Story Nodes and Focus Mode the hooks they need for trust & governance

---

## 🛠️ Export pipeline (recommended)

> Source-of-truth should live outside this folder (e.g., chart specs / scripts / notebooks).  
> This folder is the **published export target**.

### 1) Render at high quality
- Prefer **SVG** when the chart is primarily lines/text (crisp scaling)
- If using Matplotlib/Plotly/etc., render at **2×** (retina-friendly)

### 2) Convert to WebP

**Lossless (recommended for charts with text):**
```bash
cwebp -lossless -z 9 input.png -o output.webp
```

**High-quality lossy (if the chart is photo/map-heavy):**
```bash
cwebp -q 92 -m 6 input.png -o output.webp
```

### 3) Create/update the sidecar JSON 🧾
- Update `sources`, `provenance.generated_by`, `params`, and `git.commit`
- Ensure `alt` is meaningful and not a copy of the title

### 4) Register as evidence when used in narratives 🧷
If a chart will appear in **Story Nodes / Focus Mode**, ensure it’s:
- referenceable by a **catalog ID** (STAC/DCAT) and
- backed by a **PROV lineage record** (or equivalent)

---

## 🧩 Using these assets in the web app

### React import pattern (typical)
```ts
import chartUrl from "@/assets/charts/exports/webp/climate-precip-kansas--annual--v003@1600w.webp";
import meta from "@/assets/charts/exports/webp/climate-precip-kansas--annual--v003@1600w.webp.json";
```

### Rendering with accessibility ♿
```jsx
<figure>
  <img src={chartUrl} alt={meta.alt} loading="lazy" decoding="async" />
  {meta.caption && <figcaption>{meta.caption}</figcaption>}
</figure>
```

---

## 🔒 Governance & sensitive data guardrails

Charts can leak sensitive info even when they “look harmless” (e.g., precise coordinates on axes, tiny labels, identifying outliers).

**Before exporting:**
- Aggregate or bin sensitive locations
- Remove fine-grained identifiers
- Prefer regional summaries when required (county-level vs exact point)

> If a dataset has restricted visibility, the chart must respect that restriction too.

---

## 🧪 PR checklist

- [ ] Added `.webp`
- [ ] Added matching `.webp.json`
- [ ] File name matches convention (`--vNNN@<width>w`)
- [ ] Sidecar includes: `alt`, `sources`, `provenance.generated_by`, `params`
- [ ] If used in Story Nodes / Focus Mode: catalog/provenance references exist
- [ ] No sensitive location leaks / unintended disclosure
- [ ] Chart is readable on mobile (text sizes, aspect ratio)

---

## 🧰 Troubleshooting

<details>
  <summary><strong>My WebP looks blurry</strong></summary>

- Export at higher resolution (2×) before converting  
- Prefer lossless WebP for text-heavy charts  
- If starting from SVG, rasterize at the final target width (e.g., 1600w)  
</details>

<details>
  <summary><strong>File size is too big</strong></summary>

- Reduce canvas size (e.g., 1600w → 1280w)  
- Switch to high-quality lossy (`-q 90–92`)  
- Reduce excessive gridlines / shadows / noise in the chart style  
</details>

<details>
  <summary><strong>I don’t know what to put in <code>sources</code></summary>

Use the **catalog ID** of the dataset(s) powering the chart (preferred), or a stable external reference that is itself cataloged.
</details>

---

## 🔗 Related docs (repo-level)

- 📘 `docs/MASTER_GUIDE_v13.md` — pipeline invariants (contracts → evidence → UI → narrative)
- 🧾 `docs/standards/KFM_STAC_PROFILE.md` — asset metadata profile
- 🧾 `docs/standards/KFM_DCAT_PROFILE.md` — dataset/distribution metadata profile
- 🎬 `docs/templates/TEMPLATE__STORY_NODE_V3.md` — governed narrative structure + citation rules

---

### ✨ Guiding mantra
**No chart without sources. No UI without provenance.** ✅
