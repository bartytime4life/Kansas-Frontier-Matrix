---
title: "📁 Sentinel-1 QA Fixtures — Flood (Flood Mask · DEM Pooling · Hybrid Classifier Truth)"
path: "docs/data/satellites/sentinel-1/qa/fixtures/flood/README.md"
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
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-flood-fixtures-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-fixtures-flood:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-fixtures-flood"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/fixtures/flood/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded when flood QA standards or classifier models update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Flood QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/fixtures/flood/`

Deterministic golden-truth datasets for validating **VH/VV ratio**,  
**hybrid flood classifier**, and **DEM pooling hydrology** in governed flood ETL.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Pattern)

~~~text
docs/data/satellites/sentinel-1/qa/fixtures/flood/
├── 📄 README.md
│
├── 🌊 flood_reference.tif              # Ground-truth flood mask (probability or binary)
├── 🏞️ dem_pooling_reference.tif        # True hydrologic pooling / low-relief accumulation
└── 📄 classifier_reference.json        # Hybrid model truth thresholds + fusion weights
~~~

✔ Emojis BEFORE filenames  
✔ Fully matches wetlands/fixtures, coherence/fixtures, deformation/fixtures  
✔ Zero drift, box-safe  

---

## 📘 2. Purpose

These fixtures verify the **flood inference chain**:

- VH/VV ratio flood detection  
- hybrid classifier (ratio + coherence + DEM)  
- DEM pooling / basin detection  
- governance metadata propagation  
- deterministic behavior across platforms  
- proper STAC-ready flood mask generation  

Because flood layers overlap **sovereign waters**, **wetlands**, and  
**culturally sensitive hydroscapes**, the QA fixtures enforce CARE-B rules.

---

## 🧩 3. Fixture Descriptions

### 🌊 `flood_reference.tif`
Used to validate:

- ratio-based flood detection behavior  
- classifier decision surfaces  
- smoothing consistency  
- correct separation of wet vs dry pixels  
- stable hydrology-aware inferences  

### 🏞️ `dem_pooling_reference.tif`
Validates:

- DEM-dependent basin pooling  
- slope/aspect-influenced pooling logic  
- relationship between terrain and inundation  
- correctness for hydrological flood zones  

### 📄 `classifier_reference.json`
Defines:

- hybrid classifier thresholds  
- fusion weights  
- which classifier model variant is expected  
- sovereignty-safe metadata format  
- comparison baseline for `test_hybrid_classifier.py`

---

## 🔐 4. FAIR+CARE & Sovereignty Rules

Fixtures enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- correct `"kfm:governance_notes"`  
- **no raw sovereign geometries stored**  
- readiness for STAC-level masking & generalization  

Flood outputs can reveal sovereign hydroscapes → strict rules apply.

---

## 🔗 5. PROV-O Lineage

Fixtures register as:

~~~json
{
  "prov:Entity": "s1_flood_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

Downstream QA and ETL attach this lineage when validating flood products.

---

## 🧪 6. CI Integration

CI enforces:

- VH/VV ratio threshold correctness  
- classifier equivalence to truth models  
- DEM pooling equivalence  
- schema/SHACL conformance  
- reproducibility across CPU/GPU  
- governance metadata integrity  
- pixel-perfect match with all fixtures  

Any mismatch → **CI BLOCK**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict flood-QA fixture README; emoji alignment verified. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Flood Tests](../../flood/tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

