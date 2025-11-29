---
title: "🔗 Sentinel-1 Coherence — Master/Slave Pair Definitions (IW Mode · Temporal Baselines · Pair Index)"
path: "docs/data/satellites/sentinel-1/transforms/coherence/pairs/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Pair-Selection Metadata)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Oversight"

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

fair_category: "F2-A1-I2-R3"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
risk_category: "Medium–High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/sentinel1-coherence-pairs-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-coherence-pairs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-coherence-pairs:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-coherence-pairs"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/coherence/pairs/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded when ESA pair-selection rules update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Coherence Pair Metadata Directory**  
`docs/data/satellites/sentinel-1/transforms/coherence/pairs/`

Defines **master/slave SAR acquisition pairs** used for  
Sentinel-1 temporal coherence generation in KFM.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/coherence/pairs/
├── 📄 README.md
│
├── 🔗 pair_index.json           # Global index of all coherence-eligible S1 pairs
└── 🔗 iw_pairs_2025.json        # IW-mode pair listing for 2025 (KFM region only)
~~~

✔ Emoji BEFORE filenames  
✔ Matches transforms/coherence/, transforms/rtc/, transforms/orbit formatting  
✔ Box-safe, no broken fences  

---

## 📘 2. Purpose

Coherence requires **two acquisitions** of the same area:

- **Master** (older acquisition)  
- **Slave** (newer acquisition)

This directory contains the **pair-selector metadata** used by the  
Sentinel-1 coherence ETL transform to determine valid pair candidates.

Pairs are filtered based on:

- acquisition mode: **IW-only**  
- baseline interval  
- geometric consistency  
- orbit and timing compatibility  
- instrument/polarization match  
- ESA quality flags  
- cloud-based operational completeness (if downstream fusion used)  

These JSON files are **inputs**, not computed outputs.

---

## 🧩 3. File Definitions

### 🔗 `pair_index.json`
Global list of all candidate pairs (multi-year):

- acquisition IDs  
- master/slave timestamps  
- relative orbit  
- IW swath  
- temporal baseline (days)  
- geometric viability  
- ESA quality flags  
- sovereign-mask flags (detected from footprints)

Example structure:

~~~json
{
  "pairs": [
    {
      "master": "2025-01-01T12:00:00Z",
      "slave": "2025-01-13T12:00:00Z",
      "relative_orbit": 50,
      "mode": "IW",
      "baseline_days": 12,
      "sovereignty_sensitive": true
    }
  ]
}
~~~

---

### 🔗 `iw_pairs_2025.json`
IW-specific pair metadata for coherence processing in **the current year**.

Contains only:

- IW-mode  
- valid baselines  
- KFM AOI footprints  
- pre-screened by footprint geometry  

This keeps annual coherence processing efficient.

---

## 🧬 4. Coherence Transform Usage

Pair metadata is consumed by:

```
transforms/coherence/
  ↳ test_coherence_core.py
  ↳ coherence generation engine
  ↳ STAC deformation QA (indirect)
  ↳ flood/wetlands disturbance-fusion
```

At runtime:

1. Filter pairs by:
   - IW mode  
   - valid temporal baseline  
   - scene availability  
   - sovereign footprint  
2. Pass selected pair to coherence core:
   - co-registration  
   - correlation windowing  
   - coherence magnitude generation  

---

## 🔐 5. FAIR+CARE & Sovereignty Rules

Coherence pairs can reveal:

- disturbance cycles  
- human activity timelines  
- culturally sensitive change patterns  

Thus:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- `"kfm:sovereignty_uncertainty_floor"` added downstream  
- upstream metadata MUST NOT be stripped  

Pair files themselves do **NOT** contain geometries,  
but contain **timing + scene IDs**, which require **CARE-B handling**.

---

## 🧪 6. CI Validation

CI ensures:

- schema compliance  
- valid timestamps  
- correct master < slave ordering  
- baseline sanity  
- IW-only enforcement  
- no missing required fields  
- deterministic ordering  
- proper governance metadata  

Any failure → CI block.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, no-drift coherence pair metadata README; full emoji alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md)

</div>

