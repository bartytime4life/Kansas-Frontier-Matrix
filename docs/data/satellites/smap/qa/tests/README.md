---
title: "🧪 NASA SMAP — QA Master Test Suite (Radiometer · RFI · SM · FT · VWC · Uncertainty Modifiers)"
path: "docs/data/satellites/smap/qa/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public QA/Validation Suite"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

json_schema_ref: "../../../../schemas/json/tests-smap-qa-master-v11.json"
shape_schema_ref: "../../../../schemas/shacl/tests-smap-qa-master-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-master-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-master-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded with major QA schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — QA Master Test Suite**  
`docs/data/satellites/smap/qa/tests/README.md`

**Purpose**  
Provide the **central, governed test suite** validating all QA-related layers  
in the SMAP ingestion pipeline:

- ⚠️ Radiometer QA  
- 📡 RFI QA  
- 🎚️ Soil Moisture Retrieval QA  
- 🌡️ Freeze–Thaw Retrieval QA  
- 🌱 Vegetation Water Content QA  
- 📉 QA → Uncertainty Modifier Layer  

This suite ensures that all QA datasets are correct, sovereign-safe, FAIR+CARE compliant,  
and fully ready for STAC/DCAT release.

</div>

---

## 📘 1. Overview

This QA Master Suite validates:

- ✔ QA decoding correctness across all domains  
- ✔ proper mapping from QA bitfields to unified KFM QA semantics  
- ✔ pixel-level CRS alignment for all QA rasters  
- ✔ sovereignty/H3 masks work uniformly across QA products  
- ✔ full propagation of CARE labels + `"kfm:governance_notes"`  
- ✔ correct QA → uncertainty propagation  
- ✔ correct metadata integration (`kfm:qa_values`, QA schema, quality notes)  
- ✔ correct temporal and spatial metadata  
- ✔ deterministic, reproducible outputs  
- ✔ valid JSON-LD PROV-O lineage connections  

If any test fails at this level →  
**all dependent SMAP STAC Collections are blocked** until resolved.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/
├── 📄 README.md                                  # This file
│
├── 🧪 test_radiometer_qa.py                      # Radiometer QA value/bitmask tests
├── 🧪 test_rfi_qa.py                             # RFI contamination mask tests
├── 🧪 test_sm_retrieval_qa.py                    # Soil moisture retrieval QA tests
├── 🧪 test_ft_retrieval_qa.py                    # Freeze–Thaw retrieval QA tests
├── 🧪 test_vwc_retrieval_qa.py                   # Vegetation water content retrieval QA tests
├── 🧪 test_uncertainty_modifiers.py              # QA → uncertainty scaling tests (Stage 5)
│
└── 🔧 fixtures/                                   # Shared QA fixture library
    ├── radiometer/                               # Radiometer QA fixtures
    ├── rfi/                                      # RFI QA fixtures
    ├── retrieval_sm/                             # SM retrieval QA fixtures
    ├── retrieval_ft/                             # FT retrieval QA fixtures
    ├── retrieval_vwc/                            # VWC retrieval QA fixtures
    └── uncertainty_modifiers/                    # Uncertainty modifier fixtures
~~~

---

## 🧩 3. What This Suite Validates

### ⚠️ Radiometer QA  
Beam/channel QA, bitfield decoding, sensor anomalies.

### 📡 RFI QA  
Contamination likelihood, spectral interference, sovereignty-safe masking.

### 🎚️ SM Retrieval QA  
Confidence range, ambiguous retrievals, soil-canopy interactions.

### 🌡️ FT Retrieval QA  
Freeze–thaw transitions, mixed pixels, seasonal boundary stability.

### 🌱 VWC Retrieval QA  
Canopy-driven instability, ambiguous pixel handling, vegetation thresholds.

### 📉 Uncertainty Modifiers  
Integrated QA → uncertainty scaling, sovereignty floors, final uncertainty grids.

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

This master suite ensures that ALL QA layers:

- propagate `"kfm:care_label"`  
- propagate `"kfm:h3_sensitive"`  
- apply `"kfm:mask_required"`  
- enforce `"kfm:sovereignty_uncertainty_floor"`  
- include `"kfm:care_label_reason"`  
- include `"kfm:governance_notes"`  
- DO NOT leak sensitive ecological transition info  
- DO NOT provide over-precise retrieval signals in tribal lands  

Governance validated under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. CI Integration

This suite runs as part of:

- **ci.yml** (unit + integration QA tests)  
- **data_pipeline.yml** (ETL integrity)  
- **jsonld_validate.yml** (ontology + PROV validation)  
- **stac_validate.yml** (STAC/DCAT correctness)  
- **faircare_validate.yml** (sovereignty + CARE validation)

Any failure blocks:

- QA layers  
- Uncertainty modifiers  
- All SMAP STAC Item & Collection generation  

---

## 🔁 6. QA Position in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
    → radiometer QA
    → rfi QA
    → SM retrieval QA
    → FT retrieval QA
    → VWC retrieval QA
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
 → QA DATASET LAYER (validated by this master suite)
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
QA-driven uncertainty improves anomaly detection performance.

### Climate  
Reliable FT/VWC seasonal modeling and drought analysis.

### Archaeology  
Sovereignty-safe environmental signals for cultural landscape research.

### Story Node v3  
Narratives weighted by QA reliability scores.

### Focus Mode v3  
Environmental reasoning influenced by uncertainty + QA metrics.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|---------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP QA Master Suite README; unifies Radiometer, RFI, SM, FT, VWC, and uncertainty QA testing; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🔧 QA Fixtures](fixtures/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

