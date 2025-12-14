---
title: "🧾 KFM — Neo4j Cypher (Docs · Patterns · Ops Queries)"
path: "docs/graph/cypher/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Graph Board · FAIR+CARE Council"
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

intent: "graph-cypher-index"
audience:
  - "Graph Engineering"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"
  - "Frontend Engineering (API consumers)"

classification: "Public"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Graph Board · FAIR+CARE Council"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:graph:cypher:index:v11.2.6"
semantic_document_id: "kfm-graph-cypher-index"
event_source_id: "ledger:docs/graph/cypher/README.md"
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

# 🧾 **KFM — Neo4j Cypher**
`docs/graph/cypher/README.md`

**Purpose**  
Entry point for KFM’s governed Cypher documentation: **query conventions**, **ops-ready patterns**, and guidance for
writing deterministic, policy-safe graph queries that support dashboards, provenance audits, and reliability workflows.

</div>

---

## 📘 Overview

This directory contains:

- a governed pattern library (`patterns/`),
- conventions for writing safe, deterministic Cypher,
- notes for operational dashboards and alerting queries,
- reminders about the **API boundary** (frontend does not query Neo4j directly).

Cypher in KFM is used primarily for:

- graph ingestion validation and audits,
- dataset/version churn visibility,
- provenance tracing and diff analysis,
- internal ops dashboards and reliability checks.

---

## 🗂️ Directory Layout

~~~text
📁 docs/graph/                                         — Graph documentation root
└── 📁 cypher/                                         — Cypher docs and patterns (this directory)
    ├── 📄 README.md                                   — This file
    └── 📁 patterns/                                   — Governed Cypher pattern library
        ├── 📄 README.md                               — Pattern index
        └── 📄 change-windows.md                       — Operational change windows & diffs
~~~

---

## 🧭 Quick links

- Pattern library index: [`patterns/README.md`](patterns/README.md)
- Ops change windows + diffs: [`patterns/change-windows.md`](patterns/change-windows.md)

---

## 🧱 Conventions (governed)

### Parameterization (required)

All queries MUST use parameter binding:

- ✅ `WHERE d.id = $dataset_id`
- ❌ `WHERE d.id = '" + dataset_id + "'"`

Document required parameters and expected types.

### Deterministic ordering (required)

Any query that:

- uses `collect()`,
- selects “newest/previous,”
- ranks by score and applies `LIMIT`,

…MUST specify a stable `ORDER BY` before aggregation or limiting.

Examples:

- `ORDER BY dataset_id ASC, created_at DESC, version_id ASC`
- `ORDER BY urn ASC`

### Bounded work (required)

Avoid runaway cardinality:

- cap traversal depth (`*1..$max_hops`),
- cap fan-out with deterministic limits,
- avoid cartesian products unless explicitly intended.

### Safe projections (recommended)

Prefer returning:

- ids/URNs,
- counts and timestamps,
- normalized status fields,
- reason codes,

…instead of entire property maps that may include sensitive fields.

---

## 🛡️ FAIR+CARE posture

Even when graph data is “public,” query outputs can leak sensitive detail if you return raw geometry or narrow identifiers.

Guidance:

- avoid returning raw `geom`, `lat`, `lon` unless policy says it’s safe,
- prefer generalized region or coarse H3 where applicable,
- if sovereignty/sensitivity labels exist in the graph, filter/aggregate by default.

---

## 🧪 Validation & CI/CD

Recommended checks for Cypher docs and patterns:

- `markdown-lint` (KFM-MDP v11.2.6 structure + `~~~` fences)
- `diagram-check` (Mermaid blocks parse where present)
- `query-smoke-test` (optional; run patterns against staging graph snapshot)
- `governance-leakage-check` (optional; ensure “public” patterns don’t return restricted fields)

---

## 🧩 How these queries are used in KFM

### Ops dashboards and alerting

Cypher patterns can be used to power:

- “what changed in the last 24h/7d” panels,
- change spike alerts (items changed, versions created),
- provenance diff diagnostics (why a derived output changed).

### API boundary reminder

KFM frontend should not query Neo4j directly.

- Use Cypher patterns as:
  - internal tooling references,
  - backend service query building blocks,
  - ops runbooks and dashboards.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed Cypher docs index; linked pattern library and established deterministic, parameterized query conventions. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🗺️ Graph Docs](../README.md) ·
[🧩 Pattern Library](patterns/README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

