<div align="center">

# ☑️ **Kansas Frontier Matrix — Review & Validation Checklist Template**  
`docs/templates/checklist.md`

**Mission:** Deliver a **comprehensive, MCP-aligned checklist** for validating datasets, pipelines, documentation, models, and workflows  
prior to approval, deployment, or publication within the **Kansas Frontier Matrix (KFM)** — ensuring every artifact is **auditable, reproducible, secure, and standardized**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../../docs/)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../.github/workflows/docs-validate.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&logo=json)](../../.github/workflows/stac-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../.github/workflows/policy-check.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy%20%7C%20Gitleaks-red)](../../.github/workflows/)
[![SBOM & SLSA](https://img.shields.io/badge/Supply--Chain-SBOM%20%7C%20SLSA-green)](../../.github/workflows/sbom.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Review & Validation Checklist Template"
version: "v1.3.0"
last_updated: "2025-10-18"
owners: ["@kfm-docs","@kfm-architecture","@kfm-data","@kfm-security","@kfm-ai"]
tags: ["checklist","validation","mcp","stac","ci","provenance","fair","slsa","governance","ethics","accessibility"]
status: "Template"
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - JSON Schema
  - DCAT 2.0
  - W3C PROV-O
  - ISO 8601 / EPSG
  - GeoSPARQL
  - FAIR Principles
supply_chain:
  slsa_target: "Level 3"
  sbom_format: "SPDX 2.3 (JSON)"
ci_required_checks:
  - docs-validate
  - stac-validate
  - checksums
  - pre-commit
  - codeql
  - trivy
  - gitleaks
  - policy-check
---
```

---

## 🧭 Checklist Metadata

| Field                    | Description                                                     |
| :----------------------- | :-------------------------------------------------------------- |
| **Checklist ID**         | Unique ID (e.g., `CHECK-2025-001-TERRAIN`)                      |
| **Title**                | Descriptive name for review                                     |
| **Reviewer(s)**          | Name(s) of validators                                           |
| **Date Completed**       | YYYY-MM-DD                                                      |
| **Review Type**          | Data / Pipeline / Documentation / Model / Workflow / Governance |
| **Associated Artifacts** | Dataset / ADR / SOP / Experiment / Workflow IDs                 |
| **Status**               | Draft / In Review / Approved / Revisions Required               |
| **Version**              | vX.Y.Z                                                          |

---

## 🎯 Review Objective

Summarize the **scope** of this review and expected **acceptance outcome**.

> *Example:* Confirm that `ks_1m_dem_2018_2020.tif` meets **STAC 1.0**, checksum verification, access/license, and reproducibility prior to catalog inclusion.

---

## 🧱 Section 1 — Documentation Completeness

| Requirement                    | Description                                              | Status | Notes |
| :----------------------------- | :------------------------------------------------------- | :----: | :---- |
| **README Present**             | Clear, task-appropriate user documentation exists        |  ☐ / ✅ |       |
| **Metadata Declared**          | YAML header: `version`, `owners`, `last_updated`, `tags` |  ☐ / ✅ |       |
| **STAC/JSON Metadata Present** | Dataset/service has a validating metadata record         |  ☐ / ✅ |       |
| **Version History Present**    | Change log or version table included                     |  ☐ / ✅ |       |
| **License & Authors Declared** | Attribution and license stated                           |  ☐ / ✅ |       |
| **Cross-Links Verified**       | Internal links to related docs/data function             |  ☐ / ✅ |       |

---

## ⚙️ Section 2 — Reproducibility & Workflow Validation

| Requirement            | Description                                  | Status | Notes |
| :--------------------- | :------------------------------------------- | :----: | :---- |
| **Makefile Target**    | Process re-runnable via `make <target>`      |  ☐ / ✅ |       |
| **Config Versioned**   | YAML/JSON config stored and linked           |  ☐ / ✅ |       |
| **Script Versioned**   | ETL/analysis script traceable to git commit  |  ☐ / ✅ |       |
| **Container Digest**   | OCI image + digest recorded (if used)        |  ☐ / ✅ |       |
| **Checksums Verified** | SHA-256 manifests exist and match            |  ☐ / ✅ |       |
| **Automation Passed**  | CI workflow(s) completed successfully        |  ☐ / ✅ |       |
| **Logs Archived**      | Validation logs under `data/work/logs/`      |  ☐ / ✅ |       |

---

## 🌐 Section 3 — Open Standards & Accessibility

| Requirement               | Description                               | Status | Notes |
| :------------------------ | :---------------------------------------- | :----: | :---- |
| **STAC Valid**            | Conforms to STAC 1.0 schema               |  ☐ / ✅ |       |
| **Open Formats**          | GeoTIFF (COG) / GeoJSON / CSV / JSON used |  ☐ / ✅ |       |
| **CRS/EPSG Valid**        | Spatial data uses standard EPSG codes     |  ☐ / ✅ |       |
| **JSON Schema Validated** | Custom schemas validated (if any)         |  ☐ / ✅ |       |
| **Web/API Accessible**    | Available through web API or viewer       |  ☐ / ✅ |       |
| **Accessibility Basics**  | Alt text, headings, link text appropriate |  ☐ / ✅ |       |

---

## 🧬 Section 4 — Provenance & Lineage Tracking

| Requirement                 | Description                           | Status | Notes |
| :-------------------------- | :------------------------------------ | :----: | :---- |
| **Source Manifest Linked**  | Entry exists in `data/sources/**`     |  ☐ / ✅ |       |
| **Checksum Chain Complete** | SHA-256 lineage for each step         |  ☐ / ✅ |       |
| **STAC Relations Present**  | `derived_from`, `rel:source` defined  |  ☐ / ✅ |       |
| **Provenance Record**       | `provenance.md` completed and stored  |  ☐ / ✅ |       |
| **Graph Integration**       | Entity linked via PROV-O / CIDOC / KG |  ☐ / ✅ |       |

---

## 🔐 Section 5 — Security & Supply Chain

| Requirement               | Description                                       | Status | Notes |
| :------------------------ | :------------------------------------------------ | :----: | :---- |
| **CodeQL Scan Passed**    | Static analysis clean (critical issues resolved)  |  ☐ / ✅ |       |
| **Trivy Scan Passed**     | Container/dependency scan clean                   |  ☐ / ✅ |       |
| **Gitleaks Clean**        | No leaked secrets in repo or artifacts            |  ☐ / ✅ |       |
| **SBOM Generated**        | SPDX JSON available for build artifacts           |  ☐ / ✅ |       |
| **SLSA Attestation**      | Build provenance attached to release              |  ☐ / ✅ |       |
| **Secrets Hygiene**       | No plaintext secrets; OIDC used for deploy        |  ☐ / ✅ |       |
| **License Compatibility** | Mixed sources documented and compatible           |  ☐ / ✅ |       |

---

## 🔎 Section 6 — CI/CD & Audit Verification

| Requirement              | Description                       | Status | Notes |
| :----------------------- | :-------------------------------- | :----: | :---- |
| **CI Logs Available**    | Stored under `data/work/logs/ci/` |  ☐ / ✅ |       |
| **Validation Report**    | Markdown/JSON summary present     |  ☐ / ✅ |       |
| **Policy Gates Passed**  | OPA/Conftest checks clean         |  ☐ / ✅ |       |
| **Approval Workflow**    | PR merged after required checks   |  ☐ / ✅ |       |
| **Build Version Logged** | Release tag or commit recorded    |  ☐ / ✅ |       |

---

## ♿ Section 7 — Accessibility (for UI/UX changes)

| Requirement                 | Description                                 | Status | Notes |
| :-------------------------- | :------------------------------------------ | :----: | :---- |
| **Keyboard Navigation**     | All controls operable via keyboard          |  ☐ / ✅ |       |
| **Color Contrast**          | Meets WCAG 2.1 AA (≥4.5:1)                  |  ☐ / ✅ |       |
| **ARIA Labels/Roles**       | Meaningful roles/labels provided             |  ☐ / ✅ |       |
| **Motion/Prefers-reduced** | Honors motion/animation user preferences     |  ☐ / ✅ |       |
| **Screen Reader**           | Critical flows verified (NVDA/VoiceOver)     |  ☐ / ✅ |       |

---

## 🤖 Section 8 — AI/Model Validation (if applicable)

| Requirement                | Description                                        | Status | Notes |
| :------------------------- | :------------------------------------------------- | :----: | :---- |
| **Training Data Hashes**   | Logged & referenced in model card                  |  ☐ / ✅ |       |
| **Quality Gates**          | Min F1/ROUGE thresholds met                        |  ☐ / ✅ |       |
| **Bias/Fairness Checks**   | Benchmarks green; regressions blocked              |  ☐ / ✅ |       |
| **Model Card Updated**     | `docs/templates/model_card.md` patched w/ metrics  |  ☐ / ✅ |       |
| **Human-in-the-Loop**      | `@kfm-ai` approval recorded                        |  ☐ / ✅ |       |

---

## 🧪 Section 9 — Quality Assessment & Findings

Use this section to document findings, anomalies, risks, or remediation steps.

> *Example Findings:*  
> • Missing `derived_from` in STAC → add & re-validate  
> • Re-run `make checksums` post-mosaic  
> • CI logs confirm green; **Approved**

---

## 🧠 MCP Compliance Review

| MCP Principle           | Validation Status | Comments                               |
| :---------------------- | :---------------- | :------------------------------------- |
| **Documentation-first** | ☐ / ✅             | Authored prior to implementation       |
| **Reproducibility**     | ☐ / ✅             | Deterministic build verified           |
| **Open Standards**      | ☐ / ✅             | JSON Schema, STAC 1.0, open file types |
| **Provenance**          | ☐ / ✅             | Full source→output lineage tracked     |
| **Auditability**        | ☐ / ✅             | CI logs traceable to release           |

---

## ✍️ Reviewer Sign-Off

| Role                      | Reviewer | Date | Decision                          | Signature |
| :------------------------ | :------- | :--- | :-------------------------------- | :-------- |
| **Primary Reviewer**      |          |      | ✅ Approved / ❌ Revisions Required |           |
| **Data Governance Lead**  |          |      | ✅ / ❌                             |           |
| **Automation Engineer**   |          |      | ✅ / ❌                             |           |
| **Documentation Steward** |          |      | ✅ / ❌                             |           |

---

## 🔗 Related Documentation

| File                               | Description                          |
| :--------------------------------- | :----------------------------------- |
| `docs/templates/dataset.md`        | Dataset descriptor template          |
| `docs/templates/provenance.md`     | Provenance record template           |
| `docs/templates/sop.md`            | Validation/operational SOP           |
| `docs/templates/adr.md`            | Architecture Decision Record         |
| `docs/templates/model_card.md`     | AI/ML model card template            |
| `docs/architecture/ci-cd.md`       | CI/CD architecture & required checks |
| `.github/workflows/pre-commit.yml` | Automated linting & structure checks |

---

## 🧱 MCP Governance Summary

| MCP Principle           | Implementation                                      |
| :---------------------- | :-------------------------------------------------- |
| **Documentation-first** | Templates ensure peer review before publishing      |
| **Reproducibility**     | Deterministic Make + checksums + container digests  |
| **Open Standards**      | STAC/JSON Schema/GeoTIFF/GeoJSON verified           |
| **Provenance**          | Source manifests + lineage + KG links               |
| **Auditability**        | CI logs, validation reports, and sign-offs archived |

---

## 🗓️ Version History

| Version    | Date       | Author             | Summary                                                                                               |
| :--------- | :--------- | :----------------- | :---------------------------------------------------------------------------------------------------- |
| **v1.3.0** | 2025-10-18 | KFM Docs Team      | Added policy gates, AI/model validation, accessibility section, supply-chain checks, and CI expansions |
| **v1.2.0** | 2025-10-17 | KFM Docs Team      | YAML meta, security & supply-chain checks, accessibility, CI gates, and ownership fields               |
| **v1.1.0** | 2025-10-05 | Documentation Team | Expanded governance, CI/CD, and quality tracking sections                                              |
| **v1.0.0** | 2025-10-04 | KFM Docs Team      | Initial MCP-compliant validation checklist template                                                    |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*“Every Review Documented. Every Validation Proven.”*  
📍 `docs/templates/checklist.md` — Standardized validation, governance, and review across all KFM modules.

</div>