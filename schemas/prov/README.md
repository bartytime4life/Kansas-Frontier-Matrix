---
title: "KFM PROV Schemas"
path: "schemas/prov/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:schemas:prov-readme:v1.0.0"
semantic_document_id: "kfm-schemas-prov-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:prov-readme:v1.0.0"
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

# schemas/prov

## 📘 Overview

### Purpose

This directory is the canonical home for **schema contracts** that validate KFM provenance outputs (**PROV bundles**) produced by pipelines and stored under `data/prov/`. PROV is treated as a first-class catalog artifact alongside STAC and DCAT.

### Scope

**In scope**
- JSON Schema (primary) and *optional* SHACL shape bundles (if adopted) that describe **how KFM serializes provenance** and what fields/IDs are required.
- Rules and expectations for **schema versioning**, compatibility, and CI validation.

**Out of scope**
- Emitting provenance (belongs to `src/pipelines/`).
- Storing provenance bundles (belongs to `data/prov/`).
- UI rendering or API exposure (belongs to `web/` and `src/server/` respectively).

### Audience
- Catalog maintainers validating `data/prov/` outputs
- Pipeline authors generating provenance
- CI maintainers adding schema validation gates

### Definitions
- **PROV bundle**: a serialized provenance record describing *entities* (things), *activities* (processes), and *agents* (actors) and their relations.
- **Contract artifact**: a machine-validated schema/spec that producers and consumers rely on (schemas here are contract artifacts).
- **KFM PROV profile**: KFM’s constrained usage of PROV (what fields, IDs, and linkages KFM requires).

## 🗂️ Directory Layout

### This document
- `path`: `schemas/prov/README.md` (must match front-matter)

### Canonical neighbors

- `data/prov/` — PROV bundles (per run / per dataset)
- `data/stac/` — STAC collections/items
- `data/catalog/dcat/` — DCAT outputs (JSON-LD)
- `schemas/` — all schema contracts
- `src/pipelines/` — pipeline code that generates bundles
- `docs/MASTER_GUIDE_v12.md` — canonical pipeline ordering and non-negotiables
- `docs/standards/KFM_PROV_PROFILE.md` — normative profile doc (**not confirmed in repo**; may be a placeholder depending on branch)

### Target file tree

> This is the **target** contract layout for PROV schemas. Files marked `TODO` are intentionally not assumed to exist yet.

~~~text
📁 schemas/
└── 📁 prov/
    ├── 📄 README.md
    ├── 📄 kfm-prov-bundle.schema.json          # TODO: top-level bundle contract
    ├── 📄 kfm-prov-activity.schema.json        # TODO: activity contract
    ├── 📄 kfm-prov-entity.schema.json          # TODO: entity contract
    ├── 📄 kfm-prov-agent.schema.json           # TODO: agent contract
    └── 📄 CHANGELOG.md                         # TODO: schema contract changelog
~~~

## 🧭 Context

KFM’s canonical ordering is:

**ETL → STAC/DCAT/PROV catalogs → Graph → API → UI → Story Nodes → Focus Mode**:contentReference[oaicite:3]{index=3}

Within that ordering, PROV is required to preserve evidence lineage. At a minimum, each new dataset should have STAC + DCAT + a PROV activity describing the transform that generated it:contentReference[oaicite:4]{index=4}.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL / Transform Run] --> B[data/prov/ PROV bundle]
  B --> C[Validate against schemas/prov]
  C -->|pass| D[Catalog + Graph ingest boundary]
  C -->|fail| E[CI gate blocks merge / release]
~~~

## 📦 Data & Metadata

### What is validated here

- **Primary target**: PROV bundles stored under `data/prov/` (canonical home is per-run / per-dataset):contentReference[oaicite:5]{index=5}.
- **Serialized forms**: KFM documentation references provenance files such as `prov.json` or `prov.ttl` (serialization details belong in the PROV profile):contentReference[oaicite:6]{index=6}.

> Note: JSON Schema validation applies to JSON/JSON-LD serializations. If the canonical output is Turtle (`.ttl`), validation should be performed with SHACL (optional, not required unless adopted).

### Minimal provenance expectations

These are **validation targets** for the eventual schemas (exact field names are profile-defined):

- Stable identifiers for:
  - dataset/run context (e.g., `run_id`, `dataset_id`)
  - core PROV nodes: **Entity**, **Activity**, **Agent**
- Lineage relations that enable traceability:
  - derived-from / generated-by / attributed-to patterns (profile-defined):contentReference[oaicite:7]{index=7}

### Sensitivity & redaction

Even when the dataset is public, provenance may include:
- source URLs, file paths, contributor identifiers, and intermediate artifacts

Any policy-level redaction rules belong under governance docs referenced in front matter (and must be enforced at the API/UI boundary if exposed).

## 🌐 STAC, DCAT & PROV Alignment

KFM treats schemas as contract artifacts and expects machine validation at the catalog boundary:contentReference[oaicite:8]{index=8}.

Minimum alignment policy (documentation requirement):
- STAC Collection + Item(s)
- DCAT mapping
- PROV activity for the transform that generated it:contentReference[oaicite:9]{index=9}

## 🧱 Architecture

### Contracts, not conventions

Schemas in `schemas/prov/` exist so:
- producers (pipelines) and consumers (catalog tooling, graph ingest, APIs) can evolve independently,
- CI can validate provenance bundles deterministically.

### Versioning expectations

Schema contracts are expected to follow **semantic versioning**, with version bumps on any schema change and a maintained changelog:contentReference[oaicite:10]{index=10}.

## 🧠 Story Node & Focus Mode Integration

Provenance supports KFM’s evidence-first narrative rules:
- Story Nodes should link claims to evidence artifacts.
- Focus Mode should only consume provenance-linked content (no unsourced narrative).

(Story Node specifics are governed by the Story Node template; this README governs the schema layer.)

## 🧪 Validation & CI/CD

### Minimum gates (expected)

- JSON schema validation for catalog/provenance artifacts (when present)
- Fail if invalid; skip if not applicable (e.g., no `data/prov/` outputs in a PR)

### Implementation notes

Validation tooling is **not specified here**. The contract is:
- bundles produced to `data/prov/` must validate against the schema(s) in this directory,
- CI should enforce that contract.

## ⚖ FAIR+CARE & Governance

### Review triggers
- New provenance fields that expose contributor identity, sensitive locations, or restricted source details
- Any schema changes that could alter what is exposed downstream via API/UI

### CARE / Sovereignty
If provenance contains restricted locations or culturally sensitive context, the profile and downstream contracts must define redaction/generalization requirements (requires human review).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README scaffolding for PROV schema contracts | TBD |

---

Footer refs:
- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/standards/KFM_PROV_PROFILE.md` (not confirmed in repo)

