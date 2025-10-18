<div align="center">

# 🧩 Kansas Frontier Matrix — **Project Backlog**  
`docs/notes/backlog.md`

**Purpose:** Maintain a **versioned, transparent backlog** of pending work, technical debt, enhancements, and research actions across the **Kansas Frontier Matrix (KFM)** — ensuring every task is tracked with provenance, linked to data/docs, and validated under MCP governance.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../standards/documentation.md)
[![Docs Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validated&color=blue)](../../.github/workflows/docs-validate.yml)
[![Site Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Site%20Build&logo=github)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

```yaml
---
title: "Kansas Frontier Matrix — Project Backlog"
document_type: "Backlog"
version: "v1.2.0"
last_updated: "2025-10-18"
created: "2025-10-05"
owners: ["@kfm-docs","@kfm-architecture","@kfm-data","@kfm-security"]
status: "Stable"
maturity: "Production"
scope: "Docs/Notes"
license: "CC-BY 4.0"
semver_policy: "MAJOR.MINOR.PATCH"
tags: ["backlog","governance","mcp","provenance","validation","stac","ontology"]
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - site-build
  - pre-commit
  - stac-validate
  - codeql
  - trivy
semantic_alignment:
  - PROV-O
  - CIDOC CRM
  - OWL-Time
  - SKOS
  - STAC 1.0
  - JSON Schema
provenance:
  workflow_pin_policy: "actions pinned by tag or commit SHA"
  artifact_retention_days: 90
id_naming:
  pattern: "B-YYYY-NNN"    # e.g., B-2025-012
  padding: 3
priority_scale:
  - high
  - medium
  - low
---
```

---

## 📚 Table of Contents

- [🎯 Purpose](#-purpose)  
- [🧱 Structure & Workflow](#-structure--workflow)  
- [🧩 MCP Metadata Header (Per Item)](#-mcp-metadata-header-per-item)  
- [🗂️ Active Backlog Items](#️-active-backlog-items)  
- [⚙️ Task Template](#️-task-template)  
- [🔗 Knowledge Graph Mapping](#-knowledge-graph-mapping)  
- [🧠 Maintenance & Governance](#-maintenance--governance)  
- [🤖 CI Validation Hooks](#-ci-validation-hooks)  
- [🧾 Governance Notes](#-governance-notes)  
- [🧮 MCP Compliance Summary](#-mcp-compliance-summary)  
- [📎 Related Documentation](#-related-documentation)  
- [📅 Version History](#-version-history)

---

## 🎯 Purpose

The backlog is the **central operational log** for KFM documentation and development, ensuring:

* 🔁 Every open task is versioned in Git and **cross-linked** to datasets, code, or docs.  
* 🔗 Each item maintains **traceable provenance** (issues/commits/releases).  
* 🧠 Work can be **promoted** to SOPs, architecture, or CI pipelines once reproducible.  
* 🧾 Changes are governed by **MCP-DL** and included in quarterly audits.

> **Principle:** *Document first. Execute with provenance. Validate in CI.*

---

## 🧱 Structure & Workflow

```text
docs/notes/backlog.md
├── Open Tasks             # Active issues and to-dos
├── In Progress            # Assigned or ongoing work
├── Completed / Promoted   # Finished, reviewed, and migrated
└── Archived               # Deprecated or superseded items
```

**Life-cycle alignment**

- **Open → In Progress → Completed/Promoted → Archived**  
- Promotions must link to the destination doc (e.g., standards, architecture, SOP), PR/commit, and reviewer.

---

## 🧩 MCP Metadata Header (Per Item)

Each backlog item includes machine-readable YAML front-matter:

```yaml
---
id: B-2025-001
title: "Implement Dataset Checksum Automation"
author: "@kfm-data"
priority: high           # high | medium | low
status: open             # open | in-progress | complete | archived
created: 2025-10-05
updated: 2025-10-18
tags: ["checksum","automation","data-integrity","stac"]
linked_issues:
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/123
linked_commits:
  - 8b72ac3
linked_docs:
  - ../../standards/metadata.md
  - ../../architecture/data-architecture.md
linked_datasets:
  - ../../data/stac/terrain/ks_1m_dem_2018_2020.json
acceptance_criteria:
  - "Checksums generated during ETL for all assets"
  - "STAC assets include checksum:multihash"
  - "CI job publishes .sha256 sidecars under data/work/logs/"
---
```

> Headers are validated by CI (`jsonschema` + `yamllint`). Missing fields will fail **docs-validate**.

---

## 🗂️ Active Backlog Items

### 🧾 Open Tasks

| ID         | Title                                                | Priority | Owner        | Linked Docs                                      | Status |
|:-----------|:-----------------------------------------------------|:--------:|:-------------|:--------------------------------------------------|:------:|
| `B-2025-001` | Automate STAC validation during dataset upload       | **High** | @kfm-data    | [metadata.md](../../standards/metadata.md)        | ⏳ open |
| `B-2025-002` | Add hydrology time-series visualization layer        | Medium   | @kfm-web     | [web-ui.md](../../architecture/web-ui.md)         | ⏳ open |
| `B-2025-003` | Update ontology alignment with PeriodO               | Low      | @kfm-ontology| [ontologies.md](../../standards/ontologies.md)    | ⏳ open |

---

### ⚙️ In Progress

| ID         | Title                                            | Owner         | Related Commits | Linked Dataset                                  |
|:-----------|:-------------------------------------------------|:--------------|:----------------|:-------------------------------------------------|
| `B-2025-004` | CI pipeline for checksum generation               | @kfm-dataops  | `b31f1ae`       | `data/stac/terrain/ks_1m_dem_2018_2020.json`     |
| `B-2025-005` | Unit test coverage for terrain pipeline           | @kfm-qa       | `e8c91f3`       | `src/pipelines/terrain_pipeline.py`              |

---

### ✅ Completed / Promoted

| ID         | Title                               | Completed   | Promoted To                                  | Reviewer         |
|:-----------|:------------------------------------|:------------|:---------------------------------------------|:-----------------|
| `B-2025-006` | Formalized Testing Standards          | 2025-10-05  | [testing.md](../../standards/testing.md)      | @kfm-governance  |
| `B-2025-007` | Security workflow validation added    | 2025-10-05  | [security.md](../../standards/security.md)    | @kfm-security    |

---

### 🗃️ Archived

| ID         | Title                                 | Reason                       | Archived Date |
|:-----------|:--------------------------------------|:-----------------------------|:-------------:|
| `B-2024-011` | Replace legacy metadata schema draft   | Superseded by `metadata.md`  | 2025-01-10    |

> Archived items are retained under `/docs/notes/archive/` for audit.

---

## ⚙️ Task Template

```markdown
## 🧩 Task: [Short Title]
*ID:* B-YYYY-NNN  
*Priority:* High | Medium | Low  
*Owner:* @team-or-user  
*Status:* open | in-progress | complete | archived  
*Created:* YYYY-MM-DD  
*Updated:* YYYY-MM-DD  

### Description
Concise description of the task, motivation, and expected impact.

### Linked Work
- **Dataset:** `data/stac/...`
- **Doc:** `docs/standards/...`
- **Commit/PR:** `<hash>` / `#123`

### Acceptance Criteria
- [ ] Task documented with YAML header  
- [ ] Validation workflow updated (CI job link)  
- [ ] Provenance logged under `data/work/logs/`  
- [ ] Reviewer approval recorded
```

---

## 🔗 Knowledge Graph Mapping

Each backlog entry is serialized as a **`prov:Activity`** linked to the dataset(s), doc(s), and agent(s) for complete lineage.

```turtle
@prefix kfm: <https://kfm.org/id/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc:   <http://purl.org/dc/terms/> .

kfm:activity/B-2025-001
    a prov:Activity ;
    dc:title "Implement Dataset Checksum Automation" ;
    prov:wasAssociatedWith kfm:agent/kfm-data ;
    prov:used kfm:dataset/ks_1m_dem_2018_2020 ;
    prov:generated kfm:workflow/checksum_ci_pipeline ;
    dc:date "2025-10-18"^^xsd:date .
```

> Backlog → Graph ingestion: `scripts/graph_ingest_backlog.py` (nightly + on-PR).

---

## 🧠 Maintenance & Governance

| Task                      | Frequency        | Responsible        |
|:--------------------------|:-----------------|:-------------------|
| Review backlog items      | Biweekly sprint  | Documentation Lead |
| Cross-link with Issues    | Weekly           | Project Maintainers|
| Promote completed items   | Each release     | Governance Team    |
| Archive stale items       | Quarterly        | Documentation Lead |
| Validate YAML headers     | On PR            | CI/CD              |

---

## 🤖 CI Validation Hooks

| Validation              | Tool / Path                       | Purpose                                            |
|:------------------------|:----------------------------------|:---------------------------------------------------|
| **Front-matter syntax** | `yamllint`                        | Ensures each item has valid YAML headers           |
| **Schema compliance**   | `jsonschema`                      | Enforces `docs/schemas/backlog.schema.json`        |
| **Status consistency**  | `scripts/check_backlog_status.py` | Verifies state transitions & counts                |
| **Graph sync**          | `scripts/graph_ingest_backlog.py` | Pushes backlog to Neo4j/RDF                        |
| **Link checks**         | `remark-lint`                     | Confirms related relative paths exist              |

**Run locally**

```bash
make docs-validate
```

---

## 🧾 Governance Notes

* Every backlog item must link to **at least one** commit/issue or dataset.  
* Completed items require **reviewer approval** (record user/role).  
* Quarterly governance reports are published under  
  `data/work/logs/qa/backlog_summary_<YYYY_QN>.log`.

---

## 🧮 MCP Compliance Summary

| MCP Principle           | Implementation                                                                 |
|:------------------------|:-------------------------------------------------------------------------------|
| **Documentation-first** | Backlog entries authored before execution; templates enforced in PRs.           |
| **Reproducibility**     | YAML schema + Git metadata + CI logs provide an audit trail.                    |
| **Open Standards**      | Markdown + YAML + PROV-O + STAC + JSON Schema.                                 |
| **Provenance**          | Items map to `prov:Activity` with `prov:used`/`prov:generated` relationships.   |
| **Auditability**        | CI validations + quarterly reports + graph lineage retained.                    |

---

## 📎 Related Documentation

| File                               | Description                                   |
|:-----------------------------------|:----------------------------------------------|
| `docs/notes/README.md`             | Notes workspace overview.                     |
| `docs/notes/templates/README.md`   | Note & backlog entry templates.               |
| `docs/standards/documentation.md`  | Monorepo-wide writing & governance standards. |
| `docs/standards/ontologies.md`     | CIDOC-CRM · PROV-O · OWL-Time · SKOS.         |
| `docs/architecture/data-architecture.md` | File/data architecture & STAC layout.   |
| `docs/architecture/knowledge-graph.md`   | Graph ingestion & query semantics.     |

---

## 📅 Version History

| Version | Date       | Author                      | Summary                                                                 |
|:--------|:-----------|:----------------------------|:------------------------------------------------------------------------|
| v1.2.0  | 2025-10-18 | @kfm-docs                   | Upgraded to MCP-DL v6.3; added YAML header, schema hooks, CI table.     |
| v1.0.0  | 2025-10-05 | KFM Documentation/Governance| Initial backlog tracker with YAML schema, governance, and graph linkage. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Task Accounted For. Every Action Proven.”*  
📍 `docs/notes/backlog.md` · Maintained under MCP governance and CI validation.

</div>
