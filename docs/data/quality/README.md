---
title: "🧮 Kansas Frontier Matrix — Data Quality & Validation Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/quality/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Quarterly · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "LTS"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-quality-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
status: "Active / Enforced"
doc_kind: "Quality Framework"
header_profile: "standard"
footer_profile: "standard"
category: "Data · Quality · Validation"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
ttl_policy: "12 months"
provenance_chain:
  - "docs/data/quality/README.md@v10.0.0"
  - "docs/data/quality/README.md@v11.0.0"
  - "docs/data/quality/README.md@v11.1.0"
  - "docs/data/quality/README.md@v11.2.1"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🧮 **Kansas Frontier Matrix — Data Quality & Validation Framework**  
`docs/data/quality/README.md`

**Purpose**  
Define and enforce the complete **data quality, validation, and ethical auditing framework** for all datasets integrated into the Kansas Frontier Matrix (KFM).  
Ensures compliance with **FAIR+CARE**, **ISO 19157**, **DCAT 3.0**, **STAC 1.0**, and **Master Coder Protocol (MCP-DL v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare/FAIRCARE-GUIDE.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.2/manifest.zip)

</div>

---

## 📘 Overview

The **KFM Data Quality & Validation Framework (DQVF)** defines how all datasets are:

- Assessed for **structural integrity**  
- Validated for **metadata completeness**  
- Checked for **spatial accuracy** and CRS correctness  
- Verified for **provenance, consent, and lineage integrity**  
- Audited for **FAIR+CARE ethical quality**  
- Scored via a unified **Data Quality Index (DQI)**  
- Monitored continuously through telemetry + versioned audits  

This guarantees **scientific rigor**, **ethical stewardship**, and **reproducible ingestion** across all KFM pipelines.

---

## 🗂️ Directory Layout

~~~text
docs/data/quality/
├── 📄 README.md
├── 📊 completeness-audit.json
├── 🧩 metadata-lint.json
├── 🗺️ spatial-accuracy.json
└── 🧮 faircare-audit-summary.md
~~~

---

## ⚙️ Data Validation Workflows

| Workflow | Purpose | Frequency | Output |
|----------|---------|-----------|---------|
| `data-quality.yml` | Validates completeness, accuracy, & precision | Quarterly | `reports/data/completeness.json` |
| `metadata-lint.yml` | Ensures required DCAT/FAIR metadata | Continuous | `docs/data/quality/metadata-lint.json` |
| `data-provenance.yml` | Verifies lineage + consent metadata | Quarterly | `reports/data/provenance-summary.json` |
| `faircare-audit.yml` | CARE-based ethical quality review | Quarterly | `reports/data/faircare-validation.json` |

All reports are versioned and linked to the release manifest.

---

## 🧩 Validation Dimensions

### 1️⃣ Structural Integrity (Schema Compliance)
Every dataset must conform to **data-contract-v3.json**.

Checks include:

- JSON Schema Draft 2020-12 validation  
- Required field presence  
- Nullability + type enforcement  
- Cross-field logic (e.g., temporal range structure)  

Example failure:

~~~json
{
  "dataset_id": "ks_soils_1967",
  "field": "temporal.end",
  "error": "Invalid date format — expected ISO 8601"
}
~~~

---

### 2️⃣ Metadata Completeness (DCAT 3.0 + ISO 19115-1)

| Field | Required | Description |
|------|----------|-------------|
| `title` | ✅ | Dataset human-readable name |
| `description` | ✅ | Abstract of dataset scope |
| `spatial` | ✅ | Bounding box or footprint |
| `temporal` | ✅ | Start/end or interval |
| `provenance` | ✅ | Lineage + consent + authorship |
| `license` | ✅ | SPDX or CC identifier |
| `keywords` | — | For DCAT/STAC discovery |

Target threshold: **≥ 98% metadata coverage**.

---

### 3️⃣ Spatial Accuracy & CRS Validation

- All datasets must declare CRS (EPSG:4326 default)  
- Validate geometry with GeoPandas / Shapely  
- Enforce topology correctness (no self-intersections)  
- Reproject inconsistent CRS automatically  

Accuracy Target: **± 5 meters** (horizontal).

Tools: GDAL, pyproj, ogrinfo, QGIS CLI.

---

### 4️⃣ Provenance & Consent Verification (PROV-O)

Required fields:

~~~json
"provenance": {
  "creator": "Kansas Geological Survey",
  "source_url": "https://archivehub.kansasgis.org/1894_topo",
  "issued": "2025-04-02T00:00:00Z",
  "consent": "Approved under FAIR+CARE Council, 2025-Q2"
}
~~~

Datasets failing provenance validation are **blocked from production**.

---

### 5️⃣ FAIR+CARE Ethical Quality Validation

| CARE Principle | Requirement | Pass Criteria |
|---------------|-------------|---------------|
| **Collective Benefit** | Document value to communities | Required |
| **Authority to Control** | Verified cultural consent | 100% |
| **Responsibility** | Stewardship + review body | Required |
| **Ethics** | No harmful or sensitive content | 100% |

CARE failures → dataset marked **restricted**.

---

## 📊 Key Quality Metrics (DQI Dimensions)

| Metric | Definition | Target |
|--------|------------|---------|
| Schema Conformance | JSON Schema pass rate | 100% |
| Metadata Completeness | Required fields populated | ≥ 98% |
| Spatial Accuracy | Deviation from truth benchmarks | ≤ 5m |
| Checksum Integrity | Verified SHA256 hashes | 100% |
| Ethical Compliance | CARE-aligned fields validated | ≥ 90% |

---

## 🧮 Data Quality Index (DQI)

Weighted composite score:

~~~text
DQI = (S * 0.25) + (M * 0.25) + (P * 0.20) + (E * 0.30)
~~~

Where:

- **S** = Schema Conformance  
- **M** = Metadata Completeness  
- **P** = Provenance Integrity  
- **E** = Ethical Compliance  

**Passing threshold:** DQI ≥ 90  
**Remediation triggered:** DQI < 80

---

## 🧠 Continuous Validation Lifecycle

~~~mermaid
flowchart LR
A["📥 Raw Dataset"] --> B["⚙️ Schema + Metadata Validation"]
B --> C["🧭 Ethical + Provenance Review"]
C --> D["🧾 Telemetry + Lineage Logging"]
D --> E["📦 STAC/DCAT Publication"]
E --> F["🔁 Quarterly Re-Audit"]
~~~

---

## 🧾 Example Quality Report

~~~json
{
  "dataset_id": "usgs_historic_topo_1894",
  "schema_compliance": 100,
  "metadata_completeness": 98.5,
  "spatial_accuracy_m": 4.7,
  "faircare_score": 95,
  "dqi_score": 96.2,
  "status": "approved"
}
~~~

---

## ⚖️ Governance & Reporting

| Report | Maintainer | Frequency | Output |
|--------|------------|-----------|---------|
| Completeness Audit | Data QA Team | Quarterly | `completeness-audit.json` |
| Metadata Lint Summary | FAIR+CARE Council | Continuous | `metadata-lint.json` |
| Ethical Audit Report | FAIR+CARE Council | Biannual | `faircare-audit-summary.md` |
| Spatial QA Validation | GIS Engineers | Continuous | `spatial-accuracy.json` |

---

## 🕰️ Version History

| Version | Date | Summary |
|---------|---------|----------|
| v11.2.2 | 2025-11-27 | Updated to v11.2.2 standard; emoji directory; footer corrected; governance enhanced |
| v10.0.0 | 2025-11-10 | Initial publication of KFM Data Quality Framework |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📜 Data Contracts](../contracts/README.md) · [🛡️ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
