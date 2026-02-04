# 🧩 UI Components (`web/src/components/ui`)

![React](https://img.shields.io/badge/React-UI%20Layer-000000?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-Ready-000000?logo=typescript)
![Map UI](https://img.shields.io/badge/Map%20UI-MapLibre%20%2B%20Optional%20Cesium-000000?logo=openstreetmap)
![Governed](https://img.shields.io/badge/Governance-Evidence--First%20%2B%20API--Boundary-000000)

> This folder is the **reusable UI “kit”** for the KFM frontend.  
> The frontend lives under `web/` and is the **single source of truth** for the user-facing interface—**no hidden data files** and **no direct DB queries** inside the UI. Everything comes through the governed API layer.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧭 Why this folder exists

KFM’s pipeline is **non-negotiable** and the UI is intentionally downstream of contracts + governance:

```mermaid
flowchart LR
  ETL[ETL] --> C[STAC/DCAT/PROV Catalogs]
  C --> G[Neo4j Graph]
  G --> API[API Layer (contracts + redaction)]
  API --> UI[Map UI (React · MapLibre · optional Cesium)]
  UI --> Story[Story Nodes]
  Story --> Focus[Focus Mode]
```

This ordering (and the “truth path”) is core to KFM’s design.  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

✅ The frontend provides **interactive maps, timelines, and story content**  
❌ The frontend **never bypasses the API** (to preserve traceability + enforcement)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📌 Key principles (please don’t “opt out” of these 😄)

### 1) 🧾 Evidence-first UI
- Any UI element that presents “facts” must be displayable **with traceable evidence** (dataset IDs, provenance references, source links).
- “No unsourced narrative” applies to story experiences and anything surfaced in Focus Mode.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) 🛡️ API boundary rule (hard requirement)
- UI components **must not** query Neo4j directly.
- UI components **must** consume data via the governed API layer (`src/server/`) so that policy (redaction/classification) is enforceable.  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) 🧩 Composability over complexity
- Prefer small, predictable “lego-brick” components.
- Compose bigger UX (panels, modals, map toolbars) in feature/page layers, not in primitives.

### 4) ♿ Accessibility by default
- Use semantic HTML to give content meaning, improve accessibility, and keep structure clear.  [oai_citation:7‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)
- Treat keyboard + focus states as **required**, not optional polish.

### 5) 🗺️ Map-first ergonomics
- KFM is map-centric: controls, legends, toggles, and timelines must feel “GIS-grade” while staying approachable.  
- The UI layer includes a **layer registry**, accessibility audits, and usage analytics hooks as part of its contract surface.  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Recommended folder layout

> This is the intended organization pattern for `ui/`—adjust to match what’s already in the repo.

```text
📁 web/
 └─ 📁 src/
    └─ 📁 components/
       └─ 📁 ui/
          ├─ 📄 README.md                # ← you are here
          ├─ 📄 index.ts                 # barrel exports (recommended)
          ├─ 📁 primitives/              # buttons, inputs, typography, icons
          ├─ 📁 feedback/                # toast, alert, loading, empty states
          ├─ 📁 layout/                  # stack, grid, panel, splitter, resizable
          ├─ 📁 map/                     # legend, layer toggle, scale, coord readout
          ├─ 📁 story/                   # evidence cards, citations, source chips
          └─ 📁 internal/                # private helpers (not part of public UI API)
```

---

## 🧱 Component taxonomy

| Bucket 🧺 | What goes here | Notes |
|---|---|---|
| `primitives/` 🧱 | `Button`, `Input`, `Select`, `Tabs`, `Tooltip` | No business logic, minimal dependencies |
| `layout/` 🧩 | `Panel`, `Drawer`, `SplitPane`, `Stack` | Layout-only; avoid data fetching |
| `feedback/` 🚦 | `Toast`, `Alert`, `Skeleton`, `Progress` | Standardize UX for errors/loading |
| `map/` 🗺️ | `LayerToggle`, `Legend`, `TimelineScrubber` | Must respect governance & redaction |
| `story/` 📚 | `EvidenceCard`, `CitationList`, `SourceBadge` | Evidence-first patterns |

---

## 🔌 Usage

### Prefer barrel exports (recommended)
Create/maintain `web/src/components/ui/index.ts`:

```ts
// web/src/components/ui/index.ts
export * from "./primitives/Button";
export * from "./feedback/Toast";
// ...
```

Then use:

```tsx
import { Button } from "../../components/ui"; // or your alias-based import
```

> Keep import paths stable: UI primitives are foundational and used everywhere.

---

## 🎨 Styling conventions

### ✅ Use scoped styling (CSS Modules pattern)
CSS Modules are a clean default for local styles (scoped class names, easy imports):  [oai_citation:9‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)

```tsx
import styles from "./Button.module.css";

export function Button(props) {
  return <button className={styles.button} {...props} />;
}
```

> If you use a utility framework or design tokens, keep the same spirit: **avoid global CSS collisions** and keep styles near the component.

### 🧠 Keep structure readable
A good UI codebase stays maintainable when HTML/CSS are modular and organized.  [oai_citation:10‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

---

## ♿ Accessibility checklist (minimum bar)

- ✅ Semantic elements first (`button`, `nav`, `header`, `main`, `section`, `label`, etc.) for meaning + accessibility.  [oai_citation:11‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)
- ✅ Keyboard support:
  - `Tab` reaches it
  - `Enter/Space` activates it (if interactive)
  - focus ring is visible
- ✅ ARIA only when needed:
  - don’t replace semantics with ARIA
  - keep `aria-*` values synchronized with state
- ✅ Color/contrast:
  - avoid “color-only” meaning
  - provide text or icon cues

---

## 🗺️ Map UI patterns (KFM-specific)

### Map engine expectations
- KFM uses **MapLibre GL JS** for interactive 2D maps and may support **CesiumJS** for 3D views.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Data layers may come from:
  - tile endpoints (vector/raster), e.g. `/api/tiles/<layer>/{z}/{x}/{y}.pbf`
  - GeoJSON overlays (for smaller payloads)  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### State synchronization pattern
UI state should let disparate components stay in sync—e.g., timeline updates a `currentYear`, and both map + story panel respond.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Guideline:**  
- Put *global* state in a store/context/hook layer (not inside `ui/` primitives).
- Keep `ui/` components pure: they receive state + callbacks as props.

### Legend & symbology
When multiple layers are visible, the UI should provide a legend/layer control that reflects symbology.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Practical rules of thumb:**
- Legends must match actual map styling (don’t hardcode colors in 2 places).
- Support “long names” and metadata (source, year range, uncertainty).

### Labeling / type placement (avoid “map soup”)
Automated labeling must be evaluated for clarity and legibility.  [oai_citation:16‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

If you build UI for labels/tooltips:
- prefer collision-safe placement
- keep text legible across zoom levels
- don’t hide critical features behind labels

---

## 🔐 Security & sensitive data handling

### Token storage (⚠️ don’t ship risky patterns)
Storing API tokens in `localStorage` is risky: tokens are exposed to XSS, and it doesn’t enforce safe transfer (HTTPS). Consider stronger approaches (e.g., cookies/JWT strategies) for real security.  [oai_citation:17‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

**UI rule:**  
- `ui/` components **must not** “invent auth.” They should use the app’s auth/session utilities.

### Classification propagation (governance must flow end-to-end)
Outputs must not be less restricted than inputs; UI must implement safeguards (e.g., redaction behavior such as blurring/generalizing sensitive locations).  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Testing & documentation expectations

### What every “public” UI component should ship with
- ✅ Basic rendering test (smoke)
- ✅ Accessibility sanity checks (roles/labels; keyboard where relevant)
- ✅ Story/demo (Storybook or internal examples—whatever the repo uses)
- ✅ `index.ts` export (if component is part of the public UI API)

### What “map UI” components additionally need
- ✅ Controlled props (no hidden fetches)
- ✅ Handles empty/error states gracefully
- ✅ Works across zoom levels and different basemap themes

---

## 🛠️ Creating a new component (template)

### 1) Create the folder
```text
📁 web/src/components/ui/primitives/MyThing/
 ├─ 📄 MyThing.tsx
 ├─ 📄 MyThing.module.css
 ├─ 📄 index.ts
 └─ 📄 MyThing.test.tsx
```

### 2) Implement (keep it dumb, composable)
```tsx
// MyThing.tsx
type MyThingProps = {
  label: string;
  onClick?: () => void;
  disabled?: boolean;
};

export function MyThing({ label, onClick, disabled }: MyThingProps) {
  return (
    <button type="button" onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

### 3) Export it
```ts
// index.ts
export * from "./MyThing";
```

---

## ✅ PR checklist (UI folder)

- [ ] No direct DB access / no bypassing API boundary  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Evidence-first: data shown can be traced (IDs, sources, provenance)
- [ ] Accessible semantics + keyboard support  [oai_citation:20‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)
- [ ] Styling is scoped (no “surprise” globals)  [oai_citation:21‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)
- [ ] Map-related UI respects redaction/classification propagation  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Tests added/updated
- [ ] Docs/demo updated

---

## 📚 Project references (source-of-truth docs)

- 📘 **KFM Master Guide v13** — canonical pipeline ordering + UI boundary rules.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🧭 **KFM Technical Blueprint** — frontend behavior (maps/timelines), MapLibre/Cesium notes.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- 🗺️ **Making Maps (GIS map design)** — labeling & legibility heuristics for map UI.  [oai_citation:28‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  [oai_citation:29‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
- 🧱 **HTML/CSS structure** — semantic markup + modular organization reminders.  [oai_citation:30‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  [oai_citation:31‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)
- 🔐 **Client token storage caution** — localStorage risks for tokens (don’t ship this casually).  [oai_citation:32‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  [oai_citation:33‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)