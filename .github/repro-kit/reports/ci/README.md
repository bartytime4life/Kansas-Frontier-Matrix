---
title: "KFM Reproducibility Kit — CI Reports"
path: ".github/repro-kit/reports/ci/README.md"
version: "v1.0.0"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-reports-ci-readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-reports-ci-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-reports-ci-readme:v1.0.0"
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

# KFM Reproducibility Kit — CI Reports

## 📘 Overview

### Purpose

This directory defines **how KFM CI results are recorded as reproducibility reports**.

CI reports exist to make every “green” run reviewable and replayable by capturing:

- **Gate outcomes** (schema validation, contract tests, governance scans, etc.)
- **Run identifiers** (commit SHA, workflow run ID, environment identifiers)
- **Evidence of determinism** (checksums, stable IDs, diff summaries where applicable)

These reports are the reviewer-facing “receipt” that the KFM pipeline contract was honored end-to-end.

### Scope

| In Scope | Out of Scope |
|---|---|
| CI report formats and naming conventions | Implementing GitHub workflows or choosing specific action versions |
| Minimum metadata fields required for reproducible CI results | Handling production secrets, privileged data access, or non-public fixtures |
| How CI gates map to KFM subsystems (ETL/Catalog/Graph/API/UI/Story/Focus) | Defining new governance policies |
| How to store sanitized examples of reports for review | Committing large CI artifacts, full datasets, or restricted outputs |

### Audience

- Primary: CI maintainers and repo maintainers reviewing PRs
- Secondary: contributors who need to understand why CI failed and how to reproduce locally

### Definitions

- Glossary link: `docs/glossary.md` (*not confirmed in repo*; keep one canonical glossary if present)
- Terms used in this doc:
  - **CI gate**: a required check that must pass before merge (schema validation, tests, scans).
  - **CI report bundle**: a set of machine-readable + human-readable outputs summarizing CI gates.
  - **Provenance completeness**: CI confirmation that required STAC/DCAT/PROV artifacts exist and link correctly.
  - **Governance scan**: automated checks that enforce sovereignty/CARE constraints (no sensitive leakage, correct classification propagation).
  - **Deterministic check**: an output hash comparison or stable-ID integrity check against an expected baseline.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + CI gate expectations |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governed structure for this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | CI should validate correct use for Story Nodes |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | CI should validate contract changes using this |
| Schemas | `schemas/` | Standards | STAC/DCAT/PROV/story/ui/telemetry schemas (as present) |
| CI workflows | `.github/workflows/` | CI | Workflow definitions (not described here) |
| Repro kit root | `.github/repro-kit/` | CI/Docs | Entry points + runbooks |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] CI report expectations map directly to documented minimum CI gates
- [ ] Report bundle metadata is sufficient to reproduce or audit a CI run
- [ ] Governance and sovereignty scanning expectations are explicit
- [ ] This README is updated when CI report formats change

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/reports/ci/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/` | Gate definitions, job orchestration |
| Repro kit | `.github/repro-kit/` | Repro helper docs, scripts, actions |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Published boundary artifacts |
| Graph build | `src/graph/` | Ontology bindings + ingest/migrations |
| API boundary | `src/server/` | Contracted API + redaction logic |
| UI | `web/` | React/Map UI + Focus Mode UI |
| Tests | `tests/` | Unit + integration tests |
| MCP | `mcp/` | Runs, experiments, model artifacts |

### Expected file tree for this sub-area

> Recommended structure; some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 reports/
        └── 📁 ci/
            ├── 📄 README.md
            ├── 📁 schemas/                 # optional: JSON Schema for CI report JSON
            ├── 📁 templates/               # optional: report markdown templates
            ├── 📁 examples/                # optional: sanitized example bundles
            └── 📁 assets/                  # optional: diagrams, icons for reports
~~~

## 🧭 Context

### Background

KFM is designed around a strict, contract-first pipeline that must remain reproducible and auditable. CI is the enforcement layer: it runs a defined set of checks and produces artifacts that show whether the pipeline contracts were met.

CI reports should reflect the non-negotiable pipeline order:

ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode

### Assumptions

- CI validates the work *without* bypassing subsystem boundaries.
- The UI never reads the graph directly; all access flows through contracted APIs.
- The “Focus Mode rule” is treated as a hard gate: Focus Mode consumes only provenance-linked content.

### Constraints and invariants

- CI must not require production secrets to run baseline gates.
- CI must fail on governance-relevant violations, including:
  - sensitive location leakage,
  - classification propagation errors,
  - prohibited AI behaviors implied by artifacts.
- Report outputs must be safe to share at the repo’s classification level (default: open/public).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Are CI reports stored as CI artifacts only, or do we commit sanitized report snapshots under `.github/repro-kit/reports/ci/examples/`? | TBD | TBD |
| What is the canonical machine-readable CI report schema location: `schemas/telemetry/` vs `.github/repro-kit/reports/ci/schemas/`? | TBD | TBD |
| Do release runs require SBOM/SLSA attestations in addition to PR CI runs? | TBD | TBD |

### Future extensions

- Provide a single machine-readable report schema for all CI gates (lint/schema/tests/scans).
- Add sanitized example bundles that reviewers can use to understand expected outputs.
- Add a mapping table that links each CI gate to:
  - the contract artifact it protects,
  - the owning subsystem,
  - the remediation runbook.

## 🗺️ Diagrams

### CI report flow

~~~mermaid
flowchart TD
  A["PR / Push"] --> B["CI workflows (.github/workflows)"]
  B --> C["Run gates: lint · schemas · tests · scans"]
  C --> D["Generate CI report bundle"]
  D --> E["Publish as CI artifact / attach to PR"]
  D --> F["Optional: record run metadata under mcp/runs"]
  C --> G["Fail build if any required gate fails"]
~~~

### Gate mapping to pipeline stages

~~~mermaid
flowchart LR
  subgraph CI["CI gates produce CI reports"]
    L["Markdown protocol lint"] --> R["CI report bundle"]
    S["STAC/DCAT/PROV schema validation"] --> R
    G["Graph integrity tests"] --> R
    A["API contract tests"] --> R
    U["UI registry + accessibility checks"] --> R
    V["Sovereignty + security scans"] --> R
  end
~~~

## 📦 Data & Metadata

### CI report bundle goals

A CI report bundle should be:

- **Diffable**: PR reviewers can compare two bundles (e.g., before/after).
- **Traceable**: every bundle ties to a commit SHA and workflow run ID.
- **Safe**: does not embed restricted data or precise sensitive locations.
- **Portable**: can be attached to PRs/releases as artifacts without special tooling.

### Recommended bundle contents

> These are recommended conventions. Filenames may vary (**not confirmed in repo**).

| Artifact | Format | Purpose | Notes |
|---|---|---|---|
| `ci_summary.md` | Markdown | Human-readable summary of gate outcomes | Should include links to logs and artifact paths |
| `ci_gates.json` | JSON | Machine-readable gate results | Validated by a JSON Schema if defined |
| `artifact_manifest.json` | JSON | Lists produced artifacts, checksums, and locations | Prefer stable IDs where possible |
| `checksums.sha256` | text | Hash list for key outputs | Hash only safe-to-share artifacts |
| `sbom.*` | SPDX/CycloneDX | Software bill of materials | Optional; typically for releases |
| `slsa_attestation.*` | JSON | Supply chain attestation | Optional; typically for releases |

### Minimum metadata fields

For any machine-readable CI report object, include at minimum:

- `report_version`
- `generated_at`
- `repo`
- `commit_sha`
- `workflow_name`
- `workflow_run_id`
- `job_name`
- `overall_status`
- `gates[]`:
  - `gate_id`
  - `status`
  - `inputs`
  - `outputs`
  - `notes`
  - `links[]`

### Inputs

| Input | Where from | Why it matters |
|---|---|---|
| Commit SHA | GitHub context | Primary reproducibility anchor |
| Pipeline configs | `src/pipelines/` + domain runbooks | Determinism depends on config |
| Schemas/contracts | `schemas/`, `src/server/contracts/` | Gate validations are contract-first |
| Fixture datasets | repo-defined | Enables deterministic regression checks |

### Outputs

| Output | Where | Contract expectation |
|---|---|---|
| Gate results | CI artifacts | Must clearly show pass/fail per required gate |
| Validation logs | CI artifacts | Must be linkable from summaries |
| Hash comparisons | CI artifacts | Must identify baseline and method |
| Governance scan findings | CI artifacts | Must not leak sensitive details in public logs |

### Sensitivity and redaction

CI reports must not include:

- secrets or credentials,
- raw restricted datasets,
- precise coordinates for sensitive places,
- personally identifying information.

If a governance scan fails, the report should:

- describe the failure category (e.g., “sensitive location leakage”),
- reference the file path(s) and rule ID(s),
- avoid reproducing the sensitive content in the summary.

### Quality signals

- **Determinism**: repeated runs (same inputs + config + code revision) match expected hashes/stable IDs.
- **Completeness**: required boundary artifacts exist (STAC/DCAT/PROV where applicable).
- **Contract integrity**: schema + contract tests pass.
- **Governance safety**: sovereignty and classification checks pass.

### Handling non-bitwise reproducibility

When outputs cannot be byte-for-byte deterministic (e.g., floating point, platform variance), CI reports must document:

- the comparison method (tolerance/threshold),
- the expected numeric range,
- the environment identifiers (OS, runtime versions),
- whether the variance impacts downstream provenance or stable identifiers.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- CI reports should include a gate outcome for validating STAC Collections and Items when present.
- Gate outputs should list:
  - count of validated items,
  - failing file paths,
  - schema/profile version used.

### DCAT

- CI reports should include a gate outcome for validating required DCAT records when present.
- CI should confirm DCAT discovery integrity (e.g., expected dataset entries exist for published outputs).

### PROV

- CI reports should include a gate outcome confirming PROV bundles exist and link:
  - raw → work → processed outputs,
  - pipeline activity/run IDs,
  - software/tool identifiers where required.

### Versioning

- CI should fail on breaking contract changes unless version bumps and compatibility strategy are provided.
- CI reports should capture the versions of profiles/contracts used in validation.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI workflows | Orchestrate gates | `.github/workflows/` |
| Repro kit reports | Document report formats | `.github/repro-kit/reports/` |
| Validators | Validate schemas and profiles | repo-defined tooling under `tools/` and/or `src/pipelines/` |
| Graph tests | Validate ontology + constraints | `src/graph/` + `tests/` |
| API contract tests | Enforce REST/GraphQL contracts | `src/server/` + contract tests |
| UI checks | Validate registries + a11y | `web/` + UI schemas/tests |

### Interfaces and contracts

- **JSON schemas** (canonical): `schemas/` define key artifact shapes (STAC, DCAT, PROV, UI registries, telemetry) and should be validated in CI.
- **API schemas**: OpenAPI and/or GraphQL schemas (repo-defined location) must be backed by contract tests.
- **Layer registry schemas**: UI registry artifacts should be schema-validated to prevent hidden data leakage.

## 🧠 Story Node and Focus Mode Integration

### Story Node validation

CI reports should include Story Node gate outcomes when Story Node files are changed:

- template compliance,
- citation presence and formatting,
- fact vs inference vs hypothesis labeling where required,
- governance and sensitivity checks.

### Focus Mode gate

Focus Mode is evidence-only by design. CI reports must record a hard gate outcome that confirms:

- Focus Mode consumes only provenance-linked context bundles
- unsourced narrative is not allowed in provenance-locked views
- any AI/predictive content is opt-in and carries uncertainty metadata if present

## 🧪 Validation and CI/CD

### Minimum CI gates for v12-ready contributions

> This list is the baseline set of gates CI reports must be able to represent.

- [ ] Markdown protocol validation
- [ ] JSON schema validation for STAC/DCAT/PROV and telemetry artifacts (where applicable)
- [ ] Graph integrity tests
- [ ] API contract tests
- [ ] UI layer registry schema checks
- [ ] Security and sovereignty scanning gates (where applicable)

### CI report expectations checklist

- [ ] Summary report exists and is readable in GitHub UI
- [ ] Machine-readable gate results exist
- [ ] Each gate has:
  - a stable `gate_id`,
  - pass/fail status,
  - links to logs,
  - remediation hint or owning subsystem
- [ ] Any governance failure is described without leaking restricted content
- [ ] Report bundle captures commit SHA and run ID

### Local reproduction parity

Repo-specific commands are **TBD**. This directory should eventually link to the local repro entrypoints that generate the same checks and the same CI report bundle format.

~~~bash
# Placeholder: replace with repo-specific commands when added.

# 1) Run doc lint / markdown protocol validation
# <TBD>

# 2) Validate STAC/DCAT/PROV artifacts
# <TBD>

# 3) Run unit + integration tests (pipelines/graph/api/ui)
# <TBD>

# 4) Run governance scanning gates (secrets/PII/sensitive location)
# <TBD>
~~~

### Telemetry signals

> Optional, but recommended. If emitted, CI reports should list which signals fired and why.

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` | governance scan | CI logs / artifacts |
| `redaction_applied` | redaction pipeline | CI logs / artifacts |
| `catalog_published` | catalog stage | CI logs / artifacts |
| `promotion_blocked` | governance gate | CI logs / artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when changes introduce:

- new sensitive layers,
- new AI narrative behaviors,
- new external data sources,
- new public-facing endpoints.

### CARE and sovereignty considerations

CI reports must explicitly support sovereignty enforcement by recording outcomes for:

- sensitive location leakage checks,
- classification propagation checks,
- prohibited inferences such as inferring sensitive locations from partial data.

### AI usage constraints

- CI reports must not imply prohibited AI actions.
- Any AI-assisted user-facing output must remain evidence-led and provenance-linked.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial CI reports README | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
