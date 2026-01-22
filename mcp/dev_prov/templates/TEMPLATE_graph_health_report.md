---
title: "TEMPLATE — KFM Graph Health Report 🧠🕸️"
template_id: "KFM-REPORT-GRAPH-HEALTH"
template_version: "0.1.0"
kfm_protocol_version: "v13"
status: "template"
owners:
  graph_ops: "{{owner_graph_ops}}"
  data_steward: "{{owner_data_steward}}"
  ai_ops: "{{owner_ai_ops}}"
last_reviewed_utc: "{{last_reviewed_utc}}"

# Report instance metadata (populate per run)
generated_utc: "{{generated_utc}}"
period_utc:
  start: "{{period_start_utc}}"
  end: "{{period_end_utc}}"

run:
  run_id: "{{run_id}}"
  trigger: "{{trigger}}"                # schedule|manual|push|release
  workflow: "{{workflow_name}}"
  workflow_run_url: "{{workflow_run_url}}"
  git_commit: "{{git_commit}}"
  git_ref: "{{git_ref}}"
  runner: "{{runner}}"                  # github-hosted|self-hosted|local
  trace_id: "{{trace_id}}"

environment:
  name: "{{environment}}"               # dev|staging|prod
  region: "{{region}}"
  deployment: "{{deployment}}"          # docker-compose|k8s|vm|other

systems:
  graph:
    engine: "neo4j"
    uri: "{{neo4j_uri}}"
    database: "{{neo4j_database}}"
    neo4j_version: "{{neo4j_version}}"
    ontology_version: "{{ontology_version}}"
    graph_schema_version: "{{graph_schema_version}}"
  stores:
    postgis_version: "{{postgis_version}}"
    object_store: "{{object_store}}"
    search_index: "{{search_index}}"

observability:
  config_sha256: "{{config_sha256}}"
  container_image: "{{container_image}}"
  sbom_ref: "{{sbom_ref}}"
  logs_ref: "{{logs_ref}}"
  metrics_ref: "{{metrics_ref}}"

governance:
  care_label: "{{care_label}}"          # Public|Restricted|Sensitive|TBD
  classification: "{{classification}}"  # open|restricted|confidential|TBD
  policy_pack_version: "{{policy_pack_version}}"
  policy_run_id: "{{policy_run_id}}"
  redaction_profile: "{{redaction_profile}}"

report_outputs:
  report_dir: "{{report_dir}}"          # e.g., docs/reports/qa/graph_health/2026-01-22T04-05-06Z
  summary_md: "{{report_dir}}/summary.md"
  index_csv: "{{report_dir}}/index.csv"
  artifacts_index: "{{report_dir}}/artifacts.json"
---

<!--
🧩 TEMPLATE USAGE
- Intended destination: docs/reports/qa/graph_health/<timestamp_or_run_id>/summary.md
- Replace {{placeholders}} OR render via your templating step.
- Keep this report “evidence-first”: link every claim to an artifact, query output, or dashboard.
-->

<!-- Choose ONE status badge (delete the others) -->
![Graph Health: PASS](https://img.shields.io/badge/Graph%20Health-PASS-brightgreen?style=for-the-badge)
![Graph Health: WARN](https://img.shields.io/badge/Graph%20Health-WARN-yellow?style=for-the-badge)
![Graph Health: FAIL](https://img.shields.io/badge/Graph%20Health-FAIL-red?style=for-the-badge)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2ea44f?style=flat-square)
![Subsystem](https://img.shields.io/badge/subsystem-neo4j%20graph-blue?style=flat-square)
![Env](https://img.shields.io/badge/env-{{environment}}-informational?style=flat-square)
![Run](https://img.shields.io/badge/run-{{run_id}}-555?style=flat-square)

# 🧠🕸️ Graph Health Report — `{{environment}}` — `{{generated_utc}}`

> **Overall Status:** {{overall_status_emoji}} **{{overall_status}}**  
> ✅ Passed: **{{checks_passed}}/{{checks_total}}** · ⚠️ Warn: **{{checks_warn}}** · ❌ Failed: **{{checks_failed}}** · 🔥 Critical: **{{checks_critical_failed}}**  
> **Primary Risk:** {{primary_risk_summary}}  
> **Next Action:** {{next_action_summary}}

---

## 🗂 Repo context

```text
📁 mcp/
  📁 dev_prov/
    📁 templates/
      📝 TEMPLATE_graph_health_report.md   👈 this template
📁 docs/
  📁 reports/
    📁 qa/
      📁 graph_health/
        📁 {{run_id_or_timestamp}}/
          📝 summary.md
          📊 index.csv
          📦 artifacts/...
```

---

## 🎯 Purpose, scope, and what “healthy” means

### Purpose ✅
- Catch **silent graph corruption** early (constraints/indexes, duplication, missing lineage).
- Detect **pipeline regressions** (volume deltas, ingestion lag, schema drift).
- Provide **auditable evidence** for maintainers (artifacts + queries + links).

### Scope 🧭
In-scope (default):
- Neo4j graph integrity + provenance connectivity
- Metadata lineage coherence (STAC/DCAT/PROV represented in graph)
- Pipeline currency signals (ingestion lag)
- Backups are present and restorable

Out-of-scope (unless enabled):
- Full PostGIS content QA (covered by separate spatial QA runbooks)
- UI rendering correctness (covered by e2e UI checks)
- Deep content correctness (historiography validation) — this report is structural/ops integrity

### Health definition 🟢🟡🔴
- 🟢 **PASS**: No failed checks; no critical warnings; trends within baseline.
- 🟡 **WARN**: Non-critical deviations (e.g., lag near SLA, small drift under cap).
- 🔴 **FAIL**: Any hard failure (constraints invalid, backup restore fails, large unexplained deltas).
- 🔥 **CRITICAL**: Backup verification or constraints/index integrity failure.

---

## 🧾 Run snapshot

| Field | Value |
|---|---|
| Report window | `{{period_start_utc}}` → `{{period_end_utc}}` |
| Run ID | `{{run_id}}` |
| Trigger | `{{trigger}}` |
| Workflow | {{workflow_name}} |
| Commit / ref | `{{git_commit}}` / `{{git_ref}}` |
| Neo4j | `{{neo4j_version}}` · DB: `{{neo4j_database}}` |
| Ontology / schema | `{{ontology_version}}` / `{{graph_schema_version}}` |
| Policy pack | `{{policy_pack_version}}` (run: `{{policy_run_id}}`) |
| Config hash | `sha256:{{config_sha256}}` |
| Artifacts | `{{report_dir}}` |

---

## 🧪 Scorecard

> Tip: If this report is generated, keep the table stable so diffs are meaningful in PRs ✨

| ID | Check | Status | Severity | Signal | Threshold / SLA | Artifact |
|---:|---|:---:|:---:|---|---|---|
| GH-001 | Node & relationship count deltas | {{GH_001_status}} | {{GH_001_severity}} | `nodes_total`, `rels_total`, `Δ%` | Fail if `abs(Δ_nodes%) > 5%` or `abs(Δ_rels%) > 5%` | `./artifacts/node_rel_counts.csv` |
| GH-002 | Constraint & index integrity | {{GH_002_status}} | 🔥 critical | constraints online/valid, indexes online | Fail if any expected missing or not ONLINE/VALID | `./artifacts/constraints_and_indexes.csv` |
| GH-003 | Orphaned metadata nodes | {{GH_003_status}} | {{GH_003_severity}} | orphan count by type | Fail if `orphans > {{orphans_tolerance}}` | `./artifacts/orphans.csv` |
| GH-004 | Ingestion lag (currency) | {{GH_004_status}} | {{GH_004_severity}} | minutes since last seen (per source) | Warn if `> 180 min` (example SLA) | `./artifacts/ingestion_lag.csv` |
| GH-005 | Hub detection (top-degree nodes) | {{GH_005_status}} | {{GH_005_severity}} | degree distribution vs baseline | Warn if degree p95 exceeds baseline by `{{hub_p95_delta}}` | `./artifacts/hub_nodes.csv` |
| GH-006 | Property schema drift | {{GH_006_status}} | {{GH_006_severity}} | drift % and type-changes | Warn/Fail if drift `> 0.5%` | `./artifacts/schema_drift.json` |
| GH-007 | Backup verification (dump + restore) | {{GH_007_status}} | 🔥 critical | dump exists; restore succeeds | Fail if missing dump; CRITICAL if restore fails | `./artifacts/backup/restore_log.txt` |

### 📌 Auto-escalation rule
- If **2+ checks FAIL** → create/attach issue `label: ci_failure` ✅  
- If **GH-002 or GH-007 FAIL** → create **HIGH severity** issue + consider temporary ingest freeze 🧯

---

## 📈 Key metrics (for `index.csv`)

| Metric | Current | Previous | Δ | Status | Notes |
|---|---:|---:|---:|:---:|---|
| Total nodes | {{nodes_total}} | {{nodes_prev}} | {{nodes_delta_pct}} | {{nodes_delta_status}} | {{nodes_delta_note}} |
| Total relationships | {{rels_total}} | {{rels_prev}} | {{rels_delta_pct}} | {{rels_delta_status}} | {{rels_delta_note}} |
| Orphans (total) | {{orphans_total}} | {{orphans_prev}} | {{orphans_delta}} | {{orphans_status}} | {{orphans_note}} |
| Ingestion lag (max, min) | {{lag_max_min}} | {{lag_prev}} | {{lag_delta}} | {{lag_status}} | {{lag_note}} |
| Schema drift (%) | {{schema_drift_pct}} | {{schema_drift_prev}} | {{schema_drift_delta}} | {{schema_drift_status}} | {{schema_drift_note}} |
| Backup restore | {{backup_restore_ok}} | {{backup_restore_prev}} | — | {{backup_restore_status}} | {{backup_restore_note}} |

### `index.csv` suggested columns 🧾
```text
generated_utc,run_id,env,neo4j_version,graph_schema_version,
nodes_total,rels_total,nodes_delta_pct,rels_delta_pct,
constraints_invalid_count,index_offline_count,
orphans_total,orphans_by_type_json,
ingest_lag_max_minutes,ingest_lag_by_source_json,
hub_p95,hub_p95_delta,hub_top50_json,
schema_drift_pct,schema_type_changes_count,
backup_dump_present,backup_restore_ok,
overall_status
```

---

## 🔍 Findings summary

### ✅ What looks good
- {{good_1}}
- {{good_2}}
- {{good_3}}

### ⚠️ Watch items
- {{watch_1}}
- {{watch_2}}

### ❌ Failures (if any)
- {{fail_1}}
- {{fail_2}}

---

## 🧩 Check details

> Keep each check “audit-ready”:
> - **What** was checked
> - **How** it was measured (queries, dashboards, scripts)
> - **Evidence** (artifact links)
> - **Why it matters** (impact)
> - **Fix** (action + owner)

<details>
<summary><strong>GH-001 — Node & relationship count deltas 📊</strong></summary>

**Intent:** Detect bulk-load issues (duplication, drop-outs) via week-over-week volume change.

**Method:**
- Count nodes + relationships; compare to previous snapshot.
- Default fail threshold: **>5%** absolute delta.

**Results:**
- Nodes: `{{nodes_total}}` (prev: `{{nodes_prev}}`, Δ: `{{nodes_delta_pct}}`)
- Rels: `{{rels_total}}` (prev: `{{rels_prev}}`, Δ: `{{rels_delta_pct}}`)

**Artifacts:**
- `./artifacts/node_rel_counts.csv`
- `./artifacts/node_label_counts.csv`
- `./artifacts/rel_type_counts.csv`

**Interpretation:**
- {{GH_001_interpretation}}

**Action (if needed):**
- Owner: {{owner_graph_ops}}
- {{GH_001_action_items}}

</details>

<details>
<summary><strong>GH-002 — Constraint & index integrity 🔒</strong></summary>

**Intent:** Ensure core uniqueness + performance contracts are enforced (no silent corruption).

**Method:**
- Enumerate constraints and indexes (status + type).
- Fail if any expected constraint/index is missing, invalid, or offline.

**Results:**
- Invalid constraints: `{{constraints_invalid_count}}`
- Offline indexes: `{{index_offline_count}}`

**Artifacts:**
- `./artifacts/constraints_and_indexes.csv`
- `./artifacts/constraints_raw.txt`
- `./artifacts/indexes_raw.txt`

**Interpretation:**
- {{GH_002_interpretation}}

**Action (critical path):**
- Owner: {{owner_graph_ops}}
- {{GH_002_action_items}}

</details>

<details>
<summary><strong>GH-003 — Orphaned metadata nodes 🧵</strong></summary>

**Intent:** Detect broken lineage (e.g., STAC items not connected to datasets; PROV activities missing USED/GENERATED edges).

**Method:**
- Count orphans by type.
- Fail if above tolerance: `{{orphans_tolerance}}`.

**Results:**
- Total orphans: `{{orphans_total}}`
- Breakdown: `{{orphans_by_type}}`

**Artifacts:**
- `./artifacts/orphans.csv`
- `./artifacts/orphans_sample.md`

**Interpretation:**
- {{GH_003_interpretation}}

**Action:**
- Owner: {{owner_data_steward}}
- {{GH_003_action_items}}

</details>

<details>
<summary><strong>GH-004 — Ingestion lag / currency ⏱️</strong></summary>

**Intent:** Identify stalled feeds or stuck pipelines before users notice.

**Method:**
- Compute “minutes since last seen” per source from graph/provenance timestamps.
- Warn if any critical source exceeds SLA (example: **3 hours**).

**Results:**
- Max lag: `{{ingest_lag_max_minutes}}` minutes
- Lag by source: `{{ingest_lag_by_source}}`

**Artifacts:**
- `./artifacts/ingestion_lag.csv`
- `./artifacts/promql_ingestion_lag.txt` (if used)

**Interpretation:**
- {{GH_004_interpretation}}

**Action:**
- Owner: {{owner_graph_ops}}
- {{GH_004_action_items}}

</details>

<details>
<summary><strong>GH-005 — Hub detection (top-degree nodes) 🕸️</strong></summary>

**Intent:** Spot abnormal “supernodes” that often indicate accidental fan-out relationships, duplication, or ontology misuse.

**Method:**
- Compute top 50 nodes by degree.
- Compare degree distribution vs baseline (p95).

**Results:**
- p95 degree: `{{hub_p95}}` (baseline: `{{hub_p95_baseline}}`, Δ: `{{hub_p95_delta}}`)
- Top nodes: `{{hub_top50_summary}}`

**Artifacts:**
- `./artifacts/hub_nodes.csv`
- `./artifacts/hub_degree_histogram.png` (optional)

**Interpretation:**
- {{GH_005_interpretation}}

**Action:**
- Owner: {{owner_graph_ops}}
- {{GH_005_action_items}}

</details>

<details>
<summary><strong>GH-006 — Property schema drift 🧬</strong></summary>

**Intent:** Catch unplanned schema changes (new keys, type changes) before they break API/UI/AI.

**Method:**
- Sample property keys/types by node label.
- Compare to contract JSON (expected keys + types).
- Default max drift: **0.5%**.

**Results:**
- Drift: `{{schema_drift_pct}}%`
- Type changes: `{{schema_type_changes_count}}`

**Artifacts:**
- `./artifacts/schema_drift.json`
- `./artifacts/schema_drift_diff.md`
- Contract: `{{schema_contract_path}}`

**Interpretation:**
- {{GH_006_interpretation}}

**Action:**
- Owner: {{owner_graph_ops}}
- {{GH_006_action_items}}

</details>

<details>
<summary><strong>GH-007 — Backup verification (dump + restore) 💾</strong></summary>

**Intent:** Prove backups aren’t “Schrödinger backups” — they must restore.

**Method:**
- Confirm latest Neo4j dump exists.
- Optional: restore into disposable container; verify database opens and basic query succeeds.

**Results:**
- Dump present: `{{backup_dump_present}}`
- Restore OK: `{{backup_restore_ok}}`

**Artifacts:**
- `./artifacts/backup/manifest.json`
- `./artifacts/backup/restore_log.txt`
- `./artifacts/backup/restore_smoke_test.txt`

**Interpretation:**
- {{GH_007_interpretation}}

**Action (critical path):**
- Owner: {{owner_graph_ops}}
- {{GH_007_action_items}}

</details>

---

## 🛡️ Policy & governance signals

### Provenance-first publishing 🧾
- Coverage: `{{prov_coverage_pct}}%` of graph-visible datasets have PROV evidence
- Exceptions (if any): `{{prov_exceptions_count}}` → `./artifacts/prov_exceptions.csv`

**Notes:**  
- Any “graph without catalogs” is a policy violation (no bypassing STAC/DCAT/PROV).  
- Streaming/real-time data must still carry at least **stub provenance** before graph/UI use.

### Classification & redaction 🔐
- Classified nodes present: `{{classified_nodes_count}}`
- Unclassified nodes requiring labels: `{{unclassified_required_count}}`
- Redaction profile: `{{redaction_profile}}`

### CI / policy pack outcome ✅
- Policy run: `{{policy_run_id}}`
- Denies: `{{policy_denies_count}}`
- Warnings: `{{policy_warn_count}}`
- Artifact: `./artifacts/policy_pack_results.json`

---

## 🤖 AI / Focus Mode signals (optional but recommended)

> Why here? Focus Mode reliability depends on **graph quality + provenance connectivity**.

| Signal | Current | Target | Status | Evidence |
|---|---:|---:|:---:|---|
| Retrieval success rate | {{ai_retrieval_success}}% | ≥ {{ai_retrieval_target}}% | {{ai_retrieval_status}} | `./artifacts/ai_retrieval_metrics.csv` |
| Citation coverage | {{ai_citation_coverage}}% | ≥ {{ai_citation_target}}% | {{ai_citation_status}} | `./artifacts/ai_citation_metrics.csv` |
| Drift alerts | {{ai_drift_alerts}} | 0 | {{ai_drift_status}} | `./artifacts/ai_drift_report.md` |

---

## 🗺️ UI / map delivery signals (optional)

| Signal | Current | Target | Status | Evidence |
|---|---:|---:|:---:|---|
| Tile endpoint error rate | {{tile_error_rate}}% | ≤ {{tile_error_rate_target}}% | {{tile_error_status}} | `./artifacts/tiles_slo.csv` |
| Search latency (p95) | {{search_latency_p95}} ms | ≤ {{search_latency_target}} ms | {{search_latency_status}} | `./artifacts/search_latency.csv` |

---

## 🚨 Escalations, incidents, and tickets

### Issues created / linked 🧷
- `{{issue_1}}`
- `{{issue_2}}`

### Incident log (if applicable) 📟
- Incident ID: `{{incident_id}}`
- Timeline: `./artifacts/incident_timeline.md`
- Root cause: {{incident_root_cause_summary}}

---

## 🛠️ Remediation plan

| Priority | Task | Owner | Due | Status | Notes |
|---:|---|---|---|:---:|---|
| P0 | {{p0_task_1}} | {{owner_graph_ops}} | {{p0_due_1}} | {{p0_status_1}} | {{p0_note_1}} |
| P1 | {{p1_task_1}} | {{owner_data_steward}} | {{p1_due_1}} | {{p1_status_1}} | {{p1_note_1}} |
| P2 | {{p2_task_1}} | {{owner_ai_ops}} | {{p2_due_1}} | {{p2_status_1}} | {{p2_note_1}} |

---

## 📦 Artifacts

### Directory tree 🌲
```text
{{report_dir}}/
├─ summary.md
├─ index.csv
├─ artifacts.json
└─ artifacts/
   ├─ node_rel_counts.csv
   ├─ node_label_counts.csv
   ├─ rel_type_counts.csv
   ├─ constraints_and_indexes.csv
   ├─ orphans.csv
   ├─ ingestion_lag.csv
   ├─ hub_nodes.csv
   ├─ schema_drift.json
   ├─ policy_pack_results.json
   ├─ ai_retrieval_metrics.csv            (optional)
   ├─ ai_citation_metrics.csv             (optional)
   └─ backup/
      ├─ manifest.json
      ├─ restore_log.txt
      └─ restore_smoke_test.txt
```

### Artifact index 📇
- `./artifacts.json` should map artifact → producing check → checksum → source query/script.

---

## 🧷 Appendix A — Queries & scripts (examples)

> Replace these with your repo’s canonical query files (preferred) so the report is reproducible.

### Cypher: node & relationship totals (GH-001)
```cypher
// total nodes and relationships
MATCH (n) RETURN count(n) AS nodes_total;
MATCH ()-[r]->() RETURN count(r) AS rels_total;
```

### Cypher: constraints & indexes (GH-002)
```cypher
SHOW CONSTRAINTS;
SHOW INDEXES;
```

### Cypher: orphaned metadata patterns (GH-003)
```cypher
// Example orphan pattern (adjust labels/rel types to KFM ontology)
MATCH (i:StacItem)
WHERE NOT (i)-[:IN_COLLECTION|:BELONGS_TO|:PART_OF]->(:StacCollection)
RETURN i LIMIT 100;

// Example provenance orphan
MATCH (a:ProvActivity)
WHERE NOT (a)-[:USED]->() OR NOT (a)<-[:WAS_GENERATED_BY]-()
RETURN a LIMIT 100;
```

### PromQL: ingestion lag (GH-004) — optional
```text
# Example (adjust metric names)
max by (source) (time() - kfm_ingest_last_seen_timestamp_seconds)
```

### Backup smoke test (GH-007)
```text
1) Verify dump exists
2) Restore into disposable container
3) Run a basic query (e.g., nodes_total) and verify non-zero results
```

---

## 🧾 Appendix B — Thresholds & baselines

| Setting | Default | Rationale |
|---|---:|---|
| Count delta fail threshold | 5% | Coarse smoke test for duplication/dropouts |
| Ingestion SLA (warn) | 180 min | Example for frequently updating sources |
| Hub detection | Top 50 nodes | Focus on likely corruption fan-out |
| Schema drift cap | 0.5% | Catch accidental schema changes early |
| Orphan tolerance | {{orphans_tolerance}} | Depends on acceptable partial ingest |

---

## ✅ Definition of Done (DoD)

- [ ] Front matter fields populated (run_id, env, versions, period, owners)
- [ ] All GH-001..GH-007 executed (or explicitly marked N/A with reason)
- [ ] Each failing/warn check has: evidence link + interpretation + action + owner
- [ ] `index.csv` written/updated for trending
- [ ] Artifacts stored in `{{report_dir}}/artifacts/` and referenced here
- [ ] Escalation policy applied (issues created/linked where required)
- [ ] Report is PR-friendly (stable tables; minimal noise; meaningful diffs)

---

## 🗒️ Change log (template)

| Date (UTC) | Change | Author |
|---|---|---|
| {{changelog_date_1}} | {{changelog_change_1}} | {{changelog_author_1}} |
