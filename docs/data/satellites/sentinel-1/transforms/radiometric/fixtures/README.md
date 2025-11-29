---
title: "📁 Sentinel-1 Radiometric Calibration — Fixtures"
path: "docs/data/satellites/sentinel-1/transforms/radiometric/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Test Fixtures)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Instant"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-radiometric-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-radiometric-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/radiometric/fixtures/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded when ESA SAFE schema changes"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Radiometric Calibration — Fixture Library**  
`docs/data/satellites/sentinel-1/transforms/radiometric/fixtures/`

Controlled input files used by the **σ⁰ radiometric calibration ETL tests**, including  
SAFE annotation subsets, reduced calibration LUT samples, and noise-floor metadata.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/radiometric/fixtures/
├── 📄 README.md
│
├── 🛰️ SAFE_annotation.xml           # Minimal SAFE annotation for σ⁰ test runs
├── 🛰️ calibration_lut_sample.json   # Reduced ESA LUT (VV/VH), for test interpolation
└── 📄 noise_metadata.json           # Sample radiometric noise metadata
~~~

✔ Emoji BEFORE filename  
✔ No comment-emoji drift  
✔ Exactly matches orbit/fixtures, rtc/fixtures, flood/fixtures style  
✔ Box guaranteed NOT to break

---

## 📘 2. Purpose

These fixtures supply **deterministic test inputs** to the radiometric calibration stage.

They allow CI to reliably test:

- LUT loading  
- LUT interpolation  
- noise-floor subtraction  
- σ⁰ calculation stability  
- metadata correctness  
- calibration edge conditions  

Without relying on large or proprietary SAFE products.

---

## 🛰️ 3. Fixture Descriptions

### 🛰️ `SAFE_annotation.xml`
A reduced ESA SAFE annotation containing:

- incidence angle  
- slant range metadata  
- calibration reference keys  
- Doppler coefficients  
- timing information  

Used to test:

- σ⁰ normalization  
- antenna pattern correction  
- geometric dependencies  

---

### 🛰️ `calibration_lut_sample.json`
A **trimmed ESA LUT** containing only a small sample of:

- `angles[]`  
- `gain_values[]`  
- `offset_values[]`  
- full metadata header  

Used to test:

- interpolation  
- gain/offset table handling  
- monotonic angle logic  

---

### 📄 `noise_metadata.json`
Provides radio-frequency noise values for:

- noise-floor subtraction  
- border-noise modeling  
- radiometric sanity checks  

---

## 🔗 4. PROV-O Lineage Handling

Fixtures are treated as **prov:Entity** objects:

```json
{
  "prov:Entity": "s1_radiometric_fixture",
  "kfm:care_label": "CARE-A",
  "kfm:provenance_type": "test-fixture"
}
```

They allow PROV-O chains produced during tests to resolve consistently.

---

## 🧪 5. CI Integration

These fixtures are consumed by:

```
docs/data/satellites/sentinel-1/transforms/radiometric/tests/
```

CI enforces:

- schema correctness  
- numeric consistency  
- deterministic outputs  
- absence of drift in sample LUTs  
- immutability of fixtures  

Any change triggers a governance audit.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | First strict emoji-aligned fixtures README; matches transforms subtree conventions. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

