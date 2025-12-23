---
title: "Fixtures — PROV Catalogs (Invalid)"
path: ".github/actions/fixtures/catalogs/prov/invalid/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "FixtureReadme"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:catalogs:prov:invalid:readme:v1.0.0"
semantic_document_id: "kfm-fixtures-catalogs-prov-invalid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:catalogs:prov:invalid:readme:v1.0.0"
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

# Fixtures — PROV Catalogs (Invalid)

## 📘 Overview

### Purpose
- This directory contains **intentionally invalid** PROV bundles used as fixtures for CI validation.
- CI/tests should assert these fixtures **fail** the repository’s PROV schema/shape validation (negative test coverage).

### Scope

| In Scope | Out of Scope |
|---|---|
| Synthetic/fixture PROV bundles that are expected to fail validation | Production provenance outputs under `data/prov/` |
| Negative test cases for PROV parsing/schema/shape validation | Story Nodes, UI layers, API contracts |
| Deterministic, minimal failure cases | Real-world sensitive provenance or contributor-identifying data |

### Audience
- Primary: CI/validation maintainers; contributors updating schema/shape validators.
- Secondary: Contributors adding new fixture cases or debugging catalog validation failures.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: PROV-O, fixture, validator, negative test.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Invalid PROV fixtures (this folder) | `.github/actions/fixtures/catalogs/prov/invalid/` | TBD | Each fixture should be intentionally invalid and deterministic |
| Valid PROV fixtures (sibling) | `.github/actions/fixtures/catalogs/prov/valid/` | TBD | Positive coverage: these should validate successfully |
| PROV constraints / profile schemas | `schemas/prov/` | TBD | Canonical location for PROV constraints |
| Canonical pipeline PROV output | `data/prov/` | TBD | Where real pipeline outputs are expected to land |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Scope clearly distinguishes fixtures vs production outputs
- [ ] Negative-test intent is explicit (fixtures must fail validation)
- [ ] Sensitivity expectations stated (synthetic + non-sensitive)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/catalogs/prov/invalid/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Action fixtures | `.github/actions/fixtures/` | Test inputs for CI workflows/actions |
| Catalog fixtures | `.github/actions/fixtures/catalogs/` | STAC/DCAT/PROV fixture bundles for validators |
| PROV fixtures (valid) | `.github/actions/fixtures/catalogs/prov/valid/` | Fixtures expected to pass |
| PROV fixtures (invalid) | `.github/actions/fixtures/catalogs/prov/invalid/` | Fixtures expected to fail |
| PROV outputs (production) | `data/prov/` | Pipeline + catalog provenance bundles |
| PROV schemas/constraints | `schemas/prov/` | PROV constraints/profiles used by validators |

### File tree (fixture area)

~~~text
📁 .github
└── 📁 actions
    └── 📁 fixtures
        └── 📁 catalogs
            └── 📁 prov
                ├── 📁 valid
                │   └── 📄 README.md
                └── 📁 invalid
                    └── 📄 README.md
~~~

## 🧭 Context

### Why this fixture set exists
- Validators need **negative** coverage to ensure that invalid provenance is rejected consistently.
- Fixtures here protect against regressions where a broken PROV bundle might accidentally pass validation.

### Security + sensitivity
- Fixtures must be **synthetic** and **non-sensitive**:
  - No real names/emails/phone numbers.
  - No restricted site coordinates or culturally sensitive locations.
  - No credentials, tokens, or internal URLs.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[CI job / action] --> B[PROV validator]
  B --> C{Fixtures in invalid/}
  C -->|MUST FAIL| D[Non-zero / rejected]
  B --> E{Fixtures in valid/}
  E -->|MUST PASS| F[Zero / accepted]
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)
- These are **CI fixtures**, not pipeline outputs.
- Production provenance bundles are expected under `data/prov/` (not here).

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Invalid PROV fixture files | JSON / JSON-LD / RDF (as used by repo) | Added by contributors | Must fail schema/shape validation deterministically |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Expected validation failure | CI pass/fail signal | CI logs/artifacts | Validator behavior must be deterministic |

### Sensitivity & redaction
- If a fixture includes any realistic identifiers, replace them with obvious synthetic placeholders.
- Prefer minimal payloads that demonstrate the failure without carrying extra data.

### Quality signals
- Each fixture should fail for a clear reason (ideally one primary violation per file).
- Failures should be stable across platforms and validator versions.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable (this directory is PROV-only fixtures).

### DCAT
- Not applicable (this directory is PROV-only fixtures).

### PROV-O
- These fixtures intentionally violate the repository’s PROV constraints/profile (e.g., missing required identifiers, invalid types, broken references, invalid namespaces, or schema/shape failures).
- Fixtures may test:
  - Parse-level failures (invalid syntax) **and/or**
  - Schema/shape failures (syntactically valid but contract-invalid)

### Versioning
- When `prov_profile` / PROV constraints change, update fixtures so they remain meaningful:
  - Valid fixtures should continue to pass.
  - Invalid fixtures should continue to fail (for the intended reason).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| PROV constraints | `schemas/prov/` | Semver + changelog |
| Fixture inputs | `.github/actions/fixtures/catalogs/prov/**` | Keep deterministic; update with profile bumps |
| CI validators | `.github/workflows/` (or composite actions) | Contract tests required for changes |

### Extension points checklist (for future work)
- [ ] Add new invalid fixture case with a single clear violation
- [ ] Ensure a matching valid fixture exists when adding a new constraint category
- [ ] Keep fixtures minimal and synthetic (no sensitive data)
- [ ] Update CI tests to cover new fixture files

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- This fixture set does not surface directly in Focus Mode.
- Indirectly, it protects the invariant that **only provenance-linked, validated content** should flow downstream.

### Provenance-linked narrative rule
- Production rule reminder: downstream narrative claims must trace to provenance-linked evidence.
- This fixture set helps ensure provenance artifacts are rejected when malformed.

### Optional structured controls
~~~yaml
focus_layers:
  - "N/A (fixtures)"
focus_time: "N/A"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (this README)
- [ ] PROV schema/shape validation: **must fail** for each fixture file here
- [ ] Security and sovereignty checks: synthetic/non-sensitive fixtures only

### Reproduction
~~~bash
# Replace with repo-specific commands / scripts.
# Goal:
#  - Running the PROV validator against this folder MUST return non-zero (fail)
#  - Running the PROV validator against ../valid MUST return zero (pass)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Fixture pass/fail counts | CI logs | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- If fixtures or validators change behavior, ensure CI reviewers validate:
  - negative fixtures still fail
  - positive fixtures still pass

### CARE / sovereignty considerations
- Fixtures must not encode culturally sensitive knowledge, restricted locations, or community-controlled information.

### AI usage constraints
- AI transforms may summarize/structure this README, but must not invent policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial invalid PROV fixtures README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

