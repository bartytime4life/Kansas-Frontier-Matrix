---
title: "📁 Sentinel-1 QA Fixtures — Deformation (IFG · Unwrapped · LOS Generalized)"
path: "docs/data/satellites/sentinel-1/qa/fixtures/deformation/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High-Sensitivity QA Fixtures (CARE-B · InSAR · Sovereignty-Controlled)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · Remote Sensing WG · Sovereignty Board · FAIR+CARE Council"
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
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-deformation-fixtures-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../s​​​tandards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group · Sovereignty Board"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Interval"

json_schema_ref: "../../../../../schemas/json/sentinel1-deformation-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-deformation-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-fixtures-deformation:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-fixtures-deformation"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/fixtures/deformation/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next deformation QA / InSAR ETL revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Deformation QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/fixtures/deformation/`

Golden-reference datasets for validating the  
**InSAR deformation chain**:  
wrapped interferograms → unwrapped phase → sovereignty-generalized LOS displacement.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/fixtures/deformation/
├── 📄 README.md
│
├── 🛰️ ifg_reference.tif                   # Wrapped interferogram truth (phase ∈ [−π, +π])
├── 🌍 unwrapped_reference.tif             # Continuous unwrapped-phase reference
└── 🌍 los_reference_generalized.tif       # Sovereignty-generalized LOS displacement reference
~~~

✔ Emoji BEFORE filenames  
✔ Perfect alignment with radiometry/coherence/flood/wetlands fixtures  
✔ No drift, 100% box-safe  

---

## 📘 2. Purpose

These fixtures define the **canonical truth outputs** that the deformation QA suite  
compares all ETL results against.

They verify:

- IFG generation  
- unwrapping continuity  
- LOS projection correctness  
- sovereignty-generalization readiness  
- `"kfm:*"` metadata correctness  
- deterministic cross-platform results (CPU/GPU parity)

Deformation layers are considered *high-risk* because displacement patterns may  
reveal culturally sensitive or sovereign ecological conditions.

---

## 🧩 3. Fixture Descriptions

### 🛰️ `ifg_reference.tif`
Validates:

- complex conjugate multiplication for IFG  
- wrapped-phase domain correctness  
- burst alignment/misorbit issues  
- decorrelation handling  

Used in: `test_ifg_quality.py`.

---

### 🌍 `unwrapped_reference.tif`
Validates:

- branch-cut unwrapping  
- correct removal of residues  
- smooth continuous phase  
- DEM-aligned phase gradients  

Used in: `test_unwrapping_continuity.py`.

---

### 🌍 `los_reference_generalized.tif`
Reference **sovereignty-generalized LOS** displacement used to test:

- LOS vector math  
- incidence-angle integration  
- sign conventions  
- readiness for H3 masking  
- uncertainty-floor propagation  
- sovereignty-generalized spatial patterns  

Used in: `test_los_projection.py`.

---

## 🔐 4. FAIR+CARE & Sovereignty Requirements

Fixtures must enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- required `"kfm:governance_notes"`  
- downstream generalization readiness  

Fixtures **never** include raw sovereign geometries;  
they contain already-safe, generalized displacement examples.

---

## 🔗 5. PROV-O Lineage

Fixtures register with:

~~~json
{
  "prov:Entity": "s1_deformation_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

Providing reproducible provenance for all deformation QA and ETL runs.

---

## 🧪 6. CI Integration

CI verifies:

- bitwise match to golden IFG/unwrap/LOS files  
- metadata correctness  
- schema + SHACL conformance  
- deterministic behavior  
- correct sovereignty flag propagation  

Any mismatch → **CI BLOCK**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict deformation QA fixture README; emoji alignment verified; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Deformation Tests](../../deformation/tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

