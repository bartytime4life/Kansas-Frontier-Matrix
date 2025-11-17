---
title: "📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Collection Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/field_guide.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Metadata Standards Subcommittee · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-collection-field-guide-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Field Guide"
intent: "artifact-collection-annotated-field-guide"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📖 **Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Collection Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/field_guide.md`

**Purpose:**  
Serve as the **authoritative reference manual** for all fields appearing in the annotated STAC Collection templates for artifact inventories within the Kansas Frontier Matrix (KFM).  
This guide explains:

- STAC 1.0 Collection fields  
- KFM Archaeology Extension fields (`kfm:*`)  
- CARE Cultural Safety metadata (`care:*`)  
- DCAT 3.0 mapping expectations  
- Generalization & sovereignty rules  
- Ethical constraints  
- Metadata governance and CI validation logic  

It is designed for contributors, metadata engineers, archaeologists, data stewards, and governance reviewers.

</div>

---

# 🗂️ 1. STAC Collection Core Fields (STAC 1.0)

### `stac_version`
- **Definition:** STAC standard version in use.  
- **KFM Rule:** Must always be `"1.0.0"`.

---

### `type`
- Must always be `"Collection"`.  
- Distinguishes top-level grouping entities from Items.

---

### `id`
- Unique identifier for the collection.  
- Requirements:
  - Lowercase, hyphenated  
  - Reflects dataset category (`lithics`, `ceramics`, `metals`, `faunal`, `artifact-inventories`)  
  - Must match filename  

---

### `description`
- Human-readable description of the collection’s purpose, scope, and content.  
- Displayed in KFM browsers and STAC viewers.

---

### `license`
- SPDX-compliant license identifier (e.g., `"CC-BY-4.0"`).  
- **KFM Archaeology Constraint:** Only **CC-BY** or **CC0** allowed.

---

### `extent`
Defines both spatial and temporal coverage.

#### `extent.spatial.bbox`
- Bounding box array.  
- Must reflect **generalized extents only**.  
- No sensitive precision allowed (H3 generalization recommended).

#### `extent.temporal.interval`
- Array of `[start_time, end_time]` timestamp arrays.  
- Must comply with **OWL-Time** and align with known cultural phases.

---

### `links`
- Used for STAC navigation.  
- Optional for internal repo use; required for STAC API deployment.

---

# 🧭 2. KFM Archaeology STAC Extension Fields (`kfm:*`)

### Purpose
Extend STAC with archaeology-specific metadata to support:

- Knowledge Graph mapping  
- Story Node cultural narratives  
- Focus Mode contextualization  
- Domain-driven indexing  

---

### `kfm:material_class`
Controlled vocabulary:
- `"lithic"`  
- `"ceramic"`  
- `"metal"`  
- `"faunal"`  
- `"all"` (root collection only)

---

### `kfm:domain`
- Domain identifier: always `"archaeology:artifact-inventories"`.

---

### `kfm:review_cycle`
- Specifies governance cycle: `"Biannual"` or `"Quarterly"`.  
- Used by FAIR+CARE and Metadata Governance systems.

---

### `kfm:provenance_summary`
- Optional but recommended.  
- High-level description of dataset lineage.

---

# ⚖️ 3. CARE Cultural Safety Fields (`care:*`)

CARE metadata ensures ethical treatment of cultural and archaeological datasets, protecting Indigenous sovereignty and avoiding harmful representations.

---

### `care:sensitivity`
Allowed values:
- `"general"` — PD or fully non-sensitive  
- `"generalized"` — source coordinates or cultural notes generalized  
- `"restricted-generalized"` — used sparingly; requires tribal oversight  

**Forbidden for artifact collections:**  
- `"restricted"` (never allowed in public repos)

---

### `care:review`
Allowed values:
- `"faircare"` — reviewed through KFM’s FAIR+CARE Council  
- `"tribal"` — required for protohistoric metals  
- `"none-required"` — PD-only data  

---

### `care:notes`
Supplementary cultural-safety explanation.  
Examples:
- `"Motif categories filtered to remove sacred symbolism."`  
- `"Generalized polygon used to obscure culturally sensitive region boundaries."`

---

# 🔗 4. DCAT → STAC Mapping Notes

To enable dataset catalogs and automated harvesting:

| DCAT Field | STAC Mapping |
|-----------|--------------|
| `dct:title` | `description` or collection title |
| `dct:license` | `license` |
| `dct:temporal` | `extent.temporal.interval` |
| `dcat:distribution` | Not used in Collections; appears at Item-level |
| `dcat:keyword` | Optional STAC `keywords` field |

DCAT metadata ensures interoperability with external catalogs (CKAN, DataHub, etc.).

---

# 🗺️ 5. Spatial Generalization & Sovereignty Requirements

**Mandatory for all archaeology datasets:**

- Generalize using **H3 hexagons (levels 5–7)**  
- Remove precise site coordinates  
- Avoid publishing burial or ceremonial landscapes  
- Territorial boundaries must be generalized unless explicitly approved  
- Demote sensitive geometries to bounding boxes when needed  
- Provide justification in `care:notes`  

**Violation results in CI rejection.**

---

# 🧪 6. Schema Validation Rules

STAC Collections must pass:

- `stac-collection-schema.json`  
- `kfm-archaeology-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json`  

Validation checks include:

- Required field presence  
- Controlled vocabulary adherence  
- Correct geometry types  
- Sensitivity categorization  
- DCAT–STAC alignment  
- Provenance consistency between dataset → metadata → STAC  

CI workflow: `.github/workflows/artifact-stac-validate.yml`

---

# 🧠 7. Knowledge Graph Mapping

Each STAC Collection maps to KFM graph nodes:

### Node Types
- `ArtifactCollection`  
- `MaterialClass`  
- `CulturalPhaseGroup`

### Relationships
- `GROUPS`  
- `HAS_CATEGORY`  
- `HAS_CARE_SENSITIVITY`  
- `HAS_EXTENT`  

Collections enrich Story Nodes with:

- Time ranges  
- Cultural groupings  
- Spatial context  

AI narrative engines (Focus Mode v2) use these groupings for contextual inference.

---

# 📝 8. Example Interpretation

When reading annotated STAC Collection templates:

- Comments prefixed with `_comment_*` describe why a field exists  
- Every required field has a cultural, technical, or governance justification  
- Each example follows the MCP documentation-first rule  
- Templates cannot be published without CARE review completion  

---

# 🕰️ 9. Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Metadata Subcommittee · Archaeology WG · FAIR+CARE Council | Created full field guide for annotated STAC Collection templates; includes CARE, DCAT, and KFM rules |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Annotated Templates](../README.md)

</div>