---
title: "Tools — KFM Operational Tooling and Deployment Scaffolding"
path: "tools/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:tools:readme:v1.0.0"
semantic_document_id: "kfm-tools-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:readme:v1.0.0"
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

# Tools

## 📘 Overview

### Purpose
- Provide a canonical home for operational tooling that supports building, validating, and operating the Kansas Frontier Matrix (KFM) pipeline.
- Hold deployment-oriented scaffolding and ops glue that is intentionally *out of scope* for core architecture docs (cloud deployment specifics belong here and/or in separate ops repos).:contentReference[oaicite:3]{index=3}

### Scope
| In Scope | Out of Scope |
|---|---|
| Deployment/runbooks and environment scaffolding that *supports* the system | Core pipeline implementations (canonical home: `src/pipelines/`) |
| Wrapper scripts that orchestrate canonical subsystems (ETL/catalog/graph/API/UI) | Production API/server code (canonical home: `src/server/`) |
| CI/build helpers that call canonical validators | UI application code (canonical home: `web/`) |
| Operational utilities that are not data outputs | Derived datasets or catalog/provenance outputs (canonical homes: `data/<domain>/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`) |

### Audience
- KFM maintainers (data engineering, catalog, graph/ontology, API, UI)
- Contributors running builds locally or in CI
- Deployment/ops owners

### Definitions
- Glossary: `docs/glossary.md` (not confirmed in repo — add or update this link if the glossary lives elsewhere)

### Key artifacts (what this folder should link to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants |
| Security standards | `.github/SECURITY.md` + `docs/security/` | Security owners | Policy + technical standards (follow when adding deployment tooling) |
| Telemetry standards | `docs/telemetry/` + `schemas/telemetry/` | Telemetry owners | Observability/governance metrics (when tools emit governed telemetry) |

### Definition of done (for this README)
- [ ] Front-matter complete and `path` matches `tools/README.md`.
- [ ] Scope clearly distinguishes what belongs in `tools/` vs canonical subsystem roots.
- [ ] The “add a tool” pattern is documented and repeatable.
- [ ] No pipeline outputs are committed under `tools/` unless they are tool source/config (pipeline outputs belong in `data/**` and other canonical roots).

## 🗂️ Directory Layout

### This document
- `path`: `tools/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| **Data domains** | `data/` | Domain staging + processed data; catalog/provenance outputs |
| **Documentation** | `docs/` | Governed docs, standards, templates, reports |
| **Pipelines** | `src/pipelines/` | ETL, transforms, catalog builders |
| **Graph** | `src/graph/` | Ontology, constraints, migrations |
| **APIs** | `src/server/` | Contracted access layer (REST/GraphQL) |
| **Frontend** | `web/` | React-based UI (map + Focus Mode UX) |
| **Schemas** | `schemas/` | Machine-validated schemas/specs |
| **Tests** | `tests/` | Automated tests for contracts and behaviors |
| **Tools** | `tools/` | Operational tooling and deployment scaffolding |

### Expected file tree for this sub-area
~~~text
📁 tools/
├── 📄 README.md
└── 📁 <tool-name>/
    └── 📄 README.md
~~~

## 🧭 Context

### How this fits the canonical pipeline
KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

`tools/` supports that flow, but does not replace any canonical subsystem root.

### Constraints and invariants
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via `src/server/`.:contentReference[oaicite:4]{index=4}
- **Contracts are canonical:** schemas/specs must live in `schemas/` and API contracts must validate in CI.:contentReference[oaicite:5]{index=5}
- **Data outputs are not code:** derived datasets belong under `data/<domain>/processed/`, not under `src/` (and not under `tools/`).:contentReference[oaicite:6]{index=6}

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  T[tools/* wrappers & ops] --> P[src/pipelines/*]
  P --> C[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  C --> G[Graph<br/>Neo4j]
  G --> A[API<br/>src/server]
  A --> U[UI<br/>web]
  U --> S[Story Nodes<br/>docs/reports/story_nodes]
  S --> F[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Source | Notes |
|---|---|---|
| Tool-specific config | `tools/**` | Each tool must document required config and defaults |
| Canonical subsystem artifacts | `src/**`, `schemas/**`, `docs/**`, `data/**` | Tools should call into canonical modules and validate outputs |

### Outputs
| Output | Canonical destination | Notes |
|---|---|---|
| Catalog + provenance artifacts | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Required for datasets/evidence products |
| Derived datasets | `data/<domain>/processed/` | Never store derived datasets under `tools/` |
| Tool logs / run metadata | Determined by the owning subsystem | Prefer governed locations defined by subsystem docs; avoid inventing new roots |

## 🌐 STAC, DCAT & PROV Alignment

- STAC/DCAT/PROV are first-class and required for datasets and evidence products.:contentReference[oaicite:7]{index=7}
- Canonical global output locations:
  - STAC: `data/stac/collections/` and `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`:contentReference[oaicite:8]{index=8}

## 🧱 Architecture

### Components and contracts
| Component | Contract artifact | Notes |
|---|---|---|
| Deployment scaffolding | Runbook/README + validation steps | Must not bypass security or governance standards |
| CI/build helpers | Repeatable commands + references to canonical schemas/contracts | Should call canonical validators rather than re-implementing |
| Orchestration wrappers | CLI/Make targets + documented inputs/outputs | Must route outputs to canonical destinations |

### Extension points checklist (for future work)
When adding new tooling under `tools/`, ensure it does not break pipeline alignment:
- [ ] Data: no derived outputs committed under `tools/`; outputs land in canonical `data/**` roots.
- [ ] STAC: if generating STAC, create/validate collections + items.
- [ ] DCAT: if generating DCAT, ensure dataset metadata and license/attribution are present.
- [ ] PROV: if generating provenance, capture activities + agents.
- [ ] Graph: do not introduce UI-to-graph coupling; keep graph access behind the API boundary.
- [ ] API: if a tool depends on endpoints, link to the relevant contract docs and validation.
- [ ] UI: tools must not cause `web/` to query Neo4j directly.
- [ ] Story: if tooling affects story publication, ensure provenance/citations/validation workflows exist.
- [ ] Telemetry: if emitting governed telemetry, align with telemetry schemas and docs.

## ⚖ FAIR+CARE & Governance

### Review gates
- Follow the governance, ethics, and sovereignty references in this file’s front-matter for any tool that affects data handling, publication, or access.

### CARE / sovereignty considerations
- If tooling processes culturally sensitive content or locations, it must align with the sovereignty policy and any domain-specific redaction requirements.

### AI usage constraints
- This document permits summarization/structure extraction/translation/keyword indexing, and prohibits generating policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial `tools/` README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
