<div align="center">

# 🧱 Kansas Frontier Matrix — Architecture Decision Record (ADR) Template  
`docs/templates/adr.md`

**Purpose:** Provide a **structured, reproducible format** for documenting design and architectural decisions  
made throughout the **Kansas Frontier Matrix (KFM)** project — ensuring clarity, provenance, and auditability  
across technical and data infrastructure evolution.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🧩 ADR Metadata

| Field | Description |
|:------|:-------------|
| **ADR ID** | Unique identifier (e.g., `ADR-2025-001-DATA-CATALOG`) |
| **Title** | Short, descriptive name of the decision |
| **Author(s)** | Name(s) of contributors documenting this ADR |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Status** | Proposed / Approved / Deprecated / Superseded |
| **Related Components** | (e.g., `data/stac/`, `web/config/`, `src/pipelines/`) |
| **Decision Type** | Technical / Process / Governance / Infrastructure |
| **Linked Issues / PRs** | (e.g., `#142`, `#193`, `PR #58`) |
| **Supersedes / Superseded By** | Reference previous or newer ADRs |

---

## 🎯 Context

Describe the **problem, motivation, or background** that led to this decision.  
Include relevant alternatives considered and the rationale for exploring this issue.

> Example:  
> *As KFM expands to integrate multi-temporal datasets, a decision is needed on how to structure  
> metadata relationships in STAC Collections versus Items for maximum compatibility and performance.*

---

## 🧠 Decision

Clearly state the **final decision** and rationale.  
Provide technical and procedural reasoning, referencing any related standards, experiments, or data.

> Example:  
> *The project will use STAC 1.0.0 Collection → Item relationships for metadata hierarchy,  
> linking derivative datasets using `rel:derived_from` and storing provenance in `data/stac/`.*

---

## ⚙️ Implementation

Explain **how this decision will be implemented** in the codebase, workflows, or architecture.

| Implementation Area | Description | Responsible Team |
|:----------------------|:--------------|:------------------|
| **Pipelines** | Modify ETL scripts to include STAC links in outputs. | Data Engineering |
| **Metadata** | Update all `collection.json` files with hierarchical relationships. | Metadata Team |
| **CI/CD** | Add STAC structure validation to GitHub Actions. | Automation Team |

---

## 🧮 Decision Drivers

List the **key factors** that influenced the decision.

| Factor | Explanation |
|:---------|:-------------|
| **Standards Compliance** | Aligns with STAC 1.0.0 and OGC specifications. |
| **Reproducibility** | Supports deterministic metadata generation. |
| **Interoperability** | Compatible with external STAC aggregators. |
| **Maintainability** | Simplifies long-term schema evolution. |
| **Performance** | Reduces redundancy in metadata storage. |

---

## 🧾 Alternatives Considered

| Alternative | Pros | Cons |
|:--------------|:------|:------|
| **Flat Metadata Directory** | Simple structure, easy navigation | Lacks hierarchy and provenance tracking |
| **STAC Hierarchy (Chosen)** | STAC-compliant, semantically rich | Requires schema validation |
| **Hybrid STAC + Graph Model** | Connects metadata to RDF | Complex integration and maintenance |

---

## 🧠 Consequences

List **expected impacts** and **trade-offs** resulting from this decision.

| Impact | Type | Description |
|:---------|:------|:-------------|
| **Positive** | ✅ | Improves interoperability and compliance with STAC validators |
| **Negative** | ⚠️ | Requires migration of existing metadata |
| **Neutral** | ⚙️ | Does not affect existing data pipeline execution |

---

## 🧾 Validation & Provenance

Document **how this decision is validated**, tested, and recorded for reproducibility.

| Validation Method | Tool / Workflow | Evidence |
|:--------------------|:------------------|:------------|
| **Schema Validation** | `stac-validator`, `jsonschema` | ✅ Passed in CI/CD |
| **Checksum Verification** | `make checksums` | ✅ Verified |
| **Documentation Update** | `docs/architecture/data-architecture.md` | ✅ Updated |
| **CI/CD Log Record** | `.github/workflows/stac-validate.yml` | ✅ Logged |

> All validation evidence should be stored under `data/work/logs/adr/<ADR-ID>.log`.

---

## 🔐 Governance & Review

| Reviewer | Role | Review Date | Decision |
|:------------|:--------|:--------------|:------------|
| **Project Lead** | Approver | YYYY-MM-DD | ✅ Approved |
| **Data Engineer** | Technical Reviewer | YYYY-MM-DD | ✅ Approved |
| **Metadata Curator** | Documentation Reviewer | YYYY-MM-DD | ✅ Approved |

---

## 🧱 Revision & Version Control

Describe how this ADR will evolve over time and under what conditions it may be superseded.

| Version | Date | Summary | Author |
|:-----------|:------|:-----------|:-----------|
| v1.0 | 2025-10-04 | Initial decision on metadata structure standardization. | Documentation Team |
| v1.1 | TBD | (Describe changes or deprecations) |  |

---

## 🧩 Related Documentation

| Path | Description |
|:------|:-------------|
| `docs/architecture/architecture.md` | High-level system overview |
| `docs/architecture/data-architecture.md` | Data and metadata flow context |
| `docs/architecture/knowledge-graph.md` | RDF and STAC graph integration |
| `docs/templates/sop.md` | Standard Operating Procedure template |
| `.github/workflows/stac-validate.yml` | Workflow enforcing metadata validation |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | Decision documented prior to implementation. |
| **Reproducibility** | All outcomes validated by deterministic processes. |
| **Open Standards** | Aligned with STAC 1.0.0 and OGC specifications. |
| **Provenance** | Recorded in version control and CI/CD logs. |
| **Auditability** | Linked to workflows, validation logs, and commit history. |

---

## 🧾 References

1. **STAC Specification v1.0.0** — [https://stacspec.org](https://stacspec.org)  
2. **Master Coder Protocol (MCP)** — KFM Documentation Framework  
3. **Architecture Decision Records (Nygard, 2011)** — ADR methodology reference  
4. **Open Geospatial Consortium (OGC) Standards** — [https://ogc.org](https://ogc.org)

---

## 📅 Version History

| Version | Date | Author | Summary |
|:---------|:------|:----------|:----------|
| v1.0 | 2025-10-04 | KFM Documentation Team | Initial ADR template for system-level decisions. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Decision Documented. Every Choice Proven.”*  
📍 [`docs/templates/adr.md`](.) · Template for Architecture Decision Records (ADRs) under MCP standards.

</div>
