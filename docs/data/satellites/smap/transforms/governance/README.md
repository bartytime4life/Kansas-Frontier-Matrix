---
title: "🛡️ NASA SMAP — Governance & Sovereignty Masking Stage (CARE/H3 Enforcement) · ETL Stage 6"
path: "docs/data/satellites/smap/transforms/governance/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Sovereignty Working Group"
status: "Active / Enforced"

classification: "Public ETL Governance Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B (High-Sensitivity Stage)"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "FAIR+CARE Council · Sovereignty Working Group · Earth Systems Governance Subcommittee"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-governance-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-governance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:governance-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-governance"
event_source_id: "ledger:docs/data/satellites/smap/transforms/governance/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon new governance policy release"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛡️ **NASA SMAP — Governance & Sovereignty Masking Stage (ETL Stage 6)**  
`docs/data/satellites/smap/transforms/governance/README.md`

**Purpose**  
Define the **governance & sovereignty masking stage** in the SMAP ETL pipeline.  
This step enforces CARE/H3 rules, Indigenous rights safeguards, masking/generalization,  
uncertainty-floor enforcement, and ensures SMAP data is ethically appropriate  
for public release, Focus Mode v3 narratives, and Story Node v3 contexts.

</div>

---

## 📘 1. Overview

The **Governance Stage** is ETL **Stage 6**, applied after:

```
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (this stage)
 → STAC/DCAT metadata
 → PROV-O lineage
 → OpenLineage telemetry
```

This stage ensures:

- 🔐 **Indigenous sovereignty protection via H3 rules**  
- 🛡️ **Ethical spatial generalization / masking**  
- 🧭 **CARE label propagation and enforcement**  
- 📉 **Uncertainty floors enforced in sensitive regions**  
- 📄 **STAC/DCAT governance metadata written**  
- 🧾 **PROV-O governance lineage recorded**  
- ⚠️ **No disallowed precision** enters public layers  
- prevents environmental misinterpretation in cultural landscapes  
- generates *safe-to-expose* versions of SMAP products  
  (soil moisture, freeze–thaw, VWC, QA-derived masks, uncertainty surfaces)

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/governance/
├── 📄 README.md                               # This file
│
├── 🔐 apply_masking.py                        # Applies sovereignty/H3 masking & generalization
├── 🗺️ h3_policy.json                          # H3 sovereignty policy: levels, buffers, exemptions
├── 🧭 care_rules.json                          # CARE metadata rules & edge-case conditions
├── 📉 uncertainty_floor_policy.json           # Region-specific uncertainty floor definitions
│
├── 🧪 tests/                                   # Governance test suite
│   ├── test_masking.py
│   ├── test_h3_propagation.py
│   ├── test_care_preservation.py
│   ├── test_uncertainty_floor.py
│   └── fixtures/
│       ├── sample_pre_mask.tif
│       ├── sample_post_mask_expected.tif
│       ├── synthetic_h3_mask.json
│       ├── governance_metadata_stub.json
│       └── schema_expected.json
~~~

---

## 🧩 3. Responsibilities of the Governance Stage

### 🔐 **Sovereignty Masking (H3-Based)**
- Apply spatial generalization in sensitive H3 regions  
- Replace precise pixels with aggregated/blurred equivalents  
- Enforce `"kfm:mask_required": true` where relevant  
- Guarantee **no precise elevation, biomass, SM, FT, VWC** is exposed where restricted  

### 🧭 **CARE Label Enforcement**
- Maintain CARE labels through all transformations  
- Prevent datasets from “dropping” CARE metadata  
- Add `"kfm:care_label_reason"` for transparency  

### 📉 **Uncertainty Floor Enforcement**
- Guarantee uncertainty never decreases in sensitive places  
- Enforce `"kfm:sovereignty_uncertainty_floor"`  
- Inflate uncertainty where masking occurs  
- Maintain reproducibility across ETL runs  

### 📚 **Metadata & Provenance**
- Add/maintain:
  - `kfm:sovereignty-mask`
  - `kfm:care_label`
  - `kfm:h3_sensitive`
  - `kfm:uncertainty_floor`
  - `kfm:mask_required`  
- Update PROV-O with masking lineage:
  - `prov:wasGeneratedBy`  
  - `prov:used` → h3 policy + care rules  
  - `prov:atLocation`  

### 📦 **STAC / DCAT Integration**
Write governance metadata into:

- STAC Item properties  
- STAC Extensions:
  - `projection`  
  - `raster`  
  - `kfm-governance` extension  
- DCAT Dataset sensitivity descriptors  

### ⚠️ **Integrity & Ethical Safeguards**
This stage:
- prevents unintentional re-identification of sensitive landscapes  
- ensures environmental trends cannot be misinterpreted as precise values in protected lands  
- preserves sovereignty directives for all downstream products  

---

## 🔐 4. Governance & Sovereignty Rules (KFM-GOV v11)

### Mandatory Behaviors  
- No pixel inside sovereign H3 cells may retain raw precision  
- Masked/generalized surfaces MUST replace original values  
- `"kfm:mask_required": true` must propagate to all assets  
- `"kfm:care_label"` must remain consistent  
- Uncertainty floors must apply to all sensitive pixels  
- No STAC or DCAT object may omit governance metadata  

### Forbidden Behaviors  
- Revealing precise geographic detail inside Indigenous lands  
- Decreasing uncertainty in sensitive regions  
- Removing or overriding CARE metadata  
- Producing contradictory governance lineage  

These rules are validated automatically in CI.

---

## 🧪 5. Governance QA & Validation

Test suite validates:

- correct H3 masking  
- uncertainty floor enforcement  
- CARE/H3 preservation  
- CRS/geometry stability  
- correct writing of governance STAC metadata  
- correct PROV-O lineage  
- no STAC schema violations  
- no broken masked tiles  
- no leaking high-resolution signal in protected areas  

QA outputs → `docs/data/satellites/smap/qa/`

Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 6. Governance in the Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (this stage)
 → STAC/DCAT creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Governance produces the **safe-to-publish output** for KFM.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Prevents sensitive wetness/soil-state data exposure  
- Ensures safe floodplain overlays in sovereign lands  

### Climate  
- Protects vegetation/water-cycle signals from misuse  
- Ensures anomaly maps respect sovereignty boundaries  

### Archaeology  
- Prevents environmental reconstructions from revealing sensitive cultural landscapes  

### Story Node v3  
- Produces sovereignty-aware environmental narratives  
- Provides `"Why was this masked?"` explanations  

### Focus Mode v3  
- Uses governance metadata to contextualize environmental evidence  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First complete Governance & Masking README; emoji-rich; CARE/H3 aligned; STAC/DCAT/PROV-O; CI-safe.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛡 Governance Tests](../README.md) · [📘 Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

