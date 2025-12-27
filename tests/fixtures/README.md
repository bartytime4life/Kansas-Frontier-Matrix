---
title: "KFM Tests Fixtures — README"
path: "tests/fixtures/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:tests:fixtures:readme:v1.0.0"
semantic_document_id: "kfm-tests-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:fixtures:readme:v1.0.0"
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

# KFM Tests Fixtures — README

> **Purpose (required):** Define how to create, store, and maintain **small, synthetic** fixtures under `tests/fixtures/` so KFM tests remain deterministic and aligned to the canonical pipeline and CI validation behavior.

## 📘 Overview

### Purpose

- Provide a canonical home for **tiny, synthetic** inputs used by unit/integration/contract tests.
- Encode “contract expectations” for:
  - STAC/DCAT/PROV schema & integrity tests,
  - Graph ingest/import tests,
  - API request/response contract tests,
  - (optionally) UI registry and Story Node validator tests.
- Prevent silent drift by keeping fixtures **stable, diffable, and governance-safe**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Small synthetic fixtures used by tests (JSON/GeoJSON/CSV, tiny binaries) | Raw source data snapshots (belongs in `data/<domain>/raw/`) |
| Minimal/edge/invalid fixtures for schema validation (STAC/DCAT/PROV/etc.) | Full production catalogs or “golden dumps” of `data/stac/**` |
| Contract fixtures for API boundary and UI registries | Secrets/credentials, PII, or restricted locations (unless generalized + approved) |
| Fixture notes/metadata that describe “what this tests” | Defining new governance policy text or bypassing review gates |

### Audience

- **Primary:** Contributors adding/changing pipelines, catalogs, schemas, graph ingestion, API contracts, or UI registries.
- **Secondary:** Maintainers reviewing PRs and debugging CI failures.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **fixture**, **golden file**, **deterministic**, **idempotent**, **contract test**, **schema validation**, **provenance**, **redaction**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Architectural ordering + constraints |
| Tests taxonomy + CI behavior contract | `tests/README.md` | KFM Core | Determinism + “skip vs fail” semantics |
| Governed markdown structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used by this README |
| Schemas (STAC/DCAT/PROV/UI/telemetry) | `schemas/` | Data/Platform | Validators should reference these |
| Canonical catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Data/Platform | Evidence + lineage (not fixtures) |
| Pipelines | `src/pipelines/` | Data Eng | Deterministic transforms |
| Graph build + ontology bindings | `src/graph/` | Graph Eng | Graph integrity tests |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(legacy; not confirmed in repo)* | API Eng | UI must consume via API |
| UI | `web/` | Frontend | Never reads Neo4j directly |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Published artifacts live here |

### Definition of done (for this document)

- [ ] Front-matter complete and `path` matches file location
- [ ] Fixture responsibilities + placement rules documented
- [ ] Recommended sub-tree documented (and marked “not confirmed” where applicable)
- [ ] Governance/sensitivity constraints included
- [ ] Repo lint / markdown lint run (CI or local)
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `tests/fixtures/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Tests | `tests/` | Unit/integration/contract/e2e tests + fixtures |
| Schemas | `schemas/` | JSON Schemas, telemetry schemas, contract validation |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Canonical STAC/DCAT/PROV evidence artifacts |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import constraints |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(legacy; not confirmed in repo)* | Contracts, redaction, access control |
| UI | `web/` | React/Map UI (no direct graph reads) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Tools | `tools/` | Ops scripts and developer utilities |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
├── 📄 README.md
└── 📁 fixtures/
    ├── 📄 README.md
    ├── 📁 catalogs/
    │   ├── 📁 stac/
    │   │   ├── 📁 minimal_valid/
    │   │   ├── 📁 edge_cases/
    │   │   └── 📁 invalid/
    │   ├── 📁 dcat/
    │   │   ├── 📁 minimal_valid/
    │   │   ├── 📁 edge_cases/
    │   │   └── 📁 invalid/
    │   └── 📁 prov/
    │       ├── 📁 minimal_valid/
    │       ├── 📁 edge_cases/
    │       └── 📁 invalid/
    ├── 📁 graph/
    │   └── 📁 import_samples/
    ├── 📁 api/
    │   ├── 📁 requests/
    │   └── 📁 responses/
    ├── 📁 ui/
    │   └── 📁 registry/
    ├── 📁 assets/
    │   └── 📁 tiny/
    └── 📁 manifests/
        └── (optional per-fixture descriptors)
~~~

---

## 🧭 Context

### Background

KFM’s canonical ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

Fixtures exist to make subsystem contracts **testable, reproducible, and auditable** without requiring “full data” replays.

### Constraints / invariants (fixtures must respect)

- **Determinism (tests + fixtures):**
  - no network calls by default,
  - no reliance on local machine state,
  - no non-pinned randomness (seed if needed).
- **Deterministic CI behavior (“skip vs fail”):**
  - if an optional fixture root is **absent**, CI may **skip** that validation,
  - if the root is **present** but invalid, CI must **fail deterministically**.
- **No secrets/PII:** fixtures must not contain secrets, tokens, credentials, or personally identifying information.
- **API boundary preserved:** UI tests must not query Neo4j directly; they consume only API payloads/contracts.
- **No duplicate canonical homes:** fixtures are not a second copy of `data/**` or `schemas/**`.

### Assumptions

- The repo’s exact test runner(s) and commands are **not confirmed in repo**; this README focuses on placement and behavior rather than tooling.

---

## 🗺️ Diagrams

### Fixtures as contract anchors

~~~mermaid
flowchart LR
  F["tests/fixtures/**"] --> T["tests/** (unit · integration · contract · e2e)"]
  T --> V["CI gates (schema · contract · security · sovereignty)"]
  V --> C["Catalog outputs (data/stac · data/catalog/dcat · data/prov)"]
  C --> G["Graph (src/graph)"]
  G --> A["API boundary (src/server)"]
  A --> U["UI (web/)"]
  U --> S["Story Nodes (docs/reports/story_nodes)"]
  S --> FM["Focus Mode (provenance-linked)"]
~~~

---

## 📦 Data & Metadata

### Fixture design principles

1. **Small and synthetic:** fixtures are “toy” data meant to exercise logic and schemas—not a dataset mirror.
2. **Stable identifiers:** use stable IDs and filenames so snapshots don’t churn across PRs.
3. **Deterministic timestamps:** prefer fixed datetimes; avoid ingest-time “now()” fields in fixtures.
4. **License-safe:** include only open-licensed or synthetic content; add attribution when applicable.
5. **Explicit sensitivity:** if a fixture includes any location or cultural knowledge, it must be generalized/redacted and reviewed.

### Recommended per-fixture metadata

Not confirmed in repo, but recommended for non-trivial fixtures:

- A short `README.md` beside the fixture explaining:
  - what contract it exercises,
  - what should pass/fail,
  - any governance notes.

Optionally, a tiny manifest file:

~~~yaml
# not confirmed in repo — example only
fixture_id: "kfm.fixture.stac.minimal_valid.v1"
type: "stac_item"
expected: "pass"        # pass | fail
schemas:
  - "schemas/stac/item.schema.json"
notes: "Minimal valid STAC Item with KFM provenance hooks."
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC fixtures

Use three buckets to keep CI behavior explicit:

- `minimal_valid/` — MUST pass validation (baseline contract)
- `edge_cases/` — MUST pass while exercising rare/optional fields
- `invalid/` — MUST fail (to prevent “silent regressions”)

**KFM provenance hooks (recommended for valid STAC fixtures):**

- `properties.kfm:provenance_ref` — pointer to a PROV Activity/Entity bundle
- `properties.kfm:lineage_sha` — commit that produced the artifact
- `properties.kfm:telemetry_ref` — run/telemetry identifier

**Link + size discipline (recommended):**

- Avoid remote links where possible.
- If a fixture includes `http(s)` assets/links, tests should:
  - check that links resolve,
  - enforce a small size budget (e.g., ≤ 5 MB per asset).

### DCAT fixtures

- Mirror the same `minimal_valid/ | edge_cases/ | invalid/` buckets.
- Ensure dataset/distribution records include explicit license and publisher/contact fields consistent with governance.

### PROV fixtures

- Mirror the same `minimal_valid/ | edge_cases/ | invalid/` buckets.
- Include the minimal PROV triad:
  - `prov:Activity` (the run),
  - `prov:Entity` (the produced artifact),
  - `prov:Agent` (the pipeline or actor).
- Keep identifiers stable and linkable from STAC/DCAT fixtures (e.g., via `kfm:provenance_ref`).

---

## 🧱 Architecture

### Where fixtures fit

Fixtures support tests at each contract boundary:

- **ETL/pipelines**: parser/normalizer unit tests (no network by default)
- **Catalogs**: STAC/DCAT/PROV schema + integrity checks
- **Graph**: import schema and ontology binding tests
- **API boundary**: request/response contract tests + redaction behaviors
- **UI**: registry schema checks + accessibility gates
- **Story**: Story Node validator tests (published nodes remain in `docs/reports/story_nodes/`)

### Non-negotiable boundary

The UI layer (`web/`) must never read Neo4j directly; fixtures used by UI tests should be API payloads, not graph queries.

---

## 🧠 Story Node & Focus Mode Integration

### Fixture role in narrative safety

- Fixtures may be used to test Story Node validators and “provenance-linked narrative” rules.
- **Do not** store published Story Nodes under `tests/fixtures/`. Published nodes live under `docs/reports/story_nodes/`.

### Suggested (optional) fixture pattern

Not confirmed in repo:

- `tests/fixtures/story_nodes/` may hold **non-published** sample nodes used only by validators (clearly marked as test-only).

---

## 🧪 Validation & CI/CD

### Deterministic behavior contract

- If `tests/fixtures/` (or any sub-root) is absent, validations may **skip**.
- If present but invalid, CI must **fail deterministically**.

### Recommended validation checks for fixtures

- Schema validation for any STAC/DCAT/PROV fixtures present
- “Invalid fixture must fail” assertions for `invalid/` buckets
- Secret/PII scanning
- Sovereignty/sensitivity checks (especially for location data)

### Local reproduction (placeholders)

~~~bash
# not confirmed in repo — replace with repo’s actual commands
# make test
# make validate-schemas
# make validate-fixtures
~~~

### Optional: supply-chain / attestation fixtures

If/when the repo enforces signed provenance:

- Store **valid and invalid** DSSE envelopes and provenance predicates under a dedicated fixture folder (e.g., `tests/fixtures/attestations/`) to test fail-closed promotion gates.

---

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when fixtures introduce:

- new sensitive locations or culturally sensitive knowledge (even as “test data”),
- new external data sources or licenses,
- new public-facing schema fields.

### CARE / sovereignty considerations

- Treat fixtures as publishable artifacts: they must not leak restricted locations or sensitive knowledge.
- When in doubt, generalize or redact geometries and document the choice.

### AI usage constraints

AI transform permissions/prohibitions are defined in front-matter; they must remain aligned with repo governance.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial fixtures README scaffold | TBD |

---

Footer refs (do not remove):
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

---
