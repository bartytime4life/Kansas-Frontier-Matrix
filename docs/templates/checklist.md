<div align="center">

# ☑️ Kansas Frontier Matrix — Review & Validation Checklist Template  
`docs/templates/checklist.md`

**Purpose:** Provide a **structured, MCP-aligned checklist** for validating datasets, pipelines, documentation, or workflows  
before approval, deployment, or publication within the **Kansas Frontier Matrix (KFM)**.  
This template standardizes reviews across data, code, metadata, and documentation artifacts.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🧭 Checklist Metadata

| Field | Description |
|:------|:-------------|
| **Checklist ID** | Unique identifier (e.g., `CHECK-2025-001-CLIMATE`) |
| **Title** | Short descriptive title for the review checklist |
| **Reviewer(s)** | Name(s) of person(s) performing validation |
| **Date Completed** | YYYY-MM-DD |
| **Review Type** | Data / Pipeline / Documentation / Metadata / CI/CD / Model / Experiment |
| **Associated Item(s)** | Link to dataset, SOP, experiment, ADR, or workflow |
| **Status** | Draft / In Review / Approved / Rejected |
| **Version** | v1.0, v1.1, etc. |

---

## 🧾 Review Objective

Provide a short summary of **what this review or validation aims to confirm.**

> Example:  
> *Validate the metadata and STAC compliance of the `ks_1m_dem_2018_2020.tif` dataset prior to integration  
> into the processed terrain layer and web catalog.*

---

## 🧩 Section 1 — Documentation Completeness

| Requirement | Description | Status | Notes |
|:--------------|:-------------|:----------|:---------|
| ✅ **README.md Present** | Directory contains clear documentation | ☐ / ✅ |  |
| ✅ **Metadata File Present** | STAC or JSON metadata file exists and passes validation | ☐ / ✅ |  |
| ✅ **Version Info Included** | Version/date recorded in dataset or document header | ☐ / ✅ |  |
| ✅ **Author(s) & License Listed** | Attribution and license specified | ☐ / ✅ |  |
| ✅ **Cross-links Added** | Links to related docs or datasets verified | ☐ / ✅ |  |

---

## 🧩 Section 2 — Reproducibility & Workflow Validation

| Requirement | Description | Status | Notes |
|:--------------|:-------------|:----------|:---------|
| ✅ **Makefile Target Defined** | Dataset or process has reproducible `make` target | ☐ / ✅ |  |
| ✅ **Config File Versioned** | YAML/JSON config stored and linked | ☐ / ✅ |  |
| ✅ **Pipeline Script Versioned** | Code linked to a commit or tagged release | ☐ / ✅ |  |
| ✅ **Checksum Verified** | SHA-256 checksum file exists and passes validation | ☐ / ✅ |  |
| ✅ **Automation Tested** | Workflow runs successfully in CI/CD | ☐ / ✅ |  |
| ✅ **Logs Generated** | Process log written to `data/work/logs/` | ☐ / ✅ |  |

---

## 🧩 Section 3 — Open Standards Compliance

| Requirement | Description | Status | Notes |
|:--------------|:-------------|:----------|:---------|
| ✅ **STAC Schema Valid** | Validates against STAC 1.0.0 JSON Schema | ☐ / ✅ |  |
| ✅ **File Formats Open** | Data stored as open formats (GeoTIFF, CSV, JSON, etc.) | ☐ / ✅ |  |
| ✅ **Projection / CRS Valid** | Geospatial datasets use standard EPSG codes | ☐ / ✅ |  |
| ✅ **Metadata Schema Valid** | JSON Schema validation completed | ☐ / ✅ |  |
| ✅ **Web Accessibility** | Data and metadata accessible through API or web | ☐ / ✅ |  |

---

## 🧩 Section 4 — Provenance & Lineage Tracking

| Requirement | Description | Status | Notes |
|:--------------|:-------------|:----------|:---------|
| ✅ **Source Manifest Linked** | Entry exists in `data/sources/` | ☐ / ✅ |  |
| ✅ **Checksum Chain Complete** | Every transformation step has validation hash | ☐ / ✅ |  |
| ✅ **STAC Relationships Defined** | `"derived_from"`, `"rel:source"`, etc. present | ☐ / ✅ |  |
| ✅ **Provenance Record Created** | Corresponding record in `docs/templates/provenance.md` | ☐ / ✅ |  |
| ✅ **Knowledge Graph Entry** | Dataset modeled in RDF / CIDOC / PROV-O | ☐ / ✅ |  |

---

## 🧩 Section 5 — Auditability & CI/CD Verification

| Requirement | Description | Status | Notes |
|:--------------|:-------------|:----------|:---------|
| ✅ **CI Logs Available** | Workflow logs stored in `data/work/logs/ci/` | ☐ / ✅ |  |
| ✅ **Validation Report Generated** | Markdown or JSON report produced | ☐ / ✅ |  |
| ✅ **Security Scan Passed** | CodeQL / Trivy scans successful | ☐ / ✅ |  |
| ✅ **Approval Workflow Complete** | PR merged only after successful checks | ☐ / ✅ |  |
| ✅ **Build Version Logged** | Build tagged and versioned for future reference | ☐ / ✅ |  |

---

## 🧩 Section 6 — Quality & Review Notes

Summarize reviewer observations, anomalies, or corrective actions.

> **Example:**  
> - Missing `derived_from` field in STAC metadata.  
> - Dataset checksum updated after reprocessing.  
> - All STAC validations passed; approved for integration.

---

## 🧠 MCP Compliance Review

| MCP Principle | Validation Status | Notes |
|:---------------|:------------------|:----------|
| **Documentation-first** | ☐ / ✅ | Documentation exists before data release |
| **Reproducibility** | ☐ / ✅ | Results reproducible via ETL and CI/CD |
| **Open Standards** | ☐ / ✅ | STAC, GeoTIFF, JSON Schema used |
| **Provenance** | ☐ / ✅ | Source → Process → Output lineage documented |
| **Auditability** | ☐ / ✅ | CI/CD logs and approvals recorded |

---

## 🧾 Reviewer Sign-Off

| Role | Reviewer Name | Date | Decision | Signature / Initials |
|:-------|:----------------|:------|:----------|:----------------|
| **Primary Reviewer** |  |  | ✅ Approved / ❌ Revisions Required |  |
| **Data Governance Lead** |  |  | ✅ Approved / ❌ Revisions Required |  |
| **Automation / CI Engineer** |  |  | ✅ Approved / ❌ Revisions Required |  |
| **Documentation Steward** |  |  | ✅ Approved / ❌ Revisions Required |  |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | All deliverables reviewed for completeness and clarity. |
| **Reproducibility** | Verified through deterministic builds and checksums. |
| **Open Standards** | Ensured via schema and STAC validation. |
| **Provenance** | Source lineage confirmed and documented. |
| **Auditability** | Review logs and approvals tracked for governance. |

---

## 📎 Related Documentation

| File | Description |
|:------|:-------------|
| `docs/templates/dataset.md` | Dataset documentation template. |
| `docs/templates/sop.md` | SOP defining how reviews are performed. |
| `docs/templates/provenance.md` | Provenance record template for lineage. |
| `docs/architecture/ci-cd.md` | Continuous integration and audit flow. |
| `.github/workflows/pre-commit.yml` | Workflow for automated style and consistency checks. |

---

## 📅 Version History

| Version | Date | Author | Summary |
|:---------|:------|:----------|:----------|
| v1.0 | 2025-10-04 | KFM Documentation Team | Initial standardized validation checklist for MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Review Documented. Every Validation Proven.”*  
📍 [`docs/templates/checklist.md`](.) · Template for MCP-compliant review and validation checklists across the KFM ecosystem.

</div>
