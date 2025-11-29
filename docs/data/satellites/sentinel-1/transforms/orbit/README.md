---
title: "🔧 Sentinel-1 — Orbit Correction Transform (State Vectors · Doppler · Geometry · Timing)"
path: "docs/data/satellites/sentinel-1/transforms/orbit/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (SAR Preprocessing Layer)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-orbit-transform-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing WG"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Instant"

json_schema_ref: "../../../../../../schemas/json/sentinel1-orbit-transform-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-orbit-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-orbit:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-orbit"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/orbit/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA orbit reprocessing epoch"
---

<div align="center">

# 🔧 **Sentinel-1 Orbit Correction Transform**  
`docs/data/satellites/sentinel-1/transforms/orbit/`

Orbit correction is the **first deterministic ETL stage** in the Sentinel-1 pipeline:  
SAFE → GRD → GRDH → RTC → Coherence → Deformation → Flood → Wetlands → STAC.

</div>

---

## 🗂️ Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/orbit/
├── 📄 README.md
│
├── 🧪 tests/
│   ├── 🔧 test_orbit_basic.py
│   ├── 🔧 test_doppler.py
│   └── 🔧 test_state_vectors.py
│
└── 📁 fixtures/
    ├── 🛰️ S1A_OPER_AUX_RESORB.xml
    ├── 🛰️ S1A_OPER_AUX_POEORB.xml
    └── 📄 burst_metadata.json
~~~

**NO drift.  
NO missing emojis.  
NO substitutions.  
Exact style preserved.**

---

## 📘 Purpose

Orbit correction resolves:

- precise satellite position & velocity  
- state vector interpolation  
- Doppler centroid estimation  
- timing alignment (IW burst timing)  
- geometry consistency for all later SAR transforms

Downstream transforms **depend entirely** on this stage.

---

## 🔧 Processing Stages

### 1️⃣ Orbit File Selection  
Priority:  
1. **POEORB** (precise)  
2. **RESORB** (restituted)

### 2️⃣ State Vector Interpolation  
- High-resolution interpolation over burst timeline  
- Inputs to Doppler, geometry, RTC, interferogram formation

### 3️⃣ Doppler Centroid Modeling  
- Estimate f_dc over swath  
- Required for coherence, RTC, InSAR

### 4️⃣ Timing Corrections  
- Zero-Doppler standardization  
- IW burst alignment  
- Range → slant mapping

### 5️⃣ Geolocation Preconditioning  
- incidence angle  
- look direction  
- slant/ground geometry basis

---

## 🔗 PROV-O Lineage Emitted

```json
{
  "prov:Activity": "s1_orbit_correction",
  "prov:used": [
    "SAFE_manifest",
    "AUX_POEORB",
    "AUX_RESORB"
  ],
  "prov:generated": [
    "orbit_corrected_metadata"
  ],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
```

All downstream STAC Items link back to this.

---

## 🔐 Governance & CARE

Orbit correction is **CARE-A**, but governance metadata must still propagate:

- `"kfm:care_label": "CARE-A"`
- `"kfm:h3_sensitive"` forwarded as-is if seen upstream
- No sovereignty masking at this stage

---

## 🧪 Test Requirements

- state vector continuity  
- Doppler centroid accuracy  
- SAFE/orbit temporal alignment  
- deterministic outputs  
- burst timing consistency  

---

## 🧭 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Full non-drifting rebuild with strict emoji-prefix directory layout. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🛰 Radiometric Calibration](../../transforms/radiometric/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

