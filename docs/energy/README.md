---
title: "⚡🌍 KFM v11 — Energy & Carbon Intelligence Overview (FAIR+CARE · OTel-Compliant)"
description: "Top-level overview of the KFM v11 energy and carbon governance space: telemetry, conversion ledgers, schemas, and Story Node integration."
path: "docs/energy/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Energy & Carbon Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x energy-governance-compatible"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/energy-telemetry.json"
telemetry_schema: "../../schemas/telemetry/energy-carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Energy & Carbon Domain Overview"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "energy"
  applies_to:
    - "energy-conversion-ledger"
    - "energy-telemetry"
    - "carbon-ledgers"
    - "energy-story-nodes"

semantic_intent:
  - "standard"
  - "architecture"
  - "governance"
category: "Documentation · Domain Overview · Energy/Carbon"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Energy & Carbon Council · Telemetry WG"
ttl_policy: "24 months"
sunset_policy: "Supersedes prior energy domain overviews"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/energy/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-energy-domain-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-energy-domain-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:energy:domain-overview:v11.2.3"
semantic_document_id: "kfm-energy-domain-overview-v11.2.3"
event_source_id: "ledger:kfm:doc:energy:domain-overview:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
---

<div align="center">

# ⚡🌍 KFM v11 — Energy & Carbon Intelligence Overview  

`docs/energy/README.md`  

**Purpose:**  
Provide a governed, architecture-safe entry point for all energy and carbon logic in KFM v11 (telemetry, conversion, schemas, and Story Node integration).

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational "Markdown Protocol v11.2.2")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Enforced")]()

</div>

---

## 📘 1. Overview

The `docs/energy/` tree is the **governed hub** for all energy and carbon concepts in KFM v11:

- How KFM measures **energy usage** across compute, storage, and pipelines.
- How Joules are normalized to **kWh** and then to **kg CO₂e** using regional factors.
- How energy and carbon appear in:
  - Telemetry (OpenTelemetry, warehouses, ledgers)
  - STAC/DCAT catalogs and metadata
  - Neo4j knowledge graph
  - Story Nodes and Focus Mode narratives

This document explains how the subdirectories fit together and where to look when:

- Implementing or reviewing energy conversion logic.
- Adding new telemetry fields or schemas.
- Building dashboards or reports around emissions.
- Surfacing energy/carbon in Story Nodes.

---

## 🗂️ 2. Directory Layout

~~~text
docs/energy/
├── 📄 README.md                           # This file: domain-level overview
│
├── 📂 conversion/                         # Canonical Joules → kWh → CO₂e ledger
│   └── 📄 README.md                       # Energy → CO₂e Conversion Ledger spec
│
├── 🧾 telemetry/                          # Energy & carbon telemetry contracts
│   ├── 📄 README.md                       # Telemetry overview & field mapping
│   ├── 📄 otel-mapping.md                 # OTel span attributes → energy events
│   └── 📄 warehouse-schema.md             # Warehouse/TS schema for energy ledgers
│
├── 📊 dashboards/                         # Human-facing visualizations
│   ├── 📄 README.md                       # Dashboard roles and governance
│   └── 📄 grafana-views.md                # Logical spec for Grafana/BI views
│
├── 🧠 models/                             # Predictive / analytical energy models
│   ├── 📄 README.md                       # Model inventory & governance
│   └── 📄 forecasting.md                  # Spec for forecasting energy/carbon usage
│
└── 🧪 qa/                                 # QA and conformance tests
    ├── 📄 README.md                       # QA strategy, thresholds, SLO links
    └── 📄 test-vectors.md                 # Shared test vectors (reused by code repos)
~~~

All sub-READMEs MUST follow **KFM-MDP v11.2.2** and reference this file as their domain parent.

---

## 🧭 3. Context in KFM Architecture

Energy and carbon intelligence spans the full KFM stack:

- **ETL / Pipelines**
  - Capture runtime spans and resource usage.
  - Emit raw Joules as part of ETL telemetry where applicable.

- **Neo4j Knowledge Graph**
  - Stores energy/carbon attributes on:
    - Compute runs
    - Datasets
    - Model training and inference episodes
  - Uses CIDOC-CRM + PROV-O + OWL-Time alignment for lineage and intervals.

- **API Layer**
  - Exposes curated energy/carbon views and aggregates.
  - Applies access control, rate limiting, and governance rules.

- **Frontend (React / MapLibre / Cesium)**
  - Surfaces energy/carbon metrics in:
    - Timeline views
    - Layer metadata panels
    - Story Nodes / Focus Mode narratives

The `docs/energy/` tree ensures all these layers use **consistent units, factors, and semantics**, with a single authoritative conversion ledger in `docs/energy/conversion/`.

---

## 📦 4. Energy & Carbon Data Model (High-Level)

At the domain level, KFM uses:

- **Core numeric fields**
  - `energy.joules` — SI Joules, raw telemetry.
  - `energy.kwh` — normalized kWh (derived).
  - `carbon.kg_co2e` — emissions in kg CO₂e (derived).
- **Contextual fields**
  - `region` — eGRID or governed region key.
  - `factor` — kg CO₂e per kWh for region.
  - `schema_version` — e.g. `"energy-carbon-v2"`.
  - `provenance`, `source_span_id` — PROV-O lineage anchors.

Precise field-level contracts and equations are defined in:

- `docs/energy/conversion/README.md` (canonical formulas, factors).
- `docs/energy/telemetry/` (event shapes, warehouse schemas).

This README does not redefine those contracts; it locates and contextualizes them.

---

## 📡 5. Telemetry Integration (OTel → Ledger → Warehouse)

The telemetry sub-tree standardizes the flow:

1. **OpenTelemetry spans**
   - Attach raw energy counters (Joules or watt-seconds) to spans.
   - Map span attributes to KFM energy fields using `otel-mapping.md`.

2. **Conversion ledger (docs/energy/conversion/)**
   - Normalize inputs (J → kWh).
   - Apply regional factors (kWh → kg CO₂e).
   - Emit governed ledger events with full metadata.

3. **Warehouse / TS**
   - Persist ledger events using schemas in `warehouse-schema.md`.
   - Power aggregations and dashboards defined under `dashboards/`.

All code and configuration that touches energy telemetry must reference these documents and adhere to their schemas.

---

## 🧠 6. Story Nodes & Focus Mode

Energy and carbon can appear in KFM Story Nodes when:

- A dataset, model run, or pipeline has non-trivial energy/carbon usage.
- An exploration in Focus Mode benefits from contextualizing emissions.

Rules:

- Story Nodes show **aggregated, ledger-derived metrics** only.
- All values MUST be:
  - In kWh or kg CO₂e as defined in `conversion/`.
  - Bound to a clear time window and region.
  - Traceable via provenance links to underlying ledger events.

Specialized Story Node patterns for energy/carbon SHOULD be documented in:

- `web/src/components/story/` (component-level docs).
- A future `docs/story-nodes/domains/energy.md` (once defined).

This README acts as the domain anchor those components and docs point back to.

---

## ⚖ 7. FAIR+CARE & Governance

- **FAIR**
  - Findable: energy/carbon domain docs centralized here, indexed from the standards index.
  - Accessible: schemas and examples are readable by humans and machines.
  - Interoperable: units and field names aligned across telemetry, catalog, and graph.
  - Reusable: versioned constants, factors, and test vectors.

- **CARE**
  - Energy/carbon metrics are used for:
    - System-level optimization.
    - Sustainability reporting.
  - They are not used for:
    - Per-person blame or non-consensual profiling.
  - Where energy usage intersects sensitive locations or Indigenous infrastructure:
    - Apply sovereignty and sensitivity guidance from `sovereignty_policy`.

Governance changes (e.g., new factor tables, new regions, new telemetry fields) must:

- Update the appropriate sub-README.
- Reference this domain overview.
- Pass CI and Energy & Carbon Council review.

---

## 🕰️ 8. Version History

| Version  | Date       | Summary                                                  |
|----------|------------|----------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Added full domain overview aligned with KFM-MDP v11.2.2. |
| v11.2.2  | 2025-11-30 | Initial energy domain stub and basic directory layout.   |

<div align="center">

⚡🌍 **KFM v11 — Energy & Carbon Intelligence Overview**  
Scientific Insight · Sustainable Operations · FAIR+CARE Governance  

[📘 Docs Root](..) · [📂 Standards Index](../standards/README.md) · [⚖ Governance](../standards/governance/ROOT-GOVERNANCE.md)

</div>