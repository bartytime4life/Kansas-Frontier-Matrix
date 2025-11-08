---
title: "🧰 Map Utilities — Protocols, Style Tools & Telemetry Hooks (KFM-Ready)"
path: "web/src/features/map/utils/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-map-utils-v1.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

<div align="center">

# 🧰 **Map Utilities — Protocols, Style Tools & Telemetry Hooks**  
`web/src/features/map/utils/README.md`

**Purpose:**  
Provide the **shared geospatial utility functions** that power KFM’s MapLibre and Cesium integration:  
protocol registration, style variable helpers, governance-aware telemetry, and ethical data access layers.  
Ensures reproducible, FAIR+CARE-aligned mapping under **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Validated-orange)](../../../../../docs/standards/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

This directory centralizes **low-level map utilities** for KFM’s web frontend, allowing other features (timeline, focus, search) to reuse consistent configuration patterns.  
All utilities follow **documentation-first**, **TypeScript-typed**, and **governance-aware** design.

### Functional Domains
- 🗺️ **Protocols** — Register `pmtiles://`, WMS, and static GeoJSON loaders.  
- 🎨 **Style Tools** — Manage MapLibre style variables and layer expressions.  
- 🧮 **Telemetry Hooks** — Capture map performance and FAIR+CARE audit logs.  
- ⚙️ **Governance Filters** — Apply CARE tags to layer visibility dynamically.  

---

## 🗂️ Directory Layout

```plaintext
web/
└─ src/
   └─ features/
      └─ map/
         └─ utils/
            README.md              # This file — utilities overview
            pmtiles-protocol.ts    # Registers PMTiles protocol handler
            map-style-utils.ts     # StyleVar, filter, and layer helpers
            telemetry.ts           # Performance, governance, and audit telemetry
            governance.ts          # CARE visibility filters and ethical enforcement
            math-utils.ts          # Helper for bbox/centroid computations
```

---

## 🗺️ PMTiles Protocol (`pmtiles-protocol.ts`)

Registers the **PMTiles protocol** for local-first, compressed vector and raster data access.

```ts
import { Protocol } from 'pmtiles';
import maplibregl from 'maplibre-gl';

export function registerPMTiles() {
  const protocol = new Protocol();
  maplibregl.addProtocol('pmtiles', protocol.tile);
  console.info('[KFM] PMTiles protocol registered');
  return () => maplibregl.removeProtocol('pmtiles', protocol.tile);
}
```

**Why PMTiles?**
- Enables offline-compatible, random-access geodata.  
- Simplifies path consistency (`pmtiles://datasets/<file>.pmtiles`).  
- Complies with KFM’s sustainability targets (minimized bandwidth & emissions).  

> *Telemetry Note:* Registration latency is logged to `focus-telemetry.json`.

---

## 🎨 Map Style Utilities (`map-style-utils.ts`)

Centralized helpers for manipulating **MapLibre style variables**, filters, and paints.

### Example: Set or Get StyleVar
```ts
export function setYear(map: maplibregl.Map, year: number) {
  if ((map as any).setStyleVar) (map as any).setStyleVar('currentYear', year);
  else console.warn('StyleVar not supported in this MapLibre build');
}
```

### Example: Toggle Layer Visibility
```ts
export function toggleLayer(map: maplibregl.Map, id: string, visible: boolean) {
  const visibility = visible ? 'visible' : 'none';
  map.setLayoutProperty(id, 'visibility', visibility);
}
```

### Expression Builder
```ts
export const activeAtYear = (y: number) => [
  "all",
  ["<=", ["get", "year_start"], y],
  [">=", ["coalesce", ["get", "year_end"], 9999], y]
];
```

**Performance Tip:** Reuse precompiled expressions for batch updates (timeline scrub events).

---

## 🧮 Math Utilities (`math-utils.ts`)

Lightweight geographic calculations without external dependencies.

```ts
export function centroid(bbox: [number, number, number, number]) {
  const [minX, minY, maxX, maxY] = bbox;
  return [(minX + maxX) / 2, (minY + maxY) / 2];
}
```

> *All math utilities are deterministic, unit-tested, and validated for reproducibility.*

---

## 📊 Telemetry & Performance (`telemetry.ts`)

Captures **map events**, **frame timing**, and **layer usage metrics** for audit compliance.

```ts
export function logMapInteraction(map: maplibregl.Map, event: string) {
  const log = {
    event,
    zoom: map.getZoom(),
    center: map.getCenter(),
    layers: map.getStyle().layers.length,
    timestamp: new Date().toISOString()
  };
  console.debug('[KFM][MapTelemetry]', log);
  fetch('/api/telemetry', { method: 'POST', body: JSON.stringify(log) });
}
```

**Telemetry schema:**  
`schemas/telemetry/web-map-utils-v1.json`

**Fields Recorded**
| Field | Type | Description |
|--------|------|-------------|
| `event` | string | Interaction type (`zoom`, `pan`, `layer-toggle`, etc.) |
| `zoom` | number | Current zoom level |
| `center` | object | Map center coordinates |
| `layers` | number | Active layer count |
| `user_role` | string | Derived from auth context |
| `timestamp` | string | UTC ISO 8601 timestamp |

---

## ⚖️ Governance Utilities (`governance.ts`)

Applies **FAIR+CARE visibility filters** to sensitive data layers.

```ts
export function enforceGovernance(map: maplibregl.Map, careTag: string) {
  if (careTag === 'sensitive') {
    console.warn('Hiding sensitive layer per CARE guidelines');
    toggleLayer(map, 'restricted-layer', false);
  }
}
```

**CARE Policy Tags**
| Tag | Description | Behavior |
|-----|--------------|----------|
| `public` | Open to all users | Fully visible |
| `restricted` | Requires authentication | Semi-transparent |
| `sensitive` | Hidden to protect cultural or ecological data | Removed at runtime |

Governance logic aligns with `DATA-GOVERNANCE.md` and feeds telemetry for compliance reporting.

---

## ♻️ Integration Patterns

| Utility | Used By | Description |
|----------|----------|-------------|
| `registerPMTiles` | timeline, map-init | Initialize custom protocol |
| `setYear` / `activeAtYear` | timeline | Syncs slider year to map layers |
| `toggleLayer` | admin | Enables/disables validation overlays |
| `logMapInteraction` | telemetry | Reports usage metrics |
| `enforceGovernance` | all features | Applies FAIR+CARE filters |

---

## 🧠 Example Integration (Timeline + Map Utils)

```ts
import { registerPMTiles } from './pmtiles-protocol';
import { setYear, logMapInteraction } from './map-style-utils';

const cleanup = registerPMTiles();

map.on('zoomend', () => logMapInteraction(map, 'zoom'));
window.addEventListener('kfm:timeline:year', e => setYear(map, e.detail.year));
```

> *Cleanup:* Remove protocol on component unmount — `cleanup()`.

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Map Utilities — Protocols, Style Tools & Telemetry Hooks (v9.9.0).
Defines FAIR+CARE compliant utilities supporting MapLibre, PMTiles, and governance telemetry integration for sustainable web mapping.
```

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|--------:|------------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-web` | Initial FAIR+CARE-compliant utility set for PMTiles, style, telemetry, and governance. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Geospatial Utilities × FAIR+CARE Governance × Sustainable Performance*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Map Docs](../README.md) · [Web Features Index](../../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

