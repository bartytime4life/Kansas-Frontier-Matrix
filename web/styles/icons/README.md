# `web/styles/icons/`

This directory holds **SVG icon assets** and any related CSS helper classes  
for the **Kansas Frontier Matrix web viewer**.

---

## Purpose

- Provide a consistent, lightweight icon set for:
  - Map controls (zoom, geolocate, reset, legend toggle)
  - Timeline controls (play/pause, next/prev)
  - Layer visibility toggles (eye/eye-off)
  - Status indicators (loading, warning, info)
- All icons are optimized SVGs for performance and accessibility.

---

## Directory Layout

web/styles/icons/
├── readme.md          # This file
├── map/               # Map-related icons
│   ├── zoom-in.svg
│   ├── zoom-out.svg
│   ├── compass.svg
│   └── geolocate.svg
├── timeline/          # Timeline/player icons
│   ├── play.svg
│   ├── pause.svg
│   ├── step-back.svg
│   └── step-forward.svg
├── layers/            # Layer visibility and legend
│   ├── eye.svg
│   ├── eye-off.svg
│   ├── legend.svg
│   └── filter.svg
└── status/            # Status & UI feedback
├── loading.svg
├── info.svg
├── warning.svg
└── error.svg

---

## Usage

### Inline SVG
Recommended for full control (color, size via CSS):

```html
<button class="map-btn">
  <svg class="icon"><use href="web/styles/icons/map/zoom-in.svg#icon"></use></svg>
</button>

Background Images

For simple decorative use:

.btn-zoom-in {
  background: url("../icons/map/zoom-in.svg") no-repeat center;
  background-size: 1.25rem 1.25rem;
}


⸻

Design Guidelines
	•	Stroke-first style: Icons are line-based with 2px strokes, consistent with
MapLibre’s default aesthetic.
	•	Scalable: Designed at 24×24 viewBox for easy scaling.
	•	Accessible: Inline SVGs should include aria-hidden="true" or <title>
for screen readers when meaningful.
	•	Color: Inherit current text color (fill: currentColor; stroke: currentColor;).

⸻

Notes
	•	Keep SVGs minimized (use SVGO).
	•	Prefer symbols with <use> for reuse and caching.
	•	For high-contrast themes (light/dark), rely on CSS currentColor.

⸻

✅ With this structure, all map/timeline/layer/hazard controls can share
a common visual language, while keeping the bundle small and maintainable.

