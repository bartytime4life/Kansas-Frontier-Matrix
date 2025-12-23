---
title: "Fixtures — UI Registry (Invalid)"
path: ".github/actions/fixtures/ui_registry/invalid/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
doc_kind: "Readme"
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
care_label: "N/A (synthetic fixtures)"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:github:actions:fixtures:ui-registry:invalid-readme:v1.0.0"
semantic_document_id: "kfm-fixtures-ui-registry-invalid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:fixtures:ui-registry:invalid-readme:v1.0.0"
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

# Fixtures — UI Registry (Invalid)

## 📘 Overview

### Purpose
- Provide a single, durable explanation of the **intentionally invalid** UI registry fixtures stored in this folder.
- Define contributor expectations for adding new invalid fixtures so CI can reliably exercise negative-path validation (validator rejects malformed registry inputs).

### Scope
| In Scope | Out of Scope |
|---|---|
| Invalid UI registry fixture files used to assert “this should fail validation.” | Production UI layer registry definitions and the full UI rendering stack. |
| Naming + documentation conventions for invalid fixtures. | Defining the complete UI registry schema (tracked elsewhere; exact path not confirmed in repo). |
| Safety guidance so fixtures remain synthetic and non-sensitive. | Replacing CI workflows, action implementations, or test runners. |

### Audience
- Primary: contributors maintaining the **UI registry schema** and its **CI validation** gate(s).
- Secondary: UI contributors adding/editing layer registry entries who need to understand what “invalid” looks like in tests.

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **UI registry / layer registry**: JSON configuration describing map layers (name, source/URL, attributions, sensitivity flags, etc.).
  - **Fixture**: a static test input file checked into the repo.
  - **Invalid fixture**: a fixture expected to fail schema/contract validation deterministically.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/ui_registry/invalid/README.md` | CI / UI maintainers | Canonical rules for invalid fixtures. |
| Invalid fixture files | `.github/actions/fixtures/ui_registry/invalid/*.json` | CI / UI maintainers | Each file is expected to fail validation. |
| UI layer registry (production) | `web/…` (example: `web/cesium/layers/regions.json`) | UI maintainers | Example path appears in KFM templates; exact location not confirmed in repo. |
| UI registry schema | `schemas/…` | Schema owners | Exact schema path not confirmed in repo; keep fixtures aligned with schema. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (including correct `path`)
- [ ] Explains what counts as an “invalid” fixture and why we keep them
- [ ] Documents how to add new invalid fixtures safely (no real sensitive data)
- [ ] Provides a minimal reproduction approach (even if repo-specific command is “not confirmed in repo”)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/ui_registry/invalid/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub metadata | `.github/` | Workflows, actions, security policy, CI configuration. |
| GitHub Actions | `.github/actions/` | Action implementations used by CI (exact action names not confirmed in repo). |
| UI registry fixtures | `.github/actions/fixtures/ui_registry/` | Fixture inputs for UI registry validation (valid + invalid). |
| Schemas | `schemas/` | JSON schemas (may include UI registry schema; exact file not confirmed in repo). |
| UI app | `web/` | Frontend app code and registries/config used at runtime. |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 ui_registry/
            └── 📁 invalid/
                ├── 📄 README.md
                └── 📄 <invalid-fixture>.json
~~~

## 🧭 Context

### Background
A KFM UI layer registry is expected to be **schema-validated** and to support governance needs (e.g., sensitivity flags so restricted layers are not exposed). Invalid fixtures let CI assert that the registry validator rejects malformed or unsafe inputs early, before they can affect UI behavior.

### Assumptions
- A schema-validated UI/layer registry exists as a JSON artifact (exact schema + registry locations are not confirmed in repo).
- CI includes a gate that validates the UI registry/layer registry against a schema and/or contract.

### Constraints / invariants
- Keep the canonical KFM ordering intact: **ETL → catalogs → graph → APIs → UI → Story/Focus** (fixtures here only affect CI validation).
- Frontend consumes contracts via APIs (no direct graph dependency).
- Fixtures in this folder must be:
  - **synthetic** (no real sensitive coordinates, names, or endpoints)
  - **deterministic** (same failure every run)
  - **minimal** (prefer one failure mode per file)

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the authoritative UI registry schema file path under `schemas/`? | TBD | TBD |
| Which workflow/action consumes these fixtures, and what is its local entrypoint? | TBD | TBD |

### Future extensions
- Add one invalid fixture per newly introduced required field / enum value in the UI registry schema.
- If snapshot testing exists for error messages (not confirmed in repo), add fixtures that stabilize and document expected error output formats.

## 🗺️ Diagrams

### Fixture validation dataflow
~~~mermaid
flowchart LR
  A["Invalid UI registry fixture (JSON)"] --> B["UI registry validator (CI job/action)"]
  B -->|expected| C["Fail validation + emit actionable error"]
  B -->|unexpected| D["Bug: validator accepted invalid input"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant CI as CI Test Runner
  participant V as UI Registry Validator
  CI->>V: validate(fixture.json)
  V-->>CI: exit!=0 + structured error output
  CI-->>CI: assert failure is expected
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Invalid UI registry fixture | JSON | `.github/actions/fixtures/ui_registry/invalid/` | Must fail schema/contract validation. |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation error report | stdout/stderr logs (or JSON) | CI logs (and/or test snapshots) | Format not confirmed in repo. |

### Sensitivity & redaction
- Use **synthetic** values only:
  - Fake URLs/domains, fake coordinates, fake IDs.
  - No culturally sensitive locations, no private land parcel IDs, no personal names/addresses.
- If the schema contains a “sensitive” flag, do **not** include real restricted layer metadata; test only the shape/type/enum behavior.

### Quality signals
- Each invalid fixture should violate **one** rule where possible (easier to debug and maintain).
- Recommended filename pattern (examples only): `missing_required_field.json`, `wrong_type_attribution.json`, `invalid_enum_sensitivity.json`.
- Prefer fixtures that keep failing deterministically even if unrelated schema fields change.

## 🌐 STAC, DCAT & PROV Alignment
Not applicable: fixtures in this directory are CI test inputs, not datasets/products that enter STAC/DCAT/PROV catalogs.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| CI validator (UI registry) | Reject invalid registry inputs | GitHub Action / test runner (not confirmed in repo). |
| UI registry schema | Define allowed registry structure | JSON Schema under `schemas/` (path not confirmed in repo). |
| UI app registry consumer | Load registries for layer toggles and governance behaviors | Runtime config under `web/` (exact path not confirmed in repo). |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| UI registry JSON schema | `schemas/…` | Semver + changelog (recommended). |
| UI registry validator action/job | `.github/…` | Must stay aligned with schema; update fixtures when changing schema behavior. |
| Layer registry (production) | `web/…` (example: `web/cesium/layers/regions.json`) | Schema-validated. |

### Extension points checklist (for future work)
- [ ] UI: add invalid fixtures for each new required field / enum / cross-field constraint
- [ ] CI: ensure validator emits actionable errors for each invalid fixture category
- [ ] Governance: add fixtures for “restricted layer should be rejected / hidden” behaviors (without using real restricted data)

## 🧠 Story Node & Focus Mode Integration
Not directly applicable. Indirectly, stricter registry validation helps prevent invalid layers from surfacing in map UI states used during Story Nodes / Focus Mode exploration.

### Optional structured controls
~~~yaml
ci_fixture_set: "ui_registry/invalid"
expected_validation_result: "fail"
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (for this README, if enforced repo-wide)
- [ ] UI registry validator runs against each fixture in this folder and **fails**
- [ ] Fixtures contain no real sensitive/PII content (synthetic-only policy)

### Reproduction
~~~bash
# Not confirmed in repo: run the same UI registry validation entrypoint used by CI.
# The intent is:
#   - pick a fixture under this folder
#   - run the validator against it
#   - observe a non-zero exit code + a readable, schema-driven error
#
# Example (placeholder):
#   <ui-registry-validator> validate .github/actions/fixtures/ui_registry/invalid/<invalid-fixture>.json
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that add new fixture categories (new failure modes) should be reviewed by whoever owns the UI registry schema/validator.
- If a fixture might resemble real restricted data, treat it as **requires human review** and replace with synthetic values.

### CARE / sovereignty considerations
- Even in tests, do not encode or approximate restricted locations. If a fixture needs coordinates, use generic/randomized coordinates with no real-world mapping.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Add README documenting invalid UI registry fixtures | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
