---
title: "🧾 Kansas Frontier Matrix — Cultural Landscape Interaction Sphere Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/README.md"
description: "Metadata specification and governance framework for KFM v11 cultural landscape interaction-sphere datasets (DCAT + STAC + KFM + CARE)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-spheres-metadata-standards-v11.2.3"
doc_kind: "Metadata Standard"
intent: "cultural-landscape-interaction-spheres-metadata"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-interaction-spheres-metadata-standards-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-metadata-v1.json"
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
care_label: "CARE-Compliant"
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧾 Cultural Landscape Interaction Sphere Metadata Standards (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/README.md`

**Purpose**  
Provide the **metadata specification and governance framework** for all **interaction-sphere datasets** in the Kansas Frontier Matrix (KFM) v11.

Interaction spheres model:

- Broad-scale cultural networks and exchange systems  
- Contact, communication, and interaction routes  
- Fluid cultural regions across prehistoric, protohistoric, and early historic periods  

Metadata in this directory ensures that interaction-sphere datasets comply with:

- **FAIR+CARE** and sovereignty governance  
- **STAC 1.0** + KFM cultural-landscape extensions  
- **DCAT 3.0** dataset metadata standards  
- **CIDOC-CRM**, **GeoSPARQL**, **OWL-Time**, and **PROV-O** alignment  
- **KFM-MDP v11.2.2** documentation requirements  

Metadata is essential for:

- Graph ingestion  
- Map visualization and timeline overlays  
- Story Node v3 narratives  
- Focus Mode v3 interpretive logic  
- Versioned governance and auditability  

---

## 📘 Overview

Interaction-sphere metadata provides:

- Cultural, temporal, and spatial context (generalized).  
- Provenance and line-of-evidence transparency.  
- Ethical and cultural-safety details (CARE + sovereignty).  
- Discoverability through STAC and DCAT catalogs.  
- Structural scaffolding for Story Nodes and Focus Mode v3.

Typical datasets described here include:

- `great-bend-aspect/`  
- `central-plains-exchange/`  
- `protohistoric-wichita/`  
- Future interaction-sphere modules (for example, borderlands and contact zones).

Metadata files are stored as **JSON(-LD)** that combine DCAT, STAC-aligned fields, KFM extensions, and CARE metadata.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/
├── 📄 README.md                         # This file
├── 📄 great-bend-aspect-v2.json         # Metadata for Great Bend Aspect interaction sphere
├── 📄 central-plains-exchange-v2.json   # Metadata for Central Plains exchange sphere
├── 📄 protohistoric-wichita-v2.json     # Metadata for Protohistoric Wichita interaction sphere (high sensitivity)
└── 📂 templates/                        # Templates for creating new interaction-sphere metadata JSON files
~~~

Filenames must align with corresponding STAC Item IDs and provenance stems for each interaction sphere.

---

## 📚 Controlled Vocabularies (Interaction Spheres)

Interaction-sphere metadata should use consistent vocabularies, aligned with STAC and schemas in `stac/schemas/`:

| Field                     | Allowed / Example Values                                       |
|---------------------------|----------------------------------------------------------------|
| `kfm:region_type`         | `interaction_sphere`, `exchange_zone`, `contact_region`        |
| `kfm:interaction_type`    | `influence_sphere`, `contact_zone`, `exchange_corridor`, `other` |
| `care:consent_status`     | `approved`, `conditional`, `not-approved`, `not-applicable`    |

Additional vocabularies (for example, phase labels) must align with KFM’s cultural-phase ontology.

---

## 📦 Required Metadata Components (All Interaction Spheres)

Each metadata JSON file must contain:

1. **DCAT 3.0 dataset metadata**  
2. **KFM cultural-landscape extensions (`kfm:*`)**  
3. **CARE cultural-safety metadata (`care:*`)**  
4. **Provenance linkage (PROV-O references)**  
5. **STAC alignment** with the corresponding Item/Collection

Below, “dataset” refers to a single interaction-sphere dataset (for example, Great Bend Aspect v2).

---

### 1️⃣ DCAT 3.0 Metadata

Required DCAT fields:

| Field             | Description                           | Example                                                     |
|-------------------|---------------------------------------|-------------------------------------------------------------|
| `dct:title`       | Dataset title                         | `"Great Bend Aspect Interaction Sphere v2"`                 |
| `dct:description` | Generalized cultural summary          | `"Generalized Late Prehistoric–Protohistoric cultural interaction region."` |
| `dct:license`     | SPDX license                          | `"CC-BY-4.0"`                                               |
| `dct:temporal`    | OWL-Time interval / text              | `"AD 1350–1700"`                                            |
| `dct:creator`     | Primary creator / steward             | `"Cultural Landscape Working Group"`                        |
| `dcat:keyword`    | Tags                                  | `["interaction sphere", "archaeology", "Kansas"]`           |
| `dcat:distribution` | Link to distribution or STAC Item   | `"stac/items/great-bend-aspect-v2.json"`                    |

DCAT entries must be consistent with:

- STAC Collection/Item `id`, `description`, `license`, and temporal coverage.  
- CARE and provenance fields.

---

### 2️⃣ KFM Cultural-Landscape Metadata (`kfm:*`)

KFM metadata enriches DCAT and STAC with domain specifics:

| Field                     | Description                               | Example                                         |
|---------------------------|-------------------------------------------|-------------------------------------------------|
| `kfm:domain`              | Domain identifier                         | `"archaeology-cultural-landscapes"`            |
| `kfm:landscape_type` / `kfm:region_type` | Dataset class           | `"interaction_sphere"`                         |
| `kfm:culture_phase`       | Cultural phases represented               | `["Late Prehistoric", "Protohistoric-Wichita"]` |
| `kfm:generalization`      | Generalization mechanism                  | `"H3-r7"`                                       |
| `kfm:source`              | Dataset origin description                | `"Published archaeological syntheses + approved ethnohistoric summaries"` |
| `kfm:provenance`          | Path to PROV-O lineage JSON               | `"../provenance/great-bend-aspect-v2.json"`    |
| `kfm:schema_version`      | Metadata schema/template version          | `"v11.0.0"`                                     |

These fields must match KFM fields in STAC Items and provenance logs.

---

### 3️⃣ CARE Cultural-Safety Metadata (`care:*`)

Because interaction spheres may involve sensitive cultural knowledge, CARE metadata is required for all datasets.

Required fields:

| CARE Field             | Allowed / Example Values                                    | Notes |
|------------------------|-------------------------------------------------------------|-------|
| `care:sensitivity`     | `"general"`, `"generalized"`, `"restricted-generalized"`    | Many protohistoric/ethnohistoric spheres will be `"restricted-generalized"`. |
| `care:review`          | `"faircare"`, `"tribal"`, `"none-required"`                 | `tribal` required when descendant communities are directly implicated. |
| `care:notes`           | Free-text explanation of cultural-safety decisions          | Must describe generalization, redactions, and review outcomes. |
| `care:visibility_rules`| `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"` | `"h3-only"` recommended for high-sensitivity spheres. |
| `care:consent_status`  | `approved`, `conditional`, `not-approved`, `not-applicable` | Used especially for high-sensitivity (e.g., `protohistoric-wichita`). |

Forbidden in public-governed interaction-sphere metadata:

- `care:sensitivity = "restricted"`  
- Exact boundaries of sacred/ceremonial landscapes.  
- Sensitive oral-historical content without explicit tribal approval.

CARE values must be consistent with the corresponding STAC and provenance entries.

---

### 4️⃣ Provenance Linkage (PROV-O)

Every metadata record must reference a **PROV-O provenance file**:

- Field: `kfm:provenance` → path to provenance JSON for this interaction sphere:  
  - For example, `"../provenance/great-bend-aspect-v2.json"` or `"../provenance/protohistoric-wichita-v2.json"`.  

The referenced provenance log must:

- Cover raw → generalized → processed transformations.  
- Describe generalization parameters (H3, simplification) and redaction steps.  
- Record FAIR+CARE and tribal/sovereignty review events.  

---

### 5️⃣ STAC Alignment

Metadata must align with STAC Collection/Item in `../stac/` and global interaction-sphere STAC catalog.

Key alignments:

| Metadata Field           | STAC Field                                            |
|--------------------------|------------------------------------------------------|
| `dct:title`              | `id` / `description` of the corresponding STAC Item |
| `dct:license`            | STAC `license`                                      |
| `dct:temporal`           | STAC `extent.temporal` or Item temporal properties  |
| `dcat:distribution`      | STAC `assets.data.href` or Item/Collection paths    |
| `kfm:culture_phase`      | `properties.kfm:culture_phase` / `properties.kfm:phase` |
| `kfm:provenance`         | `properties.kfm:provenance`                         |
| `care:*`                 | `properties.care:*`                                  |

Any mismatch must be resolved before a dataset is considered governed and Active.

---

## 🧪 Validation & CI

Interaction-sphere metadata files must pass validation via:

- Metadata schemas in:
  - `metadata/schemas/` for interaction spheres.  
- DCAT 3.0 validation (required fields and constraints).  
- CARE schema validation (allowed values, required notes).  
- STAC crosswalk validation (alignment with STAC Items/Collections).  
- Provenance-link validation (ensuring `kfm:provenance` paths exist and are correct).

Typical CI workflows:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

Validation failures must block merges affecting interaction-sphere metadata.

---

## 🧠 Integration Into KFM Knowledge Graph

From these metadata records, graph ingestion will create/enrich:

**Nodes**

- `InteractionSphere` (e.g., Great Bend, Central Plains exchange, Protohistoric Wichita).  
- `MetadataRecord` for each dataset.  
- `CulturalPhase` nodes linked to interaction spheres.  
- `CareSensitivityState` / related nodes capturing CARE status.

**Relationships**

- `HAS_METADATA` (InteractionSphere → MetadataRecord).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE node).  
- `HAS_PROVENANCE` (via metadata → provenance link).  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase / TimeInterval).  
- `ASSOCIATED_WITH` (linking spheres to artifact inventories, other landscape datasets, and narratives).

These relationships drive graph queries, visualizations, and narrative constraints.

---

## 🔗 Related Specifications

For full governance of interaction-sphere data:

- `../README.md`  
  – Interaction-spheres dataset overview and governance.  
- `../stac/README.md`  
  – Interaction-sphere STAC catalog (Items + Collections).  
- `../stac/schemas/README.md`  
  – STAC schemas for interaction spheres.  
- `../provenance/README.md`  
  – Provenance standards and QA templates for interaction spheres.  
- `../../metadata/README.md`  
  – Global cultural-landscape metadata standards (if present).  

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Updated to KFM v11.2.3; aligned with global interaction-sphere STAC/metadata/provenance schemas and CARE vocabularies. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Initial metadata standards for interaction spheres; defined DCAT/STAC/CARE core requirements. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                                  | Prototype specification and directory structure.                        |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Spheres](../README.md)
