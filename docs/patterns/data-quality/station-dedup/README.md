---
title: "🛰️ KFM — Station Deduplication Pattern (Authoritative + Proximity + Name)"
path: "docs/patterns/data-quality/station-dedup/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pattern"
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

scope:
  domain: "data-quality"
  applies_to:
    - "etl/stations"
    - "catalogs/station-assets"
    - "graph/stations"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Reviewed quarterly; superseded by next governed revision"
commit_sha: "<latest-commit-hash>"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:patterns:data-quality:station-dedup:v11.2.6"
semantic_document_id: "urn:kfm:pattern:station-dedup:v11.2.6"
event_source_id: "urn:kfm:events:doc:station-dedup:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summarization"
  - "structure-preserving rewrite"
  - "metadata extraction"
ai_transform_prohibited:
  - "altering thresholds/radii/provider precedence without governance review"
  - "inventing merges, IDs, providers, or provenance"
  - "bypassing sovereignty/confidentiality gates"
---

<div align="center">

# 🛰️ KFM — Station Deduplication Pattern (Authoritative + Proximity + Name)
`docs/patterns/data-quality/station-dedup/README.md`

**Purpose**  
Deduplicate station entities from multiple providers (e.g., AQS, PurpleAir, custom networks) into a **single
deterministic canonical station record** using **authoritative IDs**, **spatial proximity**, and **name similarity**,
while preserving full **provenance** and generating **QA flags** for downstream rules, catalogs, and dashboards.

</div>

---

## 📘 Overview

Deduplicate station entities from multiple providers using a **3-key merge**:

1) **Authoritative ID match** (e.g., EPA SiteNumber, WMO, USGS `site_no`)  
2) **Spatial proximity** within configurable radius (e.g., 50–250 m)  
3) **Name similarity** (normalized string similarity; algorithm + threshold are governed)

### Outputs

- `canonical_station_id` (stable, deterministic)
- Provenance roll-up (all source providers + source IDs)
- QA flags for downstream rules & dashboards

### Design guarantees

- **Deterministic:** fixed radius `R_metres`, max-span `R_max`, name threshold `T_name`, H3 resolution
  `H3_res`, and provider preference list under KFM-PDC.
- **Provenance-complete:** every merge is explainable via provider/source IDs and PROV links.
- **Governable:** merges can be gated/blocked when sovereignty, sensitivity, or policy labels conflict.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 patterns/                         — Governed pattern library
    └── 📁 data-quality/                 — Data quality & record linkage patterns
        └── 📁 station-dedup/            — Station dedup pattern (authoritative + proximity + name)
            └── 📄 README.md             — This document
~~~

---

## 🧭 Context

### Problem

Stations are often duplicated across providers/networks, with:

- Different IDs for the same physical site
- Slight coordinate jitter (GPS drift, geocoding rounding, provider offsets)
- Name variants and formatting differences

### Non-goals

- This pattern **does not** deduplicate time-series observations (that is a downstream “measurement
  dedup” pattern).
- This pattern **does not** infer station identity across large distances or across weak evidence
  (no “best guess” merges).

---

## 📦 Data & Metadata

### Minimal Data Model (ingest)

- `provider` (string)
- `source_station_id` (string)
- `authoritative_id` (nullable string; e.g., WMO, AQS, USGS)
- `name` (string)
- `geom` (POINT; EPSG:4326)
- `elev_m` (nullable float)
- `start_time`, `end_time` (nullable timestamps)
- `attrs` (JSONB for raw source fields, untouched)

### QA Flags (booleans/enum)

- `authoritative_preference` (provider chosen due to trusted ID)
- `proximity_match` (distance_m ≤ `R_metres`)
- `name_match` (score ≥ `T_name`)
- `attribute_conflict` (e.g., >10 m elevation spread, or divergent start_time)
- `manual_review` (set when tie/low-confidence)
- `temporal_overlap_anomaly` (disjoint lifespans for “same” station)
- `geom_jitter` (cluster spans > `R_max`)
- `provider_superseded` (kept for lineage, not canonical)

### Output Schema (canonical table)

- `canonical_station_id` (string, primary key)
- `geom` (POINT)
- `name_primary` (string)
- `elev_m` (float, nullable)
- `providers` (JSONB; full provenance list)
- `qa_flags` (JSONB: `{authoritative_preference, proximity_match, name_match, attribute_conflict, manual_review, ...}`)
- `lineage` (PROV: entity/wasDerivedFrom for each source)
- `valid_time` (tsrange)

---

## 🧱 Architecture

### Merge Logic (deterministic)

Order of precedence:

1. If `authoritative_id` present → **hard link** cluster key = `authoritative_id`.
2. Else group candidates by **H3 cell** at resolution `H3_res` (e.g., 11–12) and filter by **distance ≤ `R_metres`**.
3. Within each spatial group, if **name_match ≥ `T_name`** → union into same cluster.

Cluster → assign:

- If any member has `authoritative_id`:  
  `canonical_station_id = urn:kfm:station:<authoritative_id>`
- Else:  
  `canonical_station_id = urn:kfm:station:<hash64(seed)>`  
  where `seed = ",".join(sorted([provider:source_station_id,...]))` and `hash64` is a deterministic
  64-bit digest (e.g., `sha256(seed)[:16]` hex).

### Reference SQL (PostGIS + similarity)

~~~sql
-- Reference-only sketch (cluster construction often requires union-find / connected-components).
-- Requires: PostGIS + pg_trgm (for similarity()).
-- Params:
--   :R_metres  (e.g., 50..250)
--   :T_name    (provider/governed threshold for your chosen similarity)
WITH norm AS (
  SELECT *,
         lower(regexp_replace(name,'[^a-z0-9 ]','', 'g')) AS name_norm
  FROM staging_stations
),
prox AS (
  SELECT
    a.provider,
    a.source_station_id,
    b.provider AS cand_provider,
    b.source_station_id AS cand_id,
    ST_DistanceSphere(a.geom, b.geom) AS distance_m,
    a.name_norm AS a_name,
    b.name_norm AS b_name
  FROM norm a
  JOIN norm b
    ON (a.provider, a.source_station_id) <> (b.provider, b.source_station_id)
   AND a.authoritative_id IS NULL
   AND b.authoritative_id IS NULL
   AND ST_DWithin(a.geom::geography, b.geom::geography, :R_metres)
),
name_hits AS (
  SELECT *,
         similarity(a_name, b_name) AS name_score
  FROM prox
  WHERE similarity(a_name, b_name) >= :T_name
),
clusters AS (
  SELECT
    COALESCE(
      n.authoritative_id,
      md5(
        string_agg(
          DISTINCT
          LEAST(n.provider||':'||n.source_station_id, nh.cand_provider||':'||nh.cand_id)
          || ',' ||
          GREATEST(n.provider||':'||n.source_station_id, nh.cand_provider||':'||nh.cand_id),
          '|' ORDER BY
          LEAST(n.provider||':'||n.source_station_id, nh.cand_provider||':'||nh.cand_id),
          GREATEST(n.provider||':'||n.source_station_id, nh.cand_provider||':'||nh.cand_id)
        )
      )
    ) AS cluster_key,
    n.provider,
    n.source_station_id
  FROM norm n
  LEFT JOIN name_hits nh
    ON nh.provider = n.provider
   AND nh.source_station_id = n.source_station_id
  GROUP BY 1, n.provider, n.source_station_id
)
SELECT * FROM clusters;
~~~

### Canonical Record Builder (Python pseudocode)

~~~python
from dataclasses import dataclass
from typing import List, Dict, Any
import hashlib

@dataclass
class Station:
    provider: str
    source_station_id: str
    authoritative_id: str|None
    name: str
    lon: float
    lat: float
    elev_m: float|None
    attrs: Dict[str,Any]

def canonical_id(members: List[Station]) -> str:
    auth = next((m.authoritative_id for m in members if m.authoritative_id), None)
    if auth:
        return f"urn:kfm:station:{auth}"
    seed = ",".join(sorted([f"{m.provider}:{m.source_station_id}" for m in members]))
    # 64-bit stable identifier as first 16 hex chars (governed).
    return "urn:kfm:station:" + hashlib.sha256(seed.encode()).hexdigest()[:16]

def pick_authoritative(members: List[Station]) -> Station:
    # deterministic preference order (edit in governance):
    order = ["AQS","USGS","WMO","NOAA","STATE","CITY","OTHER"]
    by = sorted(
        members,
        key=lambda m: (
            order.index(m.provider) if m.provider in order else 999,
            m.source_station_id
        )
    )
    return by[0]

def merge_attrs(members: List[Station]) -> Dict[str,Any]:
    out = {"providers":[{"provider":m.provider,"id":m.source_station_id} for m in members]}
    # keep non-conflicting fields; flag conflicts
    names = {m.name for m in members}
    out["name_choices"] = sorted(names)
    out["attribute_conflict"] = (len(names) > 1)
    return out
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- STAC Item properties:
  - `kfm:canonical_station_id`
  - `kfm:qa_flags.*`
  - `prov:wasDerivedFrom` (array of `provider:id`)

### DCAT

- `dct:identifier` = canonical id
- `dct:provenance` includes provider roll-up

### PROV-O

- `prov:Entity`(canonical) `prov:wasDerivedFrom` → `prov:Entity`(each source)
- `prov:Activity` “station-dedup-v1” with params `{R_metres, R_max, T_name, H3_res, preference_order}`

---

## 🧠 Story Node & Focus Mode Integration

- **Story Nodes** SHOULD reference stations by `kfm:canonical_station_id` (not raw provider IDs).
- Focus Mode SHOULD:
  - Surface `qa_flags` as confidence context (e.g., `manual_review=true`, `geom_jitter=true`).
  - Provide provenance roll-up (which providers + source IDs contributed to the canonical station).
  - Never “upgrade” a merge (e.g., change radius/threshold) without governed parameter evidence.

---

## 🧪 Validation & CI/CD

### CI Hooks (examples)

Fail the build if:

- >2% of records flip `canonical_station_id` vs previous release
- any cluster spans >`R_max` metres
- name_match median < target threshold (governed)

### Observability

Emit metrics:

- `stations.canonical.count`
- `stations.cluster.size.p95`
- `stations.qa.manual_review.count`

---

## ⚖ FAIR+CARE & Governance

- **Determinism:** fixed radius `R_metres`, name threshold `T_name`, H3 resolution `H3_res`, and
  provider preference list under KFM-PDC.
- **Sovereignty / CARE:** if sensor data is sensitive, gate merges via policy labels; require
  `manual_review=true` when labels conflict.
- **Auditability:** store provider roll-up and PROV lineage on every canonical record.

### Example QA Flag Semantics

- `authoritative_preference=true` when an `authoritative_id` exists and dictates the cluster.
- `proximity_match=true` when representative centroid is within `R_metres` of members.
- `name_match=true` when median name_score ≥ `T_name`.
- `manual_review=true` when ties or conflicts persist.

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|------|
| v11.2.6  | 2025-12-13 | Governed LTS release; aligned to KFM-MDP v11.2.6 header/footer profiles and fence/heading rules. |

---

<div align="center">

[📂 Patterns Index](../../README.md) ·
[🧪 Data Quality Patterns](../README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
