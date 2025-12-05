---
title: "⏱️ KFM v11.2.3 — NODD Delayed Queue Runbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Incident runbook for handling elevated SQS queue age/depth and delayed ingestion in the NOAA NODD SNS → SQS pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/delayed-queue-runbook.md"

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
intent: "nodd-sns-sqs-delayed-queue-runbook"
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

# ⏱️ NODD Delayed Queue Runbook  

`docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/delayed-queue-runbook.md`

Incident runbook for **handling elevated SQS queue age and depth** in the NOAA NODD SNS → SQS ingestion pipeline.

Use this when:

- Queue-age or queue-depth SLO alerts are firing (`NODD-Q-AGE-CRIT`, `NODD-Q-DEPTH-CRIT`, `NODD-Q-DEPTH-WARN`).  
- Telemetry shows **growing backlog** and **delayed ingestion** for NODD datasets.  

This runbook coordinates:

- Immediate mitigation actions  
- WAL-aware replay safety  
- Coordination with capacity tuning and DLQ handling  

⸻

## 1. Purpose & Severity

### 1.1 Purpose

This runbook defines a **step-by-step response** when the NODD ingestion queue is delayed:

- Queue age approaching or exceeding SLO (P90 > 90 seconds).  
- Queue depth increasing faster than workers can drain it.  

Goals:

- Restore queue-age and depth within SLO.  
- Avoid data loss, duplicate processing, or WAL inconsistencies.  
- Minimize impact on downstream users and dashboards.

### 1.2 Typical Triggers

- Alerts:
  - `NODD-Q-AGE-CRIT` (queue-age SLO breach).  
  - `NODD-Q-DEPTH-CRIT` or `NODD-Q-DEPTH-WARN`.  
- Dashboard symptoms:
  - Queue depth steadily rising.  
  - Queue age P90 climbing towards several minutes.  
  - Ingest latency increasing.

### 1.3 Severity Levels

- **P1**: Critical queue-age breach with risk of data staleness impacting real-time products.  
- **P2**: Sustained warning-level queue depth/age without immediate correctness issues.  
- **P3**: Pre-emptive tuning in response to anticipated load spikes (may hand off to capacity tuning).

For P1 incidents, this runbook is used **with**:

- `capacity-tuning-runbook.md`  
- `incident-replay-runbook.md` (if backlog leads to failures or extensive replays)

⸻

## 2. Preconditions & Safety Checks

Before making changes:

1. **Confirm environment**

   - Identify `env` (`dev`, `stage`, `prod`).  
   - For non-P1 cases:
     - Prefer to test adjustments in `dev`/`stage` first.  

2. **Check WAL health**

   - Confirm WAL metrics are normal:
     - No unusual spikes in `wal_records_total{status="failed"}` or `"quarantined"`.  
     - WAL backend latency and error rates acceptable.  
   - If WAL is degraded, **escalate as P1** and involve infra; do not aggressively increase throughput.

3. **Check DLQ status**

   - Review DLQ metrics:
     - DLQ depth and rate (`NODD-DLQ-RATE-CRIT` alert state).  
   - If DLQ is rapidly filling:
     - Root cause may be data/validation-related; see `dlq-drain-runbook.md` and `validation-error-investigation-runbook.md`.

4. **Check validation / governance errors**

   - Look at `validation_errors_total{error_type}`:
     - If errors are spiking:
       - Capacity alone will not fix the issue; underlying schema/gov problems must be addressed first.

5. **Check upstream status**

   - Confirm NODD and cloud storage providers are healthy; if upstream is degraded:
     - Queue build-up may be transient or partially outside KFM control.

6. **Notify stakeholders**

   - For `stage`/`prod`:
     - Announce incident status and intent to act in `kfm-nodd-sre` (and incident channel if P1).  
     - Tag relevant atmospheric system owners.

⸻

## 3. Detection & Triage

Use telemetry dashboards (`nodd-ingestion-dashboard.md`) to identify the **dominant cause** of delay.

1. **Queue age vs queue depth**

   - If queue depth is high but age is stable:
     - System may be at capacity but not yet violating SLO.  
   - If both depth and age are rising:
     - System is under-capacity or blocked.

2. **Ingest latency**

   - Check P50/P90/P99 ingest latency by dataset.  
   - If latency is high:
     - Workers may be slow per-message (CPU/I/O bound, heavy operators).  

3. **Per-dataset hotspots**

   - Identify which datasets contribute most to depth and age:
     - Some products (e.g., large HRRR or NEXRAD payloads) may dominate.  
   - This may call for dataset-specific kill-switch or backpressure.

4. **Failures and DLQ**

   - If a large fraction of messages are failing:
     - Backlog may be caused by repeated retries, DLQ cycling, or governance failures.  
   - Address root cause or temporarily pause problematic datasets.

5. **Replay activity**

   - Check `replays_total` for the period:
     - Heavy replay activity may compete with live ingestion.  
   - Consider temporarily pausing non-critical replays.

⸻

## 4. Stabilize (Immediate Actions)

If the queue is clearly delayed and SLOs are at risk:

1. **Pause non-critical replays**

   - Temporarily suspend:
     - Backfill jobs.  
     - Large DLQ drains (unless they are the cause of the incident).  
   - Ensure replay tooling respects WAL and sets `replay_reason` appropriately when paused/resumed.

2. **Consider dataset-level kill-switches (if configured)**

   - For noisy or non-critical datasets:
     - Enable kill-switch to temporarily stop new ingestion for those datasets.  
   - Document any kill-switch usage in the incident record.

3. **Confirm autoscaling policies**

   - Ensure autoscaling is allowed to scale **up** within safe limits:
     - No overly restrictive max replica count.  
     - No misconfigured scaling metric.

4. **Protect downstream systems**

   - If downstream consumers (e.g., STAC consumers, analytics) are at risk:
     - Coordinate with their owners to rate-limit or pause heavy queries during recovery.

⸻

## 5. Diagnose (Deeper Queue Analysis)

With the system stabilized, refine diagnosis:

1. **Break down queue depth by dataset**

   - Use labels or tags to determine which datasets are dominant.  
   - If 1–2 datasets are responsible:
     - Focus remediation there (per-dataset capacity, kill-switch, or code optimization).

2. **Profile operator latencies**

   - Look at per-operator spans:
     - `message-parse`  
     - `integrity-check`  
     - `metadata-extract`  
     - `stac-register`  
     - `provenance-emit`  
   - Identify whether latency is dominated by:
     - Network I/O (storage reads).  
     - CPU-bound transforms.  
     - Downstream (STAC / provenance) work.

3. **Check visibility timeout vs processing time**

   - If processing time often exceeds visibility timeout:
     - SQS may be redelivering messages, inflating queue depth and WAL attempts.  

4. **Review recent changes**

   - Look for:
     - New code deploys.  
     - Schema updates.  
     - Upstream format changes.  
     - Capacity tweaks.  
   - These may explain sudden backlog onset.

5. **Check WAL for patterns**

   - Query WAL for:
     - High counts of `status="failed"` with repeated `last_error_code`.  
     - Large sets of `status="pending"` with old `created_at`.  
   - This helps distinguish between **slow but successful** vs **stuck or failing** ingestion.

⸻

## 6. Remediate — Clearing the Delay

Choose remediation actions based on diagnosis. Use **small, measured changes** and log each step.

### 6.1 Adjust Capacity (Refer to Capacity Runbook)

- If backlog is due to insufficient capacity and errors are low:

  - Follow `capacity-tuning-runbook.md` to:
    - Increase worker counts.  
    - Adjust concurrency/batch sizes.  
    - Tune SQS visibility timeout.  

- Changes MUST:
  - Respect WAL semantics.  
  - Be applied in increments with telemetry verification between steps.

### 6.2 Throttle or Pause Specific Datasets

- If one dataset is causing disproportionate load:

  - For **non-critical** datasets:
    - Enable a per-dataset kill-switch to temporarily stop new messages from being processed.  

  - For **critical** but heavy datasets:
    - Consider partial throttling or time-window-based ingestion:
      - Focus first on most recent data.  
      - Backfill older data later via controlled replays.

- Ensure:
  - WAL records for paused datasets remain consistent (typically `pending`).  
  - Replay planning for backlog is documented for after the incident.

### 6.3 Prioritize Newer Messages (When Applicable)

- If older backlog is less critical than fresh data:

  - Configure workers (if supported) to:
    - Prefer newer messages or partitions (e.g., using multiple queues or prioritization logic).  

- After stabilizing current data:
  - Backfill older WAL records via replay, governed by `incident-replay-runbook.md`.

### 6.4 Manage DLQ & Failed Messages

- If many messages are failing and landing in DLQ:

  - Do **not** just increase capacity:
    - This will amplify the failure rate.  

  - Instead:
    - Investigate errors via `validation-error-investigation-runbook.md`.  
    - Use `dlq-drain-runbook.md` to carefully drain and replay once problems are fixed.

### 6.5 Temporary Feature Degradation (Only if Approved)

- In severe P1 incidents and only with governance approval:

  - Temporarily:
    - Disable non-essential enrichment steps (e.g., some heavy metadata transforms) if they are optional.  
    - Reduce volume of energy/cost telemetry if it significantly impacts latency.  

- Any such change MUST:
  - Be documented.  
  - Include a plan to restore full functionality after the incident.

⸻

## 7. Verify — Returning to Normal

After applying remediation:

1. **Confirm queue metrics**

   - Primary queue:
     - Depth stabilized or decreasing.  
     - P90 queue age < 90 seconds.  
   - No new `NODD-Q-AGE-CRIT` or `NODD-Q-DEPTH-CRIT` alerts.

2. **Confirm ingest latency**

   - P90 `ingest_latency_seconds` within target ranges for priority datasets.  

3. **Check DLQ and failures**

   - DLQ rate at or below SLO.  
   - No new spikes in validation/gov errors.

4. **Check WAL**

   - No unexpected growth in `status="failed"` or `"quarantined"`.  
   - WAL replays (if any) are consistent and deterministic (no `replay_mismatch_total` increases).

5. **Confirm that any temporary kill-switches or degradations are either:**

   - Turned off with system stable, or  
   - Explicitly documented as **temporary** with a follow-up plan.

⸻

## 8. Postmortem & Governance

For any P1/P2 delayed-queue event in `prod`:

1. **Create or update incident record**

   - Include:
     - Timeline of alerts and queue metrics.  
     - Actions taken (capacity changes, kill-switch usage, replays).  
     - Before/after charts for queue age, depth, and ingest latency.

2. **Root cause analysis**

   - Determine whether delay was caused by:
     - Capacity misconfiguration.  
     - Code/infra regression.  
     - Upstream provider behavior.  
     - Unexpected volume spikes.

3. **Update dependencies**

   - Consider:
     - Adjusting alert thresholds (if too noisy or too lax).  
     - Refining dashboards to better highlight early-warning signals.  
     - Optimizing particularly slow operators.

4. **Runbook & Documentation updates**

   - If this incident exposed gaps:
     - Update this runbook and related ones (`capacity-tuning`, `dlq-drain`, `incident-replay`).  
     - Ensure new standard practices are captured in docs and configs.

5. **Governance review**

   - Provenance & Reliability Council SHOULD review:
     - Whether WAL, replay, and telemetry behavior were correct under stress.  
     - Whether FAIR/CARE and sovereignty obligations were respected during incident handling.

⸻

## 9. Version History

| Version  | Date       | Notes                                                                                                      |
|---------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD delayed queue runbook; aligned with WAL, alerts, dashboards, and capacity tuning procedures. |

---

<div align="center">

⏱️ NODD Delayed Queue Runbook · KFM v11.2.3  

SLO-Driven · WAL-Safe · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Runbooks](README.md) ·  
[📈 Capacity Tuning Runbook](capacity-tuning-runbook.md) ·  
[📊 Telemetry Dashboards](../../telemetry/dashboards/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
