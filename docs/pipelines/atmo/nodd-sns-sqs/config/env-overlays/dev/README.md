---
title: "🧪 KFM v11.2.3 — NODD Dev Environment Overlay (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Development-environment overlay configuration for the NOAA NODD SNS → SQS event-driven atmospheric ingestion pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/dev/README.md"

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
intent: "nodd-sns-sqs-env-overlays-dev"
category: "Pipelines · Atmospheric · Config · Dev"

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
sunset_policy: "Superseded by next major NODD dev env overlay standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🧪 NODD Dev Environment Overlay  

`docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/dev/README.md`

Development-environment overlay for the **NOAA NODD SNS → SQS atmospheric ingestion pipeline**.

The dev overlay:

- Maps the pipeline to **non-production SNS/SQS endpoints**  
- Applies **aggressive safety limits** (small batches, strict guardrails)  
- Enables **experimentation and debugging** without risking production data or SLOs  

All dev behavior MUST remain reproducible and governed, even when experiments are enabled.

⸻

## 🗂 1. Directory Layout (Dev Overlay)

~~~text
docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/dev/
│
├── 📄 README.md                 # This file — dev overlay contract
│
├── 📄 nodd-env.dev.yaml         # Dev-specific overlay (SNS/SQS, limits, telemetry, feature flags)
└── 📄 secrets-ref.dev.yaml      # References to dev secret managers / test credentials (no raw secrets)
~~~

Additional dev-only overlay files (if introduced) MUST be documented here and validated by CI.

⸻

## 🧭 2. Purpose & Scope (Dev)

The dev overlay is designed for:

- **Fast feedback** on code, config, and schema changes  
- Safe testing of:
  - SNS/SQS integration  
  - Operator logic (`message-parse`, `metadata-extract`, `stac-register`)  
  - Replay engine and WAL behavior  
- Experimentation with:
  - New datasets and contracts  
  - Telemetry/observability setups  

Dev overlay MUST NOT:

- Point at production NODD topics or SQS queues  
- Relax governance to the point that tests become non-representative of prod behavior  
- Embed secrets directly (only references are allowed)

⸻

## 🧱 3. `nodd-env.dev.yaml` — Shape & Responsibilities

The dev overlay file `nodd-env.dev.yaml` follows the generic env overlay schema (`NoddEnvOverlay`) but with dev-specific values.

Conceptual responsibilities:

- **SNS/SQS endpoints**
  - Use dev/test AWS account or sandbox ARNs
  - Optionally reduced dataset coverage (subset of topics)

- **Replay defaults**
  - Very small `max_batch_size` and `max_batches`
  - Conservative `max_attempts` (to surface bugs early)
  - Possibly more verbose logging for replay operations

- **Safety & experimentation flags**
  - May set `allow_global_replay: true` for targeted dev-only tests
  - May enable additional debug flags (e.g., more detailed validation traces)

- **Telemetry**
  - `otel_endpoint` pointing to dev observability stack
  - Higher sampling for debugging (subject to resource constraints)

All fields MUST validate against `nodd-env-overlay-v1.json` and be compatible with:

- `replay/replay-engine/safety-guards.md`  
- `replay/replay-engine/cli-spec.md`  

⸻

## 🔑 4. `secrets-ref.dev.yaml` — Secret References

`secrets-ref.dev.yaml` holds **references** to secret-management entries, not the secrets themselves.

Typical content (conceptual:

- References to:
  - AWS credential profiles / role ARNs for dev  
  - OTel auth tokens (if required)  
  - Any dev-only API keys or endpoints

Rules:

- MUST NOT contain:
  - Plain-text access keys  
  - Tokens, passwords, or sensitive payloads  
- MAY contain:
  - Paths/IDs/ARNs for secret managers (e.g., AWS Secrets Manager, SSM Parameter Store)

CI SHOULD include checks to ensure no high-risk patterns appear in this file.

⸻

## 🧪 5. Dev Defaults vs Stage/Prod

The dev overlay SHOULD:

- Use **tighter safety limits** than stage/prod:
  - Smaller `max_records` and `batch_size`
  - Lower concurrency caps
- Allow more flexibility for:
  - Global replays (for test data only)
  - Experimental datasets and temporary configs

But dev MUST still:

- Respect the WAL state machine  
- Enforce deterministic behavior for the same inputs  
- Pass governance gates in the same logical way as prod (even if pointed at different endpoints)

Any behavior that differs intentionally from prod MUST be:

- Documented in this README and/or `nodd-env.dev.yaml` comments  
- Considered when interpreting dev test results

⸻

## 📡 6. Telemetry & Replay in Dev

In `dev`, overlays often:

- Configure replay engine to:
  - Use low `max_batch_size` (e.g., tens of records)
  - Allow isolated test replays without impacting shared queues
- Configure telemetry to:
  - Send traces/metrics/logs to a dev OTel collector
  - Potentially increase sampling to aid debugging

Integration points:

- Replay engine:
  - Reads environment (`dev`) and overlay values from `nodd-env.dev.yaml`
- Dashboards:
  - Dev dashboards should be clearly segregated from stage/prod
- Alerts:
  - Dev alerts MAY be more lenient or purely informational

⸻

## 🧬 7. Governance & FAIR+CARE in Dev

Even in dev:

- Governance references remain in effect:
  - `${governance_ref}`
  - `${ethics_ref}`
  - `${sovereignty_policy}`

Requirements:

- No logging of sensitive content (even if synthetic)
- No use of real sensitive datasets without corresponding protections
- Any test datasets emulating sensitive conditions MUST be clearly labeled as synthetic

Dev overlays MUST NEVER:

- Disable governance gates or sovereignty checks completely  
- Introduce ad hoc bypass paths that do not also exist (governed) in stage/prod

⸻

## 🧪 8. CI & Validation (Dev Overlay)

CI responsibilities for `dev` overlay:

- Validate `nodd-env.dev.yaml` and `secrets-ref.dev.yaml` against:
  - Env overlay schema
  - Secret-reference lint rules (no raw secrets)
- Ensure:
  - All required sections are present
  - Dev overlay is internally consistent (e.g., SQS/SNS identifiers resolve in dev)
- Run smoke tests:
  - Replay engine dry-runs using dev overlay
  - Basic ingestion tests against dev NODD datasets (or synthetic equivalents)

Any change to this directory in `main` MUST:

- Pass CI  
- Be traceable to a change ticket or documented ref (even for dev-only tweaks)

⸻

## 📘 9. Version History

| Version  | Date       | Notes                                                                                              |
|---------:|------------|----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD dev env overlay README; defined layout, purpose, overlay roles, and CI expectations.  |

---

<div align="center">

🧪 NODD Dev Environment Overlay · KFM v11.2.3  

Safe-by-Default · Experiment-Friendly · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Env Overlays](../README.md) ·  
[📘 Dataset Contracts](../../datasets/README.md) ·  
[♻️ Replay Engine](../../../replay/replay-engine/README.md) ·  
[⚖ Governance Charter](${governance_ref})

</div>
