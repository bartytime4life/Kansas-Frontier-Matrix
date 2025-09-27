# Kansas-Frontier-Matrix — Web Documentation

This folder (`web/docs/`) contains **developer and contributor documentation**  
for the **Kansas-Frontier-Matrix web viewer**.

The goal is to keep **architecture, design, and extension guides** close to the codebase so the UI remains **consistent, reproducible, and contributor-friendly**.

---

## Files

- **`ARCHITECTURE.md`**  
  High-level overview of the web app:
  - Component flow (`app.config.json` → `index.html`/`app.js` → MapLibre → UI)
  - Data pipelines (JSON / GeoJSON layers, STAC item references)
  - Directory layout and extension patterns

- **`STYLE_GUIDE.md`**  
  Coding & design conventions:
  - CSS tokens, responsive layout, accessibility
  - JavaScript helpers & config-driven logic
  - JSON config schema-lite (`layers[]` contract, paint/legend/time rules)
  - Commit guidelines and CI validation tips

- **`DEVELOPER_GUIDE.md`** *(planned)*  
  Practical contributor reference:
  - How `app.js` loads configs and builds the sidebar dynamically
  - Timeline slider logic and year-based filtering
  - Adding new layer types (e.g., GeoJSON with paint styles, raster tiles)
  - Debugging and testing workflows

- **`UI_DESIGN.md`** *(planned)*  
  Visual/UI reference:
  - Sidebar & timeline placement
  - Responsive rules (desktop sidebar → mobile drawer)
  - CSS design tokens & theming (light/dark, archival/sepia mode)
  - Example wireframes and mockups

---

## Purpose

The **web viewer** provides:

- A **MapLibre-based map** with a **time slider** for filtering layers  
- Historical + terrain overlays (`./tiles/` and `./vectors/`)  
- Config-driven setup via [`app.config.json`](../app.config.json)  
- A bridge between **STAC metadata** and **interactive visualization**

Documentation here ensures future developers can:

- Add or extend layers cleanly  
- Maintain reproducibility across configs and UI  
- Connect new datasets without hardcoding  
- Keep accessibility and design consistent  

---

## Contribution Guidelines

- Keep docs **short and focused** per file.  
- Reference project files by **relative paths** (e.g., `../app.css`, `../index.html`).  
- Use **Mermaid diagrams** for flows, and validate syntax in GitHub preview.

```mermaid
flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer:\nindex.html / app.js"]
  B --> C["MapLibre:\nsources / layers"]
  C --> D["UI:\nsidebar + time slider"]
````

---

✅ Following this structure ensures the Kansas-Frontier-Matrix web UI remains maintainable, accessible, and ready for contributors.

```
