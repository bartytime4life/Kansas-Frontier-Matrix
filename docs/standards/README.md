<div align="center">

# 📐 Kansas Frontier Matrix — **Standards & Governance**  
`docs/standards/README.md`

**Mission:** Define, enforce, and version **project-wide technical, scientific, and documentation standards**  
for the **Kansas Frontier Matrix (KFM)** — ensuring **clarity**, **reproducibility**, **interoperability**, and  
**long-term integrity** across every dataset, model, pipeline, and interface under the  
**Master Coder Protocol (MCP)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)](README.md)

</div>

---

## 🧭 Overview

The **Standards & Governance** layer defines the authoritative rules, templates, and validation frameworks  
that unify the **Kansas Frontier Matrix (KFM)** under the **Master Coder Protocol (MCP)**.  
It provides a structured, reproducible foundation for data, code, and documentation integrity —  
ensuring every contributor and workflow adheres to open-science rigor and auditability.

### This document governs:
- ✅ Markdown and documentation style (MCP-DL compliance)  
- ✅ Source code structure (Python, React, GIS, STAC alignment)  
- ✅ CI/CD governance and automated validation  
- ✅ Provenance, licensing, and metadata rules (FAIR + DCAT 2.0)  
- ✅ Semantic versioning, review, and archival policies  
- ✅ Official MCP templates (SOP, experiment, model card, architecture)  

---

## 🏗 Integration Across the Monorepo

The standards system interconnects with every KFM directory, workflow, and governance layer:

```mermaid
flowchart TD
  A["📐 Standards & Governance<br/>docs/standards/"] --> B["⚙️ CI/CD Workflows<br/>.github/workflows/"]
  A --> C["🧾 Documentation Rules<br/>markdown_rules.md · markdown_guide.md"]
  A --> D["🧬 MCP Templates<br/>experiment.md · sop.md · model_card.md"]
  A --> E["📁 Data & Code Standards<br/>file_architecture.md · monorepo_design.md"]
  B --> F["✅ Automated Validation<br/>STAC · Schema · Pre-Commit Hooks"]
  C --> G["🧠 Visual & Structural Consistency<br/>AI-Generated + Human Markdown"]
  D --> H["🔬 Scientific Reproducibility<br/>MCP-DL v6.2 Frameworks"]
  E --> I["📜 Data Provenance & FAIR Compliance"]
  F --> J["📊 Governance Reports<br/>docs/standards/reports/"]
````

<!-- END OF MERMAID -->

All governance components are **interoperable** and **continuously validated** within CI/CD pipelines.

---

## 🧩 Core Governance Directives

| Domain             | Standard                     | Enforcement Mechanism   | Validation             |
| :----------------- | :--------------------------- | :---------------------- | :--------------------- |
| **Documentation**  | Markdown + MCP-DL Style      | Pre-commit + CI lint    | ✅ `make docs-validate` |
| **Data Integrity** | STAC 1.0 · DCAT 2.0          | JSON Schema Validation  | ✅ `stac-validate.yml`  |
| **Code Quality**   | Python Black · ESLint        | Pre-commit · CodeQL     | ✅ `codeql.yml`         |
| **Security**       | Dependency Scanning          | Trivy + SBOM            | ✅ `trivy.yml`          |
| **Versioning**     | Semantic Versioning (SemVer) | Automated Tag & Release | ✅ `release.yml`        |
| **Provenance**     | CIDOC CRM · OWL-Time         | Metadata + Checksum     | ✅ CI Log + Hash Verify |

---

### MCP Pillars

1. 🧾 **Documentation-First** — Every change must update or cite docs.
2. 🔁 **Reproducibility** — Pipelines and results must be fully regenerable.
3. 🌐 **Open Standards** — Favor STAC 1.0, DCAT 2.0, GeoJSON, schema.org.
4. 🔍 **Auditability** — Every artifact has verifiable provenance and integrity hash.

---

## ⚙️ Validation Workflows

All documentation and datasets are validated via automated CI/CD pipelines:

```yaml
# .github/workflows/docs-validate.yml
name: Validate Documentation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Markdown Linter
        run: make docs-validate
      - name: Check Broken Links
        run: make docs-links
```

### Automated STAC & Schema Validation

All `data/stac/*.json` entries are checked against STAC 1.0 and JSON Schema.
Pull requests cannot merge unless **all validations pass**, ensuring continuous integrity.

---

## 🧱 Compliance Framework

All standards are versioned under **MCP-DL v6.2** and licensed **CC-BY 4.0** for open reuse.

| Field                  | Description                                       |
| :--------------------- | :------------------------------------------------ |
| **Document ID**        | `STD-2025-001-GOVERNANCE`                         |
| **Version**            | v6.2.2                                            |
| **Last Updated**       | 2025-10-17                                        |
| **Maintainers**        | `@kfm-architecture`, `@kfm-data`, `@kfm-security` |
| **Status**             | ✅ Stable                                          |
| **License**            | CC-BY 4.0                                         |
| **Semantic Alignment** | STAC 1.0 · DCAT 2.0 · CIDOC CRM · OWL-Time        |

---

## 🔗 Related Standards & References

* [`docs/standards/markdown_rules.md`](markdown_rules.md) — Syntax + layout validation
* [`docs/standards/markdown_guide.md`](markdown_guide.md) — Visual + GFM features
* [`docs/templates/`](../templates/) — MCP-DL Templates (SOP, experiment, model card)
* [`docs/architecture/`](../architecture/) — System + data design governance
* [`data/stac/`](../../data/stac/) — STAC metadata for datasets
* [`src/tests/validation/`](../../src/tests/) — Automated schema and integrity tests

---

## 🧾 Version History

| Version    | Date       | Changes                                                                     | Author            |
| :--------- | :--------- | :-------------------------------------------------------------------------- | :---------------- |
| **v6.2.2** | 2025-10-17 | Upgraded alignment with Markdown Guide v6.2, badge refresh, diagram clarity | @kfm-architecture |
| **v6.2.1** | 2025-10-12 | Integrated Markdown rules cross-link & metadata table update                | @kfm-data         |
| **v6.2.0** | 2025-09-10 | Governance migrated to MCP-DL v6.2 format                                   | @kfm-security     |
| **v6.1.0** | 2025-08-01 | Introduced STAC + Schema validation workflows                               | Core Team         |
| **v6.0.0** | 2025-07-14 | Initial monorepo standards structure                                        | Core Team         |

---

### 🧩 Summary

This document serves as the **constitution** of the Kansas Frontier Matrix repository —
the unified framework for documentation, validation, and governance under the **MCP-DL v6.2** standard.
All contributors and automated systems must conform to it to ensure **scientific transparency, provenance,**
and **long-term reproducibility** across Kansas Frontier Matrix.
