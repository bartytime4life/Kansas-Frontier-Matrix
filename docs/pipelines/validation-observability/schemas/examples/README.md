---
title: "🧪 KFM Validation & Observability — Schema Examples Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/schemas/examples/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / Autonomous + FAIR+CARE Council Supervision"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/schema-examples-dashboard-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Reference"
doc_kind: "Schema-Examples-Index"
intent: "validation-observability-schema-examples-index"
semantic_document_id: "kfm-schema-examples-index"
doc_uuid: "urn:kfm:schemas:validation-observability:examples:index:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **Validation & Observability — Schema Examples Index**  
`docs/pipelines/validation-observability/schemas/examples/README.md`

**Purpose:**  
Provide a **central index** for all example JSON payloads used in:  
- Validation  
- Observability  
- FAIR+CARE governance  
- Telemetry pipelines  
- Dashboard schema demonstration  
- AI anomaly examples  
- Drift/Bias/Narrative/OOD/Sovereignty evaluations  

Each linked directory contains **canonical, CI-validated** examples that conform to KFM v11 schema rules.

</div>

---

# 📘 Overview

This index is the *root reference* for all schema examples within:

```
docs/pipelines/validation-observability/dashboards/schemas/
```

The example payloads included under this tree serve as:

- **Ground-truth templates** for contributors  
- **CI fixtures** for schema validation  
- **Governance evidence** for FAIR+CARE audits  
- **Reference structures** for downstream dashboards  
- **Machine-readable documentation**  
- **Model Promotion Gate input artifacts**  

All schemas follow:

- **KFM-MDP v11** (strict formatting)
- **MCP-DL v6.3** (documentation-first)
- **STAC 1.x**, **DCAT 3**, **PROV-O**
- **FAIR+CARE + CARE-S**

---

# 🗂 Directory Layout (Schema Example Root)

```text
docs/pipelines/validation-observability/schemas/examples/
│
├── README.md                                # This file
│
├── ai/                                       # AI-specific schema examples
│   ├── anomaly/                              # AI anomaly schema examples
│   │   ├── bias/                              # Bias anomaly examples
│   │   ├── drift/                             # Drift anomaly examples
│   │   ├── embeddings/                        # Embedding anomaly examples
│   │   ├── narrative/                         # Narrative anomaly examples
│   │   ├── ood/                               # OOD anomaly examples
│   │   └── reasoning/                         # Reasoning anomaly examples
│   │
│   ├── bias/                                 # Bias-specific schemas (correlation, parity, sovereignty, etc.)
│   │   ├── correlation/
│   │   ├── narrative/
│   │   ├── parity/
│   │   ├── drift/
│   │   └── sovereignty/
│   │
│   └── drift/                                # Drift schemas
│       ├── bias/
│       ├── temporal/
│       ├── spatial/
│       ├── embeddings/
│       └── semantic/
│
├── telemetry/                                # Telemetry example schema payloads
│   ├── compute/
│   ├── energy/
│   └── sustainability/
│
└── governance/                               # Governance + FAIR+CARE schema examples
    ├── faircare/
    ├── promotion-gate/
    └── sovereignty-review/
```

---

# 🧩 What These Example Schemas Demonstrate

Each example directory contains JSON payloads illustrating:

### ✔ AI Model Anomalies  
- Bias  
- Drift  
- Reasoning faults  
- Narrative safety breaches  
- Focus Mode v3 integrity errors  
- Embedding instability  
- Out-of-distribution anomalies  

### ✔ FAIR+CARE + CARE-S Ethical Compliance  
- Cultural harm detection  
- Indigenous data sovereignty  
- Reviewer/authority constraints  
- Governance transparency  

### ✔ Telemetry Linkage  
- Compute energy (Wh)  
- Carbon output (gCO₂e)  
- Power profiles  
- Execution footprints for inference/evaluation  

### ✔ Provenance (PROV-O)  
- Who ran it  
- What data was used  
- Which model produced it  
- What output was generated  

### ✔ STAC/DCAT Mapping  
All example payloads are compatible with KFM STAC/DCAT metadata enrichment rules used for anomaly datasets.

---

# 🛠 Usage

Developers must:

- Use these examples as **canonical fixtures** when creating or updating schemas.  
- Ensure all new schema examples match KFM-MDP v11 formatting.  
- Ensure CI checks succeed using these examples.  
- Ensure FAIR+CARE + CARE-S alignment when contributing new examples.  

Governance teams should:

- Use these examples during FAIR+CARE governance reviews.  
- Validate provenance, harm-risk scoring, and sovereignty alignment.  

---

# 🧪 CI & Validation Requirements

All schema examples must:

- Pass **JSON Schema validation**  
- Pass **FAIR+CARE completeness audits**  
- Demonstrate **PROV-O lineage**  
- Include **telemetry references**  
- Use **correct STAC/DCAT fields**  
- Pass **schema-example linter** (`schema-example-lint.yml`)  
- Remain stable across releases (version-pinned)  

CI workflows triggered:

- `schema-examples-validate.yml`  
- `docs-lint.yml`  
- `faircare-schema-example-review.yml`  
- `provenance-check.yml`  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|---------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of Schema Example Index documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — Schema Example Index**  
*Consistency · Reproducibility · FAIR+CARE Governance · Provenance-Complete Intelligence*

[Back to Validation & Observability](../../README.md) ·  
[Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>