<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Icons (PNG Library)  
`docs/design/mockups/map/icons/png/`

**Raster · Optimized · Cross-Platform Compatibility**

</div>

---

## 🧭 Overview

This directory contains the **PNG rasterized exports** of the Kansas Frontier Matrix (KFM)  
**map icon system** — optimized for environments or workflows that do not natively support SVGs.  

While **SVG icons** are the authoritative source (`/svg/`), these **PNG versions** ensure  
cross-platform compatibility in offline maps, printed atlases, KML/KMZ exports, and legacy viewers  
that rely on raster graphics.

Each PNG icon corresponds directly to an SVG in `/docs/design/mockups/map/icons/svg/`  
and maintains identical shape, color, and meaning according to the **KFM visual taxonomy**.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/icons/png/
├── README.md                      # This spec (GitHub-safe)
├── event-battle_1x.png             # Standard resolution
├── event-battle_2x.png             # Retina/high-DPI export
├── place-fort_1x.png               # Example static location
├── place-fort_2x.png
├── hazard-flood_1x.png
├── hazard-flood_2x.png
└── template-icon_1x.png            # Placeholder template

Naming Convention:
{category}-{name}_{scale}.png
Example → event-battle_2x.png, hazard-tornado_1x.png

⸻

🎯 Purpose

Goal	Description
🖼️ Raster Fallback	Used in contexts where SVGs aren’t supported (KML, static maps).
🧮 Performance	Pre-rendered at standard and retina resolutions for speed and clarity.
🧭 Consistency	Mirrors SVG counterparts with consistent color and geometry.
🪶 Accessibility	Ensures icons remain legible even at small raster sizes.
🧩 Integration	Referenced by the KFM build system for KML/KMZ and static exports.


⸻

🧱 PNG Export Workflow

1. Prepare the Source SVG

Start with the approved, optimized .svg icon from
docs/design/mockups/map/icons/svg/.

2. Export via ImageMagick or Figma

Generate PNGs at multiple scales (1×, 2×, optional 3× for ultra-high DPI):

# Using ImageMagick
magick svg/place-fort.svg -resize 24x24 png/place-fort_1x.png
magick svg/place-fort.svg -resize 48x48 png/place-fort_2x.png

3. Optimize PNGs

Run lossless compression using oxipng or pngquant:

oxipng -o 4 png/*.png

or

pngquant --force --ext .png --quality=80-95 png/*.png

4. Verify Visual Consistency

Compare with the SVG to confirm correct fill, stroke, and contrast.
Each raster export should retain the same color token from palette.json.

5. Commit with Provenance

Each new PNG export should be committed with a descriptive message linking to its SVG source:

git add png/place-fort_1x.png png/place-fort_2x.png
git commit -m "Added raster exports for place-fort icon (SVG → PNG conversion)"


⸻

🎨 Design Standards

Attribute	Requirement	Notes
Size (1x)	24×24 px	Matches base map unit scale
Size (2x)	48×48 px	Retina/HiDPI compatibility
Color Accuracy	Must match SVG color tokens	Verify against palette.json
Format	PNG-24	Use transparency where applicable
Compression	Lossless	Ensure no visible artifacts
Contrast Ratio	WCAG 2.1 AA	Maintain readability on both map themes
License	CC-BY 4.0	Attribution required when reused


⸻

🧮 Integration Example (KML Export)

When generating static KML or KMZ files, PNGs are embedded as raster markers:

<Style id="fort-icon">
  <IconStyle>
    <Icon>
      <href>icons/png/place-fort_2x.png</href>
    </Icon>
    <scale>0.8</scale>
  </IconStyle>
</Style>


⸻

🧩 Mapping to SVG Sources

Each PNG must include a metadata reference in its commit message or accompanying .json record.

Example metadata (place-fort_icon.json):

{
  "id": "place-fort",
  "source": "../svg/place-fort.svg",
  "exports": {
    "1x": "png/place-fort_1x.png",
    "2x": "png/place-fort_2x.png"
  },
  "created": "2025-10-11",
  "license": "CC-BY-4.0",
  "author": "Kansas Frontier Matrix Design Team"
}


⸻

🧠 Integration with MapLibre

In the KFM MapLibre configuration (layers.json), PNG fallbacks are automatically referenced
if vector sprites are unavailable:

{
  "id": "hazards",
  "type": "symbol",
  "layout": {
    "icon-image": "hazard-flood_2x",
    "icon-size": 0.6
  },
  "paint": {
    "icon-opacity": 1.0
  }
}

🧩 Tip:
PNGs are automatically preloaded in the build pipeline via the STAC catalog metadata
under data/stac/collections/icons/.

⸻

🔐 Provenance & Versioning

Asset Type	Source	Tracking	Notes
Vector Base	.svg	Git	Master icon version
PNG Exports	.png	Git	Derived from SVGs, optimized for raster use
Metadata	.json	Git	Links to export provenance
Palette	palette.json	Git	Centralized color reference


⸻

⚖️ License

All icons and derivatives are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required for reuse or modification.
Commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-11	Initial version — added workflow, naming, and KML integration
2025-10-12	Standardized per KFM Markdown style and MapLibre linkage guide
