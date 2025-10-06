🧭 Kansas Frontier Matrix — Navigation Components

docs/design/mockups/figma/components/navigation/

Specification for the KFM web UI navigation system: Header, Global Search, Timeline, Layer Controls, and Detail Panel.
Formatted to pass GitHub’s strict Markdown/Mermaid parser.

⸻

🔖 Badge Grid

Build & Deploy	STAC Validate	CodeQL	Trivy	Pre-Commit	Docs · MCP	Design System	License
							


⸻

🪶 Overview

The Navigation system coordinates time (timeline), space (map layers), and discovery (search):
	•	Header → brand/home, global search, utility actions (help, language, auth)
	•	Timeline → range selection, zoom, scrub/play
	•	Layers → toggle visibility, set opacity, view legend
	•	Detail Panel → entity/event dossier with sources
	•	Accessibility → full keyboard and screen reader support across regions

⸻

📁 Directory

docs/design/mockups/figma/components/navigation/
├── README.md                 # This spec
├── wireframes/               # PNG/SVG exports (optional)
├── figma-refs.json           # Mappings to Figma nodes (optional)
└── notes.md                  # Design decisions & ADR links


⸻

🎨 Figma Linkage (Authoritative Mapping)

Keep this table in sync when Figma frame/component names change.
The Node ID values come from Figma “Copy link” (node-id query param).

Artboards (Frames)

Area	Figma Page	Frame Name	Node ID	Purpose
Header	KFM · UI	Header · Nav	0:1	Brand, search, utility buttons
Timeline	KFM · UI	Timeline · Controls	0:2	Range handles, zoom, play/pause
Layers	KFM · UI	Sidebar · Layers + Legend	0:3	Layer toggles, opacity, legend
Detail	KFM · UI	Detail Panel · Entity	0:4	Entity dossier + sources
Map	KFM · UI	Map View · MapLibre	0:5	Map viewport + overlays

Components ↔ Code Regions

Figma Component	Code Region / Hook	Notes
Comp/SearchField	nav.search	Ctrl + / shortcut; async suggestions (ARIA live region)
Comp/LayerToggle	nav.layers	role="switch"; tri-state supported during fetch
Comp/OpacitySlider	nav.layers.opacity	Keyboard arrows; role="slider"
Comp/TimeHandle	nav.timeline.handle	Focus ring; snap increments
Comp/PlayButton	nav.timeline.play	Toggle play/pause; disabled while fetching
Comp/DetailPanel	nav.detail	aria-expanded; selection history

If you maintain a JSON mapping, store it as figma-refs.json:

{
  "frames": {
    "header":   {"page": "KFM · UI", "name": "Header · Nav", "node": "0:1"},
    "timeline": {"page": "KFM · UI", "name": "Timeline · Controls", "node": "0:2"},
    "layers":   {"page": "KFM · UI", "name": "Sidebar · Layers + Legend", "node": "0:3"}
  },
  "components": {
    "SearchField": {"hook": "nav.search"},
    "LayerToggle": {"hook": "nav.layers"},
    "TimeHandle":  {"hook": "nav.timeline.handle"}
  }
}


⸻

🧩 Component Structure

Header
 ├─ Brand / Home
 ├─ Global Search
 └─ Utility (Help · Language · Auth)

Main
 ├─ Sidebar (Layer Controls · Legend)
 ├─ Map View (MapLibre)
 └─ Detail Panel (Entity Information)

Footer
 └─ Timeline (Handles · Zoom · Play)


⸻

🗺️ System Integration (GitHub-safe Mermaid)

flowchart LR
  subgraph UI["User Interface"]
    A["Header\nsearch · menus · help"]
    B["Timeline\nrange · zoom · play"]
    C["Layers\nvisibility · opacity"]
    D["Detail Panel\nentity dossier"]
  end

  subgraph STATE["Application State"]
    E["selectedTimeRange"]
    F["activeLayers"]
    G["selectedEntity"]
  end

  subgraph API["Backend API"]
    H["GET /events?start&end"]
    I["GET /layers-config"]
    J["GET /entity/{id}"]
  end

  subgraph MAP["Renderer"]
    K["MapLibre View\nfilters by time & layer"]
  end

  A --> B
  A --> C
  A --> D

  B --> H
  C --> I
  D --> J

  H --> E
  I --> F
  J --> G

  E --> K
  F --> K
  G --> K

<!-- END OF MERMAID -->



⸻

🧱 State & Interaction Model

Region	Default	Interaction / Focus	Active / Loading	Empty / Error
Header	Visible, home link	Tab / click	—	—
Search	Placeholder; Ctrl + /	Focus ring; async suggestions	Spinner while fetching	“No results”
Layers	Base visible	Toggle + tooltip legend	Disabled during fetch	“Layer unavailable”
Timeline	Default project window	Arrow keys / drag handles	Loading or playing animation	“No events”
Detail Panel	Collapsed	Open on select (Enter / click)	Skeleton loader	“No details available”


⸻

♿ Accessibility
	•	Landmarks: header[role="banner"], nav[aria-label="Layer controls"], main, aside[role="complementary"], footer[role="contentinfo"]
	•	Keyboard: Tab/Shift+Tab traversal; Ctrl + / focuses Search; Esc closes Detail; arrows adjust sliders
	•	ARIA: role="search", role="slider", role="switch", aria-expanded, aria-controls, live region for search results
	•	Motion/Contrast: Respect prefers-reduced-motion; maintain WCAG AA contrast

⸻

🎛 Design Tokens

Token	Purpose
--kfm-color-bg, --kfm-color-surface, --kfm-color-text	Base surfaces & text
--kfm-color-accent, --kfm-color-accent-contrast	Primary actions
--kfm-focus-ring	Focus outline color/style
--kfm-space-2/4/6/8	Spacing scale
--kfm-radius-2xl	Panel corner radius
--kfm-z-nav, --kfm-z-detail, --kfm-z-tooltip	Z-index layers


⸻

🔗 Data Contracts

Global Search

GET /search?q={q}

{
  "hits": [
    {"id": "ent:ks:Topeka", "type": "place", "label": "Topeka, Kansas"},
    {"id": "evt:1861:statehood", "type": "event", "label": "Kansas Statehood (1861)"}
  ]
}

Emits: nav.select(entityId)

Timeline

GET /events?start=1850-01-01&end=1870-12-31

[
  {"id":"evt:1854:kansas-nebraska","type":"act","t0":"1854-05-30","title":"Kansas–Nebraska Act"},
  {"id":"evt:1861:statehood","type":"statehood","t0":"1861-01-29","title":"Kansas Statehood"}
]

State: { "start": ISODate, "end": ISODate, "zoom": number }
Emits: nav.time.change(range) (debounced ~250 ms)

Layers (STAC-derived)

GET /layers-config

{
  "layers": [
    {"id":"basemap.terrain","label":"Terrain","type":"raster","visible":true,"opacity":1.0},
    {"id":"hist.topomaps","label":"Historic Topo Maps","type":"raster","visible":false,"opacity":0.8},
    {"id":"hydro.rivers","label":"Rivers","type":"vector","visible":true,"opacity":1.0}
  ]
}

State: { "<layerId>": { "visible": boolean, "opacity": 0.0..1.0 } }
Emits: nav.layers.change(state) (persist to localStorage)

Detail Panel

GET /entity/{id}

{
  "id":"ent:ks:Topeka",
  "label":"Topeka, Kansas",
  "summary":"Capital on the Kansas River.",
  "links":[{"rel":"source","href":"..."}]
}

Emits: nav.detail.open(id) / nav.detail.close()

⸻

📱 Responsive Rules
	•	≥ 1280 px: Layers sidebar open; Detail collapsible; Timeline 140–180 px
	•	768–1279 px: Layers collapsed; Detail overlays map; Timeline ~120 px
	•	< 768 px: Compact header; Search modal; single overlay sidebar; collapsible timeline

⸻

🧪 QA Checklist
	•	Headings, tables, Mermaid, and code fences render correctly on GitHub
	•	Full keyboard traversal with visible focus (do not remove outlines)
	•	Screen reader labels/roles present; live announcements for async search results
	•	Debounced timeline requests; layer state persists; clear error messages
	•	Timeline ↔ Map synchronization verified (time filter honored)

⸻

🧾 Changelog

Version	Date	Notes
v1.2	2025-10-05	Added Figma linkage section + badge grid; tightened Mermaid labels
v1.1	2025-10-05	GitHub-compliant redesign; removed HTML wrappers
v1.0	2025-10-04	Initial component spec


⸻

Contributor Rules (Formatting)
	•	Pure Markdown headings; no <div align> wrappers
	•	Mermaid labels quoted; line breaks via \n; end block exactly as shown above
	•	Keep badge URLs relative upward where possible
	•	Update Figma tables whenever node IDs change

⸻

If any section still renders oddly in your repo, point me to the exact file path & commit and I’ll align spacing and tables to your repo’s Markdown lints (some repos enforce MDX/remark rules that tweak table spacing).
