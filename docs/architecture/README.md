---
title: "Kansas Frontier Matrix — Architecture — README"
path: "docs/architecture/README.md"
version: "v1.1.0"
last_updated: "2026-01-19"
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

doc_uuid: "urn:kfm:doc:architecture:readme:v1.1.0"
semantic_document_id: "kfm-architecture-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:architecture:readme:v1.1.0"
commit_sha: "<filled-by-ci>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<filled-by-ci>"
---

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2b6cb0)
![Docs](https://img.shields.io/badge/docs-architecture-0ea5e9)
![Status](https://img.shields.io/badge/status-draft-f59e0b)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-22c55e)
![License](https://img.shields.io/badge/license-CC--BY--4.0-6366f1)

# 🏗️ KFM — Architecture — README

> [!IMPORTANT]
> This file is the canonical **index** for `docs/architecture/` and the home of KFM’s **do‑not‑break invariants**:
> pipeline spine ordering, contract boundaries, provenance rules, and policy-gate expectations.

## 🔗 Quick Links

**Read-first (repo spine):**
- 🧭 Master guide (system + pipeline source of truth): `../MASTER_GUIDE_v13.md` *(preferred)* / `../MASTER_GUIDE_v12.md` *(legacy if present)*
- 🧱 System overview (big picture, module boundaries): `./system_overview.md` *(if present)*
- 🧷 Policy Pack (OPA/Conftest, “fail closed” gates): `../../api/scripts/policy/README.md` *(if present)*

**Architecture set (this folder):**
- 🧩 v13 redesign blueprint (repo structure + minimum contracts): `./KFM_REDESIGN_BLUEPRINT_v13.md`
- 🗺️ Full architecture vision (end-to-end): `./KFM_VISION_FULL_ARCHITECTURE.md`
- 🛣️ Next stages blueprint (roadmap + vertical slices): `./KFM_NEXT_STAGES_BLUEPRINT.md`

**Docs-as-code (templates + standards):**
- 🧰 Templates: `../templates/`
- 📐 Standards & profiles (expected): `../standards/` *(may be partial)*

---

## 🧾 Table of Contents

- [📘 Overview](#-overview)
- [🧬 The Pipeline Spine](#-the-pipeline-spine)
- [🧷 Do-not-break Invariants](#-do-not-break-invariants)
- [🧱 Contract Boundaries](#-contract-boundaries)
- [⚖️ Policy Gates](#️-policy-gates)
- [🗂️ Directory Layout](#️-directory-layout)
- [🗺️ Diagrams](#️-diagrams)
- [🧠 Story Nodes & Focus Mode](#-story-nodes--focus-mode)
- [🧪 Validation & CI/CD](#-validation--cicd)
- [🧭 Roadmap Lanes](#-roadmap-lanes)
- [🕰️ Version History](#️-version-history)

---

## 📘 Overview

### Purpose ✅
- Provide a single navigation entry point for architecture documentation.
- Keep cross-cutting rules stable as new domains, evidence products, and narratives are added.
- Make architecture decisions auditable by linking them to contracts (schemas, APIs, templates, tests).

### Scope 🧩

| In Scope ✅ | Out of Scope 🚫 |
|---|---|
| Indexing architecture docs, ADRs, and diagrams | Implementing pipelines, APIs, UI, or graph code |
| Capturing canonical ordering + invariants | Replacing the Master Guide |
| Where new architecture artifacts belong | Authoring governance policy text *(belongs under `docs/governance/`)* |

### Audience 👥
- **Primary:** architecture maintainers + reviewers making cross-cutting decisions.
- **Secondary:** contributors working in Data Intake/ETL, Catalogs, Graph, API, UI, Story Nodes, Focus Mode, Telemetry.

### Definitions 📚
- Glossary (expected): `docs/glossary.md` *(if missing, treat as **not confirmed in repo**)*
- **ADR:** Architecture Decision Record (small, versioned decision note).
- **Contract artifact:** schemas, OpenAPI/GraphQL specs, policy rules, Story Node templates, validators.
- **Invariant:** a rule that must remain true across versions (pipeline ordering; API boundary; provenance-only Focus Mode).

---

## 🧬 The Pipeline Spine

> [!NOTE]
> KFM treats **metadata boundary artifacts** as first-class “interfaces” between stages.  
> The “evidence triplet” (STAC + DCAT + PROV) is required before data is considered published.

### Canonical ordering (must remain ordered) 🔒

1. 🧱 **Raw** → `data/raw/<domain>/` *(immutable inputs)*
2. 🧪 **Work** → `data/work/<domain>/` *(intermediate results)*
3. 📦 **Processed** → `data/processed/<domain>/` *(publishable artifacts)*
4. 🧾 **Catalog boundary artifacts** *(required)*  
   - 🛰️ STAC → `data/stac/collections/` + `data/stac/items/`  
   - 🧠 DCAT → `data/catalog/dcat/`  
   - 🧬 PROV → `data/prov/`
5. 🗄️ **Stores** *(serving + performance)* → PostGIS + tile/object storage *(implementation-specific)*
6. 🕸️ **Knowledge graph** → Neo4j *(references catalog IDs; no “mystery nodes”)*
7. 🧩 **API boundary** → contracts + redaction + authZ
8. 🗺️ **UI** → React + MapLibre (optional: Cesium)
9. 📖 **Story Nodes** → governed narrative artifacts
10. 🧠 **Focus Mode** → provenance-linked context bundles + AI assistance (policy-gated)

---

## 🧷 Do-not-break Invariants

> [!IMPORTANT]
> If you change *anything* that crosses stages (Data ↔ Catalog ↔ Graph ↔ API ↔ UI ↔ Narrative ↔ AI), you are changing architecture.
> Treat it as a contract change and document it (README + ADR + tests/policy gates).

### “Hard invariants” (always true) 🧷

| Invariant 🔒 | Why it exists | Typical enforcement ✅ |
|---|---|---|
| **Pipeline ordering** is never inverted | Prevents “orphan outputs” and hidden dependencies | Policy Pack + CI checks |
| **Evidence triplet required** (STAC+DCAT+PROV) | “Evidence-first publishing” + traceability | Validators + Policy Pack |
| **No mystery nodes** in graph | Graph must be reconstructable from catalogs | Graph ingest rules + policy checks |
| **UI never talks to Neo4j/PostGIS directly** | API is the redaction + contract boundary | Policy Pack + code review |
| **Focus Mode must cite sources or refuse** | Prevents hallucination-shaped UX | Policy gate + runtime checks |
| **Sensitivity classification is present** | Prevents accidental disclosure | Policy Pack + API redaction |
| **Append-only philosophy** | Auditability + time travel + reproducibility | PROV + DVC/versions + CI |
| **Deterministic ETL (or documented nondeterminism)** | Replayable pipelines + diffable outputs | Pipeline manifests + provenance |

### “Soft invariants” (strong defaults) 🧠
- Prefer **open standards** and interoperable artifacts (STAC/DCAT/PROV; Geo formats; JSON-LD).
- Prefer **config-driven** ETL (YAML/JSON configs + shared pipeline code).
- Prefer **contract-first** APIs (schemas first; tests; then implementation).
- Prefer **observability by default** (run IDs, metrics, audit logs, provenance stitching).

---

## 🧱 Contract Boundaries

KFM is intentionally **multi-store** and **contracted**:

- 🗄️ **PostGIS**: source-of-truth for heavy geospatial serving (fast spatial queries; tiling; transformations).
- 🕸️ **Neo4j**: semantic relationships, lineage navigation, multi-hop context.
- 🧩 **API**: the only approved gateway for UI & external clients (auth, redaction, contracts).
- 🧠 **Focus Mode**: a controlled synthesis layer that must remain evidence-linked.

> [!TIP]
> When in doubt, ask: “What is the contract artifact for this boundary?”  
> If you can’t point to one, you likely need to create or extend it.

---

## ⚖️ Policy Gates

> [!IMPORTANT]
> KFM’s philosophy is **fail closed**: if it doesn’t pass a gate, it doesn’t ship, publish, or display.

### Minimum gate set (v13 direction) ✅
- ✅ Schema validation (data + metadata)
- ✅ STAC/DCAT/PROV completeness
- ✅ License presence (no data without known license)
- ✅ Sensitivity classification present + respected
- ✅ Provenance completeness (inputs + steps declared)
- ✅ Focus Mode outputs include citations **or refuse**

### Runtime policy (OPA) 🛡️
Policy isn’t only CI: runtime enforcement may deny actions (including withholding AI answers) when rules are violated.

---

## 🗂️ Directory Layout

### This document
- 📄 `docs/architecture/README.md`

### Related repository paths (expected) 🧭

| Area | Path | What lives here |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v13.md` | System + pipeline source of truth |
| Architecture | `docs/architecture/` | Architecture docs, ADRs, diagrams |
| Templates | `docs/templates/` | Universal docs, story nodes, API contract templates |
| Standards | `docs/standards/` | Markdown protocol + profile docs *(may be partial)* |
| Pipelines | `src/pipelines/` *(or `pipelines/`)* | Deterministic ETL + catalog emitters |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence triplet boundary artifacts |
| Graph | `src/graph/` + `data/graph/` | Ontology + ingest fixtures/import artifacts |
| API boundary | `api/` *(or `src/server/`)* | Contracted access + redaction rules |
| UI | `web/` | React/Map UI + Focus Mode surfaces |
| Policy Pack | `api/scripts/policy/` | OPA/Conftest rules (CI + governance) |

### Expected file tree for `docs/architecture/` 🌲
~~~text
📁 docs/
└── 📁 architecture/
    ├── 📄 README.md                          # (this file) index + invariants
    ├── 📄 system_overview.md                 # optional; recommended
    ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md      # repo restructuring + contract minimums
    ├── 📄 KFM_VISION_FULL_ARCHITECTURE.md    # end-to-end architecture guidance
    ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md       # roadmap / next-stage plan
    ├── 📁 adr/                               # optional; recommended
    ├── 📁 diagrams/                          # optional; recommended (Mermaid sources)
    └── 📁 contracts/                         # optional; recommended (contract inventory pages)
~~~

### Optional-root rule of thumb 🧪
- ✅ **If optional roots are missing** → skip checks (no failure).
- ❌ **If optional roots exist but are invalid** → fail deterministically.

---

## 🗺️ Diagrams

### Canonical pipeline (high level) 🧬
~~~mermaid
flowchart LR
  subgraph Data[Data lifecycle]
    A[📥 data/raw] --> B[🧪 data/work]
    B --> C[📦 data/processed]
    C --> D[🛰️ STAC + 🧠 DCAT + 🧬 PROV]
  end

  D --> E[🗄️ Stores: PostGIS + tile/object storage]
  D --> F[🕸️ Neo4j Graph<br/>(references catalogs)]
  E --> G[🧩 API Layer<br/>(contracts + redaction)]
  F --> G
  G --> H[🗺️ UI: React + MapLibre<br/>(optional: Cesium)]
  H --> I[📖 Story Nodes]
  I --> J[🧠 Focus Mode<br/>(provenance-linked context bundle)]
~~~

### Optional: request flow (UI → API → Stores/Graph) 🔁
~~~mermaid
sequenceDiagram
  participant UI as UI (React/Map)
  participant API as API (contracts + redaction)
  participant GIS as PostGIS/Tile Store
  participant Graph as Neo4j
  UI->>API: Request context (entity_id, bbox, time)
  API->>Graph: Query subgraph + provenance refs
  API->>GIS: Fetch geometry/tiles/observations
  Graph-->>API: Semantic + lineage results
  GIS-->>API: Spatial results
  API-->>UI: Contracted payload + provenance pointers
~~~

### Optional: Watcher–Planner–Executor loop 🤖🧯
~~~mermaid
flowchart TD
  W[👀 Watcher<br/>detect change] --> P[🧠 Planner<br/>propose plan + diffs]
  P --> E[🛠️ Executor<br/>open PR + artifacts]
  E --> G[🧷 Gates<br/>policy + tests + review]
  G -->|pass| M[✅ Merge]
  G -->|fail| R[🧯 Reject + report]
~~~

---

## 🧠 Story Nodes & Focus Mode

### Story Nodes 📖
- Governed narrative artifacts intended for UI surfacing.
- Must include structured metadata and explicit provenance pointers.
- Should reference stable IDs (dataset IDs, entity IDs) rather than brittle URLs.

### Focus Mode 🧠
Focus Mode is “done” only when it is:
- ✅ **Evidence-linked**: every surfaced claim can be traced to a source.
- ✅ **Policy-gated**: citations required; sensitive outputs denied/redacted.
- ✅ **Context-aware**: map viewport/time filters affect retrieval prioritization.
- ✅ **Transparent**: UI should expose “why am I seeing this?” via provenance panels.

---

## 🧪 Validation & CI/CD

> [!NOTE]
> Exact commands are repo-specific. The point is the **gates**, not the tooling brand.

### Recommended doc + architecture checks ✅
- [ ] Markdown protocol check (front-matter present; required sections present)
- [ ] Link checks for `docs/architecture/*`
- [ ] Mermaid lint/render (if diagrams exist)
- [ ] Secrets scan (no tokens/keys embedded)
- [ ] If contract changed: schema + tests + docs updated + referenced here
- [ ] Policy Pack checks (pipeline ordering; evidence triplet; API boundary; provenance-first publishing)

### Example placeholders (replace with repo commands) 🧰
~~~bash
# Policy Pack (Conftest) — example only
# conftest test -p api/scripts/policy .

# Link check — example only
# python tools/check_links.py docs/architecture

# Markdown protocol validation — example only
# python tools/validate_markdown_protocol.py docs/architecture/README.md
~~~

---

## 🧭 Roadmap Lanes

These are “architecture lanes” (safe expansion directions) — not promises:

- 🧠 **Evidence artifacts as first-class datasets**  
  Simulations, OCR corpora, AI-predicted layers → treated like any other dataset: processed output + evidence triplet + graph refs.
- 🕹️ **Immersive & educational UX**  
  3D/AR modes, classroom narratives, “guided tours” built from Story Nodes.
- 🌐 **Federation-ready catalogs**  
  DCAT-friendly publishing for cross-repo discovery and “global index” interoperability.
- 🤝 **Community contribution with governance**  
  Reputation + moderation workflows; provenance required for contributed stories and data.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.0 | 2026-01-19 | Upgraded to v13-direction spine: evidence triplet, policy gates, contract boundaries, W-P-E loop, richer navigation | AI-assisted draft |
| v1.0.0 | 2025-12-27 | Initial `docs/architecture/` README scaffolding + doc index | AI-assisted draft |

---

## 🧾 Footer Refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v13.md` *(preferred)* / `docs/MASTER_GUIDE_v12.md` *(legacy)*
- v13 blueprint (draft): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision (draft): `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Next stages blueprint (draft): `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance root: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`