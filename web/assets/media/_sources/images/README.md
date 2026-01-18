# 🖼️ Image Sources (`web/assets/media/_sources/images/`)

![Provenance-First](https://img.shields.io/badge/Provenance-First-2ea44f) ![License-Aware](https://img.shields.io/badge/License-Aware-1f6feb) ![Web-Performance](https://img.shields.io/badge/Web-Performance-f59e0b) ![A11y](https://img.shields.io/badge/A11y-Considered-8b5cf6)

> [!IMPORTANT]
> **If an image appears anywhere in the KFM UI (or can influence a narrative), it must be traceable to a source and its processing steps.**  
> No “mystery assets” ✅

---

## 🎯 Purpose

This folder is the **single source of truth for “master” image assets** used by the Kansas Frontier Matrix (KFM) web experience:
- 🧩 UI icons & symbols
- 🏷️ Logos / brand assets
- 🗺️ Small illustrative maps (not GIS layers)
- 🎬 Story Node imagery (figures, diagrams, thumbnails)
- 🧪 Mockups & design comps used to produce final exports

Think of this folder as the **editable studio**. The site should typically **serve optimized exports** from the “published” media location (often `web/assets/media/images/`), not from `_sources/`.

---

## ✅ What goes here (and what does not)

### ✅ Goes here
- Editable or master-quality sources:
  - `*.svg`, `*.png`, `*.jpg`, `*.tif` (small), `*.psd`, `*.ai`, `*.xcf`
- Original exports from design tools (Figma / Illustrator / Inkscape / Photoshop)
- “Pre-optimization” images (before resizing/compression)

### ❌ Does **not** go here
- 🚫 **Geospatial raster layers** (COGs, MBTiles, tilesets) used as map layers  
  Those belong in the data pipeline / catalogs (and should be tracked like datasets).
- 🚫 Anything without provenance or licensing information
- 🚫 “Random screenshots” without a reason / usage context

> [!NOTE]
> **Rule of thumb:**  
> If it’s a *data layer* → it belongs with *data contracts & catalogs*.  
> If it’s *UI/story media* → it belongs here with a **media sidecar contract**.

---

## 🧱 Recommended folder layout

Use folders to keep intent obvious (create new ones when needed):

```text
web/assets/media/_sources/images/
├─ 🎛️ ui/               # UI illustrations, component art, onboarding visuals (editable masters if possible)
├─ 🧷 icons/             # Icon sources (SVG symbols, map UI glyphs) before any sprite/build steps
├─ 🏷️ logos/             # KFM + partner branding source files (tightly governed; keep variants organized)
├─ 📚 story/              # Story Node source imagery (figures, photos, diagrams) + editing originals
├─ 🗺️ maps/               # Small illustrative/non-GIS static maps (for docs/story; not tile sources)
├─ 📸 screenshots/        # Annotated/release screenshots (rare; keep minimal, redacted, dated)
└─ 📦 third-party/        # External image sources (MUST include license + attribution + provenance notes)
```

---

## 🏷️ Naming conventions (keep it boring, keep it searchable)

### ✅ Do
- **kebab-case** only: `kfm-logo-stacked.svg`
- Prefer semantic names over “final-final”: `layer-panel-empty-state.png`
- Include a scope prefix when helpful:
  - `ui-…`, `icon-…`, `story-…`, `map-…`

### ❌ Don’t
- Spaces: `My Image.png`
- Mystery names: `asdf.png`, `final2.png`
- Unclear duplicates: `logo.png` in five places

### Examples
- `icons/icon-timeline.svg`
- `logos/kfm-logo-horizontal.svg`
- `story/bleeding-kansas/figure-border-war-timeline.png`
- `ui/empty-states/empty-state-no-results.png`

---

## 🧾 Provenance & licensing (required)

Every image in this folder must have a **sidecar metadata file** that captures:
- where it came from
- what license governs it
- how we transformed it
- how to attribute it (if required)

### Sidecar filename rule
For an asset:
- `my-asset.svg`

Add:
- `my-asset.meta.json`

> [!TIP]
> If the image is generated internally (100% original), the source can be `"internal"` — but still document author + creation date.

---

## 🧩 `*.meta.json` template

<details>
<summary><strong>📄 Minimal Media Contract (copy/paste)</strong></summary>

```json
{
  "id": "kfm__icons__timeline",
  "title": "Timeline Icon",
  "description": "Icon used for timeline controls in the KFM web UI.",
  "type": "image",
  "usage": [
    "web-ui",
    "map-controls"
  ],
  "source": {
    "kind": "internal",
    "source_url": null,
    "creator": "KFM Contributors",
    "issued": "2026-01-17",
    "notes": "Designed in Inkscape from scratch."
  },
  "license": {
    "name": "CC0-1.0",
    "url": "https://creativecommons.org/publicdomain/zero/1.0/"
  },
  "attribution": {
    "required": false,
    "text": null
  },
  "processing": [
    {
      "step": "export",
      "tool": "Inkscape",
      "notes": "Exported as optimized SVG."
    }
  ],
  "integrity": {
    "sha256": null
  }
}
```
</details>

### Required fields (non-negotiable)
- `id`
- `title`
- `source.kind`
- `license.name`
- `processing[]` (even if it’s just one “created” or “export” step)

---

## 🧪 Exports & optimization (how to ship to the site)

### 🧠 Principle
- `_sources/` is for **masters**
- published media is for **fast loading**

### Recommended output formats
| Use case | Preferred | Acceptable | Avoid |
|---|---|---|---|
| Icons / symbols | `SVG` | `PNG` (if necessary) | JPG |
| Photos | `WebP` / `AVIF` | JPG | PNG (huge) |
| UI screenshots | PNG | WebP | JPG (if text-heavy) |
| Illustrations | SVG | PNG | Huge TIFFs |

> [!NOTE]
> **Performance matters:** minimize page weight and compress images aggressively *without breaking readability*. 📉

### Responsive images (when an image is shown in content)
If an image will be displayed at multiple sizes (desktop/tablet/mobile), export width variants like:
- `320w`, `640w`, `1024w`, `1440w`

…and use `srcset`/`picture` in the web layer.

---

## ♿ Accessibility & UX rules

- ✅ Always provide meaningful **alt text** (or mark decorative images as decorative)
- ✅ Avoid embedding critical text in rasters (prefer HTML/SVG text)
- ✅ Ensure icons have sufficient contrast in both light/dark themes
- ✅ Don’t encode meaning with color alone (especially in legends/diagrams)

---

## 🔒 Privacy & safety (yes, even for images)

- Strip EXIF metadata for photos/screenshots when it could contain:
  - GPS location
  - device info
  - timestamps that leak sensitive workflow
- Don’t add images that reveal private individuals, private addresses, or sensitive infrastructure.

---

## ✅ PR checklist (images)

- [ ] Asset added to `web/assets/media/_sources/images/...`
- [ ] `*.meta.json` sidecar added and complete (source + license included)
- [ ] Any required attribution text is present
- [ ] Exports are optimized and referenced correctly (don’t import `_sources/` into runtime unless intentional)
- [ ] Visual QA done in relevant UI surface (map UI, Story Node, etc.)
- [ ] File size is reasonable (no accidental 20MB PNGs 🫠)

---

## 🧭 Quick examples

### Example: third-party image
```text
third-party/
  usgs/
    usgs-historical-topo-sample.png
    usgs-historical-topo-sample.meta.json
```

### Example: story node figure set
```text
story/
  dust-bowl/
    figure-migration-flow.png
    figure-migration-flow.meta.json
    figure-migration-flow@2x.png
    figure-migration-flow@2x.meta.json
```

---

## 🧷 Related conventions in KFM

KFM treats metadata and lineage as first-class. The same mindset applies here:
- **traceable sources**
- **explicit licensing**
- **documented processing**
- **no undocumented “mystery” content**

If you need to break a rule, document the exception in the sidecar metadata and in the PR description. ✅
