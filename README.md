---
title: "Kansas Frontier Matrix — README"
path: "Kansas-Frontier-Matrix/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:readme:v12.0.0-draft"
semantic_document_id: "kfm-readme-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:readme:v12.0.0-draft"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Kansas Frontier Matrix — README

## 📘 Overview

### Purpose
Kansas Frontier Matrix (KFM) is an open-source geospatial + historical knowledge system for exploring Kansas across time and space through an interactive map/timeline experience, with governed data catalogs, a knowledge graph, APIs, and narrative UX.

This README is the entry point for:
- Understanding what KFM is and what it is *not*.
- Finding the canonical “source of truth” docs for the pipeline, contracts, governance, and standards.
- Getting to a safe “first run” path (local + reproducible), without leaking sensitive locations or bypassing governance.

### Scope
| In Scope | Out of Scope |
|---|---|
| Project overview, canonical pipeline, repo orientation | Full ETL SOPs, full ontology spec, full API contract text |
| Pointers to governed docs & templates | Unreviewed policy, ad-hoc schema invention |
| Safe contribution entry points | Publishing sensitive site coordinates |

### Audience
- Primary: contributors (data, graph, API, UI), maintainers, researchers/educators integrating datasets
- Secondary: the public and collaborators evaluating the project’s architecture and governance posture

### Definitions
- Glossary: `docs/glossary.md`
- Terms used here: STAC, DCAT, PROV-O, Neo4j, Focus Mode, Story Node, CARE/sovereignty, ETL

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (system + pipeline “source of truth”) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering + contracts |
| Governed doc templates | `docs/templates/` | Maintainers | Universal / Story Node / API Contract Extension |
| Architecture overview | `ARCHITECTURE.md` | Maintainers | High-level technical layout |
| Contribution guide | `CONTRIBUTING.md` | Maintainers | Docs-first contribution process |
| Security policy | `SECURITY.md` | Maintainers | Sensitive data handling expectations |
| Governance (FAIR+CARE / sovereignty) | `docs/governance/` | Maintainers + reviewers | Required for sensitive domains |

### Definition of done (for this README)
- [ ] Front-matter complete + valid
- [ ] Canonical pipeline ordering stated and consistent with Master Guide
- [ ] Key repo entry points linked
- [ ] Governance + CARE/sovereignty + sensitivity constraints explicitly stated
- [ ] No claims require secrets, private endpoints, or undisclosed infrastructure

## 🗂️ Directory Layout

### This document
- `path`: `Kansas-Frontier-Matrix/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + validation shapes |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | CLI helpers, validators, dev scripts |

### Expected file tree for this sub-area
~~~text
Kansas-Frontier-Matrix/
  README.md
  ARCHITECTURE.md
  CONTRIBUTING.md
  SECURITY.md

  data/
    raw/
    work/
    processed/
    stac/

  docs/
    MASTER_GUIDE_v12.md
    templates/
      TEMPLATE__KFM_UNIVERSAL_DOC.md
      TEMPLATE__STORY_NODE_V3.md
      TEMPLATE__API_CONTRACT_EXTENSION.md
    governance/
      ROOT_GOVERNANCE.md
      ETHICS.md
      SOVEREIGNTY.md

  src/
    pipelines/
    graph/
    server/

  web/
  schemas/
  tests/
  tools/
  mcp/
~~~

## 🧭 Context

### Background
Kansas data relevant to history, ecology, hazards, and culture is dispersed across many institutions, formats, and time scales. KFM’s approach is to (1) ingest and standardize datasets, (2) catalog them with interoperable metadata, (3) connect them semantically via a knowledge graph, and (4) deliver map + narrative experiences through stable contracts.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend consumes data and semantics via **contracts/APIs** (no direct graph dependency).
- All narrative experiences must remain **evidence/provenance-linked**.
- Sensitive resources (especially archaeological/cultural) must follow governance + sovereignty rules. Do not expose or infer sensitive locations.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the minimum “first run” command set per platform? | Maintainers | TBD |
| Which datasets are public vs restricted by default? | Governance reviewers | TBD |
| Which API endpoints are public vs authenticated? | Maintainers | TBD |

### Future extensions
- New data domains (deep time, climate projections, archaeology signals, etc.) should be added through governed extension points: schemas → catalogs → graph mappings → API contracts → UI layers → Story Nodes/Focus narratives.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL: ingest + transform] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j knowledge graph]
  C --> D[APIs: REST/GraphQL]
  D --> E[React + Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## What KFM is

### Mission & vision (human-facing)
KFM is an open-source geospatial platform intended to weave Kansas’s historical, cultural, and ecological narratives together on an interactive map and timeline—supporting exploration across eras, layers, and themes.

### Interactive experience (user-facing)
KFM’s UI is designed around:
- A map interface with layered geospatial data and a temporal control (timeline/era navigation).
- Layer toggles and compositing (historical maps, boundaries, routes, environment, hazards, documents).
- “Focus Mode” patterns for exploring connected entities and evidence (delivered through governed context + provenance).

## Architecture summary (developer-facing)

### Data + metadata
- Inputs may include: scanned maps, GIS layers, tabular data, text documents, imagery.
- Outputs are standardized into open formats (e.g., GeoJSON, GeoTIFF/COG, CSV) with rich metadata.
- Catalogs use open standards: STAC/DCAT for asset discovery and PROV for lineage/provenance.

### Knowledge graph + APIs
- A Neo4j graph represents entities and relationships across time/space (places, events, documents, datasets, etc.).
- APIs abstract the graph and provide stable contracts to the UI (and other clients).

### Frontend
- A modern web UI (React + MapLibre, with optional lighter 2D mapping options) loads static assets and catalog-driven configuration.
- The UI should remain deployable as static hosting where feasible; dynamic query needs go through a minimal API layer.

## Getting started (reproducible-first)

### Prerequisites (typical)
- Git
- Docker (recommended for reproducibility)
- Node.js + Python (if developing outside containers)

### Recommended first run path
1. Read the system “source of truth”: `docs/MASTER_GUIDE_v12.md`
2. Prefer containerized execution for consistent environments.
3. Use the repo’s documented orchestration (Docker Compose and/or Makefile targets) to:
   - Fetch/ingest raw data
   - Build catalogs
   - Build/refresh the graph
   - Build and serve the web UI

> Note: exact commands are intentionally documented and versioned in the Master Guide + pipeline docs so CI and local runs stay in sync.

## Contributing

- Start with `CONTRIBUTING.md`.
- Follow documentation-first development: PRs should include source metadata for new datasets, validation steps, and governance/sensitivity review where applicable.
- Expect CI to validate catalogs/schemas, run tests, and block breaking changes.

## Governance, ethics, and sensitive data

KFM follows FAIR+CARE and explicitly includes sovereignty considerations. If you work with:
- Indigenous knowledge or oral histories
- Archaeological site indicators
- Culturally sensitive materials
- Any restricted locations

…you must follow `docs/governance/SOVEREIGNTY.md` and the repo security policy. Avoid disclosing or inferring sensitive coordinates in issues, PRs, or public outputs.

## License

This README (as a governed document) is licensed under CC-BY-4.0 (see front-matter). Repository-wide code/data licensing may be defined elsewhere (e.g., LICENSE); follow the repo’s canonical licensing files and governance docs.

## Version history
| Version | Date | Notes |
|---|---|---|
| v12.0.0-draft | 2025-12-17 | README aligned to Master Guide v12 structure + governed template |
