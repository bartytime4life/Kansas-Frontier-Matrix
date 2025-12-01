<div align="center">

# ⚖️ **Cardinality Governance Procedures (Detailed Enforcement Specification)**  
`docs/telemetry/metrics/cardinality/governance/governance.md`

**Purpose**  
Define the **step-by-step enforcement logic, escalation chain, deny-match rules, investigation workflow, and governance ticketing protocol** associated with metric cardinality violations in KFM v11.  
This file operationalizes the rules declared in this directory’s `README.md`.

</div>

---

## 🧪 Enforcement Lifecycle

This lifecycle governs **all** cardinality infra changes:

1. **Emit or detect** metric samples  
2. **Validate** samples (CI + runtime)  
3. **Compare** emitted labels against the governance whitelist  
4. **Measure** series growth against ASB  
5. **Trigger** violation pipelines when needed  
6. **Record** anomaly in review logs  
7. **Quarantine** offending metrics if necessary  
8. **Open** governance ticket  
9. **Investigate → fix → restore**  
10. **Capture** remediation in Story Node

All telemetry systems MUST comply.

---

## 🧱 1. Metric Introduction Workflow

A new metric may only be introduced after the following steps:

### Step 1 — Submit Metadata
Developer MUST submit:

- `metric_name`  
- description  
- allowed label keys  
- allowed label values (enumerated)  
- expected cardinality estimate  
- expected series count in `prod`  
- owner team  
- stability classification (`alpha`, `beta`, `stable`)  
- lineage reference file  

### Step 2 — Validation
- Metadata MUST validate against telemetry schema  
- CI MUST ensure label keys exist in the cardinality whitelist  
- CI MUST ensure all values map to a bounded vocabulary  
- No forbidden labels may appear, even temporarily  

### Step 3 — Governance Approval
Telemetry Governance Council must approve:

- Label vocabularies  
- Expected series count  
- Stability classification  
- Category placement (metrics vs logs vs traces)

### Step 4 — Controlled Deployment
- New metric is enabled in **dev only**  
- After 48hr stability, deployed to **staging**  
- After review, deployed to **prod**

No metric may bypass this process.

---

## 📉 2. Label Schema Change Workflow

Label schema changes are **dangerous** and require strict approval.

### Step 1 — Proposal
Developer must propose:

- New label key  
- Full vocabulary  
- Reason for introduction  
- Query-hygiene impact  
- Estimated ASB delta  
- Expected usage patterns  

### Step 2 — Governance Review
Council will evaluate:

- Cardinality cost  
- Query complexity  
- Query cost in Grafana / Mimir  
- Impact on dashboards  
- FAIR+CARE and privacy implications  

If accepted → proceed.  
If rejected → new label is forbidden.

### Step 3 — Metadata Update
- Telemetry catalog updated  
- SCHEMA updated  
- Validation rules regenerated  
- CI rules refreshed  

### Step 4 — Deployment
Same 3-stage deploy as metric introduction.

---

## 🔎 3. Violation & Spike Handling Procedures

Violations include:

- Forbidden labels  
- Unbounded values or free-text  
- Per-entity ID labels  
- New label keys without approval  
- Raw paths or URLs  
- Any label not enumerated  
- Unexpected ASB explosion  

### 3.1 Spike detection thresholds
A spike is declared when:

- **≥30% series growth in 5 minutes**  
- **>10k new series in a metric family**  
- **A new label key appears**  
- **Cardinality shift coincides with a deploy**  

### 3.2 Spike Handling Workflow

1. **Detect spike** (scraper / Mimir / CI)  
2. **Emit spike event** to governance pipeline  
3. **Write anomaly** to `review-log.md`  
4. **Attach**:
   - service  
   - environment  
   - time window  
   - offending label(s)  
   - cardinality delta  
5. **Evaluate** need for deny-match rule  
6. **Open governance ticket**  
7. **Create Story Node seed**  
8. **Begin investigation**  

---

## 🛑 4. Quarantine Logic

Quarantine is a **hard safety measure**.  
A metric MUST be quarantined when:

- Forbidden label is detected  
- ASB exceeds hard threshold  
- New label key appears without approval  
- Free-form or unique label values appear  
- Emitted labels violate allowed vocabulary  

### Quarantine Steps

1. Inject **drop rule** (scrape-time reject)  
2. Inject **deny-match** (block queries & recording rules)  
3. Notify service owners  
4. Add entry to review log  
5. Force governance ticket creation  
6. Require remediation plan  
7. Attach PROV-O lineage  

### While Quarantined

- Dashboards referencing the metric MUST display fallback visuals  
- Alerts referencing the metric MUST be paused or revised  
- Metric MUST NOT re-enter the environment until governance re-approves  

---

## 🛠 5. Remediation Workflow

### Step 1 — Verify Root Cause
Identify:

- Commit / deploy introducing the issue  
- Feature flag or config change  
- Label key and value(s)  

### Step 2 — Remove Offending Code
Fix metric exporter:

- Remove forbidden label  
- Replace with binned category  
- Normalize path  
- Move ID to trace or log  

### Step 3 — Regenerate Metadata
Update:

- allowed_labels  
- forbidden_labels  
- vocabularies  
- lineage files  

### Step 4 — Validation
- Static check  
- CI schema validation  
- Prometheus rule validation  
- Mimir rule ingestion dry-run  

### Step 5 — Staged Redeploy
- **dev** → verification  
- **staging** → baseline cardinality  
- **prod** → full reactivation  

### Step 6 — Document Story Node
A remediation Story Node MUST be created.

---

## 📑 6. Deny-Match Rules (Templates)

A deny-match blocks ingestion or recording of metrics violating rules.

### Deny-match Template 1 — Block Entire Metric

~~~text
- action: drop
  match:
    metric_name: "kfm_graph_upserts_total"
~~~

### Deny-match Template 2 — Block Forbidden Label Key

~~~text
- action: drop
  match_re:
    label_name: "(feature_id|tile_id|trace_id)"
~~~

### Deny-match Template 3 — Block Values

~~~text
- action: drop
  match_re:
    layer: "^(.*)$"
    value: "(.*[A-Z].*)$"
~~~

### Deny-match Template 4 — Emergency Quarantine

~~~text
- action: drop
  match_re:
    __name__: ".*"
  source_labels: [ offending_label ]
~~~

---

## 📋 7. Governance Ticket Template

A telemetry governance ticket MUST include:

- Metric family  
- Offending label(s)  
- Type of violation  
- Severity level  
- ASB delta  
- Spike duration  
- Environment  
- Service owner  
- Deployment hash  
- Attached anomaly log  
- Required remediation steps  
- Link to Story Node seed  

---

## 🔎 8. Review Log Entry Template

Every anomaly MUST be appended to:

`docs/telemetry/metrics/cardinality/review-log/review-log.md`

Format:

~~~text
### [2025-11-30] Cardinality Violation — <metric_name>

- Environment: prod
- Service: tiler
- Offending Label(s): feature_id="abc123"
- Cardinality Delta: +42,331 series
- Trigger: Deploy 91fca2d
- Action: Quarantined
- Governance Ticket: GOV-2025-113
- Story Node Seed: urn:kfm:story:telemetry:cardinality:violation:2025-11-30-tiler
~~~

---

## 🧠 Story Node & Focus Mode Integration

- Every governance event produces a **Story Node seed**  
- PROV-O lineage MUST be attached  
- Focus Mode MAY generate:
  - Cardinality “Spike Timeline”  
  - “Quarantine and Restore” narrative  
  - Deployment/label mapping  
- Investigative steps become narrative material  
- Resolution MUST close the narrative loop  

---

<div align="center">

⚖️ **Cardinality Governance Procedures**  
Telemetry Stability · Deterministic Metrics · FAIR+CARE-Aligned  

[⬅ Back to Governance README](./README.md)

</div>

