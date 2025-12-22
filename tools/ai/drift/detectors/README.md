---
title: "KFM AI Drift — Detectors"
path: "tools/ai/drift/detectors/README.md"
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

doc_uuid: "urn:kfm:doc:tools:ai:drift:detectors:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-drift-detectors-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:drift:detectors:readme:v1.0.0"
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

# KFM AI Drift — Detectors

## 📘 Overview

### Purpose

- Document the **drift detector** subsystem under `tools/ai/drift/detectors/` and the expectations for adding or modifying detectors.
- Provide a **minimum, reproducible contract** for drift detector inputs/outputs so results can be: (a) reviewed by humans, (b) diffed across runs, and (c) recorded as telemetry signals.

### Scope

| In Scope | Out of Scope |
|---|---|
| Detector authoring guidance (structure, determinism, output contract) | Model training / fine-tuning workflows |
| What “baseline vs current” means for KFM runs | Selecting or acquiring external datasets |
| Output/report format for drift results | Building dashboards/alerting infra (unless explicitly added elsewhere) |
| Governance + redaction expectations for drift artifacts | Changing API/UI contracts (belongs in API/UI docs) |

### Audience

- Primary: AI/pipeline engineers adding detectors; CI/quality maintainers.
- Secondary: reviewers (governance/ethics), curators consuming quality/audit signals.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — referenced by template; add if missing)*
- Terms used in this doc:
  - **baseline**: the reference snapshot/window a detector compares against (e.g., last release, last successful run).
  - **current**: the candidate snapshot/window being evaluated (e.g., PR build, scheduled run).
  - **drift**: statistically meaningful change in distributions, outputs, or structures that can degrade quality.
  - **detector**: a deterministic routine that computes drift metrics and returns a structured result.
  - **gate**: a CI decision rule (pass/warn/fail) applied to detector results.
  - **evidence artifact**: a run output that can be referenced by catalogs/PROV/Story Nodes if promoted.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical ordering + non-negotiables. |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Review gates / policy anchors. |
| Ethics policy | `docs/governance/ETHICS.md` | TBD | AI + disclosure expectations. |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | TBD | Sensitive knowledge handling. |
| Telemetry docs | `docs/telemetry/` | TBD | Where signals are documented (template canonical). |
| Telemetry schemas | `schemas/telemetry/` | TBD | Where telemetry schemas live (template canonical). |
| This README | `tools/ai/drift/detectors/README.md` | TBD | Detector guidance + contracts. |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Detector contracts are explicit (inputs, outputs, error handling, determinism expectations)
- [ ] Reproduction/CI steps are listed (even if placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Any “proposed / not confirmed in repo” sections are clearly marked

## 🗂️ Directory Layout

### This document

- `path`: `tools/ai/drift/detectors/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/STAC outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Tools | `tools/` | Developer tools (including drift detectors) |

### Expected file tree for this sub-area

> This tree is a **recommended target shape** to keep detectors discoverable and testable.  
> Items marked “not confirmed in repo” are **proposals** until the codebase confirms exact filenames.

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 drift/
        └── 📁 detectors/
            ├── 📄 README.md                        # this file
            ├── 📄 base.py                          # detector protocol / base class (not confirmed in repo)
            ├── 📄 registry.py                      # detector registration (not confirmed in repo)
            ├── 📁 implementations/                 # concrete detectors (not confirmed in repo)
            │   ├── 📄 schema_drift.py               # e.g., field/shape changes
            │   ├── 📄 text_distribution_drift.py    # e.g., PSI/JS divergence over tokens
            │   └── 📄 embedding_drift.py            # e.g., centroid / norm / cosine shift
            └── 📁 fixtures/                         # golden test inputs/outputs (not confirmed in repo)
                └── 📄 <detector_slug>_golden.json
~~~

## 🧭 Context

### Background

KFM ingests evolving sources and may use AI-assisted transforms/extraction. Even when schemas stay stable, **distributions and model outputs can drift** (e.g., token distributions, entity extraction rates, geometry validity rates). Drift detection is an early-warning layer: it helps prevent silent quality regressions and supports repeatable governance review.

### Assumptions

- Drift detectors are **deterministic** for the same inputs/config (diffable outputs).
- Baselines are **versioned** and traceable (run ID, catalog ID, or commit/tag).
- Drift results are captured as **structured artifacts** (JSON) and optionally as **telemetry signals**.

### Constraints / invariants

- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI consumes contracts via APIs (no direct graph dependency).
- Drift artifacts must not leak sensitive locations or restricted knowledge (follow sovereignty policy).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical baseline selector (last release? last scheduled run? curated baseline)? | TBD | TBD |
| Do detectors fail the build by default, or only warn unless explicitly gated? | TBD | TBD |
| What is the canonical storage path for drift artifacts (e.g., `mcp/runs/…` vs `data/processed/…`)? | TBD | TBD |
| Which telemetry schema(s) should drift signals conform to? | TBD | TBD |

### Future extensions

- Add domain-specific detectors (e.g., spatial drift in geometry extents, temporal drift in event density).
- Add a UI-facing “quality/audit overlay” that can be surfaced in Focus Mode as *non-narrative metadata* (requires API/UI contract work).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR

  A[ETL + Normalization] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  %% Drift as a sidecar (does not break canonical ordering)
  A --> H[Drift Detectors]
  B --> H
  H --> I[Drift Report Artifacts]
  H --> J[Telemetry Signals / CI Gates]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant CI as CI Runner
  participant Drift as Drift Runner
  participant Store as Artifact Store
  participant Review as Reviewer

  CI->>Drift: execute detectors(baseline, current, config)
  Drift-->>Store: write drift_report.json (+ optional summary)
  Drift-->>CI: return status(pass/warn/fail) + metrics
  CI-->>Review: surface summary in logs/PR comment (if enabled)
~~~

## 📦 Data & Metadata

### Inputs

> The exact inputs depend on detector type. Use **stable IDs** for baseline/current references and avoid raw sensitive payloads.

| Input | Format | Where from | Validation |
|---|---|---|---|
| Baseline artifact(s) | JSON/Parquet/CSV (TBD) | Prior run output / release artifact | Schema + checksum (TBD) |
| Current artifact(s) | JSON/Parquet/CSV (TBD) | Current pipeline output | Schema + checksum (TBD) |
| Detector config | YAML/JSON | Repo config (recommended) | Schema validation (if present) |
| Thresholds / gates | YAML/JSON | Governed config (recommended) | Reviewer-approved changes |
| Redaction rules | YAML/JSON | Governance policy + run config | Must pass “no sensitive leakage” checks |

### Outputs

> Outputs should be **machine-readable first** (JSON), and **human-readable second** (Markdown summary).

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Drift report (per detector) | JSON | `mcp/runs/<run_id>/drift/<detector_slug>.json` *(recommended; not confirmed in repo)* | Drift report schema (proposed below) |
| Drift summary (optional) | Markdown | `mcp/runs/<run_id>/drift/summary.md` *(recommended; not confirmed in repo)* | N/A |
| Telemetry event(s) (optional) | JSON | Recorded per `docs/telemetry/` + `schemas/telemetry/` | Telemetry schema (TBD) |

#### Proposed drift report schema (not confirmed in repo)

~~~json
{
  "detector": { "name": "embedding_drift", "version": "0.1.0" },
  "run": {
    "run_id": "mcp-run-<id>",
    "timestamp_utc": "2025-12-22T00:00:00Z",
    "commit_sha": "<sha>",
    "inputs": {
      "baseline_ref": "baseline:<id>",
      "current_ref": "current:<id>"
    }
  },
  "metrics": [
    {
      "name": "centroid_cosine_distance",
      "value": 0.12,
      "threshold": 0.20,
      "status": "ok"
    }
  ],
  "overall_status": "ok",
  "notes": []
}
~~~

### Sensitivity & redaction

- Do **not** store raw excerpts, full documents, or precise coordinates in drift logs unless explicitly permitted by governance.
- Prefer aggregated statistics (counts, rates, distribution summaries) and hashed identifiers where needed.
- If sensitive domains are included, ensure any drift summaries are reviewed before publishing beyond internal logs.

### Quality signals

- Determinism: same inputs/config → same outputs (byte-diffable where feasible).
- Completeness: drift report includes baseline/current refs + detector version.
- Coverage: detectors declare which artifact types they support (text, embeddings, schema, graph stats, etc.).
- Safety: drift report does not include prohibited fields (sensitive locations, restricted content).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: **TBD** (depends on which dataset/evidence products are being monitored).
- Items involved: baseline/current item IDs **if** drift is computed over cataloged artifacts.
- Extension(s): **TBD** (only add if drift outputs are promoted to cataloged assets).

### DCAT

- Dataset identifiers: **TBD** (if drift outputs are attached to a DCAT dataset record).
- License mapping: inherit from dataset/evidence product license.
- Contact / publisher mapping: inherit from dataset/evidence product publisher.

### PROV-O

- `prov:wasDerivedFrom`: baseline + current artifacts (entities)
- `prov:wasGeneratedBy`: a drift `prov:Activity` (the detector run)
- Activity / Agent identities: record the detector name/version and the run environment (as permitted)

### Versioning

- Detector implementations should be versioned (SemVer recommended).
- Drift report must include the detector version and baseline/current refs so comparisons remain meaningful.

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
| Drift detectors (this area) | Detect distribution/output/schema changes | Structured drift reports + telemetry |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Detector interface | `tools/ai/drift/detectors/base.py` *(proposed; not confirmed in repo)* | SemVer + changelog |
| Drift report schema | `schemas/telemetry/` or `schemas/ai/` *(TBD; not confirmed in repo)* | SemVer + contract tests |
| Telemetry signals | `docs/telemetry/` + `schemas/telemetry/` | Schema bump required |

### Extension points checklist (for future work)

- [ ] Data: detectors added for a new domain’s artifacts (`data/<domain>/...`)
- [ ] STAC: drift outputs promoted as cataloged assets (if needed)
- [ ] PROV: drift activities recorded for promoted outputs
- [ ] Graph: drift signals linked to affected entities (if applicable)
- [ ] APIs: expose drift summaries (requires API contract doc)
- [ ] UI: add quality/audit surfaces (requires UI registry + access rules)
- [ ] Focus Mode: ensure provenance-linked disclosure rules remain intact
- [ ] Telemetry: new signals documented + schema version bumped

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Drift detectors should **not** introduce narrative claims.
- If drift results are surfaced at all, they should appear as **non-narrative audit/quality metadata** (e.g., “data quality warning” banner) and must not be presented as historical fact.

### Provenance-linked narrative rule

- Every narrative claim must trace to a dataset / record / asset ID (drift results can only add *quality context*, not facts).

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter, headings, lint)
- [ ] Unit tests for detectors (golden fixtures recommended)
- [ ] Schema validation for drift reports (if a schema exists)
- [ ] Determinism check (repeat run yields same outputs)
- [ ] Redaction checks (no prohibited sensitive fields in outputs)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run drift detectors against a baseline/current pair
# python -m tools.ai.drift.run --baseline <ref> --current <ref> --out mcp/runs/<run_id>/drift/

# 2) run tests
# pytest -q

# 3) validate schemas (if drift report schema exists)
# <schema-validator-cmd>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `kfm.drift.<detector_slug>.status` *(proposed)* | Drift runner | `docs/telemetry/` + `schemas/telemetry/` |
| `kfm.drift.<detector_slug>.<metric>` *(proposed)* | Drift runner | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- New detectors that touch sensitive domains or change gating behavior should be reviewed under `docs/governance/ROOT_GOVERNANCE.md`.
- New telemetry signals require updates in `docs/telemetry/` and schema changes in `schemas/telemetry/` (with a version bump).

### CARE / sovereignty considerations

- Drift work must not increase exposure risk: avoid logging sensitive locations, culturally restricted knowledge, or raw content.
- If drift is computed over sensitive corpora, ensure outputs are aggregate-only and reviewed before broader sharing.

### AI usage constraints

- This doc permits: summarize, structure_extract, translate, keyword_index.
- This doc prohibits: generating policy, inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial detectors README | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
