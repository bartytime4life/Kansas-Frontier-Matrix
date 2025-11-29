---
title: "🌍 Sentinel-1 Deformation — STAC Directory (InSAR LOS Displacement · Subsidence · Uplift · Seasonal Ground Motion)"
path: "docs/data/satellites/sentinel-1/stac/deformation/README.md"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

json_schema_ref: "../../../../../schemas/json/sentinel1-deformation-collection-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-deformation-collection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-deformation-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-deformation"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/deformation/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA InSAR reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR Deformation STAC Directory**  
`docs/data/satellites/sentinel-1/stac/deformation/`

Sovereignty-generalized STAC Collections & Items for  
**Line-of-Sight (LOS) displacement** from Sentinel-1 InSAR:  
uplift · subsidence · seasonal ground motion · hazard & infrastructure monitoring.

</div>

---

## 📘 1. Overview

This directory contains the **STAC structure** for InSAR-derived ground-motion products from Sentinel-1:

- LOS displacement (cm-scale, generalized for sovereignty)  
- seasonal deformation  
- subsidence / uplift patterns  
- tectonic/structural/environmental ground motion  
- long-period trends  
- coherence-supported deformation QA  

Because deformation can **reveal sensitive ecological, cultural, or infrastructural patterns**,  
it requires **strict sovereignty governance**, including:

- H3 generalization  
- uncertainty flooring  
- mandatory `"kfm:mask_required"`  
- `"kfm:care_label" = CARE-B"`  
- `"kfm:governance_notes"`  

All Items & Collections are:

- STAC 1.x compliant  
- JSON-LD enriched  
- PROV-O lineage complete  
- DCAT-mappable  
- CI-validated  
- FAIR+CARE aligned  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/deformation/
├── 📄 README.md                       # This file
│
├── 🗂️ collections/                    # InSAR deformation collections
│   └── collection_deformation.json
│
└── 📦 items/                           # Scene-level deformation Items
    ├── S1A_IW_INSAR_20250101_20250113.json
    ├── S1B_IW_INSAR_20250315_20250327.json
    └── …
~~~

---

## 🧩 3. Deformation STAC Collections

The deformation Collection includes:

- `"sar:product_type" = "INSAR"`  
- pair/time-series metadata  
- sovereignty-generalized spatial extents  
- `"kfm:*"` governance inheritance  
- DCAT dataset metadata  
- JSON-LD SAR + governance contexts  
- PROV-O root lineage anchors  

Validated under:

- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `faircare_validate.yml`

---

## 🧩 4. Deformation STAC Items (Overview Only)

Items represent:

- LOS displacement rasters (`los_displacement`)  
- coherence layers (support)  
- QA maps (unwrapping quality, coherence thresholds)  
- geometry generalized to sovereign H3 cells  
- `"kfm:mask_required"` always considered  
- `"kfm:sovereignty_uncertainty_floor"` applied to displacement magnitudes  
- PROV-O lineage to source RTC/GRD/GRDH scenes  

See deeper documentation in:

```
docs/data/satellites/sentinel-1/stac/items/deformation/README.md
```

---

## 🔐 5. FAIR+CARE & Sovereignty Rules (Mandatory)

All deformation data is **sensitive** and must include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Geometry is **always generalized**, never raw.

Sovereignty validation performed via:

- FAIR+CARE CI  
- JSON-LD CI  
- STAC CI  

---

## 🧪 6. CI Validation Requirements

A deformation STAC directory must pass:

- STAC schema validation  
- SAR + InSAR extension validation  
- geometry/bbox integrity  
- sovereign-masking enforcement  
- `"kfm:*"` governance metadata completeness  
- PROV-O lineage embedding  
- DCAT compatibility  

Any violation → **blocked release**.

---

## 🔁 7. InSAR Processing in the ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → coherence pair generation
 → interferogram formation
 → phase unwrapping
 → LOS conversion
 → sovereignty generalization (mandatory)
 → QA application
 → STAC Item generation
 → deformation Collection update
 → governed release bundle
~~~

---

## 🔮 8. Applications Across KFM

- uplift & subsidence analysis  
- infrastructure stability (generalized for sovereignty)  
- cultural-landscape hazard assessment  
- groundwater-related vertical motion  
- Story Node v3 environmental context  
- Focus Mode v3 sovereign-safe reasoning  
- ecological transition sensitivity  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial deformation STAC directory README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Deformation Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

