---
title: "📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Item Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-item-field-guide-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Field Guide"
intent: "artifact-stac-item-field-guide"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📖 **Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Item Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md`

**Purpose:**  
Serve as the **complete reference manual** for interpreting every field used in the annotated **STAC Item templates** for artifact inventories within the Kansas Frontier Matrix (KFM).  
This guide ensures contributors, metadata engineers, archaeologists, and ethics reviewers understand:

- STAC 1.0 Item structure  
- Artifact-specific metadata requirements  
- Cultural safety rules (CARE extension)  
- KFM archaeology domain extensions (`kfm:*`)  
- Generalization and sovereignty constraints  
- Validation rules for CI/CD  
- Crosswalks between STAC → DCAT → PROV-O → Knowledge Graph → Story Nodes  

</div>

---

# 🗂️ 1. STAC Core Fields (STAC 1.0)

These fields are required for **every** STAC Item describing archaeological artifact inventories in KFM.

---

## `stac_version`
- Must always be `"1.0.0"`.

---

## `type`
- Must always be `"Feature"` for STAC Items.

---

## `id`
- Lowercase, hyphenated, versioned ID (e.g., `prairie-ceramics-v1`).  
- Must match filename and provenance/metadata IDs.

---

## `bbox`
- Generalized spatial extent of the dataset.  
- Derived from **H3 5–7** region, not precise coordinates.

---

## `geometry`
- Allowed types: `"MultiPoint"`, `"Polygon"`, `"MultiPolygon"`.  
- All coordinates must be generalized; no exact provenience.

---

## `properties`
Container for archaeological, cultural, and scientific metadata.

---

## `assets.data`
Defines where the actual dataset is stored.

- `href`: relative path to CSV inventory.  
- `type`: must be `"text/csv"`.  
- `roles`: must include `"data"`.

---

## `links.collection`
Required link back to the parent STAC Collection.

---

# 🧭 2. KFM Archaeology Extension Fields (`kfm:*`)

These fields allow STAC Items to integrate cleanly with:

- KFM knowledge graph  
- Story Nodes  
- Focus Mode v2  
- Pipelines & reproducible analyses  

---

## `kfm:phase`
Cultural-phase classification (e.g., `"Late Prehistoric"`).  
Required for:

- Timelines  
- Entity linking  
- Story Node generation  
- Focus Mode contextualization  

---

## `kfm:material_class`
Controlled vocabulary:

- `"lithic"`  
- `"ceramic"`  
- `"metal"`  
- `"faunal"`

Ensures semantic consistency across datasets.

---

## `kfm:datatype`
- Must always be `"artifact-inventory"`.

---

## `kfm:source`
Institution or repository providing dataset.  
Required for provenance tracking.

---

## `kfm:provenance`
Path to PROV-O lineage JSON file.

Links each STAC Item to:

- Raw → cleaned → final transformations  
- Cultural review notes  
- Generalization process  
- Analyst + reviewer identities  

---

# ⚖️ 3. CARE Cultural Safety Fields (`care:*`)

CARE metadata ensures KFM’s archaeological data handling respects Indigenous sovereignty, avoids harm, and supports ethical representation.

---

## `care:sensitivity`
Allowed values:

- `"general"`  
- `"generalized"`  
- `"restricted-generalized"`

Rules:

- `"restricted"` is not permitted for artifact inventories.  
- `"generalized"` required whenever spatial generalization is applied.  
- `"general"` used only for PD faunal datasets.

---

## `care:review`
Indicates who completed the cultural review:

- `"faircare"`  
- `"tribal"`  
- `"none-required"`  

**Metals/protohistoric datasets must use `"tribal"`**.

---

## `care:notes`
Text field documenting cultural review considerations.

Examples:

- “Motifs filtered to avoid sacred symbolism.”  
- “Locations generalized from sensitive cultural landscapes.”  

---

## `care:visibility_rules`
Controls how much detail can be exposed to users:

- `"h3-only"` — Only H3 index allowed; **no geometry visible**  
- `"no-exact-points"` — Generalized geometry allowed

Artifact inventories must respect these safety layers.

---

# 🔬 4. Scientific Metadata (`sci:*`)

Optional but encouraged.

Examples:

- `sci:doi` — DOI of academic dataset  
- `sci:citations` — References  
- `sci:authors` — Original data creators  

Improves traceability in Story Nodes and Focus Mode.

---

# 🔗 5. DCAT → STAC Crosswalk Requirements

To ensure external interoperability (CKAN, DataHub):

| DCAT Field | STAC Mapping |
|---|---|
| `dct:title` | `id` or `description` |
| `dct:license` | `license` |
| `dct:temporal` | `properties.start_datetime` / `end_datetime` |
| `dcat:distribution` | `assets.data.href` |
| `dcat:keyword` | Custom STAC `keywords` array |

DCAT compliance is mandatory for KFM release manifests.

---

# 🌐 6. Spatial Generalization Rules

KFM prohibits publishing archaeologically sensitive coordinates.

**Rules:**

- Use **H3 level 5–7** for all spatial data.  
- Replace exact artifact provenience with generalized points.  
- Use simplified polygons for cultural landscapes.  
- Ensure bounding boxes reflect generalized extents.  
- Never publish excavation units, burial coordinates, or sacred site locations.

Generalization compliance is automatically enforced in CI.

---

# 🧪 7. Validation Requirements

All STAC Items must pass:

- `stac-item-schema.json`  
- `kfm-archaeology-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json`  
- SHA-256 checksum validation  
- Crosswalk consistency with:
  - Inventory CSV  
  - Metadata JSON  
  - Provenance JSON  
  - STAC Collection  

Validation workflows:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  

---

# 🧠 8. Knowledge Graph Mapping

STAC Items create or update entities:

### Node Types
- `ArtifactInventory`  
- `Artifact` (expanded at runtime)  
- `MaterialClass`  
- `CulturalPhase`  
- `GeneralizedSite`  

### Relationships
- `HAS_INVENTORY`  
- `BELONGS_TO_PHASE`  
- `LOCATED_AT` (via H3)  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  

Graph integration is essential for Story Nodes and Focus Mode reasoning.

---

# 📝 9. Story Node + Focus Mode Integration

Artifact metadata affects:

- Narrative tone  
- Cultural framing  
- Timeline placement  
- Provenance chip rendering  
- Sensitivity warnings  
- AI interpretability  

All STAC Items must support:

- Ethical narrative generation  
- Multi-layer map overlays  
- Temporal-context synthesis

---

# 🕰️ 10. Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Completed artifact STAC Item annotated field guide with crosswalks, safety rules, and KG/Focus Mode mapping |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial notes scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Annotated STAC Item Templates](../README.md)

</div>