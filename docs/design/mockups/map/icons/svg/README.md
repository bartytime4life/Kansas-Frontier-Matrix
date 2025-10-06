<div align="center">

# 🧭 Kansas Frontier Matrix — Map Icons (SVG Library)  
`docs/design/mockups/map/icons/svg/`

**Vector · Scalable · Accessible · Consistent**

</div>

---

## 🧭 Overview

This directory contains the **source SVG icons** used across the  
Kansas Frontier Matrix (KFM) **interactive map**, **timeline overlays**, and **UI components**.  

These SVGs form the **core iconography layer** of the project — a unified set of scalable, semantic, and  
accessible symbols representing **events, places, people, documents, hazards, and cultural sites**.  
They are optimized for use in both **MapLibre GL** and **React** components throughout the system.

Every SVG in this folder adheres to KFM’s design, accessibility, and reproducibility standards  
under the **Master Coder Protocol (MCP)** framework.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/icons/svg/
├── README.md                      # This spec (GitHub-safe)
├── event-battle.svg                # Example icon (Event)
├── place-fort.svg                  # Example icon (Place)
├── person.svg                      # Example icon (Person)
├── document-treaty.svg             # Example icon (Document)
├── hazard-flood.svg                # Example icon (Hazard)
├── culture-site.svg                # Example icon (Cultural landmark)
└── template-icon.svg               # Base template for new icons

Naming Convention:
{category}-{name}.svg
Example → event-battle.svg, hazard-tornado.svg

⸻

🎨 Design Standards

Attribute	Standard	Notes
Canvas Size	24×24 px	Core visual consistency; scalable via CSS or MapLibre
Stroke Width	1.5–2 px	Maintains clarity at all zoom levels
Colors	Palette-controlled (see palette.json)	Consistent hue per entity type
Contrast Ratio	WCAG 2.1 AA or higher	Ensures accessibility on all backgrounds
Export Format	SVG Tiny 1.2	No embedded raster data
Theme Compatibility	Dual (Light/Dark)	Adaptive color tokens via CSS or MapLibre styles

All icons must pass validation for minimal path count, accessible markup, and visual harmony.

⸻

🧩 Icon Categories

Category	Description	Example Icons
Event	Represents historical or temporal events	event-battle.svg, event-flood.svg
Place	Static locations (forts, towns, landmarks)	place-fort.svg, place-town.svg
Person	Historical figures and actors	person.svg
Document	Textual or legal artifacts	document-treaty.svg, document-deed.svg
Hazard	Environmental or natural events	hazard-flood.svg, hazard-tornado.svg
Culture	Archaeological or cultural elements	culture-site.svg, culture-artifact.svg

Guideline: Each icon must map directly to a semantic entity in the KFM knowledge graph (Place, Event, Person, etc.).

⸻

🧱 Workflow for Creating New SVG Icons

1. Design

Create the icon using Figma, Excalidraw, or Illustrator.
Keep paths simple, maintain a 24×24 px canvas, and use consistent stroke weights.

2. Optimize

Clean and minimize the SVG file to remove unnecessary metadata or transforms:

npx svgo place-fort.svg --config=../../svgo.config.js --output=place-fort.min.svg

⚙️ SVGO Config:
Use the shared KFM configuration file at tools/config/svgo.config.js.

3. Validate

Confirm the SVG structure passes validation:
	•	<svg> tag includes xmlns and viewBox="0 0 24 24".
	•	Includes <title> and <desc> for accessibility.
	•	No inline styling; use fill, stroke, stroke-width attributes.

4. Preview

Preview the icon on both light and dark backgrounds using your IDE or browser.

5. Commit

Once validated, commit with clear provenance:

git add place-fort.svg
git commit -m "Added new map icon: place-fort.svg (Forts category, WCAG verified)"


⸻

🧾 SVG Template

Use this as the base structure for new icons:

<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  width="24"
  height="24"
  role="img"
  aria-label="Fort"
>
  <title>Fort</title>
  <desc>Icon representing a historical fort location.</desc>
  <path
    d="M3 12 L9 4 L15 4 L21 12 L21 20 L3 20 Z"
    fill="#4f8ac9"
    stroke="#2b5e91"
    stroke-width="1.5"
  />
</svg>


⸻

🧮 Accessibility Guidelines
	•	Include <title> and <desc> for all SVGs (screen reader compatibility).
	•	Use descriptive aria-label matching the content type.
	•	Avoid reliance on color alone — ensure shape or outline communicates meaning.
	•	Test color contrast for dark/light backgrounds via tools such as Contrast Checker.

⸻

🧠 Integration with MapLibre

In the KFM map renderer (web/src/components/map/), icons are loaded dynamically via the
layers.json configuration file. Example:

{
  "id": "forts",
  "type": "symbol",
  "source": "forts-data",
  "layout": {
    "icon-image": "place-fort",
    "icon-size": 0.8
  },
  "paint": {
    "icon-color": "#4f8ac9"
  }
}

💡 Tip: SVGs are converted to MapLibre symbol sprites automatically during the build step.

⸻

🔐 Provenance & Versioning

Artifact	Tracking Method	Notes
SVG Source	Git	Version-controlled with commit metadata
Raster Exports	Generated from SVG	Stored in /png/ as fallback
Color Palette	palette.json	Centralized style definitions
Accessibility Checks	Manual/CI validation	Run before merges

Every SVG’s lineage (design → optimization → export) is documented in its commit message
and linked to its corresponding Figma node or Excalidraw reference when applicable.

⸻

⚖️ License

All icons and related metadata are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required for reuse or modification; commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-10	Initial version — directory setup, standards, and workflow
2025-10-11	Added accessibility, template SVG, and MapLibre integration