<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Components  
`docs/design/mockups/figma/components/navigation/README.md`

**Interactive · Temporal · Spatial · Intuitive Navigation**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../docs/standards/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🪶 Overview

The **Navigation Components** define the **core exploration and movement interface** for the Kansas Frontier Matrix (KFM) web application — the connective tissue between **space**, **time**, and **knowledge**.  
They synchronize **map**, **timeline**, and **detail panels**, enabling users to traverse centuries of Kansas data with precision and clarity.

- **Design source:** KFM Figma library (shared tokens & primitives)  
- **Implementation:** React / TypeScript under `web/src/components/navigation/`  
- **Standards:** MCP documentation-first, WCAG 2.1 AA, GitHub-safe diagrams

---

## 🧭 Component Hierarchy

docs/design/mockups/figma/components/navigation/
├── README.md
├── header/               # Global top bar: search, tabs, global actions
├── sidebar/              # Layers, filters, legends
├── timeline-controls/    # Time rail, handles, play/pause, zoom in/out
├── map-toolbar/          # Zoom, locate, layers toggle, mode switch
└── panels/               # Detail/context drawers & overlays

> Each folder includes: `README.md` (usage), `props.ts` (types), `*.tsx` (component), `*.test.tsx` (unit tests), and `a11y.md` (patterns).

---

## 🔗 System Integration (Data → State → View)

```mermaid
flowchart LR
  subgraph FE["Frontend (React)"]
    A["Header\nSearch · Tabs · Menus"]
    B["Timeline Controls\nRail · Handles · Zoom"]
    C["Map Toolbar\nZoom · Locate · Layers"]
    P["Detail Panel\nAI Summaries · Metadata"]
  end

  subgraph API["Backend API (FastAPI)"]
    D["GET /events?start&end"]
    E["GET /layers-config"]
    F["GET /entity/{id}"]
  end

  subgraph STATE["Application State (Context/Store)"]
    G["selectedTimeRange"]
    H["activeLayers"]
    I["selectedEntity"]
  end

  subgraph MAP["Renderer (MapLibre)"]
    J["Map View\nLayers & Styling"]
    K["Timeline Markers\nWindow & Highlights"]
  end

  A --> B
  A --> C
  A --> P
  B --> D
  C --> E
  P --> F
  D --> G
  E --> H
  F --> I
  G --> J
  H --> J
  I --> J
  G --> K

Contract: Route responses (Pydantic models) ↔️ TypeScript interfaces guarantee schema parity.

⸻

🧱 Responsive Layout Modes

flowchart TD
  Desk["🖥️ Desktop\nMap + Timeline + Sidebar + Detail Panel"] --> Tab["📱 Tablet\nMap + Toggle Timeline/Panel"]
  Tab --> Mob["📱 Mobile\nMap focus · Slide-up Timeline/Details"]

	•	Desktop: all regions visible; detail panel docks right.
	•	Tablet: timeline collapsible; sidebar overlays.
	•	Mobile: map first; timeline & details as slide-ups with focus management.

⸻

⚙️ State Lifecycle (Deterministic)

stateDiagram-v2
  [*] --> Idle
  Idle --> Loading : fetchData()
  Loading --> Ready : setState(data)
  Ready --> Updating : userInteraction()
  Updating --> Ready : render()

	•	Coalesced updates: batched renders on time-window & layer changes
	•	Idempotent actions: repeatable event → state transitions (MCP reproducibility)

⸻

🎨 Design Tokens (Theme-agnostic)

Token	Example (Dark/Light)	Purpose
--kfm-color-bg	#0b1020 / #ffffff	Background
--kfm-color-fg	#fafafa / #111111	Foreground
--kfm-accent	#22a7f0	Interactive states
--kfm-radius-lg	12px	Rounding scale
--kfm-shadow-md	0 2px 8px rgba(0,0,0,.25)	Elevation

Tokens: web/src/styles/tokens.css (exported to Figma as variables).

⸻

🔌 API Touchpoints

Endpoint	Function	Consumed By
/api/events?start={t0}&end={t1}	Fetch events in time window	Timeline Controls
/api/layers-config	Get map layers & styles	Map Toolbar
/api/entity/{id}	Fetch entity detail panel content	Panels / Drawer

Parity: Pydantic ↔︎ TypeScript types; strict nullability enforced.

⸻

♿ Accessibility (WCAG 2.1 AA)

Area	Technique
Keyboard	Tab/Shift+Tab/Arrows across sliders, menus; Space/Enter to activate
Roles & Names	role="slider", aria-valuenow, aria-controls for timeline; aria-expanded for accordions
Contrast	≥4.5:1; accent passes in both themes
Focus	:focus-visible outline; easy to spot on dark/light
Motion	Reduced motion honors prefers-reduced-motion
Touch	Hit targets ≥44px; drag handles accessible

Audit tools: Axe, Pa11y, Lighthouse (CI); manual keyboard walkthroughs.

⸻

🧪 Testing & QA

Area	Method
Unit	Jest + React Testing Library (input handling, disabled states, aria updates)
E2E	Playwright (search → select → zoom timeline → inspect detail → toggle layer)
Visual	Percy (snapshots per Figma commit ref)
A11y	Axe & Pa11y CI gates; color tokens checked by Stark

CI: .github/workflows/pre-commit.yml and site.yml run full doc + a11y + build checks.

⸻

🔧 Implementation Notes

Header
	•	Search debounced 250ms; result list keyboard-navigable
	•	Tabbed navigation controls route hash (deep linkable)

Timeline Controls
	•	Virtualized ticks; windowed rendering
	•	Drag handles announce aria-valuenow; PageUp/Down for coarse seek
	•	Play/pause uses requestAnimationFrame; pauses on tab blur

Map Toolbar
	•	Layer toggle reads from /api/layers-config and persists to local storage
	•	“Locate” checks permissions; fallback to manual “jump to county”

Detail Panels
	•	Focus trap on open; Esc closes; returns focus to origin
	•	AI summary includes source citations with keyboard nav

⸻

🧩 Integration Notes
	•	State management: lightweight Context + reducers; no global store required
	•	Type safety: zod guards + generated Pydantic typings ensure runtime validation
	•	Error handling: optimistic UI; toast on failure; retriable fetchers
	•	i18n-ready: text labels live in web/src/i18n/strings.ts

⸻

🔐 Governance Metadata

Field	Value
Design Source	Figma — KFM shared library
Frontend Stack	React 18, MapLibre GL, TypeScript 5
Backend Stack	FastAPI + Neo4j (CIDOC CRM / OWL-Time)
Maintainers	KFM Design & Accessibility Team
Last Updated	2025-10
License	CC-BY 4.0


⸻

🧭 Usage Examples (TSX)

Timeline handle (keyboard)

<button
  role="slider"
  aria-valuemin={start}
  aria-valuemax={end}
  aria-valuenow={value}
  aria-label="Timeline start"
  onKeyDown={onKeyDownHandle}
  className="timeline__handle"
/>

Map layer toggle item

<label>
  <input
    type="checkbox"
    checked={active}
    onChange={() => toggleLayer(id)}
    aria-pressed={active}
    aria-label={`Toggle layer ${name}`}
  />
  {name}
</label>


⸻

🧾 Accessibility Audit (Snapshot)

Check	Result	Notes
Keyboard focus order	✅	Logical, no traps
Slider semantics	✅	Roles/values announced
Contrast	✅	All tokens ≥ 4.5:1
Motion	✅	Respects prefers-reduced-motion
Screen reader	✅	Labels & descriptions provided


⸻

📦 Change Log (Design & Code)

Version	Date	Summary	Ref
v1.2	2025-10-05	Added governance, test matrix, and a11y audit section; mermaid fenced; API parity notes.	#nav-126
v1.1	2025-10-04	Token unification; keyboard handling for sliders; tablet layout refinements.	#nav-109
v1.0	2025-10-03	Initial navigation components and Figma linkage.	#nav-087


⸻

🔗 Related Documentation
	•	docs/architecture/web-ui-architecture.md
	•	docs/architecture/api-architecture.md
	•	docs/standards/metadata-standards.md
	•	web/src/components/navigation/*
	•	.github/workflows/pre-commit.yml, site.yml

⸻


<div align="center">


🧭 “Navigation is not motion — it’s understanding.”
The KFM navigation system turns movement into discovery, linking every map layer and historical moment through accessible, intuitive interaction.

</div>

