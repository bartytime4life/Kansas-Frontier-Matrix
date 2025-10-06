🧭 Navigation Components — Figma → KFM UI

docs/design/mockups/figma/components/navigation/README.md

Purpose: This guide standardizes how we design, name, export, and implement navigation components (header, sidebars, menus, breadcrumbs, tabs, timeline controls) so they render cleanly in GitHub and map 1-to-1 into the KFM React/MapLibre UI. It follows our web-UI architecture and MCP documentation conventions.

⸻

📚 Contents
	•	Scope
	•	Directory layout
	•	Design tokens (quick reference)
	•	Component inventory
	•	Figma → repo export workflow
	•	Naming & file conventions
	•	Accessibility checklist
	•	Mermaid system map
	•	Do / Don’t
	•	Contributing checklist

⸻

🎯 Scope

These assets cover global app navigation and time/space navigation specific to KFM:
	•	Global: top app bar, primary/secondary menus, command palette trigger, sidebar section switcher, search, breadcrumbs, tabs.
	•	Temporal/Spatial: timeline rail + handles, zoom controls, layer legend toggle, filter trays, map toolbar.

All components must map cleanly to the React SPA (frontend) and FastAPI data endpoints that drive the timeline and map state.

⸻

📁 Directory layout

docs/
└─ design/
   └─ mockups/
      └─ figma/
         └─ components/
            └─ navigation/
               ├─ README.md                  # this file
               ├─ tokens.md                  # extended token notes (optional)
               ├─ export/                    # exported SVG/PNG (sliced from Figma)
               │  ├─ header/
               │  ├─ sidebar/
               │  ├─ menus/
               │  ├─ timeline/
               │  └─ controls/
               └─ specs/
                  ├─ header.spec.md
                  ├─ sidebar.spec.md
                  ├─ timeline.spec.md
                  └─ menus.spec.md

Use monospace code fences for trees and keep indent widths consistent so grids/trees render correctly in GitHub.

⸻

🎨 Design tokens (quick reference)

Use tokens to keep Figma and code in sync with our React/MapLibre UI.

Token	Example value	Notes
--kfm-color-bg	#0b1020 / #ffffff	Auto switch dark/light
--kfm-color-fg	#e9edf3 / #0f1216	Body text
--kfm-color-accent	#4ea1ff	Focus rings, active states
--kfm-radius-xl	16px	Cards/menus corners
--kfm-gap-xs..xl	4, 8, 12, 16, 24	Spacing scale
--kfm-z-nav	1000	Keep nav above map canvas
--kfm-tap-target	44px	Touch min size (a11y)

Map overlays & timeline are GPU-accelerated; keep shadows subtle and avoid heavy blurs.

⸻

📦 Component inventory

Each navigation component below has a Figma frame name, an intended React mapping, and status.

Component	Purpose	Figma Frame	React Mapping (example)	Status
App Header (Top Bar)	Brand, search, primary actions	nav/header/default	<Header />	✅
Left Sidebar (Layers)	Layer toggles, legends, filters	nav/sidebar/layers	<LayerSidebar />	✅
Right Panel (Details)	Entity/timeline details	nav/sidebar/details	<DetailsPanel />	✅
Main Menu / Kebab	Secondary actions	nav/menus/kebab	<OverflowMenu />	✅
Breadcrumbs	Hierarchy & quick back	nav/breadcrumbs	<Breadcrumbs />	✅
Tabs (Section Switcher)	Swap sections (Map / Timeline / Docs)	nav/tabs/primary	<Tabs />	✅
Timeline Rail + Handles	Time navigation	nav/timeline/rail	<Timeline />	✅
Timeline Zoom+Snap	Zoom & snapping to periods	nav/timeline/controls	<TimelineControls />	✅
Map Toolbar	Zoom, locate, measure, reset view	nav/controls/map	<MapToolbar />	✅
Command Palette (⌘K)	Global command/search	nav/command	<CommandPalette />	🔄

These map to the SPA and API endpoints used by timeline and map (e.g., /events?start=…&end=…, /layers-config, /entity/{id}).

⸻

📤 Figma → repo export workflow
	1.	Name frames & variants predictably
	•	nav/<area>/<component>[/variant] (e.g., nav/timeline/rail/compact).
	2.	Slice & export
	•	Export SVG for icons, PNG @2x for composite mocks; keep transparent backgrounds.
	3.	Drop into export/ under the matching subfolder (see tree above).
	4.	Spec files
	•	For each component, create specs/<component>.spec.md with: anatomy, states, spacing, tokens, and a “dev notes” callout linking to React mapping.
	5.	Open a PR with before/after thumbnails in the description to ease review (use collapsible sections for long images).

⸻

🧾 Naming & file conventions
	•	Frames: nav/<region>/<component>/<state> (lowercase, kebab-case inside segments).
	•	Icons: ic-<name>-24.svg (24px grid).
	•	Specs: One spec per component; include success, hover, active, focus, disabled states.
	•	ARIA & roles: Annotate in spec (e.g., role="tablist", aria-current="page").
	•	Do not embed HTML <div align="center"> in docs—use pure Markdown headings and tables for reliable GitHub rendering.

⸻

♿ Accessibility checklist
	•	Keyboard: Tab / Shift+Tab traversal order matches visual order; Esc closes menus/panels.
	•	Focus: Visible 3:1 contrast ring using --kfm-color-accent.
	•	Hit area: ≥ 44×44 px for touch.
	•	Labels: aria-label/aria-expanded on toggles and menus; aria-current on active tab/breadcrumb.
	•	Timeline: Provide text equivalents (e.g., “Showing 1850–1875”) and buttons for zoom/snap.
	•	Color: All states meet WCAG AA for text/controls.
(Reference these in each *.spec.md.)

⸻

🗺 Mermaid system map

Diagram of how navigation surfaces coordinate the Timeline, Map, and API. The syntax matches our project mermaid rules and renders in GitHub.

flowchart LR
  A["Header\nsearch · menus · tabs"] --> B["Timeline\nrail · handles · zoom"]
  A --> C["Map Toolbar\nzoom · locate · layers"]
  B --> D["API\nGET /events?start&end"]
  C --> E["API\nGET /layers-config"]
  A --> F["Details Panel\nGET /entity/{id}"]
  D --> G["React State\nselectedTimeRange"]
  E --> H["React State\nactiveLayers"]
  F --> I["React State\nselectedEntity"]

<!-- END OF MERMAID -->


Keep labels short, escape line breaks with \n, and always end Mermaid blocks with the comment marker to satisfy our strict parser.

⸻

✅ Do / ❌ Don’t

Do
	•	Use tokens (colors, radius, spacing) and include them in specs.
	•	Provide clear keyboard order and focus states.
	•	Export clean SVGs (merged shapes, no stray groups).
	•	Write brief variant rationale (e.g., compact vs. roomy sidebar).

Don’t
	•	Don’t rely on absolute pixel positioning that won’t translate to responsive React.
	•	Don’t mix icon sizes; standardize to 24px grid.
	•	Don’t paste large images raw into README—use export/ and thumbnails with collapsible sections.

⸻

🧩 Contributing checklist
	•	Figma frame named per convention.
	•	Exported assets placed under export/<component>/.
	•	specs/<component>.spec.md added/updated (anatomy, states, tokens, ARIA).
	•	Screenshots added to PR (collapsed).
	•	Verified Mermaid block renders locally (if included).
	•	Links to Web UI Design Doc / Web UI Architecture where relevant for dev handoff.

⸻

References
	•	KFM Web UI Design Document — app structure, timeline & map behaviors.
	•	KFM Web UI Architecture — component/data flow between React and FastAPI/Neo4j.
	•	Generate architecture file — project-approved Mermaid block style.
	•	Advanced GitHub Formatting — tables, badges, collapsible sections; keep docs GitHub-clean.
