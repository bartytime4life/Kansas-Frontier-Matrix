---
title: "🧱 Kansas Frontier Matrix — Web Source Code (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧱 Kansas Frontier Matrix — **Web Source Code Overview**
`web/src/README.md`

**Purpose:** Documents the structure, logic, and integration framework of the Kansas Frontier Matrix frontend source code.  
Implements the core architecture for UI components, Focus Mode AI visualization, and data binding across the Knowledge Graph and STAC catalog.

[![Frontend Build](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../docs/standards/faircare-validation.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The `web/src/` directory contains all **source code** for the Kansas Frontier Matrix web application.  
It powers the user interface, data visualization, and interaction logic that link historical and environmental datasets into an integrated, ethical, and AI-driven experience.

This layer connects to:
- The **FastAPI backend** for data queries and Focus Mode intelligence  
- The **Neo4j Knowledge Graph** for semantic relationships  
- The **STAC catalog** for geospatial datasets  
- The **FAIR+CARE governance** metadata for provenance and ethical assurance  

---

## 🗂️ Directory Layout

```plaintext
web/src/
├── README.md                     # Documentation for source code structure
│
├── components/                   # Reusable UI components
│   ├── Button.jsx
│   ├── Modal.jsx
│   ├── Card.jsx
│   └── Tooltip.jsx
│
├── features/                     # Feature-specific modules (map, timeline, focus mode)
│   ├── map/
│   │   ├── MapView.jsx
│   │   ├── LayerControls.jsx
│   │   └── LegendPanel.jsx
│   ├── timeline/
│   │   ├── TimelineView.jsx
│   │   ├── TimeSlider.jsx
│   │   └── EventMarkers.jsx
│   ├── focus/
│   │   ├── FocusPanel.jsx
│   │   ├── EntitySummary.jsx
│   │   └── ExplainabilityWidget.jsx
│   └── governance/
│       ├── LicenseNotice.jsx
│       ├── ProvenancePanel.jsx
│       └── FairCareBadge.jsx
│
├── hooks/                        # Custom React hooks for data and UI logic
│   ├── useMapData.js
│   ├── useTimeline.js
│   ├── useFocusMode.js
│   └── useTelemetry.js
│
├── pages/                        # Top-level route components
│   ├── Home.jsx
│   ├── About.jsx
│   ├── Focus.jsx
│   └── Governance.jsx
│
├── store/                        # Redux state management configuration
│   ├── index.js
│   ├── mapSlice.js
│   ├── timelineSlice.js
│   ├── focusSlice.js
│   └── telemetrySlice.js
│
├── styles/                       # Design system and Tailwind overrides
│   ├── theme.css
│   ├── tokens.css
│   └── typography.css
│
├── utils/                        # Helper functions and API clients
│   ├── api.js
│   ├── formatters.js
│   ├── governance.js
│   └── telemetry.js
│
└── assets/                       # Local static assets (icons, banners)
    ├── icons/
    │   ├── map.svg
    │   ├── clock.svg
    │   └── ai.svg
    └── banners/
        └── kfm_banner.webp
```

---

## 🧠 Core Concepts

### 🔗 **Data Binding**
Frontend components fetch and render data dynamically from backend APIs using REST or GraphQL.

| Data Source | Access Method | Example |
|--------------|----------------|----------|
| **Neo4j Graph** | GraphQL Query | `useFocusMode()` retrieves linked entities and relationships. |
| **STAC Catalog** | REST API | `useMapData()` loads GeoJSON hazard layers. |
| **FAIR+CARE Metadata** | JSON-LD | `governance.js` attaches ethical metadata to entity popups. |

### 🗺️ **Map & Timeline Synchronization**
The **MapView** and **TimelineView** modules are interconnected:
- Selecting an event on the timeline highlights the corresponding map layer.  
- Panning the map adjusts visible events within the selected geographic bounds.  
- Real-time telemetry logs user interactions to support reproducibility.

### 🧭 **Focus Mode**
The **FocusPanel** and **EntitySummary** components render AI-generated summaries and provenance data.  
Explainability tools (e.g., SHAP, LIME visualizations) are embedded within `ExplainabilityWidget.jsx`.

### ⚙️ **Governance Display**
Governance data is surfaced contextually through:
- Provenance chains displayed in `ProvenancePanel.jsx`.  
- FAIR+CARE badges in `FairCareBadge.jsx`.  
- Licensing transparency in `LicenseNotice.jsx`.

---

## 🧩 Data Flow

```mermaid
flowchart TD
A[User Interaction · Map / Timeline] --> B[React State (Redux Store)]
B --> C[API Service · /api/focus / /api/events / /api/stac]
C --> D[Data Adapters · JSON → Component Props]
D --> E[UI Components Render Visualization]
E --> F[Telemetry Hook · Log Actions + Context]
F --> G[Governance System · FAIR+CARE Ledger Update]
```

Each data cycle maintains full provenance visibility and logs actions to the **telemetry schema**:  
`schemas/telemetry/work-frontend-ui-v14.json`.

---

## ⚙️ Development Workflow

### 🧱 Start Local Development
```bash
cd web
npm install
npm run dev
```
The app runs at `http://localhost:5173` (default port for Vite).

### 🧪 Run Lint and Accessibility Checks
```bash
npm run lint
npm run a11y
```
Linting enforces MCP-DL Markdown conventions and accessibility rules (WCAG 2.1 AA).

### 🚀 Build for Production
```bash
npm run build
```
The output is optimized and validated by `.github/workflows/site.yml`.

---

## 🧠 Focus Mode AI Integration

Focus Mode modules communicate directly with the backend AI reasoning system to display:
- Entity-linked historical summaries  
- Event correlation visualizations  
- Confidence and bias metrics  
- Provenance visualizations (CIDOC CRM relationships)  

Telemetry output:  
`releases/v9.3.2/focus-telemetry.json` → logged with user and system context for reproducibility.

---

## 🧩 FAIR+CARE Compliance

| Principle | Implementation |
|------------|----------------|
| **Findable** | Datasets and entities include clickable metadata linking to STAC. |
| **Accessible** | Open, responsive, and WCAG-compliant design. |
| **Interoperable** | Uses GraphQL and JSON-LD schemas for all data transfers. |
| **Reusable** | Code and documentation licensed openly under MIT/CC-BY. |
| **Collective Benefit** | Promotes ethical storytelling and historical data reuse. |
| **Authority to Control** | Displays attribution and source licensing inline. |
| **Responsibility** | All UI features validated under FAIR+CARE audits. |
| **Ethics** | Ensures sensitive or restricted data is clearly labeled. |

---

## 🧾 Governance Integration

Frontend code is linked to governance through:
- `docs/standards/governance/` — Ethical UI practices  
- `data/stac/` — Dataset metadata and STAC validation  
- `reports/audit/ui_ethics_review.json` — Accessibility and ethical review outcomes  
- `schemas/telemetry/work-frontend-ui-v14.json` — Telemetry schema for governance tracking  

---

## 🧾 Version History

| Version | Date       | Author             | Summary |
|----------|------------|--------------------|----------|
| v9.3.2   | 2025-10-28 | @kfm-ui-lab        | Added detailed source architecture and FAIR+CARE integration documentation. |
| v9.3.1   | 2025-10-27 | @bartytime4life    | Linked frontend telemetry schema and governance integration. |
| v9.3.0   | 2025-10-26 | @kfm-architecture  | Established base directory and component hierarchy documentation. |

---

<div align="center">

**Kansas Frontier Matrix** · *Human-Centered Visualization × Ethical AI × Provenance-Driven Design*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../docs/) • [⚖️ Governance Ledger](../../docs/standards/governance/)

</div>