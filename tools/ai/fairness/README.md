---
title: "KFM AI Fairness Toolkit — README"
path: "tools/ai/fairness/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Tooling"
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

doc_uuid: "urn:kfm:doc:tools:ai:fairness:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-fairness-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:fairness:readme:v1.0.0"
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

# KFM AI Fairness Toolkit — README

## 📘 Overview

### Purpose

- This README defines conventions and expected behavior for **fairness + harm evaluation** of AI components used anywhere in the KFM pipeline (extraction, classification, summarization, narrative assistance).
- It governs **inputs, outputs, provenance expectations, and review gates** for fairness reporting so downstream systems can treat fairness artifacts as evidence (not anecdotes).

### Scope

| In Scope | Out of Scope |
|---|---|
| Evaluation suites for AI outputs (sliced metrics, harm checks, reporting) | Training/fine-tuning models |
| Reproducible run artifacts + provenance capture for evaluations | Making or changing governance policy (must live under `docs/governance/`) |
| CI-friendly gating hooks (threshold checks, regression detection) | Adjudicating contested historical truth claims |
| “Fairness as disclosure”: producing reviewable evidence for humans | Storing/deriving sensitive attributes without explicit governance approval |

### Audience

- Primary: AI/pipeline maintainers implementing or running fairness checks.
- Secondary: governance reviewers, story editors, release managers, and QA.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fairness evaluation**: measuring whether model performance/behavior differs meaningfully across defined slices (not necessarily protected classes).
  - **Slice**: a subset of evaluation data (e.g., source type, time period, region, document quality band).
  - **Harm check**: automated checks for unsafe/demeaning language, misrepresentation patterns, or systematic omission signals.
  - **Evaluation suite**: a versioned collection of datasets + configs + expected outputs.
  - **Evidence artifact**: a machine-readable report + provenance that can be referenced downstream.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `tools/ai/fairness/README.md` | TBD | Conventions + contracts |
| Provenance tooling | `tools/ai/provenance/README.md` | TBD | Used to record PROV for fairness runs (path not confirmed in repo) |
| Fairness run artifacts | `mcp/runs/<run_id>/fairness/` | TBD | Recommended run output location |
| PROV bundle outputs | `data/prov/<run_id>/` | TBD | Optional: promote run lineage into canonical PROV store |
| Fairness schemas | `schemas/ai/fairness/` | TBD | Recommended: JSON Schemas for reports (not confirmed in repo) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tools/ai/fairness/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API boundary | `src/server/` | OpenAPI/GraphQL contracts, redaction, query services |
| UI | `web/` | Map UI, layer registry, Focus Mode UI |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published Story Nodes + assets |
| Schemas | `schemas/` | JSON schemas (telemetry, contracts, reports) |
| Tests | `tests/` | Unit/integration/contract tests |
| Tooling | `tools/` | Offline utilities, QA tooling, evaluators |
| Run artifacts | `mcp/runs/` | Deterministic run logs/artifacts (experiments, evals) |

### Expected local tree (this folder)

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 fairness/
        ├── 📄 README.md
        ├── 📁 configs/                  # not confirmed in repo (recommended)
        ├── 📁 checks/                   # not confirmed in repo (recommended)
        ├── 📁 datasets/                 # not confirmed in repo (recommended)
        └── 📁 reports/                  # not confirmed in repo (recommended)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Example location | Format | Sensitivity | Notes |
|---|---|---|---|---|
| Evaluation suite config | `tools/ai/fairness/configs/<suite>.yaml` | YAML | public | Defines checks + slices + thresholds (path not confirmed in repo) |
| Model outputs under test | `mcp/runs/<run_id>/outputs/` | JSON/NDJSON | varies | Must be tied to an upstream run manifest |
| Ground truth / reference labels | `data/<domain>/processed/<eval_set>/` | CSV/JSON | varies | Must be versioned + provenance-linked |
| Slice metadata | alongside eval set | CSV/JSON | varies | Prefer non-sensitive slices (source type, time, quality bands) |
| Run manifest | `mcp/runs/<run_id>/run.json` | JSON | public | Inputs, code ref, config hash (path not confirmed in repo) |

### Outputs

| Output | Recommended location | Format | Sensitivity | Notes |
|---|---|---|---|---|
| Metrics (machine-readable) | `mcp/runs/<run_id>/fairness/metrics.json` | JSON | public | Must include suite version + slice definitions |
| Summary report (human) | `mcp/runs/<run_id>/fairness/summary.md` | Markdown | public | “What changed” + limitations |
| Slice table export | `mcp/runs/<run_id>/fairness/slices.csv` | CSV | public | Aggregate only (no row-level sensitive attributes) |
| Artifacts (plots) | `mcp/runs/<run_id>/fairness/plots/` | PNG/SVG | public | Optional |
| PROV bundle | `mcp/runs/<run_id>/fairness/prov/` | PROV-JSON/JSON-LD | public | Must reference inputs + outputs |

### Sensitivity & redaction

- Do **not** infer sensitive attributes (identity, affiliation, protected class) from names, locations, or text.
- If slice definitions require sensitive labels, treat them as **restricted by default** and require explicit governance review and documented handling.
- Reports should default to **aggregate metrics** (counts, rates, confidence intervals), not row-level dumps.

### Quality signals

- Minimum recommended signals (suite-dependent):
  - Performance parity across slices (precision/recall/F1 or task-appropriate metrics)
  - Error-mode parity (false positives/negatives by slice)
  - Harm checks (e.g., unsafe language flags) and their slice distribution
  - Regression detection vs a baseline run (same suite version)
  - Coverage/omission indicators (e.g., extraction coverage by source type/time band)

## 🌐 STAC, DCAT & PROV Alignment

- **PROV (required for fairness runs):**
  - Each fairness evaluation is a PROV **Activity** that:
    - *uses* evaluation dataset entities + model output entities
    - *generates* metrics/report entities
    - is attributed to an **Agent** (tool + operator, where appropriate)
- **DCAT (optional):**
  - If an evaluation dataset is promoted to a shareable asset, define a DCAT dataset entry (title/description/license/keywords/minimum required fields).
- **STAC (typically N/A):**
  - Fairness outputs are usually non-geospatial.
  - If a fairness artifact is explicitly linked to geospatial assets (e.g., a STAC Item-based slice), record those IDs in the metrics/report as references rather than duplicating STAC.

## 🧱 Architecture

### Where this fits (pipeline-aligned)

~~~mermaid
flowchart LR
  A[ETL / Pipelines] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[AI Components (extract/classify/summarize)]
  D --> E[Fairness Toolkit (this folder)]
  E --> F[Run Artifacts + PROV Evidence]
  F --> G[API Layer]
  G --> H[UI + Story Nodes + Focus Mode]
~~~

### Components

| Component | Location | Responsibilities |
|---|---|---|
| ETL | `src/pipelines/` | Deterministic transforms that produce governed data artifacts |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Standardized metadata + lineage |
| Graph | `src/graph/` | Ontology-governed entity/relationship layer |
| **AI Fairness (this toolkit)** | `tools/ai/fairness/` | Evaluation suites, sliced metrics, harm checks, fairness reports |
| API boundary | `src/server/` | Contracted access to graph + evidence; redaction/generalization rules |
| UI | `web/` | Visualization, Focus Mode, provenance rendering |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts with evidence references |

### Interfaces / contracts

- **Report schema** (recommended): `schemas/ai/fairness/metrics.schema.json` (not confirmed in repo)
- **Suite config schema** (recommended): `schemas/ai/fairness/suite.schema.json` (not confirmed in repo)
- **Run manifest coupling**: fairness runs should reference:
  - upstream run identifier
  - suite version
  - input dataset identifiers
  - code/config hash(es)
- **API boundary invariant:** if fairness results are shown to users, they must be served via API contracts (UI must not read Neo4j directly).

### Extension points checklist (for future work)

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

- If AI-assisted content appears in Story Nodes / Focus Mode, fairness artifacts can be attached as **supporting evidence**:
  - suite name + version
  - last evaluation run ID
  - summary of key parity checks and known limitations
- Any disclosure must be **provenance-linked** (run ID + artifact path) and never presented as a substitute for primary sources.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.
- “Fairness passed” is **not** a factual claim about history; it is a statement about model behavior under a specific evaluation suite.

### Optional structured controls

~~~yaml
focus_layers:
  - "ai.fairness.summary"   # not confirmed in repo (placeholder)
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) — if applicable to the change
- [ ] Fairness report schema validation (if schemas exist)
- [ ] Regression checks vs baseline fairness run (suite-dependent)
- [ ] API contract tests (if fairness artifacts are exposed via API)
- [ ] UI schema checks (if surfaced in UI)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run a fairness suite
# python -m tools.ai.fairness.run --suite tools/ai/fairness/configs/<suite>.yaml --run-id <run_id>

# 2) validate produced metrics against schema
# python -m tools.ai.fairness.validate --metrics mcp/runs/<run_id>/fairness/metrics.json --schema schemas/ai/fairness/metrics.schema.json

# 3) promote PROV bundle to canonical store (optional)
# cp -r mcp/runs/<run_id>/fairness/prov data/prov/<run_id>/
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Slice parity deltas | Fairness metrics | `docs/telemetry/` + `schemas/telemetry/` |
| Harm-check rates | Fairness metrics | `docs/telemetry/` + `schemas/telemetry/` |
| Regression flags | CI | CI logs + run artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that should require explicit review (and may require human approval):
  - new slice definitions involving sensitive attributes
  - new harm-check categories that could change public-facing behavior
  - threshold changes that alter CI pass/fail behavior
  - exposing fairness artifacts via public API/UI

### CARE / sovereignty considerations

- Treat cultural/identity-adjacent evaluation slices as **high sensitivity** unless governance explicitly defines safe handling.
- Prefer non-sensitive, domain-relevant slices (time period, source type, document quality band, region at coarse granularity).
- If a community is impacted, document protections and redaction/generalization rules before running/recording evaluations at scale.

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use.
- Fairness artifacts may be summarized for reporting, but must not be used to generate or justify new governance policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial fairness toolkit README (scaffold + contracts) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
