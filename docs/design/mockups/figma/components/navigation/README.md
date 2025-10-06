🧭 Navigation Components — Kansas Frontier Matrix

docs/design/mockups/figma/components/navigation/README.md

A GitHub-ready spec for the Navigation system used across the Kansas Frontier Matrix (KFM) web UI: header, global search, timeline controls, map layer controls, and detail panel hooks. This doc is formatted to render cleanly on GitHub (pure Markdown headings, fenced code blocks, GitHub-safe Mermaid, compact tables). It aligns with the project’s web/UI architecture and MCP documentation standards.  ￼

⸻

Contents
	•	Scope
	•	Anatomy
	•	Interaction model
	•	States
	•	Accessibility
	•	Design tokens
	•	Data contracts (props / API)
	•	Events & telemetry
	•	Responsive rules
	•	QA checklist
	•	Changelog

⸻

Scope

The Navigation system orchestrates time, space, and search:
	•	Header bar: brand, global search, language/help, admin/login.
	•	Timeline controls: time range, zoom, scrubber, play/pause.
	•	Map layer controls: layer toggles, legend, opacity.
	•	Detail panel hook: opens entity/event “dossier” on selection.
	•	Keyboard & screen reader flow across all regions.

It connects the React SPA to the FastAPI/GraphQL API and Neo4j graph, and drives MapLibre GL and the Canvas timeline.  ￼

⸻

Anatomy

[Header]
 ├─ Brand / Home
 ├─ Global Search (entity/event/place)
 ├─ Utility: Help, Language, Admin/Login

[Main]
 ├─ Left Sidebar: Layer Controls (+ Legend)
 ├─ Map View (MapLibre)
 ├─ Right Panel: Detail / AI summary (toggle)

[Bottom]
 └─ Timeline (Canvas): handles + zoom + range

Component IDs (for code & analytics)
	•	nav.header, nav.search, nav.util, nav.layers, nav.legend, nav.map, nav.detail, nav.timeline.

⸻

Interaction model

flowchart LR
  subgraph "User"
    K["Keyboard / Screen reader"]
    M["Mouse / Touch"]
  end

  H["Header\nbrand · search · utility"] --> T["Timeline\nrange · zoom · play"]
  H --> L["Layers\nvisibility · style"]
  T --> API["API\n/events?start&end"]
  L --> CFG["Layers Config\n(STAC-driven)"]
  API --> ST["State\nselectedTimeRange"]
  CFG --> LA["State\nactiveLayers"]
  ST --> MAP["Map View\nfilter by time"]
  LA --> MAP
  MAP --> DP["Detail Panel\nentity dossier"]

  %% Accessibility flow
  K --> H
  K --> T
  K --> L
  K --> DP
  M --> H
  M --> T
  M --> L
  M --> DP
<!-- END OF MERMAID -->

	•	Timeline and map are synchronized by a shared state store; server-side filtering prevents heavy client computation.  ￼
	•	Layer config derives from the STAC catalog (data/stac), keeping UI declarative.

⸻

States

Region	Default	Hover/Focus	Active/Busy	Empty/Error
Header/brand	Link visible	Underline on focus	—	—
Search	Placeholder; Ctrl+/ focus	Focus ring; suggestions	Loading spinner	“No results”
Layers	All off except base	Tooltip legends	Indeterminate while fetching	Error banner
Timeline	Project default period	Handle focus ring	Play anim / loading data	“No events”
Detail panel	Collapsed	—	Expanded with skeleton	“No details available”

(Use system focus outlines + ARIA on all controls; never remove focus styles.)

⸻

Accessibility
	•	Landmarks: <header role="banner">, <nav aria-label="Layer controls">, <main>, <aside role="complementary">, <footer role="contentinfo">.
	•	Keyboard map:
	•	Tab/Shift+Tab traversal across header → timeline → layers → detail.
	•	Ctrl+/ focus search; Esc close detail; Space/Enter toggles; arrows adjust sliders.
	•	ARIA: aria-expanded, aria-controls, role="slider" for timeline handles, role="switch" for layer toggles, live region for search suggestions.
	•	Contrast: WCAG AA min; respect prefers-reduced-motion.

Matches project guidance for a11y and responsive SPA.

⸻

Design tokens

Keep tokens centralized (light/dark support). Suggested minimal set:

Token	Usage
--kfm-color-bg, --kfm-color-surface, --kfm-color-text	Base layers
--kfm-color-accent, --kfm-color-accent-contrast	Primary CTAs
--kfm-focus-ring	Focus outlines
--kfm-space-2/4/6/8	Spacing scale
--kfm-radius-2xl	Panel corners
--kfm-z-nav, --kfm-z-detail, --kfm-z-tooltip	Z-index layers

Use CSS variables; align with the web UI’s tokenization and MapLibre styles.

⸻

Data contracts (props / API)

Global Search
	•	Input: string q
	•	API: GET /search?q={q} → { hits:[ {id,type,label,summary?} ] }
	•	Select: emits nav.select(entityId); map & timeline center on entity.  ￼

Timeline
	•	State: {start: ISODate, end: ISODate, zoom:number}
	•	API: GET /events?start&end → array of events {id,type,t0,t1,title,importance}
	•	Emit: nav.time.change(range); debounced 250ms.

Layers
	•	Config: GET /layers-config (derived from STAC)
	•	State: {[layerId]: {visible:boolean, opacity:0..1}}
	•	Emit: nav.layers.change(state); persisted to localStorage.

Detail Panel
	•	API: GET /entity/{id} → entity graph, summary, sources
	•	Close: nav.detail.close(); maintains selection history.  ￼

⸻

Events & telemetry
	•	nav.search.submit, nav.search.select
	•	nav.time.change, nav.time.play, nav.time.pause
	•	nav.layers.toggle, nav.layers.opacity
	•	nav.detail.open, nav.detail.close

Log to client analytics (console-safe in dev) with breadcrumbing; never send PII.  ￼

⸻

Responsive rules
	•	≥1280px: left Layers open, right Detail collapsible, timeline 140–180px.
	•	768–1279px: Layers collapsed by default; timeline 120px; Detail overlays map.
	•	<768px: Header compact; search as modal; timeline collapsible; single sidebar overlay.
The SPA is optimized for desktop but degrades gracefully to mobile.

⸻

QA checklist
	•	GitHub rendering: headings, code fences, Mermaid block validates (no HTML wrappers).
	•	Keyboard: full traversal; visible focus; shortcuts working.
	•	Screen reader: regions, labels, live announcements for search results.
	•	Timeline↔API: filters match returned events; debounce respected.  ￼
	•	Layers/STAC: toggles reflect STAC config; legends match symbology.
	•	Detail: entity fetch includes summary + linked entities; error states handled.  ￼

⸻

Changelog
	•	v1.0: First GitHub-compliant spec. Synchronized state model; STAC-driven layers; a11y map; events & telemetry defined. (2025-10-05)

⸻

References
	•	Web UI Design & Architecture: timeline + map, SPA + API, component layout.  ￼
	•	STAC-driven layers, ETL/graph pipeline, and config flow.
	•	GitHub documentation and formatting guardrails.

⸻

Formatting notes for contributors
	•	Use pure Markdown headings, fenced code blocks, and GitHub-safe Mermaid (quoted labels, \n for line breaks, end with <!-- END OF MERMAID -->).
	•	Keep directory trees inside triple-backtick fences with text or none.
	•	Keep badges minimal in component docs to avoid layout overflow on GitHub.
