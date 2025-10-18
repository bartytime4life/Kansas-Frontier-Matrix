<div align="center">

# ✅ Kansas Frontier Matrix — **Integration Review Board Checklist**  
`docs/integration/reviews/checklist.md`

**Mission:** Provide a standardized, transparent, and reproducible **checklist** for Integration Board reviewers  
to evaluate every dataset, script, model, and document integrated into the **Kansas Frontier Matrix (KFM)**.  
This ensures **technical quality, provenance integrity, ethical compliance, and MCP-DL v6.3 alignment**  
before merging into the main repository.

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Aligned · STAC · CIDOC · DCAT · OWL-Time](https://img.shields.io/badge/Aligned-STAC%201.0%20%7C%20CIDOC%20CRM%20%7C%20DCAT%20%7C%20OWL--Time-green)](../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

```yaml
---
title: "Integration Review Board Checklist"
document_type: "Governance · Checklist"
version: "v1.1.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-review-board","@kfm-security","@kfm-ontology","@kfm-data"]
status: "Stable"
maturity: "Production"
scope: "Docs/Integration/Reviews"
license: "CC-BY 4.0"
audit_framework: "MCP-DL v6.3"
tags: ["review","checklist","validation","compliance","ontology","governance"]
---
````

---

## 🧭 Purpose

This checklist provides a **single source of truth** for Integration Review Board members
to validate **MCP-DL compliance**, **open-data standards**, and **provenance documentation**
for any submission entering the Kansas Frontier Matrix ecosystem.

> **Goal:** Every integration should be **scientifically reproducible**, **ethically reviewed**, and **provenance-verified** before approval.

---

## 🧩 Core Review Categories

| Category         | Description                                   | Checklist File                                             |
| :--------------- | :-------------------------------------------- | :--------------------------------------------------------- |
| 📂 Data          | Datasets, STAC items, DCAT metadata           | [Data Checklist](#📂-data-validation)                      |
| 💻 Code          | ETL scripts, utilities, pipelines             | [Code Checklist](#💻-code-validation)                      |
| 🤖 Model         | AI/ML models, training provenance             | [Model Checklist](#🤖-ai--ml-model-validation)             |
| 📚 Documentation | READMEs, SOPs, Markdown                       | [Docs Checklist](#📚-documentation--governance-validation) |
| 🔐 Security      | Containers, dependencies, CI workflows        | [Security Checklist](#🔐-security--policy-validation)      |
| ⚖️ Ethics        | Cultural data, oral histories, human subjects | [Ethics Checklist](#⚖️-ethics--governance-review)          |

---

## 📂 Data Validation

<details>
<summary>Click to expand</summary>

**Objective:** Ensure all datasets meet technical, structural, and provenance standards.

| Check                      | Description                                                                    | Status |
| :------------------------- | :----------------------------------------------------------------------------- | :----- |
| [ ] **STAC Schema**        | Validates against `stac-validator` output.                                     |        |
| [ ] **DCAT Fields**        | `license`, `source`, `provenance`, `temporal`, and `spatial` metadata present. |        |
| [ ] **Checksum**           | `.sha256` verified and logged in `data/checksums/`.                            |        |
| [ ] **CRS**                | Data projected to `EPSG:4326`.                                                 |        |
| [ ] **Temporal Range**     | Start/end dates provided and ISO 8601-compliant.                               |        |
| [ ] **Bounding Box**       | Present, accurate, matches Kansas extent.                                      |        |
| [ ] **Open Format**        | GeoJSON (vector), COG (raster), or CSV/Parquet (tabular).                      |        |
| [ ] **Attribution**        | Source license and citation recorded.                                          |        |
| [ ] **Validation Logs**    | Stored in `data/work/logs/integration/`.                                       |        |
| [ ] **Visualization Test** | Renders in `make serve` frontend preview.                                      |        |

</details>

---

## 💻 Code Validation

<details>
<summary>Click to expand</summary>

**Objective:** Ensure code adheres to MCP engineering standards, security, and maintainability.

| Check                      | Description                                                  | Status |
| :------------------------- | :----------------------------------------------------------- | :----- |
| [ ] **PEP-8 / ESLint**     | No linter or style errors.                                   |        |
| [ ] **Docstrings**         | Complete and follow Google or reST style.                    |        |
| [ ] **Type Hints**         | All functions typed.                                         |        |
| [ ] **Unit Tests**         | Coverage ≥ 85%, all pass in CI.                              |        |
| [ ] **Makefile Entry**     | Reproducible targets (`make fetch`, `make stac`).            |        |
| [ ] **Dependency Pinning** | All packages pinned by version.                              |        |
| [ ] **No Secrets**         | Environment variables, no credentials committed.             |        |
| [ ] **Performance**        | No unbounded loops or N+1 queries.                           |        |
| [ ] **Changelog**          | Updated in the same PR.                                      |        |
| [ ] **Docs Linked**        | Code references linked in Markdown (`docs/integration/...`). |        |

</details>

---

## 🤖 AI / ML Model Validation

<details>
<summary>Click to expand</summary>

**Objective:** Validate model reproducibility, explainability, and ethical documentation.

| Check                         | Description                                                           | Status |
| :---------------------------- | :-------------------------------------------------------------------- | :----- |
| [ ] **Model Card**            | `docs/model_card.md` completed with dataset, purpose, and bias notes. |        |
| [ ] **Training Data License** | Source data openly licensed and cited.                                |        |
| [ ] **Hyperparameters**       | Logged in model metadata or YAML.                                     |        |
| [ ] **Metrics**               | Precision/Recall/F1 ≥ published baseline.                             |        |
| [ ] **Reproducibility**       | Seed fixed; training deterministic.                                   |        |
| [ ] **Bias Evaluation**       | Conducted and documented.                                             |        |
| [ ] **Model Hash**            | Logged in `data/checksums/models/`.                                   |        |
| [ ] **Storage Location**      | Model artifact path recorded.                                         |        |
| [ ] **Explainability**        | SHAP/LIME or equivalent documented.                                   |        |
| [ ] **Ethical Compliance**    | Verified against MCP Ethics module.                                   |        |

</details>

---

## 📚 Documentation & Governance Validation

<details>
<summary>Click to expand</summary>

**Objective:** Ensure all documentation meets the Kansas Frontier Matrix Markdown and governance standards.

| Check                     | Description                                                       | Status |
| :------------------------ | :---------------------------------------------------------------- | :----- |
| [ ] **MCP-DL Header**     | `<div align="center">` header block with badges.                  |        |
| [ ] **YAML Front Matter** | Present, valid keys (`title`, `version`, `owners`, `tags`, etc.). |        |
| [ ] **Emojis & Sections** | Proper emoji-coded headers, semantic section flow.                |        |
| [ ] **Links / Anchors**   | Relative links functional in GitHub renderer.                     |        |
| [ ] **Mermaid Diagrams**  | End with `<!-- END OF MERMAID -->`.                               |        |
| [ ] **ToC**               | Included for long documents (>800 lines).                         |        |
| [ ] **Accessibility**     | Alt-text for images, WCAG contrast met.                           |        |
| [ ] **Cross-Linking**     | References to architecture, SOP, and standards files.             |        |
| [ ] **Version History**   | Table appended and updated.                                       |        |
| [ ] **CI Pass**           | `make docs-validate` passes with no warnings.                     |        |

</details>

---

## 🔐 Security & Policy Validation

<details>
<summary>Click to expand</summary>

**Objective:** Maintain repository security and compliance with Policy-as-Code (OPA/Conftest).

| Check                    | Description                                    | Status |
| :----------------------- | :--------------------------------------------- | :----- |
| [ ] **CodeQL SARIF**     | No critical issues unresolved.                 |        |
| [ ] **Trivy SBOM/SCA**   | Critical/High CVEs mitigated or documented.    |        |
| [ ] **Pinned Actions**   | All GitHub Actions pinned by tag or SHA.       |        |
| [ ] **No Secrets**       | Confirmed via GitGuardian or TruffleHog.       |        |
| [ ] **Container Scan**   | Docker images validated (no root user).        |        |
| [ ] **Access Policy**    | `access_policy:` defined (public/internal).    |        |
| [ ] **Ethical Access**   | Sensitive data masked or restricted.           |        |
| [ ] **Retention Policy** | Artifacts comply with MCP preservation policy. |        |
| [ ] **Policy Check**     | `make policy-check` passes OPA tests.          |        |

</details>

---

## ⚖️ Ethics & Governance Review

<details>
<summary>Click to expand</summary>

**Objective:** Ensure cultural data and oral histories are ethically managed and properly contextualized.

| Check                           | Description                                                  | Status |
| :------------------------------ | :----------------------------------------------------------- | :----- |
| [ ] **Tribal Review**           | Data approved by relevant tribal representatives.            |        |
| [ ] **Informed Consent**        | Oral histories have documented consent or restricted status. |        |
| [ ] **Cultural Sensitivity**    | Coordinates blurred or generalized for sacred sites.         |        |
| [ ] **Attribution**             | Contributors and Indigenous sources credited.                |        |
| [ ] **Representation Accuracy** | Descriptions reviewed for respectful language.               |        |
| [ ] **Ethical Disclosure**      | Risks and mitigations documented in metadata.                |        |
| [ ] **Review Record**           | Ethics approval logged in `docs/integration/reviews/logs/`.  |        |

</details>

---

## 🧮 Review Completion Summary

| Reviewer Name | Domain | Role | Status | Signature / Date |
| :------------ | :----- | :--- | :----- | :--------------- |
|               |        |      |        |                  |

**Decision:** ☐ Approved  ☐ Conditional Approval  ☐ Revisions Required

---

## 🗂 Recordkeeping

After completion, append this checklist to:

```
docs/integration/reviews/logs/YYYY-MM-DD_<dataset_or_component>.md
```

and update `audit-index.json`.

---

<div align="center">

### 🧾 “Every review is a scientific act — every check a safeguard for truth.”

**Kansas Frontier Matrix Integration Review Board · MCP-DL v6.3**

</div>
