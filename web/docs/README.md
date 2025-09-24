# Kansas-Frontier-Matrix — Web Documentation

This folder (`web/docs/`) contains **developer and contributor documentation**  
for the Kansas-Frontier-Matrix **web viewer**.  

The goal is to keep **architecture, design, and extension guides** close to the code.

---

## Files

- **`ARCHITECTURE.md`**  
  High-level overview of the web app architecture:  
  - Component flow (config → app.js → MapLibre → UI)  
  - Data pipelines (JSON / GeoJSON entities, STAC items)  
  - Directory layout and extensibility notes  

- *(planned)* **`DEVELOPER_GUIDE.md`**  
  Deeper dive for contributors:  
  - How `app.js` loads configs and builds the sidebar  
  - Timeline control and time filtering  
  - How to add new layer types or UI panels  
  - Debugging and testing tips  

- *(planned)* **`UI_DESIGN.md`**  
  Reference for CSS layers (`layout.css`, `theme.css`) and design tokens:  
  - Grid and sidebar structure  
  - Timeline placement  
  - Responsive/mobile drawer rules  
  - Theming (light/dark, archival/sepia mode)

---

## Purpose

The **web viewer** provides:
- A **lightweight MapLibre map** with time slider
- Historical + terrain overlays
- Config-driven, reproducible setup
- A bridge between **STAC metadata** and interactive visualization

Documentation here ensures future developers can:
- Extend layers and themes
- Connect new datasets
- Maintain reproducibility

---

## Contribution Guidelines

- Keep docs **short and focused** per file.  
- Reference STAC, configs, and code by relative paths.  
- Use **Mermaid diagrams** where helpful, but always validate syntax in GitHub preview.  
- If adding new files, update this `README.md` with a short description.  

---

🚀 The `web/docs/` folder is the **knowledge base for the UI/UX layer** of the Kansas-Frontier-Matrix.

