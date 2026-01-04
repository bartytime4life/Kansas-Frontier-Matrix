---
title: "Telemetry Tests 🧪📡"
path: "api/src/telemetry/__tests__/README.md"
status: "living"
version: "0.1.0"
last_updated: "2026-01-04"
owners:
  - "API / Telemetry"
  - "Governance"
tags:
  - telemetry
  - observability
  - governance
  - schemas
  - tests
---

# Telemetry tests 🧪📡

![Scope](https://img.shields.io/badge/scope-api%2Ftelemetry__tests-blue)
![Contract-first](https://img.shields.io/badge/contract--first-schemas%20drive%20changes-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2F%20CARE%20guardrails-important)
![CI Gate](https://img.shields.io/badge/CI-schema%20validation%20%2B%20security%20scans-critical)

This folder contains tests for the **API telemetry subsystem** — the bits that emit structured events/logs for:
- ✅ Operational observability (requests, errors, background jobs, performance)
- ✅ Governance & audit trails (sensitive access, redaction, policy blocks)
- ✅ Contract-first validation (telemetry payloads must match `schemas/telemetry/`)

> 🔎 KFM context: v13 explicitly treats contracts/schemas as first‑class artifacts, and calls out telemetry signals as part of governance (e.g., sensitive access, redaction, policy blocks) plus audit trails like `focus_mode_redaction_notice_shown`.  
> See: `docs/MASTER_GUIDE_v13.md` → **Contract-first**, **Validation gates**, **Telemetry-driven governance**, **Audit trails** 📘

---

## 📚 Table of contents

<details>
<summary><strong>Jump to…</strong> 👇</summary>

- [What we are protecting](#-what-we-are-protecting)
- [Test suites in this folder](#-test-suites-in-this-folder)
- [Recommended local commands](#-recommended-local-commands)
- [Fixtures and golden events](#-fixtures-and-golden-events)
- [Adding a new telemetry event](#-adding-a-new-telemetry-event)
- [Security & privacy checklist](#-security--privacy-checklist)
- [Troubleshooting](#-troubleshooting)
- [References](#-references)

</details>

---

## 🧭 What we are protecting

### 1) Contract-first telemetry ✅
KFM’s v13 design is **contract-first**: schemas/contracts are “first-class” and changes should trigger validation + compatibility checks. Telemetry is part of that same discipline:
- **If there’s a schema in `schemas/telemetry/`, every emitted event must validate against it.**
- If a schema changes, tests should fail until producers + fixtures are updated.

> CI is expected to run schema validation (including telemetry JSON if schemas exist) and reject non-conformant changes.  
> See: `docs/MASTER_GUIDE_v13.md` → **Validation gates** + **JSON Schema validation**.

### 2) Governance-grade audit trails 🧾
Telemetry is a governance tool, not just “logging”:
- Signals should exist for **sensitive data access**, **redaction occurring**, and **publication blocked by policy**.
- Audit trails should be strong enough to answer: **“who saw what and why”**.

> Example called out in v13 docs: an event like `focus_mode_redaction_notice_shown` when sensitive layers are withheld or generalized.  
> See: `docs/MASTER_GUIDE_v13.md` → **Audit trails**.

### 3) Operational logging/monitoring 📈
The project’s backend guidance expects logs/telemetry to capture things like:
- Per API request: method, endpoint, user id (if authenticated), params, status code, time taken
- Errors/exceptions: internal stack traces (server-side), plus an error ID for support reference
- Background tasks: step start/finish + issues
- Health checks (`/health`) and performance metrics

> See: **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** → “Logging and Monitoring”.

---

## 🧪 Test suites in this folder

> 🧠 The exact filenames will evolve — this is the *intentional structure* we keep stable.

| Suite | Goal | Typical assertions |
|---|---|---|
| **Schema validation** | Telemetry payloads validate against `schemas/telemetry/` | Required fields present, enums/format OK, no unknown keys (if strict) |
| **Event builders** | Event factory/helpers produce deterministic, minimal, compliant payloads | Stable timestamps/IDs (when mocked), sanitized fields |
| **Middleware / hooks** | API layer emits expected events for request/response lifecycle | request log contains method/route/status/latency |
| **Governance signals** | Redaction/policy decisions produce traceable audit events | redaction emits event, policy-block emits event, focus-mode notice emits event |
| **Safety regression** | Prevent accidental sensitive leakage inside telemetry | no PII, no secrets, no raw sensitive coordinates in fixtures |

---

## ▶️ Recommended local commands

Because the repo may be run via different workspace tools, the rule is:

> ✅ **Run the API package test runner, scoped to telemetry**, using the repo’s configured scripts.

Common patterns (pick the one that matches this repo’s tooling):

```bash
# Option A: monorepo / workspace style
cd api
npm test

# Option B: run from repo root (workspace-aware)
npm test

# Option C: if your runner supports pattern filtering
npm test -- telemetry
```

If you’re unsure, check:
- the root `README.md`
- the `api/package.json` scripts
- CI workflow config (what it actually runs)

---

## 🧊 Fixtures and golden events

We prefer **small, boring, explicit fixtures** over “randomly generated” payloads.

Recommended fixture layout (create if missing):

```text
📁 api/src/telemetry/__tests__/
├── 📄 README.md
├── 📁 fixtures/
│   ├── 📁 events/               # “golden” telemetry payloads
│   └── 📁 contexts/             # request/user/policy contexts used in tests
└── 📁 helpers/
    ├── 📄 fakeClock.ts          # freeze time
    ├── 📄 fakeIds.ts            # deterministic IDs
    └── 📄 testSink.ts           # capture emitted telemetry
```

**Golden event philosophy ✨**
- Keep fixtures **schema-valid** and **minimal**.
- Prefer **stable IDs/timestamps** (`fixed-now`, `req_123`, etc.).
- Never include anything that a secret/PII scanner would flag.

---

## 🧩 Adding a new telemetry event

### Step 0 — Decide if it’s telemetry vs. log
If you need:
- cross-cutting auditability ✅
- dashboards / aggregation ✅
- governance evidence ✅  
…then it’s telemetry.

### Step 1 — Add/extend the schema first (contract-first)
1. Add a new schema (or extend an existing one) under:
   - `schemas/telemetry/`

2. If schema evolution applies:
   - bump schema version
   - update compatibility notes (if your process requires it)

### Step 2 — Implement the producer
Implement event emission in the right layer:
- request/response events → API middleware / server boundary
- redaction/policy events → governance/redaction module (but emitted via telemetry)
- focus-mode audit signals → whichever boundary makes the decision

### Step 3 — Add a fixture
Add a minimal event fixture in:
- `api/src/telemetry/__tests__/fixtures/events/<event_name>.json`

### Step 4 — Add tests (minimum bar)
✅ **Must-have tests:**
- schema validation passes for the fixture
- producer emits the event in the correct condition
- payload is sanitized (no raw sensitive data)

### Definition of Done ✅
- [ ] Schema exists in `schemas/telemetry/` (or updated)
- [ ] Producer emits the event deterministically
- [ ] Fixtures added and sanitized
- [ ] Tests added covering schema + emission + privacy
- [ ] CI gates pass (schema validation + security scans)

---

## 🔒 Security & privacy checklist

Telemetry is **not** a safe place to dump payloads.

**Never include:**
- secrets (tokens, API keys, credentials)
- personal identifiers (PII) unless explicitly approved and protected
- raw sensitive coordinates or protected location details
- full request bodies (unless whitelisted + scrubbed)

**Prefer:**
- stable IDs (dataset_id, layer_id) over raw values
- classification tags & policy IDs over the sensitive content itself
- “redacted: true” + reason codes over the withheld data

---

## 🧯 Troubleshooting

### “Schema validation failed”
- A required field is missing or mis-typed
- An enum value changed
- The fixture includes fields not allowed by schema (if strict)

✅ Fix order:
1. Verify schema is correct  
2. Update producer  
3. Update fixtures  
4. Re-run tests

### “Telemetry emitted twice / not emitted”
- middleware executed twice (double registration)
- test harness not isolating instance lifecycle
- async flush not awaited

✅ Typical fix:
- ensure a single telemetry sink instance per test
- await flush/close on the sink (if supported)
- reset module state between tests

### “CI blocked by governance scans”
- fixture accidentally includes sensitive strings/coordinates
- logs contain stack traces with secrets embedded (rare but possible)

✅ Fix:
- replace fixture data with synthetic values
- add scrubbers in the telemetry builder layer

---

## 🔗 References

- 📘 `docs/MASTER_GUIDE_v13.md`  
  - Contract-first principle (schemas/contracts are first-class)  
  - Validation gates (schema validation + security scans)  
  - Telemetry-driven governance + audit trails (`focus_mode_redaction_notice_shown` example)

- 🧾 `docs/governance/`  
  - `ROOT_GOVERNANCE.md`, `ETHICS.md`, `SOVEREIGNTY.md`, `REVIEW_GATES.md`

- 🧬 `schemas/telemetry/`  
  - Telemetry event schemas (the source of truth for payload shape)

- 🧱 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  
  - Backend → Logging and Monitoring (what operational telemetry/logs should capture)

