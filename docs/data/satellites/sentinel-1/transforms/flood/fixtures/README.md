---
title: "📁 Sentinel-1 Flood Mapping — Fixtures (RTC γ⁰ · Coherence · SAFE Subsets · Reference Flood Raster)"
path: "docs/data/satellites/sentinel-1/transforms/flood/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity · Hydrological Test Fixtures (CARE-B)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council + Remote Sensing WG"

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
  owl_time: "Instant"

json_schema_ref: "../../../../../../schemas/json/sentinel1-flood-fixtures-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-flood-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-flood-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-flood-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/flood/fixtures/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded when next flood model or classifier revision occurs"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Flood Mapping — Fixture Library**  
`docs/data/satellites/sentinel-1/transforms/flood/fixtures/`

Reference SAFE subsets, RTC γ⁰ tiles, coherence inputs,  
and **reference flood classification outputs** for validating  
the hydrological flood ETL transform.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/flood/fixtures/
├── 📄 README.md
│
├── 🛰️ SAFE_annotation_subset.xml      # Minimal SAFE annotation for flood ETL tests
├── 🏞️ rtc_gamma0_sample_vv.tif        # RTC-corrected γ⁰ VV raster (input)
├── 🔗 coherence_sample.tif            # Coherence raster (optional fusion input)
└── 🌊 flood_reference.tif             # Reference flood raster for CI bit-exact validation
~~~

✔ Emojis BEFORE filenames  
✔ Exact match to structure of other fixture directories  
✔ No drift, no omissions  
✔ 100% box-safe  

---

## 📘 2. Purpose

These fixtures support **deterministic testing** of the flood-processing ETL pipeline:

- validates VH/VV ratio behavior  
- validates hybrid classifier logic  
- validates coherence-fusion integration  
- ensures governance metadata propagation  
- ensures consistency of terrain-aware flood smoothing  
- enforces sovereignty-sensitive masking (when downstream used)

Flood mapping is **sensitive** because it intersects sovereign hydroscapes,  
traditional waters, and culturally significant wetland zones.

---

## 🧩 3. Fixture Descriptions

### 🛰️ `SAFE_annotation_subset.xml`
Reduced ESA SAFE annotation containing:

- geometry/time metadata  
- incidence angles  
- Doppler coefficients  
- swath/burst characterization  

Used to validate alignment + geometry consistency.

---

### 🏞️ `rtc_gamma0_sample_vv.tif`
Sample **γ⁰ VV** tile produced by RTC stage.

Used for:

- flood ratio calculations  
- terrain-informed flood classification  
- bit-exact reproduction checks  

---

### 🔗 `coherence_sample.tif`
Coherence magnitude raster (sample).

Used to verify:

- hybrid flood classifier  
- disturbance-influenced hydrology detection  
- coherence → flood fusion pipeline behavior  

---

### 🌊 `flood_reference.tif`
Reference water-mask raster.

Used for verifying:

- classifier threshold logic  
- hybrid model consistency  
- DEM-aware pooling logic  
- correct QA mask outputs  
- deterministic flood inference behavior  
- hydrology-sensitive governance metadata  

All flood ETL outputs MUST match this reference file in CI.

---

## 🔗 4. PROV-O Lineage

Fixtures are registered as:

~~~json
{
  "prov:Entity": "s1_flood_fixture",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "test-fixture"
}
~~~

This ensures reproducibility, lineage integrity, and auditability.

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Flood mapping interacts with:

- sovereign water bodies  
- wetlands tied to tribal ecological knowledge  
- hydrological hazard overlays  

Thus:

- `"kfm:care_label" = "CARE-B"`
- `"kfm:h3_sensitive" = true"`
- `"kfm:mask_required" = true"`

Fixtures do **not** contain full-resolution sensitive geometry,  
but test sovereign-governance metadata propagation.

---

## 🧪 6. CI Integration

CI uses these fixtures to verify:

- flood classification correctness  
- hybrid classifier consistency  
- determinism of VH/VV ratio logic  
- correct governance metadata  
- schema + SHACL compliance  
- reproducibility across platforms  
- accurate fusion with coherence inputs  

Any mismatch triggers **instant ETL block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting flood fixtures README; emoji-prefix alignment maintained. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Flood Tests](../tests/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

