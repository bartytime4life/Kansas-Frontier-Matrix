---
title: "📁 Sentinel-1 QA — Master Fixture Library (Radiometry · Coherence · Flood · Wetlands · Deformation)"
path: "docs/data/satellites/sentinel-1/qa/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High-Sensitivity QA Fixtures (CARE-B · Sovereignty-Aware)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · RS Working Group · Sovereignty Board · FAIR+CARE Council"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-B"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-qa-fixtures-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group · Sovereignty Board"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-qa-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-qa-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when QA fixture suite updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Master Fixture Library — Sentinel-1 QA**  
`docs/data/satellites/sentinel-1/qa/fixtures/`

Cross-domain golden-truth reference datasets for validating  
**radiometry**, **coherence**, **flood**, **wetlands**, and **deformation**  
QA pipelines in a sovereignty-aware, FAIR+CARE-aligned workflow.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/fixtures/
├── 📄 README.md
│
├── 📁 radiometry/                    # σ⁰ · γ⁰ · DEM alignment QA truth references
├── 📁 coherence/                     # coherence magnitude + pair-baseline truth
├── 📁 flood/                         # flood mask + DEM pooling + classifier truths
├── 📁 wetlands/                      # γ⁰ wetness · seasonal · coherence-fusion truths
└── 📁 deformation/                   # IFG · unwrapped phase · LOS generalized displacement
~~~

✔ Emoji BEFORE folder names  
✔ Perfectly aligned with all child QA fixture directories  
✔ Zero drift, 100% box-safe  

---

## 📘 2. Purpose

The **Master QA Fixtures Directory** consolidates reference outputs for  
every Sentinel-1 QA subsystem:

- **Radiometry QA**  
  - σ⁰ calibration  
  - γ⁰ RTC correctness  
  - DEM–incidence alignment

- **Coherence QA**  
  - coherence magnitude truth  
  - pair baseline metadata  
  - sliding-window statistics

- **Flood QA**  
  - ratio + hybrid classifier outputs  
  - DEM pooling hydrology  
  - flood mask truth

- **Wetlands QA**  
  - γ⁰ wetness indicators  
  - seasonal hydrology priors  
  - coherence-fusion truth

- **Deformation QA**  
  - interferogram (IFG)  
  - unwrapped phase  
  - sovereignty-generalized LOS displacement  

These fixtures are used across all CI gates to ensure  
**deterministic, reproducible, and sovereignty-safe QA evaluations.**

---

## 🧩 3. Structure & Validation

Each child directory contains:

- canonical rasters (`*.tif`)  
- canonical metadata (`*.json`)  
- sovereignty-safe references  
- `"kfm:*"` governance metadata  
- PROV-O lineage tags  
- FAIR+CARE alignment

All QA tests compare their computed outputs against these fixtures.  
Any mismatch results in a **CI block**.

---

## 🔐 4. FAIR+CARE & Sovereignty Constraints

Although fixtures do **not** contain raw sovereign geometries,  
they **must** carry correct metadata enforcing:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- `"kfm:sovereignty_generalized"` (for deformation)  
- `"kfm:uncertainty_floor_applied"` (where applicable)

Fixtures ensure **downstream QA + ETL pipelines** operate under  
correct governance and masking expectations.

---

## 🔗 5. PROV-O Lineage

All fixture sets register as:

~~~json
{
  "prov:Entity": "s1_master_qa_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

Every QA subsystem attaches this provenance to its validation artifacts.

---

## 🧪 6. CI Integration

CI uses this directory as the **global QA truth database**, enforcing:

- consistency across QA domains  
- strict schema/SHACL compliance  
- deterministic cross-platform (CPU/GPU) behavior  
- flood/wetlands/deformation alignment  
- governance metadata integrity  
- STAC readiness for all downstream products  

Any mismatch → **CI/block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict master QA fixture README; zero drift; emoji-prefix alignment validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 QA Domains](../README.md#sentinel-1-qa-domains) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

