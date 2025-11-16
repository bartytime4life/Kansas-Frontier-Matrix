---
title: "🗺️ MapLibre GL — Rendering Performance Playbook (Offline MBTiles/PMTiles)"
path: "docs/guides/perf/maplibre-rendering-playbook.md"
version: "v10.0.1"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-render-perf-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Performance Guide"
intent: "rendering-optimization"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
semantic_document_id: "kfm-doc-rendering-playbook"
accessibility_compliance: "WCAG 2.1 AA"
machine_extractable: true
---

<div align="center">

# 🗺️ **MapLibre GL — Rendering Performance Playbook**  
`docs/guides/perf/maplibre-rendering-playbook.md`

**Purpose:**  
Optimized handbook for **offline-first MapLibre GL** deployments in KFM — targeting MBTiles/PMTiles rendering, tile cache control, frame-time profiling, and performance tuning for high-density vector/raster maps across Web & Electron.

</div>

---

# 🗂️ Directory Layout

```text
docs/
└── guides/
    └── perf/
        ├── maplibre-rendering-playbook.md   # This guide
        ├── profiles/                        # Chrome/Edge perf traces
        ├── styles/                          # Before/after style JSONs
        └── snippets/                        # micro-bench + TS utilities
````

---

# 📘 Overview

This guide provides **actionable patterns** to reach **60 FPS rendering** with large offline MBTiles/PMTiles datasets.

It includes:

* Rendering cost model
* Tile cache strategies
* PMTiles protocol setup
* Layer + label optimization
* Profiling workflows
* FAIR+CARE-aligned performance governance
* Benchmark automation

---

# 🔎 Rendering Cost Model

| Stage            | Description              | Typical Mitigation            |
| ---------------- | ------------------------ | ----------------------------- |
| **Tile I/O**     | Reading + decoding tiles | PMTiles, larger caches        |
| **Layout**       | Label placement, shaping | Simplify fonts, cached glyphs |
| **Paint**        | Fill/stroke compositing  | Merge layers, reduce overdraw |
| **Geometry**     | Vertex + feature count   | Upstream generalization       |
| **Overdraw**     | Hidden fill/stacking     | Reorder layers                |
| **Style Thrash** | Frequent transitions     | Replace with stepped values   |

---

# ⏱️ Profiling Workflow (10-Minute Loop)

## 1. **Enable Developer HUD Overlays**

```js
const map = new maplibregl.Map({...});
map.showTileBoundaries = true;
map.showCollisionBoxes = true;
```

## 2. **Profile in DevTools**

* Open Chrome/Edge **Performance** panel
* Record 10–20 seconds of panning & zooming
* Save trace to:

```
docs/guides/perf/profiles/maplibre/<scene>-trace.json
```

## 3. **Layer Isolation**

* Hide half of layers → test
* Binary search to find expensive layers
* Document findings in perf logs

## 4. **Zoom Sweep**

* Test z = **6, 10, 12, 14, 16**
* Note CPU/GPU spikes per zoom level

## 5. **Targets**

* **p90 ≤ 16 ms**, **p99 ≤ 24 ms**
* Strong frame-time stability across pans & zooms

---

# 🔒 Tile Cache & Source Tuning

### Vector Tiles (PMTiles/MBTiles)

```ts
import maplibregl from "maplibre-gl";
import { Protocol } from "pmtiles";

const protocol = new Protocol();
maplibregl.addProtocol("pmtiles", protocol.tile);

const map = new maplibregl.Map({ container: "map", style });

map.addSource("roads", {
  type: "vector",
  url: "pmtiles://file:///data/tiles/roads.pmtiles",
  minzoom: 0,
  maxzoom: 14
});

map.setMaxTileCacheSize(1024);
```

### Guidelines

* PMTiles > MBTiles for large offline sources
* Match `maxzoom` to feature fidelity
* Compress tilesets aggressively
* Avoid unnecessary low-zoom densities

---

### Raster DEM / Orthos

```js
map.addSource("dem", {
  type: "raster-dem",
  url: "pmtiles://file:///data/dem.pmtiles",
  tileSize: 512
});
map.addLayer({
  id: "hillshade",
  type: "hillshade",
  source: "dem"
});
```

* Prefer **512 px** tiles for fewer fetches
* Pre-generate overviews
* Use GPU-light hillshade parameters

---

# 🧱 Layer Simplification Tactics

### Guidelines

1. Generalize upstream (`tippecanoe`, `mapshaper`)
2. Merge similar layers using filters
3. Limit `minzoom` / `maxzoom`
4. Avoid:

   * `dasharray`
   * Pattern fills
   * Thick halos
   * Continuous zoom-based transitions

---

### One-Line Wins

* Add `minzoom` to heavy layers
* Remove hidden fills
* Flatten style ordering
* Disable unused symbol layers
* Replace translucent polygons with solids

---

# 🔤 Label Optimization

### Guidelines

* Limit font families (1–2 only)
* Disable `text-allow-overlap` when possible
* Use `symbol-sort-key` for priority
* Cache glyph ranges

### Example

```json
{
  "id": "road-labels",
  "type": "symbol",
  "source": "roads",
  "layout": {
    "text-field": ["get", "name"],
    "text-size": ["interpolate", ["linear"], ["zoom"], 10, 10, 16, 14]
  },
  "paint": {
    "text-color": "#333",
    "text-halo-color": "#fff",
    "text-halo-width": 0.5
  }
}
```

---

# ⚙️ Map Settings & Rendering Flags

### Recommended Initializer

```js
const map = new maplibregl.Map({
  container: "map",
  style,
  antialias: false,
  fadeDuration: 100,
  maxTileCacheSize: 1024
});
map.setPrefersReducedMotion(true);
```

| Option              | Impact           |
| ------------------- | ---------------- |
| `antialias: false`  | ↓ GPU load       |
| `fadeDuration: 100` | ↓ blend ops      |
| `maxTileCacheSize`  | smoother panning |

---

# 🧪 Automated Benchmark Snippet

```ts
export async function runBenchmark(map) {
  const t = [];
  let rAF;
  function loop(ts) {
    t.push(performance.now() - ts);
    rAF = requestAnimationFrame(loop);
  }
  rAF = requestAnimationFrame(loop);
  await map.easeTo({ center: [-98, 38.5], zoom: 12, duration: 2000 });
  cancelAnimationFrame(rAF);
  t.sort((a, b) => a - b);
  const p = q => t[Math.floor(t.length * q)];
  return { p50: p(.5), p90: p(.9), p99: p(.99) };
}
```

---

# 🧮 Tile Build Recommendations

### Tippecanoe Flags

| Flag                       | Description            |
| -------------------------- | ---------------------- |
| `--drop-densest-as-needed` | Reduces vertices       |
| `--maximum-tile-bytes`     | Tile size cap          |
| `--coalesce`               | Merge related polygons |
| `--detect-shared-borders`  | Reduce boundaries      |

---

# 🛠️ Troubleshooting Matrix

| Symptom        | Likely Cause          | Fix                         |
| -------------- | --------------------- | --------------------------- |
| Stutter on pan | Cache too small       | Increase cache              |
| Label lag      | Halos too large       | Shrink halo / allow collide |
| GPU spikes     | Extrusions / overdraw | Disable 3D, reorder layers  |
| Memory creep   | Re-adding sources     | Remove before re-add        |

---

# ♿ Accessibility & FAIR+CARE Requirements

* Respect **reduced-motion** settings
* Ensure WCAG AA text contrast
* Include provenance for tileset simplification
* Ensure masking of restricted cultural features

---

# 🕰 Version History

| Version | Date       | Author        | Summary                                                            |
| ------: | ---------- | ------------- | ------------------------------------------------------------------ |
| v10.0.1 | 2025-11-09 | Core Team     | Restored `###` hierarchy (Option A), full KFM-MDP v10.4 compliance |
| v10.0.0 | 2025-11-09 | A. Barta      | Upgrade for KFM v10, full telemetry integration                    |
|  v1.0.0 | 2025-11-09 | KFM Assistant | Initial performance guide                                          |

---

<div align="center">

© 2025 Kansas Frontier Matrix
Master Coder Protocol v6.3 · FAIR+CARE Certified
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Performance Guides](../README.md)
[Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
