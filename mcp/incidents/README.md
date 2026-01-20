<div align="center">

# 🚨 MCP Incidents

**Kansas Frontier Matrix (KFM) — incident command, runbooks, evidence packs, and postmortems** 🧭🗺️

`fail-closed` • `provenance-first` • `FAIR+CARE governed` • `GitOps rollback-ready` • `Focus Mode citation-enforced`

</div>

---

## 🎯 Overview

This folder is the **Master Coder Protocol (MCP)** incident system for KFM.

It’s where we:
- **Declare** incidents (platform, data, AI, governance, security, sustainability).
- **Track** response (timeline + status updates).
- **Capture evidence** (telemetry, logs, hashes, artifacts, provenance).
- **Recover** safely (rollback / quarantine / re-run with contracts).
- **Write postmortems** and **ship follow-ups** (policy updates, guardrails, tests, runbooks).

> **North Star:** If we can’t **reproduce** it, **prove** it, and **explain** it… we can’t truly “resolve” it.

---

## ✅ Golden Rules

### 1) “Fail closed” is not a bug 🧱
If a policy gate blocks a change (schema, license, sensitivity, provenance, Focus Mode citations), treat it as **a safety feature** and respond with **incident discipline**.

### 2) If it isn’t cited / provenanced… it isn’t shipped 🧾
Especially for **Focus Mode** outputs and any derived dataset/story content.

### 3) No secrets in Git 🔒
If **PII** or sensitive data ever lands in the repo: respond like a security spill (contain, revoke access, remove/purge, postmortem).

### 4) Automation must be stoppable 🛑
Watcher/Planner/Executor agents can help—but **humans own outcomes**. Always keep a **kill-switch** mindset.

---

## ⚡ Quickstart: What to do when something breaks

### Step 0 — Decide if this is an incident
Open an incident when any of the following is true:

- Users can’t access critical functionality (API/UI)  
- Data integrity / provenance / licensing is in question  
- Sensitive data exposure is possible  
- AI responses violate citation/safety rules  
- CI policy gates block releases/ingestion in a way that impacts availability  
- Energy/carbon budgets are exceeded in ways that threaten operations

### Step 1 — Declare
- Create an **incident record** using the template (below).
- Assign **Severity** (SEV0–SEV3).
- Assign roles: **IC**, **Scribe**, **Comms**, **Ops/SME**, **Governance Liaison** (as needed).

### Step 2 — Stabilize (“stop the bleed”)
Typical stabilizers:
- Flip a feature flag / disable a pipeline stage
- Roll back last known good release / data digest
- Quarantine a dataset
- Disable an agent automation path

### Step 3 — Capture evidence early (before it’s gone)
- Telemetry snapshots (include `run_id`, `config hash`, `env hash`, `trace ids`)
- CI outputs (policy gate logs)
- Repro steps + minimal failing example
- Checksums / artifact digests

### Step 4 — Communicate
- Post regular updates (even if “still investigating”)
- Be explicit about **impact** and **ETA uncertainty**
- For data governance issues: notify the **FAIR+CARE / ethics pathway** quickly

### Step 5 — Recover + Verify
- Restore service
- Validate correctness (schemas, SHACL, provenance completeness)
- Confirm no policy regressions

### Step 6 — Postmortem + follow-ups
- Blameless, evidence-backed
- Convert learnings into: tests, policies, lint rules, runbooks, dashboards

---

## 🧭 Incident Types

| Type | Examples | Typical “first containment” |
|---|---|---|
| 🛰️ Platform | API down, tiles broken, DB degraded | rollback + health checks + traffic shaping |
| 🧬 Data | corrupted geometry, wrong CRS, missing license/provenance | quarantine dataset + revert commit + re-run ETL |
| 🤖 AI / Focus Mode | uncited claim, hallucinated “validation result”, unsafe disclosure | block output + revert model/config + tighten policy |
| ⚖️ Governance | sensitive/cultural data mishandled, access control failure | revoke access + notify council + freeze publication |
| 🔐 Security | leaked token, unusual access patterns | rotate creds + restrict + audit + disclosure workflow |
| ♻️ Sustainability | runaway job, energy/carbon budget breach | throttle/disable job + enforce budgets |

> ⚠️ Note: “Incident” can also mean a *domain event dataset* (e.g., road incidents). This folder is for **operational incidents**. Domain “event records” live under the project’s **events** documentation patterns.

---

## 🚦 Severity & Escalation

| Severity | Meaning | Examples | Required actions |
|---|---|---|---|
| **SEV0** 🔥 | Catastrophic / security / irreversible risk | PII leak, sensitive locations exposed, total outage | immediate containment + council/security escalation + hourly updates |
| **SEV1** 🚨 | Major user impact or major integrity risk | ingestion halted, widespread incorrect layers, Focus Mode policy breach at scale | declare incident + frequent updates + postmortem required |
| **SEV2** ⚠️ | Partial impact / degraded service | slow tiles, one pipeline failing, high error rates | incident record + scheduled updates |
| **SEV3** 🧯 | Minor impact / near-miss | caught by policy gates, small regression, non-prod issue | incident record recommended + follow-up tasks |

---

## 🧑‍🚒 Roles (ICS-lite)

- **IC (Incident Commander)** 👩‍✈️  
  Owns coordination, scope, severity, and the “call” on rollback vs fix-forward.
- **Scribe** 📝  
  Maintains timeline, decisions, links, evidence list.
- **Comms Lead** 📣  
  Posts updates, keeps language clear, avoids speculation.
- **Ops / SME** 🛠️  
  Executes mitigations, narrows root cause, validates recovery.
- **Governance Liaison** ⚖️  
  Required for sensitive-data, cultural protocol, CARE framework incidents.

---

## 🧰 Directory Layout (recommended)

> You can start with just `README.md` + incident folders. Add templates/runbooks as the repo matures.

~~~text
mcp/incidents/
├── README.md                          # you are here 📍
├── templates/                         # 🧩 copy/paste starter docs
│   ├── incident.md
│   ├── status-update.md
│   └── postmortem.md
├── runbooks/                          # 🧯 scenario guides
│   ├── ci-policy-gate.md
│   ├── ingestion-pipeline.md
│   ├── focus-mode.md
│   ├── sensitive-data.md
│   ├── graph-neo4j.md
│   └── ui-map-rendering.md
└── incidents/
    └── 2026/
        └── INC-2026-01-20-001_example/
            ├── incident.md            # declaration + impact + owners
            ├── timeline.md            # timestamped actions + decisions
            ├── postmortem.md          # analysis + follow-ups
            └── artifacts/             # logs, exports, screenshots, hashes
                └── checksums.txt
~~~

---

## 🔎 Observability & Detection Signals

### Must-have correlation fields
Put these in logs/telemetry whenever possible:
- `incident_id`
- `run_id`
- `env_hash` / container digest
- `config_hash`
- `dataset_id` / `stac_item_id` / `dcat_id`
- `trace_id` / `span_id` (if using OpenTelemetry)
- `commit_sha` / `pr_number`

### Typical detection sources
- **Policy gates** (OPA/Conftest, schema lint, SHACL validation)
- **OpenTelemetry metrics** (latency, availability, end-to-end freshness SLOs)
- **Focus Mode telemetry** (citation coverage drift, policy violations)
- **Graph + DB telemetry** (Neo4j/PostGIS health, ingest lag)
- **UI budgets** (bundle size, time-to-interactive, map render errors)
- **Security signals** (unusual access patterns, rate spikes)
- **Energy/carbon telemetry** (runaway compute)

---

## 🧾 Evidence Pack (what every incident should capture)

### Minimum evidence checklist ✅
- [ ] The **exact failing artifact** (hash / digest)
- [ ] The **policy or contract** that failed (schema version / gate output)
- [ ] A **repro recipe** (inputs + steps)
- [ ] Logs (redacted as needed)
- [ ] Telemetry snapshot (with correlation IDs)
- [ ] “Last known good” reference (commit, digest, run_id)

### Provenance-first mindset
Treat incident artifacts like **Entities** in provenance:
- inputs → processing Activity → outputs  
- agents (humans, CI bots, W-P-E automation)  
This makes postmortems queryable and “evidence drawer” friendly.

---

## 🔁 Recovery Patterns (KFM-friendly)

### A) GitOps rollback (fastest)
- Revert the commit / PR that introduced the issue
- Re-deploy to sync external systems with repo truth
- Record: what was reverted, why, and what evidence justified it

### B) Quarantine + re-run (safest for data)
- Move/mark dataset as quarantined (classification/tag)
- Re-run deterministic ETL with pinned inputs/config/env
- Promote outputs only when policy gates pass

### C) Disable automation (stop repeats)
If a W-P-E agent created a problematic change:
- flip kill-switch / block further PRs
- tighten policy rules / approver requirements
- document the “why” for future operators

---

## 🤖 AI / Focus Mode Incident Guidance

Common triggers:
- Uncited claim
- “Invented” validation result
- Disclosure of sensitive information
- Drift in citation coverage or refusal behavior

First response:
- **Block output** (don’t “patch around” citation rules)
- Identify whether root cause is:
  - data/provenance missing,
  - retrieval failure,
  - model behavior change,
  - prompt/policy regression
- Roll back model/config if drift is confirmed
- Add policy/tests to prevent recurrence

---

## ⚖️ Governance & Sensitive Data

Some incidents require **extra rigor**:
- culturally sensitive sites
- endangered species locations
- PII / private addresses
- sensitive infrastructure

Default tactics:
- **generalize/aggregate** locations
- **tiered access** and tags
- **audit access patterns**
- council review before publication

---

## ♻️ Sustainability Guardrails

Incidents can be triggered by:
- runaway jobs
- excessive retries
- uncontrolled batch windows

Treat energy/carbon as first-class telemetry:
- enforce budgets
- throttle on error budgets
- capture energy/carbon in evidence packs

---

## 🧩 Templates (copy/paste)

<details>
<summary><strong>📄 Incident Record Template</strong> (incident.md)</summary>

~~~markdown
---
id: INC-YYYY-MM-DD-###        # stable ID
title: "Short, specific title"
status: declared|mitigating|monitoring|resolved
severity: SEV0|SEV1|SEV2|SEV3
start_time: "YYYY-MM-DDTHH:MM:SSZ"
end_time: null
owners:
  ic: "@handle"
  scribe: "@handle"
  comms: "@handle"
  ops: ["@handle"]
systems: ["api", "ui", "ingestion", "graph", "ci", "focus-mode"]
impact:
  users_affected: "who/how many"
  symptoms: ["bullet", "bullet"]
  scope_notes: "what is NOT impacted"
detection:
  signal: "alert|user report|policy gate|telemetry drift"
  first_seen: "YYYY-MM-DDTHH:MM:SSZ"
links:
  issue: ""
  pr_fixes: []
  dashboards: []
evidence:
  run_ids: []
  trace_ids: []
  commits: []
  artifacts: []
governance:
  sensitive_data_possible: false
  council_notified: false
---

## Summary
What happened?

## Current Status
What’s broken and what we’re doing now.

## Containment
What we did to stop the bleed.

## Next Actions
- [ ] …
- [ ] …

## Notes
Anything else useful for the postmortem.
~~~
</details>

<details>
<summary><strong>📣 Status Update Template</strong> (status-update.md)</summary>

~~~markdown
### Update — YYYY-MM-DD HH:MMZ
**Severity:** SEV?
**Status:** investigating|mitigating|monitoring|resolved  
**Impact:** who/what is affected  
**What we know:**  
- …  
**What we’re doing next:**  
- …  
**Next update:** in X minutes / after milestone Y
~~~
</details>

<details>
<summary><strong>🧠 Postmortem Template</strong> (postmortem.md)</summary>

~~~markdown
---
id: INC-YYYY-MM-DD-###
title: "Postmortem: …"
date: "YYYY-MM-DD"
severity: SEV?
owners:
  ic: "@handle"
  scribe: "@handle"
reviewers: ["@handle"]
---

## Executive Summary
1–3 paragraphs: impact + root cause + fix.

## Impact
- Users / systems affected
- Duration
- Data correctness notes (if applicable)

## Timeline (UTC)
| Time | Event |
|---|---|
| … | … |

## Root Cause
Primary cause + contributing factors.

## Detection & Response
- How we detected it
- What worked / didn’t work

## What Went Well ✅
- …

## What Didn’t Go Well ❌
- …

## Action Items 🧱
| Priority | Item | Owner | Due | Status |
|---:|---|---|---|---|
| P0 | … | … | … | … |

## Evidence Pack 🧾
- Telemetry run_ids:
- Trace IDs:
- Artifacts (hashes):
- Policy gate outputs:
- PRs/commits:
~~~
</details>

---

## 📚 Project Files Used (KFM documentation & research corpus)

<details>
<summary><strong>Open the list</strong> 📦</summary>

**Core KFM system docs**
- 📘 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- 📘 Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- 📘 Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- 📘 Kansas Frontier Matrix – Comprehensive UI System Overview
- 📘 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide
- 📘 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals
- 📘 Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)
- 📘 Pulse Ideas

**Repo + engineering references**
- 📗 Kansas-Frontier-Matrix Open-Source Geospatial Historical Mapping Hub Design
- 📙 Scientific Method _ Research _ Master Coder Protocol Documentation
- 📙 KFM- python-geospatial-analysis-cookbook (Nelson et al.)
- 📙 Data Mining Concepts & applications

**PDF Portfolios (open in Acrobat to browse the embedded sub-docs)**
- 🗂️ AI Concepts & more
- 🗂️ Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl
- 🗂️ Various programming langurages & resources 1
- 🗂️ Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas
</details>

---

## 🗺️ One-picture mental model (incident lifecycle)

~~~mermaid
flowchart TD
  A[Detect signal] --> B[Declare incident + set SEV]
  B --> C[Stabilize / Contain]
  C --> D[Capture evidence pack]
  D --> E[Mitigate + Recover]
  E --> F[Verify gates + correctness]
  F --> G[Resolve + Comms wrap-up]
  G --> H[Postmortem + follow-ups]
  H --> I[Policy/tests/runbooks updated]
~~~
