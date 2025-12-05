---
title: "🧰 KFM v11.2.3 — NODD Replay Runbooks Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed incident and replay runbook index for the NOAA NODD SNS → SQS ingestion pipeline, covering DLQ drains, delayed queues, incident replays, capacity tuning, and validation error investigations."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/README.md"

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

doc_kind: "Replay Runbook Index"
intent: "nodd-sns-sqs-replay-runbooks-index"
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
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD replay runbook standard"

header_profile: "standard"
footer_profile: "standard"
---

# 🧰 NODD Replay Runbooks Index  

`docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/README.md`

Governed **incident and replay runbooks** for the NOAA NODD SNS → SQS ingestion pipeline.

These runbooks define **how humans and tools interact with**:

- The NODD **Write-Ahead Log (WAL)**  
- **DLQs** and replay queues  
- **Incident replays** and backfills  
- **Capacity / latency remediation**  
- **Validation / governance error investigations**

Every replay or manual intervention touching NODD ingestion MUST follow one of these runbooks or a future governed extension.

⸻

## 🗂 1. Directory Layout (Runbooks)

    docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/
    │
    ├── 📄 README.md                          # This file — runbook index & contracts
    │
    ├── 📄 dlq-drain-runbook.md               # Draining and safely replaying DLQ messages via WAL
    ├── 📄 incident-replay-runbook.md         # High-severity incident replays (P1/P2)
    ├── 📄 delayed-queue-runbook.md           # Response playbook for elevated queue age / depth
    ├── 📄 capacity-tuning-runbook.md         # Scaling workers, tuning visibility, adjusting capacity
    └── 📄 validation-error-investigation-runbook.md
                                              # Investigating schema/gov validation error bursts

Individual runbooks are referenced by:

- **Telemetry dashboards** (`telemetry/dashboards/nodd-ingestion-dashboard.md`)  
- **Alerts & policies** (`telemetry/alerts/README.md`, `telemetry/alerts/nodd-alert-policies.md`)  
- **WAL documentation** (`replay/wal/*.md`)

⸻

## 🧭 2. Purpose & Scope

This index document:

- Defines the **minimum runbook set** required for NODD SNS → SQS.  
- Establishes **shared structure** and expectations for all runbooks.  
- Ties runbooks to **WAL semantics**, **alerts**, and **SLOs**.  
- Serves as the entry-point for SREs, pipeline engineers, and governance reviewers.

Runbooks are designed to be:

- **Deterministic** — every step is idempotent when applied twice.  
- **Traceable** — every manual action has a WAL and telemetry footprint.  
- **Governed** — CARE/FAIR and sovereignty rules are respected even under incident pressure.

⸻

## 🧱 3. Standard Runbook Structure (All Files)

Each runbook under this directory MUST follow a common structure:

1. **Purpose & Severity**  
   - What problem the runbook addresses.  
   - Typical alert IDs / policies that link to it.  
   - Applicable severity levels (P1/P2/P3).

2. **Preconditions & Safety Checks**  
   - Confirm environment (`env`) and impact scope.  
   - Verify **no kill-switch** is enabled for the dataset (if applicable).  
   - Confirm WAL backend health (quick checks).

3. **Detection & Triage**  
   - How to interpret relevant **alerts**, **dashboard panels**, and **WAL stats**.  
   - How to rule out false positives.

4. **Stabilize**  
   - Immediate actions to stop things getting worse:
     - Rate limiting.  
     - Temporarily pausing new replays.  
     - Enabling kill-switch when justified.

5. **Diagnose**  
   - Queries against:
     - WAL (e.g., by `status`, `last_error_code`).  
     - Telemetry (DLQ, latency, queue depth).  
     - Lineage (OpenLineage / provenance) where relevant.

6. **Remediate**  
   - Step-by-step actions:
     - How to replay (`failed → pending`) specific WAL slices.  
     - How to drain DLQ safely.  
     - How to apply schema or config fixes.

7. **Verify**  
   - How to confirm:
     - Alerts have cleared.  
     - SLOs are back in bounds.  
     - WAL statuses reflect successful completion.

8. **Postmortem & Governance**  
   - Required incident records, JIRAs / tickets, or postmortem templates.  
   - Updates needed in:
     - Schemas.  
     - Alert policies.  
     - Runbooks themselves.

Each runbook MUST clearly separate **automated** vs **manual** steps, and MUST avoid ambiguous language (“maybe”, “if you want”) in critical paths.

⸻

## 🔁 4. Runbook Roles & Ownership

Role expectations:

- **On-Call SRE / Pipeline Operator**  
  - Executes runbooks during incidents.  
  - Records all manual replay decisions.  

- **Atmospheric Systems Engineer**  
  - Maintains dataset-specific steps (e.g., HRRR vs NEXRAD differences).  
  - Ensures WAL semantics remain valid when pipelines change.

- **Provenance & Reliability Council**  
  - Reviews changes to runbooks each review_cycle.  
  - Ensures runbooks match WAL, telemetry, and alert specs.

Ownership:

- Each runbook file MUST list primary and secondary owning teams in its own header (not in this index).

⸻

## 🧬 5. Integration with WAL & Telemetry

All replay runbooks MUST:

- Treat the WAL as the **source of truth** for replay eligibility:
  - Operate on WAL records (`status`, `attempts`, `last_error_code`), not raw SQS messages alone.  

- Use WAL transitions that respect:
  - `wal-state-machine.md` (no illegal `status` transitions).  
  - `wal-record-model.md` (fields and invariants).

- Reference telemetry and alerts defined in:
  - `telemetry/README.md`  
  - `telemetry/dashboards/`  
  - `telemetry/alerts/`  

Examples:

- DLQ drain:
  - Uses WAL to identify `failed` records linked to DLQ messages.  
  - Transitions `failed → pending` with `replay_reason = "dlq-drain"`.  

- Incident replay:
  - Uses WAL to select records within a specific time window, dataset, and `last_error_code`.  
  - Ensures replay count and determinism metrics (`replay_mismatch_total`) are monitored.

⸻

## 📚 6. Summary of Required Runbooks

High-level expectations for the listed runbooks:

- `dlq-drain-runbook.md`  
  - Safe procedure for draining DLQ in batches.  
  - How to cap replay volumes and monitor DLQ-related alerts.

- `incident-replay-runbook.md`  
  - For major incidents (e.g., schema bugs, upstream outages).  
  - Covers how to select WAL slices, run replays, and verify outcomes.

- `delayed-queue-runbook.md`  
  - For queue age/depth SLO breaches.  
  - Emphasizes capacity scaling, worker health, and partial backpressure.

- `capacity-tuning-runbook.md`  
  - For tuning worker counts, batch sizes, SQS visibility timeouts, and concurrency.  
  - Must be tightly coupled with cost and energy considerations if used in production.

- `validation-error-investigation-runbook.md`  
  - For schema/gov error spikes (often linked to new upstream formats).  
  - Includes quick queries, sample extraction, and fix/deploy guidance.

Each runbook implementation MUST be **consistent** with this index and with the referenced WAL and telemetry contracts.

⸻

## 🧪 7. CI & Governance Requirements

CI SHOULD:

- Validate that each required runbook file:
  - Exists in this directory.  
  - Contains a YAML header aligned with KFM-MDP v11.2.3.  
  - Mentions relevant alerts or policies where appropriate.

- Optionally lint for:
  - Required headings (Purpose, Preconditions, Stabilize, Diagnose, Remediate, Verify, Postmortem).  
  - Broken internal links.

Governance reviews MUST:

- Confirm that runbooks:
  - Reflect current reality of WAL, SQS, and operators.  
  - Align with CARE/FAIR and sovereignty policies (no unsafe data exposure during incident debugging).  
  - Are kept in sync with alert and dashboard changes.

Any **replay behavior change** that bypasses these runbooks is a governance violation.

⸻

## 📘 8. Version History

| Version  | Date       | Notes                                                                                                       |
|---------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD replay runbooks index; defined required runbook set, structure, and integration with WAL/telemetry.|

---

<div align="center">

🧰 NODD Replay Runbooks Index · KFM v11.2.3  

Deterministic · Replay-Safe · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Replay](../README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[📊 Telemetry](../../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
