---
title: "🧬 KFM v11.2.3 — NODD Stage Environment Overlay (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Stage-environment overlay configuration for the NOAA NODD SNS → SQS event-driven atmospheric ingestion pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/stage/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x config-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Environment Config"
intent: "nodd-sns-sqs-env-overlays-stage"
category: "Pipelines · Atmospheric · Config · Stage"

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
sunset_policy: "Superseded by next major NODD stage env overlay standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🧬 NODD Stage Environment Overlay  

`docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/stage/README.md`

Stage-environment overlay for the **NOAA NODD SNS → SQS atmospheric ingestion pipeline**.

The stage overlay:

- Mirrors **production topology and behavior** as closely as possible  
- Uses **non-production NODD endpoints** and credentials  
- Applies **SLO-aware but slightly safer limits** than prod  
- Serves as the final **pre-production proving ground** for code, config, and governance changes  

All stage behavior MUST remain deterministic and comparable to prod for the same inputs.

⸻

## 🗂 1. Directory Layout (Stage Overlay)

~~~text
docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/stage/
│
├── 📄 README.md                  # This file — stage overlay contract
│
├── 📄 nodd-env.stage.yaml        # Stage overlay (SNS/SQS endpoints, limits, telemetry, feature flags)
└── 📄 secrets-ref.stage.yaml     # References to stage secret managers / credentials (no raw secrets)
~~~

Any additional stage-only overlay files MUST be documented here and validated in CI.

⸻

## 🧭 2. Purpose & Scope (Stage)

The stage overlay is designed for:

- **Pre-production validation** of:
  - SNS/SQS bindings and policies  
  - NODD dataset contracts and routing  
  - Ingestion operators (`message-parse`, `integrity-check`, `metadata-extract`, `stac-register`)  
  - Replay engine and WAL-driven workflows  

- **Realistic load and behavior testing** without impacting production data  

Stage overlay MUST:

- Behave as **close to prod as possible**, except where strictly necessary for safety or cost  
- Use stage-specific:
  - SNS topic ARNs  
  - SQS queue ARNs  
  - Telemetry endpoints  

Stage overlay MUST NOT:

- Point to prod NODD endpoints  
- Embed secrets directly (only references allowed)  
- Diverge from prod semantics in ways that make stage tests misleading

⸻

## 🧱 3. `nodd-env.stage.yaml` — Shape & Responsibilities

The file `nodd-env.stage.yaml` follows the generic `NoddEnvOverlay` schema (see env-overlays index) with stage-specific values.

Conceptual responsibilities:

- **SNS / SQS mapping**
  - Map datasets defined in `config/datasets/` to stage NODD SNS topics and SQS queues  
  - Ensure DLQ and redrive policies mirror prod topology  

- **Replay defaults**
  - Batch sizes and rate limits close to prod, but with a slight safety margin  
  - `max_attempts` aligned with prod to surface retry behavior accurately  

- **Safety & feature flags**
  - `allow_global_replay` SHOULD be `false` by default (mirroring prod)  
  - Dataset kill-switch defaults SHOULD follow prod, unless testing requires a difference (documented)  

- **Telemetry**
  - `otel_endpoint` pointing at stage observability stack  
  - Sampling rates configured to give useful signal without prod-level cost  

All fields MUST validate against the canonical env overlay schema (for example, `nodd-env-overlay-v1.json`) and remain compatible with:

- `replay/replay-engine/safety-guards.md`  
- `replay/replay-engine/cli-spec.md`  
- `../../telemetry/README.md`  

⸻

## 🔑 4. `secrets-ref.stage.yaml` — Secret References

`secrets-ref.stage.yaml` contains **references** to stage secret-management entries, not the secrets themselves.

Conceptual content:

- IDs / ARNs / paths for:
  - Stage AWS roles / credential sources  
  - Stage OTel exporters and auth tokens  
  - Stage-only external services (if any)

Strict rules:

- MUST NOT include:
  - Plain-text credentials  
  - Tokens, passwords, or sensitive blobs  
- MAY include:
  - Secret manager keys (e.g., AWS Secrets Manager, SSM Parameter Store)  
  - Indirections used by deployment tooling

CI SHOULD run secret-lint rules to ensure no high-risk patterns appear in this file.

⸻

## ⚖ 5. Stage vs Dev/Prod Behavior

### 5.1 Relative to Dev

Stage overlay SHOULD:

- Use **larger batch sizes and higher concurrency** than dev  
- Cover **more datasets**, ideally matching prod coverage  
- Reduce experimentation-only flags:
  - `allow_global_replay` SHOULD be `false`  
  - Debug logging levels SHOULD be closer to prod

However, stage MAY still:

- Use lower telemetry sampling than prod for cost reasons  
- Host additional debug dashboards separate from prod

### 5.2 Relative to Prod

Stage overlay MUST:

- Mirror prod semantics:
  - Same WAL state machine behavior  
  - Same replay modes and safety guards  
  - Same governance and LangGraph gating behavior  

Differences SHOULD be limited to:

- Endpoints (stage vs prod accounts)  
- Capacity tuning (`max_batch_size`, `max_batches`, concurrency)  
- Telemetry destination and sampling levels

Any **intentional semantic difference** from prod MUST:

- Be documented in this README and/or `nodd-env.stage.yaml` comments  
- Be considered during incident simulations and pre-prod rehearsals

⸻

## 📡 6. Telemetry & Replay in Stage

Stage is where we validate **telemetry and replay behavior** under near-prod conditions:

- Replay engine:
  - Reads env `stage` and overlay values from `nodd-env.stage.yaml`  
  - Enforces safety guards similar to prod limits  

- Telemetry:
  - Metrics and traces flow to stage collectors and dashboards  
  - Stage dashboards mirror prod dashboard structure:
    - `../../telemetry/dashboards/nodd-ingestion-dashboard.md`  

- Alerts:
  - Stage may use similar alert rules but:
    - Routed to stage/on-call channels  
    - Possibly lower severity or different thresholds  

Replay-related tests (DLQ drains, incident simulations) SHOULD be exercised in stage before prod:

- Using selection specs from `replay/replay-engine/selection-spec.md`  
- Through runbooks under `../runbooks/`  

⸻

## 🧬 7. Governance & FAIR+CARE in Stage

Governance references apply in stage as in prod:

- `${governance_ref}`  
- `${ethics_ref}`  
- `${sovereignty_policy}`  

Stage overlay MUST:

- Enforce the same **governance gates and sovereignty rules** as prod  
- Ensure that:
  - Sensitive patterns are handled identically (redaction, generalization)  
  - Validation and governance error codes behave the same way  

Differences in stage MAY include:

- More detailed logging of **non-sensitive** metadata for debugging  
- Additional governance test datasets and synthetic edge cases

Stage overlays MUST NOT:

- Disable governance checks that are mandatory in prod  
- Introduce replay or ingestion paths that bypass governance logic

⸻

## 🧪 8. CI & Validation (Stage Overlay)

CI responsibilities for stage overlay:

- Validate `nodd-env.stage.yaml` and `secrets-ref.stage.yaml` against:
  - Env overlay schema  
  - Secret-reference rules (no embedded secrets)  

- Check:
  - Consistency of SNS/SQS mappings with stage infrastructure manifests  
  - Replay defaults and safety limits are within acceptable ranges for stage  
  - `allow_global_replay` is configured according to policy (typically `false`)  

- Execute non-prod tests:
  - Ingestion smoke tests against stage NODD endpoints  
  - Replay engine dry-runs using stage overlay  
  - Spot validation of stage dashboards and alerts

Any change to stage overlay in `main` MUST:

- Pass CI  
- Be traceable to a change request, issue, or incident simulation  

⸻

## 📘 9. Version History

| Version  | Date       | Notes                                                                                                 |
|---------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD stage env overlay README; defined layout, purpose, overlay roles, and CI expectations.   |

---

<div align="center">

🧬 NODD Stage Environment Overlay · KFM v11.2.3  

Near-Prod · SLO-Aware · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Env Overlays](../README.md) ·  
[📘 Dataset Contracts](../../datasets/README.md) ·  
[♻️ Replay Engine](../../../replay/replay-engine/README.md) ·  
[⚖ Governance Charter](${governance_ref})

</div>
