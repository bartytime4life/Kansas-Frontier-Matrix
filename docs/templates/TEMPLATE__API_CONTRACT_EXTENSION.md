---
title: "TEMPLATE — API Contract Extension (REST/GraphQL)"
path: "docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:templates:api-contract-extension:v1.0.0"
semantic_document_id: "kfm-template-api-contract-extension-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:api-contract-extension:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions: [ "structure_extract" ]
ai_transform_prohibited: [ "generate_policy" ]

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# TEMPLATE — API Contract Extension (REST/GraphQL)

## 📘 Overview

### Change summary
- What is being added/changed/removed?

### Motivation
- Why is this needed (user story + system need)?

### Backward compatibility
- Compatible / version bump required / deprecations.

## 🗂️ Directory Layout

| Artifact | Path |
|---|---|
| API code | `src/server/` |
| API docs | `docs/` (link) |
| Schemas | `schemas/` |
| Tests | `tests/` |

## 🧭 Context

### Security + sensitivity
- If data can be sensitive, define:
  - authorization behavior
  - generalization behavior
  - audit/log behavior

## 🗺️ Diagrams

~~~mermaid
sequenceDiagram
  participant Client
  participant API
  participant Graph
  Client->>API: Request
  API->>Graph: Query (with redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>Client: Contracted payload
~~~

## 📦 Data & Metadata

### Data returned
| Field | Source | Sensitivity | Notes |
|---|---|---|---|
| TBD | TBD | public/restricted | TBD |

## 🌐 STAC, DCAT & PROV Alignment

- How responses link back to:
  - STAC item IDs
  - PROV activity/run IDs
  - DCAT dataset identifiers

## 🧱 Architecture

### REST contract
~~~json
{ "TBD": "example response" }
~~~

### GraphQL contract
~~~graphql
type TBD { id: ID! }
~~~

### Contract tests required
- REST: OpenAPI schema + integration tests
- GraphQL: schema lint + resolver tests

## 🧠 Story Node & Focus Mode Integration

- If this endpoint feeds Focus Mode, define:
  - required provenance refs
  - includePredictions behavior (if any)
  - uncertainty/confidence fields

## 🧪 Validation & CI/CD

- [ ] Contract schema updated
- [ ] Integration tests added
- [ ] Docs updated
- [ ] Sensitivity rules verified

## ⚖ FAIR+CARE & Governance

- Identify required approvals and reviewers.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial template | TBD |
