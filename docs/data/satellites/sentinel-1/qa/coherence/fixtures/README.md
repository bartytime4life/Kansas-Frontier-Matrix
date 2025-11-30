---
title: "📁 Sentinel-1 Coherence QA — Fixtures (Coherence Reference · Pair Baseline Truth · Window Stats)"
path: "docs/data/satellites/sentinel-1/qa/coherence/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA Fixtures (CARE-B · Sovereignty-Aware)"
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
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-coherence-fixtures-v11.json"

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
  geosparql: "geo:FeatureCollection"
  owl_time: "Interval"

json_schema_ref: "../../../../../schemas/json/sentinel1-coherence-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-coherence-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-coherence-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-coherence-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/coherence/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next coherence QA update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Coherence QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/coherence/fixtures/`

Reference coherence outputs, pair metadata, and window-statistics truth files for  
verifying deterministic coherence calculations in the QA pipeline.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/coherence/fixtures/
├── 📄 README.md
│
├── 🔗 coherence_reference.tif        # Reference coherence magnitude field
├── 🔗 pair_reference.json            # Expected master/slave + temporal baseline metadata
└── 📄 window_stats_reference.json    # Reference window-statistics truth (3x3 / 5x5)
~~~

✔ Emoji BEFORE filenames  
✔ Directory pattern consistent with all QA fixture blocks  
✔ Zero drift, fully box-safe  

---

## 📘 2. Purpose

These fixtures provide the **ground-truth values** required to validate:

- coherence magnitude math  
- allowable value range (0–1)  
- master/slave temporal-baseline rules  
- sliding-window correlation statistics  
- noise-floor handling  
- sovereignty metadata propagation  
- numerical determinism across CPU/GPU architectures  

They ensure all coherence-dependent products—  
**flood**, **wetlands**, **deformation**, **disturbance**—  
rest on validated foundations.

---

## 🧩 3. Fixture Descriptions

### 🔗 `coherence_reference.tif`
Reference coherence raster used to validate:

- sliding-window numerator/denominator structures  
- low-SNR behavior  
- correct complex-phase correlation reduction  
- no invalid values (<0 or >1)  
- reproducibility  

### 🔗 `pair_reference.json`
Truth metadata defining:

- master acquisition timestamp  
- slave acquisition timestamp  
- `baseline_days`  
- IW mode  
- sovereign sensitivity inheritance  
- expected `"kfm:*"` fields  

Used to test pair-baseline integrity and upstream metadata ingestion.

### 📄 `window_stats_reference.json`
Truth dataset for window-based coherence QA:

- 3×3 coherence window stats  
- 5×5 coherence window stats  
- reference numerator/denominator breakdowns  
- expected low-SNR window edge cases  

Used by `test_window_statistics.py`.

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

Coherence data is **CARE-B** when used in hydrology or disturbance analysis.

Fixtures must reflect:

- `"kfm:care_label": "CARE-B"`  
- `"kfm:h3_sensitive": true"`  
- `"kfm:mask_required": true"`  
- `"kfm:sovereignty_generalized"` applied in transforms downstream  
- no full-resolution sovereign geometry leakage  

---

## 🔗 5. PROV-O Lineage

Fixtures register as:

~~~json
{
  "prov:Entity": "s1_coherence_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

Downstream QA lineage attaches this fixture metadata to every coherence QA run.

---

## 🧪 6. CI Integration

CI ensures:

- perfect match to reference coherence values  
- correct pair-baseline metadata  
- stable window-statistics outputs  
- no numeric drift  
- schema compliance  
- full `"kfm:*"` metadata propagation  

Any mismatch → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict coherence-QA fixtures README; verified zero drift + emoji alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Coherence Tests](../tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

