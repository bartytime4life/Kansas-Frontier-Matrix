---
title: "🔗 KFM v11.2.3 — Lineage Pipelines Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index and design standard for lineage-aware pipelines in KFM, including OpenLineage CI validation, ingestion lineage, STAC lineage sync, and Story Node provenance."
path: "docs/pipelines/lineage/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x lineage-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/lineage-pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/lineage-pipelines-index-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipelines Index"
intent: "lineage-pipelines-index"
category: "Pipelines · Lineage · Provenance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major lineage pipelines standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🔗 KFM v11.2.3 — Lineage Pipelines Index  

`docs/pipelines/lineage/README.md`

**Governed index for all KFM lineage pipelines: capturing, validating, and enforcing provenance from ETL runs to STAC catalogs, graph mutations, and Story Nodes.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Lineage-OpenLineage_%2B_PROV--O-green" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document is the **governed index** for all lineage-related pipelines in KFM v11.

Lineage pipelines are responsible for:

- Capturing **run-time provenance** (OpenLineage, PROV-O) from ETL, AI, and Story Node flows.
- Validating lineage in **CI** so that merges cannot introduce orphan datasets, cycles, or schema drift without versioning.
- Synchronizing lineage into the **KFM knowledge graph**, STAC catalogs, and Story Node metadata.
- Enforcing FAIR+CARE, sovereignty, and governance policies at the **provenance layer**.

If a pipeline mutates data, the lineage pipelines defined here are what make those mutations **audit-ready, explainable, and reversible**.

---

## 🧱 2. Directory Layout (Emoji-Prefix Standard)

High-level layout under `docs/pipelines/lineage/`:

    docs/pipelines/lineage/
    │
    ├── 📄 README.md                               # This file (lineage pipelines index)
    │
    ├── 🧪 ci-validation/                          # OpenLineage CI validation pipeline
    │   └── 📄 README.md                           # CI rules, workflows, telemetry
    │
    ├── 🧬 ingestion-lineage/                      # ETL & ingestion lineage emission patterns
    │   └── 📄 README.md                           # Standards for job/run → dataset lineage
    │
    ├── 🗂️ stac-lineage-sync/                      # STAC ⇄ lineage graph synchronization
    │   └── 📄 README.md                           # Mapping STAC Items/Collections to lineage
    │
    ├── 📖 storynode-lineage/                      # Story Node & Focus Mode provenance rules
    │   └── 📄 README.md                           # Narrative lineage and evidence contracts
    │
    └── 🛡️ governance-gates/                       # Governance gates for lineage enforcement
        └── 📄 README.md                           # Policy-driven lineage validation operators

Each subdirectory MUST:

- Provide a KFM-MDP v11.2.3-compliant `README.md`.
- Declare its **scope**, **contracts**, and **telemetry**.
- Map cleanly into KFM’s **Neo4j ontology** and PROV-O model.

---

## 🗺️ 3. Lineage in KFM — Conceptual Overview

KFM’s lineage system ties together:

- **Pipelines and jobs**  
  ETL and AI jobs are modeled as `prov:Activity` and OpenLineage `Job` / `Run`.

- **Datasets, catalogs, and Items**  
  Datasets, STAC Items, and graph entities are `prov:Entity` (and in many cases `crm:E73_Information_Object`).

- **Agents and services**  
  Operators, automated services, and external providers are `prov:Agent`.

Core properties:

- **Directional** — upstream → downstream relationships (`prov:wasDerivedFrom`, `prov:used`).
- **Versioned** — datasets and models carry explicit version identifiers.
- **Graph-safe** — lineage is designed to hydrate KFM’s Neo4j graph without ambiguity.
- **Governed** — CI checks and nightly audits enforce minimal invariants (no orphans, no cycles, no silent schema drift).

Lineage is **not optional**: any pipeline that writes data must either emit or be covered by lineage pipelines defined here.

---

## 📚 4. Lineage Pipelines in Scope

### 4.1 🧪 `ci-validation/` — OpenLineage CI Validation Pipeline

- Governs:
  - PR-level lineage checks (fast, scope-limited).
  - Nightly full-graph audits.
- Enforces:
  - No orphans, cycles, or missing upstreams (unless allowed root tags).
  - Schema drift requires version bumps.
  - Version regressions fail CI.
- Integrates:
  - OpenLineage API.
  - Neo4j / provenance ledger.
  - Telemetry via `lineage-ci-telemetry.json`.

Path:

- `docs/pipelines/lineage/ci-validation/README.md`

---

### 4.2 🧬 `ingestion-lineage/` — ETL & Ingestion Lineage Patterns

- Defines:
  - How ingestion pipelines (e.g., SDA/soilDB, NOAA SNS→SQS, gNATSGO) emit OpenLineage events.
  - Standard fields for `Job`, `Run`, and dataset nodes.
- Covers:
  - Batch ETL, streaming ETL, and hybrid flows.
  - WAL-aware lineage emissions (pre- and post-commit).

Expected content:

- Job naming conventions.
- Dataset naming/namespace rules.
- Patterns for mapping WAL entries and ETL steps to lineage events.

---

### 4.3 🗂️ `stac-lineage-sync/` — STAC ⇄ Lineage Integration

- Documents:
  - How STAC Items, Collections, and Catalogs map into lineage entities.
- Responsibilities:
  - Ensuring that every STAC Item:
    - Can be traced back to one or more `prov:Activity` instances.
    - Has upstream dataset references where applicable.
  - Handling:
    - Raster/COG pipelines.
    - Vector/feature pipelines.
    - Derived products (e.g., change detection outputs).

---

### 4.4 📖 `storynode-lineage/` — Story Nodes & Narrative Provenance

- Governs:
  - Provenance for Focus Mode and Story Nodes.
  - Evidence chains for narratives, including which datasets, documents, and entities were used.
- Ensures:
  - No Story Node exists without:
    - Underlying graph entities.
    - Linked datasets or archival sources.
    - PROV-O records for AI assistance (if used).

---

### 4.5 🛡️ `governance-gates/` — Lineage Governance Operators

- Defines:
  - LangGraph / pipeline operators that:
    - Enforce lineage policies.
    - Stop or quarantine runs when provenance is incomplete.
- Includes:
  - Configurations for:
    - Sensitive datasets.
    - Sovereignty and CARE flags.
    - Energy/carbon-aware run constraints.

---

## 📏 5. Lineage Rules & Guarantees

All lineage pipelines must uphold the following invariants:

1. **No Orphans (Without Justification)**

   - Any dataset without upstreams must carry a recognized **root tag**:
     - `seed` (initial data entry).
     - `external-source` (upstream outside KFM).
   - Otherwise, it is treated as a lineage error.

2. **No Cycles**

   - Lineage graphs must be acyclic.
   - Strongly connected components size > 1 are not allowed.

3. **Schema Changes Require Versioning**

   - Structural schema changes to datasets:
     - Require a version increment.
     - Must be reflected in dataset metadata and manifests.
   - Silent drift is treated as a failure.

4. **Downstream Awareness**

   - Breaking changes must include:
     - Declared downstream compatibility strategy or migration steps.
   - Lineage CI checks for unannounced breaking changes against downstream contracts.

5. **Graph Alignment**

   - Lineage events must be mappable to:
     - CIDOC-CRM, PROV-O, OWL-Time, and GeoSPARQL.
   - Ambiguous entities/relationships are not allowed into the graph layer.

---

## 📊 6. Telemetry, FAIR+CARE, & Governance

Lineage pipelines emit telemetry that is:

- **Structured** — aligned with `telemetry_schema`.
- **Actionable** — used by SREs, data stewards, and governance councils.
- **Ethically aware** — no sensitive identifiers beyond what governance allows.

Minimum telemetry themes:

- Lineage rule violations by type.
- Number of datasets / runs checked.
- CI run IDs and nightly audit IDs.
- Latency and error rates for lineage queries and checks.
- Optional:
  - Energy (kWh) and carbon (gCO₂e) signals for lineage-intensive jobs.

FAIR+CARE alignment:

- **FAIR**:
  - Lineage improves Findability and Reusability by making origins explicit.
- **CARE**:
  - Lineage is used to track data derived from Indigenous or sensitive sources.
  - Governance gates can block or restrict downstream use when policies require.

---

## 🧩 7. Integration with ETL, STAC, Graph, and Story Nodes

Lineage pipelines connect multiple layers:

- **ETL & Pipelines**
  - Each ETL run is a lineage **Activity**.
  - WAL events map to OpenLineage `Run` and `Job` metadata.

- **STAC**
  - STAC Items are linked to upstream Activities and Entities.
  - Derived products encode their source Items and datasets.

- **Knowledge Graph (Neo4j)**
  - Lineage events hydrate:
    - `prov:Entity` and `prov:Activity` nodes.
    - Corresponding CIDOC-CRM classes and relationships.
  - Enables time-aware provenance queries across domains.

- **Story Nodes & Focus Mode**
  - Story Nodes include:
    - References to datasets, documents, and events used.
    - Provenance chains for AI-assisted outputs.
  - Lineage pipelines ensure that narratives remain **evidence-backed**.

---

## 🕰 8. Version History

| Version  | Date       | Summary                                                                                              |
|---------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial lineage pipelines index; emoji layout; CI, ingestion, STAC, Story Node, and governance refs. |

---

<div align="center">

### 🔗 KFM v11.2.3 — Lineage Pipelines Index

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Provenance Layer  

[⬅ Back to Pipelines Index](../README.md) ·  
[🧬 Provenance Standards](../../../docs/standards/provenance/README.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>