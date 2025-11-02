---
title: "🗺️ Kansas Frontier Matrix — Web Frontend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v9.3.3"
last_updated: "2025-11-02"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v9.3.3/sbom.spdx.json"
manifest_ref: "../releases/v9.3.3/manifest.zip"
data_contract_ref: "../docs/contracts/data-contract-v3.json"
ai_registry_ref: "../releases/v9.3.3/models.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
observability_ref: "../docs/telemetry/observability-matrix.md"
security_ref: "../docs/standards/security/web-ui-security.md"
license: "MIT"
owners: ["@kfm-web", "@kfm-design", "@kfm-accessibility"]
status: "Stable"
maturity: "Production"
tags: ["frontend", "react", "vite", "maplibre", "ai", "focus-mode", "accessibility", "fair", "care"]
alignment:
  - MCP-DL v6.4.3
  - FAIR+CARE
  - WCAG 2.1 AA / ISO 9241-210
  - Open Standards / React 18 / MapLibre GL
preservation_policy:
  retention: "frontend documentation permanent · audits biannual"
  checksum_algorithm: "SHA-256"
---

<div align="center">

# 🗺️ Kansas Frontier Matrix — **Web Frontend Overview**
`web/README.md`

**Purpose:** Provides a comprehensive architectural and operational overview of the Kansas Frontier Matrix web frontend.  
Defines the structure, technologies, and governance systems powering the interactive, FAIR+CARE-aligned public user interface for Kansas historical and environmental data.

[![Frontend Build](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../docs/standards/faircare-validation.md)  
[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix Web Application** functions as the public interface and visualization environment of the system’s knowledge base.  
Built with **React 18**, **Vite**, and **MapLibre GL**, it visualizes Kansas’s evolving frontier landscape — connecting historical, environmental, and cultural data through **AI-driven Focus Mode**, timeline navigation, and FAIR metadata alignment.

**Core Features:**
- 🌍 Interactive mapping of datasets and STAC layers  
- 🕰️ Timeline navigation and spatiotemporal browsing  
- 🧠 AI-powered **Focus Mode** contextual exploration  
- ⚖️ FAIR+CARE governance indicators embedded throughout the UI  
- ♿ Accessibility-verified components compliant with WCAG 2.1 AA  

---

## 🧩 Technology Stack

| Layer | Framework / Library | Purpose |
|--------|----------------------|----------|
| **Frontend Framework** | React 18 + Vite | UI rendering and build optimization |
| **Mapping Engine** | MapLibre GL JS | Open-source mapping, raster/vector layer rendering |
| **Data Visualization** | D3.js + HTML5 Canvas | Timeline animations and analytics charts |
| **State Management** | Redux Toolkit | Global state management for map and timeline sync |
| **Graph Data Queries** | Apollo Client (GraphQL) | Query layer for Neo4j graph and Focus Mode |
| **Styling / UI Library** | TailwindCSS + ShadCN/UI | Design tokens and theme system |
| **Accessibility Framework** | ARIA + ESLint A11y | Inclusive design and validation tools |
| **Build / Deploy** | Vite + GitHub Actions | CI/CD pipeline for validation and hosting |

---

## 🗂️ Directory Layout

```plaintext
web/
├── README.md                       # Overview and governance documentation
│
├── src/
│   ├── components/                 # Reusable UI elements (buttons, modals, forms)
│   ├── features/                   # Core app features (map, timeline, focus mode)
│   ├── hooks/                      # React hooks for data fetching and telemetry
│   ├── pages/                      # Routes: Home, Governance, About, API docs
│   ├── store/                      # Redux slices, state management
│   ├── styles/                     # Tailwind tokens and global themes
│   ├── utils/                      # Shared utilities (API, parsers, logging)
│   └── assets/                     # Local static assets (logos, map textures, fonts)
│
├── public/                         # Static resources
│   ├── index.html                  # App entry point
│   ├── favicon.ico                 # Browser icon
│   └── manifest.webmanifest        # PWA configuration
│
├── package.json                    # Project dependencies and scripts
├── vite.config.js                  # Vite build configuration
└── tailwind.config.js              # Theming and component tokens
```

---

## ⚙️ Build & Development

### 🧱 Install Dependencies
```bash
cd web
npm install
```

### 🚀 Run Development Server
```bash
npm run dev
```
Default URL: **http://localhost:5173**

### 🧾 Build for Production
```bash
npm run build
```
The compiled site is output to `/dist/` and automatically deployed by `site.yml`.

**CI/CD Validation Includes:**
- Markdown linting  
- Accessibility testing (Pa11y / Axe)  
- STAC and FAIR metadata validation  
- Provenance ledger synchronization  

---

## 🧠 Focus Mode Integration

Focus Mode bridges the frontend and AI/graph backends for contextual exploration.  
When a user selects an entity (e.g., *“Fort Larned”*), Focus Mode:
1. Fetches relevant events, documents, and people from Neo4j.  
2. Generates AI summaries through the backend transformer models.  
3. Displays linked datasets, confidence metrics, and provenance references.

**Key API Endpoints:**
- `/api/focus/{entity_id}` — Entity summaries and relationships  
- `/api/events?year=` — Temporal event aggregation  
- `/api/graph/query` — Neo4j context retrieval (GraphQL interface)

---

## ♻️ FAIR+CARE in UI

| Principle | Implementation | Validation |
|------------|----------------|-------------|
| **Findable** | Datasets linked to STAC/DCAT metadata | `stac-validate.yml` |
| **Accessible** | WCAG 2.1 AA validation and ARIA roles | `ui-validate.yml` |
| **Interoperable** | Uses GraphQL + REST APIs | `data-contract-v3.json` |
| **Reusable** | FAIR-compliant metadata and provenance popovers | `faircare-validate.yml` |
| **Collective Benefit** | Ethical AI summaries and credit attribution | `governance-ledger.yml` |

---

## 🎨 Design System & UX

Design follows **ISO 9241-210 human-centered principles** and the **MCP-DL v6.4.3** documentation philosophy.

**Core Tenets:**
- **Minimal & Modular:** Clean data-first UI for clarity and immersion.  
- **Responsive:** Optimized layouts for all screen sizes.  
- **Accessible:** Keyboard navigation, ARIA labeling, and skip links.  
- **Transparent:** Provenance and ethics metadata shown at every layer.  

Style sources:
- `web/styles/theme.css`  
- `web/tailwind.config.js`  
- `docs/design/style-guide.md`

---

## 🧩 Deployment & Governance Integration

| Workflow | Purpose | Output |
|-----------|----------|---------|
| `site.yml` | Build, test, and deploy frontend | `/dist` build + telemetry |
| `faircare-validate.yml` | Checks accessibility and licensing | `reports/fair/frontend_validation.json` |
| `governance-ledger.yml` | Records asset checksums | `reports/audit/ui_governance_ledger.json` |
| `security-scan.yml` | SBOM and dependency validation | `reports/audit/ui_sbom_scan.json` |

**Telemetry & Governance:**
- Focus Mode and usage metrics → `releases/v9.3.3/focus-telemetry.json`  
- Audit and lineage logs → `reports/audit/ui-accessibility.json`  
- Governance updates → `ROOT-GOVERNANCE.md`

---

## 🧾 Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.3.3 | 2025-11-02 | @kfm-architecture | Enhanced governance and observability integration; upgraded MCP-DL alignment. |
| v9.3.2 | 2025-10-28 | @kfm-architecture | Documented Focus Mode integration and build workflow. |
| v9.3.1 | 2025-10-27 | @bartytime4life | Added Tailwind, MapLibre, and deployment pipeline. |
| v9.3.0 | 2025-10-26 | @kfm-ui-lab | Created initial React architecture and documentation baseline. |

---

<div align="center">

**Kansas Frontier Matrix — “Where history, AI, and geography converge.”**  
*Spatial Storytelling × FAIR+CARE Governance × Open Knowledge*  
📍 `web/README.md` — Web Frontend Documentation

</div>
