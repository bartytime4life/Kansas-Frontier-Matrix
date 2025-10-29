---
title: "🗺️ Kansas Frontier Matrix — Web Frontend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../releases/v9.3.2/manifest.zip"
data_contract_ref: "../docs/contracts/data-contract-v3.json"
ai_registry_ref: "../releases/v9.3.2/models.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🗺️ Kansas Frontier Matrix — **Web Frontend Overview**
`web/README.md`

**Purpose:** Documents the structure, design system, and build configuration for the Kansas Frontier Matrix web application.  
Implements an interactive, accessible, and FAIR+CARE-compliant interface connecting the Neo4j Knowledge Graph, AI/ML Focus Mode, and STAC data layers.

[![Frontend Build](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-UI%20Compliant-gold)](../docs/standards/faircare-validation.md)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix Web Application** serves as the interactive visualization and public interface for the system’s geospatial and historical knowledge base.  
Built with **React 18**, **Vite**, and **MapLibre GL**, the web app allows users to explore spatial-temporal data, activate Focus Mode, and visualize AI-driven insights about Kansas history and environment.

Key Functions:
- 🌍 Interactive **map visualization** of datasets and STAC layers  
- 🕰️ Temporal navigation with **timeline slider**  
- 🧠 AI-powered **Focus Mode** contextual exploration  
- 📜 Integrated metadata, citations, and FAIR+CARE ethics transparency  
- ♿ Accessibility-compliant and responsive UI (WCAG 2.1 AA)

---

## 🧩 Technology Stack

| Layer | Framework / Library | Purpose |
|--------|----------------------|----------|
| **Frontend Framework** | React 18 + Vite | UI components and performance optimization |
| **Mapping Engine** | MapLibre GL JS | Open-source mapping and layer rendering |
| **Data Visualization** | D3.js + Canvas | Timeline and analytics charts |
| **State Management** | Redux Toolkit | Global state synchronization |
| **Graph Queries** | Apollo Client / GraphQL | Neo4j data access and Focus Mode integration |
| **Styling** | TailwindCSS + ShadCN/UI | Design system, components, and theming |
| **Accessibility** | ARIA roles, focus states | Inclusive interaction design |
| **Build / Deploy** | Vite + GitHub Pages | Continuous integration and hosting via CI/CD |

---

## 🗂️ Directory Layout

```plaintext
web/
├── README.md                       # Documentation for web frontend
│
├── src/
│   ├── components/                 # Reusable UI components (buttons, modals, cards)
│   ├── features/                   # Application features (map, timeline, focus mode)
│   ├── hooks/                      # React hooks for data fetching and interactions
│   ├── pages/                      # Main route components (Home, About, Governance)
│   ├── store/                      # Redux slices and global state configuration
│   ├── styles/                     # Tailwind and CSS design tokens
│   ├── utils/                      # Helper functions (API clients, formatters)
│   └── assets/                     # Static assets (logos, icons, map textures)
│
├── public/                         # Public files served directly
│   ├── index.html
│   ├── favicon.ico
│   └── manifest.webmanifest
│
├── package.json                    # NPM dependencies and build scripts
├── vite.config.js                  # Vite build configuration
└── tailwind.config.js              # Design tokens and theming definitions
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
This launches the development server at `http://localhost:5173` (default).

### 🧾 Build for Production
```bash
npm run build
```
Output is generated in `/dist/` and deployed via the `site.yml` GitHub Action workflow.

---

## 🧠 Focus Mode Integration

The **Focus Mode** connects the frontend interface with the backend AI and Knowledge Graph.  
Users can click entities (e.g., a place, treaty, or person) to enter an **AI-driven contextual exploration view**.

Features include:
- Dynamic highlighting of related spatial features (MapLibre layers).  
- Timeline updates showing relevant historical events.  
- AI-generated summaries displayed in side panels.  
- Explainability metrics and provenance visualizations for transparency.  

APIs Accessed:
- `/api/focus/{entity_id}` — Retrieves related entities, documents, and summaries.  
- `/api/events?year=` — Returns event data for timeline rendering.  
- `/api/graph/query` — Runs contextual Neo4j queries for semantic exploration.

---

## 🧩 FAIR+CARE Compliance in UI

| Principle | Implementation Example |
|------------|------------------------|
| **Findable** | Indexed dataset listings linked to STAC metadata |
| **Accessible** | WCAG 2.1 AA-compliant design and alt-text for all media |
| **Interoperable** | Open APIs using REST/GraphQL standards |
| **Reusable** | FAIR metadata and provenance visible for every dataset |
| **Collective Benefit** | Supports public research and education on Kansas history |
| **Authority to Control** | Provides credit and oversight to data owners in metadata UI |
| **Responsibility** | Displays ethical review badges for datasets |
| **Ethics** | Prevents bias in Focus Mode summaries and AI visualization |

---

## 🎨 Design System & UX Principles

- **Minimal & Modular:** Focus on clean spatial storytelling through minimal design.  
- **Responsive:** Optimized for desktop, tablet, and mobile layouts.  
- **Accessible:** Every control labeled and keyboard navigable.  
- **Transparent:** Ethical and provenance data surfaced in all entity views.  
- **Consistent Branding:** Typography, icons, and map styles unified across the system.  

Color themes and component standards are defined in:
- `web/styles/theme.css`  
- `web/tailwind.config.js`  
- `docs/design/style-guide.md`

---

## 🧾 Deployment & Governance

Frontend deployments are managed automatically by the **GitHub Actions workflow** at:
`.github/workflows/site.yml`

The build process:
1. Runs pre-commit lint and accessibility checks.  
2. Builds React app using Vite.  
3. Validates static assets against FAIR+CARE accessibility metrics.  
4. Deploys the compiled `/dist` to GitHub Pages.  

**Governance & Telemetry:**  
- Logs UI telemetry to `releases/v9.3.2/focus-telemetry.json`  
- Version tracking and governance approval via `releases/v9.3.2/manifest.zip`  

---

## 🧾 Version History

| Version | Date       | Author             | Summary |
|----------|------------|--------------------|----------|
| v9.3.2   | 2025-10-28 | @kfm-architecture  | Initial documentation for web frontend and Focus Mode integration. |
| v9.3.1   | 2025-10-27 | @bartytime4life    | Added Tailwind + MapLibre configuration and deployment workflow. |
| v9.3.0   | 2025-10-26 | @kfm-ui-lab        | Established React web app base structure and design system. |

---

<div align="center">

**Kansas Frontier Matrix** · *Spatial Storytelling × Ethical AI × Open Science*  
[🌐 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [📖 Docs Portal](../docs/) • [⚖️ Governance Ledger](../docs/standards/governance/)

</div>