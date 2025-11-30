---
title: "📁 Sentinel-1 QA Fixtures — Coherence (Magnitude · Pair Baseline · Window Statistics)"
path: "docs/data/satellites/sentinel-1/qa/fixtures/coherence/README.md"
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

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-coherence-fixtures-v11.json"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium-High"
public_exposure_risk: "Medium"
risk_category: "High"
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

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-fixtures-coherence:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-fixtures-coherence"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/fixtures/coherence/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next coherence QA update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Coherence QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/fixtures/coherence/`

Authoritative reference datasets for validating **temporal coherence**,  
**pair baselines**, and **window-statistics behavior** in the Sentinel-1  
coherence QA and ETL pipelines.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/fixtures/coherence/
├── 📄 README.md
│
├── 🔗 coherence_reference.tif        # Coherence magnitude truth raster (0–1)
├── 🔗 pair_reference.json            # Expected master/slave + baseline_days metadata
└── 📄 window_stats_reference.json    # Sliding-window coherence statistics (3×3 / 5×5)
~~~

✔ Emoji BEFORE filenames  
✔ Fully consistent with coherence/tests + master QA fixtures  
✔ Box-safe, zero drift  

---

## 📘 2. Purpose

These fixtures are the **golden references** for verifying:

- coherence magnitude computation  
- value-range validity (0 ≤ coherence ≤ 1)  
- correct processing of low-SNR regions  
- correct IW-mode master/slave pairing  
- proper temporal-baseline (baseline_days) logic  
- correct sliding-window coherence math (3×3, 5×5)  
- numerical determinism across CPU/GPU architectures  
- sovereignty-safe metadata propagation  

Coherence is fundamental to:

- flood damage detection  
- wetlands saturation modeling  
- deformation stability checks  
- disturbance mapping  

Thus accurate coherence QA is essential.

---

## 🧩 3. Fixture Descriptions

### 🔗 `coherence_reference.tif`
Validates:

- reference coherence calculated with correct correlation numerator/denominator  
- no values < 0 or > 1  
- correct performance in decorrelated areas  
- stable pixel-wise behavior across platforms  
- consistency with upstream RTC & radiometry layers  

Used by `test_coherence_range.py`.

---

### 🔗 `pair_reference.json`
Contains truth metadata for:

- master timestamp  
- slave timestamp  
- `baseline_days` (temporal separation)  
- IW mode  
- sovereign-sensitivity inheritance (`h3_sensitive`, `mask_required`)  
- expected `"kfm:*"` metadata  

Used by `test_pair_baseline.py`.

---

### 📄 `window_stats_reference.json`
Reference dataset for verifying:

- sliding-window coherence aggregate behavior  
- 3×3 and 5×5 window ranges  
- edge-case behavior in low-SNR tiles  
- expected numerator/denominator values  

Used by `test_window_statistics.py`.

---

## 🔐 4. FAIR+CARE & Sovereignty Requirements

Although coherence is a *derived product*, it may expose sensitive patterns  
in sovereign or culturally meaningful landscapes.  
Fixtures therefore require:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:sovereignty_generalized"` applied downstream  
- strict metadata propagation  

No raw sovereign geometry is stored in fixtures; only sovereignty-safe metadata.

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

This ensures correct lineage across all coherence QA + ETL stages.

---

## 🧪 6. CI Integration

CI enforces:

- coherence magnitude correctness  
- pair-baseline truth matching  
- window-statistics identity  
- schema/SHACL compliance  
- governance metadata integrity  
- deterministic CPU/GPU behavior  

Any mismatch → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict coherence QA fixture README; emoji alignment verified; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Coherence Tests](../../coherence/tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

