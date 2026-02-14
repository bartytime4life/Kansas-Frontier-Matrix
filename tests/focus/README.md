# Focus Mode Tests (`tests/focus`)

🛡️ `governed` · 🚫 `fail-closed` · 🔎 `evidence-first` · 🧾 `audit-ledger` · ✅ `contract-driven`

> [!IMPORTANT]
> This directory documents the **Focus Mode test suite** and the **non-negotiable invariants** it enforces.
> If a change touches Focus Mode behavior (UI, API, policy, evidence resolution, audit logging), **these tests must pass**.
> If they don’t pass, the system must fail closed (no “best effort” answers that bypass governance).

---

## Table of contents

- [What Focus tests protect](#what-focus-tests-protect)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Directory layout](#directory-layout)
- [How to run](#how-to-run)
  - [1) Policy tests (OPA/Rego)](#1-policy-tests-oparego)
  - [2) API contract + evidence resolution checks](#2-api-contract--evidence-resolution-checks)
  - [3) UI + UX tests](#3-ui--ux-tests)
  - [4) Offline + realtime tests](#4-offline--realtime-tests)
  - [5) Accessibility tests](#5-accessibility-tests)
  - [6) Security tests](#6-security-tests)
  - [7) Load / performance tests](#7-load--performance-tests)
- [Test matrix](#test-matrix)
- [Golden-set regression suite](#golden-set-regression-suite)
- [CI gates](#ci-gates)
- [Adding a new test case](#adding-a-new-test-case)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)

---

## What Focus tests protect

Focus Mode is a governed “truth path” that sits at the intersection of:

- **Evidence retrieval** (search/graph/structured queries)
- **Policy-as-code enforcement** (default-deny, cite-or-abstain)
- **Evidence resolution UX** (citations must open a human-readable evidence view)
- **Auditability** (append-only audit logging, `audit_ref` in every response)
- **Trust membrane** (frontend never bypasses the API/policy boundary)

These tests exist to ensure that Focus Mode **does not regress into**:
- uncited answers (“hallucinations”),
- leaking sensitive information,
- non-reproducible answers,
- or UI pathways that can’t actually inspect evidence.

---

## Non-negotiable invariants

### 1) Cite-or-abstain (no exceptions)

A Focus response must be either:

**A. Answer with citations**
- `citations[]` present and non-empty, and policy approves; or

**B. Abstain with audit_ref**
- `citations: []`
- a user-safe abstention message
- `audit_ref` still present (abstention is also an audited decision)

> [!NOTE]
> “Cite-or-abstain” is enforced by **policy** and **tests**. Do not weaken it in prompts.

#### Canonical Focus endpoints

Two documents reference Focus endpoints differently. Treat the following as the **preferred** contract unless your repo explicitly defines otherwise:

- **Query**: `POST /api/v1/ai/query`
- **Evidence resolver**: `GET /api/v1/evidence/{kind}/{id}` where `kind ∈ {dcat, stac, prov, doc, graph}`

If your deployment uses a gateway alias (e.g., `/focus/query` or `/evidence/resolve`), ensure the alias maps to these contracts and update the tests’ base URL accordingly.

---

### 2) Evidence must resolve (UX acceptance criterion)

Given any `citation.ref` in a Focus answer:

- the UI must be able to resolve it into a human-readable evidence view
- in **≤ 2 API calls**

This is a hard acceptance criterion: if evidence cannot be resolved, the answer is not reviewable.

---

### 3) Policy is default-deny (fail closed)

Policy must deny by default and allow only when criteria are met (e.g., citations exist and sensitivity constraints are satisfied).

Fail closed is *required*:
- missing policy input fields → deny
- unknown citation kinds → deny
- sensitivity not OK → deny

---

### 4) Every response carries an audit reference

Every Focus response includes an `audit_ref`, including abstentions.

This enables:
- incident review,
- policy-version accountability,
- and provenance chain inspection.

---

### 5) Trust membrane is preserved

Focus Mode must never introduce:
- UI → DB shortcuts
- direct client access to restricted stores
- evidence bypass via raw storage URLs

All resolution goes through governed API endpoints.

---

## Directory layout

This is the **recommended** test organization. Some folders may be absent if a Focus sub-surface is not implemented yet; in that case, the corresponding tests should be explicitly skipped (never silently ignored).

```text
tests/focus/                                  # Focus Mode test suite (contracts + policy + UX + regression)
├─ README.md                                  # You are here: how to run, what’s gated, gold-set update rules
│
├─ fixtures/                                  # Synthetic fixtures only (no sensitive real-world payloads)
├─ golden/                                    # Gold-set regression cases (questions + context + expected outcomes)
│
├─ policy/                                    # Focus-specific OPA/Rego unit tests (cite/abstain, redaction, allow/deny)
├─ contract/                                  # HTTP-level contract tests (API responses + evidence resolution behavior)
├─ ui/                                        # UI tests for Focus surfaces (component + E2E flows)
│
├─ offline/                                   # Offline persistence + sync tests (if applicable)
├─ realtime/                                  # Realtime ordering/reconnect tests (websocket/presence; if applicable)
├─ security/                                  # Security regressions (redaction, token leakage, CSRF, header rules)
└─ perf/                                      # Performance regressions (latency, throughput, UI jank/budgets)
```

> [!TIP]
> Keep `fixtures/` and `golden/` **synthetic**. Never place restricted coordinates, private identifiers, or culturally sensitive data in repo fixtures.

---

## How to run

### Prerequisites

Minimum tools used by this test suite:

- `opa` (OPA CLI) for policy tests
- `curl` for HTTP checks
- `jq` for JSON assertions (recommended)

Optional / depending on implementation:

- `conftest` (OPA-based) if your repo uses it for PR gates
- a UI runner (e.g., Playwright/Cypress)
- a load tool (e.g., k6/vegeta)

---

## 1) Policy tests (OPA/Rego)

Policy tests should be runnable from repo root. The minimal command pattern is:

```bash
# from repo root
opa test -v ./policy
```

If your repo uses Conftest for local verification, you can also run:

```bash
# example (your policy test target may differ)
conftest test -p ./policy .
```

> [!IMPORTANT]
> Policy tests must include at least:
> - allow when citations exist AND sensitivity_ok is true
> - deny without citations
> - deny when sensitivity_ok is false
> - deny when policy input schema is malformed / missing required keys

---

## 2) API contract + evidence resolution checks

These checks validate the **runtime contract**, independent of language stack.

### Environment variables

Set:

- `KFM_API_BASE_URL` (example: `http://localhost:8000`)

```bash
export KFM_API_BASE_URL="http://localhost:8000"
```

### Smoke: Focus query returns required fields

```bash
curl -sS \
  -X POST "${KFM_API_BASE_URL}/api/v1/ai/query" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What evidence bundles are available for the current view?",
    "context": {
      "time_range": ["1850-01-01", "1900-12-31"],
      "bbox": [-102.0, 36.9, -94.6, 40.0],
      "active_layers": [],
      "story_node_id": null
    }
  }' \
| jq -e '
  .audit_ref
  and (.answer_markdown | type=="string")
  and (.citations | type=="array")
'
```

Expected:
- command exits `0`
- response includes `audit_ref`
- `citations` is always an array

### Rule: answer OR abstain (no third state)

You can enforce:
- either `citations` is non-empty,
- OR it’s an abstain response with empty citations.

```bash
curl -sS \
  -X POST "${KFM_API_BASE_URL}/api/v1/ai/query" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Give me a short summary of what is provably supported by selected evidence.",
    "context": {
      "time_range": ["1850-01-01", "1900-12-31"],
      "bbox": [-102.0, 36.9, -94.6, 40.0],
      "active_layers": [],
      "story_node_id": null
    }
  }' \
| jq -e '
  (.citations | length > 0)
  or
  ((.citations | length == 0) and (.answer_markdown | test("can.t answer|cannot answer|can not answer|Try narrowing"; "i")))
'
```

### Evidence resolution checks (contract)

For each citation:

1. Parse `kind` and `ref`
2. Convert `ref` into `{kind}/{id}`
3. `GET /api/v1/evidence/{kind}/{id}` must return 200

> [!NOTE]
> Exact parsing of `ref` depends on your citation format (`prov://...`, `stac://...`, etc).
> The contract expectation is: the **kind/id** needed to resolve evidence is unambiguous.

Example (assumes `ref` uses `${kind}://<id>` form):

```bash
resp="$(
  curl -sS -X POST "${KFM_API_BASE_URL}/api/v1/ai/query" \
    -H "Content-Type: application/json" \
    -d '{
      "question": "What can you answer from verified sources only?",
      "context": { "time_range": ["1850-01-01", "1900-12-31"], "bbox": [-102.0,36.9,-94.6,40.0], "active_layers": [] }
    }'
)"

echo "$resp" | jq -e '.audit_ref' >/dev/null

echo "$resp" | jq -r '.citations[] | "\(.kind) \(.ref)"' | while read -r kind ref; do
  id="${ref#${kind}://}"
  echo "Resolving evidence: kind=${kind} id=${id}"
  curl -sS -f "${KFM_API_BASE_URL}/api/v1/evidence/${kind}/${id}" >/dev/null
done
```

---

## 3) UI + UX tests

UI test coverage should include at least:

- FocusPanel renders `answer_markdown`
- Footnotes/citations render as interactive links
- “Review evidence” flows load the evidence resolver view
- AuditDrawer can fetch and display audit ledger entry for `audit_ref`

> [!IMPORTANT]
> UI tests must not mock away evidence resolution. Use a stubbed API if needed, but the contract must remain the same.

---

## 4) Offline + realtime tests

If your Focus feature includes offline state (e.g., local persistence, background sync, or event streams):

- offline transitions must not lose data
- background queue drains safely
- realtime presence ordering is stable
- reconnect backoff is bounded

---

## 5) Accessibility tests

Focus Mode-specific a11y pitfalls to test:

- toggling Focus Mode must not trap keyboard focus in removed DOM nodes
- an always-available “Exit Focus Mode” action must exist with an accessible name
- time/session updates must not spam screen readers

Target: WCAG 2.2 AA.

---

## 6) Security tests

Security regression tests for the Focus surface should include:

- OAuth/token storage: no tokens in logs or analytics
- CSRF protections for state-changing endpoints (if cookie-based auth)
- redaction rules for sensitive scope/content identifiers in telemetry/logging
- least-privilege enforcement (role-based access)

Use OWASP ASVS as a checklist baseline.

---

## 7) Load / performance tests

If Focus Mode increases write throughput (events/sessions/presence), measure:

- p95 latency budgets for Focus endpoints
- websocket fanout under load
- client CPU / UI jank regressions (especially timers and presence)

---

## Test matrix

This matrix is the minimum layered strategy. Each row must have a corresponding test plan, runner, and CI gate.

| Test layer | What to test | Suggested tooling | Pass/fail signals |
|---|---|---|---|
| Unit tests | State machine transitions; policy evaluation; event schemas | language-native test runners | deterministic state graph coverage |
| Component/UI tests | Panel hide/show; keyboard shortcuts; timer rendering; focus outline | component harness | no layout regressions; a11y tree stable |
| Integration tests | API contract; ETag conflict handling; JSON Patch/Merge Patch | contract tests | 412 conflicts resolved correctly |
| Offline tests | IndexedDB persistence; service worker cache; background sync queue | browser automation | no data loss on offline/online transitions |
| Realtime tests | WebSocket reconnect; presence fanout; ordering | protocol harness | no duplicate presence; bounded reconnect backoff |
| Accessibility tests | Keyboard navigation; ARIA correctness; WCAG checks | automated + manual | WCAG 2.2 AA targets met |
| Security tests | OAuth flows; token storage; CSRF protections; logging redaction | ASVS-guided | no token leakage; least-privilege validated |
| Load/perf tests | event ingestion throughput; websocket fanout; client CPU | load generators + RUM | p95 latency budgets met; no UI jank |

---

## Golden-set regression suite

A “golden set” is required for Focus Mode regression stability.

Each golden test case should capture:

- question
- ViewState/context
- expected outcome class: `answer` or `abstain`
- minimum citation count (if `answer`)
- allowed citation kinds
- sensitivity expectations (e.g., must redact or must deny)
- invariants (must include `audit_ref`; citations must resolve)

> [!IMPORTANT]
> Golden tests should avoid strict string matching on full answers; instead verify:
> - presence/absence of citations correctly,
> - evidence resolution correctness,
> - no disallowed content patterns,
> - and stable, reviewable evidence trace.

---

## CI gates

Minimum CI gates for Focus Mode changes:

- ✅ **OPA policy unit tests** (default deny; cite-or-abstain)
- ✅ **API contract tests** for `/api/v1/ai/query`
- ✅ **Evidence resolver tests** for `/api/v1/evidence/{kind}/{id}`
- ✅ **Golden-set regression suite**
- ✅ **Security regression checks** (logging redaction, token leaks)
- ✅ **Accessibility checks** for Focus UI components

> [!WARNING]
> Incident playbook rule: if unsafe Focus output occurs, the response is **disable Focus endpoint via policy**, preserve audit logs, fix policy/validator/prompt, and add a regression test that reproduces the issue.

---

## Adding a new test case

### Checklist (Definition of Done)

- [ ] Test name is descriptive and stable
- [ ] Inputs are synthetic (no restricted coordinates / private IDs)
- [ ] Expected outcome is defined (`answer` vs `abstain`)
- [ ] Evidence kinds and minimum citations are specified (when answering)
- [ ] Evidence resolution is validated (resolver returns 200)
- [ ] Policy decision is validated (deny/allow expected)
- [ ] `audit_ref` is validated (present and well-formed)
- [ ] Test runs locally and in CI
- [ ] If this change impacts governance, include a governance review note in PR description

---

## Troubleshooting

### “Policy denied” but expected allow
Common causes:
- `citations` array empty
- unknown citation `kind`
- `sensitivity_ok` false
- malformed policy input schema

Fix:
- ensure the evidence pack is built correctly
- ensure the validator sets `has_citations` and sensitivity fields correctly
- update or add OPA unit tests before relaxing any logic

### “Evidence resolver 404”
Common causes:
- invalid `ref` formatting
- resolver expects a different `id` than what citations provide
- missing catalog/provenance artifacts in the environment

Fix:
- standardize citation ref formats
- ensure the resolver endpoint accepts the citation’s `kind/id` without extra parsing

### UI can’t open “Review evidence”
Common causes:
- UI routes don’t map `kind/id` consistently
- evidence endpoint requires auth but UI doesn’t carry token
- trust membrane violation attempts (UI trying to fetch from storage URL)

Fix:
- route everything through `/api/v1/evidence/...`
- keep auth/session handling consistent
- remove any direct storage URL fetching from UI

---

## Glossary

- **FocusQuery**: request payload `{ question, context{ time_range, bbox, active_layers, story_node_id } }`
- **FocusAnswer**: response payload `{ answer_markdown, citations[], audit_ref }`
- **Citation**: a structured reference that can be resolved via evidence endpoints (`dcat|stac|prov|doc|graph`)
- **Evidence resolver**: API surface that transforms a citation ref into a human-readable evidence record
- **Audit ledger**: append-only log capturing significant actions/decisions; `audit_ref` links to entries
- **Trust membrane**: policy boundary ensuring clients never access databases or restricted stores directly

