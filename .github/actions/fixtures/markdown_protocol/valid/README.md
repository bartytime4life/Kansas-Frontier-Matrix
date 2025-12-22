---
title: "Fixture — Markdown Protocol (Valid)"
path: ".github/actions/fixtures/markdown_protocol/valid/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
doc_kind: "Fixture"
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
care_label: "N/A"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:fixtures:markdown-protocol:valid-readme:v1.0.0"
semantic_document_id: "kfm-fixture-markdown-protocol-valid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:fixtures:markdown-protocol:valid-readme:v1.0.0"
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

# Fixture — Markdown Protocol (Valid)

## 📘 Overview

### Purpose
- Provide a **known-good** Markdown file that should satisfy KFM Markdown protocol validation checks.
- Serve as the “valid” fixture input for CI tests under `.github/actions/fixtures/markdown_protocol/`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Front-matter completeness, standard section structure, and `~~~` fenced blocks. | Any real ETL, catalog, graph, API, UI, or narrative changes. |

### Audience
- Primary: CI maintainers and GitHub Action authors.
- Secondary: Contributors learning the governed Markdown structure.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (if present)
- Terms used in this doc:
  - **Fixture**: A deterministic test input file used for CI validation.
  - **KFM-MDP**: Kansas Frontier Matrix Markdown Protocol (versioned).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This fixture | `.github/actions/fixtures/markdown_protocol/valid/README.md` | CI | Must remain “valid”. |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs governance | Source structure for governed docs. |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + invariants. |

### Definition of done (for this document)
- [x] YAML front-matter present and complete
- [x] `path` matches this file’s repository location
- [x] Uses `~~~` for fenced blocks (avoids nested backtick issues)
- [x] No placeholder-only tokens (e.g., `TBD`) in required fields
- [x] No external URLs (fixture remains deterministic)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/markdown_protocol/valid/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Action fixtures | `.github/actions/fixtures/markdown_protocol/` | Test inputs for Markdown protocol validation |
| Documentation templates | `docs/templates/` | Governed Markdown templates |
| Governance | `docs/governance/` | Ethics, sovereignty, and review gates |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 markdown_protocol/
            ├── 📄 README.md
            ├── 📁 valid/
            │   └── 📄 README.md
            └── 📁 invalid/
                └── 📄 README.md
~~~

## 🧭 Context

### Background
This repository uses governed Markdown conventions so docs remain:
- machine-checkable (versioned front-matter),
- consistent across teams (standard headings),
- compatible with downstream automation (parsers, validators, site generation).

### Assumptions
- The Markdown protocol validator checks front-matter shape and basic structural expectations.
- Fixtures should be small, deterministic, and not depend on external content.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Fixtures must remain self-contained and stable over time.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| None for this fixture | N/A | N/A |

### Future extensions
- Add additional fixtures that cover edge cases (tables, lists, mermaid, YAML snippets, long lines).
- Add an “invalid” sibling file that intentionally breaks one rule per test case.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant CI
  participant Fixture
  CI->>Fixture: Load Markdown
  CI->>CI: Validate front-matter + structure
  CI-->>CI: Pass (valid fixture)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| None | N/A | N/A | N/A |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Valid fixture README | Markdown | `.github/actions/fixtures/markdown_protocol/valid/README.md` | `KFM-MDP v11.2.6` |

### Sensitivity & redaction
- No sensitive fields; no redaction required.

### Quality signals
- Must remain parseable by standard Markdown tooling.
- Must pass the repository’s Markdown protocol checks.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: None (fixture)
- Items involved: None (fixture)
- Extension(s): None

### DCAT
- Dataset identifiers: None (fixture)
- License mapping: Not applicable
- Contact / publisher mapping: Not applicable

### PROV-O
- `prov:wasDerivedFrom`: Not applicable
- `prov:wasGeneratedBy`: Not applicable
- Activity / Agent identities: Not applicable (fixture)

### Versioning
- Use SemVer for this fixture file; bump when structure materially changes.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI (GitHub Actions) | Run validators on changed files | Workflow + action |
| Fixtures | Provide deterministic test inputs | Markdown files |
| Templates | Define governed doc shapes | `docs/templates/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Markdown protocol | `docs/templates/` + validator | Protocol bumps require fixture updates |
| Fixture layout | `.github/actions/fixtures/markdown_protocol/` | Additive fixtures are safe; edits must preserve intent |

### Extension points checklist (for future work)
- [ ] Data: N/A (fixture)
- [ ] STAC: N/A (fixture)
- [ ] PROV: N/A (fixture)
- [ ] Graph: N/A (fixture)
- [ ] APIs: N/A (fixture)
- [ ] UI: N/A (fixture)
- [ ] Focus Mode: N/A (fixture)
- [ ] Telemetry: N/A (fixture)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Not applicable (fixture).

### Provenance-linked narrative rule
- Not applicable (fixture).

### Optional structured controls
~~~yaml
focus_layers:
  - "example-layer"
focus_time: "1861-01-01/1865-12-31"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [x] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) — N/A (fixture)
- [ ] Graph integrity checks — N/A (fixture)
- [ ] API contract tests — N/A (fixture)
- [ ] UI schema checks — N/A (fixture)
- [ ] Security and sovereignty checks — N/A (fixture)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| None | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates
- Fixture changes should be reviewed by the CI maintainer(s) responsible for protocol validation.

### CARE / sovereignty considerations
- No communities or cultural heritage data are represented in this fixture.

### AI usage constraints
- Honor `ai_transform_permissions` and `ai_transform_prohibited` from the front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Add valid Markdown protocol fixture | KFM CI |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

