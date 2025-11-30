---
title: "🧪 Sentinel-1 Deformation QA — Test Suite (IFG · Unwrapping · LOS Projection)"
path: "docs/data/satellites/sentinel-1/qa/deformation/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High Sensitivity QA (CARE-B · InSAR · Sovereignty-Controlled)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · RS Working Group · Sovereignty Board · FAIR+CARE Council"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sentinel1-deformation-qa-tests-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group · Sovereignty Board"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Instant"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/sentinel1-deformation-qa-tests-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-deformation-qa-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-deformation-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-deformation-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/deformation/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when InSAR QA standard updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Deformation QA — Test Suite**  
`docs/data/satellites/sentinel-1/qa/deformation/tests/`

Validates **interferograms (IFG)**, **unwrapped phase**, and  
**Line-Of-Sight displacement (LOS)** prior to sovereignty-generalization.  
Ensures deformation products are accurate, stable, reproducible,  
and sovereignty-safe.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/deformation/tests/
├── 📄 README.md
│
├── 🛰️ test_ifg_quality.py             # Wrapped interferogram validity
├── 🌍 test_unwrapping_continuity.py   # Branch-cut unwrapping continuity
└── 🌍 test_los_projection.py          # LOS displacement projection + governance metadata
~~~

✔ Emojis BEFORE filenames  
✔ Matches wetlands/tests, flood/tests, coherence/tests, radiometry/tests  
✔ No drift, no omissions  
✔ Box-safe  

---

## 📘 2. Purpose

Deformation QA is required because LOS displacement layers can reveal:

- ground-motion patterns  
- hydrologic drawdown  
- culturally significant terrain change  
- sovereign ecological stress  

These tests ensure:

- numerically correct InSAR interferometry  
- correct phase-unwrapping  
- valid LOS projection  
- governance metadata correctness  
- deterministic behavior for release  

---

## 🧩 3. Test Modules

### 🛰️ `test_ifg_quality.py`
Ensures:

- correct complex multiply for IFG  
- wrapped phase ∈ [−π, +π]  
- burst & orbit alignment  
- proper handling of decorrelated regions  
- match with `ifg_reference.tif` in fixtures  

---

### 🌍 `test_unwrapping_continuity.py`
Validates:

- correct branch-cut unwrapping  
- residue detection correctness  
- no rewrap discontinuities  
- DEM geometry alignment  
- match with `unwrapped_reference.tif`  

---

### 🌍 `test_los_projection.py`
Verifies:

- correct LOS projection from unwrapped phase  
- correct incidence-angle + look-vector use  
- LOS displacement sign conventions  
- sovereignty flags (`h3_sensitive`, `mask_required`) propagation  
- agreement with `los_reference_generalized.tif`  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Deformation QA ensures:

- `"kfm:care_label": "CARE-B"`  
- `"kfm:h3_sensitive": true`  
- `"kfm:mask_required": true"`  
- `"kfm:governance_notes"` correctness  
- readiness for sovereignty-generalization transforms  

These protections prevent leakage of sensitive geophysical insights  
over tribal lands and cultural landscapes.

---

## 🔗 5. PROV-O Lineage

QA lineage for deformation:

~~~json
{
  "prov:Entity": "s1_deformation_qa_validation",
  "prov:wasGeneratedBy": "s1_deformation_qa_pipeline",
  "kfm:qa_type": "deformation",
  "kfm:care_label": "CARE-B"
}
~~~

This metadata attaches to all downstream STAC Items + Focus Mode narratives.

---

## 🧪 6. CI Integration

The CI system enforces:

- IFG quality  
- unwrapping continuity  
- LOS math correctness  
- bitwise match to fixtures  
- schema + SHACL validity  
- governance metadata presence  
- cross-platform determinism  

Any mismatch → **CI BLOCK**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict deformation-QA tests README; emoji alignment validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

