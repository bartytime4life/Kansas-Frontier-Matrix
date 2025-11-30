---
title: "📁 Sentinel-1 Governance — ETL Fixtures (H3 Masks · Generalization · Sovereignty Metadata)"
path: "docs/data/satellites/sentinel-1/transforms/governance/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High Sensitivity Test Fixtures (CARE-B · Sovereignty-Controlled)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Sovereignty Board · FAIR+CARE Council"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-B"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-governance-fixtures-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Sovereignty Board · Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Instant"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/sentinel1-governance-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-governance-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-governance-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-governance-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/governance/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when sovereignty/H3 policies update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Governance — Fixture Library**  
`docs/data/satellites/sentinel-1/transforms/governance/fixtures/`

Fixtures used to validate the full sovereignty-governed ETL chain:  
**H3 masking**, **generalization**, **uncertainty floors**, **smoothing**,  
and **CARE-B metadata propagation**.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/governance/fixtures/
├── 📄 README.md
│
├── 🛡️ h3_sample_level7.json           # Example H3 sovereignty grid for testing
├── 🌍 generalized_reference.tif        # Reference generalized raster (post-mask + smoothing)
└── 📄 governance_reference.json        # Expected metadata after governance transform
~~~

✔ Emoji BEFORE filenames  
✔ No drift, no missing elements  
✔ Format matches all prior fixtures directories  
✔ Guaranteed box-safe  

---

## 📘 2. Purpose

These fixtures support **deterministic validation** of governance enforcement across  
all Sentinel-1 derivative products (flood, wetlands, deformation, coherence):

- validates correct H3 sovereignty masking  
- validates correct smoothing and kernel application  
- ensures uncertainty floors are applied  
- verifies full `"kfm:*"` metadata propagation  
- ensures outputs match **sovereignty-protected** expectations  
- acts as the baseline for governance CI pipelines  

Governance fixtures form the **final protection layer** before STAC publication.

---

## 🧩 3. Fixture Descriptions

### 🛡️ `h3_sample_level7.json`
Represents a **sovereignty-sensitive H3 grid** (level 7), including:

- sovereign cell IDs  
- H3 boundary metadata  
- expected mask logic  
- protected-zone indicators  

Used to validate masking logic in `test_h3_masking.py`.

---

### 🌍 `generalized_reference.tif`
Reference raster showing the **correct post-governance generalization**:

- H3 masking  
- smoothing kernels  
- uncertainty floors  
- clipped detail in sovereign cells  
- deterministic visual signature applied  

Used by `test_generalization.py`.

---

### 📄 `governance_reference.json`
Expected metadata structure after governance is applied, including:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_generalized"`  
- `"kfm:uncertainty_floor_applied"`  
- `"kfm:governance_notes"`  
- PROV-O lineage fields  
- STAC-ready governance tokens  

Used by `test_governance_metadata.py`.

---

## 🔗 4. PROV-O Lineage

Fixtures are registered as:

~~~json
{
  "prov:Entity": "s1_governance_fixture",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "test-fixture"
}
~~~

This ensures CI can verify lineage correctness for all S1 governed outputs.

---

## 🔐 5. FAIR+CARE & Sovereignty Requirements

Fixtures enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:sovereignty_generalized" = true"`  
- `"kfm:uncertainty_floor_applied" = true"`

Even though they contain **sample/mock** data,  
they must reflect actual sovereignty-governance rules.

---

## 🧪 6. CI Integration

The fixtures are used by:

- `test_h3_masking.py`  
- `test_generalization.py`  
- `test_governance_metadata.py`  

CI verifies:

- correct masking behavior  
- correct generalization logic  
- metadata propagation  
- schema/SHACL validity  
- deterministic pixel behavior  
- no change to sovereignty-protected patterns  

Any mismatch → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, no-drift governance-fixtures README; emoji prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Governance Tests](../tests/README.md) · [🛡️ H3 Masks](../h3_masks/README.md)

</div>

