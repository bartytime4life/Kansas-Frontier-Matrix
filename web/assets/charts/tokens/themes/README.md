# 🎨 Chart Theme Tokens (KFM Web)

![tokens](https://img.shields.io/badge/tokens-theme%20JSON-blue)
![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fcharts%2Ftokens%2Fthemes-purple)
![a11y](https://img.shields.io/badge/a11y-contrast%20%2B%20colorblind--aware-brightgreen)
![ux](https://img.shields.io/badge/ux-provenance--first%20visuals-orange)

These files define **declarative theme tokens** for charts in the KFM web UI.  
If the UI is the “window” into KFM’s data, **themes are the glass**: consistent, accessible, and (critically) *auditable*.

> ✅ Goals: consistent charts across the app, safe defaults, easy theme additions, and “no black box” styling decisions.

---

## 🧭 Quick links

- [What lives here](#-what-lives-here)
- [Folder layout](#-folder-layout)
- [Token model](#-token-model)
- [How themes are applied](#-how-themes-are-applied)
- [Add a new theme](#-add-a-new-theme)
- [Accessibility checklist](#-accessibility-checklist)
- [Testing & CI ideas](#-testing--ci-ideas)
- [FAQ](#-faq)

---

## 📦 What lives here

This directory holds **theme definitions** for chart rendering:

- 🎚️ **Palette tokens** (categorical, sequential, diverging)
- 🧱 **Core surface + typography** tokens (background, text, axes, gridlines)
- 🧩 **Component tokens** (tooltip, selection highlight, annotations, thresholds)
- 🧾 **Metadata hooks** to support KFM’s provenance-first UX (e.g., human-readable names, notes, versioning)

> 🧠 Why tokens? Because charts show “truth claims” visually. Tokens keep that presentation **consistent** and **reviewable** in PRs.

---

## 🗂️ Folder layout

> 📌 This is the *recommended* layout. Keep themes small & composable.

```text
web/
└─ 📁 assets/
   └─ 📈 charts/
      └─ 🎛️ tokens/
         └─ 🎨 themes/
            ├─ ✅📄 README.md                      # you are here 📌
            ├─ 📐🧾 _schema.chart-theme.json       # optional: JSON Schema validation
            ├─ 🧩🧾 _template.theme.json           # starting point for new themes
            ├─ 🧱🎨🧾 base.theme.json               # shared baseline tokens
            ├─ 🌞🎨🧾 kfm-light.theme.json          # default light theme
            ├─ 🌙🎨🧾 kfm-dark.theme.json           # default dark theme
            ├─ ♿🎨🧾 kfm-high-contrast.theme.json   # accessibility-first theme
            └─ 🧪 experiments/                     # WIP themes (do not ship by default)
```

---

## 🧱 Token model

We treat theme files as **data**, not code:

- **No functions**, no computed logic
- Tokens should be stable, explicit values
- Themes may reference a shared `base.theme.json` (by convention) ✨

### ✅ Suggested top-level shape

```json
{
  "$schema": "./_schema.chart-theme.json",
  "meta": {
    "id": "kfm-light",
    "name": "KFM Light",
    "description": "Default chart theme for light surfaces.",
    "version": "1.0.0",
    "updated": "2026-01-16",
    "notes": [
      "Keep categorical palette colorblind-aware.",
      "Sequential palettes should be perceptually ordered."
    ]
  },
  "tokens": {
    "surface": {},
    "text": {},
    "axis": {},
    "grid": {},
    "tooltip": {},
    "palette": {},
    "series": {},
    "states": {},
    "semantic": {},
    "provenance": {}
  }
}
```

### 🧩 Token groups (what they mean)

| Group | Purpose | Examples |
|------:|---------|----------|
| `surface` | chart container styling | `bg`, `border`, `shadow` |
| `text` | base typography colors/sizes | `primary`, `muted`, `fontFamily` |
| `axis` | axis line/ticks/labels | `line`, `ticks`, `label` |
| `grid` | gridlines & plot guides | `major`, `minor`, `zeroLine` |
| `tooltip` | tooltip styling | `bg`, `text`, `border`, `shadow` |
| `palette` | the actual color palettes | `categorical`, `sequential`, `diverging` |
| `series` | defaults per series | `strokeWidth`, `pointRadius`, `dashPatterns` |
| `states` | hover/active/selected | `hoverAlpha`, `selectedOutline` |
| `semantic` | meaning-based colors | `good`, `warning`, `danger`, `info` |
| `provenance` | citations-friendly visuals | `captionText`, `citationLinkColor`, `sourceBadgeBg` |

---

## 🎛️ Palettes: categorical vs sequential vs diverging

Charts in KFM often switch between different scale types (especially for legends and dynamic data layers). Pick the palette type that matches the data:

### 🧺 Categorical (unordered buckets)
Use when categories have **no numeric order** (e.g., land cover classes).

```json
"palette": {
  "categorical": [
    "#2E86AB",
    "#F6AE2D",
    "#33658A",
    "#F26419",
    "#86BBD8",
    "#2F4858",
    "#B33F62",
    "#7A9E7E"
  ]
}
```

### 🌡️ Sequential (low → high)
Use for intensity/amount (precipitation, population density, temperature anomaly *if only positive*).

Two good options:

**(A) Simple list**
```json
"palette": {
  "sequential": {
    "stops": ["#f7fbff", "#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c"]
  }
}
```

**(B) Stops with positions (preferred for gradients)**
```json
"palette": {
  "sequential": {
    "stops": [
      { "t": 0.0, "color": "#f7fbff" },
      { "t": 0.5, "color": "#6baed6" },
      { "t": 1.0, "color": "#08306b" }
    ]
  }
}
```

### ⚖️ Diverging (negative ↔ neutral ↔ positive)
Use when there is a meaningful midpoint (0, baseline, historical average).

```json
"palette": {
  "diverging": {
    "stops": [
      { "t": 0.0, "color": "#b2182b" },
      { "t": 0.5, "color": "#f7f7f7" },
      { "t": 1.0, "color": "#2166ac" }
    ],
    "midpoint": 0.5
  }
}
```

---

## 🧷 Naming conventions

Keep keys **predictable** and **grep-friendly**:

- ✅ `tokens.<group>.<thing>`
- ✅ prefer `bg`, `fg`, `muted`, `border`, `outline`, `shadow`
- ✅ avoid ambiguous names like `blue1`, `blue2` unless strictly palette-local
- ✅ include intent when the color has meaning: `semantic.warning`, `semantic.danger`

Example:

```json
"tokens": {
  "surface": { "bg": "#ffffff", "border": "rgba(17, 24, 39, 0.08)" },
  "text": { "primary": "#111827", "muted": "rgba(17, 24, 39, 0.65)" },
  "axis": { "label": "rgba(17, 24, 39, 0.85)", "ticks": "rgba(17, 24, 39, 0.35)" }
}
```

---

## 🧠 How themes are applied

Implementation details will vary by charting library, but the ideal flow is:

1. **Theme chosen** (user setting, system preference, or route context)
2. **Theme tokens loaded** (static import or fetched asset)
3. **Tokens mapped** into:
   - CSS variables (for shared UI + chart chrome)
   - chart config objects (for the chart renderer)

> 💡 KFM UI emphasizes “the map behind the map” — charts should do the same: easy-to-read styling with room for captions, legends, and citations.

### Example mapping (pseudo-code)

```ts
import theme from "./kfm-light.theme.json";

// 1) Write to CSS variables for consistent chrome
applyCssVars(theme.tokens);

// 2) Convert to library-specific chart options
const chartOptions = makeChartOptions(theme.tokens);

// 3) Render
renderChart({ data, options: chartOptions });
```

---

## 🧾 Provenance-friendly styling (KFM DNA)

Charts in KFM may appear in:
- 🗺️ map popups (mini-graphs / sparklines)
- 📊 side panels (analytics, trends)
- 🧭 story/narrative views (captioned visuals)

To support KFM’s provenance-first principles:
- keep tokens for captions readable (`provenance.captionText`)
- provide a distinct style for citations / source chips (`provenance.sourceBadge*`)
- avoid color choices that imply meaning unless it’s **encoded as semantic tokens**

Example:

```json
"provenance": {
  "captionText": "rgba(17, 24, 39, 0.75)",
  "citationLinkColor": "#1d4ed8",
  "sourceBadgeBg": "rgba(17, 24, 39, 0.06)",
  "sourceBadgeText": "rgba(17, 24, 39, 0.78)"
}
```

---

## ➕ Add a new theme

### 1) Copy the template 🧬
Create `my-theme.theme.json` using `_template.theme.json`.

### 2) Fill in `meta` ✍️
- `id` must be unique
- `name` should be human-friendly (UI label)
- `version` follows semver (at least major/minor)
- add `notes` if you made non-obvious choices

### 3) Define palette(s) 🎨
- include a categorical palette of at least 8 colors
- include sequential + diverging if the theme is “full-service”

### 4) Run checks ✅
- JSON schema validation (if present)
- contrast checks (see below)
- snapshot tests (if present)

### 5) Add it to the theme registry 📚
Wherever the app lists themes, add:
- `id`, `name`, `description`
- preview chip colors (optional)

---

## ♿ Accessibility checklist

> ✅ “Readable > pretty” every time.

### Must-haves
- [ ] **Text contrast**: axis labels, tick labels, tooltip text all pass contrast on the chart surface
- [ ] **Gridlines don’t dominate**: grid should be subtle (often lower alpha)
- [ ] **Color is not the only signal**: support dash patterns, markers, annotations, or labels
- [ ] **Avoid red/green traps**: especially for semantic comparisons
- [ ] **High-contrast theme exists**: and it’s not an afterthought

### Nice-to-haves
- [ ] Safe defaults for **deuteranopia/protanopia** (categorical palette checks)
- [ ] Tooltip uses **solid background** (not translucent over noisy charts)
- [ ] Selection/hover states are obvious without relying only on color

---

## 🧪 Testing & CI ideas

If you want this folder to be “NASA-grade” reliable 🚀, here’s a solid testing ladder:

- ✅ **Schema validation**: every theme validates against `_schema.chart-theme.json`
- ✅ **Token completeness**: required keys exist (`surface.bg`, `text.primary`, etc.)
- ✅ **Contrast tests**: programmatically compute contrast ratios for critical pairs
- ✅ **Visual regression**: render a small set of canonical charts and compare snapshots
- ✅ **Diff-friendly PRs**: keep tokens stable and ordered (alphabetical keys)

> 🧩 Tip: store themes with stable formatting (sorted keys + consistent indentation) to reduce noisy diffs.

---

## ❓ FAQ

### “Why separate chart tokens from general UI tokens?”
Because charts have unique needs:
- multiple palettes (categorical/sequential/diverging)
- plot chrome (grid/axis/zero-line)
- states (hover/selection) that must remain clear on dense visuals

### “Do themes control legends too?”
Yes — legends are part of chart comprehension. Tokens should include legend text, swatch borders, and ramp behavior.

### “Where do we put experimental palettes?”
In `experiments/` with loud naming and no default export until they’re vetted.

---

## 🤝 Contributing notes

- Prefer small PRs: change **one theme** at a time
- Include before/after screenshots if you touch palettes
- Document non-obvious decisions in `meta.notes`

---

### 🏁 Bottom line

If KFM is committed to **auditable, provenance-first visualization**, then our chart themes must be:

✅ consistent • ✅ accessible • ✅ explainable • ✅ easy to evolve

🎉 Welcome to the theme layer.
