<div align="center">


🧭 Kansas Frontier Matrix — Navigation Components

docs/design/mockups/figma/components/navigation/

Interactive · Temporal · Spatial · Accessible

</div>



⸻

Overview

The Navigation system coordinates time (Timeline), space (Map + Layers), and discovery (Search + Detail Panel). It is designed for clarity, speed, and accessibility, and wired to the API, STAC-driven layer configs, and the knowledge graph.

⸻

Directory

docs/design/mockups/figma/components/navigation/
├── README.md                 # This spec (GitHub-safe)
├── wireframes/               # PNG/SVG exports from Figma
├── figma-refs.json           # Figma node references (template)
└── assets/                   # Icons, thumbnails, screenshot aids


⸻

Components

Component	Purpose	Notes
Header	Brand/home, global search, utility actions	/ to focus search; Help, Language, Auth
Timeline	Scrub/zoom/play time ranges	Emits { start, end } to filter map/layers
Layer Controls	Toggle overlays, opacity, legends	Groups by theme; STAC-derived config
Map View	Spatial context and interaction	Click markers → open Detail Panel
Detail Panel	Dossier of entity/event	Summary, sources, related links


⸻

Interaction Diagram (GitHub-safe Mermaid)

flowchart LR
  subgraph UI["User Interface"]
    A["Header\n(search · help · auth)"]
    B["Timeline\n(range · play · zoom)"]
    C["Layer Controls\n(toggles · legends)"]
    D["Map View\n(markers · overlays)"]
    E["Detail Panel\n(dossier · sources)"]
  end

  subgraph API["Backend"]
    F["FastAPI / GraphQL"]
  end

  subgraph DATA["Data & Config"]
    G["Neo4j\n(entities · events · links)"]
    H["STAC Catalog\n(layers.json)"]
  end

  A --> F
  B --> F
  C --> H
  D --> F
  E --> F
  F --> G
  F --> H
  H --> D

<!-- END OF MERMAID -->



⸻

Event Contracts

Emitter	Event	Payload	Consumer	Effect
Timeline	time:changed	{ start, end }	Map	Filter events/overlays in view
Search	search:selected	{ entityId, type }	Map, Timeline	Zoom to entity; focus its time span
Map	map:entity:clicked	{ entityId }	Detail Panel	Open dossier with sources
Layers	layers:toggle	{ layerId, on }	Map	Show/hide + update legends
Detail Panel	detail:relation:selected	{ entityId }	Map, Timeline	Navigate to related item


⸻

Accessibility
	•	Keyboard: Tab focus order; / focuses search; Esc closes panels
	•	ARIA roles: banner, search, navigation, main, complementary
	•	Timeline has aria-describedby with short usage hints
	•	Legends use shape/texture in addition to color (WCAG 2.1 AA)

⸻

Tech & Data

Subsystem	Tech	Purpose
Map	MapLibre GL JS	Rendering and spatial interaction
Timeline	HTML5 Canvas	High-density, high-FPS time rendering
Layers	STAC → layers.json	Source URLs, time extents, legends
Knowledge	Neo4j	Entities, events, relationships
API	FastAPI / GraphQL	Search, details, aggregates


⸻

Local Preview

make data      # Prepare STAC + configs
make site      # Build docs/site
make serve     # Local preview

Quick test: Search → Select → Zoom → Scrub timeline → Open detail → Toggle layers.

⸻

PR Checklist (Design + Dev)
	•	README updated with any UI/flow changes
	•	Mermaid renders on GitHub (no parser errors)
	•	A11y check (keyboard, ARIA, contrast)
	•	layers.json validated (schema + links)
	•	E2E happy-path passes (search → detail → map → time)

⸻

Change Log
	•	2025-10-05 — Initial GitHub-compliant version
	•	2025-10-06 — Added Accessibility and Event Contracts
