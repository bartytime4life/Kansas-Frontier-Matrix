# Kansas-Frontier-Matrix — Web Documentation (`web/docs/`)

This folder contains **developer and contributor documentation** for the **Kansas-Frontier-Matrix web viewer**.  
Keep **architecture, design, and extension guides** close to the codebase so the UI stays **consistent, reproducible, and contributor-friendly**.

---

## Index of documents

| File                 | Status     | Purpose                                                                |
|----------------------|------------|------------------------------------------------------------------------|
| `ARCHITECTURE.md`    | ✅ current | High-level app flow, runtime data paths, and directory layout           |
| `STYLE_GUIDE.md`     | ✅ current | CSS tokens & theming, responsive rules, JS conventions, JSON config     |
| `DEVELOPER_GUIDE.md` | 🚧 planned | How `app.js` loads configs, timeline filtering, adding new layer types  |
| `UI_DESIGN.md`       | 🚧 planned | Sidebar/timeline patterns, theming, wireframes & states                 |
| `CONTRIBUTING.md`    | ✅ current | How to propose changes, run local checks, pass CI                       |
| `CHANGELOG.md`       | ✅ current | User-visible changes to the web app and docs                            |

> Keep docs **small and focused**. Cross-link with **relative paths** into `web/` (e.g., `../index.html`, `../styles/`).

---

## How these docs connect to the app

~~~mermaid
flowchart TD
  A["STAC & Sources\n(stac/items/**)"] --> B["Config Build\n(make site-config)"]
  B --> C["Viewer Config\n(web/config/app.config.json)"]
  C --> D["Runtime\n(web/index.html + app.js)"]
  D --> E["MapLibre\n(sources/layers)"]
  D --> F["UI\n(sidebar, legend, time slider)"]
~~~

---

- **Authoritative config** → `web/config/app.config.json` (generated) is first choice at runtime  
- **Fallbacks** → `web/config/viewer.json`, `web/config/layers.json`, `web/layers.json`  
- **Styles & tokens** → `web/styles/` (light/dark themes, z-index, focus rings)  
- **Docs** → this folder explains the above so contributors ship changes that **pass CI** and don’t break the viewer  

---

## Authoring standards

- Headings: start at `#` per file; no skipped levels  
- Code fences: must be closed; use language hints (`bash`, `json`, `js`, `html`, `mermaid`)  
- Paragraphs: keep concise; prefer lists/tables for structure  
- Links: use relative paths within the repo  
- Mermaid: validate in GitHub preview; quote labels with punctuation and use `\n` for line breaks  
- Examples: mirror actual keys used by the app (camelCase for style, ISO-8601 dates)  

---

## Quick pointers

- **Add a layer?** → Document in `DEVELOPER_GUIDE.md` with JSON example, update `STYLE_GUIDE.md` for tokens  
- **New UI pattern?** → Specify placement in `UI_DESIGN.md`, reference CSS tokens  
- **Architectural change?** → Update `ARCHITECTURE.md` and the Mermaid flow  
- **Breaking change?** → Note in `CHANGELOG.md` and reference commit/PR  

---

## Minimal contracts

### Viewer config (top-level excerpt)

```json
{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 12 },
  "layers": []
}

Layer snippet (raster)

{
  "id": "usgs_topo_1894_larned",
  "title": "USGS Historic Topo — Larned (1894)",
  "type": "raster",
  "url": "./tiles/historic/usgs_1894_larned/{z}/{x}/{y}.png",
  "visible": true,
  "opacity": 0.7,
  "category": "historical",
  "time": { "start": "1894-01-01", "end": "1894-12-31" }
}

Layer snippet (GeoJSON)

{
  "id": "ks_settlements",
  "title": "Settlements, Forts, Trading Posts",
  "type": "geojson",
  "data": "data/processed/towns_points.json",
  "category": "culture",
  "timeProperty": "year",
  "popup": ["name", "type", "year", "year_end"],
  "style": {
    "circleColor": "#FF595E",
    "circleRadius": 4,
    "circleOpacity": 0.95,
    "circleStrokeColor": "#FFFFFF",
    "circleStrokeWidth": 1
  }
}


⸻

Local preview & validation

# Serve the site (from repo root or ./web)
cd web && python -m http.server 8080

# Generate & validate configs from STAC
make stac stac-validate site-config

# Lint/validate JSON configs
jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
ajv validate -s web/config/layers.schema.json      -d web/config/layers.json


⸻

Contribution workflow
	1.	Branch from main, commit small, focused changes
	2.	Run local checks (Mermaid previews, JSON validity)
	3.	Open PR with summary and links (screenshots if visual)
	4.	Pass CI (schema validation, link checks)
	5.	Update CHANGELOG.md for user-visible changes

⸻

FAQ
	•	Design tokens? → STYLE_GUIDE.md with references to ../styles/base.css
	•	Timeline filtering logic? → DEVELOPER_GUIDE.md (runtime) + ARCHITECTURE.md (flow)
	•	Mockups? → UI_DESIGN.md with image assets under web/assets/

⸻

✅ This structure keeps the web UI maintainable, accessible, and easy to extend for new Kansas layers and stories.

---
