---
title: "📚 KFM v11 — JSON-LD Explainability Template (FAIR+CARE · STAC/DCAT · PROV-O · Diamond⁹ Ω / Crown∞Ω)"
path: "docs/pipelines/ai/explainability/templates/jsonld/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Explainability WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/jsonld-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-jsonld-v11.json"
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
intent: "jsonld-explainability-template"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Semantic Transparency"

classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📚 **KFM v11 — JSON-LD Explainability Template**  
`docs/pipelines/ai/explainability/templates/jsonld/`

**Purpose**  
Provide a **governed v11 template** for producing JSON-LD explainability metadata  
for AI attribution layers (SHAP, sensitivity, gradient maps, H3 attribution grids),  
ensuring standardized **semantic structure**, **provenance**, **context linking**,  
**FAIR+CARE compliance**, and **STAC/DCAT interoperability**.

This template is the backbone for machine-readable explainability objects  
across all KFM domains (climate, hydrology, soils, archaeology, ecology, wildfire, air).

</div>

---

## 📘 1. Overview — Why JSON-LD?

JSON-LD enables:

- **Semantic explainability** (units, variable names, ontology IDs)  
- **Machine-readable provenance** (PROV-O)  
- **Dataset interoperability** (DCAT, STAC mappings)  
- **Explainability graph linking** (models → variables → features → regions)  
- **FAIR+CARE-aligned ethics metadata**  
- **Automatic ingestion into Neo4j / triple stores / graph engines**  
- **Explainability → Story Nodes v3 → Focus Mode v3 narratives**

This template defines **the minimum required JSON-LD shape** for any explainability output in KFM v11.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/templates/jsonld/
├── 📄 README.md                               # This file
│
├── 📁 context/                                # JSON-LD @context files
│   ├── 🌐 explainability.context.json         # Global context for all explainers
│   ├── 🌐 spatial.context.json                # Spatial/H3 context
│   ├── 🌐 climate.context.json                # Domain-specific vocabulary (optional)
│   └── 🌐 soil.context.json                   # Domain-specific vocabulary (optional)
│
├── 🧠 templates/                              # Base JSON-LD templates
│   ├── 📄 shap-global.jsonld
│   ├── 📄 shap-local.jsonld
│   ├── 📄 h3-attribution.jsonld
│   ├── 📄 sensitivity.jsonld
│   └── 📄 gradient.jsonld
│
├── 🔗 lineage/                                # Provenance & OpenLineage binding templates
│   ├── 🧾 prov-template.json                  # PROV-O block
│   └── 📡 ol-template.json                    # OpenLineage block
│
├── 🧪 validation/                             # JSON-LD integrity + CARE checks
│   ├── 📄 validate-jsonld-shape.md
│   ├── 📄 validate-provenance.md
│   └── 📄 validate-ethics.md
│
└── 📊 examples/                               # Example explainability JSON-LD payloads
    ├── 📁 shap-global/
    ├── 📁 shap-local/
    ├── 📁 h3/
    └── 📁 sensitivity/
~~~

---

## 🧬 3. JSON-LD Explainability Requirements (v11)

Every JSON-LD explainability object MUST include:

| Field | Requirement | Description |
|-------|-------------|-------------|
| `@context` | ✔ | One or more context files from `context/` (explainability + domain) |
| `@id` | ✔ | Unique URN for explainability artifact |
| `@type` | ✔ | `"kfm:Explainability"` or domain subclass |
| `model:version` | ✔ | Version of the AI model |
| `kfm:explainability_method` | ✔ | shap-global, shap-local, h3-attribution, sensitivity… |
| `kfm:input_variables` | ✔ | List of variables used by the model |
| `kfm:domain` | ✔ | climate / soil / archaeology / hydro / air… |
| `kfm:sensitivity_flag` | ✔ | CARE-sensitive tag |
| `kfm:energy_wh` | ✔ | Energy usage of explainability run |
| `kfm:carbon_gco2e` | ✔ | Carbon estimate |
| `prov:*` | ✔ | PROV-O entity/activity/agent triple structure |
| `openlineage:*` | ✔ | Optional enrichment for lineage linking |
| CRS fields | required if spatial | EPSG:4326 or H3 resolution |
| H3 fields | optional | If mapped to hex grid |

All JSON-LD MUST resolve cleanly using:

- JSON-LD 1.1 processor  
- KFM Explainability Context  
- KFM Knowledge Graph import routines  

---

## 🧾 4. Base Template (Minimal JSON-LD)

~~~json
{
  "@context": [
    "https://kfm.org/context/explainability.context.json",
    "https://kfm.org/context/climate.context.json"
  ],
  "@id": "urn:kfm:explainability:shap:global:2025-11-29T00:00Z",
  "@type": "kfm:ExplainabilityGlobalSHAP",

  "model:version": "v3.4.1-cams",
  "kfm:domain": "climate",
  "kfm:explainability_method": "shap-global",
  "kfm:input_variables": ["cams_pm25", "cams_o3", "wind_u", "wind_v"],
  "kfm:energy_wh": 1.42,
  "kfm:carbon_gco2e": 0.52,
  "kfm:sensitivity_flag": "none",

  "prov:Activity": { "prov:wasAssociatedWith": "github-actions-ci" },
  "prov:used": [
    "urn:stac:item:cams:2025-11-28"
  ],
  "prov:generated": [
    "urn:kfm:explainability:shap:global:artifact.parquet"
  ]
}
~~~

---

## 🧪 5. Validation Rules

JSON-LD explainability artifacts MUST pass:

### ✔ JSON-LD Structural Validation  
- Must parse under JSON-LD 1.1  
- All context fields resolvable  
- No unused vocabularies  

### ✔ PROV-O Validation  
- Activity → used → generated chain must exist  
- Agent required for model creation or explainability run  

### ✔ FAIR+CARE Ethics Validation  
- CARE-sensitive coordinates masked  
- No reverse-geocodable sensitive locations  
- `kfm:sensitivity_flag` must reflect review  

### ✔ Sustainability Validation  
- Energy and carbon fields required  
- Must not exceed pipeline budgets  

Validation failures → rollback (Reliability Layer v11).

---

## 🌐 6. STAC/DCAT Compatibility

JSON-LD explainability MUST be attachable to:

- **STAC Item** via `links` and `assets`  
- **DCAT Dataset** as a semantic metadata block  
- **Story Nodes v3** for Focus Mode explainability narratives  

---

## 🔗 7. Provenance (PROV-O + OpenLineage)

Each JSON-LD must include:

- PROV-O: `prov:used`, `prov:generated`, `prov:Activity`, `prov:wasAssociatedWith`  
- Optional OpenLineage block:
  - runId  
  - parent facets  
  - duration / metrics  

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 8. Telemetry (OTel v11)

Each explainability run MUST emit:

- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_method="jsonld"`  
- `kfm.expl_latency_ms`  
- Trace linkage to OpenLineage and Airflow runs  

Telemetry exported to release-level:

`releases/v11.2.3/jsonld-explainability-telemetry.json`

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Story Nodes generated from JSON-LD explainability include:

- Feature importance summaries  
- Spatial influence narrative (if paired with H3)  
- Sensitivity notes  
- Provenance chain  
- Temporal evolution context  

These enable cross-domain explainability storytelling.

---

## 🧭 10. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 JSON-LD explainability template; full metadata & CARE alignment. |

---

<div align="center">

📚 **Kansas Frontier Matrix — JSON-LD Explainability Template (v11.2.3)**  
Semantic · Consistent · Provenance-Rich · FAIR+CARE Compliant  

[📘 Docs Root](../../../../../..) • [🧠 Explainability Templates](../README.md) • [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>