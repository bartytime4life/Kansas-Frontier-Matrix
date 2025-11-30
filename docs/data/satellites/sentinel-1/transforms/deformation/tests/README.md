---
title: "🧪 Sentinel-1 InSAR Deformation — Test Suite Overview (IFG · Unwrapping · LOS · Sovereignty Generalization)"
path: "docs/data/satellites/sentinel-1/transforms/deformation/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High-Sensitivity · Internal Technical Test Suite"
status: "Active · Enforced"
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
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:Feature"
  owl_time: "Interval"

json_schema_ref: "../../../../../../schemas/json/sentinel1-deformation-tests-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-deformation-tests-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-deformation-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-deformation-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/deformation/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next InSAR deformation algorithm update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 InSAR Deformation — Test Suite**  
`docs/data/satellites/sentinel-1/transforms/deformation/tests/`

Validates **interferogram formation**, **phase unwrapping**, **LOS displacement**,  
and **sovereignty generalization** for Sentinel-1 deformation products in KFM v11.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/deformation/tests/
├── 📄 README.md
│
├── 🌍 test_ifg_generation.py          # Wrapped interferogram correctness
├── 🌍 test_unwrapping.py              # Branch-cut phase unwrapping validation
└── 🌍 test_los_generalization.py       # LOS displacement + sovereignty generalization checks
~~~

✔ Emoji BEFORE filenames  
✔ Same pattern as rtc/tests, coherence/tests, radiometric/tests  
✔ Guaranteed box-safe  

---

## 📘 2. Purpose

This suite ensures that InSAR deformation ETL stages:

- generate mathematically correct interferograms  
- unwrap phase reliably  
- convert phase → LOS displacement correctly  
- apply **mandatory sovereignty generalization**  
- propagate `"kfm:*"` governance metadata  
- remain deterministic across environments  
- produce STAC-ready LOS deformation rasters  

Because deformation is **high sensitivity**, rigorous testing is required to prevent  
misleading or harmful outputs.

---

## 🧩 3. Test Modules

### 🌍 `test_ifg_generation.py`
Verifies:

- complex multiply: `ifg = master * conj(slave)`  
- correct wrapped phase range (–π to +π)  
- correct co-registration behavior  
- deterministic interferogram generation  
- alignment with reference `ifg_reference.tif` (fixtures)

---

### 🌍 `test_unwrapping.py`
Ensures:

- correct branch-cut implementation  
- correct residue detection  
- stable continuous phase generation  
- no phase re-wraps  
- numeric consistency under noisy conditions  
- bit-exact match to `unwrapped_reference` fixtures  

---

### 🌍 `test_los_generalization.py`
Validates:

- correct LOS projection math  
- correct application of look vectors  
- H3 sovereignty generalization  
- uncertainty flooring  
- spatial smoothing inside sovereign zones  
- `"kfm:mask_required"` and `"kfm:sovereignty_generalized"` correct in metadata  
- strict agreement with `los_reference_generalized.tif`  

---

## 🔗 4. PROV-O & Governance Validation

Tests explicitly check:

- `"prov:used"` includes interferograms, unwrapped phase, orbit metadata, DEM  
- `"prov:wasGeneratedBy"` correct for each stage  
- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- `"kfm:sovereignty_generalized" = true`  

Any missing field → immediate CI block.

---

## 🧪 5. CI Integration

These tests run inside:

- `transform-tests.yml`  
- `data-pipeline.yml`  
- deformation-specific PR validation workflows

CI enforces:

- bitwise-stable LOS displacement  
- consistent unwrapping  
- H3 sovereignty compliance  
- correct lineage embedding  
- schema + SHACL validation  
- stable numerical outputs across OS/architecture differences  

All failures block ETL updates.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, no-drift deformation test-suite README; emoji style consistent. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

