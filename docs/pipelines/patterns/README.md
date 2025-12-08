---
title: "🧩 Kansas Frontier Matrix — Pipeline Patterns"
path: "docs/pipelines/patterns/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Pipelines WG & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Governed"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.4/docs-pipelines-patterns/signature.sig"
attestation_ref: "releases/v11.2.4/docs-pipelines-patterns/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/markdown-protocol-v11.2.4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "pipelines"
  applies_to:
    - "etl"
    - "graph"
    - "api"
    - "web"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Pipelines WG · FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded when next major pipelines-patterns spec is released"

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
  - "docs/pipelines/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-patterns-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-patterns-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:patterns:readme:v11.2.4"
semantic_document_id: "kfm-pipelines-patterns-readme-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:patterns:readme:v11.2.4"
doc_integrity_checksum: "<sha256-of-this-file>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Pipeline Patterns README**  
`docs/pipelines/patterns/README.md`

**Purpose:**  
Define the canonical layout and authoring rules for **pipeline pattern documentation** in the KFM monorepo, and connect those patterns to deterministic ETL → STAC/DCAT/PROV → Neo4j → API → Web.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() · [![KFM–MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-informational "Markdown Protocol v11.2.4")]() · [![Domain: Pipelines](https://img.shields.io/badge/Domain-Pipelines-success "Pipelines Domain")]() · [![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Pattern index is governed and active")]()

</div>

---

## 📘 Overview

This README is the **entry point** for all KFM **pipeline pattern** documentation:

- Establishes the **directory structure** for pattern guides under `docs/pipelines/patterns/`.
- Describes how patterns link to **implementation code** under `src/pipelines/**`.
- Aligns patterns with **STAC/DCAT/PROV** and the **Neo4j** knowledge graph backbone.
- Ensures every pattern is:
  - **Deterministic and config-driven** (MCP 2.0),
  - **Catalog-ready** (STAC/DCAT/GeoSPARQL),
  - **Provenance-complete** (PROV-O + OpenLineage),
  - **Story-Node-friendly** for Focus Mode usage.

If a pipeline design is not represented by a governed pattern under this index, it is **not** considered a first-class KFM pipeline pattern.

---

## 🗂️ Directory Layout

Canonical layout for pipeline patterns and their implementations:

```text
📁 KansasFrontierMatrix/
├── 📁 docs/
│   ├── 📁 pipelines/
│   │   ├── 📄 README.md                          # High-level pipelines index
│   │   ├── 📁 patterns/                          # ← Pipeline pattern catalog
│   │   │   📄 README.md                          # This file (patterns index)
│   │   │   📄 event-driven-deterministic-ingest.md   # Event-driven ingest & promotion pattern
│   │   │   📄 idempotent-safety-governance.md    # Unified idempotency/safety/governance pattern
│   │   │   📁 idempotent-node/
│   │   │   │   📄 README.md                      # Idempotent ETL node pattern
│   │   │   📁 run-state/
│   │   │   │   📄 README.md                      # Run-state pattern (per-run metadata & state)
│   │   │   └── 📁 experimental/                  # Draft / research patterns (clearly labeled)
│   │   └── 📁 sops/                              # Pipeline SOPs (runbooks, incident guides)
│   └── 📁 standards/
│       📄 kfm_markdown_protocol_v11.2.4.md
│       📁 governance/
│       │   📄 ROOT-GOVERNANCE.md
│       └── 📁 faircare/
│           📄 FAIRCARE-GUIDE.md
├── 📁 src/
│   ├── 📁 pipelines/
│   │   📁 _common/                               # Shared libs (wal, idempotency, masking, metrics)
│   │   📁 soil/
│   │   │   📁 sda_async/                         # SDA async ETL using event-driven + idempotent patterns
│   │   └── 📁 atmo/
│   │       📁 nexrad/
│   │       │   📄 watermark_logic.py             # NEXRAD watermarks (event-driven pattern)
│   │       │   📄 orchestrator.py                # Event-driven orchestrator
│   └── 📁 graph/                                 # Neo4j loaders & lineage extractors
└── 📁 data/
    📁 sources/                                   # Source manifests for pipeline inputs
    📁 raw/                                       # Raw ingested data
    📁 work/                                      # Normalized / enriched intermediates
    📁 processed/                                 # Analysis-ready outputs
    📁 stac/                                      # STAC Collections & Items for outputs
    └── 📁 dlq/                                   # Dead-letter queues for failed pipeline events
```

Authoring rules for directory trees:

- Use `📁` for directories and `📄` for files.  
- Use `text` fenced blocks, not `bash`/`sh`.  
- Use `├──` / `└──` consistently, spaces only (no tabs).  
- Include short, focused inline comments where useful.

---

## 🧭 Context

Pipeline patterns sit between **architecture** and **SOPs**:

- `docs/architecture/**`  
  - System-wide design (Neo4j backbone, API, Focus Mode).

- `docs/pipelines/README.md`  
  - Overview of pipeline domains, runtimes, and lifecycle.

- `docs/pipelines/patterns/**`  
  - **Reusable patterns**:
    - Idempotent ETL node behavior,
    - Event-driven ingestion & promotion,
    - Unified idempotency/safety/governance envelope.

- `docs/pipelines/sops/**`  
  - How operators run, debug, and roll back **specific pipelines**.

Each pattern doc should explain:

1. When to use the pattern and what problem it solves.  
2. How it flows through the KFM stack:  
   **raw → work → processed → STAC/DCAT/PROV → Neo4j → API → Web**.  
3. Required metadata, provenance, CI, and governance hooks.

---

## 🧱 Architecture

Each pattern under `docs/pipelines/patterns/` must declare:

- **Topological role**:
  - Node-level pattern (e.g., idempotent ETL node),
  - Run-level pattern (e.g., event-driven deterministic ingest),
  - Envelope pattern (e.g., idempotent safety & governance).

- **Interfaces**:
  - Inputs:
    - Source manifests under `data/sources/`,
    - Event metadata (for event-driven patterns),
    - Config and seed definitions.
  - Outputs:
    - The subtrees in `data/processed/` and `data/stac/` it populates,
    - Graph nodes/relationships it expects to be available.

- **Required cross-links**:
  - To STAC/DCAT/PROV standards in `docs/standards/`,
  - To graph models in `src/graph/**`,
  - To relevant SOPs in `docs/pipelines/sops/**`.

Patterns should include a short architectural summary (bullets or small diagram) covering:

- Orchestrator (Airflow, Dagster, custom, etc.),  
- Storage versioning (lakeFS or equivalent),  
- Event vs batch behavior (alignment to `event-driven` or `run-state` patterns).

---

## 🧠 Story Node & Focus Mode Integration

Pipeline patterns must be **Story-Node-aware**, even if the immediate pipeline is “backend-only”:

- Node- or run-level patterns should state:
  - How outputs can be referenced from Story Nodes:
    - e.g., by STAC Item ID, dataset version ID, or graph node labels.
  - Which metadata fields are required for Focus Mode:
    - Time intervals (OWL-Time compatible),
    - Spatial footprint (GeoJSON + H3 sets),
    - Provenance references (PROV bundle IDs, OpenLineage run IDs).

- When designing a new pattern:
  - Call out any **story-appropriate events**:
    - “New atmospheric window available,”
    - “Soil classification update,”
    - “Boundary or incentives change.”

- Patterns should avoid imposing UI behavior, but **must expose enough structure** for frontend teams to attach narratives cleanly (Story Nodes as a consumer, not a dependency).

---

## 🧪 Validation & CI/CD

Patterns must be **CI-enforceable**, not just prose:

- CI (`.github/workflows/kfm-ci.yml`) must be able to:
  - Check that pattern docs conform to:
    - `markdown-lint`,
    - `schema-lint` (front-matter against `json_schema_ref`),
    - `metadata-check`,
    - `footer-check`,
    - `diagram-check` where applicable.

- Pattern docs should:
  - Reference **test locations**:
    - e.g., `src/pipelines/patterns/idempotent_node/tests/`.
  - Describe the **“blocking checks”**:
    - Determinism tests,
    - Replay tests (WAL + idempotency),
    - STAC/DCAT validation for pattern outputs,
    - CARE/masking checks when applicable.

- Any new pattern should include:
  - A statement of **what CI must assert** for any pipeline claiming conformance,
  - References to the telemetry schema used for pattern-level metrics.

---

## 📦 Data & Metadata

Each pattern must specify **data and metadata contracts**:

- For data:
  - Where raw, work, and processed data live in `data/**`,
  - How partitioning or versioning is organized (e.g., by date, AOI, or semantic version).

- For metadata:
  - Which STAC collections/items will represent the outputs,
  - How DCAT records will be derived from STAC,
  - Which PROV entities/activities/agents will be emitted.

Patterns do not have to spell out **full JSON examples** in this README, but SHOULD:

- Name the relevant STAC & DCAT profiles (KFM-STAC v11, KFM-DCAT v11),  
- Identify the minimal fields required to keep artifacts:
  - Findable (identifiers, URLs),
  - Interoperable (types, schemas),
  - Reusable (lineage, license, usage constraints).

---

## ⚖ FAIR+CARE & Governance

All patterns must align with:

- Root governance:  
  - `docs/standards/governance/ROOT-GOVERNANCE.md`
- FAIR+CARE guidance:  
  - `docs/standards/faircare/FAIRCARE-GUIDE.md`
- Indigenous data sovereignty policy:  
  - `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

This README establishes that:

- **Governed patterns**:
  - Have explicit FAIR+CARE and sovereignty considerations baked into their design (e.g., masking rules, review hooks).
- **Experimental patterns**:
  - Must be clearly labeled and **not used** for pipelines touching sensitive or sovereign data until formally reviewed.

Patterns that involve:

- Archaeology,  
- Cultural heritage,  
- Tribal lands,  
- Sensitive ecology,

must either:

- Reuse an existing **CARE-aware pattern** (e.g., unified idempotent safety & governance), or  
- Undergo a **formal FAIR+CARE + sovereignty review** before promotion.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                   |
|----------:|------------|-------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-07 | Upgraded to governed, stable KFM-MDP v11.2.4; aligned with idempotent, event-driven, and safety/governance patterns; added emoji directory layout and CI/gov hooks. |
| **v0.1.0**  | 2025-12-05 | Initial draft of pipeline patterns README and basic directory guidance.                 |

---

<div align="center">

🧩 **Kansas Frontier Matrix — Pipeline Patterns**  
Deterministic Pipelines · Open Provenance · FAIR+CARE-Aligned Metadata  

[📘 Docs Root](../..) · [📂 Pipelines Index](../README.md) · [⚖ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>