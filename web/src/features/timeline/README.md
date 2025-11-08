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

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-blue)](../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Aligned-orange)](../../../docs/standards)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

- **What:** Time‑linked style layers = layers whose **visibility/paint** depends on a **currentYear** state.  
- **Why:** Reveal **where people lived**, **waterways shifted**, **prairies converted**, **species moved**, **ownership changed**.  
- **How:** A single **HTML range input** updates a **MapLibre runtime var** that drives `filter` and `expression` logic.

---

## 🗂️ Directory Layout

```

web/
src/
features/
timeline/
README.md          # This file
timeline.ts        # State, bindings, helpers
slider.tsx         # UI slider (React)
styles/
timeline-style.json   # MapLibre style with expressions
datasets/
landcover.pmtiles     # PMTiles time-sliced
hydrology.pmtiles
settlements.pmtiles

````

---

## 🧩 Core Idea (MapLibre expressions)

Use a **global year** to control layers:

- **Show features up to a year:** `["<=", ["get","year_end"], ["var","currentYear"]]`
- **Fade by recency:** `["interpolate",["linear"],["-",["var","currentYear"],["coalesce",["get","year"],["get","year_start"],0]], 0,1, 50,0.2]`
- **Color by era bucket:** `["step",["var","currentYear"], "#d8d8d8", 1850, "#b3d1ff", 1900, "#7fb3ff", 1950, "#4d94ff", 2000, "#1a75ff"]`

---

## 🧾 Minimal Style Snippet (`styles/timeline-style.json`)

```json
{
  "version": 8,
  "glyphs": "https://demotiles.maplibre.org/font/{fontstack}/{range}.pbf",
  "sources": {
    "settlements": {
      "type": "vector",
      "url": "pmtiles://datasets/settlements.pmtiles"
    }
  },
  "metadata": { "vars": { "currentYear": 1900 } },
  "layers": [
    {
      "id": "settlements-fill",
      "type": "circle",
      "source": "settlements",
      "source-layer": "settlements",
      "filter": ["all",
        ["<=", ["get","year_start"], ["var","currentYear"]],
        [">=", ["coalesce", ["get","year_end"], 9999], ["var","currentYear"]]
      ],
      "paint": {
        "circle-radius": [
          "interpolate", ["linear"], ["zoom"], 5, 1.2, 10, 3.5, 12, 6
        ],
        "circle-color": [
          "step", ["var","currentYear"],
          "#c9c9c9", 1850, "#8fd3a1", 1900, "#5bbf8f", 1950, "#2b9f7a", 2000, "#0f7a5d"
        ],
        "circle-opacity": [
          "interpolate", ["linear"],
          ["-", ["var","currentYear"], ["coalesce", ["get","year"], ["get","year_start"], 0]],
          0, 1.0, 50, 0.25
        ]
      }
    }
  ]
}
````

---

## ⚙️ Bind the Slider → Style Var (`timeline.ts`)

```ts
import maplibregl from 'maplibre-gl';

export function initTimeline(map: maplibregl.Map, initialYear = 1900) {
  // Set a style variable that paint/filters read
  map.setStyleVar('currentYear', initialYear);

  // Optionally reflect current year in UI badges, telemetry, etc.
  return {
    setYear(y: number) { map.setStyleVar('currentYear', y); },
    getYear() { return map.getStyleVar('currentYear') as number; }
  };
}
```

---

## 🖱️ Simple UI (React slider) (`slider.tsx`)

```tsx
import React from 'react';

export function YearSlider({ year, setYear }: { year: number; setYear: (y:number)=>void }) {
  return (
    <label style={{display:'grid', gap:6}}>
      <span>Year: {year}</span>
      <input
        type="range"
        min={1700}
        max={2025}
        step={1}
        value={year}
        onChange={(e)=> setYear(parseInt(e.target.value,10))}
        aria-label="Timeline year"
      />
    </label>
  );
}
```

---

## 🧩 Wiring It Up (example usage)

```ts
import { initTimeline } from './timeline';
import { createRoot } from 'react-dom/client';
import { YearSlider } from './slider';

const map = new maplibregl.Map({ container: 'map', style: '/styles/timeline-style.json' });
map.on('load', () => {
  const tl = initTimeline(map, 1880);

  // Mount UI
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

## 🧾 Era Buckets & Datasets (KFM examples)

| Layer               | Feature key(s)           | Era logic                           |
| ------------------- | ------------------------ | ----------------------------------- |
| `settlements`       | `year_start`, `year_end` | show if `year_start ≤ Y ≤ year_end` |
| `hydrology`         | `year`, `epoch`          | step colors by `epoch` vs `Y`       |
| `landcover`         | `year`, `class`          | filter by class active at `Y`       |
| `ownership_parcels` | `grant_year`, `sold`     | fade when `Y > sold`                |
| `species_range`     | `range_year`             | interpolate opacity with recency    |

---

## 🧪 Story Modes (toggleable)

* **Swipe Compare:** duplicate map with **two `currentYear` vars** (left/right).
* **Pin & Annotate:** clicking adds a **note** with `era = currentYear` for session storytelling.
* **Auto‑play:** interval increments `currentYear` for cinematic time-lapse.

---

## ♿ Accessibility & Performance

* Slider has **ARIA label** and **keyboard** support.
* Prefer **PMTiles** to minimize requests; index by year where possible.
* Keep expressions cheap (prefer `step`/`interpolate` over heavy compound filters).
* Downsample points at small zooms; reveal detail as users zoom in.

---

## 🕰️ Version History

| Version | Date       | Author | Summary                            |
| ------: | ---------- | ------ | ---------------------------------- |
|  v9.7.0 | 2025-11-08 | KFM    | Initial MapLibre timeline playbook |

---

<div align="center">

© Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to docs](../../../../docs/) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
