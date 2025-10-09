<div align="center">

# 🗺️ Kansas Frontier Matrix — LayerControls Component  
`web/src/components/LayerControls/`

**Map Layers · STAC Integration · Legends · Opacity Control**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **LayerControls** component provides a **geospatial layer management interface**  
for the Kansas Frontier Matrix’s interactive map.  

It allows users to toggle visibility, adjust opacity, and view legends for  
geospatial layers (raster and vector) sourced from the **STAC catalog** (`data/stac/catalog.json`).  

Each layer corresponds to a dataset — for example, **historic topographic maps**,  
**soil surveys**, **treaty boundaries**, **hydrology**, or **climate hazards** — enabling  
users to customize their view and explore Kansas’s temporal and environmental evolution.

This component connects directly to the **LayerContext** and **MapLibre map instance**,  
ensuring dynamic synchronization between the UI controls and the rendered layers.

---

## 🧱 Directory Structure

```text
web/src/components/LayerControls/
├── LayerControls.tsx        # Main component rendering the control panel
├── LayerItem.tsx            # Individual layer toggle + opacity slider
├── Legend.tsx               # Displays color or symbol legends
├── styles.scss              # Theming and responsive layout
└── __tests__/               # Jest + RTL tests for toggle, opacity, and sync


⸻

⚙️ Component Architecture

flowchart TD
  LYR["LayerControls\n(toggle, opacity, legend)"] --> CTX["LayerContext\n(active layers)"]
  LYR --> MAP["MapView\n(MapLibreGL JS instance)"]
  LYR --> STAC["STAC Catalog\n(data/stac/catalog.json)"]
  STAC --> MAP
  CTX --> MAP
  CTX --> UI["TimelineView\n(sync visibility by year)"]
%% END OF MERMAID


⸻

🧩 Core Features

Feature	Description	Data Source
Layer Toggling	Enables adding/removing map layers dynamically.	STAC Items
Opacity Slider	Adjusts layer transparency (0–100%) for blending datasets.	MapLibre Layer API
Legends	Displays color gradients or symbols representing layer data.	STAC metadata (assets.legend)
Layer Metadata	Provides quick info: dataset name, time span, source, license.	data/stac/catalog.json
Timeline Sync	Automatically filters visible layers based on current timeline range.	TimelineContext
Persistence	Stores user selections in localStorage for session restoration.	LayerContext
Accessibility	Keyboard focusable controls, ARIA labels for each layer toggle.	WCAG 2.1 AA


⸻

💬 Example Usage

import React from "react";
import { LayerControls } from "./LayerControls";

export function Sidebar() {
  return (
    <aside className="layer-sidebar">
      <h2>Map Layers</h2>
      <LayerControls />
    </aside>
  );
}

Example Layer Item Rendering

<LayerItem
  id="usgs_topo_1894"
  title="USGS Historic Topographic Map (1894)"
  opacity={0.8}
  active={true}
  onToggle={() => toggleLayer("usgs_topo_1894")}
  onOpacityChange={val => setLayerOpacity("usgs_topo_1894", val)}
/>


⸻

🧮 TypeScript Interfaces

export interface LayerItemProps {
  id: string;
  title: string;
  opacity: number;
  active: boolean;
  onToggle: () => void;
  onOpacityChange: (opacity: number) => void;
}

export interface MapLayer {
  id: string;
  type: "raster" | "vector";
  title: string;
  url: string;
  opacity?: number;
  year?: number;
  legend?: string;
  license?: string;
}


⸻

🎨 UI / UX Design
	•	Layout: Vertical accordion panel with collapsible legends.
	•	Controls: Switch toggle (<input type="checkbox">) and range slider for opacity.
	•	Styling:
	•	Base: TailwindCSS + SCSS (styles.scss)
	•	Framer Motion animations for expanding/collapsing legends.
	•	Color System:
	•	Text and icons adapt to theme (light / dark).
	•	Highlight color = --kfm-color-accent (turquoise).

⸻

🧠 Data Flow

sequenceDiagram
  participant U as User
  participant LC as LayerControls
  participant CTX as LayerContext
  participant MAP as MapView
  participant STAC as STAC Catalog

  U->>LC: Toggles "Soil Survey (1967)" layer
  LC->>CTX: setLayerActive(id, true)
  CTX->>MAP: addLayer(id, sourceURL)
  MAP-->>U: Layer visible with opacity 100%
  U->>LC: Adjusts opacity slider to 50%
  LC->>CTX: setLayerOpacity(id, 0.5)
  CTX->>MAP: update opacity
%% END OF MERMAID


⸻

🧪 Testing

Test Case	Description	Tool
Layer Toggle	Ensures enabling/disabling layers updates the map.	Jest + React Testing Library
Opacity Adjustment	Verifies slider changes update layer style.	Jest + DOM simulation
Legend Visibility	Confirms legends appear and collapse smoothly.	Framer Motion tests
Timeline Sync	Simulates changing timeline to auto-hide outdated layers.	Jest mocking TimelineContext
Accessibility	Validates ARIA labels, focus order, and keyboard toggles.	axe-core / Lighthouse

Target coverage: ≥ 90%.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	STAC catalog metadata, MapLibre map instance, LayerContext state
Outputs	Map overlays (raster/vector layers) rendered dynamically
Dependencies	React 18+, MapLibre GL JS, Framer Motion, TailwindCSS
Integrity	CI validates rendering consistency, STAC schema compliance, accessibility ≥ 95%


⸻

🔗 Related Documentation
	•	Web Frontend Components
	•	MapView Component
	•	Context — Layer & Timeline
	•	Web UI Architecture
	•	Data & STAC Catalog Overview

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — designed and documented under the Master Coder Protocol (MCP)
for transparent, reproducible, and geospatially accurate visualization.

“Every map layer is a chapter — the LayerControls let users choose which stories to see.”

