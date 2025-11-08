---
title: "🕰️ Interactive Timeline Layers — MapLibre Playbook (KFM-Ready)"
path: "web/src/features/timeline/README.md"
version: "v9.7.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-timeline-v1.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

<div align="center">

# 🕰️ **Interactive Timeline Layers — MapLibre Playbook**  
`web/src/features/timeline/README.md`

**Purpose:**  
Let users **scrub through eras** and environmental shifts by binding a **time slider** to **MapLibre style layers**. Turn KFM datasets into **interactive narratives** of climate, land, water, species, ownership, and archaeology.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Aligned-orange)](../../../../docs/standards/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

- **What:** Time-linked style layers = layers whose **visibility/paint** depend on a **`currentYear`** state.  
- **Why:** Reveal **where people lived**, **waterways shifted**, **prairies converted**, **species moved**, **ownership changed**.  
- **How:** A single **UI slider** updates a **MapLibre style variable** or **layer filters**, which drive expressions across layers.

> *Tip:* Prefer **style variables** for O(1) updates across many layers. If not available in your MapLibre version, update layer **`filter`** and **paint** properties imperatively per layer (see fallback below).

---

## 🗂️ Directory Layout

```plaintext
web/
└─ src/
   └─ features/
      └─ timeline/
         README.md               # This file — MapLibre timeline playbook
         timeline.ts             # Timeline state, bindings, fallbacks, telemetry hooks
         slider.tsx              # React slider UI (keyboard/ARIA friendly)
         styles/
         ├─ timeline-style.json  # MapLibre style with expressions/filters
         └─ palette.json         # Optional era colors / design tokens
         datasets/
         ├─ landcover.pmtiles    # PMTiles (time-sliced or year-tagged)
         ├─ hydrology.pmtiles
         └─ settlements.pmtiles
```

---

## 🧩 Core Idea (MapLibre expressions)

Use a **global year** to control layer filters/paints:

- **Show features active at `Y`:**  
  `["all", ["<=", ["get","year_start"], ["var","currentYear"]], [">=", ["coalesce", ["get","year_end"], 9999], ["var","currentYear"]]]`
- **Fade by recency:**  
  `["interpolate", ["linear"], ["-", ["var","currentYear"], ["coalesce", ["get","year"], ["get","year_start"], 0]], 0, 1, 50, 0.2]`
- **Color by era bucket:**  
  `["step", ["var","currentYear"], "#d8d8d8", 1850, "#b3d1ff", 1900, "#7fb3ff", 1950, "#4d94ff", 2000, "#1a75ff"]`

> *Note:* `["var","currentYear"]` requires MapLibre with style variables enabled. For earlier versions, use fallback in **Binding API**.

---

## 🧾 Minimal Style Snippet (`styles/timeline-style.json`)

```json
{
  "version": 8,
  "glyphs": "https://demotiles.maplibre.org/font/{fontstack}/{range}.pbf",
  "metadata": { "vars": { "currentYear": 1900 } },
  "sources": {
    "settlements": { "type": "vector", "url": "pmtiles://datasets/settlements.pmtiles" }
  },
  "layers": [
    {
      "id": "settlements-dots",
      "type": "circle",
      "source": "settlements",
      "source-layer": "settlements",
      "filter": ["all",
        ["<=", ["get","year_start"], ["var","currentYear"]],
        [">=", ["coalesce", ["get","year_end"], 9999], ["var","currentYear"]]
      ],
      "paint": {
        "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, 1.2, 10, 3.5, 12, 6],
        "circle-color": ["step", ["var","currentYear"],
          "#c9c9c9", 1850, "#8fd3a1", 1900, "#5bbf8f", 1950, "#2b9f7a", 2000, "#0f7a5d"
        ],
        "circle-opacity": ["interpolate", ["linear"],
          ["-", ["var","currentYear"], ["coalesce", ["get","year"], ["get","year_start"], 0]],
          0, 1.0, 50, 0.25
        ]
      }
    }
  ]
}
```

---

## ⚙️ Binding API — **Style Var** & **Fallback**

### A) Style variable (preferred) — `timeline.ts`

```ts
import maplibregl from 'maplibre-gl';

export function initTimeline(map: maplibregl.Map, initialYear = 1900) {
  // Set once; used by expressions in style JSON
  if ((map as any).setStyleVar) (map as any).setStyleVar('currentYear', initialYear);

  // Telemetry hook (optional)
  performance.mark('timeline:init');

  return {
    setYear(y: number) {
      if ((map as any).setStyleVar) (map as any).setStyleVar('currentYear', y);
      else updateFiltersFallback(map, y);
      window.dispatchEvent(new CustomEvent('kfm:timeline:year', { detail: { year: y }}));
    },
    getYear(): number {
      if ((map as any).getStyleVar) return (map as any).getStyleVar('currentYear') as number;
      return (map as any).__currentYear ?? initialYear;
    }
  };
}

// Fallback for MapLibre versions without style variables
export function updateFiltersFallback(map: maplibregl.Map, year: number) {
  (map as any).__currentYear = year;
  const layers = ['settlements-dots', /* add your layer ids */];
  for (const id of layers) {
    const base = ["all",
      ["<=", ["get", "year_start"], year],
      [">=", ["coalesce", ["get", "year_end"], 9999], year]
    ];
    map.setFilter(id, base as any);
  }
}
```

### B) Simple UI (React slider) — `slider.tsx`

```tsx
import React from 'react';

export function YearSlider({ year, setYear }: { year: number; setYear: (y:number)=>void }) {
  return (
    <label style={{ display:'grid', gap:6 }}>
      <span id="label-year">Year: {year}</span>
      <input
        type="range"
        min={1700}
        max={2025}
        step={1}
        value={year}
        onChange={(e)=> setYear(parseInt(e.target.value, 10))}
        aria-labelledby="label-year"
      />
    </label>
  );
}
```

### C) Wiring it up (example usage)

```ts
import { initTimeline } from './timeline';
import { createRoot } from 'react-dom/client';
import { YearSlider } from './slider';

const map = new maplibregl.Map({ container: 'map', style: '/styles/timeline-style.json' });
map.on('load', () => {
  const tl = initTimeline(map, 1880);

  const root = createRoot(document.getElementById('timeline-ui')!);
  const App = () => {
    const [year, setYearState] = React.useState(tl.getYear());
    const setYear = (y:number) => { setYearState(y); tl.setYear(y); };
    return <YearSlider year={year} setYear={setYear} />;
  };
  root.render(<App />);
});
```

---

## 📦 PMTiles & Protocol Setup

Register **PMTiles protocol** once (on app boot) to use `pmtiles://` URLs:

```ts
import { Protocol } from 'pmtiles';
import maplibregl from 'maplibre-gl';

const protocol = new Protocol();
maplibregl.addProtocol('pmtiles', protocol.tile);

window.addEventListener('beforeunload', () => {
  maplibregl.removeProtocol('pmtiles', protocol.tile);
});
```

> *Note:* Group time-sliced tiles by year or store `year_start`/`year_end` feature properties. Indexing by year in your tiler will yield faster scrubs.

---

## 🧾 Era Buckets & Datasets (KFM examples)

| Layer               | Feature keys               | Era logic                                |
|---------------------|----------------------------|-------------------------------------------|
| `settlements`       | `year_start`, `year_end`   | show if `year_start ≤ Y ≤ year_end`       |
| `hydrology`         | `year`, `epoch`            | color by `epoch`; fade with recency       |
| `landcover`         | `year`, `class`            | filter class active at `Y`                 |
| `ownership_parcels` | `grant_year`, `sold`       | dim when `Y > sold`                       |
| `species_range`     | `range_year`               | interpolate opacity by `|Y - range_year|` |

---

## 🧪 Story Modes (toggleable)

- **Swipe Compare:** render two maps with **independent `currentYear`** (left/right).  
- **Pin & Annotate:** clicks add notes stamped with `era = currentYear` (saved to session).  
- **Auto-play:** increment `currentYear` on an interval for cinematic time-lapse.  
- **Focus Sync:** when Focus Mode centers on an event with `date`, snap slider to that year.

---

## ♿ Accessibility & Performance

**Accessibility**
- Keyboard operable slider (`Tab`, `←/→`, `Home/End`, `PgUp/PgDn`).
- High-contrast handles; visible focus ring; ARIA labelling (`aria-labelledby`).

**Performance**
- Prefer **PMTiles** and **vector tiles**; keep expressions simple (`step`, `interpolate`).
- Update a **single variable** (or shared filters) rather than per-feature operations.
- Downsample at low zoom; reveal detail on zoom-in.
- Debounce slider updates (e.g., 16–33ms) to keep 60fps.

---

## 🔧 Telemetry & Governance Hooks

- Emit `kfm:timeline:year` custom event on changes for **telemetry** and **governance** audit.  
- Log slider interactions to `focus-telemetry.json` with fields: `{ user, ts, year, layer_count, fps }`.  
- Respect **FAIR+CARE**: ensure sensitive layers (e.g., protected sites) enforce visibility policies per `DATA-GOVERNANCE.md`.

```ts
window.addEventListener('kfm:timeline:year', (e: any) => {
  // Example: send to your telemetry collector
  // post('/api/telemetry', { event:'timeline-year', ...e.detail })
});
```

---

## 🧱 Data Contracts (timeline-ready layers)

| Field            | Req | Type      | Description                                    |
|------------------|-----|-----------|------------------------------------------------|
| `year`           | —   | `number`  | Single-year feature (optional if using range). |
| `year_start`     | ✅  | `number`  | First active year (inclusive).                  |
| `year_end`       | —   | `number`  | Last active year (inclusive; default `9999`).   |
| `epoch`          | —   | `string`  | Era label for color buckets (e.g., `pre1900`). |
| `class`          | —   | `string`  | Thematic category (e.g., landcover class).     |

> *Validation:* enforce via schema in your ETL and reject features missing `year_start`.

---

## 🧭 Known Good Defaults

- **Timeline bounds:** `min=1700`, `max=2025`, `step=1` (adjust per dataset range).  
- **Initial year:** pick from **active data density** (e.g., median of feature starts).  
- **Era palette:** neutral → cooler in older eras, warmer in recent (color-blind safe).

---

## 🕰️ Version History

| Version | Date       | Author | Summary                                         |
|--------:|------------|--------|-------------------------------------------------|
|  v9.7.0 | 2025-11-08 | KFM    | Initial KFM-ready MapLibre timeline playbook.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Docs](../../../../docs/) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>
