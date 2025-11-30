---
title: "🌍 Sentinel-1 InSAR — Interferograms (Wrapped Phase Inputs for LOS Deformation)"
path: "docs/data/satellites/sentinel-1/transforms/deformation/interferograms/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (High-Sensitivity SAR Derivative)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Oversight"

license: "MIT"
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
telemetry_schema: "../../../../../../../schemas/telemetry/sat-deformation-interferograms-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-interferograms-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-interferograms-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-deformation-interferograms:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-deformation-interferograms"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/deformation/interferograms/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded on next InSAR model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR — Wrapped Interferograms**  
`docs/data/satellites/sentinel-1/transforms/deformation/interferograms/`

Wrapped phase interferograms used as **InSAR inputs** for  
unwrapping → LOS displacement → sovereignty-generalized deformation layers.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/deformation/interferograms/
├── 📄 README.md
│
├── 🌍 ifg_20250101_20250113.tif       # Wrapped interferogram (master/slave pair)
├── 🌍 ifg_20250314_20250326.tif       # Additional wrapped interferogram
└── 🌍 ifg_20250620_20250702.tif       # Additional wrapped interferogram(s)
~~~

✔ Emoji BEFORE filenames  
✔ No drift  
✔ Mirrors deformation/, coherence/, rtc/, radiometric fixtures/tests style  
✔ 100% box-safe  

---

## 📘 2. Purpose

Wrapped interferograms represent the **complex phase difference** between two  
SAR acquisitions and are the **core input** for phase unwrapping and LOS  
displacement computation.

They encode:

- atmospheric phase  
- ground motion  
- sensor geometry  
- noise / decorrelation  

All wrapped interferograms here are **intermediate products**,  
not directly released to the public.

---

## 🧩 3. Processing Steps Producing Interferograms

### 1️⃣ Co-registration  
- Align master/slave complex images  
- Ensure identical geometry  

### 2️⃣ Interferogram Formation  
Complex multiply:

~~~text
ifg = master * conj(slave)
~~~

### 3️⃣ Phase Extraction  
Wrapped phase representation:

~~~text
phase_wrapped = atan2( imag(ifg), real(ifg) )
~~~

### 4️⃣ Optional Filtering  
- Goldstein filtering  
- Adaptive smoothing  
- Noise suppression  
- Speckle reduction  

### 5️⃣ Output  
Interferogram tiles (this directory) passed to:

- unwrapping (next stage)  
- QA masks  
- LOS displacement conversion  

---

## 🔗 4. PROV-O Lineage

Each interferogram is a **prov:Entity**, e.g.:

~~~json
{
  "prov:Entity": "s1_ifg_20250101_20250113",
  "prov:used": ["rtc_gamma0_vv", "rtc_gamma0_vh", "orbit_metadata"],
  "prov:wasGeneratedBy": "s1_ifg_generation",
  "kfm:care_label": "CARE-B",
  "kfm:h3_sensitive": true
}
~~~

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Interferograms are **high-risk** (CARE-B):

- can reveal land deformation  
- can reveal culturally sensitive risk regions  
- must NEVER be distributed without generalization  
- must propagate `"kfm:*"` metadata  

Sovereignty masking occurs in the **LOS stage**,  
but interferograms must retain all governance metadata.

---

## 🧪 6. CI Validation

CI ensures:

- correct wrapped phase range (–π to +π)  
- complex multiply logic correctness  
- alignment with fixtures  
- deterministic FFT/phase results  
- correct master/slave ordering  
- correct metadata propagation  
- schema + SHACL validation  

Any drift → CI block.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting interferogram README; emoji-prefix alignment validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🌍 Unwrapped Phase](../unwrapped/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

