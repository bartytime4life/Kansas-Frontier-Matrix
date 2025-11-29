---
title: "🔗 Sentinel-1 Coherence — ETL Transform (Master/Slave Pairs · Coherence Magnitude · Disturbance Detection)"
path: "docs/data/satellites/sentinel-1/transforms/coherence/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (SAR Derivative)"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-coherence-transform-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:Feature"
  owl_time: "Interval"

json_schema_ref: "../../../../../schemas/json/sentinel1-coherence-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-coherence-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-coherence:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-coherence"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/coherence/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded when ESA coherence model updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Sentinel-1 Coherence Transform**  
`docs/data/satellites/sentinel-1/transforms/coherence/`

Computes **temporal coherence** between Sentinel-1 master/slave acquisitions.  
Critical for detecting **disturbance**, **flood damage**, **agricultural activity**,  
and **land-change signals** in KFM.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/coherence/
├── 📄 README.md
│
├── 🔗 pairs/                     # Master/slave selection, pair metadata
│   ├── 🔗 pair_index.json
│   └── 🔗 iw_pairs_2025.json
│
├── 🧪 tests/                     # Unit + integration tests
│   ├── 🔗 test_coherence_core.py
│   ├── 🔗 test_pairing.py
│   └── 🔗 test_quality_masks.py
│
└── 📁 fixtures/                  # SAFE subsets, pair metadata, reference coherence rasters
    ├── 🛰️ SAFE_annotation_subset.xml
    ├── 🔗 pair_sample.json
    └── 📄 coherence_reference.tif
~~~

✔ Emoji BEFORE every directory and file  
✔ Exact pattern as orbit/, radiometric/, rtc/  
✔ No missing directories from the screenshot  
✔ 100% box-safe

---

## 📘 2. Purpose

This transform computes **coherence magnitude** between two Sentinel-1 SAR acquisitions:

- reveals disturbance from storms/tornadoes  
- identifies flood damage footprints  
- detects agricultural tillage/harvest cycles  
- tracks ecological or land-cover transitions  
- supports deformation masking  
- informs wetlands/saturation models  

Coherence is **sensitive** → requires **CARE-B** + sovereignty masking in downstream STAC products.

---

## 🧩 3. Inputs & Outputs

### Inputs

- master/slave SAR acquisitions  
- calibrated σ⁰ (from radiometric stage)  
- orbit metadata  
- SAFE annotation  
- sample spacing, burst timings  
- pair-selection metadata (`pairs/`)  

### Outputs

- coherence raster (`coherence.tif`)  
- coherence QA mask  
- metadata block:

~~~json
{
  "coherence": {
    "window": "5x5",
    "pair_type": "IW",
    "master": "2025-01-01T12:00:00Z",
    "slave": "2025-01-13T12:00:00Z",
    "validity": "pair"
  }
}
~~~

Outputs feed:  
- flood damage layers  
- wetlands inference  
- disturbance Story Nodes  
- deformation QA (wrapped/unwrapped consistency)

---

## 🧬 4. Processing Steps

### 1️⃣ Master/Slave Pair Selection  
From `pairs/`:

- temporal baseline checking  
- spatial-consistency filtering  
- mode validation (IW only in KFM)  

### 2️⃣ Co-Registration  
- geometric alignment  
- azimuth/range timing sync  
- orbit-driven adjustments  

### 3️⃣ Coherence Calculation  
Sliding-window magnitude:

~~~text
coh = |Σ (m * conj(s))| / sqrt( Σ|m|² · Σ|s|² )
~~~

### 4️⃣ Filtering  
- speckle suppression  
- coherence floor masking  
- optional anisotropic smoothing  

### 5️⃣ Sovereignty-Aware Generalization  
Applied in **downstream STAC layer**,  
but coherence metadata must preserve upstream governance (`CARE-B`, `h3_sensitive` etc.).

### 6️⃣ Metadata + PROV  
- pair metadata  
- window size  
- timing baseline  
- orbit lineage  

---

## 🔗 5. PROV-O Lineage

Coherence emits:

~~~json
{
  "prov:Activity": "s1_coherence_generation",
  "prov:used": ["sigma0_vv", "sigma0_vh", "orbit_metadata", "pair_metadata"],
  "prov:generated": ["coherence_raster"],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
~~~

Downstream STAC items include this lineage.

---

## 🔐 6. FAIR+CARE & Sovereignty Enforcement

Coherence is **high-risk** because it reveals:

- disturbance  
- damage footprints  
- agricultural transitions  
- ecological changes  

Thus:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- sovereignty H3 generalization applied in **STAC items** (not here)  

Transform must:
- propagate governance metadata  
- never strip upstream sovereignty labels  
- record sensitive areas in lineage  

---

## 🧪 7. CI Test Requirements

CI checks:

- correctness of coherence math  
- correct master/slave metadata use  
- pair selection logic  
- deterministic outputs across runs  
- QA mask integrity  
- schema + PDC compliance  
- correct behavior in low-signal regions  

Fixtures in `fixtures/` provide reference rasters and metadata.

---

## 🧭 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting coherence transform README; full emoji compliance. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Coherence Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md)

</div>

