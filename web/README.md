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
Describe the **KFM Web Platform**, including the React/MapLibre/Cesium UI, Focus Mode v2.4 interface, STAC/DCAT explorers, governance dashboards, telemetry integration, and MCP-based backend connections.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Web Status" src="https://img.shields.io/badge/Web_App-Stable-success" />

</div>


---

## 📘 Overview

The **KFM Web Platform** is the interactive visualization environment for Kansas Frontier Matrix v10.3.  
It merges:

- 2D/3D mapping  
- Predictive climate/hydrology overlays  
- Timeline interaction  
- Focus Mode v2.4 narrative reasoning  
- Governance + provenance indicators  
- STAC/DCAT dataset browsing  
- OpenTelemetry dashboards  

The system adheres to:

- **FAIR+CARE ethics**  
- **MCP-DL v6.3**  
- **WCAG 2.1 AA**  
- **STAC 1.0 + Versioning**  
- **DCAT 3.0**  
- **Diamond⁹ Ω / Crown∞Ω** certification  

---

## 🗂️ Directory Layout (Indented)

    web/
    ├── README.md                        # This document
    ├── ARCHITECTURE.md                  # Web subsystem deep dive
    │
    ├── public/                          # Safe, static assets
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
    │   ├── hooks/                       # useFocus, useStac, useTelemetry
    │   ├── context/                     # A11Y, theme, focus, auth
    │   ├── services/                    # STAC/DCAT, GraphQL, REST
    │   ├── utils/                       # Formatters, schema guards
    │   └── styles/                      # Tailwind themes + tokens
    │
    ├── package.json
    └── vite.config.ts

---

## 🧩 Web Architecture (Indented Mermaid)

    flowchart TD
      UI["UI Layer (React + Tailwind)"]
      FP["FocusPanel (AI Context v2.4)"]
      MV["MapView (MapLibre GL / Cesium 3D)"]
      TV["TimelineView (D3/Recharts)"]
      API["API Client (REST/GraphQL + JSON-LD)"]
      SAPI["FastAPI / GraphQL Services"]
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

---

## 🧠 Focus Mode v2.4

Capabilities:

- Subgraph-driven AI summaries  
- SHAP explainability highlights  
- CARE-sensitive narrative filters  
- JSON-LD provenance badges  
- Entity linking: people, places, events, documents  
- Prediction overlays linked to timeline  

API Behavior:

    GET /api/focus/{id}
    Returns: Narrative + citations + ethical flags + subgraph extract

---

## 🌍 Mapping Stack (2D/3D)

Components:

- **MapLibre GL** for map layers  
- **CesiumJS** for 3D globe & deep-time layers  
- Predictive climate overlays (2030–2100 SSP)  
- Hydrology layers (discharge, drought, flood, groundwater)  
- Accessibility features:
  - Keyboard pan/zoom  
  - High-contrast basemap tokens  
  - Reduced-motion mode  

---

## 📊 Timeline Engine

Features:

- D3-based scales  
- Brushing, density overlays, break-year markers  
- Linked view: timeline → map → focus  
- Historical + predictive ranges  
- WCAG AA accessible markers  

---

## ⚙️ API Client Layer

Behavior:

- Strong TypeScript DTOs  
- JSON-LD provenance injection  
- Pagination  
- Retry + rate limiting  
- Unified STAC/DCAT adapter  
- GraphQL federation support  

Internal services called:

    /api/focus/{id}
    /api/stac/search
    /api/events
    /graphql

---

## ♿ Accessibility (WCAG 2.1 AA)

Practices:

- ARIA landmarks  
- Screen reader metadata  
- Keyboard focus rings  
- High-contrast color tokens  
- Skip links  
- A11y CI scanning (axe-core)  
- Lighthouse ≥ 95 gate  

Tokens live in:

    docs/design/tokens/accessibility-tokens.md

---

## 🔐 Governance + Telemetry

Governance Indicators:

- CARE flags  
- License badges  
- Community consent icons  
- Masked geometry markers for protected data  

Telemetry includes:

- User interactions  
- Drift & bias  
- Accessibility metrics  
- Resource use  
- Ethics filter events  
- Logged to: `releases/<version>/focus-telemetry.json`

---

## 🚀 Running the Web App

    npm --prefix web install
    npm --prefix web run dev
    npm --prefix web run typecheck
    npm --prefix web run lint
    npm --prefix web run build

Local server:

    http://localhost:3000

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|------------|-----------------------------------------------------------|
| v10.3.1 | 2025-11-13 | Fully rule-aligned; Focus v2.4 update; streaming STAC UI. |
| v10.2.2 | 2025-11-12 | Predictive layers; governance dashboards; A11y telemetry. |
| v10.0.0 | 2025-11-09 | Initial v10 Web Platform foundation. |