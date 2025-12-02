---
title: "📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Item Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md"
description: "Field guide for all STAC, KFM, CARE, DCAT, and governance fields used in annotated artifact-inventory STAC Item templates for KFM v11."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-item-field-guide-v11.2.3"
doc_kind: "Field Guide"
intent: "artifact-stac-item-field-guide"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-item-field-guide-v11.2.3"
category: "Analyses · Archaeology · STAC Items · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-item-field-guide-v1.json"
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

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Item Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md`

**Purpose**  
Serve as the **complete reference manual** for interpreting every field used in the annotated STAC Item templates for artifact inventories in KFM v11.

This guide is for contributors, metadata engineers, archaeologists, and governance reviewers. It explains:

- STAC 1.0 Item structure  
- KFM archaeology extension fields (`kfm:*`)  
- CARE cultural safety extension fields (`care:*`)  
- DCAT crosswalk expectations  
- Spatial generalization and sovereignty constraints  
- Validation requirements for CI/CD  
- Mapping into the knowledge graph, Story Nodes, and Focus Mode v3  

---

## 🗂️ 1. STAC Core Fields (STAC 1.0)

These fields are required for **every** artifact-inventory STAC Item.

### `stac_version`

- Must always be `"1.0.0"` for KFM v11.

### `type`

- Must always be `"Feature"` for STAC Items.

### `id`

- Lowercase, hyphenated, versioned identifier (for example, `prairie-ceramics-v11`).  
- Must match:
  - JSON filename (without `.json`), and  
  - Inventory / provenance stems where applicable.

### `bbox`

- Generalized spatial extent of the dataset.  
- Derived from generalized geometry (for example, from H3 coverage), **not** from precise coordinates.

### `geometry`

- Allowed types: `MultiPoint`, `Polygon`, `MultiPolygon`.  
- All coordinates must be **generalized**; no exact provenience or excavation-unit centroids.

### `properties`

- Container for all attribute metadata:
  - KFM archaeology fields (`kfm:*`)  
  - CARE fields (`care:*`)  
  - Licensing and optional scientific fields  

### `assets.data`

Defines where the actual inventory is stored.

- `href` — relative path to the inventory table (for example, `../inventories/file.csv`).  
- `type` — MIME type (for example, `text/csv`).  
- `roles` — must include `"data"` for the primary inventory asset.

### `links.collection`

- Required link back to the parent STAC Collection.  
- `rel: "collection"` with `href` pointing to the relevant Collection JSON in `../collections/`.

---

## 🧭 2. KFM Archaeology Extension Fields (`kfm:*`)

These fields integrate artifact-inventory Items with KFM’s archaeology domain, knowledge graph, and AI systems.

### `kfm:domain`

- Domain identifier for artifact inventories.  
- Must be: `archaeology-artifact-inventories`.

### `kfm:phase`

- Cultural-phase classification (for example, `Late Prehistoric`, `Middle Ceramic`).  
- Used for:
  - Timelines and period filters  
  - Story Node temporal context  
  - Focus Mode phase-aware reasoning  

### `kfm:material_class`

Controlled vocabulary describing artifact material class:

- `lithic`  
- `ceramic`  
- `metal`  
- `faunal`

Must match the template used and the relevant Collection.

### `kfm:datatype`

- Dataset type indicator.  
- For these Items: `"artifact-inventory"`.

### `kfm:source`

- Institution or repository responsible for the dataset (for example, a university archive, museum, or open data portal).  
- Supports provenance and attribution.

### `kfm:generalization`

- Records how spatial generalization was performed.  
- Typical values: `"H3-r7"`, `"H3-r8"`.  
- Must be consistent with the actual transformation and reported CARE sensitivity.

### `kfm:provenance`

- Relative path to the PROV-O lineage JSON file.  
- Connects STAC metadata to ETL and review steps:
  - ingestion  
  - cleaning  
  - generalization  
  - cultural review  
  - publication  

---

## ⚖️ 3. CARE Cultural Safety Fields (`care:*`)

CARE metadata ensures ethical treatment of cultural and archaeological information.

### `care:sensitivity`

Allowed values for public-governed artifact inventories:

- `general`  
  - Clearly non-sensitive, public-domain style data.  
- `generalized`  
  - Input may contain sensitive details; output is generalized (for example, H3).  
- `restricted-generalized`  
  - Generalized outputs with additional governance constraints.

Not allowed here:

- `restricted` — not permitted in this public-governed STAC layer.

### `care:review`

Indicates which governance process reviewed the dataset.

- `faircare` — FAIR+CARE-aligned review.  
- `tribal` — sovereignty-governed review, required for certain contact-era or protohistoric materials.  
- `none-required` — only for clearly non-sensitive, PD-safe data.

### `care:notes`

- Free-text description of cultural safety decisions and transformations.  
- Examples:
  - `Motif categories generalized and filtered to remove sacred symbolism.`  
  - `Locations generalized due to proximity to sacred landscapes.`  
  - `Contact-era metals reviewed with tribal representatives; site associations generalized.`  

Notes must justify `care:sensitivity` and `care:review` without revealing sensitive content.

### `care:sovereignty`

- Indicates whether dataset use is governed by sovereignty policies (for example, `protected`).  
- Helps Focus Mode and graph queries respect sovereignty constraints.

### `care:visibility_rules` (when present)

- Specifies additional visibility constraints (examples are used in other docs):
  - `h3-only` — only H3 indices, no explicit geometry.  
  - `no-exact-points` — generalized geometry permitted, no raw coordinates.

---

## 🔬 4. Scientific Metadata (`sci:*`)

Scientific fields are optional but encouraged when artifact inventories derive from scholarly work.

Examples include:

- `sci:doi` — DOI of the dataset or associated paper.  
- `sci:citations` — key references.  
- `sci:authors` — primary authors or project leads.

These fields support reproducibility, academic credit, and provenance in Story Nodes and Focus Mode.

---

## 🔗 5. DCAT ↔ STAC Crosswalk

For external catalog interoperability, DCAT and STAC fields must be aligned. Typical mappings:

| DCAT field        | STAC mapping                                      |
|-------------------|---------------------------------------------------|
| `dct:title`       | Item `id` or a title field in metadata            |
| `dct:license`     | `license` or `dct:license` in `properties`        |
| `dct:temporal`    | temporal info in `properties` / Collection extent |
| `dcat:distribution` | `assets.data.href` and related asset metadata  |
| `dcat:keyword`    | `keywords[]` (if used)                            |

DCAT compliance is enforced at release time for KFM manifests and external catalog publishing.

---

## 🌐 6. Spatial Generalization & Sovereignty Rules

Artifact inventories must **never** expose sensitive locations.

Key rules:

- All spatial data must be **generalized** (for example, H3 levels 5–7).  
- No site-precise coordinates, excavation-unit centroids, or burial locations.  
- Cultural landscapes with high sensitivity should be represented with coarse geometry or bounding boxes.  
- Generalization decisions must align with:
  - `kfm:generalization`  
  - `care:sensitivity`  
  - `care:notes`  
  - `sovereignty_policy` referenced in front matter.

Generalization compliance is checked by CI and governance reviews.

---

## 🧪 7. Validation & CI Requirements

Any STAC Item derived from the annotated templates (via the non-annotated templates) must pass:

- STAC core Item schema validation.  
- KFM archaeology extension schema checks (`kfm:*`).  
- CARE sensitivity schema checks (`care:*`).  
- DCAT crosswalk checks (where DCAT metadata exists).  
- Provenance linkage checks:
  - `kfm:provenance` must resolve to a valid PROV-O dataset.  
- Spatial generalization checks:
  - Geometry and `bbox` must not expose site-level detail.

Typical workflows:

- `.github/workflows/artifact-stac-validate.yml`  
- Additional metadata validation workflows as configured for KFM v11.

---

## 🧠 8. Knowledge Graph Mapping

STAC Items for artifact inventories are ingested into the KFM knowledge graph.

Common node types:

- `ArtifactInventory` — represents the inventory dataset.  
- `MaterialClass` — linked via `kfm:material_class`.  
- `CulturalPhase` — linked via `kfm:phase`.  
- `GeneralizedSite` — derived from generalized spatial footprints.  
- Provenance-related nodes corresponding to PROV-O entities.

Common relationships:

- `HAS_INVENTORY` (Collection → ArtifactInventory).  
- `BELONGS_TO_PHASE` (ArtifactInventory → CulturalPhase).  
- `HAS_MATERIAL_CLASS` (ArtifactInventory → MaterialClass).  
- `HAS_PROVENANCE` (ArtifactInventory → PROV node).  
- `HAS_EXTENT` (Inventory → Spatial/Temporal extent nodes).  
- `HAS_CARE_SENSITIVITY` (Inventory → CARE/sensitivity node).

This mapping is kept consistent with KFM-OP v11, CIDOC-CRM, GeoSPARQL, and OWL-Time.

---

## 📝 9. Story Node & Focus Mode Integration

Artifact-inventory metadata drives:

- Material culture narratives in Story Nodes.  
- Phase-aware, sensitivity-aware responses in Focus Mode v3.  
- Provenance chips that expose lineage in the UI.  
- Map overlays and time sliders for artifact density and category.

To support these, each Item must provide:

- `kfm:phase` and `kfm:material_class`.  
- `care:*` fields to guide narrative and data exposure.  
- `kfm:provenance` and licensing fields for traceability.  
- Generalized geometry usable for safe visualization.

---

## 🕰 Version History

| Version   | Date       | Author                                       | Summary                                                                 |
|-----------|------------|----------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee | Aligned with KFM-MDP v11.2.2; added energy/carbon telemetry refs; clarified Focus Mode v3 and sovereignty rules. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council          | Completed artifact STAC Item annotated field guide with crosswalks, safety rules, and KG/Focus Mode mapping. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                       | Initial field-guide scaffold.                                          |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annotated STAC Item Templates](../README.md)