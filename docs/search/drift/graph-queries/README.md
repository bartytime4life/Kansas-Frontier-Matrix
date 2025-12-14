---
title: "🕸️ KFM — DRIFT Graph Queries (Neo4j Cypher Templates · Bounded Traversals · CARE Gates)"
path: "docs/search/drift/graph-queries/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Reference + Templates"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "drift-graph-queries"
audience:
  - "Search Engineering"
  - "Graph + Provenance Engineering"
  - "Focus Mode Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public (Governed)"
fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
redaction_required: true
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "Graph retrieval may touch heritage-context entities; CARE screening mandatory; bounded traversals required."
risk_category: "Governed"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:graph-queries:v11.2.6"
semantic_document_id: "kfm-drift-search-graph-queries"
event_source_id: "ledger:docs/search/drift/graph-queries/README.md"
immutability_status: "version-pinned"
machine_extractable: true

telemetry_schema: "../../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../../security/supply-chain/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "diagram-extraction"
  - "metadata-extraction"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded by drift-search-v12"
---

<div align="center">

# 🕸️ **KFM — DRIFT Graph Queries**
`docs/search/drift/graph-queries/README.md`

**Purpose**  
Define the governed **Neo4j/Cypher query layer** for DRIFT global→local retrieval: deterministic query templates,
**bounded traversals**, **rights/sensitivity filters**, and **CARE/sovereignty gates** that prevent leakage and
ensure provenance-safe evidence bundles.

<img src="https://img.shields.io/badge/Graph-Neo4j-success" />
<img src="https://img.shields.io/badge/Cypher-Templates-blue" />
<img src="https://img.shields.io/badge/Determinism-Bounded%20Traversals-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

DRIFT graph queries are the **precision stage** of hybrid retrieval:

- global recall yields anchors (communities/entities/datasets),
- graph queries expand locally in Neo4j using **bounded** traversals,
- results are filtered by **rights, sensitivity, and sovereignty** constraints,
- outputs are returned as **reference bundles** (stable ids + minimal safe fields),
- provenance and telemetry are emitted for governance review.

### Non-negotiables (governed)

- **No unbounded traversal** (every query MUST cap depth, fan-out, and result count).
- **No sensitive leakage** (no raw protected coordinates; no re-identifying joins).
- **No string-concatenated Cypher** (parameterize all inputs).
- **Deterministic ordering** (stable `ORDER BY` + stable `LIMIT`).
- **Policy gates first-class** (CARE/sovereignty outcomes are query-visible and auditable).

---

## 🗂️ Directory Layout

~~~text
📁 docs/search/drift/graph-queries/                    — DRIFT Cypher templates and query contract
├── 📄 README.md                                       — This document
├── 📁 templates/                                      — Cypher query templates (parameterized)
│   ├── 🧾 00_anchor_communities.cypher                — Community/anchor lookup (global→local bridge)
│   ├── 🧾 10_expand_entities.cypher                   — Bounded neighborhood expansion (local precision)
│   ├── 🧾 20_spatiotemporal_filter.cypher             — Time + generalized-space constrained retrieval
│   ├── 🧾 30_evidence_bundle.cypher                   — Evidence bundle materialization (refs-only)
│   ├── 🧾 40_dataset_catalog_links.cypher             — STAC/DCAT dataset linkage (refs-only)
│   └── 🧾 90_provenance_edges.cypher                  — Optional provenance neighborhood (refs-only)
├── 📁 policies/                                       — Query allowlists and safety rules
│   ├── 🧾 label_allowlist.yml                         — Allowed node labels per query family
│   ├── 🧾 rel_allowlist.yml                           — Allowed relationship types per query family
│   └── 🧾 result_fields.yml                           — Allowed return fields (safe projection rules)
└── 📁 examples/                                       — Redaction-safe examples (no sensitive locations)
    ├── 🧾 params.example.json
    └── 🧾 results.example.json
~~~

> The files above are a governed naming convention. If templates do not exist yet, create them under governance review.
> This README defines the contract they MUST satisfy.

---

## 🧭 Query packaging and parameters

### Parameterization (required)

All queries MUST be executed via parameter binding.

Minimum required parameter set for DRIFT episodes:

- `$episode_id` (stable retrieval episode id)
- `$query_hash` (sha256 normalized)
- `$max_hops` (integer; required)
- `$limit_nodes`, `$limit_edges` (integers; required)
- `$allowed_labels` (array; required)
- `$allowed_rels` (array; required)
- `$time_start`, `$time_end` (optional; ISO8601)
- `$h3_cells` or `$region_id` (optional; generalized spatial scope only)
- `$rights_class_max` (optional; policy-defined)
- `$sovereignty_mode` (required; `clear|restricted|conflict|unknown`)

### Deterministic ordering (required)

Every query MUST specify a stable ordering before applying `LIMIT`, e.g.:

- `ORDER BY n.station_id`, `ORDER BY n.id`, or `ORDER BY n.urn`
- never rely on internal Neo4j ordering

---

## 🧬 Graph query families

DRIFT uses a small number of query families to keep behavior auditable.

### 1) Anchor community lookup

Purpose: map global anchors to graph nodes that seed local traversal.

Inputs:

- anchor ids or anchor hashes
- allowed label set
- rights/sensitivity constraints

Output:

- anchor node ids + minimal safe descriptors (no sensitive geometry)

### 2) Local bounded expansion

Purpose: expand from anchors through allowed relationships within `max_hops`, while preventing fan-out.

Inputs:

- anchor node ids
- allowlisted relationships and labels
- depth and limit controls

Output:

- evidence candidate node ids + relationship stubs

### 3) Spatiotemporal constraint application

Purpose: apply time-window filters and generalized spatial scope.

Inputs:

- time bounds
- region/H3 coarse scope
- governance posture (redaction required)

Output:

- filtered candidate ids + counts

### 4) Evidence bundle materialization

Purpose: return a “refs-only” evidence bundle suitable for synthesis and provenance.

Inputs:

- candidate ids
- allowed return fields (safe projections)

Output:

- entity references and summary fields only (ids, types, titles, time ranges)

---

## 🛡️ CARE and sovereignty constraints (query-time)

Because `redaction_required: true`, graph queries MUST:

- avoid returning raw coordinates (`lon`, `lat`, `geom`, `wkt`, etc.) for sensitive classes,
- prefer generalized spatial attributes (H3 at governed resolution; region ids),
- enforce sovereignty flags:
  - block restricted nodes entirely, or
  - return only aggregated counts + generalized region-level descriptors,
  based on policy configuration.

### Required governance fields in result envelopes

Every result envelope SHOULD include (even if empty):

- `care_gate_status`: `allow|redact|deny`
- `sovereignty_gate`: `clear|restricted|conflict|unknown`
- `redaction_summary`: counters only

---

## 🧱 Example Cypher templates (schematic)

These templates are illustrative and MUST be adapted to KFM graph labels/relationships as implemented.

### Template: anchor community lookup (bounded)

~~~cypher
// 00_anchor_communities.cypher
// Purpose: resolve anchor/community ids to graph nodes with rights gating.
// Inputs: $anchor_ids (list), $allowed_labels (list), $rights_class_max (string), $limit_nodes (int)

MATCH (a)
WHERE a.anchor_id IN $anchor_ids
  AND any(lbl IN labels(a) WHERE lbl IN $allowed_labels)
  AND coalesce(a.rights_class, "public") <= $rights_class_max
RETURN
  a.urn AS urn,
  labels(a) AS labels,
  coalesce(a.title, a.name, a.urn) AS display,
  coalesce(a.sensitivity_level, "None") AS sensitivity_level
ORDER BY urn
LIMIT $limit_nodes;
~~~

### Template: bounded entity expansion (no unbounded traversal)

~~~cypher
// 10_expand_entities.cypher
// Purpose: expand from anchors through allowlisted rels and labels.
// Inputs: $anchor_urns (list), $allowed_labels (list), $allowed_rels (list),
//         $max_hops (int), $limit_edges (int), $limit_nodes (int)

MATCH (seed)
WHERE seed.urn IN $anchor_urns

MATCH p = (seed)-[r*1..$max_hops]-(n)
WHERE all(rel IN r WHERE type(rel) IN $allowed_rels)
  AND any(lbl IN labels(n) WHERE lbl IN $allowed_labels)

WITH DISTINCT n, r
RETURN
  n.urn AS urn,
  labels(n) AS labels,
  size(r) AS hop_count
ORDER BY hop_count ASC, urn ASC
LIMIT $limit_nodes;
~~~

### Template: spatiotemporal filter (generalized space only)

~~~cypher
// 20_spatiotemporal_filter.cypher
// Purpose: filter candidates by time window and generalized region/H3 scope.
// Inputs: $candidate_urns (list), $time_start (datetime?), $time_end (datetime?),
//         $h3_cells (list), $region_id (string?), $limit_nodes (int)

MATCH (n)
WHERE n.urn IN $candidate_urns

// Temporal filter (optional)
WITH n
WHERE ($time_start IS NULL OR coalesce(n.time_end, datetime("9999-12-31")) >= $time_start)
  AND ($time_end   IS NULL OR coalesce(n.time_start, datetime("0001-01-01")) <= $time_end)

// Spatial filter (generalized only)
WITH n
WHERE (
  $region_id IS NULL AND $h3_cells IS NULL
) OR (
  $region_id IS NOT NULL AND n.region_id = $region_id
) OR (
  $h3_cells IS NOT NULL AND n.h3_cell IN $h3_cells
)

RETURN
  n.urn AS urn,
  labels(n) AS labels
ORDER BY urn
LIMIT $limit_nodes;
~~~

### Template: evidence bundle (refs-only projection)

~~~cypher
// 30_evidence_bundle.cypher
// Purpose: safe projection of evidence references.
// Inputs: $candidate_urns (list), $limit_nodes (int)

MATCH (n)
WHERE n.urn IN $candidate_urns
RETURN
  n.urn AS urn,
  labels(n) AS labels,
  coalesce(n.title, n.name, n.urn) AS display,
  coalesce(n.time_start, null) AS time_start,
  coalesce(n.time_end, null) AS time_end,
  coalesce(n.source_ref, null) AS source_ref,
  coalesce(n.prov_ref, null) AS prov_ref
ORDER BY urn
LIMIT $limit_nodes;
~~~

> NOTE: The examples above intentionally avoid geometry fields. If geometry must be present, it MUST be generalized and policy-approved.

---

## 🗺️ DRIFT flow (graph retrieval focus)

~~~mermaid
flowchart TD
  A["Anchors (vector/community stage)"] --> B["Anchor resolution query"]
  B --> C["Bounded neighborhood expansion"]
  C --> D["Time + generalized-space filtering"]
  D --> E["Evidence bundle projection (refs-only)"]
  E --> F["CARE screen + synthesis"]
  E --> G["PROV + STAC episode emission (optional)"]
~~~

---

## 🔧 Performance and safety guardrails

Queries MUST implement:

- depth caps: `max_hops` enforced everywhere
- fan-out control: `LIMIT` used after stable ordering
- allowlists:
  - node labels restricted via `label_allowlist.yml`
  - relationship types restricted via `rel_allowlist.yml`
- projection rules:
  - allowed return fields restricted via `result_fields.yml`
- timeout discipline:
  - production runners SHOULD enforce query timeouts and retry policy
- denial posture:
  - when sovereignty gate conflicts or access is unknown, fail closed (deny or return aggregated results only)

---

## 📜 Provenance mapping (minimum)

Every graph query execution SHOULD be represented in provenance:

- `prov:Activity`:
  - `drift_graph_retrieval` (episode-scoped)
- `prov:Entity` inputs:
  - anchor set entity (by hash)
  - allowlist policy entities (by hash)
  - index snapshot entity
- `prov:Entity` outputs:
  - evidence bundle entity (refs-only)
  - query stats entity (counts, timings; no sensitive payload)

The evidence bundle should be linkable by `episode_id` and checksummed.

---

## 🧪 Validation and CI expectations

Changes to query templates SHOULD trigger:

- Cypher lint / parse checks (tooling-dependent)
- policy conformance checks:
  - all labels/rels used are allowlisted
  - returned fields match the safe projection spec
- determinism checks:
  - stable ordering present before every `LIMIT`
  - no nondeterministic functions used
- leakage checks:
  - geometry fields not returned unless explicitly allowed and generalized
- explain-plan thresholds (recommended):
  - prevent accidental cartesian products
  - prevent unindexed scans where avoidable

Validation results SHOULD be recorded in run logs (e.g., `mcp/runs/search/drift/<run_id>/validate.log`).

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT graph query contract; defined directory layout, bounded traversal rules, allowlists, safe projections, and validation gates. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to DRIFT Search](../README.md) ·
[🔍 Search Index](../../README.md) ·
[📜 DRIFT Provenance](../provenance/README.md) ·
[🗂️ DRIFT STAC](../stac/README.md) ·
[🏛️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

