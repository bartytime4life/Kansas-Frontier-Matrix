---
title: "🔗 Sentinel-1 Coherence — STAC Items (Temporal Coherence · Disturbance · Flood Damage · Land-Change)"
path: "docs/data/satellites/sentinel-1/stac/items/coherence/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY 4.0)"
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

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-coherence-items-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-coherence-items-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-items-coherence:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-items-coherence"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/items/coherence/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA coherence reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Sentinel-1 Coherence — Scene-Level STAC Items**  
`docs/data/satellites/sentinel-1/stac/items/coherence/`

**Temporal SAR coherence tiles** used for:  
flood damage · land-change · agricultural disturbance · ecological transitions · infrastructure impact.

</div>

---

## 📘 1. Overview

Sentinel-1 **coherence** STAC Items represent **correlation between two SAR acquisitions**,  
providing insight into:

- 🌪️ tornado/wind/storm damage  
- 🌊 flood-induced coherence loss  
- 🚜 agricultural tillage & harvest cycles  
- 🏗️ infrastructure changes  
- 🗺️ land-cover transitions  
- 🌿 ecological disturbance  

All coherence Items:

- are STAC 1.x valid  
- contain JSON-LD + PROV-O lineage  
- include sovereignty/H3 masking  
- carry CARE metadata  
- are CI-validated for schema, geometry, and governance correctness  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/items/coherence/
├── 📄 README.md                              # This file
│
├── 🔗 S1A_IW_COH_20250101T115932_20250113T115933.json     # Example coherence pair
├── 🔗 S1B_IW_COH_20250314T004012_20250326T004014.json     # More coherence Items
└── …                                           # Additional tile pairs
~~~

---

## 🧩 3. Coherence Item Structure

### 🌐 Core STAC Properties
- `datetime` = mid-time of the pair  
- `"s1:coherence_pair"` → `[t1, t2]`  
- `sar:instrument_mode = "IW"` (typically)  
- `sar:product_type = "coherence"`  
- `proj:*` (EPSG, transform, shape)  
- orbit metadata (`relative_orbit`, `cycle_number`, `orbit_state`)  

### 🗺️ Footprint & Geometry
- polygon footprint  
- `bbox`  
- sovereignty-generalized geometry in sensitive areas  

### 📦 Assets
- `"coherence"` — coherence COG  
- `"amplitude_master"` — optional  
- `"amplitude_slave"` — optional  
- `"thumbnail"` — PNG preview  
- `"qa"` — coherence quality mask  
- `"metadata"` — ancillary SAFE metadata  

### 🔐 Governance Metadata
- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (applies frequently for disturbance layers)  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

### 🔗 Link Graph
- `"self"`  
- `"collection"`  
- `" parent"` → coherence Collection  
- `"root"`  
- `"coherence:master_scene"`  
- `"coherence:slave_scene"`  

### 🧬 Lineage (PROV-O)
- `prov:wasGeneratedBy` → coherence pipeline  
- `prov:used` → master scene, slave scene, orbit, calibration LUTs  
- `prov:wasDerivedFrom` → GRD/GRDH Items  

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

Coherence can reveal:

- disturbed landscapes  
- damage footprints  
- infrastructure changes  
- sensitive ecological or cultural areas  

Therefore KFM enforces:

- `"kfm:h3_sensitive"` tagging for all coherence Items  
- `"kfm:mask_required"` for sovereign H3 intersections  
- geometry generalization  
- `"kfm:care_label"` + `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"` for risk-prone derivatives  
- `"kfm:governance_notes"` at every masking step  

Validated via:  
`faircare_validate.yml` · `jsonld_validate.yml` · `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

Each coherence Item must:

- pass STAC 1.x schema validation  
- include valid SAR/Coherence extension fields  
- contain proper link graph (master/slave/collection/root)  
- satisfy geometry ↔ bbox consistency  
- contain all governance metadata  
- meet sovereign masking rules  
- embed PROV-O lineage  
- pass DCAT compatibility checks  

Violations → **Item blocked**.

---

## 🔁 6. Coherence in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering
 → pair selection (t1, t2)
 → coherence computation
 → sovereignty masking
 → STAC Item generation
 → Collection update
 → governed release bundle
~~~

---

## 🔮 7. KFM Applications

- tornado/wind storm damage  
- flood-induced coherence loss  
- cultural-landscape impact monitoring  
- agricultural field-cycle detection  
- ecological disturbance mapping  
- land-change analysis  
- Focus Mode v3 environmental reasoning  
- Story Node v3 spatial context  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                          |
|--------:|------------|------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 coherence STAC Items README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../../collections/README.md) · [🌐 Sentinel-1 Root](../../../../../sentinel-1/README.md)

</div>

