# 🧩 Domain Layers — Map Layer Registry & Policy

![Scope](https://img.shields.io/badge/scope-web%2Fsrc%2Fservices%2Fdomain%2Flayers-2ea44f)
![Contract](https://img.shields.io/badge/contract-layer_registry-%23007ACC)
![Provenance](https://img.shields.io/badge/provenance-required-%239C27B0)
![Safety](https://img.shields.io/badge/safety-no_data_leakage-%23D32F2F)

This folder is the **domain “source of truth”** for **what the UI considers a “layer”** and the **rules** that govern layers (visibility, ordering, temporal behavior, provenance, redaction-friendly UX).  
Think: **definitions + policy + registry** ✅ (not UI components and not MapLibre calls).

---

## 🎯 TL;DR

- ✅ Define a layer once (stable ID, metadata, provenance)
- ✅ Register it in the **Layer Registry** (the canonical list)
- ✅ Keep domain logic **framework-agnostic**
- ✅ UI must **not leak data** (no “zoom around” shortcuts)
- ✅ Every layer must have **provenance + attribution** (STAC/DCAT-backed)
- ✅ Sensitive layers must follow **CARE-style redaction UX** (defense-in-depth)

---

## 🧠 What is a “Layer” in KFM?

A **Layer** is a *user-toggleable* map overlay (raster or vector), optionally time-aware, that:

- can be turned on/off
- can appear in the legend / sidebar
- has a stable identifier (for deep links, telemetry, bookmarks)
- is backed by **governed** data served through the platform (not hidden files)
- has a **provenance story** (where it came from, what it represents, how to cite it)

Examples:
- 🗺️ historical boundary overlays
- 🛰️ imagery rasters (COG/tiles)
- 🧭 routes / trails / vector features
- 🕰️ time-sliced “era” layers that react to the timeline slider
- 📍 points-of-interest layers (with strict rules for sensitive coordinates)

---

## 🧱 Clean Architecture in the Frontend (Why “domain” matters)

We treat the web app like a layered system:

- **Domain (this folder)**: pure definitions + rules (“what a layer is”)
- **Application**: use-cases / orchestrators (“toggle layer”, “sync timeline”)
- **Infrastructure**: adapters (“fetch layer catalog”, “MapLibre style conversion”)
- **UI**: components (“Sidebar toggles”, “Legend”, “MapView”)

✅ Goal: keep **policy** stable even if we swap mapping libs, fetching strategy, or UI components.

---

## ✅ Responsibilities of `domain/layers`

### 1) 📚 Layer Registry (canonical list)
The registry is the UI’s one-stop list of:
- known layers
- grouping/category info
- defaults (visible? opacity? order?)
- compatibility flags (timeline-aware? requires auth? etc.)
- provenance hooks (what to show in “About this layer”)

> If you can toggle it in the UI, it should be representable here.

### 2) 🧬 Domain Types (stable contracts)
Common domain types usually include:
- `LayerId` (stable, never recycled)
- `LayerDefinition` / `LayerConfig`
- `LayerGroup` / `Category`
- `TemporalExtent` / `TimeSliceBehavior`
- `LegendSpec`
- `ProvenanceRef` (STAC/DCAT IDs + attribution fields)
- `Sensitivity` / `RedactionPolicyHint` (UX rules, not enforcement)

### 3) 🧯 Policy & Guardrails (defense-in-depth)
This folder may include policy helpers that UI and application layers can reuse:

- ordering + z-index rules
- zoom gates (UX guardrails)
- “is layer visible at time T?”
- “is layer allowed in this mode?”
- lightweight validation for registry entries

> **Important:** enforcement of access control / redaction is server-side.  
> Domain policies here are **UX guardrails** + consistency helpers.

---

## 🚫 What does NOT belong here?

Avoid putting these in `domain/layers`:

- ❌ direct calls to MapLibre/Leaflet APIs
- ❌ React components / hooks (keep in UI/presentation)
- ❌ raw dataset files (GeoJSON, tiles, rasters) bundled into the web app
- ❌ “secret” endpoints / hardcoded URLs that bypass the server boundary
- ❌ anything that would make the UI the source of truth for data access

---

## 🔐 Non‑Negotiables (Governance & Safety)

### 🛡️ No data leakage
The UI must **respect redaction rules** and never provide a “workaround” via zooming, querying, or revealing precise coordinates through client tricks.

Practical implications:
- layers may define `minZoom` / `maxZoom` (UX bounds)
- sensitive layers must avoid “exact coordinate” display by default
- popups/legends must not expose forbidden precision even if the geometry is visible

### 🧾 Provenance required
Every layer must have enough metadata to support:
- source attribution
- license visibility (when applicable)
- a “What am I looking at?” explanation
- a link/reference to catalog entries (STAC/DCAT)

### ♿ Accessibility + 🧾 audit/telemetry hooks
Layer interactions are **user-facing actions**:
- toggles and legend entries must be screen-reader friendly
- registry IDs must be stable for analytics/audit logging

---

## ➕ Adding a new layer (Checklist ✅)

### 0) Confirm the data path (before UI work)
- [ ] Dataset is published/served through the platform boundary (API), not embedded in the client
- [ ] Any redaction/classification logic lives server-side
- [ ] Catalog metadata exists (STAC/DCAT/PROV references)

### 1) Add the layer definition
- [ ] Create/extend a `LayerDefinition` with:
  - stable `id`
  - `title` + `description`
  - layer `kind` (raster/vector/etc.)
  - temporal behavior (if any)
  - default visibility + ordering/group
  - provenance refs (STAC/DCAT identifiers + attribution)

### 2) Register it in the Layer Registry
- [ ] Add to the canonical registry list
- [ ] Ensure ID uniqueness (no collisions)
- [ ] Place in the correct group/category (UX + narrative coherence)

### 3) Provide the “About / Legend” UX pieces
- [ ] Legend entries (colors/symbols, units)
- [ ] “Source / citation” content (human-readable attribution)
- [ ] Any warnings (e.g., “generalized locations”, “sensitive precision withheld”)

### 4) Tests & validation
- [ ] Unit test: registry has unique IDs
- [ ] Unit test: required metadata present (title, provenance, etc.)
- [ ] Snapshot/contract test: registry export shape (if used by UI)

### 5) Accessibility & analytics
- [ ] Toggle labels are accessible and unambiguous
- [ ] Layer events emit stable IDs

---

## 🧪 Suggested validations (keep us honest)

Here are cheap tests that pay dividends:

- ✅ **Registry ID uniqueness**
- ✅ **Required fields present** (title, description, provenance ref)
- ✅ **Temporal consistency** (start <= end, known granularity)
- ✅ **Sensitivity rules** (if `sensitivity !== "Public"`, then “no precise coords” flag must exist)

> Tip: If you already have a shared schema/validator pattern in `schemas/` or `tools/`, plug the layer registry into it 📎

---

## 🗂️ Expected shape (example) ✨

> Your exact filenames may differ — keep the responsibilities consistent.

```text
📁 web/src/services/domain/layers/
├── 📄 README.md                    # you are here ✅
├── 📄 registry.ts                  # canonical list of LayerDefinitions
├── 📄 types.ts                     # LayerDefinition, LayerId, enums
├── 📄 policy.ts                    # ordering/visibility rules (pure)
├── 📁 __tests__/                   # fast unit tests (registry + policy)
└── 📁 docs/                        # optional: layer-specific notes/legends
```

---

## 🧩 Reference flow (data → UI)

```mermaid
flowchart LR
  A[(Catalog + Data\n(STAC/DCAT/PROV))] --> B[API boundary\n(src/server/...)]
  B --> C[Domain layer registry\n(web/src/services/domain/layers)]
  C --> D[Map adapter\n(infrastructure)]
  D --> E[Map renderer\n(MapLibre/Leaflet)]
  C --> F[UI controls\n(Sidebar/Legend/Timeline)]
```

---

## 🔗 Related docs (repo paths)

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical subsystem homes + UI contract  
- 🧭 `docs/architecture/` — system blueprints & ADRs  
- 🧾 `schemas/` — validation schemas (STAC/DCAT/PROV + UI artifacts)  
- 🧠 `docs/reports/story_nodes/` — narrative content that layers may reference

---

## 🙋 FAQ

### “Where do MapLibre layer specs live?”
Not here. Keep MapLibre-specific styling/translation in **infrastructure adapters** so the domain can remain stable if we swap mapping engines.

### “Can I hardcode a GeoJSON in the UI for a quick prototype?”
Only if it’s explicitly approved as a temporary dev artifact. The long-term rule is: **the UI is not a data source**.

### “How do I handle sensitive locations?”
Use server-side redaction + client UX guardrails:
- generalized geometries / masked coordinates
- limits on zoom/detail
- clear UI messaging (“precision withheld”)

---

✅ If you’re adding a new layer and you’re unsure where something belongs:  
**default to putting it *outside* domain** unless it’s a stable definition or a pure policy rule.