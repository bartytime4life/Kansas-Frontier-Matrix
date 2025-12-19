---
title: "KFM — src/ai README"
path: "src/ai/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:src:ai:readme:v1.0.0"
semantic_document_id: "kfm-src-ai-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:ai:readme:v1.0.0"
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

# src/ai

## 📘 Overview

### Purpose
This directory contains **AI components** used by KFM to:
- generate **evidence products** (analysis artifacts) and **draft narrative outputs** that can be reviewed and incorporated into Story Nodes / Focus Mode, and/or
- enrich ingested assets (e.g., tags, entity links), **without breaking provenance-first guarantees**.

This README documents **what belongs here**, **what does not**, and the **contracts/invariants** AI code must respect.

### Scope

| In Scope | Out of Scope |
|---|---|
| Model/prompt wrappers, deterministic post-processing, confidence/uncertainty annotation, explainability hooks, evaluation harnesses, redaction helpers | UI rendering, direct Neo4j access from UI, graph ontology definitions, “policy writing” |
| AI-generated **evidence artifacts** that can be cataloged + linked into graph + surfaced via API | Publishing uncited narrative directly to users |
| AI support code for ETL/graph ingestion (e.g., entity resolution suggestions) | Replacing curated sources; bypassing curator review |

### Audience
- Primary: AI/ML engineers, pipeline engineers, graph/API engineers
- Secondary: curators/reviewers validating drafts and evidence artifacts

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Evidence artifact**: a derived, versioned output (e.g., tags, links, summaries, analytics results) that can be traced to input sources and a transformation run.
  - **Provenance**: references/IDs that allow tracing outputs back to sources and transformations (STAC/DCAT/PROV + graph lineage).
  - **Uncertainty / confidence metadata**: numerical or categorical indicators attached to AI-derived outputs.
  - **Story Node**: a narrative capsule linked to underlying sources and datasets.
  - **Focus Mode**: an immersive view that only surfaces content with provenance and, if AI-derived content is shown, does so explicitly and (where applicable) opt-in.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical ordering + invariants) | `docs/MASTER_GUIDE_v12.md` | KFM | Source of truth for pipeline ordering + extension matrix |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | KFM | Policy entry point (must exist for enforcement) |
| Ethics | `docs/governance/ETHICS.md` | KFM | Constraints for AI behavior + review expectations |
| Sovereignty | `docs/governance/SOVEREIGNTY.md` | KFM | Rules for sensitive/culturally restricted content |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM | Narrative formatting + provenance requirements |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM | If AI outputs are exposed via API |
| Model Cards | `mcp/model_cards/` *(not confirmed in repo)* | KFM | Add one per model/prompt family |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory responsibilities + invariants are explicit
- [ ] Contributor checklist exists for new AI components
- [ ] Clear link-outs to governance + Master Guide
- [ ] “Not confirmed in repo” items are clearly marked as such

## 🗂️ Directory Layout

### This document
- `path`: `src/ai/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Pipelines | `src/pipelines/` | ETL + catalog builds; calls into AI as needed |
| Graph | `src/graph/` | Ontology bindings + graph build; consumes AI-enriched outputs |
| APIs | `src/server/` *(per Master Guide; not confirmed in repo)* | Contracted access layer; surfaces AI outputs with provenance |
| Schemas | `schemas/` | JSON schemas for AI outputs, telemetry, contracts |
| Story nodes | `docs/reports/./story_nodes/` *(per Master Guide; not confirmed in repo)* | Narrative artifacts with provenance |
| MCP | `mcp/` | Experiments, run logs, model cards, SOPs |

### Expected file tree for this sub-area
*(Only `README.md` is confirmed by this change; other folders are suggested conventions and must match the actual repo before adoption.)*

~~~text
📁 src/
└── 📁 ai/
    ├── 📄 README.md
    ├── 📁 models/                (not confirmed in repo)
    ├── 📁 prompts/               (not confirmed in repo)
    ├── 📁 pipelines/             (not confirmed in repo)
    ├── 📁 eval/                  (not confirmed in repo)
    ├── 📁 explainability/        (not confirmed in repo)
    └── 📁 redaction/             (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM’s AI layer exists to add **discoverability**, **enrichment**, and **draft narrative generation** while maintaining strict governance:
- Enrich assets with tags/annotations (e.g., image/map tags) so they are more searchable and linkable.
- Suggest entity linking/merges with confidence, keeping a clean graph as new data arrives.
- Produce draft story narratives or summaries as *drafts* for human review.
- Produce explainability + validation artifacts to keep AI auditable.

### Assumptions
- AI outputs are treated as **derived data products** and must be stored/versioned like other artifacts.
- User-facing experiences should only consume AI outputs through **APIs** and only when provenance requirements are satisfied.
- Human review is required for any AI output that changes meaning, merges entities, or drafts narrative intended for user consumption.

### Constraints / invariants (non-negotiable)
- **Canonical ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary:** UI consumes graph/AI outputs via API contracts (no direct graph dependency).
- **No unsourced narrative:** anything surfaced in narrative contexts must carry provenance refs.
- **AI-derived content must be explicit:** include confidence/uncertainty fields and flags that indicate “AI-derived vs source-derived.”
- **Sovereignty / sensitive content:** do not infer or expose sensitive locations; apply governance gating.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where are model cards stored (repo path + required fields)? | TBD | TBD |
| What is the canonical API folder (`src/server/` vs `src/api/`)? | TBD | TBD |
| What schema registry governs AI evidence artifacts? | TBD | TBD |

### Future extensions
- New **AI evidence product** types (e.g., annotation layers, link predictions, thematic clusters), each with:
  - schema + validation
  - provenance (PROV activity/agent)
  - versioning + reproducible run configs
  - curator review loop where applicable

## 🗺️ Diagrams

### AI in the KFM canonical pipeline
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph AI["AI components (src/ai)"]
    X[Extract / Classify / Link] --> Y[Evidence artifacts + confidence]
    Y --> Z[Validation + explainability artifacts]
  end

  A -. calls .-> X
  X -. writes derived outputs .-> B
  Z -. audit refs .-> B
  C -. stores confidence + lineage .-> C
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source documents / transcripts | text / json | `data/raw/` *(not confirmed in repo)* | schema + encoding checks |
| Images / maps | raster | `data/raw/` *(not confirmed in repo)* | STAC asset validation |
| Graph candidates | node/edge sets | `src/graph/` ingestion | ontology constraints |
| Run configuration | yaml/json | `configs/` *(not confirmed in repo)* | pinned versions |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Asset tags / annotations | json | `data/processed/` *(not confirmed in repo)* | `schemas/` *(not confirmed in repo)* |
| Entity-link suggestions | json/csv | `data/processed/` *(not confirmed in repo)* | `schemas/` *(not confirmed in repo)* |
| Evidence artifacts (analysis products) | json + assets | `data/processed/` + `data/stac/` *(not confirmed in repo)* | STAC + local schema |
| AI validation report | md/json | `mcp/runs/` *(not confirmed in repo)* | telemetry schema |

### Sensitivity & redaction
- Any AI-derived output that could reveal a restricted location or culturally sensitive knowledge must be generalized or omitted per governance docs.
- Prefer “coarse geometry”/generalized place references for public outputs when sensitivity is unclear.

### Quality signals
- Confidence/uncertainty fields are mandatory for AI-derived outputs.
- Evaluation gates should include regression tests on curated “golden” examples (not confirmed in repo).
- Drift checks and provenance completeness checks are required for recurring pipelines (not confirmed in repo).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- AI evidence artifacts should be representable as STAC Items/Assets (or linked from existing Items) so the derived outputs are discoverable and validated.

### DCAT
- If AI outputs are published as datasets, they must receive stable dataset identifiers and license mappings consistent with governance.

### PROV-O
- Each AI run should record:
  - `prov:Activity` = the transformation run
  - `prov:Agent` = model + version (and human reviewer, where applicable)
  - `prov:wasDerivedFrom` = input sources
  - `prov:wasGeneratedBy` = run activity

### Versioning
- AI outputs must be reproducible from pinned configs and stable IDs.
- If a model/prompt changes materially, outputs must be version-bumped and linked to predecessors.

## ✅ Contributor checklist (when adding/modifying AI code)
- [ ] Add/extend **schema** for output payloads + validate it in CI
- [ ] Attach **provenance refs** (source IDs + run IDs)
- [ ] Attach **confidence/uncertainty metadata** and “AI-derived” flags
- [ ] Create/update **model card** (or prompt card) with limitations
- [ ] Add **evaluation tests** (goldens + regression)
- [ ] Ensure **human review workflow** exists for merges/story drafts
- [ ] Ensure **API contract** exists if output is user-facing

## 🧾 Version history
| Version | Date | Change summary |
|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `src/ai` (scope + invariants + contributor checklist) |