# `web/styles/` — Viewer Styles & Themes

This folder contains the **styling assets** for the Kansas Frontier Matrix web viewer.  
It defines the **look-and-feel** of the map, overlays, timeline, and UI components, with light/dark theming and accessible defaults.

---

## Design Goals

- **Consistency** — shared tokens for color, typography, spacing, and elevations.
- **Modularity** — small CSS files with clear scopes (base, map, theme).
- **Declarative** — styles are driven by variables and semantic CSS classes.
- **Extensibility** — add a layer/category/icon without touching core code.
- **Accessibility** — high-contrast palettes, focus rings, reduced motion friendly.

---

## Directory Layout

web/styles/
├─ base.css           # Global reset + design tokens (colors, spacing, z-index, typography)
├─ map.css            # Map UI (MapLibre controls, legends, popups, clusters, measuring)
├─ theme-light.css    # Light theme variables (semantic ramps for hydro/terrain/etc.)
├─ theme-dark.css     # Dark theme variables (night-friendly ramps and surfaces)
└─ icons/             # Inline/URL SVGs & helpers (see icons/readme.md)
└─ readme.md

> The README you are reading is `web/styles/README.md`.

---

## Load Order (very important)

**Always load CSS in this order:**

```html
<link rel="stylesheet" href="web/styles/base.css">
<link rel="stylesheet" href="web/styles/map.css">
<link rel="stylesheet" href="web/styles/theme-light.css">
<link rel="stylesheet" href="web/styles/theme-dark.css">

	•	base.css sets the baseline variables and resets.
	•	map.css styles map/timeline/sidebar/popups/controls.
	•	theme-light.css and theme-dark.css provide overrides (variables + utilities).
They support both prefers-color-scheme and an explicit class hook.

Activating a Theme

You can rely on the OS preference or force a theme with a class:

<!-- Auto: OS preference determines theme -->
<body>…</body>

<!-- Force light -->
<body class="theme-light">…</body>

<!-- Force dark -->
<body class="theme-dark">…</body>

If both a class and prefers-color-scheme apply, the explicit .theme-light/.theme-dark class wins.

⸻

Key Connections & Conventions
	•	Sidebar spacing — map.css reserves room for .sidebar when the root has .has-sidebar.
The reserved width matches the sidebar width declared in CSS:
	•	desktop: 280px, mobile: 220px
	•	add .has-sidebar to <body> when the sidebar is mounted.

<body class="has-sidebar">
  <aside class="sidebar">…</aside>
  <div id="map"></div>
</body>

	•	Map container — the viewer expects a full-viewport #map (absolute, inset: 0), managed by map.css.
	•	Z-index layers — use tokens from base.css: --z-map, --z-overlay, --z-sidebar, --z-modal.
	•	Focus rings — themed via --focus-ring to ensure keyboard accessibility.
	•	Time filtering — add .time-active to visually accent features in range; .time-muted to de-emphasize out-of-range features (applied by the timeline controller).

⸻

Working With Icons

See web/styles/icons/readme.md for structure and guidance.

Inline SVG (recommended for color via currentColor)

<button class="map-btn" aria-label="Zoom in">
  <svg class="icon" width="24" height="24" aria-hidden="true">
    <use href="web/styles/icons/map/zoom-in.svg#icon"></use>
  </svg>
</button>

As Background Image

.btn-legend {
  background: url("../styles/icons/layers/legend.svg") no-repeat center;
  background-size: 1.25rem 1.25rem;
}

Tip: Inline SVGs inherit text color (currentColor), so they adapt to light/dark themes automatically.

⸻

Tokens & Semantic Ramps

The theme files expose semantic variables for consistent cartography:
	•	Hydrology: --hydro-100 … --hydro-700
	•	Terrain/Elevation: --terrain-100 … --terrain-700
	•	Vegetation: --veg-100 … --veg-700
	•	Hazards: --hazard-flood, --hazard-drought, --hazard-wildfire, --hazard-tornado
	•	Treaties/Boundaries: --treaty-fill, --treaty-stroke
	•	Rails/Trails: --rail-line, --trail-line

Use them for layer styling in your map style JSON or JS-driven layer definitions to maintain visual coherence across themes.

⸻

Example: Adding a New Symbol & Legend Entry
	1.	Add icon to web/styles/icons/ (e.g., treaties/treaty.svg).
	2.	Reference in your layer style or legend config (example from a JSON-based legend):

{
  "treaties": {
    "label": "Treaty Boundaries",
    "icon": "web/styles/icons/layers/legend.svg",
    "fillColor": "var(--treaty-fill)",
    "strokeColor": "var(--treaty-stroke)"
  }
}

	3.	Style the map layer (MapLibre layer paint example):

map.addLayer({
  id: 'treaties-fill',
  type: 'fill',
  source: 'treaties',
  paint: {
    'fill-color': ['coalesce', ['to-color', ['get', 'fillColor']], 'var(--treaty-fill)'],
    'fill-opacity': 0.5
  }
});

Use CSS variables where possible—your styles will adapt across themes automatically.

⸻

Troubleshooting & “Fix Connections”
	•	Paths on GitHub Pages: Use relative URLs like web/styles/icons/... from your HTML root.
	•	Theme not switching: Confirm the body has .theme-light or .theme-dark and that theme CSS loads after base.css.
	•	Sidebar overlap: Ensure <body class="has-sidebar"> is present when the sidebar mounts.
	•	Icon color not changing: Prefer inline SVG (with currentColor) over <img> when you want theme-aware coloring.
	•	MapLibre controls hidden: map.css sets .maplibregl-control-container with pointer-events: none at the wrapper but restores pointer-events: auto on .maplibregl-ctrl. If you replace class names, keep that pattern.

⸻

Accessibility & QA Checklist
	•	Check color contrast in both themes (WCAG AA for text/icons).
	•	Verify keyboard focus outlines on all interactive elements.
	•	Ensure hover is not the only affordance (add active/focus states).
	•	Test reduced-motion preferences if adding animations later.

⸻

Minimal Boot Snippet

<!doctype html>
<html lang="en" class="theme-light">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <link rel="stylesheet" href="web/styles/base.css">
  <link rel="stylesheet" href="web/styles/map.css">
  <link rel="stylesheet" href="web/styles/theme-light.css">
  <link rel="stylesheet" href="web/styles/theme-dark.css">
  <title>Kansas Frontier Matrix</title>
</head>
<body class="has-sidebar">
  <aside class="sidebar">…</aside>
  <div id="map"></div>
  <div class="timeline">…</div>
  <script src="web/app.js" type="module"></script>
</body>
</html>


⸻

✅ Single source of truth: The web/styles/ folder houses the tokens, themes, and shared UI rules that keep Kansas’s historical layers visually coherent, accessible, and mission-grade.

