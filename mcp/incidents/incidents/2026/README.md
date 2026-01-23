# 🚨 KFM Incident Register — 2026

![Year](https://img.shields.io/badge/year-2026-blue)
![Scope](https://img.shields.io/badge/scope-KFM%20%E2%80%A2%20MCP%20Incidents-purple)
![Principles](https://img.shields.io/badge/principles-evidence--first%20%2B%20provenance--first-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest%20%E2%80%A2%20fail--closed-red)

> 📌 **Purpose:** This folder is the **canonical, audit-friendly incident record** for the Kansas Frontier Matrix (KFM) for calendar year **2026**.  
> 🧾 **Mindset:** Evidence-first, provenance-first, and “no mystery layers” — if it impacted users, data integrity, governance, or trust, it belongs here.

⬅️ **Back:** [Incidents Home](../README.md)

---

## 📅 2026 Incident Index

> Add a row **as soon as you declare** an incident (even if details come later). Keep the title short + searchable.

| ID | Date (UTC) | Sev | Title | Status | Components | Links |
|---:|:----------:|:---:|:------|:------:|:----------|:------|
| — | — | — | _No incidents logged yet_ | — | — | — |

**Status legend:** `open` · `monitoring` · `resolved` · `closed (postmortem complete)`

---

## 🧭 What counts as an incident in KFM?

KFM incidents include any event that materially impacts:

- 🧩 **Trust & provenance** (broken STAC/DCAT/PROV linkage, missing lineage, “mystery layer” behavior)
- 🗺️ **UI correctness** (layers mismatched, time slider wrong, map rendering failures, offline packs stale)
- 🧠 **AI correctness / governance** (Focus Mode mis-citations, drift/bias alarms, prompt-security violations)
- 🧱 **Data integrity** (bad ingestion, schema drift, graph corruption, PostGIS inconsistencies)
- 🛡️ **Security / privacy / CARE** (sensitive data exposure, policy bypass, access-control failures)
- 📉 **Performance & availability** (API outages, tile bottlenecks, ingestion lag beyond agreed thresholds)

If it risks **user harm** or **loss of trust**, treat it as an incident — even if uptime is fine.

---

## 🗂️ Folder & naming standard

Each incident is a **folder** (append-only record). Use:

📁 `YYYY-MM-DD--short-slug--INC-2026-###/`

Example (placeholder):

```
📁 mcp/incidents/incidents/2026/
  📄 README.md
  📁 2026-01-18--tile-cache-regression--INC-2026-001/
    📄 INCIDENT.md
    📄 timeline.md
    📄 rca.md
    📄 action_items.md
    📁 evidence/
      📄 evidence_manifest.md
      📄 telemetry_excerpt.ndjson
      📄 prov_bundle.json
      📄 stac_snapshot.json
      📄 dcat_snapshot.json
      📄 graph_healthcheck_report.json
    📁 artifacts/
      📄 repro_steps.md
      📄 patch.diff
      📄 screenshots/
```

### ✅ Required files

- `INCIDENT.md` — single-page summary + impact + current status
- `timeline.md` — timestamps, who did what, what changed
- `rca.md` — root cause analysis (blameless, evidence-based)
- `action_items.md` — tracked remediations (with owners + due dates)
- `evidence/` — “show your work” artifacts and snapshots (see below)

---

## ✍️ Quickstart: declare a new incident

1. **Create the folder** with the naming standard.
2. Add the **index row** in this README.
3. Create `INCIDENT.md` using the template below.
4. Add a minimal `timeline.md` (start with detection → current).
5. Drop the first evidence into `evidence/` (even if incomplete).

> ⚠️ Don’t wait for perfect RCA. Declare early, document continuously.

---

## 🧾 Template: `INCIDENT.md`

Copy/paste and fill:

```markdown
---
incident_id: INC-2026-___
title: "Short, searchable title"
status: open  # open | monitoring | resolved | closed
severity: P2  # P0 | P1 | P2 | P3
start_time_utc: "2026-__-__T__:__Z"
end_time_utc: ""  # fill when known
detected_by: "telemetry|health_check|policy_gate|drift_monitor|user_report|security_scan"
reported_by: ""   # handle or team
incident_commander: ""  # optional but recommended
scribe: ""              # optional but recommended
systems:
  - api
  - ui
  - pipelines
  - graph
  - postgis
  - focus_mode
data_domains: []        # e.g. ["hydrology", "land-treaties"]
care_label: "public"    # public | restricted | sensitive (project-defined)
links:
  issue: ""
  pr: ""
  dashboards: []
  related_incidents: []
---

## Impact
- **Who/what was affected:**
- **User-visible symptoms:**
- **Blast radius:** (datasets, layers, endpoints, geographies, time ranges)
- **Trust impact:** (provenance breaks? policy bypass? mis-citation?)

## Current status
- What we know:
- What we don’t know yet:
- Mitigation in place:
- Verification steps:

## Immediate actions taken
- [ ] Containment
- [ ] Rollback (if applicable)
- [ ] Communication / advisory (if applicable)

## Evidence pointers
- `evidence/evidence_manifest.md`
- Telemetry excerpt:
- Governance-ledger pointer (AI incidents):
- STAC/DCAT/PROV snapshots:
- Graph health check report:

## Next updates
- ETA for next update:
- Owner for next update:
```

---

## 🔥 Severity rubric

<details>
<summary><strong>Click to expand severity levels (P0–P3)</strong></summary>

| Sev | Meaning | Typical examples |
|---:|---|---|
| **P0** | Critical | Sensitive data exposure, policy bypass, total outage, widespread corruption |
| **P1** | High | Major feature down (map unusable, ingestion halted), widespread incorrect results |
| **P2** | Medium | Partial degradation (some layers wrong/stale), localized integrity issues |
| **P3** | Low | Minor bug, cosmetic UI break, small performance regression with workaround |

✅ When in doubt, **start higher** and downgrade after evidence.

</details>

---

## 🧪 Evidence pack (KFM-style)

KFM incidents should ship with an **evidence pack** that makes the incident reproducible and auditable.

### Minimum evidence checklist

- [ ] 📌 **Evidence manifest** (`evidence/evidence_manifest.md`) explaining what’s included
- [ ] 🔗 **STAC/DCAT/PROV snapshots** relevant to the affected datasets/layers
- [ ] 🧾 **Telemetry excerpt** (request IDs / correlation IDs / run IDs)
- [ ] 🧠 **AI incidents:** prompt + retrieval sources + citation coverage + governance metadata
- [ ] 🧭 **Graph incidents:** health-check report + counts (orphan nodes, missing edges, lag)
- [ ] 🖼️ **UI incidents:** screenshots + console errors + browser + WebGL info (if relevant)
- [ ] 🧬 **Change provenance:** link to PR(s), commit(s), config versions, pipeline run contexts

> 🧷 Tip: Treat evidence as **“boundary artifacts”** — the same way KFM treats publishable data artifacts: structured, versioned, and cross-linked.

---

## 🔍 Detection sources you should reference (when applicable)

- 📈 **Telemetry** (performance + pipeline runs + user-facing errors)
- 🧭 **Graph health checks** (orphaned nodes, lag, freshness SLA violations)
- ✅ **Policy gates** (schema validation, provenance completeness, licensing, sensitivity rules)
- 🧠 **Bias/drift monitors** (accuracy drop, citation coverage drop, user corrections)
- 🧵 **Pulse Threads** / narrative anomaly detection (if enabled for monitoring)

---

## 🛡️ Security / Sensitive data fast path

If an incident involves **sensitive data exposure** (PII, protected site locations, restricted cultural info, secrets):

1. **Contain immediately** (revoke access, disable endpoints, remove layer)
2. **Remove exposure artifacts** (don’t “fix-forward” without removing the leak)
3. **Rotate credentials** if any chance of secret exposure
4. **Write a postmortem** with redacted evidence; store sensitive evidence securely
5. **Add/strengthen policy gates** so it can’t recur

> 🔒 KFM is FAIR + CARE aligned — incident handling must respect cultural protocols and sovereignty constraints.

---

## ✅ Closeout checklist (Definition of Done)

- [ ] Incident status = `closed (postmortem complete)`
- [ ] Postmortem (`rca.md`) is written and **blameless**
- [ ] Action items are created with owners + due dates
- [ ] Regression tests / validations added (so it doesn’t recur)
- [ ] Policy gates updated (if incident touched governance/provenance/security)
- [ ] Evidence pack is complete enough for a third party to reproduce the failure mode
- [ ] Index table updated with final links and status

---

## 📚 Reference shelf (project-wide)

This 2026 incident process is aligned with the broader KFM documentation and research library:

- 🧱 **Architecture & governance:** KFM architecture, policy gates, security posture
- 🗺️ **UI & visualization:** KFM UI system, MapLibre/Cesium workflows, AR/offline concepts
- 🧠 **AI & agents:** Focus Mode, governance ledger, WPE automation, drift/bias monitoring
- 📥 **Data intake & pipelines:** contract-first + deterministic ETL + STAC/DCAT/PROV publishing
- 💡 **Future concepts:** Pulse Threads, graph health checks, artifact registries, new domains
- 📦 **Reference portfolios:** AI, data management, mapping/WebGL, language resources

> Keep incidents readable for humans, but structured enough for machines.  
> That’s the MCP sweet spot. 🧠⚙️

---
