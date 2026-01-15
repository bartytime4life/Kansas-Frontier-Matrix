# 📊 PNG Chart Exports

![format](https://img.shields.io/badge/format-PNG-blue)
![scope](https://img.shields.io/badge/scope-web%2Fui-brightgreen)
![folder](https://img.shields.io/badge/path-web%2Fassets%2Fcharts%2Fexports%2Fpng-informational)
![tip](https://img.shields.io/badge/tip-prefer%20SVG%20when%20possible-6f42c1)

> **Location:** `web/assets/charts/exports/png/`  
> **Purpose:** A curated, source-controlled home for **static PNG snapshots** of charts used by the Web UI (previews, thumbnails, documentation imagery, and other raster-only contexts).

---

## 🧭 What this folder is for

This directory holds **PNG (bitmap) exports** of charts that are **owned by the frontend** and reused across the UI.

Common use cases:
- 🧩 **UI fallbacks** (e.g., a lightweight preview image while an interactive chart loads)
- 🖼️ **Thumbnails** (dataset cards, gallery previews, layer/tool previews)
- 🧾 **Docs & screenshots** (stable, consistent images for guides and README examples)
- 🔗 **Share images** (OpenGraph/Twitter cards where raster outputs are expected)
- 📦 **Offline packs** (when shipping a static preview is more reliable than rendering at runtime)

> [!NOTE]
> KFM’s UI includes charts/mini-graphs in context panels (pop-ups, sidebars, previews). PNG exports are useful when those visuals need to exist **outside** the live rendering pipeline (docs, previews, social cards, offline, etc.).

---

## ✅ What belongs here

- ✅ **Stable, reusable** chart images (not one-off story images)
- ✅ PNGs that represent **UI behavior** (how a chart looks) rather than being the canonical evidence artifact
- ✅ Non-sensitive visuals that are safe to commit to the repo
- ✅ Images that are versioned intentionally (you can diff/track changes PR-to-PR)

---

## 🚫 What does *not* belong here

> [!IMPORTANT]
> If it’s **data/evidence**, it should NOT live in `web/assets/**`.

- ❌ **User-generated runtime exports** (downloads created by users in the app)
  - These should be generated on-demand and saved to the user’s device or a temporary server location.
- ❌ **Evidence artifacts / dataset-derived outputs**
  - Those belong in `data/processed/**` and should be registered through the governed catalog/provenance flow (STAC/DCAT/PROV), then referenced by the UI.
- ❌ **Story-specific images**
  - Preferred: store alongside the story node under `docs/reports/story_nodes/**/assets/`
  - (If you’re working in a legacy layout where story content lives under `web/story_nodes/`, keep story-specific assets with that story—not here.)

---

## 🟣 PNG vs SVG (quick rule)

> [!TIP]
> If the graphic is primarily lines/text/shapes → **SVG** is usually better (crisp, smaller, scales cleanly).  
> If the graphic is a screenshot/raster composite or needs pixel-perfect capture → **PNG** is appropriate.

Use **PNG** when:
- 🗺️ The “chart” includes raster basemaps, imagery, or dense textures
- 📸 You need a **snapshot** of the exact rendered UI state
- 🔒 You must match an exact pixel output for docs/social/press
- 🧪 You’re doing visual regression snapshots (golden images)

---

## 🗂️ Recommended structure

You can keep PNGs flat, but subfolders make long-term maintenance easier:

```text
web/
└── assets/
    └── charts/
        └── exports/
            └── png/
                ├── README.md
                ├── 📁 sparkline/
                │   ├── sparkline--7d--320x80@1x.png
                │   ├── sparkline--7d--320x80@2x.png
                │   └── sparkline--7d--320x80.meta.json
                ├── 📁 timeseries/
                │   ├── rainfall--monthly--640x360@1x.png
                │   ├── rainfall--monthly--640x360@2x.png
                │   └── rainfall--monthly--640x360.meta.json
                └── 📁 og/
                    ├── dataset-preview--1200x630@1x.png
                    └── dataset-preview--1200x630.meta.json
```

---

## 🏷️ Naming convention

Use a consistent, grep-friendly naming scheme:

```text
<chart_id>--<variant>--<width>x<height>@<scale>x.png
```

**Rules**
- ✅ `chart_id` and `variant` should be **kebab-case**
- ✅ Always include pixel dimensions (`WxH`)
- ✅ Include scale factor (`@1x`, `@2x`) when you generate retina variants
- ✅ Prefer explicit sizes over vague names like `final.png` or `new.png`

**Examples**
- `sparkline--10y--320x80@2x.png`
- `rainfall--monthly--640x360@1x.png`
- `layer-legend--compact--480x320@1x.png`
- `dataset-preview--1200x630@1x.png` (OG / social share)

---

## 🧾 Add a metadata sidecar (recommended)

When a PNG is anything more than a pure UI icon/screenshot, include a `.meta.json` next to it:

**Example:** `rainfall--monthly--640x360.meta.json`
```json
{
  "title": "Rainfall — Monthly Time Series (Preview)",
  "alt": "Line chart preview of monthly rainfall over time.",
  "chart_id": "rainfall",
  "variant": "monthly",
  "size": { "width": 640, "height": 360, "scale": 1 },
  "owner": {
    "area": "web",
    "component_hint": "components/charts/TimeSeriesChart"
  },
  "data_lineage": {
    "type": "ui-preview",
    "note": "If this image is derived from governed data, reference the catalog/prov identifiers here."
  },
  "generated": {
    "method": "script-or-manual",
    "created_at": "YYYY-MM-DD",
    "source_commit": "git-sha-here"
  }
}
```

> [!NOTE]
> The goal isn’t bureaucracy—it’s to keep exports explainable and maintainable (especially when the image is derived from data or appears in public-facing materials).

---

## 🧼 Quality & performance checklist

- 🧠 **Export at the smallest size that meets the use case**
- 📱 Provide `@2x` variants **only** when they are actually used
- 🗜️ Run PNG optimization (lossless or near-lossless)
  - Example tools: `oxipng`, `pngquant`, `zopfli`-style optimizers
- 🌈 Avoid unnecessary transparency (it increases file size in many cases)
- 🔤 Ensure labels remain readable at target sizes (don’t shrink text into mush)

---

## ♿ Accessibility reminder

- Always provide **alt text** at the usage site (React component, markdown, etc.).
- The `.meta.json` can store a canonical `alt`, but code/docs should still pass it explicitly.

---

## 🔒 Governance & safety (non-negotiables)

- 🧭 **No sensitive or restricted imagery** in this folder.
- 🧼 Any chart based on sensitive sources must be **redacted/generalized** before becoming an export.
- 🧾 If the image is used to support a narrative claim, it must point back to governed evidence (catalog/provenance), not replace it.

---

## ✅ PR checklist (fast)

Before merging PNG exports:
- [ ] File name follows the convention (`id--variant--WxH@Nx.png`)
- [ ] File size is reasonable + optimized
- [ ] `.meta.json` exists when needed
- [ ] Not duplicating story-node assets that belong with a story
- [ ] Not storing “evidence artifacts” that belong in `data/processed/**`
- [ ] No sensitive/restricted content included

---

## 🔗 Related places

- 🧩 **Interactive charts live in UI code:** `web/components/**`
- 🧱 **General static UI assets:** `web/assets/**`
- 📚 **Story Node assets (preferred):** `docs/reports/story_nodes/**/assets/`
- 🧪 **Evidence artifacts / derived data:** `data/processed/**` (then referenced via catalogs)

---

🧷 *If you’re unsure whether an image is “UI asset” vs “evidence artifact”: default to evidence-first and keep it out of `web/assets/` until it’s properly cataloged.*
