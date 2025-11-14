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

The Kansas Frontier Matrix implements **FAIR principles** as foundational requirements for:

- Data submission  
- ETL pipelines and transformations  
- Neo4j/ontology integration  
- STAC/DCAT catalog publication  
- Self-validation and governance audits  

FAIR compliance is **mandatory** for every dataset, STAC Item, and metadata contract.

---

## 🧭 FAIR Compliance Workflow (Indented Mermaid)

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
| Global Unique ID | Dataset ID + STAC ID + graph node ID | `schema_check.py` |
| Indexed Metadata | Searchable fields: title, description, keywords, bbox, temporal range | STAC/DCAT validators |
| Catalog Entry | Dataset appears in STAC/DCAT catalogs | STAC↔DCAT bridge |
| DOI (Recommended) | Major datasets may receive DOIs | FAIR+CARE Council |

**Minimum fields:** `id`, `title`, `description`, `keywords`, `license`, `spatial`, `temporal`.

---

## 🟩 A — Accessible

Access must be **stable and appropriately governed**.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| Open Formats | GeoJSON, Parquet, CSV, NetCDF, COG | STAC validation |
| License Clarity | SPDX or CC license required | FAIR+CARE validator |
| Stable URLs | Data-access URLs must be reliable | Link checks |
| Machine-Readable | JSON/JSON-LD metadata required | Schema validators |

No dataset is published without a valid license.

---

## 🟧 I — Interoperable

Interoperability ensures data is usable across platforms and domains.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| STAC 1.0 | Valid Item/Collection | `stac-validate.yml` |
| DCAT 3.0 | Dataset-level export | DCAT exporter |
| ISO 19115 | Aligned spatial/temporal metadata | Schema validation |
| Ontology Links | CIDOC CRM / GeoSPARQL when applicable | Graph loader |

Metadata must include:

- `bbox`  
- `geometry` (if applicable)  
- `datetime` or `start` + `end`  
- Asset roles + MIME types  

---

## 🟨 R — Reusable

Reusability guarantees **long-term value and transparency**.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| Clear Licensing | Rights and reuse terms explicit | FAIR+CARE validator |
| Provenance Metadata | Data lineage and source history | `checksum_audit.py` |
| Versioning | Semantic dataset version | Data contract + CI checks |
| FAIR Documentation | README + contract + STAC metadata | `docs-lint.yml`, `schema_check.py` |

---

## 🧾 Example FAIR Contract Snippet

~~~~~json
{
  "id": "noaa_drought_index_1980_2025",
  "title": "NOAA Drought Severity Index (1980–2025)",
  "description": "Long-term drought index for Kansas compiled from NOAA climate records.",
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
├── summary.json                 # FAIR scores & summaries
├── data_care_assessment.json    # FAIR+CARE evaluations
└── fair_status_history.json     # FAIR status over time
~~~~~

---

## 🧠 FAIR in Self-Validation

Every dataset added or changed triggers:

| Workflow | Purpose |
|----------|---------|
| `stac-validate.yml` | STAC/DCAT schema validation |
| `faircare-validate.yml` | FAIR+CARE & license audit |
| `docs-lint.yml` | Documentation structure check |
| `telemetry-export.yml` | Collects energy, CO₂e, runtime metrics |

Only datasets with **FAIR-compliant** status can progress to **staging → processed → publication**.

---

## 📚 Cross-References

- `../README.md` — Data Governance Guide  
- `../self-validation/README.md` — Self-Validation Guide  
- `../audit/README.md` — Audit Guide  
- `../../../../data/ARCHITECTURE.md` — Data Architecture Spec  
- `../../../../tools/validation/README.md` — Validation Tools Registry  
- `../../../standards/faircare.md` — FAIR+CARE Standard  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | FAIR+CARE Council | Initial FAIR governance guide aligned to v10.3.0 telemetry & workflows. |

---

<div align="center">

**Kansas Frontier Matrix — FAIR Governance Guide**  
Findable × Accessible × Interoperable × Reusable  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Data Governance Guide](../README.md)

</div>
