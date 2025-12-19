---
title: "KFM src/agents — README"
path: "src/agents/README.md"
version: "v0.1.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:src:agents:readme:v0.1.0"
semantic_document_id: "kfm-src-agents-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:src:agents:readme:v0.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
  - "speculative_additions"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# src/agents

## 📘 Overview

### Purpose

`src/agents/` is the home for **automation agents** that support the Kansas Frontier Matrix pipeline with **repeatable, auditable, provenance-linked** tasks.

Agents may be used to:
- Assist ETL enrichment and normalization
- Validate catalog artifacts
- Support graph linkage and evidence products
- Draft narrative artifacts that are later curated and traced to sources

This directory must remain compatible with the canonical pipeline ordering:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### Scope

In scope:
- Agent task definitions and implementations
- Prompt and rules artifacts that are versioned and testable
- Tool adapters that enforce allowlists, redaction, and audit logging
- Contract tests and golden fixtures for deterministic outputs
- Provenance emission helpers for STAC/DCAT/PROV-aligned outputs

Out of scope:
- Frontend UI code (lives under `web/`)
- Direct UI-to-graph access patterns
- Ad hoc scripts that write derived datasets into `src/` instead of `data/processed/`

### Audience

- Pipeline and graph engineers
- Backend/API engineers adding evidence or narrative services
- Curators and reviewers validating AI-assisted suggestions

### Definitions

- **Agent**: a component that performs a bounded task (often enrichment, validation, linking, or drafting) under strict governance constraints.
- **Task**: a single unit of work with explicit inputs, outputs, and provenance.
- **Provenance**: lineage metadata that connects outputs to source artifacts and transformation activities.

See also:
- `docs/MASTER_GUIDE_v12.md` for the system flow and invariants.
- `docs/templates/` for governed document and narrative artifacts.

### Definition of done

A new agent or task is considered “done” when it:
- Produces outputs with stable IDs and provenance pointers
- Is deterministic or explicitly seed-locked where randomness exists
- Has test coverage (unit + contract/golden tests)
- Honors governance rules for sensitivity, sovereignty, and redaction
- Does not bypass API-layer contracts when integrating with UI-facing features

## 🗂️ Directory Layout

### This document

- `src/agents/README.md` (this file)

### Related repository paths

Canonical subsystem locations (see the Master Guide):
- `src/pipelines/` — ETL and transforms
- `data/stac/`, `data/catalog/dcat/`, `data/prov/` — catalog + lineage artifacts
- `src/graph/` — graph ingestion and ontology-aligned tooling
- `src/server/` — API boundary for contracted access
- `web/` — map and narrative UI

### File tree

~~~text
📁 src/
└── 📁 agents/
    └── 📄 README.md
~~~

Optional internal layout for this area is **not confirmed in repo** and should be created as needed:
- `src/agents/core/` — shared interfaces, base classes, run context
- `src/agents/tasks/` — task implementations grouped by domain
- `src/agents/tools/` — safe tool wrappers, allowlists, sanitizers
- `src/agents/prompts/` — prompt templates with versioning and tests
- `src/agents/policies/` — guardrails and redaction rules
- `src/agents/tests/` — unit tests + golden fixtures

## 🧭 Context

### Constraints and invariants

The system enforces these non-negotiables:
- **No unsourced narrative** in Focus Mode contexts.
- **Provenance is first-class**, maintained through STAC/DCAT/PROV and graph lineage.
- **Reproducibility** through deterministic, logged processing.

Agents must also respect the UI contract behavior:
- The frontend calls the API, which queries the graph and returns provenance-linked data.
- Focus Mode content must remain traceable to source data, and AI-assisted content must be clearly identified and opt-in.

### What belongs in `mcp/` vs `src/agents/`

- Experimental prototypes, model cards, and exploratory runs belong under `mcp/`.
- Production-ready agent code and stable task contracts belong under `src/agents/`.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC DCAT PROV]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  X[Agents]
  X -.enrich.-> A
  X -.catalog validate.-> B
  X -.link suggest.-> C
  X -.draft evidence.-> F
~~~

## 📦 Data and metadata expectations

### Minimum agent run metadata

Every agent execution should be able to emit or reference:
- `run_id`
- `agent_id`
- `task_id`
- input references (dataset IDs, document IDs, STAC item IDs, etc.)
- output references (derived artifact IDs)
- confidence and uncertainty metadata when inference is involved
- redaction decisions and sensitivity tags
- timestamps and configuration versions

### Example output envelope

This is a recommended structure for agent outputs and is **not confirmed in repo**.

~~~json
{
  "run_id": "run-2025-12-19T12:00:00Z-abc123",
  "agent_id": "kfm.agent.entity_linker",
  "task_id": "entity_link_suggest",
  "inputs": [
    {"kind": "stac_item", "id": "stac:item:..."},
    {"kind": "document", "id": "doc:..."}
  ],
  "outputs": [
    {"kind": "suggested_edge", "id": "edge_suggestion:..."}
  ],
  "confidence": {"score": 0.82, "calibration": "TBD"},
  "provenance": {
    "prov_activity_id": "prov:activity:...",
    "wasDerivedFrom": ["stac:item:...", "doc:..."]
  },
  "redactions": [],
  "warnings": []
}
~~~

## 🌐 STAC, DCAT and PROV alignment

When an agent produces a **derived data product**:
- Store derived datasets under `data/processed/`
- Emit or update corresponding catalog records:
  - STAC Items and Collections for spatial-temporal assets
  - DCAT dataset records for datasets and groupings
  - PROV activities for lineage and auditability

When an agent produces **suggestions** (e.g., candidate merges or links):
- Store as evidence artifacts with confidence metadata
- Ensure a human review path exists for any high-impact change
- Ensure provenance references the exact inputs used

## 🧱 Architecture notes

### Boundaries

- The UI consumes contracted data through the API layer.
- Agent outputs intended for UI presentation must be surfaced through API contracts and redaction rules.

### Extension points

Create new agents by:
1. Defining a bounded task with explicit inputs and outputs
2. Adding provenance emission for every output
3. Adding tests:
   - Unit tests for core logic
   - Golden fixtures for stable outputs
   - Contract checks for redaction and sensitivity handling
4. Documenting:
   - task purpose and expected inputs
   - output schema and confidence conventions
   - failure modes and fallback behavior

## 🧠 Story Nodes and Focus Mode integration

If an agent contributes to Story Nodes or Focus Mode:
- Every factual claim must be traceable to source artifacts
- Any inference must be clearly labeled and accompanied by confidence metadata
- Opt-in controls must gate AI-generated content
- Sensitivity and sovereignty rules apply to narrative display and map interactions

## 🧪 Validation and CI/CD

Recommended checks for agent changes:
- Lint and formatting
- Unit tests
- Determinism checks for seed-locked components
- Schema validation for produced artifacts
- Redaction and sensitivity tests for API-facing outputs

## ⚖ FAIR+CARE and governance

Agents must:
- Respect FAIR+CARE categorization and sensitivity labels
- Avoid emitting precise protected locations when restricted
- Produce audit-friendly provenance for all derived outputs
- Require human review for merges, deletions, or high-impact narrative changes

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---:|---|---|
| v0.1.0 | 2025-12-19 | Initial README for `src/agents/` | (you) |