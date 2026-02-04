# 🧱 Layout Components (KFM Web)

> **Purpose:** Layout components define the *shape* of the UI (shell, regions, panels, responsive behavior) — not the *meaning* (business logic, domain rules, data fetching).

---

## 🗺️ The KFM UI in one breath

KFM is a pipeline→catalog→database→API→UI system where **governed artifacts** flow forward and the UI is the downstream consumer.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

The `web/` directory is the canonical home for the client application (React + map configuration, etc.).  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧭 Contents

- [System boundaries (non‑negotiables)](#-system-boundaries-nonnegotiables)
- [What belongs in `layout/`](#-what-belongs-in-layout)
- [Recommended structure](#-recommended-structure)
- [Key patterns](#-key-patterns)
- [Example: composing an app shell](#-example-composing-an-app-shell)
- [Do / Don’t](#-do--dont)
- [Accessibility checklist](#-accessibility-checklist)
- [Performance checklist](#-performance-checklist)
- [Related docs](#-related-docs)

---

## 🔒 System boundaries (non‑negotiables)

### ✅ API boundary (UI never talks to databases)

The UI **must not** query PostGIS/Neo4j directly; all access is mediated through the backend API enforcement layer.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Implication for layout components:**
- Layout components **do not fetch** domain data.
- Layout components may host *containers* that use hooks/services, but the fetching logic should live outside `layout/` (e.g., `features/`, `pages/`, or `services/`).

### 🧾 Canonical “truth path” (don’t short-circuit governance)

KFM treats any shortcut around the system flow as a smell (raw → processed → catalog/prov → database → API → UI).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Layout components should therefore:
- Render “safe defaults” when data is missing (empty states, skeletons)
- Never invent data to fill gaps (that belongs upstream in pipelines/catalogs)

### 🗺️ Mapping is “just another API product”

The API serves map tiles for vector and raster layers, intended for map clients like MapLibre.  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
KFM’s prototype and design notes specifically call out MapLibre + timeline controls as first-class UI needs.  [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

**Implication for layout components:**
- Reserve stable space for a `MapViewer` region (avoid unmount/remount thrash)
- Treat panels as overlays/docks, not reflows that resize the map every frame

---

## 📦 What belongs in `layout/`

Think of `layout/` as **UI plumbing** 🪠:

- **Shells & wrappers** (page chrome)
  - `AppShell`, `BareShell`, `AuthenticatedShell`
- **Regions** (where things go)
  - `Header`, `Footer`, `Main`, `Aside`, `StatusBar`
- **Panel systems** (dock/overlay)
  - `LeftRail`, `RightPanel`, `BottomDrawer`, `ResizableSplit`
- **Responsive primitives**
  - `Drawer`, `Sheet`, `SafeArea`, `useBreakpoint()`
- **Interaction affordances that are layout-shaped**
  - skip links, top-level focus traps, “panel open” transitions

> KFM’s frontend blueprint lists reusable components like MapViewer, TimelineSlider, StoryPanel, SearchBar, and LayerControl. Layout components *make room* for these and orchestrate how they coexist.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧱 Recommended structure

This is a **suggested** folder layout for predictability (adapt as the codebase evolves):

```text
📁 web/src/components/layout/
├─ 📄 README.md                  ← you are here 👋
├─ 📁 shell/                     App shells and top-level wrappers
├─ 📁 regions/                   Header/Main/Footer/etc (landmarks)
├─ 📁 panels/                    Docked/overlay panels + split views
├─ 📁 responsive/                Breakpoints, drawers, safe-area helpers
└─ 📁 primitives/                Small layout-only building blocks
```

Naming ideas (not required, but consistent):
- `XxxLayout.tsx` for a composed layout
- `XxxRegion.tsx` for a landmark wrapper
- `useXxxLayout.ts` for layout-only hooks

---

## 🧩 Key patterns

### 1) Slot-based composition (preferred)

Instead of a “god layout” that imports everything, prefer **slots**:

- Shell owns: spacing, stacking order (z-index), responsiveness
- Feature/page owns: what gets rendered in each slot

Example slot model:
- `header`
- `mapStage`
- `leftPanel`
- `rightPanel`
- `bottomBar`

### 2) Stable map stage + detachable panels

Because map engines keep heavy state (WebGL context, sources, layers), treat the map like a “scene”:
- mount once
- update via props/events
- avoid remount on route changes unless absolutely necessary

### 3) Global UI state belongs in the store, not in layouts

The blueprint expects a global store for shared state like map viewport, selected time, active layers, story-in-view, and auth.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
Layout components can *read* that state for positioning/visibility, but should not become the place where domain behavior lives.

---

## 🧪 Example: composing an app shell

> This is an illustrative example. Adjust names to match your actual components.

```tsx
// web/src/app/App.tsx (example)
import { AppShell } from '../components/layout/shell/AppShell';
import { Header } from '../components/layout/regions/Header';
import { MapStage } from '../components/layout/regions/MapStage';
import { RightPanel } from '../components/layout/panels/RightPanel';
import { BottomBar } from '../components/layout/regions/BottomBar';

import { MapViewer } from '../components/map/MapViewer';
import { TimelineSlider } from '../components/time/TimelineSlider';
import { StoryPanel } from '../components/story/StoryPanel';

export function App() {
  return (
    <AppShell
      header={<Header />}
      mapStage={
        <MapStage>
          <MapViewer />
        </MapStage>
      }
      rightPanel={
        <RightPanel>
          <StoryPanel />
        </RightPanel>
      }
      bottomBar={<BottomBar><TimelineSlider /></BottomBar>}
    />
  );
}
```

---

## ✅ Do / Don’t

### ✅ Do

- **Use landmarks**: `header`, `nav`, `main`, `aside`, `footer`
- **Prefer CSS Grid/Flex** for responsiveness (avoid JS-measured layouts unless needed)
- **Expose slots** and keep shells generic
- **Handle empty states** for panels (collapsed, hidden, loading placeholders)
- **Keep data out**: accept `ReactNode` children or IDs, not query params

### ❌ Don’t

- Don’t fetch datasets or call the DB directly (everything goes through API).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Don’t encode domain rules in layout (“if drought layer then…”). Put that in features.
- Don’t remount heavy components (map engine) as a side-effect of panel toggles.

---

## ♿ Accessibility checklist

- [ ] A skip link is available and visible on focus
- [ ] Panels announce open/close with appropriate ARIA (and don’t steal focus unexpectedly)
- [ ] Focus is trapped in modal overlays (but **not** in docked panels)
- [ ] Keyboard navigation works for: panel toggle, close, “jump to map”, “jump to story”
- [ ] Reduced motion is respected (avoid large parallax/zoom animations)

---

## 🚀 Performance checklist

- [ ] Map stage stays mounted; only its props/state update
- [ ] Panel animations use `transform`/`opacity` (avoid layout thrash)
- [ ] Expensive children are memoized and/or virtualized where needed
- [ ] Resize observers are debounced/throttled
- [ ] Global state updates are scoped (avoid “rerender everything” on every map move)

---

## 🔗 Related docs

- 📘 UI home: `web/`  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🧠 Frontend blueprint (structure + component examples): KFM “Web Frontend (React & TypeScript)” section  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- 🧱 API boundary principle: KFM blueprint intro  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- 🗺️ Tiles and map clients: API docs excerpt  [oai_citation:13‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🧭 Repo structure guidance (governed homes): `MARKDOWN_GUIDE_v13.md.gdoc`  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)