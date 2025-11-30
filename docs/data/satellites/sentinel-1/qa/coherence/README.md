---
title: "🧪 Sentinel-1 Coherence QA — Temporal Coherence Validation (Window Stats · Pairing · Baseline Health)"
path: "docs/data/satellites/sentinel-1/qa/coherence/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA (CARE-B · Sovereignty-Aware)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sentinel1-coherence-qa-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../schemas/json/sentinel1-coherence-qa-v11.json"
shape_schema_ref: "../../../../schemas/shacl/sentinel1-coherence-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-coherence:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-coherence"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/coherence/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when coherence QA standards update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Coherence QA**  
`docs/data/satellites/sentinel-1/qa/coherence/`

Validates **temporal coherence stability**,  
**master/slave pairing correctness**,  
**window-based coherence math**,  
and **coherence-loss interpretation** for flood, wetlands, and deformation ETL.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/coherence/
├── 📄 README.md
│
├── 🧪 tests/                     # Coherence QA tests
│   ├── 🧪 test_coherence_range.py
│   ├── 🧪 test_pair_baseline.py
│   └── 🧪 test_window_statistics.py
│
└── 📁 fixtures/                  # Reference coherence rasters, metadata, pairing truth
    ├── 🔗 coherence_reference.tif
    ├── 🔗 pair_reference.json
    └── 📄 window_stats_reference.json
~~~

✔ Emoji BEFORE filenames  
✔ Fully consistent with all QA subtree patterns  
✔ 100% box-safe  

---

## 📘 2. Purpose

Coherence QA ensures:

- correct **temporal correlation** behavior  
- valid master/slave **pair metadata**  
- stable coherence **window calculations**  
- low-SNR behavior correctness  
- consistency with deformation + flood + wetlands ETLs  
- preservation of governance metadata  
- reproducibility across architectures  

Coherence QA is essential because decorrelation is used to infer:

- flooding  
- soil saturation  
- surface disturbance  
- ground instability  

All of which may intersect **sovereign hydroscapes** → CARE-B required.

---

## 🧩 3. QA Dimensions

### 🧪 Coherence Range & Validity
Checks:

- output ∈ [0, 1]  
- numeric precision  
- no negative or >1 values  
- correct behavior in uniform/noisy regions  

### 🧪 Pair Baseline Integrity
Ensures:

- correct master < slave ordering  
- appropriate temporal baseline (baseline_days)  
- valid IW-mode selection  
- agreement with upstream `pairs/` metadata  

### 🧪 Window Statistics QA
Validates:

- sliding window behavior (3×3, 5×5)  
- correct correlation numerator/denominator  
- noise-floor and low-coherence thresholds  
- stable behavior in partially coherent regions  

---

## 🔐 4. FAIR+CARE & Sovereignty Integration

Coherence QA enforces:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- correct propagation of sovereignty metadata  
- governance readiness for flood/wetlands/deformation pipelines  

Coherence can inadvertently reveal sensitive change patterns →  
thus governance is mandatory.

---

## 🔗 5. PROV-O Lineage

QA generates lineage describing correctness of coherence calculations:

~~~json
{
  "prov:Entity": "s1_coherence_qa",
  "prov:wasGeneratedBy": "s1_coherence_qa_pipeline",
  "kfm:qa_type": "coherence",
  "kfm:care_label": "CARE-B"
}
~~~

Downstream STAC Items reference this QA lineage.

---

## 🧪 6. CI Integration

CI checks:

- coherence math  
- range validity  
- correct pairing logic  
- stable window statistics  
- governance metadata compliance  
- schema + SHACL conformance  
- deterministic output match with fixtures

Any mismatch → **CI block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict coherence-QA README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](./tests/README.md) · [📁 Fixtures](./fixtures/README.md)

</div>

