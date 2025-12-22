---
title: "KFM Ops Tools"

path: "tools/ops/README.md"

version: "v0.1.0"

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


doc_uuid: "urn:kfm:doc:tools:ops:readme:v0.1.0"

semantic_document_id: "kfm-tools-ops-readme-v0.1.0"

event_source_id: "ledger:kfm:doc:tools:ops:readme:v0.1.0"

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


# KFM Ops Tools


## 📘 Overview


### Purpose

- This README governs the **location, intent, and safety expectations** for operational tooling under `tools/ops/`.

- `tools/ops/` exists to make it easy to **run, validate, package, and operate** KFM *without violating* core contracts:
  - canonical pipeline ordering
  - provenance-first behavior
  - schema/contract validation before publishing

- This directory is also the **in-repo landing zone** for “cloud deployment specifics” that design/architecture docs intentionally keep out-of-scope (those details should live here and/or in a dedicated ops repo).


### Scope

| In Scope | Out of Scope |
|---|---|
| Ops runbooks (step-by-step, human-invoked) | Secrets or credentials committed to git |
| Safe automation scripts for local/dev/prod operations | Editing core pipeline logic (belongs in `src/`) |
| Environment templates and non-secret configs | Treating the UI as a direct Neo4j client (API layer is the boundary) |
| Deployment manifests and infra helpers (if kept in-repo) | Storing datasets or derived outputs under `tools/` |
| Validation entrypoints (schema checks, smoke tests) | Ad hoc “one-off” commands with irreversible side-effects |


### Audience

- Primary: KFM maintainers and operators (DevOps / platform / release engineering)
- Secondary: contributors who need a safe place to add operational helpers


### Definitions

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Ops Script**: a repeatable command intended for automation; must be safe-by-default.
  - **Runbook**: a human-readable procedure with prerequisites, steps, rollback, and verification.
  - **Manifest**: a structured, versioned description of an environment or release (no secrets).
  - **Safety-by-default**: “dry-run first” and explicit confirmation/flags for destructive actions.
  - **Contract boundary**: UI consumes APIs; the API is the access boundary to graph/data.


### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + repo canonical locations |
| v13 redesign blueprint | `docs/architecture/` (not confirmed in repo) | Maintainers | Notes where deployment specifics should live (`tools/` and/or ops repo) |
| Markdown protocol | `docs/standards/` (not confirmed in repo) | Maintainers | Governs front-matter + structure; enforced in CI |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | This README follows the governed structure |
| Security policy | `.github/SECURITY.md` + `docs/security/` (not confirmed in repo) | Maintainers | No secrets in repo; follow disclosure + hardening rules |
| Telemetry specs | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) | Maintainers | Where ops/observability signals are defined |


### Definition of done

- [ ] Front-matter complete + valid
- [ ] Scope clearly states what belongs in `tools/ops/`
- [ ] Any example commands are labeled as **placeholders** unless verified
- [ ] Safety expectations documented (dry-run, rollback, logging)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No secrets, tokens, private keys, or sensitive locations are embedded in examples


## 🗂️ Directory Layout


### This document

- `path`: `tools/ops/README.md`


### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Ops tooling | `tools/ops/` | Runbooks + scripts for operations and deployment |
| Data domains | `data/` | Raw/work/processed outputs and catalogs |
| Documentation | `docs/` | Canonical governed docs, standards, templates |
| Pipelines | `src/pipelines/` | ETL + catalog builders (implementation) |
| Graph | `src/graph/` | Ontology bindings, migrations, graph build |
| APIs | `src/api/` | API layer implementation (contract boundary) |
| UI | `src/web/` + `web/` | Frontend app + UI configs (paths not confirmed) |
| Schemas | `schemas/` | Machine-validated contracts (STAC/DCAT/PROV/etc.) |
| CI/CD | `.github/` | Workflows, security policy, CI gates |


### `tools/ops/` shape

Current minimum (this file):

~~~text
🧰 tools/
└── ⚙️ ops/
    └── 📄 README.md
~~~

Suggested expansion (optional; **not confirmed in repo**):

~~~text
🧰 tools/
└── ⚙️ ops/
    ├── 📄 README.md
    ├── 📁 runbooks/             # procedures, rollback, verification
    ├── 📁 scripts/              # automation entrypoints (safe-by-default)
    ├── 📁 env/                  # .env.example, config templates (no secrets)
    ├── 📁 docker/               # compose files, container helpers
    ├── 📁 k8s/                  # manifests/helm (if in-repo)
    ├── 📁 terraform/            # IaC modules (if in-repo)
    └── 📁 ci/                   # helper scripts invoked by CI workflows
~~~


## 🧭 Context

KFM is governed as “documentation-as-code” and enforces **no unsourced narrative** and **provenance as a first-class concern**.

Operational tooling must therefore:

- Preserve the canonical stage ordering (don’t shortcut “ETL → catalogs → graph → APIs → UI → story”).
- Treat schemas and API contracts as the compatibility boundary (ops scripts should *validate* contracts, not silently change them).
- Prefer reproducible, deterministic runs: same inputs/config should yield the same outputs, and logs should be sufficient to audit what ran.
- Avoid introducing “hidden state” (e.g., one-off manual edits) without capturing provenance and a rollback plan.


## 🗺️ Diagrams

~~~mermaid
flowchart LR
  Operator[Operator] --> Ops[tools/ops]
  Ops --> ETL[ETL]
  ETL --> Catalogs[STAC/DCAT/PROV]
  Catalogs --> Graph[Neo4j Graph]
  Graph --> APIs[APIs]
  APIs --> UI[React/Map UI]
  UI --> Story[Story Nodes]
  Story --> Focus[Focus Mode]
~~~


## 📦 Data & Metadata


### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Repository working tree | files | git checkout | CI + lint |
| Environment configuration | env / yaml / json | `tools/ops/env/` (suggested) | schema/format checks |
| Service endpoints | urls | operator / secrets manager | health checks |
| Release parameters | flags | CLI args | argument validation |


### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run logs | text/json | `tools/ops/` or `mcp/runs/` (not confirmed) | telemetry schema (if defined) |
| Deployment manifests | yaml | `tools/ops/k8s/` (not confirmed) | kubernetes schema tooling |
| Build artifacts | image/tar | registry / artifact store | release policy |


### Sensitivity & redaction

- Treat ops logs as potentially sensitive (paths, endpoints, user IDs).
- Never embed tokens/keys in examples; use placeholders and references to a secrets manager or `.env` loaded at runtime.


### Quality signals

- Command exits are reliable (non-zero on failure).
- Scripts are idempotent where possible.
- Schema validation is performed before publishing any catalog/contract outputs.


## 🌐 STAC, DCAT & PROV Alignment


### STAC

- Collections involved: depends on what is being operated (not confirmed in repo).
- Items involved: depends on what is being operated (not confirmed in repo).
- Extension(s): must be documented and validated via `schemas/`.


### DCAT

- Dataset identifiers: must map to catalog records (not confirmed in repo).
- License mapping: must remain explicit (no “unknown license” defaults).
- Contact / publisher mapping: defined by governance docs (not confirmed in repo).


### PROV-O

- `prov:wasDerivedFrom`: expected for any derived artifacts.
- `prov:wasGeneratedBy`: expected for catalog outputs and story nodes.
- Activity / Agent identities: should be stable identifiers (script + version + operator identity when appropriate).


### Versioning

- Use semver for contracts and schemas, and ensure ops tooling does not create breaking changes without the required version bump and migration plan.


## 🧱 Architecture


### Components

| Component | Responsibility | Interface |
|---|---|---|
| Ops tooling | Safe automation + runbooks | CLI + documented procedures |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |


### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/api/` + `docs/api/` (not confirmed) | Contract tests required |
| UI layer registry | `src/web/` or `web/` (not confirmed) | Schema-validated |
| Ops runbooks | `tools/ops/runbooks/` (not confirmed) | Keep step IDs stable; include rollback |


### Extension points checklist

- [ ] Ops: new runbook added with prerequisites + rollback + verification
- [ ] Ops: new script includes `--help` and safe defaults
- [ ] Ops: no secrets committed; `.env.example` provided if needed
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump


## 🧠 Story Node & Focus Mode Integration


### How this work surfaces in Focus Mode

- Ops changes should not change “what a user can claim” without corresponding provenance.
- If ops tooling deploys a new dataset or story node bundle, Focus Mode must still be able to display evidence links and citations.


### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.


### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~


## 🧪 Validation & CI/CD


### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)


### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
# ./tools/ops/scripts/validate_schemas.sh

# 2) run unit/integration tests
# ./tools/ops/scripts/test_all.sh

# 3) run doc lint / protocol validation
# ./tools/ops/scripts/lint_docs.sh
~~~


### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| ops_run_started | ops script | `docs/telemetry/` + `schemas/telemetry/` (not confirmed) |
| ops_run_completed | ops script | `docs/telemetry/` + `schemas/telemetry/` (not confirmed) |
| deployment_event | ops pipeline | telemetry pipeline (not confirmed) |


## ⚖ FAIR+CARE & Governance


### Review gates

- Ops changes that affect access control, data visibility/redaction, or public endpoints require **human review**.
- If an ops change introduces a breaking contract (schema/API/UI registry), it requires versioning/migration documentation.


### CARE / sovereignty considerations

- Identify impacted communities and apply sovereignty rules (classification, redaction, restricted coordinates) where required.
- Prefer generalization over exposure for sensitive locations in any public logs or artifacts.


### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use (no policy generation; no inference of sensitive locations).


## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-22 | Initial `tools/ops/` README | TBD |


---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

