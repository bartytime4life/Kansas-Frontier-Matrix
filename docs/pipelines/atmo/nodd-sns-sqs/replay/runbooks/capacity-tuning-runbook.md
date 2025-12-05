---
title: "📈 KFM v11.2.3 — NODD Capacity Tuning Runbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Operational runbook for safely tuning capacity, worker counts, and SQS parameters for the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/capacity-tuning-runbook.md"

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
intent: "nodd-sns-sqs-capacity-tuning-runbook"
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

# 📈 NODD Capacity Tuning Runbook  

`docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/capacity-tuning-runbook.md`

Operational runbook for **safely adjusting capacity** of the NOAA NODD SNS → SQS ingestion pipeline:

- Worker counts and concurrency  
- Batch sizes and throughput  
- SQS visibility timeouts and redrive behavior  

This runbook MUST be used when tuning capacity in response to:

- Queue depth or queue age alerts  
- Persistent ingest latency issues  
- Planned throughput increases (new datasets, higher frequency)  

It is designed to keep:

- WAL semantics intact  
- SLOs observable  
- Cost and energy usage governed and explainable  

⸻

## 1. Purpose & Severity

### 1.1 Purpose

Use this runbook to:

- Adjust **worker capacity and concurrency** for NODD ingestion.  
- Tune **SQS parameters** (visibility timeout, max inflight messages) safely.  
- Respond to **sustained load changes** without violating SLOs or reliability contracts.  

This runbook does **not** handle:

- Immediate queue-age incident mitigation (see `delayed-queue-runbook.md` for acute incidents).  
- DLQ clear / replay operations (see `dlq-drain-runbook.md`).  

### 1.2 Typical Triggers

- Alert policies such as:
  - `NODD-Q-DEPTH-WARN` or `NODD-Q-DEPTH-CRIT` (sustained high queue depth).  
  - `NODD-LAT-TREND-WARN` (latency degradation trend).  
- Observed sustained increase/decrease in:
  - `nodd_sns.ingest_latency_seconds` P90.  
  - `nodd_sns.queue_depth` and `nodd_sns.queue_age_seconds`.  
  - Per-dataset ingest volume.

### 1.3 Severity Levels

- P3: Planned capacity change (e.g., upcoming dataset expansion).  
- P2: Corrective tuning for SLO drift without active critical alerts.  
- P1: Only if requested by on-call during incident response where capacity change is part of remediation.

⸻

## 2. Preconditions & Safety Checks

Before making any changes:

1. Confirm environment  
   - Identify `env` (dev, stage, prod).  
   - All risky changes MUST be tested in `dev` and `stage` first unless explicitly overridden during a P1 with Council approval.

2. Verify WAL health  
   - Check WAL dashboards or metrics:
     - `nodd_sns.wal_records_total{status}` (no unexpected spikes in failed/quarantined).  
     - WAL backend error metrics (from infra dashboards).  
   - If WAL is degraded, **do not** increase capacity until WAL reliability is restored.

3. Check telemetry and dashboards  
   - Open NODD ingestion dashboard:
     - Ingest latency panels.  
     - Queue depth and queue age panels.  
     - DLQ and replay panels.  
   - Confirm that any observed issue is **capacity-related** and not driven by:
     - Upstream outages.  
     - Schema/governance failures (check validation error panels).

4. Confirm no kill-switch is active for target datasets  
   - If a kill-switch flag is enabled (dataset paused), capacity changes will not have the intended effect.

5. Notify stakeholders  
   - For `stage`/`prod` changes, announce planned tuning in:
     - `kfm-nodd-sre` channel.  
     - Relevant ops/infra channel if worker autoscaling is managed centrally.

⸻

## 3. Detection & Triage

Use this section to decide **what kind of tuning** is appropriate.

### 3.1 Symptoms Suggesting Under-Capacity

- Queue depth steadily increasing even while ingest latency grows.  
- Queue age P90 approaching or exceeding 90 seconds SLO, with:
  - Workers at or near maximum CPU or network usage.  
- Ingest latency high but DLQ rate and validation errors remain low.

### 3.2 Symptoms Suggesting Over-Capacity or Mis-Tuning

- Frequent SQS visibility timeouts leading to duplicate processing attempts.  
- Elevated WAL `attempts` counts without clear upstream issues.  
- Resource usage (CPU, memory, network) significantly higher than needed for current throughput.  
- Persistent downward spikes in ingest latency accompanied by high cost/energy metrics.

### 3.3 Symptoms Suggesting Non-Capacity Issues

If any of the following hold, address them **before** capacity tuning:

- Spikes in `validation_errors_total`.  
- High `replay_mismatch_total`.  
- Frequent WAL backend errors.  
- Upstream provider issues (NODD, cloud storage) confirmed by monitoring.

In these cases, consult:

- `validation-error-investigation-runbook.md`  
- `incident-replay-runbook.md`  
- Infrastructure runbooks.

⸻

## 4. Stabilize (If Under Active Stress)

If the system is currently under heavy stress but **not** in P1 incident mode:

1. Temporarily pause non-critical replays  
   - Reduce or pause replay jobs that are not P1-critical:
     - Backfills.  
     - Large DLQ drains (coordinate with `dlq-drain-runbook.md`).  

2. Confirm autoscaling behavior  
   - If workers are autoscaled:
     - Check that autoscaling policies are active and not capped incorrectly.  
   - If manual:
     - Plan incremental changes (see section 6) rather than large jumps.

3. Set clear objective  
   - Example:
     - Reduce queue depth growth to ≤ 0 messages/minute.  
     - Bring P90 ingest latency below 300 seconds with at least 20% headroom.

⸻

## 5. Diagnose (Capacity-Specific Diagnostics)

Use these checks to determine **which knobs** to turn.

1. Worker utilization  
   - Check worker CPU, memory, and I/O utilization.  
   - If consistently > 75–80% across fleet:
     - Likely need more workers or smaller per-worker batch sizes.  

2. Per-message processing time  
   - From telemetry:
     - Look at spans for `message-parse`, `integrity-check`, `metadata-extract`, `stac-register`, `provenance-emit`.  
   - Identify which operator dominates latency:
     - This may influence whether to scale horizontally, optimize code, or adjust batch size.

3. SQS visibility timeout vs processing time  
   - Compare average/percentile processing time per message with configured visibility timeout.  
   - If processing frequently exceeds timeout:
     - Expect duplicate work and elevated WAL attempts.

4. DLQ patterns  
   - If DLQ levels are high:
     - Capacity tuning alone will not fix the pipeline; there may be systematic data issues.  
   - Resolve underlying causes before increasing throughput to avoid amplifying failures.

5. Cost and energy  
   - Review energy and cost panels for NODD ingestion:
     - Large capacity increases may be unjustified if load is episodic.  
   - Plan changes with sustainability and cost in mind.

⸻

## 6. Remediate — Capacity Tuning Actions

Perform changes in **small, reversible increments**. Document all changes in an ops log or ticket.

### 6.1 Adjust Worker Count

1. Identify current worker count and scaling mode  
   - Autoscaled or fixed.  
   - Per `env` and per dataset (if applicable).

2. Change in small steps  
   - Recommended increment: 20–30% changes per iteration, not 2–3× jumps.  
   - After each change:
     - Observe metrics for at least one or two full queue residency periods (e.g., 15–30 minutes).

3. Watch for side-effects  
   - Monitor:
     - Queue depth and queue age.  
     - Ingest latency.  
     - DLQ rates.  
     - WAL attempts and replay counts.  
   - If DLQ rate spikes after increasing workers:
     - Capacity may be amplifying a latent validation or governance issue.

### 6.2 Adjust Per-Worker Concurrency / Batch Size

1. Confirm concurrency model  
   - Per-worker batch size (messages fetched at once).  
   - Internal concurrency (threads/async tasks).

2. For CPU- or I/O-bound workers:

   - If CPU is low but latency high:
     - Slightly increase concurrency (e.g., additional async operations) while monitoring memory and I/O.  

   - If CPU is high:
     - Prefer adding more workers rather than dramatically increasing concurrency.

3. Keep WAL and SQS consistent  
   - Ensure concurrency changes do not break assumptions about one WAL record per message and correct locking semantics.

### 6.3 Tune SQS Visibility Timeout

1. Measure current processing time distribution  
   - Use telemetry to estimate max and P99 per-message processing time.

2. Set visibility timeout with margin  
   - Target:
     - Visibility timeout ≥ P99 processing time + safety buffer (e.g., 2× P99 or P99 + 30–60 seconds).  

3. Avoid excessive timeouts  
   - Very large timeouts can delay failure detection and DLQ routing.  
   - Balance between duplicate work and responsiveness to failures.

4. After changes  
   - Monitor:
     - Visibility timeout-related errors.  
     - Changes in attempts per WAL record.  

### 6.4 Tune Redrive and Backoff

If supported in your infra:

- Confirm exponential backoff for retries to avoid storm behavior.  
- Adjust redrive policies so that persistent failures:
  - Reach DLQ in a bounded number of attempts.  
  - Do not cycle infinitely.

Coordinate with:

- `dlq-drain-runbook.md` and alert policies (`NODD-DLQ-RATE-CRIT`).

⸻

## 7. Verify (Post-Tuning)

After each change, verify that:

1. Queue metrics are stable  
   - `nodd_sns.queue_depth` no longer trending upward without bound.  
   - P90 `nodd_sns.queue_age_seconds` < 90 seconds for primary queue.

2. Ingest latency within SLO  
   - P90 `nodd_sns.ingest_latency_seconds` < 300 seconds for priority datasets.  
   - No new `NODD-LAT-P90-CRIT` or `NODD-LAT-TREND-WARN` alerts firing.

3. Failures and DLQ do not spike  
   - DLQ rate is at or below SLO (< 0.05% of messages).  
   - Validation and governance errors remain stable.

4. WAL behavior is healthy  
   - WAL `attempts` not increasing unexpectedly.  
   - No surge in `replay_mismatch_total`.

5. Cost and energy acceptable  
   - Review energy/cost panels to ensure changes are justified and within expectations.

If any verification step fails, either:

- Roll back the last capacity change, or  
- Apply further tuned adjustments, respecting the same incremental approach.

⸻

## 8. Postmortem & Governance

For any significant capacity-tuning event (beyond routine minor adjustments), especially in `prod`:

1. Create or update an incident/change record  
   - Include:
     - Reason for tuning.  
     - Specific parameters changed and by how much.  
     - Time windows and metrics before/after.

2. Capture learnings  
   - Are new alerts or dashboard panels needed?  
   - Did tuning reveal weaknesses in WAL, telemetry, or governance gates?

3. Update documentation  
   - If tuning led to a new standard configuration:
     - Reflect this in:
       - Pipeline config docs.  
       - Telemetry and alerts documentation if thresholds changed.  
       - This runbook, if procedures changed.

4. Governance review  
   - Provenance & Reliability Council SHOULD review major capacity shifts at the next review cycle.  
   - Confirm alignment with FAIR/CARE and sustainability targets.

⸻

## 9. Version History

| Version  | Date       | Notes                                                                                                       |
|---------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD capacity tuning runbook; aligned with WAL, alerts, and NODD ingestion dashboard specifications.|

---

<div align="center">

📈 NODD Capacity Tuning Runbook · KFM v11.2.3  

Deterministic · SLO-Aware · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Runbooks](README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[📊 Telemetry Dashboards](../../telemetry/dashboards/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
