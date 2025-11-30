---
title: "📁 Sentinel-1 Deformation QA — Fixtures (IFG · Unwrapped · Sovereignty-Generalized LOS)"
path: "docs/data/satellites/sentinel-1/qa/deformation/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High Sensitivity QA Fixtures (CARE-B · InSAR · Sovereignty-Controlled)"
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

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "High"
risk_category: "Very High"
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

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-deformation-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-deformation-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/deformation/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded after next InSAR QA/ETL revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Deformation QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/deformation/fixtures/`

Golden-truth reference files used to validate the  
**InSAR deformation pipeline**:  
wrapped interferograms → unwrapped phase → sovereignty-generalized LOS.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/deformation/fixtures/
├── 📄 README.md
│
├── 🛰️ ifg_reference.tif                   # Reference wrapped interferogram (phase ∈ [−π, +π])
├── 🌍 unwrapped_reference.tif             # Reference unwrapped phase (continuous surface)
└── 🌍 los_reference_generalized.tif       # Reference sovereignty-generalized LOS displacement
~~~

✔ Emoji BEFORE filenames  
✔ Fully consistent with deformation/tests, governance/fixtures, coherence/fixtures  
✔ Zero drift  
✔ 100% box-safe  

---

## 📘 2. Purpose

These fixtures represent the **canonical, deterministic outputs**  
against which all deformation QA computations are validated:

- wrapped interferogram generation (IFG)  
- phase unwrapping (branch-cut)  
- LOS displacement projection  
- sovereignty-generalization readiness  
- metadata and governance inheritance  

They ensure the deformation pipeline is safe, reproducible, and compliant with  
InSAR physics, sovereignty rules, and CARE-B requirements.

---

## 🧩 3. Fixture Descriptions

### 🛰️ `ifg_reference.tif`
Provides the golden wrapped-phase map used to validate:

- correct complex interferogram generation  
- orbit timing alignment  
- burst overlap consistency  
- wrapped phase domain clipping [−π, +π]  
- sensitivity to decorrelation and noise  

Used in `test_ifg_quality.py`.

---

### 🌍 `unwrapped_reference.tif`
Ground-truth continuous phase surface verifying:

- branch-cut unwrapping correctness  
- residue detection  
- absence of rewrap defects  
- DEM geometry-consistent phase gradients  

Used in `test_unwrapping_continuity.py`.

---

### 🌍 `los_reference_generalized.tif`
Reference **sovereignty-generalized** LOS displacement map verifying:

- look-vector math  
- incidence-angle handling  
- LOS direction + sign convention  
- H3-level generalization logic  
- uncertainty-floor preparation  
- sovereignty-safe displacement fields  

Used in `test_los_projection.py`.

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

Because deformation intersects:

- sovereign lands  
- cultural landscapes  
- hydrologic drawdown  
- environmentally sensitive subsidence zones  

fixtures must enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- correct `"kfm:governance_notes"`  
- readiness for generalization in ETL  

Fixtures DO NOT contain raw sovereign geometry,  
but validate **metadata and generalization readiness**.

---

## 🔗 5. PROV-O Lineage

Fixtures register within provenance as:

~~~json
{
  "prov:Entity": "s1_deformation_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

These lineage entries attach downstream to QA + STAC outputs.

---

## 🧪 6. CI Integration

CI checks ensure:

- deterministic IFG creation  
- unwrapping accuracy  
- LOS projection correctness  
- correct inheritance of `"kfm:*"` governance metadata  
- schema + SHACL validity  
- pixel-perfect match with these fixtures  
- cross-platform determinism (CPU/GPU)  

Any mismatch → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict deformation-QA fixtures README; zero drift; emojis validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Deformation Tests](../tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

