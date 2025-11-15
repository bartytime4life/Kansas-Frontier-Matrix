---
title: "🧭 Kansas Frontier Matrix — Pipeline Guides Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-guides-index-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Pipeline Guides Index**  
`docs/guides/pipelines/README.md`

**Purpose:**  
Provide the **master index** for all Kansas Frontier Matrix (KFM) pipeline guides.  
This directory documents how KFM pipelines are **designed**, **validated**, **executed**, **promoted**, **published**, and **governed** under **FAIR+CARE**, **MCP-DL v6.3**, and **Diamond⁹ Ω / Crown∞Ω** certification.

<img alt="Pipelines" src="https://img.shields.io/badge/Pipelines-Orchestrated-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Telemetry" src="https://img.shields.io/badge/Telemetry-v3-success"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

The **Pipeline Guides** collection explains the framework that powers KFM’s ingestion, preprocessing, validation, lineage, AI integration, publishing, and governance systems.  
These guides ensure:

- Deterministic, reproducible ETL  
- FAIR+CARE enforcement  
- STAC/DCAT & Neo4j alignment  
- AI explainability + ethics compliance  
- Provenance (PROV-O / CIDOC / GeoSPARQL)  
- Telemetry & sustainability tracking  
- MCP-DL v6.3 documentation and CI validation

Every pipeline—Remote Sensing, Historical, Hydrology, Hazard, Climate, Geospatial, AI—must follow these guides.

---

## 📁 Directory Layout

~~~~~text
docs/guides/pipelines/
├── README.md                           # This file (index)
│
├── gx-validate-promote.md              # Great Expectations Validate → Promote pattern
├── ingestion-guide.md                  # Ingestion & STAC polling best practices (future)
├── preprocessing-guide.md              # Cloud mask, GSD, reprojection, RTC (future)
├── analytics-guide.md                  # Index, hazard, composite, change workflows (future)
├── lineage-guide.md                    # Lineage & provenance patterns (future)
├── publishing-guide.md                 # STAC/DCAT/Neo4j/RDF publishing (future)
└── governance-integration.md           # CARE/Sovereignty governance bindings (future)
~~~~~

> Only completed document so far:  
> **`gx-validate-promote.md`** — the canonical KFM validation→promotion workflow.

---

## 🧩 Pipeline Lifecycle (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Ingestion<br/>STAC · ETL · Raw Data"] --> B["Preprocessing<br/>cloud mask · RTC · reprojection"]
  B --> C["Analytics<br/>indices · hazards · composites"]
  C --> D["Validate<br/>Great Expectations Checkpoints"]
  D -->|PASS| E["Promote<br/>Staging → Processed"]
  D -->|FAIL| Q["Quarantine<br/>Issue · Telemetry · Governance"]
  E --> F["Publish<br/>STAC · DCAT · Neo4j · RDF"]
  F --> G["Lineage<br/>PROV-O · GeoSPARQL · CARE"]
  G --> H["Telemetry<br/>Energy · CO₂e · Metrics"]
  H --> I["Governance<br/>Ledgers · FAIR+CARE Audit"]
~~~~~

---

## 📚 Completed Guides

### **🧪 Great Expectations Validate → Promote Pipeline Guide**  
`gx-validate-promote.md`  
Defines the authoritative KFM pattern for:

- Validation → Staging → Promotion  
- GX checkpoints  
- FAIR+CARE gating  
- Quarantine workflows  
- Lineage & telemetry hooks  
- STAC/DCAT/Neo4j/RDF publishing triggers  

This guide is **mandatory** for all KFM pipelines.

---

## 🛠️ Guides To Be Authored (Scaffolds)

### **Ingestion Guide**
Will define:

- ETag-aware STAC polling  
- Batch JSONL structure  
- URL/backoff/retry rules  
- AOI filtering  
- Telemetry requirements

### **Preprocessing Guide**
Will define:

- Cloud masking  
- Harmonized GSD  
- Reprojection pipelines  
- SAR terrain correction  
- Thermal normalization  
- CARE masking utilities

### **Analytics Guide**
Will define:

- Spectral index calculation  
- Hazard detection  
- Change detection  
- Composite generation  
- Summary metrics

### **Lineage Guide**
Will define:

- PROV-O/CIDOC/GeoSPARQL alignment  
- JSON-LD lineage records  
- Governance ledger entries  
- Telemetry cross-linking

### **Publishing Guide**
Will define:

- STAC Item/Collection publication  
- DCAT 3.0 mapping  
- Neo4j Scene/County/AOI graph edges  
- RDF/JSON-LD export  

### **Governance Integration Guide**
Will define:

- CARE rule enforcement  
- Sensitive AOI masking  
- Sovereignty constraints  
- Ethical AI logging  
- FAIR+CARE compliance system

---

## ⚖️ FAIR+CARE Integration Summary

All guides enforce the following:

| Principle | Implementation |
|----------|----------------|
| **Findable** | STAC/DCAT metadata; global IDs; versioning |
| **Accessible** | Open formats; public catalogs; schema-linked docs |
| **Interoperable** | JSON-LD, PROV-O, GeoSPARQL, CIDOC CRM |
| **Reusable** | Pipelines documented, validated, reproducible |
| **CARE** | Cultural/heritage masking; sovereignty gates; ethical constraints |

Governance logs written to:

~~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~~

---

## 📡 Telemetry Summary

All pipeline guides require:

- NDJSON telemetry per stage  
- Energy + CO₂ tracking  
- CARE violation logs  
- AI refusal logs (if applicable)  
- Aggregation to:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary |
|---------|------------|------------------------|---------|
| v10.3.1 | 2025-11-14 | Pipeline Governance Team | Initial pipeline guides index; aligned with MCP-DL v6.3 & KFM Protocol. |

---

<div align="center">

**Kansas Frontier Matrix — Pipeline Guides**  
Deterministic Pipelines × FAIR+CARE × Reproducible Science × Governance by Design  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>

