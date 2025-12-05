---
title: "🛰️ KFM v11.2.3 — NODD Prod Environment Overlay (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Production-environment overlay configuration for the NOAA NODD SNS → SQS event-driven atmospheric ingestion pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/prod/README.md"

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
intent: "nodd-sns-sqs-env-overlays-prod"
category: "Pipelines · Atmospheric · Config · Prod"

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
sunset_policy: "Superseded by next major NODD prod env overlay standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🛰️ NODD Prod Environment Overlay  

`docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/prod/README.md`

Production-environment overlay for the **NOAA NODD SNS → SQS atmospheric ingestion pipeline**.

The prod overlay:

- Maps the pipeline to **production NODD SNS/SQS endpoints**  
- Applies **SLO-tuned capacity and safety limits**  
- Enforces the strictest **governance, sovereignty, and FAIR+CARE rules**  
- Serves as the **authoritative configuration** for NODD ingestion in KFM’s production environment  

All prod behavior MUST be deterministic, reproducible, and fully observable.

⸻

## 🗂 1. Directory Layout (Prod Overlay)

~~~text
docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/prod/
│
├── 📄 README.md                  # This file — prod overlay contract
│
├── 📄 nodd-env.prod.yaml         # Prod overlay (SNS/SQS endpoints, limits, telemetry, feature flags)
└── 📄 secrets-ref.prod.yaml      # References to prod secret managers / credentials (no raw secrets)
~~~

Any additional prod-only overlay files MUST be documented here and validated via CI.

⸻

## 🧭 2. Purpose & Scope (Prod)

The prod overlay is designed for:

- **Live, operational ingestion** of NOAA NODD datasets into KFM  
- **Strict adherence** to:
  - Queue-age and latency SLOs  
  - Replay safety guards  
  - Governance and sovereignty policies  

It MUST:

- Use **production** SNS topic ARNs and SQS queue ARNs for NODD  
- Mirror the **logical semantics** exercised in stage  
- Provide stable configuration for:
  - Ingestion workers  
  - Replay engine  
  - Telemetry and alerting  

It MUST NOT:

- Embed secrets directly  
- Loosen safety or governance constraints relative to stage without explicit Council approval  
- Allow experimental flags that can materially alter production behavior outside governed change windows

⸻

## 🧱 3. `nodd-env.prod.yaml` — Shape & Responsibilities

The file `nodd-env.prod.yaml` follows the shared `NoddEnvOverlay` schema (see env-overlays index) with **production** values.

Conceptual responsibilities:

- **SNS / SQS mapping**
  - Map each NODD dataset (`config/datasets/`) to its production:
    - SNS topic ARN  
    - SQS queue ARN  
    - DLQ ARN and redrive policy  
  - Ensure FIFO/standard semantics and dedupe rules match pipeline contracts  

- **Replay defaults**
  - Set:
    - `max_batch_size`  
    - `max_batches`  
    - `max_attempts`  
    - Rate limits  
  - Values MUST be tuned to maintain:
    - Ingest latency SLOs  
    - Queue-age SLOs  
    - Error budget policies  

- **Safety & feature flags**
  - `allow_global_replay` MUST be `false` in prod (unless overridden via formal governance exception).  
  - Dataset kill-switch defaults MUST reflect risk evaluations for each dataset.  

- **Telemetry**
  - Configure:
    - Production OTel endpoints  
    - Production logging sinks  
    - Sampling rates and log levels appropriate for prod  

All fields MUST validate against `nodd-env-overlay-v1.json` and remain compatible with:

- `replay/replay-engine/safety-guards.md`  
- `replay/replay-engine/cli-spec.md`  
- `../../telemetry/README.md`  

⸻

## 🔑 4. `secrets-ref.prod.yaml` — Secret References

`secrets-ref.prod.yaml` contains **references** (not secrets) to production secret-management entries.

Examples (conceptual):

- ARNs / IDs / paths for:
  - Production AWS roles and credential sources  
  - Production OTel / logging credentials  
  - Any third-party endpoints used in prod monitoring or alerting  

Rules:

- MUST NOT contain:
  - Plain-text access keys  
  - Tokens, passwords, or sensitive blobs  
- MAY contain:
  - Keys or ARNs used to look up secrets in:
    - AWS Secrets Manager  
    - SSM Parameter Store  
    - Equivalent secret management systems  

CI MUST include secret-lint checks to prevent accidental leakage in this file.

⸻

## ⚖ 5. Relationship to Dev & Stage

Prod overlay is the **reference behavior**; dev and stage approximate it.

- Relative to dev:
  - Larger batch sizes and concurrency, tuned for real workloads  
  - No “experiment-only” flags (e.g., `allow_global_replay` MUST remain `false`)  
  - Telemetry and alerting fully aligned with SRE practices  

- Relative to stage:
  - Same semantics:
    - WAL state machine  
    - Replay modes  
    - Governance and LangGraph gating  
  - Potentially:
    - More stringent safety limits  
    - Different alert routing and severities  
    - Different observability retention policies  

Any intentional difference from stage MUST be:

- Documented in:
  - This README and/or comments in `nodd-env.prod.yaml`  
- Considered in:
  - Incident rehearsals  
  - Playbooks and runbooks that transition from stage to prod

⸻

## 📡 6. Telemetry, Replay & SLOs in Prod

Prod overlay drives the **authoritative** behavior of:

- **Replay engine**:
  - Reads env=`prod` and overlay defaults from `nodd-env.prod.yaml`  
  - Enforces strict safety guards (batch, rate, attempts) defined in `replay/replay-engine/safety-guards.md`  

- **Telemetry**:
  - Metrics, traces, and logs MUST:
    - Flow to production OTel collectors and logging systems  
    - Include `env="prod"` and relevant dataset/replay labels  

- **Dashboards & Alerts**:
  - Dashboards described in:
    - `../../telemetry/dashboards/nodd-ingestion-dashboard.md`  
  - Alerts described in:
    - `../../telemetry/alerts/nodd-alert-policies.md`  
  - MUST be wired to prod overlay fields:
    - Queue ARNs  
    - Replay limits  
    - SLO thresholds  

Prod overlay changes MAY alter behavior of:

- DLQ alerts  
- Replay rate alerts  
- Latency/queue-age SLO alarms  

Such changes MUST be executed via governed change management.

⸻

## 🧬 7. Governance, FAIR+CARE & Sovereignty in Prod

Prod overlay MUST implement the **strictest** governance stance:

- Governance charter: `${governance_ref}`  
- FAIR+CARE guidelines: `${ethics_ref}`  
- Sovereignty policy: `${sovereignty_policy}`  

Requirements:

- No governance bypass paths in prod.  
- Governance gates (LangGraph, STAC/DCAT validation, CARE/FAIR rules) must be **equal to or stricter than** stage.  
- Any replay or ingestion feature that interacts with:
  - Sensitive areas  
  - Sovereign territories  
  - Cultural heritage data (if later intersected with NODD-derived layers)  
  MUST obey masking/generalization rules defined elsewhere in the KFM governance stack.

Prod overlays MUST NEVER:

- Disable governance checks that are mandatory at the system level.  
- Introduce ad hoc flags that weaken sovereignty or ethics enforcement.

⸻

## 🧪 8. CI & Validation (Prod Overlay)

CI responsibilities for the prod overlay:

- Validate `nodd-env.prod.yaml` and `secrets-ref.prod.yaml` against:
  - Env overlay schema (`nodd-env-overlay-v1.json`)  
  - Secret-lint rules (no raw secrets)  

- Check:
  - SNS/SQS ARNs match production infrastructure manifests.  
  - Replay defaults fall within approved ranges for prod.  
  - `allow_global_replay` is `false` or absent.  
  - Kill-switch defaults do not contradict Council-approved risk settings.

- Integration tests (non-prod or shadow environments) SHOULD periodically confirm:

  - A sample of prod overlay values remains accurate.  
  - Changes to prod overlay do not break:
    - Replay engine semantics  
    - WAL behavior  
    - Telemetry pipelines  

Any change to prod overlay MUST:

- Be associated with:
  - Change request / ticket  
  - Or an incident follow-up  
- Pass CI and, when applicable, stage rehearsals before prod deployment.

⸻

## 📘 9. Version History

| Version  | Date       | Notes                                                                                               |
|---------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD prod env overlay README; defined layout, purpose, overlay roles, and CI expectations.  |

---

<div align="center">

🛰️ NODD Prod Environment Overlay · KFM v11.2.3  

SLO-Tuned · Strictly Governed · Production-Grade  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Env Overlays](../README.md) ·  
[📘 Dataset Contracts](../../datasets/README.md) ·  
[♻️ Replay Engine](../../../replay/replay-engine/README.md) ·  
[⚖ Governance Charter](${governance_ref})

</div>
