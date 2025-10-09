<div align="center">

# 📚 Kansas Frontier Matrix — Sidebar Component  
`web/src/components/Sidebar/`

**Layer Management · Legends · Filters · Temporal Context**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **Sidebar Component** serves as the **control and information hub** for the Kansas Frontier Matrix  
interactive map interface. It houses **LayerControls**, **Legends**, and optional **filter panels**  
that let users customize what geospatial and historical data appear on the map.

The Sidebar integrates directly with:
- `LayerContext` for tracking visible layers and opacity.
- `TimelineContext` for time-based filtering of data.
- STAC metadata for populating dynamic legends and dataset descriptions.

It supports **collapsible panels**, **smooth transitions**, and **accessible controls**,  
all built following the **Master Coder Protocol (MCP)** for reproducible, documented design.

---

## 🧱 Directory Structure

```text
web/src/components/Sidebar/
├── Sidebar.tsx           # Main sidebar container
├── SidebarPanel.tsx      # Collapsible section wrapper
├── FilterPanel.tsx       # Optional data filtering (by theme or category)
├── LegendPanel.tsx       # Dynamic STAC-driven map legends
├── styles.scss           # Sidebar-specific styles + responsive layout
└── __tests__/            # Jest + RTL unit tests


⸻

⚙️ Component Architecture

flowchart TD
  SB["Sidebar\n(collapsible panel)"] --> LC["LayerControls"]
  SB --> LP["LegendPanel\n(STAC metadata)"]
  SB --> FP["FilterPanel\n(optional thematic filters)"]
  SB --> CTX["LayerContext · TimelineContext"]
  LC --> MAP["MapView\n(MapLibre)"]
  LP --> MAP
  FP --> MAP
%% END OF MERMAID


⸻

🧩 Key Features

Feature	Description	Data Source
Layer Management	Toggles map overlays, sets opacity, and retrieves metadata.	LayerContext / STAC
Legends	Renders dynamic map legends from STAC metadata assets.	data/stac/catalog.json
Timeline Filtering	Filters layer visibility according to the active timeline range.	TimelineContext
Category Filters	Enables filtering by data domain (climate, treaty, hydrology, etc.).	Local state / STAC tags
Responsive Design	Collapses into bottom drawer on mobile; docked panel on desktop.	CSS + Tailwind breakpoints
Accessibility	Keyboard navigation, ARIA region roles, reduced-motion support.	WCAG 2.1 AA


⸻

💬 Example Implementation

import React from "react";
import { LayerControls } from "../LayerControls";
import { LegendPanel } from "./LegendPanel";
import { FilterPanel } from "./FilterPanel";
import "./styles.scss";

export const Sidebar: React.FC = () => {
  return (
    <aside className="sidebar" role="complementary" aria-label="Map Layers and Filters">
      <header className="sidebar-header">
        <h2>Map Controls</h2>
      </header>
      <section className="sidebar-section">
        <LayerControls />
      </section>
      <section className="sidebar-section">
        <LegendPanel />
      </section>
      <section className="sidebar-section">
        <FilterPanel />
      </section>
    </aside>
  );
};


⸻

🧠 TypeScript Interfaces

export interface SidebarPanelProps {
  title: string;
  isOpen?: boolean;
  children: React.ReactNode;
  onToggle?: () => void;
}

export interface FilterOption {
  id: string;
  label: string;
  category: "climate" | "geology" | "treaty" | "infrastructure" | "archaeology";
  active: boolean;
}


⸻

🧮 Data Flow

sequenceDiagram
  participant U as User
  participant SB as Sidebar
  participant CTX as LayerContext
  participant STAC as STAC Catalog
  participant MAP as MapView

  U->>SB: Toggles "Soil Survey 1967"
  SB->>CTX: updateLayerState(id, active)
  CTX->>MAP: add/remove layer
  SB->>STAC: fetch legend for active layer
  STAC-->>SB: return legend metadata
  SB-->>U: Display legend and layer summary
%% END OF MERMAID


⸻

🎨 Styling & Layout
	•	Base width: 320px (desktop) / 100vw (mobile drawer).
	•	Panels: Accordion pattern with icons (+ / –) for expand/collapse.
	•	Transitions: Framer Motion for smooth open/close animations.
	•	Color System: Inherits ThemeContext (light/dark).
	•	Scroll Behavior: Auto-scroll on open panel, fixed legend section for quick reference.

⸻

♿ Accessibility
	•	role="complementary" applied to <aside>.
	•	Each collapsible panel is a landmark region with aria-expanded states.
	•	Keyboard shortcuts:
	•	L → toggle Sidebar visibility
	•	F → focus Filter panel
	•	Accessible icons via <svg role="img" aria-label="Toggle layer">.
	•	High contrast and large click targets validated against WCAG 2.1 AA.

Accessibility verification handled with axe-core in CI.

⸻

🧪 Testing

Test Case	Description	Tool
Layer Toggle Sync	Confirms toggling a layer updates MapLibre view.	Jest + React Testing Library
Legend Rendering	Ensures STAC legend assets load and render correctly.	Jest + Mock STAC
Accordion Behavior	Validates expand/collapse transitions and focus management.	Framer Motion tests
Accessibility Check	Validates ARIA roles and keyboard shortcuts.	axe-core
Responsive Layout	Verifies mobile vs. desktop layout behavior.	Cypress E2E

Coverage target: ≥ 90% lines and branches.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	STAC catalog, LayerContext, TimelineContext
Outputs	Active layers, visible legends, filtered map overlays
Dependencies	React, MapLibre GL JS, Framer Motion, TailwindCSS
Integrity	CI validation includes STAC schema checks and accessibility audits


⸻

🔗 Related Documentation
	•	LayerControls Component
	•	MapView Component
	•	TimelineView Component
	•	Context — Layer & Timeline
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — engineered under the Master Coder Protocol (MCP)
for traceable, modular, and accessible design.

“The Sidebar is the explorer’s toolkit — a command center for navigating Kansas across time and terrain.”

