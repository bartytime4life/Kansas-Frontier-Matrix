---
title: "🌾 Kansas Frontier Matrix — Accessible Agriculture, Land, and Resource Data Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/agriculture-resources.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-agriculture-resources-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "agriculture-resources-a11y"
fair_category: "F1-A1-I1-R1"
care_label: "Agriculture / Land / Resource Data"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Agriculture & Resources Working Group · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: true
provenance_chain:
  - "docs/accessibility/patterns/agriculture-resources.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E26 Physical Feature"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-agriculture-resources.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-agriculture-resources-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-agriculture-resources-v10.4.1"
semantic_document_id: "kfm-doc-a11y-agriculture-resources"
event_source_id: "ledger:docs/accessibility/patterns/agriculture-resources.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "inventing crop yields or ownership"
  - "removing consent or sensitivity flags"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Agriculture · Land · Resources"
jurisdiction: "Kansas / Tribal Nations / United States"
role: "a11y-pattern-agriculture-resources"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next agriculture-resources pattern update"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Accessible Agriculture, Land, and Resource Data Standards**  
`docs/accessibility/patterns/agriculture-resources.md`

**Purpose:**  
Define accessibility and FAIR+CARE governance standards for **agricultural, ecological, and resource management interfaces** in Kansas Frontier Matrix (KFM).  
Ensure all agricultural and land-related data — including crop reports, soil analysis, irrigation metrics, and land ownership/tenure records — are **presented ethically**, **readable by assistive technologies**, and **traceable through open metadata**.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Agriculture and land data are key layers in KFM’s environmental, historical, and economic systems.  
This standard ensures that visualizations and UIs representing:

- Crop yields and rotations  
- Soil types, fertility indices, and erosion risk  
- Irrigation zones and water allocations  
- Resource rights, land tenure, and stewardship agreements  

adhere to **FAIR+CARE**, **WCAG 2.1 AA**, and **ISO 14064** sustainability reporting requirements for accessibility and ethics.

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
└── patterns/
    ├── agriculture-resources.md      # This file
    ├── soil-health.md
    ├── agroforestry-biomass.md
    ├── water-rights (future)
    └── ...
```

---

## 🧩 Agricultural Accessibility Principles

| Principle              | Description                                                   | WCAG / FAIR+CARE Reference |
|------------------------|---------------------------------------------------------------|-----------------------------|
| Semantic Tables        | Tables use captions, scopes, and units for AT users.         | WCAG 1.3.1                  |
| Colorblind-Safe Layers | Maps & charts use patterns and safe palettes.                | WCAG 1.4.1                  |
| Unit Consistency       | Units clearly labeled (e.g., bushels/acre, acres, mm).       | ISO 80000                   |
| Geospatial Accessibility | Map controls labeled with crop, soil, and region identifiers.| WCAG 2.4.6                |
| Consent for Ownership Data | Private or tribal land info masked without consent.      | CARE A-2                    |
| Sustainability Context | Surface emissions, inputs, and water use in summaries.       | ISO 14064 / FAIR R-1        |

---

## 🧭 Example Implementation (Crop Yield Visualization)

```html
<section aria-labelledby="agri-title" role="region" data-fair-consent="approved">
  <h2 id="agri-title">Kansas Wheat Yield Trends (1980–2025)</h2>

  <table aria-describedby="table-description">
    <caption>Annual Wheat Yields by County</caption>
    <thead>
      <tr>
        <th scope="col">County</th>
        <th scope="col">Year</th>
        <th scope="col">Yield (bushels/acre)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Sumner</td>
        <td>2024</td>
        <td>43.8</td>
      </tr>
      <tr>
        <td>Ellis</td>
        <td>2024</td>
        <td>39.1</td>
      </tr>
    </tbody>
  </table>

  <p id="table-description">
    Data derived from USDA NASS and state agricultural reports.  
    FAIR+CARE-reviewed for data privacy and ownership compliance.
  </p>
</section>
```

### Accessibility Notes

- Always include a `<caption>` and `aria-describedby` for context.  
- Use `<th scope="col">` and `<th scope="row">` as appropriate.  
- Mask or generalize ownership and tribal land details unless consent and governance protocols allow explicit display.

---

## 🎨 Design Tokens

| Token               | Description                            | Example Value |
|---------------------|----------------------------------------|---------------|
| `agri.bg.color`     | Table/chart background                 | `#FAFAF5`     |
| `agri.text.color`   | Text color                             | `#212121`     |
| `agri.chart.green`  | Crop yield series color                | `#4CAF50`     |
| `agri.chart.orange` | Drought/depletion series color         | `#FFB300`     |
| `agri.focus.color`  | Keyboard focus outline                 | `#FFD54F`     |

Tokens must be defined and validated in `web/src/theme/tokens.json` and mapped to both light and dark modes.

---

## 🧾 FAIR+CARE Agricultural Metadata Schema

```json
{
  "data-origin": "USDA NASS",
  "data-custodian": "Kansas Dept. of Agriculture",
  "data-fair-consent": true,
  "data-license": "CC-BY 4.0",
  "data-sensitivity": "Medium",
  "data-ethics-reviewed": true,
  "data-provenance": "County-level yield statistics 1980–2025; extracted 2025-10-12",
  "data-units": "bushels/acre",
  "land-ownership-masked": true
}
```

Required elements:

- Origin and custodian  
- Consent and license fields  
- Sensitivity classification  
- Provenance, including extraction dates and transformations  
- Explicit recording of masking/aggregation for ownership or tribal data  

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Key / Attribute    | Behavior                              | Description                                |
|--------------------|----------------------------------------|--------------------------------------------|
| `Tab`              | Navigate between data regions & filters| Focus ordered by semantic importance       |
| `Arrow Keys`       | Move across table/grid cells           | Maintain logical reading order             |
| `Enter`            | Toggle filters or expand regional info | Triggers chart or table update             |
| `Esc`              | Close detail views, return to overview | Prevent user from getting “trapped”        |
| `aria-live="polite"` | Announce live updates to summaries   | Recommended for streaming ag feeds         |

---

## 🧪 Testing & Validation Workflows

| Tool           | Scope                                          | Output                                       |
|----------------|------------------------------------------------|----------------------------------------------|
| **axe-core**   | Tables, forms, and ARIA for ag dashboards      | `a11y_agriculture.json`                     |
| **Lighthouse** | Chart color contrast & keyboard flows          | `lighthouse_agriculture.json`               |
| **jest-axe**   | Component-level React accessibility tests      | `a11y_agriculture_components.json`          |
| **Faircare Script** | Consent, bias, and narrative framing audit| `agriculture_audit.json`                    |

Validation must show:

- Correct table semantics and accessible filters.  
- No color-only encodings for drought or fertility statuses.  
- FAIR+CARE compliance for ownership and tribal land data representation.

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| Collective Benefit  | Data supports sustainable agriculture and community decision-making.           |
| Authority to Control| Custodians and land stewards control visibility of sensitive land attributes.  |
| Responsibility      | All visualizations attach FAIR metadata and consent context.                   |
| Ethics              | Agricultural narratives and metrics vetted for neutrality and consent-aware framing.|

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                                          |
|--------:|------------|--------------------|--------------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | FAIR+CARE Council  | Upgraded for KFM-MDP v10.4.3; added extended YAML, masking flags, and enhanced ethics checks.   |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council  | Initial agriculture & land resource accessibility standard with FAIR+CARE metadata schema.       |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>