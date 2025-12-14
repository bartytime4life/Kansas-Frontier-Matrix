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

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "ops-dashboards-alerts"
diagram_profiles:
  - "mermaid-flowchart-v1"
---

# Overview

Three concise Cypher snippets for **ops dashboards & alerts**:

- **24h window**: dataset → versions changed → counts
- **7d window**: same rollup, weekly cadence
- **Item ↔ provenance diff**: single-statement property diff using `apoc.diff.maps`

Assumptions (rename if needed):

- Nodes:
  - `(:Dataset {id})`
  - `(:DatasetVersion {id, created_at})`
  - `(:Item {id, properties})`
  - `(:Activity {id, startedAtTime, type})`
- Relationships:
  - `(:Dataset)-[:HAS_VERSION]->(:DatasetVersion)`
  - `(:DatasetVersion)-[:HAS_ITEM]->(:Item)`
  - `(:Item)-[:WAS_GENERATED_BY]->(:Activity)`
- APOC available (for `apoc.map.fromPairs`, `apoc.diff.maps`)

---

## Graph shape (for reference)

~~~mermaid
flowchart TD
  D["Dataset"] -->|HAS_VERSION| V["DatasetVersion (created_at)"]
  V -->|HAS_ITEM| I["Item (properties)"]
  I -->|WAS_GENERATED_BY| A["Activity (startedAtTime, type)"]
~~~

---

## 1) 24h Change Window (dataset → versions changed → counts)

~~~cypher
// Roll up changes in the last 24h for dashboards/alerts.
// Deterministic: stable ordering before collect + limit.
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

---

## 2) 7d Change Window (dataset → versions changed → counts)

~~~cypher
// Roll up changes in the last 7d for weekly dashboards/alerts.
// Deterministic: stable ordering before collect + limit.
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

---

## 3) Item ↔ provenance diff (newest vs previous) using `apoc.diff.maps`

This returns a property diff between the newest and previous `Item.properties` for a given `$item_id`,
and includes the generating `Activity` ids (when present).

Parameters:

- `$item_id` (string; required)

~~~cypher
// Single-statement property diff for a specific item across the newest vs previous version.
// Requires APOC: apoc.diff.maps(mapA, mapB).
WITH $item_id AS item_id

MATCH (:Dataset)-[:HAS_VERSION]->(v:DatasetVersion)-[:HAS_ITEM]->(i:Item {id: item_id})
OPTIONAL MATCH (i)-[:WAS_GENERATED_BY]->(a:Activity)

WITH
  item_id,
  v,
  i,
  a
ORDER BY v.created_at DESC, a.startedAtTime DESC

WITH collect({
  version_id: v.id,
  created_at: v.created_at,
  activity_id: a.id,
  activity_type: a.type,
  activity_started_at: a.startedAtTime,
  props: i.properties
}) AS rows

WHERE size(rows) >= 2

WITH
  item_id,
  rows[0] AS newer,
  rows[1] AS older

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

Back to index · [`docs/graph/cypher/README.md`](../README.md) · Graph · [`docs/graph/README.md`](../../README.md) · Governance · [`docs/standards/governance/ROOT-GOVERNANCE.md`](../../../standards/governance/ROOT-GOVERNANCE.md)
