---
title: "🌡📚 KFM v11 — Climate Inference JSON-LD Output Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/inference/climate/jsonld/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/climate-inference-jsonld-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-inference-climate-jsonld-v11.json"
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

doc_kind: "Inference Template"
intent: "climate-inference-jsonld-template"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Climate Transparency"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Climate + hazard sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌡📚 **Climate Inference JSON-LD Output Template (KFM v11)**  
`docs/pipelines/ai/inference/climate/jsonld/`

**Purpose**  
Provide the **canonical v11 JSON-LD template** for climate AI inference outputs  
(e.g., PM2.5 forecasts, ozone risk, smoke/visibility indices, heat-stress maps),  

ensuring standardized **semantic structure**, **provenance**, **telemetry**,  
**FAIR+CARE compliance**, and **STAC/DCAT interoperability** across all climate inference pipelines.

</div>

---

## 📘 1. Overview — Why JSON-LD for Climate Inference?

Climate inference pipelines in KFM produce:

- Gridded hazard fields (ozone, PM2.5, smoke, temperature, humidity, wind risk)  
- Indices (AQI, heat index, fire danger, drought index)  
- Scenario/simulation outputs (near-term forecasts, hindcasts, counterfactuals)  

JSON-LD provides:

- **Semantic tagging** of variables, units, and climate domains  
- **Machine-readable provenance** (PROV-O, OpenLineage)  
- **Cross-dataset linking** via DCAT/STAC  
- **Explainability + inference graph integration** (inputs → model → outputs)  
- **FAIR+CARE** embedding (ethics, sensitivity flags)  
- Direct ingestion into **Neo4j / RDF / graph-based Focus Mode pipelines**

This template defines the **minimum JSON-LD shape** for all KFM climate inference outputs.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/inference/climate/jsonld/
├── 📄 README.md
│
├── 📁 context/                               # JSON-LD @context vocabularies
│   ├── 🌐 climate.context.json               # Climate-variable vocab (ozone, PM2.5, etc.)
│   ├── 🌐 explainability.context.json        # Shared explainability + model vocab
│   ├── 🌐 spatial.context.json               # CRS, H3, grid geometry
│   └── 🌐 temporal.context.json              # Forecast horizons, lead times, validity windows
│
├── 🧠 templates/                             # Base JSON-LD inference templates
│   ├── 📄 forecast.jsonld                    # Single-run forecast artifact
│   ├── 📄 scenario.jsonld                    # Scenario/hindcast output
│   ├── 📄 ensemble.jsonld                    # Ensemble inference summary
│   └── 📄 hazard-panel.jsonld                # Multi-variable hazard panel (e.g., PM2.5 + ozone)
│
├── 🔗 lineage/                               # PROV-O + OpenLineage templates
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                            # Validation + ethics specs
│   ├── 📄 validate-jsonld-shape.md
│   ├── 📄 validate-provenance.md
│   ├── 📄 validate-sensitivity.md
│   ├── 📄 validate-sustainability.md
│   └── 📄 validate-forecast-horizons.md
│
└── 📊 examples/                              # Example inference JSON-LD payloads
    ├── 📁 forecast/
    ├── 📁 scenario/
    ├── 📁 ensemble/
    └── 📁 hazard-panel/
~~~

---

## 🧬 3. JSON-LD Inference Requirements (v11)

Each climate inference JSON-LD artifact MUST include:

| Field                        | Required | Description                                           |
|------------------------------|----------|-------------------------------------------------------|
| `@context`                   | ✔        | Includes explainability + climate + spatial contexts |
| `@id`                        | ✔        | URN for the inference artifact                        |
| `@type`                      | ✔        | Subclass of `kfm:ClimateInference`                   |
| `model:version`             | ✔        | AI model version                                      |
| `kfm:domain`                 | ✔        | `"climate"` or `"air"`                                |
| `kfm:inference_type`         | ✔        | `forecast` · `hindcast` · `scenario` · `ensemble`     |
| `kfm:variables`              | ✔        | Names of predicted variables (e.g., pm25, o3)         |
| `kfm:lead_time_hours`        | ✔        | Forecast horizon (for forecasts)                      |
| `kfm:valid_time`             | ✔        | Valid time for the prediction                         |
| `kfm:energy_wh`              | ✔        | Energy cost of inference run                          |
| `kfm:carbon_gco2e`           | ✔        | Carbon emissions estimate                             |
| `kfm:sensitivity_flag`       | ✔        | CARE sensitivity classification                       |
| `prov:*`                     | ✔        | PROV-O activity/agent/used/generated                  |
| `openlineage:*`              | conditional | OpenLineage run binding (recommended)            |
| Spatial CRS/H3 fields        | conditional | Required if spatial output (EPSG:4326, H3 res)   |

The JSON-LD MUST:

- Expand successfully under JSON-LD 1.1  
- Map to KFM ontology terms (`KFM-OP v11`)  
- Be ingestible into the KFM knowledge graph.

---

## 🧾 4. Base Forecast Template (Minimal JSON-LD)

~~~json
{
  "@context": [
    "https://kfm.org/context/explainability.context.json",
    "https://kfm.org/context/climate.context.json",
    "https://kfm.org/context/spatial.context.json"
  ],
  "@id": "urn:kfm:inference:climate:pm25-ozone:forecast:2025-11-29T00:00Z",
  "@type": "kfm:ClimateInferenceForecast",

  "model:version": "cams-pm25-ozone-v2.1",
  "kfm:domain": "climate",
  "kfm:inference_type": "forecast",
  "kfm:variables": ["pm25", "o3"],
  "kfm:lead_time_hours": 24,
  "kfm:valid_time": "2025-11-30T00:00:00Z",

  "kfm:energy_wh": 2.17,
  "kfm:carbon_gco2e": 0.84,
  "kfm:sensitivity_flag": "none",

  "prov:Activity": { "prov:wasAssociatedWith": "urn:ci:github-actions" },
  "prov:used": [
    "urn:stac:item:cams:2025-11-29T00:00Z",
    "urn:kfm:model:cams-pm25-ozone-v2.1"
  ],
  "prov:generated": [
    "urn:kfm:artifact:pm25-ozone-forecast:2025-11-30T00:00Z"
  ]
}
~~~

---

## 🧪 5. Validation Rules (v11)

### ✔ JSON-LD Structural Validation

- JSON-LD 1.1 compliant  
- All contexts resolvable  
- No unbound prefixes  

### ✔ Climate Inference Integrity

- `kfm:variables` match model schema  
- `kfm:lead_time_hours` and `kfm:valid_time` coherent  
- Forecast windows aligned with training setups  

### ✔ Provenance Completeness

- PROV-O `Activity`, `used`, `generated`, `wasAssociatedWith` present  
- OpenLineage (if used) includes inputs & outputs  

### ✔ CARE / Ethics

- Sensitive geographic regions flagged / masked if necessary  
- `kfm:sensitivity_flag` set to match review  
- No reverse-geocodable high-risk outputs without masking  

### ✔ Sustainability

- Energy & carbon recorded  
- Within climate inference budgets  

Validation failures → rollback (Reliability Layer v11).

---

## 🌐 6. STAC/DCAT Compatibility

Each JSON-LD inference artifact MUST:

- Be attachable to a STAC Item as a metadata asset or extension  
- Map into a DCAT Dataset description  
- Support KG queries (Who generated this? With which data? When? At what cost?)  

---

## 🔗 7. Provenance (PROV-O + OpenLineage)

Each inference run MUST include:

- `prov:Activity` = inference pipeline run  
- `prov:used` = input datasets (CAMS, ancillary climate fields)  
- `prov:generated` = forecast/hazard output artifact(s)  
- `prov:wasAssociatedWith` = CI runner / pipeline agent  

OpenLineage (recommended):

- `runId`  
- `job` + `task` facets  
- Inputs/Outputs  
- Execution attributes  

Templates live under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 8. Telemetry (OTel v11)

Each inference run MUST emit:

- `kfm.inf_method="climate-jsonld"`  
- `kfm.energy_wh`  
- `kfm.carbon_gco2e`  
- `kfm.latency_ms`  
- `kfm.rows_processed`  
- CPU/GPU/memory metrics  

Telemetry is:

- Written to the release telemetry bundle  
- Linked from STAC items and lineage events  

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Climate inference JSON-LD nodes support:

- **Story Nodes** summarizing forecast context, variables, and risk areas  
- Narrative ties between climate drivers and observed impacts  
- Explainability overlays (when combined with SHAP/IG maps)  
- FAIR+CARE ethics annotation for climate risk communication  

They allow the KFM UI to answer:

- “Which model produced this warning?”  
- “What climate variables drove this prediction?”  
- “How much energy/carbon did this inference cost?”  

---

## 🧭 10. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 climate inference JSON-LD template; FAIR+CARE, lineage, telemetry integrated. |

---

<div align="center">

🌡📚 **Kansas Frontier Matrix — Climate Inference JSON-LD Template (v11.2.3)**  
Semantic · Transparent · FAIR+CARE · Provenance-Driven  

[📘 Docs Root](../../../../../..) · [🤖 Climate Inference](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>