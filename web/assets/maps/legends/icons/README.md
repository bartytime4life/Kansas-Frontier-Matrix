# 🗺️ Legend Icons (Map Symbology)

![Scope](https://img.shields.io/badge/scope-map%20legend%20icons-4c1) ![Preferred](https://img.shields.io/badge/prefer-SVG-0aa) ![A11y](https://img.shields.io/badge/a11y-ARIA%20%2B%20semantic%20HTML-0a0) ![Design](https://img.shields.io/badge/design-readable%20at%2016%E2%80%9324px-blue)

> **Folder:** `web/assets/maps/legends/icons/`  
> **Goal:** Make legends instantly understandable (small, crisp, consistent symbols) ✅

---

## 📌 What lives here?

This directory holds **static icon assets** used by the **web map UI** for things like:

- 🧭 **Legend rows** (icon + label)
- 🗂️ **Layer list / catalog chips** (quick visual cue)
- 🧷 **Point-of-interest & event markers** (when we choose icon-based symbology)

KFM’s front-end is described as a **React-based web app** with map viewers that integrate **MapLibre GL JS (2D)** and **CesiumJS (3D)**, alongside common UI elements like **layer management**, **legends for map symbology**, and a **timeline slider**. These icons are part of the `assets/` static asset space.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧠 Principles (why this matters)

### 1) 🧾 Provenance-first (even for visuals)
KFM emphasizes that what users see should be traceable and trustworthy. Apply that mindset to icons too: **every icon should have clear authorship + license + source** so the UI remains auditable and shareable.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) ♿ Accessibility & clarity are non-negotiable
The front-end is described as following cartographic best practices including **readable legends**, **high-contrast modes**, and **ARIA/semantic HTML** support for screen readers. Icons must work with that: recognizable at small sizes, high-contrast friendly, and paired with accessible labels.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 3) ⚖️ License hygiene
KFM highlights careful licensing as a core practice to avoid conflicts and support adoption (schools/agencies) and collaboration. Don’t import “random icons” without recording license/terms.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗂️ Suggested folder layout

Keep things simple, but scalable:

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 legends/
        📁 icons/
          📄 README.md   👈 you are here
          🖼️ poi--fort.svg
          🖼️ infra--railroad.svg
          🖼️ env--river.svg
          🧾 icons.manifest.json   (recommended)
```

> If the project already uses a different structure, keep this README’s **rules** and adapt the **paths**.

---

## 🏷️ Naming conventions

### ✅ Filename rules
- **kebab-case**
- **category prefix** first (so sorting groups icons)
- **one concept per icon**
- **no spaces**
- include **variant** only when needed

**Pattern:**
```
<category>--<slug>[--<variant>].svg
```

**Examples:**
- `poi--fort.svg`
- `poi--town.svg`
- `event--battle.svg`
- `infra--railroad.svg`
- `hazard--tornado.svg`
- `land--prairie--outline.svg`

### 🧩 Category suggestions (common KFM layer themes)
- `poi` (points of interest)
- `event`
- `infra` (roads/rails/utilities)
- `env` (rivers, wetlands, ecoregions)
- `admin` (boundaries, jurisdictions)
- `land` (land cover / use)
- `hazard` (storms, drought, fire)

> **Tip:** If an icon is tightly bound to one dataset/layer, the slug can match the layer id/slug to reduce mapping glue.

---

## 🎨 Design rules for legend icons

Legend icons are typically displayed **small** (often ~16–24px). Design accordingly:

### ✅ Do
- Use **SVG** when possible (crisp scaling)
- Design on a **24×24 viewBox** (or 32×32 if the set already uses it)
- Use **simple silhouettes** (avoid tiny details)
- Prefer **monochrome** shapes; let the legend swatch/color system convey the data meaning
- Use `fill="currentColor"` / `stroke="currentColor"` when appropriate (theme-friendly)
- Keep **consistent stroke width** (e.g., 1.5–2.0) across the set
- Ensure the icon reads in:
  - 🌞 light mode
  - 🌚 dark mode
  - 🦾 high-contrast mode

### ❌ Avoid
- Hard-coded fill colors (unless the icon itself must encode meaning)
- Embedded raster images inside SVG
- Micro-text (text won’t survive small sizes)
- Overly complex shapes (legend ≠ illustration)

---

## 🧾 Provenance & licensing metadata (recommended)

Because KFM cares deeply about provenance and trust, store icon metadata in a **manifest**.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ `icons.manifest.json` (example)
```json
[
  {
    "id": "poi--fort",
    "file": "poi--fort.svg",
    "title": "Fort / Outpost",
    "category": "poi",
    "tags": ["history", "military"],
    "source": "in-house",
    "license": "PROJECT-LICENSE",
    "author": "KFM Team",
    "modified": "2026-01-15",
    "notes": "Designed for readability at 16px; uses currentColor."
  }
]
```

**Suggested fields:**
- `id` (stable reference used by code)
- `file` (must match actual filename)
- `title` / `description` (used for labels/alt text)
- `category` / `tags` (search + grouping)
- `source` (in-house / vendor / link)
- `license` (SPDX if possible)
- `author`
- `modified`
- `notes`

> 🔒 If an icon has external origins, **include the source URL + license text reference** in the manifest (or a companion `LICENSES/` doc in a higher folder).

---

## 🧩 Usage patterns (front-end)

KFM’s web app is described as a React SPA with a map viewer and UI panels like legends/layer lists.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 1) Import an SVG as an image URL (common bundlers)
```ts
// Example (varies by toolchain)
import fortIconUrl from "@/assets/maps/legends/icons/poi--fort.svg";

export function LegendRow() {
  return (
    <div className="legend-row">
      <img src={fortIconUrl} alt="Fort / Outpost" />
      <span>Fort / Outpost</span>
    </div>
  );
}
```

### 2) Keep icons semantic in the legend UI ♿
- Always include a **text label** next to the icon (don’t rely on the icon alone).
- Ensure the container is keyboard/screen-reader navigable (ARIA/semantic HTML).  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ Pull request checklist (icon changes)

Before merging new/updated icons:

- [ ] Filename follows `<category>--<slug>[--variant].svg`
- [ ] SVG includes a `viewBox` and scales cleanly
- [ ] Works at **16px** and **24px**
- [ ] Uses `currentColor` where appropriate (theme-friendly)
- [ ] No unnecessary metadata/hidden layers
- [ ] Manifest updated (`icons.manifest.json`) with provenance + license
- [ ] Checked in **light/dark/high-contrast** contexts
- [ ] Legend label/alt text present (a11y)

---

## 🧯 Troubleshooting

### “Icon looks blurry”
- Check it’s truly SVG (not an embedded bitmap).
- Ensure the SVG has an integer viewBox and aligns to pixel grid at common sizes.

### “Icon disappears in dark mode”
- Avoid hard-coded dark fills; prefer `currentColor` + theme-managed colors.

### “We don’t know the license”
- Don’t ship it. Track down the license/source or replace with an in-house icon.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔗 Related (mental map)

- 🗺️ `web/viewers/` — map viewers (2D/3D integration)  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🧩 `web/components/` — UI components (legend rows, layer panels, etc.)  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🎨 `web/assets/` — static assets like icons/images  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📚 Sources (project grounding)

- KFM front-end structure, map viewers, legends/timeline, and assets folder description.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM cartographic clarity + readable legends + high-contrast + ARIA/semantic HTML note.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM provenance-first and traceability emphasis.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM licensing-care and collaboration rationale.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)