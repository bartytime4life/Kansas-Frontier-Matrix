---
title: "🗺️ Kansas Frontier Matrix — MapLibre UI Design & Interaction Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/visualization/maplibre-ui-design.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/visualization-maplibre-ui-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "maplibre-ui-design"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapLibre UI Design & Interaction Framework**  
`docs/guides/visualization/maplibre-ui-design.md`

**Purpose**  
Define the **user interface, component layout, interaction model, and governance rules**  
for the MapLibre-based visualization layer of the Kansas Frontier Matrix (KFM).  

Ensures that map experiences are:

- **Accessible** (WCAG 2.1 AA + KFM A11y standards)  
- **Governed** (CARE v2, sovereignty, masking)  
- **Performant** (FPS, latency, memory budgets)  
- **Consistent** (token-driven theming · MapLibre + React alignment)  

</div>

---

# 📘 Overview

The **MapLibre UI Design Framework** describes:

- How the web app renders maps using MapLibre GL JS  
- How React components structure map layout and controls  
- How layers are orchestrated (MapView + LayerManager)  
- How Focus Mode v2 and Story Nodes integrate onto the map  
- How runtime theming & accessibility are handled (tokens, themes, A11y/sustainability)  
- How Telemetry v2 and governance signals (CARE, sovereignty, provenance) are captured

This guide is tightly coupled with:

- `docs/guides/maplibre/README.md` (integration)  
- `docs/guides/maplibre/runtime-theming/README.md`  
- `docs/guides/visualization/timeline-visualization.md`  

---

# 🗂️ Directory Context

~~~text
docs/guides/visualization/
├── README.md                         # Visualization overview
├── maplibre-ui-design.md             # THIS document
├── timeline-visualization.md         # Temporal storytelling interface
├── explainability-dashboard.md       # AI explainability visualization
└── accessibility-standards.md        # WCAG & CARE v2 UI standards
~~~

Frontend code lives at:

~~~text
web/src/components/MapView/
web/src/features/map/
web/src/styles/tokens/map.tokens.ts
web/src/styles/themes/
~~~

---

# 🧩 UI Architecture Overview (GitHub-Safe Mermaid)

```mermaid
flowchart TD

BASE["MapLibre GL JS<br/>Base Map Canvas"] --> LM["Layer Manager<br/>sources · layers · ordering"]
LM --> PANELS["UI Panels<br/>legend · controls · metadata"]
PANELS --> FOCUS["Focus & Story Overlays<br/>AI insights · Story Node footprints"]
FOCUS --> TELE["Telemetry Hooks<br/>FPS · latency · interactions · CARE flags"]
TELE --> GOV["FAIR+CARE & A11y Reports<br/>governance · accessibility"]
````

---

# 1️⃣ Component Structure (React + MapLibre)

| Component                    | Description                                        | Key Concerns                         |
| ---------------------------- | -------------------------------------------------- | ------------------------------------ |
| `MapViewContainer`           | High-level container for map + panels              | Layout, A11y regions, theming hooks  |
| `MapCanvas`                  | Wraps MapLibre map instance                        | WebGL init, error boundaries         |
| `LayerManager`               | Registers sources + layers and controls draw order | Determinism, governance layering     |
| `LegendPanel`                | Shows symbology + provenance + CARE labels         | WCAG contrast, screen-reader support |
| `MapControls`                | Zoom, basemap, layer toggles, focus reset          | Keyboard nav, hit area, A11y tokens  |
| `TimelineOverlay` (optional) | Time slider overlay integrated with TimelineView   | A11y slider patterns, reduced motion |
| `FocusHighlightLayer`        | Highlights Focus Mode v2 entities                  | CARE/sovereignty-aware overlays      |
| `StoryNodeLayer`             | Story Node v3 footprints                           | generalized for sensitive sites      |
| `CursorHUD`                  | Shows coordinates, values, selection info          | Non-PII text, high contrast          |

---

# 2️⃣ Layout & Regions

The map UI is typically structured into regions:

* **Map Canvas** — central map area (`<main>` or landmark with ARIA)
* **Left / Right Panels** — legend, layers, governance
* **Bottom/Top Bars** — timeline, status, context hints
* **HUD** — lean overlay with coordinates, scale, debug info

All interactive elements must be reachable via keyboard, and map-specific interactions
must not break or trap focus.

---

# 3️⃣ Layer Interaction Guidelines

| Interaction           | Expected Behavior                                           | FAIR+CARE v2 Alignment                                 |
| --------------------- | ----------------------------------------------------------- | ------------------------------------------------------ |
| Hover / Tooltip       | Show concise info: title, dataset, key value, provenance    | Provide citations, avoid hidden meaning                |
| Click / Focus         | Open detailed panel: narrative, metadata, Story Nodes links | Allow keyboard activation, show CARE labels            |
| Zoom Range Visibility | Enable/disable layers at specific zoom levels               | Prevent clutter, limit overdraw & GPU use              |
| Sensitive Layers      | Require explicit toggle + warning banner                    | Protect sovereignty & sensitive cultural data          |
| Timeline Sync         | Layer visibility & styling responds to time window          | Transparent historical shifts, highlight uncertainties |

Sensitive layers MUST be visually marked and associated with CARE v2 metadata
(e.g., `careLabel: "restricted"`).

---

# 4️⃣ Design Tokens & Theming (MapUI)

Map UI uses token-driven design:

| Token                   | Purpose               | Example   |
| ----------------------- | --------------------- | --------- |
| `color.ui.bg`           | Panel background      | `#0b0c0e` |
| `color.ui.accent`       | Primary action color  | `#2b6cb0` |
| `color.map.land.fill`   | Land fill color       | `#121417` |
| `color.map.water.fill`  | Water fill color      | `#164B73` |
| `color.map.label.text`  | Map label text color  | `#EAECEF` |
| `font.ui.body`          | Base UI font family   | `"Inter"` |
| `font.map.label.family` | Map label font family | `"Inter"` |
| `size.ui.borderRadius`  | Panel border radius   | `0.75rem` |
| `size.map.label.halo`   | Label halo width      | `1.2`     |

Tokens are defined in:

* `web/src/styles/tokens/color.tokens.ts`
* `web/src/styles/tokens/typography.tokens.ts`
* `web/src/styles/tokens/map.tokens.ts`

and theme modules in `web/src/styles/themes/`.

---

# 5️⃣ Focus Mode & Story Node Integration

Map UI must support **Focus Mode v2** and **Story Node v3**:

* **FocusHighlightLayer**:

  * Highlights the focused entity geometry.
  * Fades non-focused layers for context.
  * Respects masking strategies (no raw coordinates for restricted features).

* **StoryNodeLayer**:

  * Draws Story Node footprints (point/polygon shapes).
  * Aligns colors and styles with domain semantics (e.g., treaties vs. hazards).
  * Interacts with timeline: filtered by `when` intervals.

All Focus/Story overlays must:

* Provide readable tooltips for events
* Annotate provenance and sources
* Make CARE v2 classification visible in LegendPanel and overlays

---

# 6️⃣ Telemetry v2 & Performance

Map UI interactions contribute to Telemetry v2:

* `map:init` — map initialization stats
* `map:move` — panning and zoom events
* `map:layer-toggle` — layer visibility changes
* `map:focus-entity` — when focus moves to a new entity
* `map:error` — errors from MapLibre or data sources

Each event should report:

* `fps` or `frame_latency_ms_avg`
* approximate `energy_wh` (client-side estimate optional)
* `a11y_flags` (high-contrast, large labels, reduced motion)
* `care_flags` (presence of restricted overlays)

These are aggregated under:

```text
releases/<version>/pipeline-telemetry.json
```

which is then checked by `telemetry-sync.yml`.

---

# 7️⃣ Accessibility (WCAG 2.1 AA) for Map UI

Core requirements:

* All buttons, toggles, and panels:

  * have accessible labels and ARIA roles
  * are keyboard operable
  * show focus outlines

* Map overlays:

  * avoid conveying information **only via color**
  * use patterns or icons for critical differences if needed

* Legends:

  * use high-contrast swatches and text
  * supply text equivalents for color & pattern semantics

* Reduced Motion:

  * limit map animation when user prefers reduced motion
  * avoid long continuous auto-zoom or bounce effects

Accessibility testing integrated via:

* `ui-accessibility-validate.yml`
* Lighthouse + axe checks in CI

---

# 8️⃣ CI/CD Checks for Map UI

Recommended workflows:

| Workflow                        | Purpose                                     | Artifact                                   |
| ------------------------------- | ------------------------------------------- | ------------------------------------------ |
| `ui-accessibility-validate.yml` | A11y & FAIR+CARE UI checks (Lighthouse/axe) | `reports/accessibility/maplibre-ui.json`   |
| `ui-performance-benchmark.yml`  | FPS, latency, resource usage benchmarks     | `reports/perf/maplibre-ui-benchmark.json`  |
| `telemetry-export.yml`          | Telemetry v2 export for map interactions    | `data/telemetry/web-ui.ndjson`             |
| `faircare-validate.yml`         | Ethical and CARE v2 UI checks               | `reports/faircare/ui-ethics-maplibre.json` |

All must be configured as required checks for UI-impacting changes.

---

# 9️⃣ Example FAIR+CARE Map UI Report

```json
{
  "report_id": "maplibre-ui-2025-11-16-0001",
  "component": "MapLibre UI",
  "metrics": {
    "frame_latency_ms_avg": 16.8,
    "fps_min": 34,
    "energy_wh": 0.012,
    "co2_g": 0.0049
  },
  "accessibility_compliance": "AA",
  "faircare_status": "pass",
  "a11y_flags": {
    "high_contrast_enabled": true,
    "reduced_motion": false
  },
  "care_flags": 1,
  "timestamp": "2025-11-16T12:00:00Z"
}
```

---

# 🔟 Developer Checklist (MapLibre UI)

Before merging changes that impact Map UI:

* [ ] Map layout works for desktop and mobile viewports.
* [ ] Map controls are fully keyboard-accessible.
* [ ] A11y + FAIR+CARE UI workflows pass in CI.
* [ ] Sensitive layers are clearly labeled and require explicit user activation.
* [ ] Focus Mode and Story Node overlays correctly honor CARE v2 masking.
* [ ] Telemetry v2 events are emitted for key interactions.
* [ ] Performance is within defined budgets (FPS, latency, memory).

---

# 🕰 Version History

| Version | Date       | Summary                                                                               |
| ------: | ---------- | ------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Upgraded to KFM-MDP v10.4.2; integrated Telemetry v2, CARE v2, and CI+A11y validation |
| v10.0.0 | 2025-11-09 | Initial MapLibre UI design framework with FAIR+CARE accessibility and telemetry       |

---

<div align="center">

**Kansas Frontier Matrix — MapLibre UI Design (v10.4.2)**
Spatial Storytelling × FAIR+CARE v2 × Accessible & Sustainable Map Interfaces
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
