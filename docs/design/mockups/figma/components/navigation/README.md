🧭 Kansas Frontier Matrix — Navigation Components

docs/design/mockups/figma/components/navigation/README.md

Goal: Define the information architecture and reusable UI parts for navigating the KFM web app (timeline ↔ map ↔ detail views), with GitHub‑safe diagrams, accessible patterns, and copy‑paste code snippets.

⸻

1) Overview

The Navigation set provides consistent affordances for moving through time, space, and stories:
	•	Global header (brand, search, app‑level menus)
	•	Primary tabs (Map, Timeline, Stories, Data)
	•	Context rail (left) for layers/filters
	•	Detail panel (right) for entity dossiers
	•	Map toolbar (zoom, locate, measure, basemap, layers)**
	•	Timeline controls (scrub, zoom, play/pause, jump‑to)
	•	Breadcrumbs (Place ▸ Collection ▸ Item)

Each element is modular and responsive; together they synchronize the user’s temporal window, spatial extent, and selected entity.

⸻

2) What “good” looks like
	•	Discoverable: core actions visible at a glance; secondary actions progressively disclosed.
	•	Focusable: keyboard and screen‑reader compatible (tab order, ARIA roles, visible focus).
	•	Stable: layout persists across pages; only content changes.
	•	Contextual: timeline, map, and details always reflect the same selection state.

⸻

3) GitHub‑safe System Diagram (Mermaid)

flowchart LR
  subgraph FE["Frontend"]
    A["Header\nbrand · search · menus"]
    B["Timeline Controls\nscrub · zoom · play"]
    C["Map Toolbar\nzoom · locate · layers"]
    D["Left Rail\nlayers · filters"]
    E["Detail Panel\nentity dossier"]
  end

  subgraph API["Backend API"]
    F["GET /events?start&end"]
    G["GET /layers-config"]
    H["GET /entity/{id}"]
  end

  subgraph STATE["Client State"]
    I["selectedTimeRange"]
    J["activeLayers"]
    K["selectedEntity"]
  end

  A --> B
  A --> C
  A --> D
  B --> F
  C --> G
  E --> H
  F --> I
  G --> J
  H --> K
  I --> C
  I --> B
  J --> C
  K --> E

<!-- END OF MERMAID -->


Notes: All labels with punctuation are quoted; explicit <!-- END OF MERMAID --> marker ensures GitHub’s renderer finishes correctly.

⸻

4) Files & Structure

navigation/
├─ README.md                  # this file
├─ tokens.css                 # CSS custom properties (colors, spacing, z‑index)
├─ NavigationHeader.tsx       # brand, search, menus
├─ PrimaryTabs.tsx            # Map | Timeline | Stories | Data
├─ Breadcrumbs.tsx            # hierarchical context
├─ LeftRail.tsx               # layers & filters
├─ MapToolbar.tsx             # zoom/locate/measure/basemap
├─ TimelineControls.tsx       # scrub/zoom/play/jump
├─ DetailPanel.tsx            # entity dossier shell
├─ Navigation.types.ts        # shared types & enums
├─ Navigation.a11y.test.tsx   # keyboard & aria tests
└─ stories/
   └─ Navigation.stories.tsx  # Storybook scenarios


⸻

5) Design Tokens (CSS variables)

Use a single source of truth (light/dark aware):

:root{
  --kfm-nav-h: 56px;
  --kfm-rail-w: 320px;
  --kfm-panel-w: 380px;
  --kfm-gap: 8px;
  --kfm-color-bg: #0b1020; /* dark */
  --kfm-color-fg: #e6e9f2;
  --kfm-color-muted: #9aa4b2;
  --kfm-color-accent: #62b0ff;
  --kfm-focus: 2px solid #62b0ff;
}
@media (prefers-color-scheme: light){
  :root{ --kfm-color-bg:#ffffff; --kfm-color-fg:#172033; --kfm-color-muted:#5a6573; }
}


⸻

6) Accessibility & Keyboard Maps

Roles
	•	Header: role="banner"
	•	Primary nav: role="navigation" + aria-label="Primary"
	•	Left rail: role="complementary" + aria-label="Layers and Filters"
	•	Detail panel: role="region" + aria-label="Details"
	•	Timeline group: role="group" + aria-label="Timeline Controls"

Keyboard
	•	Global: Alt+/ focus search; Esc close open panels; F6 cycle header ↔ rail ↔ map ↔ timeline ↔ details.
	•	Tabs: Arrow keys move among tabs; Enter selects; Home/End jump.
	•	Timeline: ←/→ scrub; Shift+←/→ coarse scrub; +/− zoom; Space play/pause.
	•	Map toolbar: + zoom in, - out, l locate, m basemap menu.

Focus
	•	Use visible outlines: outline: var(--kfm-focus); outline-offset: 2px;
	•	Ensure trap & restore: opening Detail Panel traps focus; closing returns focus to invoker.

⸻

7) Component API (React)

<NavigationHeader />

interface NavHeaderProps {
  onSearch:(q:string)=>void
  tabs: { id:string; label:string; href:string }[]
  activeTabId:string
}

<LeftRail />

interface LeftRailProps {
  sections: Array<{ id:string; label:string; items:React.ReactNode }>
  collapsed?: boolean
  onToggle?: () => void
}

<MapToolbar />

interface MapToolbarProps {
  onZoomIn:()=>void; onZoomOut:()=>void; onLocate:()=>void;
  onBasemap:()=>void; onLayers:()=>void
}

<TimelineControls />

interface TimelineControlsProps {
  range:[number,number]; value:number;
  onChange:(t:number)=>void; onZoom:(d:number)=>void; playing:boolean; onTogglePlay:()=>void
}

<DetailPanel />

interface DetailPanelProps {
  title:string; onClose:()=>void; children:React.ReactNode; width?:number
}


⸻

8) Layout Recipes

App shell (CSS grid)

.app{ display:grid; grid-template-rows: var(--kfm-nav-h) 1fr auto; height:100dvh; }
.main{ display:grid; grid-template-columns: var(--kfm-rail-w) 1fr var(--kfm-panel-w); gap:var(--kfm-gap); }
.header{ grid-row:1; }
.left-rail{ grid-column:1; }
.map{ grid-column:2; }
.details{ grid-column:3; }
.timeline{ grid-row:3; grid-column:1 / span 3; }
@media (max-width: 1024px){ .main{ grid-template-columns: 1fr; } .left-rail,.details{ display:none; } }


⸻

9) Content Guidelines
	•	Labels: short verb‑first (e.g., Add layer, Export KML).
	•	Empty states: provide guidance and a primary action.
	•	Errors: human‑readable messages + retry; never dead‑end.
	•	Loading: skeleton in panel; shimmer for list; spinner only if brief.

⸻

10) Do / Don’t

Do
	•	Keep primary actions in fixed positions (top left/right, bottom bar on mobile)
	•	Mirror states across surfaces (selected entity appears in header breadcrumbs, detail panel title)
	•	Provide direct links (deep‑linkable URLs for entities/times)

Don’t
	•	Hide critical actions behind more than one disclosure
	•	Use only color for state (add icon/label; meet contrast ratios)
	•	Reflow the header on every route; reserve animation for content

⸻

11) Testing & QA
	•	Unit: props, callbacks, disabled/readonly states
	•	A11y: axe/pa11y pass; keyboard paths; ARIA roles/labels present
	•	Visual: Storybook regression per component state (light/dark, compact/comfortable)
	•	E2E: map ↔ timeline ↔ details synchronization (playback, selection, back/forward)

⸻

12) Figma Handoff
	•	Components named Nav/Header, Nav/Tabs, Nav/Toolbar, Nav/Timeline, Nav/Panel
	•	Use Auto‑layout; frame sizes: 1440×900 (desktop), 1024×768 (tablet), 375×812 (mobile)
	•	Export tokens as CSS variables; export icons as SVG (24×24 grid)

⸻

13) Change Log
	•	v1.0: Initial GitHub‑safe README, component API, Mermaid diagram, a11y patterns.

⸻

14) References
	•	HTML5 semantics & ARIA landmarks (for roles and keyboard navigation)
	•	KFM architecture (integration points: /events, /layers-config, /entity/{id})
	•	WCAG 2.2 AA color & focus guidance
