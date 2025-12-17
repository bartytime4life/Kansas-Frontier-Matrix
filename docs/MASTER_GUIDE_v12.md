~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE: docs/MASTER_GUIDE_v12.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---
title: "Kansas Frontier Matrix — Master Guide v12 (Draft)"
path: "docs/MASTER_GUIDE_v12.md"
version: "v12.0.0-draft"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:master-guide:v12.0.0-draft"
semantic_document_id: "kfm-master-guide-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:master-guide:v12.0.0-draft"
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

# Kansas Frontier Matrix — Master Guide v12 (Draft)

## 📘 Overview

### What KFM is (one paragraph)
- A geospatial + historical knowledge system with governed data, catalogs, graph semantics, APIs, and a map/narrative UI.

### The canonical pipeline (non-negotiable ordering)
- ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### What “v12 evolution” means
- A documentation + contracts evolution that:
  - Keeps v11 artifacts stable
  - Adds explicit extension points for new data domains, AI evidence products, and narrative UX

### System inventory (index)
| System / Area | Canonical location | What it governs |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac organization per domain |
| STAC/DCAT/PROV | `data/stac/` + `docs/data/` | Catalog generation + mappings |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels, relationships, migrations |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL, transforms, catalog build, graph build |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | Map layers, Focus Mode UX, a11y |
| Story Nodes | `docs/reports/.../story_nodes/` + graph | Narrative artifacts with provenance |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability, security, governance metrics |
| Security | `.github/SECURITY.md` + `docs/security/` | Policy + technical standards |
| MCP | `mcp/` + `docs/templates/` | Experiments, model cards, SOPs |

### “Extension Matrix” (how new capabilities get added)
| Extension | Data | Catalog | Graph | API | UI | Story/Focus | Telemetry |
|---|---|---|---|---|---|---|---|
| New dataset | ✓ | ✓ | optional | optional | optional | optional | optional |
| New analysis product (e.g., evidence artifacts) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| New narrative node type | optional | optional | ✓ | ✓ | ✓ | ✓ | ✓ |
| New security gate | — | — | — | — | — | — | ✓ |

## 🗂️ Directory Layout

### Repo top-levels (expected)
~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### Documentation map
- `docs/MASTER_GUIDE_v11.md` (current baseline)
- `docs/MASTER_GUIDE_v12.md` (this draft)
- `docs/standards/` (governed standards, including KFM-MDP)
- `docs/templates/` (document + MCP templates)

## 🧭 Context

### What’s driving the next evolution
- Scaling: more domains, more evidence products, more narrative interactivity.
- Governance: stronger provenance + sovereignty enforcement as content grows.

### Key invariants
- No unsourced narrative in Focus Mode contexts.
- Provenance is first-class (STAC/DCAT/PROV and graph lineage).
- Reproducibility and deterministic pipelines.

### Future extensions (tracked here; details in subsystem docs)
- WDE-style discovery outputs (candidate sites, evidence panels, provenance-linked assets)
- More telemetry governance signals (security posture, energy/carbon for workloads)
- Expanded story node ingestion and versioning

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Data
    A[Raw Sources] --> B[ETL + Normalization]
    B --> C[STAC Items + Collections]
    C --> D[DCAT Dataset Views]
    C --> E[PROV Lineage Bundles]
  end

  C --> G[Neo4j Graph]
  G --> H[API Layer]
  H --> I[Map UI (React/MapLibre/Cesium)]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)
- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/reports/` outputs as needed)

### Domain expansion pattern
- New domains go under `data/<domain>/...`
- New domain docs go under `docs/<domain>/...` or `docs/data/<domain>/...` (choose one canonical location and link)

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy (how to document)
- Every new dataset must have:
  - STAC Collection + Item(s)
  - DCAT mapping (minimum title/description/license/keywords)
  - PROV activity for the transform that generated it

### Versioning expectations
- New versions link predecessor/successor
- Graph mirrors version lineage

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)
| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Next-evolution extension points
- (A) Data: new domain, new STAC extension profiles
- (B) AI evidence: artifacts as STAC assets, linked into Focus Mode
- (C) Graph: new entity types (e.g., candidate sites) with explicit provenance
- (D) API: new endpoints with contract tests and redaction policies
- (E) UI: new layer registry entries with provenance pointers and CARE gating

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”
- Story Nodes must carry provenance annotations and connect to graph entities.

### Focus Mode rule
- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty / confidence metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions
- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety
- Document redaction/generalization rules for any restricted locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0-draft | 2025-12-17 | Initial scaffolding | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
