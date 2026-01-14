# ✅ Status Icons — `web/assets/icons/status/`

![Format](https://img.shields.io/badge/format-SVG%20preferred-0b7285) ![Theming](https://img.shields.io/badge/theming-currentColor-1c7ed6) ![A11y](https://img.shields.io/badge/a11y-WAI--ARIA%20friendly-2f9e44) ![Scope](https://img.shields.io/badge/scope-KFM%20Web%20UI-f03e3e)

Small, consistent, **semantic** status glyphs used across the Kansas Frontier Matrix web UI (layer catalog, search results, map overlays, story panels, system banners, etc.). 🗺️🧭

---

## 📦 Folder

```text
📁 web/
  📁 assets/
    📁 icons/
      📁 status/
        📄 README.md   ✅ you are here
        🧩 *.svg       status icons (recommended)
        🧱 defs.svg    optional sprite sheet for <use> (recommended for caching)
        🖼️ *.png       optional raster fallbacks (MapLibre/Cesium/etc.)
```

> [!NOTE]
> This folder is **only** for *status* icons (state, health, availability, provenance, review-needed, etc.).
> Brand marks, large illustrations, and map-specific pictograms belong elsewhere. 🧠

---

## 🧭 What counts as a “status icon”?

A status icon communicates **state** (not identity):

- ✅ success / ready / valid  
- ⚠️ warning / degraded / needs review  
- ❌ error / failed / invalid  
- ⏳ queued / pending / loading  
- 🔄 syncing / recalculating / streaming  
- 🔒 locked / restricted  
- 🌐 online / offline  

In KFM, these show up in UI patterns like:
- dataset + layer toggles and load states 🗺️  
- processing / ingestion pipelines and job states 🧵  
- provenance + citation completeness (source-backed vs. “needs citation”) 🧾  
- human review flows (draft → review → published) 🧑‍⚖️  

---

## 🧱 Design principles (project-wide)

### 1) Semantic names = “stable identifiers” 🪪
Use **meaningful-but-stable** status tokens and keep them consistent over time.

✅ Good (semantic, stable):
- `success.svg`
- `warning.svg`
- `needs-review.svg`
- `unsourced.svg`

🚫 Avoid (presentation-coded / unstable):
- `green-check-16.svg`
- `warning-yellow.svg`
- `error-red-filled.svg`

> [!TIP]
> Treat the **token** as the API. Icons are just a rendering of that token.

### 2) “One fact, one place” mapping 🗂️
Maintain a **single canonical map** from status token → icon (and label).
This prevents drift across components (“warning” showing different glyphs in different screens).

Example (suggested):  
- `web/components/StatusIcon/` holds the component  
- `web/components/StatusIcon/statusIconMap.ts` holds the mapping ✅

### 3) Accessible by default ♿
- Don’t rely on color alone; shape must communicate the difference.
- If the icon is **decorative**, hide it from assistive tech.
- If the icon conveys **meaning**, provide an accessible label (or pair it with visible text).

---

## 📐 Icon spec (recommended defaults)

### ✅ File format
- **Primary:** SVG (`.svg`) — crisp at any scale, small payload.
- **Fallbacks:** PNG (`.png`) only when required by a rendering pipeline (e.g., map engines or texture atlases).

### ✅ Geometry + sizing
- **`viewBox="0 0 24 24"`** (standardized)
- Design to read at **16px** (table rows) and **20–24px** (toolbars).
- Favor simple silhouettes; avoid tiny interior details.

### ✅ Theming
Prefer **`currentColor`** so icons inherit UI theme colors automatically (light/dark/high-contrast).

**Rule of thumb:**
- outline set → `stroke="currentColor"` + `fill="none"`
- filled set → `fill="currentColor"`

### ✅ Two-tone support (optional)
If you need a subtle secondary tone, use a second path that inherits `currentColor` via `color` while the primary uses `fill`.  
(Keep it rare — two-tone is for emphasis, not decoration.)

---

## 🧩 Canonical status tokens

> [!IMPORTANT]
> These tokens are the “public API” for statuses. Add new tokens carefully (see the checklist below).

### Core operational states
| Token | Meaning | Typical UI placements |
|---|---|---|
| `unknown` | state can’t be determined | empty metadata, disconnected, not-yet-loaded |
| `pending` | queued / waiting | jobs, ingestion queues |
| `loading` | actively fetching | layer list, story step loads |
| `running` | actively processing | analysis, transforms, exports |
| `success` | completed OK | jobs, validations, ready layers |
| `warning` | completed with concerns | partial data, stale cache, degraded quality |
| `error` | failed | fetch failures, pipeline errors |

### Data governance / provenance (KFM-flavored) 🧾
| Token | Meaning | Suggested companion text |
|---|---|---|
| `sourced` | has a verified source reference | “Source attached” |
| `unsourced` | missing source reference | “Needs citation” |
| `needs-review` | human review required | “Review required” |
| `verified` | reviewed / approved | “Verified” |

### Security / access
| Token | Meaning |
|---|---|
| `locked` | restricted or permission-gated |
| `unlocked` | accessible |

---

## 🧰 Usage patterns

### ✅ React usage (recommended)
Keep usage consistent via a single component.

```tsx
// Example only — adapt to your project conventions.
type StatusToken =
  | "unknown"
  | "pending"
  | "loading"
  | "running"
  | "success"
  | "warning"
  | "error"
  | "sourced"
  | "unsourced"
  | "needs-review"
  | "verified"
  | "locked"
  | "unlocked";

export function StatusIcon({
  status,
  label,
  decorative = false,
}: {
  status: StatusToken;
  label?: string;
  decorative?: boolean;
}) {
  const ariaProps = decorative
    ? { "aria-hidden": true }
    : { role: "img" as const, "aria-label": label ?? status };

  return (
    <svg className={`StatusIcon StatusIcon--${status}`} {...ariaProps}>
      <use href={`/assets/icons/status/defs.svg#${status}`} />
    </svg>
  );
}
```

### 🧱 External SVG sprite (`defs.svg`)
Using an external sprite enables browser caching and avoids repeating large inline SVG blocks.

```html
<svg class="StatusIcon StatusIcon--warning" aria-label="Warning" role="img">
  <use href="/assets/icons/status/defs.svg#warning"></use>
</svg>
```

### 🎨 CSS (sizing + theming)
```css
.StatusIcon {
  inline-size: 1em; /* scales with text size */
  block-size: 1em;
  vertical-align: -0.125em;
  stroke: currentColor;
  fill: none;
}

.StatusIcon--success { color: var(--status-success); }
.StatusIcon--warning { color: var(--status-warning); }
.StatusIcon--error   { color: var(--status-error);   }
```

### 🗺️ MapLibre / Cesium / WebGL notes
Some renderers want raster images or texture atlases.

- If a map engine requires bitmap icons, export **PNG 1x + 2x** (or bake a texture atlas).
- Keep the *semantic token* the same (`warning`, `error`, etc.) even if the underlying asset differs.

> [!TIP]
> “Same status token everywhere” is more important than “same implementation everywhere.”

---

## ➕ Adding a new status icon (checklist) ✅

### 1) Define the token first 🪪
- [ ] Name is semantic and stable (no color/size/context encoded)
- [ ] Not duplicating an existing concept
- [ ] Works across the UI (layer list, panels, notifications)

### 2) Design the glyph 🎨
- [ ] Reads at 16px
- [ ] Distinguishable in monochrome
- [ ] Uses `currentColor` (unless intentionally special)

### 3) Ship it 🔧
- [ ] Add `*.svg` to this folder
- [ ] Update `defs.svg` (if used)
- [ ] Update the canonical map (single source of truth)
- [ ] Add/adjust tests (snapshot + a11y)

### 4) Document it 📝
- [ ] Add the token to the tables above (and describe intended meaning)

---

## 🧪 QA checklist (quick) 🔍

- [ ] Visible and recognizable on **light** and **dark** themes
- [ ] Works with **high contrast** mode
- [ ] Not relying solely on color
- [ ] Screen-reader behavior matches intent (decorative vs informative)
- [ ] No layout shift when icons load (reserve size)

---

## 📚 References used to shape these conventions

<details>
  <summary><strong>📖 Core KFM docs</strong></summary>

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (front-end structure, `assets/` purpose, responsive + accessible UI expectations)
- **Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design** (provenance-first UI + catalog philosophy)

</details>

<details>
  <summary><strong>🧩 UI / SVG / Accessibility</strong></summary>

- **Responsive Web Design with HTML5 and CSS3** (SVG symbol reuse, external `defs.svg`, `currentColor`)
- **(GoalKicker) Web / Programming Books collections** (WAI-ARIA + semantic HTML practices)

</details>

<details>
  <summary><strong>⚙️ Scalability / Architecture mindset</strong></summary>

- **Flexible Software Design** (stable identifiers + consistent standards + designing for longevity)
- **Scalable Data Management for Future Hardware** (“one fact, one place” style consolidation — applied here as a single canonical status→icon map)
- **Database Performance at Scale** (performance mindset applied to assets: cache, reduce duplication, predictable delivery)

</details>

<details>
  <summary><strong>🗺️ GIS / Mapping / 3D context</strong></summary>

- **Making Maps: A Visual Guide to Map Design for GIS**
- **Mobile Mapping: Space, Cartography and the Digital**
- **Python Geospatial Analysis Cookbook**
- **Archaeological 3D GIS**
- **WebGL Programming Guide**
- **Spectral Geometry of Graphs** (graph/network thinking → status semantics for connectivity & topology)
- **Cloud-Based Remote Sensing with Google Earth Engine** (job/task lifecycle cues)

</details>

<details>
  <summary><strong>🧠 Modeling / ML / Statistics context</strong></summary>

- **Scientific Modeling and Simulation — NASA-Grade Guide** (simulation lifecycle: running/converging/diverging)
- **Understanding Statistics & Experimental Design**
- **Regression Analysis with Python** (+ slides)
- **Graphical Data Analysis with R**
- **Think Bayes**
- **Generalized Topology Optimization for Structural Design** (optimization lifecycle cues)

</details>

<details>
  <summary><strong>🧭 Governance / Ethics / Security context</strong></summary>

- **Introduction to Digital Humanism** (human-centered clarity in UI signals)
- **On the path to AI Law’s prophecies…** (transparency + accountability cues)
- **Ethical Hacking and Countermeasures**
- **Gray Hat Python**
- **Compressed Image File Formats** (format tradeoffs; when PNG/GIF/JPEG are appropriate)

</details>

---

### ✅ If you only remember one thing…
**Treat status tokens as a stable contract** and keep a **single canonical mapping** from token → icon everywhere in the UI. 🧩🔒✅
