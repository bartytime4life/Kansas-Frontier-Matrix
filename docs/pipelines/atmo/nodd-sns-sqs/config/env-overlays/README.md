---
title: "🌐 KFM v11.2.3 — NODD Environment Overlay Configs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Environment-specific configuration overlays (dev/stage/prod) for the NOAA NODD SNS → SQS ingestion pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/README.md"

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

signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Environment Config Index"
intent: "nodd-sns-sqs-env-overlays-index"
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
sunset_policy: "Superseded by next major NODD env overlay standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🌐 NODD Environment Overlay Configs  

`docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/README.md`

Environment-specific overlay configuration for the **NOAA NODD SNS → SQS event-driven atmospheric ingestion pipeline**.

These overlays allow KFM to:

- Keep a **single canonical config** for datasets, topics, queues, and telemetry  
- Apply **dev/stage/prod differences** (ARNs, URLs, limits, feature flags) in a **deterministic, documented** way  
- Avoid environment drift while preserving safety and reproducibility  

All overlays are **declarative**, **versioned**, and validated in CI.

⸻

## 🗂 1. Directory Layout (Env Overlays)

~~~text
docs/pipelines/atmo/nodd-sns-sqs/config/env-overlays/
│
├── 📄 README.md                          # This file — env overlay index
│
├── 📁 dev/
│   ├── 📄 nodd-env.dev.yaml              # Dev overlay (low limits, test endpoints)
│   └── 📄 secrets-ref.dev.yaml           # Pointers to secret managers / test creds
│
├── 📁 stage/
│   ├── 📄 nodd-env.stage.yaml            # Stage overlay (near-prod, safe limits)
│   └── 📄 secrets-ref.stage.yaml
│
└── 📁 prod/
    ├── 📄 nodd-env.prod.yaml             # Prod overlay (real ARNs, SLO-tuned limits)
    └── 📄 secrets-ref.prod.yaml          # Indirections to secret stores (no secrets in repo)
~~~

Notes:

- Filenames are indicative; CI enforces actual presence and naming rules.  
- No raw secrets are stored here; only **references** (ARNs, secret IDs, logical keys).

⸻

## 🧭 2. Purpose & Scope

This directory exists to:

- Capture **environment-specific differences** for the NODD atmospheric pipeline in one governed place.  
- Ensure that:
  - SNS topic ARNs, SQS queue names, and DLQ bindings are correct per environment.  
  - Capacity and safety limits (batch sizes, concurrency) are tuned by `env`.  
  - Telemetry endpoints and sampling rates are environment-aware.  

Included in scope:

- Environment-mapped:
  - SNS/SQS identifiers and endpoints  
  - Replay engine defaults (batch sizes, max attempts)  
  - Telemetry destinations and sampling configs  
  - Feature flags or kill-switch defaults per dataset  

Out of scope:

- Dataset-level contracts (see `../datasets/README.md`).  
- Application secrets/credentials (handled by secret managers).  
- Non-NODD pipelines.

⸻

## 🧱 3. Overlay Model (Conceptual)

Env overlays layer on top of **base config** defined elsewhere under `config/`:

1. **Base config**  
   - Dataset contracts (`config/datasets/`)  
   - SNS topic maps (`config/sns-topics.json` or equivalent)  
   - SQS queue contracts (`config/sqs-queues.json`)  
   - Default telemetry and replay settings  

2. **Env overlay** (`env-overlays/<env>/nodd-env.<env>.yaml`)  
   - Adds or overrides:
     - Concrete ARNs / URLs  
     - Per-env limits and thresholds  
     - Flags controlling replay and DLQ behavior  

3. **Resolution**  
   - At runtime or during deployment:
     - Base config is loaded first.  
     - Env overlay is merged on top using a deterministic merge strategy.  
     - Resulting config is what the pipeline uses.

The merge strategy MUST be:

- **Explicit and deterministic**  
- **Documented** in architecture/config docs  
- **Tested** in CI with representative env files

⸻

## 🧮 4. Env Overlay Shape (Conceptual)

Each `nodd-env.<env>.yaml` SHOULD follow a shared schema, for example:

- `apiVersion`: `kfm.nodd.env/v1alpha1`  
- `kind`: `NoddEnvOverlay`  

Key sections (shape only):

- `metadata`
  - `env` (e.g., `dev`, `stage`, `prod`)  
  - `description`  
  - `labels` (e.g., `priority`, `owner_team`)  

- `sns`
  - `base_region`  
  - `topic_overrides` (map of dataset → topic ARN)  

- `sqs`
  - `queue_overrides` (dataset/queue name → ARN, DLQ ARN)  
  - `visibility_timeouts`  
  - `redrive_policies`  

- `replay_defaults`
  - `max_attempts`  
  - `max_batch_size`  
  - `max_batches`  
  - `rate_limits`  

- `telemetry`
  - `otel_endpoint`  
  - `sampling_rate`  
  - `log_level`  

- `safety_flags`
  - `allow_global_replay` (expected `false` in `prod`)  
  - `kill_switch_defaults` (dataset-level booleans)  

- `governance`
  - Optional env-specific governance knobs (e.g., stricter logging rules in `prod`).

The concrete JSON Schema for env overlays lives under:

- `schemas/json/nodd-env-overlay-v1.json` (referenced in the global schemas index).

⸻

## 🧪 5. Dev / Stage / Prod Intent

### 5.1 `dev/`

- Purpose:
  - Fast iteration, safe experimentation.  
- Behavior:
  - Low batch sizes and aggressive guardrails.  
  - Non-production SNS/SQS endpoints.  
  - May allow `allow_global_replay: true` for test-only scenarios.  

### 5.2 `stage/`

- Purpose:
  - Pre-production validation, near-prod topology.  
- Behavior:
  - Capacity and limits close to `prod`, but with:
    - Safer replay thresholds  
    - Lower telemetry cost if needed  

### 5.3 `prod/`

- Purpose:
  - Full reliability and SLO adherence.  
- Behavior:
  - Tuned batch sizes, rate limits, and SQS settings.  
  - `allow_global_replay` MUST be `false` without explicit governance waiver.  
  - Kill-switch defaults may be stricter for high-risk datasets.

⸻

## 📡 6. Telemetry & Replay Integration

Env overlays should:

- Configure **replay engine defaults**:
  - `replay_defaults.max_batch_size`  
  - `replay_defaults.max_batches`  
  - `replay_defaults.max_attempts`  
- Feed into replay engine safety guards (`replay/replay-engine/safety-guards.md`).  

For telemetry:

- `telemetry.otel_endpoint` and sampling rates MUST match:
  - Environment observability strategy  
  - Cost and data-retention policies  

Dashboards under:

- `../../telemetry/dashboards/`  

should reflect env-specific differences while using consistent metric names.

⸻

## 🧬 7. Governance, FAIR+CARE & Sovereignty

Although env overlays are mostly operational:

- They MUST NOT weaken governance in `prod` relative to `stage` without Council approval.  
- Any env-specific overrides that:
  - Change logging patterns  
  - Adjust sensitivity handling  
  - Affect replay / governance gating  

MUST be:

- Documented and reviewed.  
- Compatible with:
  - `${governance_ref}`  
  - `${ethics_ref}`  
  - `${sovereignty_policy}`  

Env files MUST NEVER embed:

- Raw secrets  
- Sensitive coordinates (beyond what underlies NODD itself)

⸻

## 🧪 8. CI & Validation

CI MUST enforce:

- **Schema validation**:
  - Every `nodd-env.<env>.yaml` validates against `nodd-env-overlay-v1.json`.  

- **Env coverage**:
  - For each environment used in deployment workflows (`dev`, `stage`, `prod`), a corresponding overlay MUST exist.  

- **No drift checks**:
  - Where appropriate, config tests SHOULD:
    - Compare `stage` and `prod` overlays for unintended diffs.  
    - Ensure critical flags (e.g., `allow_global_replay`) are set correctly.

- **Integration tests**:
  - Non-prod runs MUST confirm:
    - Correct SNS/SQS endpoints are used.  
    - Replay limits and safety guards respond to overlay changes.

Any change to env overlays in `prod` MUST:

- Be associated with a tracked change / incident.  
- Be reviewed by the Atmospheric Systems / Reliability working group.

⸻

## 📘 9. Version History

| Version  | Date       | Notes                                                                                                        |
|---------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD env overlay index; defined dev/stage/prod overlay model, schema expectations, and CI behavior. |

---

<div align="center">

🌐 NODD Environment Overlay Configs · KFM v11.2.3  

Config-First · Env-Aware · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Config](../README.md) ·  
[📘 Dataset Contracts](../datasets/README.md) ·  
[♻️ Replay Engine](../../replay/replay-engine/README.md) ·  
[⚖ Governance Charter](${governance_ref})

</div>
