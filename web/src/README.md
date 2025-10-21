---
title: "🧭 Kansas Frontier Matrix — Web Frontend"
document_type: "Developer Documentation · React / MapLibre Interface"
version: "v2.0.0"
last_updated: "2025-10-22"
status: "Tier-Ω+∞ Certified · Developer Edition"
maturity: "Production"
license: ["MIT (code)","CC-BY 4.0 (docs)"]
owners: ["@kfm-web","@kfm-architecture","@kfm-accessibility","@kfm-ai","@kfm-security"]
tags: ["web","frontend","react","typescript","vite","maplibre","timeline","stac","graphql","a11y","fair","care","mcp","provenance","developer"]
alignment:
  - MCP-DL v6.3.2
  - STAC 1.0 / DCAT 2.0
  - CIDOC CRM / OWL-Time
  - FAIR / CARE
  - WCAG 2.1 AA (3.0 ready)
validation:
  ci_enforced: true
  sbom_required: true
  slsa_attestations: true
observability:
  dashboard: "https://metrics.kfm.ai/frontend"
  metrics: ["build_status","bundle_size_kb","a11y_score","artifact_verification_pct"]
preservation_policy:
  checksum_algorithm: "SHA-256"
  retention: "365 d artifacts · 90 d logs"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Web Frontend (v2.0.0 · Tier-Ω+∞ Certified)**  
`📁 /web/src/`

### *“Time · Terrain · Story — United through Data.”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Docs · MCP-DL v6.3.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.3.2-green)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## ⚡ Quick Reference

| Task | Command | Description |
|:--|:--|:--|
| 🚀 Dev Server | `pnpm run dev` | Start Vite with hot reload |
| 🧱 Build Bundle | `pnpm run build` | Production build |
| 🧪 Test & Coverage | `pnpm run test:coverage` | Jest + RTL |
| 🔍 Lint Code | `pnpm run lint` | ESLint · Prettier |
| 🗄 Validate STAC | `make stac-validate` | Schema + checksum check |

---

## 🪶 Overview
The **Kansas Frontier Matrix Web Frontend** is a **React 18 + TypeScript** SPA visualizing Kansas’s historical, ecological, and cultural data via an interactive **MapLibre GL** map, **timeline**, and **knowledge-graph interface**.

- 🗺 Unified spatio-temporal map + timeline  
- 🧭 Knowledge graph context (CIDOC CRM / OWL-Time)  
- 🧠 AI summaries with citations (Focus Mode)  
- ♿ WCAG 2.1 AA accessible UI  
- 🔄 Provenance and checksums under MCP standards  

---

## ⚙️ Architecture
```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1D3557","primaryTextColor":"#fff"}}}%%
flowchart TD
  A["React SPA<br/>(web/src)"]:::ui --> B["MapView (MapLibre GL JS)"]:::ui
  A --> C["TimelineView (Canvas + D3)"]:::ui
  A --> D["SearchBar (Graph Queries)"]:::logic
  A --> E["AI Panel (Summaries + Citations)"]:::logic
  A --> F["DetailPanel (Entity Dossiers)"]:::ui
  A --> G["LayerControls (STAC Driven)"]:::logic
  B --> H["FastAPI Backend (REST · GraphQL)"]:::logic
  H --> I["Neo4j Knowledge Graph (CIDOC CRM · OWL-Time)"]:::data
  H --> J["STAC Assets (COG · GeoJSON · Tiles)"]:::data
  I -.-> A
  J -.-> B
  classDef data fill:#1D3557,color:#fff;
  classDef logic fill:#457B9D,color:#fff;
  classDef ui fill:#A8DADC,color:#000;
```
▣ #1D3557 Data / Architecture ▣ #457B9D Logic / API ▣ #A8DADC UI / Visualization

---

## 🗂 Directory Layout
```text
web/src/
├── components/   # UI modules (Map, Timeline, Search, AI, Detail)
├── context/      # Global state providers
├── hooks/        # useMap · useTimeline · useStac · useSearch
├── styles/       # Tailwind CSS + design tokens
├── types/        # Shared TypeScript types
├── utils/        # API client · formatters · geometry · STAC parser
├── config/       # layers.json · app.config.json · vite.config.ts
├── assets/       # SVGs · icons · manifest.json
└── index.tsx     # SPA entry point
```

---

## 🧩 Core Components
| Component | Purpose | Libraries |
|:--|:--|:--|
| **MapView** | MapLibre GL base map + STAC overlays | `maplibre-gl`, React |
| **TimelineView** | Temporal brush + playback | Canvas, `d3-scale` |
| **SearchBar** | Graph search + autocomplete | REST / GraphQL |
| **DetailPanel** | Entity dossiers + provenance | `react-markdown` |
| **AI Panel** | Q&A assistant + citations | FastAPI / AI service |
| **LayerControls** | STAC layer toggles + legends | React Hooks |

---

## 🧠 Data Flow
```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1D3557","primaryTextColor":"#fff"}}}%%
flowchart LR
  A[STAC Catalog]:::data --> B[FastAPI Backend]:::logic
  B --> C[Neo4j Graph]:::data
  C --> D["React Hooks &#40;useStac / useTimeline&#41;"]:::logic
  D --> E["UI Components &#40;Map · Timeline · Panels&#41;"]:::ui
  E --> F[Telemetry / Provenance Reports]:::output

  classDef data fill:#1D3557,color:#fff;
  classDef logic fill:#457B9D,color:#fff;
  classDef ui fill:#A8DADC,color:#000;
  classDef output fill:#E63946,color:#fff;
```
▣ #1D3557 Data ▣ #457B9D Logic ▣ #A8DADC UI ▣ #E63946 Telemetry  

1. **STAC Catalog → layers.json** built via ETL.  
2. **FastAPI → Neo4j** delivers CIDOC CRM entities.  
3. **Timeline Sync** drives map + query filters.  
4. **AI Overlay** adds citations + contextual summaries.

---

## ♿ Accessibility & Responsiveness
- Tokenized color system · AA contrast verified  
- Keyboard navigation · ARIA roles · skip links  
- Responsive layout for mobile & tablet  
- Honors `prefers-reduced-motion`  
- Focus management for panels + dialogs  

---

## 🛡 Security & Privacy
- Read-only client (no mutations / PII)  
- HTTPS-only requests · CORS restricted  
- Secrets managed in GH Encrypted Secrets  
- Gitleaks runs on each PR (`security-scan.yml`)  
- STAC licenses + citations shown inline  

---

## 🧪 Testing & Coverage
```bash
pnpm run test:coverage
```
- **Goal:** ≥ 85 % coverage · 95 % a11y validation  
- Reports → `coverage/lcov-report/`  
- [![codecov](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix/branch/main/graph/badge.svg)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)

---

## 🔗 Related Documentation
- `docs/Kansas Frontier Matrix Web UI Design Document.pdf`  
- `docs/Kansas Frontier Matrix – Monorepo Repository Design.pdf`  
- `docs/File and Data Architecture for KFM.pdf`  
- `docs/Markdown Styling Guide.pdf`  

---

## 📜 FAIR / CARE Commitment
- All datasets follow FAIR principles (Findable, Accessible, Interoperable, Reusable).  
- Cultural data flagged under `data_ethics`.  
- Provenance edges (`:DERIVED_FROM`) maintained in Neo4j graph.  

---

## 🧾 Metadata & Versioning
| Field | Value |
|:--|:--|
| **Version** | v2.0.0 |
| **Codename** | *Interactivity & Provenance Upgrade* |
| **Last Updated** | 2025-10-22 |
| **Maintainers** | @kfm-web · @kfm-architecture |
| **License** | MIT (code) · CC-BY 4.0 (docs) |
| **Semantic Alignment** | STAC 1.0 · CIDOC CRM · OWL-Time · DCAT 2.0 |
| **Maturity** | Production |

---

<div align="center">

**© 2025 Kansas Frontier Matrix**  
Built under the **Master Coder Protocol (MCP-DL v6.3.2)**  

[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256%20Verified-success)]()  
[![Semantic Alignment](https://img.shields.io/badge/CIDOC CRM · OWL--Time · STAC 1.0-blue)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.3.2
MCP-TIER: Ω+∞
DOC-PATH: web/src/README.md
MCP-CERTIFIED: true
A11Y-VERIFIED: true
STAC-VALIDATED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
FAIR-CARE-COMPLIANT: true
SECURITY-SCAN-CLEAN: true
PERFORMANCE-BUDGET-P95: 2.5s
OBSERVABILITY-ACTIVE: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->
