<!--
---
title: "GitHub Pull Request Template"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "active"
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
  - "structure_extract"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---
-->

<!--
Thanks for contributing! Please fill out what applies.
You can delete sections that are truly irrelevant, but keep checklists that touch changed subsystems.
-->

## Summary
<!-- What does this PR change and why? Keep it evidence-led and linkable. -->
- 

## Type of change (check all that apply)
- [ ] Bug fix
- [ ] Feature / enhancement
- [ ] Refactor / cleanup (no behavior change intended)
- [ ] Docs-only change
- [ ] Data ingestion / ETL
- [ ] Catalogs: STAC / DCAT / PROV
- [ ] Graph: Neo4j / ontology / migrations
- [ ] API: REST / GraphQL contracts
- [ ] UI: React / MapLibre / Cesium
- [ ] Story Nodes / Focus Mode narrative
- [ ] CI / GitHub / developer experience

## Related issues / tickets
<!-- Example: Fixes #123. Link any design docs, decision records, or governance approvals. -->
- Fixes: #
- Related: #

## Scope (what changed)
<!-- Bullet list of the main deltas, ideally grouped by subsystem -->
- 

## Validation evidence
<!-- Paste/describe how you validated this change. Prefer CI links + reproducible steps. -->
- CI status: <!-- link or "pending" -->
- Local checks (if applicable): <!-- command(s) or description -->
- Test coverage notes (if applicable): 

## Risk & rollback
- Risk level: [ ] Low  [ ] Medium  [ ] High
- Rollback plan (brief): 

---

# Subsystem checklists (complete the sections that apply)

## ✅ General (always)
- [ ] No secrets/credentials/tokens were added (including in examples, logs, fixtures)
- [ ] No new PII was introduced, or appropriate redaction/generalization is applied
- [ ] Changes are deterministic/idempotent where applicable (especially pipelines)
- [ ] Public-facing text avoids unsourced claims (provenance-first)

## 🧰 ETL / Pipelines (if applicable)
- [ ] Input sources documented (where applicable) under `data/sources/` or governed docs
- [ ] Output placement follows repo rules (raw/work/processed, no derived data in `src/`)
- [ ] Re-run behavior verified (idempotent; no duplicates)
- [ ] Any randomness is seed-locked and documented

## 🗂️ Catalogs: STAC / DCAT / PROV (if applicable)
- [ ] STAC: Collection(s) updated/added (`data/stac/collections/...`)
- [ ] STAC: Item(s) updated/added (`data/stac/items/...`) with valid geometry/time/links
- [ ] DCAT: Dataset record(s) updated/added (`data/catalog/dcat/...`) (IDs/keywords/license)
- [ ] PROV: Lineage bundle(s) updated/added (`data/prov/...`) with activity/run identifiers
- [ ] Schema validation performed (STAC/DCAT/PROV) and links are not broken

## 🧠 Graph: Neo4j / Ontology (if applicable)
- [ ] Ontology change is scoped and documented (labels/relations stable where required)
- [ ] Migration plan included (constraints/indexes/backfill) and is reversible where feasible
- [ ] Graph integrity checks pass (no orphaned references; provenance links preserved)

## 🌐 APIs: REST / GraphQL (if applicable)
- [ ] Contract updated (OpenAPI/GraphQL/schema) and backward-compat assessed
- [ ] Contract tests added/updated (integration + schema validation)
- [ ] Endpoint enforces access rules/redaction rules (no UI direct-to-graph coupling)

## 🗺️ UI: React / MapLibre / Cesium (if applicable)
- [ ] Screenshots or short clip included (for visible changes)
- [ ] A11y considerations checked (keyboard nav, contrast, semantics where applicable)
- [ ] Layer registry updated + schema-validated (if layers changed/added)
- [ ] UI consumes data via API contracts (no direct graph reads)

## 📚 Story Nodes / Focus Mode (if applicable)
- [ ] Story Node(s) added/updated under `docs/reports/.../story_nodes/`
- [ ] Every factual claim maps to a cited dataset/document ID (no “free text” claims)
- [ ] Sensitivity/CARE/sovereignty considerations reviewed and documented if triggered
- [ ] Predictive/AI-derived content is clearly labeled, opt-in, and includes uncertainty metadata (if used)

## 🧪 CI/CD gates (check what applies)
- [ ] Markdown protocol validation passes (if docs changed)
- [ ] JSON schema validation passes (STAC/DCAT/telemetry as applicable)
- [ ] Graph integrity tests pass (if graph changed)
- [ ] API contract tests pass (if API changed)
- [ ] UI schema checks pass (if UI registries changed)
- [ ] Security + sovereignty scanning gates pass (where applicable)

---

## Reviewer notes
<!-- Help reviewers: what’s the intended behavior, what are the edge cases, where to focus. -->
- 

## Checklist for maintainers (optional)
- [ ] Labels applied
- [ ] Changelog/release notes needed?
- [ ] Requires human review (governance/security/historian/editor) flagged when applicable