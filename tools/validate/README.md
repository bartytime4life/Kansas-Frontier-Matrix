---
title: "KFM Tools — Validation Suite (CI Gates + Local Checks)"
path: "tools/validate/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:tools:validate:readme:v1.0.0"
semantic_document_id: "kfm-tools-validate-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:validate:readme:v1.0.0"
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

# KFM Tools — Validation Suite (CI Gates + Local Checks)

## 📘 Overview

### Purpose

- Document the **validation suite** that supports KFM’s CI gates and local “pre-flight” checks.
- Provide a single place to understand:
  - what belongs under `tools/validate/`,
  - how validators should behave (deterministic, safe, contract-aligned),
  - how validation maps to KFM’s pipeline and governance constraints.

### Scope

| In Scope | Out of Scope |
|---|---|
| Markdown protocol validation for governed docs | Implementing ETL pipelines (belongs in `src/pipelines/`) |
| Schema validation (STAC / DCAT / PROV + other contract schemas) | Running/operating the graph database (belongs in ops/runbooks; code in `src/graph/`) |
| Story Node validation (template compliance + provenance references) | Building frontend/UI features (belongs in `web/`) |
| API contract tests (OpenAPI/GraphQL contract verification) | Authoring new governance policy (belongs in `docs/governance/`) |
| Security + sovereignty scanning gates (as applicable) | Cloud deployment specifics (belongs under `tools/` ops materials or separate ops repos) |
| Repo lint rules that enforce canonical structure | “Business logic” validation inside product code |

### Audience

- Primary: contributors and maintainers running validations locally and in CI.
- Secondary: governance reviewers and integrators who need to confirm contract compliance.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc include:
  - **CI gate**, **validator**, **contract artifact**, **evidence artifact**, **domain pack**, **Story Node**, **Focus Mode**, **STAC**, **DCAT**, **PROV**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | CI gate mapping + v13 readiness checklist |
| Markdown Work Protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Standards | Governs front-matter + structure (not confirmed in repo) |
| STAC/DCAT/PROV Profiles | `docs/standards/` | Standards | Profiles and mappings (some may be placeholders) |
| Schemas | `schemas/` | Standards/Engineering | Machine-validated contract artifacts |
| This validation suite | `tools/validate/` | Engineering | Implementation + docs for validators |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Gate matrix included (what runs, when, and what it checks)
- [ ] Reproduction steps listed (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No repo-specific commands invented without confirmation (placeholders clearly marked)

## 🗂️ Directory Layout

### This document

- `path`: `tools/validate/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/` | CI definitions that invoke validators (not confirmed in repo) |
| Standards | `docs/standards/` | Protocols + profiles validators should enforce |
| Templates | `docs/templates/` | Governing templates (incl. Story Node + Universal Doc) |
| Schemas | `schemas/` | JSON Schemas (and optional shape bundles) used by validators |
| Data catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence outputs that may be schema-validated |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts to validate |
| API | `src/server/` | Contract-first boundary; API tests validate published contracts |
| Tests | `tests/` | Unit/integration tests that may be part of CI gates |

### Expected file tree for this sub-area

~~~text
📁 tools/
└── 📁 validate/
    ├── 📄 README.md
    ├── 📁 markdown/            # optional; not confirmed in repo
    ├── 📁 schemas/             # optional; not confirmed in repo
    ├── 📁 story_nodes/         # optional; not confirmed in repo
    ├── 📁 api/                 # optional; not confirmed in repo
    ├── 📁 security/            # optional; not confirmed in repo
    └── 📁 repo_lint/           # optional; not confirmed in repo
~~~

## 🧭 Context

### Background

KFM treats validation as a first-class safeguard: governed docs, schemas, story artifacts, and API contracts are expected to fail CI deterministically when invalid, and (where appropriate) skip checks only when the relevant inputs are not present.

### Assumptions

- Validators run against a checked-out repository state (local or CI).
- Validators should be deterministic and, by default, not rely on network access.
- Validators should not mutate source artifacts unless explicitly documented and isolated.

### Constraints / invariants

- Preserve canonical pipeline ordering and enforce contract boundaries (e.g., contract-first schemas, API boundary).
- CI behavior expectation:
  - **validate if present**
  - **fail if invalid**
  - **skip if not applicable**
- Repo lint expectations include:
  - no YAML front-matter in code files,
  - no `README.me`,
  - no duplicate canonical homes without explicit deprecation markers.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What are the concrete validator entrypoints/commands (Python, Node, Make, etc.)? | TBD | TBD |
| Where are machine-readable validation reports stored (e.g., `mcp/runs/`, `data/reports/`)? | TBD | TBD |
| Which schema engine(s) are used (JSON Schema only vs optional SHACL)? | TBD | TBD |
| What’s the canonical list of “optional roots” that trigger skip behavior? | TBD | TBD |

### Future extensions

- Add domain-pack validators (ensure each domain has staging + mappings + tests + docs).
- Add telemetry-focused validators (security posture and governance signals).
- Add performance budgets for validation runtime in CI.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["Repo checkout"] --> B["tools/validate/*"]
  B --> C{"Gate results"}
  C -->|pass| D["CI green"]
  C -->|fail| E["CI red (deterministic)"]
  C -->|skip (no inputs)| F["CI green (skipped)"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Developer/CI
  participant Val as tools/validate
  participant Repo as Working Tree

  Dev->>Val: run validators
  Val->>Repo: read docs/schemas/story nodes/contracts
  Repo-->>Val: artifacts
  Val-->>Dev: exit code + logs (+ optional report)
~~~

## 🔌 Interfaces & Contracts

### Inputs

Validators may read from (examples; adjust to actual repo):

- Governed Markdown docs in `docs/` (Markdown protocol checks)
- Contract schemas in `schemas/` (schema validation)
- Catalog outputs in `data/stac/`, `data/catalog/dcat/`, `data/prov/` (schema + structural integrity)
- Story Nodes in `docs/reports/story_nodes/` (Story Node validation)
- API contracts/tests in `src/server/` + `tests/` (API contract tests)
- Security configuration and policies in `.github/` + `docs/governance/` (security/sovereignty checks)

### Outputs

- Exit codes suitable for CI gating:
  - `0` = pass (or skipped with clear log message)
  - non-zero = fail
- Human-readable logs
- Optional machine-readable reports (JSON) — not confirmed in repo

### API / Schema contracts impacted

- KFM Markdown protocol (KFM-MDP)
- Schema profiles: STAC/DCAT/PROV
- Story Node schema
- UI registry schema (if used)
- API contracts (OpenAPI/GraphQL) and their tests

## 📦 Data & Evidence

### Datasets produced/updated

- None (validators should not generate or mutate canonical datasets).

### Provenance & lineage

If validators emit reports/artifacts, they should be treated as **evidence** and recorded with:

- validator version
- inputs (paths + hashes)
- timestamp
- CI run identifier (where applicable)

*(Exact storage location not confirmed in repo.)*

### Evidence artifacts

- Validation reports can be used downstream (e.g., release manifests, audit trails) if captured and stored consistently.

## 🧯 Threat Modeling & Security

### Threats

- Secrets leaking through verbose logs
- Path traversal / unsafe file handling in validators
- Supply-chain risks in validator dependencies
- Accidental mutation of governed artifacts during validation runs

### Controls

- Prefer read-only validation; isolate any “fix” modes behind explicit flags.
- Avoid printing sensitive values; sanitize logs.
- Pin dependency versions and document upgrades.
- Run validators with least privilege in CI.

### Auditability

- Ensure every gate produces a clear pass/fail/skip statement.
- Prefer machine-readable reports when audit requirements grow.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Validation gates ensure Story Nodes meet structural rules and provenance references are present before publication.
- CI should prevent “unsourced narrative” Story Node artifacts from being published.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID (enforced by Story Node validation).

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

Minimum gate families (align to CI mapping):

- [ ] Markdown protocol validation (governed docs)
- [ ] Schema validation (STAC/DCAT/PROV + other contract schemas)
- [ ] Story Node validation
- [ ] API contract tests
- [ ] Security and sovereignty scanning gates
- [ ] Repo lint rules enforcement (canonical homes, naming constraints)

### Gate behavior contract (recommended)

| Gate family | When it runs | If inputs absent | If invalid |
|---|---|---|---|
| Markdown protocol | `docs/**` present | skip with log | fail |
| Schemas | `schemas/**` and/or catalog outputs present | skip with log | fail |
| Story Nodes | story node root present | skip with log | fail |
| API contracts | API project present | skip with log | fail |
| Security/sovereignty | security config present | skip with log | fail |
| Repo lint | always | n/a | fail |

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands and/or scripts
# (Commands are not confirmed in repo)

# 1) Markdown protocol validation
# <TBD>

# 2) Schema validation (STAC/DCAT/PROV + other schemas)
# <TBD>

# 3) Story Node validation
# <TBD>

# 4) API contract tests
# <TBD>

# 5) Security + sovereignty scanning gates
# <TBD>

# 6) Repo lint
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Validation gate outcomes | CI logs / reports | `releases/` and/or `mcp/runs/` (not confirmed in repo) |
| Security scan summary | CI | `releases/` and/or `docs/security/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that affect sovereignty rules, sensitive datasets, or public-facing narrative behavior should trigger governance review as defined in:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`
  - `docs/governance/REVIEW_GATES.md` (not confirmed in repo)

### CARE / sovereignty considerations

- Validators should avoid “inferring sensitive locations” or re-identifying protected communities.
- Where sovereignty rules apply, validation should fail if redaction/withholding requirements are violated.

### AI usage constraints

- This document’s AI transform permissions/prohibitions must remain aligned to KFM governance.
- Do not use AI transforms to create new policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial validation suite README scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
