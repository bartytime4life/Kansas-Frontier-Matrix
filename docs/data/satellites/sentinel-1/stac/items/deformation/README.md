---
title: "🌍 Sentinel-1 Deformation (InSAR LOS) — Sovereignty-Generalized STAC Items (Subsidence · Uplift · Ground Motion)"
path: "docs/data/satellites/sentinel-1/stac/items/deformation/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governance Required)"
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
care_label: "CARE-B (Generalized InSAR Displacement)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-deformation-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-deformation-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-deformation:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-deformation"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/deformation/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA InSAR processing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR Deformation — Sovereignty-Generalized STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/deformation/`

**Line-of-Sight (LOS) displacement** from Sentinel-1 InSAR:  
subsidence · uplift · seasonal ground motion · infrastructure deformation.  
All Items are **sovereignty-generalized** to prevent sensitive geographic inference.

</div>

---

## 📘 1. Overview

Sentinel-1 **InSAR Deformation STAC Items** store LOS displacement products derived from  
pairwise or time-series interferometry.  
These are among the **most sensitive** SAR-derived layers due to:

- infrastructure visibility  
- ground-motion correlation with cultural landscapes  
- potential inference of sensitive ecological or archaeological zones  

Therefore **sovereignty generalization is mandatory** for all deformation Items.

Each Item is:

- STAC 1.x valid  
- extends SAR + InSAR extension fields  
- includes generalized geometry for sovereign/tribal H3 cells  
- embeds FAIR+CARE governance metadata  
- carries PROV-O lineage  
- is DCAT compatible  
- is CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Aligned Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/deformation/
├── 📄 README.md
│
├── 🌍 S1A_IW_INSAR_20250101T115932_20250113T115933.json     # Example LOS deformation tile (synthetic ID)
├── 🌍 S1B_IW_INSAR_20250315T004012_20250327T004014.json     # Additional deformation Items
└── …                                                        # More sovereign-generalized InSAR Items
~~~

---

## 🧩 3. Deformation Item Components

### 🌐 Core STAC Fields
- `datetime` (mid-time of interferometric pair or time-series segment)  
- `"insar:pair"` → `[t1, t2]` or time-series metadata  
- `"sar:product_type" = "INSAR"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- `proj:*` CRS fields  
- orbit metadata (`orbit_state`, `relative_orbit`, `cycle_number`)  

### 🗺 Geometry (Sovereignty-Generalized)
- footprint polygon  
- H3-generalized geometry inside tribal/sovereign extents  
- `"kfm:mask_required"` always considered  
- bbox consistent with generalized geometry  

### 📦 Assets
- `"los_displacement"` — LOS displacement COG (generalized)  
- `"coherence"` — supporting coherence COG  
- `"metadata"` — ESA SAFE metadata  
- `"thumbnail"` — PNG preview  
- `"qa"` — displacement QA mask  

### 🔗 Link Structure
- `"self"`  
- `"collection"` → deformation collection  
- `"parent"`  
- `"root"`  
- `"derived_from"` → RTC or GRD/GRDH Items  
- `"insar:coherence_master"` / `"insar:coherence_slave"`  

### 🧬 PROV-O Lineage
- `prov:wasGeneratedBy` → InSAR processing pipeline  
- `prov:used` → DEM, orbit files, coherence tiles, calibration LUTs  
- `prov:wasDerivedFrom` → GRD/GRDH scenes  

---

## 🔐 4. Governance & Sovereignty Enforcement (Critical)

Deformation is extremely sensitive.  
KFM v11 sovereignty engine enforces:

- `"kfm:h3_sensitive"` on **all** deformation Items  
- `"kfm:mask_required"` (almost always true)  
- generalized LOS displacement (reduced precision)  
- `"kfm:sovereignty_uncertainty_floor"` (displacement must not suggest precision)  
- `"kfm:care_label"` = CARE-B  
- `"kfm:care_label_reason"` explaining restriction  
- `"kfm:governance_notes"` documenting masking/generalization actions  

Validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Behavior

CI checks:

- STAC schema compliance  
- InSAR extension compliance (`insar:*`, `sar:*`)  
- geometry generalization rules  
- asset roles and types  
- PROV-O lineage completeness  
- sovereignty metadata presence  
- DCAT alignment  
- QA mask alignment  

Any violation → **Item blocked**.

---

## 🔁 6. Deformation in the SAR ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → coherence generation
 → interferogram formation
 → phase unwrapping
 → LOS conversion
 → sovereignty generalization
 → displacement QA
 → STAC Item generation (this directory)
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- subsidence & uplift monitoring  
- infrastructure stability (generalized)  
- cultural-landscape hazard awareness  
- ecological transition analysis  
- Focus Mode v3 displacement-safe narratives  
- Story Node v3 sovereign-safe environmental context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                            |
|--------:|------------|--------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 deformation STAC Items README; sovereignty-generalized; FAIR+CARE/H3 aligned; CI-safe; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🌐 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

