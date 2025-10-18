<div align="center">

# 📂 Kansas Frontier Matrix — **Data Integration Review Template**  
`docs/integration/reviews/templates/data_review_template.md`

**Purpose:** Standardize **dataset and metadata reviews** for the  
**Kansas Frontier Matrix (KFM)** — ensuring all geospatial, tabular, and textual datasets  
comply with **MCP-DL v6.3**, **STAC 1.0**, and **DCAT 2.0** standards for provenance,  
formatting, and reproducibility.

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../../.github/workflows/docs-validate.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![Aligned · STAC · DCAT · CIDOC CRM](https://img.shields.io/badge/Aligned-STAC%20%7C%20DCAT%20%7C%20CIDOC%20CRM-green)](../../../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
title: "Data Integration Review Template"
document_type: "Review Template · Dataset"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-data","@kfm-architecture","@kfm-review-board"]
status: "Stable"
scope: "Docs/Integration/Reviews/Templates"
tags: ["review","data","dataset","integration","stac","provenance"]
license: "CC-BY 4.0"
audit_framework: "MCP-DL v6.3"
---
````

---

## 🧭 Overview

This template is used during **data integration reviews** to confirm datasets meet
the Kansas Frontier Matrix’s reproducibility, quality, and semantic interoperability requirements.
It applies to **geospatial layers**, **tabular datasets**, and **document-derived data products**.

> Reviewers should complete all sections below and commit this filled form
> to `docs/integration/reviews/logs/YYYY-MM-DD_<dataset>.md`.

---

## 📦 Dataset Information

| Field                | Description                      | Example                                 |
| :------------------- | :------------------------------- | :-------------------------------------- |
| **Dataset Name**     | Name of the dataset or source    | `kansas_treaties`                       |
| **Source Path**      | File location in repo            | `data/sources/treaties/usfs_royce.json` |
| **Data Type**        | Vector / Raster / Tabular / Text | `Vector (GeoJSON)`                      |
| **Responsible Team** | Data owners / maintainers        | `@kfm-data`, `@kfm-geo`                 |
| **Submission Date**  | ISO 8601 date                    | `2025-10-18`                            |
| **Reviewer(s)**      | Assigned reviewers               | `geospatial_a`, `historian_b`           |

---

## 🧩 Validation Checklist

| Check                          | Description                                                    | Status |
| :----------------------------- | :------------------------------------------------------------- | :----- |
| [ ] **STAC Schema Validation** | `stac validate` passes; conforms to STAC 1.0 spec.             |        |
| [ ] **DCAT Metadata**          | `license`, `temporal`, `spatial`, `provenance` fields present. |        |
| [ ] **Checksum Verified**      | `.sha256` validated under `data/checksums/`.                   |        |
| [ ] **Format Compliance**      | Open standard: GeoJSON, GeoTIFF (COG), CSV, or Parquet.        |        |
| [ ] **CRS Standardization**    | Spatial reference = EPSG:4326 (WGS84).                         |        |
| [ ] **Temporal Coverage**      | Start and end dates defined; ISO 8601 compliant.               |        |
| [ ] **Bounding Box Accuracy**  | Matches Kansas region (or subset).                             |        |
| [ ] **Attribution & License**  | License type recorded; source URL included.                    |        |
| [ ] **Visualization Test**     | Displays properly in web frontend (`make serve`).              |        |
| [ ] **Provenance Log**         | Source lineage documented (`data/sources/*.json`).             |        |

---

## 🧮 Data Quality Assessment

| Metric                 | Criteria                                | Result / Notes |
| :--------------------- | :-------------------------------------- | :------------- |
| **Completeness**       | % of missing or null fields             |                |
| **Accuracy**           | Cross-check with external datasets      |                |
| **Consistency**        | Metadata uniformity across fields       |                |
| **Resolution / Scale** | Spatial or temporal resolution adequate |                |
| **Duplication**        | Duplicates removed / consolidated       |                |
| **Metadata Depth**     | Comprehensive, human-readable metadata  |                |

---

## 🧠 Ontology & Semantic Alignment

**Standards Referenced:**

* STAC 1.0 (Spatial/Temporal Asset Catalog)
* DCAT 2.0 (Data Catalog Vocabulary)
* CIDOC CRM (Cultural-historical semantics)
* OWL-Time (Temporal intervals)
* PROV-O (Provenance Ontology)

| Mapping                    | Example                                          |
| :------------------------- | :----------------------------------------------- |
| `E53_Place`                | GeoJSON geometry (treaty polygon, fort location) |
| `E52_Time-Span`            | Dataset temporal coverage (1820–1876)            |
| `E63_Provenance Statement` | Source attribution in metadata                   |
| `E31_Document`             | Linked treaty text or supporting record          |

---

## 🧾 Review Summary

| Field                  | Notes |
| :--------------------- | :---- |
| **General Findings**   |       |
| **Issues Identified**  |       |
| **Actions Taken**      |       |
| **Follow-up Required** |       |

**Decision:** ☐ Approved  ☐ Conditional Approval  ☐ Revisions Required

---

## 🗃 YAML Review Record (Append to Audit Log)

```yaml
dataset: kansas_treaties
review_type: data
reviewers: ["geospatial_a","historian_b"]
status: approved
validation:
  stac: pass
  checksum: verified
  license: CC-BY-4.0
notes: "Royce polygons and metadata validated; CRS standardized to EPSG:4326."
timestamp: 2025-10-18T14:30:00Z
```

---

## 🔗 References

* [`data/sources/*.json`](../../../../data/sources/) — Source manifests
* [`data/stac/*.json`](../../../../data/stac/) — STAC items for datasets
* [`docs/integration/reviews/checklist.md`](../checklist.md) — Full review checklist
* [`docs/standards/metadata.md`](../../../standards/metadata.md) — Metadata validation schema
* [`docs/architecture/data-architecture.md`](../../../architecture/data-architecture.md) — Repository data flow

---

<div align="center">

### 🧩 “Each dataset reviewed adds a verified layer to Kansas’s living digital history.”

**Kansas Frontier Matrix Review Council · MCP-DL v6.3**

</div>
