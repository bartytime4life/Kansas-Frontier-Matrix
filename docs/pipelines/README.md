---
title: "🛠️ Kansas Frontier Matrix — Pipelines Overview & Operations Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Reliability Board"
content_stability: "stable"
backward_compatibility: "Full v10.x → v11.x compatibility"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.2.2/signature.sig"
attestation_ref: "../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/pipelines-overview-v11.2.2.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
care_label: "Public · Low-Risk"
risk_category: "ETL / Data Operations"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "pipeline-operations-overview"
category: "Pipelines · Operations · Architecture"
sensitivity: "General (auto-masking for protected datasets)"
classification: "Public"
jurisdiction: "Kansas / United States"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Reliability Board"
redaction_required: false

prov_profile: "PROV-O Core + KFM Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/pipelines-overview-v11.2.2.schema.json"
shape_schema_ref: "../../schemas/shacl/pipelines-overview-v11.2.2-shape.ttl"

doc_uuid: "urn:kfm:doc:pipelines:overview:v11.2.2"
semantic_document_id: "kfm-docs-pipelines-overview"
event_source_id: "ledger:docs/pipelines/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "rewriting pipeline logic"
  - "unverified operational claims"

transform_registry:
  allowed:
    - "summaries"
    - "semantic-highlighting"
    - "a11y-adaptations"
  prohibited:
    - "speculative additions"
    - "rewriting pipeline logic"
    - "unverified operational claims"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major pipeline architecture revision"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Pipelines Overview & Operations Guide (v11.2.2)**  
`docs/pipelines/README.md`

**Purpose**  
Define the authoritative **v11.2.2 operational architecture** for all Kansas Frontier Matrix pipelines—ETL, AI/ML–enriched, autonomous, streaming, and batch—ensuring reliability, sovereignty protection, FAIR+CARE integrity, deterministic transformations, and full governance compliance.

  
<!-- Badge Row -->
<img src="https://img.shields.io/badge/Pipelines-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img src="https://img.shields.io/badge/Lineage-OpenLineage_v2.5-orange" />
<img src="https://img.shields.io/badge/Metadata-STAC%20%2F%20DCAT%20%2F%20JSON--LD-lightgrey" />

</div>

---

## 📘 Overview

### Purpose

This document defines the **end-to-end architecture and operational expectations** for all KFM pipelines. It ensures every dataset and AI-enriched transformation moves through a reproducible, sovereign-safe, FAIR+CARE–aligned lifecycle from **raw ingest → work → processed → catalogs → knowledge graph → UI systems**.

### Executive Summary

Pipelines in KFM v11.2.2 operate under a strict operational paradigm:

- Deterministic ETL & AI behavior  
- Mandatory structural, semantic, sovereignty, and governance validation  
- Full lineage (OpenLineage v2.5 + PROV-O extensions)  
- Strict data masking & Indigenous rights protections  
- AI guardrails for OCR/NER/summarization/feature extraction  
- Immutable promotion rules and dataset versioning  
- Autonomous drift/bias detection and reliability enforcement  
- Sustainability telemetry (energy, carbon, data movement costs)  

KFM pipelines are designed to be **self-governing, self-validating, and self-auditing**, producing datasets that meet high standards of transparency, ethics, and reproducibility.

### Scope

Applies to all pipelines in:

- ETL (batch + streaming)  
- AI/ML automation  
- Validation & observability  
- Provenance & lineage  
- Story Node + Focus Mode ingestion pipelines  

### Audience

Reliability engineers · Data architects · AI/ML engineers · FAIR+CARE governance · Knowledge graph engineers · Focus Mode developers

---

## 🗂️ Directory Layout

```text
📁 KansasFrontierMatrix/                     — Monorepo root
│
📁 docs/                                     — All documentation
│   📁 pipelines/                            — Pipeline documentation (this file + domain docs)
│   │   📄 README.md                         — ← Pipelines overview & operations guide
│   │   📁 meteorology/                      — Meteorology pipeline docs (HRRR, NDFD, GRIB2/Zarr)
│   │   📁 hydrology/                        — Hydrology pipeline docs (streamflow, reservoirs, WID)
│   │   📁 hazards/                          — Hazard pipeline docs (wildfire, tornado, drought)
│   │   📁 archaeology/                      — Archaeology pipeline docs (geophysics, surveys)
│   │   📁 reliability/                      — SLOs, error budgets, rollback, hotfix patterns
│   │   📁 case-studies/                     — Real-world pipeline incident and upgrade case studies
│   📁 standards/                            — Governance, Markdown, FAIR+CARE, sovereignty
│   📁 architecture/                         — System & subsystem architecture designs
│   📁 data/                                 — Data contracts, STAC/DCAT catalogs, provenance docs
│   📁 analyses/                             — Domain research & analysis
│   📄 glossary.md                           — Unified terms
│
📁 src/                                      — Backend code
│   📁 pipelines/                            — ETL, autonomous, batch, streaming, AI flows
│   │   📁 watchers/                         — Watchers that detect upstream data changes
│   │   📁 updater/                          — Updater Runners (schedulers, webhooks)
│   │   📁 domain/                           — Domain-specific ETL (hydrology, meteorology, hazards, etc.)
│   │   📁 reliability/                      — Shared reliability primitives
│   📁 graph/                                — Neo4j schema, loaders, queries
│   📁 api/                                  — FastAPI, GraphQL gateways
│   📁 tools/                                — Utility modules and scripts
│
📁 data/                                     — Data lifecycle (raw → work → processed → stac/dcat)
📁 schemas/                                  — JSON, STAC, DCAT, SHACL, telemetry schemas
📁 .github/                                  — CI/CD workflows and policy-as-code
```

---

## 🧭 Context

The pipeline layer connects:

- **Data** ←→ **Ontology** ←→ **UI + Focus Mode**

It must align to:

- Ontologies: CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O  
- Governance & ethics: FAIR+CARE, sovereignty policies, licensing  
- Tech standards: STAC, DCAT, JSON-LD, CF conventions  
- Operational standards: SLOs, error budgets, idempotency, WAL, concurrency safety  

This guide is the **root document** for pipeline-related architecture decisions.

---

## 🗺️ Diagrams

### Pipeline Lifecycle (Data Plane)

```mermaid
flowchart LR
    A[Raw Data · External Sources] --> B[Work Layer · Normalization & Enrichment]
    B --> C[Processed Layer · Deterministic Outputs]
    C --> D[STAC/DCAT Catalogs · Data Products]
    D --> E[Graph Loaders · Neo4j]
    E --> F[UI · Focus Mode · Story Nodes]
```

### Reliability & Observability Flow

```mermaid
flowchart TD
    X[Pipeline Node] --> Y[Validation Gates]
    Y --> Z[OpenLineage Events]
    Z --> G[Governance Plane · Ledgers]
    G --> H[Alerts · Dashboards · FAIR+CARE Audits]
```

---

## 🧠 Story Node & Focus Mode Integration

Pipelines feed Focus Mode and Story Nodes:

- Only **validated, sovereignty-compliant entities** are visible.  
- Narrative generation depends on:
  - Temporal consistency via OWL-Time  
  - Spatial validity via GeoSPARQL  
  - Provenance via PROV-O (`prov:wasDerivedFrom`, `prov:used`, `prov:generatedBy`)  
  - AI guardrails ensuring no speculative content  

Focus Mode can:

- Summarize pipeline states & health  
- Show key lineage chains  
- Visualize releases and promotions over time  

Focus Mode cannot:

- Reinterpret or overwrite normative pipeline definitions  
- Invent new pipeline stages or data sources  
- Circumvent governance or kill-switch states  

---

## 🧪 Validation & CI/CD

### Validation Layers

- **Structural** — schema, types, shape, CRS  
- **Semantic** — ontology, SHACL, domain rules  
- **Sovereignty** — H3-based masking, restricted-site rules  
- **FAIR+CARE** — licensing, CARE labels, risk categories  
- **Operational** — SLOs, latency, throughput, retry patterns  
- **AI** — label drift, bias, hallucination detection, explanation logging  

### CI Integration

Typical CI jobs include:

- `docs-lint-v11` — Markdown structure + YAML spec checks  
- `schema-lint-v11` — JSON/SHACL schemas  
- `pipeline-lint-v11` — structural checks for ETL configs  
- `lineage-audit-v11` — OpenLineage + PROV-O completeness  
- `governance-audit-v11` — FAIR+CARE & sovereignty compliance  
- `etl-validation-v11` — data-contract-level validations  

Any failure **blocks promotion** and requires governance review.

---

## 📦 Data & Metadata Expectations

Pipeline outputs MUST:

- Emit STAC Items & Collections (where geospatial).  
- Emit DCAT dataset records (for higher-level dataset definition).  
- Attach JSON-LD contexts referencing KFM ontologies.  
- Store cryptographic checksums (SHA-256) of canonical artifacts.  
- Provide machine-readable provenance.

Metadata details:

- Spatial extent (`bbox`, `geometry`).  
- Temporal extent (`start_datetime`, `end_datetime`, OWL-Time).  
- Source datasets and their licenses.  
- FAIR+CARE attributes and risk categories.  
- Version identifiers and run IDs.

---

## 🧱 Architectural Classes of Pipelines

1. **Extract Pipelines**  
   - Acquire data from external API, bucket, or flat-file source.  
   - Enforce license & usage policies on ingest.

2. **Transform Pipelines**  
   - Normalize schemas, units, and CRS.  
   - Run AI steps (OCR/NER/summarization) with guardrails.  
   - Emphasize determinism and repeatability.

3. **Validation Pipelines**  
   - Perform Great Expectations, schema checks, and FAIR+CARE/sovereignty validations.  
   - Output validation reports to `data/reports/`.

4. **Load Pipelines**  
   - Publish final artifacts to STAC/DCAT.  
   - Load graph nodes and relationships.  
   - Attach provenance and telemetry.

---

## ⚖ FAIR+CARE & Governance

Pipelines are designed to uphold:

### FAIR

- **Findable:** KFM IDs, STAC/DCAT indexing, search.  
- **Accessible:** Controlled but open-sharing where legally allowed.  
- **Interoperable:** Uses STAC, DCAT, CF, and KFM ontologies.  
- **Reusable:** Rich provenance and metadata.

### CARE

- **Collective Benefit:** Data pipelines serve communities, not exploitation.  
- **Authority to Control:** Indigenous and local communities retain control over use of their data.  
- **Responsibility:** Operators enforce masking & sovereignty rules.  
- **Ethics:** Transparent limitations and hazards documented.

Governance engine (GovHooks):

- Attaches governance metadata per run.  
- Enforces kill-switches and freeze windows.  
- Logs decisions in governance ledgers.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Canonical v11.2.2 rewrite; badge/footer alignment; layout normalized; telemetry & governance hooks updated. |
| v11.0.0 | 2025-11-20 | Initial v11 pipelines overview; established basic architecture and governance linkages.        |

---

<div align="center">

## 🛠️ **Kansas Frontier Matrix — Pipelines Overview & Operations Guide (v11.2.2)**  
*Deterministic pipelines · Governed automation · FAIR+CARE-aligned data flow*

  
<img src="https://img.shields.io/badge/Pipelines-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img src="https://img.shields.io/badge/Lineage-OpenLineage_v2.5-orange" />
<img src="https://img.shields.io/badge/Metadata-STAC%20%2F%20DCAT%20%2F%20JSON--LD-lightgrey" />

  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.2 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Pipelines Home](README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[📘 KFM Documentation Home](../README.md)

</div>
