# 🧩 `web/src/components` — KFM UI Component System

![React](https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/TypeScript-typed-3178C6?logo=typescript&logoColor=fff)
![Mapping](https://img.shields.io/badge/Maps-MapLibre%20%2B%20Cesium-2E7D32?logo=mapbox&logoColor=fff)
![Architecture](https://img.shields.io/badge/Architecture-layered%20%26%20provenance-6A1B9A)
![A11y](https://img.shields.io/badge/A11y-keyboard%20%2B%20ARIA-0B7285)

> Reusable UI building blocks for **Kansas Frontier Matrix (KFM)** — the React/TypeScript front-end that powers the map-centric experience (2D/3D), storytelling, search, layer toggles, and Focus Mode chat.

---

## 🧭 What belongs in `components/`

This directory is for **reusable UI components** that can be composed into features/screens. Think:
- 🗺️ **Map-centric UI**: map viewer shell, legends, layer controls, feature popovers
- 🧵 **Narrative UI**: story panels, chapter navigation, scroll-to-map sync controls
- 🕰️ **Temporal UI**: timeline slider, time scrubber, year badges
- 🔎 **Discovery UI**: search bar, filters, catalog cards
- 🤖 **Focus Mode UI**: chat window, citations panel, tool/result renderers
- 🧱 **Shared primitives**: buttons, modals, drawers, tooltips, toasts, skeletons

✅ If you can reuse it in 2+ places, it’s probably a `component`.

🚫 If it’s page routing, app-wide providers, or backend orchestration, it likely belongs elsewhere (e.g., `pages/`, `routes/`, `store/`, `services/`, `features/`).

---

## 🏗️ Architectural contract (non‑negotiables)

KFM’s UI is part of a **layered system**. Components must **respect boundaries**:

### 1) UI never talks to the model directly 🤖🚫
The front-end should **not** call Ollama/LLMs directly. Focus Mode UI calls the **backend API** (e.g. `/focus-mode/query`) and renders results.

### 2) UI stays “data-store agnostic” 🧠➡️🌐
Components should not “know” Neo4j/PostGIS/Search Index details. They consume **API-shaped data** (DTOs) via `services/` + hooks.

### 3) Trust UX: provenance is a feature 🧾✨
When you render historical/geospatial claims, always provide pathways to:
- dataset/story/source metadata
- licensing
- “why this is shown / why it’s hidden”
- time + geography filters used

---

## 🗂️ Suggested folder layout

> This is the recommended taxonomy for keeping map + narrative + AI UI maintainable.

```text
web/src/components/
  🧱 ui/                      # Design-system-ish primitives (Button, Modal, Tooltip, Toast)
  🗺️ map/                     # MapLibre/Cesium wrappers + map UI (Legend, Popup, LayerStack)
  🧭 navigation/              # App chrome (Sidebars, Panels, Tabs, Split panes)
  🕰️ time/                    # TimelineSlider, TimeRangePicker, YearPill
  🔎 search/                  # SearchBar, FilterChips, ResultList, EmptyState
  📚 story/                   # StoryPanel, SectionNav, ScrollSyncIndicator
  🧾 provenance/              # SourceBadge, CitationList, LicenseBadge, RestrictedNotice
  🤖 focus-mode/              # Chat UI + result renderers + citations panel
  🧩 layout/                  # Layout scaffolds (Resizable panels, Responsive grids)
  🧪 __tests__/               # Cross-component tests (optional)
  📦 index.ts                 # Barrel exports (optional; see guidance below)
```

> 📝 You can deviate, but **keep grouping by responsibility** (map, story, search, time, provenance, AI), not by file type.

---

## 🧩 Component package standard (template)

Each “real” component should live in its own folder:

```text
SomeComponent/
  SomeComponent.tsx
  SomeComponent.types.ts
  SomeComponent.module.css        # or .scss / styled solution used by the project
  SomeComponent.test.tsx          # RTL preferred
  SomeComponent.stories.tsx       # if Storybook is used
  index.ts                        # export { SomeComponent }…
```

### Minimal TypeScript component skeleton

```tsx
import React from "react";
import type { SomeComponentProps } from "./SomeComponent.types";
import styles from "./SomeComponent.module.css";

export function SomeComponent({ title, children }: SomeComponentProps) {
  return (
    <section className={styles.root} aria-label={title}>
      <header className={styles.header}>
        <h2 className={styles.title}>{title}</h2>
      </header>
      <div className={styles.body}>{children}</div>
    </section>
  );
}
```

✅ Prefer **named exports** in shared component libraries for refactor safety.

---

## 🧠 State & data flow rules

### ✅ Prefer “presentational-by-default”
- Components should primarily render based on `props`.
- “Smart” wiring should live in **hooks** and **feature containers**.

### ✅ If global state is required
Use the project’s global store pattern:
- selectors/hooks like `useAppSelector`, `useAppDispatch`, or context hooks
- keep “map viewport”, “current year”, “active layers”, “current story section” in global state
- components should subscribe via hooks, not import the store directly

### ✅ Data fetching belongs in hooks/services
**Components should not `fetch()` directly** (except very small, internal demo cases). Prefer:
- `services/api.ts` (or equivalent)
- `useQuery`/`useMutation` patterns if the stack includes them
- cancellation + loading + error states handled consistently

---

## 🗺️ Map components: MapLibre/Cesium guardrails

Map libraries are **imperative**. Wrap them carefully so React stays stable.

### ✅ Do
- hold map instances in a `ref`
- isolate side effects in `useEffect`
- **clean up** listeners + map instances on unmount
- push expensive work down into map-native layers (vector tiles) where possible
- keep a clear boundary between:
  - “UI state” (React) and
  - “render state” (MapLibre/Cesium)

### 🚫 Don’t
- rebuild the map on every render
- pipe huge GeoJSON blobs into props repeatedly
- bind unbounded event listeners without cleanup

### 🧭 Layer UX expectations
- `LayerControl` should reflect active layers + symbology (Legend)
- layer toggles should show “restricted/aggregated” status when applicable
- keep “loading layer…” state visible (skeleton + progress where possible)

---

## 🤖 Focus Mode UI: rendering rules

Focus Mode components should assume:
- responses come from the **API orchestrator**
- the UI may receive:
  - an answer text
  - supporting citations
  - tool outputs (datasets, map layers, story excerpts)
  - policy restrictions (“can’t show exact location”)

### Recommended Focus Mode component split
- `FocusChatShell` (layout + panels)
- `ChatMessageList`
- `ChatComposer`
- `ToolResultRenderer/*` (maps tool results to UI renderers)
- `CitationDrawer` (source list + deep links)
- `PolicyNotice` (why something is hidden, what to do next)

---

## 🧾 Provenance, policy, and sensitive data UX

KFM follows **FAIR + CARE** governance patterns, which impacts how the UI must behave. ✨

### UI responsibilities ✅
- If a dataset/story/layer is **restricted**, do not “fail silently.”
  - show a `RestrictedNotice` component
  - explain **what** is restricted and **why**
  - suggest next steps (request access, use aggregated view, etc.)
- If sensitive locations must be protected:
  - render generalized/aggregated geometry where required (e.g., county-level)
  - label the visualization as **generalized** (avoid misleading precision)
- For distressing or sensitive historical content:
  - show a `ContentWarningBanner` before details
  - allow users to proceed intentionally

### “Trust UX” patterns to standardize
- `SourceBadge` on cards and panels
- `LicenseBadge` + “usage notes”
- `CitationList` with stable identifiers
- `WhyAmISeeingThis` / `WhyIsThisHidden` drawers

---

## ♿ Accessibility baseline

All components should be usable via keyboard and readable by screen readers.

✅ Requirements:
- Use semantic HTML (`button`, `label`, `nav`, `main`, `section`)
- Never use clickable `div` without role + keyboard handlers (and prefer not to)
- Inputs must have labels
- Dialogs must trap focus and restore it on close
- Ensure visible focus rings

---

## ⚡ Performance guidelines (maps + big data)

KFM is data-heavy. Components must keep the UI responsive:
- virtualize long lists (`ResultList`, catalog browsing, layer lists)
- debounce search inputs
- memoize expensive render computations
- avoid prop-churn (stable references for handlers and objects)
- prefer streaming/tiles from the API for large geodata sets

---

## 🧪 Testing expectations

### Unit/component tests (preferred)
- React Testing Library style tests
- validate:
  - rendering states (loading/empty/error)
  - keyboard navigation
  - policy notices
  - essential interactions (toggle layer, select year, open citation drawer)

### Map tests (pragmatic)
- mock MapLibre/Cesium wrappers
- test the wrapper API (your code), not the mapping engine itself

---

## ✅ “Add a component” checklist

When you add or update components:

- [ ] Folder + file names in **PascalCase**
- [ ] Component is reusable (or you placed it in a feature folder instead)
- [ ] Props are typed (`.types.ts`)
- [ ] Loading/empty/error states included (where relevant)
- [ ] Accessibility checked (keyboard + ARIA)
- [ ] Provenance hooks included (citations/source badges) when rendering claims
- [ ] Sensitive data behaviors respected (restricted/aggregated/warnings)
- [ ] Tests added/updated
- [ ] Export path is clean (`index.ts` or direct import), no circular deps

---

## 🔗 Related docs (in-repo)

- 📚 `docs/architecture/` (system overview, policies, data governance)
- 🤖 `docs/architecture/ai/` (Focus Mode / orchestration)
- 🧠 `web/src/store/` or `web/src/state/` (global state patterns)
- 🌐 `web/src/services/` (API client + request helpers)

> If these links move, update them here — this README is meant to be the “home base” for UI composition.
