---
title: "🏗️ Kansas Frontier Matrix — Accessible Urban Planning, Architecture, and Built Environment Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/urban-planning.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-urban-planning-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-urban-planning"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council + FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/urban-planning.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-urban-planning.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-urban-planning-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-urban-planning-v10.4.1"
semantic_document_id: "kfm-doc-a11y-urban-planning"
event_source_id: "ledger:docs/accessibility/patterns/urban-planning.md"
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
role: "a11y-pattern-urban-planning"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next urban-planning standard update"
---

<div align="center">

# 🏗️ **Kansas Frontier Matrix — Accessible Urban Planning, Architecture, and Built Environment Standards**  
`docs/accessibility/patterns/urban-planning.md`

**Purpose:**  
Establish inclusive, spatially aware, and ethically responsible design standards for urban planning data, architectural models, and built environment visualizations within the Kansas Frontier Matrix (KFM).  
Ensures that spatial and architectural information is accessible, semantically interpretable, and aligned with FAIR+CARE governance and WCAG 2.1 AA accessibility best practices.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Urban planning data in KFM includes:

- City zoning  
- Infrastructure networks (roads, utilities, transit)  
- Historic architecture and building footprints  
- Land-use change and development intensity  
- Cultural heritage and community assets  

This standard governs how these datasets are:

- Rendered in 2D and 3D map interfaces  
- Narrated through Focus Mode and story nodes  
- Exposed through accessible UI patterns and ARIA semantics  

It ensures that:

- Users can navigate city models with keyboard and assistive tech  
- Heritage and displacement contexts are ethically represented  
- Communities have meaningful control and visibility over their spatial narratives  

---

## 🧩 Built Environment Accessibility Principles

| Principle              | Description                                                                 | Standard Reference |
|------------------------|-----------------------------------------------------------------------------|--------------------|
| 3D Navigation          | City model viewers provide keyboard and screen-reader-compatible controls. | WCAG 2.1.1         |
| Landmark Labelling     | Buildings and regions tagged with aria-label and human-readable captions.  | WCAG 1.3.1         |
| Historical Sensitivity | Sites of renewal or displacement annotated with context and consent flags. | CARE E-1           |
| Color & Texture        | High-contrast and textured differentiation for structures and zones.       | WCAG 1.4.1         |
| Community Consent      | Heritage and tribal lands masked or generalized until authorized.          | CARE A-2           |
| Public Accessibility   | Public infrastructure data uses open formats and licenses.                 | FAIR F-1           |

---

## 🧭 Example Implementation (Urban Layer Viewer)

~~~html
<section aria-labelledby="urban-viewer-title" role="region">
  <h2 id="urban-viewer-title">Historic Urban Growth of Wichita (1870–2025)</h2>

  <div
    id="city-3d"
    role="application"
    aria-roledescription="3D urban model viewer"
  >
    <button aria-label="Toggle 1900 Building Footprints">1900</button>
    <button aria-label="Toggle 1950 Building Footprints">1950</button>
    <button aria-label="Toggle 2025 Building Footprints">2025</button>
  </div>

  <p role="note">
    Data compiled from Sanborn Fire Insurance Maps, local archives, and FAIR+CARE heritage reviews.  
    3D model simplified for performance and accessibility.
  </p>
</section>
~~~

### Implementation Notes

- Camera and layer controls must be reachable and operable via keyboard alone.  
- Each structure should have text metadata (age, function, heritage notes) available to screen readers.  
- Cultural or sensitive sites require `data-consent` flags and clear disclaimers via `aria-describedby`.  

---

## 🎨 Design Tokens for Urban Visualization

| Token                     | Description                     | Example Value |
|---------------------------|---------------------------------|---------------|
| urban.bg.color            | Scene background                | #F5F5F5       |
| urban.building.historic   | Historic structure color        | #795548       |
| urban.building.modern     | Modern building color           | #90A4AE       |
| urban.roads.color         | Road surface color              | #B0BEC5       |
| urban.park.color          | Parks and green space color     | #81C784       |
| urban.focus.color         | Focus outline for 3D interaction| #FFD54F       |

---

## 🧾 FAIR+CARE Urban Metadata Schema

| Field              | Description                 | Example                                                         |
|--------------------|-----------------------------|-----------------------------------------------------------------|
| data-origin        | Custodian / dataset author  | "Wichita Planning Department / KFM Archives"                    |
| data-license       | Open license                | "CC-BY 4.0"                                                     |
| data-consent       | Public release approval     | true                                                            |
| data-ethics-reviewed | Heritage/cultural review  | true                                                            |
| data-provenance    | Data lineage                | "Derived from 1895 Sanborn Fire Maps, updated 2025 KFM model."  |
| data-sensitivity   | Access level                | "Restricted (heritage)"                                         |

### Example Metadata JSON

~~~json
{
  "data-origin": "Wichita Planning Department / KFM Archives",
  "data-license": "CC-BY 4.0",
  "data-consent": true,
  "data-ethics-reviewed": true,
  "data-provenance": "Derived from 1895 Sanborn Fire Maps, updated 2025 KFM model.",
  "data-sensitivity": "Restricted (heritage)"
}
~~~

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Key             | Function                                              | Feedback                                      |
|-----------------|-------------------------------------------------------|-----------------------------------------------|
| Tab             | Move between toggles, legends, and metadata panels   | Visible focus outline maintained              |
| Arrow Keys      | Adjust 3D orientation / camera                       | Announces direction changes via ARIA feedback |
| Enter           | Activate layer toggle or building detail view        | "1950 building layer visible."                |
| Esc             | Exit 3D mode or metadata popover                     | Focus returns to the section heading          |
| aria-live       | Announces layer and metadata loading events          | "Historical data updated."                    |

---

## 🧪 Validation Workflows

| Tool            | Scope                                            | Output                                    |
|-----------------|--------------------------------------------------|-------------------------------------------|
| axe-core        | ARIA roles, regions, and landmark semantics      | a11y_urban.json                           |
| Lighthouse CI   | Rendering performance, contrast, and focus flows | lighthouse_urban.json                     |
| jest-axe        | Component-level accessibility testing            | a11y_urban_components.json                |
| Faircare Audit  | Contextual ethics and consent validation         | urban_audit.json                          |

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                       |
|---------------------|---------------------------------------------------------------------------------------|
| Collective Benefit  | Urban data used to empower communities with planning and heritage information.       |
| Authority to Control| Heritage custodians decide which assets appear in public viewers.                    |
| Responsibility      | All spatial datasets include provenance and ethic review references.                 |
| Ethics              | Narratives avoid glorifying displacement; prioritize inclusive storytelling.         |

---

## 🕰️ Version History

| Version | Date       | Author              | Summary                                                                                       |
|--------:|------------|---------------------|-----------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to KFM-MDP v10.4.3; added extended metadata, clarified ARIA guidance, and CI-aligned patterns. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council   | Introduced accessible urban planning and built environment standard with 3D map ARIA schema. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](../README.md)

</div>