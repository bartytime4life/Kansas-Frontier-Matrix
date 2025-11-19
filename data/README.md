---
title: "📦 Kansas Frontier Matrix — Data Directory Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/README.md"

version: "v11.0.1"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-readme-v11.0.1"
semantic_document_id: "kfm-doc-data-root"
event_source_id: "ledger:data/README.md"
immutability_status: "mutable-plan"

sbom_ref: "../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../releases/v11.0.1/manifest.zip"
telemetry_ref: "../releases/v11.0.1/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-directory-v1.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "data-directory"
role: "repository-data-overview"
category: "Data · Metadata · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Mixed"
sensitivity_level: "Variable"
risk_category: "Low to Medium"
indigenous_rights_flag: false
redaction_required: false

machine_extractable: true
classification: "Public Document"
jurisdiction: "United States / Kansas"
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next data-directory update"
---

# 📦 Kansas Frontier Matrix — Data Directory Overview

This folder contains **all data used in the Kansas Frontier Matrix**, organized into a transparent, FAIR+CARE-governed, reproducible pipeline structure.

All contents follow:

- **MCP-DL v6.3**
- **KFM-MDP v11**
- **KFM-OP v11 ontology mapping**
- **STAC 1.x / DCAT 3.0 metadata**
- **FAIR+CARE governance and sovereignty rules**
- **Checksum lineage + manifest verification**

---

## 📘 Purpose

The `data/` directory provides:

- A deterministic, reproducible structure for all KFM datasets  
- A predictable flow from raw → staging → processed → catalogs  
- FAIR+CARE protections, including license enforcement and sovereignty controls  
- Telemetry-backed validation (energy, carbon, schema compliance)  
- Governance logging for all sensitive assets  

---

## 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/
├── README.md                      ← this file
│
├── raw/                           ← Unmodified source datasets (immutable)
│   ├── historic/                  ← Maps, manuscripts, diaries, archival scans
│   ├── environmental/             ← NOAA, PRISM, Daymet, USGS, Mesonet
│   ├── cultural/                  ← Tribal, Indigenous, heritage datasets (H3-masked)
│   └── geology/                   ← DEMs, lithologic maps, KGS datasets
│
├── staging/                       ← Cleaned + normalized intermediates (ETL only)
│   ├── tables/                    ← Tabular cleaned files
│   ├── spatial/                   ← GeoJSON, GPKG, COG tiles
│   └── metadata/                  ← Pre-STAC/DCAT metadata bundles
│
├── processed/                     ← Pipeline outputs (deterministic)
│   ├── hydrology/                 ← Streamflow, flood history, watersheds
│   ├── climate/                   ← Climate normals, anomalies, extremes
│   ├── ecology/                   ← Biodiversity, vegetation index, GBIF/eBird merges
│   └── historical/                ← Generalized historical datasets
│
├── stac/                          ← STAC Items, Collections, Catalog
│   ├── items/
│   ├── collections/
│   └── catalog.json
│
├── dcat/                          ← DCAT 3.0 JSON-LD datasets + distributions
│
├── archive/                       ← Versioned snapshots + retired datasets
│
├── checksums/                     ← SHA-256 lineage verification
│   ├── raw/
│   ├── processed/
│   └── stac/
│
├── reports/                       ← Validation + FAIR+CARE outputs
│   ├── self-validation/           ← Schema, CARE, checksum reports
│   └── telemetry/                 ← Sustainability & performance telemetry
│
└── work/                          ← Local scratch; not used in production
~~~~

---

## 🔄 Data Lifecycle Flow

~~~~mermaid
flowchart TD
  A["raw/ (immutable sources)"]
    --> B["staging/\n(clean + normalized)"]

  B --> C["processed/\n(ETL results)"]

  C --> D["stac/ + dcat/\n(catalogs + metadata)"]

  D --> E["checksums/\nSHA-256 lineage"]

  E --> F["reports/self-validation/\nFAIR+CARE · Schema · Lineage"]

  F --> G["focus-telemetry.json"]
~~~~

---

## 🧪 Validation & Compliance

All datasets pass through:

### **1. Schema Validation**
- STAC 1.x / DCAT 3.0  
- JSON Schema / SHACL  
- Internal Data Contracts v3  

### **2. FAIR+CARE Governance**
- CARE labels for cultural/Indigenous data  
- Spatial masking (H3) where needed  
- License + rights validation  
- Sovereignty policy enforcement  

### **3. Cryptographic Integrity**
- SHA-256 lineage logs  
- Manifest consistency (SBOM/manifest)  
- Change detection across releases  

### **4. Sustainability Signals**
- energy_wh  
- carbon_gco2e  
- throughput  
- resource efficiency  

Validation outputs live in:

~~~~text
data/reports/self-validation/*
docs/reports/audit/*
releases/*/focus-telemetry.json
~~~~

---

## 🧬 STAC / DCAT Integration

Every dataset promoted to production MUST have:

- A **STAC Item**  
- A **STAC Collection** (if grouped)  
- A **DCAT Dataset**  
- A **JSON-LD lineage context**  

Stable identifier: `kfm_id`.

---

## 🧠 Contributor Guidance

Before opening a PR:

- Validate all geometry  
- Provide complete provenance  
- Supply CARE labels / cultural sensitivity notes  
- Ensure CRS is EPSG:4326 unless specified otherwise  
- Provide checksum (SHA-256)  
- Follow the **Data Submission Template**:

~~~~text
.github/ISSUE_TEMPLATE/data_submission.yml
~~~~

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.0.1 | 2025-11-19 | Rewritten using hardened v11 fence rules; GitHub-safe; aligned with data architecture v11. |
| v11.0.0 | 2025-11-19 | Initial v11 dataset directory documentation. |

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.0 · KFM-OP v11.0  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Repository Root](../README.md)  
[Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
