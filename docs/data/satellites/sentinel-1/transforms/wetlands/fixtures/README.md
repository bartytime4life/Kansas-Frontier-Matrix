---
title: "📁 Sentinel-1 Wetlands — ETL Fixtures (RTC γ⁰ · Coherence · Seasonal Summary · Reference Wetlands Mask)"
path: "docs/data/satellites/sentinel-1/transforms/wetlands/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity Test Fixtures (CARE-B)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
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
  owl_time: "Instant"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/sentinel1-wetlands-fixtures-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-wetlands-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-wetlands-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-wetlands-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/wetlands/fixtures/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded after next wetlands-model version"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Wetlands — Fixture Library**  
`docs/data/satellites/sentinel-1/transforms/wetlands/fixtures/`

Reference SAFE subsets, RTC γ⁰ tiles, coherence examples,  
and **ground-truth–aligned wetlands masks** used to validate  
the wetlands ETL transform.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/wetlands/fixtures/
├── 📄 README.md
│
├── 🛰️ SAFE_annotation_subset.xml      # Reduced SAFE annotation for wetlands tests
├── 🏞️ rtc_gamma0_sample_vv.tif        # RTC gamma0 VV tile (hydrology-corrected input)
├── 🔗 coherence_sample.tif            # Coherence magnitude sample tile
└── 🌿 wetlands_reference.tif          # Reference wetlands mask (probability or binary)
~~~

✔ Emoji BEFORE filenames  
✔ Format matches flood/fixtures, deformation/fixtures, rtc/fixtures, etc.  
✔ 100% box-safe  

---

## 📘 2. Purpose

These fixtures provide deterministic inputs for wetlands ETL testing:

- validate γ⁰ depression models  
- verify seasonal hydrology adjustments  
- test soil-saturation logic  
- verify coherence-fusion behavior  
- ensure sovereignty-ready handling  
- guarantee reproducibility of wetlands classification  

Wetlands mapping is **sensitive** due to eco-cultural, tribal,  
and hydrological importance → **CARE-B** governance applies.

---

## 🧩 3. Fixture Descriptions

### 🛰️ `SAFE_annotation_subset.xml`
Reduced ESA SAFE annotation including:

- incidence angle  
- slant-range geometry  
- timing metadata  
- DEM alignment cues  
- Doppler coefficients  

Used for verifying geometry consistency.

---

### 🏞️ `rtc_gamma0_sample_vv.tif`
Sample terrain-corrected **γ⁰ VV** raster.

Used to validate:

- wetness / saturation signature detection  
- seasonal-model behavior  
- DEM pooling interactions  
- γ⁰ depression thresholds  

---

### 🔗 `coherence_sample.tif`
Reference coherence raster for wetlands ETL.

Used to test:

- decorrelation-based wetness detection  
- coherence fusion with γ⁰  
- distinction from flood decorrelation patterns  
- seasonal noise-floor logic  

---

### 🌿 `wetlands_reference.tif`
Ground-truth aligned reference raster.

Used for:

- overall wetlands classification correctness  
- probability surface comparison  
- QA mask validation  
- sovereignty-generalization sanity checks  
- consistency across seasonal conditions  

---

## 🔗 4. PROV-O Lineage

Fixtures are registered as:

~~~json
{
  "prov:Entity": "s1_wetlands_fixture",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "test-fixture"
}
~~~

Ensures reproducible test lineage and governance audit compatibility.

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Wetlands outputs intersect:

- tribal ecological knowledge areas  
- sensitive riparian zones  
- cultural hydroscapes  

Therefore fixtures enforce:

- `"kfm:care_label": "CARE-B"`  
- `"kfm:h3_sensitive": true`  
- `"kfm:mask_required": true`  

Although fixtures do NOT contain raw sovereign geometries,  
metadata ensures masking is correctly triggered downstream.

---

## 🧪 6. CI Integration

CI ensures:

- correct wetlands classification output  
- valid seasonal-model integration  
- correct coherence fusion thresholds  
- deterministic γ⁰ wetness behavior  
- governance metadata propagation  
- schema + SHACL compliance  
- raster equivalence to `wetlands_reference.tif`  

Any mismatch → **merge blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict wetlands fixture README; emoji prefixes and layout validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Wetlands Tests](../tests/README.md) · [🌿 Seasonal Models](../seasonal_models/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

