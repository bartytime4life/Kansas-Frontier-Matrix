---
title: "KFM Tests — Unit GeoJSON Fixtures"
path: "tests/unit/fixtures/geojson/README.md"
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

doc_uuid: "urn:kfm:doc:tests:unit:fixtures:geojson:readme:v1.0.0"
semantic_document_id: "kfm-tests-unit-fixtures-geojson-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:unit:fixtures:geojson:readme:v1.0.0"
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

# KFM Tests — Unit GeoJSON Fixtures

## 📘 Overview

### Purpose
- This folder holds **GeoJSON fixture files** used by unit tests to keep geospatial logic deterministic, readable, and reproducible.
- It governs **how GeoJSON fixtures are added, named, and reviewed**, including safety expectations around geometry and coordinates.

### Scope
| In Scope | Out of Scope |
|---|---|
| Small GeoJSON fixtures for unit tests (`.geojson`, `.json`) | Large datasets, production exports, or integration-test corpora |
| Minimal geometry examples (Point/LineString/Polygon, etc.) | Secrets, credentials, PII, or precise sensitive locations |
| Synthetic or generalized shapes safe for repo inclusion | Restricted cultural/site data without governance review |

### Audience
- Primary: Contributors writing/maintaining unit tests that parse/validate/transform geometry
- Secondary: Reviewers verifying determinism, safety, and governance alignment

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: a stable, version-controlled test input file.
  - **Geometry**: a GeoJSON geometry object (e.g., `Point`, `Polygon`).
  - **Feature**: a GeoJSON object with `type: "Feature"`, `geometry`, and `properties`.
  - **FeatureCollection**: a list of `Feature`s used when tests need multiple geometries.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Unit test docs | `tests/unit/README.md` | Repo maintainers | How to run unit tests |
| Fixtures root | `tests/unit/fixtures/README.md` | Test authors | General fixture policy |
| GeoJSON fixtures | `tests/unit/fixtures/geojson/` | Test authors | This folder |
| Schemas (if used) | `schemas/` | Schema owners | JSON schema checks in CI (if present) |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] GeoJSON fixture conventions documented and unambiguous
- [ ] Validation steps are repeatable (no local-only assumptions)
- [ ] Governance + CARE/sovereignty considerations stated for geospatial fixtures

## 🗂️ Directory Layout

### This document
- `path`: `tests/unit/fixtures/geojson/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| All tests | `tests/` | Test suites and test utilities |
| Unit tests | `tests/unit/` | Fast, isolated tests |
| Fixtures root | `tests/unit/fixtures/` | File-based fixtures for unit tests |
| GeoJSON fixtures | `tests/unit/fixtures/geojson/` | GeoJSON inputs for unit tests |
| Schemas | `schemas/` | JSON schemas / validators (if used in CI) |

### Expected file tree for this sub-area
~~~text
🧪 tests/
└── 🧪 unit/
    └── 🧰 fixtures/
        └── 🗺️ geojson/
            ├── 📄 README.md
            ├── 📁 geometries/        # optional: raw geometry objects
            ├── 📁 features/          # optional: Feature / FeatureCollection fixtures
            ├── 📁 invalid/           # optional: intentionally invalid fixtures (validation tests)
            └── 📁 cases/             # optional: bug/regression repro cases (named by issue/ticket)
~~~

> Note: Subfolders are **conventions**, not requirements—create only what your tests need.

## 🧭 Context

### Background
Unit tests involving geospatial data commonly need stable examples for:
- parsing and validating GeoJSON
- geometry normalization (coordinate ordering, precision, simplification)
- bounding box / centroid calculations
- conversions (GeoJSON ↔ WKT, GeoJSON ↔ internal geometry types)
- filtering by time, layer, or other properties

GeoJSON fixtures make those tests reviewable and reproducible.

### Constraints and invariants
- Preserve the canonical pipeline ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Prefer testing **public contracts** (schemas / API payloads) over internal coupling, unless the unit under test is explicitly internal.
- Fixtures in this folder must be safe for an open repository (see Governance section).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize GeoJSON schema validation in CI for these fixtures? | TBD | TBD |
| Do we enforce a single fixture layout (geometries/features/invalid)? | TBD | TBD |

## 🗺️ Diagrams

### GeoJSON fixture usage in a unit test
~~~mermaid
flowchart LR
  T[Test code] -->|loads| F[GeoJSON fixture file]
  F -->|parsed into| G[Geometry / Feature / FeatureCollection]
  G -->|exercise unit under test| U[Parser / Validator / Transformer]
  U -->|returns| R[Result]
  R -->|assert| A[Assertions]
~~~

## 📦 Data and Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| GeoJSON fixtures | `.geojson` / `.json` | `tests/unit/fixtures/geojson/` | Prefer schema + geometry validity checks when tooling exists |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Expected results | Assertions (code) or small expected files | `tests/unit/` or `tests/unit/fixtures/` | Test-specific |

### GeoJSON content expectations
Recommended (unless a test explicitly needs a counterexample):
- Valid JSON
- Standard GeoJSON object types (`Feature`, `FeatureCollection`, geometry types)
- Coordinate order consistent with GeoJSON expectations (`[longitude, latitude]` for WGS84)

> If a fixture is intentionally invalid, place it under `invalid/` and name it clearly (see conventions).

### Sensitivity and redaction
- GeoJSON fixtures must not contain:
  - credentials, API keys, access tokens
  - personal data (PII) or restricted cultural data
  - precise sensitive locations (use synthetic geometries or generalized shapes)

## 🌐 STAC, DCAT and PROV Alignment

### STAC
- GeoJSON fixtures may be used to test:
  - `geometry` and `bbox` handling in STAC Items
  - spatial extent normalization for Collections
- Keep fixtures minimal and focused on the spatial behavior under test.

### DCAT
- If tests map spatial metadata into DCAT views, GeoJSON fixtures should include only the properties required to test that mapping.

### PROV-O
- If fixtures are used in tests that connect geometry to lineage records, keep identifiers stable and avoid random IDs.

## ✅ GeoJSON fixture conventions

### Naming
Use descriptive names encoding intent. Recommended pattern:
- `geojson__<kind>__<scenario>.geojson`

Examples:
- `geojson__geometry__polygon_minimal_valid.geojson`
- `geojson__feature__point_with_properties.geojson`
- `geojson__featurecollection__two_features_mixed_types.geojson`
- `geojson__invalid__missing_type.geojson`
- `geojson__invalid__self_intersection_polygon.geojson`

> Convention note: `__` as a category/scenario separator is recommended for readability.

### Content rules
- Keep fixtures small (reviewable in PRs).
- Prefer synthetic values:
  - placeholder IDs (e.g., `feature-0001`)
  - minimal `properties` objects
- Avoid brittle ordering dependencies:
  - tests should not assert on JSON key order
  - when order matters (e.g., coordinate sequences), document why in the test

### Valid vs invalid fixtures
- Valid fixtures:
  - should be usable by multiple tests
  - should represent “minimal realistic” objects
- Invalid fixtures:
  - must be explicitly labeled and isolated in `invalid/`
  - must include a short comment in the test explaining what invalidity is being exercised

### When to add a GeoJSON fixture vs inline geometry
Add a fixture when:
- geometry is large enough to hurt test readability
- multiple tests share the same spatial case
- you want a durable repro case for a bug/regression

Inline geometry is fine when:
- it’s very small (e.g., a 1–2 coordinate point) and test-specific

## 🧠 Story Node and Focus Mode integration

### How this work surfaces in Focus Mode
- Typically indirect: GeoJSON fixtures here may unit-test logic that:
  - builds map layers
  - validates geometry before cataloging (STAC)
  - serializes geometry for APIs/UI

### Provenance-linked narrative rule
- If a fixture models narrative/context output, ensure tests assert on **provenance identifiers** and structured fields rather than free-text claims.

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks (if enabled for READMEs)
- [ ] JSON/schema validation for GeoJSON fixtures (where tooling exists)
- [ ] Unit tests pass (see `tests/unit/README.md`)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# Run unit tests:
#   make test
# or:
#   <your-test-runner> tests/unit
#
# Validate GeoJSON fixtures (if tooling exists):
#   <geojson-validator> tests/unit/fixtures/geojson/**/*.geojson
~~~

## ⚖ FAIR+CARE and Governance

### Review gates
- GeoJSON fixtures derived from any real-world source (even partial) should be reviewed for:
  - licensing compatibility
  - sensitivity / sovereignty constraints
  - coordinate generalization expectations

### CARE / sovereignty considerations
- If a fixture is based on culturally sensitive material or restricted site data:
  - do not include it here without explicit governance review
  - prefer synthetic stand-ins that preserve structure but not sensitive content

### AI usage constraints
- This README prohibits “infer_sensitive_locations”; do not add fixtures that would enable location inference beyond what’s necessary for testing.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial GeoJSON fixtures README | TBD |

---
Footer refs:
- Fixtures root: `tests/unit/fixtures/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`