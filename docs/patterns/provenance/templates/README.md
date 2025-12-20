---
title: "🧬 KFM Provenance Templates — README"
path: "docs/patterns/provenance/templates/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "Pattern"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:patterns:provenance:templates:readme:v1.0.0"
semantic_document_id: "kfm-patterns-provenance-templates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:patterns:provenance:templates:readme:v1.0.0"
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

# 🧬 KFM Provenance Templates

## 📘 Overview

### Purpose
This folder contains **copy/paste templates** used by the KFM provenance pattern to produce **repeatable, audit-ready** lineage artifacts (run manifests, human provenance notes) that align with the canonical pipeline:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.

See the parent pattern document: `../README.md`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Template files for run-level provenance capture (manifest + human note) | Full PROV-O modeling guide (see `../README.md`) |
| CI-safe placeholder examples (no secrets; no sensitive coordinates) | Any UI implementation detail (UI consumes provenance via APIs) |
| Deterministic identifiers + checksums conventions (as fields) | Defining new governance policies |

### Audience
- Primary: KFM ETL + catalog implementers, graph ingestion maintainers, API owners.
- Secondary: Documentation maintainers, reviewers (FAIR+CARE / sovereignty), Story Node authors.

### Definitions (link to glossary)
- Glossary (preferred if present): `docs/glossary.md`
- Terms used here: `run_id`, `run manifest`, `provenance note`, `PROV bundle`, `checksum`, `stable identifier`.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Provenance Pattern | `docs/patterns/provenance/README.md` | KFM | Canonical provenance & lineage guidance |
| Run manifest template | `docs/patterns/provenance/templates/run_manifest.template.yaml` | KFM | Machine-facing skeleton (inputs/outputs/agents/config refs) |
| Provenance note template | `docs/patterns/provenance/templates/provenance_note.template.md` | KFM | Optional human note to accompany a run |
| Example bundles | `docs/patterns/provenance/examples/` | KFM | CI-safe example artifacts (masked/generalized) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (path matches)
- [ ] Template file list matches repo contents for this folder
- [ ] Guidance does not imply prohibited AI actions (no fabricated provenance)
- [ ] No secrets, tokens, or sensitive coordinates included
- [ ] Directory trees use `~~~text` fencing + emojis + aligned comments

## 🗂️ Directory Layout

### This document
- `path`: `docs/patterns/provenance/templates/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Provenance pattern | `docs/patterns/provenance/` | Pattern docs, examples, templates |
| MCP run logs | `mcp/runs/` | Run-scoped manifests + PROV bundles |
| STAC | `data/stac/` | Items/Collections that can link provenance assets |
| DCAT | `data/catalog/dcat/` | Dataset views with provenance references |
| PROV | `data/prov/` | Optional catalog-scoped provenance bundles (if used) |

### Expected file tree for this sub-area
~~~text
docs/
└── 📁 patterns/                                        # Pattern library (implementation guidance)
    └── 📁 provenance/                                  # Provenance & lineage (PROV-O aligned)
        ├── 📄 README.md                                # Main provenance pattern (policy + guidance)
        ├── 📁 examples/                                # CI-safe examples (generalized locations)
        │   ├── 📄 prov_bundle.example.jsonld           # Minimal PROV bundle (example)
        │   ├── 📄 stac_item_with_prov.example.json     # STAC Item linking provenance asset
        │   └── 📄 dcat_dataset_with_prov.example.ttl   # DCAT dataset/distribution w/ PROV links
        └── 📁 templates/                               # Copy/paste templates (this folder)
            ├── 📄 README.md                            # Template usage + conventions
            ├── 📄 run_manifest.template.yaml           # Run manifest skeleton (machine-facing)
            └── 📄 provenance_note.template.md          # Optional human note (review + context)
~~~

## 🧭 Context

### Background
KFM treats provenance as a **first-class governance artifact**: every derived output should be traceable to inputs, activities, and agents. These templates reduce drift and help keep lineage capture consistent across pipelines and teams.

### Assumptions
- Pipelines are deterministic/idempotent.
- Runs have a stable `run_id`.
- Provenance artifacts must be safe for CI (no secrets, no sensitive coordinates).

### Constraints / invariants
- The canonical ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The UI does **not** access the graph directly; provenance is served via APIs.
- Provenance must not be “filled in” by inference; it must reflect recorded pipeline facts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Is the run manifest canonical format JSON, YAML, or both? | Pipeline owner | TBD |
| Is there a standardized `run_id` schema and collision policy? | Governance + pipelines | TBD |

### Future extensions
- Add a `prov_bundle.template.jsonld` if the project wants a standardized PROV bundle skeleton (separate from examples).
- Add schema validation docs for the manifest/prov bundle if schemas exist under `schemas/`.

## 🗺️ Diagrams

### Template-to-artifact lifecycle
~~~mermaid
flowchart LR
  T1[run_manifest.template.yaml] --> M[mcp/runs/&lt;run_id&gt;/run_manifest.*]
  T2[provenance_note.template.md] --> N[mcp/runs/&lt;run_id&gt;/provenance_note.md]
  M --> P[mcp/runs/&lt;run_id&gt;/prov.jsonld]
  P --> S[STAC/DCAT references]
  S --> G[Graph ingest]
  G --> A[API layer]
  A --> U[UI / Story Nodes / Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source entity references | IDs/URIs | STAC/DCAT/source registry | Resolve + checksum present |
| Pipeline config reference | Path/URI | Repo config | Must not include secrets |
| Code revision | commit SHA | VCS | Must be recorded |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run manifest | YAML/JSON | `mcp/runs/<run_id>/run_manifest.*` | Schema (if present) |
| PROV bundle | JSON-LD | `mcp/runs/<run_id>/prov.jsonld` | PROV-O aligned |
| Provenance note | Markdown | `mcp/runs/<run_id>/provenance_note.md` | Markdown lint |

### Sensitivity & redaction
- Do not include exact coordinates for sensitive or culturally protected sites.
- Prefer generalized geometry references and/or redacted fields, per governance.

### Quality signals
- Presence of checksums for all outputs (or a referenced `checksums.sha256` file).
- Stable IDs for entities and activities.
- Manifest completeness: inputs, outputs, agents, config references.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Provenance should be linked via STAC `assets` or `links` (e.g., `assets.provenance` → `prov.jsonld`) as defined in the provenance pattern.

### DCAT
- DCAT dataset/distribution metadata can reference provenance using PROV terms (e.g., `prov:wasGeneratedBy`, `prov:wasDerivedFrom`) as defined in the provenance pattern.

### PROV-O
- Minimum: `prov:Entity`, `prov:Activity`, `prov:Agent`
- Required relations for derived outputs:
  - `prov:wasDerivedFrom` (input lineage)
  - `prov:wasGeneratedBy` (activity/run linkage)

### Versioning
- Versioned entities should support predecessor/successor semantics in catalogs and in the graph (implementation-specific; see `../README.md`).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV outputs | JSON/Turtle/JSON-LD |
| Graph | Lineage edges | Ingest jobs (no UI direct access) |
| APIs | Serve contracted provenance views | REST/GraphQL |
| UI | Render provenance summaries | API calls only |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Doc template | `docs/templates/` | Semver for template changes |
| Provenance pattern | `docs/patterns/provenance/` | Semver for governed changes |
| Run artifacts | `mcp/runs/<run_id>/` | Immutable per run; corrections = new run/version |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Nodes should reference the underlying source entities and the generating activity/run when derived from analysis.
- Focus Mode should only consume provenance-linked content (no fabricated relationships).

### Provenance-linked narrative rule
- Every narrative claim must trace to an entity/document ID and (when derived) to a run/activity ID.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (headers, fencing, no broken structure)
- [ ] Template file presence checks (paths exist as documented)
- [ ] Schema validation for STAC/DCAT/PROV where validators exist
- [ ] Security scanning (no secrets; no sensitive coords)

### Reproduction
~~~bash
# Placeholders — replace with repo-specific commands
# 1) validate markdown + links
# 2) validate STAC/DCAT/PROV outputs
# 3) run unit/integration tests
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to templates that affect required provenance fields: governance review recommended.
- Any example content that could expose sensitive locations: sovereignty review required.

### CARE / sovereignty considerations
- Do not weaken protections through “helpful” added detail.
- Prefer “least disclosure” and explicit approvals for protected sources.

### AI usage constraints
- Allowed: summarization/structure extraction for navigation
- Prohibited: inventing provenance, adding speculative relations, inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial templates README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

