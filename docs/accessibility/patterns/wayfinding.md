---
title: "🧭 Kansas Frontier Matrix — Accessible Wayfinding, Orientation, and Spatial Navigation Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/wayfinding.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-wayfinding-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-wayfinding"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council + FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/wayfinding.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-wayfinding.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-wayfinding-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-wayfinding-v10.4.1"
semantic_document_id: "kfm-doc-a11y-wayfinding"
event_source_id: "ledger:docs/accessibility/patterns/wayfinding.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Document"
jurisdiction: "United States / Kansas"
role: "a11y-pattern-wayfinding"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next wayfinding pattern update"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Accessible Wayfinding, Orientation, and Spatial Navigation Standards**  
`docs/accessibility/patterns/wayfinding.md`

**Purpose:**  
Define accessible design patterns for spatial orientation, map navigation, and UI wayfinding across Kansas Frontier Matrix (KFM) digital environments — ensuring that movement through 2D, 3D, and narrative spaces is predictable, perceivable, and inclusive under **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE** principles.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Wayfinding refers to how users perceive structure, direction, and context across KFM’s web interfaces, spatial dashboards, and immersive Focus Mode.

Accessible wayfinding:

- Minimizes cognitive load  
- Aligns keyboard, mouse, and touch behaviors  
- Supports screen readers and other assistive technologies  
- Respects cultural and environmental sensitivities in spatial data  

---

## 🧩 Accessibility & Orientation Principles

| Principle            | Description                                                                 | WCAG / ISO Reference |
|----------------------|-----------------------------------------------------------------------------|----------------------|
| Spatial Consistency  | Maintain uniform layout across screens and maps.                           | ISO 9241-112         |
| Landmark Structure   | Use ARIA landmarks (`role="navigation"`, `role="main"`, `role="search"`).  | WCAG 2.4.1           |
| Keyboard Navigation  | All directional actions mapped to arrow keys and Tab sequences.            | WCAG 2.1.1           |
| Descriptive Cues     | Provide textual feedback for orientation changes.                          | WCAG 2.4.3           |
| Map Context Awareness| Announce map layer names and zoom levels via ARIA live regions.            | WAI-ARIA 1.2         |
| Cultural Respect     | Avoid directional metaphors implying hierarchy or dominance where harmful. | FAIR+CARE Ethics     |

---

## 🧭 Example Implementation

~~~html
<nav aria-label="Spatial Navigation">
  <button aria-label="Move north" data-direction="north">⬆️</button>
  <div>
    <button aria-label="Move west" data-direction="west">⬅️</button>
    <button aria-label="Center view" data-action="center">🎯</button>
    <button aria-label="Move east" data-direction="east">➡️</button>
  </div>
  <button aria-label="Move south" data-direction="south">⬇️</button>
</nav>

<div
  id="map-container"
  role="application"
  aria-roledescription="Interactive map"
  aria-live="polite"
>
  <p class="aria-feedback" aria-live="polite">
    Zoom level 5 — Hydrology layer active.
  </p>
</div>
~~~

### Implementation Rules

- Announce all spatial actions via an `aria-live="polite"` feedback region.  
- Coordinate keyboard interactions with pointer and touch interactions.  
- Use `aria-roledescription="map"` or `"3D scene"` for complex interactive regions.  
- Always provide textual overlays for current region name, dataset, and zoom level.  

---

## 🎨 Wayfinding Design Tokens

| Token                        | Description                              | Example   |
|-----------------------------|------------------------------------------|-----------|
| wayfinding.focus.color      | Focus outline color for directional UI   | #FFD54F   |
| wayfinding.bg.panel         | Background for navigation panels         | #263238   |
| wayfinding.text.color       | Text color for labels                    | #FAFAFA   |
| wayfinding.marker.active    | Color for active markers                 | #4FC3F7   |
| wayfinding.marker.inactive  | Color for inactive markers               | #9E9E9E   |

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Key                  | Action                         | Description                                      |
|----------------------|--------------------------------|--------------------------------------------------|
| Arrow Up             | Pan north / zoom in           | Announces new location or zoom level            |
| Arrow Down           | Pan south / zoom out          | Announces new zoom level                        |
| Arrow Left / Right   | Pan west/east                 | Announces updated region or bounding box        |
| Home                 | Reset map orientation         | Focus returns to map container and context note |
| Esc                  | Exit navigation / refocus     | Returns focus to last control                   |
| aria-roledescription | Defines map for AT users      | "Map" or "3D scene"                             |

---

## 🧾 FAIR+CARE Orientation Ethics

| Guideline              | Description                                                                |
|------------------------|----------------------------------------------------------------------------|
| Transparency           | Wayfinding cues describe spatial data without colonial or exploitative terms. |
| Consent in Spatial Layers | Cultural and sacred sites require explicit opt-in display.              |
| Representation         | Local and Indigenous place names prioritized; multilingual labels supported. |
| Data Context           | Provenance tooltips provided for geospatial datasets.                      |

### Example Tooltip

~~~html
<div class="tooltip" role="note">
  🌾 Dataset: Tribal Territories (USFS, 1840–1890). Display approved by Kaw Nation.
</div>
~~~

---

## 🧪 Testing & Validation

| Tool          | Validation Scope                                     | Output                                               |
|---------------|------------------------------------------------------|------------------------------------------------------|
| axe-core      | ARIA roles, focus, and navigation feedback           | a11y_wayfinding.json                                 |
| Lighthouse CI | Focus transitions, spatial consistency, keyboard use | lighthouse_wayfinding.json                           |
| jest-axe      | Component-level ARIA/landmark tests                  | a11y_wayfinding_components.json                      |
| Manual QA     | Screen reader spatial feedback, map orientation audit| FAIR+CARE review logs                                |

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                         |
|---------------------|-------------------------------------------------------------------------|
| Collective Benefit  | Wayfinding improves discoverability for all users and communities.     |
| Authority to Control| Communities decide which cultural sites and labels may appear and when.|
| Responsibility      | Orientation logs and telemetry are stored with full provenance.        |
| Ethics              | Spatial language and metaphors are reviewed for cultural safety.       |

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                                       |
|--------:|------------|--------------------|-----------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Updated to KFM-MDP v10.4.3; added extended metadata, clarified ARIA behavior and ethical orientation rules. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council  | Initial spatial and directional accessibility pattern for maps and Focus Mode environments.  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](../README.md)

</div>