---
title: "⚒️🥇 Kansas Frontier Matrix — Artifact Results: Metals (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/metals/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Metallurgical Analysis WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-metals-results-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Artifact Analysis Results"
intent: "archaeology-artifacts-metals-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Public-Domain Metals Only"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Metallurgical Specialists · FAIR+CARE Council"
risk_category: "Material Culture (Metallurgical)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/metals/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E22 Man-Made Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-metals-results.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-metals-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:metals-results-v11.0.0"
semantic_document_id: "kfm-arch-artifact-metals-results"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/metals/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "material-description"
ai_transform_prohibited:
  - "cultural-identity-inference"
  - "origin-reconstruction"
  - "restricted-metal-source-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-metals-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next metals-results update"
---

<div align="center">

# ⚒️🥇 **Metal Artifact Results**  
`docs/analyses/archaeology/results/artifacts/metals/README.md`

**Purpose:**  
Provide a FAIR+CARE–aligned registry of **metal artifact analytical results** incorporated into the Kansas Frontier Matrix (KFM).  
These include **public-domain and culturally safe** metallurgical summaries, elemental composition datasets, alloy classifications, and generalized distribution tendencies.  
All results exclude culturally sensitive items, colonial/restricted metal contexts, and provenience-level details.

</div>

---

## 📘 Overview

Metals results in KFM synthesize:

- elemental composition (XRF, ICP-MS; PD-only)  
- alloy categories (copper alloys, iron objects, trade metals—public domain only)  
- manufacturing/technological markers (hammering, annealing, casting indicators)  
- corrosion/stability groupings (environmental, not cultural)  
- H3 r7+ generalized spatial distribution tendencies  
- environmental correlations (hydrology, terrain, soils)  
- multi-factor cluster summaries  
- uncertainty + explainability layers  

Excluded:

- restricted or sacred metal objects  
- funerary-associated metals  
- colonial-conflict materials requiring sensitivity  
- exact trade-route inference  
- culturally sensitive metallurgical traditions  

All records undergo FAIR+CARE review and PROV-O lineage validation.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/metals/
├── README.md                                   # This file
├── composition/                                # Elemental composition (generalized)
├── alloys/                                     # Alloy categories & public-safe summaries
├── manufacturing/                              # Manufacturing indicators (hammering, annealing)
├── distribution/                               # H3 generalized metal-artifact distribution surfaces
├── environmental-links/                        # Hydrology/soil/terrain correlations
├── temporal/                                   # OWL-Time aligned metal-use tendencies
├── uncertainty/                                # Uncertainty, variance & proxy disagreement
├── stac/                                       # STAC Items for metal result layers
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage & workflow logs
~~~

---

## 🧪 Metal Result Types

### **1️⃣ Elemental Composition (`composition/`)**
Includes:

- XRF/ICP-MS PD-safe elemental spectra  
- compositional cluster summaries  
- PCA of alloying elements  
- corrosion-related chemical signatures  

Never tied to restricted metal sources.

---

### **2️⃣ Alloy Categories (`alloys/`)**
Generalized alloy groupings (public domain):

- copper-based alloys  
- iron-based materials  
- brass/bronze categories  
- lead/tin admixtures (PD-only)

No restricted or sensitive metallurgical traditions included.

---

### **3️⃣ Manufacturing Indicators (`manufacturing/`)**
Contains:

- hammering/annealing evidence  
- casting indicators  
- surface microstructure summaries  

All descriptions remain technological—not cultural.

---

### **4️⃣ Distribution Patterns (`distribution/`)**
Provide:

- H3 generalized density surfaces  
- KDE smoothing  
- environmentally correlated metal-distribution zones  

No exact provenience or sensitive cluster shapes.

---

### **5️⃣ Environmental Correlations (`environmental-links/`)**
Evaluate:

- hydrology-linked metal distribution  
- soil chemistry & corrosion relationships  
- terrain-linked environmental affordances  
- paleoenvironment interactions  

Environmental-only interpretations.

---

### **6️⃣ Temporal Metal Patterns (`temporal/`)**
OWL-Time aligned summaries of:

- generalized metal-use intervals  
- environmental-coincident tendencies  
- cross-period distribution shifts  

Never used to propose cultural chronology.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Track:

- analytical variance  
- instrument uncertainty  
- material classification disagreement  
- distributional model variance  

Shown in Focus Mode as **Metal Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**
Metal-artifact STAC Items must include:

- H3 geometry  
- composition/alloy metadata  
- uncertainty layers  
- environmental driver metadata  
- lineage bundle links  

### **DCAT (`metadata/`)**
Contains:

- dataset purpose  
- access/licensing  
- CARE-informed sensitivity notes  
- public-domain verification  

### **PROV-O (`provenance/`)**
Tracks:

- datasets & instruments used  
- transformation methods  
- alloy assignment rules  
- generalization steps  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Metals results power:

- Story Node v3 material-culture context blocks  
- safe, generalized narrative explanations  
- environmental correlation insights  
- multi-material comparison overlays  

Example Focus Summary:

> **Focus Summary:**  
> Metal analyses show generalized alloy groups and distribution patterns linked to environmental factors. All data are public-domain, fully generalized, and reviewed under FAIR+CARE safeguards.

---

## 🛡 CARE & Ethical Requirements

Metal datasets must:

- exclude culturally restricted materials  
- avoid identity or group attribution  
- avoid reconstructing metallurgical traditions  
- apply H3 r7+ masking  
- disclose uncertainty transparently  
- undergo FAIR+CARE review before release  

If cultural sensitivity arises → dataset must be masked or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                  | Summary |
|--------:|------------|-----------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Metallurgical Specialists · FAIR+CARE Council | Initial metal artifact results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Metal Artifact Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>
