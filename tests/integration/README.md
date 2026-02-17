# Integration Tests (KFM)

![Governed](https://img.shields.io/badge/Governed-yes-2b6cb0)
![Evidence-first](https://img.shields.io/badge/Evidence--first-yes-2f855a)
![Fail-closed](https://img.shields.io/badge/Gates-fail--closed-c53030)

This directory contains **integration tests** for the Kansas Frontier Matrix (KFM) platform.

Integration tests validate KFM’s governed behavior **across real dependencies** (datastores, policy engine, catalog validators, provenance/attestation tooling) while preserving KFM’s **trust membrane**: external clients only interact with the system through governed APIs and published contracts.

> [!IMPORTANT]
> **Integration tests are allowed to stand up and inspect infrastructure, but the application code under test must not bypass repository interfaces or the governed API boundary.**
>
> In other words: tests can “look behind the curtain” to assert outcomes, but production code must not.  
> (If a test requires DB access from inside the service under test, that’s usually a missing port/interface.)

---

## What “integration” means in KFM

| Test type | Where | Goal | Typical runtime |
|---|---|---|---|
| Unit | `tests/unit/` | Pure logic (domain + use-case rules) | seconds |
| Integration | `tests/integration/` | Verify ports/adapters, policy gates, contracts, catalog/provenance behavior with **real services** | minutes |
| End-to-end (UI) | `tests/e2e/` | Verify user flows (Map UI / Focus Mode UI) in a browser | minutes–tens of minutes |

---

## Suggested directory layout

> [!NOTE]
> This is a **recommended** layout. Keep it tidy, but adapt it to match the repo’s actual stack and tooling.

```text
tests/
└── integration/
    ├── README.md
    ├── compose/                     # Test stack orchestration (Docker/Podman)
    │   ├── docker-compose.yml
    │   └── .env.example
    ├── api/                         # HTTP-level tests: /api/v1/* behavior + policy
    ├── contracts/                   # OpenAPI + GraphQL contract checks (diff + conformance)
    ├── policies/                    # OPA/Rego policy tests (conftest) + fixtures
    ├── catalogs/                    # STAC/DCAT/PROV validation tests
    ├── graph/                       # Neo4j “graph QA” checks (Cypher) + runner
    ├── pipelines/                   # Run a tiny lane end-to-end on synthetic fixtures
    ├── fixtures/
    │   ├── synthetic/               # Synthetic, non-sensitive seed inputs
    │   └── golden/                  # Golden expected outputs / snapshots
    └── scripts/                     # Bring-up / teardown helpers for local dev + CI
        ├── up.sh
        ├── down.sh
        └── reset.sh
```

---

## Test stack

Integration tests should run against a **local, disposable stack**.

Recommended services (adjust as needed):

| Service | Why it exists in integration tests |
|---|---|
| API service (your implementation) | System-under-test: governed endpoints, policy checks, evidence resolver |
| Postgres + PostGIS | Spatial storage + queries |
| Neo4j | Provenance/lineage graph + “graph QA” gates |
| Policy engine (OPA via `conftest` and/or sidecar) | Fail-closed allow/deny decisions for promotion + runtime exposure |
| Local object store (e.g., MinIO) | Simulate versioned bundles/artifacts (COG/PMTiles/GeoParquet/media) |
| Search (optional) | Contract tests for discovery endpoints, indexing behavior |

> [!TIP]
> Keep integration fixtures **tiny**. If the test stack is slow, tests will be skipped and governance will rot.

---

## Running integration tests locally

### 1) Prerequisites

- Container runtime: **Docker** or **Podman**
- A test runner for your stack (examples below):
  - Python: `pytest`
  - Node: `jest` / `vitest`
- Policy tooling (recommended): `opa` + `conftest`
- Catalog validators (recommended): `pystac`, `stac-check`, JSON Schema tooling

### 2) Bring up the stack

From the repo root:

```bash
cd tests/integration/compose
docker compose up -d --build
```

If you use Podman:

```bash
cd tests/integration/compose
podman compose up -d --build
```

### 3) Run the tests

<details>
<summary><strong>Python example</strong> (pytest)</summary>

```bash
# fast path: run only integration-marked tests
pytest -m integration -q

# run a single file
pytest tests/integration/api/test_health.py -q

# run with live logs
pytest -m integration -q -s
```
</details>

<details>
<summary><strong>Node example</strong> (jest/vitest)</summary>

```bash
# npm
npm run test:integration

# pnpm
pnpm test:integration
```
</details>

### 4) Tear down

```bash
cd tests/integration/compose
docker compose down -v
```

---

## What we test here

Integration tests are where KFM proves it is **governed and auditable**, not just “working”.

### Suites (recommended)

| Suite | Primary assertions | Examples |
|---|---|---|
| `api/` | API semantics, authz/authn posture, policy denies, evidence resolver behavior | `/api/v1/*` contract, deny-by-default responses when missing rights/consent |
| `contracts/` | No breaking changes without versioning | OpenAPI diff; GraphQL schema checks; consumer-driven contract fixtures |
| `policies/` | **Fail-closed** policy behavior on promotion/exposure manifests | Missing license → deny; missing consent facet → deny; expired consent → deny |
| `catalogs/` | Catalog outputs validate (STAC/DCAT/PROV) | `pystac validate …`; DCAT JSON-LD shape checks; PROV bundle required fields |
| `graph/` | Graph invariants hold before promotion | Missing attestation → fail; duplicate asset href collisions → fail; digest mismatches → fail |
| `pipelines/` | A tiny lane can run end-to-end deterministically | Same inputs → same digests; run receipt always emitted; promotion blocked when proofs missing |

---

## CI gate order (reference)

This is the typical order you want in CI so failures are fast, explainable, and “fail-closed”.

```mermaid
flowchart LR
  PR[Pull Request] --> Lint[Lint + formatting]
  Lint --> Schema[Schema validation<br/>(STAC/DCAT/PROV/Story Node)]
  Schema --> Policy[Policy gates<br/>(OPA/Rego + Conftest)]
  Policy --> Contract[Contract checks<br/>(OpenAPI / GraphQL)]
  Contract --> GraphQA[Graph QA<br/>(Neo4j Cypher)]
  GraphQA --> ITest[Integration tests<br/>(API + pipelines)]
  ITest --> Reports[Publish machine-readable reports<br/>(gate results, artifacts, logs)]
```

> [!IMPORTANT]
> CI should **block merges** on any governance violation (schema/policy/provenance/attestation), not just failing unit tests.

---

## Fixtures and test data governance

> [!CAUTION]
> **Do not commit sensitive locations or restricted cultural knowledge** into test fixtures.
>
> - Prefer fully synthetic fixtures.
> - If you must use real-world shapes, generalize them (coarser geometry, bounding boxes, or aggregated grids).
> - Treat fixtures as publishable artifacts: licenses and provenance still apply.

Recommended fixture conventions:

- `tests/integration/fixtures/synthetic/…`  
  Small, invented datasets that represent edge cases.
- `tests/integration/fixtures/golden/…`  
  Expected outputs (digests, receipts, catalogs) used for snapshot-style assertions.

---

## Adding a new integration test

### Quick checklist

- [ ] The test exercises **a contract** (API response shape, schema, or policy decision), not an implementation detail.
- [ ] The test is **deterministic** (pinned inputs; stable seeds; no time-based flakiness).
- [ ] The test leaves the stack **clean** (idempotent setup/teardown).
- [ ] The test produces artifacts that help debugging (logs, manifests, receipts).
- [ ] If the test touches governed data concepts: rights/CARE/sensitivity fields are present and asserted.

### Pattern: “Given / When / Then” with evidence

1. **Given** a minimal fixture input + a policy configuration  
2. **When** the system runs a lane / serves an endpoint  
3. **Then** the output includes:
   - valid catalogs (STAC/DCAT/PROV),
   - a run receipt / provenance link,
   - and the expected allow/deny decision with reasons.

---

## Troubleshooting

<details>
<summary><strong>Common failure modes</strong></summary>

- **Flaky tests due to time:** freeze time or pass explicit timestamps in fixtures.
- **Schema failures:** validate fixtures first; keep schemas versioned and referenced in tests.
- **Policy failures:** print conftest decision outputs (deny reasons) to the test log.
- **Graph QA failures:** export the minimal subgraph (nodes/edges) for the failing invariant.
- **Port collisions:** ensure compose uses dynamic host ports (or document fixed ports in `.env.example`).

</details>

<details>
<summary><strong>Reset everything</strong></summary>

```bash
cd tests/integration/compose
docker compose down -v
docker compose up -d --build
```
</details>

---

## Related paths (expected; adjust if your repo differs)

- `schemas/` — JSON Schemas for STAC/DCAT/PROV/story nodes/UI
- `tools/validation/` — validators and CI gate runners (catalog, policy, graph QA)
- `.github/workflows/` — CI workflows that run gates and publish reports