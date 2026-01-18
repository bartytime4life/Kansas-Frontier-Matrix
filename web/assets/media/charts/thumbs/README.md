# 🖼️ Chart Thumbnails (thumbs/)  

![scope](https://img.shields.io/badge/scope-web%20UI-blue) ![type](https://img.shields.io/badge/type-static%20media-lightgrey) ![path](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2Fcharts%2Fthumbs-orange)

Small, fast preview images for charts used across the Kansas Frontier Matrix web UI (cards, pickers, pop-ups, evidence panels) 📈🧭

> [!IMPORTANT]
> Thumbnails are **UI decoration** — not a data source.  
> ✅ Use them to *preview* a chart.  
> ❌ Never treat them as evidence, measurements, or “truth.”

---

## 📁 Location & intent

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 📈 charts/
         └─ 🖼️ thumbs/   ← ✅ you are here 📌 Small preview images for lists/catalogs/docs (web-optimized)
```

This folder is for **tiny chart preview images** that can be displayed quickly while the **real chart** renders from governed API data.

---

## ✅ What belongs here

- 🪶 **Lightweight previews** (WebP/PNG/SVG) that help users recognize a chart at a glance  
- 🌗 **Theme variants** (`light` / `dark`) when needed
- 🔁 **Versioned** outputs (avoid overwriting older thumbnails once referenced)

---

## 🚫 What does NOT belong here

- 🧱 Raw datasets, CSVs, screenshots of tables, or anything that could be interpreted as “the data”
- 🕵️ Anything containing restricted/sensitive details (locations, individuals, protected sites, etc.)
- 📚 Story-specific figures (put those inside the Story Node folder’s `assets/` instead)
- 🧪 One-off experiments (put those in an experiments area, not in UI assets)

> [!NOTE]
> If an image is *story-specific*, it should live with the story (so it can be reviewed/governed with the narrative).

---

## 🧩 Where these thumbnails show up

Typical UI placements 🎛️  
- 🗂️ Dataset / layer cards  
- 🧰 Chart gallery or “picker” grids  
- 🔍 Pop-ups / evidence panels (preview before expanding)  

**Rule of thumb:** thumbnail = *preview*, live chart = *actual view*.

---

## 🏷️ Naming rules

Keep filenames:
- lowercase ✅
- `kebab-case` ✅
- ASCII only ✅
- no spaces ✅
- no “final_final2.png” 😅

<details>
<summary><strong>Recommended filename pattern</strong> 📌</summary>

`<chart-id>__<w>x<h>__<theme>__v<rev>.<ext>`

**Fields**
- `chart-id` → stable slug for the chart (e.g. `population-by-county`)
- `w x h` → target pixel size (e.g. `320x180`)
- `theme` → `light` | `dark` | `mono` (omit if only one)
- `rev` → dataset/chart revision marker (semver, date, or short hash)

**Examples**
- `population-by-county__320x180__light__v13.0.0.webp`
- `population-by-county__320x180__dark__v13.0.0.webp`
- `land-treaties-timeline__640x360__light__v2026-01-17.png`

</details>

> [!TIP]
> If you’re unsure what to use for `rev`, pick the **dataset version** (preferred) or a **release tag**. Keep it consistent.

---

## 📐 Standard sizes

| Use case 🧭 | Size | Notes |
|---|---:|---|
| Card preview (default) | `320x180` | 16:9, fast load |
| Retina card preview | `640x360` | 2× clarity |
| Square tile (optional) | `256x256` | grids / tiles |

---

## 🖼️ Formats & optimization

Preferred order ✅  
1. **WebP** (`.webp`) — best size/quality for thumbnails  
2. **PNG** (`.png`) — when you *need* transparency or exact pixels  
3. **SVG** (`.svg`) — only for **simple** crisp line/bar previews (keep it tiny)

Performance budgets ⚡ *(guidelines — adjust if the UI needs tighter limits)*  
- `320x180`: aim for **≤ 75 KB**  
- `640x360`: aim for **≤ 150 KB**

Quality tips 👀  
- avoid tiny labels (they’ll blur at thumbnail scale)
- thicker strokes > hairlines
- keep generous padding (don’t clip axes)
- don’t encode meaning with color alone (accessibility)

---

## 🧾 Manifest metadata (strongly recommended)

A machine-readable index keeps the UI consistent and prevents “orphan” assets.

Create/update:

- `web/assets/media/charts/thumbs/manifest.json`

Example:

```json
{
  "population-by-county": {
    "alt": "Population by county (preview)",
    "latest": {
      "light": "population-by-county__320x180__light__v13.0.0.webp",
      "dark": "population-by-county__320x180__dark__v13.0.0.webp"
    },
    "source": {
      "dataset_id": "dcat:ks-population-county",
      "stac_item": "stac:item:ks-population-county-2020",
      "prov_activity": "prov:activity:population-pipeline-run-2026-01-17"
    }
  }
}
```

> [!IMPORTANT]
> If a thumbnail could be interpreted as evidence, it **must** point back to a governed dataset/version and lineage reference (even if it’s “just a preview”).

---

## 🛠️ Adding a new thumbnail

1. 🏷️ Choose a stable `chart-id`
2. 🖼️ Export at a standard size (and optionally the retina size)
3. ⚡ Optimize to WebP/PNG and keep under budget
4. 🧾 Add/update `manifest.json`
5. ✅ Verify visually in the UI (light/dark, no clipping, readable)

### PR checklist ✅

- [ ] Filename follows pattern (lowercase, no spaces)
- [ ] Size matches a standard target
- [ ] File is optimized (budget respected)
- [ ] No restricted/sensitive info is visible
- [ ] `manifest.json` updated (includes `alt` + source pointers)
- [ ] Looks good in both themes (if applicable)

---

## 🔗 Related docs (repo-local)

- 🧭 **Master Guide v13:** [`docs/MASTER_GUIDE_v13.md`](../../../../../docs/MASTER_GUIDE_v13.md)  
- 📏 **Standards & profiles:** [`docs/standards/`](../../../../../docs/standards/)  
- 📚 **Story Nodes (story assets live there):** [`docs/reports/story_nodes/`](../../../../../docs/reports/story_nodes/)  

---
