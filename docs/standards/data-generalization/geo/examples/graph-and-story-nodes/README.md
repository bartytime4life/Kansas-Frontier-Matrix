---
title: "🧠 KFM v11.2.3 — Geo Generalization: Graph & Story Node Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Worked examples showing how generalized geospatial data is represented in the KFM Neo4j graph and Story Nodes, with FAIR+CARE-aware patterns."
path: "docs/standards/data-generalization/geo/examples/graph-and-story-nodes/README.md"
version: "v11.2.3"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Metadata WG"
content_stability: "stable"
backward_compatibility: "Compatible with KFM v11.x data-generalization standards"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards:data-generalization:geo:examples:graph-and-story-nodes:v11.2.3"
semantic_document_id: "kfm-data-generalization-geo-graph-and-story-node-examples-v11.2.3"
event_source_id: "ledger:kfm:standards:data-generalization:geo:examples:graph-and-story-nodes:v11.2.3"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/docs-data-generalization-examples-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_kind: "Guide"
intent: "data-generalization-geo-graph-storynode-examples"
status: "Active / Reference"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (examples only)"
sensitivity: "General (example data only; no real coordinates)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/data-generalization-geo-graph-storynode-examples-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-generalization-geo-graph-storynode-examples-v1.shape.ttl"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major examples update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "unverified-architectural-claims"
  - "narrative-fabrication"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🧠 **KFM v11.2.3 — Geo Generalization: Graph & Story Node Examples**  
`docs/standards/data-generalization/geo/examples/graph-and-story-nodes/README.md`

**Purpose**  
Provide **concrete, end‑to‑end examples** showing how **generalized geospatial data** (e.g., H3 cells, buffered regions, fuzzy polygons) are:

1. Represented in the **Neo4j graph** with KFM‑OP v11 nodes and relationships, and  
2. Connected to **Story Nodes v3** and **Focus Mode v3** narratives,  

…while preserving FAIR+CARE, sovereignty, and data‑generalization rules from the KFM data‑generalization standards.

</div>

---

## 📘 Overview

This guide is **example‑only** and does **not** introduce new normative rules. It illustrates:

- How a **sensitive point** (e.g., archaeological site, cultural location) is generalized into:
  - A **generalized region** node (e.g., H3 cell, watershed region).  
  - One or more **Story Nodes** that speak about that region without exposing precise coordinates.

- How to wire those artifacts through the KFM pipeline:

  1. Deterministic ETL → generalized geometry.  
  2. STAC / DCAT / PROV catalogs record the generalized asset.  
  3. Neo4j receives example nodes and relationships.  
  4. Story Nodes reference the generalized region and graph IDs.  
  5. Focus Mode uses these links to provide **safe narratives** in the UI.

All coordinates and IDs in this guide are **synthetic** and **non‑sensitive**, and must be treated as **patterns**, not production data.

---

## 🗂️ Directory Layout

Recommended layout for this example set:

~~~text
📂 docs/standards/data-generalization/geo/examples/graph-and-story-nodes/
├── 📄 README.md                      # ← This file (patterns + narrative)
│
├── 📂 cypher/                        # Example Neo4j patterns (non-normative)
│   ├── 📄 floodplain_h3_example.cypher
│   ├── 📄 archaeology_region_example.cypher
│   └── 📄 shared_schema_snippets.cypher
│
├── 📂 story-nodes/                   # Example Story Node v3 JSON
│   ├── 📄 floodplain_h3_story_node.json
│   └── 📄 archaeology_region_story_node.json
│
└── 📂 stac-snippets/                 # Optional STAC snippets for context
    ├── 📄 generalized_floodplain_item.json
    └── 📄 generalized_cultural_region_collection.json
~~~

**Directory rules (examples scope):**

- Files here are **illustrative** and MUST NOT be treated as production catalogs or graph migrations.  
- Any example promoted into production MUST:
  - Move into the appropriate **pipeline, graph, or data** directory.  
  - Gain its own KFM‑MDP v11‑compliant documentation and governance review.

---

## 🧭 Context

These examples sit at the intersection of:

- `docs/standards/data-generalization/` — how we **generalize geometry** (e.g., H3, buffers, region rollups).  
- `docs/standards/faircare.md` — how we **reason about sovereignty, cultural sensitivity, and ethical use.**  
- `docs/standards/catalogs/` — how generalized assets appear in **STAC / DCAT catalogs.**  
- `src/graph/` — how generalized regions are stored in **Neo4j.**  
- `docs/architecture/story_nodes/` (or equivalent) — how **Story Node v3** references these graph entities.

These examples assume:

- A KFM‑OP v11 graph with labels such as `Place`, `GeneralizedRegion`, `Dataset`, `StoryNode`.  
- A data‑generalization pipeline that can map **raw sensitive geometries → generalized regions** deterministically.  
- Catalog entries (STAC/DCAT) that describe only the generalized geometry in public views.

---

## 🧠 Story Node & Focus Mode Integration

This section shows **paired examples**: how we model generalized spatial entities in Neo4j and expose them to Story Nodes.

### 1. Example Graph Pattern (Floodplain H3 Cell)

**Goal:** Represent a generalized floodplain region derived from raw hydrology data and connect it to a Story Node.

#### 1.1 Example Cypher (Pattern)

~~~text
// Create a generalized region representing an H3 cell (synthetic ID)
CREATE (r:GeneralizedRegion {
  kfm_id: "urn:kfm:region:h3:r7:8a2a1072b59ffff",
  kind: "h3_cell",
  h3_resolution: 7,
  region_code: "H3_R7_8A2A1072B59F",
  label: "Central Kansas Floodplain Region (Generalized)",
  geometry_ref: "stac:item:generalized_floodplain_2025:h3_r7_8a2a1072b59ffff",
  sensitivity: "generalized",
  created_at: datetime("2025-11-20T00:00:00Z")
})

// Example dataset that produced the generalized region
CREATE (d:Dataset {
  kfm_id: "urn:kfm:dataset:hydro:floodplain:2025:v1",
  title: "Kansas Floodplain Model 2025 (Generalized)",
  contract_ref: "data-contracts/hydro_floodplain_2025.json"
})

// Example Story Node shell (graph-side reference, not the full JSON representation)
CREATE (sn:StoryNode {
  kfm_id: "urn:kfm:story-node:hydro:floodplain:h3_r7_8a2a1072b59ffff:v1",
  title: "Floodplains in Central Kansas (Generalized View)"
})

// Relationships
CREATE (r)-[:DERIVED_FROM]->(d)
CREATE (sn)-[:FOCUSES_ON_REGION]->(r)
CREATE (sn)-[:USES_DATASET]->(d);
~~~

**Notes**

- `GeneralizedRegion` is **explicitly marked** as generalized (`sensitivity: "generalized"`).  
- `geometry_ref` points to the STAC Item that contains the generalized geometry only.  
- `StoryNode` is linked via semantics, not raw point location.

#### 1.2 Example Story Node JSON (Hydro)

~~~text
{
  "id": "urn:kfm:story-node:hydro:floodplain:h3_r7_8a2a1072b59ffff:v1",
  "title": "Floodplains in Central Kansas (Generalized View)",
  "kind": "narrative",
  "version": "v1.0.0",
  "target_region": {
    "kind": "GeneralizedRegion",
    "kfm_id": "urn:kfm:region:h3:r7:8a2a1072b59ffff",
    "display_name": "Central Kansas Floodplain Region (Generalized)"
  },
  "graph_links": {
    "region_node_id": "urn:kfm:region:h3:r7:8a2a1072b59ffff",
    "dataset_node_id": "urn:kfm:dataset:hydro:floodplain:2025:v1"
  },
  "spatial_extent": {
    "type": "H3",
    "value": "8a2a1072b59ffff",
    "resolution": 7
  },
  "temporal_extent": {
    "start": "2025-01-01T00:00:00Z",
    "end": "2025-12-31T23:59:59Z"
  },
  "narrative": [
    {
      "type": "paragraph",
      "text": "This Story Node describes modeled floodplain behavior across a generalized region of central Kansas. Rather than revealing parcel-level detail, it aggregates patterns at the scale of a coarse H3 cell."
    },
    {
      "type": "paragraph",
      "text": "Use this view to understand broad flood risk and regional hydrology trends. For parcel-level policy or infrastructure planning, consult local authorities and restricted datasets governed under FAIR+CARE."
    }
  ],
  "care": {
    "status": "approved",
    "statement": "Example-only generalized region; no real-world parcel or household detail.",
    "reviewer": "KFM FAIR+CARE Council (examples domain)",
    "date_reviewed": "2025-11-25"
  }
}
~~~

### 2. Example Graph Pattern (Cultural / Archaeological Region)

For culturally sensitive data, the pattern is similar, but **care blocks and region semantics** become more important.

#### 2.1 Example Cypher (Pattern)

~~~text
// Generalized cultural region (e.g., watershed-scale or county-scale, synthetic)
CREATE (cr:GeneralizedRegion {
  kfm_id: "urn:kfm:region:cultural:watershed:demo-001",
  kind: "cultural_region",
  generalization_method: "watershed-region",
  label: "Example Cultural Landscape Region (Generalized)",
  geometry_ref: "stac:item:generalized_cultural_region_demo_001",
  sensitivity: "generalized",
  cultural_sensitivity: "potential",
  created_at: datetime("2025-11-22T00:00:00Z")
})

CREATE (cd:Dataset {
  kfm_id: "urn:kfm:dataset:cultural:demo:2025:v1",
  title: "Example Cultural Landscape Dataset (Generalized)",
  contract_ref: "data-contracts/cultural_landscape_demo_2025.json"
})

CREATE (sn:StoryNode {
  kfm_id: "urn:kfm:story-node:cultural:landscape:demo-001:v1",
  title: "A Generalized View of a Cultural Landscape"
})

CREATE (cr)-[:DERIVED_FROM]->(cd)
CREATE (sn)-[:FOCUSES_ON_REGION]->(cr)
CREATE (sn)-[:USES_DATASET]->(cd);
~~~

#### 2.2 Example Story Node JSON (Cultural)

~~~text
{
  "id": "urn:kfm:story-node:cultural:landscape:demo-001:v1",
  "title": "A Generalized View of a Cultural Landscape",
  "kind": "narrative",
  "version": "v1.0.0",
  "target_region": {
    "kind": "GeneralizedRegion",
    "kfm_id": "urn:kfm:region:cultural:watershed:demo-001",
    "display_name": "Example Cultural Landscape Region (Generalized)"
  },
  "graph_links": {
    "region_node_id": "urn:kfm:region:cultural:watershed:demo-001",
    "dataset_node_id": "urn:kfm:dataset:cultural:demo:2025:v1"
  },
  "spatial_extent": {
    "type": "NamedRegion",
    "value": "demo-001",
    "generalization": "watershed-region"
  },
  "temporal_extent": {
    "start": "1800-01-01T00:00:00Z",
    "end": "1900-12-31T23:59:59Z"
  },
  "narrative": [
    {
      "type": "paragraph",
      "text": "This Story Node offers an abstract view of a cultural landscape. Exact locations, site counts, and sensitive attributes are withheld or aggregated to protect community sovereignty and cultural protocols."
    },
    {
      "type": "paragraph",
      "text": "The aim is to support education and broad-scale planning without exposing details that could enable looting, misrepresentation, or harm."
    }
  ],
  "care": {
    "status": "restricted",
    "authority_to_control": "Example Tribal Nation (placeholder)",
    "statement": "This example illustrates how restricted regions would be modeled. In production, any similar content requires explicit governance approval.",
    "date_reviewed": "2025-11-25"
  }
}
~~~

---

## 🧪 Validation & CI/CD

Even for examples, we follow **KFM‑style validation** to keep patterns trustworthy.

### 1. Example Checks

- **Schema validation**  
  - Story Node JSON snippets validate against the Story Node v3 schema.  
  - Graph patterns are checked by:
    - a lightweight **Cypher linter** (syntax).  
    - optional **test migrations** in a sandbox Neo4j instance.

- **Provenance hooks**  
  - Example STAC snippets include:
    - clearly marked `id`, `title`, and `description` as **example‑only**.  
    - no real coordinates or sensitive DOIs.

- **Docs validation**  
  - This README passes:
    - `markdown-lint`  
    - `schema-lint` (front‑matter)  
    - `metadata-check`  
    - `footer-check`  
    - `provenance-check`

### 2. Telemetry Notes (Examples)

Example CI runs may emit telemetry like:

~~~text
{
  "event": "example_validation",
  "scope": "data-generalization-geo-graph-storynode-examples",
  "status": "success",
  "timestamp": "2025-12-07T12:00:00Z"
}
~~~

Production telemetry MUST NOT count these examples as production datasets, but MAY track them under a dedicated `examples` or `sandbox` domain.

---

## ⚖ FAIR+CARE & Governance

These examples are designed to **demonstrate** how FAIR+CARE and sovereignty rules play out in practice:

- **No raw sensitive points** appear in any example.  
- All spatial references are:
  - generalized cells (`H3` or similar), or  
  - abstract region codes (`demo-001`), or  
  - synthetic bounding boxes.

- **CARE semantics**:
  - The `care` block in Story Nodes encodes:
    - status (`approved`, `restricted`),  
    - authority to control,  
    - ethical statements & review dates.

- **Sovereignty**:
  - Any real deployment of patterns like the cultural example MUST:
    - reference `../../../../faircare/FAIRCARE-GUIDE.md` and  
      `../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md`.  
    - undergo FAIR+CARE Council review.

These examples are thus **safe starting points** that operational teams can adapt into governed, real‑world implementations.

---

## 🕰️ Version History

| Version  | Date       | Author                | Summary                                                                                     |
|---------:|------------|----------------------|---------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-07 | KFM Core / Examples  | Initial examples guide for geo generalization → graph → Story Nodes; aligned with KFM‑MDP v11.2.4 and data‑generalization, FAIR+CARE, and catalog standards. |

---

<div align="center">

🧠 **KFM v11.2.3 — Geo Generalization: Graph & Story Node Examples**  
Patterns for connecting generalized geospatial data to narratives, safely and ethically.

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Data Generalization Index](../../../README.md) ·  
[📚 Catalog Standards Index](../../catalogs/README.md) ·  
[⚖ Root Governance Charter](../../../../governance/ROOT-GOVERNANCE.md)

</div>

