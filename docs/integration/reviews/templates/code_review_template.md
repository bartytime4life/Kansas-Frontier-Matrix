<div align="center">

# 💻 Kansas Frontier Matrix — **Code Integration Review Template**  
`docs/integration/reviews/templates/code_review_template.md`

**Purpose:** Standardize **code and ETL pipeline reviews** within the  
**Kansas Frontier Matrix (KFM)** to ensure that all scripts, modules,  
and automation workflows follow **MCP-DL v6.3**, **security**, and  
**reproducibility standards** before being merged into the production branch.

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../../.github/workflows/docs-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![Aligned · STAC · CIDOC · DCAT · OWL-Time](https://img.shields.io/badge/Aligned-STAC%201.0%20%7C%20CIDOC%20CRM%20%7C%20DCAT%20%7C%20OWL--Time-green)](../../../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
title: "Code Integration Review Template"
document_type: "Review Template · Code"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-architecture","@kfm-data","@kfm-security","@kfm-docs"]
status: "Stable"
scope: "Docs/Integration/Reviews/Templates"
tags: ["review","code","etl","pipeline","integration","security","mcp"]
license: "CC-BY 4.0"
audit_framework: "MCP-DL v6.3"
---
````

---

## 🧭 Overview

This template is used by maintainers and Integration Board members to evaluate
**code contributions**, **ETL pipelines**, and **scripts** being added or modified in KFM.
All reviews follow the **documentation-first** principle — every change must be
accompanied by updated docs, provenance, and automated validation coverage.

> Each completed review must be stored under
> `docs/integration/reviews/logs/YYYY-MM-DD_<module_or_script>.md`.

---

## 🧱 Component Information

| Field           | Description                        | Example                             |
| :-------------- | :--------------------------------- | :---------------------------------- |
| **Module Name** | Name of code component             | `terrain_pipeline.py`               |
| **Path**        | Repository location                | `src/pipelines/terrain_pipeline.py` |
| **Language**    | Python / JavaScript / Bash / YAML  | `Python`                            |
| **Reviewer(s)** | Assigned reviewers                 | `@kfm-data`, `@kfm-security`        |
| **Date**        | ISO 8601                           | `2025-10-18`                        |
| **CI Run ID**   | Optional reference to workflow run | `#1426`                             |

---

## 💻 Code Quality & Reproducibility Checklist

| Check                            | Description                                                       | Status |
| :------------------------------- | :---------------------------------------------------------------- | :----- |
| [ ] **Code Style**               | Conforms to PEP-8 (Python) or ESLint (JS).                        |        |
| [ ] **Type Hints / Docstrings**  | All functions include annotations and Google/reST docstrings.     |        |
| [ ] **Tests Exist**              | `pytest` or `unittest` suite runs successfully.                   |        |
| [ ] **Coverage ≥ 85%**           | Test coverage threshold achieved and logged.                      |        |
| [ ] **Dependencies Pinned**      | `requirements.txt` / `package.json` specify exact versions.       |        |
| [ ] **Makefile Integration**     | Task registered in `Makefile` (`make fetch`, `make build`, etc.). |        |
| [ ] **Logging & Error Handling** | Uses `logging` library (no print statements).                     |        |
| [ ] **Performance**              | Code tested for efficiency; no N+1 queries or long loops.         |        |
| [ ] **Reproducibility**          | Deterministic outputs; no random seed drift.                      |        |
| [ ] **Change Documentation**     | `CHANGELOG.md` or associated doc updated.                         |        |

---

## 🧠 Provenance & Semantic Alignment

**Objective:** Ensure that each script can be traced to its data lineage and ontology mapping.

| Check                          | Description                                                         | Status |
| :----------------------------- | :------------------------------------------------------------------ | :----- |
| [ ] **STAC/DCAT Linkage**      | Code references valid dataset manifests.                            |        |
| [ ] **Ontology Mapping**       | Variables/entities mapped to CIDOC CRM or OWL-Time terms.           |        |
| [ ] **Inputs/Outputs Defined** | File formats + expected schema described.                           |        |
| [ ] **Graph Hooks**            | Output compatible with Neo4j ingestion (`scripts/graph_ingest.py`). |        |
| [ ] **Metadata Logging**       | Logs include dataset ID, version, and timestamps.                   |        |
| [ ] **Checksum Registration**  | Generated data hashed in `data/checksums/`.                         |        |

---

## 🔐 Security & Compliance Review

| Check                      | Description                                             | Status |
| :------------------------- | :------------------------------------------------------ | :----- |
| [ ] **No Secrets**         | No keys, credentials, or personal data hardcoded.       |        |
| [ ] **Trivy Scan**         | Container or dependency scan shows no critical issues.  |        |
| [ ] **CodeQL Report**      | Security scan completed and no blocker findings.        |        |
| [ ] **Pinned Actions**     | All GitHub Actions pinned by tag or SHA.                |        |
| [ ] **Policy-as-Code**     | Passes OPA/Conftest rules (`make policy-check`).        |        |
| [ ] **License Compliance** | Dependencies meet repository license compatibility.     |        |
| [ ] **Access Policy**      | Code respects dataset access levels (`access_policy:`). |        |

---

## 🧩 Documentation Synchronization

| Check                     | Description                                            | Status |
| :------------------------ | :----------------------------------------------------- | :----- |
| [ ] **README Updated**    | Related documentation updated in the same PR.          |        |
| [ ] **Inline Examples**   | Example usage shown within the module or docs.         |        |
| [ ] **Mermaid Diagrams**  | Visuals in Markdown include `<!-- END OF MERMAID -->`. |        |
| [ ] **Cross-Linked Docs** | Linked to related data integration or SOP.             |        |
| [ ] **Version History**   | Incremented version noted in the module header or doc. |        |

---

## 🧮 Reviewer Summary

| Field                     | Notes                                                    |
| :------------------------ | :------------------------------------------------------- |
| **Findings**              |                                                          |
| **Actions Required**      |                                                          |
| **Follow-up Tasks**       |                                                          |
| **Dependencies Affected** |                                                          |
| **Decision**              | ☐ Approved  ☐ Conditional Approval  ☐ Revisions Required |

---

## 🗃 YAML Review Record (Append to Audit Log)

```yaml
component: terrain_pipeline
review_type: code
reviewers: ["dev_ops_a","geo_b"]
status: approved
validation:
  lint: pass
  tests: pass
  security: clean
  docs: updated
notes: "ETL script validated, dependencies pinned, and coverage at 89%."
timestamp: 2025-10-18T13:20:00Z
```

---

## 🔗 References

* [`src/pipelines/`](../../../../../src/pipelines/) — ETL and AI modules
* [`docs/integration/reviews/checklist.md`](../checklist.md) — Full review checklist
* [`docs/architecture/data-architecture.md`](../../../architecture/data-architecture.md) — Pipeline design
* [`docs/standards/markdown_rules.md`](../../../standards/markdown_rules.md) — Markdown & governance rules
* [`docs/standards/metadata.md`](../../../standards/metadata.md) — Metadata + schema validation

---

<div align="center">

### 💻 “Every script shapes the system — every line must stand the test of time.”

**Kansas Frontier Matrix Review Council · MCP-DL v6.3**

</div>
