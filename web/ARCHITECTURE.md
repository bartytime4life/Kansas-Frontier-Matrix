---
title: "🌱 Kansas Frontier Matrix — FAIR Principles Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/data-governance/fair/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/fair-governance-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌱 **Kansas Frontier Matrix — FAIR Principles Guide**  
`docs/guides/data-governance/fair/README.md`

**Purpose:**  
Define the **FAIR (Findable, Accessible, Interoperable, Reusable)** data governance requirements for all datasets, metadata, and derived products within the Kansas Frontier Matrix (KFM).  
This guide ensures that all KFM data outputs comply with **international metadata standards**, **open-data policy**, **reproducible science**, and the **Master Coder Protocol (MCP-DL v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)]()  
[![FAIR Certified](https://img.shields.io/badge/FAIR-Certified-gold.svg)]()  
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Aligned-blue.svg)]()  
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The Kansas Frontier Matrix implements **FAIR principles** as baseline requirements for:

- Data submission and ingestion  
- ETL pipelines and transformations  
- Graph/ontology integration  
- STAC/DCAT catalog publishing  
- Self-validation and governance audits  

FAIR compliance is **mandatory** for every dataset, STAC Item, and data contract.

---

## 🧭 FAIR Compliance Workflow

~~~~~mermaid
flowchart TD
  A["Dataset Submission<br/>(Data Contract + Issue Form)"]
    --> B["FAIR Completeness Check<br/>(ID · License · Metadata)"]
  B --> C["Interoperability Validation<br/>(STAC · DCAT · ISO 19115)"]
  C --> D["Reusability Verification<br/>(Licensing · Versioning · Provenance)"]
  D --> E["FAIR Status Assigned<br/>(faircare_validator.py)"]
  E --> F["Governance Ledger Update<br/>Telemetry Export"]
~~~~~

---

## 🟦 F — Findable

FAIR-compliant datasets must be **discoverable**.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| Global Unique ID | Dataset ID + STAC ID + graph ID | `schema_check.py` |
| Indexed Metadata | Title, description, keywords, bbox, temporal coverage | STAC/DCAT validators |
| Catalog Entry | Dataset appears in STAC/DCAT catalogs | STAC↔DCAT bridge |
| DOI (Recommended) | Major datasets may receive DOIs | Governance Council |

**Minimum fields:**

- `id`, `title`, `description`, `keywords`, `license`, `spatial`, `temporal`

---

## 🟩 A — Accessible

Access must be **documented, secure, and sustainable**.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| Open Formats | CSV, Parquet, GeoJSON, NetCDF, COG | STAC validation |
| Explicit License | SPDX or CC license required | FAIR+CARE validator |
| Stable URLs | Data-access URLs must be resolvable | Link checks |
| Machine-Readable | JSON/JSON-LD for metadata | Schema validators |

No dataset is published without a **valid license**.

---

## 🟧 I — Interoperable

Interoperability ensures reuse across platforms, disciplines, and tools.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| STAC 1.0 | Valid Item/Collection per spec | `stac-validate.yml` |
| DCAT 3.0 | Dataset-level metadata export | DCAT exporter |
| ISO 19115 | Spatial/temporal metadata alignment | Schema check |
| Ontology Links | CIDOC CRM, GeoSPARQL where applicable | Graph loader |

**Metadata must include:**

- `bbox`, `geometry` (if applicable)  
- `datetime` or `start`/`end`  
- Asset roles + MIME types  

---

## 🟨 R — Reusable

Reusability ensures downstream users can **trust and extend** KFM datasets.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| Clear Licensing | Rights and reuse terms specified | FAIR+CARE validator |
| Provenance Metadata | Transformation + source lineage recorded | checksum_audit |
| Versioning | Semantic version in data contracts | Data stewards |
| FAIR Documentation | README + contract + STAC metadata | docs-lint + schema_check |

---

## 🧾 Example FAIR Contract Snippet

~~~~~json
{
  "id": "noaa_drought_index_1980_2025",
  "title": "NOAA Drought Severity Index (1980–2025)",
  "description": "Long-term drought index for Kansas from NOAA climate records.",
  "keywords": ["climate", "drought", "NOAA", "Kansas"],
  "license": "Public Domain",
  "spatial": [-102.05, 37.0, -94.6, 40.0],
  "temporal": { "start": "1980-01-01", "end": "2025-01-01" },
  "provenance": "NOAA NCEI",
  "checksum": "sha256:d4a8…",
  "care_label": "public",
  "version": "v1.0.0"
}
~~~~~

---

## 🗂️ FAIR Outputs & Storage

~~~~~text
data/reports/fair/
├── summary.json                 # FAIR scores and statuses
├── data_care_assessment.json    # Combined FAIR+CARE report
└── fair_status_history.json     # Historical FAIR evaluation log
~~~~~

---

## 🧠 FAIR in Self-Validation

Every dataset triggers:

| Workflow | Role |
|----------|------|
| `stac-validate.yml` | STAC/DCAT compliance |
| `faircare-validate.yml` | FAIR+CARE metadata audit |
| `docs-lint.yml` | Documentation completeness + formatting |
| `telemetry-export.yml` | Energy, CO₂e, and validation timing |

Only datasets with **FAIR-compliant** status proceed to **staging → processed → publication**.

---

## 📚 Cross-References

- `../self-validation/README.md` — Self-validation guide  
- `../audit/README.md` — Audit governance guide  
- `../../../../data/ARCHITECTURE.md` — Data architecture specification  
- `../../../../tools/validation/README.md` — Validation tooling registry  
- `../../../standards/faircare.md` — FAIR+CARE standard  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | FAIR+CARE Council | Initial v10.3 FAIR governance guide; workflow & examples aligned to new telemetry schema. |

---

<div align="center">

**Kansas Frontier Matrix — FAIR Governance Guide**  
Findable × Accessible × Interoperable × Reusable  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Data Governance Guide](../README.md)

</div>
