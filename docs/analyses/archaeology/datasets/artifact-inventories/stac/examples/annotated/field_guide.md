---
title: "📖 Kansas Frontier Matrix — STAC Field Guide for Annotated Artifact Inventory Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/field_guide.md"
description: "Field guide for all STAC, KFM, CARE, and DCAT fields used in annotated artifact-inventory STAC examples in KFM v11."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-field-guide-v11.2.3"
doc_kind: "Field Guide"
intent: "artifact-stac-field-guide"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-field-guide-v11.2.3"
category: "Analyses · Archaeology · STAC Examples · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-field-guide-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/field_guide.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📖 Kansas Frontier Matrix — STAC Field Guide for Annotated Artifact Inventory Examples (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/field_guide.md`

**Purpose**  
Serve as the **master reference guide** for every field that appears in the annotated STAC Item and Collection examples for artifact inventories in KFM v11.

This guide explains:

- Meaning and rules for STAC 1.0 core fields  
- Requirements of the **KFM archaeology extension** (`kfm:*`)  
- Obligations of the **CARE cultural safety extension** (`care:*`)  
- Best practices for STAC ↔ DCAT alignment  
- Spatial generalization and sovereignty rules  
- How metadata maps to the Knowledge Graph, Story Nodes, and Focus Mode v3  

---

## 📘 1. STAC Core Fields (Items & Collections)

These fields come from **STAC 1.0.0** and are mandatory for all KFM archaeology metadata.

### `stac_version`

- **Definition:** STAC specification version in use.  
- **KFM rule:** Must always be `"1.0.0"`.

---

### `type`

- **Items:** must be `"Feature"`.  
- **Collections:** must be `"Collection"`.  
- Must match schema exactly.

---

### `id`

- Unique identifier for the Item or Collection.  
- **KFM rules:**
  - Must match the file stem (without extension).  
  - Lowercase; hyphens for separators.  
  - Version suffix recommended (for example, `-v11` or `-v11.2`).

---

### `description` (Collections)

- Human-readable description of the Collection’s purpose and scope.  
- Displayed in STAC viewers and KFM metadata browsers.

---

### `bbox`

- Generalized bounding box `[minLon, minLat, maxLon, maxLat]`.  
- Must reflect **generalized** extents only, derived from H3 or similar; no site-level precision.

---

### `geometry`

- Dataset geometry.  
- **Allowed types in archaeology examples:** `MultiPoint`, `Polygon`, `MultiPolygon`.  
- **KFM rules:**
  - No exact coordinates; all coordinates must be generalized.  
  - Geometry usually derived from H3 centroids or simplified polygons.

---

### `extent` (Collections)

Defines spatial and temporal coverage for all child Items.

- `extent.spatial.bbox`  
  - Generalized bounding box array.  
- `extent.temporal.interval`  
  - Array of `[start, end]` ISO-8601 timestamps.  
  - Must be OWL-Time compatible and align with cultural phases represented.

---

### `assets`

Provides access to the actual data.

- `assets.data.href`  
  - Relative or absolute link to the artifact inventory file (for example, CSV or Parquet).  
- `assets.data.type`  
  - MIME type; for tables typically `"text/csv"` or `"application/x-parquet"`.  
- `assets.data.roles`  
  - Must include `"data"` for the primary inventory asset.

---

### `links`

Used to navigate the STAC tree.

- Common relationships:
  - `rel: "collection"` from Item → parent Collection.  
  - `rel: "root"` from root Collection → catalog root (if applicable).  
- In the repo, links are optional for file-only use; required if STAC is served via API.

---

## 🧭 2. KFM Archaeology Extension Fields (`kfm:*`)

These are required for **all** artifact-inventory STAC Items and Collections in the archaeology domain.

### `kfm:domain`

- Domain identifier string, fixed for this family of datasets:  
  - `archaeology-artifact-inventories`  
- Used for ETL routing, Focus Mode queries, and graph ingestion.

---

### `kfm:phase`

- Cultural-phase or temporal grouping label.  
- Examples: `"Late Prehistoric"`, `"Middle Ceramic"`, `"Contact Period"`.  
- Drives:
  - Timelines in the web UI.  
  - Phase-based graph queries.  
  - Focus Mode temporal context.

---

### `kfm:material_class`

Controlled vocabulary describing artifact material class:

- `"lithic"`  
- `"ceramic"`  
- `"metal"`  
- `"faunal"`  
- `"all"` (root artifact Collections only)

---

### `kfm:datatype`

- Describes dataset type.  
- For artifact inventories in examples, this is effectively `"artifact-inventory"` (when used).

---

### `kfm:provenance`

- Relative path to the PROV-O lineage JSON file.  
- Must point to a file under the archaeology `provenance/` directory tree.  
- Used to connect STAC metadata to ETL and processing history.

---

### `kfm:generalization`

- Indicates how spatial generalization was performed.  
- Typical values:
  - `"H3-r7"`  
  - `"H3-r8"`  
- Must be consistent with the actual transformation applied and with governance rules.

---

### `kfm:review_cycle`

- Governance review cadence.  
- Common values: `"Biannual"`, `"Quarterly"`.  
- Used by FAIR+CARE and Metadata Standards processes to schedule re-review and re-validation.

---

## ⚖️ 3. CARE Cultural Safety Fields (`care:*`)

These fields ensure ethical handling of cultural and archaeological information.

### `care:sensitivity`

Allowed values in public-governed artifact inventories:

- `"general"` — clearly non-sensitive, PD-style data.  
- `"generalized"` — sensitive inputs, but outputs are generalized (for example, H3).  
- `"restricted-generalized"` — generalized outputs with additional governance constraints.

**Not allowed** in this public STAC context: `"restricted"`.

---

### `care:review`

Indicates which governance process reviewed the dataset.

- `"faircare"` — reviewed via FAIR+CARE-aligned processes.  
- `"tribal"` — tribal or sovereignty-based review (required for certain contact-era or sensitive materials).  
- `"none-required"` — only allowed for obviously non-sensitive, public-domain datasets.

---

### `care:notes`

- Free-text explanation of cultural-safety and sovereignty decisions.  
- Examples:
  - `Motif categories filtered for cultural safety.`  
  - `Locations generalized due to proximity to sacred sites.`  
  - `Contact-era metals reviewed with tribal representatives; site associations generalized.`  

Notes must justify the `care:sensitivity` and `care:review` values without exposing sensitive details.

---

### `care:visibility_rules` (when used)

- Describes additional visibility constraints.  
- Example values:
  - `"h3-only"` — only H3 indices allowed, no explicit geometry.  
  - `"no-exact-points"` — generalized geometry only, no raw points.

---

## 📦 4. Scientific Metadata (`sci:*`)

Scientific fields are optional but encouraged when datasets derive from academic work.

- `sci:doi` — DOI for the underlying publication or dataset.  
- `sci:citations` — list of citations.  
- `sci:authors` — primary authors or PIs.

These fields support reproducibility and scholarly credit.

---

## 🔗 5. DCAT ↔ STAC Crosswalk

For external catalog integration, DCAT and STAC fields must align.

| DCAT field        | STAC mapping                                  |
|-------------------|-----------------------------------------------|
| `dct:title`       | Collection `description` or title metadata    |
| `dct:license`     | `license`                                     |
| `dct:temporal`    | `extent.temporal.interval` or Item time props |
| `dcat:distribution` | `assets.data.href` and related metadata    |
| `dcat:keyword`    | `keywords[]` (optional STAC extension)        |

Crosswalk validation ensures KFM catalogs can be harvested by CKAN, DataHub, and similar systems.

---

## 🗺️ 6. Spatial Generalization Requirements

Mandatory rules for archaeology artifact inventories:

- No raw site coordinates or excavation-unit centroids.  
- Use **H3 generalization** (levels 5–7) or equivalent.  
- Convert sensitive feature geometries to:
  - H3 cell centroids, or  
  - Coarse polygons / bounding boxes.  
- Do not represent:
  - Burial or ceremonial landscapes.  
  - Sacred sites or restricted cultural spaces.  
- Document generalization strategy in `kfm:generalization` and `care:notes`.

Violation of these requirements should cause CI and governance checks to fail.

---

## 🧪 7. Validation & CI Requirements

Every artifact-inventory STAC Item or Collection derived from these patterns must pass:

- STAC core schemas:
  - `stac-item-schema.json`  
  - `stac-collection-schema.json`  
- KFM archaeology extension schema:
  - `kfm-archaeology-extension.json`  
- CARE sensitivity extension schema:
  - `care-sensitivity-extension.json`  
- DCAT crosswalk schema (where used):
  - `dcat-crosswalk.json`  
- Additional checks:
  - SHA-256 checksum validation (for assets where tracked).  
  - Provenance linkage checks for `kfm:provenance`.  
  - H3 generalization rule checks for spatial fields.

Example CI workflows:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`

---

## 🧠 8. Knowledge Graph Integration

Each artifact-inventory STAC document maps into the KFM knowledge graph.

### Typical node types

- `ArtifactInventory`  
- `ArtifactCollection`  
- `MaterialClass`  
- `CulturalPhase`  
- `GeneralizedSite`  

### Typical relationships

- `HAS_INVENTORY` (Collection → ArtifactInventory)  
- `BELONGS_TO_PHASE` (Inventory → CulturalPhase)  
- `HAS_MATERIAL_CLASS` (Inventory → MaterialClass)  
- `HAS_PROVENANCE` (Inventory → PROV node)  
- `HAS_EXTENT` (Inventory/Collection → SpatialExtent / TemporalExtent)  

Graph mapping is designed to remain consistent with KFM-OP v11 and GeoSPARQL / OWL-Time.

---

## 🧩 9. Focus Mode v3 Integration

Artifact metadata feeds Focus Mode v3 and Story Node pipelines.

Focus Mode v3 requires:

- `kfm:phase` (temporal context)  
- `kfm:material_class` (material culture context)  
- `care:*` metadata (for sensitivity-aware responses)  
- `kfm:provenance` (for provenance chips in the UI)  
- Source institution and licensing (from DCAT / STAC fields)

These fields allow Focus Mode to:

- Generate narratives about material culture and phases,  
- Respect sovereignty and CARE constraints,  
- Expose provenance inline for user trust.

---

## 🕰 10. Version History

| Version   | Date       | Author                                       | Summary                                                                 |
|-----------|------------|----------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee | Aligned with KFM-MDP v11.2.2; added energy/carbon schemas; clarified Focus Mode v3 and sovereignty rules. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council          | Created STAC annotated field guide; added mappings for STAC ↔ DCAT ↔ PROV-O ↔ KG; ensured KFM-MDP v10.4 compliance. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                       | Initial notes scaffold.                                                |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annotated STAC Examples](README.md)