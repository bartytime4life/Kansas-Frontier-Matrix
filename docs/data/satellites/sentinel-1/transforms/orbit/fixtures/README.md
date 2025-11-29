---
title: "📁 Sentinel-1 Orbit Fixtures — SAFE Orbit Files & Test Metadata"
path: "docs/data/satellites/sentinel-1/transforms/orbit/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Test Fixtures)"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG"

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

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing WG"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Instant"

json_schema_ref: "../../../../../../schemas/json/sentinel1-orbit-fixtures-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-orbit-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-orbit-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-orbit-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/orbit/fixtures/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next orbit-file schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Orbit Correction Fixtures**  
`docs/data/satellites/sentinel-1/transforms/orbit/fixtures/`

Reference SAFE orbit files, RESORB/POEORB samples, and burst-timing metadata  
used in orbit-correction ETL tests for KFM v11.

</div>

---

## 🗂️ Directory Layout (STRICT OPTION-A — EXACT STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/orbit/fixtures/
├── 📄 README.md
│
├── 🛰️ S1A_OPER_AUX_RESORB.xml           # Resituted orbit file (test copy)
├── 🛰️ S1A_OPER_AUX_POEORB.xml           # Precise orbit file (test copy)
│
└── 📄 burst_metadata.json               # Simplified SAFE annotation for burst timing tests
~~~

✔ **Emoji BEFORE file name**  
✔ **No comments after file names**  
✔ **No emoji drift**  
✔ **Matches transforms/orbit/tests README style exactly**

---

## 📘 1. Purpose

This directory supplies **controlled test fixtures** for validating the orbit-correction transform.

Fixtures mimic the structure of ESA SAFE AUX files and include:

- RESTITUTED (RESORB) orbit example  
- PRECISE (POEORB) orbit example  
- Simplified annotation file for burst timing + Doppler tests

They allow deterministic, schema-aligned tests across:

- state vector interpolation  
- Doppler centroid evaluation  
- orbit validity window alignment  
- SAFE metadata clock consistency  
- burst timing logic for IW mode  

---

## 🛰️ 2. Fixture Descriptions

### 🛰️ `S1A_OPER_AUX_RESORB.xml`
- ESA restituted orbit file  
- Medium-accuracy state vectors  
- Used for fallback logic in transform tests  

### 🛰️ `S1A_OPER_AUX_POEORB.xml`
- ESA precise orbit file  
- High-accuracy orbit data  
- Expected to be preferred by transform logic  

### 📄 `burst_metadata.json`
Contains reduced SAFE annotation:

```json
{
  "burst_id": "IW1",
  "sensing_start": "2025-01-01T12:00:00Z",
  "sensing_stop": "2025-01-01T12:00:06Z",
  "lines_per_burst": 2500,
  "doppler_coefficients": [1200.1, -3.4, 0.02]
}
```

Used for:

- IW burst alignment tests  
- Doppler polynomial tests  
- timing-boundary validation  

---

## 🧪 3. Test Integration

These fixtures are consumed by:

```
docs/data/satellites/sentinel-1/transforms/orbit/tests/
```

CI ensures:

- fixtures resolve to expected schema  
- orbit files integrate cleanly with SAFE mocks  
- interpolation results are deterministic  
- Doppler centroid math produces bit-exact floats  
- no drift in test sample data  

---

## 🔗 4. Governance & FAIR+CARE

Orbit-level fixtures are **non-sensitive** (CARE-A),  
but metadata must still maintain:

- provenance traceability  
- immutable test design  
- KFM FAIR consistency  

No sovereignty masking applies here.

---

## 🧭 5. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict emoji-aligned fixtures README; no drift; matches transforms/orbit/tests layout. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

