---
title: "🌩️ KFM v11.2.4 — NEXRAD SNS → SQS → Lambda/Step-Functions Ingestion Pattern (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmo/nexrad/ingestion/sns-sqs-lambda/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems Board · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-schema compatible"
status: "Active / Enforced"

doc_kind: "Pattern"
intent: "nexrad-sns-sqs-lambda-stepfunctions-ingestion"
role: "atmospheric-ingestion-pattern"
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
  - "docs/pipelines/atmo/nexrad/ingestion/sns-sqs-lambda/README.md@v11.2.3"
  - "docs/pipelines/atmo/nexrad/ingestion/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-atmo-nexrad-sns-sqs-lambda-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-atmo-nexrad-sns-sqs-lambda-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:atmo:nexrad:ingestion:sns-sqs-lambda:v11.2.4"
semantic_document_id: "kfm-pipelines-atmo-nexrad-sns-sqs-lambda-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:atmo:nexrad:ingestion:sns-sqs-lambda:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
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
  - "pattern-contract-check"

ci_integration:
  workflow: ".github/workflows/atmo-nexrad-sns-sqs-lambda.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic Radar Ingestion × Provenance-Rich × Sustainable Intelligence"
  architecture: "SNS → SQS → Lambda/Step Functions · STAC/DCAT/PROV"
  analysis: "Radar Systems · Reliability · FAIR+CARE Grounded"
  data-spec: "NEXRAD Level II · Unidata · STAC-Compatible"
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

# 🌩️ **NEXRAD SNS → SQS → Lambda/Step-Functions Ingestion Pattern**  
`docs/pipelines/atmo/nexrad/ingestion/sns-sqs-lambda/README.md`

**Purpose:**  
Define the **canonical, deterministic, provenance-rich ingestion pattern** for **NEXRAD Level II archive notifications** using the current **Unidata SNS + S3** stack, wired into KFM’s **STAC/DCAT/PROV**, **Neo4j**, and **Focus Mode** layers.

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

The Kansas Frontier Matrix relies on **timely, reproducible ingestion** of atmospheric radar data for:

- Storm nowcasting and historical replay.  
- Hydrology and flood risk modeling.  
- Story Nodes and Focus Mode narratives about significant events.

This pattern standardizes an **AWS-native ingestion contract** for **NEXRAD Level II archive notifications** using:

- **Upstream bucket**:  

  ~~~text
  unidata-nexrad-level2
  ~~~

- **Archive SNS Topic ARN**:  

  ~~~text
  arn:aws:sns:us-east-1:684042711724:NewNEXRADLevel2Archive
  ~~~

Within KFM, this pattern guarantees:

- Deterministic, idempotent message handling.  
- Replay-safe **Step Functions** workflows.  
- Idempotent **STAC Item** generation.  
- Lineage and telemetry that are **PROV-O**, **FAIR+CARE**, and **KFM-MDP v11.2.4** aligned.

It is the **canonical KFM ingestion pattern for NEXRAD Level II**.

---

## 🗂️ Directory Layout

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 ingestion/
│                   └── 📂 sns-sqs-lambda/
│                       ├── 📄 README.md                 # This file (pattern spec)
│                       ├── 📂 architecture/
│                       │   ├── 📄 sequence.md           # Sequencing and interaction details
│                       │   └── 📄 failure-modes.md      # Enumerated failure modes + mitigations
│                       ├── 📂 stac/
│                       │   └── 📄 item-template.json    # Canonical STAC Item template
│                       ├── 📂 telemetry/
│                       │   └── 📄 schema.json           # Atmo ingestion telemetry schema overlay
│                       └── 📂 governance/
│                           └── 📄 ingestion-policy.md   # NEXRAD-specific ingestion policy & SLOs
│
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 ingestion/
│                   └── 📂 sns_sqs_lambda/
│                       ├── 📄 __init__.py
│                       ├── 📄 envelope.py               # SNS→SQS envelope parsing
│                       ├── 📄 lambda_handler.py         # Decoder/fetcher Lambda entrypoint
│                       ├── 📄 step_functions_client.py  # State machine invoker
│                       ├── 📄 stac_writer.py            # STAC item creation/upsert
│                       ├── 📄 prov_lineage.py           # PROV-O activity/entity emitters
│                       └── 📄 telemetry_adapter.py      # OTel metrics + energy/carbon emit
│
├── 📂 infra/
│   └── 📂 terraform/
│       └── 📂 atmo-nexrad/
│           ├── 📄 sns_sqs_subscriptions.tf              # SNS topic, SQS queues, DLQs
│           ├── 📄 lambda_stepfunctions.tf               # Lambda + Step Functions wiring
│           └── 📄 iam_policies.tf                       # Least-privilege IAM for NEXRAD ingest
│
├── 📂 data/
│   ├── 📂 stac/
│   │   └── 📂 atmo/
│   │       └── 📂 nexrad-level2/
│   │           ├── 📂 collections/
│   │           └── 📂 items/                            # Per-radar-volume STAC Items
│   └── 📂 lineage/
│       └── 📂 atmo/
│           └── 📂 nexrad/
│               └── 📂 sns-sqs-lambda/
│                   ├── 📂 prov/                         # PROV-O JSON-LD per run/activity
│                   └── 📂 manifests/                    # run_manifest.json per workflow run
│
└── 📂 .github/
    └── 📂 workflows/
        └── 📄 atmo-nexrad-sns-sqs-lambda.yml            # CI: contract, schema, telemetry checks
~~~

---

## 🧭 Context

### Updated NEXRAD Sources (2025)

KFM ingests NEXRAD Level II radar volumes from the **Unidata** S3 + SNS distribution:

- **S3 bucket**: `unidata-nexrad-level2`  
- **SNS topic ARN**: `arn:aws:sns:us-east-1:684042711724:NewNEXRADLevel2Archive`

All ingestion components **must** reference these identifiers in configuration and provenance.

### Integration into KFM

The ingestion pattern feeds:

- A **STAC Collection** for NEXRAD Level II.  
- **Item-per-volume** metadata with station/time coverage.  
- Neo4j **radar scene nodes** and relationships to **stations** and **events**.  
- Focus Mode overlays for storms and weather narratives.

---

## 🧱 Architecture

### High-Level Flow

~~~mermaid
flowchart LR
    NEXRAD["NEXRAD SNS Topic\n(NewNEXRADLevel2Archive)"]
      --> Q["SQS Queue\n(NEXRAD ingest)"]
    Q --> L["Lambda Decoder/Fetcher\n(idempotent envelope)"]
    L --> S["Step Functions Workflow\nvalidate → STAC → catalog → telemetry"]
    S --> C["KFM STAC Catalog"]
    C --> G["Neo4j Graph"]
    G --> F["API & Focus Mode"]
~~~

### 1. SQS Subscription Contract

#### Queue Requirements

- Encrypted SQS queue (KMS-managed key).  
- SNS → SQS subscription with `sqs:SendMessage` scoped by `SourceArn` = NEXRAD topic.  
- Message retention: **4–14 days**, depending on pipeline tier.  
- Visibility timeout:  

  ~~~text
  visibility_timeout ≥ 2 × max_lambda_runtime
  ~~~

#### Optional FIFO Configuration

When FIFO is enabled:

- `MessageDeduplicationId` = `sha256(body.nexrad_key)` (or full object key).  
- `MessageGroupId` = `"nexrad"` or `"nexrad:<station>"`.  

This preserves ordering within **per-station/per-hour** groupings where required.

---

### 2. Lambda Decoder / Fetcher

Responsibilities:

1. Parse SNS → SQS payload into a **normalized envelope**.  
2. Extract S3 object key (NEXRAD file).  
3. Validate `bucket == "unidata-nexrad-level2"`.  
4. Fetch object metadata (size, ETag, version_id if present).  
5. Compute deterministic data checksum (e.g., SHA-256 of object).  
6. Compute **idempotency key**:

   ~~~text
   idempotency_key = sha256(bucket + key + checksum)
   ~~~

7. Forward a structured, **idempotent envelope** to the Step Functions state machine.

Error behavior:

- **Hard failures** (invalid schema, wrong bucket, permanent auth error) → DLQ.  
- **Soft failures** (network flakiness, throttling) → exponential backoff retry with deterministic schedule (see event-driven safety pattern).

---

### 3. Step Functions Workflow

Canonical workflow name (example): `kfm-atmo-nexrad-l2-ingest-v2`.

#### 3.1 Phases

1. **Validate-Input Node**

   - Validate envelope schema and required fields.  
   - Ensure bucket/topic IDs match expected values.  
   - Create initial PROV-O `Activity` node with `startedAtTime`.

2. **Generate-STAC-Item Node**

   - Parse radar volume filename into station, timestamp, scan type.  
   - Derive deterministic **STAC Item ID** (e.g., hash of station + timestamp + level).  
   - Build STAC 1.x Item with:

     - `geometry`: station cone or bounding box.  
     - `properties.datetime`: radar timestamp.  
     - `properties.kfm:station`, `kfm:product_level`, etc.  

3. **Write-To-KFM-Catalog Node**

   - WAL-protected write to STAC storage (`data/stac/atmo/nexrad-level2/items/`).  
   - Idempotent upsert: existing item with same ID + checksum is not duplicated.  
   - Update DCAT metadata if needed.

4. **Telemetry-Emit Node**

   - Emit energy, carbon, and cost telemetry fields:

     - `energy_kwh` (Lambda+Step Functions compute).  
     - `carbon_kgco2e` (regional factor).  
     - `cost_usd` (estimated AWS cost).  

   - Emit reliability metrics: latency, retries, DLQ counts.

5. **Commit & Finalize Node**

   - Close PROV-O Activity with `endedAtTime`.  
   - Record `prov:used` (NEXRAD source object) and `prov:generated` (STAC Item entity).  
   - Attach audit signature and reference to SBOM/SLSA attestations.

#### 3.2 Replay / Backfill Workflow

A dedicated replay state machine (e.g., `nexrad-replay-v2`) allows deterministic re-runs:

- Accepts **station/time windows**.  
- Hydrates the SQS queue or direct Step Functions input with synthetic events that mirror production envelopes.  
- Uses the **same DAG** and **same config**, with run-level seeds and config digests frozen.  
- Writes PROV-O and telemetry with explicit `kfm:replay = true`.

---

## 📦 Data & Metadata

### STAC Item Requirements

Each NEXRAD radar volume produces **one STAC Item**:

- **Core fields**

  - `id`: deterministic ID (e.g., hash over station + datetime + level + source checksum).  
  - `geometry`: station cone or station-centered bbox.  
  - `bbox`: bounding box for the station coverage (optional but recommended).  
  - `properties.datetime`: radar timestamp.  

- **Extensions / properties**

  - `properties.kfm:station_id`  
  - `properties.kfm:product_level` (e.g., "L2")  
  - `properties.kfm:source_bucket = "unidata-nexrad-level2"`  
  - `properties.kfm:source_key` (original object key)  
  - `properties.kfm:checksum_sha256` (payload checksum)  
  - `properties.kfm:energy_kwh`, `kfm:carbon_kgco2e`, `kfm:cost_usd`  

- **Assets**

  - `assets.raw` → original radar file in Unidata bucket (or mirrored location).  
  - `assets.derivative` → any decoded/translated format (e.g., COG, Zarr).  

### PROV-O Provenance

For each ingestion run:

- **Activity**

  - `prov:Activity` with ID:  

    ~~~text
    urn:kfm:activity:atmo:nexrad:l2:<run_id>
    ~~~

  - Links:

    - `prov:used` → NEXRAD source entity (`urn:kfm:entity:unidata:nexrad-l2:<bucket>/<key>`).  
    - `prov:generated` → STAC Item entity (`urn:kfm:entity:stac:item:nexrad-l2:<id>`).  
    - `prov:wasAssociatedWith` → pipeline agent (`urn:kfm:agent:pipeline:atmo-nexrad-l2-ingest@v11.2.4`).  

- **Entities**

  - Source S3 object entity with ETag, size, checksum.  
  - STAC Item entity with item ID and checksum.

All PROV-O documents are written as JSON-LD under:

~~~text
data/lineage/atmo/nexrad/sns-sqs-lambda/prov/<run-id>.jsonld
~~~

---

## 🧪 Validation & CI/CD

CI and runtime checks must cover:

- **Schema validation**

  - Envelope JSON vs. `atmo-ingestion-v1` schema.  
  - STAC Items vs. STAC 1.x + KFM STAC profiles.  
  - Telemetry payload vs. `schemas/telemetry/atmo-ingestion-v1.json`.

- **Contract checks**

  - Bucket must be `unidata-nexrad-level2`.  
  - SNS topic ARN must match `NewNEXRADLevel2Archive`.  
  - Idempotency keys must be stable and unique per content.

- **Determinism & idempotency**

  - Re-running the workflow on the same envelope must not produce duplicate Items.  
  - WAL logs must allow reconstruction of run state.

- **Telemetry**

  - Spans for each Step Functions state.  
  - Metrics: ingestion latency, error rate, DLQ depth, energy/carbon per run.  

The `.github/workflows/atmo-nexrad-sns-sqs-lambda.yml` workflow should:

- Run unit tests for envelope parsing and idempotency.  
- Validate example STAC Items and PROV-O docs.  
- Validate sample CI telemetry blobs.

---

## ⚖ FAIR+CARE & Governance

This pattern is **FAIR** because:

- NEXRAD ingestion outputs are cataloged as STAC & DCAT datasets with clear, stable IDs.  
- Provenance is recorded for each radar volume, enabling reuse and reproducibility.  

It is **CARE-aligned** because:

- Radar data here is **non-sensitive**, but overlapping use with sensitive overlays (e.g., heritage sites) relies on this ingestion being traceable and auditable.  
- Energy and carbon telemetry make atmospheric processing **transparent** and open to sustainability review.

Governance hooks:

- Ingestion policy for NEXRAD is documented in:  

  ~~~text
  docs/pipelines/atmo/nexrad/ingestion/sns-sqs-lambda/governance/ingestion-policy.md
  ~~~

- Any change to:

  - Source bucket or SNS topic ARN.  
  - STAC Item structure or provenance fields.  
  - Telemetry schema for atmo ingestion.

must be reviewed by:

- Atmospheric Systems Board, and  
- FAIR+CARE Oversight.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                 |
|----------:|------------|-------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial KFM-aligned ingestion pattern for new NEXRAD SNS topic + Step Functions. |
| v11.2.3  | 2025-12-01 | Prep work and preliminary policy scaffolding (internal draft).         |
| v11.2.2  | 2025-11-18 | STAC + PROV harmonization for atmo ingestion baselines.                |

---

<div align="center">

🌩️ **KFM v11.2.4 — NEXRAD SNS → SQS → Lambda/Step-Functions Ingestion Pattern**  
Deterministic Radar Ingestion · STAC/DCAT/PROV-Ready · FAIR+CARE Aligned  

[📘 Atmo Pipelines Index](../../../../README.md) · [📨 Event-Driven Safety Pattern](../../../../patterns/event-driven-ingestion-safety/README.md) · [⚖ Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>