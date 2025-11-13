---
title: "🧩 Kansas Frontier Matrix — STAC Versioning Integration Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/versioning.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/story-nodes-versioning-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — STAC Versioning Integration Guide**  
`docs/reports/visualization/focus_mode/story_nodes/versioning.md`

**Purpose:**  
Implement and govern **STAC Versioning Indicators** within Focus Mode Story Nodes to enable dataset lineage tracking, version scrubbing, diffs, reproducibility locking, and temporal navigation across all KFM visualization layers.

**Certification:**  
Diamond⁹ Ω / Crown∞Ω • FAIR+CARE • ISO 14064 • SLSA v1.0 • SBOM-Tracked

</div>


---

## 🔌 Overview — Integrating STAC Versioning Into the KFM Stack

This guide defines the **complete wiring** of the STAC Versioning Extension into every KFM subsystem that interacts with Story Nodes, including:

- Metadata ingestion (ETL)
- Neo4j knowledge graph
- FastAPI / GraphQL APIs
- React + MapLibre UI
- Story Node schema v2.4
- Telemetry lineage logging
- Reproducibility workflows

All steps adhere to MCP-DL v6.3, FAIR+CARE, and STAC Versioning Indicators Spec v1.0.

---

### 🗂️ Directory Layout

    docs/
    └── reports/
        └── visualization/
            └── focus_mode/
                └── story_nodes/
                    ├── versioning.md
                    ├── schemas/
                    │   └── story-node-v2.4.json
                    ├── examples/
                    │   └── versioning-demo.json
                    └── assets/
                        └── diagrams/
                            └── version-lineage-flow.svg

---

## 🧬 Metadata Ingestion Pipeline

### ⚙️ Step 1 — Extract STAC Versioning Fields

Story Node ETL must parse the following:

- `properties.version`
- `properties.deprecated`
- `links[rel=predecessor]`
- `links[rel=successor]`
- `links[rel=latest]`
- Optional branching lineage via `links[rel=alternate]`

### Required Additions to Story Node Schema (v2.4)

Indented JSON (no fenced blocks):

    {
      "version": "string",
      "is_deprecated": "boolean",
      "lineage": {
        "predecessor": "string|null",
        "successor": "string|null",
        "latest": "string|null"
      }
    }

### ETL Responsibilities

- Normalize all versioning fields  
- Convert HREF references into internal KFM Item IDs  
- Push lineage graph updates to the Provenance Graph Vector (PGV)

---

## 🕸️ Neo4j Knowledge Graph Wiring

### 🧱 Step 2 — Add Version Relationship Types

Relationships:

- `(:Item)-[:PREDECESSOR]->(:Item)`
- `(:Item)-[:SUCCESSOR]->(:Item)`
- `(:Item)-[:LATEST]->(:Item)`

### Migration (Cypher)

    MATCH (i:Item)
    WITH i, i.links AS links
    FOREACH (l IN links |
      CASE l.rel
        WHEN 'predecessor' THEN MERGE (i)-[:PREDECESSOR]->(:Item {id:l.href})
        WHEN 'successor' THEN MERGE (i)-[:SUCCESSOR]->(:Item {id:l.href})
        WHEN 'latest' THEN MERGE (i)-[:LATEST]->(:Item {id:l.href})
      END
    );

---

## 🚦 API Integration Layer (FastAPI / GraphQL)

### 🔍 Endpoints

### 1. **Lineage Resolution**
`GET /stac/items/{id}/lineage`

Returns:

    {
      "predecessors": [],
      "current": {},
      "successors": [],
      "latest": {}
    }

### 2. **Version Diff**
`GET /stac/items/{id}/diff?against={otherId}`

Outputs:

- metadata diff  
- asset inventory diff  
- geometry/extent diff  
- quality flags  

### 3. **Version Lock**
`POST /focus/story-node/{id}/lock-version/{versionId}`

Enables Focus Mode reproducibility.

---

## 🖥️ UI / Front-End Wiring (React + MapLibre)

### 🎛️ Step 4 — Story Node Version Strip

Add a UI element that displays:

- predecessor → current → successor  
- “latest” label  
- deprecated flag  
- version hover previews  
- click-to-diff functionality  
- keyboard arrow navigation  

### 🖼️ Step 5 — Focus Mode Binding

When a version is selected:

- Freeze all map layers to that version  
- Disable auto-updating datasets  
- Lock data panels (charts, tables, histograms)  
- Send telemetry event `version_locked`

---

## 🧪 Diffing Logic — Metadata & Assets

### 🔎 Step 6 — Diff Engine Requirements

- Compare metadata fields  
- Compare asset inventory  
- Geometry diff (GeoDiff) or pixel raster diff  
- Semantic score change detection  
- Unified representation:

    {
      "properties": { "title": ["old", "new"] },
      "assets": { "map": "changed" },
      "geometry": "unchanged"
    }

---

## 🧾 Provenance, Reproducibility & Telemetry

### 🔏 Step 7 — Version Stamping

Every Focus Mode output must embed:

- STAC Item ID  
- Version string  
- Full lineage chain  
- Diff manifest hash  
- Timestamp  
- User + session fingerprint  

### 📡 Telemetry Events

Emit:

- `version_navigated`  
- `version_diffed`  
- `version_locked`  
- `lineage_inspected`  
- `deprecated_warning_shown`  

All stored under `focus-telemetry.json`.

---

## 🚀 End-to-End Flow Diagram

    STAC Item →
      ETL Parser →
        Version Fields Extracted →
          Neo4j Lineage Relationships →
            API: /lineage /diff →
              Story Node →
                UI Version Strip →
                  Focus Mode Version Lock →
                    Telemetry + Reproducibility

---

## 📚 Example Versioned STAC Item

    {
      "id": "ks-landcover-2025-10-31",
      "properties": {
        "version": "2025.10.31",
        "deprecated": false
      },
      "links": [
        { "rel": "latest", "href": "./ks-landcover-2025.json" },
        { "rel": "predecessor", "href": "./ks-landcover-2025-07-15.json" },
        { "rel": "successor", "href": "./ks-landcover-2026-02-01.json" }
      ]
    }

---

## 🕒 Version History

| Version   | Date       | Notes                                                             |
|-----------|------------|-------------------------------------------------------------------|
| v10.2.2   | 2025-11-13 | Initial STAC versioning integration guide for Story Nodes.        |
| v10.2.3   | 2025-11-13 | Updated to full memory-rule compliance + directory layout fix.    |
