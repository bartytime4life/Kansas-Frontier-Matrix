---
title: "Research Evaluations — README"
path: "docs/research/evaluations/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "active"
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

doc_uuid: "urn:kfm:doc:research:evaluations:readme:v1.0.0"
semantic_document_id: "kfm-research-evaluations-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:evaluations:readme:v1.0.0"
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

# Research Evaluations

## 📘 Overview

### Purpose
This directory holds **evaluation artifacts and governed summaries** that measure the quality, correctness, performance, and safety of KFM components and outputs (e.g., ETL extraction quality, catalog integrity, graph correctness, API contract behavior, UI rendering fidelity, and Focus Mode narrative constraints).

Evaluations are intended to be **repeatable and provenance-linked**: every reported result should trace back to specific inputs (datasets/assets) and a reproducible run/activity identifier.

### Scope
| In Scope | Out of Scope |
|---|---|
| Evaluation plans, protocols, metrics definitions | Brainstorming / early notes (use `docs/research/drafts/`) |
| Repro steps + run references (e.g., run IDs, config refs) | Production “how-to” docs for pipelines (use `docs/pipelines/` if applicable) |
| Result summaries (tables, plots, deltas, limitations) | Raw/derived datasets themselves (use `data/raw/`, `data/processed/`) |
| Governance/audit notes for evaluation outcomes | Uncited narrative claims |

### Audience
- Primary: KFM contributors running experiments and measuring changes
- Secondary: reviewers validating claims; maintainers making go/no-go decisions

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: evaluation, baseline, benchmark, metric, run ID, provenance, reproducibility, sensitivity

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Research home | `docs/research/README.md` | TBD | High-level research map (if/when present) |
| Draft notes | `docs/research/drafts/README.md` | TBD | Pre-evaluation ideation and sketches |
| Runs + experiment artifacts | `mcp/runs/` + `mcp/experiments/` | TBD | Recommended home for logs + heavy artifacts |
| Provenance bundles | `data/prov/` | TBD | Link evaluations to PROV activities when available |
| STAC catalogs | `data/stac/` | TBD | Reference item/collection IDs used in evaluation |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory intent and conventions are clear
- [ ] Includes repeatability + provenance expectations (no uncited results)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/evaluations/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Evaluation dossiers | `docs/research/evaluations/` | This folder: human-readable evaluation records |
| Experiment artifacts | `mcp/runs/` + `mcp/experiments/` | Run logs, notebooks, model cards, large outputs |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` | Raw and derived data (not stored in docs) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV records for traceability |
| Schemas | `schemas/` | JSON schemas for telemetry, catalogs, contracts |
| Tests | `tests/` | Regression tests and fixtures |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 evaluations/
        ├── 📄 README.md
        ├── 📁 YYYY-MM-DD__eval__<short-slug>/
        │   ├── 📄 README.md
        │   ├── 📄 findings.md
        │   ├── 📄 metrics.json
        │   ├── 📄 provenance.md
        │   └── 📁 assets/
        │       ├── 📄 chart-01.png
        │       └── 📄 table-01.csv
        └── 📁 YYYY-MM-DD__eval__<another-slug>/
            └── 📄 README.md
~~~

## 🧭 Context

### Background
Evaluations provide an evidence trail for:
- detecting regressions (quality/performance/safety),
- validating improvements,
- supporting governance review (especially when handling sensitive or high-impact content),
- ensuring alignment with the canonical KFM pipeline and its invariants.

### Assumptions
- Evaluations may touch any pipeline stage, but **do not bypass** standard contracts and provenance expectations.
- Evaluation dossiers stored here should primarily be **lightweight summaries + pointers**, not large binary payloads.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Every claim in an evaluation summary should be traceable to an input set and a run/activity reference.

### How to add a new evaluation (folder protocol)
1. Create a new folder: `YYYY-MM-DD__eval__<short-slug>/`
2. Add `README.md` with:
   - question + hypothesis (if any),
   - scope and non-goals,
   - inputs (dataset IDs / STAC item IDs / commit refs),
   - method (what was measured, how),
   - metrics + thresholds (if defined),
   - results + deltas vs baseline,
   - limitations and confounders,
   - reproduction steps (commands/config refs),
   - provenance references (run ID, PROV activity if available).
3. Store heavy artifacts (logs, big result bundles) in `mcp/runs/` or `mcp/experiments/` and link to them.
4. If the evaluation impacts any public-facing claims or releases, flag for appropriate governance review.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should we standardize a `schemas/telemetry/evaluation.schema.json` for `metrics.json`? | TBD | TBD |
| Where should “golden” baselines live (tests vs mcp vs data/processed)? | TBD | TBD |

### Future extensions
- Add a schema-validated evaluation metrics format (telemetry-aligned).
- Add CI hooks to detect missing provenance links when evaluations publish results.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Evaluation Plan] --> B[Run / Experiment]
  B --> C[Metrics + Artifacts]
  C --> D[Evaluation Dossier (docs/research/evaluations)]
  C --> E[PROV Activity (data/prov)]
  C --> F[Regression Tests / Gates (tests/ + CI)]
  D --> G[Decision: accept / investigate / revert]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Dataset(s) under test | files + metadata | `data/...` + catalogs | STAC/DCAT presence; basic integrity checks |
| Run configuration | YAML/JSON | `mcp/` or pipeline config | Config lint + deterministic settings |
| Baseline metrics | JSON/CSV | prior evaluation folder or `mcp/` | Schema (if available) + sanity checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Evaluation summary | Markdown | `docs/research/evaluations/<eval>/README.md` | This doc’s conventions |
| Findings narrative | Markdown | `.../<eval>/findings.md` | N/A |
| Metrics bundle | JSON | `.../<eval>/metrics.json` | TBD (recommended future schema) |
| Plots/tables | PNG/CSV | `.../<eval>/assets/` | N/A |

### Sensitivity & redaction
- Do not include secrets, credentials, or raw PII in evaluation artifacts.
- If evaluation uses restricted/sensitive sources or locations, follow the governance references in the front-matter and document the generalization/redaction applied.

### Quality signals
Common examples (choose what applies; define precisely in the dossier):
- extraction accuracy (precision/recall/F1, error rates),
- catalog integrity (broken links, schema validation pass rate),
- graph integrity (constraint violations, orphan nodes),
- API behavior (contract conformance, latency, error budgets),
- UI fidelity (render checks, layer consistency),
- narrative constraints (citation coverage, prohibited inference checks).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If an evaluation uses geospatial assets, list **STAC Collection/Item IDs** in the dossier.
- Link results to specific STAC assets when reporting spatial/temporal correctness.

### DCAT
- If evaluating a dataset “as a product,” reference its DCAT identifier (if available) and the exact dataset version.

### PROV-O
- Prefer to record or reference a **PROV activity/run ID** that generated the evaluated outputs.
- When a PROV bundle exists, include:
  - `prov:wasDerivedFrom` (inputs),
  - `prov:wasGeneratedBy` (activity/run),
  - `prov:wasAssociatedWith` (agent/team/tool).

### Versioning
- Record the baseline and comparison target (e.g., commit tags, dataset versions, schema versions).
- Keep evaluations append-only when possible; supersede via a new evaluation folder rather than rewriting history.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Evaluation dossier | Human-readable evidence | Markdown + links to artifacts |
| Runs/experiments | Generate results | `mcp/runs/` / `mcp/experiments/` |
| Catalogs + provenance | Traceability | STAC/DCAT/PROV references |
| CI gates (optional) | Prevent regressions | tests + validation jobs |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Catalog schemas | `data/stac/` + validators | Semver + validation required |
| API contracts (if evaluated) | `src/server/` + `docs/` | Backward compat or version bump |
| Evaluation metrics schema | **not confirmed in repo** | Propose adding under `schemas/telemetry/` |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Evaluations may be used to justify:
- promoting a new layer/story node to “supported,”
- gating or warning on low-confidence extractions,
- enabling/disabling AI narrative behaviors based on citation coverage.

### Provenance-linked narrative rule
If an evaluation makes factual claims about historical content or entities, it must include dataset/document identifiers and citation references consistent with Focus Mode expectations.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (lint, front-matter sanity)
- [ ] Links resolve (local paths, referenced artifacts)
- [ ] If STAC/DCAT/PROV are referenced: confirm IDs resolve and schemas validate
- [ ] If API behavior is evaluated: confirm contract test references exist
- [ ] Sensitivity rules verified (no secrets/PII)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands.
# 1) Run the evaluation pipeline / notebook
# 2) Validate catalogs (STAC/DCAT/PROV) referenced by the evaluation
# 3) Run regression tests related to the evaluated component(s)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Metric deltas vs baseline | evaluation run output | `docs/research/evaluations/<eval>/metrics.json` (schema TBD) |
| CI regression status | CI logs | `.github/workflows/...` (as applicable) |

## ⚖ FAIR+CARE & Governance

### Review gates
- If evaluation results affect public-facing behavior (UI, Focus Mode narratives, published layers), require reviewer sign-off appropriate to the impacted subsystem.
- If sensitive datasets are involved, follow `sovereignty_policy` and document redaction/generalization.

### CARE / sovereignty considerations
- Identify impacted communities when evaluation touches culturally sensitive content, locations, or narratives.
- Prefer aggregation/generalization when reporting sensitive geographies.

### AI usage constraints
- Do not infer sensitive locations or create new policy language in evaluation summaries.
- Keep “fact vs inference vs hypothesis” explicit when interpreting results.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for research evaluations directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

