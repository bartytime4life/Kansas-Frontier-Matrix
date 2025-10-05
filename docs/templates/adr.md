<div align="center">

# 🧱 Kansas Frontier Matrix — Architecture Decision Record (ADR) Template  
`docs/templates/adr.md`

**Mission:** Provide a **standardized, reproducible template** for documenting architectural, technical, and governance decisions within the **Kansas Frontier Matrix (KFM)** — ensuring clarity, provenance, and long-term traceability of every change.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![Architecture Decisions](https://img.shields.io/badge/ADR-Standardized-brightgreen)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

## 🧩 ADR Metadata

| Field | Description |
|:------|:-------------|
| **ADR ID** | Unique identifier (e.g., `ADR-2025-001-PIPELINE-STRUCTURE`) |
| **Title** | Concise title summarizing the decision |
| **Author(s)** | Names and roles of contributors |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Status** | Proposed / Approved / Implemented / Superseded / Deprecated |
| **Decision Type** | Technical / Process / Governance / Infrastructure |
| **Related Components** | (e.g., `data/stac/`, `src/pipelines/`, `web/config/`) |
| **Linked Issues / PRs** | (e.g., `#142`, `PR #58`) |
| **Supersedes / Superseded By** | Reference any older/newer ADRs |

---

## 🎯 Context

Describe the **problem statement**, **motivations**, and **background** behind this decision.  
Include performance, scalability, or policy considerations, and note any competing approaches evaluated.

> *Example:*  
> As Kansas Frontier Matrix evolves to handle multi-temporal, multi-modal datasets, a decision is required regarding the data catalog hierarchy. Options include a flat metadata structure or a hierarchical STAC Collection → Item model with provenance relationships.

---

## 🧠 Decision

State the **final decision**, including the rationale and any trade-offs made.  
Describe why this approach was chosen, referencing standards, experiments, or documentation.

> *Example:*  
> KFM will adopt **STAC 1.0.0 hierarchical metadata**, linking derived datasets via `rel:derived_from` and embedding provenance in `data/stac/` for full lineage tracking.

---

## ⚙️ Implementation Plan

Define how the decision will be carried out across relevant systems.

| Implementation Area | Action Item | Responsible Team |
|:----------------------|:-------------|:------------------|
| **ETL Pipelines** | Update STAC generation scripts in `src/pipelines/`. | Data Engineering |
| **Metadata** | Revise `collection.json` files for hierarchical relationships. | Metadata Curators |
| **Automation** | Add schema validation workflow to `.github/workflows/stac-validate.yml`. | CI/CD Team |
| **Documentation** | Update affected diagrams and docs in `docs/architecture/`. | Documentation Team |

---

## 🧮 Decision Drivers

| Factor | Justification |
|:--------|:---------------|
| **Standards Alignment** | Ensures compliance with STAC 1.0.0 and OGC metadata models. |
| **Reproducibility** | Enables deterministic data lineage and consistent validation. |
| **Maintainability** | Simplifies evolution of metadata schemas. |
| **Performance** | Optimizes data discovery without increasing complexity. |
| **Transparency** | Improves user access to provenance information. |

---

## 🧾 Alternatives Considered

| Alternative | Pros | Cons |
|:-------------|:------|:------|
| **Flat Directory Model** | Simple and easy to navigate | No explicit hierarchy; poor provenance visibility |
| **Hierarchical STAC (Chosen)** | Standards-based and interoperable | Adds complexity to schema validation |
| **STAC + Knowledge Graph Hybrid** | Future extensibility for RDF integration | High implementation overhead |

---

## 🧩 Consequences

| Type | Impact | Description |
|:------|:---------|:-------------|
| ✅ Positive | Compatibility | Fully compliant with STAC and external metadata tools |
| ⚠️ Negative | Migration Cost | Requires reindexing of current datasets |
| ⚙️ Neutral | Operations | Does not alter CI/CD or deployment process |

---

## 🔍 Validation & Provenance

Define how the decision will be **validated**, **tested**, and **logged** for MCP compliance.

| Validation Step | Tool / Workflow | Verification Evidence |
|:------------------|:------------------|:-----------------------|
| **STAC Validation** | `stac-validator`, `jsonschema` | ✅ Validation report stored under `_reports/` |
| **Checksums** | `make checksums` | ✅ Logged SHA-256 manifests |
| **Workflow Run** | `.github/workflows/stac-validate.yml` | ✅ CI/CD build logs |
| **Documentation Update** | `docs/architecture/data-architecture.md` | ✅ Commit verified |

> 🗒️ **All validation evidence must be saved in:** `data/work/logs/adr/<ADR-ID>.log`.

---

## 🔐 Governance & Review

| Reviewer | Role | Review Date | Decision |
|:-----------|:--------|:--------------|:------------|
| Project Lead | Approver | YYYY-MM-DD | ✅ Approved |
| Technical Architect | Reviewer | YYYY-MM-DD | ✅ Approved |
| Data Steward | Compliance | YYYY-MM-DD | ✅ Approved |

---

## 🧱 Revision & Versioning

Describe how this ADR can evolve, be deprecated, or superseded by a new one.

| Version | Date | Author | Summary |
|:-----------|:------|:----------|:----------|
| v1.0 | 2025-10-05 | Documentation Team | Initial decision structure established. |
| v1.1 | TBD | TBD | Future update or revision summary. |

---

## 📎 Related Documents

| Path | Description |
|:------|:-------------|
| `docs/architecture/architecture.md` | High-level system overview |
| `docs/architecture/data-architecture.md` | Data model and metadata lineage |
| `docs/architecture/knowledge-graph.md` | Semantic relationships and RDF mappings |
| `docs/templates/sop.md` | Procedural steps related to ADR enforcement |
| `.github/workflows/stac-validate.yml` | CI/CD metadata validation workflow |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation Example |
|:---------------|:------------------------|
| **Documentation-first** | ADR written before implementation or deployment. |
| **Reproducibility** | Validated through CI/CD workflows and checksum evidence. |
| **Open Standards** | Decision aligns with STAC, OGC, and FAIR data practices. |
| **Provenance** | Recorded in version control and ADR log directories. |
| **Auditability** | Linked to workflows, commit hashes, and data manifests. |

---

## 🧾 References

1. [STAC Specification v1.0.0](https://stacspec.org)  
2. [Open Geospatial Consortium (OGC)](https://ogc.org)  
3. [Architecture Decision Records (Nygard, 2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html)  
4. **Master Coder Protocol (MCP)** — KFM Documentation Framework  

---

## 📅 Version History

| Version | Date | Author | Notes |
|:---------|:------|:----------|:--------|
| **v1.0** | 2025-10-05 | Kansas Frontier Matrix Documentation Team | Initial MCP-aligned ADR template for KFM architecture decisions. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Decision Documented. Every Choice Proven.”*  
📍 [`docs/templates/adr.md`](.) · MCP-compliant Architecture Decision Record template for reproducible design governance.

</div>
