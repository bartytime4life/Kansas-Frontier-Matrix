---
title: "📐 Kansas Frontier Matrix — Artifact Inventory Metadata Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-metadata-schemas-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Schema Index"
intent: "artifact-inventory-metadata-schemas"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Artifact Inventory Metadata Schemas**  
`docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md`

**Purpose:**  
Define and govern the **JSON Schema standards** used to validate *metadata files* for all artifact inventory datasets within the Kansas Frontier Matrix (KFM).  
These metadata schemas ensure compliance with:

- **DCAT 3.0**  
- **STAC 1.0 (referential alignment)**  
- **CIDOC-CRM conceptual mapping**  
- **PROV-O lineage structures**  
- **CARE Cultural Safety Metadata**  
- **FAIR standards (Findable, Accessible, Interoperable, Reusable)**  
- **MCP-DL v6.3 documentation-first governance**

Metadata in this directory describes datasets located in:
- `inventories/`  
- `stac/items/`  
- `provenance/`  

It is essential for searchability, reproducibility, graph ingestion, Focus Mode v2 interpretability, and cultural compliance.

</div>

---

# 📘 Overview

This folder contains:

- **Metadata validation schemas**  
- **CARE sensitivity schemas specific to metadata**  
- **DCAT 3.0 alignment schemas**  
- **Provenance/lineage validation schemas**  
- **Composite schemas** linking metadata to STAC and provenance specs  

Each metadata file in `metadata/` must validate against one or more schemas located here.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/
├── README.md                                  # This file
├── dcat-metadata-schema.json                   # DCAT 3.0 validation schema
├── metadata-core-schema.json                   # Core metadata fields validator
├── care-metadata-schema.json                   # CARE cultural safety metadata validator
├── provenance-link-schema.json                 # Ensures metadata ↔ provenance linkage
├── stac-crosswalk-schema.json                  # Ensures STAC–metadata alignment
└── templates/                                  # Schema templates for contributors
~~~

---

# 📦 1. Core Metadata Schema (`metadata-core-schema.json`)

This schema validates the **baseline metadata structure** for artifact inventories.

### Required fields:

| Field | Description |
|---|---|
| `dct:title` | Human-readable dataset title |
| `dct:description` | Summary of dataset contents |
| `dct:license` | SPDX ID (`CC-BY-4.0` or `CC0`) |
| `kfm:phase` | Cultural-phase classification |
| `kfm:material_class` | Artifact material type |
| `kfm:source` | Data origin institution |
| `kfm:provenance` | Path to PROV-O JSON |

### Optional but encouraged:

- `keywords`  
- `citation`  
- `contactPoint`  

---

# 📦 2. DCAT 3.0 Schema (`dcat-metadata-schema.json`)

Ensures DCAT compliance for all artifact inventory metadata.

### Required:

| DCAT Field | Example |
|---|---|---|
| `dct:title` | `"Flint Hills Lithic Inventory v1"` |
| `dct:license` | `"CC-BY-4.0"` |
| `dcat:distribution` | `"inventories/flint-hills-lithics-v1.csv"` |
| `dct:temporal` | `"1200–1400 CE"` |
| `dcat:keyword` | `["lithic", "archaeology", "inventory"]` |

### DCAT–STAC Crosswalk Requirements:

| DCAT | STAC |
|---|---|
| `dct:title` | `description` or `id` |
| `dcat:distribution` | `assets.data.href` |
| `dct:temporal` | `properties.start_datetime/end_datetime` |
| `dct:license` | `license` |

All metadata and STAC Items must remain aligned.

---

# 📦 3. CARE Metadata Schema (`care-metadata-schema.json`)

Validates cultural safety metadata for artifact inventories.

### Required fields:

| Field | Allowed Values |
|---|---|---|
| `care:sensitivity` | `"general"`, `"generalized"`, `"restricted-generalized"` |
| `care:review` | `"faircare"`, `"tribal"`, `"none-required"` |
| `care:notes` | Free text explaining safety review |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"` |

### Rules:

- `"restricted"` sensitivity is forbidden in public KFM datasets  
- `"tribal"` review required for protohistoric metals  
- All dataset generalization steps must be documented in `care:notes`

---

# 📦 4. Provenance Link Schema (`provenance-link-schema.json`)

Ensures that metadata files:

- Correctly reference PROV-O lineage JSON  
- Include valid paths to provenance logs  
- Follow naming conventions across:
  - `metadata/FILE.json`
  - `provenance/FILE.json`
  - `stac/items/FILE.json`
  - `inventories/FILE.csv`

Required field:
- `kfm:provenance` (MUST match filename stem)

---

# 📦 5. STAC Crosswalk Schema (`stac-crosswalk-schema.json`)

Ensures metadata and STAC items **stay synchronized**.

Checks:

| Metadata Field | Must Match STAC |
|---|---|---|
| `dct:title` | STAC `id` or `description` |
| `kfm:phase` | STAC `properties.kfm:phase` |
| `kfm:material_class` | STAC `properties.kfm:material_class` |
| `kfm:source` | STAC `properties.kfm:source` |
| `kfm:provenance` | STAC `properties.kfm:provenance` |

Validation failure halts CI + ingestion pipelines.

---

# 🧪 Validation Workflows

Metadata is validated in:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

Validators perform:

1. Schema validation  
2. CARE cultural review enforcement  
3. Provenance integrity checks  
4. DCAT 3.0 completeness checks  
5. STAC crosswalk consistency  
6. FAIR+CARE ethical compliance  

Any mismatch → **CI failure** and governance block.

---

# 🧠 Integration Into KFM Knowledge Graph

Metadata fields populate graph nodes:

### Artifact-Level Nodes
- `ArtifactInventory`
- `MaterialClass`
- `CulturalPhase`
- `DatasetSource`
- `GeneralizedSite`

### Relationships
- `HAS_METADATA`  
- `HAS_CARE_SENSITIVITY`  
- `HAS_PROVENANCE`  
- `BELONGS_TO_PHASE`  
- `HAS_DISTRIBUTION`  

These relationships power:

- Story Nodes  
- Temporal culture arcs  
- Focus Mode v2 interpretive layers  
- Map + timeline overlays  

---

# 📝 Contributor Workflow

1. Create metadata JSON from a template (in `/templates`).  
2. Validate locally using:
   - `jsonschema`  
   - KFM CLI validator  
3. Confirm alignment with STAC Item + provenance.  
4. Ensure CARE cultural safety metadata is complete.  
5. Commit & submit PR for FAIR+CARE governance.  

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · Metadata Subcommittee · FAIR+CARE Council | Added full metadata schema index, DCAT/STAC crosswalk validation, CARE requirements |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial schema structure and baseline validators |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Metadata Directory](../README.md)

</div>