---
title: "📊 Kansas Frontier Matrix — Historical Results: Tables (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/historical/results/tables/README.md"
version: "v10.2.2"
last_updated: "2025-11-11"
review_cycle: "Quarterly / FAIR+CARE Data Standards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/analyses-historical-results-tables-v3.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Historical Results: Tables**  
`docs/analyses/historical/results/tables/README.md`

**Purpose:**  
Document and catalogue all **tabular output artifacts** generated within the Historical Domain Results workflows of the Kansas Frontier Matrix (KFM).  
These tables capture population dynamics outputs, archival correlation results, energy & governance summaries—each aligned to FAIR+CARE standards and governed under Master Coder Protocol v6.3.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Historical-orange)](../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)  
[![Status: Active](../../releases/v10.2.0/manifest.zip)](../../releases/v10.2.0/manifest.zip)

</div>

---

## 📘 Overview

This folder holds all tabular artifacts produced as final outputs in the historical results stream: CSV files of model outputs, validation logs, sustainability metrics, and archival-dataset indexes.  
Tables are structured to support reproducibility, cross-domain interoperability, and FAIR+CARE governance.

---

## 🗂️ Directory Layout

```bash
docs/analyses/historical/results/tables/
 ├── README.md
 ├── population-dynamics-model.csv              # Reconstructed population model outcomes 1850-1950
 ├── archival-correlation-results.csv            # Harmonised archival record links and metadata
 ├── energy-sustainability-log.csv               # Energy usage and carbon footprint for results workflows
 └── method-validation-summary.csv                # Methods model validation and provenance metrics
```

Each table includes an embedded metadata side-car (JSON or YAML) listing dataset IDs, columns, units, provenance references, checksum and generation date.

---

## 🧾 Table Descriptions

| File                                           | Description                                             | Format |
|------------------------------------------------|---------------------------------------------------------|--------|
| `population-dynamics-model.csv`                 | Modelled population estimates and migration fluxes 1850–1950 | CSV    |
| `archival-correlation-results.csv`              | Table linking archival materials, treaties, spatial location | CSV    |
| `energy-sustainability-log.csv`                  | Tabulation of energy (kWh), emissions (gCO₂e), runtime   | CSV    |
| `method-validation-summary.csv`                  | Validation results (RMSE, bias, completeness) for methods used | CSV    |

---

## ⚖️ FAIR+CARE Governance Summary

| Principle             | Implementation                                                | Verification Source            |
|------------------------|---------------------------------------------------------------|--------------------------------|
| **Findable**           | Tables indexed with persistent UUID and catalog metadata      | `manifest_ref`                 |
| **Accessible**         | CSV files licensed under CC-BY 4.0 and publicly archived      | FAIR+CARE Registry             |
| **Interoperable**      | Machine-readable CSV with metadata side-cars (JSON-LD)        | `telemetry_schema`             |
| **Reusable**           | Provenance, licensing, and versioning included in metadata    | Metadata side-cars             |
| **Collective Benefit** | Data supports cross-domain research and heritage studies     | FAIR+CARE Audit                |
| **Authority to Control**| Sensitive cultural data aggregated/protected appropriately   | IDGB Consent Records           |
| **Responsibility**     | Energy, runtime and emissions tracked across workflows        | `energy-sustainability-log.csv`|
| **Ethics**             | Anonymisation, aggregation and transparency for archival data | Governance Ledger              |

---

## 🕰️ Version History

| Version | Date       | Author                            | Summary                                  |
|---------|------------|-----------------------------------|------------------------------------------|
| v10.2.2 | 2025-11-11 | FAIR+CARE Historical Results Council | Published tables documentation aligned with v10.2 schema and governance protocols |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Historical Results](../README.md) · [Datasets →](../datasets/README.md)

</div>

