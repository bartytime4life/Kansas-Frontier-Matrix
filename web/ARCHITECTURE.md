---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../releases/v10.3.0/manifest.zip"
telemetry_ref: "../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture**  
`web/ARCHITECTURE.md`

**Purpose:**  
Define the **technical, ethical, and operational architecture** for the Kansas Frontier Matrix (KFM) Web Platform.  
The web tier implements all user-facing interaction: mapping, storytelling, exploration, governance review, and Focus Mode v2.4 AI-assisted reasoning.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **KFM Web Application** is a **React + MapLibre + CesiumJS** environment built to:

- Visualize historical, ecological, hydrologic, and predictive datasets  
- Provide an accessible and ethical interface for KFM’s knowledge graph  
- Deliver AI-assisted narratives and reasoning via Focus Mode v2.4  
- Expose STAC/DCAT catalogs, dataset metadata, and provenance chips  
- Integrate governance indicators (CARE labels, consent signals)  
- Emit telemetry for performance, ethics, accessibility, and sustainability  

This document codifies web-tier module boundaries, contracts, compliance gates, and CI/CD integration.

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
web/
├── README.md
├── ARCHITECTURE.md                # This file
│
├── public/                        # Static, non-sensitive assets
│   ├── images/
│   ├── icons/
│   ├── manifest.json
│   └── robots.txt
│
├── src/
│   ├── components/                # UI building blocks
│   │   ├── MapView/              # MapLibre (2D) + Cesium (3D)
│   │   ├── TimelineView/         # Temporal navigation
│   │   ├── FocusPanel/           # Narrative reasoning UI
│   │   ├── StoryNode/            # Cards + narrative units
│   │   ├── LayerControls/        # STAC/DCAT toggles
│   │   ├── Accessibility/        # A11y helpers + ARIA wrappers
│   │   └── Shared/               # Buttons, modals, cards
│   │
│   ├── pages/                    # Route-level containers
│   ├── hooks/                    # Telemetry, governance, focus, stac
│   ├── context/                  # Providers (A11y, Theme, Focus, Auth)
│   ├── services/                 # REST/GraphQL/STAC/DCAT clients
│   ├── utils/                    # Formatters, schema guards
│   └── styles/                   # Tailwind tokens + themes
│
├── package.json
├── vite.config.ts
└── telemetry.json                # Optional local dev telemetry
~~~~~

---

## 🧩 Web Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  UI["UI Layer<br/>(React + Tailwind)"]
  MAP["MapView<br/>(MapLibre · Cesium)"]
  TIME["TimelineView<br/>(D3 Charts)"]
  FOCUS["FocusPanel<br/>AI Context v2.4"]
  API["API Client<br/>(REST · GraphQL · JSON-LD)"]
  SVC["Backend Services<br/>(FastAPI · GraphQL)"]
  KG["Neo4j Knowledge Graph"]
  CAT["STAC/DCAT Catalogs"]
  GOV["Governance Middleware"]
  TEL["Telemetry & Ethics Logs"]

  UI --> MAP
  UI --> TIME
  UI --> FOCUS

  MAP --> API
  TIME --> API
  FOCUS --> API

  API --> SVC
  SVC --> KG
  SVC --> CAT
  SVC --> GOV
  SVC --> TEL
~~~~~

---

## 🧠 Focus Mode v2.4 (Ethical AI)

Focus Mode renders **entity-centric narratives** from the knowledge graph with explicit **FAIR+CARE protections**.

### Key Capabilities
- Narrative synthesis based on graph subtrees  
- SHAP-derived explainability chips (“Why this?”)  
- CARE filters (tribal sovereignty, cultural sensitivity)  
- JSON-LD provenance tokens  
- Predictive overlays linked to timeline context  
- Masked geometry for heritage and restricted sites  

### API Contract

~~~~~text
GET /api/focus/{id}

Returns:
  narrative: string
  subgraph: object
  explainability: array
  ethics_flags: array
  provenance: JSON-LD
  telemetry: object
~~~~~

---

## 🌍 Mapping Tier (MapLibre + Cesium)

### Supported Map Features
- 2D vector tiles, raster layers, COG rendering  
- 3D globe, historical terrain, paleoshorelines  
- Hydrology + climate + hazard overlays  
- Treaty boundaries, land patents, historical basemaps  
- Keyboard navigation, screen-reader cues, ARIA-labeled controls  

### Symbology & Legends
- Located at `docs/reports/visualization/**/legends/`  
- Map layers carry metadata from STAC Items and Story Nodes  

---

## 📊 Timeline Engine

- Temporal brushing & filtering  
- Aggregated density plots (D3/Recharts)  
- Predictive epochs (2030–2100)  
- Linked interactions with MapView & Focus Panel  
- High-contrast, keyboard-accessible time markers  

---

## ⚙️ API Client Layer

### Responsibilities
- Fully typed DTOs (TypeScript)  
- Automatic provenance injection (JSON-LD)  
- STAC/DCAT item search + pagination  
- GraphQL federation support  
- Exponential backoff + retry policies  
- Ethics-aware filtering (client-side masks)

### Key Endpoints
- `/api/stac/search`  
- `/api/events`  
- `/api/focus/{id}`  
- `/graphql`

---

## ♿ Accessibility (WCAG 2.1 AA)

Accessibility is not optional — it's a **governance requirement**.

### Enforced Practices
- ARIA navigation landmarks  
- Skip links  
- Screen-reader-friendly metadata  
- High-contrast, colorblind-safe palettes  
- Keyboard tab order + visible focus rings  
- Reduced-motion mode  
- Automated CI scanning (axe-core + Lighthouse ≥ 95)

Accessibility tokens:  
```
docs/design/tokens/accessibility-tokens.md
```

---

## 🔐 Governance + Provenance Integration

### Governance Indicators
- CARE labels  
- Heritage masking icons  
- Consent-required data banners  
- License chips + ethics warnings  
- StoryNode-to-dataset provenance chips  

### Telemetry
Captured and exported to:

```
../releases/v10.3.0/focus-telemetry.json
```

Metrics include:

- WebVitals (LCP, FID, CLS)  
- A11y violations  
- Ethics violations avoided/triggered  
- Focus Mode reasoning depth  
- Layer interaction stats  

Governance logs stored at:

```
../docs/reports/audit/web-governance-ledger.json
```

---

## 🔁 CI/CD (Web Tier)

| Workflow | Purpose | Artifact |
|----------|---------|----------|
| `docs-lint.yml` | Markdown & metadata validation | lint logs |
| `build-and-deploy.yml` | Build integrity + deployment | build metrics |
| `accessibility_scan.yml` | Lighthouse/axe CI gating | a11y reports |
| `codeql.yml` | Static analysis | SARIF |
| `trivy.yml` | CVE scans | vulnerabilities.json |
| `telemetry-export.yml` | Merges telemetry outputs | focus-telemetry.json |

Everything must pass before merge.

---

## 💾 Build, Security & Deployment

### Build System
- Vite (fast HMR, optimized bundling)  
- Node LTS  
- Deterministic lockfile  

### Security
- No secrets in client bundle  
- CSP + COOP + CORP headers at edge  
- Pinned dependencies (Dependabot)  
- SBOM: `../releases/v10.3.0/sbom.spdx.json`

### Deployment
- Static hosting (Pages/S3/CloudFront)  
- CI verification  
- Hash-based asset caching  

---

## 🧭 Integration with Backend (Indented Mermaid)

~~~~~mermaid
flowchart TD
  UI["React Application"] --> API["API Client Layer"]
  API --> SVC["FastAPI · GraphQL"]
  SVC --> KGO["Governance Middleware"]
  SVC --> KG["Neo4j Graph"]
  SVC --> STAC["STAC/DCAT Layer"]
  SVC --> LOG["Telemetry & Audit Logs"]
~~~~~

---

## 🚀 Local Development

~~~~~bash
npm --prefix web install
npm --prefix web run dev
npm --prefix web run lint
npm --prefix web run typecheck
npm --prefix web run build
~~~~~

Local URL:

```
http://localhost:3000
```

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Architecture Team | Fully updated for v10.3; ethics + telemetry integrated; diagrams corrected. |
| v10.2.2 | 2025-11-12 | Web Architecture Team | Added predictive UI, governance indicators, improved Focus Mode. |
| v10.0.0 | 2025-11-09 | KFM Core Team | Initial v10 architecture draft. |

---

<div align="center">

**Kansas Frontier Matrix — Web Application Architecture**  
Ethical UX × Explainable AI × FAIR+CARE × Standardized Metadata  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Overview](README.md) · [Master Guide](../docs/MASTER_GUIDE_v10.md)

</div>
