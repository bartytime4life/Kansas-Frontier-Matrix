---
title: "UI Registry Fixture for GitHub Actions"
path: ".github/actions/fixtures/ui_registry/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:ui-registry:readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixture-ui-registry-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:ui-registry:readme:v1.0.0"
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

# UI Registry Fixture for GitHub Actions

## 📘 Overview

### Purpose
This directory holds **fixture inputs** used by GitHub Actions tests to validate the **UI registry** (also called the **layer registry**) contract.

The goal is to:
- keep UI registry validation **deterministic**,
- provide **known-good** and **known-bad** cases for regression testing,
- ensure CI fails fast when the registry format drifts from its schema.

### Scope
| In Scope | Out of Scope |
|---|---|
| Synthetic UI registry fixtures used for CI validation | Production UI registry content |
| Example failure modes (missing fields, wrong types, invalid values) | UI runtime behavior, rendering, styling correctness |
| Documentation for how to add fixtures safely | Changes to the schema itself (document those under `schemas/` + a contract doc) |

### Audience
- Primary: CI maintainers, UI maintainers, schema/contract maintainers
- Secondary: contributors adding or modifying UI layers

### Definitions
- Glossary link: `docs/glossary.md` (if present)
- UI registry / layer registry: a JSON config that declares which layers the UI can load, along with required metadata.
- Fixture: small, synthetic example files used to test validators (not production data).

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/ui_registry/README.md` | CI maintainers | How fixtures work |
| UI registry schema | `schemas/…` | Schema maintainers | Canonical validator contract (exact path varies) |
| UI layer registry config | `web/…` | UI maintainers | Example canonical registry location is `web/cesium/layers/regions.json` |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Fixtures are synthetic and do not include secrets, PII, or restricted locations
- [ ] At least one valid fixture exists
- [ ] At least one invalid fixture exists and is asserted to fail
- [ ] Validation behavior is deterministic and reproducible in CI

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/ui_registry/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/` | workflows, actions, CI policy |
| Fixtures | `.github/actions/fixtures/` | deterministic inputs for CI tests |
| UI app | `web/` | UI implementation and registries |
| Schemas | `schemas/` | JSON Schemas and other contract specs |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 ui_registry/
            ├── 📄 README.md
            ├── 📁 valid/
            │   └── 📄 *.json
            └── 📁 invalid/
                └── 📄 *.json
~~~

Notes:
- The `valid/` and `invalid/` subfolders are a recommended convention for clarity.
- If your action expects a different layout, keep the validator as the source of truth and adjust this README accordingly.

## 🧾 Data Flow / Pipeline Placement

This fixture directory supports **CI validation** of a UI-facing contract.
It does not change KFM’s canonical pipeline ordering; it protects the UI boundary by keeping registry formats schema-compliant.

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React or Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI registry fixture | JSON | `.github/actions/fixtures/ui_registry/**` | JSON Schema validator (CI step) |
| UI registry schema | JSON Schema | `schemas/**` | schema lint + tests |
| Production UI registry | JSON | `web/**` | same validator as fixtures |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation logs | text | CI logs | N/A |
| Pass/fail signal | boolean | CI job status | N/A |

### Sensitivity & redaction
- Fixtures must be **synthetic**.
- Do not include:
  - API keys, tokens, credentials
  - personal data
  - restricted or sensitive location coordinates
- Use `example.com` style placeholders for URLs and mock IDs.

### Quality signals
- Minimal fixtures: include only fields needed to exercise the validator.
- Deterministic ordering: keep JSON stable (avoid randomized IDs).
- Clear intent: filename should explain the scenario being tested.

## 🌐 STAC, DCAT & PROV Alignment

This is a UI configuration fixture, not a dataset catalog.
However, registry entries that represent data layers should be capable of linking to provenance-aware assets when the UI or Story Nodes surface them.

If the UI registry format supports it, prefer references to:
- dataset identifiers (DCAT)
- asset identifiers (STAC Items/Collections)
- lineage bundles (PROV)

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| CI fixtures | Known inputs for tests | filesystem paths under `.github/actions/fixtures/` |
| Validator | Enforces UI registry schema | action step / script (see workflow) |
| UI layer registry | Declares UI layers | JSON config under `web/` |
| Schemas | Define contract requirements | JSON Schema under `schemas/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| UI registry schema | `schemas/**` | Semver + changelog for breaking changes |
| UI registry content | `web/**` | validated in CI |
| Fixture examples | `.github/actions/fixtures/ui_registry/**` | updated alongside schema changes |

### Extension points checklist
- [ ] Schema: add/adjust schema rules and bump schema version appropriately
- [ ] Fixtures: add a new valid example for the new capability
- [ ] Fixtures: add at least one invalid example for the new rule
- [ ] UI: update registry authoring docs if fields changed
- [ ] CI: ensure validator fails when invalid and passes when valid

## 🧠 Story Node & Focus Mode Integration

This fixture set does not create narrative content.
Still, UI layers are often used by Story Nodes and Focus Mode experiences; registry entries should be compatible with provenance-linked rendering (no unsourced claims).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Validate all `valid/**/*.json` fixtures against the UI registry schema
- [ ] Validate all `invalid/**/*.json` fixtures and assert they fail with expected errors
- [ ] Validate production UI registry file(s) under `web/**` using the same validator

### Reproduction
~~~bash
# Run the same command used in CI.
# Look for the "UI registry" (or "layer registry") validation step in GitHub workflows.
# Example placeholder:
#   ./tools/validate-ui-registry --fixtures .github/actions/fixtures/ui_registry
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- CI/schema maintainers approve schema changes
- UI maintainers approve registry field changes
- Governance review may be required if new layers surface sensitive content

### CARE / sovereignty considerations
- Fixtures must not leak sensitive locations or restricted community data.
- If you need “realistic” geometry, use generalized or synthetic shapes.

### AI usage constraints
- Respect front-matter `ai_transform_prohibited` rules; do not add content that infers sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for UI registry fixtures | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
