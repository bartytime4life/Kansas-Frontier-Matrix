---
title: "📥 Kansas Frontier Matrix: Late Prehistoric H3 Input Dataset Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-provenance-inputs-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-provenance-inputs"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Input Data / Lineage"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-provenance-inputs.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-provenance-inputs-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:late-prehistoric-h3-inputs-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-inputs"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-lineage"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-results-late-prehistoric-h3-provenance-inputs"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next provenance-input update"
---

<div align="center">

# 📥 **Kansas Frontier Matrix — Late Prehistoric H3 Provenance Inputs**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/README.md`

**Purpose:**  
Document all **input datasets** used to generate Late Prehistoric H3 generalized clusters, including  
generalized archaeological points, environmental layers, hydrology datasets, and model inputs.  
These inputs serve as the **root of the PROV-O lineage chain** and are essential for reproducibility,  
CARE governance, and ethical heritage protection.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

The H3 generalization pipeline requires multiple inputs that are:

- **Generalized to protect sensitive archaeological sites**  
- **Reviewed by tribal partners and CARE governance**  
- **Fully documented under PROV-O and STAC/DCAT metadata**  
- **Versioned and reproducible** under WAL → Retry → Rollback controls  

This registry describes *only* inputs permitted for public or semi-public processing—  
all unreleased/sensitive raw materials are stored under secure governance controls.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/
├── README.md                         # This file
├── archaeological_generalized.geojson # Generalized archaeological points (H3-safe)
├── environmental_rasters/            # Climate, soils, vegetation surfaces
├── hydrology/                        # River networks, watersheds, alluvial boundaries
├── terrain/                          # DEMs, slope/aspect surfaces (generalized)
├── predictive_inputs/                # Model feature layers used in KDE/predictive modeling
├── cultural_landscapes/              # Interaction zones, territory approximations
└── metadata/                         # Input-level STAC/DCAT metadata
````

---

## 🧬 Input Dataset Categories

### 1️⃣ Archaeological Inputs (Generalized)

**File:** `archaeological_generalized.geojson`
**Contains:**

* H3-jittered or masked archaeological site points
* Tribal-approved generalization levels (r7+, or >5 km buffers)
* Generalized temporal attributes (occupation bands only)

**CARE Notes:**

* No precise site data is stored here
* Masking practices logged in `care_review.md`
* Provenance: `prov:Entity` + `care:sensitivity="generalized"`

---

### 2️⃣ Hydrology Inputs

Includes:

* **Major rivers and tributaries** (generalized)
* **Paleochannels** (where applicable)
* **Watershed boundaries**
* **Floodplain generalizations**

Used for:

* corridor modeling
* environmental affordance assessment
* Late Prehistoric movement analysis

Generalized to protect culturally sensitive waterway associations.

---

### 3️⃣ Environmental Inputs

Located in: `environmental_rasters/`

* Climate reconstructions (temp/precip)
* Drought indices (PDSI)
* Vegetation & landcover (historic & modern)
* Soils (drainage, fertility, texture classes)

All rasters must:

* be resampled for privacy protection
* include STAC lineage metadata
* follow uncertainty propagation rules

---

### 4️⃣ Terrain Inputs

Located in: `terrain/`

Includes:

* DEM-derived slope
* Aspect
* Relative relief
* Terrain ruggedness

Used in predictive modeling and H3 smoothing phases.

---

### 5️⃣ Predictive Model Inputs

Located in: `predictive_inputs/`

Examples:

* Environmental suitability surfaces
* KDE-derived intensity rasters
* Training + test splits (generalized)
* Predictor composites

All must include:

* `prov:used`
* `kfm:model_parameters`
* Reproducibility configs (seed, config hash)

---

### 6️⃣ Cultural Landscape Inputs

Located in: `cultural_landscapes/`

Includes:

* Interaction spheres (Great Bend, Wichita, Plains Village)
* Trade corridors (generalized)
* Cultural influence regions

CARE rules strictly govern:

* precision
* boundaries
* allowed descriptive language

---

## 🧭 Metadata Requirements (STAC/DCAT)

Each input dataset must include:

* **STAC Item** with:

  * `kfm:domain = archaeology`
  * `care:sensitivity = generalized`
  * `prov:wasGeneratedBy` entry referencing generalization activities

* **DCAT Dataset** with:

  * `dct:title`, `dct:description`, `dcat:theme`, `dcat:distribution`
  * Spatial + temporal extents
  * CARE notes

Metadata files placed in:

```
inputs/metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 surfaces:

* input-to-output lineage chips
* provenance relationships (`prov:used`)
* CARE-linked data constraints
* context notes for environmental + cultural inputs

Example Focus Note:

> **Focus Summary:**
> Late Prehistoric H3 layers were generated from generalized archaeological points and
> environmental surfaces reviewed under CARE governance.
> All sensitive landscapes were masked or aggregated before modeling.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                             |
| ------: | ---------- | ---------------------------------- | ------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial provenance input registry for Late Prehistoric H3 clusters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Input Dataset Registry · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Provenance](../README.md) · [Back to Activity Records](../activity_records/README.md)

</div>
