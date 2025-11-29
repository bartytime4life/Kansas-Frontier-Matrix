---
title: "🛰️ Sentinel-1 Radiometric Calibration — ETL Transform (σ⁰ VV/VH · LUTs · Noise Correction)"
path: "docs/data/satellites/sentinel-1/transforms/radiometric/README.md"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-radiometric-transform-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
risk_category: "Low"
public_exposure_risk: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-radiometric-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-radiometric-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-radiometric:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-radiometric"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/radiometric/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA radiometric model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 Radiometric Calibration Transform**  
`docs/data/satellites/sentinel-1/transforms/radiometric/`

Produces **σ⁰ VV/VH calibrated backscatter**, removing noise, applying ESA LUTs,  
and preparing data for RTC → Coherence → Flood → Wetlands → InSAR pipelines.

</div>

---

## 🗂️ Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/radiometric/
├── 📄 README.md
│
├── 📁 calibration_luts/               # ESA LUTs used during σ⁰ calibration
│   ├── 📄 lut_vv.json
│   └── 📄 lut_vh.json
│
├── 🧪 tests/
│   ├── 🛰️ test_sigma0_core.py
│   ├── 🛰️ test_noise_floor.py
│   └── 🛰️ test_lut_interpolation.py
│
└── 📁 fixtures/
    ├── 🛰️ SAFE_annotation.xml
    ├── 🛰️ calibration_lut_sample.json
    └── 📄 noise_metadata.json
~~~

✔ **Emoji BEFORE folders/files**  
✔ **Consistent with the entire STAC + transforms hierarchy**  
✔ **No drift, no missing emojis, no substitutions**

---

## 📘 1. Purpose

Radiometric calibration converts Sentinel-1 **raw amplitude** into physically meaningful  
**σ⁰ backscatter** (VV/VH), providing:

- radiometric consistency  
- unit-normalized SAR measurements  
- correction of instrument & geometry effects  
- the foundation for:  
  - GRD/GRDH  
  - RTC γ⁰  
  - Coherence  
  - Flood mapping  
  - Wetlands observables  
  - InSAR deformation preconditioning

This transform is **mandatory** before any downstream SAR analytics.

---

## 🧩 2. Inputs & Outputs

### **Inputs**
- ESA SAFE annotation XML  
- RAW amplitude or GRD amplitude  
- Calibration LUTs (VV/VH)  
- Noise vectors / radiometric metadata  
- Orbit-corrected geometric parameters  

### **Outputs**
- **σ⁰ VV COG**
- **σ⁰ VH COG**
- Backscatter metadata:
  ```json
  {
    "sigma0_vv": "...",
    "sigma0_vh": "...",
    "noise_floor_applied": true,
    "calibration_lut_version": "ESA-2025",
    "radiometric_corrections": ["noise", "antenna_pattern", "range_spreading"]
  }
  ```

All outputs feed **RTC** or directly become **GRD/GRDH** STAC assets.

---

## 🧬 3. Processing Stages

### 3.1 LUT Loading & Interpolation
- Load VV/VH calibration LUTs  
- Interpolate per-pixel gain + offset  
- Validate LUT integrity via schema

### 3.2 Noise Floor Correction
- Subtract radiometric noise  
- Handle border-noise anomalies  
- Produce “clean amplitude” signal

### 3.3 Antenna Pattern Correction
Ensures consistent illumination:
- pattern gain removal  
- incidence-angle normalization  

### 3.4 Range Spreading Loss Correction
Correct power decay due to geometry.

### 3.5 σ⁰ Conversion
Final computation:
```
σ⁰ = (calibrated_amplitude²) * calibration_gain
```

### 3.6 Metadata Export
Generate:
- calibration provenance  
- LUT version  
- noise-floor metadata

---

## 🔗 4. PROV-O Lineage

Radiometric transforms emit lineage:

```json
{
  "prov:Activity": "s1_radiometric_calibration",
  "prov:used": [
    "SAFE_annotation",
    "calibration_lut",
    "noise_metadata"
  ],
  "prov:generated": [
    "sigma0_vv",
    "sigma0_vh"
  ],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
```

This lineage becomes embedded in **all downstream STAC Items**.

---

## 🔐 5. FAIR+CARE & Sovereignty Considerations

Radiometric calibration is generally **CARE-A**,  
but calibration outputs inherit upstream governance flags.

This stage:

- **does not perform sovereignty masking**  
- but must propagate:
  - `"kfm:care_label"`  
  - `"kfm:h3_sensitive"` (if upstream flagged)  
  - `"kfm:governance_notes"`  

Downstream transforms (flood, wetlands, InSAR) apply restrictions.

---

## 🧪 6. Testing Requirements

Tests must verify:

- LUT interpolation accuracy  
- noise-floor subtraction correctness  
- consistent σ⁰ results across platforms  
- deterministic (bit-exact) outputs  
- calibrated radiometry consistency  
- valid JSON schema compliance  

Failures → **CI block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict emoji-compliant radiometric transform README, aligned with orbit subtree. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🔧 Orbit Transform](../orbit/README.md) · [🏞️ RTC Transform](../../transforms/rtc/README.md)

</div>

