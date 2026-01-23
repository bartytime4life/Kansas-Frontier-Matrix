---
title: "🧠🧭 Focus Mode Incident Runbook"
file: "mcp/incidents/runbooks/focus-mode.md"
version: "0.1.0"
last_updated: "2026-01-23"
status: "draft"
doc_kind: "runbook"
references:
  - "Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf"
  - "Kansas Frontier Matrix – Comprehensive UI System Overview.pdf"
  - "📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf"
  - "Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf"
  - "Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf"
  - "🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf"
  - "Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf"
  - "Additional Project Ideas.pdf"
  - "AI Concepts & more.pdf"
  - "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"
  - "Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf"
  - "Various programming langurages & resources 1.pdf"
ethics: "FAIR+CARE; provenance-first; policy-gated (OPA/Conftest); citation-required; sensitive-data aware; fail-closed."
faircare:
  findable: "Stable path under /mcp/incidents/runbooks + unique title."
  accessible: "Plain Markdown; usable offline."
  interoperable: "Uses shared KFM terms (DCAT/STAC/PROV, OPA, RBAC, Story Nodes)."
  reusable: "Checklists + templates; cloneable for other subsystems."
  care_collective_benefit: "Prioritizes safe fallback, transparency, and community trust."
  care_authority_to_control: "Respects classification & sensitive-location handling."
  care_responsibility: "Explicit on-call ownership + escalation steps."
  care_ethics: "Stop-the-line for uncited/sensitive output; least-privilege + auditability."
doc_uuid: "b1b16d69-06e0-4e49-88e8-5e7cbeed5fc1"
git_commit: "TBD"
checksum: "TBD"
---

![runbook](https://img.shields.io/badge/doc-runbook-blue)
![focus-mode](https://img.shields.io/badge/component-Focus%20Mode-6f42c1)
![policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-success)
![stance](https://img.shields.io/badge/stance-evidence%E2%80%91first-important)

📁 `mcp/`  
└─ 📁 `incidents/`  
&nbsp;&nbsp;&nbsp;└─ 📁 `runbooks/`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ 🧠 `focus-mode.md`

---

## 🎯 What “Focus Mode” is (and why incidents matter)

**Focus Mode** is KFM’s AI assistant experience: it answers user questions with **citations**, is **context-aware** (map view, time range, active layers), and provides **explainability/audit** surfaces. It is designed to *refuse* rather than fabricate when sources are missing.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:2‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

**Non-negotiable invariant (policy-gated):**  
Any Focus Mode output that cannot cite a source **must refuse** (fail closed).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

> [!IMPORTANT]
> 🧷 **Incidents involving uncited claims, sensitive-data leakage, or policy bypass attempts are automatically “stop-the-line.”**  
> The system is explicitly built around automated policy gates and “fail closed” behavior.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧑‍🤝‍🧑 Ownership & escalation

**Primary owner:** `TBD` (KFM AI / Platform)  
**Secondary:** `TBD` (Data Intake / Governance)  
**Tertiary:** `TBD` (UI / Map Rendering)

**Escalate immediately when:**
- Sensitive data / PII / restricted layer is exposed (SEV0)  
- Focus Mode answers without citations (SEV0/SEV1 depending on blast radius)  
- Governance/policy gate is bypassed or “fail open” behavior is observed (SEV0)

---

## 🧱 Architecture snapshot

### Components (conceptual)
- **UI** (React): invokes Focus Mode via backend APIs (REST/GraphQL) and surfaces provenance + citations.  [oai_citation:5‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:6‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **Focus Mode Service** (AI Layer): parses query → retrieves evidence (graph + geospatial + docs) → generates draft → applies policy checks → returns answer with citations; logs to governance ledger.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Retrieval dependencies:** Neo4j (knowledge graph), PostGIS (spatial/time), full-text/vector search (e.g., Elasticsearch).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Governance gate:** OPA runtime policy checks; Conftest policies in CI; “fail closed”.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Auditability:** Immutable governance ledger logging for answers + provenance.  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Observability:** telemetry with run identifiers + config hashes; Focus Telemetry tracks AI performance signals.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

```mermaid
flowchart LR
  U[👤 User] --> UI[🖥️ React UI]
  UI --> API[🧩 REST/GraphQL API]
  API --> FM[🧠 Focus Mode Service (AI Layer)]
  FM --> R1[(🕸️ Neo4j Graph)]
  FM --> R2[(🗺️ PostGIS)]
  FM --> R3[(🔎 Search Index)]
  FM --> OPA[🛡️ OPA Policy Gate]
  OPA -->|allow| OUT[✅ Answer + Citations]
  OPA -->|deny| REFUSE[⛔ Refuse / Safe Fallback]
  OUT --> LEDGER[(📜 Governance Ledger)]
  REFUSE --> LEDGER
```

---

## ✅ “Golden Signals” for Focus Mode

> [!TIP]
> If you don’t have dashboards yet, start with these and wire them into “Focus Telemetry” (latency, query volume, etc.).  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### Core SLIs (recommended)
- **Availability:** % successful requests (2xx) to Focus Mode endpoint(s)
- **Latency:** p50 / p95 / p99 response time
- **Citation coverage:** % answers with ≥1 citation (should be ~100% by policy)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **OPA deny rate:** per policy ID / rule group (helps detect regressions or attacks)  [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Refusal rate:** sudden spikes can indicate retrieval/index outage, policy misconfig, or prompt injection attempt
- **Dependency health:** Neo4j/PostGIS/index health & query latency (graph + spatial indexes + caching matter)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Alert seeds (starter thresholds)
- 🚨 5xx rate > 2% for 5m (Focus Mode or API)
- 🐢 p95 latency > 8s for 10m (Focus Mode)
- 🧷 citation coverage < 99.9% for 5m (treat as policy violation)
- 🛡️ OPA denials spike 5× baseline (possible attack/policy regression)
- 🕳️ retrieval timeouts (Neo4j/PostGIS/search) > baseline 3×
- 🧊 governance ledger write failures > 0 (audit gap risk)

---

## 🚦Severity guide (KFM-leaning)

- **SEV0 (Stop-the-line):** policy bypass, uncited answers in prod, sensitive/PII exposure, “fail open” behavior  
- **SEV1:** widespread outage (Focus Mode unavailable), governance ledger failing, major latency regression  
- **SEV2:** degraded quality (high refusal rate, partial retrieval failures, incorrect citations)  
- **SEV3:** isolated UI issues, minor formatting/citation rendering issues with low impact

---

## 🧪 Quick triage checklist (first 10 minutes)

> [!NOTE]
> Focus Mode is built around “evidence-backed” answers, OPA gating, and immutable logging. Treat triage as: **Is evidence retrieval healthy? Is policy gate behaving? Is audit logging intact?**  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 1) Confirm the symptom (user-reported vs alert)
- [ ] What changed? (deploy, policy update, index refresh, ingestion run)
- [ ] What’s the blast radius? (all users? specific dataset/layer? specific time range?)

### 2) Run the smoke test questions (known-good)
Pick 2–3 “golden queries” that must return citations.
- [ ] Query A: “What datasets support **X** in **current map view**?”
- [ ] Query B: “Summarize **Y** between **year1-year2** for **county Z**”
- [ ] Query C: “Show sources for **current AQI** in map view” (also tests domain models)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 3) Check gates + logs (minimum)
- [ ] **OPA allow/deny** decision logs (is it denying everything?)
- [ ] **Citation presence** and citation-to-source validity
- [ ] **Governance ledger write success** (no audit gaps)  [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 4) Check retrieval dependencies
- [ ] Neo4j query latency / errors
- [ ] PostGIS query latency / spatial index health
- [ ] Search index health (timeouts, shard failures)
- [ ] Cache hit rate (if present)

---

## 🧯Immediate containment levers (safe fallbacks)

> [!IMPORTANT]
> KFM’s philosophy is “fail closed.” If gates or evidence are compromised, **disable generation** and fall back to “sources-only” or “refusal” rather than degrade into speculation.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### A) “Refusal-first mode” (recommended in uncertainty)
- Force Focus Mode to **refuse** any response that can’t produce citations and/or fails OPA checks. (This should already happen; if not, treat as SEV0.)

### B) “Sources-only mode”
- Disable final natural-language generation; return:
  - retrieved sources list
  - brief, template-only summaries (“here are the documents/layers that match”)
- Goal: preserve trust and reduce hallucination risk.

### C) Stop automated agents (if incident involves automation / PRs)
KFM proposes a kill-switch to halt agent actions (e.g., Watcher–Planner–Executor) by creating a `.agent-freeze` file or setting a config flag.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🛠️ Common incident playbooks

### FM-001 — Focus Mode down / 5xx / timeouts
**Signals**
- API error rate spike after deployment; logs show runtime errors.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Immediate actions**
- [ ] Roll back the last deploy (Focus Mode service or API gateway)
- [ ] Confirm dependency health (Neo4j/PostGIS/index) to avoid “rollback into same outage”
- [ ] Enable “sources-only mode” if generation is the failing component

**Diagnostics**
- Check caching/indexes: PostGIS spatial indexes, Neo4j graph indexes, caching of frequent queries help performance; regressions often show here.  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Correlate errors with deployment time; KFM expects CI/CD + monitoring + alerts post-deploy.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

### FM-002 — Latency regression / degraded responsiveness
**Signals**
- p95 latency climbing; timeouts; higher CPU/mem; spike in heavy queries

**What to check**
- [ ] PostGIS slow queries + spatial index health (vacuum/analyze/EXPLAIN)
- [ ] Neo4j slow queries + graph indexes
- [ ] Cache hit-rate drop (if cache invalidation changed)
- [ ] “Expensive ops” are supposed to be offline (tiling/precompute). If they’re happening online, that’s a regression.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Mitigations**
- [ ] Temporarily tighten query limits (map extent, time span, max docs)
- [ ] Degrade to “sources-only mode” under load
- [ ] Rate-limit suspicious traffic (abuse prevention is part of API security posture)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

### FM-003 — Missing citations / citation coverage drops
**Signals**
- Citation coverage < 100% (should be ~100% by policy)
- Users report answers without sources

**Why this is critical**
- Policy gates require that Focus Mode outputs include citations; otherwise it must refuse.  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**Immediate actions**
- [ ] Treat as SEV0 if visible in production
- [ ] Switch to “refusal-first mode” or disable generation until fixed
- [ ] Identify if the failure is:
  - retrieval returned empty evidence
  - citation renderer bug (UI)
  - policy gate misconfigured (OPA not enforcing)

**Diagnostics checklist**
- [ ] Retrieval empty? (Neo4j/PostGIS/index health; filters too strict)
- [ ] UI rendering? The UI is responsible for surfacing citations and provenance.  [oai_citation:31‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- [ ] OPA decision logs: is the “citations required” rule firing?  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

### FM-004 — OPA deny storm (false positives) or policy regression
**Signals**
- OPA deny rate spikes; refusal rate spikes
- Same policy ID denies most queries

**Immediate actions**
- [ ] Confirm whether it’s attack traffic vs policy bug
- [ ] If policy regression: roll back policy pack OR temporarily relax the single problematic rule (do **not** disable gating globally)

**Why**
OPA runtime checks intercept Focus Mode requests/responses; policies are intended to be updated without redeploying, but misconfigs can block.  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### FM-005 — Hallucination / “answer doesn’t match cited sources”
**Signals**
- Users report mismatch between claim and linked source
- Internal evals show groundedness regression

**Immediate actions**
- [ ] Switch to “sources-only mode” for the impacted route
- [ ] Increase refusal thresholds (require stronger evidence)

**Diagnostics**
- [ ] Inspect the **evidence bundle** used for the answer (what docs, what graph nodes, what PostGIS query)
- [ ] Re-run with deterministic settings (telemetry includes run IDs + config hashes for replay/audit)  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Check whether conceptual attention nodes / taxonomy mapping is broken (retrieval targeting issue).  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

### FM-006 — Sensitive data / PII exposure (stop-the-line)
**Signals**
- Location of sensitive sites, endangered species, private info, or restricted layers exposed
- Data classification mismatch (marked public but should be sensitive)

**Immediate actions**
- [ ] **Disable Focus Mode** or “sources-only mode” for impacted data domain
- [ ] **Revoke public access** by changing classification to restricted/sensitive and hiding from UI/API
- [ ] Remove leaked artifacts; rotate/patch as needed
- [ ] Start formal incident log + notify governance council if applicable  [oai_citation:36‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Built-in design supports**
- KFM includes data sensitivity classification fields; UI/API may hide layers by default or require acknowledgement; roles can gate access.  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- CARE/ethics: obfuscation/generalization may be used for sensitive locations (rounded coordinates, uncertainty), and warnings/metadata are first-class.  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:39‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

**Emergency procedure (repo hygiene)**
- Remove from git if secrets/PII were committed; purge if needed; document what happened.  [oai_citation:40‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### FM-007 — “Wrong context” (map view/time range/layers not respected)
**Signals**
- Answer ignores current viewport/time slider
- Answer references a different region/time than UI state

**Design intent**
Focus Mode integrates map context (location/time/layers). If this breaks, treat as correctness incident.  [oai_citation:41‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Diagnostics**
- [ ] Verify UI is sending correct context payload (viewport bbox, time range, layer IDs)
- [ ] Confirm the server’s context normalizer (projection, bbox normalization) is correct
- [ ] Confirm map/timeline state isn’t stale (live dashboards may replay recent time series).  [oai_citation:42‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

### FM-008 — Governance ledger write failures
**Signals**
- Requests succeed but ledger logging fails (audit gap)
- Policy requires logging; platform emphasizes auditability/provenance-first

**Immediate actions**
- [ ] Treat as SEV1 (or SEV0 if combined with policy bypass)
- [ ] Degrade to refusal or “sources-only” if you cannot safely record outputs
- [ ] Repair ledger connectivity/permissions

**Why**
Focus Mode answers are intended to be logged in an immutable governance ledger.  [oai_citation:43‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### FM-009 — Drift / bias / domain model regression affecting answers
**Signals**
- Drift alerts; incorrect nowcasts; quality flags spike; community reports incorrect real-time values

**Relevant dependency example**
KFM includes domain-specific bias correction (e.g., air-quality correction + deterministic runs + STAC provenance). If upstream model breaks, Focus Mode answers degrade.  [oai_citation:44‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:45‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Actions**
- [ ] Pin to last-known-good model version
- [ ] Increase uncertainty/refusal on impacted domains until corrected
- [ ] Ensure corrected dataset STAC items + provenance are intact (determinism + metadata is expected).  [oai_citation:46‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

### FM-010 — Upstream ingestion lag / stale “real-time” answers
**Signals**
- Live feed answers are stale; “minutes since last seen” grows

**Recommended monitoring**
- Track data-source lag as “minutes since last seen” per pipeline (SLA).  [oai_citation:47‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**Diagnostics**
- [ ] Watcher health (idempotent fetch via ETag/Last-Modified suggested in proposals)  [oai_citation:48‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- [ ] Orphaned nodes in graph (STAC item without dataset, PROV Activity without USED/WAS_GENERATED_BY).  [oai_citation:49‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🔐 Security & abuse incidents (prompt injection, misuse, scraping)

KFM includes application security (authz, rate limiting, sanitization) and a **prompt security subsystem** (“Prompt Gate”) to defend against prompt injection and prevent sensitive leakage.  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**When you suspect prompt injection**
- [ ] Increase refusal strictness
- [ ] Disable tool-like actions (if any exist) and use sources-only
- [ ] Add a targeted OPA rule to block the pattern (keep an audit trail)
- [ ] Rate limit abusive actors

---

## 🔄 Rollback & recovery (GitOps-first)

> [!NOTE]
> KFM’s workflow leans toward GitOps / PR-first changes (including modeling outputs), so rollback should be deterministic and auditable.  [oai_citation:51‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### A) Roll back a bad deploy (Focus Mode service / API)
- [ ] Revert deployment artifact (container tag / release)
- [ ] Validate with smoke tests (citations + context)
- [ ] Confirm monitoring returns to baseline

### B) Roll back a bad policy pack update (OPA/Conftest)
- [ ] Revert policy version
- [ ] Confirm deny storm stops
- [ ] Confirm citations-required rule still enforced (don’t weaken the core invariant)  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### C) Roll back a data ingestion / catalog regression
- [ ] Prefer `git revert` over history rewrites
- [ ] If secrets/PII, follow emergency procedure (remove + purge if necessary)  [oai_citation:53‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Rebuild affected indexes (graph, search) and validate orphan checks

---

## 🧾 Incident records (audit-friendly)

KFM emphasizes traceability with unique run identifiers + hashes so runs can be audited or replayed.  [oai_citation:54‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**Record at minimum**
- Incident ID: `INC-YYYYMMDD-###`
- Start/End times, SEV
- Impact summary + affected components
- Evidence:
  - OPA decision logs
  - Retrieval evidence bundle
  - Ledger write status
  - Deployment/policy/version identifiers
- Mitigation steps taken
- Root cause & corrective actions

> [!TIP]
> Consider attaching a `run_manifest.json` for the incident reproduction bundle (inputs, outputs, hashes).  [oai_citation:55‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 Useful diagnostics (copy/paste snippets)

> [!WARNING]
> Commands below are templates — adapt to your deployment (docker-compose, systemd, k8s). Keep least-privilege.

### Health checks
```bash
# Focus Mode endpoint (replace host/path)
curl -sS https://<host>/api/focus/health || exit 1

# OPA health
curl -sS http://<opa-host>:8181/health || exit 1
```

### Quick “golden query” (manual)
```bash
curl -sS https://<host>/api/focus \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "question":"Summarize key changes in this area between 1930 and 1940",
    "map_context":{"bbox":[-100,37,-94,40],"time_range":[1930,1940],"layers":["<layer-id>"]}
  }'
```

### Neo4j / PostGIS / index sanity (examples)
```sql
-- PostGIS: ensure spatial index exists (example)
SELECT tablename, indexname FROM pg_indexes WHERE schemaname='public' AND indexname ILIKE '%gist%';
```

```cypher
// Neo4j: sample check for orphaned PROV activities
MATCH (a:ProvActivity)
WHERE NOT (a)--()
RETURN count(a) AS orphan_activities;
```

---

## 📚 Reference library (all project files)

### Core KFM design/architecture sources used in this runbook
- 🧭🤖 **AI System Overview** — Focus Mode evidence-first, context integration, explainability & AI-layer service details.  [oai_citation:56‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:57‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🖥️ **UI System Overview** — UI surfaces provenance + citations; API decoupling.  [oai_citation:58‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:59‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 📥 **Data Intake Guide** — governance ledger logging, OPA checks, emergency procedures, agent kill switch.  [oai_citation:60‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:61‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:62‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧩 **Comprehensive Architecture** — automated policy gates, fail-closed, observability/telemetry.  [oai_citation:63‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:64‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 🧱 **Comprehensive Technical Documentation** — performance, caching, monitoring, provenance-first + “advisory-only” stance.  [oai_citation:65‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:66‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🌟 **Latest Ideas & Future Proposals** — idempotent watchers (ETag/Last-Modified), enhanced Focus Mode Q&A, rollout patterns.  [oai_citation:67‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:68‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- 💡 **Innovative Concepts** — natural language co-pilot, digital twin/AR/VR, sensitive-location protections.  [oai_citation:69‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) [oai_citation:70‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🧠 **Additional Project Ideas** — orphan detection, lag monitoring, run manifests, conceptual attention nodes, artifact signing.  [oai_citation:71‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:72‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:73‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 📦 Project reference portfolios (open in Acrobat for embedded docs)
These are included in the project as **PDF portfolios** (handy “ops reference shelf” for on-call debugging):
- 🤖 **AI Concepts & more** (portfolio) — open in Acrobat.  [oai_citation:74‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🗺️ **Maps / GoogleMaps / Virtual Worlds / WebGL** (portfolio) — open in Acrobat.  [oai_citation:75‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- 🧮 **Data Management / Architectures / Bayesian Methods** (portfolio) — open in Acrobat.  [oai_citation:76‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- 💻 **Various programming languages & resources** (portfolio) — open in Acrobat.  [oai_citation:77‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)

> [!NOTE]
> These portfolios are great for quick refreshers (Docker/Git/SQL/WebGL/GIS/ETL) during incidents, but the operational source-of-truth remains the KFM architecture + intake guides above.

---

## 🧾 TODOs for repo hardening (recommended next steps)
- [ ] Add `mcp/incidents/runbooks/opa-policy-pack.md` (OPA deny storms / policy rollout)
- [ ] Add `mcp/incidents/runbooks/data-intake.md` (ingestion lag, orphan repair, rollback)
- [ ] Add `mcp/incidents/runbooks/ledger.md` (append-only logging + audit recovery)
- [ ] Add `mcp/incidents/dashboards/focus-telemetry.md` (SLIs/PromQL seeds)
- [ ] Add a “golden queries” suite + CI smoke tests validating citation coverage
