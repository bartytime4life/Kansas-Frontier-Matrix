---
title: "GitHub Actions Fixtures"
path: ".github/actions/fixtures/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures-readme:v1.0.0"
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

# GitHub Actions Fixtures

## 📘 Overview

### Purpose
This directory contains **test fixtures** consumed by local GitHub Actions under `.github/actions/`.
Fixtures provide deterministic, reviewable inputs to validate KFM’s documentation and contract gates.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal, synthetic inputs for action tests | Production datasets or catalog outputs |
| Both passing and failing examples | Large binaries, proprietary files |
| Security-safe samples for scanning tools | Secrets, credentials, sensitive locations |

### Audience
- Primary: Contributors authoring or updating local actions and workflow gates.
- Secondary: Contributors adding docs/schemas/story nodes who need to understand CI expectations.

### Definitions
- Link: `../../../docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: A file used as input to a validator or gate.
  - **Valid fixture**: Expected to pass a validator.
  - **Invalid fixture**: Expected to fail a validator.
  - **Gate**: A CI check that blocks merge if validation fails.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Parent actions README | `../README.md` | CI maintainers | Overview of local actions |
| Master Guide | `../../../docs/MASTER_GUIDE_v12.md` | Architecture | Canonical pipeline + invariants |
| Templates | `../../../docs/templates/` | Docs governance | Governs front-matter + structure |
| Schemas | `../../../schemas/` | DataOps | JSON schemas validated in CI |
| Governance | `../../../docs/governance/` | Governance | Review triggers, ethics, sovereignty |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Fixture organization documented (this file)
- [ ] Fixtures are small, deterministic, and offline-safe
- [ ] No secrets, no PII, no restricted locations
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | Workflow entrypoints that call actions |
| Local actions | `.github/actions/` | Composite and/or JS actions |
| Fixtures | `.github/actions/fixtures/` | Inputs used by action tests |
| Documentation | `docs/` | Governed docs and templates |
| Schemas | `schemas/` | JSON schemas used by validators |
| Data | `data/` | Raw/work/processed + catalog outputs |
| Graph | `src/graph/` | Ontology bindings + graph build |
| API | `src/api/` | API layer contracts and handlers |
| Web UI | `web/` | React/Map UI and layer registry |

### Suggested fixture layout

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        ├── 📄 README.md
        ├── 📁 markdown_protocol/
        │   ├── 📁 valid/
        │   └── 📁 invalid/
        ├── 📁 catalogs/
        │   ├── 📁 stac/
        │   ├── 📁 dcat/
        │   └── 📁 prov/
        ├── 📁 graph/
        │   ├── 📁 valid/
        │   └── 📁 invalid/
        ├── 📁 api_contracts/
        │   ├── 📁 valid/
        │   └── 📁 invalid/
        ├── 📁 ui_registry/
        │   ├── 📁 valid/
        │   └── 📁 invalid/
        ├── 📁 story_nodes/
        │   ├── 📁 valid/
        │   └── 📁 invalid/
        └── 📁 security/
            ├── 📁 safe_samples/
            └── 📁 tripwires/
~~~

Notes:
- Folder names are **conventions**, not requirements. Create only what your actions/tests need.
- Keep fixtures minimal; prefer multiple tiny fixtures over one large “kitchen sink” file.

## 🧭 Context

### Why fixtures exist in KFM
KFM’s pipeline relies on “do not break” contracts across stages (catalogs, graph, APIs, UI, and narrative).
Fixtures allow CI to test validators deterministically and to prove that both success and failure cases behave as intended.

### Safety and determinism rules
- **Offline-first:** fixtures must not require network access.
- **Deterministic:** same input must yield the same result.
- **No secrets:** never store tokens/keys/passwords, even “dummy” values that resemble real formats.
- **No sensitive locations:** do not include precise locations that could be restricted under sovereignty rules.
- **Small and reviewable:** reviewers should be able to understand a fixture quickly.

## 🗺️ Diagrams

~~~text
PR / Push
  └─> .github/workflows/<workflow>.yml
        └─> .github/actions/<action>/
              └─> uses .github/actions/fixtures/<pack>/
                    ├─ valid/   (must pass)
                    └─ invalid/ (must fail)
~~~

## 📦 Data & Metadata

### Naming conventions
Use stable, intention-revealing names:
- `valid__<topic>__<case>.<ext>`
- `invalid__<topic>__<case>.<ext>`

Examples:
- `valid__frontmatter__universal_doc.md`
- `invalid__story_node__missing_citations.md`
- `valid__stac__item_minimal.json`
- `invalid__openapi__breaking_change.yaml`

### Optional fixture manifests
If a fixture pack grows, consider adding a small manifest to document expectations:

~~~yaml
# manifest.yaml (optional)
fixtures:
  - id: "valid__stac__item_minimal"
    path: "catalogs/stac/valid/valid__stac__item_minimal.json"
    expected: "pass"
    validator: "stac-schema"
    notes: "Minimal STAC item with required fields."
~~~

## 🌐 STAC, DCAT & PROV Alignment

Fixtures in `catalogs/` should represent:
- Minimal **STAC** Collection/Item samples for schema validation
- Minimal **DCAT** dataset records for catalog mapping validation
- Minimal **PROV** bundles for lineage validation

Guidelines:
- Use synthetic IDs and synthetic timestamps.
- Prefer minimal required fields first; add targeted optional fields only when testing them.

## 🧱 Architecture

### Fixture packs mapped to subsystem contracts

| Subsystem | Typical fixture pack | What it should validate | Do not break rule |
|---|---|---|---|
| Catalogs | `catalogs/` | Schema + linkage for STAC/DCAT/PROV | Machine-validated catalogs |
| Graph | `graph/` | Ontology/constraints expectations | Stable labels/edges or explicit migration |
| APIs | `api_contracts/` | OpenAPI/GraphQL contract lint/tests | Backward compatible or version bump |
| UI | `ui_registry/` | Layer registry schema checks | No hidden leakage of restricted data |
| Story | `story_nodes/` | Story Node structure + provenance | No uncited claims |
| Security | `security/` | Secret scanning and policy checks | No secrets, no unsafe patterns |

### API boundary reminder
Fixtures that model UI behavior must target **API outputs** (contracted payloads), not direct graph access.

## 🧠 Story Node & Focus Mode Integration

### How fixtures support narrative integrity
Story-node fixtures should include:
- At least one “valid” Story Node that demonstrates required provenance structure
- At least one “invalid” Story Node that demonstrates a failing case (for example missing provenance)

### Provenance-linked narrative rule
Every claim in narrative fixtures should be traceable to an internal reference (dataset/document ID) or a clearly marked hypothesis section.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation for catalog fixtures
- [ ] Graph integrity checks for graph fixtures
- [ ] API contract tests for API fixtures
- [ ] UI schema checks for UI fixtures
- [ ] Security and sovereignty checks for security fixtures

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run markdown protocol validation
# 2) validate schemas
# 3) run action/unit tests
~~~

### Telemetry signals
Not applicable by default. If fixtures are used to validate telemetry schemas, document signals and storage locations here.

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to fixtures that affect validation outcomes should be reviewed by the owners of the corresponding gate.
- Any fixture that touches sovereignty-sensitive concepts requires governance review.

### CARE and sovereignty considerations
- Fixtures must not reveal restricted locations, culturally sensitive sites, or other protected knowledge.
- Prefer generalized geometries and synthetic records.

### AI usage constraints
Ensure the front-matter permissions/prohibitions match intended use of fixtures in automated tooling.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial fixtures README | TBD |

---

Footer refs:
- Governance: `../../../docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `../../../docs/governance/ETHICS.md`
- Sovereignty: `../../../docs/governance/SOVEREIGNTY.md`
