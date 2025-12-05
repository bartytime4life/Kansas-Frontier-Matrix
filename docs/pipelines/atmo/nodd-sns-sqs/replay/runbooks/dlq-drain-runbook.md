---
title: "🧹 KFM v11.2.3 — NODD DLQ Drain Runbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed incident runbook for draining and replaying Dead-Letter Queue (DLQ) messages in the NOAA NODD SNS → SQS ingestion pipeline using WAL-safe semantics."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/dlq-drain-runbook.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x replay-contract compatible"
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

doc_kind: "Replay Runbook"
intent: "nodd-sns-sqs-dlq-drain-runbook"
category: "Pipelines · Atmospheric · Replay · Runbooks"

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
sunset_policy: "Superseded by next major NODD replay runbook standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🧹 NODD DLQ Drain Runbook  

`docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/dlq-drain-runbook.md`

Incident runbook for **safely draining and replaying SQS Dead-Letter Queue (DLQ) messages** for the NOAA NODD SNS → SQS ingestion pipeline.

This runbook ensures that:

- DLQ processing is **WAL-safe** and **deterministic**.  
- Replays **do not amplify bugs** or create duplicate STAC/provenance writes.  
- All actions are traceable and aligned with CARE/FAIR and sovereignty policies.

DLQ drains MUST NEVER bypass the NODD WAL semantics defined under:

- `replay/wal/README.md`  
- `replay/wal/wal-record-model.md`  
- `replay/wal/wal-state-machine.md`

⸻

## 1. Purpose & Severity

### 1.1 Purpose

Use this runbook when:

- DLQ alerts fire (for example, `NODD-DLQ-RATE-CRIT`).  
- DLQ depth is growing or has reached a threshold that requires action.  
- You need to replay DLQ messages after fixing underlying issues.

Goals:

- Safely drain DLQ without data loss.  
- Respect WAL and replay semantics.  
- Avoid repeated ingestion failures and non-deterministic outcomes.

### 1.2 Typical Triggers

- Alert:
  - `NODD-DLQ-RATE-CRIT` (DLQ SLO breach).  
- Dashboards:
  - DLQ depth increasing over time.  
  - DLQ rate spike correlated with validation or governance errors.  

### 1.3 Severity Levels

- P1: DLQ growth threatens data completeness or hides critical failures in `prod`.  
- P2: Sustained DLQ accumulation without immediate downstream impact.  
- P3: Planned DLQ drain after known fixes (e.g., after a schema hotfix).

⸻

## 2. Preconditions & Safety Checks

Before draining DLQ:

1. Confirm environment

   - Identify `env` (`dev`, `stage`, `prod`).  
   - For `prod`, a DLQ drain MUST have:
     - An incident or change ticket.  
     - A clear, written scope.

2. Confirm root cause is understood or strongly suspected

   - Review validation and governance error metrics:
     - `nodd_sns.validation_errors_total{error_type}`.  
   - Consult:
     - `validation-error-investigation-runbook.md` (if errors spiked).  
     - Application / infra change logs.

   If the underlying error cause is unknown:
   - Treat as P1 and escalate for investigation **before** large-scale replay.

3. Verify WAL health

   - Check:
     - WAL backend reachable and healthy.  
     - No unusual spikes in WAL errors.  
   - If WAL is degraded, **do not** proceed; fix WAL first.

4. Confirm message → WAL correlation

   - DLQ messages MUST carry:
     - `wal_id` and `dataset` (or equivalent) in attributes or body.  
   - If correlation is broken for a subset:
     - Handle them separately and manually.  
     - Never mass-replay untracked messages.

5. Check capacity & queue state

   - Inspect primary queue metrics:
     - Depth and age.  
   - If primary queue is already delayed:
     - Coordinate with `delayed-queue-runbook.md` and `capacity-tuning-runbook.md` before adding replay load.

6. Notify stakeholders

   - For `stage`/`prod`:
     - Announce planned DLQ drain in `kfm-nodd-sre` and incident/change channel.  
     - Include scope (datasets, time window, approximate volume).

⸻

## 3. Detection & Triage

Determine the **shape** of the DLQ problem:

1. Volume and trend

   - Measure:
     - Current DLQ depth.  
     - DLQ rate over last 15–60 minutes.  
   - Determine if:
     - The situation is stable, growing, or decreasing.

2. Error-type breakdown

   - For a sample of DLQ messages (via WAL or message attributes), identify:
     - Dominant `last_error_code` values in WAL.  
     - Whether errors are:
       - Schema/validation-related.  
       - Governance-related.  
       - IO/network-related.  
       - Unknown/unclassified.

3. Dataset breakdown

   - Compute DLQ volume by `dataset`.  
   - This indicates whether:
     - Only one or a small set of datasets are affected.  
     - The problem is systemic across all NODD data.

4. Time-window characterization

   - Determine the time window:
     - Are DLQ items clustered around a specific deploy or upstream change?  
     - Are they consistently generated over a long period?

5. Confirm fix readiness

   For each major error class you plan to replay:

   - Verify that a fix is in place:
     - E.g., schema patch, code fix, governance rule adjustment.  
   - For classes that are not yet resolved:
     - Do **not** replay them; they will simply fail again.

⸻

## 4. Stabilize (Immediate Actions)

If DLQ growth is active and uncontrolled:

1. Pause non-essential replays and backfills

   - Prevent additional load while you investigate DLQ contents.  
   - Ensure replay jobs are stopped for affected datasets.

2. Consider temporary dataset kill-switch

   - If a non-critical dataset is producing a high volume of DLQ messages:
     - Pause ingestion for that dataset until the issue is fixed.

3. Confirm no active major deploys

   - If a relevant deploy is in progress:
     - Coordinate with release owners before any mass DLQ action.

4. Set explicit DLQ drain scope

   - Example scopes:
     - Only messages with a specific `last_error_code`.  
     - Only a given time range.  
     - Only specific `dataset` values.

   No DLQ drain should proceed without a clearly defined scope.

⸻

## 5. Diagnose (WAL-Centric DLQ Analysis)

All DLQ analysis MUST be anchored to the WAL.

1. Extract sample WAL records

   - Use `wal_id` from a representative set of DLQ messages to fetch associated WAL records.  
   - Confirm fields:
     - `status` (expected `failed` or `quarantined`).  
     - `last_error_code`, `last_error_message`.  
     - `dataset`, `object_uri`, `time_range_start`, `time_range_end`.  

2. Classify error codes

   - Group by `last_error_code`, for example:
     - `validation_failed_schema_mismatch`  
     - `governance_hard_fail`  
     - `integrity_missing_object`  
     - `stac_validation_failed`  
     - `io_error_upstream`  

3. Identify replayable vs non-replayable classes

   Replayable (after fix):

   - Transient IO/network issues now resolved.  
   - Schema mismatches due to a deploy that has since been fixed.  
   - Known upstream anomalies that are now handled.

   Non-replayable until further work:

   - `governance_hard_fail` without a new policy.  
   - Permanent upstream object loss (e.g., consistent 404 with no recovery path).

4. Confirm WAL state consistency

   - Each DLQ message with a `wal_id` MUST have:
     - A corresponding WAL record.  
     - `status` in `failed` or `quarantined` state.  

   If mismatches are found:
   - Document them, handle them as special manual cases.

⸻

## 6. Remediate — DLQ Drain & Replay (Step-by-Step)

Perform replays in **bounded batches**, using WAL as the orchestrator.

### 6.1 Define Replay Plan

1. Document:

   - Datasets to include.  
   - Error codes/classes targeted.  
   - Time windows (start and end).  
   - Batch sizes per run (for example, 500–2000 messages per batch).  

2. Decide environment path

   - Optional dry-run or partial drain in `stage` using a copied DLQ segment, when feasible.  
   - For `prod`, start with a small pilot batch.

3. Coordinate capacity

   - Ensure worker capacity is sufficient:
     - If backlog in primary queue exists, coordinate with `delayed-queue-runbook.md` and `capacity-tuning-runbook.md`.  

### 6.2 Transition WAL Records for Replay

Replay actions MUST be driven by WAL:

1. Select WAL records

   Example selection criteria (conceptual):

   - `status = "failed"`  
   - `dataset ∈ {chosen datasets}`  
   - `last_error_code ∈ {error codes now fixed}`  
   - `created_at` within chosen time window  
   - `attempts < max_attempts`  

2. Mark for replay

   - For each selected WAL record:
     - Set `status = "pending"` from `failed`.  
     - Increment `attempts` if your implementation increments on claim, not on mark.  
     - Set `replay_reason = "dlq-drain"`.  

   All transitions MUST respect `wal-state-machine.md`.

3. Re-enqueue / trigger replay

   - Re-introduce work in a controlled way:
     - Rebuild SNS/SQS messages from WAL.  
     - Or directly schedule internal replay jobs that use WAL as the source.

   Never push messages back to QUEUE without ensuring WAL is updated first.

### 6.3 Process Replay Batches

For each replay batch:

1. Limit size

   - Keep batch sizes small enough to:
     - Avoid saturating workers.  
     - Observe effects between batches.

2. Monitor during replay

   - Watch:
     - DLQ depth (should decrease or remain stable).  
     - Primary queue depth/age.  
     - Validation errors and `replay_mismatch_total`.  

3. Stop on unexpected signals

   - If replayed messages still fail with the same `last_error_code`, or `replay_mismatch_total` increases:
     - Stop the drain for that error class.  
     - Return records to `failed` or `quarantined` as appropriate.  
     - Investigate before continuing.

### 6.4 Handling Non-Replayable Records

For records that remain unreplayable:

1. Decide long-term state

   - Typically:
     - `status = "quarantined"`.  
     - `last_error_code` documenting the permanent issue.

2. Maintain documentation

   - Track non-replayable classes in:
     - Runbooks or issue trackers.  
     - Dataset-specific documentation if they require special handling.

3. Confirm governance stance

   - Some governance failures may require:
     - Policy updates.  
     - Additional restrictions.  
     - Consultation with CARE/sovereignty stakeholders.

⸻

## 7. Verify — Post-Drain Health Checks

After DLQ drain operations:

1. Confirm DLQ metrics

   - DLQ depth at or near zero (for selected scope).  
   - DLQ rate back to normal or near zero.  
   - No ongoing `NODD-DLQ-RATE-CRIT` alerts.

2. Confirm primary queue and latency

   - Primary queue depth and age within SLO.  
   - Ingest latency P90 below target thresholds for priority datasets.

3. Confirm WAL consistency

   - Replayed records:
     - Now have `status = "succeeded"` or `quarantined` (depending on outcomes).  
   - No unexpected spikes in:
     - `wal_records_total{status="failed"}`.  
     - `replay_mismatch_total`.

4. Confirm no new error classes emerged

   - Examine `last_error_code` distributions for any new patterns created by replay.  
   - If new codes appear, consider additional fixes before further drains.

5. Confirm downstream correctness

   - Spot-check:
     - STAC Items for sampled replays.  
     - Provenance entries.  
     - Downstream dashboards or derived products.

⸻

## 8. Postmortem & Governance

For any significant DLQ drain, especially in `prod`:

1. Incident record or change log

   - Include:
     - Scope and volume of DLQ drain.  
     - Error classes involved.  
     - Time windows and batch sizes.  
     - Metrics before and after.

2. Root cause analysis

   - Document:
     - Upstream changes.  
     - Code bugs or config issues.  
     - Telemetry or alert gaps.

3. Policy and configuration updates

   - If new validation/gov rules were needed:
     - Capture them in:
       - Pipeline config.  
       - Telemetry and alert policies.  
       - Governance docs.

4. Runbook updates

   - Update this runbook and:
     - `validation-error-investigation-runbook.md`  
     - `incident-replay-runbook.md`  
     - `capacity-tuning-runbook.md`, if relevant.

5. Governance review

   - Provenance & Reliability Council SHOULD:
     - Confirm replays preserved determinism.  
     - Confirm CARE/FAIR and sovereignty obligations were respected (no unsafe logging of sensitive content).

⸻

## 9. Version History

| Version  | Date       | Notes                                                                                                      |
|---------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD DLQ drain runbook; established WAL-driven replay approach, batching rules, and governance ties.|

---

<div align="center">

🧹 NODD DLQ Drain Runbook · KFM v11.2.3  

WAL-Driven · Deterministic · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Runbooks](README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[📊 Telemetry Alerts](../../telemetry/alerts/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
