---
title: "🧬 KFM v11.2.4 — Lineage Standards Index"
path: "docs/standards/lineage/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Data Provenance Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x lineage-contract compatible"
status: "Active / Enforced"

doc_kind: "Standards Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "lineage"
  applies_to:
    - "etl"
    - "streaming"
    - "ai-ml"
    - "stac"
    - "dcat"
    - "graph"
    - "story-nodes"
    - "focus-mode"
    - "energy-telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/lineage-standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/lineage/lineage-standards-v1.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:docs:standards:lineage:index:v11.2.4"
semantic_document_id: "kfm-std-lineage-index-v11.2.4"
event_source_id: "ledger:kfm:docs:standards:lineage:index:v11.2.4"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🧬 KFM v11.2.4 — Lineage Standards Index  
`docs/standards/lineage/README.md`

**Purpose:**  
Serve as the canonical index for **lineage and provenance standards** in KFM — including OpenLineage integration, PROV-O exports, and catalog alignment — so that all pipelines (ETL, streaming, AI/ML, STAC/DCAT, graph ingestion, Story Nodes, Focus Mode) share a governed, deterministic, and audit-ready provenance layer.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/standards/lineage/
├── 📄 README.md                         # 🧬 Lineage Standards Index (this file)
├── 📄 openlineage-integration.md        # 🧬 OpenLineage Integration Standard (operational lineage)
├── 📂 prov-o-export/                    # 📜 PROV-O export and archival profiles (planned/expanding)
│   └── 📄 README.md                     # 📜 PROV-O Export & Archival Standard (to be created)
└── 📂 mapping-profiles/                 # 🔗 Mappings between OpenLineage, STAC, DCAT, PROV-O (planned)
    └── 📄 README.md                     # 🔗 Lineage Mapping Profiles (to be created)
```

Author rules:

- Each subdirectory under `docs/standards/lineage/` **must** contain a `README.md` that:
  - Defines scope and responsible governance body.  
  - Specifies required fields and schemas.  
  - Describes alignment with STAC, DCAT, and PROV-O.  
- New lineage-related standards must:
  - Be added to this tree with an emoji and short description.  
  - Link to relevant schemas under `schemas/` and CI workflows under `.github/workflows/`.

---

## 📘 Overview

Lineage standards in KFM ensure that:

- Every data transformation (ETL, AI/ML, catalog build, graph ingest) is **traceable**.  
- Historical runs are **reproducible** and **audit-safe**.  
- Provenance is **machine-readable** and **graph-integrated** for Story Nodes and Focus Mode.  

This index coordinates three main concerns:

1. **Operational lineage (OpenLineage)**  
   - Real-time job/run/dataset lineage via Marquez/OpenLineage.  
2. **Semantic & archival provenance (PROV-O)**  
   - Long-lived provenance bundles exportable to graphs and catalogs.  
3. **Alignment with metadata standards (STAC/DCAT)**  
   - Making lineage visible and interoperable in catalogs and downstream tools.

The standard `openlineage-integration.md` is the **primary operational lineage spec**; other docs build on it for archival and semantic mapping.

---

## 🧭 Context

Within the KFM pipeline:

> Deterministic ETL → **OpenLineage Events** → STAC/DCAT/PROV Catalogs → Neo4j Knowledge Graph → API → Frontend → Story Nodes & Focus Mode

Lineage standards:

- Bind together **runtime events** (OpenLineage) with **semantic provenance** (PROV-O) and **catalog metadata** (STAC/DCAT).  
- Ensure that every Story Node, Focus Mode view, and dataset has:
  - A clear, queryable provenance chain.  
  - A link back to the pipelines and models that produced it.  
- Provide the foundation for:
  - Governance decisions.  
  - Energy/carbon audits.  
  - Reproducibility checks and red-team reviews.

This index is referenced by:

- Pipeline architecture docs (e.g., queue-centric architecture, soil ingestion pipeline).  
- Energy standards (for linking energy telemetry to lineage).  
- Governance and security standards (for supply-chain and provenance enforcement).

---

## 🧱 Architecture

From an architecture perspective, lineage standards organize into:

- **OpenLineage Integration Standard** (`openlineage-integration.md`)  
  - Defines job naming, run events, dataset semantics, and version facets.  
  - Specifies AI/ML-specific facets (model version, dataset version, explainability, energy).  
  - Details the emission path (pipeline node → OpenLineage client → Marquez).  

- **PROV-O Export & Archival Standard** (planned under `prov-o-export/`)  
  - Will specify how OpenLineage records are transformed into PROV-O bundles.  
  - Will define retention and archival policies for long-term provenance.  

- **Mapping Profiles** (planned under `mapping-profiles/`)  
  - Will describe exact crosswalks between:
    - OpenLineage concepts and PROV-O.  
    - OpenLineage datasets and STAC/DCAT records.  

Core architectural expectations:

- OpenLineage is the **runtime lineage source-of-record**.  
- PROV-O is the **semantic and archival representation** used in graphs and catalogs.  
- All new lineage patterns must be compatible with both layers.

---

## 📦 Data & Metadata

Lineage standards define shared metadata requirements:

- **Jobs & runs**
  - Naming pattern: `kfm.<domain>.<subsystem>.<pipeline>.<step>`.  
  - `runId`, `state`, timestamps, and error messages.  

- **Datasets**
  - `namespace`, `name`, `type` (file/table/graph/vector/model).  
  - **Dataset version facets** (mandatory) per `openlineage-integration.md`.  

- **AI/ML**
  - Model artifact digests and model-card IDs.  
  - Training dataset hashes and provenance references.  
  - Explainability and energy/carbon facets.

- **Telemetry**
  - Lineage-related telemetry exported to:
    - `releases/v11.2.4/lineage-telemetry.json`.  
    - Metrics defined in `lineage-v1.json` and related schemas.

All lineage-related metadata MUST be:

- **Machine-readable** and schema-validated.  
- **Resolvable** (e.g., URNs/URLs must point to real resources where access is permitted).  
- **Stable over time**, except where explicitly versioned or deprecated.

---

## 🌐 STAC, DCAT & PROV Alignment

This index coordinates lineage standards with catalog and provenance ecosystems:

- **STAC**
  - Datasets produced by pipelines must link to:
    - OpenLineage job/run IDs for generation.  
    - Dataset version identifiers used in lineage facets.  

- **DCAT**
  - `dcat:Dataset` entries can incorporate:
    - Lineage references as identifiers or qualified relations.  
    - Version and provenance information sourced from OpenLineage and PROV-O exports.  

- **PROV-O**
  - Lineage standards must be expressible as:
    - `prov:Activity` (runs/jobs).  
    - `prov:Entity` (datasets, models, telemetry objects).  
    - `prov:Agent` (pipelines, services, maintainers).  
  - PROV bundles must be:
    - Exportable from OpenLineage records.  
    - Ingestible by KFM’s Neo4j graph and external tools.

The lineage standards under this index are responsible for making these mappings **explicit, testable, and documented**.

---

## 🧪 Validation & CI/CD

Lineage standards are enforced through CI/CD:

- **Lineage audit workflows** (e.g., `.github/workflows/lineage-audit.yml`) must:
  - Validate OpenLineage events against the `lineage-v1.json` schema.  
  - Check for the presence of dataset version facets.  
  - Ensure that all governed jobs emit `START` and `COMPLETE`/`FAIL` events.  

- **Provenance checks**:
  - Verify that critical datasets (e.g., soil layers, hydrology, AI outputs) have:
    - At least one lineage path from raw sources to final products.  
    - PROV or OpenLineage records matching declared standards.  

- **Reproducibility tests**:
  - Use lineage metadata to:
    - Reconstruct pipeline configurations and environment.  
    - Re-run selected jobs and compare outputs within allowed tolerances.

New lineage standards added under this index **must**:

- Define their own validation rules and schemas.  
- Document how CI/CD workflows enforce compliance.

---

## ⚖ FAIR+CARE & Governance

Lineage is a cornerstone of FAIR+CARE and KFM governance:

- **FAIR**
  - *Findable*: provenance records and lineage events are indexed and searchable.  
  - *Accessible*: authorized users can query lineage to understand data origins and transformations.  
  - *Interoperable*: relies on OpenLineage, PROV-O, STAC, and DCAT to integrate with external systems.  
  - *Reusable*: versioned lineage enables re-analysis, red-teaming, and independent verification.

- **CARE & sovereignty**
  - Lineage describes **how** data about communities, lands, and histories is processed.  
  - Standards must ensure:
    - Lineage does not leak restricted information (e.g., internal paths that reveal sensitive locations).  
    - Sovereignty and geoethical policies (e.g., masking, generalization) are themselves tracked via lineage facets where appropriate.  

Governance responsibilities:

- **Data Provenance Board**:
  - Owns evolution of lineage standards under this index.  
  - Reviews changes to OpenLineage integration and PROV profiles.  

- **FAIR+CARE Council**:
  - Reviews lineage implications for sensitive or sovereignty-relevant datasets.  
  - Ensures lineage practices do not undermine cultural-safety or privacy guidelines.

Any deviation from lineage standards must be:

- Documented as an exception.  
- Reviewed and approved by the relevant governance bodies.  

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                          |
|--------:|------------|-------------------|----------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial KFM-MDP v11.2.4–aligned Lineage Standards Index.       |

Future revisions must:

- Add new lineage-related standards and update the directory layout accordingly.  
- Track evolution of OpenLineage integration, PROV-O export profiles, and mapping guides.  
- Keep governance references and telemetry schema paths synchronized with global standards.

---

<div align="center">

🧬 **KFM v11.2.4 — Lineage Standards Index**  
Deterministic Provenance · Catalog-Integrated Lineage · FAIR+CARE Governance  

[📘 Docs Root](../../..) · [📂 Standards Index](../README.md) · [🧬 OpenLineage Standard](./openlineage-integration.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>