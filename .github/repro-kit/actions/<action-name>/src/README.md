---
title: "KFM Repro Kit Action — ACTION_NAME — src README"
path: ".github/repro-kit/actions/<action-name>/src/README.md"
version: "v1.0.0-draft"
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

doc_uuid: "urn:kfm:doc:github:repro-kit:action:ACTION_NAME:src-readme:v1.0.0-draft"
semantic_document_id: "kfm-repro-kit-action-ACTION_NAME-src-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:github:repro-kit:action:ACTION_NAME:src-readme:v1.0.0-draft"
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

# KFM Repro Kit Action — `ACTION_NAME` — `src/README.md`

This is the **source-level** README for the KFM “Repro Kit” GitHub Action named `ACTION_NAME` (directory: `.github/repro-kit/actions/<action-name>/`). It is written using the **KFM Universal Governed Doc** structure so it can pass KFM’s **Markdown protocol validation** CI gate.

> Replace all `ACTION_NAME`, `<action-name>`, and `TBD` placeholders with the action’s actual details.

---

## 📘 Overview

### Purpose

- Describe **what this action enforces** (the “CI gate” it implements) and why it exists in KFM.
- Define the action’s **inputs/outputs**, deterministic behavior expectations, and safety constraints (FAIR+CARE + sovereignty).

**Design intent (aligned to KFM Master Guide):** KFM requires contributions to pass a set of CI gates (markdown protocol, schema validation, graph integrity, API contract tests, UI schema checks, and security/sovereignty scanning). This action should implement **one** gate (or one cohesive bundle) as a reusable GitHub Action.

### Scope

| In Scope | Out of Scope |
|---|---|
| Action behavior and contract (inputs/outputs) | Redesigning KFM pipeline architecture |
| Deterministic execution + reproducibility guidance | Implementing new data domains end-to-end |
| Logging/telemetry conventions (if applicable) | Changing governance policies (docs/governance) |
| Security + sovereignty safeguards for CI output | Bypassing/weakening CI gates |

### Audience

- Primary: CI maintainers, repo maintainers, contributors implementing/maintaining this action.
- Secondary: Domain maintainers who need to understand why a PR is blocked by this gate.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc: `repro-kit`, `CI gate`, `KFM-MDP`, `contract-first`, `evidence-first`, `classification propagation`, `sensitive-location leakage`.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action root | `.github/repro-kit/actions/<action-name>/` | CI | Expected home for the action |
| Action contract | `.github/repro-kit/actions/<action-name>/action.yml` | CI | **Not confirmed in repo** (expected GitHub Action contract file) |
| Action source | `.github/repro-kit/actions/<action-name>/src/` | CI | Implementation code + this README |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Docs | Canonical pipeline + CI gates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Structure used by this doc |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Used by Story Node validation gates |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Used by API contract validation gates |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | **not confirmed in repo** (per Master Guide) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (passes KFM-MDP checks)
- [ ] Action purpose and “gate(s)” clearly stated (what it blocks and why)
- [ ] Inputs/outputs documented and match `action.yml` (when present)
- [ ] Reproduction steps provided (how to run the same checks locally)
- [ ] Security + CARE/sovereignty considerations explicitly stated
- [ ] Version history updated

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/actions/<action-name>/src/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI / workflows | `.github/workflows/` | Workflow entrypoints that call this action |
| Repro kit actions | `.github/repro-kit/actions/` | Local, reusable GitHub Actions for KFM CI gates |
| Documentation | `docs/` | Canonical governed docs (Master Guide, templates, governance) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV, telemetry, etc.) |
| Pipelines | `src/pipelines/` | ETL + catalog builds/transforms |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API boundary | `src/server/` | Contracted APIs (no direct UI-to-graph access) |
| UI | `web/` | React/Map client (API-only; no direct graph calls) |
| MCP runs/experiments | `mcp/` | Runs, experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 .github/
└─ 📁 repro-kit/
   └─ 📁 actions/
      └─ 📁 <action-name>/
         ├─ 📄 action.yml                     (expected; not confirmed in repo)
         ├─ 📄 README.md                      (optional; not confirmed in repo)
         └─ 📁 src/
            └─ 📄 README.md                   (this file)
~~~

---

## 🧭 Context

### Background

KFM’s “v12-ready” definition of done includes CI gates such as:
- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation (STAC/DCAT/PROV + telemetry + story schemas where applicable)
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver/integration tests)
- UI schema checks (layer registry)
- Security + sovereignty scanning (secret scan, PII scan, sensitive-location leakage checks, classification propagation checks)

This action exists so the repository can **reuse** gate logic consistently across workflows, with predictable, reproducible outputs.

### Assumptions

- Workflow uses `actions/checkout` before running this action.
- The action can determine the set of changed files (either via git diff or workflow-provided inputs).
- The action is deterministic: same inputs → same results, and it avoids introducing nondeterminism in logs/report ordering.

### Constraints / invariants

- **Canonical pipeline ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary holds:** UI must not read Neo4j directly; all access is via contracted APIs.
- **No sensitive location leaks:** CI output must not print precise coordinates or restricted details that violate sovereignty policy.
- **No classification downgrades:** no downstream output may be less restricted than any upstream input in lineage.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which specific CI gate(s) does `ACTION_NAME` implement (single gate vs bundle)? | TBD | TBD |
| What is the exact input/output contract (final `action.yml`)? | TBD | TBD |
| What is the expected runner environment (OS, runtime, toolchain)? | TBD | TBD |

### Future extensions

- Add structured output formats (e.g., JSON report) to enable downstream aggregation.
- Add optional workflow summary output (GitHub Step Summary) with redaction-safe details.
- Add provenance hooks (emit run IDs / references in a consistent format) if the gate produces artifacts.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart TD
  PR[Pull Request / Push] --> WF[GitHub Workflow]
  WF --> A[KFM Repro Kit Action: ACTION_NAME]
  A -->|pass| OK[✅ Gate Passed]
  A -->|fail| BLOCK[⛔ Gate Failed (blocks merge)]

  subgraph GateScope[What this gate may validate]
    DOCS[Markdown protocol + link checks]
    CATALOGS[STAC/DCAT/PROV schema validation]
    GRAPH[Graph integrity tests]
    API[API contract tests]
    UI[UI schema checks]
    SEC[Secret/PII/sensitive-location scans]
  end

  A --> DOCS
  A --> CATALOGS
  A --> GRAPH
  A --> API
  A --> UI
  A --> SEC
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub Actions
  participant Gate as ACTION_NAME
  Dev->>GH: Push/PR
  GH->>Gate: Run action with inputs + workspace
  Gate-->>GH: Annotations + exit code + optional report
  GH-->>Dev: Check status (pass/fail)
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Repository workspace | Filesystem | `actions/checkout` | Must exist; required |
| Changed files (optional) | list/pathspec | git diff / workflow input | Validate paths are inside repo |
| Action configuration (optional) | file path | repo file (TBD) | Schema-validate config if present |
| Action inputs | strings/bools | `with:` in workflow | Validate required fields; default safely |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Pass/fail status | exit code | N/A | GitHub Actions semantics |
| Annotations | GH UI annotations | N/A | GitHub Actions annotation format |
| Gate report (optional) | JSON/Markdown | workflow artifact | Define schema if used |
| Logs | text | GH logs | Must avoid secrets/sensitive data |

### Sensitivity & redaction

- Do not print secrets, tokens, or raw PII.
- Do not print restricted coordinates or sensitive location details.
- If the gate analyzes content that may include sensitive references, report failures in a **redaction-safe** manner (e.g., file + line + rule ID, but no sensitive payload echoes).

### Quality signals

- Determinism: stable ordering of findings, stable formatting, stable exit codes.
- Completeness: action states what it checked (and what it explicitly did not check).
- Reproducibility: action documents how to run the same checks locally.

---

## 🌐 STAC, DCAT & PROV Alignment

> If `ACTION_NAME` validates or generates catalogs, document specifics here. If not applicable, keep the section but state “N/A”.

### STAC

- Collections involved: `data/stac/collections/**` (if applicable)
- Items involved: `data/stac/items/**` (if applicable)
- Extension(s): TBD

### DCAT

- Dataset identifiers: `data/catalog/dcat/**` (if applicable)
- License mapping: TBD
- Contact / publisher mapping: TBD

### PROV-O

- `prov:wasDerivedFrom`: source → derived artifacts (if applicable)
- `prov:wasGeneratedBy`: CI run ID / pipeline run ID (if applicable)
- Activity / Agent identities: define stable identifiers if emitting provenance

### Versioning

- If the action produces versioned outputs, link predecessor/successor appropriately (and avoid overwriting without version bump).

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub workflow | Orchestrates jobs and steps | `.github/workflows/*.yml` |
| Action contract | Declares inputs/outputs | `action.yml` (expected; not confirmed in repo) |
| Action implementation | Runs gate logic | `src/` |
| Validators/scanners | Perform checks | repo tools / scripts / libraries (TBD) |
| Reporter | Writes annotations/report | GitHub Actions APIs / stdout |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Action I/O | `.github/repro-kit/actions/<action-name>/action.yml` | Change inputs/outputs with semver bump |
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| UI registry schema | `web/**` (TBD) | Schema-validated |

### Extension points checklist (for future work)

- [ ] Add/expand the gate to cover an additional CI requirement (justify scope)
- [ ] Add structured report output + schema
- [ ] Add telemetry signals (see Validation section)
- [ ] Add “changed-files only” mode for faster PR feedback

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Indirectly: by ensuring Story Nodes and narrative artifacts merged into main are **template-compliant** and **provenance-linked**, preventing unsourced narrative from reaching Focus Mode.

### Provenance-linked narrative rule

- Any gate that checks Story Nodes should confirm:
  - required citations exist,
  - fact vs inference vs hypothesis is separated where required,
  - any “AI-generated” content is opt-in and clearly labeled (if present).

### Optional structured controls

~~~yaml
# If ACTION_NAME inspects Focus Mode control blocks, specify what it expects.
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Determine scope (all files vs changed files)
- [ ] Run the gate’s validator(s)
- [ ] Emit redaction-safe annotations
- [ ] Produce optional structured report artifact (if used)
- [ ] Exit non-zero on errors (and configurable on warnings, if desired)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands.
# Goal: run the exact same checks locally as CI runs in ACTION_NAME.

# 1) (optional) set up toolchain
# 2) run validator(s) with the same configuration as CI
# 3) inspect report output and exit code

# Example:
# ./tools/validate/validate_docs.sh
# ./tools/validate/validate_catalogs.sh
# ./tools/validate/validate_security.sh
~~~

### Telemetry signals (if applicable)

If this action emits structured signals (recommended for auditability), align to KFM’s suggested telemetry events such as:
- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (scope, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Treat changes to this action as governance-relevant when they:
  - reduce/relax CI checks,
  - modify redaction behavior,
  - change how sensitivity/classification is validated,
  - change what gets logged/emitted in reports.

### CARE / sovereignty considerations

- CI output must not become a side-channel for restricted content.
- Findings should be specific enough to fix issues, but redaction-safe.
- Enforce “no classification downgrades” in any derived outputs the action produces.

### AI usage constraints

- If `ACTION_NAME` uses AI assistance in any way (not typical for CI), it must be:
  - opt-in,
  - clearly labeled as AI-generated,
  - accompanied by uncertainty/confidence metadata where applicable,
  - prohibited from inferring or revealing sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-29 | Initial scaffold for action `ACTION_NAME` source README | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`