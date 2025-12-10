---
title: "🧭 Event→Action Map — Keep STAC/DCAT & Graph Aligned"
path: "docs/events/README.md"
version: "v11.2.x"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & Metadata Councils"
content_stability: "stable"

doc_kind: "Runbook"
status: "Active / Canonical"
intent: "event-routing"
semantic_document_id: "kfm-doc-events-routing-v11.2.x"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

header_profile: "standard"
footer_profile: "standard"

standards:
  - STAC 1.0.x (KFM-STAC v11 profile)
  - DCAT 3.0 (KFM-DCAT v11 profile)
  - PROV-O (derivations, activities)
  - KFM-MDP v11.2.x (authoring)
  - KFM-PDC v11 (pipeline/data contracts)

governance:
  fairness: "FAIR+CARE"
  sovereignty: "Indigenous data-sovereignty aligned"
  supply_chain: "SBOM + SLSA attestations"
  rollback_policy: "Auto-repoint to previous DatasetVersion on post-publish regression"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../releases/v11.2.6/signature.sig"
telemetry_ref: "../../releases/v11.2.6/events-telemetry.json"
telemetry_schema: "../../schemas/telemetry/events-routing-v1.json"
---

# 🧭 Event→Action Map — Keep STAC/DCAT & Graph Aligned

This runbook defines how **`event_kind`** and **`status`** drive KFM behavior across:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → UI

with guarantees of **idempotent upserts**, **reversible rollbacks**, and **provenance continuity**.

---

## 🗂️ Directory Layout

~~~text
docs/events/
├── 📄 README.md                    # Event→Action Map (this file, canonical routing runbook)
├── 📁 specs/
│   ├── 📄 product-availability.md  # Detailed spec for product-availability events
│   ├── 📄 reprocessing.md          # Detailed spec for reprocessing events
│   ├── 📄 algorithm-change.md      # Detailed spec for algorithm-change events
│   └── 📄 mission-status.md        # Optional: mission/collection status events
├── 📁 handlers/
│   ├── 📄 kfm-events-router.md     # Implementation notes for the events router service
│   └── 📄 neo4j-sync.md            # Graph sync / constraint behavior per event_kind
└── 📁 playbooks/
    ├── 📄 outages.md               # Operator playbooks (pause & backfill)
    └── 📄 reprocessing-algos.md    # Reprocessing + algorithm-change combined flows
~~~

Related (implementation & data) — authoritative details live in their own READMEs:

- `src/events/router/` — event router service and routing logic  
- `src/pipelines/events/` — ETL pipelines that materialize event-driven changes  
- `data/events/` — normalized event logs (for audit & testing)  
- `data/stac/**/collection.json` — STAC Collections affected by events  
- `data/catalogs/**` — DCAT datasets and distributions  
- `src/graph/events/` — Neo4j ingestion and constraints for event-driven updates  

---

## 📘 Overview

KFM receives **events** (internal and external) that describe changes in:

- **Product availability**  
- **Reprocessing campaigns**  
- **Algorithm versions**  
- **Mission/collection status**

This runbook standardizes how those events:

1. **Modify ETL behavior** (pause, resume, parallel ingest, branch)  
2. **Update STAC/DCAT/PROV catalogs** (new versions, flags, lineage)  
3. **Update the Neo4j graph** (versions, edges, status tags)  
4. **Surface through API & UI** (default versions, ribbons, filters, Story Nodes)

Rule of thumb:

> Prefer **additive / branching** over destructive mutation. Never drop provenance.

---

## 🔁 Canonical Mapping (Event → Action)

~~~text
Legend:
- ETL Action      → src/pipelines/** behavior
- Catalog Action  → STAC/DCAT/PROV updates
- Graph Action    → Neo4j nodes/edges/tags
~~~

| event_kind            | status      | ETL Action                                                                | Catalog Action (STAC/DCAT)                                         | Graph Action (Neo4j)                                              |
|-----------------------|------------:|---------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|
| product-availability  | ongoing     | **Pause** fresh fetch; mark source line **unverified**; backlog tasks    | Add `kfm:ingest_state=paused`, `kfm:qc=unverified`, `kfm:reason`   | Freeze edges from latest `Item→Collection`; add `:Paused` tag     |
| product-availability  | resolved    | **Requeue** backfill window; resume normal ingest                        | Clear pause flags; append new `DatasetVersion` with backfill note  | Unfreeze edges; link new version; add `:Backfilled` event node    |
| reprocessing          | (any)       | **Pin** prior version for reads; ingest new line **in parallel**         | New `Item`/`Version` with `processing_level` consistent; `altlineage` | Branch version node; dual edges (old=`active`, new=`candidate`) |
| algorithm-change      | (any)       | **Branch** collections; update `processing_level` & schema if needed     | New `Collection` (major) or `processing:minor` (minor changes)     | New branch; update constraints; annotate model hash/SBOM          |

> Routing invariant: read-paths remain stable; **default version** changes only via explicit event handling.

---

## 🧩 Minimal Routing Logic (Pseudo-Config)

Router configuration MUST be **declarative** (no hard-coded logic in handlers). Example:

~~~yaml
when:
  - match: { event_kind: "product-availability", status: "ongoing" }
    do:
      - etl.pause: true
      - etl.backlog.create: true
      - catalog.flags:
          kfm:ingest_state: "paused"
          kfm:qc: "unverified"
      - graph.tag:
          collection: ":Paused"

  - match: { event_kind: "product-availability", status: "resolved" }
    do:
      - etl.requeue_backfill:
          window: "last_known_gap"
      - catalog.new_version:
          note: "backfill after outage"
      - catalog.flags:
          kfm:ingest_state: "active"
          kfm:qc: "verified"
      - graph.unfreeze:
          collection: true

  - match: { event_kind: "reprocessing" }
    do:
      - etl.pin_previous: true
      - etl.parallel_ingest_new_line: true
      - catalog.new_version:
          lineage: "altlineage"
      - graph.dual_edges:
          old: "active"
          new: "candidate"

  - match: { event_kind: "algorithm-change" }
    do:
      - etl.branch_collection: true
      - catalog.bump_processing_level: true
      - graph.branch_and_annotate:
          model_hash: "<sha256>"
          sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
~~~

Actual router config lives under:

- `configs/events/router-events-routing.yaml`  

and MUST be referenced in CI and provenance.

---

## 🏷️ Required Metadata Flags (STAC/DCAT)

### STAC

On **Collections** and (when applicable) **Items**:

- `kfm:ingest_state` ∈ `{ "active", "paused" }`  
- `kfm:qc` ∈ `{ "verified", "unverified" }`  
- `kfm:version` — semantic version or derivation hash (string)  
- `kfm:processing_level` — aligns to algorithm / processing line  
- `kfm:event_ref` — canonical event identifier for the last state change  

Example (Collection):

~~~json
{
  "type": "Collection",
  "id": "noaa-hrrr",
  "properties": {
    "kfm:ingest_state": "paused",
    "kfm:qc": "unverified",
    "kfm:version": "v2025.12.10",
    "kfm:processing_level": "analysis",
    "kfm:event_ref": "evt-2025-12-10-hrrr-outage"
  }
}
~~~

### DCAT

On **Datasets**:

- `dct:hasVersion`, `dct:isVersionOf`  
- `prov:wasDerivedFrom` (prior version or upstream dataset)  
- `dcat:versionNotes` — short description: outage, backfill, reprocess, algo-change  
- `kfm:event_ref` — same canonical event id used in STAC  

Example (Dataset):

~~~json
{
  "@type": "dcat:Dataset",
  "dct:identifier": "noaa-hrrr",
  "dct:isVersionOf": "noaa-hrrr-root",
  "dct:hasVersion": "v2025.12.10",
  "prov:wasDerivedFrom": "noaa-hrrr:v2025.12.01",
  "dcat:versionNotes": "Paused ingest due to provider outage; pending backfill.",
  "kfm:event_ref": "evt-2025-12-10-hrrr-outage"
}
~~~

---

## 🧪 CI / Checks (Gate Publishing)

Event-driven changes MUST NOT reach production catalogs or graph unless all checks pass:

- **Great Expectations** (or equivalent) test suites:
  - per branch / per DatasetVersion  
  - validate data quality under both `active` and `candidate` lines

- **OpenLineage**:
  - emit lineage events on transitions:
    - pause / resume  
    - reprocessing start / completion  
    - algorithm-change deployment

- **Schema / Contract** (KFM-PDC v11):
  - fail on schema drift  
  - enforce required STAC/DCAT and `kfm:*` fields

- **Provenance**:
  - append PROV `Activity` per event-driven run  
  - capture `prov:Agent` for operators and services

- **Energy / Carbon** (FAIR+CARE-aligned):
  - OTel metrics for runtime / energy impact during parallel runs  
  - comparisons between old and new lines (for governance & sustainability dashboards)

CI workflow:

- `.github/workflows/events-routing.yml`

MUST:

- validate router config syntax  
- dry-run routing decisions on a curated event fixture set  
- run STAC/DCAT schema validation and mission-tag / event-flag checks  

---

## 🧱 Graph Constraints (Neo4j)

Graph-level invariants ensure stable reads and safe branching.

### Versioning constraints

- `(:Dataset)-[:HAS_VERSION]->(:DatasetVersion { kfm_version })`  
- At most **one** `DatasetVersion` per `Dataset` may be tagged as `active_default = true`.

During reprocessing:

- There MAY be:
  - one `DatasetVersion` with `{ active_default: true, role: "active" }`  
  - one `DatasetVersion` with `{ active_default: false, role: "candidate" }`  
- CI must ensure the router never results in **two** defaults.

### Algorithm-change constraints

- A major algorithm-change SHOULD produce a new `(:Collection)` with:
  - incremented `processing_level` or equivalent  
  - references back via `:DERIVED_FROM_COLLECTION` edges  
- The old `Collection` remains queryable and linked to its `DatasetVersion`s.

Example (informal):

- `(c_old:Collection { id: "sentinel-2-l2a-2025" })`  
- `(c_new:Collection { id: "sentinel-2-l2a-2026" })`  
- `(c_new)-[:DERIVED_FROM_COLLECTION]->(c_old)`

Graph ingestion under `src/graph/events/ingest_events.py` MUST enforce these invariants.

---

## 🧰 Operator Playbook Snippets

These commands are illustrative CLI patterns (actual CLI lives under `tools/kfm-cli/`).

### Pause (ongoing outage)

~~~bash
kfm etl pause --source NOAA-HRRR --reason "API degraded" --backlog create
kfm catalog flag --collection hrrr \
  --set kfm:ingest_state=paused,kfm:qc=unverified
kfm graph tag --collection hrrr --add :Paused
~~~

### Resolve + Backfill

~~~bash
kfm etl backfill --source NOAA-HRRR --window "2025-12-05..2025-12-10"
kfm catalog version --collection hrrr \
  --note "post-outage backfill"
kfm graph unfreeze --collection hrrr
~~~

### Reprocessing (parallel)

~~~bash
kfm etl pin --collection landsat-8 --version 2025.12.05
kfm etl ingest --collection landsat-8 \
  --line "reproc-2025-12" --parallel
~~~

### Algorithm Change (branch)

~~~bash
kfm etl branch --collection sentinel-2 --processing-level L2A-2026
kfm catalog new-collection --from sentinel-2 --processing-level L2A-2026
~~~

All operator actions MUST be reflected as events in `data/events/` and PROV bundles.

---

## 🧭 Decision Tree (Quick Reference)

1. **Is the product temporarily unavailable?**  
   → `event_kind=product-availability`, `status=ongoing`  
   → **Pause** ingest + mark `unverified` + create backlog.

2. **Has it recovered?**  
   → `event_kind=product-availability`, `status=resolved`  
   → **Requeue backfill** + resume ingest + update version and flags.

3. **Is the supplier reprocessing old data?**  
   → `event_kind=reprocessing`  
   → **Pin old** for reads + **parallel ingest** new line + dual edges.

4. **Did the algorithm change?**  
   → `event_kind=algorithm-change`  
   → **Branch collection** + bump `processing_level` + update constraints.

---

## 🧩 UI / API Consistency Notes

- **API defaults**:
  - Default read path points to `DatasetVersion` with `active_default=true`.  
  - APIs SHOULD provide toggles for:
    - `candidate` versions  
    - historical versions by `kfm:version` or PROV id.

- **Story Nodes**:
  - Must display event ribbons:
    - paused  
    - backfill  
    - reprocessing  
    - algorithm branch
  - Link directly to:
    - associated STAC Collections / DCAT datasets  
    - PROV Activities and Agents  
    - affected `DatasetVersion` graph nodes.

- **Focus Mode diffs**:
  - Show STAC/DCAT field deltas (before vs after event).  
  - Visualize graph edge changes (e.g., which edges were frozen/unfrozen).

---

## ✅ Acceptance Criteria

An event-driven change is considered **acceptable** when:

- No **orphaned STAC Items** or **dangling graph edges** remain after transitions.  
- Read-path stability: previously resolvable URIs remain resolvable (even if they no longer represent the default version).  
- PROV chain is continuous:
  - every new `DatasetVersion` has `prov:wasDerivedFrom`.  
- SBOM and SLSA attestations are **updated** for algorithm changes and reprocessing pipelines.  
- Telemetry records:
  - routing decisions  
  - CI outcomes  
  - energy/carbon metrics (for FAIR+CARE review).

---

## 🕰️ Version History

| Version  | Date       | Description                                                                 |
|----------|------------|-----------------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Aligned with KFM-MDP v11.2.6; added directory layout and CI/graph details. |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Reliability Guild** and **Metadata Council**, with co-review by the Governance Council  
- must be updated whenever KFM changes event routing semantics, catalog-graph mappings, or rollback policies

Edits require approval from the Reliability Guild and Metadata Council and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and events-routing validation in CI.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🧭 **Kansas Frontier Matrix — Event→Action Map (STAC/DCAT/Graph Alignment) v11.2.x**  
Deterministic Events · Catalog–Graph Harmony · FAIR+CARE Aligned  

[📘 Docs Root](../README.md) · [📂 Standards Index](../standards/README.md) · [📡 Events Index](./README.md) · [⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>