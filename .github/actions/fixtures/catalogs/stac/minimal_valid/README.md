---
title: "STAC Fixture — minimal_valid (CI)"
path: ".github/actions/fixtures/catalogs/stac/minimal_valid/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "Fixture"
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

doc_uuid: "urn:kfm:doc:fixtures:catalogs:stac:minimal-valid:v1.0.0"
semantic_document_id: "kfm-fixture-catalogs-stac-minimal-valid-v1.0.0"
event_source_id: "ledger:kfm:doc:fixtures:catalogs:stac:minimal-valid:v1.0.0"
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

# STAC Fixture — minimal_valid

## 📘 Overview

### Purpose
- Provide a **small, deterministic, schema-valid** STAC example that CI can use as a baseline fixture.
- Catch validator/config regressions (schemas, link resolution, strictness) without requiring full domain data.

### Scope
| In Scope | Out of Scope |
|---|---|
| Minimal STAC JSON needed to validate a simple catalog/collection/item shape | Production datasets, large assets, or domain-specific semantics |

### Audience
- Primary: CI / schema maintainers
- Secondary: Developers adding or updating STAC validators

### Definitions (link to glossary)
- Link: TBD (define canonical glossary path if/when present)
- STAC: SpatioTemporal Asset Catalog
- Fixture: a tiny input set used by tests/CI

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Fixture directory | `.github/actions/fixtures/catalogs/stac/minimal_valid/` | CI maintainers | Contains the STAC JSON files and this README |
| Production STAC outputs | `data/stac/` | Catalog stage | Not used by this fixture |

### Definition of done (for this fixture)
- [ ] All STAC JSON in this directory validates under the repo’s STAC validator configuration
- [ ] All `href` links resolve when validated from this directory (prefer relative links)
- [ ] Fixture remains synthetic and contains no sensitive locations/PII

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/catalogs/stac/minimal_valid/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI fixtures | `.github/actions/fixtures/` | Small deterministic test inputs for GitHub Actions |
| STAC fixtures | `.github/actions/fixtures/catalogs/stac/` | STAC-focused fixtures (baseline + edge cases) |
| STAC catalogs (generated) | `data/stac/` | Canonical STAC outputs from the catalog stage |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 catalogs/
            └── 📁 stac/
                └── 📁 minimal_valid/
                    ├── 📄 README.md
                    ├── 📄 <stac-root-or-catalog>.json
                    ├── 📄 <stac-collection>.json
                    └── 📄 <stac-item>.json
~~~

## 🧭 Context

### Background
KFM treats STAC (along with DCAT and PROV) as a **first-class catalog layer** in the canonical pipeline. This fixture exists so CI can validate that the STAC tooling still accepts a minimal “happy path” input.

### Assumptions
- Fixture JSON is intentionally minimal and synthetic (no real-world sensitive locations).
- The CI validator(s) are configured to scan this directory (or its parent) as an input.

### Constraints / invariants
- Keep this fixture **minimal**: only add fields/extensions when they are required for the baseline validator contract.
- Prefer adding new fixture folders (e.g., `./extensions/<name>/...`) instead of expanding `minimal_valid` when testing optional extensions.
- Do not add non-deterministic values (timestamps that change, random IDs, etc.).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical CI command/entrypoint for STAC validation in this repo? | TBD | TBD |
| What STAC validator implementation/version is expected (python, node, etc.)? | TBD | TBD |

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["Fixture: minimal_valid (STAC JSON)"] --> B["CI: STAC schema + link validation"]
  B --> C["Pass/Fail gate for PRs"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC fixture JSON | JSON | `.github/actions/fixtures/catalogs/stac/minimal_valid/` | STAC schema + link integrity |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation report/logs | CI logs | GitHub Actions logs | N/A |

### Sensitivity & redaction
- This fixture should remain **public + synthetic**. If a test case requires realistic geometry, use generalized/fictional coordinates.

### Quality signals
- Validation is deterministic and repeatable across platforms.
- No broken links within the STAC JSON (relative link resolution preferred).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This directory provides a baseline for STAC validation.
- It should not attempt to represent full KFM STAC profile coverage; that belongs in dedicated fixtures.

### DCAT / PROV
- Not applicable for this fixture.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Run the repository’s STAC validator against this directory.
- [ ] Ensure the validator checks both **schema compliance** and **`href` integrity**.
- [ ] Confirm the fixture passes in CI on the default runner image(s).

### Reproduction
~~~bash
# Replace these placeholders with the repo’s actual validation commands/workflow entrypoint.
#
# 1) run stac validation
# <repo-command> validate stac .github/actions/fixtures/catalogs/stac/minimal_valid/
~~~

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: no
- Security council review: no
- Historian/editor review: no

### CARE / sovereignty considerations
- Keep the fixture synthetic and avoid encoding culturally sensitive locations or restricted site information.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Add README describing the minimal_valid STAC CI fixture | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

