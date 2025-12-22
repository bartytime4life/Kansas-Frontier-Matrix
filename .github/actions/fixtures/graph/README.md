---
title: "Graph Fixtures for GitHub Actions"
path: ".github/actions/fixtures/graph/README.md"
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

doc_uuid: "urn:kfm:doc:ci:fixtures:graph-readme:v1.0.0"
semantic_document_id: "kfm-ci-fixtures-graph-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:fixtures:graph-readme:v1.0.0"
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

# Graph Fixtures for GitHub Actions

## 📘 Overview

### Purpose

This directory holds small, deterministic graph fixtures intended for CI workflows and local smoke tests that exercise the KFM Graph stage.

These fixtures are **not** production data. They are intentionally minimal so they can be loaded quickly and repeatedly inside GitHub Actions.

### Scope

| In Scope | Out of Scope |
|---|---|
| Synthetic or minimally redacted node/edge data used for tests (CSV/JSON), plus optional Cypher seed scripts | Real source datasets, large exports, or anything that would belong under `data/` |
| Fixture manifests describing expected node/edge counts and stable IDs | Secrets, credentials, API keys, or private endpoints |
| Deterministic examples that validate common labels/relations and traversals | Any fixture that requires network access to execute |

### Audience

- Primary: CI/workflow authors and graph pipeline maintainers.
- Secondary: API and UI developers who need stable graph test data.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc: fixture, graph ingest, nodes, relationships, Cypher, deterministic.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/graph/README.md` | CI maintainers | Conventions + usage |
| Fixture root | `.github/actions/fixtures/graph/` | CI maintainers | One subfolder per fixture |
| Graph implementation | `src/graph/` | Graph maintainers | Canonical graph build/ingest code |
| Production graph import assets | `data/graph/` | Data/Graph maintainers | Canonical import CSVs and post-import scripts |

### Definition of done

- [ ] Front-matter complete and valid
- [ ] Fixtures are deterministic and small enough for CI
- [ ] No secrets, PII, or sensitive locations are included
- [ ] Each fixture is self-contained and documented
- [ ] Validation steps below are repeatable in CI and locally

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/graph/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Composite actions and action helpers |
| Workflows | `.github/workflows/` | CI pipelines that may consume fixtures |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Graph data exports | `data/graph/` | Import CSVs and optional post-import scripts |
| Tests | `tests/` | Unit/integration tests that may load fixtures |

### Suggested fixture layout

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 graph/
            ├── 📄 README.md
            └── 📁 <fixture_name>/
                ├── 📄 manifest.yml
                ├── 📄 nodes.csv
                ├── 📄 relationships.csv
                └── 📄 seed.cypher
~~~

Notes:

- `<fixture_name>` should be short, kebab-case, and describe the scenario being tested.
- File names above are examples; fixtures may use multiple node/edge files if that better matches the ingest tooling.

## 🧩 Fixture conventions

### Determinism requirements

- Prefer stable, human-readable IDs (e.g., `place:001`, `event:042`) over random UUIDs.
- Keep input ordering stable (sort by ID where practical).
- Avoid time-dependent values unless the test explicitly validates time logic.

### Content requirements

- Keep fixtures synthetic when possible.
- If real-world names are needed for coverage, keep them generic and avoid sensitive or culturally protected locations unless explicitly approved under governance.

### Manifest recommendations

Each fixture should include a small manifest file (e.g., `manifest.yml`) that documents:

- What the fixture is testing
- Expected node and relationship counts
- Any invariants the test should assert (e.g., “each Event links to a Document via `mentions`”)

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Graph ingest succeeds using the fixture
- [ ] Graph integrity checks for expected labels/relations
- [ ] Any workflow or test that depends on the fixture asserts expected counts/IDs

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) list available fixtures
ls .github/actions/fixtures/graph

# 2) run graph-related tests
# pytest -k graph

# 3) run a graph ingest smoke test, pointing at a fixture directory
# python -m <your-graph-ingest-module> --fixture .github/actions/fixtures/graph/<fixture_name>
~~~

### Telemetry signals

Not applicable for fixtures. If a workflow records fixture load timings or counts, document that in the workflow and keep logs non-sensitive.

## 🧠 Story Node & Focus Mode Integration

Fixtures are CI-only artifacts and do not surface in the user-facing Story Node or Focus Mode UX by default.

If a fixture is ever promoted for demos or UI development, it must still follow the provenance-linked narrative rule used elsewhere in KFM: every surfaced claim must trace to a source artifact and identifiers.

## ⚖ FAIR+CARE & Governance

### Review gates

Any fixture that includes real-world sensitive information, culturally protected sites, or detailed coordinates requires human review against:

- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations

- Keep fixtures synthetic and minimal.
- Avoid including any data that could reasonably be interpreted as restricted site information.

### AI usage constraints

- AI transforms are allowed only as declared in the front-matter.
- Do not use AI to infer or generate sensitive locations or policies.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for graph fixtures | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
