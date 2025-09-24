# Kansas-Frontier-Matrix — Web Style Guide

This style guide defines conventions for **CSS, JavaScript, JSON configs, and documentation** in the `web/` portion of the project.  
Following these rules ensures a **consistent, maintainable, and accessible** viewer.

---

## 1. CSS

### Layering
- **`layout.css`** → structural grid + components  
- **`theme.css`** → color palette, typography, shadows  
- **`theme-alt.css`** (optional) → experimental themes (e.g., sepia archival view)

### Naming
- Use **BEM-like prefixing** with `kfm-`:
  - `.kfm-sidebar`, `.kfm-layer__title`, `.kfm-timeline`
- Variants → suffix modifiers: `.is-open`, `.is-active`
- Utility classes → `.kfm-shadow`, `.kfm-accent`

### Variables
- Define **design tokens** at `:root`:  
  `--bg`, `--panel`, `--accent`, `--radius`, `--shadow-1`  
- Use tokens instead of hard-coded hex values.

### Responsiveness
- Breakpoints:  
  - `max-width: 1024px` → mobile/drawer sidebar  
- Use **CSS grid** for layout (not floats).

### Accessibility
- Always include **`:focus-visible`** states (`--focus` color).  
- Provide **reduced motion** fallbacks (`prefers-reduced-motion`).  
- Support **high contrast mode** (`forced-colors: active`).  

---

## 2. JavaScript (`app.js`)

### Structure
- Wrap in an **IIFE** (`(() => { ... })();`) to avoid globals.  
- Use **const** and **let**, never `var`.  
- Prefer small helpers:  
  ```js
  const $ = (sel, root=document) => root.querySelector(sel);
  const $$ = (sel, root=document) => [...root.querySelectorAll(sel)];
````

### Config-driven

* Load configs in order:
  `app.config.json → viewer.json → layers.json` → fallback.
* Avoid hardcoding — everything should be derived from config or STAC.

### UI

* Sidebar & timeline are **generated dynamically** from config/data.
* Use `dataset` attributes (e.g., `data-layer-id`) for binding.
* Keep DOM updates minimal (batch reflows when possible).

---

## 3. JSON Configs (`viewer.json`, `layers.json`)

### Formatting

* Indent with **2 spaces**.
* Use lowercase, hyphen-separated IDs:

  ```json
  { "id": "usgs-topo-1894" }
  ```
* Include **title, description, type, version** at minimum.

### Structure

* `start` and `end` → ISO8601 (`YYYY-MM-DD`).
* Use arrays for `urls`, `sources`, `path` (GeoJSON-like `[lon, lat]`).
* Include **provenance** (`sources`) wherever possible.

---

## 4. Documentation (Markdown)

### Layout

* Wrap at **80–100 characters** when reasonable.
* Use `##` headings for sections, `---` for dividers.
* Tables should use **GitHub-flavored Markdown** (GFM).

### Diagrams

* Use **Mermaid** diagrams.
* Quote labels and use `\n` for line breaks:

  ```mermaid
  flowchart TD
    A["Config:\nviewer.json"] --> B["App JS:\ninit()"]
  ```

---

## 5. Accessibility & UX

* Favor **high contrast** colors (`--ink` vs. `--bg`).
* Use **tabular numbers** for years/temporal sliders.
* Test in **light/dark**, **mobile/desktop**, and **print**.

---

## 6. Commit Guidelines

* Prefix commits with scope:

  * `css:`, `js:`, `data:`, `docs:`
* Example:

  ```
  css: add focus-visible outlines to sidebar toggles
  js: fix timeline filter for raster overlays
  data: add demo_entities.geojson for MapLibre
  docs: update STYLE_GUIDE.md with commit rules
  ```

---

✅ Following this style guide keeps the **Kansas-Frontier-Matrix web UI** clean, reproducible, and contributor-friendly.

```
