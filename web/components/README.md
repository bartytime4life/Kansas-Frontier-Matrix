# `web/components/` — Kansas-Frontier-Matrix UI Modules

Modular, framework-free JavaScript that powers the **Kansas-Frontier-Matrix** MapLibre viewer.  
Each module is standalone, ES-module friendly, and designed to plug into `web/app.js` and styles in [`web/css/map.css`](../css/map.css).

---

## 📦 What’s here

### `timeline.js`
Interactive year slider / timeline control.

**Highlights**
- Min/max/step with robust clamping
- Play / pause with drift-free RAF and FPS control
- Keyboard (arrows, PageUp/Down, Home/End) + wheel with modifiers
- A11y labels (`aria-*`), optional `formatValueText` for screen readers
- Emits callbacks **and** DOM events (`change`, `play`, `pause`, `rangechange`)
- Optional tick marks (`showTicks`, `ticks`, `tickInterval`)
- Public API: `mount()`, `setValue()`, `setRange()/setBounds()`, `setOptions()`, `onChange()/offChange()`, `isPlaying()`, `setDisabled()`, `getState()`, `destroy()`

**Usage**
```js
import Timeline from "./components/timeline.js";

const tl = new Timeline({
  min: 1800, max: 2025, value: 1900, step: 1,
  autoplay: false, fps: 12, loop: true, showTicks: true, tickInterval: 10
}).mount("#timebox");

tl.onChange((y) => KFM.setYear(y));         // callback API
tl.addEventListener("change", e => {        // DOM event API (optional)
  console.log("Year:", e.detail.value);
});
````

---

### `legend.js`

**Dynamic** legend control that can infer symbology from live map layers and/or read explicit entries from config.

**Highlights**

* Groups by `category`/`group`
* Shows entries only for visible layers (and GeoJSON companions)
* Can auto-derive swatches for line/fill/circle/raster/hillshade/image
* Year badge via `setYear(y)`
* Public API: `refresh()`, `setLayersConfig(cfg)`, `setYear(y)`, `getContainer()`, `destroy()`

**Attach**

```js
import LegendControl from "./components/legend.js";
const legend = new LegendControl({ layersConfig: cfg.layers, title: "Legend" });
map.addControl(legend, legend.getDefaultPosition?.() || "bottom-right");
legend.setYear(1936);
```

**Explicit legend (in `config` layer entry)**

```json
{
  "id": "ks_landcover",
  "title": "Land Cover",
  "legend": [
    { "color": "#1b9e77", "label": "Forest" },
    { "color": "#d95f02", "label": "Cropland" },
    { "color": "#7570b3", "label": "Urban" }
  ]
}
```

---

### `legend-control.js`

**Minimal** legend control with a live Year badge and tiny builder API. Use this if you want a very small control and you’ll populate rows yourself.

**Highlights**

* Collapsible header with persisted state
* Optional year row (`showYear`)
* Helpers: `clear()`, `addSection(title)`, `addRow(section, item)`, `setBody(node)`, `setTitle()`, `setCollapsed()`
* Wire timeline → legend via `wireTimelineToLegend(timeline, legend)`

**Attach**

```js
import "./components/legend-control.js"; // IIFE exposes window.LegendControl + wireTimelineToLegend

const legend = new window.LegendControl({ title: "Legend", position: "bottom-right" });
map.addControl(legend, legend.getDefaultPosition());

// Optional: build rows
const sec = legend.addSection("Trails");
legend.addRow(sec, { lineColor: "#4361EE", lineWidth: 3, label: "Historic Trail" });

// Timeline sync
window.wireTimelineToLegend(tl, legend);
```

**When to use which legend**

* Use **`legend.js`** if you want automatic symbology from the map + grouping from config.
* Use **`legend-control.js`** for a minimal shell you’ll fill manually.

---

### `popup.js`

Popup builder + multi-layer click handler utilities.

**Highlights**

* Escape-safe HTML, flexible field mapping (`title/meta/date/desc/link`)
* Dedupes overlapping results; optional debug properties view
* Optional **cluster** expansion (for clustered GeoJSON sources)
* Optional **feature highlight** via `setFeatureState({selected:true})`
* Exposes `attachPopup(map, opts)` and `attachLayerPopup(map, layerId, opts)`

**Usage**

```js
import { attachPopup } from "./components/popup.js";

attachPopup(map, {
  layers: ["events_point", "places_point"],
  maxFeatures: 10,
  clusterSourceId: "events_src", // if the source uses clustering
  highlight: true                // style must read ["feature-state","selected"]
});
```

---

### `sidebar.js`

Sidebar container and utilities for a right-docked panel.

**Highlights**

* Header + `#timebox` + `#layerbox`
* Groups as `<details>` with persisted open/closed state
* Row helper with checkbox + opacity slider
* Emits events: `openchange`, `rowtoggle`, `rowopacity`
* Row API: `setChecked()`, `setOpacity()`, `setBadge()`, `setTitle()`, `focus()`

**Usage**

```js
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
```

---

## 🔌 Integration pattern (in `web/app.js`)

```js
import Timeline from "./components/timeline.js";
import LegendControl from "./components/legend.js";
import { attachPopup } from "./components/popup.js";
import Sidebar from "./components/sidebar.js";

// Sidebar skeleton
const sidebar = new Sidebar({ title: cfg.title, subtitle: cfg.subtitle }).mount();

// Timeline → year updates map + legend
const tl = new Timeline({
  min: toYear(cfg.time?.min) ?? 1700,
  max: toYear(cfg.time?.max) ?? 2100,
  value: initialYear, step: cfg.time?.step ?? 1,
  autoplay: !!cfg.time?.autoplay, fps: cfg.time?.fps ?? 8, loop: cfg.time?.loop !== false
}).mount("#timebox");
tl.onChange((y) => KFM.setYear(y));

// Legend
const legend = new LegendControl({ layersConfig: cfg.layers, title: cfg.legendTitle || "Legend" });
map.addControl(legend, legend.getDefaultPosition?.() || "bottom-right");

// Popups
attachPopup(map, { layers: visibleInteractiveLayerIds, maxFeatures: 12 });
```

---

## 🎨 Styling hooks (see [`map.css`](../css/map.css))

* `.kfm-legend`, `.kfm-legend-header`, `.kfm-legend-year`, `.kfm-year-badge`, `.kfm-legend-section`, `.kfm-legend-row`, `.kfm-legend-swatch`, `.kfm-legend-label`
* `.kfm-popup-*` (title, meta, desc, debug)
* `.kfm-sidebar` (container), `.kfm-badge` (small pill)
* `.kfm-timeline`, `.kfm-timeline-dock`, `.kfm-btn`

Dark mode is automatic via `prefers-color-scheme`. Safe-area insets are respected via CSS variables.

---

## ⚙️ Conventions & tips

* **No cross-imports** between components; keep them decoupled.
* Prefer **callbacks + DOM events** (both are exposed) so `app.js` can wire any state machine.
* For GeoJSON **per-feature time**, use layer config fields (`timeProperty`, `timeStartProperty`, `timeEndProperty`) and let `app.js` apply filters.
* If you add a new component, update:

  1. this folder with the JS file,
  2. CSS hooks in `web/css/map.css`,
  3. a usage example in this README.

---

## 🔍 Troubleshooting

* Legend shows nothing? Ensure the layer is added to the map and visible; for GeoJSON helpers, the legend checks `id`, `id_line`, `id_circle`.
* Popups not firing? Confirm `opts.layers` are actual **layer IDs** and that `queryRenderedFeatures` can see them at your zoom.
* Timeline not advancing? Check `fps > 0`, `loop` setting, and `prefers-reduced-motion` (autoplay is disabled for users who prefer reduced motion).

---

## 📝 License

These modules are MIT-licensed with the rest of the repository.

```
```
