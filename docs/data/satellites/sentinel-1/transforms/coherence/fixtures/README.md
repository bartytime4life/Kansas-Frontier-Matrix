---
title: "📁 Sentinel-1 Coherence — Fixtures (SAFE Subsets · Pair Metadata · Reference Coherence Tiles)"
path: "docs/data/satellites/sentinel-1/transforms/coherence/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Test Fixtures)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council + Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Interval"

json_schema_ref: "../../../../../../schemas/json/sentinel1-coherence-fixtures-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-coherence-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-coherence-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-coherence-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/coherence/fixtures/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded after next ESA coherence reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Coherence — Fixture Library**  
`docs/data/satellites/sentinel-1/transforms/coherence/fixtures/`

Fixtures supporting unit + integration testing for the  
**temporal coherence ETL pipeline**: SAFE subsets, pair metadata samples,  
and reference coherence rasters for bit-exact validation.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/coherence/fixtures/
├── 📄 README.md
│
├── 🛰️ SAFE_annotation_subset.xml     # Reduced SAFE annotation (timing + geometry)
├── 🔗 pair_sample.json               # Minimal master/slave pair metadata
└── 📄 coherence_reference.tif        # Reference coherence magnitude raster (5×5 window)
~~~

✔ Emojis BEFORE filenames  
✔ Exact match to coherence/tests, orbit/fixtures, rtc/fixtures  
✔ Zero drift, zero collapse, zero omissions  
✔ Box-safe (single fence, no internal backticks)

---

## 📘 2. Purpose

These fixtures provide **deterministic inputs** and **known outputs** for verifying  
the Sentinel-1 coherence transform.

Tests rely on these fixtures to validate:

- correct master/slave pairing  
- accurate geometric co-registration  
- correct implementation of the 5×5 coherence window  
- deterministic floating-point behavior  
- correct QA mask logic  
- correct propagation of sovereignty + CARE metadata  

They ensure that coherence generation is **reproducible**, **governed**, and  
**mathematically stable** across updates.

---

## 🧩 3. Fixture Descriptions

### 🛰️ `SAFE_annotation_subset.xml`
A reduced version of an ESA SAFE annotation file.

Contains:

- IW burst timing  
- line/pixel geometry  
- incidence angle fields  
- Doppler coefficients  
- orbit references  

Used to test:

- co-registration  
- geometry consistency  
- timing alignment  

---

### 🔗 `pair_sample.json`
Minimal master/slave pair metadata sample.

Includes:

- master + slave timestamps  
- relative orbit  
- coherence-eligible baseline  
- IW mode constraint  
- sovereign-sensitive flag  

Used to test:

- pairing logic  
- metadata ingestion  
- governance propagation  

---

### 📄 `coherence_reference.tif`
A small (test-scale) coherence magnitude raster.

Used for:

- bit-exact coherence validation  
- sliding-window window correctness  
- QA mask validation  
- downstream flood/wetlands fusion QA tests  

Must match expected values exactly — CI checks bitwise equality.

---

## 🔗 4. PROV-O Lineage

Fixtures participate in test provenance:

~~~json
{
  "prov:Entity": "s1_coherence_fixture",
  "prov:label": "Coherence Test Fixture",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "test-fixture"
}
~~~

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Because coherence inference can reveal disturbance  
and potentially culturally sensitive temporal patterns:

- fixtures carry **CARE-B**  
- `"h3_sensitive": true` propagated  
- `"mask_required": true` verified in tests  
- no geometries present here, but metadata inherits governance flags  

Test logic validates **correct metadata propagation**, not only numeric correctness.

---

## 🧪 6. CI Integration

Used by:

- `test_coherence_core.py`  
- `test_pairing.py`  
- `test_quality_masks.py`

CI enforces:

- deterministic output  
- schema validity  
- correct governance metadata attachment  
- stable reference raster comparisons  
- bit-exact behavior in coherence generation  

Failures → **block merge**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting coherence fixture README; emojis validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

