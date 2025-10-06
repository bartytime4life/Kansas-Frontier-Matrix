<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Icons  
`docs/design/mockups/map/icons/`

**Symbolic · Consistent · Accessible Design Language**

</div>

---

## 🧭 Overview

The **Map Icons** directory defines the **visual symbol system** used across the  
Kansas Frontier Matrix (KFM) web interface — specifically for **MapLibre GL**, **timeline overlays**,  
and AI-generated “site dossier” popups.  

These icons provide a unified visual vocabulary to represent entities such as **people, places, events,  
landmarks, and hazards**, following KFM’s visual consistency and accessibility standards (WCAG 2.1 AA).

Icons are designed for use in both the **interactive web map** and **printed/static map exports**  
(e.g., KML/KMZ for Google Earth). Each icon aligns with KFM’s metadata-driven approach, ensuring  
semantic meaning, thematic color consistency, and clear readability at multiple zoom levels.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/icons/
├── README.md                        # This spec (GitHub-safe)
├── svg/                             # Vector icons (primary source)
│   ├── event.svg
│   ├── person.svg
│   ├── fort.svg
│   ├── treaty.svg
│   ├── hazard.svg
│   └── ... (others)
├── png/                             # Raster exports (fallback, 1x/2x)
│   ├── event_1x.png
│   ├── event_2x.png
│   ├── fort_1x.png
│   └── ...
└── palette.json                     # Thematic color and size definitions

Naming Convention:
{category}-{name}.svg or {category}_{zoomlevel}.png
Example → event-battle.svg or hazard_tornado_2x.png

⸻

🧱 Icon Categories

Category	Description	Example Uses	Symbol Style
Event	Represents historical or temporal events.	Battles, treaties, floods.	Circular symbol with temporal mark.
Place	Static geographic features.	Forts, rivers, towns.	Square or landmark-based outline.
Person	Historical figures or related entities.	Leaders, explorers, tribal representatives.	Silhouette or bust shape.
Document	Linked archival materials.	Treaties, deeds, letters.	Folded-paper or scroll icon.
Hazard	Natural or environmental events.	Flood, tornado, drought.	Triangular warning motif.
Culture	Archaeological or cultural features.	Sites, oral traditions.	Stylized motif or pottery fragment shape.
Infrastructure	Built environment.	Railroads, trails, routes.	Line-marker composite.

Visual Semantics:
Each icon encodes type and interaction — event icons often pulse or highlight on timeline scrub,
while place icons anchor geographic context.

⸻

🎨 Design Standards

Attribute	Requirement	Notes
Format	SVG (base), PNG (fallback)	SVG preferred for MapLibre and scale fidelity
Canvas Size	24×24 px (core), scalable up to 48×48 px	Consistent across categories
Stroke Width	1.5–2 px	Harmonizes at various map zoom levels
Palette	Defined in palette.json	Color-coded by theme (terrain, time, type)
Contrast Ratio	WCAG 2.1 AA	All icons must pass color contrast validation
Color Mode	Dual — Light/Dark theme compatible	Icons automatically adjust via CSS filter or MapLibre style layer
License	CC-BY 4.0	All icons free for reuse with attribution


⸻

🎨 Thematic Palette (excerpt from palette.json)

{
  "themes": {
    "base": {
      "fill": "#444444",
      "stroke": "#222222"
    },
    "highlight": {
      "fill": "#ffcc00",
      "stroke": "#d19a00"
    },
    "event": {
      "fill": "#ff6f61",
      "stroke": "#cc5244"
    },
    "hazard": {
      "fill": "#e03c31",
      "stroke": "#8c1d18"
    },
    "place": {
      "fill": "#4f8ac9",
      "stroke": "#2b5e91"
    },
    "treaty": {
      "fill": "#a67c52",
      "stroke": "#704c24"
    }
  },
  "sizes": {
    "small": 16,
    "medium": 24,
    "large": 32
  }
}


⸻

🧮 Integration Workflow

1. Design or Import Icons
	•	Create in Figma, Excalidraw, or Illustrator, export to SVG.
	•	Flatten groups and remove metadata to reduce file size.
	•	Keep path count minimal (≤10 paths per icon).

2. Optimize

Use SVGO or similar:

npx svgo svg/event-battle.svg --config=svgo.config.js --output=svg/event-battle.min.svg

3. Convert for Web Use

Generate PNG fallbacks (1×, 2×):

magick svg/event-battle.svg -resize 48x48 png/event-battle_2x.png

4. Reference in MapLibre Config

Link icon URLs in the layers.json (STAC-derived) config:

{
  "id": "treaty-sites",
  "type": "symbol",
  "source": "treaty-data",
  "layout": {
    "icon-image": "treaty",
    "icon-size": 1.0,
    "icon-allow-overlap": true
  },
  "paint": {
    "icon-color": "#a67c52"
  }
}

5. Document Updates

Every new icon must be documented here and referenced in the component README
(e.g., /docs/design/mockups/figma/components/navigation/README.md).

⸻

🧩 Accessibility & Semantic Guidance
	•	All icons include a <title> tag and descriptive aria-label in the SVG markup.
	•	Avoid relying on color alone to convey meaning — shape and contrast should remain distinctive.
	•	Tooltip or legend descriptions are dynamically fetched from the STAC metadata (via layers.json).
	•	In timeline or search results, icons must match their entity type in the Neo4j knowledge graph.

Example SVG snippet:

<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Fort">
  <title>Fort</title>
  <path d="M3 12 L9 4 L15 4 L21 12 L21 20 L3 20 Z" fill="#4f8ac9" stroke="#2b5e91" stroke-width="2"/>
</svg>


⸻

⚖️ License

All icons, SVGs, and related metadata are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required when reused or modified; commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-10	Initial version — added structure, palette, and icon workflow
2025-10-11	Enhanced accessibility and MapLibre integration examples