---
title: "GitHub Actions Fixture Pack — Story Nodes (README)"
path: ".github/actions/fixtures/story_nodes/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:story-nodes-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-story-nodes-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:story-nodes-readme:v1.0.0"
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

# GitHub Actions Fixture Pack — Story Nodes

## 📘 Overview

### Purpose

This directory contains Story Node Markdown fixtures intended for use by GitHub Actions and other CI checks to:

- validate Story Node conformance,
- regression-test Story Node validators, and
- exercise edge-cases in a deterministic way.

These fixtures are **not** published Story Nodes and must not be referenced by the production UI.

### Scope

| In scope | Out of scope |
|---|---|
| Sample Story Node Markdown used as **test inputs** for CI | Curated/published Story Nodes (live in `docs/reports/story_nodes/`) |
| Valid + intentionally-invalid examples to test validators | Real datasets, catalogs (STAC/DCAT/PROV), or graph fixtures (unless explicitly added elsewhere) |
| Conventions for naming and organizing fixture files | Implementing or modifying validators/actions (belongs under `.github/actions/` code and/or `src/`) |

### Audience

- Contributors adding or updating Story Node validation logic
- Contributors adding new Story Node features (Focus controls, citations, redaction rules) and need fixtures
- CI maintainers

### Definitions

- **Fixture:** A small, deterministic test artifact (here: Markdown) used to verify validators.
- **Story Node:** A provenance-linked narrative artifact consumed by Focus Mode. See template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`.
- **Published Story Node:** A Story Node intended for end users. Canonical home: `docs/reports/story_nodes/` (see Master Guide + v13 blueprint).

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| This README | `.github/actions/fixtures/story_nodes/README.md` | Explains fixture intent + conventions |
| Story Node template (governed) | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Start here for valid fixtures |
| Canonical Story Node home (published) | `docs/reports/story_nodes/` | Not this directory |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + invariants |
| Story Node schema | `schemas/storynodes/` | Used by validators when present |

### Definition of Done

- [ ] Fixtures are **small**, **deterministic**, and **purpose-labeled** (valid vs invalid).
- [ ] Valid fixtures conform to `TEMPLATE__STORY_NODE_V3` structure and include citations/data references as required.
- [ ] Invalid fixtures fail for a **single, intentional reason** (so validator errors stay precise).
- [ ] Fixtures contain **no secrets**, **no PII**, and **no restricted location disclosures** (use synthetic or generalized content).

## 🗂️ Directory Layout

### Where these fixtures live (and where story nodes do not)

KFM’s canonical pipeline ends in Story Nodes and Focus Mode, with Story Nodes being the narrative artifacts consumed by the UI via the API boundary.

This fixture folder exists only to support CI validation of that layer. (See `docs/MASTER_GUIDE_v12.md` and `docs/templates/TEMPLATE__STORY_NODE_V3.md`.)

### Expected file tree (minimum)

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 story_nodes/
            └── 📄 README.md
~~~

### Recommended structure (when fixtures are added)

> Create these subfolders only when you add the first fixture file.

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 story_nodes/
            ├── 📄 README.md
            ├── 📁 valid/
            │   └── 📄 valid__minimal_story_node.md
            └── 📁 invalid/
                └── 📄 invalid__missing_front_matter.md
~~~

## 🧭 Context

### Why these fixtures exist

KFM enforces evidence-based storytelling: Story Nodes and Focus Mode only consume provenance-linked content, and published Story Nodes must validate (front-matter, citations, entity references, redaction).

KFM’s v13 CI mapping lists Markdown protocol validation and Story Node validation among the minimum CI gates for readiness.

These fixtures exist so those checks can be tested and evolved without relying on production story content.

### Constraints and invariants

- **Do not treat fixtures as published content.** Published Story Nodes belong under `docs/reports/story_nodes/`.
- **Determinism:** Fixture files should be stable across runs and diff-friendly.
- **API boundary reminder:** The UI consumes Story Nodes through the API boundary; fixtures must not imply UI → Neo4j direct access.

### Open questions (fill in when wiring CI)

| Question | Owner | Target |
|---|---|---|
| Which workflow/action consumes these fixtures? | CI maintainers | next CI iteration |
| What is the expected CLI entrypoint for Story Node validation? | Contracts/validation owners | next CI iteration |
| Do validators require referenced dataset/entity IDs to resolve during unit tests? | Graph + catalog owners | next CI iteration |

## 🗺️ Diagrams

### CI fixture usage (conceptual)

~~~mermaid
flowchart LR
  A["PR changes<br/>Story Node template / validator"] --> B["GitHub Actions"]
  B --> C["Story Node validator"]
  C --> D["Fixtures<br/>.github/actions/fixtures/story_nodes/**"]
  C --> E["Pass/Fail (CI gate)"]
~~~

## 📦 Data & Metadata

### What a “valid” fixture should include

A valid fixture should be a minimal Story Node that:

- has required YAML front-matter for Story Nodes (per the Story Node v3 template),
- contains at least one cited claim (or at minimum, source bundle rows),
- includes representative “key entities” links (Place/Event/Person/Org) **if** the validator checks them.

If the validator checks Focus Mode hints, include the optional controls:

~~~yaml
focus_layers:
  - "example-layer-id"
focus_time: "1856-01-01/1856-12-31"
focus_center: [-98.0000, 38.0000]
~~~

### What an “invalid” fixture should test

Keep invalid fixtures intentionally narrow. Examples:

- Missing Story Node front-matter section
- Missing citations / source bundle entries
- Broken entity references (if validator checks graph linkage)
- Redaction/sensitivity violation (only with synthetic data)

## 🌐 STAC, DCAT & PROV Alignment

Fixtures may include fake-but-well-formed IDs to test link structure (e.g., `stac_item_id`, `dcat_dataset_id`, `prov_activity_id`)—but **do not** require real catalog assets unless the validator explicitly resolves them in CI.

If ID resolution is required, pair Story Node fixtures with corresponding catalog/graph fixtures in their own fixture packs (location not defined here).

## 🧱 Architecture

### How Story Nodes are served (real system)

- Story Nodes are consumed by the UI through the API boundary (see `src/server/` and contracts in `src/server/contracts/`).
- The UI must not connect to Neo4j directly.
- Focus Mode consumes provenance-linked context only.

This fixture directory exists to ensure that the Story Node layer remains compliant with those invariants.

## 🧠 Story Node & Focus Mode Integration

### What fixtures should cover over time

As validators mature, consider adding fixtures that cover:

- Focus Mode controls: `focus_layers`, `focus_time`, `focus_center`
- “AI insight” opt-in fields and uncertainty metadata (if supported)
- Multiple sources and mixed evidence types (documents + map layers)
- Redaction/generalization markers for sensitive locations

## 🧪 Validation & CI/CD

### Suggested validation contract (what fixtures enable)

- Valid fixtures **must pass**
- Invalid fixtures **must fail** with stable, specific error messages
- Validators should fail deterministically when the relevant roots exist and the content is invalid

### Running locally

Not confirmed in repo:

- Add the local command used by the Story Node validator here (e.g., `npm run validate:storynodes` or `python tools/validate_storynodes.py`).

## ⚖ FAIR+CARE & Governance

### Governance review triggers (fixtures)

- If any fixture includes sensitive knowledge patterns (even synthetic), request review.
- If fixtures are used to test AI narrative behavior, ensure it remains opt-in and labeled.

### Sovereignty safety

- Never include restricted coordinates or culturally sensitive knowledge in fixtures.
- Prefer synthetic geometries and generalized locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for Story Node fixtures | TBD |

---

Footer refs:

- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
