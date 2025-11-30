---
title: "💧📚 KFM v11 — Hydrology JSON-LD Explainability Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/hydrology/jsonld/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/hydro-jsonld-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hydrology-jsonld-v11.json"
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

doc_kind: "Explainability Template"
intent: "hydrology-jsonld-explainability-template"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-Compliant · Watershed-Sensitive · Semantic Transparency"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Watershed/tribal hydrology sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 💧📚 **Hydrology JSON-LD Explainability Template (KFM v11)**  
`docs/pipelines/ai/explainability/hydrology/jsonld/`

**Purpose**  
Provide the **canonical v11 JSON-LD template** for hydrology explainability objects  
across runoff models, flood-risk surrogates, evapotranspiration predictors,  
soil-moisture inference, and watershed-scale deep learning models.  

This ensures **semantic interoperability**, **provenance integrity**,  
**FAIR+CARE alignment**, and **Focus Mode explainability support**.

</div>

---

## 📘 1. Overview — Why JSON-LD for Hydrology?

Hydrology explainability often includes:

- Spatial attribution maps (grid or H3)  
- CAMS-driven sensitivity  
- Watershed-scale influences  
- Temporal storm-window logic  
- Multi-variable climate coupling  

JSON-LD enables:

- Semantically rich representation of hydrologic processes  
- Machine-readable explainability structure  
- Ingestion into Neo4j / triplestore KG  
- STAC/DCAT linking  
- PROV-O lineage  
- FAIR+CARE ethical metadata  
- Story Node v3 integration  

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/hydrology/jsonld/
├── 📄 README.md
│
├── 📁 context/                                  # JSON-LD @context files
│   ├── 🌐 hydrology.context.json
│   ├── 🌐 explainability.context.json
│   ├── 🌐 spatial.context.json
│   └── 🌐 climate.context.json
│
├── 🧠 templates/                                # Base JSON-LD templates
│   ├── 📄 shap-global.jsonld
│   ├── 📄 shap-local.jsonld
│   ├── 📄 integrated-gradients.jsonld
│   ├── 📄 h3-attribution.jsonld
│   ├── 📄 sensitivity.jsonld
│   └── 📄 temporal.jsonld
│
├── 🔗 lineage/                                  # PROV-O + OpenLineage templates
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                               # Validation specs
│   ├── 📄 validate-jsonld-shape.md
│   ├── 📄 validate-provenance.md
│   ├── 📄 validate-huc-watersheds.md
│   ├── 📄 validate-care.md
│   └── 📄 validate-sustainability.md
│
└── 📊 examples/                                 # Example JSON-LD explainability outputs
    ├── 📁 shap-global/
    ├── 📁 shap-local/
    ├── 📁 ig/
    ├── 📁 sensitivity/
    └── 📁 temporal/
~~~

---

## 🧬 3. JSON-LD Explainability Requirements (v11)

Every hydrology JSON-LD explainability artifact MUST include:

| Field | Required | Description |
|-------|----------|-------------|
| `@context` | ✔ | Must reference explainability + hydrology + spatial contexts |
| `@id` | ✔ | Unique URN for artifact |
| `@type` | ✔ | Subclass of `kfm:HydrologyExplainability` |
| `model:version` | ✔ | Hydrology AI model version |
| `kfm:domain` | ✔ | `"hydrology"` |
| `kfm:explainability_method` | ✔ | shap-global, shap-local, integrated-gradients, etc. |
| `kfm:input_variables` | ✔ | Model inputs (CAMS + hydrology variables) |
| `watershed_id` | ✔ | HUC-level watershed identifier |
| `datetime` | ✔ | Timestamp for inference/explainability run |
| `kfm:h3_res` | conditional | Required for hex-grid explainability |
| `kfm:sensitivity_flag` | ✔ | CARE/sovereignty-handling indicator |
| `kfm:energy_wh` | ✔ | Energy consumption |
| `kfm:carbon_gco2e` | ✔ | Carbon emissions |
| `prov:*` | ✔ | PROV-O lineage block |
| `openlineage:*` | conditional | Rich lineage integration |
| CRS fields | conditional | Required if spatial (EPSG:4326) |

---

## 🧪 4. Validation Rules (v11)

Validation MUST enforce:

### ✔ JSON-LD Structural Integrity  
- JSON-LD 1.1 compliance  
- Context expansion correctness  
- No unresolved vocabularies  

### ✔ Watershed Integrity  
- `watershed_id` aligns with hydrology pipeline domains (HUC4–HUC12)  
- Spatial extents match watershed boundaries  

### ✔ Provenance Completeness  
- PROV-O: used/generate/activity/agent required  
- OpenLineage optional but recommended  

### ✔ CARE / Sovereignty  
- Sensitive hydrologic areas masked/generalized  
- No high-risk reverse-geocodable outputs  
- CARE metadata required  

### ✔ Sustainability  
- Energy/carbon usage included  
- No budget exceedance  

Failure → rollback (Reliability Layer v11).

---

## 🌐 5. STAC/DCAT Compatibility

Each JSON-LD explainability artifact MUST:

- Integrate with STAC Items as an `asset` or `metadata extension`  
- Be linkable from a DCAT Dataset graph  
- Fit the KFM Explainability Context model for the Neo4j KG  

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Each artifact MUST include:

- `prov:Activity` — explainability run  
- `prov:used` — CAMS + hydrology datasets  
- `prov:generated` — attribution assets  
- `prov:wasAssociatedWith` — compute agent  

If OpenLineage is included:

- `runId`  
- `inputs`  
- `outputs`  
- execution metadata  

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Every hydrology explainability run MUST emit:

- `kfm.expl_method="hydrology-jsonld"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_latency_ms`  
- `gpu_pct`, `cpu_pct`, `ram_mb`  
- `kfm.rows_processed`  

Telemetry is written to the release bundle and linked from STAC/lineage.

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Hydrology JSON-LD explainability objects SHOULD generate a Story Node that captures:

- Key hydrologic drivers  
- Climate → hydrology linkages  
- Spatial influence patterns  
- Watershed sensitivity  
- FAIR+CARE notes  
- Full provenance chain  
- Sustainability footprint  

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 hydrology JSON-LD explainability template; CARE, lineage, telemetry compliant. |

---

<div align="center">

💧📚 **Kansas Frontier Matrix — Hydrology JSON-LD Explainability Template (v11.2.3)**  
Semantic · Ethical · Watershed-Aware · FAIR+CARE Compliant  

[📘 Docs Root](../../../../../..) · [🧠 Hydrology Explainability](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>