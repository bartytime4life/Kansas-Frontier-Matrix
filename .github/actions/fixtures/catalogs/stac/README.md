---
title: "STAC Catalog Fixtures for CI"
path: ".github/actions/fixtures/catalogs/stac/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:ci:fixtures:catalogs:stac:readme:v1.0.0"
semantic_document_id: "kfm-ci-fixtures-catalogs-stac-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:fixtures:catalogs:stac:readme:v1.0.0"
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

# STAC Catalog Fixtures for CI

## 📘 Overview

### Purpose
- Provide **small, deterministic STAC JSON fixtures** used by CI and/or composite actions to validate:
  - JSON structure against the project’s STAC-related schemas
  - Internal link integrity between STAC objects
- Make it easy for contributors to update fixtures safely when STAC contracts evolve.

### Scope
| In Scope | Out of Scope |
|---|---|
| Minimal STAC Catalog / Collection / Item examples used for tests | Production catalogs and datasets (canonical outputs live under `data/stac/`) |
| Synthetic data suitable for public repos | Real sensitive coordinates, personal data, or copyrighted assets |
| Offline-friendly fixtures (relative links preferred) | Fixtures that require network calls or external hosting |

### Audience
- CI maintainers working under `.github/`
- Catalog/schema maintainers updating `schemas/` or STAC profile expectations
- Contributors adding or modifying STAC-related validation actions

### Definitions
- **STAC**: SpatioTemporal Asset Catalog JSON metadata objects (Catalog, Collection, Item).
- **Fixture**: A small, test-only dataset designed to exercise validators deterministically.
- **HREF**: The link target in `links[].href` fields.

See `docs/glossary.md` for canonical definitions if present.

### Key artifacts
- `docs/MASTER_GUIDE_v12.md` — canonical pipeline ordering and catalog expectations
- `schemas/` — schema definitions used by validators (STAC/DCAT/PROV)
- `data/stac/` — canonical home for real STAC outputs
- `.github/actions/` — composite actions that may consume these fixtures
- `.github/workflows/` — CI workflows that call validators

### Definition of done
- [ ] This README validates under the KFM Markdown protocol.
- [ ] Fixtures in this folder validate against the intended schema rules.
- [ ] Fixture link graphs are internally consistent (no broken relative references).
- [ ] Fixtures are deterministic and do not rely on external network access.
- [ ] No sensitive or restricted data is included.

## 🗂️ Directory Layout

### This document
- Path: `.github/actions/fixtures/catalogs/stac/README.md`

### Related repository paths
- Canonical STAC outputs: `data/stac/`
- Canonical schema store: `schemas/`
- Catalog build pipelines: `src/pipelines/` (if present)
- CI workflows: `.github/workflows/`
- Composite actions: `.github/actions/`

### Expected file tree for this sub-area
This directory should contain one or more STAC fixture sets. Keep each fixture set **small** and **self-contained**.

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 catalogs/
            └── 📁 stac/
                ├── 📄 README.md
                ├── 📁 minimal_valid/
                │   ├── 📄 catalog.json
                │   ├── 📄 collection.json
                │   └── 📄 item.json
                └── 📁 edge_cases/
                    └── 📄 <additional-stac-json-files>.json
~~~

## 🧭 Context

### Background
KFM treats catalogs (STAC/DCAT/PROV) as **first-class evidence artifacts** that feed downstream graph/API/UI workflows. These fixtures exist to keep CI validation deterministic and to protect the catalog contracts from accidental regressions.

### Assumptions
- Validators run in CI without relying on external services.
- Fixtures are designed to be stable over time and to survive refactors.
- Relative `href` links are preferred so fixture directories can be moved/copied as a unit.

### Constraints / invariants
- **Do not** place production or large datasets in `.github/actions/fixtures/`.
- Fixtures must remain **small** and **fast** to validate.
- Do not include sensitive locations, PII, or culturally restricted content.
- Prefer synthetic geometry extents and timestamps that are clearly fictional.
- Keep IDs stable once a fixture is referenced by tests (avoid breaking test expectations).

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC fixture objects | JSON | This folder (and subfolders) | Schema + link integrity checks in CI |
| Schema definitions | JSON Schema | `schemas/` | Schema compilation / schema lint in CI |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation pass/fail | CI result | GitHub Actions logs | Must be deterministic |
| Optional test reports | JSON / JUnit | CI artifacts | Repo-specific (not defined here) |

### Sensitivity & redaction
- Fixtures should be safe for public distribution.
- If a test requires “realistic” geometry, use generalized/synthetic shapes and avoid identifying details.

### Quality signals
- All fixtures are schema-valid for their STAC object type.
- All `links[].href` values resolve correctly within the fixture set.
- No external network dependency is required to validate.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Fixture sets should include at least one **Collection** and one **Item** (minimum viable coverage).
- Prefer relative `href` links between objects.
- Ensure `links` relationships are internally coherent (root/self/parent/child/item/collection as applicable).

### DCAT
- Not defined in this fixture directory.
- If DCAT fixtures are needed, store them under a dedicated DCAT fixtures sub-area and document it there.

### PROV-O
- Not defined in this fixture directory.
- If PROV fixtures are needed, store them under a dedicated PROV fixtures sub-area and document it there.

### Versioning
- When schema expectations or profiles change, update:
  - Fixture JSON as needed
  - This README’s `version` and `last_updated`
  - Any CI tests or workflows that pin assumptions to fixture content

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Fixture pack | Provides deterministic STAC JSON inputs for CI | Files under `.github/actions/fixtures/catalogs/stac/` |
| CI validation | Runs schema + integrity checks | `.github/workflows/` + `.github/actions/` |
| Schema store | Defines machine-validated contracts | `schemas/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Markdown protocol | `docs/standards/` | Governed by KFM-MDP version |
| STAC-related schemas | `schemas/` | SemVer + changelog (repo policy) |
| STAC fixtures | `.github/actions/fixtures/catalogs/stac/` | Update with tests; keep deterministic |

### Extension points checklist
- [ ] STAC: add a new fixture set that exercises a new schema rule
- [ ] STAC: add a new link integrity edge case fixture
- [ ] CI: add/adjust validators to cover new STAC profile constraints
- [ ] Docs: keep this README synchronized with fixture folder structure

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirectly: valid catalogs underpin evidence discoverability and provenance-linked navigation.
- Fixtures provide regression protection so catalog structure changes do not silently break downstream consumers.

### Provenance-linked narrative rule
- This document makes no narrative claims about historical facts.
- Any future “example” claims added here should be clearly synthetic and test-oriented.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front matter + structure)
- [ ] Schema validation for STAC JSON fixtures
- [ ] Link integrity checks for STAC `links[].href`
- [ ] Repo lint checks (no large/binary data in fixtures)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate STAC schemas against fixture JSON
# <repo-command> validate stac --fixtures .github/actions/fixtures/catalogs/stac/

# 2) run unit/integration tests that reference fixtures
# <repo-command> test

# 3) run doc lint / markdown protocol checks
# <repo-command> lint:docs
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to fixtures that affect schema expectations should be reviewed by:
  - Catalog/schema maintainers
  - CI workflow maintainers
- If fixture content ever includes culturally sensitive material: requires human review.

### CARE / sovereignty considerations
- Fixtures should avoid culturally sensitive or restricted information by default.
- If test coverage requires such patterns, use generalized/synthetic representations and follow sovereignty policy.

### AI usage constraints
- Respect the `ai_transform_permissions` / `ai_transform_prohibited` fields in front matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for STAC fixture directory | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
