<div align="center">

# 🧰 Kansas Frontier Matrix — **Review Templates Directory**  
`docs/integration/reviews/templates/README.md`

**Mission:** Centralize all **review templates** used by the Kansas Frontier Matrix (KFM)  
to ensure consistent, reproducible, and transparent evaluation of **data, code, AI models,  
documentation, and security components** under the **Master Coder Protocol (MCP-DL v6.3)**.  

These templates serve as the **operational framework** for Integration Board reviewers  
and contributors, providing standardized Markdown and YAML structures that enforce  
**provenance, validation, reproducibility, and ethics.**

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../.github/workflows/policy-check.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Aligned · STAC · CIDOC · DCAT · OWL-Time](https://img.shields.io/badge/Aligned-STAC%201.0%20%7C%20CIDOC%20CRM%20%7C%20DCAT%20%7C%20OWL--Time-green)](../../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

```yaml
---
title: "Integration Review Templates Directory"
document_type: "Governance · Templates"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-review-board","@kfm-docs","@kfm-security","@kfm-data"]
status: "Stable"
maturity: "Production"
scope: "Docs/Integration/Reviews/Templates"
license: "CC-BY 4.0"
tags: ["review","template","governance","workflow","validation"]
audit_framework: "MCP-DL v6.3"
---
````

---

## 📘 Purpose

This directory houses **standardized review templates** used across all Kansas Frontier Matrix
integration reviews — ensuring every change, from datasets to code to AI/ML models,
is evaluated using consistent, auditable criteria.

> Templates are designed to be **copied or referenced directly** in PRs, peer reviews,
> or Integration Board evaluations, reducing ambiguity and improving traceability.

---

## 🗂 Directory Layout

```text
docs/integration/reviews/templates/
├── README.md                   → Directory overview and governance (this file)
├── data_review_template.md     → Template for dataset & metadata validation
├── code_review_template.md     → Template for ETL & script reviews
├── model_review_template.md    → Template for AI/ML model evaluation
├── doc_review_template.md      → Template for documentation & governance checks
└── security_review_template.md → Template for container, dependency & policy reviews
```

Each file defines:

* A **summary header** (`### Review Summary`)
* Structured **checklists**
* A **decision block** for sign-off
* Optional **YAML metadata** to embed into audit logs

---

## 🧩 Template Overview

### 📂 `data_review_template.md`

**Purpose:** Review datasets, STAC/DCAT metadata, and geospatial compliance.
**Covers:** CRS validation, file format, schema checks, STAC/DCAT, checksum, and visualization test.
**Output:** Review summary Markdown + YAML record in `docs/integration/reviews/logs/`.

---

### 💻 `code_review_template.md`

**Purpose:** Validate Python/JavaScript ETL pipelines, AI/NLP modules, and utilities.
**Covers:** Code quality (PEP-8/ESLint), reproducibility, type hints, unit tests, Makefile integration.
**Output:** Markdown file with validation notes + CI logs cross-reference.

---

### 🤖 `model_review_template.md`

**Purpose:** Review AI/ML models and ensure ethical, transparent, and reproducible results.
**Covers:** Model card completeness, dataset provenance, hyperparameters, reproducibility, bias audit.
**Output:** Model review record with performance summary and SHA-256 hash.

---

### 📚 `doc_review_template.md`

**Purpose:** Ensure documentation adheres to **Markdown Guide** and **MCP-DL standards**.
**Covers:** YAML front matter, header block, internal links, accessibility, and version history.
**Output:** Markdown verification summary with any fixes applied in PR.

---

### 🔐 `security_review_template.md`

**Purpose:** Audit Docker images, dependencies, and CI/CD pipelines for vulnerabilities and compliance.
**Covers:** Trivy, CodeQL, OPA/Conftest checks, supply chain pinning, and access policy validation.
**Output:** Security report + pass/fail YAML appended to audit-index.

---

## 🧠 How to Use Templates

| Step | Action                                                 | Example                                                                              |
| :--- | :----------------------------------------------------- | :----------------------------------------------------------------------------------- |
| 1️⃣  | Copy relevant template to PR                           | `cp docs/integration/reviews/templates/data_review_template.md my_dataset_review.md` |
| 2️⃣  | Fill checklist fields and add reviewer signature       | `Reviewed by: @maintainer_name`                                                      |
| 3️⃣  | Commit with dataset or code PR                         | `git add docs/integration/reviews/logs/YYYY-MM-DD_<component>.md`                    |
| 4️⃣  | Upon approval, append YAML block to `audit-index.json` | `{ "id": "YYYY-MM-DD_<component>", "status": "approved" }`                           |

---

## 🧾 YAML Header Example (for all templates)

```yaml
dataset: kansas_treaties
review_type: data
reviewers: ["historian_a","geo_b"]
status: approved
validation:
  stac: pass
  checksum: verified
  license: CC-BY-4.0
notes: "All metadata and boundaries validated against USFS sources."
timestamp: 2025-10-18T12:00:00Z
```

---

## ⚙️ Integration With Automation

Each completed template automatically feeds into:

* `audit-index.json` → aggregated CI audit log
* Neo4j → links review to dataset entity (`:REVIEWED_BY` relation)
* MCP Analytics → searchable AI index (semantic embeddings)

> CI automation scans this directory for new reviews and updates the audit index daily.

---

## 🔗 Related Files

| File                                             | Description                                        |
| :----------------------------------------------- | :------------------------------------------------- |
| `../checklist.md`                                | Comprehensive review checklist (Integration Board) |
| `../logs/audit-index.json`                       | Machine-readable review log index                  |
| `../README.md`                                   | Integration Reviews overview                       |
| `../../metadata-standards.md`                    | STAC/DCAT/CIDOC ontology alignment                 |
| `../../../../.github/workflows/policy-check.yml` | Policy-as-Code validation pipeline                 |

---

## 📅 Version History

| Version    | Date       | Author             | Summary                                                                            |
| :--------- | :--------- | :----------------- | :--------------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-18 | KFM Review Council | Initial directory definition, added five standardized templates, MCP-DL alignment. |

---

<div align="center">

### 🧩 “Templates turn governance into practice — every checkbox a proof of integrity.”

**Kansas Frontier Matrix Review Council · MCP-DL v6.3**

</div>
