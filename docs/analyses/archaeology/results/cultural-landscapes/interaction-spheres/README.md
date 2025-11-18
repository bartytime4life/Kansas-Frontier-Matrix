---
title: "🌀🌾 Kansas Frontier Matrix — Cultural Landscapes: Interaction Sphere Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/interaction-spheres/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Cultural Landscape WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-interaction-spheres-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-cultural-landscape-interaction-spheres"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Generalized Cultural Landscape"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Cultural Landscape Interpretation"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/interaction-spheres/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Place"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscape-interaction-spheres.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscape-interaction-spheres-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:interaction-spheres-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-interaction-spheres"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/interaction-spheres/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "environmental-context-linking"
ai_transform_prohibited:
  - "cultural-identity-inference"
  - "exact-boundary-drawing"
  - "restricted-landscape-reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-interaction-spheres-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next interaction-sphere synthesis"
---

<div align="center">

# 🌀🌾 **Cultural Landscapes — Interaction Sphere Results**  
`docs/analyses/archaeology/results/cultural-landscapes/interaction-spheres/README.md`

**Purpose:**  
Document KFM’s **generalized environmental and landscape-based interaction sphere results**, representing broad-scale zones of shared environmental affordances, movement tendencies, ecological similarities, and non-specific cultural interactions across phases of Kansas prehistory and history.  
These interaction spheres are *not cultural territories*, *not social/tribal identifications*, and *not historical claims*—they are **environmentally derived, CARE-governed generalizations**.

</div>

---

## 📘 Overview

Interaction spheres in the KFM represent **landscape-scale environmental and mobility-based relationships** among archaeological datasets, including:

- broad similarity regions  
- shared ecological affordances  
- hydrology-linked movement zones  
- generalized activity regions  
- multi-period environmental corridors  
- coarse-scale clustering tendencies  
- cross-domain overlays (climate, soils, vegetation, hydrology)  

These outputs are:

- **H3 r7+ generalized**  
- **non-attributional** (no cultural identity statements)  
- **environmentally grounded**  
- **supported by uncertainty layers**  
- **filtered via FAIR+CARE governance**  
- **validated by PROV-O lineage**  

Interaction spheres **do NOT** define cultural boundaries, territories, or restricted landscapes.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/interaction-spheres/
├── README.md                                   # This file
├── late-prehistoric/                           # Late Prehistoric environmental interaction spheres
├── protohistoric/                              # Protohistoric generalized spheres
├── multi-period/                               # Cross-period comparative spheres
├── hydrology-linked/                            # Hydrology-based interaction regions
├── environmental-affordances/                   # Environmental drivers for sphere formation
├── uncertainty/                                 # Uncertainty & proxy disagreement layers
├── stac/                                        # STAC Items for interaction sphere datasets
├── metadata/                                    # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage documenting source datasets & methods
~~~

---

## 🌀 Interaction Sphere Categories

### **1️⃣ Late Prehistoric Interaction Spheres (`late-prehistoric/`)**
Represent:

- environmentally similar zones  
- stable hydrology + terrain patterns  
- ecological affordance clusters  
- generalized settlement–landscape alignments  

---

### **2️⃣ Protohistoric Interaction Spheres (`protohistoric/`)**
Generalized representations of:

- environmental co-use regions  
- movement corridors  
- hydrology-climate linked zones  
- shifting eco-hydrological patterns  

---

### **3️⃣ Multi-Period Comparative Spheres (`multi-period/`)**
Describe:

- areas of long-term ecological similarity  
- persistent movement affordance zones  
- multi-era stability of environmental drivers  

No cultural continuity or identity is inferred.

---

### **4️⃣ Hydrology-Linked Interaction Spheres (`hydrology-linked/`)**
Capture:

- river/terrace/stream system influences  
- floodplain stability regions  
- water-access affordances across time  
- hydrology & cluster interaction patterns  

---

### **5️⃣ Environmental-Affordance Spheres (`environmental-affordances/`)**
Document:

- soil + vegetation + hydrology composite areas  
- ecozone interactions  
- climate-linked landscape potentials  
- terrain mobility affordances  

These are environmental patterns, not cultural territories.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Interaction sphere STAC Items must include:

- H3 geometry only  
- spatial generalization documentation  
- uncertainty layers  
- environmental driver metadata  
- CARE classification & access-level metadata  
- lineage references  

### **DCAT (`metadata/`)**
Documents:

- dataset purpose  
- environmental drivers  
- FAIR+CARE governance  
- distribution metadata  
- sensitivity classifications  

### **PROV-O (`provenance/`)**
Tracks:

- datasets used (climate, hydrology, soils, vegetation, settlement generalizations)  
- model transformations (KDE, H3, ML/GAM)  
- generalization/masking stages  
- uncertainty propagation  
- narrative safety checks  

All provenance must pass CI validation before results enter the KFM system.

---

## 🧠 Focus Mode Integration

Interaction spheres help Focus Mode v3:

- contextualize environmental relationships  
- explain broad landscape-use tendencies  
- enhance Story Node landscape summaries  
- provide environmentally grounded multi-period insights  
- display uncertainty and driver weights  

Example Focus Summary:

> **Focus Summary:**  
> Interaction spheres identify broad regions shaped by stable hydrology, soils, vegetation, and terrain. These generalized zones reflect environmental patterns, not cultural territories, and have been CARE-reviewed for cultural safety.

---

## ⚠️ CARE & Ethical Requirements

All sphere outputs must:

- avoid mapping or implying tribal or cultural boundaries  
- avoid describing sacred or restricted landscapes  
- avoid identity inference  
- apply H3 r7+ generalization  
- disclose uncertainty  
- undergo FAIR+CARE Council review  
- reflect only environmental affordances  

If any sphere approaches cultural sensitivity → it must be masked, generalized further, or excluded.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Cultural Landscape WG · FAIR+CARE Council | Initial registry for generalized interaction sphere results. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Interaction Sphere Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>