---
title: "README — PROV Catalog Fixtures (GitHub Actions)"
path: ".github/actions/fixtures/catalogs/prov/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:catalogs:prov:readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-catalogs-prov-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:catalogs:prov:readme:v1.0.0"
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

# README — PROV Catalog Fixtures (GitHub Actions)

## 📘 Overview

### Purpose
This directory contains **small, deterministic PROV fixtures** used by CI (GitHub Actions) to validate KFM provenance/lineage expectations in a fast, reproducible way.

These fixtures are intended to:
- assert validator behavior (known-good fixtures pass; known-bad fixtures fail deterministically),
- support contract/schema evolution without depending on production catalogs,
- keep provenance examples **synthetic** and **public-safe**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal PROV fixture bundles (e.g., JSON / JSON-LD) | Production lineage bundles under `data/prov/**` |
| “Valid” and “Invalid” cases for deterministic CI expectations | End-to-end ETL lineage for a real dataset |
| ID conventions and naming for fixture artifacts | Graph/API/UI fixtures (tracked elsewhere) |
| Fixtures demonstrating redaction/generalization mechanics | Any sensitive locations, culturally restricted knowledge, PII |

### Audience
- Primary: CI/workflow maintainers; catalog/profile maintainers.
- Secondary: pipeline contributors adding provenance capture; reviewers verifying contract compliance.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **PROV / PROV-O**: W3C provenance vocabulary used to describe lineage.
  - **Entity**: something produced/used (e.g., a dataset artifact).
  - **Activity**: something that happened (e.g., a pipeline run/step).
  - **Agent**: actor responsible for an activity (person/system).
  - **Fixture**: small example used by CI for deterministic validation.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/catalogs/prov/README.md` | Repo maintainers | Governs PROV fixture conventions |
| PROV fixtures | `.github/actions/fixtures/catalogs/prov/**` | CI + Catalog owners (TBD) | Small examples used for CI/tests |
| Canonical PROV outputs | `data/prov/**` | Pipeline/Catalog owners | Generated lineage bundles (not fixtures) |
| Schemas / contracts | `schemas/**` (and/or `schemas/prov/**`) | Contract maintainers | Fixtures should validate against these |
| Standards / profiles | `docs/standards/**` | Standards owners | KFM-PROV profile (path not confirmed here) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Conventions documented for valid and invalid fixtures
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Mermaid diagrams render in GitHub markdown

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/catalogs/prov/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Catalog fixtures | `.github/actions/fixtures/catalogs/` | Fixture catalogs (STAC/DCAT/PROV) |
| PROV fixtures | `.github/actions/fixtures/catalogs/prov/` | This folder |
| Canonical lineage outputs | `data/prov/` | Generated PROV bundles (non-fixture) |
| Schemas | `schemas/` | Validation contracts (JSON schema, shapes, etc.) |
| Pipelines | `src/pipelines/` | ETL + catalog build tooling |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API | `src/api/` (or repo equivalent) | API layer (UI never reads graph directly) |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 catalogs/
            └── 📁 prov/
                ├── 📄 README.md
                ├── 📁 valid/
                │   └── 📄 minimal_lineage.jsonld
                ├── 📁 invalid/
                │   ├── 📄 missing_activity.jsonld
                │   └── 📄 broken_linkage.jsonld
                └── 📄 manifest.yaml
~~~

> The filenames above are placeholders. Keep names stable and descriptive (what behavior is being tested).

## 🧭 Context

### Background
KFM treats provenance as a first-class “evidence layer” that supports downstream trust:
- catalog artifacts are produced first (STAC/DCAT/PROV),
- then used to build the graph,
- then served via APIs to the UI and narrative layers.

Fixtures exist so CI can verify provenance contracts without needing full production outputs.

### Assumptions
- Fixtures are small and reviewable in PRs.
- Fixtures are synthetic and do not contain sensitive locations or PII.
- Each invalid fixture is designed to fail for a single primary reason (when feasible).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Fixtures must not become a shadow copy of production lineage outputs.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize a single PROV serialization (JSON-LD vs JSON) for fixtures? | CI + Catalog owners | TBD |
| Do we require canonical ordering/compaction to reduce diff noise? | Contract owners | TBD |
| Do we validate PROV fixtures via JSON Schema, SHACL, or both? | Catalog owners | TBD |

### Future extensions
- Add fixtures for:
  - multi-step activity chains,
  - multi-agent attribution,
  - derivation chains across ETL stages,
  - redaction/generalization examples that are explicitly labeled and synthetic.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph CI["CI / GitHub Actions"]
    F["PROV fixtures\n.github/actions/fixtures/catalogs/prov"] --> V["Validate\n(PROV schema + profile)"]
    V --> R["CI status + logs"]
  end

  A["ETL"] --> B["STAC/DCAT/PROV Catalogs"]
  B --> C["Neo4j Graph"]
  C --> D["APIs"]
  D --> E["React/Map UI"]
  E --> S["Story Nodes"]
  S --> FM["Focus Mode"]

  B --> V
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer (PR)
  participant CI as GitHub Actions
  participant Val as Validator
  Dev->>CI: push / open PR
  CI->>Val: load PROV fixture
  Val-->>CI: pass/fail + diagnostics
  CI-->>Dev: CI status (green/red)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PROV fixtures | JSON / JSON-LD | `.github/actions/fixtures/catalogs/prov/**` | PROV schema + KFM-PROV profile constraints |
| Optional manifest | YAML | `.github/actions/fixtures/catalogs/prov/manifest.yaml` | YAML lint (+ schema if defined) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation results | logs | GitHub Actions logs | deterministic pass/fail + diagnostic output |

### Sensitivity & redaction
Fixtures must not include:
- secrets, tokens, credentials,
- PII (emails, phone numbers, private addresses),
- sensitive or culturally restricted site locations (unless generalized and explicitly marked as a synthetic/redaction example).

### Quality signals
- Fixtures are deterministic and diffable.
- IDs are stable; no nondeterministic timestamps unless explicitly testing time behavior.
- Each invalid fixture has a clear, documented failure intent.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Not covered here. If a PROV fixture references a STAC item/asset ID, keep the reference stable and synthetic (or point to a sibling fixture if your CI expects cross-links).

### DCAT
Not covered here. If a PROV fixture references a DCAT dataset identifier, keep it stable and synthetic (or reference a sibling DCAT fixture if your CI expects cross-links).

### PROV
Recommended minimum components for a *valid* fixture:
- at least one Entity, Activity, Agent,
- at least one linkage (e.g., generation/association/derivation),
- stable identifiers that resemble the patterns used by the real pipeline.

Recommended minimum components for an *invalid* fixture:
- intentionally omit one required component or break one required linkage,
- avoid introducing multiple unrelated errors in the same fixture.

### Versioning
When provenance contracts evolve:
- keep old fixtures if they represent important backward-compat behavior (or move them to a `deprecated/` folder),
- bump fixture sets and document expected behavior changes in the Version History below.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| PROV fixtures | deterministic examples | filesystem paths in `.github/actions/fixtures/catalogs/prov/**` |
| Validators | schema + profile enforcement | CI steps (workflow/action dependent) |
| Contracts | define “valid provenance” | `schemas/**` + `docs/standards/**` |

### Interfaces / contracts
- Fixtures should validate against the repo’s canonical contracts (schemas/profiles).
- CI should fail deterministically for invalid fixtures and pass for valid fixtures.

### Extension points checklist
- [ ] Add fixture for a new provenance rule
- [ ] Add a negative fixture for the primary failure mode
- [ ] Update manifest/workflow enumeration for new files (if used)
- [ ] Confirm fixture remains synthetic + governance-safe

## 🧠 Story Node & Focus Mode Integration

This fixture directory is not a Story Node surface.

Indirectly, PROV fixtures help ensure Story Nodes and Focus Mode only consume provenance-linked content by keeping provenance validation gates reliable.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks for this README
- [ ] Syntax checks for PROV serialization (JSON / JSON-LD)
- [ ] Schema/profile validation for PROV fixtures
- [ ] (Optional) cross-link sanity checks against STAC/DCAT fixtures
- [ ] Security + sovereignty scanning gates (where applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands or workflow references.

# 1) Validate PROV fixtures against schemas/profiles (preferred: same command CI runs)
# <command>

# 2) Run tests referencing fixtures
# <command>

# 3) Lint docs (markdown protocol)
# <command>
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- CI/workflow maintainers approve changes that alter fixture enumeration or expected pass/fail behavior.
- Contract/profile maintainers approve changes that redefine “valid provenance” expectations.

### CARE / sovereignty considerations
- Fixtures must be synthetic/redacted.
- Do not encode restricted location detail in examples.
- If demonstrating redaction mechanics, label the fixture clearly as synthetic/redaction.

### AI usage constraints
- Ensure doc permissions/prohibitions in front-matter match intended use.
- Do not use AI to infer or reconstruct sensitive locations from redacted examples.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for PROV fixtures directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
