---
title: "♻️ KFM v11.2.3 — NODD Incident Replay Runbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "High-severity incident runbook for WAL-safe, deterministic replays in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/incident-replay-runbook.md"

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
intent: "nodd-sns-sqs-incident-replay-runbook"
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

# ♻️ NODD Incident Replay Runbook  

`docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/incident-replay-runbook.md`

High-severity runbook for **WAL-safe, deterministic replays** in the NOAA NODD SNS → SQS ingestion pipeline.

Use this when an incident requires:

- Reprocessing **a specific time window** of NODD data  
- Repeating ingestion after a **bug fix** or **config correction**  
- Repairing outputs after a **bad deploy**, **upstream anomaly**, or **partial data loss**  

All actions MUST:

- Use the **WAL as the source of truth**  
- Respect the **WAL state machine** and **record model**  
- Avoid duplicate STAC/provenance writes or non-deterministic outcomes  

Referenced specs:

- WAL contract: `replay/wal/README.md`  
- WAL record model: `replay/wal/wal-record-model.md`  
- WAL state machine: `replay/wal/wal-state-machine.md`  

⸻

## 1. Purpose & Severity

### 1.1 Purpose

This runbook defines how to:

- Plan and execute **incident-driven replays**  
- Constrain scope by dataset, time window, and error type  
- Use WAL to drive replays rather than ad hoc SQS/SNS operations  
- Verify that outputs are correct and deterministic after replay  

It is used when:

- A bug or misconfiguration corrupted or skipped a subset of ingests  
- An upstream provider event caused bad data that now has a fix  
- A rollback/roll-forward requires **rebuilding** STAC/provenance for a window  

### 1.2 Typical Triggers

- Validated incident in `prod` such as:
  - Defective deployment affecting NODD ingestion  
  - Schema or governance rule error causing silent drops or repeated failures  
  - Upstream mis-publishing corrected retroactively  

- Telemetry evidence:
  - Spikes or gaps in ingest success metrics  
  - Unexpected patterns in WAL `status` or `attempts`  
  - Replay mismatches detected (`replay_mismatch_total` > 0)

### 1.3 Severity Levels

- P1: Incident with user-visible or product-level impact requiring immediate replay  
- P2: Serious but not immediately user-visible data quality issue requiring limited-scope replay  
- P3: Planned replay (e.g., correcting known issues for a historical window)  

For P1/P2, this runbook MUST be linked in the incident record.

⸻

## 2. Preconditions & Safety Checks

Before you initiate any incident replay:

1. Confirm environment  

   - Identify `env` (`dev`, `stage`, `prod`).  
   - For `prod`, ensure:
     - An incident ticket exists (or create one).  
     - The scope and goals of replay are documented.

2. Confirm fix readiness  

   - Verify the **root cause** is understood and resolved or mitigated:
     - Code patch deployed.  
     - Schema/gov rules updated.  
     - Upstream data corrected or quarantined.  
   - If the cause is unclear:
     - Do not replay; first escalate investigation.

3. Verify WAL health  

   - WAL backend must be:
     - Reachable and healthy  
     - Free from unusual error rates  
   - WAL metrics should NOT indicate:
     - Storage errors  
     - Massive version conflicts  

4. Verify telemetry and lineage working  

   - Confirm ingest telemetry is operative:
     - Ingest latency, queue metrics, WAL metrics  
   - Confirm lineage systems (OpenLineage / provenance pipeline) are online or their failure modes are understood.

5. Check live ingestion state  

   - Evaluate:
     - Primary queue depth and age  
     - DLQ depth and rate  
   - If system is already stressed:
     - Coordinate with `delayed-queue-runbook.md` and `capacity-tuning-runbook.md` before adding replay load.

6. Notify stakeholders  

   - Communicate replay intent in:
     - `kfm-nodd-sre`  
     - Incident channel (if P1/P2)  
   - Include:
     - Time window  
     - Dataset(s)  
     - Expected volume  
     - Risk assessment  

⸻

## 3. Detection & Triage

Determine **why** replay is needed and define a **precise scope**.

1. Identify affected datasets  

   - Use telemetry and WAL to determine which `dataset` values are impacted:
     - Examples: `goes-abi`, `nexrad-l2`, `hrrr`, `surface-obs`.

2. Define temporal scope  

   - Determine the time interval that needs replay:
     - Example:
       - From: deploy start time / upstream failure onset  
       - To: deploy rollback time / fix deployment time  
   - Use:
     - `event_time`  
     - `time_range_start` / `time_range_end`  
     - `created_at` in WAL  

3. Identify error patterns  

   - Inspect WAL fields:
     - `status` (`failed` vs `succeeded`)  
     - `last_error_code` / `last_error_message`  
   - Decide whether replay targets:
     - Failed ingests (e.g., schema mismatches now fixed)  
     - Succeeded ingests that must be **replaced** due to bad code (requires special care)  
     - Missing ingests (never attempted due to bug)

4. Classify replay type  

   - Replay failed-only:
     - Default and safest scenario (failed records only).  

   - Repair-and-replace:
     - Previously “succeeded” records known to be wrong; requires:
       - Careful deletion/overwrite logic in STAC and provenance  
       - Extra governance approval  

   - Fill missing:
     - Records that should exist but have no WAL entries or `pending/failed` states only.

5. Confirm that replay is the correct remediation  

   - For some incidents, **forward fixes** or new ETL runs may be preferred over replay.  
   - Confirm with system owners and Council if in doubt.

⸻

## 4. Stabilize (If Under Active Incident)

If the incident is ongoing or system is unstable:

1. Pause non-essential replays and backfills  

   - Stop any scheduled backfills or DLQ drains unrelated to this incident.  
   - Ensure replay tooling is not already running ad hoc replays for the same window.

2. Consider dataset kill-switches  

   - For affected datasets:
     - Temporarily pause new ingestion if it is generating more broken data.  
   - Document any kill-switch state changes in the incident record.

3. Freeze risky changes  

   - Pause non-critical deploys or configuration changes to avoid complicating replay.  

4. Confirm capacity state  

   - Ensure there is enough capacity headroom to process replays:
     - If not, coordinate with `capacity-tuning-runbook.md`.

⸻

## 5. Diagnose — WAL-Centric Incident Analysis

Use the WAL as the primary forensic tool.

1. WAL slice selection  

   - Query WAL by:
     - `dataset ∈ affected datasets`  
     - `event_time` or `time_range_*` within incident window  
     - `status` in `{failed, succeeded, pending}` depending on replay type  
   - Export this slice to a controlled location (if needed) for analysis.

2. Error and status distributions  

   - Group records by:
     - `status` (`failed`, `succeeded`, `quarantined`)  
     - `last_error_code`  

   - Identify:
     - Dominant error codes for failed records  
     - Whether “succeeded” items are actually incorrect due to logic error

3. Detect missing records  

   - For some incidents:
     - Source logs or upstream listings may show more objects than WAL records.  
   - Identify gaps where:
     - Upstream objects exist, but no WAL record exists.  
   - These may require **fresh ingest** rather than replay.

4. Understand replay risk  

   - For each candidate slice, assess:
     - Volume (number of records).  
     - Diversity of error codes.  
     - Impact if replayed incorrectly.

5. Document replay scope  

   - In the incident ticket, document:
     - Datasets  
     - Time range  
     - Status classes (failed-only vs also succeeded)  
     - Estimated WAL count  

⸻

## 6. Remediate — Replay Plan & Execution

All replays MUST be governed by the WAL state machine.

### 6.1 Choose Replay Mode

1. Failed-only replay  

   - Replay WAL records where:
     - `status = "failed"`  
     - `last_error_code` belongs to error classes now fixed  
     - `attempts < max_attempts`  

   - This is the default mode for most incidents.

2. Repair-and-replace replay  

   - Replay WAL records where:
     - `status = "succeeded"` but outputs are logically invalid based on incident analysis  
   - Requires:
     - Additional logic to safely update or replace STAC items and provenance records  
     - Governed migration approach (may be handled via a special migration pipeline)  

3. Fill missing replay  

   - For missing WAL records:
     - May require constructing new WAL entries and ingesting as new data.  
   - This is more like **backfill** than replay but may be managed under this runbook.

Any mode beyond failed-only MUST be explicitly approved by the Provenance & Reliability Council for `prod`.

### 6.2 Mark WAL Records for Replay

For the selected scope:

1. Filter WAL records  

   - For failed-only:
     - `status = "failed"`  
     - `last_error_code ∈ {fixed error codes}`  
     - Within the temporal window  
     - Under retry limit  

2. Apply state transitions  

   - For each selected record:
     - Set `status = "pending"` (from `failed`, per `wal-state-machine.md`).  
     - Set or update:
       - `replay_reason = "incident"`  
       - `updated_at = now()`  
     - Ensure `version` is incremented as per optimistic concurrency rules.

3. Prepare re-enqueue mechanism  

   - Implementation-specific:
     - Reconstruct SQS messages from WAL fields, or  
     - Use internal replay job that reads from WAL and processes like normal ingestion.

All transitions MUST be logged with:

- Incident ID  
- Operator identity (or automated job identity)  
- Dataset and size of replay batch  

### 6.3 Execute Replay in Batches

1. Start with a pilot batch  

   - Small subset (for example, a few hundred records) from the replay scope.  
   - Monitor behavior closely:
     - Success/failure pattern  
     - DLQ rate  
     - `replay_mismatch_total` metrics  

2. Observe and validate  

   - Confirm that:
     - Failures have decreased for the replayed error class.  
     - WAL statuses for these records move to `succeeded` or appropriate terminal state.  
     - STAC items and provenance outputs look correct on spot-check.

3. Scale up carefully  

   - If pilot batch is successful:
     - Increase batch size in controlled increments.  
   - Avoid replays so large they overload workers or saturate queues.

4. Stop on anomalies  

   - If:
     - New or unexpected `last_error_code` appears, or  
     - `replay_mismatch_total` increases, or  
     - DLQ rate spikes again,  
   - Immediately pause replays for that error class or dataset and return to diagnosis.

⸻

## 7. Verify — Post-Replay Validation

When replay batches are complete or paused:

1. WAL verification  

   - For replayed scope:
     - Majority (or target subset) of WAL records should now have:
       - `status = "succeeded"` or properly `quarantined`.  
   - Ensure:
     - No uncontrolled growth in `attempts`.  
     - No abnormal pattern of repeated failures.

2. Telemetry verification  

   - Confirm:
     - Ingest latency metrics have not regressed.  
     - DLQ depth and rate are under control.  
     - Queue depth/age are within SLOs.

3. Output verification  

   - Spot-check:
     - STAC Items (metadata, geometry, temporal coverage).  
     - Provenance entries (linkage, activities, entities).  
   - Confirm:
     - No duplicate items or broken lineage for the replayed time window.

4. Replay determinism verification  

   - Check `nodd_sns.replay_mismatch_total`:
     - Should remain zero or stable.  
   - If mismatches exist:
     - Document them and escalate for deeper analysis.

5. Downstream impact verification  

   - Coordinate with data consumers:
     - Ensure their systems see corrected/expected data.  
   - Check any user-facing dashboards or products for consistency.

⸻

## 8. Postmortem & Governance

For any P1/P2 incident replay, or large-scale P3 replay:

1. Complete incident record  

   - Include:
     - Replay scope and rationale.  
     - Root cause summary (code/infra/upstream).  
     - Timeline of:
       - Detection  
       - Fix deployment  
       - Replay execution  

2. Document replay outcomes  

   - Summarize:
     - Number of WAL records replayed  
     - Error class breakdown before/after  
     - Any remaining quarantined records  

3. Identify process or tooling gaps  

   - Could improved:
     - Alerting  
     - Dashboards  
     - WAL analytics  
     - Pre-deploy checks  
   - Have prevented the incident or reduced the replay scope?

4. Update documentation  

   - If new standard replay patterns emerged:
     - Update this runbook and related documents:
       - `dlq-drain-runbook.md`  
       - `delayed-queue-runbook.md`  
       - `capacity-tuning-runbook.md`  
       - Relevant pipeline/operator docs  

5. Governance review  

   - Provenance & Reliability Council SHOULD:
     - Confirm that replay preserved determinism and lineage integrity.  
     - Check that CARE/FAIR and sovereignty rules were followed (no unsafe debugging logs, no unauthorized data exposure).  
     - Approve or request changes to replay policies as needed.

⸻

## 9. Version History

| Version  | Date       | Notes                                                                                                      |
|---------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD incident replay runbook; defined WAL-centric replay scope, batching strategy, and governance. |

---

<div align="center">

♻️ NODD Incident Replay Runbook · KFM v11.2.3  

WAL-First · Deterministic · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Runbooks](README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[📊 Telemetry Alerts](../../telemetry/alerts/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
