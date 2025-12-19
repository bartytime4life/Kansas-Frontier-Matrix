---
title: "KFM CI — README"
path: "docs/ci/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:ci:readme:v1.0.0"
semantic_document_id: "kfm-ci-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:readme:v1.0.0"
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

# KFM CI README

## 📘 Overview

### Purpose
This document describes the Continuous Integration expectations for the Kansas Frontier Matrix (KFM)
repository, focusing on validation gates that protect the canonical pipeline ordering and governance
constraints.

This README is a governed overview. It does not attempt to enumerate every workflow file or command
used by the repo. If CI workflow definitions exist in the repository (for example under `.github/`),
they are the implementation source of truth.

### Scope
| In Scope | Out of Scope |
|---|---|
| CI quality gates that keep KFM artifacts valid and governed (docs, schemas, data, graph, APIs, UI) | Hosting/provider-specific CI infrastructure details and secrets management configuration |
| Required validation categories for “v12-ready” contributions | Writing or changing governance policy text (must live under `docs/governance/`) |
| How to propose or extend CI checks without breaking contracts | Bypassing review, forcing merges, or disabling gates |

### Audience
- Primary: maintainers, reviewers, release managers
- Secondary: contributors adding data, pipelines, graph changes, API changes, UI changes, or Story Nodes

### Definitions
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: CI, validation gate, provenance, STAC, DCAT, PROV, contract test, “v12-ready”

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline and minimum CI gates live here |
| CI documentation | `docs/ci/README.md` | Maintainers | This document |
| GitHub automation | `.github/` | Maintainers | Workflows and community health files may live here (not confirmed in repo) |
| Schemas | `schemas/` | DataOps | Validation of STAC/DCAT/PROV/telemetry (not confirmed in repo) |
| Tests | `tests/` | Engineering | Unit/integration/contract tests (not confirmed in repo) |

### Definition of done for this document
- [ ] Front-matter complete + valid
- [ ] CI gates described match the Master Guide requirements
- [ ] Validation steps are listed and repeatable at a category level (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No secrets, credentials, or sensitive locations included

## 🗂️ Directory Layout

### This document
- `path`: `docs/ci/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI provider configuration | `.github/` | Workflow definitions, security files, templates (not confirmed in repo) |
| Documentation standards and templates | `docs/standards/`, `docs/templates/` | Markdown protocol and governed templates |
| Validation schemas | `schemas/` | JSON schemas for catalogs, telemetry, contracts (not confirmed in repo) |
| Pipeline code | `src/pipelines/` | ETL + catalog generation + transforms (not confirmed in repo) |
| Graph code | `src/graph/` | Ontology bindings, graph build, migrations (not confirmed in repo) |
| API code | `src/server/` | REST/GraphQL contracts + tests (not confirmed in repo) |
| UI code | `web/` | React/Map UI + layer registry + a11y checks (not confirmed in repo) |

### Expected file tree for this sub-area
The exact CI provider and filenames are not confirmed in repo. This is a target layout to keep CI
documentation discoverable and reviewable.

~~~text
📁 .github/
├── 📁 workflows/
│   ├── 📄 ci.yml
│   ├── 📄 security.yml
│   └── 📄 pages.yml
└── 📄 SECURITY.md

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 ci/
│   ├── 📄 README.md
│   ├── 📁 checklists/
│   │   ├── 📄 PR_CHECKLIST.md
│   │   └── 📄 RELEASE_CHECKLIST.md
│   └── 📁 runbooks/
│       └── 📄 CI_TROUBLESHOOTING.md
└── 📁 templates/
    ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
    ├── 📄 TEMPLATE__STORY_NODE_V3.md
    └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
~~~

## 🧭 Context

### Background
KFM is a multi-stage, contract-driven system. CI exists to prevent invalid artifacts from entering the
repository and to enforce non-negotiable invariants such as provenance-first, deterministic pipelines,
and the canonical stage ordering:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### Assumptions
- Git-based contribution flow with reviews and automated checks (not confirmed in repo)
- Data and narrative outputs must remain reproducible and provenance-linked

### Constraints and invariants
- The canonical pipeline ordering is preserved.
- Frontend consumes contracts via APIs only. UI must not read Neo4j directly.
- No unsourced narrative is permitted in Focus Mode contexts.
- Any sensitive content must follow sovereignty guidance, including redaction and generalization.
- CI must not leak secrets, credentials, or restricted locations in logs or artifacts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which CI provider and workflow files are authoritative in this repo? | Maintainers | TBD |
| Where are schema validators and contract tests implemented? | Maintainers | TBD |
| What is the release workflow and artifact publishing approach? | Maintainers | TBD |

### Future extensions
- Scheduled validations for dynamic sources and catalogs
- Preview environments for UI and docs (if supported)
- Dataset regression tests for geometry validity, ranges, and completeness
- Provenance audits that fail builds when required PROV fields are missing

## 🗺️ Diagrams

### System validation flow
~~~mermaid
flowchart LR
  PR[Pull request changes] --> Gate[CI validation gates]
  Gate --> Docs[Docs lint + markdown protocol]
  Gate --> Schemas[Schema validation: STAC/DCAT/PROV/telemetry]
  Gate --> Graph[Graph integrity tests]
  Gate --> API[API contract tests]
  Gate --> UI[UI checks: build + a11y + layer registry]
  Gate --> Sec[Security + sovereignty scans]
  Docs --> Merge[Merge allowed]
  Schemas --> Merge
  Graph --> Merge
  API --> Merge
  UI --> Merge
  Sec --> Merge
~~~

### Optional sequence for a typical PR
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as CI system
  participant Rev as Reviewer
  Dev->>CI: Open PR
  CI->>CI: Run required gates
  CI-->>Dev: Report pass/fail + artifacts
  Rev->>CI: Review checks + diffs
  Rev-->>Dev: Approve or request changes
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Code changes | source | PR diff | lint + tests |
| Documentation changes | Markdown | PR diff | markdown protocol + link checks |
| Catalog changes | JSON/JSON-LD | PR diff | schema validation + integrity checks |
| Data changes | files | PR diff | checksums + format checks + optional domain checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Lint/test reports | logs | CI artifacts | CI-defined |
| Schema validation reports | logs/json | CI artifacts | STAC/DCAT/PROV/telemetry schemas |
| Build artifacts | optional | CI artifacts | depends on subsystem |

### Sensitivity and redaction
- CI logs and artifacts must not contain secrets, tokens, credentials, or private keys.
- When validating restricted layers, ensure logs do not reveal sensitive coordinates or names that must be generalized.

### Quality signals
- Schema validity for catalogs and telemetry
- Broken-link and reference integrity checks for docs
- Determinism checks for pipelines where possible
- Provenance completeness checks for story and evidence artifacts

## 🌐 STAC, DCAT & PROV Alignment

### STAC
CI should validate:
- STAC item and collection JSON schema conformance
- Item-to-collection linkage integrity
- Broken-link checks for asset hrefs where feasible

### DCAT
CI should validate:
- Minimum required fields for dataset descriptions
- License and publisher mapping expectations (where defined)

### PROV-O
CI should validate:
- Presence of `prov:wasDerivedFrom` and `prov:wasGeneratedBy` where required
- Activity/run identifiers are recorded for generated artifacts

### Versioning
- New versions should link predecessor/successor where applicable.
- Graph should mirror version lineage for entities and artifacts.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Docs checks | Markdown lint + protocol enforcement | `docs/` |
| Schema validation | STAC/DCAT/PROV/telemetry validation | `schemas/` + `data/` |
| Graph tests | Graph integrity + constraints | `src/graph/` |
| API checks | OpenAPI/GraphQL contract tests | `src/server/` |
| UI checks | Build, lint, a11y, layer registry checks | `web/` |
| Security checks | secret scanning + dependency scanning | repo-wide |

### Interfaces and contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Markdown protocol | `docs/standards/` | Governed changes require review |
| Templates | `docs/templates/` | Template updates are semver + changelog |
| JSON schemas | `schemas/` | Semver + contract tests required |
| API schemas | `src/server/` + docs | Backward compat or version bump |

### Extension points checklist
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] Catalog: STAC collection + item validation included
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Story/Focus: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Nodes and Focus Mode must only consume provenance-linked content.
- Every narrative claim should trace to a dataset/record/asset identifier.

### Provenance-linked narrative rule
- CI should include checks (where implemented) that prevent merging story content without citations and identifiers.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Required CI gates for v12-ready contributions
The following gate categories are required at the project level. Exact commands and workflow
definitions are implementation details.

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security and sovereignty scanning gates where applicable

### Reproduction
Replace placeholders with repo-specific commands once confirmed.

~~~bash
# Example placeholders — replace with repo-specific commands

# Docs
# make docs-lint

# Schemas (STAC/DCAT/PROV/telemetry)
# make validate-schemas

# Graph
# make graph-test

# API
# make api-contract-test

# UI
# make ui-check

# Security
# make security-scan
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| CI run id | CI provider | CI logs / artifacts |
| Validation summary | validators | `docs/telemetry/` (not confirmed in repo) |
| Schema versions | schemas | `schemas/` |

## ⚖ FAIR+CARE & Governance

### Review gates
Changes may require additional review when they affect governance, sensitive content, or public exposure.

### Governance review triggers
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### CARE and sovereignty considerations
- Document redaction and generalization rules for any restricted locations.
- Ensure compliance with sovereignty constraints in both outputs and CI logs.

### AI usage constraints
- Ensure this document’s AI permissions and prohibitions match intended use.
- Do not use AI processes to infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial CI README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
