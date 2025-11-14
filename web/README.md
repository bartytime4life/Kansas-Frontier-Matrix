---
title: "🌐 Kansas Frontier Matrix — Web Application & Focus Mode Platform (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../releases/v10.3.0/manifest.zip"
telemetry_ref: "../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-readme-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application & Focus Mode Platform**  
`web/README.md`

**Purpose:**  
Describe the **KFM Web Platform**, including the React/MapLibre/Cesium UI, Focus Mode v2.4 interface, STAC/DCAT explorers, governance dashboards, telemetry integration, and MCP-backed API connections.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![License](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)  
[![Web Status](https://img.shields.io/badge/Web_App-Stable-success)]()

</div>

---

## 📘 Overview

The **KFM Web Platform** is the interactive visualization environment for Kansas Frontier Matrix v10.3.  
It merges:

- 2D/3D mapping  
- Predictive climate/hydrology overlays  
- Temporal navigation (timeline)  
- Focus Mode v2.4 narrative reasoning  
- Governance + provenance indicators  
- STAC/DCAT dataset browsing  
- Telemetry and observability dashboards  

The web stack adheres to:

- **FAIR+CARE** ethics  
- **MCP-DL v6.3**  
- **WCAG 2.1 AA**  
- **STAC 1.0 + Versioning**  
- **DCAT 3.0**  

---

## 🗂️ Directory Layout

~~~~~text
web/
├── README.md                        # This document
├── ARCHITECTURE.md                  # Web subsystem deep dive
│
├── public/                          # Static assets
│   ├── images/
│   ├── icons/
│   ├── manifest.json
│   └── robots.txt
│
├── src/
│   ├── components/
│   │   ├── MapView/
│   │   ├── CesiumView/
│   │   ├── TimelineView/
│   │   ├── FocusPanel/
│   │   ├── StoryNode/
│   │   ├── LayerSwitcher/
│   │   └── Shared/
│   │
│   ├── pages/
│   │   ├── Home/
│   │   ├── Explore/
│   │   ├── Governance/
│   │   └── About/
│   │
│   ├── hooks/                       # useFocus, useStac, useTelemetry, etc.
│   ├── context/                     # A11y, theme, focus, auth
│   ├── services/                    # STAC/DCAT, GraphQL, REST API clients
│   ├── utils/                       # Formatters, schema guards, helpers
│   └── styles/                      # Tailwind themes, tokens, layout styles
│
├── package.json
└── vite.config.ts
~~~~~

---

## 🧩 Web Architecture

~~~~~mermaid
flowchart TD
  UI["UI Layer<br/>(React + Tailwind)"]
  FP["FocusPanel<br/>(AI Context v2.4)"]
  MV["MapView<br/>(MapLibre GL / Cesium 3D)"]
  TV["TimelineView<br/>(D3/Recharts)"]
  API["API Client<br/>(REST · GraphQL · JSON-LD)"]
  SAPI["Backend Services<br/>(FastAPI · GraphQL)"]
  KG["Neo4j Knowledge Graph"]
  CAT["STAC/DCAT Catalogs"]
  TEL["Telemetry & Governance Ledgers"]

  UI --> FP
  UI --> MV
  UI --> TV
  FP --> API
  MV --> API
  TV --> API
  API --> SAPI
  SAPI --> KG
  SAPI --> CAT
  SAPI --> TEL
~~~~~

---

## 🧠 Focus Mode v2.4

**Capabilities**

- Entity-centric narratives (people, places, events, Story Nodes)  
- SHAP explainability overlays and “Why this?” panels  
- CARE-sensitive narrative filters and redaction where needed  
- JSON-LD provenance badges and citation links  
- Cross-layer correlation (raster, vector, time series, text)  
- Timeline-linked predictive overlays (e.g., future drought indices)  

**API Behavior**

~~~~~text
GET /api/focus/{id}
Response: {
  narrative,
  subgraph,
  ethics_flags,
  telemetry,
  citations
}
~~~~~

---

## 🌍 Mapping Stack (2D/3D)

- **MapLibre GL** for 2D basemaps and interactive layers  
- **CesiumJS** for 3D globe, deep-time paleogeographic overlays  
- Support for:
  - Climate projections (2030–2100)  
  - Hydrology (discharge, drought, flood, groundwater)  
  - Land cover & terrain  
  - Historical maps & treaty boundaries  

**Accessibility**

- Keyboard pan/zoom  
- High-contrast color tokens  
- Reduced-motion mode  
- ARIA-compliant map controls  

---

## 📊 Timeline Engine

- D3-based scales and domain ranges  
- Brushing & zooming for time windows  
- Density overlays and epoch markers  
- Linked views: timeline → map → Focus Mode  
- Supports both historical ranges and forecast horizons  

---

## ⚙️ API Client Layer

**Responsibilities**

- Typed DTOs (TypeScript) for all REST & GraphQL responses  
- JSON-LD injection for provenance fields  
- Pagination, retry, and rate-limiting strategies  
- Unified STAC/DCAT search adapter  
- GraphQL support for flexible queries  

Representative calls:

- `/api/focus/{id}`  
- `/api/stac/search`  
- `/api/events`  
- `/graphql`  

---

## ♿ Accessibility (WCAG 2.1 AA)

**Practices**

- ARIA landmarks and roles  
- Screen reader-friendly labels and text alternatives  
- Keyboard focus states with visible rings  
- High-contrast theme tokens and color palettes  
- Skip links for main content  
- Automated A11y CI (e.g. axe-core/Lighthouse) with thresholds (≥ 95)  

Tokens are documented in:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 🔐 Governance & Telemetry

**Governance Indicators**

- CARE labels and license badges in UI  
- Masked geometries for sensitive/heritage sites  
- Dataset-level ethics summaries and links to governance records  

**Telemetry**

- User interaction events (e.g., layer toggles, focus selection)  
- A11y metrics, performance timings  
- Bias/drift indicators surfaced from backend telemetry  
- Logged to:  

```
../releases/<version>/focus-telemetry.json
```

---

## 🚀 Running the Web App

~~~~~bash
npm --prefix web install
npm --prefix web run dev       # Development server
npm --prefix web run typecheck
npm --prefix web run lint
npm --prefix web run build     # Production build
~~~~~

Local development URL:

- `http://localhost:3000`

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|--------|------|
| v10.3.1 | 2025-11-13 | Rule-aligned README; Focus Mode v2.4 details; updated telemetry references. |
| v10.2.2 | 2025-11-12 | Added predictive overlays, governance dashboards, A11y telemetry integration. |
| v10.0.0 | 2025-11-09 | Initial v10 web platform foundation (React + MapLibre + Cesium). |

---

<div align="center">

**Kansas Frontier Matrix — Web Platform**  
Spatial Narratives × Temporal Insight × Ethical AI  
© 2025 Kansas Frontier Matrix — MIT  

[Back to Master Guide](../docs/MASTER_GUIDE_v10.md) · [System Architecture](../src/ARCHITECTURE.md)

</div>
