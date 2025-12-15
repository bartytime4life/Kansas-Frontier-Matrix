---
title: "🗺️ Kansas Frontier Matrix — Map Styling Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/maps/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"
backward_compatibility: "Aligned: v10.x → v11.x"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-maps-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status_category: "Specification"
doc_kind: "Specification"
intent: "web-styles-maps"
role: "specification"
category: "Web · Styles · Maps"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Spatial-Dependent"
sensitivity_level: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/styles/maps/README.md@v10.3.2"
  - "web/src/styles/maps/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  geosparql: "N/A"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-styles-maps.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-maps-shape.ttl"

doc_uuid: "urn:kfm:doc:web-styles-maps-v11.2.6"
semantic_document_id: "kfm-doc-web-styles-maps"
event_source_id: "ledger:web/src/styles/maps/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-visual-semantics"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next map-style system major update"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map Styling Specification (v11)**  
`web/src/styles/maps/README.md`

Defines the **map-specific styling contract** for the Kansas Frontier Matrix (KFM) Web Platform:
MapLibre (2D) + Cesium (3D) UI styling, layer legend presentation, masking/generalization visuals,
and governance-safe map affordances (A11y-first, FAIR+CARE-aligned, sovereignty-aware).

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../mcp/MCP-README.md)
· [![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)](../../../../docs/standards/)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)

</div>

---

## 📘 Overview

This document governs the **visual styling layer** used by map-centric UI surfaces in the KFM web application, including:

- **MapLibre GL JS** map containers, controls, popups, tooltips, and overlay chrome (2D).
- **CesiumJS** container styling for 3D mode and any 3D UI overlays (3D).
- **Layer legend and HUD styling** (readable, A11y-safe, responsive).
- **Masking/generalization visuals** used to ethically represent restricted or sensitive spatial content.
- **Governance-safe map affordances** (clear warnings, non-optional overlays when required).

**Non-negotiables (contract):**

- Map styles **must be token-driven** (no ad-hoc colors/spacing that bypass tokens/themes).
- Map styling **must not weaken governance signaling**:
  - masking/generalization must remain obvious,
  - sovereignty and restriction notices must remain visible and legible,
  - warnings must not become “decorative” via styling.
- Map styling must remain **accessible by default** (WCAG 2.1 AA+), including high-contrast and reduced-motion support.
- The frontend remains a **consumer** of backend governance decisions; the UI **renders** those decisions and does not override them.

---

## 🗂️ Directory Layout

~~~text
📁 web/
└── 📁 src/
    └── 📁 styles/
        └── 📁 maps/
            ├── 📄 README.md          # This specification (map styling contract)
            ├── 📄 maplibre.css       # MapLibre containers, controls, popups, overlays (tokenized)
            ├── 📄 cesium.css         # Cesium containers + 3D UI overlays (tokenized)
            ├── 📄 layers.css         # Layer symbolization helpers (borders, lines, fills, highlight states)
            ├── 📄 legends.css        # Legend layout, swatches, labels, accessibility helpers
            ├── 📄 masking.css        # Masking/generalization visuals (H3/grid/patterns) for restricted content
            └── 📄 hud.css            # HUD styling (cursor readout, scale bar, debug overlays when allowed)
~~~

**Directory rule:** if file names differ in the repository, update this tree to match **without changing the contract** (token-first, governance-safe, A11y-first).

---

## 🧭 Context

KFM’s map UI is designed for **spatial + temporal storytelling** and dataset exploration:

- Users navigate through time (timeline/slider) and space (map/3D view), switching basemaps and overlays.
- Datasets and layers are catalog-driven; each layer is expected to have styling and a legend presentation.
- The interface blends modern mapping UI with a historical reading experience; styling supports long-form narrative consumption.

This map styling layer is downstream of:

- **Design tokens and theming** (shared conventions and CSS variables).
- **Governance overlays** (CARE labels, sovereignty flags, masking requirements).
- **Layer configuration** provided by backend/catalog services (e.g., STAC/DCAT-backed metadata and layer descriptors).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph DS["Design System"]
    TOK["tokens/** (colors, spacing, typography)"]
    THE["themes/** (CSS variables)"]
    MIX["mixins/** (focus rings, reduced-motion)"]
  end

  subgraph MAP["Map Styling Layer"]
    CSS2D["maplibre.css"]
    CSS3D["cesium.css"]
    LAY["layers.css"]
    LEG["legends.css"]
    MSK["masking.css"]
    HUD["hud.css"]
  end

  TOK --> THE
  THE --> MAP
  MIX --> MAP

  CFG["Layer config + dataset metadata (STAC/DCAT)"] --> UI["Map UI Components"]
  GOV["Governance decisions (CARE/sovereignty/masking)"] --> UI

  MAP --> UI
  UI --> UX["User Experience (2D/3D + Timeline + Legend)"]
~~~

---

## 🧱 Architecture

### Token-first styling contract

Map styles must use **design tokens and theme variables** for:

- colors (including contrast-safe palettes),
- typography and sizing,
- spacing and layout rhythm,
- radii and elevation,
- z-index/layering rules for overlays and drawers.

**Prohibited:**

- “magic” hex colors in map CSS unless defined as a token-derived variable.
- pixel-perfect overrides that break high-contrast mode.
- hiding governance UI via opacity, z-index tricks, or “display: none” (unless explicitly governed and tested).

### `maplibre.css` responsibilities

MapLibre-specific CSS governs:

- map container sizing and responsive behavior,
- control styling (zoom/compass/attribution),
- popup and tooltip styling,
- overlay container styling (legends, chips, warnings, HUD mount points).

Accessibility requirements:

- all controls must have clear focus indicators,
- controls must remain operable with keyboard-only navigation,
- map UI must remain usable under large text and high-contrast settings.

### `cesium.css` responsibilities

Cesium-specific CSS governs:

- Cesium canvas container and overlay mounts,
- any 3D UI elements (timelines/controls if enabled),
- consistent typography and chrome styling that matches the 2D map.

Motion requirements:

- 3D-related UI transitions must respect reduced-motion preferences.
- any animated UI must degrade to a static presentation mode.

### `layers.css` responsibilities

`layers.css` provides **layer-agnostic styling helpers** used across many map overlays:

- selection and hover states (e.g., outlines, glow alternatives that remain accessible),
- boundary emphasis rules (do not overpower masking overlays),
- consistent thickness/opacity conventions for lines and fills,
- safe defaults for dense layers (avoid visual noise and misleading salience).

Important constraint:

- **Data category styling** (hydrology vs. admin boundaries) is allowed,
- **Governance meaning** (restricted/sovereignty/masked) must be reserved for governance overlay components and masking styles.

### `legends.css` responsibilities

Legend styling must:

- remain readable on small viewports and in split-pane layouts,
- provide accessible swatches and text labels,
- support screen-reader-friendly descriptions (via structure and SR-only helpers in the component layer),
- preserve license/provenance display areas (do not truncate or hide the metadata region).

### `masking.css` responsibilities

Masking/generalization visuals are a **governance safeguard**, not a decorative effect.

Masking styles must:

- make generalized regions clearly distinct from precise layers,
- avoid patterns that could be mistaken for “normal” symbology,
- remain visible in every theme, including high-contrast mode,
- support layered overlays (masking should remain visible above base layers where policy requires).

### `hud.css` responsibilities

HUD styling governs:

- cursor readouts (coarse region labels, not necessarily precise coordinates),
- scale bars and map status indicators,
- debug overlays in development modes (must not leak sensitive data; must be gated by policy and build flags).

HUD constraint:

- HUD must not obscure governance warnings, legends, or critical interaction areas.

---

## 🧠 Story Node & Focus Mode Integration

Map styling must support narrative and focus workflows:

- **Story Node footprints** (points/lines/polygons) must be legible, discoverable, and accessible.
- **Focus state highlighting** must be visually distinct from generic selection states and must not conflict with masking overlays.
- If a Story Node or Focus target is governed as generalized/masked, map styling must:
  - ensure the generalized visual is clearly indicated,
  - avoid presenting “precise” styling affordances (e.g., sharp pinpoint markers) when precision is prohibited.

---

## 🌐 STAC, DCAT & PROV Alignment

Map views frequently preview datasets and assets discovered via catalog services.

Map styling must preserve space and readability for catalog-derived metadata display in:

- legends,
- tooltips/popups,
- layer chips and badges (license, provenance, governance notices).

Key rule:

- **Catalog/provenance content is rendered by components**, but **styles must not make that content unreadable** (e.g., low contrast badges, truncation, hidden overflow without affordances).

---

## ⚖ FAIR+CARE & Governance

Map styling is a governance-critical surface because it can unintentionally reveal sensitive information.

Minimum governance requirements:

- Sovereignty and restriction notices must remain **visually prioritized** and **non-optional** when policy requires.
- Masking/generalization must remain **obvious** (no “subtle” masking).
- Styling must not imply precision when precision is withheld (avoid precise markers for generalized locations).
- Do not visually “down-rank” warnings (e.g., smaller, lighter, or low-contrast text for serious notices).

Indigenous data protection implications:

- This styling layer must support sovereignty signals and culturally sensitive restrictions.
- Icons, patterns, and colors must avoid culturally inappropriate symbolism.

---

## 📦 Data & Metadata

### Telemetry implications

CSS does not emit telemetry directly, but map styling influences interaction behavior and error rates.

When significant changes are made to map styling, monitor (via approved telemetry dashboards):

- interaction shifts (layer toggles, legend opens, map control usage),
- A11y mode usage (high-contrast and reduced-motion sessions),
- governance affordance engagement (masking notices viewed, “why masked?” interactions).

Telemetry emitted by the web layer must conform to `telemetry_schema` and must remain non-PII.

---

## 🧪 Validation & CI/CD

Map styling changes must be validated to avoid regressions in governance signaling and accessibility.

Minimum validation expectations:

- **Contrast validation** for map UI chrome, legends, and warnings across themes.
- **Reduced-motion validation** for any UI transitions affected by styles.
- **Visual regression checks** for:
  - masked vs. unmasked overlays,
  - legend readability,
  - control focus visibility,
  - sovereignty/warning overlays.
- **Layout regression checks** on narrow and split-pane viewports.

Repository guidance:

- Prefer codified checks in CI over manual-only reviews.
- If new tokens or theming variables are required, they must be introduced through the design-token pipeline (not ad-hoc CSS).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Reformatted to KFM-MDP v11.2.6 heading registry and section order; clarified governance-critical masking rules; tightened token-first contract; updated release artifact references. |
| v10.4.0 | 2025-11-15 | Introduced map styling spec; aligned MapLibre/Cesium/legends/masking with tokens & themes. |
| v10.3.2 | 2025-11-14 | Hardened CARE/sovereignty overlay styling in maps. |
| v10.3.1 | 2025-11-13 | Initial map-specific styles for MapLibre and base legends. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Styles Overview](../README.md) · [💻 Web Source Overview](../../README.md) · [🌐 Web Platform Overview](../../../README.md) · [🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
