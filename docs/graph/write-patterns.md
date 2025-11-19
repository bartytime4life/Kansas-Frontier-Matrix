---
title: "🧩 Kansas Frontier Matrix — Graph Write Patterns & Lineage-Safe Upserts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/graph/write-patterns.md"

# Versioning & Release
version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Guaranteed for all v10.x → v11.x pipelines"

# Git Commit & Integrity
commit_sha: "<latest-commit-hash>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"

# SBOM, Manifest, Telemetry
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/graph-write-patterns-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

# Governance & Standards
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
risk_profile: "Low Risk · Automatic Lineage Enforcement · Strict Provenance Required"

# Protocol Versions
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

# Document Classification
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "graph-write-patterns"
category: "Graph · Lineage · Write Safety"
sensitivity: "General (Non-sensitive) — auto-masked for protected datasets"

# Lineage, Ontology, Metadata
prov_profile: "PROV-O Core + KFM Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"
ontology_ref:
  - "../graph/ontology/cidoc-crm-mapping.md"
  - "../graph/ontology/spatial-temporal-patterns.md"
  - "../graph/ontology/core-entities.md"
metadata_profiles:
  - "../../schemas/dcat/kfm-dcat-v11.json"
  - "../../schemas/stac/kfm-stac-v11.json"
  - "../../schemas/jsonld/kfm-context-v11.json"

# Validation & CI
validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-audit-v11"
  - "governance-audit-v11"
ci_integration:
  workflow: ".github/workflows/kfm-pipelines.yml"
  environment: "staging → production (governed promotion)"

# FAIR + CARE
fair_category: "F1-A1-I1-R1"
care_compliance: "CARE-Compliant · Provenance-Enforced · Sensitivity-Aware"

# Runtime Infrastructure
runtime:
  graph_engine: "Neo4j Enterprise v5.x"
  lineage_bus: "OpenLineage v2.5"
  governance_hooks: "GovHooks v4"
  reliability_framework: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"
  ai_agents: "LangGraph Autonomous Updater v11"

---
<div align="center">

# 🧩 **Kansas Frontier Matrix**  
## **Graph Write Patterns & Lineage-Safe Upserts**  
`docs/graph/write-patterns.md`

[![Docs – MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-4B32C3)](#)
[![License – MIT](https://img.shields.io/badge/License-MIT-2EA44F)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-009688)](#)
[![Status – Diamond⁹ Ω / Crown∞Ω](https://img.shields.io/badge/Status-Diamond⁹%20Ω%20%2F%20Crown∞Ω-512DA8)](#)
[![Neo4j Graph](https://img.shields.io/badge/Backend-Neo4j%20Graph-008CC1)](#)
[![Reliability](https://img.shields.io/badge/Pipelines-Reliable%20Upserts%20%2F%20Rollback-795548)](#)

</div>

--- ✦ ---

## 1. 🧭 Overview

This document defines the **v11 canonical graph write patterns** for the Kansas Frontier Matrix (KFM), governing:

- deterministic & idempotent writes  
- lineage-safe upserts  
- PROV-O + OpenLineage integration  
- rollback-ready versioning  
- ontology-aligned entity modeling  
- Focus Mode v3 compatibility  
- reliability (WAL → Retry → Rollback → Hotfix → Lineage)

All writes follow:

> `data → ETL/AI pipelines → Neo4j Graph → FastAPI/GraphQL → React+MapLibre → Story Nodes → Focus Mode`

These patterns are **mandatory** for:

- ETL pipelines (`src/pipelines/graph/*`)  
- Autonomous updaters (LangGraph)  
- CI/CD workflows performing graph mutations  
- Ontology-governed ingest operations  

--- ✦ ---

## 2. 🎯 Scope & Intended Audience

**Applies to:**

- Neo4j writes (nodes, relationships, properties)  
- Provenance edges (PROV-O / KFM lineage extensions)  
- OpenLineage emission  
- Versioning & soft deletion  
- Other pipeline components that perform mutations  

**Excludes:**

- Ontology deep spec → `docs/graph/ontology/*.md`  
- API read-patterns → `web/ARCHITECTURE.md`  
- Reliability plane internals → `docs/pipelines/reliable-pipelines.md`  

--- ✦ ---

## 3. 🏛️ Architecture at a Glance

~~~mermaid
graph TD
  A[Raw Datasets · NOAA · USGS · KSHS · Tribal Archives] --> B[ETL / AI Pipelines<br/>LangGraph · CrewAI · Python]
  B --> C[Validated Staging<br/>STAC · DCAT · JSON-LD]
  C --> D[Idempotent Upserts<br/>Neo4j MERGE Patterns]
  D --> E[Lineage Layer<br/>PROV-O · OpenLineage]
  E --> F[Knowledge APIs<br/>FastAPI · GraphQL]
  F --> G[Focus Mode v3 · Story Nodes<br/>MapLibre · Cesium · Timeline]
~~~

--- ✦ ---

## 4. 🧱 Design Principles (v11)

1. **Stable IDs (`kfm_id`)**  
   Deterministic, ontology-aligned, used for every MERGE.

2. **Pre-declared Constraints**  
   All entity types must have uniqueness constraints before pipelines run.

3. **Idempotent Writes**  
   Retriable, atomic, deterministic.

4. **Lineage-Embedded**  
   Every write links to:
   - Source (Dataset, Collection, Archive)  
   - Run (IngestRun / TransformRun)  

5. **OpenLineage-Driven**  
   All pipelines emit START → COMPLETE/FAIL for governance transparency.

6. **Temporal Safety**  
   Soft versioning using `v`, `v_from`, `v_to`, `v_tag`.

7. **Rollback-Compatible**  
   No destructive deletes—soft deletes with provenance.

--- ✦ ---

## 5. 🧩 Node Upsert Pattern (Idempotent MERGE)

### 5.1 Minimal Pattern

~~~cypher
MERGE (p:Place {kfm_id: $kfm_id})
  ON CREATE SET
    p.name        = $name,
    p.created_at  = datetime(),
    p.v           = $version,
    p.source      = $source,
    p.kind        = $kind,
    p.geom_wkt    = $geom_wkt
  ON MATCH SET
    p.name        = coalesce($name, p.name),
    p.updated_at  = datetime(),
    p.v           = $version;
~~~

### 5.2 Constraint (Required)

~~~cypher
CREATE CONSTRAINT place_kfm_id_unique IF NOT EXISTS
FOR (p:Place)
REQUIRE p.kfm_id IS UNIQUE;
~~~

--- ✦ ---

## 6. 🔗 Relationship Upsert Patterns

### 6.1 With Stable ID

~~~cypher
MATCH (a:Place {kfm_id: $a_id})
MATCH (b:Place {kfm_id: $b_id})

MERGE (a)-[r:CONNECTED_TO {kfm_id: $rel_id}]->(b)
  ON CREATE SET r.strength = $strength, r.kind = $kind, r.created_at = datetime(), r.v = $version
  ON MATCH  SET r.strength = $strength, r.updated_at = datetime(), r.v = $version;
~~~

Constraint:

~~~cypher
CREATE CONSTRAINT rel_connected_to_kfm_id_unique IF NOT EXISTS
FOR ()-[r:CONNECTED_TO]-()
REQUIRE r.kfm_id IS UNIQUE;
~~~

### 6.2 Without Stable ID

~~~cypher
MATCH (a:Dataset {kfm_id: $dataset_id})
MATCH (b:Place   {kfm_id: $place_id})

MERGE (a)-[r:COVERS]->(b)
  ON CREATE SET r.created_at = datetime(), r.v = $version
  ON MATCH  SET r.updated_at = datetime(), r.v = $version;
~~~

--- ✦ ---

## 7. 🧬 Lineage: PROV-O Patterns

### 7.1 Source Provenance

~~~cypher
MERGE (src:Source {uri: $source_uri})
  ON CREATE SET src.name = $source_name, src.kind = $source_kind, src.created_at = datetime()
  ON MATCH SET src.last_seen_at = datetime();

MATCH (p:Place {kfm_id: $kfm_id})
MERGE (p)-[:`prov:wasDerivedFrom`]->(src);
~~~

### 7.2 Run-Level Provenance

~~~cypher
MERGE (run:IngestRun {run_id: $run_id})
  ON CREATE SET
    run.job_name   = $job_name,
    run.started_at = datetime($run_started_at),
    run.env        = $env,
    run.commit_sha = $commit_sha,
    run.pipeline   = $pipeline_name
  ON MATCH SET run.last_seen_at = datetime();

MATCH (p:Place {kfm_id: $kfm_id})
MERGE (p)-[:`prov:wasGeneratedBy`]->(run);
~~~

--- ✦ ---

## 8. ⏱️ Soft Versioning & Time-Travel

### 8.1 Version Windowing

~~~cypher
MATCH (p:Place {kfm_id: $kfm_id})
SET p.v_tag = $version_tag,
    p.v_from = coalesce(p.v_from, datetime()),
    p.v_to = null;
~~~

### 8.2 Soft Delete

~~~cypher
MATCH (p:Place {kfm_id: $kfm_id})
SET p.deleted = true,
    p.deleted_at = datetime(),
    p.deleted_by = $run_id,
    p.v_to = coalesce(p.v_to, datetime());
~~~

--- ✦ ---

## 9. 📡 OpenLineage Pattern

~~~json
{
  "eventType": "COMPLETE",
  "job": { "namespace": "kfm.ingest", "name": "places_upsert" },
  "run": { "runId": "<run-id>" },
  "inputs": [
    { "namespace": "s3://kfm-staging", "name": "places.parquet" }
  ],
  "outputs": [
    { "namespace": "neo4j://kfm", "name": "Place" }
  ],
  "producer": "kfm://pipelines/v11.0.0"
}
~~~

--- ✦ ---

## 10. 🔁 CI/CD Integration

Stages:

1. **Validate** (STAC/DCAT/JSON-LD)  
2. **Dry-run graph upsert** (`--dry-run`)  
3. **Reliability guards** (WAL/Retry/Rollback)  
4. **Apply** (`--apply` + OpenLineage events)

--- ✦ ---

## 11. 📐 Required Constraints

~~~cypher
CREATE CONSTRAINT place_kfm_id_unique IF NOT EXISTS
FOR (p:Place)
REQUIRE p.kfm_id IS UNIQUE;

CREATE CONSTRAINT source_uri_unique IF NOT EXISTS
FOR (s:Source)
REQUIRE s.uri IS UNIQUE;

CREATE CONSTRAINT dataset_kfm_id_unique IF NOT EXISTS
FOR (d:Dataset)
REQUIRE d.kfm_id IS UNIQUE;

CREATE CONSTRAINT ingest_run_id_unique IF NOT EXISTS
FOR (r:IngestRun)
REQUIRE r.run_id IS UNIQUE;

CREATE CONSTRAINT connected_to_kfm_id_unique IF NOT EXISTS
FOR ()-[r:CONNECTED_TO]-()
REQUIRE r.kfm_id IS UNIQUE;
~~~

--- ✦ ---

## 12. 🗂️ Directory Layout

~~~text
docs/
└── graph/
    ├── write-patterns.md
    └── ontology/
        ├── README.md
        ├── cidoc-crm-mapping.md
        └── spatial-temporal-patterns.md

src/
└── pipelines/
    ├── graph/
    │   ├── upsert_places.py
    │   ├── upsert_datasets.py
    │   ├── upsert_relationships.py
    │   └── lineage/
    │       ├── openlineage_emitter.py
    │       └── prov_links.py
    └── reliability/
        ├── wal/
        ├── rollback/
        └── retry/

.github/
└── workflows/
    └── kfm-pipelines.yml

schemas/
└── telemetry/
    └── graph-write-patterns-v1.json
~~~

--- ✦ ---

## 13. ✅ Implementation Checklist

- [ ] Stable IDs (`kfm_id`)  
- [ ] Constraints present  
- [ ] MERGE-based upserts  
- [ ] Lineage links (Source + Run)  
- [ ] Versioning tags  
- [ ] Soft-delete instead of hard-delete  
- [ ] OpenLineage events emitted  
- [ ] Reliability guards active  
- [ ] CI validation passes  

--- ✦ ---

## 14. 🛡️ Evolution & Governance

All changes must pass:

- **FAIR+CARE review**  
- **Ontology integrity check**  
- **Lineage completeness audit**  
- **CI docs-lint + schema-lint**  
- **Governed promotion (staging → production)**  

--- ✦ ---

## 15. 🧰 Quick Snippets

### Node Upsert + Lineage

~~~cypher
MERGE (p:Place {kfm_id: $kfm_id})
  ON CREATE SET p.name = $name, p.created_at = datetime(), p.v = $version
  ON MATCH SET  p.name = coalesce($name, p.name), p.updated_at = datetime(), p.v = $version;

MERGE (src:Source {uri: $source_uri})
MERGE (p)-[:`prov:wasDerivedFrom`]->(src);

MERGE (run:IngestRun {run_id: $run_id})
MERGE (p)-[:`prov:wasGeneratedBy`]->(run);
~~~

--- ✦ ---

## 16. 🕰️ Version History

| Version   | Date       | Notes |
|-----------|------------|-------|
| v11.0.0   | 2025-11-19 | Full v11 upgrade (MDP v11.0, OP v11.0, PDC v11.0). Expanded metadata, governance, sustainability schemas, and lineage extensions. |
| v10.4.3   | 2025-11-19 | Initial lineage-safe write patterns. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
🧩 Lineage-Safe Graph Writes · Diamond⁹ Ω / Crown∞Ω Certified  
FAIR+CARE Compliant · MCP-DL v6.3 · KFM-MDP v11.0 · KFM-OP v11.0  

[⬅ Back to Documentation Index](../README.md) ·  
[Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>