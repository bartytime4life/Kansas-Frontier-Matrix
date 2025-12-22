---
title: "MCP Model Cards — README"
path: "mcp/model_cards/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:mcp:model-cards:readme:v1.0.0"
semantic_document_id: "kfm-mcp-model-cards-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:mcp:model-cards:readme:v1.0.0"
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

A model card is a compact, human-readable record of:
- the model’s architecture,
- training data (and how it was assembled),
- intended use,
- limitations / known failure modes,
- evaluation results (where applicable).

This supports responsible use and helps reviewers interpret model-derived outputs.

### Scope
Model cards should exist for any model that:
- produces **user-visible** content (e.g., summaries, classifications, suggested links),
- produces **AI-derived artifacts** that may be cataloged and surfaced in the UI,
- performs automated extraction or linking used to populate the graph (e.g., NER, entity resolution, change detection).

### Audience
- Pipeline developers & maintainers
- Data curators / editors
- Governance reviewers (ethics, sovereignty, security)
- Downstream users who need to understand what model outputs mean

### What this folder is not
- Not a storage location for large binaries (model weights, huge logs, datasets).
- Not a substitute for STAC/DCAT/PROV lineage records (those remain the canonical provenance layer).

---

## 🗂️ Directory Layout

### Where model cards live
- Markdown: `mcp/model_cards/`
- This README: `mcp/model_cards/README.md`

### Recommended sub-structure
~~~text
📁 mcp/
├── 📁 model_cards/
│   ├── 📄 README.md
│   ├── 📁 <model_id>/
│   │   ├── 📄 MODEL_CARD.md
│   │   ├── 📁 eval/
│   │   │   ├── 📄 report.md
│   │   │   └── 📄 metrics.json
│   │   ├── 📁 configs/
│   │   │   ├── 📄 training.yaml
│   │   │   └── 📄 inference.yaml
│   │   └── 📄 CHANGELOG.md
│   └── 📄 INDEX.md  (optional; curated list of active models)
~~~

### Related repository paths
- `mcp/experiments/` — experiment logs/results
- `mcp/sops/` — SOPs for retraining, updating, or deploying models
- `mcp/runs/` — run manifests / pipeline artifacts (if used in this repo)
- `docs/` — general documentation
- `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` — catalog + provenance outputs

---

## 🧭 Context

### How model cards fit KFM’s architecture
KFM’s pipeline is layered (ETL → Catalogs/Provenance → Graph → API → UI → Story/Focus). Model cards sit in the **AI layer documentation** and must align with provenance and governance controls.

When a model produces outputs that affect the graph, APIs, or user-visible content:
- provenance must identify the model version that generated the artifact,
- outputs must be linkable to evidence IDs,
- predictive / inferential content must be opt-in and labeled with uncertainty.

### When to create or update a model card
Create a model card when:
- introducing a new model or major version,
- changing training data, preprocessing, or objectives,
- changing evaluation methodology or metrics,
- promoting a model from “prototype” to “production” use.

Update a model card when:
- changing runtime configuration in a way that affects outputs (thresholds, prompts, post-processing),
- discovering new limitations or bias risks,
- deprecating or replacing a model.

---

## 🧩 Pipeline Integration

### Inputs
A model card should reference (not necessarily store) the following:
- **Training/finetuning data**: dataset IDs (STAC/DCAT), versions, filters
- **Source corpora**: document sets, map layers, or annotated samples (with IDs)
- **Code & configuration**: commit SHA, config files, dependency pins
- **Execution environment** (optional but recommended): hardware class, runtime, container tag

### Outputs
A model card should provide pointers to:
- **Model artifacts** (where stored): weights/package tag, checksum, license
- **Evaluation artifacts**: metrics JSON, test set IDs, qualitative examples
- **Run lineage**: PROV activity IDs (training runs, evaluation runs)
- **Downstream products**: evidence layers, extracted entities, story-node drafts (if applicable)

### Sensitivity & redaction
If training/evaluation data includes:
- restricted locations,
- culturally sensitive knowledge,
- personal data,

the model card must:
- avoid reproducing sensitive details,
- describe generalization/redaction that is applied downstream,
- flag governance review triggers.

### Quality signals
Minimum recommended quality signals to include in each model card:
- evaluation metrics (precision/recall/etc.) on a defined test set
- coverage notes (time periods, regions, document types)
- failure modes and “do not use for …” statements
- confidence/uncertainty behavior (thresholds, calibration, what the score means)

---

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements
Model cards are **documentation**, but they must be consistent with the provenance layer:
- Training/evaluation runs should have a `prov:Activity` identifier.
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
- story nodes must still be evidence-led,
- model contributions must be marked (AI-generated vs curated),
- Focus Mode must only show provenance-linked content by default.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode rule
Any content derived from model outputs that is shown in Focus Mode:
- must have provenance (no uncited facts),
- must be opt-in if predictive/inferential,
- must present uncertainty/confidence metadata.

### Recommended UI affordances (if/when exposed)
- “Model details” link → model card summary (via API)
- “AI-generated” label + confidence indicator
- “View sources” panel that resolves to STAC/DCAT/PROV IDs

---

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] YAML front-matter matches the governed template keys
- [ ] Model ID + version are present and consistent with run logs / PROV
- [ ] Training/eval dataset references resolve to catalog entries (STAC/DCAT) where applicable
- [ ] No sensitive locations or restricted details are disclosed
- [ ] Limitations and intended uses are explicit
- [ ] Any user-visible AI outputs are described with opt-in + uncertainty behavior

---

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: TBD
- Security council review: TBD
- Historian/editor review: TBD

### Governance review triggers (non-exhaustive)
- New sensitive layers or restricted-location content
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints that expose model outputs

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for MCP model_cards | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`