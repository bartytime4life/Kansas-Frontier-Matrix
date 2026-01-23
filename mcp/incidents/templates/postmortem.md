---
title: "POSTMORTEM — {{incident_title}}"
doc_kind: "Incident Postmortem"
incident_id: "{{INC-YYYYMMDD-###}}"
status: "draft" # draft | in_review | published | archived
severity: "SEV-?" # SEV-0 | SEV-1 | SEV-2 | SEV-3 | SEV-4
timezone: "UTC"
start_time_utc: "YYYY-MM-DDTHH:MM:SSZ"
detected_time_utc: "YYYY-MM-DDTHH:MM:SSZ"
mitigated_time_utc: "YYYY-MM-DDTHH:MM:SSZ"
resolved_time_utc: "YYYY-MM-DDTHH:MM:SSZ"
duration_minutes: 0

owners:
  incident_commander: "{{name}}"
  scribe: "{{name}}"
  primary_oncall: "{{name}}"
  engineering_owner: "{{team_or_person}}"
  governance_owner: "{{team_or_person}}"

components_impacted:
  # Examples: kfm/ui, kfm/api, kfm/pipelines, kfm/graph, kfm/search, kfm/ai, kfm/governance, kfm/registry, kfm/observability
  - "{{component}}"

customer_facing: true
data_classification: "internal" # public | internal | restricted | sensitive
care_label: "Public" # Public | Sensitive—Blurred | Restricted—Approval Needed | {{custom}}

governance:
  policy_pack_version: "{{v13}}"
  conftest_run_url: ""
  rego_rules_triggered: []
  fair_care_flags: [] # e.g., ["IndigenousDataSovereignty", "SensitiveLocation", "PII"]

evidence:
  run_ids: []              # pipeline run IDs
  correlation_ids: []      # request / trace IDs
  run_manifests: []        # e.g., data/audits/{{run_id}}/run_manifest.json
  evidence_manifests: []   # e.g., data/audits/{{run_id}}/evidence_manifest.json
  prov_records: []         # e.g., prov/{{id}}.jsonld
  stac_assets: []          # STAC Item/Collection IDs or paths
  dcat_datasets: []        # DCAT dataset IDs or paths
  oci_artifacts: []        # digests/tags for PMTiles/COGs/models; include cosign verify evidence
  dashboards: []           # links/screenshots
  logs: []                 # log queries, exports, snippets, etc.

related_links:
  incident_issue: ""
  pull_requests: []
  deployments: []
  comms: []                # status posts, announcements, emails, etc.

# Optional: if you publish this postmortem
license: "CC-BY-4.0"
last_updated_utc: "YYYY-MM-DDTHH:MM:SSZ"
---

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Severity](https://img.shields.io/badge/severity-SEV--%3F-lightgrey)
![Scope](https://img.shields.io/badge/scope-KFM%20%2F%20MCP-blue)
![Mode](https://img.shields.io/badge/postmortem-blameless-success)

# 📛 Postmortem: {{incident_title}}

> 🧠 **Blameless + evidence-first**
>
> - Focus on *system behavior* and *decision context*, not individual fault.
> - Link every key claim to **evidence** (dashboards, logs, run manifests, commits, dataset IDs).
> - If the incident touched **sensitive data**, treat this as a **governance + safety** event first.

---

## 🧭 Quick Start

### 📁 Where this file lives
```text
📁 mcp/
  📁 incidents/
    📁 YYYY/
      📄 {{incident_id}}-{{short_slug}}.md
    📁 templates/
      ✅ postmortem.md   (this template)
```

### ✅ How to use
1. **Copy** this template into a new incident file (see folder layout above).
2. Replace all `{{placeholders}}`.
3. Attach or link an **Evidence Pack** (run manifests, policy gate results, dashboards).
4. Convert Action Items into **GitHub issues** (or tracked tasks) and link them below.
5. Mark `status: in_review` → `published` when approved.

---

## 🧯 Severity Ladder (tune this to your team)

> Tip: In KFM, **data integrity**, **provenance**, and **CARE / sensitivity handling** can be as critical as uptime.

| Severity | Definition (rule of thumb) | Examples |
|---|---|---|
| **SEV-0** 🚨 | Safety, privacy, or governance breach; *or* confirmed tampering/supply-chain compromise | PII exposed, sensitive site coordinates leaked, Cosign verification bypassed, policy fails open |
| **SEV-1** 🔥 | Major outage or widespread incorrect results; core platform unusable | API down, map tiles unavailable platform-wide, graph corruption affecting most queries |
| **SEV-2** ⚠️ | Significant feature degradation or partial incorrectness with meaningful user impact | Search broken, one major layer wrong/stale, Focus Mode returning uncited/low-quality answers |
| **SEV-3** 🛠️ | Limited impact or narrow blast radius; workaround exists | One story node broken, one dataset ingestion failed, localized performance regression |
| **SEV-4** 🧹 | Cosmetic or low-risk; no meaningful impact | Minor UI bug, typo in metadata caught before publish |

### 🏷️ Incident type tags (select)
- ☐ Availability / outage  
- ☐ Performance / latency  
- ☐ Data integrity (wrong/stale/missing)  
- ☐ Provenance / metadata integrity (STAC/DCAT/PROV)  
- ☐ Knowledge graph integrity (constraints/indexes/drift)  
- ☐ Governance / policy (OPA/Rego/Conftest)  
- ☐ Security / privacy / sensitive locations  
- ☐ AI quality / citations / drift  
- ☐ Collaboration / moderation / community content  
- ☐ Other: {{...}}

---

## 🧾 Executive Summary (non-technical) 🗞️

**What happened?**  
{{2–4 sentences in plain language.}}

**Customer / user impact**  
{{Who was impacted, what they experienced, and how they discovered it.}}

**Root cause (one-liner)**  
{{Primary root cause in one sentence.}}

**Fix (one-liner)**  
{{What permanently prevents recurrence (or what’s underway).}}

---

## 🎯 Impact

### 👥 User impact
- **Surfaces affected:** ☐ 2D Map ☐ 3D Globe/Terrain ☐ Timeline ☐ Story Nodes ☐ Search ☐ Focus Mode (AI) ☐ Offline Packs ☐ Dashboards/Simulations ☐ Exports/Sharing
- **Symptoms:** {{errors, stale data, missing layers, wrong answers, slow UI, etc.}}
- **Duration:** {{minutes/hours}} (from {{start_time}} to {{end_time}} UTC)
- **Severity justification:** {{why this is SEV-?}}

### 🧱 System impact (choose all that apply)
KFM flows are often: **Raw Data → ETL Pipelines → Knowledge Graph/DB → Web Platform (Map+Timeline+Stories) → Focus Mode (AI) → Governance & Telemetry**

| Layer | Examples | Impacted? |
|---|---|:---:|
| 🗃️ Data Intake (ETL) | ingest → validate → transform → publish | ☐ |
| 🧾 Metadata & Provenance | STAC / DCAT / PROV completeness | ☐ |
| 🕸 Knowledge Graph | Neo4j nodes/edges, constraints, indexes | ☐ |
| 🔎 Search | full-text index (e.g., Elasticsearch), embeddings index | ☐ |
| 🔌 API | REST / GraphQL, auth, tiles, time-series endpoints | ☐ |
| 🗺️ UI | React app, MapLibre/Cesium, story renderer | ☐ |
| 🤖 Focus Mode (AI) | RAG retrieval → LLM → governance check → citations | ☐ |
| ⚖ Policy/Governance | OPA/Rego + Conftest, FAIR+CARE enforcement | ☐ |
| 📦 Artifacts | OCI registry, digests, Cosign signatures | ☐ |
| 📈 Observability | telemetry, correlation IDs, dashboards, alerts | ☐ |

### 🧬 Data integrity impact
- **Was incorrect data served?** ☐ No ☐ Yes (details below)
- **Blast radius:** {{datasets/layers/regions/time ranges affected}}
- **Provenance integrity:** ☐ intact ☐ partial ☐ broken  
  - {{e.g., missing PROV activity; wrong STAC asset link; mis-tagged dataset}}
- **Graph integrity:** ☐ intact ☐ drift detected ☐ corruption suspected  
  - {{e.g., constraint violations, orphaned metadata nodes, unexpected deltas}}
- **Rollback required?** ☐ No ☐ Yes → see **Rollback & Recovery**

### 🛡️ Security / privacy / CARE impact (high priority)
- **Sensitive coordinates or protected locations exposed?** ☐ No ☐ Yes
- **PII or secrets committed/served?** ☐ No ☐ Yes
- **CARE / cultural protocol implications?** ☐ No ☐ Yes
- **Immediate containment actions taken:**  
  - ☐ flipped classification to restrict access  
  - ☐ removed / purged offending artifacts  
  - ☐ notified governance council / data stewards  
  - ☐ added/updated policy gate (Rego/Conftest)  
  - ☐ published a public notice (if appropriate)

---

## 🔎 Detection & Response

### 🚨 How was it detected?
- ☐ Alert (metrics / logs)  
- ☐ Weekly Graph Health Check flagged drift  
- ☐ Drift monitoring / citation coverage alert (AI)  
- ☐ User report  
- ☐ Maintainer noticed manually  
- ☐ CI / Policy Gate failure (fail-closed)  
- ☐ Other: {{...}}

**Detection signal (link evidence):** {{dashboard/log query/issue link}}

### 🧑‍🚒 Roles
- **Incident Commander (IC):** {{name}}
- **Scribe:** {{name}}
- **Tech Lead:** {{name}}
- **Comms Lead:** {{name}}
- **Governance / Data Steward:** {{name}}

### 📣 Communications
- **Internal channel:** {{slack/discord/thread link}}
- **External status update:** {{status page / post link}}
- **User-facing note embedded in UI (if any):** {{link/screenshot}}
- **Pulse Thread / narrative update (optional):** {{link}}  
  *(Use when an incident has a meaningful spatial + temporal “story,” and attach evidence manifest.)*

---

## 🕓 Timeline (UTC)

> Tip: include **run_id** and **correlation_id** wherever possible so the event stream is auditable.

| Time (UTC) | Event | Owner | Evidence |
|---|---|---|---|
| {{YYYY-MM-DD HH:MM}} | Incident started (or first bad deploy) | {{name}} | {{link}} |
| {{...}} | Detection | {{name}} | {{link}} |
| {{...}} | Mitigation applied | {{name}} | {{link}} |
| {{...}} | Full resolution confirmed | {{name}} | {{link}} |

---

## 🧠 Root Cause Analysis (RCA)

### 🎯 What was the primary root cause?
{{Explain in concrete technical terms.}}

### 🧩 Contributing factors
- {{Factor 1}}
- {{Factor 2}}
- {{Factor 3}}

### 🔬 “5 Whys” (optional but recommended)
1. **Why did users see the issue?** → {{...}}
2. **Why did the system behave that way?** → {{...}}
3. **Why was that condition possible?** → {{...}}
4. **Why wasn’t it prevented by policy/tests/monitoring?** → {{...}}
5. **Why was that gap present?** → {{...}}

### 🧾 What changed? (diff-based)
- **Code change(s):** {{PR/commit links}}
- **Data change(s):** {{dataset IDs, STAC/DCAT paths, commit links}}
- **Config change(s):** {{env/config diffs}}
- **Artifact change(s):** {{OCI tag/digest changes}}
- **Policy change(s):** {{Rego rule IDs / Conftest output}}

---

## 🩹 Mitigation, Resolution, and Recovery

### 🚑 Immediate mitigation (stop the bleeding)
- ☐ Roll back deployment  
- ☐ Disable automation (Watcher/Planner/Executor kill-switch)  
- ☐ Flip dataset classification to restrict access  
- ☐ Disable a problematic layer/story/feature flag  
- ☐ Rate-limit / backpressure ingestion watcher  
- ☐ Hotfix in API  
- ☐ Cache purge / CDN invalidation  
- ☐ Other: {{...}}

### 🔁 Rollback & recovery details (GitOps + data as source of truth)
If rollback was used, document **exactly** what was reverted and how external stores were reconciled.

- **Git revert:** {{commit(s)}}  
- **Graph rollback:** {{CSV snapshot restore / migration rollback / Cypher cleanup}}  
- **Data rollback:** {{revert data files, re-run pipelines to resync PostGIS/Neo4j}}  
- **Sensitive data emergency procedure (if applicable):**  
  - ☐ revoke public access immediately  
  - ☐ remove files and purge from history if required  
  - ☐ council notification + postmortem + new policy rule

### ✅ Verification (proof we’re actually fixed)
- **Checks performed:** {{queries, smoke tests, e2e tests}}
- **Dashboards stable for:** {{N hours}}
- **Graph Health Check results:** {{pass/fail + link}}
- **AI answer quality:** {{citation coverage %, drift metrics, eval suite link}}
- **User confirmation:** ☐ No ☐ Yes (details)

---

## 🧾 Evidence Pack (audit trail)

> Goal: someone should be able to **replay** the incident path or validate claims without guesswork.

### 📌 Required evidence (minimum)
- **Run manifest(s):** {{paths/links}}  
  Example path: `data/audits/{{run_id}}/run_manifest.json`
- **Evidence manifest(s):** {{paths/links}}  
  *(Include dataset IDs, query params, timestamps, tool versions.)*
- **Policy gate output:** {{Conftest/OPA logs, rule IDs}}
- **Deployment artifacts:** {{image tags, digests, env config}}
- **Logs & traces:** {{log queries; correlation IDs}}
- **Dashboards:** {{links/screenshots}}

### 📦 Artifact integrity (OCI + signatures)
| Artifact | Tag | Digest | Cosign verified? | Evidence |
|---|---|---|:---:|---|
| {{pmtiles/cog/model}} | {{tag}} | `sha256:...` | ☐ | {{link}} |

### 🧬 Provenance pointers
- **PROV record(s):** {{prov JSON-LD}}
- **STAC item(s)/collection(s):** {{IDs/paths}}
- **DCAT dataset(s):** {{IDs/paths}}

---

## ⚖️ Governance & Policy Analysis

### ✅ Which gates worked?
- ☐ Schema validation  
- ☐ STAC/DCAT/PROV completeness  
- ☐ License present  
- ☐ Sensitivity classification enforced  
- ☐ Provenance-first publishing  
- ☐ AI citation requirement enforced  
- ☐ Supply chain verification (Cosign)  
- ☐ Other: {{...}}

### ❌ Which gates failed (or were missing)?
- {{Gate that didn’t exist / didn’t fire / had loophole}}
- {{Why it didn’t catch the issue}}

### 🔐 CARE / sensitivity handling (if relevant)
- **Was geo-obfuscation required?** ☐ No ☐ Yes (describe approach)  
- **Were cultural protocols / TK labels involved?** ☐ No ☐ Yes  
- **Was differential access applied by role?** ☐ No ☐ Yes

### 🧯 Policy changes proposed
- **New/updated Rego rule(s):** {{IDs + summary}}
- **Fail-closed behavior confirmed?** ☐ Yes ☐ No
- **Reviewers required:** {{data steward / governance council / security}}

---

## 📈 Observability & Monitoring Gaps

> KFM emphasizes telemetry with **run identifiers**, **configuration hashes**, and **correlation IDs**.

### 📊 What metrics/alerts fired?
- {{alert name}} — {{threshold}} — {{link}}
- {{...}}

### 🕳️ What was missing?
- {{missing metric}}
- {{missing log field (e.g., run_id not propagated)}}
- {{missing dashboard}}
- {{missing health check}}

### 🛠️ Monitoring improvements
- {{new alert}}  
- {{new dashboard}}  
- {{add run_id/correlation_id propagation}}  

---

## 🧪 Testing & QA Improvements ✅

> Treat tests like guardrails: unit → integration → end-to-end → policy gates.

- **Unit tests to add:** {{...}}
- **Integration tests to add:** {{...}}
- **E2E tests to add (UI/API):** {{...}}
- **Data validation tests:** {{schema, distributions, invariants}}
- **Determinism / reproducibility:**  
  - ☐ seed set / recorded  
  - ☐ tool versions captured  
  - ☐ run context serialized  
  - ☐ replay confirmed

---

## 🤖 Focus Mode / AI-Specific Section (fill only if relevant)

<details>
<summary><strong>Open AI incident checklist 🤖</strong></summary>

### 🧠 What failed?
- ☐ Retrieval (graph/search) returned wrong/empty context  
- ☐ LLM generation hallucinated / mis-cited  
- ☐ Governance check failed open (should fail closed)  
- ☐ Prompt security issue (injection/jailbreak)  
- ☐ Drift detected (accuracy down / citation coverage down)  
- ☐ Performance/latency regression  
- ☐ Other: {{...}}

### 📏 Quality signals
- **Citation coverage:** {{%}}
- **Eval suite link:** {{...}}
- **User feedback signal:** {{...}}

### 🛡 Prompt security notes
- **Input pattern:** {{...}}
- **Blocked/allowed outcome:** {{...}}
- **Rule/policy updates:** {{...}}

</details>

---

## 🕸 Graph Integrity Section (fill only if relevant)

<details>
<summary><strong>Open graph health checklist 🕸</strong></summary>

Weekly checks often include:
- ☐ Node & relationship count deltas (unexpected jumps/drops)  
- ☐ Constraint & index integrity (online/valid)  
- ☐ Orphaned metadata / broken lineage links  
- ☐ Schema drift detection  
- ☐ Performance regressions on key Cypher queries  

**Findings:** {{...}}  
**Evidence:** {{link}}  

</details>

---

## 🌱 What Went Well / What Didn’t / Where We Got Lucky

### ✅ What went well
- {{...}}

### ❌ What didn’t go well
- {{...}}

### 🍀 Where we got lucky
- {{...}}

---

## 🧯 Action Items (CAPA)

> Prefer “systemic” items: policy gates, tests, monitoring, safer defaults, better runbooks.

| ID | Action | Type (Prevent/Detect/Mitigate) | Owner | Due | Status | Link |
|---:|---|---|---|---|---|---|
| A1 | {{...}} | Prevent | {{name}} | {{YYYY-MM-DD}} | ☐ | {{issue}} |
| A2 | {{...}} | Detect | {{name}} | {{YYYY-MM-DD}} | ☐ | {{issue}} |
| A3 | {{...}} | Mitigate | {{name}} | {{YYYY-MM-DD}} | ☐ | {{issue}} |

---

## 📚 Documentation / Runbooks Updated

- ☐ Runbook updated: {{link}}
- ☐ SOP updated: {{link}}
- ☐ Glossary updated (if terms were ambiguous): {{link}}
- ☐ Story / narrative updated (if user-facing): {{link}}

---

## ✅ Definition of Done (DoD) 🧾

Before marking `status: published`, ensure:

- [ ] Front-matter complete (IDs, times, severity, owners, classification)  
- [ ] Executive summary is understandable by non-technical readers  
- [ ] Timeline has evidence links and includes run_id/correlation_id where possible  
- [ ] Root cause + contributing factors documented (not just “human error”)  
- [ ] Evidence Pack linked (run manifests, policy output, dashboards, logs)  
- [ ] Security/CARE section completed (even if “N/A”)  
- [ ] At least 1 **policy** improvement or justification why not needed  
- [ ] At least 1 **test** improvement or justification why not needed  
- [ ] At least 1 **monitoring** improvement or justification why not needed  
- [ ] Action items converted into tracked issues with owners and due dates  
- [ ] Review completed by Engineering + Governance/Data Steward (as applicable)

---

## 📎 Appendix

### 🔗 Handy links
- Incident issue: {{...}}
- PRs: {{...}}
- Deployments: {{...}}
- Dashboards: {{...}}
- Logs/traces: {{...}}

### 🗒️ Notes / transcript
{{Paste or link to key notes, meeting logs, or chat transcript.}}
