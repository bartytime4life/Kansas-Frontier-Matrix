<div align="center">

# 🖼️ Kansas Frontier Matrix — Public Assets  
`web/public/assets/`

**Logos · Icons · Images · Maps**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../docs/design/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/public/assets/` directory contains **static media and brand assets**  
used throughout the Kansas Frontier Matrix web application.  
These include **logos, icons, placeholder images, and map overlays**  
used in components such as the Header, MapView, Timeline, and Modals.

All assets here are **served directly from the CDN or build output** and  
are not processed by Vite or Webpack. This ensures predictable URLs and  
long-term caching for production deployments.

Design and color palettes follow the **Kansas Frontier Matrix Design System**  
under the **Master Coder Protocol (MCP)** — guaranteeing consistency,  
reproducibility, and provenance tracking for every image or icon.

---

## 🧱 Directory Structure

```text
web/public/assets/
├── logo.svg                # Primary logo (vector)
├── logo-dark.svg           # Dark theme logo variant
├── favicon-32x32.png       # Browser favicon
├── icons/                  # UI icons for map, timeline, AI, etc.
│   ├── map-marker.svg
│   ├── timeline.svg
│   ├── ai-bot.svg
│   ├── filter.svg
│   └── info.svg
├── images/                 # Static illustrations and placeholder media
│   ├── placeholder.jpg
│   ├── header-bg.jpg
│   └── prairie-sunrise.jpg
├── maps/                   # Geospatial overlays, scanned maps, static tiles
│   ├── topo_1894_overlay.png
│   ├── treaty_boundaries_outline.svg
│   └── hydrology_network_light.svg
└── README.md               # This documentation file


⸻

🎨 Design System Integration

Assets align with the official Design Mockups stored under
docs/design/mockups/ and the theme tokens from web/config/themes.json.

Token	Example	Use
--kfm-color-accent	#00b3b3	Logo & primary highlight color
--kfm-color-bg-dark	#0b1020	Background fill for dark variant
--kfm-radius	1rem	Icon rounding and corner consistency
--kfm-shadow	0 2px 8px rgba(0,0,0,0.15)	Drop shadows for UI icons

All vector assets (.svg) should use CSS variables for color fills, allowing
automatic adaptation to theme changes (light/dark).

Example:

<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <circle cx="32" cy="32" r="30" fill="var(--kfm-color-accent)" />
</svg>


⸻

🧩 Asset Provenance

Asset	Source	License	Purpose
logo.svg	Custom KFM design (Figma export)	MIT	Main site logo
map-marker.svg	Custom KFM icon set	MIT	MapView marker icon
ai-bot.svg	RemixIcon derivative	MIT	AI Assistant
placeholder.jpg	Unsplash (public domain)	CC0	Demo image for empty states
topo_1894_overlay.png	USGS Public Archive	Public Domain	Historic map overlay
treaty_boundaries_outline.svg	Digitized by KFM Team	CC-BY 4.0	Treaty visualization layer

All third-party assets include a metadata header embedded in their filename
or an accompanying .json descriptor under assets/meta/.

⸻

🗺️ Usage in Components

Component	Asset Used	Description
Header	logo.svg, logo-dark.svg	Displayed in the navigation bar
MapView	/icons/map-marker.svg, /maps/topo_1894_overlay.png	Map markers and historical overlays
TimelineView	/icons/timeline.svg	Timeline toolbar icon
AIAssistant	/icons/ai-bot.svg	Assistant avatar
Modals	/icons/info.svg, /icons/filter.svg	Contextual icons for help/settings
Public Branding	favicon-32x32.png, apple-touch-icon.png	Used in web manifest and browser tabs


⸻

📦 Asset Optimization

All raster images undergo optimization using Sharp or ImageMagick
in the CI pipeline:
	•	PNGs compressed with pngquant --quality=80-95
	•	JPEGs optimized with mozjpeg -quality 85
	•	SVGs minified with svgo --multipass
	•	Checksum (.sha256) generated for each asset in build output

Optimized assets are published to the CDN or GitHub Pages under /assets/.

⸻

♿ Accessibility and Compliance
	•	All decorative images include role="presentation" or empty alt attributes.
	•	Informational graphics (maps, icons) include descriptive alt text or ARIA labels.
	•	Icons use scalable vector paths to ensure crispness on high-DPI displays.
	•	Colors adhere to WCAG 2.1 AA contrast guidelines.
	•	Fallbacks provided for older browsers that do not support SVG.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Design mockups, icon sets, STAC overlays
Outputs	Optimized, versioned static assets
Dependencies	Sharp, SVGO, TailwindCSS, Figma Export
Integrity	SHA256 checksums, license metadata, Git version control


⸻

🔗 Related Documentation
	•	Web Public README
	•	Web Configuration
	•	Design Mockups
	•	Accessibility Guidelines

⸻

📜 License

All custom KFM assets are released under the MIT License,
with external assets attributed under their respective open licenses.

© 2025 Kansas Frontier Matrix — Produced under the Master Coder Protocol (MCP)
for verifiable provenance, open-source accessibility, and long-term archival value.

“Every pixel and vector tells a story — the assets here visualize Kansas’s living history.”

