---
title: "TEMPLATE 🚨 Incident Report (KFM × MCP)"
path: mcp/incidents/templates/incident.md
version: "v1.0.0"
last_updated: "2026-01-23"
status: "active"
doc_kind: "template"
license: "CC-BY-4.0"
markdown_protocol_version: "v13"
pipeline_contract_version: "v1"

# Canonical refs (update if repo moves)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"
faircare_ref: "docs/guides/governance/faircare-oversight.md"
policy_pack_ref: "api/scripts/policy/README.md"
incident_response_ref: "docs/security/incident_response.md"
security_policy_ref: ".github/SECURITY.md"

# ---- Copy-time fields (replace when creating a real incident) ----
incident_id: "INC-YYYYMMDD-###"
incident_status: "TEMPLATE" # open | mitigated | resolved | postmortem_published | closed
severity: "SEV?"            # SEV0 | SEV1 | SEV2 | SEV3 | SEV4
priority: "P?"
start_time_utc: "YYYY-MM-DDTHH:MM:SSZ"
detected_time_utc: "YYYY-MM-DDTHH:MM:SSZ"
end_time_utc: "YYYY-MM-DDTHH:MM:SSZ"

reported_by: "TBD"
owner: "TBD"
incident_commander: "TBD"
scribe: "TBD"
reviewers: []

environments: ["prod"]      # prod | staging | dev | local | ci
incident_type: []           # data | pipeline | graph | api | ui | ai | security | governance | performance | supply-chain | other
components: []              # e.g., api/, web/, src/pipelines/, src/graph/, data/, mcp/
domains: []                 # e.g., historical | hydrology | agriculture | archaeology | public-safety
regions: []                 # e.g., county IDs, bbox, "statewide"
time_span: ""               # e.g., "1854–1861" or "2026-01-01..2026-01-07"

user_impact: "TBD"
data_impact: "TBD"
security_impact: "TBD"
gov_review_required: "TBD"  # yes | no | pending

related_issues: []
related_prs: []
related_commits: []
related_runs: []            # pipeline run IDs / MCP run IDs / notebook paths
related_dashboards: []

dataset_ids: []             # internal dataset stable IDs
stac_ids: []                # STAC item/collection IDs
dcat_ids: []                # DCAT dataset/distribution IDs
prov_bundle_ids: []         # PROV bundle IDs

artifact_digests: []        # sha256:...
artifact_signatures: []     # cosign/sigstore refs (if used)
sbom_refs: []               # SPDX/CycloneDX refs (if used)
slsa_attestations: []       # provenance attestations (if used)

governance_ledger_entries: []
policy_gate_results: []     # OPA/Conftest rule IDs + outcomes

doc_uuid: "00000000-0000-0000-0000-000000000000"
doc_integrity_checksum: "sha256:TBD"
---

# 🚨 Incident Report (KFM × MCP)

![KFM](https://img.shields.io/badge/KFM-geospatial%20knowledge%20platform-2ea44f)
![MCP](https://img.shields.io/badge/MCP-documentation%20protocol-v13-blue)
![Evidence](https://img.shields.io/badge/provenance-evidence--first-6f42c1)
![Governance](https://img.shields.io/badge/FAIR%20%2B%20CARE-sensitivity--aware-orange)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)

> [!IMPORTANT]
> **Evidence-first + fail-closed.** For KFM, an incident write-up is only “done” when *claims are backed by artifacts* (IDs, checksums, logs, run manifests, STAC/DCAT/PROV refs, policy outputs) and *prevention* is shipped (tests, policies, runbooks, or guardrails). ✅

**Quick Nav:**  
[🧩 Use](#-how-to-use-this-template) · [🧾 Summary](#-summary) · [🎯 Impact](#-impact) · [🕵️ Detection](#-detection--triage) · [🕰️ Timeline](#️-timeline) · [📦 Evidence](#-evidence--provenance-locker) · [🧪 Investigation](#-investigation-scientific-method) · [🧩 Root Cause](#-root-cause--contributing-factors) · [🛠️ Fixes](#️-mitigation--recovery) · [📌 Actions](#-corrective--preventive-actions-capa) · [🧭 Governance](#-governance--ethics-faircare) · [🔐 Security](#-security--privacy) · [📣 Comms](#-communications) · [🧾 Appendix](#-appendix) · [✅ Sign-off](#-sign-off)

---

## 🧩 How to use this template

1) **Copy** this file to: `mcp/incidents/<YYYY>/INC-<YYYYMMDD>-###__short_slug.md`  
2) Update the **YAML front-matter** (⚠️ especially `path`, `incident_id`, timestamps, severity, owners)  
3) Create an **artifact folder** (see layout below) and attach all evidence there  
4) Keep updates **chronological**, add links to issues/PRs, and keep decisions in the **Governance Ledger** if required  
5) When resolved, complete **Root Cause**, **CAPA**, and **Lessons Learned**, then publish the postmortem ✅

### 🗂️ Recommended incident folder layout (📁 + 🧾 + 📦)

```text
📁 mcp/
└─ 📁 incidents/
   ├─ 📁 templates/
   │  └─ 📄 incident.md
   └─ 📁 2026/
      └─ 📁 INC-20260123-001__short_slug/
         ├─ 📄 INC-20260123-001__short_slug.md
         ├─ 📁 artifacts/
         │  ├─ 📁 logs/              # API, pipeline, UI console, DB logs (sanitized)
         │  ├─ 📁 queries/            # Cypher/SQL/GraphQL used to investigate
         │  ├─ 📁 exports/            # graph snapshots, CSV exports, STAC/DCAT diffs
         │  ├─ 📁 screenshots/        # UI evidence, policy failures, dashboards
         │  ├─ 📁 repro/              # minimal repro scripts, notebooks, configs
         │  └─ 📁 policy/             # conftest/OPA outputs, rule IDs, reports
         └─ 📄 README.md (optional)   # quick index to artifacts
```

---

## ✅ Definition of Done (DoD)

- [ ] YAML front-matter updated (✅ `path`, `incident_id`, timestamps, severity, owners)
- [ ] Impact quantified (users/data/system + scope + duration)
- [ ] Timeline completed (UTC timestamps; who/what/decision)
- [ ] Evidence locker complete (artifacts stored + checksums/digests)
- [ ] Root cause validated (not just suspected)
- [ ] Mitigation + recovery validated (verification steps recorded)
- [ ] CAPA tasks created (owners + due dates + links to issues/PRs)
- [ ] Policy/test/runbook updated **or** rationale documented if not
- [ ] Governance + FAIR/CARE review complete if triggered
- [ ] Postmortem published (or “internal-only” classification recorded)

---

## 🧾 Summary

### One-liner (tweet-length)
`<INCIDENT_ID>: <What broke> → <who/what impacted> → <current status>`

### What happened (plain language)
- **Symptoms:**  
  - `<symptom 1>`  
  - `<symptom 2>`
- **Primary impact:** `<users/data/features impacted>`
- **Current state:** `open / mitigated / resolved`

### Affected surfaces (check all that apply)
- [ ] 🧬 Data (raw/work/processed, STAC, DCAT, PROV)
- [ ] 🧠 AI / Focus Mode (RAG, citations, guardrails, prompt gate)
- [ ] 🗺️ UI (MapLibre/Cesium, timeline slider, layers, story nodes, analytics)
- [ ] 🧩 Graph (Neo4j, node/edge integrity, orphaned nodes)
- [ ] 🔌 API (FastAPI/GraphQL, auth, rate limits, caching)
- [ ] 🧱 Infra (DB, object storage, registry, CI/CD, secrets)
- [ ] 🔐 Security / Privacy (PII/sensitive data, supply chain, access control)
- [ ] 🧭 Governance (policy violations, FAIR/CARE, ethics)

---

## 🎯 Impact

### Impact at a glance
| Category | Scope | Notes |
|---|---:|---|
| Users affected | `<# / %>` | `<who + how measured>` |
| Data affected | `<datasets/records>` | `<stable IDs + distributions>` |
| Geographic scope | `<bbox / counties / statewide>` | `<include IDs>` |
| Time span impacted | `<range>` | `<historical timeline or real-time window>` |
| Availability | `<%/SLO>` | `<errors, downtime>` |
| Correctness | `<high/med/low>` | `<wrong outputs? misaligned map? drift?>` |
| Privacy/Safety | `<none/possible/confirmed>` | `<PII? sensitive sites? sovereignty?>` |

### Severity rubric (KFM-friendly)
| Severity | Meaning | Examples (not exhaustive) |
|---|---|---|
| **SEV0** | Critical breach / safety risk / irrecoverable corruption | Confirmed sensitive data leak; governance compromise; widespread “authoritative” misinformation; irreversible data loss |
| **SEV1** | Major outage or major integrity issue | Core map or API down; systemic corruption with limited recovery window |
| **SEV2** | Partial outage / limited integrity issue | Some layers broken; subset of users; workaround exists |
| **SEV3** | Minor issue | Cosmetic UI issues; minor perf regression |
| **SEV4** | Near miss / observation | Policy gate caught it; no user impact |

> [!CAUTION]
> If the incident affects **public-safety or time-sensitive hazard layers**, treat severity as **SEV0/SEV1** and document any communication constraints clearly.

---

## 🕵️ Detection & Triage

### Detection source (how did we learn?)
- [ ] Monitoring/alert
- [ ] CI/CD (policy gate, tests)
- [ ] User report (issue/discussion/email)
- [ ] Data QA report (graph health, metadata audits)
- [ ] Governance review (FAIR/CARE, ethics, sovereignty)
- [ ] AI telemetry (citation coverage, drift, refusal rate, hallucination flags)

**First detected by:** `<name/handle>`  
**Detected at (UTC):** `<timestamp>`  
**Initial hypothesis:** `<what we thought at first>`  
**Triage decision:** `<why SEV? + what to do first>`

### Immediate containment (first 15 minutes)
- [ ] Freeze risky deployments (CI/CD pause or rollback)
- [ ] Disable automation (Watcher/Planner/Executor kill-switch, if relevant)
- [ ] Restrict access (classification flip / RBAC / blocklist)  
- [ ] Preserve evidence (log snapshots, exports, digests)
- [ ] Start incident channel / assign commander + scribe

---

## 🕰️ Timeline

> [!TIP]
> Use **UTC**. Put the most objective timestamps first (alerts, CI runs, deploys, merges).

| Time (UTC) | Event | Who | Evidence / Link |
|---|---|---|---|
| `<YYYY-MM-DDTHH:MMZ>` | Detected `<alert/issue>` | `<@>` | `<artifact/log/dashboard>` |
| `<...>` | Triage started | `<@>` | `<notes>` |
| `<...>` | Mitigation applied | `<@>` | `<PR/commit/run>` |
| `<...>` | Verification passed | `<@>` | `<test output/QA report>` |
| `<...>` | Resolved | `<@>` | `<release/deploy>` |
| `<...>` | Postmortem published | `<@>` | `<link>` |

---

## 📦 Evidence & Provenance Locker

### 📌 “Minimum Evidence Set” (attach or link)
- [ ] 🔎 **Primary logs** (API request IDs, pipeline run logs, UI console logs)  
- [ ] 🧾 **Run manifest(s)** (pipeline + MCP runs; include tool versions + config)  
- [ ] 🧬 **Metadata diffs** (STAC/DCAT/PROV changes, before/after)  
- [ ] 🧩 **Graph snapshot/diff** (CSV import bundle, Cypher export, or report)  
- [ ] 🧱 **Policy outputs** (OPA/Conftest report, rule IDs that fired)  
- [ ] 🔐 **Access/audit trail** (who accessed what, if relevant; sanitized)  
- [ ] 🧾 **Checksums/digests** (sha256 for key artifacts; signatures if used)  

### Artifact index (fill these in)
| Artifact | Location (repo path) | Hash/Digest | Notes |
|---|---|---|---|
| Incident folder | `mcp/incidents/<YYYY>/<INCIDENT_ID>*/` | `sha256:TBD` | |
| Logs bundle | `.../artifacts/logs/` | `sha256:TBD` | **Sanitize secrets/PII** |
| Queries used | `.../artifacts/queries/` | `sha256:TBD` | SQL/Cypher/GraphQL |
| STAC diff | `.../artifacts/exports/stac_diff.*` | `sha256:TBD` | |
| DCAT diff | `.../artifacts/exports/dcat_diff.*` | `sha256:TBD` | |
| PROV bundle | `.../artifacts/exports/prov_bundle.*` | `sha256:TBD` | |
| Policy report | `.../artifacts/policy/` | `sha256:TBD` | rule IDs + outputs |
| Graph export | `.../artifacts/exports/graph_*` | `sha256:TBD` | |

### Provenance pointers (IDs)
- **Dataset stable IDs:** `<dataset_ids[]>`
- **STAC item/collection IDs:** `<stac_ids[]>`
- **DCAT dataset/distribution IDs:** `<dcat_ids[]>`
- **PROV bundle IDs:** `<prov_bundle_ids[]>`
- **Governance ledger entries:** `<governance_ledger_entries[]>`
- **Policy gate results:** `<policy_gate_results[]>`

> [!WARNING]
> If the incident involves **sensitive data**, treat it like a **secret**:
> 1) revoke/deny access immediately, 2) remove from repo, 3) **purge from history if required**, 4) document the governance/policy gap that allowed it.

---

## 🧪 Investigation (Scientific Method)

> [!NOTE]
> We follow “Master Coder Protocol” style: **hypothesize → test → measure → conclude**. Record units, uncertainty/error margins, and cross-verification steps when relevant.

### Problem statement (observable facts only)
- `<fact 1 with evidence>`
- `<fact 2 with evidence>`

### Hypotheses (ranked)
1. `<hypothesis 1>`
2. `<hypothesis 2>`
3. `<hypothesis 3>`

### Experiments / checks performed
| Test | Expected | Actual | Result | Evidence |
|---|---|---|---|---|
| `<test 1>` | `<expected>` | `<actual>` | ✅/❌ | `<link>` |
| `<test 2>` | `<expected>` | `<actual>` | ✅/❌ | `<link>` |

### Reproduction steps (minimal + deterministic)
1. `<step 1>`
2. `<step 2>`
3. `<step 3>`

**Environment captured:**  
- OS: `<...>`  
- App versions: `<...>`  
- Dataset version(s): `<...>`  
- Commit SHA(s): `<...>`  
- Config: `<...>`  
- Random seeds (if any): `<...>`  

---

## 🧩 Root Cause & Contributing Factors

### Root cause (single sentence, precise)
`<root cause>`

### Contributing factors
- `<factor 1>` (e.g., missing test, policy gap, brittle integration)
- `<factor 2>`
- `<factor 3>`

### Why it wasn’t caught earlier (honest + specific)
- Monitoring gap: `<...>`
- QA gap: `<...>`
- Review/process gap: `<...>`
- Governance gap: `<...>`

---

## 🛠️ Mitigation & Recovery

### Immediate mitigation (what stopped the bleeding)
- `<mitigation step 1>`  
- `<mitigation step 2>`  

**Verification:**  
- [ ] User-facing symptoms gone
- [ ] Data integrity checks passed
- [ ] Policy gates pass (or fail for correct reasons)
- [ ] Graph health checks clean
- [ ] AI citations/guardrails behaving (if relevant)

### Recovery steps (restore correct state)
- **Data rollback:** `<git revert / restore older files / mark deprecated in DCAT>`
- **Graph rollback:** `<re-import CSV snapshots / migration rollback / mark obsolete>`
- **Deployment rollback:** `<rollback release>`
- **Automation rollback:** `<disable agent / revert agent PR / tighten planner>`  
- **Access rollback:** `<restore classification / re-enable endpoint>`  

### “Known-good” checkpoint
- **Commit SHA:** `<...>`
- **Release tag:** `<...>`
- **Dataset version(s):** `<...>`

---

## 📌 Corrective & Preventive Actions (CAPA)

> [!TIP]
> CAPA should include **tests/policies** that make the incident **hard to repeat**. Prefer “guardrails that fail-closed”.

### Action items (track like tickets)
| Action | Owner | Due | Type | Link |
|---|---|---:|---|---|
| `<add test for X>` | `<@>` | `<date>` | Prevent | `<issue/PR>` |
| `<add OPA rule for Y>` | `<@>` | `<date>` | Prevent | `<issue/PR>` |
| `<add runbook + dashboard>` | `<@>` | `<date>` | Detect | `<issue/PR>` |
| `<backfill / repair dataset>` | `<@>` | `<date>` | Correct | `<issue/PR>` |

### CAPA checklist
- [ ] Regression test added
- [ ] Policy gate updated (OPA/Conftest) or rationale documented
- [ ] Monitoring/alert added or tuned
- [ ] Documentation updated (runbooks, SOPs, architecture notes)
- [ ] Model card / experiment report updated (if AI)
- [ ] Data catalog metadata updated (STAC/DCAT/PROV + deprecations)
- [ ] Postmortem shared to stakeholders/community (if applicable)

---

## 🧭 Governance & Ethics (FAIR/CARE)

### Sensitivity classification (required if any data involved)
- **Sensitivity:** `public | internal | restricted | sensitive`
- **CARE label / community constraints:** `<...>`
- **Jurisdiction:** `<...>`
- **Sovereignty concerns:** `yes/no` (explain)

### Governance triggers (check if applicable)
- [ ] Involves Indigenous/sovereign/community-governed data
- [ ] Involves culturally sensitive locations (e.g., archaeological sites)
- [ ] Involves minors / PII / protected classes
- [ ] Produces “authoritative” narratives that may harm groups
- [ ] Introduces new public-facing AI behavior
- [ ] Requires policy exception

**Governance decision:** `<approve/deny/mitigate>`  
**Ledger entry:** `<id/link>`  
**Reviewers:** `<council/maintainers>`

> [!IMPORTANT]
> **Focus Mode outputs must be traceable.** If an incident involves AI-generated narratives/claims, record which sources were cited, which were missing, and how the system validated (or failed to validate) them.

---

## 🔐 Security & Privacy

### Security classification
- [ ] Not a security incident
- [ ] Potential security incident (investigating)
- [ ] Confirmed security incident (containment active)

### If security/privacy-related, capture:
- **Attack vector / cause:** `<prompt injection / supply chain / auth bypass / misconfig / data exposure / other>`
- **Systems touched:** `<...>`
- **Data exposed:** `<none/possible/confirmed + scope>`
- **Indicators of compromise (IOCs):** `<hashes/domains/ips (sanitize)>`
- **Access controls status:** `<RBAC, tokens, key rotation>`

### Supply chain / artifact integrity (if applicable)
- [ ] SBOM captured (SPDX/CycloneDX)
- [ ] Artifact digests recorded (sha256)
- [ ] Signatures verified (cosign/sigstore)
- [ ] SLSA/provenance attestation stored

> [!CAUTION]
> Never paste secrets/tokens into this doc. If you need to reference them, store in a secure system and link a **sanitized pointer** only.

---

## 🧠 AI / Focus Mode (optional)

<details>
<summary><strong>🧠 Expand AI / Focus Mode incident checklist</strong></summary>

### AI incident category
- [ ] Missing citations / broken provenance links
- [ ] Hallucination / unsupported claim
- [ ] Prompt injection / retrieval poisoning
- [ ] Model drift / degraded quality
- [ ] Unsafe output / policy violation
- [ ] Tool misuse (wrong layer/region/time span)
- [ ] Excessive refusal / blocked legitimate request

### Record the full AI context (sanitized)
- **Model + version:** `<...>`
- **System prompts / policy pack version:** `<...>`
- **Retrieval mode:** `<RAG on/off; index versions>`
- **Query constraints:** `<region/time span/layers>`
- **Citation coverage metric:** `<%>`
- **Governance check outcome:** `<pass/fail + why>`
- **Telemetry snapshot:** `<latency, cost, tokens, error rates>`

### Evidence to attach (AI)
- [ ] Prompt + tool calls (sanitized)
- [ ] Retrieved sources list + IDs (STAC/DCAT/PROV)
- [ ] Output + citations as produced
- [ ] Guardrail decisions + policy gate output

### Fix patterns (choose)
- [ ] Strengthen “citation-required” gate (fail-closed)
- [ ] Tighten retrieval filters (time/region/layer constraints)
- [ ] Add disallowed claim patterns (e.g., “cannot assert without source”)
- [ ] Update model card (limitations, known failure modes)
- [ ] Add eval/benchmark to catch recurrence

</details>

---

## 🧬 Data Intake / Pipeline (optional)

<details>
<summary><strong>🧬 Expand data intake + rollback checklist</strong></summary>

### Pipeline stage impacted
- [ ] Acquire (fetchers/watchers)
- [ ] Validate (schema, geometry, license)
- [ ] Transform (normalize, reproject, simplify)
- [ ] Catalog (STAC/DCAT)
- [ ] Graph build (CSV import, node/edge integrity)
- [ ] Publish (API/distributions/tiles)
- [ ] QA/Audits (graph health, drift checks)

### Data quality checks (minimum)
- [ ] Completeness (required fields present; no silent null storms)
- [ ] Consistency (units, time formats, CRS, naming conventions)
- [ ] Validity (geometry validity, ranges, types)
- [ ] Uniqueness (stable IDs; no duplicate keys)
- [ ] Timeliness (freshness; correct “as-of”)
- [ ] Licensing (compatible + recorded)
- [ ] Sensitivity classification set (FAIR/CARE)

### Geospatial “gotchas” (common KFM failures)
- [ ] CRS mismatch (EPSG:4326 vs EPSG:3857, etc.)
- [ ] Invalid geometries (self-intersections, ring issues)
- [ ] Topology issues (dangles, gaps, overlaps)
- [ ] Time-index drift (timestamps parsed incorrectly)
- [ ] Tile/render mismatch (simplification too aggressive)

### Rollback procedure (data + graph)
- [ ] Git revert the ingest commit(s)
- [ ] Mark distribution deprecated in DCAT + note successor
- [ ] Re-import previous graph CSV snapshot (stable IDs restore)
- [ ] Run policy gates + QA suite again
- [ ] If sensitive data leaked: remove files + **purge history if required**
- [ ] Disable automation if it caused recurrence (kill-switch)

</details>

---

## 🧩 Graph Health (optional)

<details>
<summary><strong>🧩 Expand graph health + integrity checklist</strong></summary>

### What failed?
- [ ] Orphan nodes (no valid edges)
- [ ] Broken references (IDs not found)
- [ ] Property schema drift (unexpected keys/types)
- [ ] Hub explosion (suspiciously high-degree node)
- [ ] Duplicate stable IDs
- [ ] Mismatch between DCAT/STAC and graph

### What to attach
- [ ] Graph health report output
- [ ] Cypher queries used
- [ ] Before/after degree distribution snapshot
- [ ] Backup verification logs (if used)

</details>

---

## 🗺️ UI / Map / Timeline / Story Nodes (optional)

<details>
<summary><strong>🗺️ Expand UI + rendering incident checklist</strong></summary>

### UI mode affected
- [ ] Exploration Mode
- [ ] Story Mode (Story Nodes)
- [ ] Analytics Mode
- [ ] Focus Mode panel (citations + provenance)

### Capture the UI state (for reproducibility)
- **Browser + version:** `<...>`
- **Device:** `<desktop/mobile/AR device>`
- **2D/3D engine:** `<MapLibre/Cesium>`
- **Map style / tileset:** `<style id + version>`
- **Active layers:** `<list>`
- **Timeline state:** `<timestamp range + slider position>`
- **Viewport:** `<center, zoom, bearing, pitch>`
- **Filters:** `<region/time/layer filters>`

### Common rendering failures
- [ ] WebGL context lost / shader failure
- [ ] Tile 404 / CORS
- [ ] Incorrect projection / CRS
- [ ] Time slider desync with layer timestamps
- [ ] Story Node references missing assets/IDs
- [ ] Accessibility regression (keyboard, ARIA, contrast)

### Evidence
- [ ] Screenshot(s) / screen recording
- [ ] Console logs
- [ ] Network HAR (sanitized)
- [ ] Layer provenance panel output

</details>

---

## 📣 Communications

### Stakeholders
- Internal: `<maintainers/teams>`
- External/community: `<users/partners>`
- Governance council/ethics reviewers: `<names>`

### Updates log
| Time (UTC) | Channel | Message summary | Link |
|---|---|---|---|
| `<...>` | `<issue/discussion/chat>` | `<...>` | `<...>` |

### Post-incident messaging (if needed)
- **What we will say:** `<clear, non-blaming>`
- **What we will not say:** `<sensitive, speculative>`
- **Who approves:** `<@>`

---

## 🧠 Lessons Learned

### What went well ✅
- `<...>`

### What went poorly ⚠️
- `<...>`

### Where we got lucky 🍀
- `<...>`

### One concrete improvement (if we can only do ONE thing)
`<...>`

---

## 🧾 Appendix

### Queries used (paste or link)
- **Cypher:** `artifacts/queries/*.cypher`
- **SQL (PostGIS):** `artifacts/queries/*.sql`
- **API calls / curl:** `artifacts/repro/*.sh`

### Commands / scripts executed
```bash
# Example (replace)
# ./api/scripts/policy/run_conftest.sh
# python src/pipelines/run_ingest.py --dataset <id> --dry-run
```

### Policy gate output (paste short summary)
- Rule(s) triggered: `<...>`
- Outcome: `<pass/fail>`
- Report path: `artifacts/policy/<...>`

---

## ✅ Sign-off

| Role | Person | Date | Notes |
|---|---|---:|---|
| Incident Commander | `<@>` | `<YYYY-MM-DD>` | |
| Owner | `<@>` | `<YYYY-MM-DD>` | |
| Scribe | `<@>` | `<YYYY-MM-DD>` | |
| Reviewer (Tech) | `<@>` | `<YYYY-MM-DD>` | |
| Reviewer (Governance/Ethics) | `<@>` | `<YYYY-MM-DD>` | |

---

## 📚 Project Reference Shelf (optional)

<details>
<summary><strong>📚 Expand “where to look” references</strong></summary>

### Core KFM docs
- 🧱 Comprehensive Architecture, Features, and Design
- 🧭 AI System Overview (Focus Mode, governance checks, citations)
- 🗺️ UI System Overview (map/timeline/story/focus modes)
- 🧬 Data Intake Guide (rollback, sensitive data emergency procedure, policy pack)
- 💡 Innovative Concepts & Future Proposals (OCI artifacts, signatures, agent kill-switch, graph health checks)
- 🧾 Design audits & enhancement opportunities (doc gaps, ops checklists)

### Technical libraries / background references
- 🧠 AI concepts collection (RAG, safety, drift, prompt security)
- 🗺️ Geospatial / WebGL / virtual worlds references (MapLibre/Cesium/WebGL gotchas)
- 🧰 Programming + engineering references (SOPs, reproducibility, documentation protocol)
- 🧪 Data science / management references (anomaly detection, quality, privacy)
- 🧭 Geospatial analysis cookbook (PostGIS/CRS/validity troubleshooting)

</details>
