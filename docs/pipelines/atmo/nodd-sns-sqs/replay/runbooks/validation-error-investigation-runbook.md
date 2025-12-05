---
title: "🧪 KFM v11.2.3 — NODD Validation Error Investigation Runbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed runbook for investigating, classifying, and remediating validation and governance error bursts in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/validation-error-investigation-runbook.md"

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
intent: "nodd-sns-sqs-validation-error-investigation-runbook"
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

# 🧪 NODD Validation Error Investigation Runbook  

`docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/validation-error-investigation-runbook.md`

Governed runbook for **investigating validation and governance error bursts** in the NOAA NODD SNS → SQS ingestion pipeline.

Use this when:

- Validation / governance error alerts fire (for example, `NODD-VAL-ERR-WARN`).  
- DLQ messages are dominated by specific schema, integrity, or governance failure types.  
- You need to understand whether errors arise from upstream changes, code regressions, or configuration/gov issues.

All investigation MUST be:

- **WAL-anchored** (using WAL records as ground truth)  
- **Reproducible** (steps can be re-run from the same inputs)  
- **CARE/FAIR compliant** (no unsafe handling of sensitive content)  

Referenced specs:

- WAL: `../wal/README.md`, `../wal/wal-record-model.md`, `../wal/wal-state-machine.md`  
- Alerts: `../../telemetry/alerts/README.md`, `../../telemetry/alerts/nodd-alert-policies.md`  
- Dashboards: `../../telemetry/dashboards/nodd-ingestion-dashboard.md`  

⸻

## 1. Purpose & Severity

### 1.1 Purpose

This runbook defines how to:

- Diagnose **validation and governance error spikes**  
- Classify errors by dataset, type, and cause  
- Decide whether to:
  - Patch schemas or code  
  - Adjust governance rules  
  - Quarantine or replay affected records  

It is used when:

- Validation errors increase suddenly or persist at elevated levels  
- DLQ is being filled with consistent failure patterns  
- Upstream format changes are suspected

### 1.2 Typical Triggers

- Alert `NODD-VAL-ERR-WARN` (validation/gov error surge) is firing.  
- DLQ analysis shows many messages with similar failure codes.  
- Application logs highlight repeated schema or governance violations during NODD ingestion.

### 1.3 Severity Levels

- P1: Validation/gov errors causing large data loss or systemic ingest failure.  
- P2: Sustained error spikes for one or more critical datasets.  
- P3: Localized errors or minor schema drift detected early.

For P1/P2 incidents, this runbook MUST be linked from the incident record.

⸻

## 2. Preconditions & Safety Checks

Before deep investigation:

1. Confirm environment  

   - Identify `env` (`dev`, `stage`, `prod`).  
   - For `prod` incidents:
     - Ensure an incident or change ticket is open.

2. Check other incident runbooks  

   - If queue-age or depth alerts are also firing:
     - Coordinate with `delayed-queue-runbook.md`.  
   - If DLQ depth is high:
     - Also consult `dlq-drain-runbook.md`.

3. Verify WAL health  

   - Ensure WAL backend is reachable and stable.  
   - No major WAL storage or concurrency errors.

4. Confirm telemetry visibility  

   - Ensure `nodd_sns.validation_errors_total` metrics are present and updating.  
   - Confirm DLQ metrics are available for cross-check.

5. Respect data sensitivity  

   - If validation errors involve potentially sensitive content (e.g., derived from locations intersecting sovereign or protected areas):
     - Adhere to sovereignty policies and CARE guidelines when inspecting payloads.  
   - Prefer **metadata-level** and **redacted** inspection where possible.

6. Notify stakeholders  

   - Announce investigation in `kfm-nodd-sre` and, for P1/P2, in the incident channel.  
   - Include which datasets and environments appear affected.

⸻

## 3. Detection & Triage

Use telemetry and WAL to understand the basic shape of the problem.

1. Error rate and trend  

   - Review `nodd_sns.validation_errors_total{dataset,env,error_type}` as a rate or derivative.  
   - Determine:
     - When the spike started.  
     - Whether rates are increasing, stable, or declining.

2. Dataset scope  

   - Identify which datasets are emitting most errors:
     - Single dataset (e.g., `goes-abi` only).  
     - Clustered by similar product type.  
     - System-wide (multiple datasets at once).

3. Error-type distribution  

   - Group by `error_type` (from telemetry and WAL `last_error_code`), such as:
     - `schema_mismatch`  
     - `geo_invalid`  
     - `integrity_missing_object`  
     - `governance_hard_fail`  
     - `stac_validation_failed`

4. Time correlation  

   - Compare onset of errors with:
     - Recent deploys.  
     - Schema/contract updates.  
     - Upstream provider notices or known change windows.

5. Impact assessment  

   - Estimate:
     - Fraction of ingest attempts failing.  
     - Number of records affected per dataset.  
   - Decide if severity is P1, P2, or P3.

⸻

## 4. Stabilize (If Errors Are Ongoing)

If validation/gov errors are still actively occurring at high rate:

1. Pause non-critical replays and backfills  

   - Avoid compounding errors with additional replays until the cause is understood.

2. Consider dataset kill-switch for severe, localized issues  

   - For non-critical datasets heavily affected:
     - Temporarily pause new ingestion.  
   - For critical datasets:
     - Seek a minimal mitigation (e.g., targeted filter) and escalate to P1 if necessary.

3. Avoid blind schema/contract changes  

   - Do NOT make ad hoc schema or governance changes in prod without:
     - Clear hypothesis.  
     - Validation in `dev`/`stage`.  
     - Council awareness for P1/P2 issues.

4. Protect DLQ and WAL  

   - Ensure DLQ and WAL systems are not overwhelmed:
     - If necessary, temporarily rate-limit ingestion while investigation proceeds.

⸻

## 5. Diagnose — WAL and Payload Analysis

Anchor the diagnosis on WAL records and redacted payload samples.

1. Pull representative WAL slice  

   - For affected datasets, query WAL where:
     - `status = "failed"`  
     - `last_error_code` matches the dominant failure types  
     - `created_at` within the problematic time window

2. Confirm WAL correctness  

   - Ensure each error in telemetry has a corresponding WAL record with:
     - Appropriate `last_error_code` and `last_error_message`.  
     - Correct `dataset`, `object_uri`, and temporal fields.

3. Sample payloads safely  

   - Retrieve a limited number of source objects or derived payloads:
     - Prefer `dev`/`stage` or a private investigation environment.  
   - Apply:
     - Redaction for sensitive fields.  
     - Spatial generalization if necessary (H3 or equivalent).

4. Compare payloads vs contracts  

   - Check relevant schema/contract docs:
     - SNS/SQS message schema (`sns-schema/`, `sqs-contract/`).  
     - Dataset-specific ingestion contracts (`config/dataset-contracts/`).  
     - STAC writer contracts (`stac-writers/`).

   - Identify where actual payload diverges from:
     - Required JSON schema.  
     - Expected field types or ranges.  
     - Required metadata (CRS, time, geometry).

5. Distinguish error types  

   For each major `last_error_code`:

   - Schema mismatch:
     - Fields missing or types changed (e.g., integer vs string).  

   - Spatial/temporal validity:
     - Invalid geometries, out-of-range timestamps.  

   - Integrity:
     - Missing source objects or truncated payloads.  

   - Governance:
     - Violations of sensitivity, sovereignty, or CARE rules.  

   - STAC validation:
     - Invalid Items or Collections based on STAC/KFM extensions.

6. Hypothesize root causes  

   - Summarize per dataset:
     - Upstream format change?  
     - Code or schema regression?  
     - New governance rule catching previously unhandled cases?

⸻

## 6. Remediate — Fixes and Changes

Choose an appropriate remediation based on diagnosed causes.

### 6.1 Upstream Format Changes

If upstream providers changed formats:

1. Update ingestion contracts  

   - Amend dataset contracts in `config/dataset-contracts/` to match new format.  
   - Ensure contracts are versioned and documented.

2. Adjust parsing and validation logic  

   - Update relevant operators:
     - `message-parse`  
     - `metadata-extract`  
     - Downstream schema validation  

3. Regenerate schemas (if applicable)  

   - Update JSON Schema and tests that encode the expected envelopes.

4. Validate in `dev`/`stage`  

   - Re-run a sample workflow with updated logic before enabling in `prod`.

### 6.2 Schema / Code Regression

If a deploy introduced a bug:

1. Patch or rollback code  

   - Coordinate with deployment owners to:
     - Rollback to known-good version, or  
     - Hotfix and redeploy with tests.

2. Enhance tests  

   - Add tests to:
     - CI for schema validation.  
     - Unit/integration tests covering the failure scenario.

3. Plan replays  

   - Once code is fixed, use:
     - `dlq-drain-runbook.md` for draining DLQ records.  
     - `incident-replay-runbook.md` for any required replays beyond DLQ.

### 6.3 Governance Rule Issues

If errors are `governance_hard_fail` or similar:

1. Review governance rules  

   - Check:
     - `langgraph-gates` configs.  
     - CARE/sovereignty rules in `care.rules.yaml` or equivalent.

2. Decide on policy direction  

   - Confirm with governance stakeholders whether:
     - The hard fail is correct and data must be quarantined, or  
     - Rules need adjustment to allow specific cases with safeguards.

3. Apply changes cautiously  

   - Adjust governance configs only:
     - With documented rationale.  
     - After testing in non-prod.  
   - Maintain strict logging and audit trails for any change that lowers restrictions.

4. Quarantine or replay  

   - For records that violated governance before rules were corrected:
     - Leave in `quarantined` if they remain non-compliant.  
     - Or reclassify and replay only with explicit governance approval.

### 6.4 Data Integrity Issues

If objects are missing or corrupted:

1. Confirm upstream problem  

   - Validate that object loss or truncation is on the provider side.  

2. Explore recovery options  

   - Check for mirrors, redundancy, or fallback sources.  

3. Decide fate of records  

   - If data cannot be recovered:
     - Mark WAL records as `quarantined` with a clear `last_error_code`.  
   - Avoid repeated replays that will always fail.

⸻

## 7. Verify — Error Reduction and System Health

After applying fixes:

1. Monitor validation errors  

   - Ensure `nodd_sns.validation_errors_total` rate returns to normal or near zero for affected errors.  
   - Confirm `NODD-VAL-ERR-WARN` and related alerts clear.

2. Check DLQ behavior  

   - For error classes you expect to be resolved:
     - DLQ depth should flatten or decrease.  
     - New DLQ entries for those error types should be rare.

3. Confirm WAL transitions  

   - For previously failing records that have been replayed:
     - WAL statuses should move from `failed` to `succeeded` or acceptable terminal states.  
   - No increase in `replay_mismatch_total`.

4. Validate outputs  

   - Spot-check:
     - STAC items from previously failing cases.  
     - Provenance trails for those items.  
   - Confirm they meet contracts and governance requirements.

5. Check no collateral damage  

   - Ensure:
     - Other datasets are unaffected or improved.  
     - No new validation error types have appeared as a side effect.

⸻

## 8. Postmortem & Governance

For significant validation/gov error incidents (P1/P2) or large P3 events:

1. Complete incident or change record  

   - Include:
     - Error types, datasets, and volumes.  
     - Root cause analysis (upstream, code, config, governance).  
     - Fixes implemented and their validation.

2. Document error classes  

   - Maintain a knowledge list of:
     - Common `last_error_code` patterns.  
     - Standard remediation approaches.

3. Improve tests and monitoring  

   - Add:
     - CI tests covering the failing cases.  
     - New dashboard views or alert refinements if needed.

4. Update documentation  

   - If new contract or governance rules were introduced:
     - Update:
       - Dataset contracts.  
       - Governance docs.  
       - Operator docs (e.g., `integrity-check`, `metadata-extract`, `stac-register`).

5. Governance review  

   - Provenance & Reliability Council SHOULD:
     - Confirm remediation maintained deterministic behavior.  
     - Review any governance rule changes.  
     - Approve adjustments to alert thresholds or runbooks if needed.

⸻

## 9. Version History

| Version  | Date       | Notes                                                                                                                  |
|---------:|------------|------------------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD validation error investigation runbook; defined WAL-centered diagnosis, remediation patterns, and checks. |

---

<div align="center">

🧪 NODD Validation Error Investigation Runbook · KFM v11.2.3  

WAL-Anchored · Schema-Grounded · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Runbooks](README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[📊 Telemetry Alerts](../../telemetry/alerts/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
