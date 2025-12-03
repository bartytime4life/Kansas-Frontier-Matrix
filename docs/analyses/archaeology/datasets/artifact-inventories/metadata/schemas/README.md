---
title: "📐 Kansas Frontier Matrix — Artifact Inventory Metadata Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md"
description: "JSON Schema index for validating KFM v11 artifact-inventory metadata (DCAT, STAC, CARE, and provenance crosswalks)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-metadata-schemas-v11.2.3"
doc_kind: "Schema Index"
intent: "artifact-inventory-metadata-schemas"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-metadata-schemas-v11.2.3"
category: "Analyses · Archaeology · Metadata · Schemas"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-metadata-schemas-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📐 Kansas Frontier Matrix — Artifact Inventory Metadata Schemas (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md`

**Purpose**  
Define and govern the **JSON Schema standards** used to validate **metadata files** for artifact inventory datasets within the Kansas Frontier Matrix (KFM) v11.

These metadata schemas ensure compliance with:

- **DCAT 3.0**  
- **STAC 1.0** (referential alignment with `stac/items/`)  
- **CIDOC-CRM** (conceptual mapping)  
- **PROV-O** (lineage structures)  
- **CARE** cultural safety metadata  
- **FAIR** principles (Findable, Accessible, Interoperable, Reusable)  
- **MCP-DL v6.3** documentation-first governance  

Metadata validated by these schemas describes datasets located in:

- `inventories/`  
- `stac/items/`  
- `provenance/`  

and is essential for searchability, reproducibility, graph ingestion, Focus Mode v3 interpretability, and cultural compliance.

---

## 📘 Overview

This folder contains:

- **Core metadata validation schemas**  
- **DCAT 3.0 alignment schemas**  
- **CARE sensitivity schemas specific to metadata**  
- **Provenance-link validation schemas**  
- **STAC crosswalk schemas** linking metadata to STAC Items and provenance specs  

Every metadata file in `metadata/` must validate against one or more schemas from this directory as part of CI.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/
├── 📄 README.md                        # This file
├── 📄 dcat-metadata-schema.json        # DCAT 3.0 validation schema
├── 📄 metadata-core-schema.json        # Core metadata fields validator
├── 📄 care-metadata-schema.json        # CARE cultural safety metadata validator
├── 📄 provenance-link-schema.json      # Ensures metadata ↔ provenance linkage
├── 📄 stac-crosswalk-schema.json       # Ensures STAC–metadata alignment
└── 📂 templates/                       # Schema templates for contributors
~~~

This layout is **normative** for artifact-inventory metadata schemas.

---

## 1️⃣ Core Metadata Schema (`metadata-core-schema.json`)

The **core metadata schema** validates the baseline structure for artifact-inventory metadata files.

### Required fields

| Field          | Description                       |
|----------------|-----------------------------------|
| `dct:title`    | Human-readable dataset title      |
| `dct:description` | Summary of dataset contents  |
| `dct:license`  | SPDX ID (for example, `CC-BY-4.0`, `CC0-1.0`) |
| `kfm:phase`    | Cultural-phase classification     |
| `kfm:material_class` | Artifact material type     |
| `kfm:source`   | Data origin institution / repository |
| `kfm:provenance` | Path to PROV-O JSON log       |

### Optional but strongly encouraged

- `dcat:keyword`  
- Citation information (for example, `dct:bibliographicCitation`)  
- Contact point (for example, `dcat:contactPoint`)  

The core schema ensures that all metadata records carry the minimal information required for FAIR discovery, attribution, and governance.

---

## 2️⃣ DCAT 3.0 Schema (`dcat-metadata-schema.json`)

The **DCAT metadata schema** enforces DCAT 3.0 compliance for artifact-inventory metadata.

### Required DCAT fields

| DCAT Field         | Example                                           |
|--------------------|---------------------------------------------------|
| `dct:title`        | `"Flint Hills Lithic Inventory v11"`             |
| `dct:license`      | `"CC-BY-4.0"`                                     |
| `dcat:distribution`| `"inventories/flint-hills-lithics-v11.csv"`      |
| `dct:temporal`     | `"1200–1400 CE"` or an interval representation   |
| `dcat:keyword`     | `["lithic", "archaeology", "inventory"]`         |

### DCAT ↔ STAC crosswalk expectations

The schema ensures that:

| DCAT Field         | Must align with STAC                           |
|--------------------|-----------------------------------------------|
| `dct:title`        | STAC `id` or `description`                    |
| `dcat:distribution`| STAC `assets.data.href`                       |
| `dct:temporal`     | STAC temporal properties / Collection extent  |
| `dct:license`      | STAC `license` / `dct:license`                |

Any inconsistency between DCAT and STAC is treated as a validation failure.

---

## 3️⃣ CARE Metadata Schema (`care-metadata-schema.json`)

The **CARE metadata schema** validates cultural safety information at the metadata level.

### Required CARE fields

| Field                | Allowed Values / Notes                                      |
|----------------------|------------------------------------------------------------|
| `care:sensitivity`   | `"general"`, `"generalized"`, `"restricted-generalized"`   |
| `care:review`        | `"faircare"`, `"tribal"`, `"none-required"`                |
| `care:notes`         | Required when sensitivity is `generalized` or `restricted-generalized` |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"`                      |

### Rules enforced by schema

- `care:sensitivity = "restricted"` is **forbidden** for artifact-inventory metadata in the public-governed catalog.  
- `care:review = "tribal"` is required for certain contact-era / protohistoric metal datasets.  
- All spatial generalization and redaction steps must be documented in `care:notes`.  

These rules must align with the global sovereignty policy and other CARE documentation.

---

## 4️⃣ Provenance Link Schema (`provenance-link-schema.json`)

The **provenance link schema** ensures that metadata records correctly reference PROV-O lineage logs.

Checks include:

- `kfm:provenance` must be present and must:
  - Match the filename stem with corresponding file in `provenance/`.  
  - Use consistent relative paths (for example, `"provenance/flint-hills-lithics-v11.json"`).  

The schema is used to confirm cross-file consistency across:

- `metadata/FILE.json`  
- `provenance/FILE.json`  
- `stac/items/FILE.json`  
- `inventories/FILE.ext`  

Any mismatch between these locations is treated as an error and must be corrected before release.

---

## 5️⃣ STAC Crosswalk Schema (`stac-crosswalk-schema.json`)

The **STAC crosswalk schema** ensures metadata and STAC Items remain synchronized.

It verifies that:

| Metadata Field      | Must match STAC Item field                        |
|---------------------|---------------------------------------------------|
| `dct:title`         | STAC `id` or `description`                        |
| `kfm:phase`         | STAC `properties.kfm:phase`                       |
| `kfm:material_class` | STAC `properties.kfm:material_class`            |
| `kfm:source`        | STAC `properties.kfm:source` (if present)         |
| `kfm:provenance`    | STAC `properties.kfm:provenance`                  |

Validation failure here indicates drift between metadata and STAC, and must block CI and ingestion pipelines.

---

## 🧪 Validation Workflows

Artifact-inventory metadata is validated using:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/faircare-audit.yml` (where CARE-related checks apply)  

Validators perform:

1. JSON Schema validation against:
   - `metadata-core-schema.json`  
   - `dcat-metadata-schema.json`  
   - `care-metadata-schema.json`  
   - `provenance-link-schema.json`  
   - `stac-crosswalk-schema.json`  
2. CARE cultural review enforcement.  
3. Provenance integrity checks (paths and filename stems).  
4. DCAT 3.0 completeness and crosswalk checks.  
5. STAC alignment and ontology consistency checks.  
6. FAIR+CARE ethical compliance.

Any mismatch or violation results in **CI failure** and a governance block until resolved.

---

## 🧠 Integration Into the KFM Knowledge Graph

The schemas defined here drive consistent graph ingestion.

### Node types influenced by metadata schemas

- `ArtifactInventory`  
- `MaterialClass`  
- `CulturalPhase`  
- `DatasetSource`  
- `GeneralizedSite`  
- CARE-related nodes (for example, `CareSensitivityState`)  

### Relationships enforced by validation

- `HAS_METADATA` (Inventory → Metadata record)  
- `HAS_CARE_SENSITIVITY` (Inventory → CARE node)  
- `HAS_PROVENANCE` (Inventory → provenance log)  
- `BELONGS_TO_PHASE` (Inventory → CulturalPhase)  
- `HAS_DISTRIBUTION` (Metadata → distribution/asset nodes)  

These relationships power:

- Story Nodes (material/phase narratives)  
- Temporal culture arcs  
- Focus Mode v3 interpretive layers  
- Map + timeline overlays with sensitivity-aware behavior  

---

## 📝 Contributor Workflow

1. Start from a metadata template in `metadata/templates/`.  
2. Populate fields according to the **Metadata Standards** README and these schemas.  
3. Run local validation using:
   - `jsonschema`  
   - Any KFM CLI metadata validator (if available).  
4. Check alignment with:
   - Corresponding STAC Item in `stac/items/`.  
   - Provenance file in `provenance/`.  
5. Ensure CARE metadata is complete and accurate.  
6. Submit a PR; CI and FAIR+CARE governance will enforce adherence to these schemas.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee · FAIR+CARE Council | Updated schema index for KFM v11.2.3; clarified DCAT/STAC/CARE crosswalk roles and CI integration. |
| v10.4.0   | 2025-11-17 | Archaeology WG · Metadata Standards Subcommittee · FAIR+CARE Council | Added full metadata schema index, DCAT/STAC crosswalk validation, and CARE requirements. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                             | Initial schema structure and baseline validators.                       |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Metadata Directory](../README.md)
