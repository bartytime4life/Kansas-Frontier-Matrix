```markdown
---
title: "🗺️ Kansas Frontier Matrix — MapLibre Runtime Theming with Design Tokens (Accessible · Energy-Aware · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/maplibre/runtime-theming/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-runtime-theming-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **MapLibre Runtime Theming with Design Tokens**
`docs/guides/maplibre/runtime-theming/README.md`

**Purpose:**  
Teach how to **sync color palette, typography, and icon system** with **MapLibre GL** at runtime using **design tokens** so maps adapt live to **accessibility needs** (WCAG 2.1 AA+), **ambient energy mode** (battery-saver), and **context** (dark/light, high-contrast, dyslexia-friendly labels).

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Aligned-orange)](#)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

**Runtime theming** lets KFM switch **map colors, fonts, and icons** without reloading style JSONs.  
We centralize branding in **design tokens** (JSON variables) and propagate them into MapLibre **paint/layout** properties, **glyphs**, and **sprite** references via code. Benefits:

- **Accessibility-first:** contrast-checked palettes, larger label sizes, dyslexia-friendly fonts, focus outlines.
- **Energy-aware:** simplified palettes and disabled effects when in **battery saver** or **low-CPU** contexts.
- **Consistency:** UI and map share the **same tokens** (no drift).
- **Performance:** small diffs at runtime instead of loading new styles.

---

## 🗂️ Directory Layout

```

docs/guides/maplibre/runtime-theming/   # This guide and examples
web/                                     # React + MapLibre client
├─ src/
│  ├─ design-tokens/                   # Source-of-truth tokens
│  │  ├─ base.json                     # palette, spacing, radii, shadows
│  │  ├─ map.json                      # map-specific tokens (road, water, land)
│  │  └─ themes/
│  │     ├─ light.json
│  │     ├─ dark.json
│  │     └─ high-contrast.json
│  ├─ theming/
│  │  ├─ token-resolver.ts             # merges base + theme + env (a11y/energy)
│  │  ├─ maplibre-style-bridge.ts      # applies tokens to MapLibre runtime
│  │  └─ energy-sentry.ts              # detects battery/CPU & toggles features
│  ├─ map/
│  │  ├─ style.json                    # canonical style (token placeholders)
│  │  └─ layers.ts                     # layer keys and safe update helpers
│  └─ icons/
│     ├─ [sprite@1x.png](mailto:sprite@1x.png)                 # icon sprite
│     ├─ [sprite@2x.png](mailto:sprite@2x.png)
│     └─ sprite.json                   # sprite index
└─ public/fonts/                        # Inter, Source Serif, OpenDyslexic (licensed)

````

---

## 🧩 Concepts (plain language)

- **Design tokens:** shared variables (e.g., `color.brand.600`, `font.label`, `size.12`) used across UI and map.
- **Runtime styling:** changing MapLibre **paint/layout** properties with code (`setPaintProperty`, `setLayoutProperty`).
- **Energy mode:** if device reports **battery saver** or high CPU load, we simplify visuals (fewer layers, no halos).
- **A11y profiles:** user selects **Default**, **High Contrast**, **Dyslexia-Friendly**, **Large Labels**; we map these to token sets.

---

## ⚙️ Implementation Steps

1) **Author tokenized style**  
   In `web/src/map/style.json`, reference **placeholders** that your bridge will replace at runtime:

```json
{
  "version": 8,
  "name": "KFM Base",
  "sprite": "/icons/sprite",
  "glyphs": "/fonts/{fontstack}/{range}.pbf",
  "sources": { /* ... */ },
  "layers": [
    {
      "id": "land",
      "type": "fill",
      "source": "basemap",
      "source-layer": "land",
      "paint": { "fill-color": "{color.land.fill}" }
    },
    {
      "id": "water",
      "type": "fill",
      "source": "basemap",
      "source-layer": "water",
      "paint": { "fill-color": "{color.water.fill}" }
    },
    {
      "id": "road-primary",
      "type": "line",
      "source": "transport",
      "source-layer": "road",
      "filter": ["==", "class", "primary"],
      "paint": {
        "line-color": "{color.road.primary}",
        "line-width": "{size.road.primary.width}"
      }
    },
    {
      "id": "label-place",
      "type": "symbol",
      "source": "places",
      "source-layer": "place",
      "layout": {
        "text-field": ["get", "name"],
        "text-font": ["{font.label.family}"],
        "text-size": "{font.label.size}"
      },
      "paint": {
        "text-color": "{color.label.text}",
        "text-halo-color": "{color.label.halo}",
        "text-halo-width": "{size.label.halo}"
      }
    }
  ]
}
````

2. **Resolve tokens**
   Merge **base + map + theme + a11y + energy** into a flat map:

```ts
// web/src/theming/token-resolver.ts
import base from "../design-tokens/base.json";
import map from "../design-tokens/map.json";
import light from "../design-tokens/themes/light.json";
import dark from "../design-tokens/themes/dark.json";
import highContrast from "../design-tokens/themes/high-contrast.json";

type Profile = "light" | "dark" | "high-contrast";
type A11y = { dyslexia?: boolean; largeLabels?: boolean; };
type Energy = { batterySaver?: boolean; lowCPU?: boolean; };

export function resolveTokens(profile: Profile, a11y: A11y, energy: Energy) {
  const theme = profile === "dark" ? dark : profile === "high-contrast" ? highContrast : light;
  const merged = { ...base, ...map, ...theme };

  if (a11y.dyslexia) merged["font.label.family"] = "OpenDyslexic";
  if (a11y.largeLabels) merged["font.label.size"] = Math.round((merged["font.label.size"] ?? 14) * 1.25);

  if (energy.batterySaver || energy.lowCPU) {
    merged["color.label.halo"] = merged["color.bg"];               // simpler halos
    merged["effect.glow.enabled"] = false;                         // drop expensive effects
    merged["size.road.primary.width"] = 2;                         // thinner lines
  }

  return flatten(merged);
}

// Flatten nested token objects to dot.notation => value
function flatten(obj: any, path: string[] = [], out: Record<string, any> = {}) {
  Object.entries(obj).forEach(([k, v]) => {
    const p = [...path, k];
    if (v && typeof v === "object" && !Array.isArray(v)) flatten(v, p, out);
    else out[p.join(".")] = v;
  });
  return out;
}
```

3. **Bridge tokens → MapLibre**
   Replace placeholders in style and apply deltas safely:

```ts
// web/src/theming/maplibre-style-bridge.ts
import type { Map } from "maplibre-gl";

export function applyTokens(map: Map, tokens: Record<string, any>) {
  map.getStyle().layers?.forEach(layer => {
    // Paint properties
    const paint = (layer as any).paint ?? {};
    Object.keys(paint).forEach(prop => {
      const val = (paint as any)[prop];
      const resolved = resolve(val, tokens);
      if (resolved !== undefined) map.setPaintProperty(layer.id, prop, resolved);
    });

    // Layout properties
    const layout = (layer as any).layout ?? {};
    Object.keys(layout).forEach(prop => {
      const val = (layout as any)[prop];
      const resolved = resolve(val, tokens);
      if (resolved !== undefined) map.setLayoutProperty(layer.id, prop, resolved);
    });
  });
}

function resolve(value: any, tokens: Record<string, any>) {
  if (typeof value === "string" && value.startsWith("{") && value.endsWith("}")) {
    const key = value.slice(1, -1);
    return tokens[key];
  }
  return value;
}
```

4. **Detect energy & a11y**
   Lightweight heuristics (no PII; opt-in):

```ts
// web/src/theming/energy-sentry.ts
export async function senseEnergy() {
  const navAny = navigator as any;
  const bs = navAny?.getBattery ? await navAny.getBattery() : null;
  const batterySaver = !!(bs && !bs.charging && bs.level < 0.25);
  const lowCPU = ("hardwareConcurrency" in navigator) && (navigator.hardwareConcurrency ?? 4) <= 4;
  return { batterySaver, lowCPU };
}

export function senseA11y(): { dyslexia: boolean; largeLabels: boolean } {
  const prefersContrast = matchMedia("(prefers-contrast: more)").matches;
  const prefersLargeText = matchMedia("(min-resolution: 1.5dppx)").matches; // crude proxy for hi-DPI zoom
  return { dyslexia: false, largeLabels: prefersContrast || prefersLargeText };
}
```

5. **Wire up in React**

```ts
// web/src/map/MapView.tsx
import { useEffect } from "react";
import maplibregl from "maplibre-gl";
import baseStyle from "./style.json";
import { resolveTokens } from "../theming/token-resolver";
import { applyTokens } from "../theming/maplibre-style-bridge";
import { senseEnergy, senseA11y } from "../theming/energy-sentry";

export function MapView() {
  useEffect(() => {
    const map = new maplibregl.Map({
      container: "map",
      style: baseStyle as any
    });

    (async () => {
      const energy = await senseEnergy();
      const a11y = senseA11y();
      const profile = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
      const tokens = resolveTokens(profile as any, a11y, energy);
      map.on("load", () => applyTokens(map, tokens));
    })();

    return () => map.remove();
  }, []);

  return <div id="map" style={{ width: "100%", height: "100%" }} />;
}
```

---

## ♿ Accessibility Checklist (WCAG 2.1 AA)

* Text contrast ≥ **4.5:1** for all admin and label layers.
* **High-contrast theme** available and discoverable (toggle + system `prefers-contrast`).
* **Dyslexia option** uses OpenDyslexic (licensed) or fallback with increased letter spacing.
* **Hit targets** ≥ 44×44 for map controls.
* **Focus states** visible with tokenized outline color.
* **Motion reduction:** respect `prefers-reduced-motion` (disable animated symbol transitions).

---

## 🔋 Energy-Aware Modes

* **Battery Saver:** simplify effects (no glows), reduce halo width, throttle label collisions.
* **Low-CPU:** downshift line-widths and symbol layers; prefer static sprites over SDF-heavy effects.
* **Offline/Low-memory:** collapse POI sublayers and lower source tile cache.

---

## 🧾 Token Examples

```json
{
  "color": {
    "bg": "#0B0C0E",
    "land": { "fill": "#121417" },
    "water": { "fill": "#164B73" },
    "road": { "primary": "#E0B050" },
    "label": { "text": "#EAECEF", "halo": "#0B0C0E" }
  },
  "font": { "label": { "family": "Inter", "size": 14 } },
  "size": { "road": { "primary": { "width": 3 } }, "label": { "halo": 1.2 } },
  "effect": { "glow": { "enabled": true } }
}
```

---

## 🧾 Governance & Telemetry Hooks

* Log theme switches and **token diffs** to `focus-telemetry.json` (no PII).
* Record **a11y toggles** and **energy mode** as environment facets for reproducibility.
* Maintain **SBOM** entries for fonts and sprites; include license notices.

---

## 🧪 Validation

* **Contrast tests:** assert each label layer meets threshold given background token.
* **Snapshot tests:** json-diff expected vs. applied MapLibre style after token resolution.
* **Perf budget:** max time to re-theme ≤ 60 ms; frames dropped < 2 during toggle.

---

## 🧩 Integration Tips

* Keep **style layer IDs** stable; the bridge relies on them.
* Avoid hard-coded colors in **data-driven** layers—use token-derived expression stops.
* External datasets (e.g., hydrology hazard overlays) should consume **semantic tokens** like `color.hazard.flood` rather than hex.

---

## 🕰️ Version History

| Version | Date       | Author     | Summary                                                 |
| ------: | ---------- | ---------- | ------------------------------------------------------- |
| v10.0.0 | 2025-11-10 | KFM Assist | Initial runtime theming guide with tokens, a11y, energy |

---

<div align="center">

© Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to docs/guides](../../README.md) · [Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
```
