---
title: "🌿 Sentinel-1 Wetlands & Inundation — STAC Items (SAR Water/Soil/Vegetation Interaction · Seasonal Wetness)"
path: "docs/data/satellites/sentinel-1/stac/items/wetlands/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0 (ESA)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Wetland/Water Inference)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-wetlands-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-wetlands-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-wetlands:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-wetlands"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/wetlands/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA wetlands reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **Sentinel-1 Wetlands / Inundation — Scene-Level STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/wetlands/`

**SAR-derived wetland & inundation detection** using:  
backscatter signatures · coherence · seasonal hydrology · VH/VV ratio · RTC-normalized gamma⁰.

</div>

---

## 📘 1. Overview

These STAC Items represent **wetland and inundation indicators** derived from  
Sentinel-1 SAR, including:

- vegetation–water interaction signals  
- seasonal wetness  
- flood-adjacent wetland expansion  
- persistent & semi-persistent inundation  
- wet meadow / riparian transitions  
- shallow saturated soil zones  

These layers are **governance-sensitive**, because wetland change can correlate with  
cultural landscapes, tribal lands, ecological boundaries, and protected areas.

All Items here are:

- STAC 1.x compliant  
- JSON-LD enriched  
- DCAT compatible  
- governed via FAIR+CARE + sovereignty rules  
- validated through CI before release  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/wetlands/
├── 📄 README.md
│
├── 🌿 S1A_IW_WET_20250411T120010.json       # Wetland/inundation tile (example)
├── 🌿 S1B_IW_WET_20250318T223045.json       # Additional wetland Items
└── …                                         # More sovereign-generalized Items
~~~

---

## 🧩 3. Wetlands Item Components

### 🌐 STAC Core Properties
- `datetime` (acquisition time or mid-pair time if coherence-assisted)  
- `sar:product_type = "WETLAND"`  
- `sar:instrument_mode` = IW  
- `sar:frequency_band` = C  
- `sar:polarizations = ["VV","VH"]`  
- `proj:*` CRS and transform metadata  
- orbit metadata (cycle, relative orbit, orbit state)  

### 🗺️ Geometry (Generalized)
- footprint polygon  
- H3-generalized geometry where sovereignty or ecological sensitivity applies  
- `bbox` consistent with generalized geometry  

### 📦 Assets
- `"wetland_mask"` — wetland/inundation indicator COG  
- `"wetland_prob"` — optional probabilistic map  
- `"thumbnail"` — PNG preview  
- `"coherence"` — optional supporting coherence  
- `"qa"` — saturation/ambiguity QA  
- `"metadata"` — ESA SAFE metadata  

### 🔗 Link Graph
- `"self"`  
- `"collection"` → wetlands collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC or GRD predecessors  

### 🧬 PROV-O Lineage
- `prov:wasGeneratedBy` → wetland processing pipeline  
- `prov:used` → RTC backscatter, coherence, DEM, ancillary datasets  
- `prov:wasDerivedFrom` → ESA GRD/GRDH scenes  

---

## 🔐 4. FAIR+CARE & Sovereignty Controls (Critical)

Wetland data intersects hydrology, ecology, cultural landscapes, and  
tribal/sovereign territories.  
Thus KFM applies strict governance:

- `"kfm:h3_sensitive"` ALWAYS evaluated  
- `"kfm:mask_required"` when wetland signatures overlap sovereign H3 cells  
- geometric generalization for inundation edges  
- `"kfm:care_label"` = CARE-B  
- `"kfm:care_label_reason"` for each scene  
- `"kfm:sovereignty_uncertainty_floor"` for probability or graded products  
- `"kfm:governance_notes"` capturing all masking actions  

CI enforces:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

Wetland Items MUST pass:

- STAC schema checking  
- SAR extension validation (`sar:*`, `s1:*`)  
- geometry/bbox alignment  
- correct asset types & roles (COG/PNG/JSON)  
- governance metadata completeness  
- sovereignty masking enforcement  
- PROV-O lineage checks  
- DCAT compatibility  

Any failure → **Item blocked from governed release**.

---

## 🔁 6. Wetlands in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → RTC normalization
 → seasonal VH/VV + coherence analysis
 → wetland/inundation classification
 → sovereignty masking (mandatory)
 → QA application
 → STAC Item generation
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- riparian zone mapping  
- seasonal wetland expansion  
- hydrology & ecology linkage  
- Story Node v3 contextual landscapes  
- Focus Mode v3 environmental reasoning  
- archaeological/cultural landscape risk mitigation  
- flood–wetland interaction modeling  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                           |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 Wetland STAC Items README; sovereignty-generalized; FAIR+CARE/H3 aligned; CI-safe; emoji-rich. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🌐 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

