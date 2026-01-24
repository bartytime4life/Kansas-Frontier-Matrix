---
title: "KFM — data/graph/cypher/ (Post-Import Cypher Scripts)"
path: "data/graph/cypher/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:graph:cypher:readme:v1.0.0"
semantic_document_id: "kfm-data-graph-cypher-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:graph:cypher:readme:v1.0.0"
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

# KFM — `data/graph/cypher/` (Post-Import Cypher Scripts)

This directory contains **optional Cypher scripts** intended to run *after* bulk import (or after a loader run) to finalize the graph instance:

- constraints and indexes,
- post-load normalization,
- lightweight derived relationships that are deterministic and reproducible.

This folder is for **generated/operational scripts**, not for the canonical ontology or migrations.

Canonical pipeline ordering is preserved:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose

- Provide a predictable location for Cypher scripts that:
  - prepare a fresh database after import,
  - enforce constraints/indexes aligned with the governed ontology,
  - apply deterministic “touch-up” steps required by the runtime.

### Scope

| In Scope | Out of Scope |
|---|---|
| Constraint/index scripts used after bulk import | Ontology definitions (governed under `src/graph/` and docs) |
| Deterministic post-load normalization | Ad-hoc manual fixes to production data |
| Load-time safety scripts (idempotent) | UI or API logic |

### Audience

- Primary: graph maintainers and operators running graph build/import pipelines.
- Secondary: reviewers verifying governance and safety constraints.

---

## 🗂️ Directory Layout

### This document
- `path`: `data/graph/cypher/README.md`

### Expected tree

data/
└── 🕸️ graph/
    └── 🧠 cypher/
        ├── 📄 README.md                       # 📘 What these scripts do, run order, idempotency rules, and safety notes
        ├── 🔒📄 00-constraints.cypher          # Constraint definitions (uniqueness/required props); run first
        ├── 📇📄 01-indexes.cypher              # Index definitions for performance; run after constraints
        ├── 🧼📄 10-normalize.cypher            # Normalization/cleanup queries (standardize props, fix minor drift)
        └── 🧾🗂️ manifest.json                  # (optional) Script registry: order, purpose, expected effects, checksums

Notes:
- Filenames are ordered to encourage repeatable application.
- If the repo uses a different ordering scheme, document it here and enforce via CI.

---

## 🧱 Script Design Rules (must follow)

### 1) Idempotency (required)

Scripts MUST be safe to run more than once.

- Use `IF NOT EXISTS` where supported for constraints/indexes.
- For normalization writes, prefer `MERGE`/`SET` patterns that do not duplicate entities.
- Avoid non-deterministic operations (random, time-dependent assignments).

### 2) No business logic leakage

These scripts must not “implement the API” or “implement the UI.” They can:

- enforce graph constraints,
- normalize imported fields,
- add deterministic derived relationships if defined by the graph subsystem.

Any behavior that affects user-facing semantics must live behind the API boundary (and be contract-tested).

### 3) Evidence-first linking

When scripts add or modify relationships, they must not erase evidence/provenance hooks.

Where applicable, preserve columns/properties that point to:
- STAC IDs,
- DCAT dataset IDs,
- PROV activity IDs.

---

## 🔒 Safety & Governance

### Sensitivity and redaction

Cypher scripts must not create new sensitive location exposure.

If scripts compute derived geometry or attach locations:
- ensure they respect generalization/redaction requirements,
- ensure the API boundary can enforce visibility rules.

### Prohibited content

- No secrets, tokens, or credentials.
- No embedding of private endpoints that bypass policy.
- No “infer sensitive locations” operations.

---

## ✅ Validation & QA (minimum)

### Minimum checks

- [ ] Cypher lint (repo tool, if present).
- [ ] Scripts run in a clean local instance without error.
- [ ] Constraints/indexes match the governed ontology expectations.
- [ ] Post-load scripts are idempotent.
- [ ] No policy violations (no new sensitive exposures).

### Reproduction (placeholders)

    # Placeholder only — replace with repo-specific commands.
    #
    # 1) Load bulk CSVs (data/graph/csv/*) into Neo4j
    # 2) Apply cypher scripts in order:
    #    - 00-constraints.cypher
    #    - 01-indexes.cypher
    #    - 10-normalize.cypher
    # 3) Run smoke tests / integrity queries

---

## 🧠 Story Node & Focus Mode Integration

These scripts matter downstream because they help keep the graph stable and queryable by the API boundary.

Constraints and deterministic normalization are a prerequisite for:

- stable entity IDs,
- stable relationships,
- consistent evidence/provenance references that Story Nodes and Focus Mode can cite.

Focus Mode remains provenance-linked only; these scripts must not introduce unsourced narrative facts.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for `data/graph/cypher/` | TBD |

---

Footer refs:
- Graph import root: `data/graph/README.md`
- Import CSVs: `data/graph/csv/README.md`
- Graph code/ontology: `src/graph/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
