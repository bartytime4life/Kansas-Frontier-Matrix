<div align="center">

# 🖼️ Kansas Frontier Matrix — Public Images  
`web/public/assets/images/`

**Static Illustrations · Backgrounds · Thumbnails**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../../docs/design/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/public/assets/images/` directory contains **raster-based images and illustrations**  
used throughout the Kansas Frontier Matrix web application.  
These assets support the visual storytelling layer of the platform —  
ranging from **backgrounds**, **header banners**, and **historical photos**,  
to **placeholder images** and **component thumbnails** used in documentation or loading screens.

All images here are **served statically** from the public CDN and are not bundled or transformed by the Vite build process.  
They are optimized, compressed, and stored under open or public domain licenses with metadata provenance tracking.

---

## 🧱 Directory Structure

```text
web/public/assets/images/
├── placeholder.jpg          # Fallback image for empty states
├── header-bg.jpg            # Top banner background
├── prairie-sunrise.jpg      # Thematic hero image for landing page
├── kansas-river-aerial.webp # Optimized web background for hydrology sections
├── topo-overlay.png         # Historic topographic image overlay
├── timeline-bg.jpg          # Timeline gradient or texture background
├── thumbnails/              # Component thumbnails and documentation imagery
│   ├── timeline-thumb.png
│   ├── mapview-thumb.png
│   └── aiassistant-thumb.png
└── README.md                # This documentation file


⸻

🧩 Asset Categories

Category	Description	Format	Example Use
Backgrounds	Full-width hero or panel backgrounds for headers and sections.	JPG / WEBP	Landing pages, Modals
Placeholders	Default images used when datasets lack visual content.	JPG	DetailPanel, cards
Illustrations	Scenic or abstract Kansas imagery for storytelling.	JPG / PNG	Home and About sections
Overlays	Transparent PNGs layered on the MapView or Timeline.	PNG	MapView topographic overlay
Thumbnails	Small UI representations for documentation or AI-generated content previews.	PNG	Docs, tooltips


⸻

🧠 Design & Theming Guidelines

All image selections and processing adhere to the Kansas Frontier Matrix Design System:
	•	Aspect Ratio → Prefer 16:9 or 21:9 for hero backgrounds.
	•	Resolution → Minimum width 1920 px (desktop) or 1280 px (tablet).
	•	Compression → JPEG quality ≈ 85, WebP quality ≈ 80.
	•	Color Palette → Harmonized to match the app’s theme:
	•	Accent: #00b3b3
	•	Neutral backgrounds: #0b1020 (dark) / #ffffff (light)
	•	Dynamic Theming: Use prefers-color-scheme CSS to swap images (e.g., header-bg-dark.jpg).

Example:

body {
  background-image: url("/assets/images/header-bg.jpg");
}
@media (prefers-color-scheme: dark) {
  body {
    background-image: url("/assets/images/header-bg-dark.jpg");
  }
}


⸻

🧮 Optimization Pipeline

Each raster asset passes through the automated CI compression and verification pipeline:

Tool	Function
Sharp	Converts large images → JPEG/WebP, optimizes size.
MozJPEG	Compresses JPGs to high-quality progressive output.
pngquant	Reduces color depth for transparent PNGs.
cwebp	Generates modern WebP versions for supported browsers.
ImageMagick	Validates resolution, DPI, and metadata.
SHA-256 Checksums	Generated for reproducibility and cache integrity.


⸻

♿ Accessibility Standards
	•	Every image used in the UI must include descriptive alt text.
	•	Decorative images should use empty alt="" or role="presentation".
	•	Avoid text baked into images — use HTML/CSS for accessibility and localization.
	•	Ensure minimum contrast ratio of 4.5:1 between overlays and background images.
	•	All content imagery follows WCAG 2.1 AA compliance.

⸻

🧾 Provenance & Licensing

Asset	Source	License	Notes
placeholder.jpg	Generated in-house	MIT	Generic placeholder
prairie-sunrise.jpg	Unsplash (Public Domain)	CC0	Landscape background
kansas-river-aerial.webp	USGS Public Archive	Public Domain	Hydrology section
topo-overlay.png	USGS 1894 Topo Series	Public Domain	Map overlay
timeline-bg.jpg	Custom KFM Design	MIT	Gradient background

Each asset includes a corresponding metadata .json file in the meta/ folder when attribution or license tracking is required.

Example:

{
  "id": "prairie-sunrise",
  "source": "Unsplash / John Doe",
  "license": "CC0",
  "tags": ["kansas", "sunrise", "prairie"],
  "checksum": "sha256:e4b9f1..."
}


⸻

🧩 Usage in Components

Component	Image	Purpose
Header	header-bg.jpg	Hero banner background
MapView	topo-overlay.png	Historical map layer overlay
TimelineView	timeline-bg.jpg	Thematic gradient backdrop
DetailPanel	placeholder.jpg	Fallback when no image provided
Docs / About Page	prairie-sunrise.jpg	Scenic background illustration


⸻

🧪 Validation & Integrity

CI runs validation checks for:
	•	File existence and naming consistency.
	•	Minimum/maximum resolution limits.
	•	File format compliance (no EXIF, embedded profiles).
	•	SHA256 integrity validation.
	•	JSON metadata schema conformance.

Each release build attaches image checksums to the deployment manifest for version tracking.

⸻

🔗 Related Documentation
	•	Public Assets Overview
	•	Public Icons
	•	Design Mockups
	•	Accessibility Review

⸻

📜 License

All custom images are released under the MIT License,
with third-party photos used under CC0 or Public Domain licenses.

© 2025 Kansas Frontier Matrix — Produced under the Master Coder Protocol (MCP)
for verifiable provenance, accessibility, and long-term archival value.

“Every image is a window into Kansas — the frontier’s light, land, and legacy rendered in pixels.”

