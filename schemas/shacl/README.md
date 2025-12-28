---
title: "KFM SHACL Schemas & Shape Bundles"
path: "schemas/shacl/README.md"
version: "v1.0.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:schemas:shacl:readme:v1.0.0"
semantic_document_id: "kfm-schemas-shacl-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:shacl:readme:v1.0.0"
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

# KFM SHACL Schemas & Shape Bundles

## 📘 Overview

### Purpose
KFM v13 is shifting toward a **buildable, contract-first, evidence-first** platform with a canonical pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Within that governance model, `schemas/` is the canonical home for contracts. The v13 blueprint explicitly calls out **JSON Schema + optional SHACL shape bundles** as part of the schemas design.

This folder documents **how KFM organizes SHACL shapes** so that:
- RDF / JSON-LD representations of KFM artifacts can be validated consistently,
- graph- and narrative-adjacent constraints can be expressed as contracts,
- validation remains deterministic and CI-friendly (“validate if present; fail if invalid; skip if not applicable”).

### Scope
In scope:
- SHACL shape bundles for validating RDF / JSON-LD artifacts produced or consumed by the KFM pipeline
- Conventions for organizing, naming, versioning, and testing SHACL shapes
- Guidance on where SHACL validation fits in Catalog and Graph stages

Out of scope:
- Authoring the ontology itself (see Ontology Protocol; path referenced in the v13 blueprint)
- Implementing CI workflows/tooling (those live under `.github/` / `tools/` / `tests/`)
- Any UI logic (UI must not query Neo4j directly; all access is via API contracts)

### Audience
- Catalog owners (STAC/DCAT/PROV producers)
- Graph/ontology owners (graph ingest and constraints)
- CI/QA maintainers responsible for contract validation gates

### Key invariant reminders
- **Contracts are canonical:** schemas/specs must live under `schemas/` and should validate in CI.
- **Evidence first:** artifacts must exist as cataloged, versioned outputs before graph loading or storytelling.
- **No UI direct-to-graph reads:** SHACL validation supports upstream correctness; the UI still consumes only API outputs.

## 🗂️ Directory Layout

### This document
- `path`: `schemas/shacl/README.md` (must match front-matter)

### Related canonical roots (context)
- `schemas/` — canonical schema/spec home (JSON Schema + optional SHACL bundles)
- `data/catalog/dcat/` — DCAT outputs (often JSON-LD)
- `data/prov/` — PROV bundles (may be JSON or JSON-LD)
- `src/graph/` — graph code and ontology bindings (validation may occur pre-ingest or on exports)
- `src/server/contracts/` — API contracts (separate from SHACL; UI must not bypass)
- `docs/reports/story_nodes/` — governed Story Nodes (must validate; may eventually have SHACL representations)

### Recommended folder structure (not confirmed in repo)
This repo location exists to provide **one canonical home** for SHACL shapes to avoid “mystery duplicates.”
If the repo later chooses to co-locate shapes under `schemas/dcat/` or `schemas/prov/`, this README should be updated to preserve a single canonical strategy.

~~~text
📁 schemas/
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 story_nodes/            # NOTE: some docs also refer to storynodes (naming to be standardized)
├── 📁 ui/
├── 📁 telemetry/
└── 📁 shacl/
    ├── 📄 README.md
    ├── 📁 bundles/            # SHACL “bundles” grouped by validation target
    │   ├── 📁 dcat/           # DCAT JSON-LD validation shapes
    │   ├── 📁 prov/           # PROV JSON-LD validation shapes
    │   ├── 📁 story_nodes/    # Story Node structural/citation shapes (if represented as RDF/JSON-LD)
    │   └── 📁 graph/          # Graph export / ontology-alignment shapes (when applicable)
    ├── 📁 fixtures/           # Minimal RDF/JSON-LD examples for deterministic tests
    └── 📁 reports/            # (optional) Saved validation reports for debugging (do not treat as source data)
~~~

## 🧭 Context

### Why SHACL exists in KFM
KFM already relies on schemas/contracts as first-class artifacts. While JSON Schema covers JSON outputs, SHACL is valuable when:
- an artifact is represented as RDF or JSON-LD (common for DCAT/PROV),
- constraints are better expressed in a graph-shaped way (node/property constraints, link constraints),
- the goal is consistent “contract-first” validation across pipeline boundaries.

The v13 blueprint explicitly raises the timing question: **adopt SHACL validation for JSON-LD bundles now or later** (target noted as v13.1.0). This folder is the canonical place to capture those shapes so adoption is incremental and governed.

### SHACL vs JSON Schema (decision guide)
Use the simplest contract that can reliably enforce the requirement.

| Requirement | Prefer | Notes |
|---|---|---|
| Validate a JSON document structure | JSON Schema | Primary contract mechanism for JSON artifacts |
| Validate RDF triples / JSON-LD graph constraints | SHACL | Targeted to RDF/JSON-LD constraints and graph patterns |
| Validate both JSON and JSON-LD views of the “same” artifact | Both | Keep versions aligned; avoid duplicated rules where possible |

## 🧩 SHACL authoring conventions

### File formats
Preferred (recommended):
- Turtle: `.ttl` (reviewable diffs, easy prefix management)

Allowed (only if needed; not confirmed in repo):
- `.jsonld` for shapes if a SHACL engine requires it

### Naming and versioning
KFM schema governance expects schemas to be versioned and evolved deliberately.

Recommended conventions:
- Bundle directory reflects the validation target: `bundles/<target>/`
- Bundle file name includes an explicit semantic version:
  - `bundles/prov/kfm-prov-bundle__v1.0.0.ttl`
  - `bundles/dcat/kfm-dcat-bundle__v1.0.0.ttl`

If a bundle changes (new constraints, changed severity, breaking constraint), bump the version and document migration expectations.

### Stable identifiers
Recommended: every shape has a stable `sh:name` and/or IRI aligned to KFM stable-ID practices. Example pattern:

- `urn:kfm:shacl:<bundle>:<shape>:v<major>.<minor>.<patch>`

(Exact IRI scheme for SHACL shapes is not confirmed in repo; keep it stable once chosen.)

### Severity policy
Recommended:
- Use SHACL severity to reflect governance intent:
  - `sh:Violation` for contract-breaking constraints (fail CI when enforced)
  - `sh:Warning` for best practices / non-breaking guidance
  - `sh:Info` for metadata hints

## 🧪 Validation & CI/CD

### Contract-first CI principle
Validation must behave deterministically:
- **validate if present; fail if invalid; skip if not applicable**

This matches the v13 definition-of-done expectations for CI behavior.

### Where SHACL validation fits
- **Catalog stage (DCAT/PROV):**
  - Validate DCAT outputs in `data/catalog/dcat/` when they are JSON-LD.
  - Validate PROV bundles in `data/prov/` when they are JSON-LD.
- **Graph stage:**
  - If the graph export is available as RDF/JSON-LD (or a transform exists), validate it with graph bundle shapes.
  - Otherwise, keep graph integrity checks as graph-native tests (Cypher/fixtures) and treat SHACL as an extension point.
- **Story Nodes (future-friendly):**
  - Story Nodes must validate; JSON Schema likely handles structure/front-matter.
  - SHACL may be used if Story Nodes are expressed as RDF/JSON-LD for linked-data interoperability.

### Tooling (not confirmed in repo)
This README does not mandate a specific SHACL engine.
Implementations may use:
- a Python SHACL engine (e.g., pySHACL),
- a JVM SHACL engine,
- or other standards-compliant tooling.

If/when tooling is standardized, document it under `tools/` and wire it into CI.

### Suggested deterministic test approach (not confirmed in repo)
1. Maintain minimal fixtures in `schemas/shacl/fixtures/`
2. Run validation against fixtures in CI
3. Assert:
   - the report is produced,
   - violations match expected counts / messages (or stable codes if supported)

## ⚖ FAIR+CARE & Governance

SHACL shapes are *contracts*, and contract changes can affect downstream behavior:
- Avoid constraints that encourage or enable **inference of sensitive locations** or identity beyond what governance allows.
- Treat any shape that enforces or modifies fields related to **sensitivity/classification** as governance-relevant and requiring review.
- SHACL validation complements (but does not replace) other CI gates such as secret/PII scanning and redaction/generalization enforcement.

When a referenced policy or standard is missing, follow the project rule: mark “not confirmed in repo” and propose adding it in the canonical location rather than inventing new rules.

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v1.0.0 | 2025-12-28 | Initial README establishing canonical `schemas/shacl/` conventions |

