# 📊 Chart Specs Library (KFM Web)

| 🧭 Scope | 🧩 What this is | 🎯 Primary goal |
|---|---|---|
| `web/assets/charts/specs/library/` | A **reusable “spec library”** for charts (templates + fragments + conventions) | Consistent, interpretable, **provenance-linked** charts across the KFM UI |

> [!IMPORTANT]
> In KFM, charts are not “decoration.” They are part of the **analysis + trust surface**: charts should be *immediately interpretable* and (when applicable) expose **sources + metadata** the same way map layers do. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧠 Context (how charts are used in KFM)

KFM’s front-end is a modern **React (TypeScript) SPA** with MapLibre (2D) and optional Cesium (3D) for visualization. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Charts show up in places like:
- **Statistical summaries & quick charts** for a dataset/query result (e.g., rainfall over time for a county). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Pop-ups / side panels** when a user clicks a map feature (a common pattern is “click → details panel → chart”). [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Provenance-first UI** patterns (e.g., tooltips/captions that include the dataset origin, and chart captions that include citations). [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ What belongs here (and what doesn’t)

### ✅ Put here
- **Declarative chart templates/specs** that can be reused across multiple views.
- **Spec fragments** (shared axis/legend/tooltip rules, number formatting, interaction patterns).
- **Themes & palettes** aligned with KFM cartographic conventions.
- **Small example fixtures** (tiny JSON/CSV samples) for documentation & visual regression tests.

### ❌ Don’t put here
- React components (those live under `web/components/…` per KFM’s web structure). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Dataset pipelines or heavy computations (those belong server-side / pipeline-side; KFM charts may be computed backend with Python/pandas where appropriate). [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗂️ Suggested layout (inside `library/`)

```text
📁 web/
  📁 assets/
    📁 charts/
      📁 specs/
        📁 library/
          📄 README.md
          📁 templates/          # 📐 full chart blueprints (ready to render)
          📁 fragments/          # 🧱 shared pieces (axes, tooltips, legends, encodings)
          📁 themes/             # 🎨 palettes, typography, spacing, grid rules
          📁 examples/           # 🧪 tiny fixtures + screenshots (optional but encouraged)
          📁 schemas/            # 🧾 JSON Schema for validation (optional but ideal)
```

> [!NOTE]
> If you already have an existing structure, keep it — the goal is *clarity + consistency*, not churn.

---

## 🧭 Non‑negotiable principles (KFM-aligned)

### 1) 🧾 Evidence-first & provenance-linked
KFM treats **evidence artifacts** (including derived/analytical outputs) as first-class, with provenance and catalog alignment before UI use. [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

For chart specs, that means:
- Every spec SHOULD be able to surface:
  - **dataset identifiers** (DCAT / dataset IDs),
  - **asset IDs** (STAC item/collection IDs where relevant),
  - **lineage** (PROV bundle IDs / activity IDs),
  - **license + attribution** (at minimum). [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- If a chart appears in a “trust-sensitive” context (Story Nodes / Focus Mode / evidence panels), citations must be first-class, not an afterthought. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) 🧩 Contract-first (versioned & validated)
KFM’s v13 stance: **schemas/contracts are first-class artifacts** and changes require versioning + compatibility discipline. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

For chart specs, that means:
- Specs should be **machine-validated** (JSON Schema strongly recommended).
- Breaking changes → bump the spec version and/or spec ID.

### 3) 🗺️ Cartographic + visualization consistency
KFM’s conventions emphasize:
- Legends include **units** and clear labels,
- Time-based visuals **label the time shown**,
- Symbology stays consistent across similar layers,
- Use established guidelines (e.g., ColorBrewer) when appropriate. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Apply the same discipline to charts:
- Axis labels MUST include **units** when measurable.
- Time series MUST show the time granularity (year/month/day).
- Color encoding MUST be consistent with map layer color meaning (don’t make “heat” blue on one chart and red on another).

### 4) ♿ Accessibility by default
KFM explicitly targets accessibility with high-contrast support and semantic/ARIA-friendly UI patterns. [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

For chart specs:
- Don’t rely on color alone (use shape/line style/annotation).
- Provide text alternatives: captions, summaries, or screen-reader friendly descriptions.

### 5) 🖱️ Map-sync interactions (chart ↔ map)
Interactive chart-to-map linking is a powerful (and expected) pattern for spatiotemporal analysis: clicking a chart point can reveal the corresponding spatial layer/time slice on the map. [oai_citation:15‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)

In KFM terms:
- A chart interaction should emit a **typed event** (e.g., `timeSelected`, `rangeSelected`, `categorySelected`) that the map/timeline can consume.
- The “selected time” should line up with KFM’s temporal navigation concepts.

---

## 🧾 The “ChartSpecBundle” pattern (recommended)

A **portable chart spec** should contain two parts:
1) **KFM metadata wrapper** (provenance, contracts, accessibility, intent)
2) **Engine-specific payload** (whatever the renderer expects)

### Minimal bundle (example)

```json
{
  "id": "kfm.chart.timeseries.rainfall",
  "version": "1.0.0",
  "title": "Rainfall over time",
  "description": "Monthly rainfall for a selected county; supports click-to-set timeline.",
  "kind": "timeseries",
  "engine": "vega-lite",

  "inputs": {
    "contract": "kfm.timeseries@1",
    "fields": { "x": "date", "y": "rain_mm", "series": "county" },
    "expected_units": { "y": "mm", "x": "date" }
  },

  "provenance": {
    "datasets": ["dcat:us.noaa.precip.kansas.monthly@2025-05"],
    "stac": ["stac:collection:climate-precip-kansas"],
    "prov": ["prov:bundle:precip-etl-run-2025-05-01"],
    "license": "public-domain-or-source-license-id",
    "attribution": "NOAA (processed by KFM pipeline X)"
  },

  "a11y": {
    "summary": "Line chart showing rainfall totals per month.",
    "high_contrast_safe": true
  },

  "interactions": {
    "onPointClick": { "emits": "timeSelected", "payload": { "field": "date" } }
  },

  "spec": {
    "/* engine payload here */": true
  }
}
```

> [!TIP]
> If you’re unsure what to include in provenance fields, follow the KFM “catalog boundary artifacts” mindset: PROV describes lineage; STAC/DCAT make it discoverable; and these should be established before evidence reaches UI surfaces. [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🎛️ Common chart “kinds” to standardize

Standardizing kinds makes UI integration easier (filters, toolbars, export, captions, etc.):

- `timeseries` 📈 (single/multi-series)
- `histogram` 📊
- `bar` / `stacked_bar` 🧱
- `scatter` ✳️
- `boxplot` 📦
- `heatmap` 🌡️
- `small_multiples` 🪟
- `sparkline` ⚡ (for popups / compact summaries)

> [!NOTE]
> KFM documentation explicitly calls out “small charts in pop-ups” as a valuable interpretability feature — keep these specs lightweight and fast. [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧪 Validation & QA (recommended gates)

Because KFM favors **CI-enforced quality** and contract validation, chart specs should follow the same philosophy. [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Suggested checks
- ✅ JSON schema validation (required fields present; versions valid)
- ✅ No missing unit labels for quantitative axes
- ✅ Provenance block present for any chart shown in evidence/story contexts
- ✅ Accessibility metadata present (summary/caption)
- ✅ Screenshot regression (optional but great for stability)

---

## 🧰 Adding a new chart spec (workflow)

1. **Pick the kind** (timeseries, histogram, etc.).
2. Create a new spec file in `templates/` (full spec) or `fragments/` (partial).
3. Add an **example fixture** under `examples/` (tiny!).
4. Add/confirm:
   - units,
   - legend rules,
   - provenance wiring (IDs, not giant blobs),
   - a11y summary.
5. Run validation (schema + lint + screenshot if available).
6. Link it from any higher-level “catalog” page or component that consumes it.

---

## ✅ Definition of Done (quick checklist)

- [ ] Spec has a stable `id` + `version` (semver).
- [ ] Inputs contract is clear (`inputs.contract`, expected fields & units).
- [ ] Legends/labels are not ambiguous (units included). [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Time-based visuals label the time displayed/granularity. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Provenance is wired for evidence-grade surfaces (DCAT/STAC/PROV IDs). [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] a11y summary exists; spec supports high-contrast expectations. [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] (If interactive) chart emits typed events for timeline/map syncing. [oai_citation:24‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)

---

## 🔗 Related places in the repo (orientation)

- `web/components/…` → React components that **render** these specs. [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- `docs/MASTER_GUIDE_v13.md` → the “contracts + evidence-first” backbone (recommended reading). [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `docs/standards/…` → STAC/DCAT/PROV profiles and governance rules (where chart provenance should align).
- `data/catalog/…` + `data/prov/…` → where dataset IDs and provenance bundles originate. [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 References (project files used)

- KFM Technical Documentation (charts in UI, D3/similar, provenance in visualization, web structure, accessibility). [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM Master Guide v13 excerpts (contract-first + evidence/provenance artifact rules). [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:34‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Cloud-based remote sensing reference (chart point click → reveal spatial layer/time slice pattern). [oai_citation:35‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)
