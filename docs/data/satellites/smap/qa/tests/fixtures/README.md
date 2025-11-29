---
title: "📦 NASA SMAP — QA Master Fixture Library (Radiometer · RFI · SM · FT · VWC · Uncertainty)"
path: "docs/data/satellites/smap/qa/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Synthetic QA Fixture Library"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/tests-smap-qa-master-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/tests-smap-qa-master-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded with major QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP QA Master Fixture Library**  
`docs/data/satellites/smap/qa/tests/fixtures/README.md`

**Purpose**  
Provide the **shared synthetic fixture library** used across the entire SMAP QA testing stack:  
Radiometer QA · RFI QA · Soil Moisture Retrieval QA · Freeze–Thaw Retrieval QA ·  
Vegetation Water Content QA · QA → Uncertainty Modifiers.

This directory contains **sovereignty-safe, FAIR+CARE-compliant, deterministic** fixture data  
ensuring stable, reproducible, governed QA validation.

</div>

---

## 📘 1. Overview

These fixtures supply standard inputs for QA test suites validating:

- ⚠️ Radiometer QA decoding & anomaly flags  
- 📡 RFI contamination patterns  
- 🎚️ Soil Moisture retrieval confidence  
- 🌡️ Freeze–Thaw retrieval ambiguity  
- 🌱 Vegetation Water Content retrieval instability  
- 📉 QA → Uncertainty scaling behavior  
- 🛡 sovereignty masking & CARE metadata  
- 📑 STAC/DCAT QA metadata  
- 🔗 PROV-O lineage blocks  
- 🗺 pixel-level CRS/grid alignment  
- deterministic and reproducible outputs across CI  

All fixture content is **synthetic only** to avoid real environmental signal leakage.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/tests/fixtures/
├── 📄 README.md                               # This file
│
├── 📁 radiometer/                             # Radiometer QA fixtures
│   ├── sample_qa_flags.tif
│   ├── sample_qa_codes.json
│   ├── sample_metadata.json
│   └── schema_expected.json
│
├── 📁 rfi/                                    # RFI QA fixtures
│   ├── sample_rfi_mask.tif
│   ├── sample_rfi_codes.json
│   ├── sample_metadata.json
│   ├── expected_rfi_interpretation.json
│   └── schema_expected.json
│
├── 📁 retrieval_sm/                           # Soil Moisture retrieval QA fixtures
│   ├── sample_sm_conf.tif
│   ├── sample_metadata.json
│   ├── expected_sm_classification.json
│   └── schema_expected.json
│
├── 📁 retrieval_ft/                           # Freeze–Thaw retrieval QA fixtures
│   ├── sample_ft_conf.tif
│   ├── sample_ft_qa_mask.tif
│   ├── sample_metadata.json
│   ├── expected_ft_interpretation.json
│   └── schema_expected.json
│
├── 📁 retrieval_vwc/                          # Vegetation Water Content retrieval QA fixtures
│   ├── sample_vwc_conf.tif
│   ├── sample_vwc_qa_mask.tif
│   ├── sample_metadata.json
│   ├── expected_vwc_interpretation.json
│   └── schema_expected.json
│
└── 📁 uncertainty_modifiers/                  # QA → uncertainty modifier fixtures
    ├── sample_uncertainty_scale.tif
    ├── sample_metadata.json
    ├── expected_uncertainty_output.json
    └── schema_expected.json
~~~

---

## 🧩 3. Fixture Domains & Role

### ⚠️ Radiometer QA Fixtures  
Validate bitflag → QA decoding and beam/channel anomaly detection.

### 📡 RFI Fixtures  
Test contamination detection, spectral anomalies, and sovereign-safe masking.

### 🎚️ Soil Moisture Retrieval QA Fixtures  
Ensure SM retrieval confidence, ambiguous pixels, and sovereign behavior are correct.

### 🌡️ Freeze–Thaw Retrieval QA Fixtures  
Validate transition detection, instability handling, and FT seasonal sensitivity.

### 🌱 Vegetation Water Content QA Fixtures  
Validate canopy-driven retrieval noise, ambiguous VWC behavior, and FT/VWC interactions.

### 📉 Uncertainty Modifier Fixtures  
Validate integrated QA → uncertainty scaling and sovereignty-protected uncertainty floors.

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Requirements

All fixture directories ensure:

- `"kfm:care_label"` present  
- `"kfm:h3_sensitive"` propagated where applicable  
- `"kfm:mask_required"` indicated for sovereign H3 zones  
- `"kfm:sovereignty_uncertainty_floor"` enforced  
- `"kfm:governance_notes"` present  
- no real-world ecological or cultural signal leakage  

Governance assured via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. Validation Workflow

QA test suites consume these fixtures to validate:

- decoding logic  
- confidence ranges  
- ambiguity detection  
- spatial alignment  
- sovereignty safety  
- metadata correctness  
- uncertainty scaling  
- PROV-O lineage integrity  
- STAC/DCAT compliance  
- deterministic output ordering  

Any fixture mismatch → **CI hard fail**.

---

## 🔁 6. Position in SMAP ETL Pipeline (Fixture Scope)

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
    → (uses radiometer, rfi, sm, ft, vwc QA fixtures)
 → uncertainty propagation
    → (uses uncertainty modifier fixtures)
 → governance masking
 → provenance building
 → stac_writer
~~~

Fixtures simulate each QA component in isolation to allow robust, reproducible CI validation.

---

## 🔮 7. Applications Across KFM

### Hydrology  
Quality-controlled, uncertainty-aware environmental layers.

### Climate  
Reliable FT/VWC seasonal analyses built on safe QA signals.

### Archaeology  
QA-weighted environmental indicators reduce risk in cultural landscape interpretation.

### Story Node v3  
Narratives incorporate QA-backed environmental evidence.

### Focus Mode v3  
Reasoning integrates sovereign-safe QA/uncertainty models.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                           |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP QA master fixture README; FAIR+CARE/H3 aligned; CI-safe; STAC/DCAT/PROV integrated; emoji-rich.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 QA Master Tests](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

