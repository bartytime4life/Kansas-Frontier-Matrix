---
title: "🗺️ MapLibre GL — Rendering Performance Playbook (Offline MBTiles/PMTiles)"
path: "docs/guides/perf/maplibre-rendering-playbook.md"
version: "v10.0.0"
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
---

<div align="center">

# 🗺️ **MapLibre GL — Rendering Performance Playbook**  
`docs/guides/perf/maplibre-rendering-playbook.md`

**Purpose:**  
Optimized handbook for **offline-first MapLibre GL** deployments in KFM — targeting MBTiles/PMTiles rendering, tile cache control, frame-time profiling, and performance tuning for high-density vector/raster maps across web and Electron.  

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../..)
[![License](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards)
[![Status](https://img.shields.io/badge/Status-Stable_Build-brightgreen)](#)

</div>

---

## 📘 Overview

This guide provides actionable patterns to achieve **60 FPS rendering** with large **offline MBTiles/PMTiles** datasets.  
It details cost factors (I/O, layout, paint, geometry, overdraw), offers profiling workflows, and gives style/layer optimization recipes suitable for KFM’s high-resolution frontier datasets and 3D timeline overlays.

---

## 🗂️ Directory Layout (drop-in for KFM)

```plaintext
docs/
└── guides/
    └── perf/
        ├── maplibre-rendering-playbook.md   # This guide
        ├── profiles/                        # Performance profiles (.json/.cpuprofile)
        ├── styles/                          # Before/after style JSONs
        └── snippets/                        # TypeScript/JS benchmark utilities
```

---

## 🔎 Rendering Cost Model

| Stage | Description | Typical Mitigation |
|--------|--------------|--------------------|
| **Tile I/O** | Reading + decoding tiles (SQLite/HTTP range) | PMTiles protocol handler, cache warmup |
| **Layout** | Label placement, text shaping | Limit fonts, reuse glyphs, `text-size` scaling |
| **Paint** | Fill, stroke, opacity compositing | Merge similar layers, minimize overdraw |
| **Geometry** | Vertex + feature count | Simplify upstream, limit zoom range |
| **Overdraw** | Redundant pixel writes | Order layers, remove hidden fills |
| **Style Thrash** | Data-driven zoom transitions | Replace with static steps when possible |

---

## ⏱️ Profiling Workflow (10-Minute Loop)

1. **Enable HUD**
   ```js
   const map = new maplibregl.Map({...});
   map.showTileBoundaries = true;
   map.showCollisionBoxes = true;
   ```
2. **Record CPU Profile (Chrome/Edge)**
   * Open *DevTools → Performance* → record panning/zooming.
   * Save trace → `docs/guides/perf/profiles/<scene>.json`.
3. **Layer Isolation**
   * Binary-search visible layers; hide half → measure → repeat.
4. **Zoom Sweep**
   * Capture z = 6, 10, 12, 14, 16; note ms spikes.
5. **Set Performance Targets**
   * **P90 ≤ 16 ms**, **P99 ≤ 24 ms** (smooth 60 FPS).

---

## 🧰 Tile Cache & Source Tuning

### Vector (PMTiles/MBTiles)

```ts
import maplibregl from "maplibre-gl";
import { Protocol } from "pmtiles";

maplibregl.addProtocol("pmtiles", new Protocol().tile);
map.addSource("roads", {
  type: "vector",
  url: "pmtiles://file:///data/tiles/roads.pmtiles",
  minzoom: 0,
  maxzoom: 14
});
map.setMaxTileCacheSize(1024);
```

**Tips**
- **PMTiles** > MBTiles for range requests & web streaming.
- Match **`maxzoom`** to data fidelity.
- Trim low-value zooms (e.g., parcels ≥ z13).

### Raster DEM / Orthos

```js
map.addSource("dem", {
  type: "raster-dem",
  url: "pmtiles://file:///data/dem.pmtiles",
  tileSize: 512
});
map.addLayer({ id: "hillshade", type: "hillshade", source: "dem" });
```

*512 px tiles → fewer fetches; pre-generate overviews.*

---

## 🧱 Layer Simplification Tactics

1. **Generalize early** (`tippecanoe --drop-densest-as-needed`).
2. **Merge** layers with identical paint/layout via filters.
3. **Delay render** until meaningful zooms (`minzoom`/`maxzoom`).
4. **Avoid costly props:** `dasharray`, wide halos, patterned fills.

---

## 🔤 Label Optimization

* Limit `text-size`; prefer single font stack.  
* Disable `text-allow-overlap` unless vital.  
* Use `symbol-sort-key` for priority ordering.  
* Cache glyph ranges; reduce re-layout.

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

## ⚙️ Map Settings & Flags

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

| Option | Impact |
|--------|---------|
| `antialias: false` | ↓ GPU cost |
| `fadeDuration: 100` | ↓ blending overhead |
| `maxTileCacheSize` | trade RAM ↔ smoothness |

---

## 🧪 Automated Benchmark Snippet

```ts
export async function runBenchmark(map) {
  const t = [];
  let rAF;
  function loop(ts){t.push(performance.now()-ts);rAF=requestAnimationFrame(loop);}
  rAF=requestAnimationFrame(loop);
  await map.easeTo({center:[-98,38.5],zoom:12,duration:2000});
  cancelAnimationFrame(rAF);
  t.sort((a,b)=>a-b);
  const p=q=>t[Math.floor(t.length*q)];
  return {p50:p(.5),p90:p(.9),p99:p(.99)};
}
```

---

## 🧮 Tile Build Recommendations

| Tool | Flag | Effect |
|------|------|--------|
| `tippecanoe` | `--drop-densest-as-needed` | Fewer vertices |
| `--maximum-tile-bytes` | cap tile size |
| `--coalesce` | merge geometries |
| `--detect-shared-borders` | optimize boundaries |

---

## 🧩 “One-Line Wins”

- Add `minzoom` to hidden layers.  
- Remove deprecated style entries.  
- Replace translucent fills with solids.  
- Disable unused symbol layers.  

---

## 🛠️ Troubleshooting Matrix

| Symptom | Likely Cause | Fix |
|----------|--------------|-----|
| Stutter on pan | Cache small / antialias on | raise cache / disable AA |
| Label lag | heavy halos / overlap true | shrink halos / allow collide |
| GPU spikes | overdraw, extrusions | flatten order, disable 3D |
| Memory growth | orphaned sources | `removeSource` before re-add |

---

## ♿ Accessibility & FAIR+CARE Notes

* Honor OS **reduced motion** preferences.  
* Maintain **text legibility** across DPIs.  
* Record all tile provenance & simplification metadata in STAC items.  

---

## 🕰 Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-09 | A. Barta | Upgraded for KFM v10; aligns with FAIR+CARE + new telemetry schema. |
| v1.0.0 | 2025-11-09 | KFM Assistant | Initial release of MapLibre performance guide. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Docs Index](../..) · [Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
