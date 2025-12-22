---
title: "KFM Tools — AI Drift Checks"
path: "tools/ai/drift/README.md"
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

doc_uuid: "urn:kfm:doc:tools:ai-drift:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-drift-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai-drift:readme:v1.0.0"
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

# KFM Tools — AI Drift Checks

## 📘 Overview

### Purpose

This directory documents **AI drift checks** for KFM: repeatable, CI-friendly evaluations that detect **unexpected changes** in AI outputs (e.g., NLP extraction, classification, summarization) by comparing a **current run** against a **known baseline**.

The goal is to:
- prevent unreviewed regressions (or large behavior shifts) from silently entering the pipeline,
- keep drift checks reproducible and provenance-aware (PROV-aligned where applicable),
- support governance review triggers for new user-visible AI behavior.

> Note: “repo drift” (repository structure drift) is a separate concern handled by repo lint and structure standards, not by this tool README.

### Scope

| In scope | Out of scope |
|---|---|
| Baseline-vs-current comparisons on controlled fixture inputs | Training, fine-tuning, or selecting models |
| CI gating rules for “output hasn’t drastically changed” (unless intentional) | Real-time production monitoring stack (dashboards/alerts) |
| Drift reporting (diff summaries + metrics) | Deciding historical truth; drift checks only signal change |
| Schema/provenance/link-integrity “quality signals” *as they relate to AI outputs* | Full ETL validation for every domain (handled by ETL pipelines) |
| Redaction/sanitization rules for drift logs and artifacts | Publishing sensitive raw fixtures in public artifacts |

### Audience

- **Primary:** AI/ML and pipeline maintainers, CI maintainers, reviewers updating baselines.
- **Secondary:** Curators and governance reviewers validating user-visible AI behavior changes.

### Definitions

- **Baseline:** A versioned “expected output” snapshot for a fixed fixture set.
- **Fixture set:** A curated, licensed set of test inputs (documents/records) used for deterministic evaluation.
- **Output drift (regression):** Meaningful changes in structured outputs compared to baseline.
- **Data drift:** Changes in input distributions (when measurable in fixtures or sampled corpora).
- **Concept drift:** World/process changes that invalidate prior assumptions (rarely detectable with fixtures alone).
- **Schema drift:** Output shape changes (fields/types) that may require schema updates.
- **Provenance orphan:** Output items lacking source references (should not surface to Focus Mode).

### Key artifacts

| Artifact | Format | Expected path | Notes |
|---|---|---|---|
| Drift report (machine) | JSON | `mcp/runs/<run_id>/drift/report.json` *(not confirmed in repo)* | Primary CI artifact for gating |
| Drift summary (human) | Markdown | `mcp/runs/<run_id>/drift/summary.md` *(not confirmed in repo)* | Review-friendly diff summary |
| Baseline snapshot | JSON/NDJSON | `mcp/baselines/<baseline_id>/...` *(not confirmed in repo)* | Versioned expected outputs |
| PROV activity bundle | JSON-LD / TTL | `data/prov/<run_id>.*` *(not confirmed in repo)* | Treat drift run as an Activity |
| CI annotations | Text/JSON | CI-native | PR comment / checks interface |

### Definition of done

- [ ] Drift checks run deterministically on a fixed fixture set.
- [ ] Drift report includes: tool version, fixture version, baseline version, and diff/metrics.
- [ ] CI gate clearly signals pass/fail and why.
- [ ] Baseline update process is documented and requires review when user-visible behavior changes.
- [ ] Sensitive data is not leaked in logs/artifacts; redaction rules documented.

---

## 🗂️ Directory Layout

### This document
- `tools/ai/drift/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/raw/`, `data/work/`, `data/processed/` | Required staging (raw → work → processed) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/` | STAC + DCAT outputs (canonical) |
| Provenance | `data/prov/` | PROV bundles for transforms and runs |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/telemetry/…); drift schema recommended |
| Pipelines | `src/pipelines/` | ETL + catalog building pipelines |
| Graph | `src/graph/` | Graph ingest + ontology tooling |
| API boundary | `src/server/` | Contracts + endpoints; UI does not read Neo4j directly |
| UI | `web/` | React/MapLibre UI; consumes API outputs |
| Run logs / experiments | `mcp/` | Run manifests, experiments, evaluations |
| Tests / fixtures | `tests/` | Fixture corpora + unit/integration tests |
| Tools | `tools/` | Non-prod utilities, including this drift area |

### Expected file tree (this sub-area)

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 drift/
        └── 📄 README.md
~~~

> Additional scripts/schemas/fixtures for drift checks are **not confirmed in repo** and should only be added if/when implemented.

---

## 🧭 Context

### Background

KFM’s implementation approach calls for **AI quality guardrails**, including:
- unit tests for NLP pipelines with expected outputs,
- benchmarking (precision/recall when ground truth exists),
- **CI checks that run a small pipeline on sample text and ensure output hasn’t drastically changed unless intentionally**,
- governance oversight for deploying new user-visible AI behavior.

This README provides the documentation contract for that “output drift” portion.

### Assumptions

- A fixture set exists (or will be created) that is safe, licensed, and appropriate for CI.
- A baseline output snapshot exists (or will be created) for comparisons.
- Drift checks are designed to be deterministic or explicitly record nondeterminism sources.

### Constraints and invariants

Non-negotiables:
1. **Deterministic + replayable:** Same inputs + same versions must yield consistent drift results.
2. **No sensitive leakage:** Drift artifacts should avoid printing raw protected text or precise restricted locations.
3. **API boundary respected:** If drift results ever surface in UI, they do so through `src/server/` APIs.
4. **No unsourced narrative:** Drift checks must not encourage publishing AI output without provenance.

### Open questions

| Question | Owner | Target |
|---|---|---|
| Where should baselines live (`mcp/baselines/` vs `tests/fixtures/` vs release artifacts)? | TBD | TBD |
| What are “drastic change” thresholds per pipeline type? | TBD | TBD |
| Do we require manual sign-off to update baselines for user-visible AI behaviors? | Governance | TBD |
| What schema should define drift report structure? | AI tooling | TBD |

### Future extensions

- Nightly drift runs on broader samples (not just fixtures).
- Dashboard summaries of drift over time (still provenance-safe).
- Automated detection of schema drift (suggest schema updates + changelog entry).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  PR[Pull Request / Model or Prompt Change] --> CI[CI Pipeline]
  CI --> DR[AI Drift Runner]
  DR --> FIX[Fixture Inputs]
  DR --> BASE[Baseline Snapshot]
  DR --> REP[Drift Report]
  REP --> GATE{CI Gate}
  GATE -->|pass| MERGE[Merge / Release]
  GATE -->|fail| REVIEW[Review + Decide: Fix or Update Baseline]
  REP --> PROV[PROV Activity Bundle]
  PROV --> LOGS[Run Logs / MCP]
~~~

~~~mermaid
sequenceDiagram
  autonumber
  participant Dev as Developer
  participant CI as CI
  participant Drift as Drift Runner
  participant Base as Baseline Store
  participant Gov as Review/Governance

  Dev->>CI: Open PR (model/prompt/pipeline change)
  CI->>Drift: Run drift checks on fixture set
  Drift->>Base: Load baseline outputs
  Drift-->>CI: Emit drift report + pass/fail
  alt Fail (unexpected drift)
    CI-->>Dev: Block merge with diff summary
    Dev->>Gov: Request review if behavior is user-visible
  else Pass (within tolerance)
    CI-->>Dev: Allow merge
  end
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Fixture corpus | Text/JSON/etc | `tests/` or `mcp/` *(not confirmed in repo)* | License + sensitivity review |
| Baseline snapshot | JSON/NDJSON | `mcp/baselines/` *(not confirmed in repo)* | Schema validation + versioned |
| Current AI output | JSON/NDJSON | CI run output | Schema validation |
| Drift thresholds/config | YAML/JSON | `tools/ai/drift/` *(not confirmed in repo)* | Config schema validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Drift report | JSON | `mcp/runs/<run_id>/drift/report.json` *(not confirmed in repo)* | `schemas/...` *(not confirmed in repo)* |
| Human summary | Markdown | `mcp/runs/<run_id>/drift/summary.md` *(not confirmed in repo)* | Markdown protocol |
| PROV bundle | JSON-LD/TTL | `data/prov/<run_id>.*` *(not confirmed in repo)* | PROV profile validation |
| CI status | CI-native | PR checks | Deterministic pass/fail |

### Sensitivity & redaction

- Do not emit raw sensitive text into CI logs by default.
- Do not emit exact coordinates for restricted locations; use generalization rules.
- If fixtures contain sensitive material, keep them access-controlled and ensure CI handling aligns with sovereignty policy.

### Quality signals

In addition to “diff vs baseline”, drift checks should (where applicable) report:
- **Schema & completeness**: missing required fields or type mismatches.
- **Geometric validity**: geometry correctness (if outputs include spatial data).
- **Temporal consistency**: invalid or implausible date ranges.
- **Provenance completeness**: missing/empty source references (orphan outputs).
- **Data link integrity**: references to missing entity IDs.
- **Audit tags**: ensure AI-generated outputs carry “AI-generated” + confidence metadata.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Drift reports are not inherently geospatial assets, but may be attached as **assets** to the relevant STAC Item representing an AI “evidence product” (optional; not confirmed in repo).
- Collections involved: *(not confirmed in repo)*
- Items involved: *(not confirmed in repo)*
- Extension(s): *(not confirmed in repo)*

### DCAT

- Drift reports are typically internal QA artifacts; if published, they should map to DCAT as quality/provenance documentation linked from the relevant dataset record (optional; not confirmed in repo).

### PROV-O

Treat a drift run as a **PROV Activity**:
- `prov:used`: fixture corpus, baseline snapshot, model/prompt versions
- `prov:generated`: drift report + summary artifacts
- `prov:wasAssociatedWith`: the drift tool/agent identity (software version)

~~~text
Example (conceptual):
- Activity: drift_check_run_2025_12_22
  used: fixtures_vX, baseline_vY, model_vZ
  generated: drift_report_run_abc123
  associatedWith: tools/ai/drift@v1.0.0
~~~

### Versioning

- Baselines MUST be versioned.
- Baseline updates should link to predecessor/successor and include a rationale (especially when behavior is user-visible).

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Drift runner | Orchestrates fixture run + baseline compare | CLI / CI entrypoint *(not confirmed in repo)* |
| Comparator | Computes diffs and change rates | Library interface *(not confirmed in repo)* |
| Metrics | Optional numeric drift scores | Library interface *(not confirmed in repo)* |
| Reporter | Writes JSON + Markdown summaries | File outputs |
| Baseline store | Stores “expected outputs” snapshots | Versioned artifacts |
| CI integration | Enforces pass/fail thresholds | CI job step |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Drift report schema | `schemas/ai/drift_report.schema.json` *(not confirmed in repo)* | Semver + changelog |
| Fixture manifest | `tests/fixtures/...` *(not confirmed in repo)* | Versioned + reviewed |
| PROV bundle format | `schemas/prov/` | Must validate in CI |

### Extension points checklist (for future work)

- [ ] Add a drift report JSON schema under `schemas/`
- [ ] Add a small, safe fixture corpus under `tests/`
- [ ] Add a baseline snapshot store + versioning rules under `mcp/`
- [ ] Add CI job step(s) for drift checks
- [ ] Add PROV emission for drift runs
- [ ] Add API endpoint for drift status (if user-facing)
- [ ] Add UI badge/toggle behavior for AI suggestions (opt-in)

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Drift checks help ensure that any AI-assisted extraction feeding Story Nodes does not shift unexpectedly without review.
- If drift indicates missing provenance, outputs should not be eligible for Focus Mode consumption.

### Provenance-linked narrative rule

- Focus Mode only consumes **provenance-linked** content.
- Any predictive or AI-suggested content must be opt-in and carry uncertainty/confidence metadata.

### Optional structured controls (example)

~~~yaml
# Example policy shape — not confirmed in repo
drift_policy:
  max_changed_records_ratio: 0.05
  max_schema_errors: 0
  fail_on_provenance_orphans: true
  require_governance_review_for_user_visible_changes: true
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (for governed docs)
- [ ] Schema validation (STAC/DCAT/PROV/telemetry + drift report schema when present)
- [ ] Drift regression checks on fixture set (this tool)
- [ ] Graph integrity checks (if drift run touches graph import fixtures)
- [ ] API contract tests (if drift status is surfaced via API)
- [ ] Security and sovereignty scanning gates (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run drift checks against baseline
# (entrypoint not confirmed in repo)

# 2) validate schemas
# (validator commands not confirmed in repo)

# 3) run tests
# (test runner not confirmed in repo)
~~~

### Telemetry signals (if applicable)

| Signal | Type | Description |
|---|---|---|
| drift_changed_ratio | float | Fraction of outputs changed vs baseline |
| drift_schema_error_count | int | Count of schema validation failures |
| drift_provenance_orphan_count | int | Outputs missing provenance refs |
| drift_link_integrity_error_count | int | Broken/missing entity references |
| drift_confidence_shift | float | Aggregate confidence delta (if tracked) |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Drift-related changes that should trigger review:
- Updating baselines for **user-visible AI behavior changes**.
- Increasing tolerance thresholds without justification.
- Adding new fixture corpora with sensitive content.
- Any change that affects redaction/generalization rules for restricted locations.

### Sovereignty safety

- Apply sovereignty policy to any fixture content and drift artifacts.
- Log redaction/generalization actions (without leaking protected details).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial scaffolding for AI drift checks README | TBD |

---

Footer refs:
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/governance/ETHICS.md`