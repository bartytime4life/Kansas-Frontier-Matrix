---
title: "MCP Model Cards — README"
path: "mcp/model_cards/README.md"
version: "v1.0.1"
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

doc_uuid: "urn:kfm:doc:mcp:model-cards:readme:v1.0.1"
semantic_document_id: "kfm-mcp-model-cards-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:mcp:model-cards:readme:v1.0.1"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "speculative_additions"
  - "infer_sensitive_locations"
  - "generate_policy"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# MCP Model Cards — README

## 📘 Overview

### Purpose
This directory contains **Model Cards** for AI/ML models used within the Kansas Frontier Matrix (KFM) pipeline.

A Model Card is a compact, human-readable record of:
- the model’s architecture / approach (at a level safe for sharing),
- training/finetuning and evaluation context (referenced by dataset IDs, not raw data),
- intended use and out-of-scope use,
- limitations / known failure modes,
- evaluation results (where applicable),
- governance and sensitivity constraints for downstream use.

Model Cards support reproducibility, review, and responsible interpretation of AI-derived outputs.

### Scope
Model cards SHOULD exist for any model that:
- produces **user-visible** content (summaries, classifications, suggested links),
- produces **AI-derived artifacts** that may be cataloged and surfaced in the UI,
- performs automated extraction or linking used to populate the graph (NER, entity resolution, change detection),
- drafts or enriches narrative components (Story Nodes / Focus Mode), even if a human editor is always required.

Model cards MAY exist for prototypes (recommended) but must exist for production use.

### What this folder is not
- Not a storage location for large binaries (model weights, huge logs, datasets).
- Not a substitute for STAC/DCAT/PROV lineage records (those remain the canonical provenance layer).
- Not a place to store secrets (keys, tokens) or restricted prompts.

### Audience
- Pipeline developers & maintainers
- Data curators / editors
- Governance reviewers (ethics, sovereignty, security)
- Downstream users who need to understand what model outputs mean

### Definitions
- **Model Card**: a governed document describing how a model is intended to be used, what it was evaluated on, and where it fails.
- **Model artifact**: the packaged model/prompt/config used for inference, referenced by version and checksum/digest.
- **Model-derived artifact**: an output that may be cataloged (STAC/DCAT) and must be traceable via PROV.
- **Provenance**: lineage describing inputs, activities (runs), agents, and outputs (PROV-O alignment).

### Key artifacts (what this folder points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Model Cards (per model) | `mcp/model_cards/<model_id>/MODEL_CARD.md` | Model owner | Required for deployed models |
| Evaluation report | `mcp/model_cards/<model_id>/eval/report.md` | Model owner | Human-readable summary of eval |
| Evaluation metrics | `mcp/model_cards/<model_id>/eval/metrics.json` | Model owner | Machine-readable metrics |
| Config snapshots | `mcp/model_cards/<model_id>/configs/*.yaml` | Model owner | No secrets; document thresholds/prompts |
| Model changelog | `mcp/model_cards/<model_id>/CHANGELOG.md` | Model owner | Required once production |
| Optional model index | `mcp/model_cards/INDEX.md` | MCP | Curated list of active models |

### Definition of done (for this README)
- [ ] Front-matter complete and consistent with the doc path and IDs
- [ ] Directory layout and naming rules are unambiguous
- [ ] Provenance alignment expectations are explicit (PROV activity + model version)
- [ ] Governance / sensitivity handling requirements are explicit
- [ ] Validation steps are listed and repeatable

---

## 🗂️ Directory Layout

### This document
- `mcp/model_cards/README.md` — directory contract, expectations, and workflow

### Related repository paths
- `mcp/experiments/` — experiment logs/results
- `mcp/sops/` — SOPs for retraining, promotion, rollback, incident handling
- `mcp/runs/` — run manifests / pipeline artifacts (if used in this repo)
- `docs/` — general documentation
- `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` — catalog + provenance outputs

### Expected file tree for this sub-area
~~~text
📁 mcp/
└── 📁 model_cards/
    ├── 📄 README.md
    ├── 📄 INDEX.md  (optional; curated list of active models)
    ├── 📁 <model_id>/
    │   ├── 📄 MODEL_CARD.md
    │   ├── 📁 eval/
    │   │   ├── 📄 report.md
    │   │   └── 📄 metrics.json
    │   ├── 📁 configs/
    │   │   ├── 📄 training.yaml
    │   │   └── 📄 inference.yaml
    │   └── 📄 CHANGELOG.md
~~~

---

## 🧭 Context

### Background
KFM’s canonical pipeline ordering is preserved end-to-end:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Model Cards sit in the **AI (MCP) documentation layer** and provide a human-readable counterpart to:
- STAC/DCAT/PROV provenance and catalog records,
- run manifests,
- model artifact versioning.

### Assumptions
- Any model output that influences graph structure, user-visible content, or story drafting must be **traceable by version**.
- Model outputs are treated as **derived artifacts** and do not become “facts” unless backed by evidence and provenance.
- Governance constraints (ethics, sovereignty, security) apply to model selection, evaluation data, and output surfacing.

### Constraints / invariants
- Frontend must not read Neo4j directly; UI only consumes model metadata through contracted APIs.
- Any narrative or summarization must remain evidence-led (no uncited facts).
- Sensitive locations, culturally sensitive knowledge, and personal data must not be disclosed in model cards or configs.
- Run logs and PROV records must identify the model version that generated artifacts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize a “minimum required sections” checklist for `MODEL_CARD.md`? | TBD | TBD |
| Do we require an `INDEX.md` registry for all active models? | TBD | TBD |
| Do we need a schema/validator for model cards? | TBD | TBD |

### Future extensions
- Add a simple completeness validator for `MODEL_CARD.md` in CI.
- Add a curated `INDEX.md` registry (active model IDs, status, latest eval date).
- Add a stable mapping from PROV activity IDs to model card paths.

---

## 🗺️ Diagrams

### Where model cards fit in KFM
~~~mermaid
flowchart LR
  A[ETL inputs] --> B[Catalog + Provenance]
  B --> C[Graph ingest]
  C --> D[API layer]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  M[Model Card] -. documents .-> X[Model / Prompt / Config]
  X --> Y[Inference run]
  Y --> Z[Derived artifacts]
  Z --> B
~~~

---

## 📦 Data & Metadata

### Inputs (what model cards must reference)
A model card should reference (not necessarily store) the following:
- **Training/finetuning data**: dataset IDs (STAC/DCAT), versions, filters
- **Source corpora**: document sets, map layers, annotated samples (with IDs)
- **Code & configuration**: commit SHA, config file paths, dependency pins (if tracked)
- **Execution environment** (recommended): hardware class, runtime/container tag

### Outputs (what model cards must point to)
A model card should provide pointers to:
- **Model artifacts** (where stored): weights/package tag, checksum, license
- **Evaluation artifacts**: metrics JSON, test set IDs, qualitative examples
- **Run lineage**: PROV activity IDs (training, evaluation, inference)
- **Downstream products**: evidence layers, extracted entities, story-node drafts (if applicable)

### Sensitivity & redaction
If training/evaluation data includes:
- restricted locations,
- culturally sensitive knowledge,
- personal data,

the model card must:
- avoid reproducing sensitive details,
- describe the redaction/generalization applied downstream,
- flag governance review triggers for promotion or public exposure.

### Quality signals
Minimum recommended quality signals to include in each model card:
- evaluation metrics (precision/recall/etc.) on a defined test set
- coverage notes (time periods, regions, document types)
- failure modes and explicit “do not use for …” statements
- confidence/uncertainty behavior (thresholds, calibration, what the score means)

---

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements
Model cards are documentation, but must remain consistent with the provenance layer:
- Training/evaluation/inference runs should have a `prov:Activity` identifier.
- Model-derived evidence products should be representable as STAC assets/items where relevant.
- DCAT mappings should exist for any packaged dataset/evidence product intended for export.

### Practical linkage
At minimum, each deployed model should have:
- a stable model identifier (used in PROV + logs),
- a model version string,
- a model card file path,
- a checksum reference for the released artifact.

---

## 🧱 Architecture

### How model cards are served
Model cards are stored in-repo for review and governance. If model card data needs to be shown in UI:
- serve it via the API layer (do not read internal stores directly),
- include only non-sensitive fields suitable for public display,
- link UI displays back to provenance/evidence IDs.

### Relationship to Story Nodes
If a model contributes to story-node drafting or enrichment:
- story nodes must remain evidence-led,
- model contributions must be marked (AI-generated vs curated),
- Focus Mode must default to provenance-linked content.

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Any Focus Mode content derived from model outputs must:
- resolve to evidence identifiers (STAC/DCAT/PROV),
- disclose that the content is AI-derived where applicable,
- carry uncertainty/confidence metadata.

### Provenance-linked narrative rule
- No uncited facts.
- Any inferential or predictive content must be opt-in and explicitly labeled.
- Editors/curators must have a clear correction path when model outputs are wrong.

### Optional structured controls
Recommended UI affordances (if/when exposed):
- “Model details” link → model card summary (via API)
- “AI-generated” label + confidence indicator
- “View sources” panel that resolves to STAC/DCAT/PROV IDs

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] YAML front-matter matches governed keys and doc path
- [ ] Model ID + version are present and consistent with run logs / PROV
- [ ] Training/eval dataset references resolve to catalog entries (where applicable)
- [ ] No sensitive locations or restricted details are disclosed
- [ ] Limitations and intended uses are explicit
- [ ] User-visible AI outputs are described with opt-in + uncertainty behavior

### Reproduction
This repo may provide standardized commands/scripts; if so, document them here when available:
- schema validation (STAC/DCAT/PROV)
- doc linting (KFM-MDP)
- unit/integration tests for MCP pipelines and API contracts

### Telemetry signals (if applicable)
- Drift indicators for extraction/classification quality
- Error rates for entity resolution/linking
- Human correction rates and reversal/rollback events
- Coverage gaps (regions/time periods/document types)

---

## ⚖ FAIR+CARE & Governance

### Review gates
Approvals may be required depending on sensitivity and exposure:
- FAIR+CARE council review: TBD
- Security council review: TBD
- Historian/editor review: TBD

### CARE / sovereignty considerations
- Treat culturally sensitive knowledge as high-risk by default.
- If a model could expose restricted locations or sensitive entities, require governance review before promotion.
- Ensure redaction/generalization behavior is documented and testable.

### AI usage constraints
This folder must not contain:
- secrets/credentials,
- private prompts with restricted content,
- unredacted sensitive training/evaluation text,
- instructions that imply prohibited behavior (e.g., inferring sensitive locations).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for MCP model_cards | TBD |
| v1.0.1 | 2025-12-28 | Format upgrade: aligned to KFM Universal governed doc structure; clarified provenance + governance rules | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
