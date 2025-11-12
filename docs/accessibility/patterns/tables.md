---
title: "📊 Kansas Frontier Matrix — Accessible Tables & Data Grids (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/tables.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-tables-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Accessible Tables & Data Grids**
`docs/accessibility/patterns/tables.md`

**Purpose:**  
Establish accessible, consistent table and grid structures for **data visualization, analytics dashboards, and Focus Mode interfaces**, ensuring keyboard navigability, semantic clarity, and **WCAG 2.1 AA** compliance under **FAIR+CARE** ethical governance.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Tabular layouts and data grids are core to Kansas Frontier Matrix’s **Focus Mode**, **Governance Dashboards**, and **Dataset Validation Reports**.  
Accessible tables ensure that all users — including those using screen readers or alternative navigation — can understand, navigate, and act upon structured information ethically and efficiently.

**Use Cases**
- FAIR+CARE audit logs  
- STAC/DCAT metadata tables  
- Telemetry and validation dashboards  
- Interactive grid-based explorers  

---

## 🧩 Accessibility Standards

| Requirement | Description | WCAG / Standard |
|--------------|--------------|-----------------|
| **Semantic Structure** | Use `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>` appropriately. | WCAG 1.3.1 |
| **Header Association** | Use `scope="col"` and `scope="row"` for relationships. | WCAG 1.3.2 |
| **Keyboard Navigation** | All cells navigable via `Tab` and arrow keys in grids. | WCAG 2.1.1 |
| **Focus Order** | Logical traversal respecting visual layout. | WCAG 2.4.3 |
| **Responsive Layout** | Maintain table meaning when linearized. | WCAG 1.3.2 |
| **Summaries & Captions** | Each table must include `<caption>` or `aria-label`. | WCAG 1.3.1 |
| **Sorting Indicators** | Use `aria-sort="ascending|descending"`. | WAI-ARIA 1.2 |
| **Cultural Context** | Numeric, date, and unit formats adapt to locale. | FAIR+CARE Cultural Standards |

---

## 🧭 Semantic Example

```html
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
```

**Implementation Rules**
- Provide a `<caption>` summarizing the dataset’s content.  
- Use `<th>` for headers with `scope` attributes.  
- For sortable headers, use `aria-sort`.  
- Avoid merging cells (`rowspan`, `colspan`) unless necessary; provide `aria-describedby` for multi-level headers.  

---

## 🧮 Data Grid Enhancements

For interactive or virtualized grids (React Table, AG Grid, etc.), adopt **WAI-ARIA Grid Patterns**:

| Feature | ARIA Role | Notes |
|----------|------------|-------|
| Table container | `role="grid"` | Provides structure for keyboard control |
| Column header | `role="columnheader"` | Includes `aria-sort` attributes |
| Row header | `role="rowheader"` | Announced as row labels |
| Data cell | `role="gridcell"` | Focusable element for keyboard traversal |
| Selection | `aria-selected="true|false"` | Used for multi-row selection |
| Live updates | `aria-live="polite"` | Announces data refreshes non-disruptively |

Keyboard Mapping Example:
- `Arrow Up/Down` → Move between rows  
- `Arrow Left/Right` → Move between columns  
- `Home/End` → Jump to start or end of row  
- `Ctrl+F` → Search/filter dataset  

---

## 🎨 Design Tokens

| Token | Description | Example |
|--------|--------------|---------|
| `table.border.color` | Line color for grid cells | `#E0E0E0` |
| `table.header.bg` | Background of header row | `#F5F5F5` |
| `table.row.focus` | Highlight color for active row | `#FFF59D` |
| `table.text.color` | Default text color | `#212121` |
| `a11y.focus.color` | Focus outline | `#FFD54F` |

---

## 🧾 Ethical Display Guidelines

| Guideline | FAIR+CARE Justification |
|------------|--------------------------|
| **Respect Sensitivity** | Mask or generalize culturally restricted data. |
| **Plain Language** | Avoid jargon in column names. |
| **Color Safety** | Color-coded data must have textual equivalents. |
| **Data Transparency** | Include provenance tooltips (`data-provenance` attributes). |

Example:
```html
<td data-provenance="USGS Kansas Station 2024-06-18">311.4</td>
```

---

## 🧪 Testing & Validation

| Tool | Validation Focus | Output |
|------|------------------|--------|
| **axe-core** | Table semantics and ARIA roles | `reports/self-validation/web/a11y_tables.json` |
| **jest-axe** | Grid role testing for React | `reports/ui/a11y_grids.json` |
| **Lighthouse CI** | Caption and sort state checks | `reports/ui/lighthouse_tables.json` |
| **Manual QA** | NVDA/VoiceOver keyboard navigation | FAIR+CARE Council logs |

---

## ⚖️ FAIR+CARE Integration

| Principle | Application |
|------------|-------------|
| **Collective Benefit** | Data tables convey transparent insights for all communities. |
| **Authority to Control** | Localized views respect regional data governance. |
| **Responsibility** | Versioned updates and metadata provenance are auditable. |
| **Ethics** | Visualization avoids stigmatization or bias through presentation. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Created comprehensive accessible table and grid specification; integrated ARIA roles, token standards, and ethical display guidance. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Forms](forms.md) · [Back to A11y Patterns Index](README.md)

</div>
