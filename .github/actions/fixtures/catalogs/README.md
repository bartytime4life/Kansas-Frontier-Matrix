---
title: "KFM GitHub Actions Fixture Catalogs"
path: ".github/actions/fixtures/catalogs/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:catalogs-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-catalogs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:catalogs-readme:v1.0.0"
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

# KFM GitHub Actions Fixture Catalogs

## 📘 Overview

### Purpose

This directory is reserved for **small, deterministic fixture catalogs** used by GitHub Actions to validate KFM’s catalog contracts (STAC, DCAT, PROV) and the behavior of validators (pass/fail) in a reproducible way.

These fixtures are intended to:
- keep CI tests fast and stable,
- provide clear “known-good” and “known-bad” examples,
- avoid depending on large production catalogs for unit-level validation.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal STAC Collection/Item fixtures | Production catalog outputs under `data/**` |
| Minimal DCAT dataset-record fixtures | Large binaries / real asset payloads |
| Minimal PROV bundles (Entity/Activity/Agent) | Real sensitive locations, culturally restricted info |
| Negative fixtures to assert deterministic failures | Graph/API/UI fixtures (tracked elsewhere) |

### Audience

- Primary: CI maintainers, schema/contract maintainers, catalog stage maintainers.
- Secondary: contributors adding/adjusting STAC/DCAT/PROV artifacts or validation rules.

### Definitions

- Glossary: `docs/glossary.md`
- Fixture catalog: a small, self-contained catalog example designed to be validated in CI.
- Positive fixture: a fixture expected to validate successfully.
- Negative fixture: a fixture expected to fail validation in a specific, deterministic way.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM core | Canonical pipeline ordering + invariants |
| STAC outputs | `data/stac/**` | Catalog stage | Production catalog outputs (not fixtures) |
| DCAT outputs | `data/catalog/dcat/**` | Catalog stage | Production catalog outputs (not fixtures) |
| PROV outputs | `data/prov/**` | Catalog + pipelines | Production lineage bundles (not fixtures) |
| Schema contracts | `schemas/**` | Contract maintainers | Fixture validation should target these schemas |
| CI workflows | `.github/workflows/**` | CI maintainers | Specific workflow names are not confirmed here |

### Definition of done

- [ ] Front-matter complete and `path` matches the actual file path
- [ ] Conventions documented for valid and invalid fixtures
- [ ] Fixtures are minimal, deterministic, and free of sensitive content
- [ ] Reproduction notes exist so failures can be debugged locally

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/catalogs/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Canonical outputs of the catalog stage |
| Schema contracts | `schemas/stac/**`, `schemas/dcat/**`, `schemas/prov/**` | Validation targets for fixtures |
| Pipelines | `src/pipelines/**` | ETL + catalog build tooling (not confirmed in this directory) |
| GitHub Actions | `.github/**` | CI workflows/actions, including fixtures |

### Expected fixture tree

This is a recommended structure for fixtures in this folder. Adjust it to match actual files as they land.

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 catalogs/
            ├── 📄 README.md
            ├── 📁 stac/
            │   ├── 📁 valid/
            │   └── 📁 invalid/
            ├── 📁 dcat/
            │   ├── 📁 valid/
            │   └── 📁 invalid/
            ├── 📁 prov/
            │   ├── 📁 valid/
            │   └── 📁 invalid/
            └── 📄 manifest.yaml
~~~

## 🧭 Context

### Why these fixtures exist

KFM relies on machine-validated catalog artifacts. Fixtures allow CI to validate schemas and validator behavior without relying on large production catalogs or external networks.

This supports the canonical ordering where catalog artifacts are produced and validated before downstream stages consume them:
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Conventions for fixtures

- **Keep fixtures minimal**: only include the fields required to test the rule in question.
- **Prefer relative, non-network `href`s**: fixtures should not require external downloads during CI.
- **Negative fixtures should fail for one primary reason**:
  - If possible, isolate a single missing/invalid field per negative fixture to make errors diagnosable.
- **Stable identifiers**:
  - Use stable IDs so validator error output remains diffable.

### Manifest convention

If `manifest.yaml` exists, it should be used to list fixture files and expected outcomes, for example:
- category: `stac|dcat|prov`
- case: `valid|invalid`
- expected: `pass|fail`
- expected_reason: short label (e.g., `missing_required_field`)

If no manifest exists, CI should explicitly enumerate fixture files in the workflow logic.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Fixture catalogs<br/>.github/actions/fixtures/catalogs/**"] --> B["CI validator job"]
  B -->|pass| C["Green build"]
  B -->|fail| D["Deterministic failure<br/>action logs + diffable output"]
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC fixtures | JSON | `./stac/**` | STAC schema + KFM profile constraints |
| DCAT fixtures | JSON / JSON-LD | `./dcat/**` | DCAT constraints + KFM profile constraints |
| PROV fixtures | JSON / JSON-LD | `./prov/**` | PROV constraints + KFM profile constraints |
| Optional manifest | YAML | `./manifest.yaml` | YAML lint + schema if defined |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI validation result | logs | GitHub Actions run logs | Deterministic pass/fail behavior |

### Sensitivity and redaction

Fixtures in CI must not contain:
- precise restricted locations,
- culturally sensitive knowledge requiring special handling,
- PII or private correspondence.

Use synthetic or redacted examples only.

### Quality signals

- Fixtures validate against the same schemas used for production artifacts.
- Fixtures remain stable and diffable (IDs, formatting, ordering).
- Negative fixtures fail deterministically.

## 🌐 STAC, DCAT and PROV Alignment

### STAC

- Provide at least one minimal **Collection** and **Item** positive fixture.
- Negative fixtures should cover common failure modes:
  - missing required fields,
  - invalid geometry/time,
  - invalid asset structure.

### DCAT

- Provide at least one minimal dataset record fixture with:
  - title/description/license/keywords at minimum.
- Negative fixtures should cover:
  - missing license,
  - invalid identifiers/required fields.

### PROV-O

- Provide at least one minimal bundle covering:
  - Entity, Activity, Agent
  - `wasGeneratedBy`, `wasAssociatedWith`, or similar linkage.
- Negative fixtures should cover:
  - missing linkage or invalid IDs.

### Versioning

When contracts change:
- bump fixture versions if required,
- keep fixtures aligned with schema evolution,
- document breaking changes in CI expectations.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Catalog fixtures | deterministic examples | filesystem paths in `.github/actions/fixtures/catalogs/**` |
| CI validators | schema + rule enforcement | GitHub Actions workflow steps |
| Schema contracts | define allowed structure | `schemas/**` (JSON Schema / shape bundles) |

### Interfaces and contracts

- Fixtures should target schemas under `schemas/` as the contract source of truth.
- CI should fail deterministically when fixtures are invalid and pass for valid fixtures.

### Extension points checklist

- [ ] Add fixtures for new schema fields or new validation rules
- [ ] Add negative cases for newly enforced constraints
- [ ] Update manifest/workflow enumeration to include new cases
- [ ] Ensure any new fixture remains synthetic and governance-safe

## 🧠 Story Node and Focus Mode Integration

This fixture directory is **not** a Story Node surface.

Indirectly, these fixtures support Story Node and Focus Mode integrity by enforcing:
- provenance-first catalog outputs,
- deterministic validation gates before downstream narrative layers consume artifacts.

## 🧪 Validation and CI

### Validation steps

- [ ] Markdown protocol checks for this README
- [ ] Schema validation for fixture catalogs (STAC/DCAT/PROV)
- [ ] Workflow determinism checks (valid passes, invalid fails)
- [ ] Security and sovereignty checks (ensure fixtures contain no sensitive content)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands or workflow references.

# 1) Validate fixture catalogs against schemas (preferred: same command CI runs)
# make validate-fixture-catalogs

# 2) Run schema validation directly (if a script exists)
# python -m tools.validate_catalogs --fixtures .github/actions/fixtures/catalogs

# 3) Run markdown lint (if enabled)
# make lint-docs
~~~

### Telemetry signals

Not applicable unless CI records fixture-validation metrics in `docs/telemetry/` (not confirmed here).

## ⚖ FAIR+CARE and Governance

### Governance review triggers

- Adding fixtures derived from external datasets
- Adding fixtures that include sensitive geographies or community knowledge
- Any changes that alter public-facing validation rules for catalogs

### CARE and sovereignty considerations

- Keep fixtures synthetic/redacted.
- Do not encode restricted location detail in “example geometry.”

### AI usage constraints

This directory should not introduce AI-generated narrative. If AI is used to generate synthetic examples, ensure:
- examples are reviewed,
- no sensitive inference is introduced.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README scaffold for catalog fixtures | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
