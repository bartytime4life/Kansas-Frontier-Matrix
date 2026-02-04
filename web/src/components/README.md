<div align="center">

# 🧩 `web/src/components`  
### Kansas Frontier Matrix (KFM) — Reusable UI Building Blocks 🌾🗺️

![React](https://img.shields.io/badge/React-SPA-61DAFB?logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-typed-blue?logo=typescript&logoColor=white)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20maps-2E7D32)
![CesiumJS](https://img.shields.io/badge/CesiumJS-3D%20globe-263238)
![Evidence First](https://img.shields.io/badge/Evidence--First-%F0%9F%94%8D%20Citations%20Required-important)
![API Only](https://img.shields.io/badge/Truth%20Path-API%20%E2%86%92%20UI-success)

</div>

> **According to a documentation snapshot imported on Feb 4, 2026**, the KFM UI is *evidence-first*: every map layer, chart, and AI answer must remain traceable to sources, following a strict “truth path” from governed APIs to the UI.  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🎯 What this folder is for

This directory contains **reusable, composable UI components** used across the KFM React/TypeScript app: maps, panels, timeline controls, story/scrollytelling widgets, Focus Mode UI, and shared primitives.

KFM’s front-end is described as a **React + TypeScript SPA** with:
- **MapLibre GL JS** for 2D maps
- **CesiumJS** for 3D globe/terrain
- **Timeline sliders/animations** for time-based exploration
- A **Story Node viewer** enabling “scrollytelling” (narrative text drives map state)
- A **global store** (Redux or Context API) to keep components synchronized
- **API-only communication** (REST/GraphQL), *never* direct DB/file access  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 What goes where (components vs everything else)

**✅ Put it in `components/` when:**
- It’s reusable in more than one route/screen
- It’s a UI building block (map panel, timeline control, citation chip, modal, chart wrapper)
- It has a clean, prop-driven interface
- It can be documented and tested in isolation

**❌ Don’t put it in `components/` when:**
- It’s a full page/route container (belongs in `pages/` / `routes/` / `views/`)
- It’s a data-fetching/service module (belongs in `services/`, `api/`, `lib/`)
- It’s a generic hook (belongs in `hooks/`)
- It’s domain logic (belongs in `domain/` / `state/` / `store/`)

> **Rule of thumb:** components *render* and *compose*; services *fetch*; state *coordinates*.

---

## 🗂️ Suggested folder layout (recommended ✨)

> This is a **suggested** taxonomy for long-term maintainability — adopt it gradually as the component library grows.

```text
web/src/components/
  🧱 ui/                  # small primitives (Button, Card, Modal, Tabs, Toast…)
  🧩 layout/              # app shell pieces (Panels, Splitters, Drawers…)
  🗺️ map/                 # MapLibre/Cesium wrappers + legends + layer panels
  ⏳ time/                # timeline slider, playback controls, time scrubbers
  📖 story/               # Story Node viewer + scrollytelling helpers
  🤖 focus-mode/          # chat UI, citations, sources list, safety affordances
  🧾 provenance/          # source badges, citation chips, audit/meta displays
  🧪 dev/                 # demo-only helpers (storybook fixtures, mock panels)
```

---

## 🧱 Component packaging standard (per component)

Use a **folder-per-component** pattern for anything non-trivial:

```text
SomeComponent/
  📄 SomeComponent.tsx
  🎨 SomeComponent.module.css        # or .scss if we standardize it
  🧪 SomeComponent.test.tsx
  🧾 SomeComponent.types.ts          # optional
  🧩 index.ts                        # re-export surface
```

### Naming conventions 🏷️
- Components: **PascalCase** (`StoryNodeViewer`, `TimelineSlider`)
- Files: match component (`StoryNodeViewer.tsx`)
- CSS modules: `ComponentName.module.css`
- Exports: use `index.ts` barrel exports for ergonomic imports

> Consistent naming & clean structure improve usability and navigation in any system.  [oai_citation:3‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

---

## 🔌 Data + state rules (KFM “truth path”)

### 1) UI must be API-only ✅
The UI **must never** query databases or read server files directly — access is routed through the governed API layer.  [oai_citation:4‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Component implication:**  
- Presentational components shouldn’t `fetch()` directly unless they are explicitly *containers* (and even then, prefer calling a typed API client).
- Use a `services/apiClient` (or equivalent) and pass results down as props.

### 2) Keep UI in sync via a global store 🧠
KFM describes using a **global store** (Redux or Context API) so a timeline year change updates maps *and* charts together.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Component implication:**
- “Leaf” components prefer local state
- “Coordinator” components subscribe to global state and distribute props downward
- Avoid **prop drilling** past 2–3 layers; prefer selector hooks

---

## 🤖 Focus Mode UI rules (citations, safety, trust)

### Evidence-first answers 🧾
KFM’s AI approach enforces that answers must be backed by sources and rendered with citation markers that the UI converts into clickable references.  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Component implication (mandatory):**
- Any component rendering AI output must support:
  - **Citation markers** (e.g., `[1] [2]`) → clickable footnotes
  - A **Sources panel** (titles, dataset IDs, doc IDs, etc.)
  - A “no source” state (see below)

### 🚫 No Source, No Answer (UI behavior)
If the API response has:
- `answer` but **no sources** → render a warning UI and prompt the user to refine the query
- `sources` but missing metadata → render as “Unknown source” and log the defect (don’t silently hide)

### Prompt Gate & request hygiene 🧼
The Focus Mode pipeline includes **prompt sanitization** via a “Prompt Gate” to neutralize malicious input before retrieval/generation.  [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Component implication:**
- Treat the backend as the source of truth for enforcement, but the UI should:
  - Show a clear error state for blocked queries
  - Preserve user text locally (so they can edit/resubmit)
  - Never try to “work around” policy blocks

---

## 🔐 Security & governance (fail-closed mindset)

KFM governance is described as “**fail closed**” (missing metadata/policy violations block by default) with RBAC roles and OPA policy enforcement.  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Component implications:**
- Always handle:
  - `401` → re-auth / login CTA
  - `403` → permission CTA (“request access”, “switch role”, etc.)
  - `404` → missing dataset/story node state
- You may hide UI affordances based on role **for UX**, but never assume front-end hiding equals security.

---

## ♿ Accessibility & semantics (required)

KFM is used by researchers, educators, and the public — accessibility isn’t optional.

### Semantic HTML first 🧱
Semantic HTML is explicitly described as giving content “meaning and structure” so assistive tech and search engines can understand it.  [oai_citation:10‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

**Component rules:**
- Prefer `<button>` over clickable `<div>`
- Use landmarks (`<header>`, `<main>`, `<nav>`, `<aside>`, `<footer>`) in layout components
- Use proper headings hierarchy in panels/modals (`h2`/`h3`, etc.)

### Practical accessibility tips ✅
Accessibility guidance includes alt text, semantic labeling, and `label` / `aria-label` usage for form elements.  [oai_citation:11‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

**Component checklist:**
- Images: `alt=""` for decorative, descriptive `alt` for informational
- Forms: always use `<label>` (or `aria-label` if no visible label)
- Keyboard: tab order is logical; modals trap focus; ESC closes dialogs
- Map UI: ensure legend/layer toggles are keyboard operable and readable

---

## 🗺️ Map components (React + MapLibre + Cesium) — patterns

Map engines are **imperative**; React is **declarative**. Wrap maps as “imperative islands” and keep the bridge clean.

### ✅ Recommended pattern: create once, update via effects
- Create map/globe once on mount
- Store instance in a `ref`
- Apply updates (layers, filters, camera) in separate effects
- Cleanup on unmount

<details>
<summary>🧪 MapLibre wrapper example (template)</summary>

```tsx
import { useEffect, useRef } from "react";
import maplibregl, { Map } from "maplibre-gl";

type Props = {
  styleUrl: string;
  center: [number, number];
  zoom: number;
  onReady?: (map: Map) => void;
};

export function MapLibreView({ styleUrl, center, zoom, onReady }: Props) {
  const elRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<Map | null>(null);

  // Create once
  useEffect(() => {
    if (!elRef.current || mapRef.current) return;

    const map = new maplibregl.Map({
      container: elRef.current,
      style: styleUrl,
      center,
      zoom,
    });

    mapRef.current = map;
    onReady?.(map);

    return () => {
      map.remove();
      mapRef.current = null;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [styleUrl]);

  // Update camera without re-creating the map
  useEffect(() => {
    mapRef.current?.easeTo({ center, zoom, duration: 300 });
  }, [center, zoom]);

  return <div ref={elRef} style={{ width: "100%", height: "100%" }} />;
}
```
</details>

### Timeline ↔ map synchronization ⏳🗺️
Since timeline sliders and animations are first-class UI elements, keep time state in the global store so maps, legends, and charts stay consistent.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📖 Story components (scrollytelling)

KFM describes a Story Node viewer that links narrative text with map states so the map updates as the reader scrolls (“scrollytelling”).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Component implications:**
- Separate:
  - `StoryText` (render narrative, headings, citations)
  - `StoryMapController` (apply map state: extent, layers, time)
  - `StoryProgress` (scroll position → active node)
- Allow deterministic playback (important for demos & reproducibility)

---

## 🧪 Testing expectations

**Minimum expectation for every non-trivial component:**
- Unit tests for rendering and interactions (keyboard + mouse)
- Snapshot tests only for stable primitives (avoid brittle snapshots on complex panels)
- Integration tests for map + timeline + story interactions (best in e2e)

> If a component is critical to “trust” (citations, provenance, role visibility), it **must** be tested.

---

## ✅ PR checklist (paste into your PR description)

- [ ] Component is in the correct subfolder (`ui/`, `map/`, `time/`, `story/`, `focus-mode/`, etc.)
- [ ] Props are typed; no `any` unless justified
- [ ] No direct DB/file access; API-only data flow preserved  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Accessibility: semantic elements + labels + keyboard nav  [oai_citation:15‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444) [oai_citation:16‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
- [ ] Focus Mode output renders citations + sources (or shows “no source” guard UI)  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] Tests added/updated
- [ ] Docs updated (this README or component-level docs as needed)

---

## 🔗 Related docs (project-wide)

KFM documentation emphasizes maintaining architecture docs, dataset notes, and contribution guidelines to keep the project a “living knowledge base.”  [oai_citation:18‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

Suggested neighbors (repo-dependent):
- `docs/architecture/` 📚
- `docs/datasets/` 🗃️
- `CONTRIBUTING.md` 🤝
- `docs/governance/` 🏛️

---

## 📚 Source docs used (from project files)

- Kansas Frontier Matrix Comprehensive System Documentation (PDF)  [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint (PDF)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design (PDF)  [oai_citation:21‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
- Learn to Code HTML & CSS (PDF)  [oai_citation:22‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- Professional Web Design: Techniques and Templates (PDF)  [oai_citation:23‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- Node.js / React / CSS / HTML (PDF)  [oai_citation:24‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
