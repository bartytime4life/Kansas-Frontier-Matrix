---
title: "KFM Tests — CSV Fixtures"
path: "tests/unit/fixtures/csv/README.md"
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

doc_uuid: "urn:kfm:doc:tests:unit:fixtures:csv:readme:v1.0.0"
semantic_document_id: "kfm-tests-unit-fixtures-csv-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:unit:fixtures:csv:readme:v1.0.0"
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

# KFM Tests — CSV Fixtures

## 📘 Overview

### Purpose
- This folder holds **CSV-based fixtures** used by unit tests to keep test inputs:
  - deterministic (same input → same output),
  - reviewable (small, readable diffs),
  - reproducible (portable across machines/CI).
- This README governs **how CSV fixtures are added, named, formatted, and reviewed**.

> If anything here conflicts with the parent fixtures guidance, defer to: `tests/unit/fixtures/README.md`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Small, deterministic CSV files for unit tests | Large datasets, production exports, or integration-test corpora |
| CSVs that model edge cases (missing values, header variants, typing quirks) | Secrets, credentials, API keys, or tokens |
| Synthetic or redacted samples safe for repo inclusion | PII or precise sensitive locations (even if “publicly known”) |

### Audience
- Primary: Contributors writing/maintaining unit tests that consume CSV inputs
- Secondary: Reviewers verifying determinism, safety, and governance alignment

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: a stable, version-controlled test input file.
  - **Schema (CSV)**: the expected columns (and sometimes types/constraints) a CSV must have.
  - **Generalization**: coarsening sensitive fields (e.g., coordinates) to avoid inference.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Unit test docs | `tests/unit/README.md` | Repo maintainers | How to run unit tests |
| Parent fixtures rules | `tests/unit/fixtures/README.md` | Repo maintainers | Global fixture conventions |
| CSV fixtures directory | `tests/unit/fixtures/csv/` | Test authors | Add CSV inputs here |
| Schemas | `schemas/` | Schema owners | Use when validating fixtures (if applicable) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] CSV fixture conventions documented and unambiguous
- [ ] Validation steps are repeatable (no local-only assumptions)
- [ ] Governance + CARE/sovereignty constraints stated for CSV fixtures

## 🗂️ Directory Layout

### This document
- `path`: `tests/unit/fixtures/csv/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| All tests | `tests/` | Test suites, test utilities, and test docs |
| Unit tests | `tests/unit/` | Fast, isolated tests |
| Unit fixtures | `tests/unit/fixtures/` | File-based fixtures for unit tests |
| CSV fixtures | `tests/unit/fixtures/csv/` | This folder: CSV inputs/expected outputs |
| Schemas | `schemas/` | JSON schemas / validators used in CI |

### Expected file tree for this sub-area
~~~text
🧪 tests/
└── 🧪 unit/
    └── 🧰 fixtures/
        └── 🧾 csv/
            ├── 📄 README.md
            ├── 📄 <fixture-name>.csv
            ├── 📄 <fixture-name>.expected.csv      # optional: expected-output snapshot
            └── 📄 <fixture-name>.schema.json       # optional: column/type spec (if adopted)
~~~

## 🧭 Context

### Background
CSV fixtures commonly support unit tests in these pipeline-adjacent areas:
- ETL helpers (parsing/normalization of tabular inputs)
- Schema mapping logic (columns → canonical fields)
- Catalog/metadata utilities (if some catalog step consumes CSV summaries)

CSV fixtures should remain unit-level: **small**, **focused**, and **stable**.

### Assumptions
- Unit tests can load local files from this directory.
- Test code is responsible for parsing CSV deterministically (e.g., explicit delimiter/encoding).

### Constraints / invariants
- Canonical pipeline ordering is preserved conceptually: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- CSV fixtures must not create backdoors around governance (e.g., embedding precise sensitive locations).
- Prefer testing public contracts/transform behavior over internal coupling—unless the unit under test is explicitly internal.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we adopt a formal CSV “schema sidecar” convention (`*.schema.json`) for column/type validation in CI? | TBD | TBD |

### Future extensions
- Add a lightweight index of CSV fixtures once volume grows (e.g., a short table in this README).
- Add CI validation helpers for CSV headers/types where applicable.

## 🗺️ Diagrams

### CSV fixture usage (unit-test level)
~~~mermaid
flowchart LR
  T[Test code] -->|reads| F[CSV fixture file]
  F -->|parse| P[Parser / loader]
  P --> D[Rows / DataFrame / DTO]
  D --> U[Unit under test]
  U --> R[Result]
  R --> A[Assertions]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| CSV fixture files | `.csv` | `tests/unit/fixtures/csv/` | Header/shape checks in tests; optional schema validation if adopted |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Expected outputs | Assertions (code) or `*.expected.csv` | `tests/unit/` or `tests/unit/fixtures/csv/` | Test-specific |

### Sensitivity & redaction
CSV fixtures **must not contain**:
- credentials, API keys, tokens
- PII (names/emails/phone numbers, etc.)
- precise sensitive locations (use synthetic/generalized coordinates)

### Quality signals
Prefer fixtures that are:
- minimal but realistic (reflect real column names/shapes)
- stable (avoid timestamps/random IDs unless fixed)
- diff-friendly (consistent ordering and formatting)

## ✅ CSV fixture conventions

### Naming (recommended)
- Use descriptive names that encode intent and scenario:
  - `etl__census__minimal_valid.csv`
  - `etl__census__missing_required_column.csv`
  - `parse__dates__non_iso_format.csv`
- Prefer `__` as a visual separator for category vs scenario.

### CSV formatting rules (recommended defaults)
To keep fixtures portable across OS/tooling:
- Encoding: **UTF-8** (no BOM).
- Line endings: **LF** (`\n`) preferred.
- Header row: **required** unless the test explicitly targets “no header” behavior.
- Delimiter: comma (`,`) unless a specific delimiter is being tested.
- Quoting: use standard double-quote CSV quoting rules when needed.

> If your unit under test requires different parsing assumptions (e.g., `;` delimiter), encode that intent in the filename and test description.

### Content rules
- Keep fixtures small and reviewable in PRs:
  - Prefer ≤ ~200 rows unless you are testing performance thresholds (rare for unit tests).
- Prefer synthetic/stable values:
  - stable IDs (e.g., `row-0001`)
  - fixed dates (e.g., `1900-01-01`) if exact time is not under test
- Avoid locale-dependent formatting:
  - Use `.` decimal separator
  - Avoid thousands separators (e.g., prefer `10000` not `10,000`)
- Missing values:
  - Prefer empty fields for missing (`...,,...`) unless the behavior under test requires a sentinel (e.g., `NA`).

### Determinism: ordering and normalization
- If row order is **not** under test:
  - write fixtures in a stable sorted order (by an ID column), **or**
  - sort in test code before asserting.
- If row order **is** under test:
  - keep the intended order explicit and documented in the test.

### Geospatial-ish CSVs (lat/lon columns)
If a CSV includes coordinates (even approximate):
- Use **synthetic or generalized** coordinates that do not reveal sensitive locations.
- Keep coordinate field naming consistent *within the fixture set* (e.g., `lon,lat` or `longitude,latitude`) and document it in the test.

### When to add a fixture vs inline CSV in test code
Add a fixture when:
- the table is large enough to harm readability if embedded in the test
- multiple tests share the same input
- you want a durable repro case for a bug/regression

Inline data is fine when:
- it’s short (roughly < ~15 lines) and test-specific

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Unit tests pass (see `tests/unit/README.md`)
- [ ] CSV fixtures are reviewed for determinism and sensitivity
- [ ] (Optional) Header/schema checks are enforced for fixtures modeling stable interfaces

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# Run unit tests:
#   make test
# or:
#   <your-test-runner> tests/unit
#
# Optional: validate CSV headers/types with a helper script (if adopted):
#   <csv-validator> tests/unit/fixtures/csv/*.csv
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
CSV fixtures that are derived from real-world sources (even partial) should be reviewed for:
- licensing compatibility
- sensitivity / sovereignty constraints
- coordinate redaction/generalization rules

### CARE / sovereignty considerations
- If a fixture is based on culturally sensitive material or restricted site data:
  - do not include it here without explicit governance review
  - prefer synthetic stand-ins that preserve structure but not sensitive content

### AI usage constraints
- This README prohibits “infer_sensitive_locations”; do not add CSV fixtures that would enable location inference beyond what’s necessary for testing.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial CSV fixtures README | TBD |

---
Footer refs:
- Parent fixtures rules: `tests/unit/fixtures/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`