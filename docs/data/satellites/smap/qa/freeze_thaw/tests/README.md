---
title: "🧪 NASA SMAP — Freeze–Thaw Retrieval QA Test Suite (Confidence · Ambiguity · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/freeze_thaw/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public QA Test Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-ft-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-ft-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:freeze-thaw-qa-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-freeze-thaw-qa-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/freeze_thaw/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next FT QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP Freeze–Thaw Retrieval QA Test Suite**  
`docs/data/satellites/smap/qa/freeze_thaw/tests/README.md`

**Purpose**  
Validate the **Freeze–Thaw (FT) QA dataset** produced by the SMAP ETL, guaranteeing that  
confidence rasters, ambiguity masks, metadata, and sovereignty-aware governance behavior  
are correct, deterministic, and compliant with KFM v11.2 governance and metadata rules.

</div>

---

## 📘 1. Overview

This test suite ensures FT QA layers:

- 🌡️ correctly reflect freeze–thaw retrieval confidence  
- ⚠️ identify ambiguous or transitional FT states  
- 🎚️ integrate properly with uncertainty propagation  
- 🗺️ align spatially with SMAP core rasters  
- 🛡 propagate CARE/H3 sovereignty metadata  
- 📑 include valid STAC/DCAT metadata  
- 🔗 embed complete PROV-O lineage  
- 🚫 do not reveal sensitive, high-precision seasonal boundaries in sovereign lands  

Any failure → **KFM blocks FT QA dataset release**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/freeze_thaw/tests/
├── 📄 README.md                                  # This file
│
├── 🧪 test_ft_confidence_ranges.py               # Validate FT confidence values/ranges
├── 🧪 test_ft_ambiguity_mask.py                  # Validate ambiguous/mixed state detection
├── 🧪 test_ft_metadata_integrity.py              # STAC/DCAT metadata tests
├── 🧪 test_governance_preservation.py            # CARE/H3 sovereignty metadata propagation tests
│
└── 🔧 fixtures/
    ├── sample_ft_conf.tif                       # Synthetic FT confidence layer
    ├── sample_ft_qa_mask.tif                    # Synthetic FT ambiguity mask
    ├── sample_metadata.json                     # QA metadata stub
    ├── expected_ft_interpretation.json          # Deterministic FT decoding/classification
    └── schema_expected.json                     # Strict validation schema
~~~

---

## 🧩 3. Test Domains & Expectations

### 🌡️ **FT Confidence Range Tests**
Validate:

- allowed 0–100 or normalized confidence ranges  
- correct mapping to FT retrieval outcomes (Frozen/Thawed/Ambiguous)  
- stable behavior across test tiles  

### ⚠️ **Ambiguity Mask Tests**
Validate:

- detection of mixed-state transitions  
- snow/rain contamination handling  
- canopy-driven FT noise  
- seasonal boundary instability  
- sovereign-safe generalization in sensitive zones  

### 🗺️ **Spatial Alignment Tests**
Validate:

- CRS integrity  
- pixel-level alignment with SMAP processed rasters  
- correct scaling behavior across tiles  
- consistency with radiometer QA and RFI masks  

### 📑 **Metadata Integrity Tests**
Validate:

- STAC QA fields (`kfm:qa_values`, FT-specific QA schema)  
- DCAT quality notes  
- `"kfm:care_label"` and `"kfm:care_label_reason"`  
- "kfm:governance_notes" presence  
- temporal + spatial extents  
- PROV-O lineage roots  

### 🛡 **Governance Preservation Tests**
Validate:

- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` in sovereign regions  
- `"kfm:sovereignty_uncertainty_floor"` retained  
- correct CARE label propagation  
- no false precision near tribal boundaries  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Freeze–Thaw transitions often correlate with ecological and cultural boundaries  
in Indigenous territories.  
Therefore FT QA must:

- avoid revealing over-precise transitions  
- apply sovereignty-aware aggregation  
- maintain uncertainty floors  
- include `"kfm:governance_notes"` where masking occurs  
- respect all CARE A/B policies  

Governance is enforced via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. CI Integration

This test suite is executed under:

- **ci.yml**  
- **data_pipeline.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **faircare_validate.yml**  

Any failure halts FT QA dataset publication.

---

## 🔁 6. FT QA in SMAP’s ETL Chain

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → FT retrieval QA (validated here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
Accurate winter/spring transition context.

### Climate  
Freeze-line dynamics for modeling cold-season hazards.

### Archaeology  
Avoid misinterpreting environmental signals in sensitive cultural landscapes.

### Story Node v3  
Seasonal narratives grounded in QA-backed confidence.

### Focus Mode v3  
Confidence affects explanation detail & weighting.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                           |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Freeze–Thaw QA test-suite README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; complete & robust.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🌡️ FT QA Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

