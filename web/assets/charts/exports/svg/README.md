# SVG Chart Exports 📈🧩

![SVG](https://img.shields.io/badge/format-SVG-informational?logo=svg&logoColor=white)
![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Fcharts-success)
![KFM](https://img.shields.io/badge/KFM-provenance--first-critical)

> Static, **exported SVG charts** for the KFM web app (React UI) and any governed narrative surfaces that need portable, crisp visuals.  
> This folder is **exports/output** — not the source-of-truth for chart logic.

---

## 🔎 What this folder is for

KFM surfaces **statistical summaries & charts** (e.g., quick rainfall-over-time or station trends) and can render charts either:
- on the backend (Python/pandas), or
- in the frontend (D3 or similar)  
…and then present them in the UI (including popups/side panels) and in Focus Mode contexts.

This directory exists so we can keep a set of **pre-rendered SVGs** that are:

- ✅ crisp at any zoom (vector)
- ✅ easy to embed in UI + Markdown
- ✅ diffable in PRs (with a little discipline)
- ✅ cache-friendly & fast to load

---

## 📦 Directory layout

```text
web/
└─ assets/
   └─ charts/
      └─ exports/
         └─ svg/
            ├─ README.md
            ├─ <chart_id>.svg
            └─ <chart_id>.meta.json
```

> **Rule:** Every `*.svg` **must** have a matching `*.meta.json` sidecar. 🧾✅

---

## ✅ What belongs here (and what doesn’t)

| ✅ YES | 🚫 NO |
|---|---|
| Static SVG charts used across UI | Raw data files (those live under `data/…`) |
| Regression snapshots for chart components | Interactive chart logic (that lives in `web/components/…`) |
| Story/Focus visuals *when provenance-linked* | Anything that leaks sensitive locations/identifiers |
| Optimized, sanitized SVGs | SVGs with scripts/external refs (security risk) |

---

## 🧭 KFM contract reminder (why we’re strict)

KFM’s non‑negotiable ordering is:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**

That means:

- **No chart should appear in Focus Mode / governed Story contexts unless it is traceable to cataloged evidence.**
- UI must respect governance and redaction rules (no “data leakage” via visuals).
- Exports must be reproducible and stable (deterministic pipeline mindset).

🔗 See:  
- `../../../../../docs/MASTER_GUIDE_v13.md`  
- `../../../../../docs/governance/ETHICS.md`  
- `../../../../../docs/governance/SOVEREIGNTY.md`  
- `../../../../../docs/standards/KFM_STAC_PROFILE.md`  
- `../../../../../docs/standards/KFM_DCAT_PROFILE.md`  
- `../../../../../docs/standards/KFM_PROV_PROFILE.md`

---

## 🏷️ Naming conventions (chart IDs)

Use **kebab-case**, stable, semantic IDs:

`<domain>--<subject>--<metric>--<geo>--<timerange>--v<major>`

Examples:
- `climate--rainfall--annual-total--ks-bourbon-county--1950-2020--v1.svg`
- `hazards--tornadoes--count--ks-statewide--1950-2024--v1.svg`

### Rules
- **Stable IDs** across regenerations (don’t rename unless semantics change).
- Avoid `latest`, `new`, `final`, `v2-final-final` 😄
- Include `v<major>` when:
  - chart meaning changes,
  - dataset changes materially,
  - chart type/encoding changes (line → bar, etc.).

---

## 🧾 Provenance sidecar (required): `<chart_id>.meta.json`

Every exported chart must be linkable back to evidence and governance context.

### Minimal schema (recommended)

```json
{
  "chartId": "climate--rainfall--annual-total--ks-bourbon-county--1950-2020--v1",
  "title": "Annual Rainfall — Bourbon County, KS (1950–2020)",
  "description": "Annual precipitation totals aggregated from cataloged observations.",
  "createdAt": "2026-01-15T00:00:00Z",

  "generator": {
    "tool": "python/pandas|d3",
    "entrypoint": "path/to/script/or/component",
    "version": "git_sha_or_semver",
    "params": {}
  },

  "evidence": {
    "stac": ["data/stac/items/<item>.json"],
    "dcat": ["data/catalog/dcat/<dataset>.json"],
    "prov": ["data/prov/<bundle>.json"]
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Source attribution + KFM chart credit"
  },

  "sensitivity": {
    "level": "public|restricted|sensitive",
    "notes": "If restricted/sensitive, explain redaction/generalization applied."
  },

  "integrity": {
    "inputHash": "sha256:…",
    "outputHash": "sha256:…"
  },

  "usage": {
    "ui": ["StationPopup", "FocusMode"],
    "storyNodes": ["<optional-story-slug>"]
  }
}
```

### Hard gate 🚧
If `evidence.stac/dcat/prov` is empty, the SVG is **not eligible** for:
- Focus Mode
- Published Story Nodes
- Any “evidence-forward” UI claim

Keep it as:
- dev-only,
- design mock,
- or move it to a non-governed area with clear labeling.

---

## 🧱 SVG export rules (the boring stuff that saves us later)

### ♿ Accessibility (required)
Inside each SVG:
- include a `<title>` and `<desc>`
- keep axis labels + units visible
- don’t rely on color alone for meaning (use markers/labels)

> Accessible SVGs are not “nice-to-have” — they’re part of KFM’s UI contract.

### 🔒 Security
SVG is XML (and can be weaponized if treated loosely). Therefore:
- **No `<script>`**
- **No external URLs** (`<image href="http…">`, remote fonts, etc.)
- avoid inline event handlers (`onload=…`)

### 📐 Responsiveness
- must include a `viewBox`
- prefer responsive sizing (`width="100%"`, let layout control height)
- keep text readable at small sizes (popup + mobile contexts)

---

## 🎨 Style guidance (keep it consistent)

- Match KFM UI typography + spacing tokens where possible.
- Use consistent axis formatting:
  - stable tick rounding
  - stable date formatting (no locale surprises)
- Include legend when needed — but keep it compact.
- Prefer **minimal ink**: emphasize the signal, not the frame. 🧠

<details>
<summary>💡 Why this matters (design + legal)</summary>

- KFM’s credibility depends on visuals being **interpretable** and **traceable**.
- Maps/charts can also carry copyright constraints in their *representation* (linework, colors, layout), so we track attribution and licensing in the sidecar.
</details>

---

## 🧪 Optimization & QA checklist

Before committing:
- [ ] `*.meta.json` exists and references valid catalog artifacts (when evidence-linked)
- [ ] SVG renders correctly in Chrome/Firefox/Safari
- [ ] SVG contains `<title>` + `<desc>`
- [ ] No scripts/external refs
- [ ] File size reasonable (target: **< 200 KB**; justify if bigger)
- [ ] Deterministic output (re-export produces identical SVG if inputs unchanged)
- [ ] No sensitive location leaks (labels, coordinates, IDs)

> Tip: Keep attribute order stable when exporting — it reduces diff noise 📉

---

## 🔌 Using an exported SVG

### In the web UI (generic)
```html
<img
  src="/assets/charts/exports/svg/<chart_id>.svg"
  alt="Short human description of what the chart shows"
/>
```

### In React (generic import pattern)
```tsx
import chartUrl from "../assets/charts/exports/svg/<chart_id>.svg";

export function ChartFigure() {
  return <img src={chartUrl} alt="Short human description" />;
}
```

### In Markdown (docs / stories)
```md
![Annual rainfall — Bourbon County, KS (1950–2020)](../../../../../web/assets/charts/exports/svg/<chart_id>.svg)
```

> For governed Story Nodes: **the narrative must cite the same evidence** referenced by the chart’s sidecar.

---

## 🆘 Troubleshooting

**SVG looks blurry**  
→ Ensure you’re not embedding it as a raster fallback somewhere, and that `viewBox` is correct.

**Text shifts between machines**  
→ Avoid external fonts; use system-safe stacks or convert labels to paths *only if absolutely necessary* (but prefer real text for accessibility).

**Diff is massive after re-export**  
→ Export deterministically (stable sorting, stable tick placement) + run an optimizer consistently.

---

## 🔗 Related paths (handy)

- UI chart components: `../../../../components/` (look for chart-related components)
- UI styling: `../../../../styles/`
- Story Nodes (v13 governed): `../../../../../docs/reports/story_nodes/`
- Story Node template: `../../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md`

---

## ✅ TL;DR

If it’s in here, it should be:
- **portable** (SVG),
- **safe** (sanitized),
- **consistent** (style + deterministic),
- **traceable** (meta sidecar linking evidence),
- **governed** (no sensitive leaks).

🚀 Happy exporting!
