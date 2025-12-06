---
title: "🌩️ KFM v11.2.4 — NEXRAD Ingestion Index & Architecture (SNS/SQS/Lambda/Step Functions · Batch/Replay)"
path: "docs/pipelines/atmo/nexrad/ingestion/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems Board · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-schema compatible"
status: "Active / Enforced"

doc_kind: "Pipeline Index"
intent: "atmo-nexrad-ingestion-architecture"
role: "ingestion-root-index"
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
  - "docs/pipelines/atmo/nexrad/ingestion/README.md@v11.2.3"
  - "docs/pipelines/atmo/nexrad/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-atmo-nexrad-ingestion-index-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-atmo-nexrad-ingestion-index-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:atmo:nexrad:ingestion:index:v11.2.4"
semantic_document_id: "kfm-pipelines-atmo-nexrad-ingestion-index-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:atmo:nexrad:ingestion:index:v11.2.4"

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
  workflow: ".github/workflows/atmo-nexrad-ingestion-index.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic Radar Ingestion × Provenance-Rich × Sustainable Intelligence"
  architecture: "SNS/SQS/Lambda/Step Functions · Batch/Replay"
  analysis: "Atmospheric Systems · Reliability · FAIR+CARE Grounded"
  data-spec: "NEXRAD Level II · Unidata · STAC-Ready"
  telemetry: "Latency · Cost · Energy/Carbon · Reliability"
  graph: "Radar Scenes · Stations · Activities"

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

# 🌩️ **KFM v11.2.4 — NEXRAD Ingestion Index & Architecture**  
`docs/pipelines/atmo/nexrad/ingestion/README.md`

**Purpose:**  
Serve as the **root index and architecture guide** for all **NEXRAD Level II ingestion pipelines** in KFM v11.2.4, covering:

- Real-time and archive flows from **Unidata NEXRAD S3 + SNS**,  
- **SNS/SQS/Lambda/Step Functions** ingestion patterns,  
- STAC/DCAT/PROV alignment and Neo4j graph wiring,  
- Deterministic replay, telemetry, and Focus Mode integration.

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

The NEXRAD ingestion subsystem in KFM:

- Ingests **NEXRAD Level II** radar volumes from the Unidata S3 + SNS distribution.  
- Emits **STAC Items** for each volume, with station/timestamp coverage.  
- Records **PROV-O lineage** and **telemetry** (latency, cost, energy, carbon).  
- Populates the **Neo4j atmospheric graph** and drives **Focus Mode** overlays.

This document:

- Indexes all NEXRAD ingestion pipeline docs under `docs/pipelines/atmo/nexrad/ingestion/`.  
- Describes the **canonical architecture** and **contract boundaries**.  
- Connects ingestion to KFM-wide patterns like:

  - Event-Driven Ingestion Safety Pattern.  
  - SNS Message Filtering Architecture.  
  - Lineage Telemetry Integration Standard.

---

## 🗂️ Directory Layout

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 ingestion/
│                   ├── 📄 README.md                   # This file (ingestion index & architecture)
│                   └── 📂 sns-sqs-lambda/
│                       ├── 📄 README.md               # SNS → SQS → Lambda/Step Functions pattern
│                       ├── 📂 architecture/
│                       │   ├── 📄 sequence.md         # Detailed call/order diagrams
│                       │   └── 📄 failure-modes.md    # Failure modes & mitigations
│                       ├── 📂 stac/
│                       │   └── 📄 item-template.json  # Canonical NEXRAD STAC Item template
│                       ├── 📂 telemetry/
│                       │   └── 📄 schema.json         # Atmo ingestion telemetry overlay
│                       └── 📂 governance/
│                           └── 📄 ingestion-policy.md # NEXRAD-specific policies & SLOs
│
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 ingestion/
│                   ├── 📄 __init__.py
│                   ├── 📄 config.py                   # Ingestion config (topics, buckets, stations)
│                   ├── 📄 routing.py                  # Topic/queue routing & SNS filter helpers
│                   ├── 📄 replay.py                   # Replay/rebackfill orchestration
│                   └── 📂 sns_sqs_lambda/
│                       ├── 📄 envelope.py             # SNS→SQS envelope parsing
│                       ├── 📄 lambda_handler.py       # Decoder/fetcher Lambda entrypoint
│                       ├── 📄 step_functions_client.py# State machine invoker
│                       ├── 📄 stac_writer.py          # STAC item creation/upsert
│                       ├── 📄 prov_lineage.py         # PROV-O emitters
│                       └── 📄 telemetry_adapter.py    # OTel metrics + energy/carbon
│
├── 📂 infra/
│   └── 📂 terraform/
│       └── 📂 atmo-nexrad/
│           ├── 📄 sns_sqs_subscriptions.tf            # SNS topic, SQS queues, DLQs
│           ├── 📄 lambda_stepfunctions.tf             # Lambda + Step Functions wiring
│           ├── 📄 iam_policies.tf                     # Least-privilege IAM for NEXRAD ingest
│           └── 📄 alarms_telemetry.tf                 # Latency, DLQ, error-rate, cost alarms
│
├── 📂 data/
│   ├── 📂 stac/
│   │   └── 📂 atmo/
│   │       └── 📂 nexrad-level2/
│   │           ├── 📂 collections/
│   │           └── 📂 items/                          # Per-volume Items
│   └── 📂 lineage/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 sns-sqs-lambda/
│                   ├── 📂 prov/                       # PROV-O JSON-LD per run
│                   └── 📂 manifests/                  # run_manifest.json per workflow run
│
└── 📂 .github/
    └── 📂 workflows/
        └── 📄 atmo-nexrad-ingestion-index.yml         # CI for docs & contract checks
~~~

---

## 🧭 Context

NEXRAD Level II ingestion is a **Tier-1 atmospheric subsystem**:

- It must be **highly reliable**, **deterministic**, and **provenance-rich**.  
- It powers both **real-time** use cases (e.g., storm nowcasting) and **historical replay**.  
- It is fully aligned with:

  - **Event-Driven Ingestion Safety Pattern**  
    (`docs/pipelines/patterns/event-driven-ingestion-safety/README.md`)  
  - **SNS Message Filtering Architecture**  
    (`docs/pipelines/messaging/sns-filtering/README.md`)  
  - **Lineage Telemetry Integration Standard**  
    (`docs/pipelines/lineage/lineage-telemetry-standard.md`).

Sources (2025):

- S3 bucket: `unidata-nexrad-level2`.  
- SNS topic ARN: `arn:aws:sns:us-east-1:684042711724:NewNEXRADLevel2Archive`.

All KFM NEXRAD ingestion pipelines must treat these as **configurable but governed constants**, referenced in config and recorded in PROV-O.

---

## 🧱 Architecture

### High-Level Pattern

- **Ingress**: Unidata SNS topic publishes new radar volume notifications.  
- **Transport**: AWS SNS → SQS queues (STD or FIFO) with governed SNS filter policies.  
- **Edge Compute**: Lambda-based decoder/fetcher normalizes envelopes and enforces idempotency.  
- **Workflow**: Step Functions orchestrate validation, STAC creation, catalog writes, provenance, and telemetry.  
- **Storage & Graph**: Outputs become STAC Items, DCAT datasets, and Neo4j nodes/relationships.  
- **Replay**: A dedicated replay state machine re-runs ingestion for specified station/time windows deterministically.

At the pattern level, this index ties together:

- `sns-sqs-lambda/README.md` (detailed pattern).  
- Cross-cutting patterns for event safety, alerts/rollback, and lineage.

---

## 📦 Data & Metadata

NEXRAD ingestion must yield:

- **STAC Collection** for NEXRAD Level II (e.g., `kfm-atmo-nexrad-l2`).  
- **STAC Items** per volume with:

  - Deterministic `id`.  
  - Station geometry/bbox.  
  - Radar timestamp as `properties.datetime`.  
  - KFM-specific properties (station ID, product level, source bucket/key, checksums).  
  - Telemetry properties (energy, carbon, cost) as allowed by schemas.

- **PROV-O lineage**:

  - Activities representing each pipeline run and each volume-level process.  
  - Entities for source S3 objects, STAC Items, and derivative products.  
  - Agents representing Unidata (external) and KFM pipelines (internal).

- **Telemetry documents** that comply with `atmo-ingestion-v1` and the Lineage Telemetry standard.

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC**:  
  - NEXRAD Collection and Items adhere to **KFM-STAC v11**.  
  - Items include KFM-specific `kfm:*` properties and STAC extensions needed for radar.

- **DCAT**:  
  - A DCAT Dataset wraps the STAC Collection for catalog exports.  
  - Includes `dct:source` referencing Unidata, `dct:conformsTo` referencing this doc and STAC profiles.

- **PROV-O**:  
  - Each ingest run is a `prov:Activity`.  
  - Uses `prov:used` to reference original radar files.  
  - Uses `prov:generated` for the STAC Items and derivative datasets.  
  - Connects to agents `unidata:nexrad` and `kfm:pipeline:atmo-nexrad-l2-ingest`.

All mappings follow `kfm-DCAT`, `kfm-STAC`, and `kfm-PROV` profiles.

---

## 🧪 Validation & CI/CD

CI for this index focuses on:

- **Markdown & schema**:

  - KFM-MDP v11.2.4 compliance (front-matter, headings, layout).  
  - JSON/SHACL validation for referenced schemas (where present).

- **Link & reference checks**:

  - Links to `sns-sqs-lambda/README.md` and other docs remain valid.  
  - STAC/DCAT/PROV standard references are present and correctly named.

For the actual pipelines (referenced here), CI includes:

- Contract tests for envelope parsing and SNS/SQS message schemas.  
- STAC Item validation against STAC 1.x + KFM-STAC.  
- PROV-O JSON-LD validation and lineage telemetry checks.  
- Latency, DLQ, and error-rate thresholds with alerts wired to reliability channels.

---

## ⚖ FAIR+CARE & Governance

- **FAIR**

  - NEXRAD outputs are **findable** via STAC/DCAT catalogs and Neo4j graph.  
  - They are **accessible** through documented APIs and data products.  
  - **Interoperability** is ensured via standards alignment.  
  - **Reusability** is backed by rich provenance and telemetry.

- **CARE**

  - Radar data is generally low-risk, but may participate in analyses with sensitive overlays (e.g., heritage, vulnerable sites).  
  - Provenance and telemetry ensure that any combined analyses have clear lineage, enabling governance reviews and redactions if needed.

Governance expectations:

- Any change to **upstream identifiers**, **ingestion contracts**, or **core STAC/provenance fields** requires:

  - Atmospheric Systems Board approval, and  
  - FAIR+CARE Oversight review when impacts cross domains.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                           |
|----------:|------------|-------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial NEXRAD ingestion root index aligned to KFM-MDP v11.2.4 and sns-sqs-lambda pattern. |
| v11.2.3  | 2025-12-01 | Draft internal structure and directory layout (not published).    |
| v11.2.2  | 2025-11-18 | Early atmo ingestion notes folded into nexrad top-level docs.    |

---

<div align="center">

🌩️ **KFM v11.2.4 — NEXRAD Ingestion Index & Architecture**  
Deterministic Radar Ingestion · STAC/DCAT/PROV-Ready · FAIR+CARE Aligned  

[📘 Atmo Pipelines Index](../README.md) · [🌩️ SNS→SQS→Lambda Pattern](sns-sqs-lambda/README.md) · [⚖ Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>