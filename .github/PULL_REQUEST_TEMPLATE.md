---
title: "KFM — Pull Request Template"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "template"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:github:pull-request-template:v1.0.0"
semantic_document_id: "kfm-github-pull-request-template-v1.0.0"
event_source_id: "ledger:kfm:doc:github:pull-request-template:v1.0.0"
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

# Pull Request

<!--
KFM governance reminders:
- Preserve canonical pipeline order:
  ETL → STAC/DCAT/PROV Catalogs → Neo4j Graph → APIs → React/Map UI → Story Nodes → Focus Mode
- Frontend consumes through API contracts (no direct graph dependency).
- No unsourced narrative in user-facing surfaces; provenance + citations are required.
-->

## 📘 Overview

### Purpose
- **What**: <!-- 1–3 sentences -->
- **Why**: <!-- link issue(s) / user story -->
- **How**: <!-- high-level approach -->

### Type of change
- [ ] Dataset / catalog (STAC/DCAT/PROV)
- [ ] ETL / pipeline
- [ ] Graph / ontology / migration
- [ ] API contract (REST/GraphQL)
- [ ] Web UI (React/MapLibre)
- [ ] Story Node / Focus Mode narrative
- [ ] Telemetry / observability
- [ ] Security / governance / policy docs
- [ ] Documentation-only
- [ ] Other: <!-- describe -->

### Scope
| In Scope | Out of Scope |
|---|---|
| <!-- --> | <!-- --> |

### Related issues / tickets
- Closes: #
- Related: #

### Key artifacts touched
| Artifact | Path / Identifier | Change | Notes |
|---|---|---|---|
| <!-- e.g., Pipeline module --> | <!-- src/pipelines/... --> | <!-- add/modify/remove --> | <!-- --> |

### Definition of done
- [ ] PR description complete (this template filled)
- [ ] All changes are deterministic/replayable (seeded if applicable)
- [ ] Tests/validation updated and passing (see below)
- [ ] Documentation updated (docs-first; missing docs treated as a bug)
- [ ] Provenance + sensitivity handled (FAIR+CARE + sovereignty)

---

## 🗂️ Directory Layout

### Changed areas (check all that apply)
| Area | Path(s) | Notes |
|---|---|---|
| Data | `data/` | <!-- raw/work/processed/stac --> |
| Pipelines | `src/pipelines/` | <!-- --> |
| Catalogs | `data/stac/` + `docs/data/` | <!-- STAC/DCAT/PROV --> |
| Graph | `src/graph/` + `docs/graph/` | <!-- --> |
| APIs | `src/server/` + `docs/` | <!-- --> |
| Frontend | `web/` | <!-- --> |
| Story Nodes | `docs/reports/.../story_nodes/` | <!-- --> |
| Schemas | `schemas/` | <!-- --> |
| Tests | `tests/` | <!-- --> |
| CI | `.github/workflows/` | <!-- --> |
| MCP artifacts | `mcp/` | <!-- experiments/model cards/SOPs --> |

### File tree (optional but helpful)
~~~text
📦 <root>
├─ 📁 data/
│  ├─ 📁 raw/
│  ├─ 📁 work/
│  ├─ 📁 processed/
│  └─ 📁 stac/
├─ 📁 src/
├─ 📁 web/
├─ 📁 docs/
└─ 📁 tests/
~~~

---

## 🧭 Context

### Pipeline ordering & contract invariants (must be true)
- [ ] I did **not** bypass the canonical pipeline ordering (ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode).
- [ ] UI changes (if any) consume KFM data through API contracts (no direct Neo4j/graph access).
- [ ] I did **not** add unsourced narrative in any user-facing surface; citations/provenance exist or are queued.

### Assumptions
- <!-- -->

### Risks / impact
- **Risk level**: [ ] Low [ ] Medium [ ] High
- **User impact**: <!-- -->
- **Performance impact**: <!-- -->
- **Breaking change?**: [ ] No [ ] Yes (describe + mitigation)

### Rollout / migration plan (if needed)
- [ ] No rollout needed
- [ ] Requires migration/backfill (describe):
  - <!-- -->

---

## 📦 Data & Metadata

### If this PR changes or adds datasets
- [ ] Data staged correctly (`data/raw/` → `data/work/` → `data/processed/`)
- [ ] New/updated STAC Collection + Item(s) created under `data/stac/`
- [ ] DCAT view updated (if applicable)
- [ ] PROV lineage updated (`prov:wasDerivedFrom` / `prov:wasGeneratedBy`, run IDs)
- [ ] Validation performed (schema + geometry/range checks)
- [ ] Large assets tracked appropriately (e.g., DVC) and not committed directly to Git if oversized

### If this PR adds or changes an analysis / ML artifact
- [ ] Experiment log added under `mcp/experiments/` (hypothesis, inputs, method, outputs)
- [ ] Model card added/updated under `mcp/model_cards/` (model version, data, limits, bias notes)
- [ ] Outputs stored under `data/processed/` (not `src/`)
- [ ] Uncertainty/confidence fields included (where applicable)

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC IDs / Collections / Items**:
  - <!-- -->
- **DCAT dataset identifiers**:
  - <!-- -->
- **PROV activity/run IDs**:
  - <!-- -->

---

## 🧱 Architecture

### Components changed
- <!-- e.g., src/pipelines/...; src/server/...; web/... -->

### API contract impact (if any)
- [ ] No API changes
- [ ] REST contract changed (link to doc / OpenAPI update):
  - <!-- -->
- [ ] GraphQL schema/resolvers changed (link):
  - <!-- -->
- [ ] Contract extension doc added (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` as governing format)

---

## 🧠 Story Node & Focus Mode Integration (if relevant)

- [ ] No Story/Focus changes
- [ ] Story Node(s) added/updated (path + IDs):
  - <!-- -->
- [ ] Evidence-led narrative with cited dataset/document IDs
- [ ] Sensitivity handling described (redaction/generalization)

---

## 🧪 Validation & CI/CD

### Checks run (paste commands + results)
- <!-- Example:
~~~bash
make test
~~~
-->

### Test coverage
- [ ] Unit tests updated/added
- [ ] Integration tests updated/added
- [ ] Schema validation updated/added (`schemas/`)
- [ ] Data validation updated/added (ranges, geometry validity, null checks)
- [ ] Frontend checks (lint/build/a11y) run (if UI touched)

### Evidence (optional)
- Screenshots / GIFs (UI)
- Logs (pipeline run)
- Sample outputs (small, non-sensitive)

---

## ⚖ FAIR+CARE & Governance

### Sensitivity / sovereignty / ethics
- [ ] No sensitive locations/PII introduced
- [ ] If sensitive content exists, it is generalized/redacted per `docs/governance/SOVEREIGNTY.md`
- [ ] CARE considerations reviewed (collective benefit, authority to control, responsibility, ethics)
- [ ] Security implications reviewed (authz/audit/logging; see `.github/SECURITY.md`)

### Approvals needed
- [ ] None
- [ ] FAIR+CARE council review
- [ ] Security council review
- [ ] Historian/editor review
- [ ] Other: <!-- -->

---

## 🙋 Reviewer Notes

- Suggested reviewers: @
- Review focus areas:
  - <!-- -->