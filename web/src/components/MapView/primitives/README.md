---
title: "🗺️ Kansas Frontier Matrix — MapView Primitives Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/MapView/primitives/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/web-mapview-primitives-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-components-mapview-primitives-v2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public (spatial-governed)"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-mapview-primitives"
semantic_intent:
  - "UI-primitive"
  - "map-rendering"
  - "spatial-governance"
  - "low-level-graphics"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/map/README.md@v10.3.1"
  - "web/src/components/MapView/README.md@v10.4.0"
  - "web/src/components/MapView/primitives/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E34 Inscription"
  schema_org: "Map"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../../schemas/json/web-components-mapview-primitives-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-components-mapview-primitives-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-mapview-primitives-v11.2.2"
semantic_document_id: "kfm-doc-web-components-mapview-primitives-v11"
event_source_id: "ledger:web/src/components/MapView/primitives/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (primitive layer)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "coordinate-inference"
  - "unverified-geographic-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Requirements"
    - "🧪 Testing Expectations"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapView Primitives Overview**  
`web/src/components/MapView/primitives/README.md`

**Purpose:**  
Define the **low-level, legacy MapLibre UI primitives** that remain part of  
`web/src/components/MapView/` after the v10.4 → v11.2.2 migration.  
These primitives serve as internal presentation utilities used by MapView’s  
higher-order v3 components.  

They MUST comply with:  
- **FAIR+CARE** spatial governance requirements  
- **WCAG 2.1 AA+** accessibility  
- **Non-speculative spatial ethics**  
- **Deterministic rendering with no business logic**  

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

MapView primitives include the original **2D MapLibre UI elements** from the pre–v10.4  
`map/` folder, now retained strictly as **internal presentation helpers**.

They support higher-level MapView v3 layers:

- `StoryNodeLayer`  
- `FocusHighlightLayer`  
- `DatasetFootprintLayer`  
- `SovereigntyMaskLayer`  
- `LegendPanel`  
- `MapControls`  

**Primitives MUST NOT:**

- Render raw spatial coordinates  
- Expose sensitive geometries  
- Perform interpolation, inference, or “fill in missing shapes”  
- Render AI-derived spatial content  
- Associate locations with Story Nodes or Events unless provided directly by parent components  
- Emit telemetry directly (that’s handled by higher-level wrappers)

Primitives serve **only** as deterministic, safe render utilities.

---

## 🗂️ Directory Structure

~~~text
web/src/components/MapView/primitives/
│
├── 🗺️ MapContainer.tsx         # Legacy MapLibre wrapper; base mount for v3 map
├── 🔘 LayerToggle.tsx           # Old layer toggle primitive (keyboard + tooltip)
├── 🎨 Legend.tsx                # Legacy static legend block (fallback under LegendPanel)
└── ✨ FeatureHighlight.tsx       # Legacy geometry highlighter (coarse/generalized only)
~~~

New primitives must be documented here.

---

## 🧩 Component Responsibilities

### 🗺️ MapContainer.tsx

**Role:**  
Base wrapper used to mount MapLibre internally before v3 MapViewContainer superseded it.

**Responsibilities:**

- Provide a consistent DOM mount for map initialization  
- Forward map reference/hooks to higher-level orchestrators  
- Serve as safe anchor for fallback spatial overlays  

**Governance:**

- No raw geometry rendering  
- No direct base-layer loads  
- Must respect governance from parent (CARE, sovereignty, masking flags)  

---

### 🔘 LayerToggle.tsx

**Role:**  
Legacy toggle switch to show/hide map layers.

**Responsibilities:**

- Display toggle with:
  - High-contrast colors  
  - Clear on/off states  
  - ARIA labeling  
- Propagate toggle events to higher-level map orchestrators  

**Governance:**

- Must disable or hide toggles for restricted layers  
- Must show reason codes for disabled toggles (e.g., “Sovereignty restricted”)  

**A11y:**

- Keyboard-operable  
- Screen-reader descriptive label  

---

### 🎨 Legend.tsx

**Role:**  
Legacy accessible legend component.

**Responsibilities:**

- Show basic symbol/color sets for map overlays  
- Provide descriptive text for each class/symbol  
- Act as fallback for StoryNodeLayer/Masking overlays  

**Governance:**

- CARE classification labeling (e.g. Restricted, Public, Sovereignty-Controlled)  
- No inaccurate or speculative color semantics  

**A11y:**

- WCAG AA contrast  
- SR-only descriptions for color ramps  

---

### ✨ FeatureHighlight.tsx

**Role:**  
Legacy renderer for focus/hover highlight geometries.

**Responsibilities:**

- Draw simple outlines/halos for selected objects  
- Coarse/generalized rendering only  
- No precise polygons or sensitive shapes  

**Governance:**

- Must route masked items to sovereignty overlays  
- MUST NOT display full-resolution geometry  
- May only render generalized primitives passed from parent  

---

## 🔐 Governance & FAIR+CARE Integration

MapView primitives MUST:

- Respect all CARE metadata + sovereignty constraints  
- Mask or generalize spatial values when required  
- Provide visual cues for masking (color, icon, pattern)  
- Avoid any “best guess” or inferred geometry  
- Never export spatial details directly  
- Never override governance rules passed from parent components  

Governance failures are **CI blockers**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

All primitives MUST:

- Provide ARIA roles for toggle/legend elements  
- Respect reduced-motion settings for highlight animations  
- Maintain 4.5:1 contrast  
- Keep text accessible through SR-only prompts  
- Allow full keyboard control  

Accessibility regressions block CI.

---

## 📈 Telemetry Requirements

Primitives **do not** emit telemetry directly.

They MUST:

- Expose stable props/events so MapViewContainer and LayerManager can emit telemetry  
- Avoid passing any sensitive geographic info in events  
- Not modify telemetry payloads from higher components  

---

## 🧪 Testing Expectations

Each primitive MUST include:

- Unit tests (render, props, visual states)  
- Governance masking tests (sensitive sites → no disclosure)  
- A11y tests (ARIA roles, focus, labels, contrast)  
- Snapshot tests (optional for stable UI states)  
- No data-fetching or API tests  

Test locations:

~~~text
tests/unit/web/components/MapView/primitives/**
tests/integration/web/components/MapView/primitives/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; full governance, A11y, spatial ethics alignment |
| v10.4.0 | 2025-11-15 | Primitives migrated under MapView; FAIR+CARE alignment added |
| v10.3.2 | 2025-11-14 | Pre-refactor primitives stabilized |
| v10.3.1 | 2025-11-13 | Initial primitive components under old `map/` folder |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · GeoSPARQL · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>