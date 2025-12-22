---
title: "Pull Request Template"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---
-->

## 📘 Summary

### What changed?

<!-- 1–5 sentences. Link issues/tickets if applicable. -->

### Why?

<!-- Motivation + user impact. -->

### What areas does this touch? (check all that apply)

- [ ] ETL / pipelines
- [ ] Catalogs (STAC / DCAT / PROV)
- [ ] Graph (ontology, ingest, migrations)
- [ ] AI (models, prompts, evidence products)
- [ ] API (REST/GraphQL contracts)
- [ ] UI (React/Map UI, MapLibre, a11y)
- [ ] Story Nodes / Focus Mode narrative
- [ ] Docs / templates / standards
- [ ] CI / tooling / GitHub configuration

## 🧭 Architecture + invariants (must remain true)

- [ ] Canonical pipeline ordering preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- [ ] API boundary preserved: **UI does not read Neo4j directly**
- [ ] Stable IDs / deterministic transforms (idempotent ETL where applicable)
- [ ] No secrets or sensitive locations/PII introduced in code, data, logs, or artifacts

## 🌐 STAC / DCAT / PROV (if applicable)

- [ ] STAC: Items/Collections updated and schema-valid
- [ ] DCAT: Dataset catalog updated and consistent
- [ ] PROV: Provenance recorded (source IDs + run/activity IDs)

Evidence/paths:
- STAC: `data/stac/...`
- DCAT: `data/catalog/dcat/...`
- PROV: `data/prov/...`

## 🧱 Graph (if applicable)

- [ ] Ontology/schema changes documented and versioned (if required)
- [ ] Migrations included for non-backwards-compatible changes
- [ ] Graph tests/constraints updated (if present)

Evidence/paths:
- Ontology/docs: `docs/graph/...` (if present)
- Migrations: `src/graph/migrations/...` (if present)

## 📦 API (if applicable)

- [ ] Contract change documented (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` for governed contract updates)
- [ ] Contract tests updated/added (OpenAPI/GraphQL lint + resolver/integration tests)

## 🧪 Validation & CI/CD

### What did you validate? (check all that apply)

- [ ] CI is green
- [ ] Unit/integration tests updated (if applicable)
- [ ] Schema validation updated/passing (if applicable)
- [ ] Docs/templates updated in the same PR (if applicable)

### Notes for reviewers

<!-- Call out anything risky, non-obvious, or needing special attention. -->

## ⚖ FAIR+CARE & Governance

- [ ] Governance review required? (mark and explain)
- [ ] CARE/sovereignty considerations documented (if applicable)
- [ ] Sensitive data handling / generalization confirmed (if applicable)

## 🕰️ Version History (optional)

- Summary of notable changes if this PR is part of an incremental rollout.
~~~
