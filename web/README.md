---
title: "🌐 Kansas Frontier Matrix — Web Application & Focus Mode Platform (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../releases/v9.7.0/manifest.zip"
telemetry_ref: "../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-readme-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application & Focus Mode Platform**
`web/README.md`

**Purpose:** Describe the modular, accessible, and FAIR+CARE-aligned **KFM Web Platform** — including Focus Mode, Data Explorer, and Governance Dashboard — with architecture, directory layout, contracts, and CI/CD touchpoints for reproducible releases.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **KFM Web Platform** is the user-facing layer for viewing **timeline + map** narratives and AI **Focus Mode** insights backed by a Neo4j knowledge graph and FastAPI/GraphQL services.  
It is **standards-first** (STAC 1.0.0, DCAT 3.0, JSON-LD, WCAG 2.1 AA) and governed by **MCP v6.3** with telemetry and immutable ledgers per release.

---

## 🗂️ Directory Layout

```
web/
├── README.md                          # This file
├── ARCHITECTURE.md                    # Web architecture specification
│
├── public/                            # Static assets (no secrets)
│   ├── images/
│   ├── icons/
│   └── manifest.json
│
├── src/                               # React + TypeScript application
│   ├── components/                    # MapView, TimelineView, FocusPanel, etc.
│   ├── pages/                         # Route-level screens (Home, Explore)
│   ├── hooks/                         # useTelemetry, useFocus, useGovernance
│   ├── context/                       # Providers (Theme, Focus, Auth)
│   ├── services/                      # REST/GraphQL clients, STAC/DCAT fetchers
│   ├── utils/                         # Formatters, schema guards, a11y helpers
│   └── styles/                        # Tailwind config, tokens, variables
│
├── package.json                       # Pinned dependencies & scripts
└── vite.config.ts                     # Vite build config (or next.config.js)
```

---

## 🧩 Web Architecture

```mermaid
flowchart TD
A["User Interface (React)"] --> B["Focus Mode (UI)"]
A --> C["MapView (MapLibre)"]
A --> D["TimelineView (D3/Recharts)"]
B --> E["API Client (REST/GraphQL)"]
C --> E
D --> E
E --> F["FastAPI/GraphQL Services"]
F --> G["Neo4j (Knowledge Graph)"]
F --> H["STAC/DCAT Catalogs"]
```

- **Focus Mode (UI):** renders server-produced summaries and subgraph results.  
- **MapView:** open-source spatial rendering with accessible controls.  
- **TimelineView:** time-aware analytics and brushing.  
- **API Client:** typed DTOs; retries, pagination, and ETag caching.

---

## 🧠 Focus Mode (AI Context Engine)

**Goal:** help users explore contextual relationships while preserving ethics and explainability.

| Aspect | Implementation |
|-------|-----------------|
| API | `GET /api/focus/{entity_id}` → subgraph + AI summary |
| Model | `focus_transformer_v1` (server inference only) |
| Explainability | SHAP/LIME-linked screens from FocusPanel |
| CARE | Gate sensitive content; show consent, attribution, and provenance |
| Telemetry | Focus interactions exported to `focus-telemetry.json` |

---

## ⚙️ Frontend Stack

| Layer | Tooling | Role |
|------|---------|------|
| Framework | React 18 + TypeScript | UI + state |
| Build | Vite (or Next) | Fast, deterministic builds |
| Styling | Tailwind CSS | Tokenized, responsive design |
| Map | MapLibre GL JS | Open geospatial rendering |
| Charts | D3 / Recharts | Density/time-series charts |
| State | React Context + lightweight store | Focus, theme, a11y |
| A11y | Semantic HTML + ARIA + Headless UI | WCAG 2.1 AA |
| Data | STAC/DCAT + GraphQL | Interoperable catalogs and entities |

---

## ⚖️ FAIR+CARE & Accessibility

- **A11y:** keyboard navigation, focus rings, alt text, skip links; contrast ≥ 4.5:1.  
- **Ethics:** CARE flags in Focus Mode; provenance chips to governance ledgers.  
- **Docs:** see `../docs/standards/ui_accessibility.md` and `../docs/standards/faircare.md`.

---

## 🧾 Contracts & Validation

| Contract | Purpose | Validator |
|---------|---------|----------|
| STAC Items/Collections | Layer discovery & metadata | `stac-validate.yml` |
| DCAT 3.0 | Catalog interop | `stac-dcat-bridge.yml` |
| API DTOs | Typed responses for UI | Schema guards in `src/services` |
| A11y Contract | Route-level checks | `accessibility_scan.yml` (Lighthouse/axe) |

---

## 🔁 CI/CD — Workflow → Artifact Mapping

| Workflow | Enforces | Artifact |
|----------|----------|---------|
| `docs-lint.yml` | Markdown/YAML/JSON conformance | `reports/self-validation/docs/lint_summary.json` |
| `build-and-deploy.yml` | Build & deploy web app | `docs/reports/telemetry/build_metrics.json` |
| `telemetry-export.yml` | Merge workflow metrics | `../releases/v9.7.0/focus-telemetry.json` |
| `codeql.yml` / `trivy.yml` | Security scanning | `reports/security/*` |

---

## ♿ Design Tokens (Accessibility-First)

| Token | Location | Standard |
|------|----------|----------|
| Colors | `docs/design/tokens/color-palette.md` | WCAG 2.1 AA |
| Typography | `docs/design/tokens/typography-system.md` | ISO 9241-210 |
| Spacing | `docs/design/tokens/spacing-grid.md` | MCP Layout |
| A11y | `docs/design/tokens/accessibility-tokens.md` | FAIR+CARE |

---

## 📊 Web Sustainability Signals

| Metric | Target | Verified By |
|-------|--------|-------------|
| Page Weight | ≤ 1.5 MB | CI |
| Accessibility | ≥ 95 (Lighthouse) | `accessibility_scan.yml` |
| Energy / Perf | Tracked per build | `docs/reports/telemetry/build_metrics.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | KFM Core Team | Upgraded and aligned: contracts, CI artifacts, a11y & ethics notes, telemetry schema. |
| v9.6.0 | 2025-11-03 | KFM Core Team | Added governance sync and Focus Mode explainability. |
| v9.5.0 | 2025-11-02 | KFM Core Team | Enhanced accessibility tokens and monitoring. |
| v9.3.2 | 2025-10-28 | KFM Core Team | Established web UI and Focus Mode interfaces. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](../docs/README.md) · [Web Architecture](ARCHITECTURE.md)

</div>