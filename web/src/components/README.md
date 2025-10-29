---
title: "🧩 Kansas Frontier Matrix — Web UI Components (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **Web UI Components**
`web/src/components/README.md`

**Purpose:** Documents reusable user interface (UI) components for the Kansas Frontier Matrix frontend.  
Implements consistent, accessible, and FAIR+CARE-compliant interface elements for the web app’s spatial, temporal, and AI-assisted visualization features.

[![Frontend Build](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../../docs/standards/faircare-validation.md)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The `components/` directory contains the **building blocks** of the Kansas Frontier Matrix web user interface.  
Each component is modular, fully documented, and designed with accessibility, reusability, and ethical visualization in mind.

UI components adhere to:
- **MCP-DL v6.3** documentation and reproducibility standards  
- **FAIR+CARE** compliance for transparent, human-centered data interaction  
- **WCAG 2.1 AA** accessibility requirements  
- **Design tokens** defined in `web/src/styles/theme.css` and `tailwind.config.js`  

---

## 🗂️ Directory Layout

```plaintext
web/src/components/
├── README.md               # Documentation for UI components
│
├── Button.jsx              # Reusable button with variants (primary, secondary, link)
├── Modal.jsx               # Accessible modal component with keyboard support
├── Card.jsx                # Structured content container for map and entity info
├── Tooltip.jsx             # Hover/focus tooltip with contextual metadata
├── Accordion.jsx           # Expandable/collapsible content sections
├── Table.jsx               # Responsive data table for metadata display
├── Badge.jsx               # FAIR+CARE and provenance badges
├── Loader.jsx              # Animated loader/spinner for data fetch states
└── Icon.jsx                # Vector icon component for consistent UI
```

---

## ⚙️ Component Design Principles

| Principle | Implementation |
|------------|----------------|
| **Accessibility First** | All components use semantic HTML and ARIA attributes. |
| **Reusability** | Components follow atomic design—configurable props and scoped styles. |
| **Consistency** | Theming unified through TailwindCSS and shared tokens. |
| **Transparency** | Provenance, ethical indicators, and metadata displayed inline. |
| **Performance** | Lightweight and optimized for dynamic rendering with React 18. |

Each component undergoes **UI governance validation** for accessibility, metadata display, and ethical representation.

---

## 🧱 Example Components

### 🟩 Button.jsx

Reusable button component with multiple styles, keyboard focus states, and loading behavior.

```jsx
<Button
  variant="primary"
  aria-label="Open Focus Mode"
  onClick={() => openFocus(entityId)}
>
  Open Focus Mode
</Button>
```

**Props:**
| Name | Type | Description |
|------|------|--------------|
| `variant` | string | `"primary"`, `"secondary"`, or `"link"` |
| `disabled` | boolean | Toggles click interaction |
| `onClick` | function | Callback function |
| `aria-label` | string | Accessibility label for screen readers |

---

### 🧾 Modal.jsx

Accessible modal with keyboard navigation and background focus trapping.

```jsx
<Modal title="FAIR+CARE Metadata" onClose={() => setShowModal(false)}>
  <p>This dataset follows FAIR and CARE principles.</p>
</Modal>
```

Features:
- Focus trapping and ESC key close support  
- Scroll lock prevention for background  
- Themed header and footer sections  

---

### 🧭 Tooltip.jsx

Displays contextual information such as provenance or dataset confidence.

```jsx
<Tooltip content="Derived from NOAA hazard dataset (2025)">
  <span>Hazard Source</span>
</Tooltip>
```

Features:
- Keyboard focus and hover activation  
- Directional placement (top, bottom, left, right)  
- Supports HTML and markdown content  

---

### 🎖️ Badge.jsx

Renders ethical and provenance status for visual cues (FAIR, CARE, Ethics, Verified).

```jsx
<Badge type="fair">FAIR Certified</Badge>
<Badge type="care">CARE Aligned</Badge>
<Badge type="ethics">Ethically Verified</Badge>
```

Color-coded tokens reference `web/src/styles/tokens.css`.

---

## 🧠 Accessibility Compliance

All UI components are validated under automated and manual accessibility testing.

| Tool | Purpose |
|------|----------|
| **axe-core / pa11y** | Automated WCAG 2.1 AA compliance validation |
| **eslint-plugin-jsx-a11y** | Accessibility linting for React JSX |
| **Keyboard Navigation Audit** | Manual keyboard focus and interaction testing |
| **Contrast Checker** | Ensures all colors meet WCAG contrast ratios |

Accessibility reports are generated automatically by the build process and logged at:  
`reports/ui-accessibility.json`

---

## 🧩 FAIR+CARE Metadata Integration

Each component can display or embed provenance and ethical metadata, ensuring data transparency and contextual awareness.

| Metadata Type | Component | Source |
|----------------|------------|---------|
| FAIR Badge | `Badge.jsx` | `reports/fair/hazards_summary.json` |
| CARE Statement | `Modal.jsx` | `docs/standards/faircare-validation.md` |
| Provenance Tooltip | `Tooltip.jsx` | `reports/audit/ai_hazards_ledger.json` |
| Dataset License | `Card.jsx` | `data/stac/items/*.json` |

> ⚖️ These integrations guarantee that users always see the data’s origin, rights, and ethical classification at the point of use.

---

## 🧾 Governance Integration

Each component’s design and code are reviewed under the **FAIR+CARE UI Governance Workflow**:
- `.github/workflows/faircare-validate.yml` — Accessibility and ethics validation  
- `.github/workflows/governance-ledger.yml` — Provenance checksum registration  
- `.github/workflows/site.yml` — CI/CD build and deployment validation  

All UI metadata (e.g., icons, colors, licenses) is verified against:
- `docs/standards/governance/ui-governance.md`
- `schemas/telemetry/work-frontend-ui-v14.json`
- `reports/audit/ui_ethics_review.json`

---

## 🧾 Version History

| Version | Date       | Author            | Summary |
|----------|------------|-------------------|----------|
| v9.3.2   | 2025-10-28 | @kfm-ui-lab       | Initial release of UI component documentation with FAIR+CARE integration. |
| v9.3.1   | 2025-10-27 | @bartytime4life   | Added provenance tooltips and accessibility test coverage. |
| v9.3.0   | 2025-10-26 | @kfm-architecture | Established atomic design component structure. |

---

<div align="center">

**Kansas Frontier Matrix** · *Accessible UI × FAIR+CARE Governance × Ethical Visualization*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [📖 Docs Portal](../../../docs/) • [⚖️ Governance Ledger](../../../docs/standards/governance/)

</div>