# 🧩 `web/components/ui` — KFM UI Kit

![React](https://img.shields.io/badge/React-SPA-61DAFB?logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/TypeScript-Typed%20UI-3178C6?logo=typescript&logoColor=fff)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20Maps-1A1A1A?logo=mapbox&logoColor=fff)
![Cesium](https://img.shields.io/badge/Cesium-3D%20Terrain-2E5D7D?logo=cesium&logoColor=fff)
![Provenance](https://img.shields.io/badge/Provenance-First-7B2CBF)

> Reusable, composable UI components for the **Kansas Frontier Matrix (KFM)** web app.  
> This folder is where we keep the **UI building blocks** that sit around the map/timeline canvas: panels, controls, dialogs, data cards, provenance/citation widgets, and the “story + focus” experience.

---

## 📌 Quick Links

- [🧠 KFM UI Principles](#-kfm-ui-principles)
- [📦 What Belongs in `ui/`](#-what-belongs-in-ui)
- [🗺️ Core Surfaces](#️-core-surfaces)
- [🧾 Provenance UI Contract](#-provenance-ui-contract)
- [📚 Story Nodes UI](#-story-nodes-ui)
- [🤖 Focus Mode UI](#-focus-mode-ui)
- [🧱 Adding a Component](#-adding-a-component)
- [♿ Accessibility Checklist](#-accessibility-checklist)
- [🧪 Testing Expectations](#-testing-expectations)
- [🧭 Related Folders](#-related-folders)

---

## 🧠 KFM UI Principles

KFM’s UI is not “just a map.” It’s a **trustable knowledge interface**.

**Non‑negotiables:**
1. **🧾 Provenance-first UI**  
   Every map layer, chart, metric, and narrative claim must be traceable to evidence. The UI should always provide a path to “inspect source.”
2. **🧪 Evidence-first UX**  
   No unsourced story text. No “AI says so” without references. If the UI shows synthesized text, it must be clearly labeled and evidence-linked.
3. **🔌 API boundary rule**  
   UI talks to governed APIs only (never directly to the graph or raw stores).
4. **🧭 Human-centered, calm defaults**  
   Simple for casual users, deep for power users. Make the “next right action” obvious.
5. **♿ Accessibility & responsiveness**  
   Keyboard-first and screen-reader usable. Works on desktop and degrades gracefully to tablets/phones.

---

## 📦 What Belongs in `ui/`

This folder is for **reusable UI components**, not domain logic.

✅ **Good fits**
- UI primitives: buttons, inputs, dialogs, tooltips, toasts, tabs, etc.
- Layout patterns: panels, sidebars, drawers, split panes, sticky headers.
- Data presentation: cards, tables, key/value inspectors, empty/error states.
- Provenance widgets: citations, source badges, license displays, metadata sheets.
- Narrative UI: story stepper, markdown renderer wrapper, media frame.
- Focus Mode UI: Q&A panel, answer cards, evidence lists, citation clickthrough.

🚫 **Not here**
- Map engine integration logic (belongs in `web/viewers/`)
- Page-level composition (belongs in `web/views/`)
- API clients and query orchestration (belongs in hooks/services layer)
- Domain-specific one-off UI (belongs near the view that owns it)

---

## 🗺️ Core Surfaces

Even if implementations evolve, KFM’s UI tends to revolve around these surfaces:

- 🗂️ **Layer Catalog / Layer Panel**  
  Toggle datasets on/off, opacity, ordering, filtering, metadata access.
- 🧾 **Legend + Symbology**  
  Always reflects what the map is currently showing.
- 🕰️ **Timeline Slider**  
  Scrub through years/dates; time-enabled layers respond deterministically.
- 🧭 **Search Bar**  
  Search places, datasets, entities, documents.
- 🪟 **Feature Popover / Inspector Panel**  
  Click a feature → see attributes + “inspect source” + related evidence.
- 📚 **Story Panel**  
  Narrative + map synchronization + step navigation.
- 🤖 **Focus Mode Panel**  
  Ask questions about current context → answers with citations.

---

## 🧱 Suggested Component Taxonomy

> Use this as an organizing guide (not a hard rule).

### 🧷 Primitives
- `Button`, `IconButton`, `Input`, `Select`, `Checkbox`, `Radio`, `Switch`
- `Badge`, `Tag`, `Tooltip`, `Popover`
- `Dialog`, `Drawer`, `Modal`, `Toast`
- `Tabs`, `Accordion`, `Stepper`
- `Spinner`, `Skeleton`, `Progress`

### 🗺️ Map Chrome
- `LayerToggle`, `LayerOpacity`, `LayerOrderControls`
- `Legend`, `ScaleBar`, `BasemapPicker`
- `TimelineSlider`
- `FeaturePopup`, `FeatureInspector`
- `SearchBar`, `QuickFilters`

### 🧾 Provenance & Trust Widgets
- `SourceBadge` (publisher / attribution)
- `LicenseBadge`
- `Citation` / `CitationList`
- `MetadataSheet` (dataset metadata)
- `ProvenanceChip` (derived / raw / AI-generated indicator)
- `RedactionNotice` (CARE/sensitivity safeguards)

### 📚 Story Nodes
- `StoryPanel`
- `StoryStepper` (next/prev or scroll progress)
- `StoryMarkdown` (sanitized renderer wrapper)
- `StoryMedia` (image/media container with caption + citation affordances)

### 🤖 Focus Mode
- `FocusModePanel`
- `QuestionComposer`
- `AnswerCard` (clearly labeled as synthesized)
- `EvidenceSidebar` / `EvidenceDrawer`
- `CitationJump` (click citation → open underlying dataset/doc metadata)

---

## 🧾 Provenance UI Contract

Any component that visualizes **dataset-backed information** must have a way to expose:

- **Source & attribution** (publisher / origin)
- **License** (what users are allowed to do)
- **Temporal coverage** (year/date range, “as-of” timestamps when relevant)
- **Spatial coverage** (bbox/region, scale/resolution if relevant)
- **Lineage / derivation** (raw vs processed vs AI/analysis output)
- **Evidence links** (STAC/DCAT/PROV references, or API routes that resolve them)
- **Classification/redaction flags** (CARE/sovereignty sensitivity handling)

### ✅ UX patterns we prefer
- An **ⓘ info affordance** beside a dataset/layer name → opens a metadata sheet
- Citation chips in captions/footnotes that are **clickable**
- **Explicit AI labeling** (icon + “AI summary” + evidence list)
- “Show me the underlying data” path (download/open metadata)

---

## 📚 Story Nodes UI

Story Nodes are KFM’s “guided tour” mode: narrative text synchronized with map + timeline.

**UI goals:**
- Keep narrative readable (typography + spacing)
- Keep navigation obvious (stepper/scroll progress)
- Sync map state deterministically (camera/layers/time)
- Always preserve “exit story mode” → return to free exploration

### 🧰 Implementation notes (UI-facing)
- Story content is typically **Markdown** (rendered to HTML safely)
- Story progression is driven by a **config** (e.g., steps that say which layers/time/camera to set)
- Story UI must support:
  - next/prev
  - jump to step
  - optional auto-play
  - deep links to specific steps (nice-to-have)

---

## 🤖 Focus Mode UI

Focus Mode is the **evidence-backed assistant** inside the web UI.

**UI rules:**
- Focus Mode answers must:
  - be clearly labeled as synthesized
  - provide citations/references
  - enable citation clickthrough to the underlying data/doc record
- Focus Mode should be context-aware:
  - selected feature (if any)
  - active layers
  - current time on the timeline
  - current map viewport

**Good UX affordances:**
- “Use map context” toggle (on by default)
- Evidence drawer next to each answer
- One-click “highlight on map” for entities/places mentioned (when safe)

---

## 🧰 Usage

> Patterns shown below are examples — align them to your project’s actual import paths and conventions.

```ts
import { Button } from "@/components/ui/button";
import { Drawer } from "@/components/ui/drawer";
import { CitationList } from "@/components/ui/citations";

export function Example() {
  return (
    <Drawer title="Dataset Details">
      <CitationList citations={[/* ... */]} />
      <Button onClick={() => {/* ... */}}>Open metadata</Button>
    </Drawer>
  );
}
```

---

## 🧱 Adding a Component

### ✅ Definition of Done (UI Component)
- [ ] **Typed props** (TypeScript) + sensible defaults
- [ ] **Accessible** (keyboard + ARIA + focus management)
- [ ] **Composable** (doesn’t hard-code layout assumptions)
- [ ] **Supports loading/error/empty** (when it depends on data)
- [ ] **Provenance hooks**:
  - If it displays data: it must provide a path to metadata + citations
- [ ] **No direct graph/db access**
- [ ] **Tested** (unit tests for logic + basic render states)

### 🧭 Naming conventions
- `PascalCase` for components: `FeatureInspector.tsx`
- `kebab-case` for files if your repo uses that convention consistently
- Prefer `index.ts` barrels per folder *only if* it improves ergonomics and avoids circular deps.

---

## ♿ Accessibility Checklist

- Focus order makes sense (tab through controls logically)
- Dialogs/drawers trap focus and restore it on close
- Tooltip content is available to keyboard users (not hover-only)
- Color is never the only signal (use icons/text too)
- All icons have labels (`aria-label`) when they convey meaning
- Large clickable targets (esp. in map chrome)

---

## 🧪 Testing Expectations

Minimum recommended coverage:
- Render test (smoke)
- Interaction test (click/keyboard)
- “Data states”: loading / error / empty / success
- Snapshot tests only when they add value (avoid brittle snapshots)

---

## 🧭 Related Folders

```text
📁 web/
├── 📁 components/
│   ├── 📁 ui/                 👈 you are here
│   └── 📁 ...                 (app-level components)
├── 📁 viewers/                🗺️ MapLibre/Cesium integration + map engine logic
├── 📁 views/                  🧱 Page-level composition (MapPage, CatalogPage, StoryPage)
├── 📁 story_nodes/            📚 (if present) story content assets consumed by UI
└── 📁 styles/                 🎨 global styles / overrides (if present)
```

---

## 🔗 Related Docs (Project)

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline & structure
- 📏 `docs/standards/` — STAC/DCAT/PROV profiles & governance conventions
- 🧩 `schemas/ui/` — UI schema(s) if used for telemetry/layout contracts
- 📚 `docs/reports/story_nodes/` — governed Story Nodes (draft/published) if using v13 layout

---

## 🧠 Guiding Thought

> If a user can’t answer: “Where did this come from?”  
> …then our UI hasn’t finished the job yet. ✅
