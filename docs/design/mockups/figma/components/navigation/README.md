# 🧭 Kansas Frontier Matrix — Navigation Components
`docs/design/mockups/figma/components/navigation/`

**Purpose:** Define the UI and interaction model for moving through **time**, **space**, and **story** in the Kansas Frontier Matrix web app.  

---

## 🪶 Overview
Navigation includes:

- **Global Header** — brand, search, menus  
- **Primary Tabs** — Map · Timeline · Stories · Data  
- **Context Rail** — Layers / Filters (left)  
- **Detail Panel** — Entity dossier (right)  
- **Map Toolbar** — Zoom · Locate · Layers  
- **Timeline Controls** — Scrub · Zoom · Play  
- **Breadcrumbs** — Place ▸ Collection ▸ Item  

Each piece is modular and synchronized across devices and views.

---

## 🧩 System Diagram (GitHub-safe Mermaid)

```mermaid
flowchart LR
  subgraph FE["Frontend"]
    A["Header\nbrand · search · menus"]
    B["Timeline\nscrub · zoom · play"]
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



⸻

📁 Directory Structure

navigation/
├── README.md
├── tokens.css
├── NavigationHeader.tsx
├── PrimaryTabs.tsx
├── Breadcrumbs.tsx
├── LeftRail.tsx
├── MapToolbar.tsx
├── TimelineControls.tsx
├── DetailPanel.tsx
├── Navigation.types.ts
├── Navigation.a11y.test.tsx
└── stories/
    └── Navigation.stories.tsx


⸻

🎨 Design Tokens

:root {
  --kfm-nav-h: 56px;
  --kfm-rail-w: 320px;
  --kfm-panel-w: 380px;
  --kfm-gap: 8px;
  --kfm-color-bg: #0b1020;
  --kfm-color-fg: #e6e9f2;
  --kfm-color-accent: #62b0ff;
  --kfm-focus: 2px solid #62b0ff;
}


⸻

♿ Accessibility

Roles

Region	ARIA Role	Label
Header	banner	App header
Tabs	navigation	Primary
Left Rail	complementary	Layers and Filters
Details	region	Details
Timeline	group	Timeline Controls

Keyboard Shortcuts

Action	Keys
Focus search	Alt + /
Close panel	Esc
Cycle focus	F6
Scrub timeline	← / →
Zoom timeline	+ / −
Play / pause	Space


⸻

🧱 Layout Example

.app {
  display: grid;
  grid-template-rows: var(--kfm-nav-h) 1fr auto;
  height: 100vh;
}

.main {
  display: grid;
  grid-template-columns: var(--kfm-rail-w) 1fr var(--kfm-panel-w);
  gap: var(--kfm-gap);
}

@media (max-width: 1024px) {
  .main { grid-template-columns: 1fr; }
  .left-rail, .details { display: none; }
}


⸻

🔌 Component APIs (React)

interface NavHeaderProps {
  onSearch: (q: string) => void;
  tabs: { id: string; label: string; href: string }[];
  activeTabId: string;
}

interface LeftRailProps {
  sections: { id: string; label: string; items: React.ReactNode }[];
  collapsed?: boolean;
  onToggle?: () => void;
}

interface MapToolbarProps {
  onZoomIn: () => void;
  onZoomOut: () => void;
  onLocate: () => void;
  onBasemap: () => void;
  onLayers: () => void;
}

interface TimelineControlsProps {
  range: [number, number];
  value: number;
  onChange: (t: number) => void;
  onZoom: (d: number) => void;
  playing: boolean;
  onTogglePlay: () => void;
}

interface DetailPanelProps {
  title: string;
  onClose: () => void;
  children: React.ReactNode;
  width?: number;
}


⸻

🧪 Testing
	•	Unit – Props, callbacks, disabled states
	•	Accessibility – ARIA labels, focus order
	•	Visual – Storybook regression tests
	•	E2E – Timeline ↔ Map ↔ Details synchronization

⸻

🧭 Figma Handoff
	•	Component names: Nav/Header, Nav/Tabs, Nav/Toolbar, Nav/Timeline, Nav/Panel
	•	Frame sizes: 1440×900 (desktop), 1024×768 (tablet), 375×812 (mobile)
	•	Export icons as SVG, 24×24 grid

⸻

📜 Changelog

Version	Date	Notes
1.0	2025-10-05	Initial GitHub-safe formatting and diagram
