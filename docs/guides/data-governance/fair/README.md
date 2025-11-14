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
This guide ensures that all KFM data outputs comply with **international metadata standards**, **open-data policy**, **scientific reproducibility**, and the **Master Coder Protocol (MCP-DL v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)]()  
[![FAIR Certified](https://img.shields.io/badge/FAIR-Certified-gold.svg)]()  
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Aligned-blue.svg)]()  
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The Kansas Frontier Matrix implements **FAIR principles** as foundational requirements for:

- Data submission  
- ETL pipelines  
- Graph/ontology integration  
- STAC/DCAT catalog publication  
- Scientific reproducibility  
- Governance & audit logs  

FAIR compliance is **mandatory** for every dataset, STAC Item, and metadata contract.

---

## 🧭 FAIR Compliance Workflow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Dataset Submission<br/>(Data Contract + Issue Form)"]
    --> B["FAIR Completeness Check<br/>(Schema, ID, License, Metadata)"]
  B --> C["Interoperability Validation<br/>(STAC · DCAT · ISO19115)"]
  C --> D["Reusability Verification<br/>(Licensing · Versioning · Provenance)"]
  D --> E["FAIR Status Assigned<br/>faircare_validator.py"]
  E --> F["Governance Ledger Update<br/>Telemetry Export"]
~~~~~

---

## 🟦 F — Findable

FAIR-compliant datasets must be **easily discoverable** by both humans and machines.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| **Global Unique ID** | Dataset ID + STAC ID + graph entity ID | `schema_check.py` |
| **Indexed Metadata** | Searchable fields: title, keywords, bbox, temporal range | STAC/DCAT |
| **Catalog Entry** | Listed under `data/stac/` and `dcat_exports/` | STAC/DCAT bridge |
| **DOI (Optional)** | Recommended for major releases | Governance Council |

### Required Fields (Minimum)

```
id, title, description, keywords, license, spatial, temporal
```

---

## 🟩 A — Accessible

Access must be **authorized, documented, and persisted**.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| **Open Formats** | GeoJSON, Parquet, CSV, NetCDF, COG | STAC validation |
| **License Clarity** | SPDX or CC license required | FAIR+CARE validator |
| **Stable URLs** | Data-access URLs must be permanent | Link checker |
| **Machine-Readable** | JSON + JSON-LD required | Schema validator |

**No dataset may be published without a valid license.**

---

## 🟧 I — Interoperable

Interoperability ensures that data can be used across systems, ontologies, and software.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| **STAC 1.0** | Must include a valid STAC Item or Collection | `stac-validate.yml` |
| **DCAT 3.0** | Dataset-level export | DCAT converter |
| **ISO 19115 Alignment** | Spatial/temporal metadata required | Schema validator |
| **Ontology Linkages** | CIDOC CRM / GeoSPARQL when applicable | Graph loader |

### Required Metadata Fields

```
bbox, geometry (if applicable), datetime, start/end, asset roles, MIME types
```

---

## 🟨 R — Reusable

Reusability guarantees that other researchers, agencies, or community groups can build upon KFM datasets.

### Requirements

| Requirement | Description | Verified By |
|------------|-------------|-------------|
| **Clear Licensing** | MUST specify reuse rights | FAIR+CARE validator |
| **Provenance Metadata** | Must provide dataset lineage | Checksum audit |
| **Versioning** | Semantic dataset version required | Data contract |
| **FAIR Documentation** | README + contract + STAC metadata | Docs lint / validator |

---

## 🧾 Example FAIR Metadata Contract Snippet

~~~~~json
{
  "id": "noaa_drought_index_1980_2025",
  "title": "NOAA Drought Severity Index (1980–2025)",
  "description": "Long-term drought index for Kansas compiled from NOAA climate records.",
  "keywords": ["climate", "drought", "NOAA", "historic"],
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

## 🗂️ Where FAIR Outputs Are Stored

~~~~~text
data/reports/fair/
├── summary.json
├── data_care_assessment.json
└── fair_status_history.json
~~~~~

- `summary.json` — FAIR score summary  
- `data_care_assessment.json` — full FAIR+CARE evaluation  
- `fair_status_history.json` — longitudinal FAIR scoring log  

---

## 🧠 FAIR Enforcement in Self-Validation

Every dataset submitted triggers these workflows:

| Workflow | Purpose |
|----------|----------|
| `stac-validate.yml` | STAC/DCAT schema validation |
| `faircare-validate.yml` | FAIR+CARE metadata + license review |
| `docs-lint.yml` | Checks README, contract completeness |
| `telemetry-export.yml` | Energy, CO₂e, runtime |

Only datasets with **FAIR compliance = true** may advance to *staging → processed → publication*.

---

## 📚 Cross-References

- **Self-Validation Guide:** `../self-validation/README.md`  
- **FAIR+CARE Standard:** `../../../standards/faircare.md`  
- **Governance Charter:** `../../../standards/governance/ROOT-GOVERNANCE.md`  
- **Data Architecture:** `../../../../data/ARCHITECTURE.md`  
- **Validation Tools:** `../../../../tools/validation/README.md`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | FAIR+CARE Council | Initial FAIR governance guide for v10.3 system. |

---

<div align="center">

**Kansas Frontier Matrix — FAIR Governance Guide**  
Findable × Accessible × Interoperable × Reusable  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Data Governance](../README.md)

</div>

