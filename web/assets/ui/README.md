<div align="center">

# 🎛️ Kansas-Frontier-Matrix — UI Icons & Elements  
`web/assets/ui/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Store **small UI icons and vector elements** used by the web viewer  
(buttons, toggles, chevrons, zoom controls, etc.).  

These assets ensure a **consistent, lightweight design system** across the MapLibre viewer and site.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Design tokens\n(palette.json · typography.json)"] --> B["UI SVGs\n(icons, controls)"]
  B --> C["Optimize\n(svgo · remove metadata)"]
  C --> D["UI Assets\n(web/assets/ui/)"]
  D --> E["Integrated in app.js & app.css"]
  E --> F["Viewer build & deploy"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

web/assets/ui/
├── chevron-left.svg
├── chevron-right.svg
├── zoom-in.svg
├── zoom-out.svg
├── layers-toggle.svg
├── legend.svg
└── README.md

	•	Chevron icons → navigation (timeline, carousels)
	•	Zoom controls → MapLibre UI buttons
	•	Layers toggle → show/hide map overlays
	•	Legend icons → small helper graphics

⸻

🧭 Conventions
	•	Format → SVG only (scalable, lightweight, CSS-stylable)
	•	Naming → lowercase-hyphenated (zoom-in.svg, layers-toggle.svg)
	•	Optimize → run svgo before commit
	•	Style → use currentColor for fills/strokes where possible, so icons inherit theme colors
	•	Size → default viewBox should be square (0 0 24 24 or 0 0 32 32)

⸻

📑 Example Icon (zoom-in.svg)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M11 8v3H8v2h3v3h2v-3h3v-2h-3V8h-2z"/>
  <circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

	•	Uses currentColor → inherits UI theme from palette.json
	•	Simple paths, minimal markup

⸻

🔗 Integration
	•	app.js → loads icons dynamically or inlines them into UI controls
	•	app.css → can reference icons via mask-image or background-image
	•	Viewer tests → ensure required icons (zoom, chevrons, layers) exist

⸻

📝 Notes
	•	✅ Keep icons ≤5 KB each
	•	✅ Use consistent stroke width and corner radii for a unified look
	•	❌ Do not embed text or external fonts in SVGs
	•	❌ Do not include large illustrations/screenshots here (use web/assets/screenshots/)

⸻

📚 See Also
	•	../ → global web assets (logos, palette, typography)
	•	../icons/ → platform/browser favicons & app icons
	•	../../config/ → viewer config referencing icons
	•	../../tests/ → tests checking asset presence

⸻

✅ Mission Principle

UI icons must be clean, optimized, themeable, and reusable.
They enable a consistent and lightweight user experience in the Frontier Matrix web viewer.
