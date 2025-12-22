---
title: "KFM GitHub Actions — Local Actions"
path: ".github/actions/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:local-actions-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-local-actions-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:local-actions-readme:v1.0.0"
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

# KFM GitHub Actions — Local Actions

## 📘 Overview

### Purpose

- Provide **repo-local, reusable GitHub Actions** under `.github/actions/` that implement CI “gates” and helper steps used by workflows in `.github/workflows/`.
- Keep validation logic **consistent, versioned with the repository**, and aligned with KFM’s governed pipeline and contract boundaries.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local actions under `.github/actions/` and how to structure/use them | Implementing or changing workflows under `.github/workflows/` |
| Guidance for adding new composite actions for validation gates | Defining new governance policy (see `docs/governance/*`) |
| CI gate mapping to KFM subsystems/contracts | Changing the KFM pipeline ordering or subsystem boundaries |

### Audience

- Primary: CI maintainers and repository maintainers.
- Secondary: Contributors adding or modifying data, schemas, story nodes, API contracts, or UI registry config.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Workflow**: A GitHub Actions workflow YAML file under `.github/workflows/`.
  - **Local action**: An action defined in this repo under `.github/actions/<action-name>/`.
  - **Gate**: A validation step that fails CI if a required contract/invariant is violated.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/README.md` | Repo maintainers | Documents the local actions area |
| Workflows | `.github/workflows/` | CI maintainers | Call into local actions |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline + minimum gates |
| Governance | `docs/governance/` | Governance owners | Ethics + sovereignty rules |
| Schemas | `schemas/` | Contracts owners | Canonical validation targets *(not confirmed in repo)* |
| Story Nodes | `docs/reports/story_nodes/` | Story owners | Canonical story-node root *(not confirmed in repo)* |
| API contracts | `src/server/contracts/` | API owners | Canonical API contract location *(not confirmed in repo)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Mermaid diagram renders (no parse errors)
- [ ] CI gates list aligns with `docs/MASTER_GUIDE_v12.md`
- [ ] Local action layout guidance is clear and repo-safe (no secrets/PII, deterministic expectations)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | CI entrypoints (PR, push, scheduled) |
| Local actions | `.github/actions/` | Composite/local actions used by workflows |
| Documentation | `docs/` | Canonical governed docs (Master Guide, templates, policies) |
| Schemas | `schemas/` | Contract schemas for STAC/DCAT/PROV/storynodes/ui/telemetry *(not confirmed in repo)* |
| Pipelines | `src/pipelines/` | ETL + transformations |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Generated STAC/DCAT/PROV artifacts *(some roots may be optional depending on repo state)* |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API boundary | `src/server/` | Canonical API access layer *(not confirmed in repo)* |
| UI | `web/` | Canonical UI app *(not confirmed in repo)* |

### Expected local action layout

~~~text
📁 .github/
├── 📁 workflows/
│   └── 📄 <workflow>.yml
└── 📁 actions/
    ├── 📄 README.md
    ├── 📁 <action-name>/
    │   ├── 📄 action.yml
    │   ├── 📄 README.md
    │   └── 📁 scripts/                 (optional; keep repo-local + deterministic)
    └── 📁 <another-action-name>/
        ├── 📄 action.yml
        └── 📄 README.md
~~~

---

## 🧭 Context

### Why local actions?

Local actions are a maintainability and governance tool:

- One gate → one implementation → reused everywhere.
- When a contract changes (schema, story node rules, API contract version), the CI logic changes **in one place**.

### When to create a new local action

Create a local action when:

- The same steps are needed in more than one workflow/job.
- The steps implement a **KFM contract** (schema validation, story node validation, API contract tests, etc.).
- You need to pin the logic to the repository (not an external marketplace action).

### Repo drift / optional roots

Some canonical roots may not exist in a given repository snapshot (“not confirmed in repo”). CI should:

- **Skip** validations that depend on optional roots when those roots are absent.
- **Fail deterministically** when those roots are present but invalid. *(This is a KFM v13 redesign principle and is safe to apply as a CI rule of thumb.)*

---

## 🗺️ Diagrams

### Workflows → local actions → gates

> Mermaid rendering note:
> - Avoid unquoted `*` (wildcards) inside node labels.
> - Prefer quoted labels: `NODE["text with / and ( )"]`.

~~~mermaid
flowchart LR
  PR["Pull Request / Push"] --> WF[".github/workflows/ (workflow files)"]
  WF --> ACT[".github/actions/ (local actions)"]

  ACT --> G1["Markdown protocol validation"]
  ACT --> G2["Schema validation (STAC/DCAT/PROV + Story Node schemas)"]
  ACT --> G3["Graph integrity tests"]
  ACT --> G4["API contract tests (OpenAPI/GraphQL)"]
  ACT --> G5["UI layer registry schema checks"]
  ACT --> G6["Security + sovereignty scans (as applicable)"]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Repository checkout | GitHub Actions runner | Includes changed files in PR/push |
| Schemas, contracts, configs | Repo paths (`schemas/`, `src/server/contracts/`, `web/…`) | May be optional roots depending on repo state |
| Data artifacts | `data/**` | Validators should treat outputs as *data*, not code |

### Outputs

| Output | Where | Notes |
|---|---|---|
| Pass/fail status | GitHub Checks | Blocks merge when required gates fail |
| Logs | GitHub Actions logs | Keep non-sensitive and actionable |
| Optional reports/artifacts | Workflow artifacts | Use only when necessary; avoid leaking restricted info |

---

## 🌐 STAC, DCAT & PROV Alignment

Local actions in this directory may validate:

- **STAC** collections/items (`data/stac/**`) against `schemas/stac/**` *(paths not confirmed in repo)*.
- **DCAT** dataset records (`data/catalog/dcat/**`) against `schemas/dcat/**` *(paths not confirmed in repo)*.
- **PROV** bundles (`data/prov/**`) against `schemas/prov/**` *(paths not confirmed in repo)*.

If your action validates any of the above, it must be:

- Deterministic (same inputs → same results).
- Strict about schema errors.
- Careful about sovereignty rules (restricted locations, culturally sensitive knowledge).

---

## 🧱 Architecture

### How workflows reference local actions

In workflow YAML, reference local actions via a relative path:

~~~yaml
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Example local action usage
      - name: Run schema validation
        uses: ./.github/actions/<action-name>
        with:
          # define inputs in the action.yml
          target: "schemas/"
~~~

### Action types supported here

- **Composite actions** (`runs: using: composite`) are recommended for repo-local validation glue.
- Docker/JS actions are possible but should be justified (complex runtime needs, performance, etc.).

### Action documentation expectations

Each local action directory should include:

- `action.yml` (required)
- `README.md` explaining:
  - what it validates
  - inputs/outputs
  - what constitutes failure
  - how to reproduce locally (if applicable)

---

## 🧠 Story Node & Focus Mode Integration

If an action validates Story Nodes, it should enforce:

- front-matter validity (required keys, versioning)
- citations/provenance-linking rules
- entity reference resolution (IDs/links resolve)
- redaction/generalization compliance for restricted material

This supports the KFM invariant that **published narratives must not be unsourced** and that Focus Mode surfaces **provenance-linked** content only.

---

## 🧪 Validation & CI/CD

### Minimum CI gates

The Master Guide defines a baseline set of CI gates for “v12 contributions” that workflows should enforce via local actions and/or workflow steps:

- [ ] Markdown protocol validation (template + front matter + links)
- [ ] Schema validation (STAC/DCAT/PROV + story node schemas)
- [ ] Graph integrity tests
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI layer registry schema checks
- [ ] Security + sovereignty scanning where applicable

### CI behavior principle

- If a gate depends on a root that does not exist in the current repo snapshot, the workflow should **skip** that gate.
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands/scripts.

# 1) Markdown protocol checks
# <TBD>

# 2) Schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
# <TBD>

# 3) Graph integrity tests
# <TBD>

# 4) API contract tests
# <TBD>

# 5) Security + sovereignty scanning
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI gate results | GitHub Actions | `docs/telemetry/` + `schemas/telemetry/` *(not confirmed in repo)* |

---

## ⚖ FAIR+CARE & Governance

### Review gates

- CI maintainers approve changes to `.github/workflows/` and `.github/actions/`.
- Governance owners review anything that:
  - changes sovereignty handling or redaction behavior
  - affects handling of culturally sensitive or restricted locations
  - introduces new automated inference over sensitive content

### CARE / sovereignty considerations

- CI must not introduce leakage of restricted coordinates or culturally sensitive material.
- Any scans must treat restricted outputs as sensitive and avoid publishing them in public logs/artifacts.

### AI usage constraints

- Ensure action logic does **not** “infer sensitive locations” or generate new policy.
- If an action uses AI tooling (not typical for CI), it must be opt-in and governance-reviewed.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for local actions | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
