# 🖼️ Open Graph Chart Exports (PNG) — `web/assets/charts/exports/png/og/`

![asset](https://img.shields.io/badge/asset-PNG-blue?style=flat-square)
![use](https://img.shields.io/badge/use-Open%20Graph%20%2B%20Twitter%20Cards-brightgreen?style=flat-square)
![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fcharts-orange?style=flat-square)
![discipline](https://img.shields.io/badge/discipline-provenance--first-6f42c1?style=flat-square)

> **TL;DR ✅**  
> This folder contains **pre-rendered PNG “share cards”** derived from KFM charts, intended for social link previews via **`og:image`** / **`twitter:image`** metadata.

---

## 📦 What this folder is (and why it exists)

KFM’s UI (`web/`) includes chart components and narratives (Story Nodes). In-app charts are interactive, but social platforms typically scrape **static images** for previews — so we keep a curated set of **Open Graph–friendly PNG exports** here. 🌾📈

---

## 🧭 Quick map of where this fits

```text
📁 web/
  ├─ 📁 components/        🧩 UI building blocks (charts live here)
  ├─ 📁 story_nodes/       📚 narrative content (markdown + config)
  └─ 📁 assets/
     └─ 📁 charts/
        └─ 📁 exports/
           └─ 📁 png/
              └─ 📁 og/
                 ├─ 📄 README.md              👈 you are here
                 ├─ 🖼️ kfm-og__*.png          ✅ share cards
                 └─ 🧾 kfm-og__*.og.json      (optional) provenance sidecars
```

---

## ✅ What belongs here

- 🖼️ **PNG share cards** for:
  - 📚 Story Node landing pages
  - 🗺️ Dataset / layer landing pages
  - 🔎 Focus Mode “answer pages” that have a canonical permalink
  - 🧾 Reports or dashboards that should render cleanly in a social preview

---

## 🚫 What does *not* belong here

- ❌ Raw data exports (CSV/GeoJSON/Parquet/etc.)
- ❌ Chart source code / React components
- ❌ “Random screenshots” that can’t be reproduced
- ❌ User uploads or sensitive/private imagery

> 🧠 **Rule of thumb:** This is for **marketing/preview visuals**, not for evidence storage. Evidence stays in the data/catalog/provenance layers.

---

## 📐 Sizing & format standards

| Variant 🎛️ | Filename suffix | Dimensions | When to use |
|---|---:|---:|---|
| Standard OG ✅ | `__1200x630` | 1200×630 | Default Open Graph preview |
| Retina OG ✨ | `__2400x1260` | 2400×1260 | Optional crisp preview (hi‑DPI) |
| Square fallback 🟦 | `__1080x1080` | 1080×1080 | Optional for platforms that crop to square |

**PNG guidance:**
- 🧊 Prefer **opaque PNG** unless transparency is needed.
- 📉 Keep **file sizes small** (aim ≤ ~600KB when possible).
- 🧹 Optimize before committing (see workflow below).

---

## 🏷️ Naming convention (stable + grep-friendly)

Use stable, predictable names so they can be referenced from meta tags and permalinks:

### ✅ Pattern
`kfm-og__<slug>__<variant>.png`

### ✅ Examples
- `kfm-og__drought-index__1200x630.png`
- `kfm-og__tornado-tracks__2400x1260.png`
- `kfm-og__story__prairie-fire__1200x630.png`

### Slug rules 🧩
- lowercase
- `kebab-case` *or* segmented with `__` for hierarchy
- no spaces
- no timestamps inside the slug (handle versioning separately)

---

## 🧾 Provenance sidecars (optional but strongly encouraged)

KFM is provenance-first. If an OG image is derived from a particular chart + dataset release, add a sibling sidecar:

`kfm-og__drought-index__1200x630.og.json`

Suggested schema:

```json
{
  "kind": "kfm.og-image",
  "chart_id": "drought-index",
  "slug": "drought-index",
  "variant": "1200x630",
  "data_release": "YYYY-MM",
  "sources": {
    "stac_item": "data/stac/items/…",
    "dcat_dataset": "data/catalog/dcat/…",
    "prov_bundle": "data/prov/…"
  },
  "generated_by": {
    "tool": "TBD (see Export workflow)",
    "git_commit": "abcdef1",
    "generated_at": "YYYY-MM-DDTHH:mm:ssZ"
  },
  "notes": "Short human-friendly context about what the image depicts."
}
```

> 🧩 If you can’t capture provenance yet, still keep the PNG name stable and leave a TODO in the PR.

---

## 🔗 How these PNGs are used (Open Graph + Twitter)

These exports are meant to be referenced in page `<head>` metadata, e.g.:

```html
<meta property="og:image" content="https://example.com/og/kfm-og__drought-index__1200x630.png" />
<meta name="twitter:image" content="https://example.com/og/kfm-og__drought-index__1200x630.png" />
```

**Implementation tip:** search the codebase for:
- `og:image`
- `twitter:image`
- `OpenGraph`
- `TwitterCard`

---

## 🛠️ Export workflow (recommended)

Preferred approach: **generate OG PNGs from chart components/config** so exports don’t drift from the UI.

1. 🧩 Identify the chart in `web/components/` (or the chart config driving it).
2. 📏 Render it in a deterministic viewport (ex: 1200×630).
3. 🖼️ Export to PNG into this folder using the naming convention above.
4. 🧾 (Optional) add `.og.json` provenance sidecar.
5. 🧹 Optimize the PNG (e.g., `pngquant`, `oxipng`, etc.).
6. ✅ Verify readability at thumbnail scale.

> 💡 **Note on formats:** In general, SVG is ideal for in-app charts (resolution independent), but **PNG is used here** because many social scrapers expect raster preview images.

---

## 🧠 Caching & versioning (avoid stale previews)

Social platforms can cache previews aggressively. Two common strategies:

- ✅ **Stable filename**, but bust caches on publish (e.g., CDN purge / query param).
- ✅ **Fingerprinted publish output** (content hash) while keeping a stable mapping from permalink → image URL.

If you adopt fingerprinting, keep the *source* exports here stable and let the build/publish step handle hashing.

---

## 🧪 QA checklist

Before committing new images:

- [ ] 📐 Dimensions match the filename variant
- [ ] 👀 Text is readable at thumbnail size
- [ ] 🔒 No sensitive/private info appears (names, exact protected sites, etc.)
- [ ] 🧹 Image is optimized (not multi‑MB)
- [ ] 🔗 Image is referenced by a canonical page/permalink
- [ ] 🧾 (Optional) `.og.json` sidecar added

---

## 🔒 Privacy & safety notes

OG images can be cached and redistributed by third parties. Avoid including:
- 👤 personal identifiers
- 🏠 private addresses / precise sensitive coordinates
- 🛑 “internal-only” layers or unpublished datasets

When in doubt: **use an abstracted/aggregated view** (binned counts, anonymized tiles, generalized geometries). ✅

---

## 🧭 Related docs (repo)

- 📘 `/docs/MASTER_GUIDE_v13.md` — repo layout & documentation rules
- 🏗️ `/docs/architecture/` — architecture + integration notes
- 📚 `/docs/reports/story_nodes/` — Story Node conventions (markdown + assets)

---
✨ If you add a new OG image, consider adding a tiny “why this exists” note in the PR description (what page uses it + what chart/dataset it represents).
