---
title: "🏺 Kansas Frontier Matrix — Unified Heritage Standards v11 (Schemas · Examples · Assets)"
path: "docs/standards/heritage/HERITAGE_STANDARDS_v11.md"
version: "v11.0.0"
last_updated: "2025-11-20"

review_cycle: "Annual / FAIR+CARE Council & Focus Mode Board"

commit_sha: "<latest-commit-hash>"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/heritage-standards-v11.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"

status: "Active / Enforced"
doc_kind: "HeritageStandards"
intent: "heritage-standards-v11"
role: "heritage-governance-reference"

fair_category: "F1-A1-I1-R1"
care_label: "Protected / High-Risk"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Heritage Protection"
redaction_required: true

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWork"
  owl_time: "Instant"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/heritage-standards-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/heritage-standards-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:heritage:standards:v11"
semantic_document_id: "kfm-heritage-standards-v11"
event_source_id: "ledger:docs/standards/heritage/HERITAGE_STANDARDS_v11.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
  - "culturally sensitive inference"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Internal Heritage Governance Document"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major KFM heritage revision"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Unified Heritage Standards v11**  
**Schemas · Examples · Assets**  
`docs/standards/heritage/HERITAGE_STANDARDS_v11.md`

**Status:** Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

**Purpose:**  
Provide the complete, canonical **single-source-of-truth** for all **heritage-protection standards** in KFM v11, merging:  
- The **Schemas Index**  
- The **Example Library**  
- The **Assets Index**  

This unified document governs ALL heritage pipelines, visual assets, generalization methods, metadata rules, and FAIR+CARE requirements.

[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold.svg)]()  
[![Markdown KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM--MDP_v11.0.0-blue.svg)]()  
[![License CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)]()

</div>

---

# 📘 Overview

This unified v11 heritage reference defines the **schemas**, **examples**, and **assets** required to:

- Protect culturally sensitive locations  
- Implement spatial masking (H3 generalization)  
- Apply CARE sovereignty fields  
- Validate heritage metadata  
- Control publication via STAC/DCAT  
- Provide reproducible lineage logs (PROV-O)  
- Supply safe/abstracted visuals  

This is the **authoritative** heritage document for KFM v11.

---

# 🧩 Part I — Heritage Standards Schemas (Merged)

## 📐 Schema Directory Layout

```text
schemas/
│
├── h3-generalization-standard.json
├── heritage-sensitive-location.schema.json
├── heritage-dataset.schema.json
├── heritage-protection-flags.schema.json
├── lineage-provenance.schema.json
│
└── examples/
```

## 🧱 Schema Descriptions

### 🧮 `h3-generalization-standard.json`
Defines all H3 rules:  
- Allowed resolutions  
- Removal of raw coordinates  
- Aggregation thresholds  
- NHPA §304 compliance  
- CARE sovereignty overrides  

### 🏺 `heritage-sensitive-location.schema.json`
Defines:  
- Cultural sensitivity levels  
- CARE labels  
- Tribal affiliation fields  
- Prohibited raw lat/lon  
- Required H3 hexes  
- Required sovereignty governance  

### 📦 `heritage-dataset.schema.json`
Defines STAC/DCAT alignment:  
- Dataset metadata  
- Temporal + spatial extent  
- CARE metadata  
- Lineage logs  
- H3 requirements  

### 🔐 `heritage-protection-flags.schema.json`
Defines:  
- Tier I–III protection  
- Display/export restrictions  
- Indexing rules  

### 🧬 `lineage-provenance.schema.json`
Defines PROV-O lineage:  
- `wasDerivedFrom`  
- `generatedBy`  
- SHA256 integrity  
- Workflow versioning  

---

# 🧩 Part II — Example Library (Merged)

## 📚 Example Directory Layout

```text
examples/
│
├── h3-generalization-demo.json
├── sensitive-location-example.json
├── heritage-dataset-stac.json
├── heritage-dataset-dcat.json
├── provenance-lineage-example.json
└── storynode-heritage-demo.json
```

## 🧱 Example: H3 Generalization

```json
{
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "site_count": 4,
  "periods": ["Archaic", "Late Prehistoric"],
  "heritage_protected": true,
  "generalization_method": "H3",
  "raw_coordinates_removed": true,
  "mcp_protected": true,
  "care_level": "Level III"
}
```

## 🏺 Example: Sensitive Location Metadata

```json
{
  "id": "KS-ARCH-004198",
  "type": "heritage_site",
  "cultural_sensitivity": "restricted",
  "legal_basis": "NHPA Section 304",
  "care_level": "Level III",
  "tribal_affiliation": ["Kaw Nation"],
  "description": "Earthen mound feature with significant cultural importance.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "raw_coordinates_removed": true,
  "mcp_protected": true
}
```

## 📦 Example: STAC Item

```json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "ks-heritage-generalized-2025",
  "collection": "kfm-heritage",
  "properties": {
    "heritage_protected": true,
    "care_level": "Level III",
    "generalization_method": "H3",
    "h3_resolution": 7,
    "raw_coordinates_removed": true,
    "mcp_protected": true
  },
  "assets": {
    "hex_geojson": {
      "href": "hexes/ks-heritage-2025.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

## 🗃️ Example: DCAT Metadata

```json
{
  "dct:title": "Kansas Protected Heritage (Generalized to H3-r7)",
  "dct:spatialResolution": "H3-r7",
  "dct:provenance": "Generalized from protected archaeological coordinates.",
  "dct:conformsTo": "KFM Heritage H3 Generalization Standard v11",
  "dct:rights": "NHPA §304 restrictions apply; CARE Level III."
}
```

## 🧬 Example: Lineage Metadata

```json
{
  "version": "2025.11.20",
  "lineage": {
    "predecessor": "2025.07.15",
    "successor": "2026.02.01",
    "latest": "2026.02.01"
  },
  "reproducibility": {
    "workflow_hash": "sha256-b94c...",
    "inputs_hash": "sha256-09af...",
    "prov": {
      "wasDerivedFrom": "urn:kfm:raw:heritage:2025-07-15",
      "generatedBy": "urn:kfm:workflow:heritage-generalization-v11"
    }
  }
}
```

## 🧩 Example: Story Node (Heritage)

```json
{
  "id": "node-ks-heritage-102",
  "type": "story-node",
  "title": "Ancient Mound Site (Generalized)",
  "heritage_protected": true,
  "cultural_sensitivity": "restricted",
  "periods": ["Late Woodland"],
  "summary": "A generalized representation of an important cultural heritage location.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "mcp_protected": true,
  "display_rules": {
    "map": "hex",
    "timeline": true
  },
  "relations": [],
  "spacetime": {
    "geometry": { "type": "Point", "coordinates": [0, 0] },
    "when": { "start": "1600-01-01T00:00:00Z", "precision": "year" }
  }
}
```

---

# 🧩 Part III — Heritage Assets (Merged)

## 🎨 Asset Directory Layout

```text
assets/
│
├── diagrams/
│   ├── h3-protection-flow.svg
│   ├── heritage-protection-overview.svg
│   ├── sensitive-location-governance.svg
│   ├── lineage-flow.svg
│   └── ...
│
├── icons/
│   ├── heritage_protected.svg
│   ├── heritage_level_III.svg
│   ├── cultural_care_flag.svg
│   └── ...
│
├── infographics/
│   ├── heritage_risk_matrix.svg
│   ├── h3-resolution-scale.svg
│   └── ...
│
└── templates/
    ├── heritage_stac_template.json
    ├── heritage_dcat_template.json
    └── storynode_heritage_template.json
```

## 🎨 Asset Requirements

All heritage assets must adhere to:

- No sensitive/sacred imagery  
- Abstraction-only  
- WCAG 2.1 AA+ contrast  
- Vector-first (SVG)  
- FAIR+CARE labeling  
- Proper directory placement  
- No depiction of real coordinates or burial sites  

## 🧪 Asset Validation

All assets require:

- Heritage Stewardship Unit review  
- FAIR+CARE Council approval  
- Metadata tagging  
- CARE classification  
- H3 generalization for location-linked diagrams  
- Compliance with KFM iconography standard v11  

Local validator:

```text
make validate-heritage-assets
```

---

# 🕰 Version History

| Version  | Date       | Notes                                                         |
|----------|------------|---------------------------------------------------------------|
| v11.0.0  | 2025-11-20 | Unified heritage schemas, examples, assets into one v11 doc. |
| v10.x    | 2025       | Previous separate heritage documents.                         |

---

<div align="center">

**Kansas Frontier Matrix — Unified Heritage Standards v11**  
*Schemas · Examples · Assets*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0

[Back to Heritage Standards](README.md) ·  
[Back to Standards Directory](../README.md) ·  
[Back to Repository Root](../../../README.md)

</div>
.