---
title: "🧩 KFM — Cypher Pattern Library (Ops · Catalog · Provenance)"
path: "docs/graph/cypher/patterns/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Graph Board"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "cypher-pattern-index"
audience:
  - "Graph Engineering"
  - "Reliability Engineering"
  - "Data Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "FAIR+CARE Council · Graph Board"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:graph:cypher:patterns:index:v11.2.6"
semantic_document_id: "kfm-graph-cypher-patterns-index"
event_source_id: "ledger:docs/graph/cypher/patterns/README.md"
provenance_chain:
  - "initial:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-claims"
  - "unverified-architectural-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧩 **KFM — Cypher Pattern Library**
`docs/graph/cypher/patterns/README.md`

**Purpose**  
A governed index of **ready-to-run** Neo4j Cypher patterns used across KFM for:
ops dashboards, catalog churn visibility, provenance audits, and reliability alerting.

</div>

---

## 📘 Overview

This directory is the canonical home for **KFM-approved Cypher patterns**.

Patterns here MUST be:

- deterministic (stable ordering before `collect`, stable `LIMIT` behavior),
- parameterized (no string concatenation; bind `$params`),
- governed (FAIR+CARE posture respected; avoid sensitive leakage),
- documented (assumptions, required labels/fields, expected outputs),
- portable (works across environments with minimal renaming).

---

## 🗂️ Directory Layout

~~~text
📁 docs/graph/cypher/                                 — Cypher documentation root
├── 📄 README.md                                      — Cypher index (entry point)
└── 📁 patterns/                                      — Governed Cypher pattern library (this directory)
    ├── 📄 README.md                                  — Pattern index (this file)
    └── 📄 change-windows.md                          — Operational change windows & diffs
~~~

---

## 🧭 Pattern Index

| Pattern | Primary use | Notes |
|---|---|---|
| [`change-windows.md`](change-windows.md) | Ops dashboards & alerts for dataset/version churn; item property diffs | Includes 24h + 7d rollups and an `apoc.diff.maps` diff |

---

## 🧱 Conventions and requirements

### Parameterization (required)

Patterns MUST use parameter binding:

- ✅ `WHERE n.id = $id`
- ❌ `WHERE n.id = '" + id + "'"`

Document required parameters explicitly in each pattern file.

### Deterministic ordering (required)

If a query uses `collect()` or chooses “newest/previous”, it MUST specify a stable ordering first:

- `ORDER BY dataset_id ASC, ts DESC, version_id ASC`
- `ORDER BY created_at DESC, id ASC`

### Bounded work (required)

Patterns MUST guard against runaway cardinality:

- cap traversals (depth caps where relevant),
- use `LIMIT` with deterministic ordering,
- avoid cartesian products unless explicitly intended and documented.

### Safe projections (recommended)

For ops and governance use, prefer returning:

- ids/URNs,
- counts,
- timestamps,
- normalized reason codes and statuses,

…rather than full property payloads that could include sensitive fields.

---

## 🧪 Validation & CI/CD

Recommended checks for this directory:

- `markdown-lint`: one H1 per file; approved headings; `~~~` fences only
- `diagram-check`: Mermaid blocks parse if present
- `query-smoke-test` (optional): execute patterns against a staging snapshot
- `governance-leakage-check` (optional): prevent restricted fields from being returned in “public” dashboards

---

## ⚖ FAIR+CARE & Governance

- Avoid returning raw sensitive geometry and restricted identifiers.
- If a graph includes sovereignty/sensitivity labels, patterns SHOULD:
  - filter restricted content by default, or
  - aggregate results (counts only) where necessary.
- Any new pattern that changes governance posture must be reviewed under the FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed Cypher pattern index for `docs/graph/cypher/patterns/`. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧾 Cypher Index](../README.md) ·
[🗺️ Graph Docs](../../README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

