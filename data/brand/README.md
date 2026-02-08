# 🌾 Kansas Frontier Matrix (KFM) — Brand & Data‑Viz System  
<sub>📁 `data/brand/` • One visual language across UI, maps, and exported artifacts</sub>

![scope](https://img.shields.io/badge/scope-data%2Fbrand-0b7285) ![design-tokens](https://img.shields.io/badge/design-tokens-yes-1f2937) ![maps](https://img.shields.io/badge/maps-MapLibre%20%2B%20Cesium-2563eb) ![principles](https://img.shields.io/badge/principles-FAIR%20%2B%20CARE-7c3aed) ![focus-mode](https://img.shields.io/badge/UX-evidence--backed-16a34a)

> 🎛️ This folder is the **single source of truth** for KFM’s visual identity: **themes**, **design tokens**, **map styles**, **icons**, and **data‑viz patterns**.  
> KFM itself is built as an *evidence-first geospatial knowledge hub*—so the brand must reinforce clarity, trust, and provenance in every pixel. :contentReference[oaicite:0]{index=0}

---

## ✨ What “brand” means in KFM (not just logos)
KFM’s UI aims to support exploration *without losing trust*: we **show sources**, **limit clutter (progressive disclosure)**, and stay **consistent** across interactions. :contentReference[oaicite:1]{index=1}  
So “brand” here includes:

- 🎨 **Theme + tokens** (colors, typography, spacing, elevation, motion)
- 🗺️ **Cartographic styling** (basemaps, overlays, legends, label rules)
- 📊 **Chart and table patterns** (scales, comparisons, uncertainty cues)
- 🧾 **Provenance UI** (citation chips, evidence panels, “map behind the map”)
- 🧭 **Voice + labeling rules** (neutral, precise, respectful; no “mystery meat”)

---

## 🧭 Principles (brand rules that come from the system)
These are non-negotiables because they follow KFM’s platform goals: provenance-first, auditable, human-centered exploration. :contentReference[oaicite:2]{index=2}

### 1) Evidence-first visuals 🧾
If a UI surface makes a claim, it must provide a path to evidence (citations → sources → metadata → raw artifacts).  
This matches Focus Mode’s expectation that responses are **evidence-backed** and cite sources directly. :contentReference[oaicite:3]{index=3}

### 2) Progressive disclosure 🪟
Default views should be calm and legible; details appear on demand. :contentReference[oaicite:4]{index=4}

### 3) Tokenized + themeable 🎛️
Theming is a first-class feature: implement via **CSS variables / design tokens** (colors, fonts) and apply a theme class on the `<body>` (e.g., `.theme-dark`). :contentReference[oaicite:5]{index=5}

### 4) Accessibility is baseline ♿
Theme choices must support readability and contrast—especially because KFM is map-heavy and information-dense. (Use the “quality gates” below.)

### 5) FAIR + CARE (community-aware data storytelling) 🤝
We keep data discoverable and reusable **without ignoring community rights**—including Indigenous data sovereignty considerations, provenance, and authority labeling. :contentReference[oaicite:6]{index=6}

---

## 📦 Recommended folder layout
> This is the target layout for `data/brand/`. If some folders don’t exist yet, treat them as TODO scaffolding.

```text
data/brand/
├─ README.md                   # ← you are here 🧭
├─ tokens/ 🎛️
│  ├─ tokens.json              # source-of-truth tokens (design + map)
│  ├─ tokens.schema.json       # validation schema (optional but recommended)
│  ├─ tokens.css               # generated CSS variables
│  ├─ tokens.ts                # generated TS tokens for UI
│  └─ tokens.map.json          # generated map token bundle (line widths, label sizes)
├─ themes/ 🌗
│  ├─ theme-light.css
│  ├─ theme-dark.css
│  └─ theme-high-contrast.css
├─ logos/ 🧩
│  ├─ kfm-mark.svg
│  ├─ kfm-wordmark.svg
│  └─ usage.md
├─ icons/ 🧷
│  ├─ sprite.svg               # map/icon sprite (if using)
│  ├─ sprite.json
│  └─ attribution.md
├─ maps/ 🗺️
│  ├─ style-basemap-light.json
│  ├─ style-basemap-dark.json
│  ├─ style-overlays.json
│  └─ cartography-guide.md
├─ viz/ 📊
│  ├─ chart-guidelines.md
│  ├─ legend-patterns.md
│  └─ timeline-patterns.md
└─ exports/ 🖨️
   ├─ svg/                     # static exports for reports
   ├─ png/
   └─ pdf/
```

---

## 🚀 Quick start (developer + designer)
### 1) Use theme + tokens in the UI
KFM theming should be done through tokens/CSS variables and theme classes. :contentReference[oaicite:7]{index=7}

```css
/* Example pattern (generated) */
:root {
  --kfm-color-bg: #ffffff;
  --kfm-color-fg: #0b1220;
  --kfm-font-sans: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  --kfm-space-3: 12px;
}

/* Theme switch (handwritten OR generated) */
body.theme-dark {
  --kfm-color-bg: #0b1220;
  --kfm-color-fg: #e5e7eb;
}
```

### 2) Use tokens in MapLibre styles (2D)
KFM’s stack uses MapLibre GL JS for vector maps. :contentReference[oaicite:8]{index=8}

```json
{
  "id": "historic-trails",
  "type": "line",
  "source": "kfm",
  "paint": {
    "line-width": ["get", "kfm_line_width_md"],
    "line-dasharray": [2, 2]
  }
}
```

### 3) Keep fonts minimal (performance + consistency)
Loading many fonts can increase load time; prefer a small set of typefaces. :contentReference[oaicite:9]{index=9}

---

## 🎛️ Design Tokens: conventions + rules
### Token philosophy
Tokens are *meaning*, not styling hacks. Don’t name tokens by layout/position or raw appearance.

- ✅ Prefer semantic names like `color.surface.canvas`, `color.text.primary`, `map.line.trail`, `map.fill.boundary`
- ❌ Avoid positional/presentational names like `left`, `right`, `red`, `bigText` (hard to reuse safely) :contentReference[oaicite:10]{index=10}
- ❌ Avoid class/token names based on “where it sits” (e.g., `sidebarBox`) instead of “what it is” (e.g., `filterPanel`) :contentReference[oaicite:11]{index=11}

### Minimum token sets (ship these first)
**Core UI**
- `color.*` (surface, text, border, brand, semantic feedback)
- `type.*` (font families, sizes, line heights, weights)
- `space.*` (spacing scale)
- `radius.*`
- `shadow.*` (if used)
- `motion.*` (durations, easing)

**Map**
- `map.line.*` (widths, dash arrays)
- `map.fill.*` (opacity defaults for polygons)
- `map.label.*` (sizes, halo/outline rules)
- `map.palette.*` (categorical/sequential/diverging sets)

---

## 🧩 Layout & readability (web + map UI)
Whitespace isn’t “empty”; it structures information and directs attention. :contentReference[oaicite:12]{index=12}

### Grid discipline 📐
A grid system helps maintain rhythm, alignment, and cross-page consistency. :contentReference[oaicite:13]{index=13}

**Brand rule:** The UI should “feel the same” even when modules change.

---

## 🗺️ Cartography guide (maps as a branded product)
KFM maps are not just backgrounds—they’re *arguments* with evidence attached. This section is the “rules of the road.”

### Start with intent (the first design decision)
Before styling anything, answer:
- What do you want the map to do (and for whom)?
- What message should it communicate?
- What data should be emphasized or subdued?
- What conventions (including cultural conventions) affect colors and symbols? :contentReference[oaicite:14]{index=14}

### Visual hierarchy 🧠
Brand rule: **Figure/ground** is mandatory. If everything is “loud,” nothing is legible.

- Basemap should be quieter than overlays.
- Labels should compete only with what’s relevant.
- Uncertainty should be explicit (opacity, dashed edges, annotation).

### Color choices 🎨
Use tested palettes and simulate accessibility cases:
- Use resources like ColorBrewer and Color Oracle when selecting map palettes. :contentReference[oaicite:15]{index=15}

### Tooling workflow 🛠️
If a map is destined for publication-quality output, expect a multi-tool pipeline:
- Web mapping tools can be limited; GIS output may not meet high-quality design needs.
- Graphic design software provides more control over text, color, symbols, and finishing. :contentReference[oaicite:16]{index=16}

**Brand rule:** “No single tool does everything.” Use the right tool at each stage. :contentReference[oaicite:17]{index=17}

### Icons (maps + UI) 🧷
If using map icons, standardize them via a sprite and document licensing/attribution.  
(Example sources include OSM-style symbol sets—ensure you check licensing before shipping.) :contentReference[oaicite:18]{index=18}

---

## 📊 Data‑viz guide (charts, tables, comparisons)
### Comparisons must be honest
- Outliers can distort scales; you may need alternate views or scale choices to keep charts interpretable. :contentReference[oaicite:19]{index=19}
- When comparing distributions, keep scales comparable and choose layouts that make comparison easy (e.g., stacked histograms rather than side-by-side when it helps). :contentReference[oaicite:20]{index=20}

### “Clarity > decoration”
Your visuals must support the platform’s trust goals: show sources and keep clutter low. :contentReference[oaicite:21]{index=21}

---

## ⏳ Time & timeline patterns (spatio‑temporal UX)
KFM is inherently time-aware. Timeline UX should be designed by answering:
1) **What** is presented?  
2) **Why** is it presented (user task)?  
3) **How** is it presented (visual encoding)? :contentReference[oaicite:22]{index=22}

### Progressive disclosure for timelines
A strong pattern is stacked “facets” that can collapse/expand (overview → detail), with related external resources on demand. :contentReference[oaicite:23]{index=23}

**Brand rule:** Time navigation must not hide meaning—show ordering and context.

---

## 🧾 Provenance, governance, and “truth path” alignment
KFM’s data flows through a “Truth Path” (raw → processed → cataloged → API → UI). :contentReference[oaicite:24]{index=24}

Brand assets should follow the same spirit:

### Required metadata for any shipped asset
Every logo/icon/font/style/palette should include:
- Source (creator / origin)
- License
- Version (and change log notes)
- Where it’s used (UI, map styles, reports)
- Any cultural or authority labeling (when applicable)

### Evidence + privacy expectations
Focus Mode is designed so model calls run locally (no external data leakage), and responses cite sources. :contentReference[oaicite:25]{index=25}  
Brand/UI must support this (citation chips, evidence drawers, “open source” panels).

---

## 🤝 FAIR + CARE: respectful data storytelling rules
CARE principles emphasize protecting Indigenous rights while still supporting open data. :contentReference[oaicite:26]{index=26}

**Brand guidelines derived from this:**
- Use neutral, respectful labels; avoid deficit framing.
- When data involves Indigenous communities or Traditional Knowledge:
  - include appropriate authority/provenance metadata
  - use labeling conventions (e.g., TK / biocultural labels where relevant)
  - prioritize consent-aware presentation and access patterns :contentReference[oaicite:27]{index=27}

---

## ✅ Quality gates (must pass before merge)
### Accessibility gates ♿
- [ ] Text meets contrast requirements in all supported themes
- [ ] Map palettes are color‑blind safe (simulate)
- [ ] Charts do not rely on color alone (use pattern/shape/labels)
- [ ] Icons have text alternatives where needed

### Cartography gates 🗺️
- [ ] Figure/ground hierarchy is clear at target zoom levels
- [ ] Labels are legible and don’t collide in critical extents
- [ ] Legend + scale + source attribution appear on export surfaces

### Provenance gates 🧾
- [ ] Asset has license + attribution file
- [ ] Source and change notes documented
- [ ] Map styles reference dataset/source identifiers where applicable (so the “why” is auditable)

---

## 🛠️ Contribution workflow (how to change the brand safely)
1. **Open an issue** describing the user problem (not just “make it prettier”)  
2. **Edit tokens** in `tokens/tokens.json` (single source of truth)  
3. Regenerate derived files (`tokens.css`, `tokens.ts`, `tokens.map.json`)  
4. Update any map styles / UI components that consume the changed tokens  
5. Attach screenshots for:
   - light theme
   - dark theme
   - high contrast theme
   - map at 3 zoom levels (e.g., statewide, county, neighborhood)
6. Ensure all **Quality Gates** above are checked ✅

---

## 📚 Source materials (project files this README is grounded in)
- 🏗 KFM system + UI principles (provenance-first, theming, trust patterns) :contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}:contentReference[oaicite:30]{index=30}
- 🗺 Cartographic design questions + multi-tool workflow guidance :contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}
- ⏳ Time-oriented visualization design (what/why/how; expandable facets) :contentReference[oaicite:33]{index=33}:contentReference[oaicite:34]{index=34}
- 🤝 CARE principles + provenance/authority labeling considerations :contentReference[oaicite:35]{index=35}
- 🧱 Web layout discipline: whitespace + grids + meaningful naming :contentReference[oaicite:36]{index=36}:contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}:contentReference[oaicite:39]{index=39}

---

<details>
<summary>🧠 Philosophy: “Brand is a trust interface”</summary>

KFM’s value is not only *what* it shows on a map, but **how** it proves it.  
Brand decisions must therefore optimize for:
- legibility
- auditability
- respectful representation
- consistency across modalities (2D, 3D, reports, search, AI explanations)

If a visual pattern makes provenance harder to see, it is **not on-brand**.
</details>

