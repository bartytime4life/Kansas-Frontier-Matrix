🧭 Kansas Frontier Matrix — Navigation Components

docs/design/mockups/figma/components/navigation/README.md

GitHub-ready spec for the KFM web UI navigation: header, global search, timeline, layer controls, detail panel, and accessibility/keyboard behavior. Designed to render cleanly on GitHub, with a Mermaid diagram that passes the strict parser.

⸻

Overview

The navigation system coordinates time (timeline), space (map + layers), and discovery (search) across the KFM web app. It stitches the TimelineView, MapView, Layer Controls, Search, and Detail Panel into one cohesive, accessible experience, backed by a FastAPI/GraphQL API and a Neo4j knowledge graph.  ￼

Goals
	•	Fast orientation: users can land, search, scrub time, and reveal details in ≤3 interactions.
	•	Temporal + spatial sync: timeline range filters the map; selecting a map entity focuses the timeline.  ￼
	•	Modularity: components are independent and versioned with the monorepo; new layers/features plug in via configuration.  ￼

⸻

Components (UI spec)

1) Header Bar
	•	Brand/home (click → reset view to current default extent & time window)
	•	Global Search (type-ahead across People/Places/Events; Enter to open details; ↓/↑ navigate results)
	•	Utility: Help, Language, Admin/Login (admin switches to curation actions)  ￼

2) Timeline (bottom)
	•	Zoomable, pannable range.
	•	Scrub by drag; zoom with wheel/trackpad; play for auto-advance.
	•	Emits [start,end] to filter visible layers/events; the map updates in place.  ￼

3) Map Toolbar (left)
	•	Zoom / Locate / Measure (optional)
	•	Layer Controls: toggles + legends grouped by theme (Maps, Environment, Settlements, Documents). Reads from the STAC-driven layer config.  ￼

4) Detail Panel (right)
	•	“Site dossier” with title, summary, facts, linked entities, sources; deep-links to map/timeline.
	•	Includes AI summary (with citations) and “related” items.  ￼

5) Keyboard & Accessibility
	•	Global: / focuses search, ? opens shortcuts, Esc closes panels.
	•	Timeline: ←/→ nudge window; Shift+arrow = larger step.
	•	Search list: roving tabindex, ARIA combobox roles, proper labelling for screen readers.
	•	Complies with WAI-ARIA roles (banner, search, navigation, main, complementary).  ￼

⸻

Interaction model (GitHub-safe Mermaid)

flowchart LR
  subgraph UI["Navigation Surface"]
    A["Header\n(search · help · admin)"]
    B["Timeline\n(range · play · zoom)"]
    C["Layer Controls\n(toggles · legends)"]
    D["Map View\n(markers · overlays)"]
    E["Detail Panel\n(dossier · sources)"]
  end

  subgraph API["API Layer"]
    F["FastAPI / GraphQL"]
  end

  subgraph DATA["Data"]
    G["Neo4j\n(people · places · events)"]
    H["STAC Catalog\n(layers.json)"]
  end

  %% Flows
  A --> F
  B --> F
  C --> H
  D --> F
  E --> F
  F --> G
  F --> H
  H --> D

  %% Notes
  %% All labels quoted; end marker below for GitHub

<!-- END OF MERMAID -->


This diagram mirrors the documented frontend–API–graph/STAC wiring and uses only GitHub-safe Mermaid features.  ￼

⸻

States & events (contract)

Emitter	Event	Payload	Consumer	Effect
Timeline	time:changed	{ start, end }	Map, API	Filter layers/events by range
Search	search:selected	{ entityId, type }	Map, Timeline	Zoom to entity; focus its time
Map (marker)	map:entity:clicked	{ entityId }	Detail Panel	Open dossier, fetch summary
Layers	layers:toggle	`{ layerId, on	off }`	Map
Detail actions	detail:relation:selected	{ entityId }	Map, Timeline	Navigate to related item

Server-side heavy lifting (graph traversals, aggregations) happens in the API; the client stays light.  ￼

⸻

Rendering & data sources
	•	Map: MapLibre GL JS; basemap + historical overlays (COGs, GeoJSON, or tiles) from STAC-declared assets.  ￼
	•	Timeline: HTML5 Canvas for smooth, dense timelines at 60 fps.
	•	Config: layers.json generated from the STAC catalog; includes time extents & legends.  ￼

⸻

Accessibility & inclusive design checklist
	•	Keyboard access to all controls; visible focus states.
	•	ARIA roles and labelled regions: banner, search, navigation, main, complementary.
	•	Timeline has aria-described instructions and live region feedback for range updates.
	•	Color contrast meets WCAG AA; legends use shape/texture, not color alone.
	•	Screen-reader friendly search (combobox pattern).  ￼

⸻

Performance & testing
	•	Canvas timeline to avoid DOM thrash; cluster map markers; lazy-load detail content.
	•	Tests: search → select → focus flows; timeline–map sync; layer toggles; detail navigation (RTL + E2E).
	•	CI enforces passing tests before merge.  ￼

⸻

Authoring & contribution (for designers/devs)
	•	Figma: keep component names aligned to code (Header, TimelineView, LayerControls, MapView, DetailPanel).
	•	PR checklist: update this README and any diagrams first; add/adjust tests; ensure layer config and STAC are valid; bump changelog if behavior changes.  ￼
	•	Docs-first: commit doc updates with the code (MCP).  ￼

⸻

How to preview locally
	1.	Start the stack (API, graph, tiles, web):

make bootstrap
make data            # fetch → process → stac-validate
make up              # docker compose up (api, neo4j, web)

	2.	Open the web app; test search → select → detail → time scrub.  ￼

⸻

Non-goals (keep out of navigation)
	•	Raw data editing (belongs in admin curation).
	•	Heavy analytics UI (separate “analysis” mode/module).
	•	Map styling editor (managed in config).

⸻

Appendix — Rationale & sources
	•	Separation of concerns (UI vs. API vs. graph/STAC) keeps the client responsive and the system extensible.  ￼
	•	STAC-driven layers allow add/remove overlays without code changes.  ￼
	•	AI “dossiers” surface concise, cited context without overwhelming the UI.  ￼

⸻

Change log (snippet)
	•	2025-10-05: Initial GitHub-compliant rebuild (timeline/search/layers/detail spec & Mermaid)
	•	2025-10-06: Added accessibility section and PR checklist

⸻

End of file
