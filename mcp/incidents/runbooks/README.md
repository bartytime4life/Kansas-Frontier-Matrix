---
kfm_mdp: "v11.2.6"
doc_type: "readme"
doc_stage: "foundation"
doc_status: "draft"
doc_scope: "mcp.incidents.runbooks"
doc_version: "0.1.0"
doc_uuid: "0d9a0c6e-6a2e-4e4d-9a72-2e61e6c0f0c5"
semantic_document_id: "kfm.mcp.incidents.runbooks.readme"
title: "🧯 Incident Runbooks (MCP)"
description: "Operational runbooks for responding to KFM incidents with evidence-first, provenance-first, fail-closed governance."
owners:
  - "KFM Maintainers"
  - "MCP Ops"
classification: "public"
license: "MIT"
tags:
  - "incidents"
  - "runbooks"
  - "sre"
  - "security"
  - "data-governance"
  - "telemetry"
  - "provenance"
---

# 🧯 Incident Runbooks (MCP)

![Status](https://img.shields.io/badge/status-draft-yellow)
![Ops](https://img.shields.io/badge/ops-evidence--first-blue)
![Governance](https://img.shields.io/badge/governance-fail--closed-red)
![Provenance](https://img.shields.io/badge/provenance-PROV%20%2B%20receipts-brightgreen)

Welcome to the **KFM incident runbook library** — a practical, repeatable way to respond to outages, data integrity issues, security events, and AI/pipeline anomalies **without breaking provenance**.

KFM’s golden rule applies here too: **no black boxes**. Every action is logged, reversible when possible, and traceable to evidence.

---

## 🧭 What “Runbooks” Mean in KFM

A **runbook** is a step-by-step operational guide that:
- ✅ gets the system stable (containment)  
- ✅ restores service safely (recovery)  
- ✅ preserves evidence & lineage (provenance)  
- ✅ produces a postmortem + hardening tasks (prevention)

In KFM, runbooks are **GitOps-friendly**:
- Prefer **PR-first** fixes for code/config/data changes.
- Prefer **idempotent** remediation steps (safe to re-run).
- Prefer **fail-closed** gates when safety or integrity is uncertain.

---

## 📦 Directory Layout

```text
mcp/
└─ incidents/ 🧯
   ├─ runbooks/ 📒
   │  ├─ README.md ✅ (you are here)
   │  ├─ TEMPLATE_runbook.md 🧩
   │  ├─ catalog/ 🛰️
   │  ├─ graph/ 🕸️
   │  ├─ api/ 🚪
   │  ├─ ui/ 🗺️
   │  ├─ pipelines/ 🧰
   │  ├─ security/ 🛡️
   │  ├─ ai/ 🤖
   │  └─ infra/ 🏗️
   └─ (incident_cases)/ 🧾  ← created per incident (see “Incident Workspace”)
```

> 🔒 **Rule:** Runbooks live here. **Incident-specific evidence and notes do not** — they go into an incident workspace folder (tracked, timestamped, hashed).

---

## ⚡ Quickstart: When an Incident Hits

1. **Create an incident workspace**  
   - Create a new folder (example): `mcp/incidents/incident_cases/INC-YYYYMMDD-###/`
2. **Assign roles** (even if it’s “just you” — name the hat you’re wearing)
3. **Pick the closest runbook** from this directory and follow it
4. **Open an evidence log** (append-only) and start capturing:
   - what you saw
   - when it happened (UTC + local)
   - what you changed
   - what you verified
5. **Stabilize → Recover → Verify → Document → Prevent**

---

## 🎭 Standard Incident Roles (Lightweight)

| Role | Emoji | Responsibilities |
|---|---:|---|
| Incident Commander (IC) | 🎛️ | owns coordination, severity, stop/go decisions |
| Operations Lead | 🧰 | executes technical steps, tracks changes |
| Scribe | 📝 | keeps the log tight: timestamps + evidence + decisions |
| Comms | 📣 | internal/external updates, status page, release notes |
| SME | 🧠 | domain expert (graph, PostGIS, pipelines, AI, security, etc.) |

> 🧠 Tip: Even solo incidents benefit from “IC vs Ops vs Scribe” separation (prevents tunnel vision).

---

## 🚦Severity Model (Default)

| Severity | Label | Definition | Target cadence |
|---|---|---|---|
| Sev0 | 🔥 Critical | safety/security risk OR widespread outage OR data integrity compromised | updates every 15 min |
| Sev1 | 🚨 Major | core functionality degraded, limited blast radius | updates every 30 min |
| Sev2 | ⚠️ Minor | partial feature impact, workaround exists | updates hourly |
| Sev3 | 🧊 Low | nuisance, cosmetic, or non-urgent | daily / async |

> If provenance or integrity is uncertain: **escalate severity** until verified.

---

## 🧾 Incident Workspace (Required)

Each incident gets a workspace folder containing **only** incident-specific artifacts.

**Recommended structure:**
```text
INC-YYYYMMDD-###/
├─ 00_meta/ 🧷
│  ├─ incident.yaml
│  └─ timeline.md
├─ 10_evidence/ 🔍
│  ├─ logs/
│  ├─ screenshots/
│  ├─ queries/
│  └─ hashes.sha256
├─ 20_actions/ 🧰
│  ├─ commands.md
│  ├─ diffs/
│  └─ rollback.md
├─ 30_verification/ ✅
│  ├─ checks.md
│  └─ metrics.md
└─ 90_postmortem/ 🧠
   ├─ postmortem.md
   └─ action_items.md
```

### Evidence rules
- 🧷 **Append-only** where possible (timeline, evidence notes).
- 🔐 Hash files you collect (`sha256`) and record hashes in `hashes.sha256`.
- 🧾 Prefer saving raw outputs (logs/queries) **instead of paraphrasing**.
- 🧭 If a runbook step changes system state, record:
  - actor (who/what ran it)
  - command or PR link
  - pre/post verification results

---

## 🧬 Provenance & Governance Expectations

Runbooks must respect KFM’s pipeline spine and trust boundaries:
- **No UI direct-to-DB** shortcuts (UI goes through the governed API).
- **No “mystery fixes”** (manual edits without receipts).
- **No bypassing policy gates** without a documented exception trail.
- Prefer **PR-first** for:
  - schema changes
  - metadata fixes
  - policy changes
  - pipeline code changes
  - config changes

### ✅ “Fail-Closed” default
If a runbook cannot prove safety/integrity:
- contain first (disable, isolate, restrict)
- restore only after verification
- keep evidence for later analysis

---

## 🧩 Runbook Standard (Required Sections)

Every runbook file in this directory should include:

1. **Summary** (what it covers + when to use)
2. **Signals / Detection** (alerts, symptoms, dashboards, logs)
3. **Impact / Blast Radius** (what breaks, who is affected)
4. **Immediate Safety Checks** (data integrity, secrets, sensitive layers)
5. **Triage Checklist** (fast, deterministic checks)
6. **Containment Steps** (stop the bleeding)
7. **Recovery Steps** (restore service safely)
8. **Verification Steps** (prove it’s actually fixed)
9. **Rollback Plan** (how to undo)
10. **Evidence Capture** (minimum artifacts)
11. **Comms Template** (internal/external)
12. **Postmortem Trigger** (when required + how to write)
13. **Hardening Tasks** (prevention: tests, monitors, policy updates)

---

## 🧩 Runbook Template

Create new runbooks by copying:

- `TEMPLATE_runbook.md 🧩`

Naming convention (suggested):
- `RBK-<domain>-<slug>.md`  
  Examples:
  - `RBK-api-5xx-spike.md`
  - `RBK-graph-orphaned-prov.md`
  - `RBK-catalog-schema-validation-fail.md`
  - `RBK-security-secret-exposed.md`
  - `RBK-ai-citations-missing.md`

---

## 📒 Index: Core Runbook Topics (Seed Set)

> These are **recommended** runbooks to maintain as the minimum viable set.

### 🚪 API / Services
- API outage / 5xx spike
- Slow queries (PostGIS or graph)
- Auth/role regression (if enabled)
- Rate limit / abuse event

### 🛰️ Catalog / Metadata
- STAC/DCAT/PROV validation failures
- Missing license / missing sensitivity label
- Broken asset links / checksum mismatch
- “Mystery dataset” detection (catalog exists without provenance)

### 🕸️ Graph / Neo4j
- Orphaned nodes (items without parents, prov without edges)
- Constraint/index not online
- Node/relationship count anomalies
- Backup verification failure

### 🧰 Pipelines / Intake
- Watcher stuck / ingestion lag
- ETag/Last-Modified mismatch loops
- Partial pipeline write / non-atomic publish
- Determinism drift (same inputs, different outputs)

### 🤖 AI / Focus Mode
- Missing citations (policy failure)
- Prompt injection attempts (input gate triggers)
- Retrieval failures (graph/index outages)
- Drift/bias alarms (evaluation suite triggers)

### 🛡️ Security
- Secret exposure / credential leak
- Supply-chain / dependency compromise
- Unauthorized data access attempt
- Sensitive layer exposure / redaction failure

### 🗺️ UI
- Layer registry mismatch (layer present but not loadable)
- Timeline desync (time-enabled layers wrong)
- Story Node render failures
- Accessibility regressions (critical UI controls inaccessible)

---

## 🧠 Incident Flow (Mermaid)

```mermaid
flowchart TD
  A[🚨 Detect Signal] --> B[🎛️ Declare Incident + Severity]
  B --> C[🧾 Create Incident Workspace]
  C --> D[🧰 Triage + Evidence Capture]
  D --> E{🔒 Safety/Integrity Risk?}
  E -- Yes --> F[🧯 Contain (Fail-Closed)]
  E -- No --> G[🛠️ Stabilize + Recover]
  F --> G
  G --> H[✅ Verify + Monitor]
  H --> I[📝 Postmortem + Action Items]
  I --> J[🧱 Hardening: tests, monitors, policy updates]
```

---

## 📣 Comms: Minimal Update Template

Use this in the incident workspace (and adapt as needed):

- **Status:** Investigating / Identified / Mitigating / Monitoring / Resolved  
- **Impact:** who/what is affected  
- **Start time:**  
- **Current hypothesis:** (keep short)  
- **Actions taken:** (bullet list, with links to evidence/PRs)  
- **Next update:** (time)  

---

## ✅ Definition of “Resolved” (KFM Standard)

An incident is **Resolved** only when:
- root cause is understood (even if partial)
- service is stable (measured, not vibes)
- integrity checks pass (catalog + provenance + access rules)
- rollback plan exists for the shipped fix
- postmortem is created (if required) and action items are tracked

---

## 🔧 Contributing Runbooks

1. Copy `TEMPLATE_runbook.md`
2. Keep steps **deterministic** and **idempotent**
3. Embed commands as code blocks and specify *where they run* (local, CI, container, prod)
4. Include explicit verification checks (what “good” looks like)
5. Prefer links to:
   - contracts/schemas
   - policy gates
   - telemetry conventions
6. Submit via PR (runbooks are production infrastructure)

---

## 🧷 Related (Recommended Reading)

- 📥 Data intake & pipeline spine (raw → work → processed → catalogs → graph → API → UI → AI)
- 🧭 AI governance (citations required, prompt gates, policy checks)
- 🗺 UI provenance surfacing (layer provenance panels, sensitivity labels)
- 🕸 Graph health & provenance integrity checks
- ⚙ Watcher–Planner–Executor (automation with PR-first execution)

---

## ✅ Next TODOs (Repo Hygiene)

- [ ] Add `TEMPLATE_runbook.md` (if not already present)
- [ ] Create first seed runbooks under `catalog/`, `graph/`, `security/`, `pipelines/`, `ai/`
- [ ] Add a top-level `mcp/incidents/README.md` that explains incident case storage + postmortems
- [ ] Add CI lint for runbook front-matter + required sections
