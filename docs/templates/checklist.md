<div align="center">

# ☑️ Kansas Frontier Matrix — Review & Validation Checklist Template  
`docs/templates/checklist.md`

**Mission:** Deliver a **comprehensive, MCP-aligned checklist** for validating datasets, pipelines, documentation, and workflows  
prior to approval, deployment, or publication within the **Kansas Frontier Matrix (KFM)**.  
This ensures every artifact — code, data, or document — is **auditable, reproducible, and standardized**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![Validation](https://img.shields.io/badge/Checklist-Standardized-brightgreen)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

## 🧭 Checklist Metadata

| Field | Description |
|:------|:-------------|
| **Checklist ID** | Unique ID (e.g., `CHECK-2025-001-TERRAIN`) |
| **Title** | Descriptive name for review |
| **Reviewer(s)** | Name(s) of validators |
| **Date Completed** | YYYY-MM-DD |
| **Review Type** | Data / Pipeline / Documentation / Model / Workflow / Governance |
| **Associated Artifacts** | Dataset, ADR, SOP, experiment, or workflow being reviewed |
| **Status** | Draft / In Review / Approved / Revisions Required |
| **Version** | v1.0, v1.1, etc. |

---

## 🎯 Review Objective

Summarize what the review aims to validate or verify.

> *Example:*  
> Confirm that the `ks_1m_dem_2018_2020.tif` dataset meets STAC 1.0.0 metadata compliance, checksum verification, and reproducibility before web catalog integration.

---

## 🧱 Section 1 — Documentation Completeness

| Requirement | Description | Status | Notes |
|:-------------|:-------------|:---------|:-------|
| **README.md Present** | Directory includes clear user-facing documentation | ☐ / ✅ |  |
| **Metadata File Present** | STAC or JSON metadata validated successfully | ☐ / ✅ |  |
| **Version & Date Declared** | Dataset or document includes version history | ☐ / ✅ |  |
| **Author & License Declared** | Proper attribution and license information provided | ☐ / ✅ |  |
| **Cross-links Verified** | References to related data/docs function correctly | ☐ / ✅ |  |

---

## ⚙️ Section 2 — Reproducibility & Workflow Validation

| Requirement | Description | Status | Notes |
|:-------------|:-------------|:---------|:-------|
| **Makefile Target Defined** | Process can be re-run using a `make` command | ☐ / ✅ |  |
| **Config File Versioned** | YAML/JSON configuration stored and linked | ☐ / ✅ |  |
| **Pipeline Script Versioned** | ETL or transformation script tagged in Git | ☐ / ✅ |  |
| **Checksum Verified** | SHA-256 checksum validated | ☐ / ✅ |  |
| **Automation Tested** | CI/CD job executed successfully | ☐ / ✅ |  |
| **Logs Generated** | Validation logs archived in `data/work/logs/` | ☐ / ✅ |  |

---

## 🌐 Section 3 — Open Standards Compliance

| Requirement | Description | Status | Notes |
|:-------------|:-------------|:---------|:-------|
| **STAC Schema Valid** | Validates against STAC 1.0.0 schema | ☐ / ✅ |  |
| **Open File Formats** | Data stored in non-proprietary formats (GeoTIFF, JSON, CSV) | ☐ / ✅ |  |
| **CRS / EPSG Valid** | Geospatial datasets use standard EPSG codes | ☐ / ✅ |  |
| **Metadata Schema Validated** | JSON Schema compliance confirmed | ☐ / ✅ |  |
| **Web Accessibility Confirmed** | Accessible through web API or viewer | ☐ / ✅ |  |

---

## 🧬 Section 4 — Provenance & Lineage Tracking

| Requirement | Description | Status | Notes |
|:-------------|:-------------|:---------|:-------|
| **Source Manifest Linked** | Dataset has entry in `data/sources/` | ☐ / ✅ |  |
| **Checksum Chain Complete** | Each step includes SHA-256 lineage | ☐ / ✅ |  |
| **STAC Relationships Defined** | `derived_from`, `rel:source` present | ☐ / ✅ |  |
| **Provenance Log Created** | Record completed using `provenance.md` template | ☐ / ✅ |  |
| **Knowledge Graph Linked** | Entity represented in RDF / CIDOC / PROV-O | ☐ / ✅ |  |

---

## 🔎 Section 5 — CI/CD & Audit Verification

| Requirement | Description | Status | Notes |
|:-------------|:-------------|:---------|:-------|
| **CI Logs Available** | Logs available in `data/work/logs/ci/` | ☐ / ✅ |  |
| **Validation Report Generated** | Markdown/JSON validation summary present | ☐ / ✅ |  |
| **Security Scan Passed** | CodeQL and Trivy scans successful | ☐ / ✅ |  |
| **Approval Workflow Completed** | PR merged post-validation | ☐ / ✅ |  |
| **Build Version Logged** | Build tagged for reproducibility | ☐ / ✅ |  |

---

## 🧩 Section 6 — Quality Assessment & Review Notes

Document findings, anomalies, or recommendations.

> *Example:*  
> - Missing `derived_from` attribute in STAC.  
> - Re-run `make checksums` after data migration.  
> - Metadata validated; CI/CD logs confirm success — approved.

---

## 🧠 MCP Compliance Review

| MCP Principle | Validation Status | Comments |
|:---------------|:------------------|:-----------|
| **Documentation-first** | ☐ / ✅ | Documentation written before implementation. |
| **Reproducibility** | ☐ / ✅ | Deterministic build verified. |
| **Open Standards** | ☐ / ✅ | JSON Schema, STAC 1.0.0, and open file types used. |
| **Provenance** | ☐ / ✅ | Source-to-output lineage tracked. |
| **Auditability** | ☐ / ✅ | CI/CD logs traceable to dataset release. |

---

## 🧾 Reviewer Sign-Off

| Role | Reviewer Name | Date | Decision | Signature |
|:------|:---------------|:------|:-----------|:------------|
| **Primary Reviewer** |  |  | ✅ Approved / ❌ Revisions Required |  |
| **Data Governance Lead** |  |  | ✅ Approved / ❌ Revisions Required |  |
| **Automation Engineer** |  |  | ✅ Approved / ❌ Revisions Required |  |
| **Documentation Steward** |  |  | ✅ Approved / ❌ Revisions Required |  |

---

## 🧩 Related Documentation

| File | Description |
|:------|:-------------|
| `docs/templates/dataset.md` | Dataset descriptor template for metadata and schema tracking. |
| `docs/templates/provenance.md` | Provenance record for lineage documentation. |
| `docs/templates/sop.md` | SOP for validation workflows. |
| `docs/architecture/ci-cd.md` | CI/CD and governance process overview. |
| `.github/workflows/pre-commit.yml` | Automated linting and formatting validator. |

---

## 🧱 MCP Governance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | Templates ensure artifacts are peer-reviewed before publishing. |
| **Reproducibility** | All steps validated with deterministic Makefile & checksum workflows. |
| **Open Standards** | Formats verified through schema validators (STAC, JSON). |
| **Provenance** | Each artifact connected to source via lineage metadata. |
| **Auditability** | Logs and sign-offs stored in repository for compliance. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|:---------|:------|:----------|:----------|
| **v1.1** | 2025-10-05 | Documentation Team | Expanded sections for governance, CI/CD, and quality tracking. |
| **v1.0** | 2025-10-04 | KFM Docs Team | Initial MCP-compliant validation checklist template. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Review Documented. Every Validation Proven.”*  
📍 [`docs/templates/checklist.md`](.) · Use this to standardize validation, governance, and review across all KFM modules.

</div>
