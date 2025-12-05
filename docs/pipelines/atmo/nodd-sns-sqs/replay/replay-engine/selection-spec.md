---
title: "🎯 KFM v11.2.3 — NODD Replay Selection Spec (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Canonical selection-spec schema and semantics for the NODD WAL-driven replay engine used by the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/selection-spec.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x replay-selection-contract compatible"
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

doc_kind: "Replay Engine Selection Spec"
intent: "nodd-sns-sqs-replay-engine-selection-spec"
category: "Pipelines · Atmospheric · Replay · Engine"

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
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD replay selection-spec standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🎯 NODD Replay Selection Spec  

`docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/selection-spec.md`

Canonical **selection-spec schema** for the NODD WAL-driven replay engine.

This document defines:

- The **shape** of replay selection specs (YAML/JSON).  
- How filters map to **WAL queries** and **guardrails**.  
- How selection specs integrate with:
  - `nodd-replay` CLI  
  - Runbooks (`../runbooks/`)  
  - WAL record model and state machine  

Selection specs are **governed artifacts**: they are versioned, auditable, and may be attached to incident records and CI jobs.

⸻

## 🧭 1. Purpose & Design Goals

Selection specs exist to:

- Encode **replay intent declaratively**:
  - Datasets  
  - Time windows  
  - Status and error classes  
  - Limits and guardrails  

- Provide a **portable artifact** that can be:
  - Reviewed by humans  
  - Re-used in `dev` / `stage` / `prod`  
  - Executed via CLI and schedulers

- Enable **deterministic replays**:
  - Running the same selection against the same WAL slice MUST yield the same candidate set (modulo allowed WAL changes).

Design goals:

- **Explicit scope** — no “implicit everything” selections.  
- **Guard-aware** — selection specs cooperate with safety limits.  
- **Versioned** — schema version changes are tracked and validated.  
- **Tool-agnostic** — usable by CLI, automated jobs, and governance tooling.

⸻

## 🧱 2. Top-Level Schema (Conceptual)

A selection spec is a single document with these top-level fields:

- `apiVersion` (required)  
- `kind` (required)  
- `metadata` (required)  
- `spec` (required)

Conceptual outline:

~~~yaml
apiVersion: "kfm.nodd.replay/v1alpha1"
kind: "ReplaySelection"

metadata:
  name: "nodd-dlq-drain-2025-12-04"
  description: "Drain failed GOES-ABI records from DLQ after schema hotfix."
  env: "prod"
  labels:
    replay_reason: "dlq-drain"
    incident_id: "INC-2025-1234"

spec:
  mode: "failed-only"
  filters:
    datasets: ["goes-abi"]
    status: ["failed"]
    error_codes: ["stac_validation_failed"]
    event_time:
      start: "2025-12-04T00:00:00Z"
      end:   "2025-12-04T06:00:00Z"
    attempts:
      max: 5

  limits:
    max_records: 5000
    batch_size: 500
    max_batches: 20

  options:
    dry_run: false
    allow_repair_and_replace: false
~~~

Actual JSON Schema / validation is implemented in code; this document defines **semantics** and **required fields**.

⸻

## 🧾 3. Metadata Block

### 3.1 Fields

`metadata` MUST include:

- `name` (string, required)  
  - Human-readable, unique within the context of a run or incident.  

- `description` (string, required)  
  - Brief description of why this selection exists.  

- `env` (string, required)  
  - Target environment (`dev`, `stage`, `prod`, ...).  
  - MUST match CLI `--env` or environment variable `KFM_ENV` during execution.

- `labels` (object, optional but strongly recommended)  
  - Arbitrary key/value labels used for:
    - Incident correlation (`incident_id`)  
    - Replay reason (`replay_reason`)  
    - Owning team (`owner_team`)  

Example:

~~~yaml
metadata:
  name: "nodd-goes-abi-schema-fix-replay"
  description: "Replay failed GOES-ABI records after schema v3 hotfix."
  env: "stage"
  labels:
    replay_reason: "incident"
    incident_id: "INC-2025-1187"
    owner_team: "kfm-atmo"
~~~

### 3.2 Semantics

- `labels.replay_reason` SHOULD align with allowed values used in WAL:
  - `dlq-drain`, `incident`, `backfill`, `test` (non-prod).  
- CLI and telemetry MAY propagate these labels into spans and metrics.

⸻

## 🎮 4. Spec: Mode & Filters

The `spec` block defines how WAL records are selected.

### 4.1 Mode

`spec.mode` (string, required):

- Allowed values:
  - `"failed-only"` (default; safest)  
  - `"repair-and-replace"` (advanced, governance-gated)  
  - `"backfill"` (for fill-missing workflows)  

Mode semantics MUST match the replay engine spec (`README.md`).

### 4.2 Filters Block

`spec.filters` (object, required) MUST define:

- Dataset filters  
- Status / error filters  
- Time filters  
- Attempt limits

#### 4.2.1 Dataset Filters

Fields:

- `datasets` (array of strings, optional but strongly recommended)  
- `datasets_exclude` (array of strings, optional)

At least one of:

- `datasets`  
- OR an explicit governance-approved config that allows global dataset selection in non-prod.

Example:

~~~yaml
filters:
  datasets: ["goes-abi", "nexrad-l2"]
~~~

Semantics:

- `datasets` is an inclusion list.  
- `datasets_exclude` MAY be used with `datasets` or a global selection (non-prod) for advanced workflows; in `prod`, global selection without `datasets` is forbidden by guards.

#### 4.2.2 Status & Error Filters

Fields:

- `status` (array of strings, optional)  
  - Allowed values: `failed`, `succeeded`, `pending`, `quarantined`.  

- `error_codes` (array of strings, optional)  
  - E.g., `stac_validation_failed`, `schema_mismatch`, `governance_hard_fail`.  

If omitted in `failed-only` mode:

- Engine defaults to `status = ["failed"]` (subject to safety guards).

Example:

~~~yaml
filters:
  status: ["failed"]
  error_codes: ["stac_validation_failed", "schema_mismatch"]
~~~

#### 4.2.3 Time Filters

At least one time dimension MUST be specified:

- `event_time` (object, optional)  
  - `start` (RFC3339 string)  
  - `end`   (RFC3339 string)  

- `created_at` (object, optional)  
  - `start` (RFC3339 string)  
  - `end`   (RFC3339 string)  

- `time_range_overlap` (object, optional)  
  - `start` (RFC3339 string)  
  - `end`   (RFC3339 string)  

Example:

~~~yaml
filters:
  event_time:
    start: "2025-12-04T00:00:00Z"
    end:   "2025-12-04T03:00:00Z"
~~~

In `prod`, selection specs without any time filters MUST be rejected by safety guards unless explicitly overridden.

#### 4.2.4 Attempts Filters

Fields:

- `attempts` (object, optional):

  - `max` (integer, optional)  
    - Default: engine’s configured `max_attempts`.  

  - `min` (integer, optional)  
    - Rarely used; for advanced introspection.

Example:

~~~yaml
filters:
  attempts:
    max: 4
~~~

Semantics:

- Records with `attempts > max` MUST NOT be replayed.  
- CLI MUST show how many records are excluded by attempts limits during `select` and `dry-run`.

#### 4.2.5 Direct wal_id Filters (Advanced)

For surgical replays:

- `wal_ids` (array of strings, optional)  

Usage:

- For very small, targeted replays (e.g., 1–10 records).  

Guard:

- When `wal_ids` is present:
  - Dataset/time filters MAY be omitted, but environment-specific guardrails STILL apply (e.g., `prod` vs non-prod).  
  - Engine MUST validate that each `wal_id` belongs to the expected environment and WAL backend.

⸻

## 🧮 5. Spec: Limits & Options

### 5.1 Limits Block

`spec.limits` (object, optional but strongly recommended):

- `max_records` (integer, optional)  
  - Maximum number of WAL records this selection is allowed to target.  
  - Guardrail: cannot exceed environment-level `max_selection_records`.  

- `batch_size` (integer, optional)  
  - Suggested batch size for replay; obeys environment-level caps.  

- `max_batches` (integer, optional)  
  - Upper bound on number of batches; prevents accidental massive replays.

Example:

~~~yaml
limits:
  max_records: 10000
  batch_size: 500
  max_batches: 30
~~~

### 5.2 Options Block

`spec.options` (object, optional):

- `dry_run` (boolean, default false)  
  - When true, engine MUST treat selection as simulation only.  

- `allow_repair_and_replace` (boolean, default false)  
  - For `repair-and-replace` mode, MUST be explicitly true and governance-approved.  

- `respect_kill_switch` (boolean, default true)  
  - If false, overrides dataset kill-switches (for non-prod testing only); forbidden in `prod`.

- `notes` (string, optional)  
  - Free-form operator notes for future readers.

⸻

## 🧪 6. Example Selection Specs

### 6.1 DLQ Drain — Failed-Only Replay (Prod)

~~~yaml
apiVersion: "kfm.nodd.replay/v1alpha1"
kind: "ReplaySelection"

metadata:
  name: "nodd-goes-dlq-drain-2025-12-04"
  description: "Replay GOES-ABI DLQ failures after STAC schema hotfix."
  env: "prod"
  labels:
    replay_reason: "dlq-drain"
    incident_id: "INC-2025-2301"
    owner_team: "kfm-atmo"

spec:
  mode: "failed-only"
  filters:
    datasets: ["goes-abi"]
    status: ["failed"]
    error_codes: ["stac_validation_failed"]
    event_time:
      start: "2025-12-04T00:00:00Z"
      end:   "2025-12-04T06:00:00Z"
    attempts:
      max: 3

  limits:
    max_records: 5000
    batch_size: 500
    max_batches: 15

  options:
    dry_run: false
    allow_repair_and_replace: false
~~~

### 6.2 Incident Replay — Pilot Batch (Stage)

~~~yaml
apiVersion: "kfm.nodd.replay/v1alpha1"
kind: "ReplaySelection"

metadata:
  name: "nodd-hrrr-incident-pilot"
  description: "Pilot replay for HRRR schema regression window."
  env: "stage"
  labels:
    replay_reason: "incident"
    incident_id: "INC-2025-2199"

spec:
  mode: "failed-only"
  filters:
    datasets: ["hrrr"]
    status: ["failed"]
    created_at:
      start: "2025-12-03T18:00:00Z"
      end:   "2025-12-03T19:00:00Z"
    attempts:
      max: 2

  limits:
    max_records: 500
    batch_size: 100
    max_batches: 5

  options:
    dry_run: true
    allow_repair_and_replace: false
~~~

### 6.3 Surgical Replay — Specific wal_ids (Dev)

~~~yaml
apiVersion: "kfm.nodd.replay/v1alpha1"
kind: "ReplaySelection"

metadata:
  name: "nodd-surgical-dev-replay"
  description: "Replay specific WAL records in dev for debugging."
  env: "dev"
  labels:
    replay_reason: "test"

spec:
  mode: "failed-only"
  filters:
    wal_ids:
      - "wal_01HFZC8YVE2V63Z0TQ3Q2N4G1J"
      - "wal_01HFZC9C34Y9FZR9EN6P1VCKVS"
    attempts:
      max: 5

  limits:
    max_records: 20
    batch_size: 5
    max_batches: 4

  options:
    dry_run: false
    respect_kill_switch: true
~~~

⸻

## 🧩 7. Execution Mapping (CLI & Engine)

### 7.1 CLI Mapping

Given a selection spec saved at `selection.yaml`, the CLI command:

~~~text
nodd-replay from-spec \
  --env prod \
  --selection-file selection.yaml \
  --run \
  --confirm
~~~

MUST:

- Load and validate:
  - `apiVersion`, `kind`, `metadata.env`, `spec.*`  
- Enforce safety guards defined in `safety-guards.md`.  
- Execute replay according to:
  - `mode`, `filters`, `limits`, `options`.

`nodd-replay select` and `dry-run` MAY also emit selection specs with `--save-spec`.

### 7.2 Engine Mapping

Engine MUST:

- Translate `filters` into WAL queries.  
- Apply `limits` and guardrails as described in replay engine and safety-guards specs.  
- Propagate `metadata.labels` and `spec.mode` into:
  - WAL `replay_reason`  
  - Telemetry labels  

⸻

## 🧪 8. Validation & CI

Validation responsibilities:

- **Schema validation**  
  - Selection specs MUST be JSON Schema–validated in CI for:
    - Example specs in docs  
    - Specs stored in infrastructure or incident repos.

- **Compatibility validation**  
  - `apiVersion` MUST be compatible with current engine version.  
  - CLI MUST fail with a clear error if spec `apiVersion` is unsupported.

- **Guardrail tests**  
  - CI MUST include tests where:
    - Over-broad or malformed specs are rejected.  
    - Non-prod vs prod behavior differs appropriately.

Any change to:

- Required fields  
- Field semantics  
- Allowed modes or filter names  

MUST:

- Update this document.  
- Update CLI help and replay engine docs.  
- Rev the `apiVersion` (e.g., `v1alpha2`) if change is breaking.

⸻

## 📘 9. Version History

| Version  | Date       | Notes                                                                                                                   |
|---------:|------------|-------------------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD replay selection-spec; defined apiVersion, metadata, filters, limits, options, and CLI/engine integration. |

---

<div align="center">

🎯 NODD Replay Selection Spec · KFM v11.2.3  

Declarative · Guarded · WAL-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Engine](README.md) ·  
[🧾 CLI Spec](cli-spec.md) ·  
[🛡️ Safety Guards](safety-guards.md) ·  
[🔗 Integration Notes](integration-notes.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
