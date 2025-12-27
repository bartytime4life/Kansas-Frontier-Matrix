---
title: "KFM Standards Index"
path: "docs/standards/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:standards:readme:v1.0.0"
semantic_document_id: "kfm-standards-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:standards:readme:v1.0.0"
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

# `docs/standards/` — KFM governed standards

This directory is the canonical home for **KFM standards, protocols, and profiles** that keep the platform consistent across the full pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.**

> **Important:** Some existing module footers link to `docs/standards/INDEX.md` (legacy).  
> Prefer linking to `docs/standards/README.md` going forward. If `INDEX.md` exists, it should be treated as an alias/redirect stub.

---

## 📘 Overview

### Purpose

- Provide a **single index** for the standards that govern how KFM data, metadata, and documentation are produced and validated.
- Clarify what is **normative** (must follow) vs. what is **advisory** (recommended patterns).
- Make “contract-first” expectations discoverable: what must be **versioned**, **validated**, and **reviewed**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Documentation protocol (KFM-MDP), templates usage rules, link hygiene | Domain documentation (belongs under `data/<domain>/` or `docs/<area>/`) |
| Repository structure standards (where artifacts must live) | Implementation details of every pipeline (belongs under `src/` + subsystem docs) |
| Catalog profiles for STAC/DCAT/PROV | Raw datasets themselves (belongs under `data/raw/`) |
| Graph/ontology governance (labels/edges, ingestion invariants) | UI/UX copy and feature specs (belongs under `web/` + `docs/design/`) |
| FAIR+CARE and sovereignty standards as they affect publication | Private operational runbooks and secrets (never in repo) |

### Audience

- **Primary:** maintainers, reviewers, and contributors touching governed artifacts (data, catalogs, graph, API, UI, story nodes).
- **Secondary:** downstream consumers who need to understand how KFM guarantees provenance, ethics, and reproducibility.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this index:
  - **Standard:** a governed rule set for how artifacts are shaped, named, stored, and reviewed.
  - **Protocol:** a normative process or format that is expected to be enforced (by CI, tooling, or review).
  - **Profile:** a KFM-scoped alignment to an external standard (e.g., STAC 1.0, DCAT 3, W3C PROV-O).
  - **Contract:** a machine-validated schema/spec that producers and consumers agree on (often paired with schemas under `schemas/`).

### Standards index

| Standard / Guide | Type | Governs | Pipeline stage(s) | Repo status |
|---|---|---|---|---|
| `./KFM_MARKDOWN_WORK_PROTOCOL.md` | Protocol (work) | How to write governed Markdown (front matter, required sections, fences, link rules) | All | expected |
| `./kfm_markdown_protocol_v11.2.6.md` | Protocol (spec) | Version-pinned KFM-MDP spec used by validators | Docs/CI | not confirmed in repo |
| `./KFM_REPO_STRUCTURE_STANDARD.md` | Standard | Canonical roots + placement rules | All | not confirmed in repo |
| `./KFM_ONTology_PROTOCOL.md` | Protocol | Graph ontology bindings + label/edge invariants | Graph/API | not confirmed in repo |
| `./KFM_STAC_PROFILE.md` | Profile | STAC 1.0 alignment for KFM catalogs | Catalog | not confirmed in repo |
| `./KFM_DCAT_PROFILE.md` | Profile | DCAT 3 alignment for discovery/catalog mapping | Catalog | not confirmed in repo |
| `./KFM_PROV_PROFILE.md` | Profile | PROV-O alignment for lineage bundles | Catalog/Provenance | not confirmed in repo |
| `./faircare/FAIRCARE-GUIDE.md` | Standard/Guide | FAIR+CARE application + review triggers | All | not confirmed in repo |
| `./sovereignty/INDIGENOUS-DATA-PROTECTION.md` | Standard | Indigenous data protection (masking/generalization, access) | All | not confirmed in repo |
| `./integration/README.md` | Standards index | Cross-system integration conventions (idempotency, outbox, etc.) | ETL/API | not confirmed in repo |

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Default governed doc scaffold |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Contract-first endpoint/schema changes |
| Schema registry | `schemas/README.md` | Canonical index of machine-validated contracts |
| Security policy | `.github/SECURITY.md` | Vulnerability reporting + expectations |

### Definition of Done

- [ ] This index lists every **normative** standard under `docs/standards/` and explains what it governs.
- [ ] All standards listed here have:
  - [ ] governed front matter,
  - [ ] a clear scope,
  - [ ] a version history,
  - [ ] governance/ethics/sovereignty references.
- [ ] Links in this index resolve (no broken references).
- [ ] Any standard that introduces or modifies policy is flagged as **requires human review**.
- [ ] CI and review guidance references this index as the starting point for governed work.

---

## 🗂️ Directory Layout

### This document lives at

- `docs/standards/README.md`

### Related repository paths

| Artifact / Area | Path |
|---|---|
| Master Guide + documentation map | `docs/MASTER_GUIDE_v12.md` |
| Governed templates | `docs/templates/` |
| Data lifecycle roots | `data/raw/`, `data/work/`, `data/processed/` |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph build + ontology | `src/graph/` |
| Pipelines | `src/pipelines/` |
| API boundary + contracts | `src/server/` and `src/server/contracts/` *(not confirmed in repo)* |
| UI boundary | `web/` |
| Story Nodes | `docs/reports/story_nodes/` |
| Security + policies | `.github/SECURITY.md`, `docs/security/` *(not confirmed in repo)* |

### Expected file tree for this sub-area

~~~text
📁 docs/
└── 📁 standards/
    ├── 📄 README.md                              ← you are here
    ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md           (expected)
    ├── 📄 kfm_markdown_protocol_v11.2.6.md        (not confirmed in repo)
    ├── 📄 KFM_REPO_STRUCTURE_STANDARD.md          (not confirmed in repo)
    ├── 📄 KFM_ONTology_PROTOCOL.md                (not confirmed in repo)
    ├── 📄 KFM_STAC_PROFILE.md                     (not confirmed in repo)
    ├── 📄 KFM_DCAT_PROFILE.md                     (not confirmed in repo)
    ├── 📄 KFM_PROV_PROFILE.md                     (not confirmed in repo)
    ├── 📁 faircare/
    │   └── 📄 FAIRCARE-GUIDE.md                   (not confirmed in repo)
    ├── 📁 sovereignty/
    │   └── 📄 INDIGENOUS-DATA-PROTECTION.md       (not confirmed in repo)
    └── 📁 integration/
        └── 📄 README.md                           (not confirmed in repo)
~~~

---

## 🧭 Context

### Why `docs/standards/` exists

KFM scales by adding new data domains, evidence products, graph entities, APIs, and UI layers — but **only** if everything stays consistent with the canonical pipeline and governance expectations. Standards are how KFM:

- Keeps documentation and implementation in sync as versions evolve.
- Ensures new additions don’t bypass provenance, sovereignty, or review.
- Makes CI checks possible and predictable (standards provide what validators check against).

### Key invariants

- Preserve the canonical ordering: **ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend must not query the graph directly; the **API is the only boundary**.
- Focus Mode must not present **unsourced** narrative; provenance is first-class.
- Standards changes that affect public outputs are treated as **governed changes** (reviewed, versioned).

---

## 🗺️ Diagrams

### Standards-to-pipeline influence map

~~~mermaid
flowchart LR
  subgraph S[docs/standards]
    MDP[KFM-MDP (Markdown Protocol)] --> CI[CI validation gates]
    RS[Repo Structure Standard] --> CI
    STAC[KFM-STAC Profile] --> CAT[Catalog build outputs]
    DCAT[KFM-DCAT Profile] --> CAT
    PROV[KFM-PROV Profile] --> CAT
    ONTO[KFM-ONTO Protocol] --> G[Graph ingest]
    FAIR[FAIR+CARE] --> CI
    SOV[Sovereignty] --> CI
  end

  CAT --> G --> API[Contracted APIs] --> UI[React/Map UI] --> STORY[Story Nodes] --> FOCUS[Focus Mode]
  CI --> CAT
  CI --> G
  CI --> API
  CI --> UI
  CI --> STORY
~~~

---

## 📦 Data & Metadata

### What standards govern

- **Where artifacts live** (data lifecycle roots, catalogs, graph artifacts, contracts, docs).
- **How artifacts are documented** (front matter, required sections, versioning).
- **How artifacts are made interoperable** (STAC/DCAT/PROV alignment).
- **How artifacts are consumed safely** (API boundary, sovereignty rules, provenance requirements).

### Data lifecycle

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/`
- Catalog discovery + provenance live alongside: `data/catalog/dcat/`, `data/prov/`

---

## 🌐 STAC, DCAT & PROV Alignment

### Minimum alignment expectation

Every dataset/evidence product intended for downstream use should have:

- A **STAC Collection** + **STAC Item(s)** (spatiotemporal access + assets)
- A **DCAT mapping** for discovery (title/description/license/keywords minimum)
- A **PROV activity/bundle** that records how outputs were produced (activities, agents, derivations)

### Versioning expectations

- New versions link predecessor/successor.
- Graph mirrors version lineage (do not create orphaned/untraceable entities).

---

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV profiles + schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL contracts + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### API boundary rule

- The client/UI must never bypass the API to query Neo4j.
- If a UI feature needs new graph data, the correct change is: **extend the API contract** (and implement with tests).

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Story Nodes must carry provenance annotations and connect to catalog + graph entities.
- Standards define what “valid citation” and “traceable source” means.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Predictive/uncertain content (if ever allowed) must be opt-in and include uncertainty metadata.

---

## 🧪 Validation & CI/CD

### Minimum CI gates for governed work

- Markdown protocol validation (front matter + required section registry)
- Link integrity checks (no broken paths)
- JSON schema validation (STAC/DCAT/telemetry where applicable)
- Graph integrity tests (constraints, migrations)
- API contract tests (OpenAPI/GraphQL)
- UI registry/schema checks
- Security + sovereignty scanning gates (where applicable)

### Practical contributor guidance

- Standards changes should be accompanied by:
  - updated version numbers,
  - version history entries,
  - and (when relevant) schema updates under `schemas/`.

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers or restricted locations
- New AI narrative behaviors or summarization outputs
- New external data sources
- New public-facing endpoints

### Sovereignty safety

- Document redaction/generalization rules for any restricted locations.
- Do not “unmask” generalized locations in public-facing views.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `docs/standards/` README (index + structure scaffold) | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
