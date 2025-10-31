---
title: "🖥️ Kansas Frontier Matrix — Web UI Architecture (Tier-Ω+∞ Certified)"
path: "docs/architecture/web-ui-architecture.md"
version: "v2.1.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / UI & Accessibility Council"
commit_sha: "<latest-commit-hash>"
license: "MIT (code) · CC-BY 4.0 (docs)"
owners: ["@kfm-architecture","@kfm-web","@kfm-docs","@kfm-accessibility"]
maturity: "Production"
status: "Stable"
tags: ["web","architecture","frontend","react","maplibre","timeline","ui","a11y","fair","care","governance"]
sbom_ref: "../../releases/v2.1.1/sbom.spdx.json"
manifest_ref: "../../releases/v2.1.1/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/UI-GOVERNANCE.md"
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - WCAG 2.1 AA / 3.0 Draft
  - React 18 / MapLibre GL JS
  - ISO/IEC 9241 Accessibility
validation:
  frontmatter_required: ["title","version","last_updated","owners","license"]
  docs_ci_required: true
  mermaid_end_marker: "<!-- END OF MERMAID -->"
preservation_policy:
  retention: "web architecture permanent · assets 365d"
  checksum_algorithm: "SHA-256"
---

<div align="center">

# 🖥️ **Kansas Frontier Matrix — Web UI Architecture (v2.1.1 · Tier-Ω+∞ Certified)**  
`docs/architecture/web-ui-architecture.md`

**Mission:** Define the **frontend system design and governance model** of the **Kansas Frontier Matrix (KFM)** —  
a FAIR+CARE-aligned, accessible, and AI-enhanced web interface for geospatial and historical data exploration.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue?logo=markdown)](../../docs/)
[![WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-brightgreen)](../../docs/standards/accessibility.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Design%20Aligned-gold)](../../docs/standards/faircare-validation.md)
[![License: MIT · CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM Web UI** provides an interactive, map-based visualization platform for exploring Kansas datasets, historical archives, and AI-driven narratives.  
It bridges spatial and temporal dimensions — combining **MapLibre geospatial rendering**, **React-based components**, and **AI contextual summaries** in **Focus Mode**.

Each frontend component is **versioned, accessible, and governance-audited** under FAIR+CARE principles and **MCP-DL documentation standards**.

---

## 🧩 Web UI Architecture Overview

```mermaid
flowchart TD
  subgraph WEB["Frontend Layer"]
    W1["React 18 SPA"]
    W2["MapLibre GL JS (Base Maps + Layers)"]
    W3["D3.js Timeline + Chart Components"]
    W4["Focus Mode · AI Assistant Panel"]
  end

  subgraph API["Backend APIs"]
    A1["FastAPI REST Endpoints"]
    A2["GraphQL · SPARQL Queries"]
    A3["AI Reasoning API"]
  end

  subgraph DATA["Data Layer"]
    D1["STAC / DCAT Metadata"]
    D2["GeoJSON / GeoTIFF / CSV"]
    D3["Knowledge Graph Entities"]
  end

  subgraph GOV["Governance & Observability"]
    G1["FAIR+CARE Design Audit"]
    G2["Accessibility (WCAG 2.1 AA)"]
    G3["Telemetry + Provenance Logs"]
  end

  W1 --> W2 --> W3
  W3 --> W4
  W4 --> A3
  W2 --> A1
  W1 --> A2
  A1 --> D1
  A2 --> D3
  D1 --> G1
  D3 --> G2
  G3 --> W1
```
<!-- END OF MERMAID -->

---

## 🧱 Component Breakdown

| Component | Description | Framework / Library |
|:--|:--|:--|
| **Map Renderer** | Displays dynamic base maps and vector overlays. | MapLibre GL JS |
| **Timeline Component** | Enables temporal data exploration. | D3.js |
| **Focus Mode** | AI-driven contextual entity summaries and document linking. | React + REST/AI APIs |
| **Layer Manager** | Handles dataset filtering, opacity, and metadata views. | React State + Hooks |
| **Search Panel** | GraphQL-backed search for entities and datasets. | Apollo Client |
| **Accessibility Layer** | Ensures WCAG compliance and ARIA labeling. | axe-core, Lighthouse |
| **Telemetry Engine** | Captures interactions and provenance events. | OpenTelemetry |

---

## ⚙️ Frontend Data Flow

```mermaid
sequenceDiagram
  participant User
  participant WebUI
  participant API
  participant GraphDB
  participant Ledger

  User->>WebUI: Search / Navigate / Select Layer
  WebUI->>API: Fetch STAC/DCAT metadata
  API->>GraphDB: Query entities via GraphQL
  API-->>WebUI: Return metadata + features
  WebUI->>Ledger: Log action and provenance event
  Ledger-->>WebUI: Confirm record hash
```
<!-- END OF MERMAID -->

---

## 🧠 Focus Mode (AI Integration)

| Function | Description | Source |
|:--|:--|:--|
| **Entity Contextualization** | Generates summaries for people, events, or places. | `api/v1/ai/focus/` |
| **Document Linking** | Connects datasets with related reports and archives. | Knowledge Graph |
| **Explainability** | Displays reasoning chain and confidence levels. | AI Governance Ledger |
| **Bias Detection Feedback** | Highlights low-confidence results for review. | FAIR+CARE Audit Reports |

---

## ⚖️ FAIR + CARE Integration

| Principle | Implementation | Verification |
|:--|:--|:--|
| **Findable** | Searchable entities and datasets via GraphQL interface. | `/api/v1/graph/query` |
| **Accessible** | Open, WCAG 2.1 AA-compliant UI design. | Accessibility Audit |
| **Interoperable** | JSON-LD + STAC/DCAT metadata powering UI layers. | STAC Catalog Validation |
| **Reusable** | Versioned component design under MCP-DL governance. | CI/CD Provenance Reports |
| **Collective Benefit (CARE)** | Inclusive design + open civic education access. | FAIR+CARE Board Certification |

---

## 🔍 Accessibility & Internationalization

| Category | Requirement | Status |
|:--|:--|:--|
| **WCAG 2.1 AA** | All UI elements keyboard-navigable. | ✅ |
| **Contrast Ratio** | ≥ 4.5:1 for text and data overlays. | ✅ |
| **Screen Reader Support** | ARIA roles added to map/timeline components. | ✅ |
| **Localization (i18n)** | English (en), Spanish (es), Osage (osa). | ✅ |
| **Alt Text** | All imagery and icons described in metadata. | ✅ |

---

## ⚙️ CI/CD & Governance Workflows

| Workflow | Function | Output |
|:--|:--|:--|
| `ui-validate.yml` | Validates accessibility and UI standards. | `reports/validation/ui_validation.json` |
| `policy-check.yml` | Ensures component metadata and FAIR+CARE tags. | `reports/audit/policy_check.json` |
| `governance-ledger.yml` | Registers web component versions in ledger. | `data/reports/audit/ui_governance_ledger.json` |
| `docs-validate.yml` | Verifies diagrams and documentation syntax. | `reports/validation/docs_validation.json` |

---

## 🧾 Governance Metadata Example

```json
{
  "component": "FocusModePanel",
  "version": "v2.1.1",
  "owner": "@kfm-web",
  "license": "MIT",
  "faircare": {
    "accessible": true,
    "inclusive": true,
    "open_source": true
  },
  "governance": {
    "ledger_entry": "data/reports/audit/ui_governance_ledger.json",
    "checksum": "sha256:8d9a10b7...",
    "validated_at": "2025-11-16T13:00:00Z"
  }
}
```

---

## 🧩 Observability Metrics

| Metric | Description | Target | Tool |
|:--|:--|:--|:--|
| **UI Build Success** | Build completion rate per deployment. | 100% | GitHub Actions |
| **Accessibility Coverage** | WCAG 2.1 AA validation success rate. | 100% | axe-core CI |
| **Component Version Sync** | Governance ledger version match. | 100% | `governance-ledger.yml` |
| **Telemetry Uptime** | Focus Mode event capture rate. | ≥ 99% | OpenTelemetry |

---

## 🕰 Version History

| Version | Date | Author | Summary |
|:--|:--|:--|:--|
| **v2.1.1** | 2025-11-16 | @kfm-web | Standardized web UI architecture; added Focus Mode AI integration, accessibility table, and governance metadata schema. |
| v2.0.0 | 2025-10-25 | @kfm-docs | Added MapLibre and GraphQL visualization interface. |
| v1.0.0 | 2025-10-04 | @kfm-architecture | Initial web UI structure and accessibility baseline. |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*“Design Ethically. Visualize Transparently.”*  
📍 `docs/architecture/web-ui-architecture.md` — Web architecture and governance documentation for the Kansas Frontier Matrix.

</div>

