---
title: "📖 Kansas Frontier Matrix — STAC Field Guide for Annotated Artifact Inventory Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/field_guide.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-field-guide-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Field Guide"
intent: "artifact-stac-field-guide"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📖 **Kansas Frontier Matrix — STAC Field Guide for Annotated Artifact Inventory Examples**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/field_guide.md`

**Purpose:**  
Serve as the **master reference guide** explaining every field that appears in the annotated STAC Item and STAC Collection examples for artifact inventories.  

This field guide ensures contributors understand:  
- Meaning, purpose, and rules for each STAC core field  
- Requirements of the **KFM Archaeology Extension (`kfm:*`)**  
- Obligations of the **CARE Cultural Safety Extension (`care:*`)**  
- Best practices for STAC + DCAT alignment  
- Cultural sensitivity protocols and generalization requirements  
- How metadata maps to the Knowledge Graph, Story Nodes, and Focus Mode v2  

</div>

---

# 📘 1. STAC Core Fields (Items & Collections)

These fields come directly from **STAC 1.0.0** and are mandatory for all KFM archaeological metadata.

---

## `stac_version`
**Definition:** Version of STAC spec used.  
**KFM Rule:** Must **always** be `"1.0.0"`.

---

## `type`
**STAC Item:** `"Feature"`  
**STAC Collection:** `"Collection"`  
**KFM Rule:** Must match schema exactly.

---

## `id`
**Definition:** Unique identifier for the dataset or collection.  
**KFM Rule:**  
- Must match file stem  
- Lowercase, hyphenated  
- Version suffix required (e.g., `-v1`)

---

## `description` (Collections)
Human-readable description of dataset group.  
Used in STAC viewers and KFM metadata browsers.

---

## `bbox`
Generalized bounding box.  
**KFM Rule:** Must reflect generalized extents, not original coordinates.

---

## `geometry`
Geometry of the dataset.  
**Allowed types:** `MultiPoint`, `Polygon`, `MultiPolygon`.

**KFM Rule:**  
- **No exact coordinates allowed**  
- Must be H3 generalized or simplified geometries

---

## `extent` (Collections)
Defines spatial + temporal extents.

### `extent.spatial.bbox`
Generalized bounding box array.

### `extent.temporal.interval`
ISO timestamps; OWL-Time compliant.

---

## `assets`
Provides access to actual data.

### `assets.data`
- `href`: relative or absolute link to artifacts inventory  
- `type`: correct MIME (e.g., `"text/csv"`)  
- `roles`: must include `"data"`

---

## `links`
Used for STAC tree navigation.

### Required for KFM:
- `rel: "collection"` → link to parent Collection

Optional in internal repo unless STAC API is deployed.

---

# 🧭 2. KFM Archaeology Extension Fields (`kfm:*`)

These are **mandatory for all artifact inventory datasets** in the archaeology domain.

---

## `kfm:phase`
Cultural-phase name.  
Examples: `"Late Prehistoric"`, `"Middle Ceramic"`.

**Used for:**  
- Timelines  
- Story Nodes  
- Graph filtering  
- Focus Mode context  

---

## `kfm:material_class`
Controlled vocabulary:

- `"lithic"`  
- `"ceramic"`  
- `"metal"`  
- `"faunal"`  
- `"all"` (collections only)

---

## `kfm:datatype`
For artifact inventories:  
**Always** `"artifact-inventory"`.

---

## `kfm:source`
Institution providing dataset (e.g., `"WSU Open Collections"`).

---

## `kfm:provenance`
Relative path to PROV-O lineage JSON.

---

## `kfm:review_cycle`
Validation + governance cycle.  
Examples: `"Biannual"`, `"Quarterly"`.

---

# ⚖️ 3. CARE Cultural Safety Fields (`care:*`)

These fields are **required** for every archaeology dataset in KFM.

---

## `care:sensitivity`
Allowed values:

- `"general"`  
- `"generalized"`  
- `"restricted-generalized"`

**Rules:**  
- `"restricted"` **not permitted** for artifact inventories  
- `"generalized"` required if coordinates are generalized  
- `"general"` for faunal (PD) datasets  

---

## `care:review`
Indicates cultural review authority.

Allowed values:

- `"faircare"`  
- `"tribal"`  
- `"none-required"`

**Rules:**  
- Metal protohistoric inventories → `"tribal"`  
- Ceramics with motifs → `"faircare"`

---

## `care:notes`
Explanation of cultural safety adjustments.

Examples:  
- `"Motif categories filtered for cultural safety."`  
- `"Location generalized due to sacred-site proximity."`  

---

## `care:visibility_rules`
Visibility restrictions:

- `"h3-only"` → Only H3 index allowed (no geometry)  
- `"no-exact-points"` → Geometry allowed but generalized

---

# 📦 4. Scientific Metadata (`sci:*`)

Optional but encouraged.

### Examples:
- `sci:doi`
- `sci:citations`
- `sci:authors`

KFM encourages inclusion when publishing datasets based on academic work.

---

# 🔗 5. DCAT → STAC Crosswalk Rules

DCAT metadata must be reflected in STAC Items/Collections.

| DCAT Field | Required STAC Mapping |
|---|---|
| `dct:title` | `description` or STAC Item name |
| `dct:license` | STAC `license` |
| `dct:temporal` | STAC `properties.start_datetime` / `end_datetime` |
| `dcat:distribution` | STAC `assets.data.href` |
| `dcat:keyword` | Custom `keywords` field (optional) |

---

# 🗺️ 6. Spatial Generalization Requirements

To protect archaeological site locations:

- All coordinates must be generalized, never exact  
- Use **H3 levels 5–7**  
- No excavation unit IDs  
- No burial features  
- No raw LiDAR grid locations  
- Use simplified polygons for landscapes  

Failure to generalize → **automatic dataset rejection** by CI.

---

# 🧪 7. Validation & CI Requirements

Every STAC Item or Collection must pass:

- `stac-item-schema.json`  
- `stac-collection-schema.json`  
- `kfm-archaeology-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json`  
- SHA-256 checksum validation  
- Provenance linkage validation  
- H3 generalization rule checks  

CI workflows:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  

---

# 🧠 8. Knowledge Graph Integration

Each STAC Item maps directly to:

### Node Types:
- `ArtifactInventory`  
- `MaterialClass`  
- `CulturalPhase`  
- `GeneralizedSite`  

### Relationships:
- `HAS_INVENTORY`  
- `BELONGS_TO_PHASE`  
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  

---

# 🧩 9. Focus Mode v2 Integration

Artifact metadata drives:

- Material culture narratives  
- Regional chronology synthesis  
- Sensitivity-aware narrative shaping  
- Provenance chips (audit trail in UI)  

Focus Mode requires:

- Cultural phase  
- Material class  
- Sensitivity classification  
- Provenance linkage  
- Source institution  

---

# 🕰️ 10. Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created STAC Annotated Field Guide; added mappings for STAC ↔ DCAT ↔ PROV-O ↔ KG; ensured KFM-MDP v10.4 compliance |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial notes scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Annotated STAC Examples](README.md)

</div>