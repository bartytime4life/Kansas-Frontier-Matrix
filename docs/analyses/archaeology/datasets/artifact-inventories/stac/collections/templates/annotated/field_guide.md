---
title: "📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Collection Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/field_guide.md"
description: "Authoritative field guide for all fields used in annotated STAC Collection templates for KFM v11 artifact inventories, including STAC, KFM, CARE, DCAT, and governance rules."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Metadata Standards Subcommittee · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-collection-field-guide-v11.2.3"
doc_kind: "Field Guide"
intent: "artifact-collection-annotated-field-guide"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-collection-field-guide-v11.2.3"
category: "Analyses · Archaeology · STAC Collections · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-collection-field-guide-v1.json"
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
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/field_guide.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Collection Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/field_guide.md`

**Purpose**  
Serve as the **authoritative reference manual** for all fields appearing in the annotated STAC Collection templates for artifact inventories within the Kansas Frontier Matrix (KFM).

This guide explains:

- STAC 1.0 Collection fields  
- KFM archaeology extension fields (`kfm:*`)  
- CARE cultural safety metadata (`care:*`)  
- DCAT 3.0 mapping expectations  
- Generalization and sovereignty rules  
- Ethical and governance constraints  
- Schema and CI validation logic  

It is intended for contributors, metadata engineers, archaeologists, data stewards, and governance reviewers.

---

## 🗂️ 1. STAC Collection Core Fields (STAC 1.0)

### `stac_version`

- **Definition:** STAC standard version in use.  
- **KFM rule:** Must always be `"1.0.0"` for Collections and Items in KFM v11.

---

### `type`

- Must always be `"Collection"` for these documents.  
- Distinguishes top-level grouping entities (Collections) from Items.

---

### `id`

- Unique identifier for the Collection.  
- Requirements:
  - Lowercase  
  - Hyphenated if multi-word  
  - Reflects dataset category (`lithics`, `ceramics`, `metals`, `faunal`, `artifact-inventories`)  
  - Should match the filename (without extension)

---

### `description`

- Human-readable description of the Collection’s purpose, scope, and contents.  
- Displayed in KFM browsers, Story Node side-panels, and STAC viewers.

---

### `license`

- SPDX-compliant license identifier (for example: `"CC-BY-4.0"`).  
- **KFM archaeology constraint:** Only **CC-BY** or **CC0** permitted for public-governed artifact Collections.

---

### `extent`

Defines both spatial and temporal coverage of all child Items.

#### `extent.spatial.bbox`

- Bounding box array: `[[minLon, minLat, maxLon, maxLat]]`.  
- Must reflect **generalized extents only**:
  - No site-precise or household-precise coordinates  
  - Typically derived from H3 footprint envelopes  

#### `extent.temporal.interval`

- Array of `[start_time, end_time]` timestamp arrays.  
- Must:
  - Use ISO 8601 timestamps  
  - Be consistent with **OWL-Time** interpretations  
  - Align with known cultural phases represented in the Collection  

---

### `links`

- Used for STAC navigation and cross-linking.  
- Optional for pure file-based catalogs; required when exposed via a STAC API.  
- When present, must correctly reference:
  - `self` (this Collection)  
  - `root` artifact Collection (for non-root Collections)  
  - Child Items and/or sub-Collections  

---

## 🧭 2. KFM Archaeology STAC Extension Fields (`kfm:*`)

**Purpose**  
Extend STAC with archaeology-specific metadata to support:

- Knowledge graph mapping (Neo4j / GeoSPARQL)  
- Story Node material-culture narratives  
- Focus Mode contextualization  
- Domain-driven search and filtering  

---

### `kfm:material_class`

Controlled vocabulary (Collection-level):

- `"lithic"`  
- `"ceramic"`  
- `"metal"`  
- `"faunal"`  
- `"all"` — root artifact Collection only  

Values must match the Collection’s actual content and the associated filenames.

---

### `kfm:domain`

- Domain identifier for this family of Collections.  
- For artifact inventory Collections, always:

~~~text
archaeology-artifact-inventories
~~~

This string is used consistently across ETL, Focus Mode, Story Nodes, and the graph layer.

---

### `kfm:review_cycle`

- Governance review cadence.  
- Common values:
  - `"Biannual"`  
  - `"Quarterly"`  

Used by FAIR+CARE and Metadata Standards processes to schedule re-review and re-validation.

---

### `kfm:provenance_summary`

- Optional but strongly recommended.  
- Short, human-readable description of typical provenance patterns for this Collection, such as:

> Aggregated from public-domain lithic catalogs with H3 generalization and sovereignty review.

Helps reviewers quickly understand lineage before reading detailed PROV-O files.

---

## ⚖️ 3. CARE Cultural Safety Fields (`care:*`)

CARE metadata ensures ethical treatment of cultural and archaeological datasets, protecting Indigenous sovereignty and avoiding harmful disclosure or misrepresentation.

---

### `care:sensitivity`

Allowed values for artifact Collections:

- `"general"`  
  - Public-domain or fully non-sensitive material.  
- `"generalized"`  
  - Sources may contain sensitive details, but published data is generalized (for example, H3-based, motif grouping).  
- `"restricted-generalized"`  
  - Used sparingly; indicates that even generalized outputs are under special governance.

**Forbidden for artifact Collections in public repos:**

- `"restricted"` — not allowed for public-governed STAC resources.

---

### `care:review`

Allowed values:

- `"faircare"`  
  - Reviewed through FAIR+CARE-aligned governance processes.  
- `"tribal"`  
  - Sovereignty-governed review, required for sensitive protohistoric or contact-era materials.  
- `"none-required"`  
  - Use only for clearly public-domain data confirmed as non-sensitive.

---

### `care:notes`

- Supplementary free-text explanation of cultural safety treatment.  
- Examples:
  - `Motif categories filtered to remove sacred symbolism.`  
  - `Generalized polygon used to obscure culturally sensitive region boundaries.`  
  - `Contact-era metals reviewed with tribal representatives; site associations generalized.`  

`care:notes` must be descriptive enough to justify sensitivity and review choices without exposing sensitive details.

---

## 🔗 4. DCAT → STAC Mapping Notes

To support external catalogs and automated harvesting, basic **DCAT 3.0** fields map to STAC as follows:

| DCAT Field        | STAC Mapping                      |
|-------------------|-----------------------------------|
| `dct:title`       | Collection `description` or title |
| `dct:license`     | `license`                         |
| `dct:temporal`    | `extent.temporal.interval`        |
| `dcat:distribution` | Item-level assets, not Collections |
| `dcat:keyword`    | STAC `keywords[]` (optional)      |

DCAT metadata ensures interoperability with CKAN, DataHub, and other catalog ecosystems.

---

## 🗺️ 5. Spatial Generalization & Sovereignty Requirements

Mandatory for **all** archaeology artifact Collections represented in public-governed STAC:

- Use **H3-based generalization** (for example, levels 5–7) to derive extents and summary geometry.  
- Remove or replace precise site coordinates with:
  - H3 centroids  
  - Generalized polygons  
  - Bounding boxes derived from aggregated coverage  
- Do not publish:
  - Burial or ceremonial landscapes  
  - Sacred locations or restricted cultural features  
- Generalize territorial boundaries unless explicitly approved per sovereignty policy.  
- When in doubt, prefer **more coarse generalization** and document the rationale in `care:notes`.

Failure to adhere to these requirements is grounds for CI rejection and governance rollback.

---

## 🧪 6. Schema Validation Rules

STAC Collections derived from the annotated templates must validate against:

- `stac-collection-schema.json`  
- `kfm-archaeology-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json` (where applicable)

Validation checks include:

- Presence of required STAC fields  
- Controlled vocabulary adherence (`kfm:*`, `care:*`)  
- Correct value types and geometry structure  
- Sensitivity categorization consistent with dataset contents  
- DCAT–STAC alignment where crosswalks are defined  
- Provenance consistency between:
  - Source datasets  
  - Metadata files  
  - STAC Collections and Items  

CI workflow (normative):

- `.github/workflows/artifact-stac-validate.yml`

---

## 🧠 7. Knowledge Graph Mapping

Each artifact STAC Collection maps to KFM graph structures, for example:

### Node types

- `ArtifactCollection`  
- `MaterialClass`  
- `CulturalPhaseGroup`

### Relationships

- `GROUPS` (Collection → Item / ArtifactInventory)  
- `HAS_CATEGORY` (Collection → MaterialClass)  
- `HAS_CARE_SENSITIVITY` (Collection → CARE/Sensitivity node)  
- `HAS_EXTENT` (Collection → SpatialExtent / TemporalExtent)

Graph mappings are used to:

- Enrich Story Nodes with temporal and spatial context  
- Support Focus Mode reasoning about cultural phases and material classes  
- Enable graph-based queries over artifact inventories without exposing sensitive detail

---

## 📝 8. Reading Annotated Templates

The annotated JSON templates in this directory use `_comment*` fields to explain semantics:

- Keys such as `_comment_stac_version`, `_comment_material_class` provide human-readable descriptions.  
- Every required field includes either:
  - A technical justification (schema/validation reason), and/or  
  - A cultural/ethical justification (CARE and sovereignty reason).  

Important rules:

- `_comment*` fields exist **only** in annotated documentation templates.  
- They must **not** be preserved in production STAC Collections.  
- Production documents must be based on the non-annotated templates in `../`.

---

## 🕰 9. Version History

| Version   | Date       | Author                                      | Summary                                                                 |
|-----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Metadata Standards Subcommittee · Archaeology WG | Aligned with KFM-MDP v11.2.2; added energy/carbon schemas; clarified CARE/sovereignty rules and validation workflow. |
| v10.4.0   | 2025-11-17 | Metadata Subcommittee · Archaeology WG · FAIR+CARE Council | Created full field guide for annotated STAC Collection templates, including CARE, DCAT, and KFM rules. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                      | Initial scaffold of the field guide.                                   |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annotated Templates](../README.md)