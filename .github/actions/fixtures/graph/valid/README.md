---
title: "Graph Fixtures — Valid (CI Fixtures)"
path: ".github/actions/fixtures/graph/valid/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:graph:valid-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-graph-valid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:graph:valid-readme:v1.0.0"
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

# Graph Fixtures — Valid

## 📘 Overview

### Purpose
- Provide “known-good” graph fixture sets used by CI (and optionally local tooling) to confirm the graph validation/import pipeline accepts canonical valid examples.
- Keep fixture sets small, deterministic, and aligned to the project’s ontology and provenance expectations.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal, deterministic fixture sets that **must validate successfully** | Production-scale datasets |
| Synthetic / anonymized examples only | Any secrets, credentials, tokens |
| Ontology-aligned labels/edges and referential integrity | Real sensitive locations, private data, culturally restricted detail |
| Optional provenance stubs (STAC/DCAT/PROV IDs) | Unverifiable provenance claims |

### Audience
- Primary: Graph/ontology contributors and CI maintainers.
- Secondary: Pipeline/API/UI contributors adding or debugging integration tests.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **fixture**, **fixture set**, **manifest**, **referential integrity**, **ontology**, **provenance stub**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Valid fixture sets | `.github/actions/fixtures/graph/valid/<fixture_slug>/` | Graph maintainers | Each folder is expected to validate “green”. |
| Fixture manifest (recommended) | `<fixture_slug>/manifest.(yml|yaml|json)` | Fixture author | Declares intent + provenance stubs + file names. |
| Node/edge data | `<fixture_slug>/*` | Fixture author | Prefer text-based formats; keep minimal. |
| Validation outputs | (CI-generated) | CI | Location is workflow-defined. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory layout + “what belongs here” is explicit
- [ ] Safety constraints (no secrets/PII/sensitive locations) are explicit
- [ ] Guidance is tooling-agnostic (does not assume a specific script name unless linked)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/graph/valid/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI fixtures root | `.github/actions/fixtures/graph/` | Graph fixtures consumed by CI and/or local checks |
| Valid fixtures | `.github/actions/fixtures/graph/valid/` | Fixture sets that **must pass** validation |
| Invalid fixtures (optional) | `.github/actions/fixtures/graph/invalid/` | Fixture sets that **must fail** validation |
| Graph subsystem | `src/graph/` | Ontology bindings, constraints, graph build logic |
| Graph documentation | `docs/graph/` | Ontology + migrations + constraints docs (if present) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Machine-readable metadata + lineage bundles |
| Graph import exports (non-fixture) | `data/graph/` (e.g., `data/graph/csv/`) | Real graph import artifacts |

### Folder shape (example)
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 graph/
            └── 📁 valid/
                ├── 📄 README.md
                └── 📁 <fixture_slug>/
                    ├── 📄 manifest.yml
                    ├── 📄 nodes.csv
                    └── 📄 relationships.csv
~~~

## 🧭 Context

### Why “valid” fixtures matter
- CI needs deterministic, minimal examples to verify the graph layer accepts canonical structures.
- These fixtures are a **contract**: everything under `valid/` should pass graph validation consistently.

### Relationship to the KFM pipeline
- The graph layer sits downstream of catalogs and upstream of API/UI.
- Fixtures should not encourage bypassing the API boundary: UI must never query the graph directly.

### What belongs in a valid fixture set
- Minimal node + relationship data that:
  - parses cleanly,
  - respects ontology label/type expectations,
  - maintains referential integrity (no dangling edges),
  - uses stable IDs (deterministic, no randomness).

### What must never be in fixtures
- Secrets, credentials, tokens, private keys.
- Real personally identifying information (PII).
- Sensitive or restricted location detail (use synthetic/generalized stand-ins).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[valid/<fixture_slug>] --> B[Graph validator(s)]
  B -->|pass| C[CI continues]
  B -->|fail| D[CI fails]
~~~

~~~mermaid
flowchart LR
  ETL --> CATS["STAC/DCAT/PROV"]
  CATS --> GRAPH["Neo4j Graph"]
  GRAPH --> API["API boundary"]
  API --> UI["UI"]
  UI --> SN["Story Nodes"]
  SN --> FM["Focus Mode"]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Fixture manifest (recommended) | YAML/JSON | repo | schema lint (if available) |
| Nodes | CSV/JSON | repo | parse + constraint checks |
| Relationships | CSV/JSON | repo | referential integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation result | exit code | CI logs | non-zero on failure |
| Report artifact (optional) | JSON/TXT | CI artifacts | workflow-defined |

### Sensitivity & redaction
- Fixtures here are intended to be **public/open** samples.
- If you need to model restricted data behaviors, use **synthetic placeholders** and document redaction behavior in governed docs (not in CI fixtures).

## 🌐 STAC, DCAT & PROV Alignment

### Goal
- Keep fixtures compatible with the system’s provenance-first expectations, even if you only include stub identifiers.

### Recommended manifest provenance fields
- `stac_item_ids`: list of referenced STAC Item IDs (may be empty)
- `dcat_dataset_ids`: list of referenced DCAT dataset identifiers (may be empty)
- `prov_activity_ids`: list of referenced PROV activity/run IDs (may be empty)

### Minimum expectation
- Do not claim provenance that does not exist in-repo.
- Prefer empty arrays over unverifiable identifiers.

## 🧱 Architecture

### Fixture set contract
A fixture set is considered “valid” when all of the following are true:

1. All fixture files are parseable by the graph validation/import tooling.
2. Node identifiers are unique and stable.
3. Every relationship references existing node identifiers.
4. Labels and relationship types conform to the ontology/constraints.
5. Optional provenance fields are well-formed and non-sensitive.

### Naming conventions (recommended)
- Folder name: `<domain>__<scenario>__v<semver>`
- Keep fixtures small and purpose-built (prefer multiple small fixtures over one large fixture).

### Example manifest (recommended)
~~~yaml
fixture_id: "historical__minimal_place_event__v1.0.0"
description: "Minimal valid fixture: Place + Event + Document with provenance stubs."
expected_valid: true

files:
  nodes: "nodes.csv"
  relationships: "relationships.csv"

provenance:
  stac_item_ids: []
  dcat_dataset_ids: []
  prov_activity_ids: []

notes:
  - "Synthetic identifiers only."
  - "No sensitive locations."
~~~

### Do not break rules
- Do not change fixture semantics without updating whatever consumes it in CI/tests.
- Do not add large binaries; keep fixtures text-based and reviewable.
- Do not embed real sensitive location detail or personal data.

## 🧠 Story Node & Focus Mode Integration
- These fixtures are primarily graph-level, but should remain compatible with:
  - provenance-linked Story Nodes, and
  - Focus Mode’s “no unsourced narrative” requirement.
- If a fixture includes narrative-oriented nodes (e.g., `Document`), prefer:
  - fixture-local citations (if present), or
  - empty provenance fields (rather than unverifiable claims).

## 🧪 Validation & CI/CD

### How to add a new valid fixture
1. Create a new folder: `valid/<fixture_slug>/`
2. Add the minimum required files for your graph validator/importer.
3. Add a `manifest.(yml|yaml|json)` describing intent + provenance stubs.
4. Run the same validation step used by CI against the fixture folder.

### Local validation (example)
~~~bash
# Example only — adjust to repo tooling:
./tools/graph/validate-fixtures --path .github/actions/fixtures/graph/valid
~~~

### Expected CI behavior
- Every fixture under `valid/` must pass.
- If any valid fixture fails, the CI job should fail.

## ⚖ FAIR+CARE & Governance

### Review gates
- Reviewers should include:
  - Graph/ontology owners (for label/edge model changes)
  - CI maintainers (for fixture consumption and stability)

### CARE / sovereignty considerations
- Do not encode restricted or culturally sensitive location detail in CI fixtures.
- Use synthetic/generalized placeholders and document the rationale if a sensitive domain is being modeled.

### AI usage constraints
- Respect `ai_transform_permissions` / `ai_transform_prohibited` in front matter.
- Do not use AI to infer sensitive locations from partial or ambiguous data.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for valid graph fixtures | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

