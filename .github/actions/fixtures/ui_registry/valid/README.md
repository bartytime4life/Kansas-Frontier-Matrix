---
title: "UI Registry Fixtures — Valid Set"
path: ".github/actions/fixtures/ui_registry/valid/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:ui-registry:valid-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-ui-registry-valid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:ui-registry:valid-readme:v1.0.0"
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

# UI Registry Fixtures — Valid Set

## 📘 Overview

### Purpose
- Provide **schema-valid** UI registry examples used by GitHub Actions fixtures to confirm the UI registry validator **accepts known-good inputs**.
- Keep these fixtures **small, deterministic, and representative** so CI failures are actionable.

### Scope

| In Scope | Out of Scope |
|---|---|
| Valid UI registry fixture files used by CI | Defining the UI registry schema itself (lives under `schemas/` if present) :contentReference[oaicite:2]{index=2} |
| Conventions for naming + organizing valid fixtures | Front-end implementation details (actual layer rendering lives under `web/`) :contentReference[oaicite:3]{index=3} |
| How to add a new “valid” test case | Workflow wiring or runner configuration (handled by `.github/workflows/*`) *(not confirmed in repo)* |

### Audience
- Primary: CI maintainers and schema/contract owners.
- Secondary: UI developers adding new layer/registry capabilities.

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **UI registry**: a contract artifact describing UI layers/configuration consumed by the UI stage. :contentReference[oaicite:4]{index=4}
  - **Fixture**: a minimal example file used in automated validation tests.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| UI registry schemas | `schemas/ui/` | Schema owners | Minimum contract set includes UI registry schemas. :contentReference[oaicite:5]{index=5} |
| UI layer registry runtime | `web/**/layers/**` | UI team | Consumer location for layer registry artifacts. :contentReference[oaicite:6]{index=6} |
| Canonical pipeline | (see Master Guide) | KFM Core Team | The non-negotiable ordering includes UI downstream of APIs. :contentReference[oaicite:7]{index=7} |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Every fixture here validates against the UI registry schema(s) (when present) :contentReference[oaicite:8]{index=8}
- [ ] Each fixture has an intent note (filename and/or adjacent comment file) explaining what it covers
- [ ] No fixture includes secrets, personal data, or sensitive locations

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/ui_registry/valid/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions fixtures | `.github/actions/fixtures/` | Test inputs for local composite actions / CI steps |
| UI registry fixtures | `.github/actions/fixtures/ui_registry/` | Valid + invalid examples for the registry validator |
| Schemas (contracts) | `schemas/` | JSON schemas + contract validators :contentReference[oaicite:9]{index=9} |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 ui_registry/
            ├── 📄 README.md                      # overview (optional)
            ├── 📁 valid/
            │   ├── 📄 README.md                  # this document
            │   └── 📄 <fixture files...>         # schema-valid inputs
            └── 📁 invalid/
                ├── 📄 README.md                  # invalid fixtures guidance (optional)
                └── 📄 <fixture files...>         # schema-invalid inputs
~~~

## 🧭 Context

### Background
KFM is contract-first and validates artifacts against schemas as part of quality gates. :contentReference[oaicite:10]{index=10}  
These fixtures exist to ensure the UI registry validator continues to accept known-good registry documents as the schema and UI evolve.

### Assumptions
- A UI registry schema exists under `schemas/ui/` (or equivalent) and is referenced by CI. :contentReference[oaicite:11]{index=11} *(exact wiring not confirmed in repo)*
- The CI job / action runs a “validate UI registry” step on files in this fixtures directory. *(not confirmed in repo)*

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved. :contentReference[oaicite:12]{index=12}
- Frontend consumes contracts via APIs (no direct graph dependency). :contentReference[oaicite:13]{index=13}

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the authoritative UI registry schema file (exact path + versioning rule)? | TBD | TBD |
| Which workflow/action consumes this directory (exact filename and invocation)? | TBD | TBD |
| What file formats are accepted for the registry (JSON only vs YAML, etc.)? | TBD | TBD |

### Future extensions
- Add a fixture per major registry feature (new layer types, new optional fields, new constraints).
- Add a “minimal valid” fixture and a “maximal valid” fixture to catch boundary regressions.

## 🗺️ Diagrams

### Fixture validation flow (CI)
~~~mermaid
flowchart LR
  A[Valid fixture files<br/>.github/actions/fixtures/ui_registry/valid] --> B[CI / GitHub Action<br/>UI registry validator]
  B --> C[Schema(s)<br/>schemas/ui/*]
  C --> D{Valid?}
  D -->|Yes| E[CI passes]
  D -->|No| F[CI fails + reports errors]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| UI registry fixture | JSON / YAML *(not confirmed in repo)* | This directory | Must validate against UI registry schema(s) when present :contentReference[oaicite:14]{index=14} |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation result | CI status + logs | GitHub Actions run | Schema validation + lint rules *(workflow not confirmed in repo)* |

### Sensitivity & redaction
- Fixtures must not contain secrets, API keys, personal data, or precise sensitive locations.
- If a layer example requires geometry, prefer **synthetic** or **generalized** geometry.

### Quality signals
- All fixtures are schema-valid and stable (no nondeterministic ordering/content). :contentReference[oaicite:15]{index=15}
- Each new fixture includes a clear “why this exists” note (via filename convention or adjacent note file).

## 🌐 STAC, DCAT & PROV Alignment
Not applicable for these CI fixtures (they are UI-contract tests, not catalog artifacts). The broader system still requires catalog alignment and schema validation for STAC/DCAT/PROV in their respective canonical locations. :contentReference[oaicite:16]{index=16}

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Valid fixtures (this dir) | Provide known-good examples | File system inputs to CI |
| UI registry validator (action) | Validate fixtures against schema | CI step / action runner *(not confirmed in repo)* |
| UI registry schema(s) | Define allowed structure and constraints | `schemas/ui/*` :contentReference[oaicite:17]{index=17} |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI registry schema | `schemas/ui/` :contentReference[oaicite:18]{index=18} | Semver + changelog *(not confirmed in repo)* |

## 🧪 Validation & maintenance

### Adding a new valid fixture
1. Create a new fixture file in this directory.
2. Ensure it validates against the current schema(s) in `schemas/ui/` (if present). :contentReference[oaicite:19]{index=19}
3. Keep it minimal: include only fields required to cover the intended case.
4. Avoid sensitive content; use synthetic IDs and generalized coordinates if geometry is required.

### CI expectations
- The CI gate should fail deterministically if a “valid” fixture becomes invalid after schema changes. :contentReference[oaicite:20]{index=20} *(exact CI wiring not confirmed in repo)*

