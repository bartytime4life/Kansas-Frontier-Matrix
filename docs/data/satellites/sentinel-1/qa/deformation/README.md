---
title: "🧪 Sentinel-1 Deformation QA — InSAR Validation (IFG · Unwrapping · LOS · Sovereignty Generalization Readiness)"
path: "docs/data/satellites/sentinel-1/qa/deformation/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High Sensitivity QA (CARE-B · InSAR · Sovereignty-Controlled)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · Remote Sensing WG · Sovereignty Board · FAIR+CARE Council"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-B"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sentinel1-deformation-qa-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "High"
risk_category: "Very High"
redaction_required: true

data_steward: "Remote Sensing Working Group · Sovereignty Board"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../schemas/json/sentinel1-deformation-qa-v11.json"
shape_schema_ref: "../../../../schemas/shacl/sentinel1-deformation-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-deformation:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-deformation"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/deformation/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded after next InSAR QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Deformation QA**  
`docs/data/satellites/sentinel-1/qa/deformation/`

Validates the **InSAR deformation chain**:  
**interferogram generation (IFG)** → **phase unwrapping** → **LOS displacement** → **sovereignty generalization readiness**.

Ensures deformation outputs are accurate, reproducible, and safe for  
sovereignty-controlled landscapes.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/deformation/
├── 📄 README.md
│
├── 🧪 tests/                     # InSAR QA test suite
│   ├── 🧪 test_ifg_quality.py
│   ├── 🧪 test_unwrapping_continuity.py
│   └── 🧪 test_los_projection.py
│
└── 📁 fixtures/                  # Reference IFG, unwrapped, LOS truth data
    ├── 🛰️ ifg_reference.tif
    ├── 🌍 unwrapped_reference.tif
    └── 🌍 los_reference_generalized.tif
~~~

✔ Emoji BEFORE filenames  
✔ Matches flood/qa, radiometry/qa, coherence/qa  
✔ 100% box-safe  

---

## 📘 2. Purpose

Deformation QA ensures KFM’s Sentinel-1 InSAR deformation products:

- are interferometrically coherent  
- unwrap correctly  
- produce stable LOS displacements  
- propagate sovereignty & CARE metadata  
- can be safely generalized and masked in later transforms  
- are reliable for scientific / historical / hydrological insight

Deformation layers drive:

- Story Node v3 geological/hydrological/archaeological contexts  
- Focus Mode v3 terrain-change narratives  
- hazard mapping (subsidence, uplift)  
- environmental resource risk monitoring  

Because InSAR displacement may reveal culturally sensitive change patterns, QA here is **CARE-B and sovereignty-enforced**.

---

## 🧩 3. QA Dimensions

### 🧪 Interferogram QA (`test_ifg_quality.py`)
Verifies:

- proper master/slave complex multiply  
- wrapped phase range ∈ [–π, +π]  
- burst alignment correctness  
- orbit-metadata alignment  
- interferogram coherence expectations  
- correct behavior in decorrelated regions  

Matches fixture: `ifg_reference.tif`.

---

### 🧪 Unwrapping QA (`test_unwrapping_continuity.py`)
Ensures:

- branch-cut unwrapping correctness  
- residue detection → correct cuts  
- absence of rewrap discontinuities  
- stable continuous-phase output  
- DEM/geometry consistency  

Matches fixture: `unwrapped_reference.tif`.

---

### 🧪 LOS Projection QA (`test_los_projection.py`)
Verifies:

- correct LOS displacement math  
- correct use of look vectors & incidence angles  
- stable behavior in low-coherence regions  
- correct sovereignty metadata inheritance  
- ready for generalization rules (`mask_required`, `h3_sensitive`)  

Matches fixture: `los_reference_generalized.tif`.

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Because deformation patterns can reveal sensitive:

- hydrologic drawdown  
- structural stress  
- archaeological disturbance  
- tribal-land environmental changes  

QA must enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:governance_notes"` correctness  
- predictable sovereignty-safe behavior before transforms downstream  

The QA suite **does not apply generalization**,  
but ensures the metadata required by the governance transform is correct.

---

## 🔗 5. PROV-O Lineage

Deformation QA outputs attach lineage:

~~~json
{
  "prov:Entity": "s1_deformation_qa_validation",
  "prov:wasGeneratedBy": "s1_deformation_qa_pipeline",
  "kfm:qa_type": "deformation",
  "kfm:care_label": "CARE-B"
}
~~~

This ensures reproducibility & auditability across releases.

---

## 🧪 6. CI Integration

CI enforces:

- interferogram correctness  
- unwrapping continuity  
- LOS math validity  
- cross-platform determinism  
- fixture matching  
- schema/SHACL alignment  
- governance metadata propagation  

Any mismatch → **CI BLOCK**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict deformation QA README; emoji prefix + structure validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](./tests/README.md) · [📁 Fixtures](./fixtures/README.md)

</div>

