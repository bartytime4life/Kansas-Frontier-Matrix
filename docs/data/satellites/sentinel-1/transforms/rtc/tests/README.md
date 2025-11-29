---
title: "🧪 Sentinel-1 RTC — Test Suite Overview (γ⁰ Terrain Correction Validation)"
path: "docs/data/satellites/sentinel-1/transforms/rtc/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Test Suite)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
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

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "Instant"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-rtc-tests:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-rtc-tests"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/rtc/tests/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next RTC model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 RTC — Test Suite**  
`docs/data/satellites/sentinel-1/transforms/rtc/tests/`

Tests that validate **Radiometric Terrain Correction (RTC)** outputs:  
DEM alignment, incidence-angle modeling, γ⁰ correctness, snap-grid projection,  
and reproducible ground geometry across all SAR scenes.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Prefix)

~~~text
docs/data/satellites/sentinel-1/transforms/rtc/tests/
├── 📄 README.md
│
├── 🏞️ test_rtc_core.py           # Core γ⁰ terrain normalization tests
├── 🏞️ test_projection.py         # Grid alignment + projection fidelity
└── 🏞️ test_dem_alignment.py      # DEM-to-burst geometry consistency tests
~~~

✔ Emoji BEFORE filenames  
✔ Exactly matches orbit/tests + radiometric/tests formatting  
✔ Guaranteed box-safe (no broken fences)

---

## 📘 2. Purpose

This test suite ensures RTC transform outputs are:

- geometrically correct  
- radiometrically stable  
- terrain-normalized using correct DEM tiles  
- aligned to the **grid_defs** snap grid  
- reproducible across platforms  
- compliant with STAC + PDC contracts  

All tests validate **γ⁰ VV/VH raster correctness** against reference fixtures.

---

## 🧩 3. Test Modules

### 🏞️ `test_rtc_core.py`
Validates:

- γ⁰ = σ⁰ × cos(θ_local)/cos(θ_incident)  
- correct σ⁰ → γ⁰ conversion  
- terrain normalization accuracy  
- behavior for steep-slope DEM areas  
- deterministic floating-point results  

---

### 🏞️ `test_projection.py`
Ensures:

- orthorectification is correct  
- output matches expected EPSG:32614 projection  
- pixel alignment matches `grid_defs/`  
- correct warp/resample logic  
- no half-pixel drifts or slant-range offsets  

---

### 🏞️ `test_dem_alignment.py`
Checks:

- DEM tile CRS compatibility  
- slope/aspect derivation for incidence angle  
- DEM footprint alignment to burst geometry  
- no NaNs, spikes, voids after clipping  
- consistent DEM-based incidence angle fields  

---

## 🔗 4. Governance & FAIR+CARE Notes

RTC is **CARE-A**, but tests must ensure:

- upstream `"kfm:*"` metadata passes through unmodified  
- PROV-O lineage includes DEM + griddefs inputs  
- all metadata is PDC-compliant  
- reproducibility metadata (energy, carbon) is stable  

No sovereignty masking occurs at this stage.

---

## 🧪 5. CI Integration

These tests run automatically in:

- `transform-tests.yml`  
- `data-pipeline.yml`  
- PR checks involving DEM, radiometric, or RTC logic  

CI enforces:

- deterministic γ⁰ rasters  
- schema + SHACL + STAC alignment  
- no unintended numerical drift  
- all fixture-based raster comparisons pass bit-exact checks  

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting RTC test-suite README; emoji prefix preserved. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

