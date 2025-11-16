---
title: "🗺️ Kansas Frontier Matrix — MapView Primitives Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/MapView/primitives/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-components-mapview-primitives-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-mapview-primitives"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/map/README.md@v10.3.1"
  - "web/src/components/MapView/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E34 Inscription"
  schema_org: "Map"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../schemas/json/web-components-mapview-primitives.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-components-mapview-primitives-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-mapview-primitives-v10.4.0"
semantic_document_id: "kfm-doc-web-components-mapview-primitives"
event_source_id: "ledger:web/src/components/MapView/primitives/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "coordinate inference"
  - "unverified geographic claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public (spatial-governed)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release"
sunset_policy: "Superseded upon MapView v3 primitive refactor"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapView Primitives Overview**  
`web/src/components/MapView/primitives/README.md`

**Purpose:**  
Document the **low-level, legacy MapLibre UI primitives** used internally by  
`web/src/components/MapView/` after the v10.4 refactor.  
These primitives are still supported for backwards compatibility, testability,  
and for gradual migration toward the full MapView v2 subsystem.

They must comply with **FAIR+CARE**, **WCAG 2.1 AA**, and non-speculative spatial ethics.

</div>

---

# 📘 Overview

The MapView primitives include the original **2D MapLibre UI elements** from the pre–v10.4  
`map/` folder. They now exist solely as **implementation helpers** for MapView’s  
high-level layers such as:

- `StoryNodeLayer`
- `FocusHighlightLayer`
- `DatasetFootprintLayer`
- `SovereigntyMaskLayer`
- `LegendPanel`
- `MapControls`

These primitives must never:

- Expose restricted spatial detail  
- Display unmasked coordinates  
- Leak dataset-sensitive geographic information  
- Perform speculative transformations  
- Render AI-derived spatial data  

They serve **only** as safe, deterministic presentation tools.

---

# 🧱 Directory Structure (Labeled)

~~~text
web/src/components/MapView/primitives/
├── MapContainer.tsx              # Legacy base MapLibre wrapper; mounts map instance
├── LayerToggle.tsx               # Old per-layer toggle; used in wrapped controls
├── Legend.tsx                    # Legacy accessible legend block
└── FeatureHighlight.tsx          # Legacy feature highlight renderer (no inference)
~~~

---

# 🧩 Component Responsibilities

## 🗺️ **MapContainer.tsx**
A minimal wrapper used to mount MapLibre and forward references.

Responsibilities:
- Initialize map instance in legacy contexts  
- Provide predictable mount point for MapViewContainer  
- Allow story/focus spatial overlays to anchor safely  

Governance:
- No coordinates may be emitted raw  
- No ungoverned layers may be added directly  

---

## 🧮 **LayerToggle.tsx**
Legacy toggle to show/hide map layers.

Used internally by:
- `MapControls.tsx`
- `LegendPanel.tsx`

Requirements:
- High-contrast toggle  
- Keyboard operability  
- Clear ARIA labeling  

Governance:
- Must not expose unavailable/sensitive layers  
- Must present reason codes for disabled layers  

---

## 🎨 **Legend.tsx**
Legacy accessible legend UI.

Serves as:
- A fallback block  
- A simple legend unit beneath the new LegendPanel  

Rules:
- WCAG AA contrast for color ramps  
- CARE-aware labeling (Public / Restricted / Sovereignty-Controlled)  
- No misleading color semantics  

---

## ✨ **FeatureHighlight.tsx**
Legacy viewer for map highlight geometry.

Still used for:
- Focus Mode highlight previews  
- Story Node hover states  
- Generic selection outlines  

Governance:
- No precise point/line/polygon rendering for sensitive sites  
- Must route to sovereignty masking layer when relevant  
- Spatial information must be coarse/generalized  

---

# 🔐 Governance & FAIR+CARE Considerations

All primitives must:

- Respect CARE metadata  
- Never display raw coordinates for sensitive datasets  
- Use H3 generalization or safe fallback graphics  
- Provide provenance context when rendering derived geometries  
- Avoid speculative map-based storytelling or inference  

If primitives violate governance → **CI BLOCK**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

Primitives MUST:

- Use ARIA-compliant roles  
- Support keyboard focus and toggles  
- Use WCAG AA contrast  
- Provide SR-only metadata summaries  
- Respect `prefers-reduced-motion`  

A11y regressions → **hard fail**.

---

# 📈 Telemetry Responsibilities

Primitives do **not** send telemetry directly,  
but must ensure:

- Events forwarded to higher-level components are stable  
- No PII or coordinate-level detail is emitted  
- Interactions do not break telemetry schemas  

---

# 🧪 Testing Expectations

Each primitive must include:

- Unit tests  
- Governance masking tests  
- A11y tests  
- Snapshot tests (optional)  
- No network/API testing (UI only)  

Test locations:

~~~text
tests/unit/web/components/MapView/primitives/**
tests/integration/web/components/MapView/primitives/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Primitives migrated under MapView; FAIR+CARE alignment added |
| v10.3.2 | 2025-11-14 | Pre-refactor map primitives stabilized |
| v10.3.1 | 2025-11-13 | Initial primitive components under old `map/` |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

