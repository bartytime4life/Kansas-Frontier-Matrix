<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Interface  
`docs/design/mockups/map/`

**Spatial · Interactive · Time-Aware Exploration**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Map%20Interface-purple)](./figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **Map Interface** is the visual core of the Kansas Frontier Matrix, enabling users to explore Kansas’s historical and environmental data through **space and time**.  
It combines spatial layers (maps, vector data, raster overlays) with temporal awareness from the **timeline** and contextual data from the **knowledge graph**.

The map interface is designed to be:
- **Interactive** — Zoom, pan, and toggle thematic layers dynamically.  
- **Temporal** — Synchronize data visibility with the timeline scrubber.  
- **Informative** — Display popups, highlights, and AI-assisted summaries for selected entities.  
- **Accessible** — Fully keyboard- and screen reader-friendly, WCAG 2.1 AA compliant.  

---

## 🧭 Key Features

| Feature | Description | Implementation |
|----------|--------------|----------------|
| 🗺 **Dynamic Layers** | Toggle historical base maps, hydrology, treaties, or events | STAC-driven configuration (`layers.json`) |
| 🕰 **Timeline Sync** | Map filters automatically update when the timeline range changes | React hook emits `{start, end}` to MapLibre sources |
| 🔍 **Entity Highlights** | Clicking a place/event zooms and outlines corresponding geometry | Layer style updates + React context |
| 📜 **Tooltips & Popups** | Contextual cards show metadata, sources, and AI summaries | Markdown-enabled popups rendered from `/entity/{id}` |
| 📚 **Basemap Modes** | Switch between terrain, sepia, and light/dark basemaps | MapLibre style switching via dropdown |
| ♿ **Accessibility** | Keyboard navigation and ARIA-compliant map controls | Implemented via focus rings, `tabindex`, and ARIA labels |

---

## 📁 Directory Structure

```text
docs/design/mockups/map/
├── README.md                  # This file
├── wireframes/                # Map interface mockups (Figma exports)
│   ├── map-main-view.png
│   ├── layer-controls.svg
│   ├── popup-preview.png
│   └── timeline-linked-map.svg
├── icons/                     # Map control icons (zoom, locate, basemap)
│   ├── icon-locate.svg
│   ├── icon-layers.svg
│   ├── icon-map-style.svg
│   └── checksums.txt
├── thumbnails/                # Small preview images for docs
│   ├── map-overview-thumb.png
│   └── popup-thumb.png
└── figma-refs.json            # Figma node reference metadata


⸻

🧩 System Integration (GitHub-Safe Mermaid)

flowchart LR
  A["Timeline Component\n(start,end)"] --> B["Map Controller\n(MapLibre React Hook)"]
  B --> C["MapLibre GL JS\n(base + overlay layers)"]
  C --> D["STAC Metadata\n(data/stac/catalog.json)"]
  B --> E["Popup Manager\n(fetch /entity/{id})"]
  E --> F["Knowledge Graph (Neo4j)\nvia FastAPI"]

<!-- END OF MERMAID -->


The map interface connects to both the timeline and the knowledge graph, ensuring spatial events and entities stay synchronized in time and context.

⸻

🧠 Layer Taxonomy

Category	Example Layer	Format	Source
Base Maps	Kansas Topographic (USGS 1880s)	GeoTIFF (COG)	data/stac/items/usgs_topo_1880.json
Boundaries	County & Treaty Lines	GeoJSON	data/stac/items/treaty_1854.json
Hydrology	Rivers, Lakes, Aquifers	Shapefile / GeoJSON	data/sources/hydro/
Infrastructure	Railroads, Trails	GeoJSON	data/sources/transport/
Events	Tornado Paths, Floods	CSV → GeoJSON	data/sources/hazards/

All layers are indexed via STAC and described in data/stac/catalog.json, allowing the map to dynamically discover and render available content.

⸻

🎨 Design Tokens

Token	Example	Purpose
--kfm-map-bg	#0b1020	Map background color (dark mode)
--kfm-highlight	#4F9CF9	Entity highlight border
--kfm-water	#3BA2E0	River and lake coloring
--kfm-hillshade	rgba(0,0,0,0.15)	Elevation shading overlay
--kfm-legend-bg	#ffffffd9	Legend panel background

These tokens ensure consistent theming across layers and interaction states.

⸻

🧾 Interaction Flow

sequenceDiagram
  participant User
  participant MapUI
  participant API
  participant Graph
  User->>MapUI: Click on Map Feature
  MapUI->>API: GET /entity/{id}
  API->>Graph: Cypher query (entity metadata)
  Graph-->>API: JSON (entity + relationships)
  API-->>MapUI: Render popup with metadata + links
  MapUI-->>User: Highlight entity + show linked events

<!-- END OF MERMAID -->



⸻

🔍 Provenance & Integrity

Asset	Figma Node	Exported	SHA256
map-main-view.png	figma://node/44:18	2025-09-30	sha256-3d7a…
layer-controls.svg	figma://node/44:21	2025-09-30	sha256-19cd…
popup-preview.png	figma://node/44:25	2025-09-30	sha256-f24e…
timeline-linked-map.svg	figma://node/44:28	2025-09-30	sha256-7ae9…

Checksums are verified in CI to maintain consistency between exported assets and documented references.

⸻

🧾 Related Documents
	•	Navigation Components
	•	Web UI Architecture
	•	System Architecture
	•	Data Format Standards
	•	Design Tokens

⸻

📜 License & Credits

Map interface design © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Created by the KFM Design & Interaction Team, adhering to Master Coder Protocol principles of documentation-first, open standards, and reproducibility.

