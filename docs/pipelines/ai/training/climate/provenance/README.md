---
title: "🌡🔗 KFM v11 — Climate AI Training Provenance Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/training/climate/provenance/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/climate-training-provenance-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-training-climate-provenance-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Provenance Module"
intent: "climate-training-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Climate-Sensitive · Provenance-Safe"

classification: "Public (Governed)"
sensitivity: "Moderate (climate/hazard-level modeling)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌡🔗 **Climate AI Training Provenance Framework (KFM v11)**  
`docs/pipelines/ai/training/climate/provenance/`

**Purpose**  
Define the **v11 governed provenance architecture** for all *climate AI training pipelines*,  
ensuring every stage of data ingestion, model training, evaluation, explainability, and promotion  
is recorded with **PROV-O**, **OpenLineage**, **STAC/DCAT**, and **FAIR+CARE governance metadata**.

Climate ML models must be *verifiably reproducible*, *ethically governed*, *energy-aware*, and *historically traceable*.

</div>

---

## 📘 1. Overview — What Provenance Means for Climate AI in KFM

Climate AI pipelines use large heterogeneous datasets (CAMS, ERA5, HRRR, AQS, NLCD, MODIS).  
Model transparency requires:

- Full input lineage (who/what/when/how)
- Transformation lineage (preprocessing, feature engineering, harmonization)
- Model artifact lineage (architecture, hyperparameters, epochs)
- Evaluation lineage (datasets, metrics, event windows)
- Explainability lineage (SHAP/IG/CAMS derivations)
- Sustainability lineage (energy, carbon, runtime)
- Ethical lineage (CARE, sovereignty, sensitive-region handling)

The KFM v11 Provenance Framework ensures **every artifact**—dataset, model, evaluation, or explainability output—  
includes a complete machine-readable lineage chain.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/training/climate/provenance/
├── 📄 README.md
│
├── 🔧 templates/                         # Base provenance templates
│   ├── 🧾 prov-activity.json             # PROV-O activity skeleton
│   ├── 🧾 prov-entity.json               # Entity template (datasets, models)
│   ├── 🧾 prov-agent.json                # Pipeline agent template
│   ├── 📡 ol-run.json                    # OpenLineage Run template
│   ├── 📡 ol-job.json                    # OpenLineage Job template
│   └── 📡 ol-facets.json                 # Available OL facets
│
├── 🌐 stac/                              # Provenance-aware STAC extensions
│   ├── 📄 stac-provenance-template.json
│   └── 📄 stac-collection-template.json
│
├── 🧪 validation/                        # Provenance validation rules
│   ├── 📄 validate-prov-o.md
│   ├── 📄 validate-openlineage.md
│   ├── 📄 validate-stac-linking.md
│   ├── 📄 validate-ontology-alignment.md
│   └── 📄 validate-ethics-care.md
│
└── 📊 examples/                          # Example provenance bundles
    ├── 📁 dataset/
    ├── 📁 model/
    ├── 📁 evaluation/
    ├── 📁 explainability/
    └── 📁 pipeline-run/
~~~

---

## 🧬 3. Provenance Requirements (v11)

Every climate training artifact MUST include:

### ✔ PROV-O Core Elements

| Field | Description |
|-------|-------------|
| `prov:Entity` | dataset, model, metric bundle, explainability map |
| `prov:Activity` | training run, evaluation run, ingestion, preprocessing |
| `prov:Agent` | CI system, pipeline, human reviewer |
| `prov:used` | input datasets and model dependencies |
| `prov:generated` | outputs (models, metrics, explainability assets) |
| `prov:wasAssociatedWith` | execution agent |

### ✔ OpenLineage Elements

| Field | Description |
|--------|-------------|
| `runId` | Unique lineage run identifier |
| `job.name` | Climate-pipeline job |
| `inputs[]` | Upstream datasets |
| `outputs[]` | Generated artifacts |
| `facets` | Metrics, dataset versions, data quality, sustainability |

### ✔ FAIR+CARE Lineage

| Requirement | Description |
|-------------|-------------|
| CARE | Sensitive-area handling, masking rules |
| FAIR | Reproducible metadata, public-good handling |
| Sovereignty | Tribal/watershed-sensitive climate zones protected |

### ✔ Sustainability Lineage

- Energy (Wh)  
- Carbon (gCO₂e)  
- Hardware class  
- Duration  
- Memory/compute footprints  

---

## 📦 4. Required Provenance Bundles

Each training pipeline MUST emit:

### 1. **Dataset Provenance Bundle**
- CAMS/ERA5/HRRR source metadata  
- Spatial/temporal extents  
- Variable dictionary  
- CARE + governance evaluation  
- STAC/DCAT links  

### 2. **Model Provenance Bundle**
- Model architecture  
- Hyperparameters  
- Seed values  
- Epochs  
- Training window  
- Dataset lineage linkage  

### 3. **Evaluation Provenance Bundle**
- Metrics  
- Evaluation datasets  
- Explainability lineage pointers  
- FAIR+CARE flags  

### 4. **Explainability Provenance Bundle**
- SHAP/IG/CAMS-explainability methods  
- Attribution parameters  
- Output artifacts  
- JSON-LD linkage  

### 5. **Pipeline Run Provenance (OpenLineage)**  
- Job + task lineage  
- Input/output pointers  
- Sustainability metrics  
- Run status  

---

## 🧪 5. Validation Rules (v11)

Provenance MUST satisfy:

### ✔ Structural Validity
- JSON-LD/JSON schema compliance  
- PROV-O required fields  
- OpenLineage job/run validity  
- STAC/DCAT alignment  

### ✔ Data Integrity
- Correct dataset IDs, version tags, temporal ranges  
- Accurate linkages to training windows  
- No missing entities or dangling lineage edges  

### ✔ CARE + Sovereignty Checks
- Sensitive regions masked  
- No coordinate resolution beyond allowed precision  
- CARE flag must reflect policy review  

### ✔ Sustainability Checks
- Energy/carbon recorded  
- Must not exceed pipeline governance budget  

Validation failures → **rollback** + governance review.

---

## 🌐 6. STAC + DCAT Integration

Every provenance bundle MUST:

- Link as a STAC Item asset  
- Map to DCAT via JSON-LD `@context`  
- Embed PROV-O under `properties` and `links`  
- Support hyperlinking to model cards + telemetry  

---

## 🔗 7. Provenance Templates (Minimal Examples)

### PROV-O Activity Template

~~~json
{
  "prov:Activity": {
    "prov:id": "urn:kfm:activity:climate-training:2025-11-29T00",
    "prov:startTime": "2025-11-29T00:00:00Z",
    "prov:endTime": "2025-11-29T01:20:00Z",
    "prov:wasAssociatedWith": "urn:ci:github-actions"
  }
}
~~~

### OpenLineage Run Template

~~~json
{
  "runId": "ol-abc123",
  "job": {"name": "kfm.climate.training.v11"},
  "inputs": ["urn:stac:item:cams:2025-11-29","urn:kfm:dataset:era5:v2025"],
  "outputs": ["urn:kfm:model:cams-pm25-v3.2"],
  "facets": {
    "kfm_sustainability": {
      "energy_wh": 4.2,
      "carbon_gco2e": 2.1,
      "hardware": "A100-40GB"
    }
  }
}
~~~

---

## 📡 8. Telemetry Integration (OTel v11)

Provenance MUST include or reference telemetry for:

- Training duration  
- GPU/CPU usage  
- Energy/carbon  
- Dataset read/write volume  
- H3 grid cell counts  
- Memory footprint  

Telemetry is linked into:

- STAC  
- JSON-LD  
- OpenLineage facets  
- Release-level governance bundles  

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Provenance bundles generate Story Nodes covering:

- Model training origin & dataset lineage  
- Climate driver importance  
- Critical training periods (storms, smoke events, heat waves)  
- Version-to-version drift  
- FAIR+CARE governance narrative  
- Sustainability footprint  

These fuel **explainable, audit-ready climate model histories**.

---

## 🧭 10. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 climate training provenance framework; unified with STAC/OL/PROV-O/CARE/telemetry. |

---

<div align="center">

🌡🔗 **Kansas Frontier Matrix — Climate AI Training Provenance (v11.2.3)**  
Traceable · Ethical · Reproducible · FAIR+CARE · Governance-Enforced  

[📘 Docs Root](../../../../../..) • [🌡 Climate Training Pipelines](../README.md) • [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>