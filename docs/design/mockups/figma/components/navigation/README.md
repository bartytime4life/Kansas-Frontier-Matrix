<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Components  
`docs/design/mockups/figma/components/navigation/`

**Interactive · Temporal · Spatial · Accessible**

</div>

---

## Overview

The navigation system coordinates **time** (Timeline), **space** (Map + Layers), and **discovery** (Search + Detail Panel).  
It’s designed for clarity, speed, and accessibility, and is wired to the **API**, **STAC-driven layer configs**, and the **knowledge graph**.

---

## Directory

```text
docs/design/mockups/figma/components/navigation/
├── README.md                 # This spec (GitHub-safe)
├── wireframes/               # PNG/SVG exports from Figma
├── figma-refs.json           # Figma node references (template)
└── assets/                   # Icons, thumbnails, screenshot aids


⸻

Components

Component	Purpose	Notes
Header	Brand/home, global search, utility actions	/ focuses search; Help, Language, Auth
Timeline	Scrub/zoom/play time ranges	Emits {start, end} to filter map/layers
Layer Controls	Toggle overlays, opacity, legends	Groups by theme; STAC-derived config
Map View	Spatial context and interaction	Click markers → open Detail Panel
Detail Panel	Dossier of entity/event	Summary, sources, related links


⸻

Interaction Diagram (GitHub-safe Mermaid)

flowchart LR
  %% UI Layer
  subgraph UI["User Interface"]
    A["Header\n(search · help · auth)"]
    B["Timeline\n(range · play · zoom)"]
    C["Layer Controls\n(toggles · legends)"]
    D["Map View\n(markers · overlays)"]
    E["Detail Panel\n(dossier · sources)"]
  end

  %% Backend
  subgraph API["Backend"]
    F["FastAPI / GraphQL"]
  end

  %% Data & Config
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
DetailPanel	detail:relation:selected	{ entityId }	Map, Timeline	Navigate to related item

Notes:
• All events should be typed in code and logged (dev mode) for traceability.
• Avoid tight coupling: use a central emitter/bus or React context to dispatch and subscribe.

⸻

Accessibility
	•	Keyboard: Predictable Tab order; / focuses search; Esc closes panels; arrow keys in timeline.
	•	ARIA roles: banner, search, navigation, main, complementary, region.
	•	Timeline help: aria-describedby with short usage hints; ensure focus ring visible at all times.
	•	Legends: Encode with shape/texture + color (WCAG 2.1 AA); provide text equivalents.
	•	Contrast: Maintain AA minimums; test both light/dark themes.
	•	Hit targets: ≥ 44×44 px for touch.

⸻

Tech & Data

Subsystem	Tech	Purpose
Map	MapLibre GL JS	Rendering and spatial interaction
Timeline	HTML5 Canvas	High-density, high-FPS time rendering
Layers	STAC → layers.json	Source URLs, time extents, legends
Knowledge	Neo4j	Entities, events, relationships
API	FastAPI / GraphQL	Search, details, aggregates


⸻

API / Event I/O (reference)
	•	Timeline → API: GET /events?start=YYYY-MM-DD&end=YYYY-MM-DD
	•	Search → API: GET /search?q=... → { items: [{ id, type, title, timeSpan }] }
	•	Detail → API: GET /entity/{id} → { summary, sources[], relations[] }
	•	Layers → STAC: GET /layers-config (layers.json) → [ { id, type, url, time, legend } ]

Performance tip: Cache layers.json with immutable asset URLs; prefer COG/GeoJSON for streaming.

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
	•	A11y check (keyboard, ARIA, contrast, focus states)
	•	layers.json validated (schema + links)
	•	E2E happy-path passes (search → detail → map → time)
	•	Event payloads are typed and logged (dev)

⸻

Change Log
	•	2025-10-06 — Hardened Mermaid; added API I/O; expanded A11y & event typing notes.
	•	2025-10-05 — Initial GitHub-compliant version.

⸻

Notes for Maintainers

Keep this file GitHub-safe:
	•	Quote all Mermaid labels containing punctuation.
	•	End Mermaid diagrams with <!-- END OF MERMAID -->.
	•	Use fenced code blocks for trees, tables, and commands.
	•	When adding new components (e.g. Mini-Map, Bookmarks), update Components, Event Contracts, and A11y sections.

