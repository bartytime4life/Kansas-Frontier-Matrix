---
title: "🧊 Kansas Frontier Matrix — Freeze Runbook (v11) · Release Pipeline Safety Procedure (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/release/runbooks/freeze-runbook.md"
version: "v11.0.0"
last_updated: "2025-11-23"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipeline-freeze-runbook-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Runbook"
intent: "freeze-procedure"
role: "incident-response · reliability"
category: "Pipelines · Release · Runbooks"

classification: "Governed Document"
sensitivity: "Mixed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Reliability-Critical"
indigenous_rights_flag: true
redaction_required: false

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority · Responsibility · Ethics"

data_steward: "KFM Reliability Engineering · FAIR+CARE Council"

provenance_chain:
  - "docs/pipelines/release/runbooks/freeze-runbook.md@v10.4.1"
  - "docs/pipelines/release/runbooks/freeze-runbook.md@v11.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/pipeline-freeze-runbook-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/pipeline-freeze-runbook-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:freeze-runbook-v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas · Tribal Jurisdiction (as applicable)"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next freeze-runbook update"
---

<div align="center">

# 🧊 **KFM v11 — Freeze Runbook**  
`docs/pipelines/release/runbooks/freeze-runbook.md`

**Purpose**  
Define the *official, governed, reproducible procedure* for safely **freezing** any ETL, AI/ML, geospatial, heritage, or STAC/DCAT pipeline during KFM v11 release operations.  

A **freeze** stops canary progression, halts promotion, and ensures all downstream systems use **last_good** artifacts until issues are resolved.

This runbook is a core component of **Reliable Pipelines v11**.

</div>

---

# 📘 1. When to Freeze (Freeze Triggers)

A freeze MUST be executed immediately when any of the following conditions occur:

## 1.1 Data Quality (DQ) Triggers
- Null/dup bounds exceeded  
- Referential integrity failure  
- Out-of-range values (spatial/temporal)  
- Schema drift detected  

## 1.2 Drift Triggers
- PSI > threshold  
- KL or KS failures  
- SHAP/LIME explainability drift  
- Focus Mode narrative-grounding drift  
- Cultural/CARE drift indicators spike  

## 1.3 CARE / Sovereignty Triggers (Automatic Hard Freeze)
- Sensitive-site masking failure (H3 < r7)  
- RAW coordinates detected  
- Missing/invalid community consent token  
- Sovereignty policy violation  
- NHPA §304 breach  

## 1.4 System Reliability Triggers
- Retry storm  
- WAL replay loops  
- Orchestrator timeouts  
- Cost or carbon overspending  

## 1.5 Security / Integrity Triggers
- SBOM mismatch  
- Dependency CVE critical severity  
- Attestation failure  

## 1.6 Human Escalation
- FAIR+CARE Council request  
- Tribal governance request  
- Reliability Engineering override  

---

# 🧭 2. Preconditions Before Executing Freeze

Verify all:

### Operator Permissions
- Access to orchestrator logs  
- Ability to modify freeze flags  
- Access to promotion gate  
- Ability to page on-call teams  

### System State
- Identify failing gate (DQ, drift, CARE, security, etc.)  
- Confirm last_good artifact availability  
- Ensure dashboards are accessible  
- Verify alert routing is active  

---

# 🧨 3. Freeze Procedure (Exact Ordered Steps)

This section is deterministic, reproducible, and CI-auditable per **Reliable Pipelines v11**.

---

## Step 1 — Activate Freeze Flag

Mark the pipeline as **FROZEN** in the orchestrator:

```text
orchestrator/state/<pipeline>/freeze.flag = true
````

Also update the governance ledger:

```
docs/reports/audit/governance-ledger.json
```

Record:

* timestamp
* pipeline ID
* operator
* trigger type
* severity
* CARE status
* link to diff/drift/DQ report

---

## Step 2 — Halt Canary Progression

Stop canary steps **immediately**:

```text
canary/state/<pipeline>/enabled = false
```

Ensure:

* all pending canary jobs are cancelled
* no new percentage slices are scheduled
* monitoring is switched from *promotion mode* to *investigation mode*

---

## Step 3 — Route All Consumers to `last_good`

Switch all read pointers:

```text
current = last_good
candidate = frozen_candidate
```

Includes:

* Neo4j ingestion pointers
* Data lake / parquet sources
* Model registry references
* STAC/DCAT distributions
* Story Node & Focus Mode inference layers

Confirm downstream systems reload safely.

---

## Step 4 — Stop Downstream DAGs

Pause:

* dependent ETL pipelines
* model inference tasks
* scheduled Story Node generation
* ingest jobs that rely on candidate artifacts

Set:

```text
dag/<pipeline>/paused = true
```

---

## Step 5 — Collect Evidence (Diffs, Logs, Drift, CARE)

Generate snapshot evidence:

```
reports/pipelines/freeze/<pipeline>/<timestamp>/
```

Include:

* DQ diff
* Drift report (psi, kl, ks, shap)
* CARE violations
* Promotion diff
* Logs (orchestrator, WAL)
* Cost & sustainability metrics

This is required for **governance review**.

---

## Step 6 — Page On-Call (If Needed)

Severity tiers:

|  Tier | Trigger                     | Escalation                              |
| ----: | --------------------------- | --------------------------------------- |
| **A** | CARE, Sovereignty, Security | FAIR+CARE Council + Reliability On-Call |
| **B** | Drift, DQ, schema           | Reliability On-Call                     |
| **C** | Performance/cost            | Pipeline owner                          |

Notification templates exist in:

```
docs/pipelines/release/runbooks/incident-response.md
```

---

## Step 7 — Start Root-Cause Investigation

Follow:

* `incident-response.md`
* `dq/README.md`
* `drift/README.md`
* `care/README.md`
* Promotion gate logs

Determine if freeze requires:

* quick fix
* full rollback
* data patch
* model retraining
* governance escalation

---

## Step 8 — Update Dashboards

Update:

* Reliability SLO dashboard
* Drift dashboard
* Lineage dashboard
* Cost/sustainability dashboard
* CARE compliance dashboard

Freeze state MUST be visible system-wide.

---

# 🔄 4. Unfreeze Procedure (Unlocking the Pipeline)

Only after:

* All failing gates are green
* CARE/Sovereignty concerns resolved
* Governance Council approval for sensitive datasets
* New candidate validated in **shadow mode**
* Canary 1% → 5% slices pass

---

## Step 1 — Clear Freeze Flag

```text
orchestrator/state/<pipeline>/freeze.flag = false
```

## Step 2 — Reset Canary State

```text
canary/state/<pipeline>/enabled = true
canary/state/<pipeline>/percent = 1
```

## Step 3 — Trigger Shadow Run

Validate:

* DQ
* Drift
* CARE
* Schema
* Security
* Cost

## Step 4 — Re-Enable Downstream DAGs

```text
dag/<pipeline>/paused = false
```

## Step 5 — Governance Sign-Off

CARE-sensitive datasets require:

* FAIR+CARE Council approval
* Tribal governance approval (if flagged)

---

# 📊 5. Telemetry Outputs

Freeze events produce:

* `freeze_trigger_type`
* `freeze_severity`
* `freeze_root_cause`
* `care_violation_flags`
* `drift_flags`
* `dq_flags`
* `artifact_reverted_to`
* `freeze_duration_sec`

Telemetry written to:

```
releases/<version>/focus-telemetry.json
docs/pipelines/release/dashboards/reliability.json
```

---

# 🧭 6. Governance Integration

Freeze events append to:

```
docs/reports/audit/governance-ledger.json
```

Governance review includes:

* FAIR+CARE compliance
* Sovereignty checks
* Cultural impact
* Provenance validation
* Inference leakage review
* SLO/SLA health

---

# 🕰️ 7. Version History

| Version |       Date | Notes                             |
| ------: | ---------: | --------------------------------- |
| v11.0.0 | 2025-11-23 | First v11 Freeze Runbook release. |

---

[Back to Runbooks](README.md) ·
[Back to Release Pipelines](../README.md) ·
[Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

```
