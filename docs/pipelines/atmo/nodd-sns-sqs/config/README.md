---
title: "⚙️ KFM v11.2.3 — NOAA NODD SNS → SQS Configuration Contracts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed configuration contracts for NOAA NODD SNS topics, SQS queues, DLQs, and dataset-specific ingestion rules in the KFM event-driven atmospheric pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/config/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x config-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Configuration Specification"
intent: "nodd-sns-sqs-config-spec"
category: "Pipelines · Atmospheric · Config"

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
sunset_policy: "Superseded by next major NODD configuration standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# ⚙️ NOAA NODD SNS → SQS Configuration Contracts  

`docs/pipelines/atmo/nodd-sns-sqs/config/README.md`

**Governed configuration model for NOAA NODD SNS topics, SQS queues, DLQs, and dataset-specific ingestion contracts in the KFM atmospheric auto-update pipeline.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Config-Declarative-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document defines the **configuration contracts** that control the NOAA NODD SNS → SQS ingestion pipeline in KFM:

- SNS topics, subscriptions, and message schemas.  
- SQS queues, DLQs, and retry policies.  
- Dataset-specific ingestion contracts (routing, priorities, validation profiles).  
- Environment overlays (dev/stage/prod) and governance hooks.

Configuration is:

- **Declarative** — stored as YAML/JSON in this directory.  
- **Versioned** — changes tracked via git and subject to CI checks.  
- **Deterministic** — the same config + code must produce the same routing and behavior.  

No ad hoc or implicit configuration is permitted.

---

## 🗂 2. Directory Layout (Emoji-Prefix Standard)

Configuration docs live under `docs/pipelines/atmo/nodd-sns-sqs/config/`:

    docs/pipelines/atmo/nodd-sns-sqs/config/
    │
    ├── 📄 README.md                          # This file (config contracts index)
    │
    ├── 🛰️ sns-topics.yaml                    # Declared SNS topics and filters (logical spec)
    ├── 📬 sqs-queues.yaml                    # SQS queue, DLQ, and retry policies (logical spec)
    │
    ├── 🧩 datasets/                          # Dataset-specific ingestion contracts
    │   ├── 📄 goes-abi.yaml                  # GOES ABI config (topics, routes, STAC profile)
    │   ├── 📄 nexrad-l2.yaml                 # NEXRAD Level II config
    │   ├── 📄 nexrad-l3.yaml                 # NEXRAD Level III config
    │   ├── 📄 hrrr.yaml                      # HRRR model output config
    │   └── 📄 surface-obs.yaml               # Surface observations config
    │
    └── 🌱 env-overlays/                      # Environment-specific overrides (logical)
        ├── 📄 dev.yaml                       # Dev overrides (reduced fan-out, test buckets)
        ├── 📄 stage.yaml                     # Stage overrides
        └── 📄 prod.yaml                      # Prod-specific routing and limits

Actual cloud resources (ARNs, secrets, credentials) MUST live in infrastructure IaC repositories; this directory describes the **logical contracts**, not secrets.

---

## 🛰 3. SNS Topic Configuration

Logical SNS topics and filters are captured in `sns-topics.yaml`.

Conceptual structure:

    topics:
      - name: nodd-goes-abi
        description: "NOAA NODD GOES ABI notifications"
        dataset: goes-abi
        subject_pattern: "OBJECT_CREATED:*"
        message_schema_version: "1.0"
        filters:
          - attribute: "product"
            values: ["ABI-L1b-Rad", "ABI-L2-CMIP"]
      - name: nodd-nexrad-l2
        dataset: nexrad-l2
        subject_pattern: "OBJECT_CREATED:*"
        message_schema_version: "1.0"

Rules:

- Each topic must map to one or more **KFM dataset IDs**.  
- Message schema versions must be compatible with `sns-schema/message-v1.json`.  
- Filters must be **inclusive and low-cardinality**, preventing unnecessary fan-out.

Any change to `sns-topics.yaml` MUST be validated in CI against:

- Schema for SNS topic config.  
- Pipeline tests verifying routing behavior.

---

## 📬 4. SQS Queue & DLQ Configuration

SQS queue contracts are defined in `sqs-queues.yaml`.

Conceptual structure:

    queues:
      - name: nodd-primary-queue
        description: "Primary NODD ingest queue"
        visibility_timeout_seconds: 300
        max_receive_count: 5
        dlq: nodd-dlq
        redrive_policy: "standard"
        tags:
          purpose: "nodd-ingestion"
          env: "shared"
      - name: nodd-dlq
        description: "Dead-letter queue for NODD pipeline"
        retention_days: 14

Contract requirements:

- All SNS subscriptions used by this pipeline must target **queues declared here**.  
- Visibility timeouts MUST be tuned to ingestion time bounds (documented in tests).  
- DLQs must exist and be referenced by runbooks in `replay/runbooks/dlq-drain-runbook.md`.  

No queue may be used in the code unless it is documented here.

---

## 🧩 5. Dataset Ingestion Contracts

Per-dataset configuration in `datasets/*.yaml` defines:

- Dataset metadata and routing.  
- Priority and sampling behavior.  
- Validation and STAC profiles.

Conceptual structure:

    dataset: "goes-abi"
    description: "GOES-East/West ABI scenes via NODD"
    sns_topics:
      - nodd-goes-abi
    sqs_queue: "nodd-primary-queue"
    priority: "high"
    stac_collection_id: "kfm-goes-abi"
    validation_profile: "goes-abi-v1"
    governance_profile: "standard-atmo"
    watermark_strategy: "per-tile-with-safety-margin"
    replay_policy:
      allowed: true
      requires_approval: false

Rules:

- `dataset` must match canonical KFM dataset IDs used in STAC and the graph.  
- `validation_profile` and `governance_profile` must map to existing definitions in validation/gate docs.  
- `replay_policy` controls how replays are allowed for the dataset (bound to replay runbooks).

Any new dataset integration must include:

- A `datasets/<dataset>.yaml` file.  
- Tests ensuring SNS/SQS routing and ingestion behave as intended.

---

## 🌱 6. Environment Overlays

`env-overlays/*.yaml` provide **logical overrides** per environment:

- `dev.yaml` — reduced fan-out, test buckets, smaller concurrency.  
- `stage.yaml` — near-prod behavior, but with safe limits.  
- `prod.yaml` — full routing and resource usage.

Conceptual overlay pattern:

    overrides:
      sqs_queues:
        nodd-primary-queue:
          visibility_timeout_seconds: 120
      datasets:
        goes-abi:
          priority: "low"
          stac_collection_id: "kfm-goes-abi-dev"

Rules:

- Overlays must be **pure overrides**; they cannot introduce new datasets or queues not declared in base configs.  
- Effective config = base config + environment overlay, resolved deterministically.  
- CI must test at least `dev` and `prod` overlays for shape and invariants.

Secrets, ARNs, and credentials are NEVER stored here; they must be wired via infrastructure and environment variables.

---

## 🧪 7. CI Validation & Contract Tests

Configuration is subject to CI:

- **Schema validation**:
  - `sns-topics.yaml`, `sqs-queues.yaml`, `datasets/*.yaml`, and `env-overlays/*.yaml` must pass JSON Schema/SHACL validation.

- **Static routing checks**:
  - No dataset without an SNS topic or SQS queue.  
  - No SNS topic without a mapped dataset.  
  - No queue reference to a non-existent DLQ.

- **Simulation tests**:
  - Given synthetic events, routing logic (message → SNS topic → SQS queue → dataset) must match config.

- **Change impact checks**:
  - CI may compute a diff of datasets or routing behavior and require human review for impactful changes.

No configuration change can merge without passing these checks.

---

## ⚖️ 8. Governance & FAIR+CARE Considerations

Configuration interacts with governance in several ways:

- Datasets involving **sensitive or sovereign content** MUST reference an appropriate `governance_profile`.  
- Certain datasets may require:
  - Restricted SNS fan-out.  
  - Separate SQS queues with tighter access controls.  
  - Different DLQ retention or replay policies.

Configuration must **not** loosen governance protections without review:

- Changing governance profiles or routing for sensitive datasets requires FAIR+CARE and sovereignty review.  
- CI may enforce additional checks for datasets flagged as sensitive (e.g., archaeology, tribal overlays).

---

## 🕰 9. Version History

| Version  | Date       | Notes                                                                                          |
|---------:|------------|------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial configuration spec for NODD SNS → SQS; defined SNS, SQS, dataset contracts, env overlays. |

---

<div align="center">

### ⚙️ NOAA NODD SNS → SQS Config · KFM v11.2.3

Declarative · Deterministic · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Pipeline](../README.md) ·  
[🧠 Operators](../operators/README.md) ·  
[📊 Telemetry](../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>