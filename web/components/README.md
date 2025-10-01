<div align="center">

# `web/components/` — Kansas-Frontier-Matrix UI Modules  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Modular, framework-free JavaScript powering the **Kansas-Frontier-Matrix** MapLibre viewer.  
Each module is ES-module friendly, standalone, and plugs into `web/app.js` + styles in [`web/css/map.css`](../css/map.css).  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["UI Modules (timeline.js · legend.js · popup.js · sidebar.js)"] --> B["Import into app.js"]
  B --> C["Wire with MapLibre layers"]
  C --> D["Style via map.css"]
  D --> E["Deploy site + viewer"]

<!-- END OF MERMAID -->



⸻

📦 Components

⏳ timeline.js

Interactive year slider / timeline control.

Highlights
	•	Min/max/step with robust clamping
	•	Play/pause with drift-free RAF + FPS control
	•	Keyboard + wheel navigation
	•	A11y: aria-*, formatValueText for screen readers
	•	Emits callbacks and DOM events (change, play, pause)
	•	Optional tick marks (ticks, tickInterval)
	•	Public API: mount(), setValue(), setRange(), setOptions(), onChange(), getState(), destroy()

Usage

import Timeline from "./components/timeline.js";

const tl = new Timeline({
  min: 1800, max: 2025, value: 1900, step: 1,
  autoplay: false, fps: 12, loop: true, showTicks: true, tickInterval: 10
}).mount("#timebox");

tl.onChange((y) => KFM.setYear(y));
tl.addEventListener("change", e => console.log("Year:", e.detail.value));


⸻

🗂️ legend.js

Dynamic legend control that infers symbology from map layers or explicit config.

Highlights
	•	Groups by category/group
	•	Auto-derives swatches (line/fill/circle/raster)
	•	Year badge via setYear(y)
	•	Public API: refresh(), setLayersConfig(), setYear(), getContainer(), destroy()

Usage

import LegendControl from "./components/legend.js";
const legend = new LegendControl({ layersConfig: cfg.layers, title: "Legend" });
map.addControl(legend, legend.getDefaultPosition?.() || "bottom-right");
legend.setYear(1936);

Explicit legend example

{
  "id": "ks_landcover",
  "title": "Land Cover",
  "legend": [
    { "color": "#1b9e77", "label": "Forest" },
    { "color": "#d95f02", "label": "Cropland" },
    { "color": "#7570b3", "label": "Urban" }
  ]
}


⸻

🗂️ legend-control.js

Minimal legend with year badge + builder API.

Highlights
	•	Collapsible header, persisted state
	•	Helpers: clear(), addSection(), addRow(), setTitle()
	•	Wire timeline → legend via wireTimelineToLegend()

Usage

import "./components/legend-control.js"; // exposes window.LegendControl

const legend = new window.LegendControl({ title: "Legend" });
map.addControl(legend);

const sec = legend.addSection("Trails");
legend.addRow(sec, { lineColor: "#4361EE", lineWidth: 3, label: "Historic Trail" });
window.wireTimelineToLegend(tl, legend);


⸻

📌 popup.js

Popup builder + multi-layer click handler.

Highlights
	•	Escape-safe HTML, flexible field mapping
	•	Dedupes overlapping results
	•	Cluster expansion for clustered sources
	•	Optional feature highlighting (setFeatureState)
	•	API: attachPopup(map, opts), attachLayerPopup(map, layerId, opts)

Usage

import { attachPopup } from "./components/popup.js";

attachPopup(map, {
  layers: ["events_point", "places_point"],
  maxFeatures: 10,
  clusterSourceId: "events_src",
  highlight: true
});


⸻

📑 sidebar.js

Sidebar container for map controls + layer toggles.

Highlights
	•	Header with title/subtitle + groups as <details>
	•	Row helpers with checkbox + opacity slider
	•	Emits events: rowtoggle, rowopacity, openchange
	•	API: addGroup(), addLayerRow(), setBadge(), setOpacity()

Usage

import Sidebar from "./components/sidebar.js";

const sidebar = new Sidebar({
  title: cfg.title || "Kansas-Frontier-Matrix",
  subtitle: cfg.subtitle || "Time-aware layers"
}).mount();

const group = sidebar.addGroup("Historical Maps");
group.addLayerRow({
  id: "usgs_topo_1894",
  title: "USGS Topo (1894)",
  badge: "[1894]",
  checked: true,
  opacity: 0.85,
  onToggle: (checked) => KFM.setVisible("usgs_topo_1894", checked),
  onOpacity: (v) => KFM.setOpacity("usgs_topo_1894", v)
});


⸻

🔌 Integration Pattern (web/app.js)

import Timeline from "./components/timeline.js";
import LegendControl from "./components/legend.js";
import { attachPopup } from "./components/popup.js";
import Sidebar from "./components/sidebar.js";

const sidebar = new Sidebar({ title: cfg.title }).mount();
const tl = new Timeline({ min: 1700, max: 2100, step: 1 }).mount("#timebox");
tl.onChange((y) => KFM.setYear(y));

const legend = new LegendControl({ layersConfig: cfg.layers });
map.addControl(legend);

attachPopup(map, { layers: visibleInteractiveLayerIds, maxFeatures: 12 });


⸻

🎨 Styling Hooks (web/css/map.css)
	•	.kfm-legend, .kfm-legend-row, .kfm-legend-swatch
	•	.kfm-popup-* (title, meta, desc, debug)
	•	.kfm-sidebar, .kfm-badge
	•	.kfm-timeline, .kfm-btn

Dark mode is automatic via prefers-color-scheme. Safe-area insets respected with CSS vars.

⸻

⚙️ Conventions & Tips
	•	Keep modules decoupled (no cross-imports).
	•	Expose callbacks + DOM events so app.js wires state.
	•	For per-feature time, use config (timeProperty, timeStartProperty).
	•	When adding a new component:
	1.	Add JS file to this folder
	2.	Add CSS hooks in web/css/map.css
	3.	Update usage examples here

⸻

🔍 Troubleshooting
	•	Legend empty? Check that map layer IDs match config.
	•	Popups not firing? Confirm opts.layers exist in MapLibre.
	•	Timeline not advancing? Check fps > 0, loop, and prefers-reduced-motion.

⸻

📝 License

These UI modules are MIT-licensed with the rest of the repository.
