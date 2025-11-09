---
title: "🗺️ Kansas Frontier Matrix — MapLibre Rendering Performance Playbook (v10 Optimized)"
path: "docs/guides/geo/maplibre-rendering-playbook.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-render-perf-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapLibre Rendering Performance Playbook**  
`docs/guides/geo/maplibre-rendering-playbook.md`

**Purpose:**  
Optimize MapLibre GL for **offline-first**, **FAIR+CARE-compliant** map rendering in the Kansas Frontier Matrix (KFM).  
Provides practical recipes to reduce frame time (ms) and memory consumption for **MBTiles/PMTiles** raster and vector datasets in both **web** and **Electron** environments.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enabled-orange)](../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Stable_Build-brightgreen)](../../../releases/)
</div>

---

## 📘 Overview

This playbook targets **MapLibre GL v3+** rendering with **large PMTiles or MBTiles** sources.  
Small performance optimizations (2–4 ms/frame) compound to deliver a consistent **60 FPS** experience during timeline panning, spatial animation, and Focus Mode overlays.

It covers:
- **Profiling loops** to isolate performance hotspots  
- **Tile cache tuning & data source configuration**  
- **Layer/labelling optimization** for minimal overdraw  
- **Raster rendering best practices** for offline tile archives  

---

## 🗂️ Directory Layout

```plaintext
docs/guides/geo/
├── maplibre-rendering-playbook.md     # This guide
├── profiles/                          # Performance trace profiles (.json/.cpuprofile)
├── styles/                            # Before/after optimized style JSONs
└── snippets/                          # TS/JS benchmark and diagnostic scripts
```

---

## 🔎 Rendering Performance Factors

| Category | Description | Optimization Strategy |
|-----------|-------------|------------------------|
| **Tile I/O** | Fetching + decoding MBTiles/PMTiles | Range requests + increased cache size |
| **Layout** | Label placement, text shaping, collisions | Fewer fonts, pre-generated labels |
| **Paint** | Symbol, line, fill operations per layer | Merge identical paints; simplify filters |
| **Geometry** | Feature & vertex count | Generalize geometries upstream |
| **Overdraw** | Multiple fills on same area | Sort & merge layers; avoid transparency stacking |
| **Style Thrash** | Complex zoom expressions | Replace dynamic with stepped transitions |

---

## ⏱️ 10-Minute Profiling Loop

1. **Enable Map Debug UI**
   ```js
   const map = new maplibregl.Map({...});
   map.showTileBoundaries = true;
   map.showCollisionBoxes = true;
   map.showPadding = false;
   ```
2. **Record CPU Profile (Chrome/Edge)**
   - DevTools → Performance → Record during zoom/pan  
   - Save as `.json` under `docs/guides/geo/profiles/`
3. **Hide Layers by Halves**
   - Binary-search visible layers; identify top offenders
4. **Stress-test Labels**
   - Toggle `text-allow-overlap` and reduce `text-size`  
   - Identify collision or halo-heavy layers
5. **Goal Metrics**
   - **P90 ≤ 16 ms**, **P99 ≤ 24 ms** (60 FPS)

---

## 🧰 Tile Cache & Source Tuning

### Vector Tiles (PMTiles / MBTiles)

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

**Guidelines**
- Use **PMTiles** for single-file, range-read tilesets.  
- Limit `maxzoom` to dataset resolution (avoid ≥ z15).  
- Tune `maxTileCacheSize` (512–2048) per RAM availability.

### Raster Tiles (Hillshade / DEM)

```js
map.addSource("hillshade", {
  type: "raster-dem",
  url: "pmtiles://file:///data/dem.pmtiles",
  tileSize: 512
});
map.addLayer({ id: "hillshade", type: "hillshade", source: "hillshade" });
```

**Best Practices**
- `tileSize: 512` → fewer network reads  
- Prebuild COG pyramids for hillshades  
- Use lightweight compression (`LZW` or `DEFLATE`)

---

## 🧱 Layer Optimization

| Technique | Description | Example |
|------------|--------------|----------|
| **Generalize** | Reduce vertices using `tippecanoe --drop-densest-as-needed` | Lower file size & parse time |
| **Merge Layers** | Combine layers with same style/filter | Multiple road types → one layer |
| **Zoom Filtering** | `minzoom` / `maxzoom` for layer visibility | Parcels visible ≥ z13 |
| **Avoid Costly Paints** | Skip dasharrays, wide halos | Replace with sprites or simple fills |

---

## 🔤 Label Optimization

- Limit **fonts** and **glyph ranges**  
- Avoid `text-allow-overlap: true` unless critical  
- Use `symbol-sort-key` for ordered rendering  
- Cache label anchors in style JSON  

**Minimal Symbol Example**
```json
{
  "id": "roads-label",
  "type": "symbol",
  "source": "roads",
  "layout": {
    "text-field": ["get", "name"],
    "text-size": ["interpolate", ["linear"], ["zoom"], 10, 10, 16, 14],
    "text-anchor": "center"
  },
  "paint": {
    "text-color": "#333",
    "text-halo-color": "#fff",
    "text-halo-width": 0.5
  }
}
```

---

## ⚙️ Recommended Map Settings

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

| Setting | Effect | Recommendation |
|----------|--------|----------------|
| `antialias` | GPU smoothing | Disable for 2D |
| `fadeDuration` | Blend time | 50–150 ms |
| `maxTileCacheSize` | Cached tiles | 1024 for desktop, 512 for mobile |

---

## 🧮 Automated Benchmark Script

```ts
export async function runBenchmark(map) {
  const samples = [];
  let handle;
  function loop(ts){ samples.push(performance.now() - ts); handle = requestAnimationFrame(loop); }
  handle = requestAnimationFrame(loop);
  await map.easeTo({ center: [-98,38.5], zoom: 10, duration: 1500 });
  cancelAnimationFrame(handle);
  samples.sort((a,b)=>a-b);
  const p=q=>samples[Math.floor(samples.length*q)];
  return {p50:p(.5).toFixed(2), p90:p(.9).toFixed(2), p99:p(.99).toFixed(2)};
}
```

---

## 🧾 Optimization Checklist

| Issue | Likely Cause | Fix |
|-------|---------------|-----|
| Pan stutter | Cache too small or antialias on | Raise cache / disable AA |
| Label lag | Large halos or font set | Simplify style |
| GPU spikes | Layer overdraw | Merge / re-order |
| Memory leak | Unreleased sources | `map.removeSource()` before re-add |

---

## ♿ Accessibility & FAIR+CARE Notes

- Respect OS **reduced motion** preferences  
- Maintain **legible text contrast** and **DPI scaling**  
- Use **CARE-aligned map masks** for sacred / restricted sites  
- Document all style generalizations in provenance metadata  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Upgraded for KFM v10; standardized FAIR+CARE render telemetry |
| v9.7.0 | 2025-11-09 | A. Barta | Initial performance playbook for offline MapLibre rendering |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geo Guides](./README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

