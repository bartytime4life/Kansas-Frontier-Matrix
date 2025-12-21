---
title: "KFM UI Schemas — README"

path: "schemas/ui/README.md"

version: "v1.0.0"

last_updated: "2025-12-21"

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



doc_uuid: "urn:kfm:doc:schemas:ui:readme:v1.0.0"

semantic_document_id: "kfm-schemas-ui-readme-v1.0.0"

event_source_id: "ledger:kfm:doc:schemas:ui:readme:v1.0.0"

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

# KFM UI Schemas

## 📘 Overview

### Purpose

- Define what belongs in `schemas/ui/` and how these schemas protect the UI contract boundary.
- Primary intent: **validate UI layer registry JSON** used by the web runtime so new layers can be added/configured without breaking the UI.

### Scope

| In Scope | Out of Scope |
|---|---|
| JSON Schema(s) that validate UI configuration artifacts (especially layer registries) | UI runtime code in `web/`, API contract specs under `src/server/contracts/`, ETL/catalog/graph schemas |

### Audience

- Primary: UI engineers, contract/schema owners, CI maintainers.
- Secondary: Curators/maintainers updating layer registry JSON entries; Story Node authors referencing layer IDs.

### Definitions (link to glossary)

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: **layer registry**, **layer id**, **Focus Mode**, **provenance**, **sensitivity**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `schemas/ui/README.md` | Contracts owners | Directory conventions + validation expectations |
| UI layer registry schema | `schemas/ui/<ui-layer-registry>.schema.json` | UI contracts owner | Filename not confirmed in repo |
| Layer registry JSON configs | `web/**/layers/**` | UI team | Canonical consumer path for layer registries |
| Story Nodes | `docs/reports/story_nodes/**` | Curators | `focus_layers` should reference stable layer IDs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Scope and boundaries documented (what belongs / what does not)
- [ ] Versioning expectations documented (SemVer + changelog)
- [ ] Validation steps listed and repeatable (placeholders allowed)
- [ ] Governance + CARE/sovereignty considerations explicitly stated for sensitive layers

## 🗂️ Directory Layout

### This document

- `path`: `schemas/ui/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Schemas (all) | `schemas/` | Contract artifacts (JSON Schema + profiles) |
| UI schemas | `schemas/ui/` | UI configuration schemas (layer registry schema is canonical here) |
| UI layer registries | `web/**/layers/**` | JSON configs defining layers available at runtime |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL + response contracts consumed by UI |
| Story Nodes | `docs/reports/story_nodes/**` | Provenance-linked narrative + optional focus controls |

### Expected tree (target shape)

~~~text
📁 schemas/
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 storynodes/
├── 📁 telemetry/
└── 📁 ui/
    ├── 📄 README.md
    └── 📄 <ui-layer-registry>.schema.json  (not confirmed in repo)
~~~

## 🧭 Context

### Why this directory exists

- KFM’s pipeline is ordered and contract-first: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- The UI is extensible via **layer registry JSON**; schemas here ensure those registries remain **machine-validated** and safe to evolve.

### Contract boundary rules (non-negotiable)

- The UI must **not** query Neo4j directly; all graph access is via the API layer.
- The layer registry should reference API endpoints / tiles / assets **through the API boundary**, not internal graph connections.

### Sensitivity considerations

- If a layer could expose restricted locations or culturally sensitive knowledge, protection must happen before UI display (generalization/redaction), and any Story Node assets must pass review gates.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[schemas/ui<br/>UI JSON Schema] --> B[CI: schema validation]
  B --> C[web/**/layers/**<br/>Layer registry JSON]
  C --> D[UI runtime<br/>React + Map engine]
  D --> E[Focus Mode]
  E --> F[API context bundle<br/>(provenance-linked)]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry config | JSON | `web/**/layers/**` | Validate against `schemas/ui/*.schema.json` |
| UI schema | JSON Schema | `schemas/ui/**` | JSON Schema validation (dialect not confirmed in repo) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation results | CI logs | `.github/workflows/**` | Schema validation gates |

### Sensitivity & redaction

- UI schemas should support capturing (or gating) sensitivity-relevant metadata for layers.
- Field names and enforcement rules are **not confirmed in repo**; treat as extension candidates to align with governance requirements.

### Quality signals

- Layer registries validate in CI before deploy.
- Layer IDs remain stable and resolvable (especially if referenced by Story Nodes for Focus Mode).
- Registries do not introduce unintended disclosure paths (e.g., restricted geometries).

## 🌐 STAC, DCAT & PROV Alignment

- UI schemas are not STAC/DCAT/PROV schemas, but the **layers they describe** should surface evidence that remains provenance-linked via the API boundary.
- Recommended pattern (inference): layer entries include optional dataset/provenance “hints” (IDs or labels) that help the UI render an evidence panel while still relying on API responses as the source of truth.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/**/layers/**` | Schema-validated |

### Extension points checklist (for future work)

- [ ] UI: add/modify layer registry entry (keep backward compatible when possible)
- [ ] Schemas: bump schema version + update changelog when breaking
- [ ] Story: ensure any `focus_layers` values resolve to layer registry IDs

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Story Nodes may include `focus_layers` that toggle UI layers in Focus Mode.
- Therefore: registry `id` values must be stable and should match whatever naming/ID conventions Story Nodes use.

### Provenance-linked narrative rule

- Focus Mode consumes provenance-linked content only.
- Any predictive or AI-generated content must be opt-in and clearly marked with uncertainty metadata.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV + UI schemas)
- [ ] UI layer registry schema checks
- [ ] API contract tests (if UI consumes new/changed endpoints)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas/ui
# 2) validate web/**/layers/** JSON files against schemas/ui
# 3) run markdown protocol lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| not confirmed in repo | not confirmed in repo | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- New sensitive layers
- New external data sources
- Any changes that could expose restricted locations

### CARE / sovereignty considerations

- Document and enforce redaction/generalization rules for restricted locations before UI display.
- Ensure provenance is available for any layer shown in Focus Mode.

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for `schemas/ui/` | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

