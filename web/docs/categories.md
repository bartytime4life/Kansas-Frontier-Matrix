<div align="center">

# 🗂 Kansas-Frontier-Matrix — Layer Categories (`web/docs/CATEGORIES.md`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Purpose

**Categories** define how layers are grouped in the sidebar and how they’re colored in legends and UI chips.  
They live in `config/categories.json` and are referenced by each layer’s `category` field.

---

## 📂 Example Schema (`config/categories.json`)

```json
{
  "categories": {
    "environment":    "#3A86FF",
    "culture":        "#FF595E",
    "infrastructure": "#8D99AE",
    "disaster":       "#D00000",
    "reference":      "#6C757D"
  }
}


⸻

🎨 Current Categories

Key	Color	Purpose
environment	🔵 #3A86FF	Land cover, hydrology, climate, soils, terrain
culture	🔴 #FF595E	Treaties, oral histories, archaeology, historic POIs
infrastructure	⚪ #8D99AE	Railroads, roads, towns, parcels, utilities
disaster	🟥 #D00000	Hazards, disasters, FEMA declarations, perimeters
reference	⚫ #6C757D	Basemaps, boundaries, grids, PLSS, topo maps


⸻

🧩 Usage
	1.	In your layer config, set a valid category:

{
  "id": "railroads_1900",
  "title": "Railroads (c. 1900)",
  "category": "infrastructure",
  "type": "geojson",
  "data": "./vectors/infrastructure/railroads_1900.geojson",
  "legendKey": "railroads"
}

	2.	Sidebar grouping and legend chips will automatically use the category color.
	3.	Adding a new category requires updating config/categories.json and ensuring any style tokens (if used) in style.css are aligned.

⸻

🌳 Category Taxonomy (Visual)

flowchart TD
  C["Categories"] --> E["environment\n#3A86FF"]
  C --> CU["culture\n#FF595E"]
  C --> I["infrastructure\n#8D99AE"]
  C --> D["disaster\n#D00000"]
  C --> R["reference\n#6C757D"]

  E --> E1["hydrology (rivers, wetlands)"]
  E --> E2["landcover (NLCD)"]
  E --> E3["terrain (DEM, hillshade)"]

  CU --> CU1["treaties & reservations"]
  CU --> CU2["archaeological sites"]
  CU --> CU3["oral histories / POIs"]

  I --> I1["railroads (c. 1900)"]
  I --> I2["roads & towns"]
  I --> I3["parcels / PLSS"]

  D --> D1["tornado tracks"]
  D --> D2["flood extents / declarations"]
  D --> D3["wildfire perimeters"]

  R --> R1["basemaps (topos, imagery)"]
  R --> R2["boundaries (counties)"]
  R --> R3["grids / indexes"]

Diagram shows Category → example layers with the legend color value per category.

⸻

✅ Validation
	•	Ensure every layer.category matches a key in config/categories.json.
	•	Quick check:

jq -e '.layers[] | .category' web/app.config.json

	•	CI will fail if unknown categories are present.

⸻


<div align="center">


Categories keep the Kansas-Frontier-Matrix UI organized, thematic, and accessible.
Use them consistently for clean grouping and reliable legend colors.

</div>
```
