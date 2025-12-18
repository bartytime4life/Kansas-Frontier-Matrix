---
title: "KFM Tests — Unit Fixtures"
path: "tests/unit/fixtures/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:tests:unit:fixtures:readme:v1.0.0"
semantic_document_id: "kfm-tests-unit-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:unit:fixtures:readme:v1.0.0"
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

# KFM Tests — Unit Fixtures

## 📘 Overview

### Purpose
- This folder holds **file-based fixtures** used by unit tests (e.g., JSON, GeoJSON, CSV, TXT) to keep tests deterministic, readable, and reproducible.
- It governs **how fixtures are added, named, and reviewed** so test inputs remain stable over time.

### Scope
| In Scope | Out of Scope |
|---|---|
| Small, deterministic fixture files for unit tests | Large datasets, production exports, or integration-test corpora |
| Minimal examples for schema/contract edge cases | Secrets, credentials, PII, or precise sensitive locations |
| Synthetic or redacted samples safe for repo inclusion | Any restricted cultural/site data without governance review |

### Audience
- Primary: Contributors writing/maintaining unit tests
- Secondary: Reviewers verifying determinism, safety, and governance alignment

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: a stable, version-controlled test input file.
  - **Golden**: a fixture used as an expected-output snapshot (only if the project adopts golden testing).
  - **Redaction/generalization**: removing or coarsening sensitive fields (e.g., coordinates).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Unit test docs | `tests/unit/README.md` | Repo maintainers | How to run unit tests |
| Fixtures directory | `tests/unit/fixtures/` | Test authors | Add new fixture files here |
| Schemas (if validating fixtures) | `schemas/` | Schema owners | Used for JSON/schema checks |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Fixture conventions documented and unambiguous
- [ ] Validation steps are repeatable (no local-only assumptions)
- [ ] Governance + CARE/sovereignty considerations stated for fixtures

## 🗂️ Directory Layout

### This document
- `path`: `tests/unit/fixtures/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| All tests | `tests/` | Test suites and test utilities |
| Unit tests | `tests/unit/` | Fast, isolated tests |
| Unit fixtures | `tests/unit/fixtures/` | This folder: file-based inputs for unit tests |
| Schemas | `schemas/` | JSON schemas / validators used in CI |

### Expected file tree for this sub-area
~~~text
🧪 tests/
└── 🧪 unit/
    └── 🧰 fixtures/
        ├── 📄 README.md
        ├── 📁 json/         # optional: generic JSON fixtures
        ├── 🗺️ geojson/      # optional: GeoJSON geometries/features
        ├── 🧾 csv/          # optional: small tabular fixtures
        └── 🧪 stac/         # optional: STAC Items/Collections fixtures
~~~

> Note: The subfolders above are **conventions**, not requirements—create only what your tests need.

## 🧭 Context

### Background
Unit tests should be:
- **Deterministic** (same inputs → same outputs)
- **Small + focused** (unit-level behavior, not end-to-end pipelines)
- **Safe to share** (no secrets; no sensitive location leakage)

Fixtures make unit tests easier to review and keep stable across refactors.

### Assumptions
- Unit tests can load local files from this directory.
- Fixtures represent **minimal** shapes of data the system handles (e.g., STAC/DCAT/PROV artifacts, API payloads, graph exports), but are not full production datasets.

### Constraints / invariants
- Conceptual pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Prefer testing public contracts (schemas/APIs) over internal coupling—unless the unit under test is explicitly internal.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize “golden” output fixtures (snapshots) and update workflows? | TBD | TBD |

### Future extensions
- Add a lightweight fixture index here once fixture volume grows.
- Add schema-validation helpers so fixtures are validated automatically in CI.

## 🗺️ Diagrams

### Fixture usage (unit-test level)
~~~mermaid
flowchart LR
  T[Test code] -->|loads| F[Fixture file]
  F -->|parsed into| D[Domain object / DTO]
  D -->|exercise unit under test| U[Function / module]
  U -->|returns| R[Result]
  R -->|assert| A[Assertions]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Unit fixture files | JSON / GeoJSON / CSV / TXT | `tests/unit/fixtures/` | Prefer schema validation when schemas exist |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Test expectations | Assertions (code) or small expected files | `tests/unit/` or `tests/unit/fixtures/` | Test-specific |

### Sensitivity & redaction
- Fixtures must not contain:
  - credentials, API keys, access tokens
  - personal data (PII) or restricted cultural data
  - precise sensitive locations (use generalized coordinates or synthetic geometries)

### Quality signals
- Prefer fixtures that are:
  - minimal but realistic
  - schema-valid when schemas are available
  - stable (avoid timestamps / random IDs unless fixed)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Use STAC fixtures when unit-testing catalog parsing/validation.
- Keep fixtures minimal: **1 Collection + 1 Item** is often enough to cover logic paths.

### DCAT
- If a test needs DCAT views/mappings, fixtures should include only the fields required by the mapping logic being tested (e.g., title/description/license/keywords).

### PROV-O
- Use PROV-like fixtures when testing lineage extraction or provenance-linking behavior.
- Keep agent/activity/entity identifiers stable.

### Versioning
- If a fixture represents a “versioned” artifact, use explicit predecessor/successor references inside the fixture to model expected behavior.

### Extension points checklist (for future work)
- [ ] Data: add a domain-relevant fixture set under a clear subfolder (e.g., `stac/`, `geojson/`)
- [ ] STAC: add minimal Collection + Item fixtures for new edge cases
- [ ] PROV: add stable activity + agent identifiers if lineage logic is under test
- [ ] Graph: add minimal subgraph payload fixtures if graph serialization is under test
- [ ] APIs: add request/response fixtures if contract serialization is under test
- [ ] UI: add minimal layer-registry fixtures if UI config parsing is under test
- [ ] Focus Mode: add provenance-linked context bundle fixtures (if applicable)
- [ ] Telemetry: add minimal telemetry payload fixtures (if applicable)

## ✅ Fixture conventions

### Naming (recommended)
- Use descriptive names that encode intent:
  - `stac__item__minimal_valid.json`
  - `stac__item__missing_datetime.json`
  - `geojson__polygon__invalid_self_intersection.geojson`
- Prefer `__` as a visual separator for category vs scenario.

### Content rules
- Keep fixtures small (reviewable in PRs).
- Prefer synthetic values:
  - placeholder IDs (e.g., `item-0001`)
  - generalized dates (e.g., `1900-01-01T00:00:00Z`) if exact time is not under test
- Avoid brittle ordering dependencies:
  - if JSON order is irrelevant, tests should not assert on serialized key order.

### When to add a fixture vs inline data
- Add a fixture when:
  - data is large enough to harm readability if embedded in the test
  - multiple tests share the same input
  - you want a durable repro case for a bug/regression
- Inline data is fine when:
  - it’s < ~15 lines and test-specific

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Typically indirect: fixtures here may be used to unit-test code that **builds** Story Nodes or Focus Mode context bundles (e.g., verifying provenance pointers are preserved in outputs).

### Provenance-linked narrative rule
- If a fixture models narrative/context output, ensure it includes (or allows tests to assert) **provenance identifiers** rather than free-text claims.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (if enabled for READMEs)
- [ ] JSON/schema validation for fixtures that model STAC/DCAT/PROV (where validators exist)
- [ ] Unit tests pass (see `tests/unit/README.md`)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# Run unit tests:
#   make test
# or:
#   <your-test-runner> tests/unit
#
# Validate fixture schemas (if tooling exists):
#   <schema-validator> tests/unit/fixtures/stac/*.json
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Fixtures that include any real-world derived content (even partial) should be reviewed for:
  - licensing compatibility
  - sensitivity / sovereignty constraints
  - coordinate redaction/generalization rules

### CARE / sovereignty considerations
- If a fixture is based on culturally sensitive material or restricted site data:
  - do not include it here without explicit governance review
  - prefer synthetic stand-ins that preserve structure but not sensitive content

### AI usage constraints
- This README prohibits “infer_sensitive_locations”; do not add fixtures that would enable location inference beyond what’s necessary for testing.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial fixtures README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`