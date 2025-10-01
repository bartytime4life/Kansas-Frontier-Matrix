<div align="center">

# 🎨 Kansas-Frontier-Matrix — CSS Layering  
`web/css/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Provide the **styling system** for the MapLibre web viewer.  
CSS is **layered** so structure, theming, MapLibre polish, and reusable UI parts stay modular and easy to maintain.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["layout.css\n(App shell & structure)"] --> B["theme.css\n(Color tokens & theming)"]
  B --> C["map.css\n(MapLibre polish & UI)"]
  C --> D["components.css\n(Reusable widgets)"]
  D --> E["Viewer\n(web/index.html · app.js)"]

<!-- END OF MERMAID -->



⸻

📦 Files (by responsibility)
	•	layout.css — App shell & structure
Grid (toolbar, sidebar, map), panels (cards, toggles, sliders, timeline), responsive/mobile drawer, safe-area/RTL hooks.
Treat this file as the skeleton of the web app.
	•	theme.css — Skinning layer
Color palettes, typography, elevation, radii, and utility tokens (--kfm-*) with a compat bridge to core tokens (--bg, --panel, --text, …).
Supports system light/dark and class-forced themes (.kfm-theme-dark, .kfm-theme-light).
	•	map.css — MapLibre polish
Theming for MapLibre controls, popups, legend, timeline dock, side info panel (all .kfm-* map UI).
Handles safe-area margins, RTL, :focus-visible, reduced motion, and forced colors.
	•	components.css — Reusable UI components
Buttons, cards, sliders (with filled-track pattern), toggles, popups/tooltips.
Designed to work with layout.css/theme.css tokens; no hard-coded colors.
	•	(optional future) theme-alt.css — Alternate themes (e.g., sepia / parchment for archival maps).

⸻

🔗 Usage order

Always include in this order:

<link rel="stylesheet" href="css/layout.css">     <!-- structure -->
<link rel="stylesheet" href="css/theme.css">      <!-- skin/tokens -->
<link rel="stylesheet" href="css/map.css">        <!-- MapLibre polish -->
<link rel="stylesheet" href="css/components.css"> <!-- reusable UI -->

This guarantees tokens are defined before map/components overrides, and ensures safe-area/RTL rules cascade correctly.

⸻

🎛️ Design tokens

All layers use CSS custom properties at :root.

Core tokens (consumed by layout/components/map):
	•	Surfaces & ink: --bg, --panel, --panel-2, --text, --muted, --border
	•	Accents: --accent, --accent-2, --danger
	•	Geometry: --radius, --radius-sm, --radius-xs
	•	Elevation: --shadow-1, --shadow-2, --shadow
	•	Typography: --font, --mono
	•	A11y & safe areas: --focus-ring, --safe-top/right/bottom/left

Theme tokens (native to theme.css):
	•	--kfm-bg, --kfm-surface, --kfm-border, --kfm-ink, --kfm-ink-dim, --kfm-accent, …
These map to the core tokens so you can reskin without touching structure.

Changing tokens in theme.css propagates across the app.

⸻

📱 Responsiveness & behavior
	•	Desktop: Sidebar docked (grid: sidebar | map).
	•	Mobile (≤1024px): Sidebar becomes a drawer — toggled by JS with .is-open.
	•	Timeline / overlays: re-position to edges, with safe-area insets to avoid notches.
	•	Range sliders: unified filled-track pattern; JS sets --value (0–100%).

⸻

♿ Accessibility
	•	Focus rings: use :focus-visible with --focus-ring (components) or --focus (layout).
	•	Reduced motion: @media (prefers-reduced-motion: reduce) disables transitions/animations.
	•	High contrast: @media (forced-colors: active) uses system colors and removes shadows.
	•	RTL: safe-area and key components account for [dir="rtl"].

⸻

🤝 Contribution guidelines
	•	Add new layout/structure to layout.css.
	•	Add color/typography/visual rules to theme.css.
	•	Add/extend MapLibre UI in map.css.
	•	Add/extend reusable widgets in components.css.
	•	Prefer tokens over hard-coded values; keep safe-area/RTL in mind.
	•	Test in light/dark, desktop/mobile, and with reduced motion + forced colors.

⸻

🗂️ Quick reference

File	Role	Safe to edit?
layout.css	Structure & UI shell	Yes (new layout/structure)
theme.css	Colors & style tokens	Yes (preferred place for theme changes)
map.css	MapLibre & map UI polish	Yes (controls, popups, legend)
components.css	Reusable UI components	Yes (buttons, cards, sliders, toggles)


⸻

🧩 Tips
	•	Import paths relative to web/ (e.g., css/layout.css).
	•	Keep sidebar drawer behavior consistent with JS (.is-open).
	•	For sliders, ensure JS updates --value to keep the filled track in sync.
	•	Use GitHub Pages friendly paths (./…, not ../…).

⸻

📚 See also
	•	../components/ — UI modules (timeline, legend, sidebar, popup)
	•	../assets/palette.json — design tokens that can feed theme.css
	•	Root README.md and web/ docs for viewer wiring

⸻

✅ Mission Principle

This modular CSS system makes it easy to scale, reskin, and maintain the Kansas-Frontier-Matrix viewer.

⸻


