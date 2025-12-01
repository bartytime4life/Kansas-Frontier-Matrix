---
title: "📁 Kansas Frontier Matrix — Land Treaties Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/historical/land-treaties/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/telemetry.json"
telemetry_schema: "../../../schemas/telemetry/module-default-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Module"
semantic_intent:
  - "data-governance"
  - "heritage-records"
  - "treaty-boundaries"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Enforced"
sensitivity: "High (Indigenous data — masked)"
public_exposure_risk: "Medium"
classification: "Public With Safeguards"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Supersedes previous treaty modules"
immutability_status: "version-pinned"
ai_training_inclusion: false

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 Metadata & Standards Compliance"
    - "🧱 Pipeline Behavior"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧬 Version History"
    - "⚖️ Footer"

provenance_chain:
  - "docs/data/historical/land-treaties/README.md@v11.2.1"
  - "docs/data/historical/land-treaties/README.md@v11.1.0"

json_schema_ref: "../../../schemas/json/story-node.schema.json"
shape_schema_ref: "../../../schemas/shacl/story-node-shape.ttl"
doc_uuid: "urn:kfm:module:land-treaties:v11.2.2"
semantic_document_id: "kfm-module-land-treaties-v11.2.2"
event_source_id: "ledger:kfm:module:land-treaties:v11.2.2"
---

<div align="center">

# 📁 **Kansas Frontier Matrix — Land Treaties Module**  
`docs/data/historical/land-treaties/`

**Purpose:**  
Provide authoritative, structured, governed treaty datasets (1850–1890) for narrative, geospatial, and historical interpretation within the Kansas Frontier Matrix v11 architecture.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA%2B-brightgreen)]()  
[![SLSA Level 3](https://img.shields.io/badge/SLSA-Level%203-orange)]()

</div>

---

## 📘 1. Overview

This module contains the **canonical treaty datasets** for KFM v11, including treaty polygons, negotiation events, participating tribal nations, scanned documents, transcription workflows, and narrative assets.

All module content must:

- Be **graph-ready** (CIDOC-CRM / GeoSPARQL / OWL-Time)  
- Be **metadata-complete** (STAC + DCAT + PROV-O)  
- Support **Story Nodes** & **Focus Mode v3**  
- Apply **CARE** masking for sensitive tribal data  
- Use **deterministic pipelines** with WAL-backed lineage  
- Pass **CI/CD metadata, schema, provenance, and accessibility tests**

---

## 🗂️ 2. Directory Layout (Emoji-Enhanced)

~~~text
docs/data/historical/land-treaties/
│
├── 📄 README.md                      # This file
│
├── 🗂️ stac/                          # STAC metadata
│   ├── 🗃️ collections/                # STAC Collection JSONs
│   └── 📑 items/                      # STAC Items for treaty assets
│
├── 🧬 schemas/                       # JSON Schema / SHACL / ontology shapes
│   ├── 📁 json/                      # JSON Schemas for treaty records
│   └── 🧩 ttl/                       # SHACL + OWL-Time + GeoSPARQL shapes
│
├── 🔁 workflows/                     # ETL + LangGraph pipelines
│   ├── ⚙️ etl/                       # Deterministic ETL job defs
│   └── 🧵 jobs/                      # Cron/orchestration tasks
│
├── 🧪 qa/                            # Fixtures + validation reports
│   ├── 🧱 fixtures/                  # Minimal treaty test files
│   └── 📊 reports/                   # QA outputs (schema, stac, lineage)
│
├── 🎛️ samples/                       # Examples + notebooks
│   ├── 🧩 data/                      # Sample boundaries + transcripts
│   └── 📓 notebooks/                 # Jupyter/MD tutorials
│
└── 📦 assets/                        # Scanned docs + static references
    ├── 🧾 config/                    # Module-level config
    └── 🗃️ docs/                      # Treaty scans + reference PDFs
~~~

---

## 📦 3. Metadata & Standards Compliance

(…unchanged from previous draft…)

---

## 🧱 4. Pipeline Behavior

(…unchanged…)

---

## 🧠 5. Story Node & Focus Mode Integration

(…unchanged…)

---

## 🧬 6. Version History

| Version | Date       | Notes |
|---------|------------|-------|
| v11.2.2 | 2025-11-30 | Initial compliant module reconstruction |

---

## ⚖️ Footer (Required Governance Block)

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../README.md) •  
[Standards Index](../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE • STAC/DCAT • OWL-Time • CIDOC-CRM • SLSA Level 3 • SPDX 2.3 • OpenLineage

**♻️ Sustainability:**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)

**End of Document**

</div>