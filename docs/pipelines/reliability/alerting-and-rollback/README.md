---
title: "🚨 KFM v11.2.4 — SQS/Lambda Alerting & lakeFS Safe Rollback (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/pipelines/reliability/alerting-and-rollback/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Eng · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x"
status: "Active / Enforced"

doc_kind: "Runbook + Pattern"
intent: "reliability-alerting-rollback"
role: "reliability-runbook-and-pattern"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "reliability"
  applies_to:
    - "etl"
    - "ai-workloads"
    - "messaging"
    - "data-lake"
    - "governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Reliability & Rollback"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/reliability-telemetry.json"
telemetry_schema: "schemas/telemetry/reliability-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/reliability/alerting-and-rollback/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-reliability-alerting-rollback-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-reliability-alerting-rollback-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:reliability:alerting-and-rollback:v11.2.4"
semantic_document_id: "kfm-pipelines-reliability-alerting-and-rollback-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:reliability:alerting-and-rollback:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "pattern-contract-check"

ci_integration:
  workflow: ".github/workflows/reliability-alerting-rollback.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Reliable Pipelines × Safe Rollback × Sustainable Operations"
  architecture: "SQS/Lambda Alerting · lakeFS Branching · PROV-Tracked"
  analysis: "Evidence-Led · MTTR-Aware · FAIR+CARE Grounded"
  data-spec: "CloudWatch · lakeFS · Neo4j Lineage"
  telemetry: "Alerts · Incidents · Energy/Carbon Impact"
  graph: "Events · Activities · DatasetVersions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🚨 **KFM v11.2.4 — SQS/Lambda Alerting & lakeFS Safe Rollback**  
`docs/pipelines/reliability/alerting-and-rollback/README.md`

**Purpose:**  
Define a governed **alerting + rollback pattern and runbook** that hardens KFM pipelines by:

- Standardizing **CloudWatch → SNS** alerting for **Amazon SQS & AWS Lambda** (low‑noise, SLO‑aware).  
- Providing a **lakeFS branch + reset/revert** rollback pattern so data‑lake state can be restored to a **known‑good commit** deterministically.  

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

This runbook + pattern ensures that:

- Messaging and worker health issues (SQS backlog, Lambda errors) trigger **meaningful, de‑duplicated alerts** instead of noisy pages.  
- Data corruption or bad promotions can be **rolled back safely** using **lakeFS branches and commits**, with full **PROV‑O provenance** and governance notes.  

It applies to:

- **ETL & AI workloads** using SQS/Lambda or equivalent event‑driven components.  
- **Data‑lake environments** tracked by lakeFS (e.g., `env/dev`, `env/stage`, `env/prod`).  
- **Governed rollback paths** where provenance and ethics matter as much as uptime.

In KFM v11.2.4 this document is **Diamond⁹ Ω / Crown∞Ω** certified and considered normative for reliability practices around SQS/Lambda and lakeFS.

---

## 🗂️ Directory Layout

Canonical layout for this pattern within the KFM monorepo:

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 reliability/
│           └── 📂 alerting-and-rollback/
│               ├── 📄 README.md                    # This file (pattern + runbook)
│               ├── 📂 runbooks/
│               │   ├── 📄 sqs-lambda-sev2.md       # Detailed incident steps per severity
│               │   └── 📄 lakefs-rollback.md       # Deep-dive rollback procedures
│               └── 📂 specs/
│                   ├── 📄 cw-metrics-and-alarms.md # Metrics catalog + alarm contracts
│                   └── 📄 lakefs-branching.md      # Branch/merge/reset/revert standards
│
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 reliability/
│           └── 📂 alerting_and_rollback/
│               ├── 📄 __init__.py
│               ├── 📄 sqs_metrics_adapter.py       # Pull/push SQS metrics into KFM telemetry
│               ├── 📄 lambda_metrics_adapter.py    # Lambda metrics transforms & ErrorRatio calc
│               ├── 📄 alert_dispatcher.py          # SNS routing, severity mapping
│               ├── 📄 lakefs_client.py             # Thin client for branch/create/merge/reset
│               ├── 📄 incident_recorder.py         # Writes incident docs & PROV nodes
│               └── 📄 config.py                    # Thresholds, SNS topics, env bindings
│
├── 📂 infra/
│   └── 📂 terraform/
│       └── 📂 reliability/
│           ├── 📄 sqs_lambda_alerts.tf             # Terraform for CloudWatch/SNS wiring
│           └── 📄 lakefs_env_branches.tf           # lakeFS env/run branch configuration
│
├── 📂 data/
│   └── 📂 lineage/
│       └── 📂 reliability/
│           ├── 📂 incidents/                       # PROV + incident records (JSON/JSON-LD)
│           └── 📂 rollbacks/                       # Rollback events and justifications
│
└── 📂 .github/
    └── 📂 workflows/
        ├── 📄 reliability-alerting-tests.yml       # Unit tests for metrics/alert code
        └── 📄 reliability-rollback-audit.yml       # lakeFS + provenance + policy checks
~~~

**Author rules:**

- All reliability alerting/rollback docs reference this pattern and live under `docs/pipelines/reliability/alerting-and-rollback/`.  
- Terraform and implementation code must point back here in comments or module docs.  
- Any new subdirectory under these trees must be added to this layout with an emoji + short description.

---

## 🧭 Context

KFM pipelines rely heavily on:

- **Amazon SQS** for decoupled, back‑pressure‑tolerant messaging.  
- **AWS Lambda** (or equivalent event workers) for scalable compute.  
- **lakeFS** to treat the lake like a **versioned Git repository** with branches, commits, and merges.

Failure scenarios we care about:

- **SQS backlog surge** or **oldest message age spikes** indicating consumer lag or dead consumers.  
- **Lambda error rates or throttling** leading to dropped work or DLQ growth.  
- **Bad data promotions** that poison downstream STAC, graph, or models, requiring **fast, safe rollback**.

This pattern splits concerns cleanly:

- **Alerting path**: CloudWatch → SNS → Pager/Chat (with anti‑noise controls).  
- **Rollback path**: lakeFS run branches → env branch promotion → deterministic reset/revert, with provenance.

---

## 🧱 Architecture

### 1. CloudWatch Alerting (SQS + Lambda)

#### 1.1 Key Metrics — SQS

Metrics:

- `ApproximateNumberOfMessagesVisible` → backlog growth  
- `ApproximateAgeOfOldestMessage` → latency / SLA breach risk  
- `NumberOfMessagesReceived / Deleted` → flow health (dashboard, not usually paged)  

KFM starting thresholds (tune per pipeline SLO):

- **BacklogHigh**  
  - Condition: `ApproximateNumberOfMessagesVisible ≥ 1,000` for **5 min**  
- **OldestAgeHigh**  
  - Condition: `ApproximateAgeOfOldestMessage ≥ 300s` for **5 min**  
- **BacklogSev2 (night)**  
  - Condition: `ApproximateNumberOfMessagesVisible ≥ 5,000` for **15 min** (off‑hours dampening)

#### 1.2 Key Metrics — Lambda

Metrics:

- **ErrorRatio**  
  - Definition: `Errors / Invocations ≥ 2%` for **5 min**  
- **Throttles**  
  - Definition: `Throttles ≥ 5` for **5 min**  
- **DLQ depth** (if configured)  
  - Definition: DLQ message count `> 0` for **10 min**

> **Alert fatigue guardrails**  
> - Prefer **composite alarms** (e.g., `OldestAgeHigh AND BacklogHigh`) before paging.  
> - Use **period ≥ 60s** and **datapoints_to_alarm ≥ 3**.  
> - Disable “OK” notifications; use daily/weekly dashboards for clears.  
> - Route Sev2/Sev3 to a **single SNS topic** with filter policies (`team="kfm-pipelines"`).

#### 1.3 Terraform Starter (Canonical Pattern)

~~~hcl
# SNS topic
resource "aws_sns_topic" "kfm_alerts" {
  name = "kfm-pipelines-alerts"
}

# SQS: Oldest message age
resource "aws_cloudwatch_metric_alarm" "sqs_oldest_age_high" {
  alarm_name          = "kfm-sqs-OldestAgeHigh"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 3
  metric_name         = "ApproximateAgeOfOldestMessage"
  namespace           = "AWS/SQS"
  period              = 60
  statistic           = "Maximum"
  threshold           = 300

  dimensions = {
    QueueName = var.queue_name
  }

  alarm_actions = [aws_sns_topic.kfm_alerts.arn]
}

# SQS: Backlog high
resource "aws_cloudwatch_metric_alarm" "sqs_backlog_high" {
  alarm_name          = "kfm-sqs-BacklogHigh"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 3
  metric_name         = "ApproximateNumberOfMessagesVisible"
  namespace           = "AWS/SQS"
  period              = 60
  statistic           = "Average"
  threshold           = 1000

  dimensions = {
    QueueName = var.queue_name
  }

  alarm_actions = [aws_sns_topic.kfm_alerts.arn]
}

# Lambda: Error ratio via math expression
resource "aws_cloudwatch_metric_alarm" "lambda_error_ratio" {
  alarm_name          = "kfm-lambda-ErrorRatioHigh"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 3
  threshold           = 0.02
  alarm_actions       = [aws_sns_topic.kfm_alerts.arn]

  metric_query {
    id          = "err"
    return_data = false

    metric {
      metric_name = "Errors"
      namespace   = "AWS/Lambda"
      period      = 60
      stat        = "Sum"

      dimensions = {
        FunctionName = var.lambda_name
      }
    }
  }

  metric_query {
    id          = "inv"
    return_data = false

    metric {
      metric_name = "Invocations"
      namespace   = "AWS/Lambda"
      period      = 60
      stat        = "Sum"

      dimensions = {
        FunctionName = var.lambda_name
      }
    }
  }

  metric_query {
    id          = "ratio"
    expression  = "err / IF(inv, inv, 1)"
    label       = "ErrorRatio"
    return_data = true
  }
}
~~~

> **Integration notes**  
> - Wire SNS → Pager/Chat bridge with **message attributes** (`service`, `severity`, `environment`).  
> - Apply **quiet‑hours routing** where acceptable (no quiet hours for P0).  
> - Mirror metrics into **Grafana** with KFM cardinality rules (no unbounded labels).

---

### 2. Safe Rollback with lakeFS

#### 2.1 Pattern

- Every pipeline run writes into its own **lakeFS run branch**:  
  - Example: `runs/run-2025-12-06T02-10Z-abc123`.  
- **Promotion** merges the run branch into an **environment branch** (e.g., `env/prod`) **only after** all validation gates pass:  
  - Data quality (Great Expectations, similar).  
  - Model behavior checks (SHAP, domain‑specific metrics).  
  - KFM provenance checks (PROV‑O shape, telemetry completeness).  
- **Rollback**: move the environment branch `HEAD` back to a **known‑good commit** or revert a specific merge; then re‑materialize derived views and clear caches.

#### 2.2 Reference Commands

~~~bash
# Create isolated run branch from env/stage
lakefs branch create \
  lakefs://kfm/env/stage \
  lakefs://kfm/runs/run-2025-12-06T02-10Z-abc123

# Write artifacts (STAC items, parquet, tiles, etc.) to the run branch...

# After checks pass, promote to env/prod:
lakefs merge \
  lakefs://kfm/runs/run-2025-12-06T02-10Z-abc123 \
  lakefs://kfm/env/prod

# If hotfix/rollback is needed:

# Option A: reset env/prod HEAD to a known-good commit
lakefs branch reset \
  lakefs://kfm/env/prod \
  --to-commit <good_commit_sha>

# Option B: revert a specific merge commit
lakefs revert \
  lakefs://kfm/env/prod \
  --commit <bad_merge_sha>

# Then: re-run validation/materialization over env/prod
# and clear caches / tiles / API layers as required.
~~~

#### 2.3 Provenance & Governance

- Emit **PROV‑O JSON‑LD** for each run with:
  - Inputs (dataset versions, code refs, config digests).  
  - lakeFS commit IDs and branches.  
  - Telemetry: energy/carbon/cost for the run.  
- Stamp the promoted commit with:
  - **SLSA attestation** and **SBOM digest** from `releases/v11.2.4`.  
- On rollback:
  - Emit a **correction Activity** in PROV that references:
    - The reverted commit.  
    - Reason category (`data-quality`, `governance`, `security`, etc.).  
    - Human approver, if manual.  

---

### 3. Runbook — Common Scenarios

#### 3.1 Backlog Surge (Sev2)

1. **Confirm signal**  
   - Inspect CloudWatch graphs for `ApproximateNumberOfMessagesVisible` and `ApproximateAgeOfOldestMessage`.  
   - Check Lambda **ErrorRatio** and **Throttles**.  
2. **Stabilize flow**  
   - Temporarily increase Lambda concurrency or provisioned throughput.  
   - Ensure DLQ depth is not growing; if it is, triage DLQ messages.  
3. **Guard data quality**  
   - If upstream data looks suspect, **pause promotion** into `env/prod` (lakeFS merge hold).  
   - Continue writing into run branches while debugging.  
4. **After resolution**  
   - Reduce concurrency back to baseline.  
   - Update thresholds and composite logic if alerts were noisy.  
   - File a short incident report in `data/lineage/reliability/incidents/`.

#### 3.2 Bad Data Promotion (Sev2)

1. Identify **env/prod** head commit `<bad_sha>` and last known‑good `<good_sha>`.  
2. Choose rollback mode:
   - **Reset** (`branch reset --to-commit <good_sha>`) when the entire bad run should disappear.  
   - **Revert** (`revert --commit <bad_sha>`) to preserve history but undo the merge.  
3. **Re‑validate** over current env/prod:
   - Run data quality checks.  
   - Re‑publish derived data (tiles, materialized views).  
4. **Rebuild downstream indices**:
   - Neo4j, search indices, tiles, caches, etc.  
5. Record:
   - PROV correction event in `data/lineage/reliability/rollbacks/`.  
   - Human‑readable incident summary + governance note.

---

## 📦 Data & Metadata

Key artifacts:

- **Telemetry**  
  - CloudWatch metrics → internal reliability telemetry streams (via adapters).  
  - KFM telemetry documents in `releases/v11.2.4/reliability-telemetry.json`.  

- **Incidents & Rollbacks**  
  - `data/lineage/reliability/incidents/*.json` (incident summaries).  
  - `data/lineage/reliability/rollbacks/*.prov.jsonld` (PROV correction events).  

- **Infrastructure as Code**  
  - Terraform modules under `infra/terraform/reliability/` parameterized by environment, queue name, and Lambda function name.  

Metadata alignment:

- **DCAT**: reliability telemetry datasets can be cataloged as DCAT Datasets with:
  - `dct:title` = "KFM Reliability Telemetry (SQS/Lambda + lakeFS)"  
  - `dct:conformsTo` = reliability standard v11.2.4  
- **PROV‑O**: incidents and rollbacks modeled as Activities; lakeFS commits and datasets as Entities; engineers and automation as Agents.

---

## 🧪 Validation & CI/CD

CI workflows **must** verify:

- **Terraform plan checks**  
  - No alarms with missing SNS actions.  
  - No alarm configurations without environment scoping.  

- **Alerting unit tests**  
  - ErrorRatio calculation.  
  - Composite alarm conditions.  
  - SNS message formatting (including severity, service, environment attributes).

- **Rollback policy checks**  
  - Only whitelisted roles may perform lakeFS `reset` / `revert` on env branches.  
  - Every rollback triggers a PROV correction document and an incident record.  

- **Telemetry schema checks**  
  - `reliability-telemetry.json` validates against `schemas/telemetry/reliability-v1.json`.  
  - Metrics names and label sets comply with KFM cardinality and naming rules.

SLOs (recommended defaults):

- **Incident MTTA (Mean Time to Acknowledge)**:  
  - Sev2: ≤ 15 minutes during on‑call hours.  

- **Rollback MTTR for bad data promotions**:  
  - Sev2: ≤ 60 minutes from detection to env/prod corrected.  

- **Alert noise**:  
  - < 1 false‑positive Sev2 per service per week under normal operation.

---

## ⚖ FAIR+CARE & Governance

This reliability pattern supports FAIR+CARE by:

- **FAIR**  
  - Reliability telemetry and incident history are stored as **findable**, **accessible** datasets with clear provenance.  
  - Rollback events are modeled using PROV‑O for **interoperability** with other KFM lineage standards.  

- **CARE**  
  - Alerting and rollback patterns are designed to **protect downstream consumers** (including heritage and sensitive overlays) from prolonged exposure to bad data.  
  - Rollback decisions are documented, with explicit **responsibility** and justification, so governance bodies can review them.  

Governance expectations:

- Any changes to:
  - Default alert thresholds, or  
  - lakeFS promotion/rollback rules  

must be reviewed by Reliability Eng + FAIR+CARE Council when they affect:

- Data used in regulated reporting.  
- Data participating in heritage/sensitive overlays.  

---

## 🕰️ Version History

| Version   | Date       | Description                                                                                          |
|----------:|------------|------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial governed runbook + pattern for SQS/Lambda alerting and lakeFS safe rollback, with CI hooks. |

---

<div align="center">

🚨 **KFM v11.2.4 — SQS/Lambda Alerting & lakeFS Safe Rollback**  
Reliable Messaging · Deterministic Rollback · Provenance‑First  

[📘 Pipelines Index](../../README.md) · [🧱 Reliability Patterns](../README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>