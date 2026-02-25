<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2c2f2f9a-0e73-4f5a-8e7b-3c2f0d48b9d1
title: Adapters Integration Tests
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-25
updated: 2026-02-25
policy_label: public
related:
  - ../../README.md
  - ../README.md
tags: [kfm, adapters, tests, integration]
notes:
  - Generated template. Replace TODOs after confirming repo tooling (runner, scripts, compose/testcontainers).
[/KFM_META_BLOCK_V2] -->

# Adapters — Integration Tests

**Purpose:** Integration-level tests for `packages/adapters` that validate **real I/O boundaries** (DB/object-store/policy/upstream HTTP) and enforce KFM’s **trust membrane + contract posture** at the adapter edge.

**Status:** draft • **Owners:** TBD • **Scope:** adapters-only (no UI E2E)

![CI](https://img.shields.io/badge/CI-TODO-blue) <!-- TODO: replace with shields.io GitHub Actions workflow badge -->
![Coverage](https://img.shields.io/badge/Coverage-TODO-blue) <!-- TODO -->
![Policy](https://img.shields.io/badge/Policy-default--deny-important) <!-- TODO: replace with real policy badge if available -->

---

## Quick navigation

- [Purpose and scope](#purpose-and-scope)
- [How it fits in KFM](#how-it-fits-in-kfm)
- [Quickstart](#quickstart)
- [Test matrix](#test-matrix)
- [Directory layout](#directory-layout)
- [Adding or updating tests](#adding-or-updating-tests)
- [CI expectations](#ci-expectations)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## Purpose and scope

This directory contains **integration tests** that:

- exercise adapter implementations against **real dependencies** (ideally containerized)
- validate adapter behavior against **stable contracts** (ports/interfaces, schemas, policy expectations)
- catch “it worked in unit tests” failures at the **infrastructure boundary**

### What belongs here ✅

- Adapter ↔ DB integration (e.g., PostGIS/SQL repositories)
- Adapter ↔ object storage integration (read/write; checksum behavior)
- Adapter ↔ policy engine integration (default-deny, obligations surfaced)
- Adapter ↔ upstream HTTP API integration (mock server or recorded fixtures; **no internet**)

### What must NOT go here ❌

- Unit tests (put under `packages/adapters/tests/unit` or equivalent)
- UI E2E tests (Playwright/Cypress; belongs under apps/web packages)
- Load/perf tests (separate harness)
- Tests that require production credentials, production network access, or real vendor accounts
- Large datasets or sensitive artifacts checked into Git

> **WARNING:** Treat all integration tests as if they could run in CI on every PR.  
> If a test is slow/flaky, quarantine it explicitly (tag/label) rather than silently breaking the suite.

---

## How it fits in KFM

KFM’s architecture separates **core logic** from **infrastructure**. Adapters are the “edge” where that coupling is allowed—and therefore where we need the strongest integration checks.

```mermaid
flowchart LR
  subgraph Core["Core (pure)"]
    Domain["Domain models"]
    UseCases["Use cases / services"]
    Ports["Interfaces (ports)"]
    Domain --> UseCases --> Ports
  end

  subgraph Adapters["packages/adapters"]
    Impl["Adapter implementations"]
  end

  subgraph Infra["External systems (test-only)"]
    DB[(DB / PostGIS / SQL)]
    Obj[(Object store)]
    Policy[(Policy engine)]
    Http[(Upstream HTTP APIs)]
  end

  Ports --> Impl
  Impl --> DB
  Impl --> Obj
  Impl --> Policy
  Impl --> Http

  Tests["Integration tests (this dir)"] -. verify .-> Impl
  Tests -. provision .-> Infra
```

### Why we test here (KFM invariants)

- Adapters are the bridge between core logic and external systems; core logic should not talk directly to infrastructure.  
- Policy and contract checks should be enforced and fail closed at boundaries.  
- Promotion/publishing posture depends on passing contract/policy gates and producing auditable artifacts (run receipts, checksums) where applicable.

---

## Quickstart

> **TODO:** Choose the command that matches this repo’s workspace tooling and the actual `package.json` scripts.

### Prerequisites

- Node + package manager (pnpm/npm/yarn) **(confirm in repo)**
- Docker Engine (for local dependencies) **(if tests use containers)**

### Run the integration suite

```bash
# Option A: pnpm (example)
pnpm -C packages/adapters test:integration

# Option B: npm workspaces (example)
npm --workspace packages/adapters run test:integration

# Option C: yarn workspaces (example)
yarn workspace @kfm/adapters test:integration
```

### Run a single test file

```bash
# Example patterns — adapt to your runner (jest/vitest/etc.)
pnpm -C packages/adapters test:integration -- tests/integration/<something>.test.ts
```

---

## Environment and secrets

**Never** commit credentials. Prefer `.env.test` loaded by the test runner or harness.

```bash
# Example: copy a template (if present)
cp .env.test.example .env.test
```

Recommended environment variable conventions (rename to match existing config):

```dotenv
# .env.test (example ONLY — confirm real keys)
KFM_TEST_DB_URL=postgres://postgres:postgres@localhost:5432/kfm_test
KFM_TEST_OBJSTORE_ENDPOINT=http://localhost:9000
KFM_TEST_OBJSTORE_ACCESS_KEY=minioadmin
KFM_TEST_OBJSTORE_SECRET_KEY=minioadmin
KFM_TEST_POLICY_URL=http://localhost:8181
KFM_TEST_UPSTREAM_BASE_URL=http://localhost:4010
```

---

## Test matrix

> **TODO:** Replace placeholders with the adapters that actually exist in `packages/adapters/src`.

| Adapter | External dependency | Happy-path test | Failure-mode test | Notes |
|---|---|---|---|---|
| `PostGISRepository` (example) | Postgres/PostGIS container | CRUD roundtrip + geometry validity | bad creds / missing schema | isolate via per-test schema |
| `ObjectStoreAdapter` (example) | S3-compatible (MinIO) | put/get + checksum verification | missing object / access denied | no prod buckets |
| `PolicyAdapter` (example) | OPA (or equivalent) | allow/deny behavior on fixtures | default deny enforced | keep fixtures small |
| `UpstreamClient` (example) | mock HTTP server | parse + retry/backoff | 500/timeout mapping | no internet |

---

## Directory layout

> **NOTE:** This is a **recommended** layout. Update it to reflect what actually exists in this subtree.

```text
packages/adapters/tests/integration/
├── README.md
├── fixtures/                 # small, deterministic fixtures (JSON, SQL, golden files)
├── helpers/                  # test harness utilities (ports, wait-for, seeding)
├── docker/                   # optional: compose files, init scripts, migrations
│   ├── docker-compose.yml
│   └── init/
└── *.test.{ts,js}            # integration specs (name by adapter or dependency)
```

### Naming conventions (recommended)

- `*.int.test.ts` or `*.integration.test.ts` for clarity
- Group tests by adapter: `postgis.repository.integration.test.ts`, `policy.adapter.integration.test.ts`

---

## Adding or updating tests

1. **Identify the contract** being proven  
   - What interface/port is the adapter implementing?
   - What invariants must hold (timeouts, retries, schema validation, default-deny, etc.)?

2. **Provision dependencies deterministically**
   - Prefer containers (compose/testcontainers) with fixed versions
   - Use seeded fixtures/migrations
   - Avoid shared mutable state between tests

3. **Write tests to be CI-safe**
   - No internet
   - No reliance on wall-clock time (freeze time if needed)
   - Cleanup resources (DB schemas, buckets, temp files)

4. **Encode failure modes**
   - wrong credentials
   - missing upstream
   - invalid data payloads
   - policy denies by default

5. **Document any required env vars**
   - Add to `.env.test.example` (if used)
   - Add to this README’s [Environment and secrets](#environment-and-secrets)

---

## CI expectations

- Integration tests should run in CI as part of the quality gates for boundary correctness.
- If a test can’t run on every PR, it must be explicitly marked (quarantined) and justified.

**Suggested minimum Definition of Done**
- [ ] Runs locally with one command
- [ ] Runs in CI with no manual steps
- [ ] Deterministic (no flakes across 10 reruns)
- [ ] No secrets committed; no prod network calls
- [ ] Clear failure messages + troubleshooting notes

---

## Troubleshooting

### Docker/containers
- **Port already in use:** change local ports or stop conflicting containers.
- **Slow startup:** add a wait-for helper with bounded timeouts (no infinite waits).
- **Works locally, fails in CI:** check for hidden dependencies on local state (cached images, local DNS).

### Database
- **Migrations not applied:** ensure the harness applies schema before tests.
- **State leakage:** use per-test schema names or transaction rollbacks.

### Policy engine
- **Unexpected allows:** ensure default-deny is enforced and fixture inputs match the policy input schema.

---

## References

> **TODO:** Replace these with real repo-local links once confirmed.

- KFM “Definitive Design & Governance Guide (vNext)” — source-of-truth for invariants (truth path, trust membrane, cite-or-abstain).
- Promotion Contract — defines minimum gates (identity, licensing, sensitivity, catalog validation, receipts, policy/contract tests).
- Policy bundle + fixtures/tests — default-deny posture and CI-blocking policy tests.

---

<p align="right"><a href="#adapters--integration-tests">Back to top ↑</a></p>
