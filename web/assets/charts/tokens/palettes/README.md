# 🎨 Chart Palette Tokens (Design Tokens)

![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Fcharts-blue)
![Type](https://img.shields.io/badge/type-design%20tokens-6f42c1)
![Goal](https://img.shields.io/badge/goal-accessible%20%26%20consistent-1f883d)

> [!IMPORTANT]
> Palettes are **UI contracts** 🤝  
> Changing colors can change meaning, comparability, and accessibility. Treat palette edits like any other breaking UI change.

---

## 🧭 Why this folder exists

This directory is the **single source of truth** for chart color palettes used across the web UI (charts, legends, heatmaps, choropleth-like charts, timelines, etc.).

**Goals:**
- ✅ **Consistency**: the same concept uses the same palette everywhere (no “temperature is blue→red in one chart and green→purple in another”)
- ✅ **Accessibility**: palettes must work for color‑vision deficiencies and common viewing conditions (dark mode, projectors, low-contrast screens)
- ✅ **Clarity**: palettes match data type (sequential/diverging/categorical) and avoid misleading “pretty but wrong” maps

---

## 📁 Where you are (context)

```text
🌐 web/
  🎛️ assets/
    📊 charts/
      🧩 tokens/
        🎨 palettes/
          README.md   👈 you are here
          …           (palette token files live here)
```

> [!NOTE]
> If you need **UI theme colors** (buttons, surfaces, text), those typically belong in a **separate** theme token area.  
> This folder is **charts-first**: data visualization palettes, not general branding colors.

---

## 🚀 How to use palettes

### Common access pattern (group · name · levels)
We model palettes so you can select them by:
- **group** (a palette family / library)
- **name** (the palette inside that group)
- **levels** (how many discrete colors you need)

**Example (conceptual):**
```js
// group.name[levelCount]
const colors = palettes.sequential.blues[9];   // 9-step sequential palette
const diverge = palettes.diverging.red_blue[11];
const cats   = palettes.qualitative.safe[8];
```

### Practical guidance
- **Use the smallest level count** that still communicates the story
- Prefer **5–9 steps** for binned quantitative data
- Prefer **continuous scales** in code (interpolation) *only* if the palette is designed for it (monotonic lightness for sequential)

---

## 🧠 Palette taxonomy (pick the right tool)

| Palette type | ✅ Use when | ⚠️ Avoid when |
|---|---|---|
| **Sequential** 🌡️ | ordered values (low → high), intensity, rates, counts | categories with no order |
| **Diverging** ⚖️ | values around a meaningful midpoint (0, average, baseline) | data without a true midpoint |
| **Qualitative / Categorical** 🧩 | distinct groups (crop type, county, category labels) | ordered or continuous values |
| **Cyclical** 🔁 | phase/angle/time-of-day (0° ≈ 360°) | anything that implies “low→high” |

> [!TIP]
> If users will compare **two charts** side-by-side, palettes must be identical *and* the domain mapping must match (same bins, same min/max rules, same midpoint logic).

---

## 🎯 Consistency rules (KFM-style)

### 1) Same measurement → same palette (everywhere)
If a variable is shown in multiple places (e.g., temperature, rainfall, NDVI), keep its palette stable so users build intuition.

### 2) Prefer intuitive semantics
Use conventional associations where appropriate:
- 💧 blues for water-related measures
- 🌿 greens for vegetation/biomass
- 🔥 warm colors for heat/fire risk (when contextually correct)

### 3) Avoid red–green traps 🚫
Red/green combinations are a common failure mode for accessibility.  
When a two-color contrast is needed, prefer alternatives like **blue/orange** or **purple/green** (with validated contrast and colorblind simulation).

---

## ♿ Accessibility “definition of done”

Before a palette is considered “ready” ✅, it should pass:

- [ ] **Color-vision deficiency sanity check** (deuteranopia/protanopia at minimum)
- [ ] **Light & dark backgrounds** (legends, axis labels, tooltips still readable)
- [ ] **Monotonic lightness** for sequential palettes (so “higher” doesn’t look “lower”)
- [ ] **Symmetry** for diverging palettes (equal emphasis on both sides of the midpoint)
- [ ] **Category separability** for qualitative palettes (colors remain distinct when adjacent)

> [!WARNING]
> “Rainbow” palettes often introduce false boundaries and imply structure that isn’t in the data. Use only if there’s an explicit, justified reason.

---

## 🏷️ Naming + organization conventions

### File naming 🗃️
- ✅ `lower_case_with_underscores`
- ✅ short but descriptive
- ✅ stable names (renames are breaking changes)

Examples:
- `sequential.blues.json`
- `diverging.red_blue.json`
- `qualitative.safe.json`

### Token IDs (recommended)
Treat palettes like other governed assets and give them stable IDs:

```text
kfm.ui.chart.palette.<type>.<name>.v<major>
```

Examples:
- `kfm.ui.chart.palette.sequential.blues.v1`
- `kfm.ui.chart.palette.diverging.red_blue.v1`
- `kfm.ui.chart.palette.qualitative.safe.v1`

---

## 🧩 Recommended token shape (schema-friendly)

> [!NOTE]
> This is a suggested structure so tokens can be validated in CI and consumed predictably.

```json
{
  "id": "kfm.ui.chart.palette.sequential.example.v1",
  "type": "sequential",
  "group": "sequential",
  "name": "example",
  "steps": {
    "3": ["#112233", "#556677", "#aabbcc"],
    "5": ["#0b1320", "#1d3557", "#457b9d", "#a8dadc", "#f1faee"]
  },
  "metadata": {
    "intended_for": ["binned_quantitative", "legends"],
    "notes": "Example only. Replace with real palette values.",
    "source": "internal|colorbrewer|cmocean|custom",
    "license": "see upstream source"
  }
}
```

**Rules of thumb:**
- ✅ store colors as `#RRGGBB` (CSS-friendly)
- ✅ provide multiple step counts (3/5/7/9/11 as needed)
- ✅ include provenance + license fields in `metadata`

---

## 🛠️ Adding a new palette

1. **Choose palette type** (sequential/diverging/qualitative/cyclical)
2. **Create a token file** in this folder using the naming conventions
3. **Include metadata**
   - source/provenance (where did it come from?)
   - intended use (what charts should use it?)
   - notes on midpoint / domain expectations (if diverging)
4. **Run validation** (schema + lint + any palette preview checks)
5. **Update any index/manifest** used by the chart layer (if applicable)

> [!TIP]
> If you’re adding a palette for a specific domain (🌾 agriculture, 🛰️ remote sensing, 🏛️ historical narratives), consider adding a short note about **why** this palette supports interpretation.

---

## 🔁 Changing an existing palette (treat as breaking)

When editing an existing palette:
- assume screenshots, story nodes, and user expectations may change
- keep **old versions** available whenever feasible
- bump the palette `v<major>` if meaning/appearance changes significantly

> [!IMPORTANT]
> Palette changes should be reviewed like UI contract changes (accessibility + consistency + comparability).

---

## 🧰 Anti-patterns (what not to do)

<details>
  <summary>🚫 “Just pick something that looks nice”</summary>

Aesthetic-first palettes can:
- introduce false boundaries
- hide important variance
- break consistency across the app
- fail accessibility checks

Prefer governed palettes with clear intent and provenance.
</details>

<details>
  <summary>🚫 Reusing categorical palettes for continuous data</summary>

Categorical palettes are meant for *distinct labels*, not low→high scales.  
They can create artificial “step changes” that aren’t real.
</details>

---

## ✅ Checklist for reviewers

- [ ] Palette type matches data type
- [ ] Naming + versioning follow conventions
- [ ] Metadata includes provenance + intended usage
- [ ] Accessibility checks completed (and documented)
- [ ] No new red–green dependency introduced
- [ ] Consistency with existing chart/map semantics preserved

---

## 📌 Quick glossary

- **Palette**: an ordered list of colors used to encode values or categories
- **Levels / steps**: number of colors in the palette (e.g., 7-step)
- **Domain**: the data range mapped into the palette (min/max, bins, midpoint)
- **Legend contract**: palette + domain mapping must be understandable and stable

---