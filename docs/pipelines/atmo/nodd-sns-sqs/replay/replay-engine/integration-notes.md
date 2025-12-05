---
title: "🔗 KFM v11.2.3 — NODD Replay Engine Integration Notes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Integration guidance for wiring the NODD WAL-driven replay engine into schedulers, CI, runbooks, telemetry, and governance for the NOAA NODD SNS → SQS pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/integration-notes.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x replay-engine-integration compatible"
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

doc_kind: "Replay Engine Integration Notes"
intent: "nodd-sns-sqs-replay-engine-integration-notes"
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
sunset_policy: "Superseded by next major NODD replay engine integration standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🔗 NODD Replay Engine Integration Notes  

`docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/integration-notes.md`

This document explains **how the NODD Replay Engine integrates** with:

- Schedulers (cron / EventBridge / GitHub Actions)  
- Runbooks and operational workflows  
- WAL storage and state machine  
- Telemetry, dashboards, and alerts  
- Governance (FAIR+CARE, sovereignty, LangGraph gates)  
- Lineage and the KFM knowledge graph  

It complements:

- Replay Engine spec: `README.md`  
- CLI spec: `cli-spec.md`  
- Selection model: `selection-spec.md`  
- Safety guards: `safety-guards.md`  
- Runbooks index: `../runbooks/README.md`  

and provides **wiring guidance** for production-grade deployments.

⸻

## 🧭 1. Integration Scope & Principles

The replay engine MUST be integrated following these principles:

- **WAL-First**  
  All replay decisions flow from WAL selection; no direct SQS “magic” without WAL correlation.

- **Runbook-Driven**  
  DLQ drains, delayed queues, incident replays, and validation-error remediation use **runbooks** that call the replay engine, not bespoke scripts.

- **Declarative Selection**  
  Selection specs are **declarative artifacts** that can be stored, reviewed, and re-used across environments.

- **Guardrail-Enforced**  
  All integrations must respect safety guards (batch limits, rate limits, attempts, kill-switches).

- **Governance-Aware**  
  Integrations MUST respect sovereignty, CARE, and governance flags—even under incident pressure.

⸻

## 🧩 2. Integration Map (Conceptual)

The replay engine participates in the broader NODD ingestion ecosystem as follows:

- **Schedulers / Jobs**  
  - Trigger replay engine commands (`nodd-replay`) with **selection specs**.  

- **Runbooks**  
  - Provide human-readable procedures that map directly to CLI invocations.  

- **WAL**  
  - Acts as the **single source of truth** for what can be replayed and why.  

- **SQS**  
  - Receives reconstructed messages when replays are executed through the hot-path workers.  

- **Telemetry & Alerts**  
  - Surface replay activity, guardrail hits, and mismatches.  

- **Lineage & Graph**  
  - Capture replay provenance in OpenLineage and Neo4j.

All integrations MUST preserve this shape; deviations must be explicitly governed and documented.

⸻

## 🕰 3. Scheduler Integration (Cron / EventBridge / GitHub Actions)

### 3.1 Patterns

Schedulers SHOULD use the CLI as their primary integration point:

- **Nightly DLQ health checks**  
  - `nodd-replay select` + `dry-run` to estimate replay feasibility.  

- **Scheduled small-batch DLQ drains**  
  - `nodd-replay run` with:
    - `--mode failed-only`  
    - Constrained selection and guardrails.  

- **Planned backfill windows**  
  - `nodd-replay from-spec --dry-run` in `stage`, then `--run` in `prod` with governance approval.

### 3.2 GitHub Actions Example (Conceptual)

Jobs in `.github/workflows/` SHOULD:

- Use `nodd-replay dry-run` for **preview** on PRs (non-prod).  
- Use `nodd-replay from-spec --dry-run` in nightly pipelines to ensure specs remain valid.  
- Only use `nodd-replay run` in `prod` when triggered via change/incident workflows.

See replay engine `cli-spec.md` and runbooks for detailed examples.

⸻

## 📚 4. Runbook Integration

The replay engine is explicitly referenced in:

- `../runbooks/dlq-drain-runbook.md`  
- `../runbooks/incident-replay-runbook.md`  
- `../runbooks/delayed-queue-runbook.md`  
- `../runbooks/validation-error-investigation-runbook.md`  
- `../runbooks/capacity-tuning-runbook.md` (indirectly, via replay load awareness)

Each runbook MUST:

- Map **plain-language steps** to **concrete CLI invocations**.  
- Reference selection specs and modes (`failed-only`, `incident`, `backfill`).  
- Use **WAL status transitions** defined in `../wal/wal-state-machine.md`.

Runbooks MUST be updated when:

- CLI commands/flags change.  
- Selection spec shape changes.  
- New replay modes or guardrails are introduced.

⸻

## 🧱 5. WAL & Storage Integration

The replay engine depends on the WAL contract:

- Record Model: `../wal/wal-record-model.md`  
- State Machine: `../wal/wal-state-machine.md`  
- Storage Backends: `../wal/wal-storage-backends.md`

Integration rules:

- Replay selection MUST query WAL via its canonical storage backend(s); no parallel record formats.  
- State transitions MUST be persisted atomically with respect to `status`, `attempts`, `replay_reason`, and `version`.  
- Any WAL schema migration MUST keep the replay engine SDK / queries in sync.

If multiple WAL backends are used (e.g., DB + object archive):

- The replay engine MUST treat **one** as **authoritative for mutable state** (typically the relational backend).

⸻

## 📡 6. Telemetry, Dashboards & Alerts

The replay engine MUST integrate with telemetry defined in:

- `../../telemetry/README.md`  
- `../../telemetry/dashboards/nodd-ingestion-dashboard.md`  
- `../../telemetry/alerts/nodd-alert-policies.md`

### 6.1 Metrics Integration

Replay engine MUST emit metrics that:

- Distinguish replay activity from hot-path ingestion.  
- Tag replay traffic with:
  - `dataset`, `env`, `replay_reason`, `mode`.  

Ops dashboards SHOULD:

- Show replay batch counts and sizes.  
- Show impact on queue depth/age and WAL statuses.  
- Correlate replay runs with validation errors and DLQ rates.

### 6.2 Alerts

Alerts MAY:

- Fire when:
  - Replay errors spike (`replay_mismatch_total` rising).  
  - Replay throughput threatens SLOs (queue age/depth).

Runbooks MUST specify which replay alerts map back to which **mitigation procedures**.

⸻

## 🧬 7. Governance & LangGraph Integration

Replay operations MUST respect KFM governance:

- Root governance: `${governance_ref}`  
- FAIR/CARE: `${ethics_ref}`  
- Sovereignty policy: `${sovereignty_policy}`  

Integration expectations:

- LangGraph governance gates MUST treat replay operations identically to hot-path ingests:
  - Same provenance, sensitivity, and sovereignty checks.  
  - No “governance bypass” just because an operation is a replay.  

- Any governance-related errors (`governance_hard_fail`) surfaced in replay:
  - MUST follow `validation-error-investigation-runbook.md`.  
  - MAY lead to `quarantined` WAL status, not forced success.

If a replay requires **temporary policy adjustments**:

- Adjustments MUST be:
  - Documented, versioned, and reviewed.  
  - Time-bounded and reversible.  
  - Tested in non-prod where feasible.

⸻

## 🕸 8. Lineage & Knowledge Graph Integration

Replay engine activity MUST **enrich lineage**, not obscure it.

### 8.1 OpenLineage

Each replay batch SHOULD:

- Emit OpenLineage runs with:
  - `runId` correlated to `wal_id` sets or selection spec ID.  
  - `job.name` indicating replay mode (e.g., `nodd.replay.failed-only`).  
  - `parentRunId` or appropriate references to original runs when repair-and-replace is used.

### 8.2 Neo4j / KFM Graph

The KFM knowledge graph SHOULD:

- Represent replay activities as distinct `prov:Activity` instances.  
- Link WAL records and replay activities using:
  - Edges such as `(:WalRecord)-[:HAS_REPLAY_ACTIVITY]->(:Activity)` (exact labels per ontology).  

Downstream analyses (e.g., reliability or incident reviews) can then:

- Trace which graph elements originated from replays vs first ingestion.  
- Confirm that no replay contradicted existing provenance without record.

⸻

## 🧪 9. CI & Non-Prod Integration

CI and non-prod environments MUST use the same replay engine and CLI, but with:

- **Safe defaults**:
  - Small `--batch-size` and strict `--max-batches`.  
  - Non-prod WAL backends and queues.  

- **Contract tests**:
  - Selection specs in this directory or tests MUST be validated periodically.  
  - Runbook examples MUST be executable in non-prod (even if on synthetic WAL).

CI jobs SHOULD:

- Run `nodd-replay select` and `dry-run` against fixture WAL data.  
- Verify:
  - State machine compliance under replay.  
  - Idempotency of re-running the same selection.  
  - Guardrail enforcement and exit codes.

⸻

## ⛔ 10. Integration Anti‑Patterns (Forbidden)

The following patterns are **forbidden**:

- Direct SQS re-insertion of DLQ messages **without** updating WAL.  
- Custom scripts that:
  - Mutate `status` in WAL ignoring the state machine.  
  - Bypass `nodd-replay` and safety guards.  
- Replays that:
  - Ignore `max_attempts`.  
  - Ignore dataset kill-switches.  
  - Bypass governance gates, telemetry, or lineage emission.

If an emergency requires deviation (e.g., severe P1), the deviation MUST:

- Be explicitly documented.  
- Be treated as an incident requiring follow-up governance review and tooling updates.

⸻

## 📘 11. Version History

| Version  | Date       | Notes                                                                                                                   |
|---------:|------------|-------------------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD replay engine integration notes; defined scheduler, runbook, telemetry, governance, and lineage integration.|

---

<div align="center">

🔗 NODD Replay Engine Integration Notes · KFM v11.2.3  

WAL-First · Runbook-Driven · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Engine](README.md) ·  
[🧾 CLI Spec](cli-spec.md) ·  
[♻️ Replay Engine Overview](README.md) ·  
[🧰 Replay Runbooks](../runbooks/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
