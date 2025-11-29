---
title: "🌿 Sentinel-1 Wetlands — Scene-Level STAC Items (SAR Wetness · Inundation · Riparian Dynamics)"
path: "docs/data/satellites/sentinel-1/stac/wetlands/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0 (ESA Open Data)"
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
care_label: "CARE-B (Wetland / Inundation Derivatives)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-wetlands-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-wetlands-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-wetlands-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-wetlands-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/wetlands/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA wetlands reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **Sentinel-1 Wetlands STAC Items**  
`docs/data/satellites/sentinel-1/stac/wetlands/items/`

Scene-level STAC Items representing  
**wetland, saturation, shallow inundation, and riparian wetness states**  
derived from Sentinel-1 SAR (RTC γ⁰, coherence, VH/VV ratios).

</div>

---

## 📘 1. Overview

Wetland STAC Items represent Sentinel-1 SAR–derived environmental indicators, including:

- shallow inundation  
- saturated soils  
- riparian wetness  
- ephemeral pooling  
- seasonal wetland expansion  
- vegetation–water interaction signatures  

These layers are **governance-sensitive**, often intersecting:

- tribal waterways  
- ecologically sensitive zones  
- cultural landscapes  
- sovereignty-protected hydroscapes  

Thus **generalization is mandatory** under KFM sovereignty rules.

All Items are:

- STAC 1.x valid  
- JSON-LD enriched  
- DCAT compatible  
- PROV-O lineage complete  
- sovereignty-safe  
- FAIR+CARE compliant  
- CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/wetlands/items/
├── 📄 README.md
│
├── 🌿 S1A_IW_WET_20250411T120010.json     # Example scene-level wetland indicator
├── 🌿 S1B_IW_WET_20250318T223045.json     # Additional wetland Items
└── …                                       # More sovereign-generalized Items
~~~

---

## 🧩 3. Wetland Item Structure

### 🌐 Core Metadata  
- `datetime`  
- `"sar:product_type" = "WETLAND"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `proj:*` CRS + transformation metadata  
- ESA orbit metadata (cycle, relative orbit, orbit_state)

### 🗺 Geometry (Sovereignty-Generalized)  
- polygon footprint  
- bbox  
- H3-generalized geometry inside sovereign zones  
- `"kfm:mask_required"` always evaluated  

### 📦 Assets  
- `"wetland_mask"` → COG  
- `"wetland_prob"` (optional)  
- `"qa"` → uncertainty/ambiguity QA  
- `"coherence"` (optional supporting signal)  
- `"thumbnail"` → PNG  
- `"metadata"` → ESA SAFE ancillary metadata  

### 🔗 Link Graph  
- `"self"`  
- `"collection"` → wetland Collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC/GRD/GRDH/Coherence items  

### 🧬 PROV-O Lineage  
- `prov:wasGeneratedBy` → wetlands pipeline  
- `prov:used` → RTC γ⁰, coherence, DEM, LUTs  
- `prov:wasDerivedFrom` → ESA source scenes  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Wetlands can reveal:

- hydrological behavior of sovereign lands  
- ecologically vulnerable areas  
- culturally significant water/land transitions  

Therefore Items **must** include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Governance validated through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

Wetland Items must pass:

- STAC schema validation  
- SAR/Wetlands extension validation  
- geometry ↔ bbox integrity checks  
- governance field completeness  
- sovereignty generalization rules  
- PROV-O lineage shape  
- DCAT metadata compatibility  
- correct media type roles (COG, PNG, JSON)  

Any violation → **Item blocked from governed release**.

---

## 🔁 6. Wetlands in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → RTC gamma0 generation
 → coherence fusion (optional)
 → wetland classifier (SAR + coherence + seasonal models)
 → sovereignty masking (mandatory)
 → wetland QA
 → STAC Item generation (this directory)
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- hydrology modeling  
- ecological landscape transitions  
- riparian habitat monitoring  
- seasonal wetland analyses  
- Story Node v3 environmental narratives  
- Focus Mode v3 sovereign-safe environmental reasoning  
- climate & drought interactions  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                           |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 Wetlands Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Wetland Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

