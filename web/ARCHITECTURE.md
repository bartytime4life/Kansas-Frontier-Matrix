---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v10.3.2"
last_updated: "2025-11-14"
review_cycle: "Quarterly / Autonomous + FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.2/sbom.spdx.json"
manifest_ref: "../releases/v10.3.2/manifest.zip"
telemetry_ref: "../releases/v10.3.2/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v3.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture**  
`web/ARCHITECTURE.md`

**Purpose:**  
Define the *complete*, *deep-level*, FAIR+CARE-governed system architecture for the Kansas Frontier Matrix Web Platform — covering 2D/3D rendering pipelines, UI state management, Focus Mode v2.5 reasoning interfaces, STAC/DCAT metadata exploration, provenance surfaces, governance overlays, accessibility (WCAG 2.1 AA), telemetry instrumentation, and integration with the KFM API, Knowledge Graph, and Operations Control Plane.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Web Status](https://img.shields.io/badge/Web_App-Stable-success)]()
[![A11y](https://img.shields.io/badge/WCAG-2.1%20AA-blueviolet)]()

</div>

---

# 📘 Executive Summary

The **KFM Web Platform** is a **spatial-temporal reasoning interface** connecting:

- **React UI** (components, router, state, context)
- **MapLibre GL** (2D vector rendering)
- **CesiumJS** (3D terrain, deep-time earth models)
- **Focus Mode v2.5** (AI-assisted reasoning)
- **STAC/DCAT explorers**
- **Story Node visualizations**
- **Timeline engine (D3/Recharts)**
- **A11y and governance overlays**
- **Operations Control Plane integrations**  
- **Telemetry and sustainability monitoring**

It is the *public cognitive surface* of KFM.

---

# 🧬 Full System Architecture (Top-Level)

```mermaid
flowchart TD
    UI[React UI Layer<br/>Tailwind · Zustand] --> MAP[MapLibre Renderer]
    UI --> THREE[Cesium 3D Terrain Engine]
    UI --> FOCUS[FocusMode v2 5 Panel]
    UI --> STORY[StoryNode Cards]
    UI --> TL[Timeline Engine]

    MAP --> API[API Client<br/>REST · GraphQL · JSON LD]
    THREE --> API
    FOCUS --> API
    TL --> API
    STORY --> API

    API --> SVC[Backend Services<br/>FastAPI · GraphQL · GovHooks]
    SVC --> KG[Neo4j Knowledge Graph]
    SVC --> STAC[STAC DCAT Catalogs]
    SVC --> GOV[Governance Ledger]
    SVC --> OPS[Ops Plane<br/>WAL · Retry · Rollback · Hotfix · Lineage]
    SVC --> TEL[Telemetry<br/>Perf · A11y · Ethics · Energy]
```

---

# 🧱 Directory Structure (Authoritative v10.3.2)

```
web/
├── README.md
├── ARCHITECTURE.md               # This file
│
├── public/                       # Static assets
│   ├── images/
│   ├── icons/
│   ├── manifest.json
│   └── robots.txt
│
├── src/
│   ├── components/
│   │   ├── MapView/             # 2D mapping (MapLibre)
│   │   ├── CesiumView/          # 3D terrain & globe
│   │   ├── TimelineView/        # Time navigation
│   │   ├── FocusPanel/          # Focus Mode v2.5 UI
│   │   ├── StoryNode/           # Narrative unit components
│   │   ├── Governance/          # CARE labels, masking icons
│   │   ├── StacExplorer/        # Dataset browsing
│   │   ├── DcatExplorer/
│   │   ├── LayerSwitcher/
│   │   └── Shared/
│   │
│   ├── pages/
│   │   ├── Home/
│   │   ├── Explore/
│   │   ├── StoryNodes/
│   │   ├── Governance/
│   │   └── About/
│   │
│   ├── hooks/                   # useFocus • useTelemetry • useStac • useA11y
│   ├── context/
│   ├── services/                # STAC/DCAT clients · GraphQL · REST · provenance injectors
│   ├── utils/                   # Formatters, schema guards, JSON-LD generators
│   └── styles/                  # Tailwind tokens & theming
│
├── package.json
└── vite.config.ts
```

---

# 🧠 Focus Mode v2.5 – Internal Architecture

### Purpose  
Provide AI-driven narrative analysis of people, places, events, treaties, ecological changes, and Story Nodes.

### Internal Modules  
- **FocusController** – orchestrates API calls  
- **NarrativeRenderer** – high-level narrative UI  
- **ExplainabilityLayer** – SHAP overlays & Why-This explanations  
- **EthicsGuard** – CARE filters, sovereignty rules  
- **TemporalAligner** – timeline-aware story placement  
- **SpatialHighlighter** – map feature highlighting  

---

## Focus Mode v2.5 Pipeline

```mermaid
flowchart LR
    E1[User selects entity] --> E2[FocusController]
    E2 --> API[/api/focus/{id}/]
    API --> E3[Narrative Generator]
    E3 --> E4[Story Node Builder]
    E3 --> X1[Explainability Layer]
    E3 --> X2[Ethics/Care Filter]
    E4 --> MAP[MapView Highlight]
    E4 --> TL[Timeline Sync]
```

---

# 🌍 Mapping Engine — MapLibre Deep Architecture

```mermaid
flowchart TB
    LAY[STAC Layers] --> VT[Vector Tile Pipeline]
    VT --> WGL[WebGL Renderer]
    WGL --> UI[Interactive Map Controls]
    UI --> GOV[Governance Masks<br/>H3 r7 Generalization]
    WGL --> FOCUS[Focus Highlights]
```

### MapLibre Guarantees
- GPU-accelerated vector rendering  
- COG raster fallback  
- H3-masked geometries for sensitive sites  
- Colorblind-safe ramps  
- Framerate-optimized tile caching  

---

# 🌎 CesiumJS — 3D Terrain & Time Engine

```mermaid
flowchart LR
    DEM[Elevation Mesh] --> T3D[Cesium Terrain]
    HIST[Historical Rasters] --> T3D
    PRED[Predictive Futures Layers] --> T3D
    T3D --> CAM[Camera Animator<br/>Temporal Flight Path]
```

Features:
- Paleogeographic layers  
- Forecasting overlays (climate, hydrology)  
- Timeline-bound terrain morphing  
- 3D Story Node extrusion  

---

# 📊 Timeline Engine — D3 / Recharts

```mermaid
flowchart LR
    DAT[Time Series] --> SCALE[D3 Scales]
    SCALE --> RANGE[Time Domain Selector]
    RANGE --> UI[Timeline Component]
    UI --> MAPLINK[Map Sync]
```

---

# 🔧 API Client Architecture

### Principles
- TypeScript DTO schema guards  
- JSON-LD provenance injection  
- Ethics filters pre-response  
- STAC/DCAT pagination  
- GraphQL delegation for subgraph queries  
- Exponential backoff + retry logic  

```mermaid
flowchart TD
  REQ[UI Request] --> CL[API Client]
  CL --> REST[REST Layer]
  CL --> GQL[GraphQL Layer]
  REST --> PROV[Provenance Injector]
  GQL --> PROV
  PROV --> RES[UI Response]
```

---

# ♿ Accessibility (WCAG 2.1 AA+ Architecture)

Accessibility is non-negotiable and mandated by governance.

### Components:
- **ARIA roles** for map, timeline, panels  
- **A11y Tokens** (high contrast, large text, reduced motion)  
- **Keyboard-first map control**  
- **Screen-reader narrative explanations**  
- **A11y CI Gate** (Axe-core/Lighthouse ≥ 95%)

Tokens defined in:

```
docs/design/tokens/a11y-tokens.md
```

---

# 🛡️ Governance Integration Architecture

### Governance UI Features
- Consent-required data banners  
- CARE label warnings  
- License chips  
- Provenance traces (Story Node → Dataset → STAC → Source)  
- Masking for sensitive tribal/heritage areas  

Governance flow:

```mermaid
flowchart LR
    U[User Selects Layer] --> GOVF[Governance Filter]
    GOVF --> CAREF[CARE Rules Applied]
    CAREF --> UI[UI Legend + Masking]
    UI --> TEL[Telemetry Event]
```

---

# 📦 STAC/DCAT Explorer Architecture

### Features  
- STAC search  
- COG previews  
- DCAT dataset → distribution mapping  
- Keyword filters  
- Spatial/temporal slicers  
- Lineage chips  
- Provenance flow-out  

```mermaid
flowchart LR
    S1[STAC Search] --> S2[STAC Item Panel]
    S2 --> S3[Layer Preview]
    S1 --> D1[DCAT Dataset]
    D1 --> D2[DCAT Distribution]
```

---

# 📈 Telemetry & Observability Architecture

Telemetry export to:

```
../releases/v10.3.2/focus-telemetry.json
```

Metrics:
- WebVitals (LCP, FID, CLS)  
- A11y scanning  
- Layer toggles  
- AI reasoning depth  
- GPU framerate (MapLibre/Cesium)  
- Sustainability: energy (Wh) & carbon (gCO₂e)  
- Error boundary events  

---

# 🛡️ Security & Privacy Architecture

### Controls
- RBAC + OAuth2/JWT  
- Query depth limiting for GraphQL  
- CORS + strict CSP headers  
- Sanitized STAC/DCAT inputs  
- Sensitive geometry masking (H3 r7)  
- No secrets in client bundle  
- Dependency pinning  
- SBOM-backed verification at build time  

---

# 🧵 Operations Control Plane (WAL → Retry → Rollback → Hotfix → Lineage)

```mermaid
flowchart LR
    W[WAL] --> R1[Retry]
    R1 --> RB[Rollback]
    RB --> HF[Hotfix]
    HF --> LG[Lineage]
    LG --> TEST[Ops Tests]
```

The Web UI interfaces with Ops APIs for:
- Provenance display  
- Ethics warnings  
- Layer-level rollback previews  
- Hotfix result summaries  

---

# ☁️ Multi-Cloud Deployment Architecture

```mermaid
flowchart TD
    U[User] --> CDN[CDN Cache]
    CDN --> WUI[Web App Dist]
    WUI --> API[API Gateway]
    API --> KG[Neo4j Cluster]
    API --> ST[STAC Storage]
    API --> OPS[Ops Plane Services]
    API --> TL[Telemetry Export]
```

---

# 🚀 Development & Build

### Setup

```bash
npm --prefix web install
npm --prefix web run dev
```

### Build

```bash
npm --prefix web run build
```

Output served from:

```
web/dist/
```

---

# 🕰️ Version History

| Version | Date | Summary |
|--------|-------|---------|
| **v10.3.2** | 2025-11-14 | Fully rebuilt deep architecture; added rendering pipelines, governance UI, STAC/DCAT explorer model, Focus Mode v2.5 flows, accessibility architecture, multi-cloud, security, telemetry. |
| **v10.3.1** | 2025-11-13 | Upgraded v10 architecture. |
| **v10.2.2** | 2025-11-12 | Preliminary predictive overlay support. |
| **v10.0.0** | 2025-11-09 | Initial v10 web subsystem. |

---

<div align="center">

**Kansas Frontier Matrix — Web Architecture**  
Spatial Reasoning × Narrative AI × Ethical UX  
© 2025 KFM — MIT License  
[Back to Web README](README.md) · [System Architecture](../src/ARCHITECTURE.md)

</div>
