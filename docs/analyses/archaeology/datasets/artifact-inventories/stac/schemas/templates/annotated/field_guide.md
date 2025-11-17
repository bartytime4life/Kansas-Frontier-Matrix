---
title: "📖 Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Schema Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/field_guide.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Metadata Standards Subcommittee · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-schema-field-guide-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Field Guide"
intent: "artifact-stac-schema-field-guide"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📖 **Kansas Frontier Matrix — Field Guide for Annotated Artifact STAC Schema Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/field_guide.md`

**Purpose:**  
Provide the **authoritative reference** for interpreting every component inside the annotated schema templates used to validate artifact inventory **STAC Items** and **STAC Collections** in the Kansas Frontier Matrix (KFM).  
This guide explains:

- STAC 1.0 schema-level validation rules  
- KFM archaeology extension field constraints (`kfm:*`)  
- CARE cultural safety schema (`care:*`)  
- DCAT 3.0 crosswalk schema mappings  
- JSON Schema Draft 2020–12 conventions  
- CI/CD validator expectations  
- How validated metadata enters the graph, Story Nodes, and Focus Mode v2  

</div>

---

# 🧩 1. JSON Schema Draft 2020–12 — Overview

All schemas in KFM conform to **JSON Schema Draft 2020–12**, enforced by:

- KFM validators  
- GitHub CI workflows  
- STAC compliance tooling  
- Downstream validation inside the Neo4j ingestion pipeline  

### Required schema-level components:

| Component | Purpose |
|---|---|
| `$schema` | Identifies schema version for validators |
| `title` | Human-readable name for schema |
| `type` | Data type of root object |
| `required` | Fields that **must** be present |
| `properties` | Allowed fields + sub-schemas |
| `enum` / `const` | Constraint validators (critical for CARE/KFM fields) |

All schema templates in KFM must include:

- `$schema`: Draft 2020–12  
- `type`: `"object"`  
- No `$ref` to external schemas outside the repo unless documented

---

# 🗂️ 2. STAC Item Schema Components

The annotated STAC Item schema validates artifact inventory Items.

### Required fields:

| Field | Notes |
|---|---|
| `id` | Must match filename + version pattern |
| `type` | Forced to `"Feature"` |
| `stac_version` | `"1.0.0"` only |
| `bbox` | Four-number array; generalized only |
| `geometry` | No raw coordinates |
| `properties` | Container for domain metadata |
| `assets` | All Items must include `"data"` asset |

### Rules:

- `geometry.type`: Must be `MultiPoint`, `Polygon`, or `MultiPolygon`  
- `assets.data.roles`: Must include `"data"`  
- `properties`: Must accept KFM + CARE extension fields  

All STAC Item schemas prohibit:

- Raw coordinates  
- Sensitive archaeological provenience  
- `"restricted"` CARE statuses  

---

# 🗂️ 3. STAC Collection Schema Components

Validates groups of artifact inventory Items.

### Required fields:

| Field | Notes |
|---|---|
| `id` | Matches collection filename |
| `stac_version` | `"1.0.0"` mandatory |
| `type` | `"Collection"` |
| `extent.spatial` | Must define generalized bounding box |
| `extent.temporal` | Must follow OWL-Time conventions |
| `license` | SPDX code; `"CC-BY-4.0"` or `"CC0"` |

Prohibited:

- Exact spatial extents  
- Missing temporal intervals  
- Non-open licenses  

Allowed geometry for extent: **generalized bbox only**.

---

# 🧭 4. KFM Archaeology Schema Components (`kfm:*`)

These fields sit within `properties` (for Items) or root (for Collections).

### `kfm:phase`
- Cultural phase identifier (string)  
- Required for Items  
- Drives timeline logic + Focus Mode narrative context  

### `kfm:material_class`
- Enum: `"lithic"`, `"ceramic"`, `"metal"`, `"faunal"`, `"all"`  
- Required for both Items + Collections  

### `kfm:datatype`
- Constant: `"artifact-inventory"`  
- Ensures internal consistency  

### `kfm:source`
- Organization providing dataset  
- Enables Provenance chain linking  

### `kfm:provenance`
- Path to associated PROV-O JSON  
- Required for Items  

### `kfm:review_cycle`
- `"Biannual"` or `"Quarterly"`  
- Required for Collections  
- Used by FAIR+CARE governance  

Every KFM archaeology schema must validate these fields.

---

# ⚖️ 5. CARE Sensitivity Schema Components (`care:*`)

CARE ensures Indigenous sovereignty, ethical representation, and cultural safety.

### `care:sensitivity`
Allowed values:
- `"general"`  
- `"generalized"`  
- `"restricted-generalized"`

**Forbidden for Items:** `"restricted"`

### `care:review`
Allowed values:
- `"faircare"`  
- `"tribal"`  
- `"none-required"`

Metals/protohistoric artifacts → `"tribal"` required.

### `care:notes`
Provides human-readable cultural context and disclosure.

Examples:
- “Motifs filtered to avoid sacred symbolism.”
- “Coordinates generalized to H3 level 6.”

### `care:visibility_rules`
Allowed:
- `"h3-only"`  
- `"no-exact-points"`

Generalization requirements enforced at schema level.

---

# 🔗 6. DCAT → STAC Crosswalk Schema

Validates interoperability mapping between DCAT metadata and STAC.

### Required DCAT fields:

| DCAT Field | Required STAC Mapping |
|---|---|
| `dct:title` | STAC `description` or semantic equivalent |
| `dct:license` | STAC `license` |
| `dct:temporal` | STAC `extent.temporal.interval` |
| `dcat:distribution` | STAC `assets.data.href` (for Items) |
| `dcat:keyword` | STAC `keywords` |

Failure to align → **CI rejection**.

---

# 🧪 7. Schema Validation Logic in CI

Each schema is validated via:

- `jsonschema` Python validator  
- KFM internal schema validator  
- GitHub Actions workflow:
  - `.github/workflows/artifact-stac-validate.yml`

Validation checks include:

- Required fields present  
- Controlled vocabulary adherence  
- No forbidden CARE values  
- Spatial & temporal constraint checks  
- Crosswalk consistency  
- Schema structure (Draft 2020–12 conformant)  

Failed validation blocks PR merges.

---

# 🧠 8. Knowledge Graph Mapping Rules

Schema fields map directly to KFM graph entities:

### Item-Level:
| Field | Node |
|---|---|
| `kfm:phase` | `CulturalPhase` |
| `kfm:material_class` | `MaterialClass` |
| `care:sensitivity` | `CulturalSafetyLevel` |
| `bbox` | `GeneralizedSpatialExtent` |

### Collection-Level:
| Field | Node |
|---|---|
| `id` | `ArtifactCollection` |
| `extent.spatial` | `SpatialCoverage` |
| `extent.temporal` | `TemporalCoverage` |

### Relationships:
- `HAS_INVENTORY`  
- `BELONGS_TO_COLLECTION`  
- `HAS_CARE_SENSITIVITY`  
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  

---

# 📝 9. Story Node & Focus Mode Integration

Schemas influence:

- Automatic narrative shape  
- Cultural warnings  
- Provenance chips  
- Time-scope alignment  
- Descriptive safety (CARE-compliant)  
- AI interpretability through metadata exposure  

Focus Mode requires:

- Cultural phase  
- Provenance  
- Sensitivity  
- Material class  
- Generalized spatial info  

---

# 🏛️ 10. Sovereignty & Cultural Safety Enforcement

Schemas enforce the following absolute rules:

- **No raw coordinates**  
- **No burial or ceremonial features**  
- **No restricted datasets**  
- **No colonial-framing language**  
- **Mandatory review for protohistoric datasets**  
- **Generalization always required** (H3 5–7)  

Violations → CI fail + governance block.

---

# 🕰️ 11. Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Metadata Subcommittee · Archaeology WG · FAIR+CARE Council | Completed annotated schema field guide with crosswalk, safety, compiler-level, and graph mapping rules |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial scaffolding |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Annotated Schema Templates](../README.md)

</div>