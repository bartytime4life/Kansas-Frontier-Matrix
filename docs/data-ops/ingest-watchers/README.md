---
title: "👁️ KFM — Ingest Watchers (README)"
path: "docs/data-ops/ingest-watchers/README.md"
version: "v11.2.6"
last_updated: "2025-12-20"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Data-Ops & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "README"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-ingest-watchers-readme"
license: "CC-BY-4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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

doc_uuid: "urn:kfm:doc:data-ops:ingest-watchers:readme:v11.2.6"
semantic_document_id: "kfm-data-ops-ingest-watchers-readme-v11.2.6"
event_source_id: "ledger:kfm:doc:data-ops:ingest-watchers:readme:v11.2.6"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 👁️ KFM — Ingest Watchers (README)

## 📘 Overview

### Purpose
Ingest Watchers continuously observe **source endpoints, drops, and upstream feeds** for changes, convert those observations into **ingest intents**, and enforce **quality-control (QC) gates** before any content is promoted into STAC/DCAT/PROV catalogs, the Neo4j graph, and downstream APIs/UI.

This folder documents the *operational layer* around ingestion: **signals**, **trigger rules**, **QC gates**, and **provenance attachments** that make ingestion deterministic, auditable, and safe.

### Scope
| In Scope | Out of Scope |
|---|---|
| Watch strategies (polling/webhook/file-drop), trigger rules, and suppression | Implementing parsers/transform logic (ETL internals) |
| QC gate requirements + failure handling | UI rendering details (except audit expectations) |
| Provenance/lineage attachments (STAC/DCAT/PROV + run IDs) | Non-ingest observability (general infra monitoring) |
| Operational runbook pointers and triage workflow | Incident response policy (lives in security/runbooks) |

### Audience
- Primary: Data-Ops, ETL maintainers, ingestion/on-call, QA maintainers
- Secondary: Graph/API maintainers, story-node editors (to understand provenance expectations)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Key terms used here:
  - **Watcher**: a process that detects change and emits an *ingest intent*.
  - **Ingest intent**: a structured event describing *what to ingest* and *why now*.
  - **QC gate**: a deterministic validation step that must pass before promotion.
  - **Promotion**: moving an asset from raw/work outputs to cataloged/graph-served outputs.
  - **Provenance attachments**: STAC/DCAT/PROV references bound to each ingest run and its products.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Operational signals + gates standard | `docs/data-ops/ingest-watchers/OPERATIONAL_SIGNALS_AND_GATES.md` | Data-Ops | Canonical definitions for triggers + QC gates |
| Data-Ops overview | `docs/data-ops/README.md` | Data-Ops | Entry point for ops standards |
| Data quality checks | `docs/data-ops/data-quality/README.md` | Data-Ops | Cross-links to check families |

### Definition of done (for this README)
- [ ] Front-matter complete + valid
- [ ] Directory placement matches `path`
- [ ] Links resolve within repo (or are clearly marked TBD)
- [ ] Invariants preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- [ ] Mentions of sensitive handling defer to sovereignty policy (no sensitive location inference)

---

## 🗂️ Directory Layout

### This directory
~~~text
📁 docs/
└── 📁 data-ops/
    └── 📁 ingest-watchers/
        ├── 📄 README.md
        └── 📄 OPERATIONAL_SIGNALS_AND_GATES.md
~~~

### Related repository paths (operational touchpoints)
~~~text
📁 data/
├── 📁 raw/                 # source snapshots / drops (domain-specific subtrees)
├── 📁 work/                # staging + intermediate products
│   └── 📁 logs/             # run logs (ingest + qc + catalog + graph)
└── 📁 stac/                # published STAC collections/items

📁 docs/
├── 📁 data-ops/             # operational standards + runbooks
├── 📁 governance/           # ROOT_GOVERNANCE / ETHICS / SOVEREIGNTY
└── 📁 ci/                   # CI checklists + runbooks

📁 schemas/
└── (STAC/DCAT/PROV + telemetry schemas)
~~~

> NOTE: Exact subpaths under `data/` are domain-specific. This README documents watcher behavior and contracts, not domain structures.

---

## 🧭 Context

### Why ingest watchers exist
KFM ingests a mix of:
- APIs that change continuously (real-time feeds, rolling updates)
- Periodic releases (monthly/quarterly datasets)
- Manual source drops (archival PDFs, scans, tables, shapefiles)

Watchers provide the “front door discipline”:
1) detect change,
2) trigger deterministic ingest,
3) enforce QC gates,
4) attach provenance,
5) promote safely.

### System invariants (non-negotiable)
- **No direct UI-to-graph coupling**: UI reads through APIs only.
- **No promotion without QC**: failed gates stop promotion and emit actionable errors.
- **Every promoted artifact is provenance-linked**: STAC/DCAT/PROV identifiers bound to run IDs.
- **Idempotent ingestion**: same input should not create duplicates; reruns are safe.

### Operational philosophy
- Prefer **boring and deterministic** over clever:
  - stable IDs, stable hashes, deterministic transforms
  - explicit gate results with machine-readable reason codes
- Prefer **“fail closed”** on schema/provenance gaps:
  - if a watcher cannot prove what changed (or cannot bound risk), it should not promote

---

## 🗺️ Diagrams

### Watcher-to-pipeline flow
~~~mermaid
flowchart LR
  S[Source endpoint / drop / feed] --> W[Ingest Watcher]
  W --> I[Ingest intent event]
  I --> E[ETL run (deterministic)]
  E --> Q[QC gates]
  Q -->|pass| C[STAC/DCAT/PROV catalogs]
  C --> G[Neo4j graph build / refresh]
  G --> A[API layer]
  A --> U[React/Map UI]
  U --> N[Story Nodes]
  N --> F[Focus Mode]
  Q -->|fail| H[Hold + alert + remediation ticket]
~~~

---

## 📦 Data & Metadata

### What a watcher must emit (minimum contract)
A watcher should emit an ingest intent with enough information to:
- reproduce the ingest decision
- locate the source material
- explain why it triggered
- bind run outputs to provenance

Minimum fields (conceptual):
- `source_id` (stable identifier)
- `detected_change` (hash diff, ETag change, updated timestamp, file manifest delta, etc.)
- `intent_type` (new, update, backfill, reprocess, repair)
- `requested_range` (time window / spatial bounds if applicable)
- `priority` (normal/high + reason)
- `idempotency_key` (stable key for dedupe)
- `requested_by` (service principal / user)
- `sensitivity_mode` (public/restricted handling mode)

> The canonical signal taxonomy, trigger rules, and QC gate definitions live in:
> `docs/data-ops/ingest-watchers/OPERATIONAL_SIGNALS_AND_GATES.md`.

### Promotion boundaries (where watchers “hand off”)
- **Raw/source retention**: `data/raw/…` (or domain equivalents)
- **Work/staging**: `data/work/…` (intermediate outputs)
- **Catalog outputs**: `data/stac/…` + DCAT views + PROV bundles
- **Graph + API surfacing**: only after catalog + provenance readiness is verified

### Sensitivity & redaction
Watchers must respect:
- `docs/governance/SOVEREIGNTY.md`
- `docs/governance/ETHICS.md`

Operational rules:
- never infer or enrich sensitive locations beyond allowed policies
- always carry sensitivity flags forward into catalogs / API responses
- ensure public promotion excludes restricted geometry/attributes where required

---

## 🌐 STAC, DCAT & PROV Alignment

### Required mapping (watcher responsibilities)
Watchers must ensure the downstream run can record:
- **STAC**: stable collection/item IDs and asset checksums
- **DCAT**: dataset identifiers + license mapping for catalog views
- **PROV-O**:
  - `prov:wasGeneratedBy`: the ingest run / activity ID
  - `prov:wasDerivedFrom`: source identifiers, manifests, or upstream dataset versions
  - agent identity (service principal) and time bounds

### Provenance attachment checklist
- [ ] input manifest captured (hashes + sizes + source URIs)
- [ ] run configuration snapshot recorded (version pins, rules)
- [ ] QC gate results recorded (pass/fail + reason codes)
- [ ] output asset hashes recorded (before promotion)
- [ ] STAC/DCAT/PROV references written to the audit panel payloads (where applicable)

---

## 🧱 Architecture

### Where watchers live in the KFM system
Watchers are a Data-Ops mechanism that:
- observes sources and emits ingest intents (events/jobs)
- triggers ETL executions
- blocks promotion on QC failures
- writes logs and artifacts needed for governance/audit

Watchers MUST NOT:
- bypass catalogs
- write directly into UI-facing stores
- mutate Neo4j directly (graph changes are pipeline-driven)

### Operational interfaces
Typical interfaces include (implementation-specific):
- scheduled polling
- webhook handlers
- file-drop directory monitors
- release manifest comparators
- “repair triggers” (re-run on schema change, backfill request, or governance override)

> If an API contract is added for watcher status/controls, document it via
> `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (governed contract + tests).

---

## 🧠 Story Node & Focus Mode Integration

### Why watchers matter to narrative layers
Story Nodes and Focus Mode must only surface **provenance-linked** content.
Watcher-enforced QC + provenance attachments ensure:
- citations resolve to catalog IDs
- timelines and map layers are not built on partial/ambiguous ingest states
- restricted/sensitive materials are not leaked through “helpful” enrichment

### Focus Mode expectations (operational)
- if a dataset is in “hold” due to gate failure, Focus Mode must not show it as canonical
- audit panels should show:
  - last successful ingest run
  - last failure reason (if any) + remediation pointer
  - dataset version + provenance references

---

## 🧪 Validation & CI/CD

### Minimum validation steps
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Data-quality checks (domain-specific + shared checks)
- [ ] Graph integrity checks (constraints + invariants)
- [ ] API contract tests (if watcher status endpoints exist)
- [ ] Security + sovereignty scanning gates (as applicable)

### Operator quick links
- Data-Ops root: `docs/data-ops/README.md`
- Data quality root: `docs/data-ops/data-quality/README.md`
- Ingest watcher signals/gates: `docs/data-ops/ingest-watchers/OPERATIONAL_SIGNALS_AND_GATES.md`
- CI runbooks: `docs/ci/runbooks/README.md`

---

## ⚖ FAIR+CARE & Governance

### Review triggers
- New watcher touching a sensitive source category
- New enrichment that changes location precision or attribution semantics
- New auto-promotion path that bypasses QC gates (not allowed; requires redesign)
- Any change that alters provenance fields or schema contracts

### Approvals
- FAIR+CARE council review: **as required by data domain**
- Security council review: **as required by risk classification**
- Historian/editor review: **if it alters narrative-facing evidence behaviors**

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v11.2.6 | 2025-12-20 | Initial ingest-watchers README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

