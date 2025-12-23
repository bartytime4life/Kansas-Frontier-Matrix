---
title: "STAC Edge Case Fixtures — README"
path: ".github/actions/fixtures/catalogs/stac/edge_cases/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "active"
doc_kind: "CI Fixture Documentation"
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

doc_uuid: "urn:kfm:doc:ci-fixtures:stac-edge-cases-readme:v1.0.0"
semantic_document_id: "kfm-ci-fixtures-stac-edge-cases-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci-fixtures:stac-edge-cases-readme:v1.0.0"
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

# STAC Edge Case Fixtures — README

## 📘 Overview

### Purpose
This directory contains **STAC fixture catalogs** representing *edge cases* intended for CI workflows and local tests that validate the **Catalogs** stage. These fixtures are designed to exercise schema validation, link/href resolution, and “do not break” invariants before catalogs are used downstream (graph build, APIs, UI, and Story Nodes).

### Scope

| In Scope | Out of Scope |
|---|---|
| Small, deterministic STAC JSON fixtures (Catalog / Collection / Item) | Production STAC outputs under `data/stac/` |
| Both “should pass” and “should fail” cases (document expected outcome) | Large binary assets (GeoTIFFs, imagery, etc.) |
| Offline/self-contained link graphs (no network required) | External network calls during tests |
| Validator behavior around STAC versioning / links / required fields | DCAT/PROV fixtures (handled elsewhere) |

### Audience
- Primary: maintainers of **STAC schemas + validators** and **GitHub Actions** that enforce catalog correctness.
- Secondary: ETL contributors who need to understand “what will fail CI” before publishing a new dataset.

### Definitions
- **STAC**: SpatioTemporal Asset Catalog JSON.
- **Entry point**: the first STAC JSON document the harness loads for a case.
- **HREF**: link target (relative or absolute) used in STAC `links` and `assets`.
- **Valid fixture**: expected to pass schema + link checks.
- **Invalid fixture**: intentionally violates a single contract rule (expected to fail with a specific class of error).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/catalogs/stac/edge_cases/README.md` | CI maintainers | Top-level guidance + index |
| Fixture root | `.github/actions/fixtures/catalogs/stac/edge_cases/` | CI maintainers | Case directories live here |
| STAC schemas | `schemas/` (profile-dependent) | Catalogs maintainers | Used by schema validation gate |
| Usage references | `.github/` | CI maintainers | Search for `fixtures/catalogs/stac/edge_cases` |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Clear “how to add a case” guidance
- [ ] Index table present (even if initially empty)
- [ ] States that fixtures are non-production and may be intentionally invalid
- [ ] Sensitivity/PII guidance included (fixtures must be safe to publish)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/catalogs/stac/edge_cases/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI fixtures | `.github/actions/fixtures/` | Test inputs for CI workflows/actions |
| Production STAC outputs | `data/stac/` | Generated catalogs (collections/items) |
| Schemas | `schemas/` | JSON Schemas for STAC/DCAT/PROV profiles |
| Pipelines | `src/pipelines/` | ETL + catalog build tooling |
| Catalog docs | `docs/data/` | Mapping + profile docs |

### Fixture layout conventions
Cases should be **self-contained** and **offline**: any STAC `links` that are meant to resolve during validation should resolve to files inside the case directory (or intentionally demonstrate a broken link).

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 catalogs/
            └── 📁 stac/
                └── 📁 edge_cases/
                    ├── 📄 README.md
                    ├── 📁 case__<kebab-slug>/
                    │   ├── 📄 <entrypoint>.json
                    │   ├── 📄 <linked-asset-or-child>.json
                    │   ├── 📄 expected.md            (optional)
                    │   └── 📄 notes.md               (optional)
                    └── 📁 case__<kebab-slug-2>/
                        └── ...
~~~

Recommended naming:
- `case__<kebab-slug>/` (e.g., `case__missing-self-link/`, `case__invalid-bbox/`)
- Keep each case focused: **one primary edge condition per case**.

### Edge case index
Add one row per case directory. Keep this table updated as new cases are added.

| Case directory | Category | Expected outcome | Notes |
|---|---|---|---|
| `case__TBD/` | TBD | pass / fail | Replace with real cases |

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC JSON fixture(s) | `.json` | This directory | JSON Schema + link/href checks (CI) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validator result (pass/fail + messages) | CI logs / test output | N/A | Must match workflow expectations |

### Sensitivity & redaction
- Fixtures **must not** encode real sensitive locations, protected sites, or personal data.
- Use fabricated IDs, generalized coordinates, or clearly fictional place names.

### Quality signals
- Each case should be deterministic (stable IDs, stable ordering where relevant).
- Avoid mixing multiple unrelated failures in one “invalid” case.
- If your harness supports it, include a short `expected.md` describing the intended failure class (schema vs link vs logical).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Fixtures target the repository’s STAC profile (`stac_profile` in front-matter) and whatever validator behavior CI enforces.
- For invalid fixtures, document **exactly** what is broken (e.g., missing required field, invalid geometry, broken `links` graph).

### DCAT
- Not in scope for this fixture set.

### PROV-O
- Not in scope for this fixture set.

### Versioning
- If a fixture is meant to test versioning semantics, include the relevant predecessor/successor links and describe the expected validator behavior.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Catalogs (CI) | Validate STAC fixtures | JSON Schema + link resolver |
| Catalogs (prod) | Publish STAC outputs | `data/stac/` generation pipeline |
| Pipelines | Generate catalogs from processed data | `src/pipelines/` configs + runs |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (if present) |
| CI workflows | `.github/workflows/` | Must remain deterministic |

### Extension points checklist (for future work)
- [ ] Add a new `case__.../` folder with minimal STAC JSON
- [ ] Update the Edge case index table
- [ ] Ensure the case is self-contained (or intentionally demonstrates a broken reference)
- [ ] Add/adjust tests so the case is exercised in CI

## 🧠 Story Node & Focus Mode Integration
- Not directly applicable (fixtures are internal), but correct catalog validation protects downstream provenance and “no hallucinated sources” constraints by ensuring catalog integrity before Story Nodes consume assets.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] JSON schema validation for STAC fixtures
- [ ] Link/href resolution checks (offline)
- [ ] Determinism check (no network dependency, stable file ordering)

### Reproduction
~~~bash
# Replace with repo-specific commands.
# Tip: search for a validator entrypoint in `tools/`, `src/pipelines/catalog/`, or `.github/workflows/`.

# Example sanity check (JSON parse only):
# python -m json.tool .github/actions/fixtures/catalogs/stac/edge_cases/<case>/...json > /dev/null
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to STAC schemas or validators should receive review from the Catalogs maintainers.
- Any fixture that could implicate sovereignty/sensitivity concerns (even accidentally) requires human review.

### CARE / sovereignty considerations
- Keep fixtures culturally neutral and synthetic.
- Do not include restricted Indigenous knowledge, precise sensitive locations, or personal data.

### AI usage constraints
- Ensure fixtures cannot be used to infer sensitive locations (avoid “real-but-hidden” coordinates).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial edge-case fixtures README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

