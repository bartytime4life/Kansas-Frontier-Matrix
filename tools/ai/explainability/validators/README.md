---
title: "KFM — Explainability Validators (README)"
path: "tools/ai/explainability/validators/README.md"
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

doc_uuid: "urn:kfm:doc:tools:ai:explainability:validators-readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-explainability-validators-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:explainability:validators-readme:v1.0.0"
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

# KFM — Explainability Validators

## 📘 Overview

### Purpose
- This README defines conventions and expectations for **explainability validator** utilities under `tools/ai/explainability/validators/`.
- These validators act as **quality + governance gates** for explainability artifacts so they are safe to store as evidence products and (when applicable) safe to surface through APIs/UI in provenance-constrained contexts.

### Scope

| In Scope | Out of Scope |
|---|---|
| Validating explainability artifacts (e.g., SHAP/LIME outputs) for schema, completeness, and safety | Training models or generating explainability values |
| Ensuring validator outputs are reproducible, deterministic, and diffable | UI rendering and UX decisions |
| Emitting validator results suitable for AI validation reports and provenance logging | Publishing Story Nodes (separate curator workflow) |
| Redaction / generalization checks on validator outputs | Defining new governance policy (handled in governed docs) |

### Audience
- Primary: AI/ML contributors implementing explainability or AI evidence products.
- Secondary: pipeline maintainers, reviewers, auditors, and curators consuming AI validation reports.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Explainability artifact**: machine output that explains model behavior (e.g., feature attributions).
  - **Validator**: deterministic check that produces pass/fail + diagnostics for an artifact.
  - **AI validation report**: run-level audit artifact capturing model checks, explainability summaries, and governance signals.
  - **Uncertainty metadata**: confidence score(s), intervals, or explicit “unknown/uncertain” flags when AI output is probabilistic.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `tools/ai/explainability/validators/README.md` | AI subsystem | Governed via KFM Markdown Protocol |
| Explainability subsystem entrypoint | `tools/ai/explainability/README.md` | AI subsystem | Parent README (expected) |
| Validator outputs (recommended) | `data/reports/ai/validation/**` | AI runs | **not confirmed in repo** (recommended canonicalization) |
| Provenance bundles | `data/prov/**` | Pipeline | Canonical location for PROV artifacts |
| Schemas for validator outputs | `schemas/**` | Schemas | **not confirmed in repo** (add if missing) |
| Run logs / experiment artifacts | `mcp/runs/**` | MCP | **not confirmed in repo** (recommended for run-level storage) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Scope and contracts are explicit (what validators must/must not do)
- [ ] Proposed directory layout is documented (and labeled if not yet implemented)
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `tools/ai/explainability/validators/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tools | `tools/` | Developer tooling, scripts, and validators |
| AI tooling | `tools/ai/` | AI utilities (model runs, evaluation, explainability) |
| Explainability | `tools/ai/explainability/` | Explainability docs + utilities |
| Validators | `tools/ai/explainability/validators/` | Deterministic explainability validation checks |
| Reports | `data/reports/` | Run outputs / evidence products (as needed) |
| Provenance | `data/prov/` | PROV bundles for transformations and runs |
| Schemas | `schemas/` | JSON Schemas + constraints validated in CI |
| Pipelines | `src/pipelines/` | ETL/catalog/graph build pipelines |
| Graph | `src/graph/` | Ontology bindings, constraints, migrations |
| APIs | `src/server/` (or repo equivalent) | API contracts + tests (UI never queries graph directly) |

### Suggested local structure (may differ; label non-existent dirs before adding)
~~~text
📁 tools/
└── 🤖 ai/
    └── 🧠 explainability/
        ├── 📄 README.md
        └── ✅ validators/
            ├── 📄 README.md
            ├── 📁 checks/              # not confirmed in repo
            ├── 📁 schemas/             # not confirmed in repo
            ├── 📁 fixtures/            # not confirmed in repo
            └── 📁 reports/             # not confirmed in repo (local/dev-only)
~~~

## 🧭 Context

### Why validators exist
- KFM’s architecture treats provenance and auditability as first-class requirements, and AI-derived content must be transparent about provenance and limitations.
- Explainability artifacts are part of the audit trail: they help justify why an AI system made a classification, linkage, extraction, or summary decision.
- Validators provide a **deterministic enforcement layer** before an explanation is stored, referenced, or exposed via downstream layers (graph/API/UI).

### Where validators run in the canonical pipeline
KFM’s canonical pipeline ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

Validators align to the **AI evidence** portion of the pipeline, typically:
- after a model run produces explainability artifacts and
- before those artifacts are recorded as run evidence and/or linked into graph/API/UI workflows.

### Non-negotiable behavior for validator code
- Deterministic: same inputs → same outputs (byte-diff-friendly when feasible).
- Offline-first: no network calls in CI contexts unless explicitly approved.
- No secrets: do not read tokens/keys; do not write sensitive config into outputs.
- Redaction-aware: never emit restricted locations or sensitive fields unless the output classification allows it.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["AI Model Run Outputs"] --> B["Explainability Artifacts (e.g., SHAP/LIME)"]
  B --> C["Explainability Validators (this directory)"]
  C --> D["AI Validation Report (human-readable + machine-readable)"]
  C --> E["PROV Bundle (validator activity + outputs)"]
  D --> F["Graph / API Layer (optional ingest & serving)"]
  E --> F
  F --> G["UI / Focus Mode (provenance-linked, opt-in for AI/predictive content)"]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Explainability artifact(s) | JSON/CSV/Parquet (TBD) | Model run outputs | schema + required fields + ranges |
| Run manifest (model + params) | JSON (TBD) | run system / MCP logs | required IDs + timestamps |
| Source references | IDs/URIs (TBD) | catalogs/graph refs | resolvable identifiers only |
| Redaction policy hints | config (TBD) | governance layer | enforced classification + sensitivity |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validator results (pass/fail + diagnostics) | JSON (recommended) | `data/reports/ai/validation/<run_id>/validators.json` | **not confirmed in repo** (add schema under `schemas/`) |
| AI validation report summary | Markdown/JSON (TBD) | `data/reports/ai/validation/<run_id>/report.md` | **not confirmed in repo** |
| PROV activity bundle | JSON-LD | `data/prov/<run_id>/prov.jsonld` | validate vs PROV profile |

### Sensitivity & redaction
- If validator outputs could contain:
  - precise coordinates of restricted locations,
  - culturally sensitive knowledge,
  - or personal data (PII),
  then validators MUST either redact/generalize the field(s) or fail closed (depending on classification rules).

### Quality signals
- Provenance completeness: validator can identify inputs and reference run IDs.
- Uncertainty is present when the model output is probabilistic or inferential.
- No “orphan” references: identifiers in the artifact resolve to known datasets/entities where required.
- Output schema validity: validator outputs are machine-checkable.
- Reproducibility: outputs are stable across runs for the same inputs.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If explainability artifacts are promoted to “evidence products,” they should be representable as STAC assets or referenced by STAC Items/Collections.
- Validators should not generate STAC by default, but MAY enforce that any STAC references provided are well-formed.

### DCAT
- If explainability artifacts are published as dataset-level products, they should map to DCAT dataset views.
- Validators may enforce basic dataset metadata completeness when a DCAT mapping is present.

### PROV-O
- Validator execution itself is an auditable transformation:
  - Inputs: explainability artifacts + run manifests
  - Outputs: validator results + report summaries
- Record `prov:wasGeneratedBy`, `prov:used`, and Activity/Agent identities in a PROV bundle when applicable.

### Versioning
- When validator output schemas or required fields change, treat it as a contract change (semver + changelog).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Explainability validators | Validate explainability artifacts + emit results | CLI/module entrypoints (TBD) + JSON outputs |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked + opt-in AI |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| PROV constraints | `schemas/prov/` | Profile-aligned |
| Explainability report schema | `schemas/**` | **not confirmed in repo** (add if missing) |
| API schemas | `src/server/` + docs | Contract tests required |

### Extension points checklist (for future work)
- [ ] AI evidence: validator outputs treated as evidence artifacts and linked into Focus Mode (when approved)
- [ ] PROV: validator activity + agent identifiers recorded per run
- [ ] Schemas: validator output schema added and validated in CI
- [ ] APIs: endpoints expose validator results only via API contracts (no UI→graph direct access)
- [ ] Story/Focus Mode: any surfaced AI content remains opt-in + uncertainty-marked

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Default: validator artifacts are **audit evidence** for internal review.
- Optional (if productized): selected explainability summaries can be shown as provenance-linked “why the system thinks this” panels.
- Any predictive/AI-derived content remains opt-in and must carry uncertainty metadata.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

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
- [ ] Schema validation (STAC/DCAT/PROV and any validator output schemas)
- [ ] Graph integrity checks (if validator outputs are ingested)
- [ ] API contract tests (if outputs are exposed)
- [ ] UI schema checks (if surfaced in layer registry / UI config)
- [ ] Security and sovereignty checks (as applicable)
- [ ] Explainability validator suite runs on fixtures/samples

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands / entrypoints.

# 1) Run validator unit tests
#    (e.g., pytest tools/ai/explainability/validators)

# 2) Run validators on a local run folder
#    (e.g., python -m tools.ai.explainability.validators <args>)

# 3) Validate schemas (if validator outputs have schemas)
#    (e.g., a repo-specific schema lint command)

# 4) Run markdown lint/protocol validation (repo CI)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Validator pass rate | CI / runs | `docs/telemetry/` + `schemas/telemetry/` (TBD) |
| Redaction events count | validator outputs | `data/reports/**` (TBD) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that affect what becomes publishable evidence should be reviewed (especially where outputs could surface in Focus Mode).
- Any new AI narrative behaviors, sensitive layers, external sources, or public endpoints should trigger governance review.

### CARE / sovereignty considerations
- If outputs could reveal restricted locations or culturally sensitive knowledge, enforce generalization/redaction rules and log the decision in provenance/audit outputs.

### AI usage constraints
- Validators should support the “no unsourced narrative” posture by checking:
  - provenance references exist and resolve (where applicable),
  - AI/predictive content is clearly flagged,
  - uncertainty/confidence metadata is present when required,
  - and human-in-the-loop review remains possible (reports are readable and actionable).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for explainability validators | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
