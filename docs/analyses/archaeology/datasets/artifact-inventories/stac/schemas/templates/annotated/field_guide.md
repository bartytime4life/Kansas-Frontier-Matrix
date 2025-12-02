---
title: "📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Schema Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/field_guide.md"
description: "Field guide for all JSON Schema components used in annotated STAC schema templates for KFM v11 artifact-inventory Items and Collections, including KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Metadata Standards Subcommittee · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-schema-field-guide-v11.2.3"
doc_kind: "Field Guide"
intent: "artifact-stac-schema-field-guide"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-schema-field-guide-v11.2.3"
category: "Analyses · Archaeology · STAC Schemas · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-schema-field-guide-v1.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Metadata Standards Subcommittee · Archaeology Working Group"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/field_guide.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Schema Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/field_guide.md`

**Purpose**  
Provide the **authoritative reference** for interpreting every component used in the annotated schema templates that validate artifact-inventory **STAC Items** and **STAC Collections** in KFM v11.

This guide explains:

- STAC 1.0 schema-level validation rules  
- KFM archaeology extension field constraints (`kfm:*`)  
- CARE cultural safety schema rules (`care:*`)  
- DCAT 3.0 crosswalk schema mappings  
- JSON Schema Draft 2020-12 conventions  
- CI/CD validator expectations  
- How validated metadata enters the knowledge graph, Story Nodes, and Focus Mode v3  

---

## 🧩 1. JSON Schema Draft 2020-12 — Overview

All artifact-inventory STAC schemas in KFM conform to **JSON Schema Draft 2020-12**. This is enforced by:

- KFM schema validators  
- GitHub CI workflows  
- STAC compliance tools  
- Downstream validation during ingestion into the graph and Focus Mode pipelines  

### Required schema-level components

| Component  | Purpose                                                   |
|-----------|-----------------------------------------------------------|
| `$schema` | Identifies schema version for validators                  |
| `title`   | Human-readable name for schema                            |
| `type`    | Data type of the root object (always `"object"` here)     |
| `required`| Fields that must be present                               |
| `properties` | Allowed fields and their subschemas                   |
| `enum` / `const` | Tight constraints, critical for `kfm:*` and `care:*` |

KFM schema templates must:

- Use `$schema: "https://json-schema.org/draft/2020-12/schema"`  
- Set `type: "object"` at the root  
- Avoid external `$ref` outside the repository unless explicitly documented  

---

## 🗂️ 2. STAC Item Schema Components

The annotated STAC Item schema template validates artifact-inventory Items.

### Required fields

| Field          | Notes                                                             |
|----------------|-------------------------------------------------------------------|
| `id`           | Must match filename stem and version pattern                      |
| `type`         | Must be `"Feature"`                                               |
| `stac_version` | Must be `"1.0.0"`                                                 |
| `bbox`         | Generalized four-number array (minLon, minLat, maxLon, maxLat)   |
| `geometry`     | No raw coordinates; allowed types are MultiPoint/Polygon variants |
| `properties`   | Container for archaeology and CARE metadata                       |
| `assets`       | Must include a `"data"` asset with `href`, `type`, and `roles`    |

### Key rules

- `geometry.type` must be one of: `"MultiPoint"`, `"Polygon"`, or `"MultiPolygon"`.  
- Raw point geometries representing exact sites are forbidden.  
- `assets.data.roles` must include `"data"`.  
- `properties` must be capable of holding `kfm:*`, `care:*`, and optional scientific fields.  

The Item schema templates are designed to **reject**:

- Raw, non-generalized coordinates  
- Items with forbidden CARE labels (`care:sensitivity = "restricted"`)  
- Items lacking primary data assets or provenance references  

---

## 🗂️ 3. STAC Collection Schema Components

The annotated STAC Collection schema template validates Collections that group artifact inventories.

### Required fields

| Field                | Notes                                                                 |
|----------------------|-----------------------------------------------------------------------|
| `id`                 | Must match Collection filename and grouping semantics                 |
| `stac_version`       | Must be `"1.0.0"`                                                     |
| `type`               | Must be `"Collection"`                                                |
| `extent.spatial`     | Must define generalized bounding boxes                               |
| `extent.temporal`    | Must provide OWL-Time compatible intervals                           |
| `license`            | SPDX code, typically `"CC-BY-4.0"` (or `"CC0-1.0"` for PD-only cases) |

Prohibited in Collection extent schemas:

- Exact spatial extents derived from raw site-level geometry  
- Missing temporal intervals for archaeology Collections  
- Non-open or mismatched licenses relative to items  

---

## 🧭 4. KFM Archaeology Schema Components (`kfm:*`)

KFM archaeology fields sit within `properties` (Items) or at the root of Collections.

### Core fields

- `kfm:domain`  
  - Domain identifier; for artifact inventories: `archaeology-artifact-inventories`.

- `kfm:phase`  
  - Cultural-phase identifier (for example, `"Late Prehistoric"`, `"Middle Ceramic"`).  
  - Required for Items.  
  - Drives timeline logic and Focus Mode temporal context.

- `kfm:material_class`  
  - Enum: `"lithic"`, `"ceramic"`, `"metal"`, `"faunal"`, `"all"` (Collections).  
  - Required for Items and Collections to align with their material group.

- `kfm:datatype`  
  - For artifact-inventory Items, the templates use `"artifact-inventory"` as a constant.

- `kfm:source`  
  - Source institution or repository (for example, a museum, archive, or university lab).  
  - Supports provenance and credit.

- `kfm:provenance`  
  - Path or identifier for PROV-O lineage JSON.  
  - Required for Items; strongly recommended for Collections.

- `kfm:review_cycle`  
  - For example: `"Biannual"` or `"Quarterly"`.  
  - Used by governance processes to schedule re-review.

The archaeology extension schema enforces appropriate types and, where needed, enums or const values.

---

## ⚖️ 5. CARE Sensitivity Schema Components (`care:*`)

CARE extension schemas ensure cultural safety and sovereignty protection.

### `care:sensitivity`

Allowed values:

- `"general"` — clearly non-sensitive data.  
- `"generalized"` — sensitive input, generalized output (for example, via H3).  
- `"restricted-generalized"` — generalized output with additional access controls.

Not allowed in public artifact-inventory schemas:

- `"restricted"`.

### `care:review`

Allowed values:

- `"faircare"` — reviewed under FAIR+CARE-aligned processes.  
- `"tribal"` — sovereignty-governed review; required for certain contact-era materials.  
- `"none-required"` — only for clearly PD-safe and non-sensitive datasets.

### `care:notes`

- Free-text explanation describing cultural review considerations.  
- Expected to document:
  - motif filtering,  
  - spatial generalization decisions,  
  - any tribal/sovereignty feedback.

### `care:visibility_rules`

- Typically: `"h3-only"` or `"no-exact-points"`.  
- Used to express additional constraints on how much spatial detail may be shown in STAC or UI layers.

The CARE schema templates enforce allowed values and presence of notes for sensitive contexts.

---

## 🔗 6. DCAT ↔ STAC Crosswalk Schema

DCAT crosswalk templates validate that STAC metadata can be correctly mapped into DCAT for external catalogs.

Key mapped fields:

| DCAT field        | STAC mapping example                                |
|-------------------|-----------------------------------------------------|
| `dct:title`       | STAC `description` or title metadata                |
| `dct:license`     | STAC `license` or `dct:license` in `properties`     |
| `dct:temporal`    | STAC temporal extent (Item or Collection)           |
| `dcat:distribution` | STAC `assets.data.href`                          |
| `dcat:keyword`    | STAC `keywords[]` (optional but recommended)        |

Crosswalk schemas help CI confirm that **DCAT manifests remain internally consistent** with their STAC sources.

---

## 🧪 7. Schema Validation Logic in CI

Annotated templates are designed to plug into KFM’s CI validation:

- JSON Schema Draft 2020-12 validation (for Items, Collections, extensions, and crosswalks).  
- Controlled vocab and enum checks for `kfm:*` and `care:*`.  
- Cross-schema consistency checks (for example, Items vs Collections vs crosswalk).  

Typical CI flow (referenced from other docs):

1. Validate schema files themselves.  
2. Use those schemas to validate STAC Items/Collections in `stac/items/` and `stac/collections/`.  
3. Fail CI if:
   - Required fields are missing,  
   - CARE values are invalid or misused,  
   - DCAT crosswalk rules do not hold, or  
   - Generalization rules appear violated (based on geometry/bbox constraints + CARE settings).

---

## 🧠 8. Knowledge Graph Mapping Rules (Schema Level)

The schemas underpin consistent mapping from STAC metadata into the knowledge graph.

Examples:

- `kfm:phase` → `CulturalPhase` nodes and edges from `ArtifactInventory`.  
- `kfm:material_class` → `MaterialClass` nodes.  
- `care:sensitivity` → `CulturalSafetyLevel` or analogous nodes.  
- `bbox` / `geometry` (generalized) → `GeneralizedSpatialExtent` nodes with H3 references embedded elsewhere in the system.

By enforcing schema-level constraints, KFM ensures:

- Consistent ontology mapping (KFM-OP v11).  
- GeoSPARQL / OWL-Time compatibility for spatial/temporal reasoning.  
- CARE-aligned graph paths used by Focus Mode and Story Nodes.

---

## 📝 9. Story Node & Focus Mode Integration

While schemas operate at the structural level, they directly affect downstream behavior:

- Story Node creation relies on `kfm:phase`, `kfm:material_class`, and `care:*` states to decide what narratives can be generated.  
- Focus Mode v3 relies on schema-constrained metadata to:
  - Understand dataset scope and sensitivity,  
  - Render provenance chips,  
  - Filter queries based on CARE and sovereignty states,  
  - Avoid using disallowed data in responses.

If a schema allows invalid or underspecified metadata, Focus Mode and Story Nodes may behave incorrectly; hence the strict schema rules.

---

## 🕰 10. Version History

| Version   | Date       | Author                                               | Summary                                                                 |
|-----------|------------|------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Metadata Standards Subcommittee · Archaeology Working Group | Updated for KFM v11.2.3; added energy/carbon telemetry references and clarified CARE/sovereignty semantics and Focus Mode v3 integration. |
| v10.4.0   | 2025-11-17 | Metadata Subcommittee · Archaeology WG · FAIR+CARE Council | Completed annotated schema field guide with crosswalk, safety, and graph mapping rules. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                               | Initial scaffolding for schema field guide.                            |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annotated Schema Templates](../README.md)