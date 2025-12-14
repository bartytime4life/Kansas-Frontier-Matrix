---
title: "🧩 KFM — Operational Change Windows & Diffs (Neo4j Cypher Patterns)"
path: "docs/graph/cypher/patterns/change-windows.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Board"
content_stability: "stable"
status: "Ready-to-Run"

doc_kind: "Query Patterns"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "ops-dashboards-alerts"
audience:
  - "Reliability Engineering"
  - "Graph Engineering"
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
data_steward: "FAIR+CARE Council · Reliability Board"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:graph:cypher:patterns:change-windows:v11.2.6"
semantic_document_id: "kfm-graph-cypher-change-windows"
event_source_id: "ledger:docs/graph/cypher/patterns/change-windows.md"
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

# 🧩 **KFM — Operational Change Windows & Diffs (Neo4j Cypher Patterns)**
`docs/graph/cypher/patterns/change-windows.md`

**Purpose**  
Provide three **ready-to-run** Cypher patterns for ops dashboards and alerts:
**24h** and **7d** change windows (dataset → versions → item counts), plus a **property diff** (newest vs previous)
using `apoc.diff.maps`.

</div>

---

## 📘 Overview

This doc contains three concise snippets:

- 24h window: dataset → versions changed → counts
- 7d window: same rollup, weekly cadence
- Item ↔ provenance diff: property diff (newest vs previous) using `apoc.diff.maps`

All snippets are designed for:

- deterministic dashboards (stable ordering before `collect` and `limit`)
- alert thresholds (version_count, total_items_changed)
- low-friction ops adoption (single-file patterns)

---

## 🗂️ Directory Layout

~~~text
📁 docs/graph/cypher/                                 — Cypher docs and query patterns
├── 📄 README.md                                      — Cypher index (entry point)
└── 📁 patterns/                                      — Query pattern library (governed)
    └── 📄 change-windows.md                          — Operational change windows & diffs (this file)
~~~

---

## 🧭 Context

### Assumptions (rename labels/fields if needed)

Nodes:

- `(:Dataset {id})`
- `(:DatasetVersion {id, created_at})`
- `(:Item {id, properties})`
- `(:Activity {id, startedAtTime, type})`

Relationships:

- `(:Dataset)-[:HAS_VERSION]->(:DatasetVersion)`
- `(:DatasetVersion)-[:HAS_ITEM]->(:Item)`
- `(:Item)-[:WAS_GENERATED_BY]->(:Activity)`

APOC:

- APOC is available for `apoc.diff.maps(mapA, mapB)`.

### Operational intent

- Use windowed rollups for:
  - alerting on unusually large changes,
  - tracking freshness and churn by dataset,
  - highlighting version spikes after releases/backfills.
- Use property diffs for:
  - “why did this item change?” debugging,
  - validating that provenance and payload changes align.

---

## 🧱 Architecture

### 1) 24h change window (dataset → versions changed → counts)

~~~cypher
// Roll up changes in the last 24h for dashboards/alerts.
// Deterministic: stable ordering before collect().
WITH datetime() AS now
MATCH (d:Dataset)-[:HAS_VERSION]->(v:DatasetVersion)
WHERE v.created_at >= (now - duration('P1D'))
OPTIONAL MATCH (v)-[:HAS_ITEM]->(i:Item)
WITH
  d.id AS dataset_id,
  v.id AS version_id,
  v.created_at AS ts,
  count(i) AS item_count
ORDER BY dataset_id ASC, ts DESC, version_id ASC
WITH
  dataset_id,
  collect({version: version_id, created_at: ts, items: item_count}) AS versions_changed,
  sum(item_count) AS total_items_changed
RETURN
  dataset_id,
  versions_changed,
  total_items_changed,
  size(versions_changed) AS version_count
ORDER BY total_items_changed DESC, version_count DESC, dataset_id ASC;
~~~

### 2) 7d change window (dataset → versions changed → counts)

~~~cypher
// Roll up changes in the last 7d for weekly dashboards/alerts.
// Deterministic: stable ordering before collect().
WITH datetime() AS now
MATCH (d:Dataset)-[:HAS_VERSION]->(v:DatasetVersion)
WHERE v.created_at >= (now - duration('P7D'))
OPTIONAL MATCH (v)-[:HAS_ITEM]->(i:Item)
WITH
  d.id AS dataset_id,
  v.id AS version_id,
  v.created_at AS ts,
  count(i) AS item_count
ORDER BY dataset_id ASC, ts DESC, version_id ASC
WITH
  dataset_id,
  collect({version: version_id, created_at: ts, items: item_count}) AS versions_changed,
  sum(item_count) AS total_items_changed
RETURN
  dataset_id,
  versions_changed,
  total_items_changed,
  size(versions_changed) AS version_count
ORDER BY total_items_changed DESC, version_count DESC, dataset_id ASC;
~~~

### 3) Item ↔ provenance property diff (newest vs previous) using `apoc.diff.maps`

Parameters:

- `$item_id` (string; required)

~~~cypher
// Property diff for a specific item across the newest vs previous version.
// Requires APOC: apoc.diff.maps(mapA, mapB).
WITH $item_id AS item_id
MATCH (:Dataset)-[:HAS_VERSION]->(v:DatasetVersion)-[:HAS_ITEM]->(i:Item {id: item_id})
OPTIONAL MATCH (i)-[:WAS_GENERATED_BY]->(a:Activity)
WITH v, i, a, item_id
ORDER BY v.created_at DESC, a.startedAtTime DESC
WITH collect({
  version_id: v.id,
  created_at: v.created_at,
  activity_id: a.id,
  activity_type: a.type,
  activity_started_at: a.startedAtTime,
  props: i.properties
}) AS rows, item_id
WHERE size(rows) >= 2
WITH rows[0] AS newer, rows[1] AS older, item_id
RETURN
  item_id,
  older.version_id AS old_version_id,
  newer.version_id AS new_version_id,
  older.created_at AS old_created_at,
  newer.created_at AS new_created_at,
  older.activity_id AS old_activity_id,
  newer.activity_id AS new_activity_id,
  apoc.diff.maps(older.props, newer.props) AS properties_diff;
~~~

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  D["Dataset"] -->|HAS_VERSION| V["DatasetVersion - created_at"]
  V -->|HAS_ITEM| I["Item - properties"]
  I -->|WAS_GENERATED_BY| A["Activity - startedAtTime, type"]
~~~

---

## 📦 Data & Metadata

### Output fields (window rollups)

- `dataset_id` (string)
- `versions_changed` (array of `{version, created_at, items}`)
- `total_items_changed` (int)
- `version_count` (int)

### Output fields (property diff)

- `item_id` (string)
- `old_version_id`, `new_version_id` (string)
- `old_created_at`, `new_created_at` (datetime)
- `old_activity_id`, `new_activity_id` (string; nullable)
- `properties_diff` (map; APOC diff output)

### Determinism notes (ops-safe)

- Sorting before `collect()` ensures stable `versions_changed` ordering.
- Sorting before `collect()` in the diff query ensures deterministic newest/previous selection.

---

## 🧪 Validation & CI/CD

Recommended checks for changes to this file or to the graph schema it assumes:

- `markdown-lint`: one H1, approved H2s only, `~~~` fences only
- `diagram-check`: Mermaid parses under `mermaid-flowchart-v1`
- `schema-lint` / `metadata-check`: required front-matter keys present
- `query-smoke-test` (optional): run each snippet against a staging graph snapshot
- `provenance-check` (optional): ensure `(:Item)-[:WAS_GENERATED_BY]->(:Activity)` consistency

---

## 🌐 STAC, DCAT & PROV Alignment

- PROV-O:
  - `:DatasetVersion` is a natural `prov:Entity` version node.
  - `:Activity` aligns with `prov:Activity` (use `startedAtTime` as a time anchor).
  - `:Item` property diffs support lineage audits (what changed between derived entities).
- STAC/DCAT:
  - If Items represent STAC Items or DCAT Distributions, the 24h/7d rollups provide ops visibility into catalog churn.
  - The diff query can be used to validate that changes in `properties` align with expected provenance/activity updates.

---

## ⚖ FAIR+CARE & Governance

- These queries are designed to support governance and reliability by surfacing **counts and diffs**, not sensitive content.
- If `Item.properties` can include restricted fields (e.g., sensitive geometry), dashboards SHOULD:
  - avoid rendering raw property payloads,
  - prefer summarized diffs (keys changed, counts) rather than full values.
- If sovereignty or sensitivity labels exist in the graph, extend the window rollups with policy-gated filters (deny or aggregate).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed pattern pack for operational change windows and item property diffs; aligned to KFM-MDP v11.2.6 headings, fences, and footer rules. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Ready--to--Run-brightgreen" />

[🧾 Cypher Index](../README.md) ·
[🗺️ Graph Docs](../../README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
