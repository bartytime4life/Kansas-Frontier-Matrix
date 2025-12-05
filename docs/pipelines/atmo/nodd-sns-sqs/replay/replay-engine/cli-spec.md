---
title: "🧾 KFM v11.2.3 — NODD Replay Engine CLI Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Canonical CLI contract for the NODD WAL-driven replay engine used by the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/cli-spec.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x replay-cli-contract compatible"
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

doc_kind: "Replay Engine CLI Spec"
intent: "nodd-sns-sqs-replay-engine-cli-spec"
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
sunset_policy: "Superseded by next major NODD replay engine CLI standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🧾 NODD Replay Engine CLI Specification  

`docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/cli-spec.md`

Canonical **command-line interface (CLI)** contract for the NODD WAL-driven replay engine used by the NOAA NODD SNS → SQS ingestion pipeline.

This document defines:

- Supported **commands** and **subcommands**  
- Standard **flags**, **selection arguments**, and **output formats**  
- Required **safety guards** and **dry-run behaviors**  
- How the CLI integrates with **WAL, SQS, telemetry, and runbooks**

The CLI MUST be treated as a **governed API**: breaking changes require a version bump and governance review.

⸻

## 🧭 1. Purpose & Scope

The replay engine CLI:

- Provides a **human- and automation-facing** interface for WAL-driven replays.  
- Encodes **selection specs**, **batch execution**, and **dry-run analysis**.  
- Is used by:
  - On-call SREs following replay runbooks  
  - Scheduled jobs (cron/EventBridge)  
  - CI jobs validating replay behavior in non-prod

Out of scope:

- Direct low-level WAL mutations (handled via service layer or migrations).  
- Ad hoc SQS message re-injection without WAL correlation.  
- Arbitrary shell scripts that bypass this CLI and the safety guards it enforces.

⸻

## 🧱 2. CLI Overview

### 2.1 Binary Name

The canonical binary name is:

- `nodd-replay`

Alternative wrappers (e.g., `kfm-nodd-replay`) MUST be thin shims around this CLI and MUST NOT change semantics.

### 2.2 Top-Level Command Shape

High-level structure:

- `nodd-replay select` — Construct and validate a selection spec (no WAL mutation).  
- `nodd-replay dry-run` — Simulate replay for a selection (no WAL mutation or SQS enqueue).  
- `nodd-replay run` — Execute a replay for a given selection spec (mutating).  
- `nodd-replay from-spec` — Run using a pre-saved selection spec file.  
- `nodd-replay inspect` — Inspect WAL records for a selection without replay.  

Each subcommand MAY support both **CLI flags** and **YAML/JSON selection files**, but MUST always produce a machine-readable summary on demand.

⸻

## 🔧 3. Global Flags & Environment

### 3.1 Global Flags

The following global flags MUST be supported by all subcommands:

- `--env <string>`  
  - Environment identifier: `dev`, `stage`, `prod`, etc.  
  - Default MAY be read from `KFM_ENV`, but explicit `--env` is preferred in automation.

- `--config <path>`  
  - Path to replay engine config file (YAML/JSON) containing:
    - WAL connection info  
    - SQS endpoints/ARNs  
    - Default batch limits  

- `--output <format>`  
  - Output format for summaries:
    - `table` (human-friendly)  
    - `json` (machine-friendly)  
    - `yaml` (machine-friendly)  

- `--log-level <level>`  
  - One of: `error`, `warn`, `info`, `debug`.  
  - Default: `info` in non-interactive automation, `warn` in interactive usage.

- `--selection-file <path>`  
  - Path to a selection spec file (YAML/JSON).  
  - If provided, this MAY substitute selection flags where allowed.

### 3.2 Environment Variables

The CLI MUST support reading defaults from environment variables:

- `KFM_ENV` — Default environment (`dev`, `stage`, `prod`).  
- `KFM_WAL_DSN` — WAL database/endpoint connection string.  
- `KFM_SQS_PRIMARY_QUEUE` — Primary NODD SQS queue.  
- `KFM_SQS_DLQ_QUEUE` — NODD DLQ queue ARN/name (for cross-checks).  

Environment-derived values MUST be overridden by explicit flags when present.

⸻

## 🎯 4. Selection Arguments (Common Across Commands)

Selection flags define **which WAL records** are targeted. They are shared across `select`, `dry-run`, `run`, and `inspect`:

- `--dataset <id>`  
  - Single dataset ID (e.g., `goes-abi`, `nexrad-l2`).  

- `--dataset-in <ids>`  
  - Comma-separated list of datasets.

- `--status <value>`  
  - One of: `failed`, `succeeded`, `quarantined`, `pending`.  
  - Default for replay: `failed`.

- `--error-code <code>`  
  - Filter by exact `last_error_code`.  

- `--error-code-in <codes>`  
  - Comma-separated list of error codes.

- `--event-time-start <RFC3339>`  
- `--event-time-end <RFC3339>`  
  - Filter by `event_time` window.

- `--created-after <RFC3339>`  
- `--created-before <RFC3339>`  
  - Filter by WAL `created_at`.

- `--attempts-max <int>`  
  - Only include records with `attempts ≤ attempts-max`.  
  - Default SHOULD be the engine’s configured `max_attempts`.

- `--limit <int>`  
  - Hard cap on number of WAL records returned in selection.  
  - Used for pilot batches and safety.

If both `--selection-file` and explicit selection flags are provided:

- CLI MUST either:
  - Merge flags into file-based selection (with a clear precedence rule documented), or  
  - Reject the combination as ambiguous and require one or the other.

⸻

## 🧪 5. `select` Command

### 5.1 Purpose

- Build and validate a **selection spec** from CLI flags or an input file.  
- Return a **summary of candidate WAL records** without modifying WAL or SQS.  
- Optionally persist the spec for later use with `dry-run` or `run`.

### 5.2 Usage Shape

~~~text
nodd-replay select [GLOBAL FLAGS] [SELECTION FLAGS] \
  [--save-spec <path>] \
  [--show-examples <n>]
~~~

### 5.3 Behavior

- Query WAL using selection criteria.  
- Produce:

  - Count of candidate WAL records.  
  - Summary by:
    - `dataset`  
    - `status`  
    - `last_error_code`  

- If `--save-spec` is provided:
  - Write a stable, versioned selection spec to the given path.

- If `--show-examples <n>` is provided:
  - Include up to `n` sample `wal_id` values and key fields for inspection.

### 5.4 Output

Depending on `--output`:

- `table`: human-readable summary (counts, top error codes).  
- `json` / `yaml`: structured object including:
  - the selection spec  
  - aggregated stats  
  - optional sample records

⸻

## 🧪 6. `dry-run` Command

### 6.1 Purpose

- Simulate replay for a selection without:
  - Changing WAL states  
  - Enqueuing messages to SQS  

Used to estimate impact and verify that replay scope and guardrails are acceptable.

### 6.2 Usage Shape

~~~text
nodd-replay dry-run [GLOBAL FLAGS] [SELECTION FLAGS] \
  [--batch-size <int>] \
  [--max-batches <int>] \
  [--mode <mode>]
~~~

Where:

- `--mode` is one of:
  - `failed-only` (default)  
  - `repair-and-replace`  
  - `backfill`

### 6.3 Behavior

- Loads selection spec (from flags or `--selection-file`).  
- Applies guardrails (batch size, max batches, attempts).  
- Computes:

  - Total WAL records selected.  
  - Predicted number of batches.  
  - Estimated message volume (for SQS and STAC writes).  

- DOES NOT:

  - Change `status` in WAL.  
  - Write to SQS.  
  - Alter STAC or provenance.

### 6.4 Output

- Summary of:
  - `total_records`, `batch_size`, `estimated_batches`  
  - Distribution by dataset and error code  
  - Mode (`failed-only`, `repair-and-replace`, `backfill`)

The JSON/YAML output SHOULD be consumable by automation to decide whether to proceed with `run`.

⸻

## ▶️ 7. `run` Command

### 7.1 Purpose

- Execute an actual replay for a given selection, subject to safety limits.

### 7.2 Usage Shape

~~~text
nodd-replay run [GLOBAL FLAGS] [SELECTION FLAGS] \
  [--batch-size <int>] \
  [--max-batches <int>] \
  [--mode <mode>] \
  [--confirm]
~~~

- `--confirm`:
  - Required in non-interactive contexts or when `--output` is `json` or `yaml`.  
  - In interactive mode, CLI MAY prompt for confirmation if `--confirm` is omitted.

### 7.3 Behavior

For each batch:

1. Select next subset of WAL records according to selection and guardrails.  
2. Apply WAL transitions:
   - `status: "failed" → "pending"` (for failed-only mode).  
   - `replay_reason = "dlq-drain"` or `"incident"` (depending on runbook context).  
3. Reconstruct ingestion work and enqueue:
   - Equivalent to original SNS/SQS messages, or  
   - Engine-specific replay tasks that feed standard operators.  
4. Track progress and update telemetry.

The command MUST:

- Stop if guardrails are violated (e.g., max attempts reached).  
- Provide a clear exit code:
  - `0` on success  
  - Non-zero on failures (with structured error output if `--output json`/`yaml`).

### 7.4 Output

Per run:

- Batches processed  
- Records attempted / succeeded / failed / quarantined  
- Any new error classes encountered

⸻

## 📦 8. `from-spec` Command

### 8.1 Purpose

- Execute `dry-run` or `run` from a previously saved selection spec, without reconstructing the spec from flags.

### 8.2 Usage Shape

~~~text
nodd-replay from-spec [GLOBAL FLAGS] \
  --selection-file <path> \
  [--mode <mode>] \
  [--batch-size <int>] \
  [--max-batches <int>] \
  [--dry-run | --run] \
  [--confirm]
~~~

Behavior:

- Validates selection spec version and compatibility.  
- Executes `dry-run` or `run` logic as if the same spec had been created via flags.  

Useful for:

- Repeatable incident replays.  
- Coordinated replays across environments (with environment-aware differences in config).

⸻

## 🔍 9. `inspect` Command

### 9.1 Purpose

- Inspect WAL records matching a selection without replaying them.  
- Used in investigation and runbook workflows.

### 9.2 Usage Shape

~~~text
nodd-replay inspect [GLOBAL FLAGS] [SELECTION FLAGS] \
  [--limit <int>] \
  [--show-fields <fields>]
~~~

- `--show-fields <fields>`:
  - Comma-separated list of additional WAL fields to include (e.g., `object_uri,time_range_start,time_range_end,last_error_code`).

Behavior:

- Return a paginated view or sample of WAL records.  
- Never modifies WAL or queues.

⸻

## 🛡 10. Exit Codes & Error Handling

The CLI MUST use consistent exit codes:

- `0` — Success (command completed as intended).  
- `1` — Generic error (unhandled exception or framework-level failure).  
- `2` — Invalid arguments, malformed selection, or incompatible spec version.  
- `3` — Guardrail violation (e.g., batch limits, max attempts exceeded).  
- `4` — Backend failures (WAL or SQS unreachable).  

On failure, and when `--output json` or `yaml` is set, the CLI SHOULD emit:

- `error_code` (stable machine-readable code)  
- `error_message` (redacted summary)  
- `context` (selection and environment snapshot, where safe)

⸻

## 📡 11. Telemetry Integration (CLI-Level)

The CLI MUST emit metrics/spans that complement engine-level telemetry:

- Metrics:
  - `nodd_sns.replay_cli_invocations_total{command,env}`  
  - `nodd_sns.replay_cli_failures_total{command,env,error_code}`  

- Spans:
  - One span per CLI invocation, including:
    - Command and mode  
    - Selection spec hash or ID  
    - Environment and dataset count

These metrics tie CLI usage back to replay outcomes and incident records.

⸻

## 🧪 12. CI & Contract Validation

CI MUST ensure that:

- All documented commands and flags exist and have help text.  
- `--help` for each command prints a stable and complete description.  
- Example invocations in runbooks:
  - Parse and map cleanly to CLI commands defined here.  
- Selection specs produced by `select --save-spec` are:
  - Version-tagged.  
  - Accepted by `from-spec` in compatible CLI versions.

Breaking changes to:

- Command names  
- Flag names  
- Flag semantics

MUST be treated as CLI contract changes and require:

- New CLI minor/major version  
- Updated documentation and runbooks  
- Governance review

⸻

## 📘 13. Version History

| Version  | Date       | Notes                                                                                                              |
|---------:|------------|--------------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD replay engine CLI spec; defined commands, selection flags, safety guards, and CI/telemetry contracts. |

---

<div align="center">

🧾 NODD Replay Engine CLI Spec · KFM v11.2.3  

WAL-First · Deterministic · Runbook-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Engine](README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[🧰 Runbooks](../runbooks/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
