Got it — here’s a clean, GitHub-safe replacement you can paste directly into
docs/design/mockups/figma/components/navigation/README.md.
No HTML wrappers, no special tokens, and the Mermaid block validates on GitHub.

⸻

🧭 Navigation Components — Kansas Frontier Matrix

docs/design/mockups/figma/components/navigation/README.md

Specification for the KFM web UI navigation system: Header, Global Search, Timeline, Layer Controls, and Detail Panel.
This doc follows strict GitHub rendering rules (pure Markdown headings, fenced code blocks, GitHub-safe Mermaid, compact tables).

⸻

Contents
	•	Scope
	•	Anatomy
	•	Interaction Model
	•	States
	•	Accessibility
	•	Design Tokens
	•	Data Contracts
	•	Events & Telemetry
	•	Responsive Rules
	•	QA Checklist
	•	Changelog

⸻

Scope

The Navigation system coordinates time (timeline), space (map layers), and discovery (search):
	•	Header: brand/home, global search, utility actions (help, language, auth).
	•	Timeline: range selection, zoom, scrub/play.
	•	Layers: toggle visibility, set opacity, view legend.
	•	Detail Panel: entity/event dossier with sources.
	•	Keyboard + screen reader support across all regions.

⸻

Anatomy

[Header]
 ├─ Brand / Home
 ├─ Global Search  (entities · events · places)
 └─ Utility (Help · Language · Login)

[Main]
 ├─ Left Sidebar: Layer Controls (+ Legend)
 ├─ Map View (MapLibre)
 └─ Right Panel: Detail / AI Summary (toggle)

[Bottom]
 └─ Timeline: range handles · zoom · play/pause


⸻

Interaction Model

flowchart LR
  A["Header\nbrand · search · help"] --> B["Timeline\nrange · zoom · play"]
  A --> C["Layers\nvisibility · opacity · legend"]
  B --> D["API\nGET /events?start&end"]
  C --> E["Config\nGET /layers-config"]
  A --> F["Detail Panel\nentity dossier"]
  D --> G["State\nselectedTimeRange"]
  E --> H["State\nactiveLayers"]
  F --> I["State\nselectedEntity"]
  G --> MAP["Map View\nfiltered by time"]
  H --> MAP
  I --> MAP

<!-- END OF MERMAID -->


Notes
	•	Timeline and Map share state; API filters by {start,end} to reduce client load.
	•	Layer UI is driven by declarative config produced from the STAC catalog.

⸻

States

Region	Default	Hover/Focus	Active/Busy	Empty/Error
Header/Brand	Clickable home	Underline on focus	—	—
Search	Placeholder; Ctrl+/ focus	Focus ring; suggestions	Spinner while fetching	“No results”
Layers	Base layers only	Tooltip/legend visible	Toggle disabled during fetch	Error banner
Timeline	Project default window	Handle focus ring	Play animation / loading	“No events”
Detail Panel	Collapsed	—	Skeleton while loading	“No details available”


⸻

Accessibility
	•	Landmarks:
header[role="banner"], nav[aria-label="Layer controls"], main, aside[role="complementary"], footer[role="contentinfo"]
	•	Keyboard:
	•	Tab / Shift+Tab traverse Header → Timeline → Layers → Detail.
	•	Ctrl+/ focus Search; Esc closes Detail; Space/Enter toggles; arrows adjust sliders.
	•	ARIA:
role="search", role="slider" (timeline handles), role="switch" (layer toggles), aria-expanded, aria-controls, live region for async search results.
	•	Motion/Contrast: Respect prefers-reduced-motion; maintain WCAG AA contrast.

⸻

Design Tokens

Token	Purpose
--kfm-color-bg, --kfm-color-surface, --kfm-color-text	Base surfaces & text
--kfm-color-accent, --kfm-color-accent-contrast	Primary actions
--kfm-focus-ring	Focus outline color/style
--kfm-space-2/4/6/8	Spacing scale
--kfm-radius-2xl	Panel corner radius
--kfm-z-nav, --kfm-z-detail, --kfm-z-tooltip	Z-index stacking

Keep tokens centralized; mirror in MapLibre layer styles where appropriate.

⸻

Data Contracts

Global Search

GET /search?q={q}

{
  "hits": [
    {"id": "ent:ks:Topeka", "type": "place", "label": "Topeka, Kansas", "summary": "Capital of Kansas"},
    {"id": "evt:1856:bleeding", "type": "event", "label": "Bleeding Kansas (1854–1861)"}
  ]
}

Emits: nav.select(entityId) → centers map/timeline on selection.

Timeline

GET /events?start=1850-01-01&end=1870-12-31

[
  {"id":"evt:1854:kansas-nebraska","type":"treaty","t0":"1854-05-30","t1":null,"title":"Kansas–Nebraska Act"},
  {"id":"evt:1861:statehood","type":"statehood","t0":"1861-01-29","t1":null,"title":"Kansas Statehood"}
]

State: { "start": ISODate, "end": ISODate, "zoom": number }
Emits: nav.time.change(range) (debounced ~250 ms).

Layers (STAC-derived)

GET /layers-config

{
  "layers": [
    {"id":"basemap.terrain","label":"Terrain","type":"raster","visible":true,"opacity":1.0},
    {"id":"hist.topomaps","label":"Historic Topo Maps","type":"raster","visible":false,"opacity":0.8},
    {"id":"hydro.rivers","label":"Rivers","type":"vector","visible":true,"opacity":1.0}
  ]
}

State: { [layerId]: { "visible": boolean, "opacity": 0.0..1.0 } }
Emits: nav.layers.change(state) (persist to localStorage).

Detail Panel

GET /entity/{id}

{
  "id":"ent:ks:Topeka",
  "label":"Topeka, Kansas",
  "summary":"Capital on the Kansas River.",
  "links":[{"rel":"source","href":"..."}]
}

Emits: nav.detail.open(id) / nav.detail.close().

⸻

Events & Telemetry
	•	nav.search.submit, nav.search.select
	•	nav.time.change, nav.time.play, nav.time.pause
	•	nav.layers.toggle, nav.layers.opacity
	•	nav.detail.open, nav.detail.close

Log breadcrumbs in dev; avoid PII; batch network sends.

⸻

Responsive Rules
	•	≥1280px: Layers sidebar open; Detail collapsible; Timeline 140–180 px tall.
	•	768–1279px: Layers collapsed by default; Detail overlays Map; Timeline ~120 px.
	•	<768px: Compact Header; Search modal; single overlay sidebar; collapsible Timeline.

⸻

QA Checklist
	•	Headings, code fences, tables, and Mermaid render on GitHub.
	•	Full keyboard traversal with visible focus (no removed outlines).
	•	Screen reader labels/roles present; live announcement for async search results.
	•	Timeline ↔ API filters align; debounce in effect.
	•	Layers reflect STAC config; legend matches symbology.
	•	Detail loads with skeleton; errors show clear messages.

⸻

Changelog
	•	v1.1 — Fix GitHub rendering: removed HTML wrappers, validated Mermaid, tightened tables.
	•	v1.0 — Initial spec.

⸻

Mermaid Tips (GitHub)
	•	Use triple backticks with the mermaid language.
	•	Quote labels that contain punctuation and use \n for line breaks.
	•	Put <!-- END OF MERMAID --> outside the code fence (as shown above).
	•	Avoid HTML comments inside Mermaid blocks.
