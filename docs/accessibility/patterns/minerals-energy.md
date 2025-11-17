---
title: "🪨 Kansas Frontier Matrix — Accessible Minerals, Energy, and Extraction Data Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/minerals-energy.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-minerals-energy-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-minerals-energy"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Moderate"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/minerals-energy.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-minerals-energy.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-minerals-energy-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-minerals-energy-v10.4.1"
semantic_document_id: "kfm-doc-a11y-minerals-energy"
event_source_id: "ledger:docs/accessibility/patterns/minerals-energy.md"
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
role: "a11y-pattern-minerals-energy"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next minerals/energy standard update"
---

<div align="center">

# 🪨 **Kansas Frontier Matrix — Accessible Minerals, Energy, and Extraction Data Standards**  
`docs/accessibility/patterns/minerals-energy.md`

**Purpose:**  
Set accessibility, environmental ethics, and visualization standards for mineral, energy, and extraction-related datasets used within the Kansas Frontier Matrix (KFM).  
Ensure all subsurface and extraction data — including oil fields, gas wells, mining permits, and renewables — remain perceptible, governance-linked, and ethically contextualized under **FAIR+CARE** certification.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Mineral and energy data layers within KFM include:

- Oil and gas fields, wells, and pipelines  
- Mining permits, mine footprints, and reclamation sites  
- Wind, solar, and geothermal installations  
- Historical extraction activity and lease boundaries  

This pattern ensures that:

- Extraction data is accessible and meaningful to all users  
- Environmental and social impacts are clearly conveyed  
- Metadata supports FAIR+CARE governance, consent, and provenance  
- Sustainable energy and transition narratives are emphasized over extraction valorization  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── minerals-energy.md         # This file
    ├── navigation.md
    ├── network-infrastructure.md
    ├── notifications.md
    ├── parks-conservation.md
    ├── planetarium-3d.md
    ├── pollinators-ecosystem-services.md
    ├── prairie-restoration.md
    ├── rail-transit.md
    ├── soil-health.md
    ├── space-remote-sensing.md
    ├── system-controls.md
    ├── tables.md
    ├── telemetry-streams.md
    ├── testing-validation.md
    ├── tooltips.md
    ├── transportation-mobility.md
    ├── urban-planning.md
    ├── vehicle-logistics.md
    └── wildlife-tracking.md
```

---

## 🧩 Accessibility & Energy Data Principles

| Principle              | Description                                                            | Standard Reference |
|------------------------|------------------------------------------------------------------------|--------------------|
| Semantic Layer Labels  | Every well, mine, or energy site includes ARIA metadata + text labels. | WCAG 1.3.1         |
| Contrastive Mapping    | Fossil vs. renewable energy distinguished via color + pattern safely.  | WCAG 1.4.1         |
| Consent Visibility     | Extraction data shown only with regulatory and community/tribal consent.| CARE A-2           |
| Measurement Units      | Use `<abbr>` or text for units (BTU, kWh, barrels, CO2e).              | WCAG 3.1.3         |
| Temporal Traceability  | Time filters and change visualizations accessible via keyboard.        | WCAG 2.1.1         |
| Ethical Context        | Historical sites annotated with social and environmental impact notes. | FAIR+CARE Ethics   |

---

## 🧭 Example Implementation (Energy Infrastructure Map)

~~~html
<section aria-labelledby="energy-map-title" role="region" data-fair-consent="approved">
  <h2 id="energy-map-title">Kansas Energy Infrastructure — Oil, Gas, and Renewables</h2>

  <div id="energy-map" role="application" aria-roledescription="Energy dataset map">
    <button aria-label="Toggle oil wells">Oil Wells</button>
    <button aria-label="Toggle wind turbines">Wind Turbines</button>
    <button aria-label="Toggle solar farms">Solar Farms</button>
  </div>

  <p role="note">
    Data sourced from Kansas Geological Survey, EIA, and Department of Energy.  
    FAIR+CARE-reviewed for cultural and environmental sensitivity.
  </p>
</section>
~~~

### Accessibility Features

- Each layer toggle uses `aria-label` and a clear text/emoji combination.  
- `aria-roledescription="Energy dataset map"` clarifies the map’s purpose to assistive tech.  
- Consent metadata flagged on parent container (`data-fair-consent`).  
- Fossil and renewable datasets distinguished by both color and icon shape.

---

## 🎨 Design Tokens for Energy Visualization

| Token                | Description                          | Example Value |
|----------------------|--------------------------------------|---------------|
| energy.bg.color      | Background for energy maps           | #E0F2F1       |
| energy.oil.color     | Oil extraction symbols               | #5D4037       |
| energy.gas.color     | Natural gas markers                  | #90A4AE       |
| energy.wind.color    | Wind turbine symbols                 | #81C784       |
| energy.solar.color   | Solar installation polygons          | #FFB300       |
| energy.focus.color   | Focus outline for interactive items  | #FFD54F       |

---

## 🧾 FAIR+CARE Energy Metadata Schema

| Field                | Description                         | Example                                   |
|----------------------|-------------------------------------|-------------------------------------------|
| data-origin          | Custodian or data source            | "Kansas Geological Survey / DOE"          |
| data-license         | License                             | "CC-BY 4.0"                                |
| data-consent         | Public release authorization        | true                                      |
| data-sensitivity     | Environmental impact rating         | "Medium"                                  |
| data-ethics-reviewed | FAIR+CARE council validation        | true                                      |
| data-provenance      | Provenance chain                    | "KGS Oil Well Registry → KFM Dataset v10.0" |
| data-emission-profile| Emissions profile / impact measure  | "CO2e: 1.2t/MWh"                          |

### Example JSON

~~~json
{
  "data-origin": "Kansas Geological Survey / DOE",
  "data-license": "CC-BY 4.0",
  "data-consent": true,
  "data-sensitivity": "Medium",
  "data-ethics-reviewed": true,
  "data-provenance": "KGS Oil Well Registry → KFM Dataset v10.0",
  "data-emission-profile": "CO2e: 1.2t/MWh"
}
~~~

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Key / Attribute    | Function                                 | Feedback                                     |
|--------------------|------------------------------------------|----------------------------------------------|
| Tab                | Move between dataset toggles and controls| Announces focused control and state          |
| Enter              | Enable/disable dataset layer             | "Solar farms layer activated."               |
| Arrow Keys         | Pan between map regions                  | Announces location and active layer context  |
| Esc                | Exit map focus / close modals            | Restores focus to previous control           |
| aria-live="polite" | Announces dataset visibility changes     | "Gas fields layer hidden."                   |

---

## 🧪 Validation Workflows

| Tool           | Scope                                      | Output                                   |
|----------------|--------------------------------------------|------------------------------------------|
| axe-core       | Map ARIA roles, focus, and contrast        | a11y_energy.json                         |
| Lighthouse CI  | Keyboard navigation and performance audit  | lighthouse_energy.json                   |
| jest-axe       | Component-level React/Vue energy widgets   | a11y_energy_components.json              |
| Faircare Script| Consent and environmental ethics validation| energy_ethics.json                       |

Validation confirms:

- All energy toggles and map interactions are accessible.  
- Color choices respect WCAG AA and colorblind constraints.  
- Consent and sensitivity metadata are present and enforced.  

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                             |
|---------------------|-----------------------------------------------------------------------------|
| Collective Benefit  | Open visibility into energy transition and emissions supports public debate.|
| Authority to Control| Data custodians control inclusion of extraction and ownership records.     |
| Responsibility      | Provenance and emissions metadata embedded directly in dataset descriptors.|
| Ethics              | Visuals and narratives emphasize sustainability over extractive glorification.|

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                                         |
|--------:|------------|--------------------|-------------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to KFM-MDP v10.4.3; added extended metadata, clarified consent/emissions semantics, and ensured one-box-safe formatting. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council  | Created accessible minerals and energy standard with consent metadata, WCAG-compliant map design, and emission traceability.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>