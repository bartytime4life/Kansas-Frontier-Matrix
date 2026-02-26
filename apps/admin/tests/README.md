<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/f2e86a04-4540-4ad4-b120-643a05ca595d
title: apps/admin/tests — Test Suite
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-26
updated: 2026-02-26
policy_label: public
related:
  - apps/admin/README.md
  - docs/governance/REVIEW_GATES.md
  - policy/README.md
tags: [kfm, admin, tests]
notes:
  - This README is intentionally conservative: update commands/paths once the admin test runner is confirmed in-repo.
[/KFM_META_BLOCK_V2] -->

# `apps/admin/tests` — Admin surface test suite

Test suite for the **Admin/Steward** surface of KFM: permissions, policy enforcement UX, and contract-level behavior that protects the trust membrane.

![status](https://img.shields.io/badge/status-draft-lightgrey)
![scope](https://img.shields.io/badge/scope-admin%20surface-blue)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)
![coverage](https://img.shields.io/badge/coverage-TODO-lightgrey)
![policy](https://img.shields.io/badge/policy-default%20deny%20tested-brightgreen)

---

## Quick links

- [What belongs here](#what-belongs-here)
- [How this fits in the repo](#how-this-fits-in-the-repo)
- [Test types and minimum coverage](#test-types-and-minimum-coverage)
- [Run tests](#run-tests)
- [Writing new tests](#writing-new-tests)
- [Fixtures and test data policy](#fixtures-and-test-data-policy)
- [CI gates](#ci-gates)
- [Troubleshooting](#troubleshooting)
- [Directory tree](#directory-tree)

---

## What belongs here

✅ **Include tests that validate the Admin app’s responsibilities**, especially around governance and safety:

- **AuthZ / role gating**: public/contributor/reviewer/steward/operator access boundaries.
- **Policy surface UX**: policy labels, obligations/notices, redaction/generalization cues.
- **Contract checks** for admin-only endpoints and workflows (promotion queue, review queues, etc.).
- **“No-leak” tests**: verify restricted metadata is not exposed in errors, logs, or UI state.

❌ **Do not** put these here:

- Backend unit tests (put them next to backend modules or in the backend test tree).
- Policy pack unit tests (OPA/Rego) — those live with the policy bundle repository.
- Shared end-to-end harnesses (e.g., Focus Mode golden query harness) — those typically live at repo-root `tests/`.

---

## How this fits in the repo

The KFM architecture treats governance as enforceable behavior:

- **Policy semantics must match in CI and runtime**. CI results are meaningless if they don’t reflect runtime enforcement.
- The **UI never makes policy decisions**; it only renders the outcomes (badges, notices, restricted states).
- Tests in this directory focus on **the Admin UI surface + its governed API interactions**, not direct DB/storage access.

### Test boundary diagram

```mermaid
flowchart LR
  AdminUI[Admin UI] --> API[Governed API]
  API --> PDP[Policy decision point]
  API --> Evidence[Evidence resolver]
  API --> Store[Data stores and indexes]

  Tests[Test suite in apps/admin/tests] --> AdminUI
  Tests --> API
  Tests --> PDP
  Tests --> Evidence
```

> NOTE: This README includes **placeholders** for runner commands and folders. Replace TODOs once you confirm the actual admin stack (e.g., Jest/Vitest/Playwright, Cypress, pytest, etc.).

---

## Test types and minimum coverage

| Test type | Goal | Examples | Runs in CI | Must block merge? |
|---|---|---|---:|---:|
| **AuthZ UI tests** | Route + component gating by role | public can’t see steward panels; steward can approve | ✅ | ✅ |
| **API contract tests** | Requests/responses match the contract + policy posture | 403/404 never leak restricted metadata; DTO schema stable | ✅ | ✅ |
| **Policy outcome UX tests** | UI renders policy labels + obligations correctly | “public_generalized” shows “geometry generalized” notice | ✅ | ✅ |
| **Audit trail tests** | Actions create auditable events | “approve promotion” emits audit_ref/run id | ✅ | ✅ |
| **Smoke tests** | “App boots” sanity | admin app loads, key routes respond | ✅ | ⚠️ recommended |

### Coverage matrix (minimum)

These scenarios should be represented at least once:

- **Default deny**: unprivileged roles are denied access to admin workflows.
- **Role escalation is impossible client-side**: changing local state cannot unlock admin functions without server authorization.
- **No restricted leakage**: responses and UI error surfaces do not reveal restricted dataset names, coordinates, or sensitive metadata.
- **Obligations render**: when policy returns obligations, the UI renders required notices (not optional).

---

## Run tests

### 1) Discover the actual runner (one-time setup)

From repo root, identify the admin test runner:

- Inspect `apps/admin/package.json` (or equivalent) for scripts like `test`, `test:ci`, `test:e2e`.
- Look for tool configs: `jest.config.*`, `vitest.config.*`, `playwright.config.*`, `cypress.config.*`, `pytest.ini`, etc.
- Confirm whether tests require **backend services** (API, DB) or run against mocks.

### 2) Common command patterns (replace with real ones)

> WARNING: These are templates. Update once confirmed in-repo.

```sh
# Option A: workspace-aware package manager (common in monorepos)
pnpm -C apps/admin test
pnpm -C apps/admin test:ci

# Option B: run inside the admin app
cd apps/admin
npm test
npm run test:ci
```

### 3) Integration / e2e mode (if applicable)

If the Admin UI tests require a running API:

```sh
# Pseudo-flow — update to match your compose/dev scripts
# 1) start backend
# 2) start admin app
# 3) run e2e suite
```

---

## Writing new tests

### Design principles (KFM-aligned)

1. **Test the boundary, not the internals**
   - Admin UI tests should prove “UI doesn’t bypass policy”: it cannot fetch or reveal restricted info without authorization.

2. **Prefer contract-first assertions**
   - If an endpoint has an OpenAPI/JSON schema, write a contract test that will fail on breaking changes.

3. **Fail closed**
   - If a test cannot safely model a restricted scenario, it should assert that the system denies or redacts by default.

4. **Golden tests for governance workflows**
   - For promotion/review workflows, keep “golden” fixtures that represent canonical cases and run them in CI.

### Suggested test naming

- `*.authz.spec.*` — role gating and forbidden transitions
- `*.contract.spec.*` — DTO and HTTP contract assertions
- `*.obligations.spec.*` — notices/badges/redaction UX
- `*.audit.spec.*` — audit trail / receipts

### PR checklist for adding/updating tests

- [ ] The test asserts behavior at the **policy boundary** (UI + governed API), not by reaching into internals.
- [ ] Fixtures are **synthetic** and contain **no PII** or restricted coordinates.
- [ ] At least one assertion covers **default deny** or **no-leak** behavior.
- [ ] Test is deterministic (no real network calls; no time-dependent assertions without a fixed clock).
- [ ] Added/updated tests run in CI and would **block merge** on regression.

---

## Fixtures and test data policy

Tests in this directory may model sensitive cases; **the fixtures must remain safe**.

### Rules

- Use **synthetic** fixtures by default.
- Never store real PII in fixtures.
- Never store exact coordinates for restricted locations — use generalized geometry (or fake data).
- Treat “policy label” as part of the fixture contract (`public`, `restricted`, `public_generalized`, etc.).
- When policy includes obligations, fixtures should include the obligation payload and the UI test must assert it is rendered.

### Example fixture shape (illustrative)

```json
{
  "user": { "role": "steward" },
  "resource": { "policy_label": "public_generalized" },
  "obligations": [
    { "type": "show_notice", "message": "Geometry generalized due to policy." }
  ]
}
```

---

## CI gates

This directory is expected to contribute to **hard merge gates**.

### Minimum gate posture

- Admin tests should run on PR and **block merge** when:
  - policy outcomes change unexpectedly,
  - contracts break,
  - restricted leakage is detected,
  - audit trail requirements regress.

### Recommended CI outputs

- JUnit / test report artifact
- Coverage report (if applicable)
- “No-leak” scan output (optional but strongly recommended)

---

## Troubleshooting

- **Flaky auth tests**: ensure user identity/role is injected via a single mechanism (fixture → API), not set ad-hoc in UI state.
- **E2E failures**: confirm backend is up, seeded with safe fixtures, and policy bundle loaded.
- **Contract drift**: regenerate clients/schemas only via the approved pipeline; update tests in the same PR.

---

## Directory tree

> PROPOSED: update this tree to match the real folder layout.

```text
apps/admin/tests/                                      # Admin app tests (authz, contracts, obligations, audit UX)
├── README.md                                          # This file (scope, commands, fixtures policy, CI mapping)
├── fixtures/                                          # Synthetic users/resources/obligations (safe + deterministic)
├── authz/                                             # Route gating + role-based UI visibility tests
├── contracts/                                         # Admin API schema/contract tests (DTOs, OpenAPI, compat checks)
├── obligations/                                       # Badges/notices/redaction UX tests (policy-driven UI behavior)
├── audit/                                             # Audit trail + run receipt UI expectations (rendering + linking)
└── e2e/                                               # Optional end-to-end flows (UI + API) for critical admin journeys
```

---

### Back to top

↑ [Quick links](#quick-links)
