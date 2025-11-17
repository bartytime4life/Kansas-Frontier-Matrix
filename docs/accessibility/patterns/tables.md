---
title: "📊 Kansas Frontier Matrix — Accessible Tables & Data Grids (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/tables.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-tables-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-tables-grids"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/tables.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-tables.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-tables-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-tables-v10.4.1"
semantic_document_id: "kfm-doc-a11y-tables"
event_source_id: "ledger:docs/accessibility/patterns/tables.md"
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
role: "a11y-pattern-tables"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next tables/grids standard update"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Accessible Tables & Data Grids**  
`docs/accessibility/patterns/tables.md`

**Purpose:**  
Establish accessible, consistent table and grid structures for data visualization, analytics dashboards, and Focus Mode interfaces — ensuring keyboard navigability, semantic clarity, and **WCAG 2.1 AA** compliance under **FAIR+CARE** ethical governance.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Tabular layouts and data grids are core to KFM’s:

- Focus Mode entity views  
- Governance and FAIR+CARE audit dashboards  
- STAC/DCAT metadata explorers  
- Telemetry and validation reports  

Accessible tables ensure that all users — including screen reader users and keyboard-only users — can:

- Understand structure and relationships  
- Navigate efficiently  
- Interact with sorting, filtering, and selection  
- Interpret data in ethical, culturally aware ways  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── tables.md                  # This file (tables & data grids pattern)
    ├── telemetry-streams.md
    ├── testing-validation.md
    ├── tooltips.md
    ├── transportation-mobility.md
    ├── urban-planning.md
    ├── vehicle-logistics.md
    └── wildlife-tracking.md
```

---

## 🧩 Accessibility Standards

| Requirement          | Description                                                 | WCAG / Standard |
|----------------------|-------------------------------------------------------------|-----------------|
| Semantic Structure   | Use `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>` properly. | WCAG 1.3.1     |
| Header Association   | Use `scope="col"` and `scope="row"` for relationships.      | WCAG 1.3.2     |
| Keyboard Navigation  | Cells navigable via keyboard in grid contexts.              | WCAG 2.1.1     |
| Focus Order          | Logical traversal matches visual reading order.             | WCAG 2.4.3     |
| Responsive Layout    | Table meaning preserved when linearized.                    | WCAG 1.3.2     |
| Summaries & Captions | Use `<caption>` and/or `aria-label` or `aria-describedby`.  | WCAG 1.3.1     |
| Sorting Indicators   | Use `aria-sort="ascending|descending|none"`.                | WAI-ARIA 1.2   |
| Cultural Context     | Locale-aware date, number, and unit formats.                | FAIR+CARE      |

---

## 🧭 Semantic Table Example

~~~html
<table aria-describedby="dataset-description">
  <caption>Kansas River Floodplain Data — 2024</caption>
  <thead>
    <tr>
      <th scope="col">Station ID</th>
      <th scope="col">Date</th>
      <th scope="col" aria-sort="descending">Discharge (m³/s)</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KFR-001</td>
      <td>2024-06-18</td>
      <td>311.4</td>
      <td>Normal</td>
    </tr>
    <tr>
      <td>KFR-002</td>
      <td>2024-06-18</td>
      <td>892.7</td>
      <td>Flood Warning</td>
    </tr>
  </tbody>
</table>
~~~

### Implementation Rules

- Always provide a `<caption>` that succinctly explains the table’s purpose.  
- Use `<th scope="col">` and `<th scope="row">` to clarify header relationships.  
- When columns are sortable, apply `aria-sort` to the active header.  
- Avoid complex spanning (`rowspan`, `colspan`) unless necessary; if used, provide `aria-describedby` for clarity.  

---

## 🧮 Data Grid Enhancements (Interactive Grids)

For highly interactive or virtualized tables (e.g., React Table, AG Grid):

### WAI-ARIA Grid Roles

| Feature           | ARIA Role        | Notes                                     |
|------------------|------------------|-------------------------------------------|
| Grid container   | `role="grid"`    | Declares an interactive data grid         |
| Column header    | `role="columnheader"` | Works with `aria-sort`                 |
| Row header       | `role="rowheader"`    | Announces row labels                    |
| Data cell        | `role="gridcell"`     | Focusable cells for keyboard traversal  |
| Selection state  | `aria-selected`       | Indicates row/column selection         |
| Live updates     | `aria-live="polite"`  | Announces refresh or changes           |

### Keyboard Mapping

- Arrow Up / Down → move between rows  
- Arrow Left / Right → move between columns  
- Home / End → start/end of row  
- Ctrl+Home / Ctrl+End → start/end of grid  
- Enter / Space → activate cell actions where applicable  

---

## 🎨 Design Tokens

| Token                  | Description                     | Example Value |
|------------------------|---------------------------------|---------------|
| table.border.color     | Line color for cell boundaries  | #E0E0E0       |
| table.header.bg        | Header row background color     | #F5F5F5       |
| table.row.focus        | Highlight for focused row       | #FFF59D       |
| table.text.color       | Default text color              | #212121       |
| a11y.focus.color       | Focus outline color             | #FFD54F       |

---

## 🧾 Ethical Display Guidelines

| Guideline           | FAIR+CARE Justification                                |
|---------------------|--------------------------------------------------------|
| Respect Sensitivity | Mask or generalize culturally sensitive data.         |
| Plain Language      | Avoid jargon in headers and cell values.              |
| Color Safety        | Never rely on color alone; provide text indicators.   |
| Data Transparency   | Use provenance attributes or tooltips for sources.    |

### Provenance Example

~~~html
<td data-provenance="USGS Kansas Station · 2024-06-18">311.4</td>
~~~

---

## 🧪 Testing & Validation

| Tool        | Validation Focus                     | Output                                  |
|-------------|--------------------------------------|-----------------------------------------|
| axe-core    | Table semantics and ARIA roles       | a11y_tables.json                        |
| jest-axe    | React/JS-based grid semantics        | a11y_grids.json                         |
| Lighthouse  | Structure, headings, and captions    | lighthouse_tables.json                  |
| Manual QA   | NVDA/VoiceOver keyboard navigation   | FAIR+CARE Council logs                  |

Tests confirm:

- Proper use of table and grid roles.  
- No keyboard traps or inaccessible cells.  
- Captions and summaries accurately describe table content.  

---

## ⚖️ FAIR+CARE Integration

| Principle           | Application                                                       |
|---------------------|-------------------------------------------------------------------|
| Collective Benefit  | Tabular data helps communities understand shared conditions.      |
| Authority to Control| Stakeholders can restrict or adjust sensitive fields.             |
| Responsibility      | Versioning and provenance logs ensure accountability.             |
| Ethics              | Table layouts avoid stigmatizing framing of communities or groups.|

---

## 🕰️ Version History

| Version | Date       | Author                  | Summary                                                                                  |
|--------:|------------|-------------------------|------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council   | Upgraded to KFM-MDP v10.4.3; added extended YAML metadata and clarified grid ARIA rules. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council  | Initial accessible tables and data grid specification, including ARIA and ethical guidance. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns](../README.md)

</div>