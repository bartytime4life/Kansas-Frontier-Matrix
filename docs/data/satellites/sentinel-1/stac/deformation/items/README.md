---
title: "🌍 Sentinel-1 Deformation — Scene-Level STAC Items (InSAR LOS Displacement · Subsidence · Uplift)"
path: "docs/data/satellites/sentinel-1/stac/deformation/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR-Derived Product)"
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
care_label: "CARE-B (Generalized InSAR Product)"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-deformation-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-deformation-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-deformation-items-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-deformation-items"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/deformation/items/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA InSAR reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR Deformation STAC Items**  
`docs/data/satellites/sentinel-1/stac/deformation/items/`

Sovereignty-generalized scene-level InSAR displacement products:  
**LOS displacement · subsidence · uplift · seasonal movement**,  
governed under strict CARE-B + sovereignty masking rules.

</div>

---

## 📘 1. Overview

These STAC Items represent **InSAR-derived ground motion** from Sentinel-1 SAR:

- ✨ **LOS (Line-of-Sight) displacement**
- 📉 **subsidence**
- 📈 **uplift**
- 🔁 **seasonal deformation cycles**
- 🌀 **coherence-supported deformation QA**

Because displacement patterns can reveal sensitive details  
(infrastructure, cultural landscapes, ecological zones, hydrological systems),  
**these Items undergo mandatory sovereignty generalization**.

Every Item is:

- STAC 1.x compliant  
- JSON-LD enriched  
- DCAT compatible  
- PROV-O lineage complete  
- FAIR+CARE + sovereignty enforced  
- validated in CI  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/deformation/items/
├── 📄 README.md
│
├── 🌍 S1A_IW_INSAR_20250101_20250113.json
├── 🌍 S1B_IW_INSAR_20250315_20250327.json
└── …                                          # Many sovereign-generalized deformation Items
~~~

---

## 🧩 3. Item Structure

### 🌐 Core STAC Properties
- `datetime` (mid-pair or TS epoch)  
- `"sar:product_type" = "INSAR"`  
- `"insar:pair"` or `"insar:timeseries"` metadata  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `proj:*` CRS, transform, shape  
- orbit metadata (cycle, orbit_state, relative orbit)

### 🗺 Geometry (Always Generalized)
- footprint polygon  
- sovereignty-generalized shapes using H3  
- bbox consistent with generalized geometries  
- `"kfm:mask_required" = true` when intersecting sovereign areas  

### 📦 Assets
- `"los_displacement"` → displacement COG (generalized)  
- `"coherence"` → optional coherence supporting tile  
- `"qa"` → unwrapping/ambiguity QA  
- `"thumbnail"` → PNG  
- `"metadata"` → SAFE metadata  

### 🔗 Link Graph
- `"self"`  
- `"collection"` → deformation Collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC / GRD / GRDH sources  

### 🧬 PROV-O Lineage
- `prov:wasGeneratedBy` → InSAR pipeline  
- `prov:used` → DEMs, orbit files, coherence, LUTs  
- `prov:wasDerivedFrom` → ESA scenes  
- includes energy & carbon metadata for sustainability accounting  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

All Items **must** include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

These ensure:

- **no exposure of precise deformation values** in sovereign areas  
- **mandatory generalization** of magnitude & geometry  
- protection against inference of sensitive cultural or ecological conditions  

Governance validated via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`

---

## 🧪 5. CI Validation Requirements

To pass CI, deformation Items must satisfy:

- STAC schema compliance  
- SAR + InSAR extension validation  
- geometry ↔ bbox integrity  
- sovereign H3 generalization checks  
- `"kfm:*"` governance field completeness  
- PROV-O lineage structure  
- DCAT metadata compatibility  
- correct asset roles & media types  

Any violation → **release blocked**.

---

## 🔁 6. InSAR Processing in the ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → coherence pair assembly
 → interferogram formation
 → phase unwrapping
 → LOS conversion
 → sovereignty generalization (mandatory)
 → deformation QA
 → STAC Item generation (this directory)
 → deformation Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- sovereign-safe subsidence & uplift monitoring  
- cultural-landscape hazard analysis  
- hydrological + ecological coupling  
- Story Node v3 environmental context  
- Focus Mode v3 sovereign-safe reasoning  
- long-term deformation trend analysis (generalized)  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                              |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 InSAR deformation Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.         |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Deformation Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

