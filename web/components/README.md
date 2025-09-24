# `web/components/` — Kansas-Frontier-Matrix UI Modules

This directory contains modular, framework-free JavaScript components that power the **Kansas-Frontier-Matrix** web viewer.  
Each module is standalone, lightweight, and designed to connect cleanly with the MapLibre map (`web/app.js`) and styling in [`web/css/map.css`](../css/map.css).

---

## 📂 Components

### [`legend.js`](./legend.js)
Dynamic map legend control.

- Reads layer definitions (e.g., from `config/layers.json`).
- Supports symbology blocks with `color` + `label`.
- Collapsible header, styled via `.kfm-legend` classes.
- Attachable with `map.addControl(new LegendControl({ layersConfig }), "bottom-right");`.

### [`popup.js`](./popup.js)
Popup builder + click handler utilities.

- Safe HTML (sanitized) from GeoJSON/Vector features.
- Flexible field mapping (`title`, `meta`, `date`, `desc`, `link`).
- Handles multiple overlapping features (dedup + list).
- Usage: `attachPopup(map, { layers: ["events", "places"] })`.

### [`sidebar.js`](./sidebar.js)
Sidebar container and helpers.

- Docked right panel (`.kfm-sidebar`) with header, time slot, and layer groups.
- Groups are collapsible (`<details>`).
- Helpers for adding layer rows with checkbox + opacity slider.
- Used by `app.js` to build the layer tree UI.

### [`timeline.js`](./timeline.js)
Interactive year slider / timeline control.

- Min/max/year range with step.
- Play/pause auto-advance with configurable FPS and looping.
- Emits `onChange(year)` callbacks to update the map.
- Dock mode (`.kfm-timeline-dock`) if mounted without a container.

---

## 🧩 Integration

All components are **vanilla JS classes** or utilities. They don’t require frameworks, only a DOM + MapLibre.

Example (inside `app.js`):

```js
import LegendControl from "./components/legend.js";
import { attachPopup } from "./components/popup.js";
import Sidebar from "./components/sidebar.js";
import Timeline from "./components/timeline.js";

// Sidebar
const sidebar = new Sidebar({ title: "Kansas-Frontier-Matrix" }).mount();

// Timeline
const tl = new Timeline({ min: 1800, max: 2025, value: 1900 }).mount(document.getElementById("timebox"));
tl.onChange((y) => KFM.setYear(y));

// Legend
map.addControl(new LegendControl({ layersConfig: cfg.layers }), "bottom-right");

// Popups
attachPopup(map, { layers: ["events", "places"] });
````

---

## 🎨 Styling

All UI components rely on CSS hooks defined in [`map.css`](../css/map.css):

* `.kfm-legend` — legend control
* `.kfm-popup-*` — popup title/meta/desc
* `.kfm-sidebar` — sidebar container
* `.kfm-timeline-dock` — floating dock for the timeline

Dark mode is supported automatically via `prefers-color-scheme`.

---

## 📜 Notes

* Keep components **small & decoupled**; no cross-imports.
* Document any new CSS hooks in `map.css`.
* If adding new components, provide:

  * **JS module** in this folder.
  * **CSS hooks** in `web/css/map.css`.
  * **Usage example** in this README.

```
