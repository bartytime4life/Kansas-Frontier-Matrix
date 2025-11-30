---
title: "📁 Sentinel-1 Flood QA — Fixtures (Flood Mask · DEM Pooling · Classifier Truth)"
path: "docs/data/satellites/sentinel-1/qa/flood/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA Fixtures (CARE-B · Hydrology · Sovereignty-Aware)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-B"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-flood-fixtures-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/sentinel1-flood-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-flood-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-flood-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-flood-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/flood/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when flood QA models update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Flood QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/flood/fixtures/`

Golden-truth, sovereign-safe reference files for validating  
flood detection logic:  
**ratio math**, **hybrid classifier fusion**, and **DEM pooling behavior**.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/flood/fixtures/
├── 📄 README.md
│
├── 🌊 flood_reference.tif              # True flood mask for classifier validation
├── 🏞️ dem_pooling_reference.tif        # Truth DEM-based pooling / low-relief water detection
└── 📄 classifier_reference.json        # Expected classifier outputs, thresholds, and fusion weights
~~~

✔ Emoji BEFORE filenames  
✔ Matches radiometry/fixtures, wetlands/fixtures, coherence/fixtures, deformation/fixtures  
✔ 100% box-safe, no drift  

---

## 📘 2. Purpose

These QA fixtures serve as **deterministic golden standards** for validating:

- ratio-based flood detection  
- hybrid classifier outputs  
- DEM pooling hydrology logic  
- coherence-enhanced flood inference  
- governance metadata propagation  

Flood detection intersects **sovereign hydroscapes**,  
so fixtures follow CARE-B and sovereignty-safe patterns.

---

## 🧩 3. Fixture Descriptions

### 🌊 `flood_reference.tif`
Binary or probability flood mask used to validate:

- classifier decision surfaces  
- VH/VV ratio threshold correctness  
- smoothing behavior  
- floodwater identification accuracy  
- STAC-ready results  

### 🏞️ `dem_pooling_reference.tif`
Reference DEM pooling raster:

- identifies topographic basins  
- highlights likely standing water  
- ensures DEM-aware hydrology logic matches expected behavior  
- supports hydrology QA in `test_dem_pooling.py`

### 📄 `classifier_reference.json`
Expected classifier truth for verifying:

- threshold values  
- fusion weights (ratio, coherence, DEM)  
- correct classifier variant (e.g., `hybrid_model_2025`)  
- deterministic model behavior  
- metadata correctness  

---

## 🔐 4. FAIR+CARE & Sovereignty Integration

Flood fixtures are **CARE-B** and must validate the presence and correctness of:

- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:governance_notes"`  
- `"kfm:care_label": "CARE-B"`  
- sovereign-safe flood inference  
- no leakage of precise hydroscape detail  

Fixtures do **not** contain raw sovereign geometry but drive metadata enforcement.

---

## 🔗 5. PROV-O Lineage

Fixtures attach governance lineage:

~~~json
{
  "prov:Entity": "s1_flood_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

---

## 🧪 6. CI Integration

CI checks:

- ratio correctness  
- classifier correctness  
- DEM pooling correctness  
- deterministic classification  
- metadata integrity  
- schema + SHACL validity  
- bitwise match with fixtures  

Any mismatch → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-29 | Initial strict flood-QA fixtures README; emoji-prefix validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Flood Tests](../tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

