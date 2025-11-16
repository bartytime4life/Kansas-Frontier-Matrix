---
title: "🗺️ Kansas Frontier Matrix — MapLibre Runtime Theming with Design Tokens (Accessible · Energy-Aware · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/maplibre/runtime-theming/README.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-maplibre-runtime-theming-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "web-maplibre-runtime-theming"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed"
sensitivity_level: "Varies by layer"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🗺️ **MapLibre Runtime Theming with Design Tokens**  
`docs/guides/maplibre/runtime-theming/README.md`

**Purpose**  
Define how to **sync color palette, typography, and icon system** with **MapLibre GL** at runtime using  
**design tokens** so maps adapt live to **accessibility needs** (WCAG 2.1 AA+), **ambient energy mode**  
(battery-saver / low-CPU), and **context** (light/dark, high-contrast, dyslexia-friendly labels).

This guide ties together:

- `web/src/styles/tokens/**`
- `web/src/styles/themes/**`
- `web/src/styles/mixins/**`
- `web/src/components/MapView/**` (MapLibre)
- A11y + energy-aware runtime features

</div>

---

# 📘 Overview

**Runtime theming** lets KFM change **map colors, fonts, and icons at runtime** without swapping style JSON files.  
We:

- Centralize branding & accessibility in **design tokens**  
- Map tokens into MapLibre **paint** / **layout** properties, glyphs, and sprites via code  
- Respect **user preferences** (light/dark, high contrast, reduced motion, dyslexia-friendly fonts)  
- Respond to **energy/CPU constraints** (battery saver, low core-count devices)  

Benefits:

- **Accessibility-first:** guaranteed contrast, label size scaling, dyslexia-friendly fonts, visible focus.  
- **Energy-aware:** fewer visual effects, simpler palettes in low-power contexts.  
- **Consistency:** UI (`Tailwind`, React) and map share the **same tokens**.  
- **Performance:** small runtime diffs instead of full style reloads.

---

# 🗂️ Directory Layout (Theming Integration · v10.4.2)

~~~text
docs/guides/maplibre/runtime-theming/
└── README.md                         # This guide

web/
└── src/
    ├── styles/
    │   ├── tokens/                   # Design tokens
    │   │   ├── color.tokens.ts       # color.* tokens
    │   │   ├── typography.tokens.ts  # font.* tokens
    │   │   ├── spacing.tokens.ts     # size.* tokens
    │   │   └── map.tokens.ts         # map-specific color/size tokens
    │   ├── themes/                   # Light/dark/high-contrast theme maps
    │   │   ├── light.ts
    │   │   ├── dark.ts
    │   │   └── highContrast.ts
    │   └── mixins/                   # Focus ring, layout, transitions
    │       ├── focus-ring.ts
    │       ├── layout.ts
    │       └── transitions.ts
    │
    ├── theming/
    │   ├── token-resolver.ts         # Merge tokens + theme + a11y + energy
    │   ├── maplibre-style-bridge.ts  # Apply tokens to MapLibre at runtime
    │   └── energy-sentry.ts          # Detect energy/CPU & A11y prefs
    │
    ├── components/
    │   └── MapView/
    │       ├── MapViewContainer.tsx  # Orchestrates map + theming
    │       ├── MapCanvas.tsx         # MapLibre instance
    │       └── primitives/           # Lower-level helpers (optional)
    │
    └── map/
        ├── style.json                # Canonical style with token placeholders
        └── layers.ts                 # Layer ids, helpers for safe updates

web/public/fonts/                     # Inter, Source Serif, OpenDyslexic, etc.
web/public/icons/                     # Sprite sheets & JSON index
~~~

---

# 🧱 Runtime Theming Architecture (Mermaid · GitHub-Safe)

```mermaid
flowchart TD

subgraph TOKENS["Tokens + Themes"]
  T["Design Tokens<br/>colors · fonts · sizes"]
  TH["Theme Profiles<br/>light · dark · high-contrast"]
end

subgraph CONTEXT["Runtime Context"]
  A11Y["A11y Preferences<br/>contrast · reduced motion"]
  EN["Energy/CPU Hints<br/>battery saver · low cores"]
end

subgraph RESOLVE["Resolver"]
  R["Token Resolver<br/>merge tokens + theme + context"]
end

subgraph MAP["MapLibre Runtime"]
  M["MapCanvas<br/>MapLibre style & layers"]
  B["Bridge<br/>apply tokens → paint/layout"]
end

T --> R
TH --> R
A11Y --> R
EN --> R
R --> B
B --> M
````

---

# 1️⃣ Design Tokens → MapLibre Style Placeholders

MapLibre base style (`web/src/map/style.json`) should reference token **placeholders** that the bridge will fill at runtime:

```json
{
  "version": 8,
  "name": "KFM Base",
  "sprite": "/icons/sprite",
  "glyphs": "/fonts/{fontstack}/{range}.pbf",
  "sources": { /* ... omitted ... */ },
  "layers": [
    {
      "id": "land",
      "type": "fill",
      "source": "basemap",
      "source-layer": "land",
      "paint": { "fill-color": "{color.map.land.fill}" }
    },
    {
      "id": "water",
      "type": "fill",
      "source": "basemap",
      "source-layer": "water",
      "paint": { "fill-color": "{color.map.water.fill}" }
    },
    {
      "id": "road-primary",
      "type": "line",
      "source": "transport",
      "source-layer": "road",
      "filter": ["==", "class", "primary"],
      "paint": {
        "line-color": "{color.map.road.primary}",
        "line-width": "{size.map.road.primary.width}"
      }
    },
    {
      "id": "label-place",
      "type": "symbol",
      "source": "places",
      "source-layer": "place",
      "layout": {
        "text-field": ["get", "name"],
        "text-font": ["{font.map.label.family}"],
        "text-size": "{font.map.label.size}"
      },
      "paint": {
        "text-color": "{color.map.label.text}",
        "text-halo-color": "{color.map.label.halo}",
        "text-halo-width": "{size.map.label.halo}"
      }
    }
  ]
}
```

These `{...}` placeholders will be replaced with actual values (hex, numeric, arrays)
using the token resolver and style bridge.

---

# 2️⃣ Token Resolver (`token-resolver.ts`)

The resolver merges:

* base tokens (`color.tokens.ts`, `typography.tokens.ts`, etc.)
* map-specific tokens (`map.tokens.ts`)
* theme module (`light.ts`, `dark.ts`, `highContrast.ts`)
* runtime context (A11y + energy)

A sketch:

```ts
// web/src/theming/token-resolver.ts
import * as colors from "../styles/tokens/color.tokens";
import * as typography from "../styles/tokens/typography.tokens";
import * as mapTokens from "../styles/tokens/map.tokens";
import * as light from "../styles/themes/light";
import * as dark from "../styles/themes/dark";
import * as highContrast from "../styles/themes/highContrast";

export type ThemeProfile = "light" | "dark" | "high-contrast";

export interface A11yContext {
  dyslexia?: boolean;
  largeLabels?: boolean;
  reducedMotion?: boolean;
}

export interface EnergyContext {
  batterySaver?: boolean;
  lowCPU?: boolean;
}

export function resolveTokens(
  profile: ThemeProfile,
  a11y: A11yContext,
  energy: EnergyContext
): Record<string, any> {
  const theme =
    profile === "dark" ? dark.tokens :
    profile === "high-contrast" ? highContrast.tokens :
    light.tokens;

  const merged = {
    ...colors.tokens,
    ...typography.tokens,
    ...mapTokens.tokens,
    ...theme
  };

  // Accessibility adjustments
  if (a11y.dyslexia) {
    merged["font.map.label.family"] = "OpenDyslexic";
  }
  if (a11y.largeLabels) {
    const baseSize = merged["font.map.label.size"] ?? 14;
    merged["font.map.label.size"] = Math.round(baseSize * 1.25);
  }

  if (a11y.reducedMotion) {
    merged["effect.map.glow.enabled"] = false;
  }

  // Energy-aware adjustments
  if (energy.batterySaver || energy.lowCPU) {
    merged["effect.map.glow.enabled"] = false;
    merged["color.map.label.halo"] = merged["color.bg"] ?? "#000000";
    merged["size.map.road.primary.width"] = 2;
  }

  return flattenTokens(merged);
}

function flattenTokens(
  obj: any,
  path: string[] = [],
  out: Record<string, any> = {}
): Record<string, any> {
  Object.entries(obj).forEach(([k, v]) => {
    const p = [...path, k];
    if (v && typeof v === "object" && !Array.isArray(v)) {
      flattenTokens(v, p, out);
    } else {
      out[p.join(".")] = v;
    }
  });
  return out;
}
```

This yields a flat map: `"color.map.land.fill" → "#101418"` etc.

---

# 3️⃣ Style Bridge (`maplibre-style-bridge.ts`)

This bridge replaces placeholders and calls `map.setPaintProperty` and `map.setLayoutProperty` safely.

```ts
// web/src/theming/maplibre-style-bridge.ts
import type { Map } from "maplibre-gl";

export function applyTokensToMap(map: Map, tokens: Record<string, any>) {
  const style = map.getStyle();
  if (!style?.layers) return;

  style.layers.forEach(layer => {
    const paint: Record<string, any> = (layer as any).paint ?? {};
    Object.keys(paint).forEach(prop => {
      const resolved = resolvePlaceholder(paint[prop], tokens);
      if (resolved !== undefined) {
        map.setPaintProperty(layer.id, prop, resolved);
      }
    });

    const layout: Record<string, any> = (layer as any).layout ?? {};
    Object.keys(layout).forEach(prop => {
      const resolved = resolvePlaceholder(layout[prop], tokens);
      if (resolved !== undefined) {
        map.setLayoutProperty(layer.id, prop, resolved);
      }
    });
  });
}

function resolvePlaceholder(value: any, tokens: Record<string, any>) {
  if (typeof value === "string" && value.startsWith("{") && value.endsWith("}")) {
    const key = value.slice(1, -1);
    return tokens[key];
  }
  return value;
}
```

---

# 4️⃣ Energy & A11y Detection (`energy-sentry.ts`)

This module infers energy and accessibility context:

```ts
// web/src/theming/energy-sentry.ts
export async function senseEnergy(): Promise<{ batterySaver: boolean; lowCPU: boolean }> {
  const navAny = navigator as any;
  let batterySaver = false;
  let lowCPU = false;

  try {
    if (navAny.getBattery) {
      const bs = await navAny.getBattery();
      batterySaver = !bs.charging && bs.level < 0.25;
    }
  } catch {
    // ignore
  }

  if ("hardwareConcurrency" in navigator) {
    const cores = navigator.hardwareConcurrency ?? 4;
    lowCPU = cores <= 4;
  }

  return { batterySaver, lowCPU };
}

export function senseA11y(): {
  dyslexia: boolean;
  largeLabels: boolean;
  reducedMotion: boolean;
} {
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const highContrast = matchMedia("(prefers-contrast: more)").matches;
  const dyslexia = false; // future: read from user profile/preference
  const largeLabels = highContrast;
  return { dyslexia, largeLabels, reducedMotion };
}
```

---

# 5️⃣ Wiring in MapView

```tsx
// web/src/components/MapView/MapViewContainer.tsx
import { useEffect } from "react";
import maplibregl from "maplibre-gl";
import baseStyle from "../../map/style.json";
import { resolveTokens } from "../../theming/token-resolver";
import { applyTokensToMap } from "../../theming/maplibre-style-bridge";
import { senseEnergy, senseA11y } from "../../theming/energy-sentry";

export function MapViewContainer() {
  useEffect(() => {
    const map = new maplibregl.Map({
      container: "map",
      style: baseStyle as any
    });

    (async () => {
      const energy = await senseEnergy();
      const a11y = senseA11y();
      const prefersDark = matchMedia("(prefers-color-scheme: dark)").matches;
      const prefersHC = matchMedia("(prefers-contrast: more)").matches;
      const profile = prefersHC ? "high-contrast" : prefersDark ? "dark" : "light";

      const tokens = resolveTokens(profile as any, a11y, energy);

      map.on("load", () => {
        applyTokensToMap(map, tokens);
      });
    })();

    return () => map.remove();
  }, []);

  return <div id="map" style={{ width: "100%", height: "100%" }} />;
}
```

---

# ♿ Accessibility Requirements

Runtime theming must ensure:

* **Text contrast ≥ 4.5:1** for all place, road, and administrative labels.
* **High-contrast theme** uses distinct, unambiguous colors for core layers.
* **Dyslexia-friendly option** uses OpenDyslexic or a similar font (licensed).
* **Reduced-motion** disables animated transitions (symbol fades, glows, pulses).
* Map controls and overlays follow KFM A11y mixins (focus ring, hit area, etc.).

---

# 🔋 Energy-Aware Behavior

When `batterySaver` or `lowCPU` is detected:

* Turn off expensive effects (`effect.map.glow.enabled = false`).
* Use simplified halos and backgrounds.
* Use fewer overlays (optionally drop high-detail layers).
* Prefer vector outlines over heavy raster glows.

---

# 📡 Telemetry v2 Integration

Runtime theming events should emit Telemetry v2 entries (non-PII) with:

* `event`: `map_theme_applied`
* `theme_profile`: `light|dark|high-contrast`
* `dyslexia_enabled`: boolean
* `large_labels`: boolean
* `battery_saver`: boolean
* `low_cpu`: boolean

This supports analyzing:

* which profiles are used most
* energy-saving modes triggered
* distribution of A11y usage

---

# 🧪 Testing

Recommended tests:

* **Contrast tests:** verify token combinations meet WCAG thresholds.
* **Snapshot tests:** confirm style diff before/after token application.
* **Perf tests:** ensure applying tokens does not cause jank or long stalls (≤ 60 ms).
* **A11y tests:** ensure large-label and dyslexia modes actually modify map text properties.

---

# 🕰 Version History

| Version | Date       | Summary                                                                                                     |
| ------: | ---------- | ----------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Upgraded to KFM-MDP v10.4.2; aligned with styles/tokens/themes mixins; added Telemetry v2 and CARE v2 hooks |
| v10.0.0 | 2025-11-10 | Initial runtime theming guide with tokens, accessibility, and energy-awareness                              |

---

<div align="center">

**Kansas Frontier Matrix — MapLibre Runtime Theming (v10.4.2)**
Accessible Cartography × Energy-Aware Rendering × Token-Driven Consistency
© 2025 Kansas Frontier Matrix — MIT License · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
