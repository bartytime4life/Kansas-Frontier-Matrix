---
title: "Data Work Notes — README"
path: "data/work/_notes/README.md"
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

doc_uuid: "urn:kfm:doc:data:work-notes-readme:v1.0.0"
semantic_document_id: "kfm-data-work-notes-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work-notes-readme:v1.0.0"
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

# Data Work Notes — README

## 📘 Overview

### Purpose

- Define what belongs in `data/work/_notes/` and what must never land here.
- Provide a lightweight, repeatable structure for run notes, QA findings, and human decisions made during the **work** stage of the data lifecycle.
- Ensure notes remain **evidence-first**: they must point to canonical artifacts (STAC/DCAT/PROV) rather than becoming a parallel source of truth.

### Scope

| In Scope | Out of Scope |
|---|---|
| Human-authored notes about intermediate artifacts in `data/work/` | Raw source snapshots (must live under `data/raw/`) |
| QA findings, anomaly tracking, and transformation decisions | Final datasets intended for publication (must live under `data/processed/`) |
| Pointers to PROV bundles, run manifests, dataset IDs, and catalog entries | Canonical STAC/DCAT/PROV JSON artifacts (must live under `data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| Minimal, sanitized samples for debugging when safe | Secrets, credentials, private keys, tokens |
| Redaction/generalization notes for later enforcement in API/UI | Any content that attempts to infer or disclose sensitive locations |

### Audience

- Primary: KFM maintainers working in ETL and data QA.
- Secondary: Catalog/graph/API maintainers who need context for why a dataset looks the way it does.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Raw**: immutable input snapshots captured for reproducibility.
  - **Work**: intermediate transformations and staging outputs.
  - **Processed**: published/derived datasets suitable for cataloging and graph ingest.
  - **Run ID**: stable identifier for a pipeline execution.
  - **PROV bundle**: canonical lineage artifact stored under `data/prov/`.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/_notes/README.md` | Maintainers | Folder contract and hygiene rules |
| Work notes | `data/work/_notes/**/*.md` | Maintainers | Must reference run IDs + provenance |
| Work-stage artifacts | `data/work/` | ETL | Intermediate outputs and staging |
| Processed outputs | `data/processed/` | ETL | Published/derived datasets |
| STAC catalogs | `data/stac/` | Catalog | Collections + items only |
| DCAT records | `data/catalog/dcat/` | Catalog | Dataset/distribution metadata |
| PROV bundles | `data/prov/` | ETL/Catalog | Activity + agent + entity lineage |
| Pipelines | `src/pipelines/` | ETL | Code that produces artifacts |
| Story Nodes | `docs/reports/story_nodes/` | Editors | Curated narratives, provenance-linked |

### Definition of done

- [ ] Front-matter complete and valid
- [ ] Notes content is non-sensitive and contains no secrets or PII
- [ ] Any claims about data changes include links to run IDs and referenced artifact IDs
- [ ] Validation steps are listed and repeatable
- [ ] Governance and CARE/sovereignty considerations are explicit when applicable

## 🗂️ Directory Layout

### This document

- `path`: `data/work/_notes/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Raw inputs | `data/raw/` | Immutable input snapshots |
| Work stage | `data/work/` | Intermediate/working outputs |
| Processed outputs | `data/processed/` | Published/derived datasets |
| STAC | `data/stac/` | Collections + items for assets |
| DCAT | `data/catalog/dcat/` | Dataset/distribution metadata |
| PROV | `data/prov/` | Provenance bundles for runs |
| Pipelines | `src/pipelines/` | ETL + transforms |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API boundary | `src/server/` | Contracts + endpoints + redaction |
| UI | `web/` | React/Map clients |
| Story Nodes | `docs/reports/story_nodes/` | Narrative layer |

### Expected file tree for this sub-area

~~~text
📁 data/
├─ 📁 raw/
├─ 📁 work/
│  ├─ 📁 _notes/
│  │  ├─ 📄 README.md
│  │  ├─ 📁 runs/          # optional: run-scoped notes
│  │  ├─ 📁 datasets/      # optional: dataset-scoped notes
│  │  └─ 📁 qa/            # optional: QA findings and checks
│  └─ …
├─ 📁 processed/
├─ 📁 stac/
├─ 📁 catalog/
│  └─ 📁 dcat/
└─ 📁 prov/
~~~

### File naming

Recommended patterns for note files:

- Run notes: `data/work/_notes/runs/YYYY-MM-DD__<pipeline>__run-<run_id>.md`
- Dataset notes: `data/work/_notes/datasets/<dataset_id>/YYYY-MM-DD__<topic>.md`
- QA notes: `data/work/_notes/qa/YYYY-MM-DD__<dataset_or_run>__<check>.md`

If the repo already defines a canonical naming scheme elsewhere, that standard overrides these suggestions.

### Suggested note template

~~~markdown
---
title: "Work note — <short topic>"
date: "YYYY-MM-DD"
status: "draft"
run_id: "<run-id>"
prov_activity_id: "<prov-activity-id>"
inputs:
  - "<input artifact id or path>"
outputs:
  - "<output artifact id or path>"
risks:
  - "<privacy/sensitivity risk or NONE>"
---

## Summary
- What happened and why.

## Observations
- What changed or what was discovered.

## Decisions
- Decision, rationale, alternatives considered.

## Validation
- Checks run and outcomes.

## Next steps
- What is needed to move from work → processed or to close the issue.
~~~

## 🧭 Context

### Background

KFM’s data lifecycle expects a staged flow from **raw → work → processed**, followed by cataloging and provenance artifacts. The `_notes` folder exists so humans can record decisions and QA context during the work stage without turning those notes into “shadow truth”.

### Assumptions

- Work-stage outputs are reproducible from raw inputs plus pipeline code/config.
- Canonical lineage lives in PROV bundles; notes link to those IDs rather than duplicating them.
- Catalog artifacts (STAC/DCAT) remain machine-validated and do not live in documentation directories.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI never reads the graph directly; access is via contracted APIs only.
- Notes must not introduce sensitive location inference or disclose restricted details.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should note files be scaffolded automatically during ETL runs | TBD | TBD |
| Should `run_id` format be standardized repo-wide | TBD | TBD |
| Should `_notes` be indexed into a lightweight search artifact | TBD | TBD |

### Future extensions

- Auto-generate run-scoped note stubs linked to PROV activity IDs.
- Optionally convert selected note fields into structured telemetry or run manifests.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[data/raw] --> B[ETL pipelines]
  B --> C[data/work]
  C --> N[data/work/_notes]
  C --> D[data/processed]
  D --> E[STAC/DCAT/PROV catalogs]
  E --> F[Graph ingest]
  F --> G[APIs]
  G --> H[UI]
  H --> I[Story Nodes]
  I --> J[Focus Mode]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant ETL as ETL Pipeline
  participant WORK as data/work
  participant NOTES as data/work/_notes
  participant PROV as data/prov

  ETL->>WORK: write intermediate artifacts
  ETL->>PROV: write provenance bundle (activity + entities)
  ETL->>NOTES: add or update human note (run_id + prov_activity_id)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Run context | ID strings + metadata | Pipeline execution | Must include run_id and provenance link |
| Work artifacts | Files | `data/work/` | Basic sanity checks as appropriate |
| Catalog/prov references | IDs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | IDs must resolve to real artifacts |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Work notes | Markdown | `data/work/_notes/**/*.md` | Human-readable; do not replace canonical artifacts |

### Sensitivity & redaction

- Do not include credentials, tokens, private keys, or personal information.
- Do not include precise sensitive locations. If location discussion is required, use the same generalization level expected at the API boundary.

### Quality signals

Recommended fields to capture in notes when relevant:

- Record counts before/after transformation
- Schema validation result summaries
- Geometry validity checks and exceptions
- Known missingness or bias notes
- Any redaction/generalization applied or required downstream

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Notes may reference STAC Collection/Item IDs.
- Notes must not become the canonical home for STAC JSON.

### DCAT

- Notes may reference DCAT dataset IDs/distributions.
- Notes must not replace DCAT metadata mapping.

### PROV-O

- Run-scoped notes should reference:
  - `prov:wasDerivedFrom` source IDs or artifact IDs
  - `prov:wasGeneratedBy` activity ID
  - Agent identity where appropriate

### Versioning

- If a note references a dataset version, specify it explicitly.
- If a new version is created, link it to predecessor/successor relationships through canonical artifacts rather than through narrative alone.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Work stage | Intermediate artifacts | Files under `data/work/` |
| Notes | Human context | Markdown under `data/work/_notes/` |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j | Served via API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Provenance-linked content |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Catalog artifacts | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Stable identifiers required |

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- By default, `_notes` do not surface directly in Focus Mode.
- Notes can inform curation, QA, and editorial decisions, but final narrative must cite canonical datasets/documents and provenance IDs.

### Provenance-linked narrative rule

- Every claim that becomes user-facing must trace to a dataset, record, or asset ID that resolves through STAC/DCAT/PROV and the API boundary.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Secret and PII scanning gates
- [ ] If notes include referenced IDs, verify they resolve to real artifacts
- [ ] Security and sovereignty checks when notes mention sensitive content

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Notes created/updated | Maintainers | `data/work/_notes/` (git history) |
| Run provenance | ETL | `data/prov/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Notes that introduce or discuss sensitive sources, locations, or communities require review per governance docs.
- If a note becomes the basis for a public Story Node, editorial review is required.

### CARE / sovereignty considerations

- Identify impacted communities and follow any protection, redaction, or generalization rules that apply.
- Treat culturally sensitive content as high-risk by default and escalate for human review.

### AI usage constraints

- Only use AI transforms consistent with the front-matter permissions.
- AI must not be used to infer sensitive locations or create new policy text.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-28 | Initial README for `data/work/_notes/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

