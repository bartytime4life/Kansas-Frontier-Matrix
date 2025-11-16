---
title: "🗺️ MapLibre GL — Rendering Performance Playbook (Offline MBTiles/PMTiles · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/perf/maplibre-rendering-playbook.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-render-perf-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Performance Guide"
intent: "maplibre-rendering-perf"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
sensitivity_level: "System-level performance"
machine_extractable: true
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-maplibre-rendering-playbook"
doc_uuid: "urn:kfm:doc:perf:maplibre-rendering-playbook-v10.4.2"
---

<div align="center">

# 🗺️ **MapLibre GL — Rendering Performance Playbook (Offline MBTiles/PMTiles)**  
`docs/guides/perf/maplibre-rendering-playbook.md`

**Purpose**  
Provide an optimized, FAIR+CARE-aware handbook for **offline-first MapLibre GL** deployments in KFM —  
focusing on **MBTiles/PMTiles rendering**, tile cache control, frame-time profiling, and performance tuning  
for high-density vector/raster maps in the web client and Electron apps.  

This playbook integrates with **Telemetry v2** and **FAIR+CARE v2** so that performance work remains  
**sustainable, transparent, and ethically governed**.

</div>

---

# 📘 Overview

This guide describes how to achieve and maintain:

- ~**60 FPS** rendering for heavy **offline MBTiles/PMTiles** scenes  
- Stable performance for **frontier-scale datasets** and **timeline overlays**  
- Reproducible **profiling results**, with Telemetry v2 metrics (energy, CO₂e, latency)  
- FAIR+CARE v2–aligned rendering that respects accessibility and sovereignty constraints  

It covers:

- Rendering cost model and hot spots  
- Profiling workflows and small scripts  
- Tile cache strategies and PMTiles specifics  
- Layer & style optimization tactics  
- Integration with KFM’s telemetry & governance workflows  

---

# 🗂️ Directory Layout

~~~text
docs/guides/perf/
│
├── telemetry-profiling.md             # Telemetry profiling & benchmark framework
├── maplibre-rendering-playbook.md     # ← THIS GUIDE
├── gdal-3.12-upgrade.md               # GDAL / geoprocessing performance patterns
└── reports/                           # Benchmark JSONs and perf telemetry logs
~~~

---

# 🔎 Rendering Cost Model

MapLibre rendering cost can be approximated as:

- **Tile I/O** — reading & decoding tile data (PMTiles/MBTiles/HTTP)  
- **Layout** — label placement, glyph shaping, collision checks  
- **Paint** — applying fills, strokes, halos, opacities, patterns  
- **Geometry** — vertex & feature counts per tile  
- **Overdraw** — redundant pixel writes from complex layers  
- **Style Thrash** — too many zoom-/data-driven transitions  

| Stage        | Description                              | Typical Mitigation                          |
|--------------|------------------------------------------|---------------------------------------------|
| **Tile I/O** | Reading+decoding tiles                   | PMTiles, cache warmup, fewer sources        |
| **Layout**   | Label placement & shaping                | Fewer fonts, reuse glyphs, simpler labels   |
| **Paint**    | Fills, strokes, opacity, haloes          | Merge layers, reduce alpha stacking         |
| **Geometry** | Vertex count & feature density           | Upstream simplification, filtered zooms     |
| **Overdraw** | Layers rendering atop each other         | Reorder layers, hide fully covered layers   |
| **Style Thrash** | Frequent dynamic style calculations | Favor stepped functions over continuous     |

---

# ⏱️ Profiling Workflow (10-Minute Loop)

1. **Enable MapLibre’s Internal Debug Helpers**

   ```js
   const map = new maplibregl.Map({...});
   map.showTileBoundaries = true;
   map.showCollisionBoxes = true;
````

2. **Profile in DevTools**

   * Open Chrome/Edge **Performance** panel
   * Record 10–20 seconds of panning & zooming
   * Save trace to:
     `docs/guides/perf/reports/maplibre/<scene>-trace.json`

3. **Layer Isolation**

   * Hide half of the layers → test
   * Binary search to find expensive layers
   * Document problem layers in perf reports

4. **Zoom Sweep**

   * Test z = 6, 10, 12, 14, 16
   * Note spikes in CPU/GPU per zoom level

5. **Targets**

   * **p90 frame time ≤ 16 ms**, **p99 ≤ 24 ms**
   * Strong frame-time stability across pans & zooms

---

# 🧰 Tile Cache & Source Tuning

## Vector Tiles (PMTiles/MBTiles)

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

**Guidelines**

* Prefer **PMTiles** for offline + range-based loading
* Match `maxzoom` to **actual data fidelity**
* Drop highly detailed layers at low zooms (e.g., parcels only at z≥13)
* Use a **sane `maxTileCacheSize`**; tradeoff RAM vs. smoothness

## Raster / DEM

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

* 512 px tiles reduce fetches
* Precompute overviews; do not rely on implicit resampling for performance-critical views

---

# 🧱 Layer Simplification Tactics

1. **Generalize upstream**

   * Use `tippecanoe` or similar to reduce vertices.

2. **Merge paint-equivalent layers**

   * Replace multiple similarly styled layers with one layer, using filters.

3. **Constrain zoom ranges**

   * `minzoom` and `maxzoom` to avoid showing dense layers at low zoom.

4. **Avoid heavy features**

   * Limit use of `line-dasharray`, wide halos, and patterned fills unless essential.

---

# 🔤 Label Optimization (High Impact)

* Limit font families (ideally one or two).
* Avoid `text-allow-overlap: true` unless absolutely required.
* Use simple `text-size` functions (e.g., 2-step zoom interpolation).
* Use `symbol-sort-key` to control important label priority.

```json
{
  "id": "road-labels",
  "type": "symbol",
  "source": "roads",
  "source-layer": "road_labels",
  "layout": {
    "text-field": ["get", "name"],
    "text-size": ["interpolate", ["linear"], ["zoom"], 10, 10, 16, 14],
    "text-padding": 2
  },
  "paint": {
    "text-color": "#333333",
    "text-halo-color": "#ffffff",
    "text-halo-width": 0.5
  }
}
```

---

# ⚙️ Map Settings & Runtime Flags

```js
const map = new maplibregl.Map({
  container: "map",
  style,
  antialias: false,
  fadeDuration: 100,
  maxTileCacheSize: 1024
});

// Respect OS reduced-motion setting
if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  map.setPrefersReducedMotion(true);
}
```

| Option              | Impact                                |
| ------------------- | ------------------------------------- |
| `antialias: false`  | lowers GPU load                       |
| `fadeDuration: 100` | reduces blending                      |
| `maxTileCacheSize`  | controls memory ↔ smoothness tradeoff |

---

# 🧪 Automated Benchmark Snippet

A small utility that uses `requestAnimationFrame` to capture frame times for a scripted camera move:

```ts
export async function runBenchmark(map: maplibregl.Map) {
  const samples: number[] = [];
  let id: number;

  function loop(prev: number) {
    const now = performance.now();
    samples.push(now - prev);
    id = requestAnimationFrame(() => loop(now));
  }

  id = requestAnimationFrame((ts) => loop(ts));

  await map.easeTo({
    center: [-98, 38.5],
    zoom: 12,
    duration: 2000
  });

  cancelAnimationFrame(id);
  samples.sort((a, b) => a - b);

  const p = (q: number) => samples[Math.floor(samples.length * q)] || 0;

  return {
    p50: p(0.5),
    p90: p(0.9),
    p99: p(0.99)
  };
}
```

Attach these metrics to Telemetry v2 for reproducible, run-to-run comparisons.

---

# 🧮 Tile Build Recommendations

| Tool         | Flag/Setting                 | Effect                      |
| ------------ | ---------------------------- | --------------------------- |
| `tippecanoe` | `--drop-densest-as-needed`   | Drops only densest features |
|              | `--maximum-tile-bytes=50000` | Caps tile size              |
|              | `--coalesce`                 | Merges adjacent geometries  |
|              | `--detect-shared-borders`    | Optimizes shared boundaries |

Keep performance configs under version control, e.g.:

* `docs/guides/perf/styles/`
* `docs/guides/perf/profiles/`

---

# 🧰 “One-Line Wins”

* Add `minzoom` to layers that are invisible at small scales.
* Remove unused or legacy layers from styles.
* Replace partially transparent fills with solid versions where possible.
* Disable debug layers in production builds.

---

# ♿ Accessibility, FAIR+CARE & Map Rendering

* Respect user preferences (`prefers-reduced-motion` and high contrast themes).
* Ensure label fonts + sizes remain legible across DPIs and zooms.
* When simplifying / hiding layers that involve sensitive cultural sites, coordinate with CARE v2 policies:

  * Some data must remain generalized/hidden even at high zooms.
* Origin & transformation metadata for tiles should be reflected in:

  * STAC Items for the tileset
  * Telemetry & lineage logs for the pipelines

---

# 🧩 Telemetry v2 + Benchmark Integration

Map rendering benchmarks should emit Telemetry v2 entries:

* `energy_wh` / `co2_g` for render test runs
* Benchmark FPS and frame-time percentiles (`p50`, `p90`, `p99`)
* Context: style version, tileset version, device/runtime profile

These feed into:

* `docs/guides/perf/reports/benchmark-results.json`
* `releases/<version>/pipeline-telemetry.json`

and are validated via:

* `telemetry-validate.yml`
* `faircare-validate.yml`
* `ledger-sync.yml`

---

# 🕰 Version History

| Version | Date       | Author     | Summary                                                                                 |
| ------: | ---------- | ---------- | --------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Core Team  | Upgraded to Telemetry v2 & FAIR+CARE v2; inset directory layout; ISO-aligned perf notes |
| v10.0.0 | 2025-11-09 | A. Barta   | Initial MapLibre perf playbook for KFM v10                                              |
|  v1.0.0 | 2025-11-09 | KFM Assist | Original base version of MapLibre performance tips                                      |

---

<div align="center">

**Kansas Frontier Matrix — MapLibre Rendering Performance Playbook (v10.4.2)**
High-Fidelity Maps × FAIR+CARE v2 × Sustainable Rendering × Telemetry v2

© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Performance Guides](./README.md) ·
[Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
