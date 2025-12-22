---
title: "Tools — AI Explainability (README)"
path: "tools/ai/explainability/README.md"
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

doc_uuid: "urn:kfm:doc:tools:ai:explainability:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-explainability-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:explainability:readme:v1.0.0"
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

# Tools — AI Explainability (README)

## 📘 Overview

### Purpose
This directory documents **how KFM produces explainability artifacts** for AI outputs (e.g., model predictions, suggested links, classifications), and how those artifacts are stored as **auditable evidence** alongside run metadata.

Explainability here is treated as **governance support**: it helps curators and auditors answer *“why did the AI do that?”* for a specific model run and output.

### Scope

| In Scope | Out of Scope |
|---|---|
| Generating explanation artifacts for model outputs (feature attribution, local examples, error slices) | Training/retraining models (belongs in model training pipeline docs) |
| Producing an “AI validation report” per run (summary + links to artifacts) | Production UI rendering logic (belongs in `web/`) |
| Provenance tagging & linking explanations to model/version/run IDs | Bypassing human review for critical AI-derived content |
| Redaction/generalization of sensitive fields in explainability outputs | Direct UI-to-graph reads (contracts live at the API boundary) |

### Audience
- **Primary:** AI/pipeline contributors, reviewers, auditors, curators
- **Secondary:** API/UI contributors integrating “explanation” panels, maintainers of telemetry/governance metrics

### Definitions
- Glossary: **not confirmed in repo** (expected: `docs/glossary.md`)
- Terms used in this doc:
  - **Explainability artifact:** Any file(s) that justify/interpret an AI output (e.g., SHAP-style attributions, local rationales, error analysis).
  - **AI validation report:** A per-run report that summarizes model outputs + checks + links to the explainability artifacts.
  - **Evidence artifact:** Downstream-consumable outputs with provenance (e.g., PROV-linked reports/assets).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline + invariants |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM maintainers | Doc structure + front-matter |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review + policy anchors |
| PROV outputs | `data/prov/` | DataOps | Lineage for runs + derived artifacts |
| MCP artifacts | `mcp/` | AI/DataOps | Experiments, model cards, SOPs |
| Explainability tools | `tools/ai/explainability/` | AI | This folder |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] No broken links (CI doc lint / markdown protocol)
- [ ] Clearly states where explainability outputs live (paths + conventions)
- [ ] Explicitly states provenance + redaction requirements
- [ ] Includes repeatable validation steps (even if placeholders)

---

## 🗂️ Directory Layout

### This document
- `path`: `tools/ai/explainability/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tools | `tools/` | Dev + analysis utilities (non-production) |
| AI tools (this) | `tools/ai/explainability/` | Scripts/notebooks for explainability + report generation |
| Pipelines | `src/pipelines/` | Deterministic ETL + transforms (if explainability is wired into pipelines) |
| PROV bundles | `data/prov/` | Lineage for AI runs + generated artifacts |
| STAC/DCAT | `data/stac/`, `data/catalog/dcat/` | Catalog entries if explainability outputs are published as evidence products |
| API boundary | `src/server/` | Contracted access layer that can surface explanation links |
| UI | `web/` | Focus Mode rendering + “AI explanation” affordances |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area (recommended)
~~~text
📁 tools/
└── 📁 ai/
    └── 📁 explainability/
        ├── 📄 README.md
        ├── 📁 configs/                 # not confirmed in repo
        ├── 📁 notebooks/               # not confirmed in repo
        ├── 📁 scripts/                 # not confirmed in repo
        ├── 📁 schemas/                 # not confirmed in repo
        └── 📁 examples/                # not confirmed in repo
~~~

---

## 🧭 Context

### Where explainability fits in the pipeline
Explainability work should attach to **specific model runs** and generate **reviewable evidence**:
- the explanation artifacts themselves (plots/json/html)
- a summarized **AI validation report** that links outputs back to:
  - model identifier + version
  - run identifier
  - input dataset(s) / record sets
  - provenance references

### Why this matters in KFM
KFM’s narrative and Focus Mode workflows must remain **provenance-first** and **human-reviewed** for critical AI-derived content. Explainability artifacts are a key part of the audit trail.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph AI["AI (Model Run)"]
    P["Predictions / Suggestions"] --> E["Explainability Artifacts"]
    E --> R["AI Validation Report (per run)"]
  end

  subgraph Prov["Lineage"]
    R --> PROV["PROV bundle (activity + entities)"]
  end

  subgraph Surfacing["Downstream Surfacing"]
    PROV --> API["API boundary (contracted links/refs)"]
    API --> UI["Focus Mode UI (optional explanation panel)"]
  end
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Model outputs (predictions, labels, suggested links) | JSON/CSV/etc. | run outputs | schema/shape checks |
| Features / tokens used by the model | model-specific | run inputs | redaction rules |
| Run manifest (model id/version, params, commit) | JSON/YAML | pipeline/MCP | required fields present |
| Ground truth / review labels (if available) | CSV/JSON | curation outputs | consistency checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Explainability artifacts (local/global) | PNG/SVG/JSON/HTML | **not confirmed in repo** (recommend `mcp/runs/<run_id>/explainability/`) | schema if standardized |
| AI validation report | Markdown/PDF/HTML | **not confirmed in repo** (recommend `mcp/runs/<run_id>/ai_validation_report.md`) | doc lint + required sections |
| PROV references | JSON/RDF | `data/prov/` | PROV profile validation (if present) |

### Sensitivity & redaction
- **Do not** output or infer sensitive locations.
- Generalize or omit:
  - personally identifying information (PII)
  - culturally sensitive locations/attributes
  - any restricted coordinates or site references (sovereignty rules)
- Ensure reports clearly label:
  - what is **model output**
  - what is **human-reviewed**
  - confidence/uncertainty (if applicable)

### Quality signals
Recommended checks (model/task dependent):
- Slice-based error analysis (time period, geography bins, doc type)
- Explanation stability (are top attributions robust across small perturbations?)
- Coverage (percent of outputs with usable explanations)
- Human disagreement rate (review overrides vs acceptances)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If explainability artifacts are treated as **evidence products**:
- consider attaching them as STAC item assets, or
- create a dedicated “evidence” collection for derived artifacts (not confirmed in repo)

### DCAT
If reports are published/curated as datasets:
- register them as DCAT datasets with clear license + publisher mapping (not confirmed in repo)

### PROV-O
Minimum expectation:
- explanations and validation reports should be PROV **Entities**
- generated by a PROV **Activity** representing the model run
- linked to source inputs via `prov:wasDerivedFrom`
- include model/version identifiers and run IDs as metadata

### Versioning
- Report/version should be tied to:
  - code commit SHA
  - model version
  - dataset version/IDs
  - run ID
- Avoid “floating” explanations without immutable references.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Explainability tool | Generate explanation artifacts | CLI / notebook / script |
| Run manifest | Persist run metadata | file + schema |
| PROV writer | Record lineage | output to `data/prov/` |
| API boundary (optional) | Serve links/refs to reports | REST/GraphQL |
| UI (optional) | Render “AI explanation” affordance | API calls |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Run manifest schema | **not confirmed in repo** (recommend `schemas/ai/run_manifest.schema.json`) | semver + changelog |
| Explainability artifact schema (if any) | **not confirmed in repo** | semver + compatibility notes |
| API schema (if surfacing) | `src/server/` + docs | contract tests required |

### Extension points checklist (for future work)
- [ ] Define/confirm canonical output locations for explainability artifacts
- [ ] Define/confirm run manifest schema + required IDs
- [ ] Add PROV bundle generation (activity/entity/agent) for explainability outputs
- [ ] Add API endpoint(s) to fetch report metadata (if needed)
- [ ] Add UI rendering for “AI explanation” (if needed)
- [ ] Add telemetry: explanation coverage, override rates, drift signals

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
If Focus Mode shows AI-assisted content:
- provide a way to view:
  - **what evidence** backed the output (citations/provenance)
  - **what the model emphasized** (explainability artifact summary)
  - **who approved/edited** it (human-in-the-loop audit)

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- AI explanations must link back to the run + model/version that produced them.

### Focus Mode behavior expectations (if present)
- “AI explanation” toggle shows:
  - link to AI validation report
  - summary of top attributions / rationale
  - warnings when explanation is unavailable or low confidence

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (doc lint)
- [ ] If schemas exist: validate run manifest + artifact schemas
- [ ] If PROV is emitted: validate PROV bundle integrity
- [ ] If API endpoints exist: contract tests
- [ ] Security + sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) generate explanations for a run
# python tools/ai/explainability/scripts/explain_run.py --run-id <RUN_ID>

# 2) write/update AI validation report
# python tools/ai/explainability/scripts/write_report.py --run-id <RUN_ID>

# 3) validate docs + schemas
# make lint
# make validate-schemas
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Explanation coverage (%) | explainability tool outputs | `docs/telemetry/` + `schemas/telemetry/` |
| Human override rate | curation/admin UI logs | `docs/telemetry/` + `schemas/telemetry/` |
| Drift / error spikes | eval pipeline | `docs/telemetry/` + `schemas/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Explainability outputs that may influence narrative or public-facing content should be reviewed by:
  - historian/editor (narrative correctness)
  - governance reviewer (CARE/sovereignty)
  - security reviewer (if sensitive fields appear)

### CARE / sovereignty considerations
- Identify impacted communities and apply protection rules before publishing any explanation artifacts.
- Avoid publishing raw text snippets or coordinates if they risk revealing sensitive information.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions align with repo policy.
- Do not imply prohibited actions (e.g., inferring sensitive locations).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for explainability tooling | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
