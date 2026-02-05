# 🎛️ UI Image Assets (Web Client)

![Scope](https://img.shields.io/badge/scope-web%2Fui-informational)
![Preferred](https://img.shields.io/badge/prefer-SVG%20%7C%20WebP-success)
![Policy](https://img.shields.io/badge/policy-provenance--first-blueviolet)
![Performance](https://img.shields.io/badge/goal-fast%20loads%20%26%20crisp%20maps-brightgreen)

> [!IMPORTANT]
> This directory is for **UI-only imagery** (icons, controls, illustrations, brand marks).  
> Anything that represents **data** (rasters/tiles/COGs, screenshots used as evidence, etc.) should live in the *data/etl/catalog* world — not here. 🧭🗺️

---

## 📌 What this folder is for

**Path:** `web/src/assets/images/ui/`

This folder holds images that support the **user interface** of the Kansas Frontier Matrix web app:
- 🧭 Navigation + UI chrome (buttons, tabs, tool icons)
- 🗺️ Map UI assets (markers, cursors, legend icons, controls)
- 🧩 “Empty state” / onboarding illustrations
- 🏷️ Brand marks (logos, wordmarks) used *inside the UI*

The goal is simple: **crisp visuals + small payloads + traceable sources**. ✅

---

## ✅ What belongs here (and what doesn’t)

### ✅ Put these here
- `icons/*.svg` (toolbar icons, UI actions)
- `markers/*` (MapLibre marker images, cluster icons)
- `logos/*` (KFM logos used in UI shell)
- `illustrations/*` (onboarding, empty states)
- `patterns/*` (subtle UI textures/backgrounds — if necessary)

### 🚫 Don’t put these here
- ❌ Map tiles, imagery layers, COGs, PMTiles, basemaps  
- ❌ Dataset screenshots used as “evidence” in documentation
- ❌ Random downloads with unknown licenses
- ❌ UI screenshots (those should typically live in `/docs/` or a documentation assets folder)

> [!TIP]
> If an asset’s meaning is **“data on the map”** it needs a provenance trail that lives with datasets/catalogs.  
> If the asset’s meaning is **“UI decoration / interface affordance”** it belongs here. 🎚️

---

## 🗂️ Suggested structure

```text
web/src/assets/images/ui/
├─ 🧩 icons/
│  ├─ ui/          # generic UI icons (search, close, settings)
│  ├─ map/         # map-specific icons (layer, pin, measure)
│  └─ status/      # warnings, info, success, etc.
├─ 🗺️ markers/
│  ├─ pins/
│  ├─ clusters/
│  └─ sprites/
├─ 🏷️ logos/
├─ 🎨 illustrations/
├─ 🧵 patterns/
└─ 🧾 _manifest/
   └─ ui-assets.manifest.json
```

> [!NOTE]
> The `_manifest/` folder is recommended even if we don’t enforce it yet in CI. It’s the “map behind the map” idea… but for UI assets. 🧾✨

---

## 🧱 Formats we support

| Format | Use it for | Avoid it for | Notes |
|---|---|---|---|
| **SVG** ✅ | icons, simple illustrations, logos | photos | Small, scalable, theme-friendly |
| **WebP** ✅ | UI illustrations, non-transparent imagery | tiny icons | Great compression; keep originals if needed |
| **PNG** ✅ | transparency, crisp pixel art, map markers | photos | Use when SVG isn’t viable |
| **JPG/JPEG** | photos, large imagery without transparency | icons, text-heavy UI | Lossy compression; watch artifacts |
| **GIF** ⚠️ | rare: tiny UI animation | everything else | Prefer CSS/SVG/Lottie/video instead |

---

## 🏷️ Naming conventions

Keep names **predictable**, **sortable**, and **greppable**:

### ✅ Rules
- **kebab-case** only: `layer-toggle.svg`
- include **domain prefix** when useful: `map-pin-primary.png`
- include **state/variant**: `search-idle.svg`, `search-active.svg`
- include **theme** if needed: `logo-light.svg`, `logo-dark.svg`
- include **size only when it matters**: `marker-pin-24.png`, `marker-pin-48.png`

### ❌ Avoid
- `Final_FINAL2.png`
- `icon(1).svg`
- `LayerToggleNEW.svg`

---

## ♿ Accessibility (non-negotiable)

- ✅ **Don’t bake text into images** (hard to localize, not screen-reader friendly).
- ✅ Provide meaningful `alt` text for `<img>` usage.
- ✅ Decorative imagery should use empty alt: `alt=""` and be hidden from assistive tech when appropriate.
- ✅ Icons that convey meaning should have accessible labels (e.g., button aria-label).

---

## ⚡ Performance budgets

> [!TIP]
> UI assets should feel instant — especially around maps where the user is already loading tiles. 🗺️⚡

Suggested budgets (tune as we learn):
- 🧩 **Icons (SVG):** typically **< 5 KB** each
- 🗺️ **Markers (PNG/WebP):** **< 20 KB** each (prefer fewer variants)
- 🎨 **Illustrations:** target **< 150 KB** each (WebP preferred)
- 🧵 **Patterns/backgrounds:** **< 80 KB** — and only if actually needed

Also:
- strip metadata where possible (especially PNG/JPG)
- avoid shipping multiple near-duplicates (same shape, tiny changes)

---

## 🧾 Provenance & licensing

KFM is an evidence-first platform — that ethos applies to UI assets too.  
Every non-trivial UI image should be traceable:

### ✅ Minimum provenance requirements
- Source (who made it? where did it come from?)
- License (what can we legally do with it?)
- Attribution (if required)
- Notes (what it’s used for)

### 📄 Manifest (recommended)

Create/update: `web/src/assets/images/ui/_manifest/ui-assets.manifest.json`

Example entry:

```json
{
  "id": "map-pin-primary",
  "file": "markers/pins/map-pin-primary.png",
  "type": "marker",
  "source": "Designed in-house (KFM UI kit)",
  "license": "Proprietary (project-owned)",
  "attribution": null,
  "created_at": "2026-02-05",
  "notes": "Default MapLibre marker for point features."
}
```

> [!WARNING]
> If you can’t answer “where did this come from and under what license?”, **don’t add it**. 🚫

---

## 🔁 Asset lifecycle

```mermaid
flowchart LR
  A[🎨 Design / Create] --> B[📦 Export (SVG/PNG/WebP)]
  B --> C[🧽 Optimize (svgo/sharp/etc.)]
  C --> D[🧾 Add/Update Manifest Entry]
  D --> E[🧩 Use in UI (React/MapLibre)]
  E --> F[🧪 Verify (visual + perf)]
```

---

## 🧩 How to use assets in code

### React/TypeScript import (typical bundler behavior)

```tsx
import searchIcon from "@/assets/images/ui/icons/ui/search.svg";

export function SearchButton() {
  return (
    <button type="button" aria-label="Search">
      <img src={searchIcon} alt="" />
    </button>
  );
}
```

### Inline SVG (preferred for theming)
If your toolchain supports SVGR (or similar), inline SVG icons allow CSS-driven color + sizing.

```tsx
// Example only — actual import syntax depends on bundler config.
import { ReactComponent as LayersIcon } from "@/assets/images/ui/icons/map/layers.svg";

export function LayersToggle() {
  return (
    <button type="button" aria-label="Layers">
      <LayersIcon />
    </button>
  );
}
```

### MapLibre marker usage (conceptual)

```ts
import pinPng from "@/assets/images/ui/markers/pins/map-pin-primary.png";

// Example helper
async function loadImage(url: string): Promise<HTMLImageElement> {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = url;
  });
}

// In map setup:
const img = await loadImage(pinPng);
map.addImage("kfm-pin", img, { pixelRatio: 2 });
```

> [!NOTE]
> Map markers should be designed to stay legible at multiple zoom levels, and avoid tiny details that shimmer. 🗺️🔍

---

## ✅ Add-a-new-asset checklist

- [ ] Pick the right format (**SVG first** for icons)
- [ ] Name it using the conventions above
- [ ] Optimize it (size + metadata)
- [ ] Ensure it works on **light + dark** backgrounds (if applicable)
- [ ] Add/update the manifest entry (source + license)
- [ ] Wire it into UI with accessible labeling
- [ ] Confirm it doesn’t regress load performance

---

## 🔎 Quick FAQ

<details>
  <summary><strong>Why are we so strict about provenance for “just UI icons”?</strong></summary>

Because KFM’s credibility depends on traceability. If we can’t govern small assets, we won’t govern big ones.  
Also, licensing mistakes often happen in “small” places (icons, illustrations). 🧾🛡️

</details>

<details>
  <summary><strong>Where do screenshots for docs go?</strong></summary>

Prefer a documentation assets folder (e.g., `docs/assets/`), not the UI runtime bundle.  
UI bundles should ship only what the app needs at runtime. 📚➡️🧩

</details>

---

## 📚 References (project-informed)

These sources shape our conventions around **web UI consistency**, **format selection**, **clean separation of concerns**, and **KFM’s provenance-first philosophy**:

- *Professional Web Design: Techniques and Templates (5e)* — image formats, compression awareness, and practical web design workflow.  [oai_citation:0‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- *Learn to Code HTML & CSS* — semantic mindset, separation of structure vs. presentation, and maintainable front-end practices.  [oai_citation:1‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- *Kansas Frontier Matrix – Comprehensive System Documentation* — provenance-first system design and UI/architecture context (React + Map UI focus).  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- *Node.js (intro text)* — reinforces the JS ecosystem/tooling mindset that typically underpins the web build pipeline.  [oai_citation:3‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
