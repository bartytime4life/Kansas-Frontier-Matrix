---
title: "🌩️ KFM v11.2.4 — NEXRAD Atmospheric Radar Pipelines Index (Level II · Ingestion · Products · Stories)"
path: "docs/pipelines/atmo/nexrad/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems Board · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-schema compatible"
status: "Active / Enforced"

doc_kind: "Pipeline Index"
intent: "atmo-nexrad-pipelines-index"
role: "nexrad-root-architecture"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "atmospheric"
  applies_to:
    - "ingestion"
    - "stac"
    - "provenance"
    - "telemetry"
    - "graph"
    - "products"
    - "focus-mode"
    - "replay"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Atmospheric Ingestion"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/pipelines-telemetry.json"
telemetry_schema: "schemas/telemetry/atmo-ingestion-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

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
  - "docs/pipelines/atmo/nexrad/README.md@v11.2.3"
  - "docs/pipelines/atmo/README.md@v11.2.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-atmo-nexrad-index-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-atmo-nexrad-index-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:atmo:nexrad:index:v11.2.4"
semantic_document_id: "kfm-pipelines-atmo-nexrad-index-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:atmo:nexrad:index:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/atmo-nexrad-index.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic Radar Pipelines × Provenance-Rich × Sustainable Intelligence"
  architecture: "NEXRAD Level II · Ingestion · Products · Stories"
  analysis: "Atmospheric Systems · Reliability · FAIR+CARE Grounded"
  data-spec: "Unidata NEXRAD Level II · STAC/DCAT"
  telemetry: "Latency · Cost · Energy/Carbon · Reliability"
  graph: "Radar Scenes · Stations · Weather Events"

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

# 🌩️ **KFM v11.2.4 — NEXRAD Atmospheric Radar Pipelines Index**  
`docs/pipelines/atmo/nexrad/README.md`

**Purpose:**  
Act as the **root index and architecture hub** for all **NEXRAD Level II atmospheric radar pipelines** in KFM v11.2.4, spanning:

- **Ingestion** (Unidata SNS/S3 → SNS/SQS → Lambda/Step Functions),  
- **Products** (derived composites, tiles, analysis-ready layers),  
- **Lineage & Telemetry** (PROV-O + OpenTelemetry), and  
- **Narratives** (Story Nodes + Focus Mode overlays).

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

The NEXRAD subsystem is KFM’s **primary atmospheric radar backbone**. It:

- Ingests **NEXRAD Level II** radar volumes from Unidata’s S3 + SNS distribution.  
- Produces **versioned, STAC-compliant Items** per volume.  
- Emits **lineage telemetry** for every run and scene.  
- Feeds the **Neo4j atmospheric graph**, hydrology models, and UI overlays.  
- Supports **real-time monitoring**, **historical replay**, and **Story Node** construction for major storms.

This index:

- Describes the **NEXRAD pipeline family** structure.  
- Points to the canonical **SNS → SQS → Lambda/Step Functions** ingestion pattern.  
- Connects NEXRAD pipelines to cross-cutting KFM patterns (event safety, alerting/rollback, lineage telemetry).

---

## 🗂️ Directory Layout

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               ├── 📄 README.md                         # This file (NEXRAD root index)
│               └── 📂 ingestion/
│                   ├── 📄 README.md                     # Ingestion index & contracts
│                   └── 📂 sns-sqs-lambda/
│                       ├── 📄 README.md                 # SNS → SQS → Lambda/StepFns pattern
│                       ├── 📂 architecture/
│                       ├── 📂 stac/
│                       ├── 📂 telemetry/
│                       └── 📂 governance/
│               # (Future) products, diagnostics, stories may live here:
│               # 📂 products/, 📂 diagnostics/, 📂 stories/
│
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               ├── 📄 __init__.py
│               ├── 📄 config.py                         # Station lists, topic ARNs, buckets
│               ├── 📄 routing.py                        # SNS filter helpers & routing logic
│               ├── 📄 replay.py                         # Station/time replay orchestration
│               └── 📂 ingestion/
│                   └── 📂 sns_sqs_lambda/
│                       ├── 📄 envelope.py               # SNS→SQS envelope normalization
│                       ├── 📄 lambda_handler.py         # Decoder/fetcher Lambda
│                       ├── 📄 step_functions_client.py  # State machine invoker
│                       ├── 📄 stac_writer.py            # STAC Item creation/upsert
│                       ├── 📄 prov_lineage.py           # PROV-O emitters
│                       └── 📄 telemetry_adapter.py      # Metrics & energy/carbon hooks
│
├── 📂 infra/
│   └── 📂 terraform/
│       └── 📂 atmo-nexrad/
│           ├── 📄 sns_sqs_subscriptions.tf              # SNS topic, SQS queues, DLQs
│           ├── 📄 lambda_stepfunctions.tf               # Lambda & Step Functions wiring
│           ├── 📄 iam_policies.tf                       # Least-privilege IAM policies
│           └── 📄 alarms_telemetry.tf                   # Latency, DLQ, cost, energy alarms
│
├── 📂 data/
│   ├── 📂 stac/
│   │   └── 📂 atmo/
│   │       └── 📂 nexrad-level2/
│   │           ├── 📂 collections/                      # NEXRAD Collection(s)
│   │           └── 📂 items/                            # Per-volume STAC Items
│   └── 📂 lineage/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 sns-sqs-lambda/
│                   ├── 📂 prov/                         # PROV-O JSON-LD
│                   └── 📂 manifests/                    # run_manifest.json per run
│
└── 📂 .github/
    └── 📂 workflows/
        ├── 📄 atmo-nexrad-index.yml                     # This doc’s CI (lint, schema, links)
        └── 📄 atmo-nexrad-sns-sqs-lambda.yml            # Ingestion pattern CI
~~~

---

## 🧭 Context

NEXRAD pipelines sit at the intersection of:

- **External radar infrastructure** (NOAA/Unidata NEXRAD Level II S3 + SNS).  
- **KFM ingestion patterns** (SNS/SQS, event-driven safety, alerting/rollback).  
- **KFM atmospheric modeling and storytelling** (hydrology, weather stories, risk maps).

Key upstream assumptions:

- Source bucket: `unidata-nexrad-level2`.  
- New archive SNS topic:  
  `arn:aws:sns:us-east-1:684042711724:NewNEXRADLevel2Archive`.

Key KFM dependencies:

- **Event-Driven Ingestion Safety Pattern**  
  `docs/pipelines/patterns/event-driven-ingestion-safety/README.md`  
- **SNS Message Filtering Architecture**  
  `docs/pipelines/messaging/sns-filtering/README.md`  
- **Lineage Telemetry Integration Standard**  
  `docs/pipelines/lineage/lineage-telemetry-standard.md`  
- **SQS/Lambda Alerting & lakeFS Safe Rollback**  
  `docs/pipelines/reliability/alerting-and-rollback/README.md`

This doc is the **entry point** that ties those patterns together for NEXRAD-specific use.

---

## 🧱 Architecture

At a high level, the NEXRAD pipeline family covers:

1. **Ingestion (Real-Time & Archive)**  
   - SNS → SQS → Lambda → Step Functions.  
   - Idempotent STAC Item creation.  
   - PROV-O lineage and telemetry emission.

2. **Replay & Backfill**  
   - Station/time-window re-runs driven by Step Functions.  
   - Deterministic replays using frozen configs and input manifests.

3. **Product Generation (Future Expansion)**  
   - Derived composites (e.g., reflectivity mosaics).  
   - Analysis-ready tiles and grids for hydrology and risk.  

4. **Story Node & Focus Mode Integration**  
   - Linking radar scenes to events, places, and historical narratives.  
   - Providing Focus Mode overlays for significant storm timelines.

The detailed ingestion pattern lives in:

- `docs/pipelines/atmo/nexrad/ingestion/sns-sqs-lambda/README.md`

and defines the **precise SNS/SQS/Lambda/StepFns contract** used by the family.

---

## 📦 Data & Metadata

NEXRAD pipelines must:

- Represent each radar volume as a **STAC Item** in a NEXRAD Collection.  
- Attach **telemetry fields** (latency, cost, energy, carbon) where allowed.  
- Maintain **PROV-O provenance** for:

  - Source S3 object (Unidata).  
  - Pipeline runs and derivative products.  
  - Agents (Unidata, KFM pipelines).

Data surfaces:

- `data/stac/atmo/nexrad-level2/` — metadata-facing view.  
- Downstream derived products (e.g., mosaics) will have their own Collections/Items but point back to NEXRAD items via `prov:used` and `kfm:source_ids`.

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC**

  - NEXRAD Collection (e.g., `kfm-atmo-nexrad-l2`) documented under `collections/`.  
  - Items per radar volume under `items/`.  
  - KFM properties: `kfm:station_id`, `kfm:product_level`, `kfm:source_bucket`, `kfm:source_key`, `kfm:checksum_sha256`, plus telemetry properties.

- **DCAT**

  - A DCAT Dataset for NEXRAD Level II references the STAC Collection.  
  - Fields like `dct:source`, `dct:conformsTo`, and `dct:provenance` refer to Unidata source and this pattern.

- **PROV-O**

  - Activities: ingest runs, per-volume processing steps.  
  - Entities: source objects, STAC Items, derived products.  
  - Agents: Unidata NEXRAD, KFM pipeline(s).  

Mappings follow KFM’s `kfm-STAC`, `kfm-DCAT`, and `kfm-PROV` profiles and are enforced at CI via the lineage telemetry standard.

---

## 🧪 Validation & CI/CD

NEXRAD pipeline docs and code are validated via:

- **Docs CI** (`.github/workflows/atmo-nexrad-index.yml`):

  - KFM-MDP compliance (front-matter, headings, layout, directory section).  
  - Link checks to ingestion and standards docs.

- **Pipeline CI** (`.github/workflows/atmo-nexrad-sns-sqs-lambda.yml`):

  - Envelope/schema contract tests.  
  - STAC validation.  
  - PROV-O JSON-LD validation.  
  - Telemetry schema validation (atmo-ingestion-v1).  
  - Determinism tests for idempotent re-runs.

Reliability and alerting integrate:

- Event-driven ingestion safety checks (duplicates, retries, DLQs, watermarks).  
- SQS/Lambda alerting and lakeFS rollback patterns for safe recovery.

---

## ⚖ FAIR+CARE & Governance

- **FAIR**

  - NEXRAD outputs are made **Findable** via STAC/DCAT and graph nodes.  
  - **Accessible** via documented APIs and public/open data licenses (subject to upstream terms).  
  - **Interoperable** thanks to STAC/DCAT/PROV alignment.  
  - **Reusable** through rich metadata, provenance, and telemetry.

- **CARE**

  - Radar is generally low-risk, but may intersect **sensitive domains** (e.g., coupled with heritage/wildfire layers).  
  - Provenance and telemetry ensure such cross-domain products remain auditable and governable.  
  - Any use of NEXRAD in sensitive overlays must follow relevant CARE and sovereignty policies referenced in this doc’s front-matter.

Governance:

- Changes to NEXRAD ingestion contracts, STAC structures, or upstream identifiers require:

  - Atmospheric Systems Board approval, and  
  - FAIR+CARE review if cross-domain impacts exist (e.g., when joined with heritage or demographic layers).

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                 |
|----------:|------------|-------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial KFM-MDP-aligned NEXRAD pipelines index; wired to sns-sqs-lambda pattern. |
| v11.2.3  | 2025-12-01 | Draft directory layout and architecture notes (internal, superseded).  |
| v11.2.2  | 2025-11-18 | Early atmo ingestion consolidation; NEXRAD docs began under atmo root. |

---

<div align="center">

🌩️ **KFM v11.2.4 — NEXRAD Atmospheric Radar Pipelines Index**  
Deterministic Radar Ingestion · STAC/DCAT/PROV-Ready · FAIR+CARE Aligned  

[📘 Atmo Pipelines Index](../README.md) · [🌩️ NEXRAD Ingestion (SNS→SQS→Lambda)](ingestion/README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>