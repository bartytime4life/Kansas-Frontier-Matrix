---
title: "🏺📑 Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/README.md"
description: "DCAT + STAC + KFM + CARE metadata specification for the Great Bend Aspect interaction-sphere dataset in KFM v11."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-great-bend-aspect-metadata-v11.2.3"
doc_kind: "Dataset Metadata"
intent: "great-bend-aspect-metadata"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-great-bend-aspect-metadata-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-metadata-v1.json"
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
care_label: "CARE-Compliant (Generalized)"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺📑 Great Bend Aspect Interaction Sphere — Metadata (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/README.md`

**Purpose**  
Provide the **metadata specification** for the **Great Bend Aspect (GBA) Interaction Sphere**, ensuring:

- FAIR+CARE alignment and sovereignty awareness.  
- **DCAT 3.0** and **STAC 1.0** interoperability.  
- Consistent **KFM cultural-landscape extensions (`kfm:*`)**.  
- Explicit **CARE** cultural-safety metadata.  
- Crosswalks to PROV-O provenance and graph ingestion.

This metadata governs how the Great Bend Aspect interaction sphere is described, discovered, and ethically used within the Kansas Frontier Matrix (KFM).

For the dataset overview, see:

- `../README.md`

For global interaction-sphere metadata standards, see:

- `../../metadata/README.md`

---

## 📘 Overview

The Great Bend Aspect Interaction Sphere describes a generalized Late Prehistoric–Protohistoric cultural landscape associated with:

- Ancestral Wichita and related Plains horticultural traditions.  
- Semi-sedentary horticulture blended with bison hunting.  
- Distinctive ceramic, architectural, and subsistence patterns.  
- Prairie–riverine ecotones in central Kansas.  
- Interaction with Central Plains, Southern Plains, and early contact networks.

This metadata ensures that the dataset:

- Uses **generalized geometry** only.  
- Encodes **cultural-phase and interaction-sphere semantics** via `kfm:*`.  
- Includes **CARE** fields suitable for **elevated sensitivity** (but not high-restricted).  
- Maintains consistent linkages with STAC Items and PROV-O provenance.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/
├── 📄 README.md                               # This file
└── 📄 great-bend-aspect-v2.json               # DCAT + KFM + CARE metadata for v2
~~~

`great-bend-aspect-v2.json` must be kept in sync with:

- `../stac/great-bend-aspect-v2.json` (STAC Item).  
- `../provenance/great-bend-aspect-v2.json` (provenance log).

---

## 📦 Metadata Specification (DCAT + KFM + CARE)

The metadata JSON must contain:

1. **DCAT 3.0 dataset metadata**.  
2. **KFM cultural-landscape extensions (`kfm:*`)**.  
3. **CARE** cultural-safety metadata (`care:*`).  
4. **Provenance linkage** to a PROV-O log.  
5. **STAC crosswalk** fields consistent with the STAC Item.

Below summarizes required components for `great-bend-aspect-v2.json`.

---

### 1️⃣ DCAT 3.0 Fields

| Field             | Description                         | Example                                                           |
|-------------------|-------------------------------------|-------------------------------------------------------------------|
| `dct:title`       | Dataset title                       | `"Great Bend Aspect Interaction Sphere v2"`                       |
| `dct:description` | Generalized cultural summary        | `"Generalized Late Prehistoric–Protohistoric interaction region in central Kansas."` |
| `dct:license`     | License                             | `"CC-BY-4.0"`                                                     |
| `dct:temporal`    | Temporal coverage (OWL-Time aligned)| `"AD 1350–1700"`                                                  |
| `dct:creator`     | Primary creator or steward          | `"Cultural Landscape Working Group"`                              |
| `dcat:keyword`    | Tags                                | `["Great Bend Aspect","Wichita","Late Prehistoric","Protohistoric"]` |
| `dcat:distribution` | STAC reference or asset path      | `"../stac/great-bend-aspect-v2.json"`                             |

These DCAT fields must crosswalk correctly to STAC:

- Title / description ↔ STAC `id` / `description`.  
- Temporal coverage ↔ STAC `extent.temporal` / Item temporal properties.  
- Distribution ↔ STAC `assets.data.href` or Item path.

---

### 2️⃣ KFM Cultural-Landscape Metadata (`kfm:*`)

KFM fields embed domain semantics and governance.

| Field                     | Purpose                                 | Example                                                    |
|---------------------------|-----------------------------------------|------------------------------------------------------------|
| `kfm:domain`              | Domain identifier                       | `"archaeology-cultural-landscapes"`                       |
| `kfm:landscape_type` / `kfm:region_type` | Dataset class          | `"interaction_sphere"`                                     |
| `kfm:culture_phase`       | Cultural phases represented             | `["GBA-Early","GBA-Middle","GBA-Late"]`                   |
| `kfm:generalization`      | Spatial generalization mechanism        | `"H3-r7"` (or `"H3-r6"` as implemented)                   |
| `kfm:source`              | Data origin summary                     | `"Public-domain archaeological synthesis and regional survey reports"` |
| `kfm:provenance`          | Link to PROV-O JSON provenance          | `"../provenance/great-bend-aspect-v2.json"`               |
| `kfm:schema_version`      | Metadata schema/template version        | `"v11.0.0"` or updated as appropriate                     |

These must match the STAC Item’s `properties.kfm:*` and the provenance record’s KFM fields.

---

### 3️⃣ CARE Cultural-Safety Metadata (`care:*`)

Because the GBA includes protohistoric components and descendant-community significance, **CARE metadata is mandatory**.

Recommended fields:

| CARE Field             | Recommended Values / Notes                               |
|------------------------|----------------------------------------------------------|
| `care:sensitivity`     | `"generalized"`                                          |
| `care:review`          | `"faircare"` (tribal advisory consultation recommended) |
| `care:notes`           | For example: `"Generalized polygons used; sensitive narratives and site-level details excluded."` |
| `care:visibility_rules`| `"polygon-generalized"` or `"h3-only"` for specific layers |
| `care:consent_status`  | `approved`, `conditional`, `not-approved`, or `not-applicable` (e.g., `"approved"` for v2) |

**Forbidden** in public-governed GBA metadata:

- `care:sensitivity = "restricted"`  
- Exact sacred/ceremonial geographies, even in descriptions.  
- Inclusion of sensitive oral histories without explicit approval.

CARE fields must be consistent with:

- STAC CARE fields (`../stac/great-bend-aspect-v2.json`).  
- CARE fields in the provenance log.

---

## 🌍 Spatial Metadata Requirements

Spatial metadata in `great-bend-aspect-v2.json` must reflect:

- Geometry type: generalized **MultiPolygon** (as per STAC).  
- CRS: **EPSG:4326** for all coordinates referenced in STAC and internal notes.  
- Generalization:
  - Use H3 mosaics and polygon simplification at a scale that prevents inference of protected sites.  
  - Avoid site-level or feature-level locational hints in the description.

Bounding boxes used in DCAT and STAC are:

- Derived from generalized geometries.  
- Coarse enough to respect CARE and sovereignty policies.

---

## 🕰 Temporal Metadata Requirements

Temporal coverage must:

- Match the interaction-sphere span (approximately AD 1350–1700).  
- Use OWL-Time-consistent forms (intervals) in STAC and DCAT.  
- Align with KFM’s cultural-phase ontology for GBA and related phases.

Metadata may optionally:

- Break coverage into Early/Middle/Late GBA phases in `kfm:culture_phase`.  
- Indicate uncertainty margins in descriptive fields or an optional uncertainty block.

---

## 🧪 Provenance Linkage

The metadata must link directly to the PROV-O log:

- `kfm:provenance: "../provenance/great-bend-aspect-v2.json"`

The referenced provenance file must:

- Describe raw → generalized → processed lineage.  
- Document generalization (H3, simplification thresholds).  
- Record FAIR+CARE review steps and any tribal advisory input.  

Provenance is validated via the schemas and workflows described in:

- `../provenance/README.md`  
- `../../provenance/README.md`

---

## ⚖️ Ethical Governance & Cultural Context

All Great Bend Aspect metadata must:

- Avoid colonial or overly deterministic language.  
- Emphasize interpretive uncertainty, especially for protohistoric components.  
- Make no territorial claims or exclusive ownership assertions.  
- Recognize descendant communities’ ties to the landscape while respecting sovereignty policies.  
- Respect GBA as an interpretive model rather than fixed political boundaries.

---

## 🧠 Integration Into KFM Ecosystem

Metadata generated according to this standard drives:

### Knowledge Graph

**Nodes**

- `InteractionSphere` (Great Bend Aspect).  
- `MetadataRecord` for GBA.  
- `CulturalPhase` (`GBA-Early`, `GBA-Middle`, `GBA-Late`).  
- CARE-related nodes (for sensitivity states).

**Relationships**

- `HAS_METADATA` (InteractionSphere → MetadataRecord).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE node).  
- `HAS_PROVENANCE` (InteractionSphere → ProvenanceRecord via `kfm:provenance`).  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase/TimeInterval).  

### Story Nodes & Focus Mode v3

- Provide dataset-level context, titles, and descriptions.  
- Drive sensitivity badges, narrative framing, and timeline placement.  
- Attach provenance chips and warnings when necessary.

---

## 📊 Metadata Summary (Illustrative)

| Field              | Value                                          |
|--------------------|------------------------------------------------|
| Title              | Great Bend Aspect Interaction Sphere v2       |
| Sensitivity        | generalized                                   |
| CARE Review        | FAIR+CARE (tribal advisory consultation recommended) |
| Culture Phases     | GBA-Early / GBA-Middle / GBA-Late             |
| Spatial Generalization | H3-r7 (public-governed representation)    |
| Provenance Linked  | Yes (`../provenance/great-bend-aspect-v2.json`) |
| Status             | 🟢 Active / Governed                          |

Authoritative values are recorded in metadata, provenance, and release manifests.

---

## 🔗 Related Specifications

- `../README.md`  
  – Great Bend Aspect interaction-sphere dataset overview and governance.  
- `../stac/README.md`  
  – Great Bend Aspect STAC catalog (Collection + Item).  
- `../provenance/README.md`  
  – Great Bend Aspect provenance index and standards.  
- `../../metadata/README.md`  
  – Global interaction-sphere metadata standards.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Updated for KFM v11.2.3; aligned with interaction-sphere metadata standards; added telemetry references and clarified CARE semantics. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial Great Bend Aspect metadata specification; defined DCAT/KFM/CARE fields and generalization guidelines. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Prototype metadata content and directory structure.                     |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Great Bend Aspect Dataset](../README.md)
