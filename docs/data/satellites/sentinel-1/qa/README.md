---
title: "🧪 Sentinel-1 QA — Quality Assurance & Validation Framework (GRD · RTC · Coherence · Flood · Wetlands · Deformation)"
path: "docs/data/satellites/sentinel-1/qa/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B · Sovereignty-Affected QA)"
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

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/sentinel1-qa-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group · Sovereignty Board"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../schemas/json/sentinel1-qa-v11.json"
shape_schema_ref: "../../../schemas/shacl/sentinel1-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next QA schema/standard update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 QA — Quality Assurance Overview**  
`docs/data/satellites/sentinel-1/qa/`

Governed QA system for validating **every Sentinel-1 derivative layer** used in KFM:  
GRD → RTC → Coherence → Flood → Wetlands → Deformation (LOS) → STAC outputs.

Ensures correctness, reproducibility, sovereignty compliance, and FAIR+CARE alignment.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/
├── 📄 README.md
│
├── 🧪 radiometry/                 # σ⁰ / γ⁰ radiometric QA (RTC input validation)
├── 🧪 coherence/                  # Coherence quality, window stats, decorrelation
├── 🧪 flood/                      # Flood classification QA (ratio, hybrid, DEM pooling)
├── 🧪 wetlands/                   # Wetlands/saturation QA (γ⁰, coherence, seasonal models)
├── 🧪 deformation/                # InSAR deformation QA (IFG, unwrapping, LOS checks)
└── 📁 fixtures/                   # Reference QA truth data (sample rasters, masks, metadata)
~~~

✔ Emoji BEFORE folders  
✔ Perfect alignment with `smap/qa/**` and all QA trees  
✔ Zero drift  
✔ Box-safe  

---

## 📘 2. Purpose

The **Sentinel-1 QA subsystem** ensures:

- GRD → RTC correctness  
- γ⁰ normalization validity  
- coherence-phase stability  
- flood/wetlands hydrological validity  
- deformation correctness (IFG → unwrap → LOS)  
- STAC metadata integrity  
- sovereignty enforcement readiness  
- troubleshooting of SAR anomalies (noise, decorrelation, DEM mismatch)

QA is required for:

- operational pipeline certification  
- governance council review  
- STAC-level release approvals  
- model calibration cycles  
- reproducibility & reliability audits  

---

## 🧩 3. QA Domains

### 🧪 Radiometry QA
Validates:

- σ⁰ VV/VH radiometric calibration  
- RTC γ⁰ conversion  
- incidence-angle consistency  
- DEM slope/aspect alignment  
- numeric stability

### 🧪 Coherence QA
Checks:

- coherence range validity  
- temporal baseline health  
- window-statistics correctness  
- low-SNR behavior  
- sovereign-risk indicators  

### 🧪 Flood QA
Ensures:

- ratio threshold correctness  
- hybrid-classifier fusion consistency  
- DEM pooling validity  
- flood mask comparators  
- governance metadata propagation  

### 🧪 Wetlands QA
Ensures:

- γ⁰ wetness signal integrity  
- seasonal-model behavior  
- hydrology-aware thresholds  
- coherence-fusion effects  
- sovereign-area safe results  

### 🧪 Deformation QA
Ensures:

- IFG correctness  
- unwrap continuity  
- LOS projection math  
- sovereignty generalization  
- smoothing + uncertainty floors  

---

## 🔐 4. FAIR+CARE & Sovereignty Integration

QA enforces:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:sovereignty_generalized"` metadata verification  
- `"kfm:uncertainty_floor_applied"` correctness  

QA does **not** expose full-resolution sensitive data;  
fixtures and results are sovereignty-scrubbed.

---

## 🔗 5. PROV-O Lineage

QA products are **prov:Entity** with a QA-specific provenance profile:

~~~json
{
  "prov:Entity": "s1_qa_surface",
  "prov:wasGeneratedBy": "s1_qa_pipeline",
  "kfm:care_label": "CARE-B",
  "kfm:qa_type": "validation"
}
~~~

---

## 🧪 6. CI Integration

CI executes the complete QA stack:

- unit + integration QA  
- raster equivalence  
- metadata validation  
- STAC contract validation  
- sovereignty masking consistency  
- deterministic-signal tests  
- low-SNR and error-case QA  

Any mismatch → CI fail → no release.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 QA overview; directory alignment + CARE/H3 governance validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../../README.md) · [🛡 Governance Transform](../transforms/governance/README.md) · [📁 Fixtures](./fixtures/README.md)

</div>

