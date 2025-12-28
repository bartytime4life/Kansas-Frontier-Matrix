---
title: "🧪 MCP Experiments — Index & Rules (v11 LTS · Diamond⁹ Ω / Crown∞Ω)"
path: "mcp/experiments/README.md"
version: "v11.2.6"
last_updated: "2025-12-28"
status: "active"
doc_kind: "Index"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & MCP Board"
content_stability: "stable"

header_profile: "standard"
footer_profile: "standard"
intent: "mcp-experiment-index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"

telemetry_ref: "releases/v11.2.6/mcp-experiments-telemetry.json"
telemetry_schema: "schemas/telemetry/mcp-experiments-v11.json"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"

semantic_document_id: "kfm-mcp-experiments-index"
event_source_id: "ledger:kfm:mcp:experiments:index:v11.2.6"
doc_uuid: "urn:kfm:mcp:experiments:index:v11.2.6"

machine_extractable: true
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "US-KS"

classification: "open"
sensitivity: "public"
fair_category: "FAIR+CARE"
care_label: "Mixed"

ai_transform_permissions:
  - "summarize"
  - "timeline_generation"
  - "semantic_highlighting"
  - "a11y_adaptations"
  - "metadata_extraction"
  - "layout_normalization"
ai_transform_prohibited:
  - "content_alteration"
  - "speculative_additions"
  - "narrative_fabrication"
  - "governance_override"
  - "provenance_fabrication"

provenance_chain:
  - "urn:kfm:mcp:experiments:index:v11.0.0"
  - "urn:kfm:mcp:experiments:index:v11.2.6"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🧪 MCP Experiments — Index & Rules (v11 LTS)

## 📘 Overview

### Purpose
This README is the **canonical index and enforcement surface** for all experiment work under **MCP-DL v6.3**.
An “experiment” in KFM is any reproducible activity that produces **new evidence artifacts** (data, models, metrics, derived layers, evaluations) that may later feed catalogs, graph, APIs, UI, Story Nodes, or Focus Mode.

### Scope

| In Scope | Out of Scope |
|---|---|
| Experiment records (IDs, intent, inputs/outputs, configs, seeds), artifact locations, reproducibility rules, catalog/provenance expectations, governance and sensitivity guardrails. | Domain ETL recipes (live in `src/pipelines/**`), deployment/ops procedures (live in `tools/**`), unsourced narrative (belongs only in Story Nodes with evidence links). |

### Audience
- Primary: contributors running experiments (data engineering, modeling/AI, QA, pipeline maintainers).
- Secondary: governance reviewers, editors, and auditors validating reproducibility and provenance.

### Definitions (link to glossary)
- Glossary: `docs/glossary.md` *(not confirmed in repo; recommended)*
- **Experiment**: a bounded investigation whose outputs are **replayable** and **auditable**.
- **Run record**: machine-readable execution log + config snapshot stored under `mcp/runs/`.
- **Evidence artifact**: an output that is treated as **data + metadata** (STAC/DCAT/PROV) before it can appear in UI/narrative.
- **Provenance-first**: catalogs and lineage are produced **before** graph/UI/story surfacing.

### Key artifacts (what this document points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Experiments index (this doc) | `mcp/experiments/README.md` | MCP Board | Rules + index |
| Run records | `mcp/runs/` | MCP Board | Execution logs, configs, seeds |
| Telemetry bundle | `releases/<version>/mcp-experiments-telemetry.json` | MCP Board | Energy/carbon + perf |
| Telemetry schema | `schemas/telemetry/mcp-experiments-v11.json` | Schemas | Validation contract |
| STAC outputs | `data/stac/` | Catalog Maintainers | Items/Collections for spatial outputs |
| DCAT outputs | `data/catalog/dcat/` | Catalog Maintainers | Dataset/distribution discovery |
| PROV outputs | `data/prov/` | Catalog Maintainers | Lineage bundles |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory layout matches canonical homes (no “mystery” paths)
- [ ] Rules are explicit (MUST/SHOULD) and CI-checkable
- [ ] Governance + sovereignty guardrails are stated
- [ ] Index table format is stable and automation-friendly

## 🗂️ Directory Layout

### This document
- `path`: `mcp/experiments/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Experiments | `mcp/experiments/` | Experiment records + index |
| Run logs | `mcp/runs/` | Replayable run logs + configs + seeds |
| Model cards | `mcp/model_cards/` | Model documentation + limitations |
| Raw data | `data/raw/` | Immutable inputs |
| Working data | `data/work/` | Intermediate artifacts |
| Processed outputs | `data/processed/` | Published/derived datasets |
| STAC | `data/stac/` | STAC Items/Collections |
| DCAT | `data/catalog/dcat/` | DCAT datasets/distributions |
| PROV | `data/prov/` | PROV lineage bundles |

### Expected file tree for this sub-area
~~~text
📁 mcp/
├── 📁 experiments/
│   ├── 📄 README.md                           — Canonical index + rules (this file)
│   ├── 📄 YYYY-MM-DD_<DOMAIN>-EXP-###.md       — Experiment record (single-file mode)
│   └── 📁 YYYY/
│       └── 📁 YYYY-MM-DD_<DOMAIN>-EXP-###/
│           ├── 📄 README.md                    — Experiment record (folder mode)
│           ├── 📁 config/                      — Frozen configs (copies; source-of-truth in repo)
│           ├── 📁 results/                     — Figures/tables/maps (small, reviewable)
│           └── 📁 notes/                       — Optional scratch notes (no governance bypass)
├── 📁 runs/
│   └── 📄 README.md                           — Run records and reproducibility logbook
└── 📁 model_cards/
    └── 📄 README.md                           — Model cards index
~~~

## 🧭 Context

### Background
KFM treats experiments as **governed scientific work**: reproducible by design, provenance-linked by default, and safe for public release under FAIR+CARE and sovereignty constraints.
Any output that could influence graph/UI/story must have an auditable chain from inputs → transforms → outputs.

### Constraints / invariants
- Canonical pipeline ordering is preserved:
  - **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- **No UI direct-to-graph access**: UI consumes only API contracts.
- **No unsourced narrative**: experiments may generate drafts, but Story Nodes must remain evidence-linked and reviewable.
- **Determinism**: where randomness exists, seeds and non-default parameters MUST be logged.

### Assumptions
- Experiments are executed via repo-tracked code and config (or clearly referenced external tooling) with sufficient detail to replay.
- Large artifacts are stored as datasets under `data/**` and referenced by catalogs, not embedded into experiment Markdown.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize on single-file vs folder-mode experiment records (or allow both permanently)? | MCP Board | TBD |
| Do we publish a machine index (CSV/JSON) alongside this README for automation? | MCP Board | TBD |

### Future extensions
- A machine-readable experiment registry (JSON/CSV) generated from front-matter.
- Optional validation schema for experiment records (JSON Schema under `schemas/mcp/`).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[mcp/experiments record] --> B[mcp/runs run record]
  B --> C[data artifacts]
  C --> D[STAC/DCAT/PROV catalogs]
  D --> E[Graph ingest]
  E --> F[API boundary]
  F --> G[UI surfaces]
  G --> H[Story Nodes]
  H --> I[Focus Mode]
~~~

## 📦 Data & Metadata

### What counts as an experiment
An activity MUST be recorded as an MCP experiment if it produces any of the following:
- new derived datasets (tables/rasters/vectors/time series),
- trained or fine-tuned models,
- evaluation results (benchmarks, ablations, bias audits),
- transformations that change interpretation-ready outputs (e.g., harmonization, masking/generalization, datum conversions),
- AI-assisted artifacts intended to influence Story Nodes or Focus Mode.

### Experiment ID and naming
**Supported patterns**
- **Single-file mode:** `YYYY-MM-DD_<DOMAIN>-EXP-###.md`
- **Folder mode:** `YYYY/YYYY-MM-DD_<DOMAIN>-EXP-###/README.md`

**Domain codes (non-exhaustive)**
- `CLIMATE`, `HYDRO`, `GEO`, `AI`, `NLP`, `ARCH`, `HAZARD`, `STORY`, `PIPELINE`

### Minimum required contents for an experiment record
Each experiment record MUST include:
- **Identity:** experiment ID, date, domain, owner/agent(s), status
- **Objective:** hypothesis/question, success criteria
- **Inputs:** dataset IDs / paths + checksums (or references to manifests)
- **Method:** steps + parameters + seed(s) + environment notes
- **Outputs:** artifact paths + intended catalog actions (STAC/DCAT/PROV)
- **Results:** key metrics, plots/tables (or links), uncertainty/limitations
- **Governance:** sensitivity notes, sovereignty handling, CARE notes
- **Provenance pointers:** run record ID(s) + lineage bundle reference(s)

### Suggested (optional) record skeleton
~~~yaml
# (Place in the experiment record, not in this README.)
experiment_id: "2025-12-28_AI-EXP-001"
domain: "AI"
status: "draft|active|completed|blocked|archived"
owners:
  - "handle-or-team"
run_records:
  - "mcp/runs/<run-id>/"
inputs:
  - "data/raw/<domain>/... (checksum: sha256:...)"
outputs:
  - "data/processed/<domain>/... (intended catalogs: stac|dcat|prov)"
seeds:
  - 1337
contracts:
  stac_profile: "KFM-STAC v11.0.0"
  dcat_profile: "KFM-DCAT v11.0.0"
  prov_profile: "KFM-PROV v11.0.0"
~~~

### Index of experiments
This table is intended to remain **automation-friendly** (stable columns, minimal formatting).

| Experiment ID | Title | Domain | Start date | Status | Primary outputs |
|---:|---|---|---:|---|---|
| _none_ | — | — | — | — | — |

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Experiments that produce spatial assets SHOULD emit STAC Items (and update/attach to an appropriate Collection):
- Spatial datasets: STAC Item with geometry/bbox/time.
- Non-spatial artifacts: STAC Item MAY use `geometry: null` with clear asset metadata.

### DCAT
Experiments producing publishable datasets SHOULD register a DCAT dataset record and distributions (formats, access methods).

### PROV-O
Experiments that transform data MUST produce provenance lineage linking:
- raw inputs (`prov:used` / `prov:wasDerivedFrom`)
- run/activity (`prov:wasGeneratedBy`)
- outputs (with stable IDs + checksums)

### Canonical locations
~~~text
📁 data/
├── 📁 stac/                 — STAC collections + items
├── 📁 catalog/dcat/         — DCAT datasets + distributions
└── 📁 prov/                 — PROV bundles (lineage)
~~~

## 🧱 Architecture

### Components touched by experiments
| Component | Responsibility | Interface |
|---|---|---|
| Experiment record | Human-readable + reviewable log | Markdown file(s) in `mcp/experiments/` |
| Run record | Replayable execution record | `mcp/runs/` |
| Artifact store | Data outputs | `data/{raw,work,processed}/**` |
| Catalogs | Discovery + lineage | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Contracts | Validation schemas | `schemas/**` |

### Interfaces / contracts (expectations)
- Experiments MUST reference:
  - dataset locations under `data/**`,
  - run logs under `mcp/runs/**`,
  - catalog outputs under `data/{stac,catalog/dcat,prov}/**` where applicable.
- Experiments MUST NOT imply:
  - UI consumption of Neo4j directly,
  - narrative publication without evidence and review.

## 🧠 Story Node & Focus Mode Integration

Experiments that generate or modify Story Nodes MUST:
- separate **facts** vs **interpretation** vs **hypotheses**,
- include evidence IDs (STAC/DCAT/PROV/document identifiers),
- apply sovereignty-first handling (generalize/mask sensitive locations by default),
- route final narrative through Story Node review gates (no direct Focus Mode injection).

## 🧪 Validation & CI/CD

### CI expectations (minimum)
- Filename pattern checks for experiment records.
- Markdown protocol checks (single H1; stable H2 structure; tilde-fenced blocks).
- Required experiment metadata presence (ID, dates, run record refs, inputs/outputs).
- Provenance expectations where outputs are produced (PROV refs + checksums).
- Secret/PII scanning + sovereignty checks for sensitive location leakage.

### Local checklist (author)
- [ ] Experiment record created and filled
- [ ] Config snapshot captured (or referenced) + seed(s) recorded
- [ ] Run record created under `mcp/runs/`
- [ ] Outputs stored under `data/**`
- [ ] Catalog updates planned/emitted (STAC/DCAT/PROV) where applicable
- [ ] Governance notes included

## ⚖ FAIR+CARE & Governance

### FAIR+CARE notes
- **FAIR profile:** evidence artifacts must be findable and attributable via catalogs.
- **CARE label:** this index is `Mixed` because experiments may span multiple sensitivity regimes.

### Sovereignty and sensitive locations
- Do not publish precise coordinates for culturally sensitive resources by default.
- Prefer generalized representations (e.g., grid/H3, buffered extents, or redacted geometry) when risk exists.
- If an experiment touches Tier-A or culturally sensitive datasets, request review per governance procedures.

### Required approvals (when applicable)
- [ ] FAIR+CARE Council review (sensitivity high, Tier-A, cultural/heritage)
- [ ] Security review (secrets, access tokens, restricted endpoints, threat model changes)
- [ ] Editorial review (Story Node publication)

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-28 | Re-structured to Universal governed-doc layout; normalized canonical paths; strengthened reproducibility + catalog/provenance expectations; removed HTML-only centering in favor of protocol-safe Markdown. |
| v11.2.6 | 2025-12-12 | Prior draft baseline. |

---

[⬅️ MCP Home](../README.md) · [📘 Master Guide](../../docs/MASTER_GUIDE_v12.md) · [🏛️ Governance Charter](../../docs/governance/ROOT_GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — CC-BY-4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω
