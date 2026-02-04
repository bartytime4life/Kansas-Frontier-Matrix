# 🧩 `web/src/features` — Feature Modules

![React](https://img.shields.io/badge/React-%E2%9A%9B%EF%B8%8F-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-%F0%9F%93%98-blue)
![Feature-first](https://img.shields.io/badge/Architecture-Feature--First-brightgreen)
![Provenance-first](https://img.shields.io/badge/Policy-Provenance--First-orange)

Welcome to the **feature layer** of the KFM web app. Each folder here represents a **cohesive product capability** (a “vertical slice”) that can be developed, tested, and evolved with minimal cross-module coupling.

> 🎯 Goal: keep UI code **modular**, **scalable**, and **governed** — especially for map + timeline + AI “Focus Mode” workflows.

---

## 📌 What belongs in `features/`?

A feature module owns the end-to-end UI implementation for a capability:

- ✅ **UI components** (feature-scoped)
- ✅ **routes / pages** (if the feature is navigable)
- ✅ **state** (local store, reducers, atoms, query caches, etc.)
- ✅ **hooks** (feature-specific logic + orchestration)
- ✅ **services** (API calls + adapters)
- ✅ **types** (DTOs, domain types)
- ✅ **utils** (formatters, helpers)
- ✅ **tests** for everything above

Examples of “feature-shaped” capabilities you’ll commonly see in KFM:

- 🗺 **Map Viewer** (2D MapLibre + optional 3D Cesium)
- 🧱 **Layer Control** (toggle layers, legends, symbology)
- ⏳ **Timeline** (time slider + time-scoped filters)
- 📚 **Catalog / Search** (dataset discovery)
- 🤖 **Focus Mode** (AI chat + citations UX)
- 📖 **Stories** (narrative player / story panels)

---

## 🧠 Feature design principles

### 1) 🧱 Vertical slice ownership
A feature should be able to answer:
- “What UI does it render?”
- “What API endpoints does it call?”
- “What state does it own?”
- “How is it tested?”

If the answers are scattered across the repo, it’s usually a sign the module boundary needs tightening.

### 2) 🌐 API-first (no “backdoor data paths”)
Front-end features should treat the backend API as the **single gateway** for data.  
Avoid “creative shortcuts” like bypassing adapters, reading local files directly, or mixing mock data into production code paths.

**Rule of thumb:** UI talks to **services**, services talk to **API client**, API client talks to backend.

### 3) 🧾 Provenance-first UX
KFM is evidence-first. If a user is shown a claim (especially from Focus Mode), the UI should:
- display citations/footnotes when available
- make citations *clickable* to reveal source metadata
- gracefully degrade if the backend returns “insufficient evidence”

---

## 🗂 Recommended module layout

Each feature folder should follow a predictable shape:

```text
web/src/features/
  🧩 <feature-name>/
    README.md                # optional: feature-local notes
    index.ts                 # public exports (barrel)
    routes/                  # route-level components (if any)
    components/              # feature-scoped UI pieces
    hooks/                   # feature orchestration
    services/                # API + adapters (fetch wrappers)
    state/                   # store slices / reducers / atoms
    types/                   # feature types + API DTOs
    utils/                   # helpers/formatters
    __tests__/               # unit/integration tests
```

### 🔒 Public API rule
Only export what other modules should import from `index.ts`.

✅ Prefer:
```ts
// features/timeline/index.ts
export * from "./routes/TimelinePage";
export * from "./state/timelineSlice";
export * from "./hooks/useTimeline";
```

🚫 Avoid importing deep internals:
```ts
// ❌ anti-pattern
import { computeBuckets } from "@/features/timeline/utils/bucketMath";
```

If other features need something, consider moving it to:
- `web/src/shared/` (generic)
- `web/src/lib/` (infrastructure)
- `web/src/components/` (truly reusable UI)

---

## ➕ Adding a new feature (checklist)

1. 📁 Create folder: `web/src/features/<feature-name>/`
2. 🧭 Add routes (if needed):
   - add page component under `routes/`
   - register route in app router
3. 🔌 Add API adapter:
   - define typed requests/responses in `types/`
   - implement calls in `services/`
4. 🧠 Add state:
   - feature-local state in `state/`
   - keep global state minimal and intentional
5. 🧪 Add tests:
   - logic tests for utils/hooks/state
   - UI tests for route-level behavior
6. ♿ Validate UX:
   - keyboard navigation works
   - focus states are visible
   - screen reader labels exist for controls
7. ⚡ Performance sanity:
   - avoid rendering huge GeoJSON sets without tiling/aggregation
   - code-split heavy views (Map/Cesium/Focus Mode)

---

## 🗺 Map-centric feature guidance

### MapLibre (2D)
Typical responsibilities inside a map feature:
- initialize the map instance
- manage layer lifecycle (add/remove/update)
- style layers consistently (legend aligns with map)
- handle feature selection + popups
- synchronize viewport + filters with global app state

**Tip:** Treat “layer definitions” as data:
- one place to define: source → style → legend metadata → query params

### Cesium (3D)
If 3D is enabled:
- isolate Cesium in its own feature module or submodule
- lazy-load Cesium to keep initial bundle smaller
- ensure state sync between 2D ↔ 3D (camera, selection, active layers)

---

## ⏳ Timeline feature guidance

Timeline should be a *first-class* input to other features:
- map filters respond to selected year/range
- stories highlight relevant passages
- catalog queries can be scoped by time

**Best practice:** timeline state emits a single “time filter object” consumed by other modules:
```ts
type TimeFilter = { mode: "year" | "range"; year?: number; start?: string; end?: string };
```

---

## 🤖 Focus Mode feature guidance

Focus Mode is special because it’s **policy-bound**.

UI responsibilities:
- render chat + streaming responses (if supported)
- render citations as footnotes / chips
- allow users to open source detail panels (dataset/document metadata)
- handle refusal states cleanly (“no sources found”)

UX pattern suggestion:
- show a small “Evidence” area below each assistant message
- allow expanding it to reveal:
  - dataset title + license
  - document excerpt
  - geo/time scope used for retrieval

---

## ♿ UX / Accessibility guardrails

Use these as “definition-of-done” checks:

- ✅ Buttons look clickable and have hover/focus states
- ✅ Forms have labels + error messaging
- ✅ Content works on narrow screens (no horizontal scrolling)
- ✅ Keyboard-only navigation works end-to-end
- ✅ Map controls remain usable on touch devices
- ✅ Color is not the only signal (icons/labels/patterns)

---

## ⚡ Performance guardrails

- Prefer **vector tiles / server filtering** over giant GeoJSON payloads
- Debounce search & map-move triggered requests
- Virtualize long lists (catalog results, document lists)
- Code-split heavy routes (Map, Cesium, Focus Mode)
- Avoid expensive re-renders: memoize selectors, use stable callbacks

---

## 🧪 Testing expectations

- `utils/` → unit tests
- `state/` → reducer/action tests
- `hooks/` → hook tests (mock services)
- `routes/` → integration tests (render + user flows)
- smoke test: “load app, toggle layer, move time, open citation”

---

## ✅ Quick “Where do I put this?” guide

| If you’re adding… | Put it in… |
|---|---|
| a reusable UI button used everywhere | `web/src/components/` |
| a map-layer toggle panel | `features/layers/components/` |
| a “fetch datasets” call | `features/catalog/services/` |
| a shared API client wrapper | `web/src/lib/api/` |
| a Kansas-specific formatting helper | `features/<domain>/utils/` |
| a global app setting | `web/src/state/` (or app-level store) |

---

## 🧭 Conventions

- Folder names: `kebab-case` (e.g., `focus-mode`, `map-viewer`)
- Components: `PascalCase.tsx`
- Hooks: `useSomething.ts`
- Keep `index.ts` clean (public exports only)
- No cross-feature deep imports

---

## 🙋 FAQ

### “My feature needs to share logic with another feature.”
If it’s truly reusable:
- move it to `shared/` or `lib/`
If it’s only used by two features but still domain-specific:
- consider a small **domain module** rather than duplicating

### “Where do I put assets (icons/images)?”
- Feature-only assets: `features/<feature>/assets/`
- Global assets: `web/src/assets/`

---

> 🧠 Keep it boring. Predictable structure is a superpower.