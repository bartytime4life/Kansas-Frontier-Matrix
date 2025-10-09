<div align="center">

# 🗺️ Kansas Frontier Matrix — MapView Component  
`web/src/components/MapView/`

**Interactive Mapping · Historical Layers · Spatial Storytelling**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **MapView Component** is the interactive **geospatial visualization engine**  
of the Kansas Frontier Matrix web application. It renders **historical and modern datasets**  
from the project’s **STAC catalog**, integrating them with the knowledge graph’s  
people, places, and events.

Built using **MapLibre GL JS**, the component supports dynamic overlays of **Cloud-Optimized GeoTIFFs (COGs)**,  
**GeoJSON features**, and **temporal layers**, synchronized with the **timeline view**.  

MapView serves as the visual anchor of the application — connecting Kansas’s physical geography  
to its cultural and historical evolution.

---

## 🧱 Directory Structure

```text
web/src/components/MapView/
├── MapView.tsx             # Main map rendering component
├── MapLayer.tsx            # Handles individual STAC-defined layers
├── MapLegend.tsx           # Displays legends and layer info
├── MapMarker.tsx           # Entity or event markers
├── PopupInfo.tsx           # On-click information windows
├── styles.scss             # Theming, responsive sizing, overlays
└── __tests__/              # Jest + RTL tests for map rendering and interactions


⸻

⚙️ Component Architecture

flowchart TD
  M["MapView\n(MapLibre GL JS)"] --> C["LayerContext\n(visible layers, opacity)"]
  M --> T["TimelineContext\n(time range filter)"]
  M --> STAC["STAC Catalog\n(data/stac/catalog.json)"]
  M --> MAPLAYER["MapLayer Components\n(raster/vector)"]
  M --> POP["PopupInfo\n(entity details)"]
  MAPLAYER --> LEG["MapLegend"]
  POP --> DP["DetailPanel"]
%% END OF MERMAID


⸻

🧩 Core Features

Feature	Description	Data Source
STAC-Driven Layers	Dynamically loads raster/vector datasets from STAC items.	data/stac/catalog.json
Temporal Filtering	Filters visible layers and features based on current timeline range.	TimelineContext
Interactive Markers	Displays locations of historical sites, treaties, and events.	Neo4j Knowledge Graph
Popup Information	Shows summaries and links to the DetailPanel for selected entities.	/api/entity/{id}
Legends & Overlays	Draws STAC-defined legends for active map layers.	STAC metadata
Basemap Controls	Switch between modern, terrain, or satellite base layers.	MapLibre Styles
Accessibility	Keyboard navigation (arrow keys, tab focus), screen-reader ARIA roles.	WCAG 2.1 AA


⸻

💬 Example Implementation

import React, { useEffect, useRef } from "react";
import maplibregl from "maplibre-gl";
import { useLayer } from "../../context/LayerContext";
import { useTimeline } from "../../context/TimelineContext";
import { loadSTACLayers } from "../../utils/mapUtils";
import "maplibre-gl/dist/maplibre-gl.css";
import "./styles.scss";

export const MapView: React.FC = () => {
  const mapContainer = useRef(null);
  const { visibleLayers } = useLayer();
  const { range } = useTimeline();

  useEffect(() => {
    const map = new maplibregl.Map({
      container: mapContainer.current,
      style: "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
      center: [-98.3, 38.5],
      zoom: 6,
    });

    loadSTACLayers(map, visibleLayers, range);

    return () => map.remove();
  }, [visibleLayers, range]);

  return <div ref={mapContainer} className="map-view"></div>;
};


⸻

🧠 Data Flow

sequenceDiagram
  participant U as User
  participant MV as MapView
  participant CTX as LayerContext
  participant STAC as STAC Catalog
  participant API as FastAPI
  participant KG as Knowledge Graph

  U->>MV: Toggles layer visibility
  MV->>CTX: Updates visibleLayers state
  CTX->>STAC: Loads metadata for selected layers
  MV->>API: GET /events?bbox=&start=&end=
  API->>KG: Query events by location and time
  KG-->>API: Returns geo-tagged events
  API-->>MV: Returns GeoJSON features
  MV-->>U: Renders map layers and markers
%% END OF MERMAID


⸻

🎨 Styling & UI
	•	Layout: Map occupies central viewport region in AppShell.
	•	Style Sources: MapLibre base styles (Voyager, Terrain, Satellite) + custom overlays.
	•	Layer Styling: Categorical (for boundaries, trails) and continuous (for raster values).
	•	Legend UI: Displays STAC item titles, color gradients, and year range.
	•	Responsiveness: Map resizes with ResizeObserver, preserving center/zoom state.

⸻

♿ Accessibility

Feature	Implementation
Keyboard Navigation	Arrow keys to pan, +/- to zoom, Tab cycles focusable controls.
Screen Reader Support	Descriptive aria-label for map container (“Interactive Kansas Map”).
Focus Indicators	High-contrast outline via AccessibilityContext.
Reduced Motion	Disables smooth panning/animations when prefers-reduced-motion is set.
Tooltips	Accessible tooltips with ARIA role="tooltip" attributes.

Accessibility validations are performed automatically in CI via axe-core and Lighthouse.

⸻

🧪 Testing

Test Case	Description	Tool
Layer Loading	Ensures all STAC layers load correctly from catalog.	Jest + MSW
Opacity Control	Validates LayerControls sliders modify map opacity.	Jest DOM
Popup Rendering	Tests popups show entity summaries on marker click.	React Testing Library
Timeline Sync	Verifies time-based filtering of features.	Jest mock TimelineContext
Accessibility Audit	Confirms ARIA roles and color contrast compliance.	axe-core

Target coverage: ≥ 90% for rendering and interaction tests.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	STAC metadata (data/stac/catalog.json), API data (/api/events), maplibre-gl instance
Outputs	Interactive map tiles, markers, overlays, and legends
Dependencies	React 18+, MapLibre GL JS, Framer Motion, TailwindCSS
Integrity	CI validates STAC schema, accessibility, and functional tests before merge


⸻

🔗 Related Documentation
	•	LayerControls Component
	•	TimelineView Component
	•	DetailPanel Component
	•	Web Frontend Components Overview
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Developed under the Master Coder Protocol (MCP)
for transparency, reproducibility, and cross-domain interoperability.

“The MapView is the heart of the frontier — where Kansas’s stories take shape on the land itself.”

