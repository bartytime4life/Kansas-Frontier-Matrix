---
title: "KFM Tests — Unit Fixtures (JSON)"
path: "tests/unit/fixtures/json/README.md"
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

doc_uuid: "urn:kfm:doc:tests:unit:fixtures:json:readme:v1.0.0"
semantic_document_id: "kfm-tests-unit-fixtures-json-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:unit:fixtures:json:readme:v1.0.0"
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

# KFM Tests — Unit Fixtures (JSON)

## 📘 Overview

### Purpose
- This folder holds **JSON fixtures** used by unit tests to keep test inputs deterministic, readable, and reproducible.
- It governs **how JSON fixtures are added, formatted, named, and reviewed**, especially when fixtures model public contracts (STAC/DCAT/PROV shapes, API payloads, graph exports).

### Scope
| In Scope | Out of Scope |
|---|---|
| Small, deterministic `.json` fixtures for unit tests | Large datasets, production exports, integration-test corpora |
| Minimal examples for schema/contract edge cases | Secrets, credentials, tokens, PII, or restricted cultural data |
| Synthetic or redacted samples safe for repo inclusion | Precise sensitive locations (use generalized geometry or synthetic) |
| Canonical/minimal STAC/DCAT/PROV JSON shapes (when needed) | “Living” fixtures that change with time (timestamps/UUIDs not fixed) |

### Audience
- Primary: Contributors writing/maintaining unit tests
- Secondary: Reviewers verifying determinism, safety, and governance alignment

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: a stable, version-controlled test input file.
  - **Schema-valid**: conforms to a JSON Schema (or other validator) when such a schema exists.
  - **Contract fixture**: a fixture that represents a public-facing structure (catalog, API payload, etc.).
  - **Golden**: a snapshot-style expected output fixture (only if the project adopts golden testing).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Unit test docs | `tests/unit/README.md` | Repo maintainers | How to run unit tests |
| Fixtures root | `tests/unit/fixtures/README.md` | Repo maintainers | Global fixture rules |
| JSON fixtures directory | `tests/unit/fixtures/json/` | Test authors | This folder |
| Schemas | `schemas/` | Schema owners | Used for JSON/schema checks |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] JSON fixture conventions documented and unambiguous
- [ ] Formatting/validation steps are repeatable (no local-only assumptions)
- [ ] Governance + CARE/sovereignty considerations stated for JSON fixtures

## 🗂️ Directory Layout

### This document
- `path`: `tests/unit/fixtures/json/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| All tests | `tests/` | Test suites and test utilities |
| Unit tests | `tests/unit/` | Fast, isolated tests |
| Unit fixtures | `tests/unit/fixtures/` | All fixture types |
| JSON fixtures | `tests/unit/fixtures/json/` | This folder: JSON inputs for unit tests |
| Schemas | `schemas/` | JSON schemas / validators used in CI |

### Expected file tree for this sub-area
~~~text
🧪 tests/
└── 🧪 unit/
    └── 🧰 fixtures/
        └── 🗂️ json/
            ├── 📄 README.md
            ├── 🛰️ stac/       # optional: STAC Item/Collection/Catalog JSON fixtures
            ├── 🏷️ dcat/       # optional: DCAT(-ish) dataset/view fixtures
            ├── 🧬 prov/       # optional: PROV(-ish) activity/entity/agent fixtures
            ├── 🔌 api/        # optional: request/response payload fixtures
            ├── 🕸️ graph/      # optional: minimal graph export/serialization fixtures
            └── 🧩 misc/       # optional: small generic JSON fixtures
~~~

> Note: Subfolders are **conventions**, not requirements—create only what your tests need.

## 🧭 Context

### Background
Unit tests should be:
- **Deterministic** (same inputs → same outputs)
- **Small + focused** (unit-level behavior, not end-to-end pipelines)
- **Safe to share** (no secrets; no sensitive location leakage)

JSON fixtures support unit tests by providing reviewable, reusable inputs and by enabling targeted coverage of edge cases.

### Assumptions
- Unit tests can load local files from this directory.
- JSON fixtures may represent minimal “shapes” of:
  - catalog objects (STAC/DCAT/PROV),
  - API payloads (request/response),
  - internal DTOs used at module boundaries,
  - minimal graph serialization payloads (if testing serialization logic).
- Test runner commands are **not confirmed in repo** in this README; placeholders are provided and should be replaced once the canonical test commands are known.

### Constraints / invariants
- Keep the conceptual pipeline ordering intact: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Prefer testing **public contracts** (schemas/APIs) over internal coupling—unless the unit under test is explicitly internal.
- JSON fixtures must be stable: avoid variable timestamps, random UUIDs, and environment-dependent values unless fixed.

## 🗺️ Diagrams

### JSON fixture usage (unit-test level)
~~~mermaid
flowchart LR
  T[Test code] -->|loads| F[JSON fixture]
  F -->|parsed into| D[Domain object / DTO]
  D -->|exercise unit under test| U[Function / module]
  U -->|returns| R[Result]
  R -->|assert| A[Assertions]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| JSON fixture files | `.json` | `tests/unit/fixtures/json/` | Prefer schema validation when schemas exist |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Test expectations | Assertions (code) or small expected JSON | `tests/unit/` or `tests/unit/fixtures/json/` | Test-specific |

### Sensitivity & redaction
JSON fixtures must not contain:
- credentials, API keys, access tokens
- personal data (PII) or restricted cultural/site data
- precise sensitive locations (use generalized coordinates or synthetic geometries)

If a real-world-derived structure is required for a test, prefer:
- structural fidelity over content fidelity (synthetic stand-ins),
- redaction/generalization for any location-like fields.

### Quality signals
Prefer JSON fixtures that are:
- minimal but realistic
- schema-valid when schemas are available
- stable (no volatile fields unless fixed)
- formatted consistently (low diff noise)

## 🌐 STAC, DCAT & PROV Alignment

### STAC (JSON fixtures)
Use STAC fixtures when unit-testing:
- parsing/validation of STAC Items/Collections/Catalogs,
- mapping logic from ETL outputs to STAC,
- any STAC extension behavior you support.

Guidance:
- Keep fixtures minimal: often **1 Collection + 1 Item** covers most logic paths.
- Use stable IDs and stable datetime strings.
- Prefer synthetic footprints/geometries that do not reveal sensitive sites.

### DCAT (JSON fixtures)
Use DCAT(-view) fixtures when unit-testing:
- catalog view generation,
- mappings to/from DCAT fields.

Guidance:
- include only the fields required by the mapping logic under test (title/description/license/keywords/etc.),
- keep identifiers stable.

### PROV-O (JSON fixtures)
Use PROV-like fixtures when unit-testing:
- lineage extraction,
- provenance-linking behavior,
- trace queries and transformations.

Guidance:
- keep agent/activity/entity identifiers stable,
- prefer explicit `used` / `wasGeneratedBy` relationships if your code expects them.

## ✅ JSON fixture conventions

### File naming (recommended)
Use descriptive names that encode intent:
- `stac__item__minimal_valid.json`
- `stac__item__missing_datetime.json`
- `api__search__request__minimal.json`
- `prov__activity__etl_run__minimal.json`

Recommendations:
- Prefer `__` as a visual separator between **domain** and **scenario**.
- Prefer lowercase + underscores.

### JSON formatting rules (recommended)
To reduce diff noise and improve reviewability:
- UTF-8 encoding
- newline at end of file
- stable indentation (recommended: 2 spaces)
- no trailing whitespace
- avoid floating-point noise (use simple values unless precision is under test)

**Key ordering note:** JSON object key order is not semantically meaningful; however, using a stable formatter or stable manual ordering improves diff readability.

### Content rules
- Keep fixtures small and PR-reviewable.
- Prefer synthetic values:
  - placeholder IDs (e.g., `item-0001`)
  - generalized datetimes (e.g., `1900-01-01T00:00:00Z`) when exact time is not under test
- Avoid brittle ordering dependencies:
  - if JSON order is irrelevant, tests should not assert on serialized key order.

### When to add a JSON fixture vs inline JSON in test code
Add a fixture when:
- data is large enough to harm readability if embedded in the test
- multiple tests share the same input
- you want a durable repro case for a bug/regression

Inline JSON is fine when:
- it’s short (roughly < ~15 lines) and test-specific
- it’s clearer to inline the shape right next to the assertion

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (if enabled for READMEs)
- [ ] JSON validity check (parseable JSON)
- [ ] Schema validation (where schemas exist for the fixture type)
- [ ] Unit tests pass (see `tests/unit/README.md`)

### Reproduction
~~~bash
# NOTE: Commands below are placeholders — not confirmed in repo.
# Replace with the repo’s canonical unit-test + validation commands.

# 1) Run unit tests:
#   make test
# or:
#   <your-test-runner> tests/unit

# 2) Validate JSON is parseable:
#   python -m json.tool tests/unit/fixtures/json/<file>.json >/dev/null

# 3) Validate against schemas (if tooling exists):
#   <schema-validator> --schema schemas/<schema>.json tests/unit/fixtures/json/<file>.json
~~~

### Fixture review checklist (PR gate)
- [ ] The fixture is minimal and clearly named
- [ ] The fixture contains no secrets/PII/sensitive locations
- [ ] The fixture is parseable JSON
- [ ] The fixture is schema-valid (if a schema exists)
- [ ] The unit test asserts behavior, not incidental formatting

## ⚖ FAIR+CARE & Governance

### Review gates
If a JSON fixture includes any real-world derived content (even partial), it should be reviewed for:
- licensing compatibility
- sensitivity / sovereignty constraints
- coordinate redaction/generalization rules

### CARE / sovereignty considerations
If a fixture is based on culturally sensitive material or restricted site data:
- do not include it here without explicit governance review
- prefer synthetic stand-ins that preserve structure but not sensitive content

### AI usage constraints
This README prohibits “infer_sensitive_locations”; do not add JSON fixtures that would enable location inference beyond what’s necessary for testing.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial JSON fixtures README | TBD |

---
Footer refs:
- Fixtures root README: `tests/unit/fixtures/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`