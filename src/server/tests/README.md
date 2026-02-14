<!--
File: src/server/tests/README.md
Purpose: Server-side test guide for the KFM governed API boundary.
-->

# Server Tests (`src/server/tests`) 🧪🧭

![Layer](https://img.shields.io/badge/layer-API%20boundary-2b6cb0)
![Governed](https://img.shields.io/badge/governance-evidence--first-2f855a)
![Policy](https://img.shields.io/badge/policy-default%20deny%20(fail--closed)-c53030)
![Contracts](https://img.shields.io/badge/contracts-contract--first-805ad5)

This directory contains the **automated test suite for the KFM server/API layer** (the governed boundary that enforces *policy*, *provenance*, and *trust* guarantees).

> [!IMPORTANT]
> **If a test conflicts with a KFM invariant, the invariant wins.**  
> We would rather break a build than silently weaken governance.

---

## What lives here

**In scope**
- ✅ Unit tests for server-facing **domain + use-case** logic (pure logic; minimal I/O)
- ✅ Integration tests for **adapters** (DB, graph, storage, search) behind repository interfaces
- ✅ Contract tests for **OpenAPI/GraphQL** schemas and endpoint behavior
- ✅ Policy enforcement tests for **fail-closed** authorization and “cite-or-abstain” behavior
- ✅ Regression tests for **redaction**, **sensitivity handling**, and **evidence resolution**
- ✅ Smoke tests for **startup**, **health**, **migration**, and minimal “happy path” flows

**Out of scope (usually)**
- ❌ UI tests (belong in `web/` test strategy)
- ❌ Pipeline validation (belongs in `src/pipelines/` + `tools/` + CI data gates)
- ❌ Pure OPA/Rego unit tests (usually live under a `policy/` module)  
  ↳ This folder may include *integration* checks that policy is *called* and *enforced*.

---

## KFM invariants these tests must protect

These are **system-level contracts**. This folder’s tests exist to prevent accidental regressions.

| Invariant / Guarantee | What to test (minimum) | Typical failure mode |
|---|---|---|
| **Trust membrane** (no bypass of governed API boundary) | External callers cannot access protected data without API + policy decisions; server code does not allow “side doors” | “Debug” endpoints or direct storage URLs leak data |
| **Fail-closed policy** (default deny) | Missing/invalid auth, missing policy input fields, policy engine downtime ⇒ **deny** | “Allow on error” or “allow on missing claims” |
| **Cite-or-abstain** (Focus Mode & narrative answers) | If citations missing or sensitivity not OK ⇒ **deny/abstain** (per contract) | Model returns text without evidence; API passes it through |
| **Evidence resolvability** | Every `citation.ref` and provenance ref can be resolved to a human-readable view via governed endpoints | Citation IDs exist but can’t be dereferenced |
| **Sensitive data handling** (FAIR/CARE) | Restricted/precise data never leaves boundary without explicit grants; generalized outputs exist where required | “Precise geometry” slips into public responses |
| **Contract-first APIs** | Schema changes require contract updates + compatibility checks + tests | Silent breaking changes to endpoints |

> [!NOTE]
> Some details (exact endpoint list, exact schema keys) may vary by repo version.  
> This README treats the invariants as fixed, and the *mechanics* as implementation-defined.

---

## Quick start (run tests)

Because KFM server implementations can vary (e.g., Python/FastAPI vs Node/TS), **use the section that matches your runtime**.

### 1) Minimal prerequisites
- A working **dev environment** for the server runtime
- Optional but recommended: **Docker/Podman** for integration dependencies (PostGIS/Neo4j/OPA/etc.)
- Access to **non-sensitive test fixtures only** (synthetic or redacted)

### 2) Run unit tests only (fast loop)
Pick the closest match:

<details>
<summary><strong>Python server (pytest)</strong></summary>

```bash
# from repo root
python -m pytest -q src/server/tests/unit
```

Common variants:
```bash
python -m pytest -q src/server/tests -m "not integration"
python -m pytest -q src/server/tests/unit -k "focus_mode"
```
</details>

<details>
<summary><strong>Node/TypeScript server (Jest/Vitest)</strong></summary>

```bash
# from repo root (one of these will exist)
npm test -- --runInBand
pnpm test -- --runInBand
yarn test --runInBand
```

Target folder patterns:
```bash
npm test -- src/server/tests/unit
npm test -- -t "Focus Mode"
```
</details>

### 3) Run integration tests (requires dependencies)
Integration tests should be **opt-in** and **clearly labeled**.

Typical approaches:
- Start dependencies via `docker compose up -d` (preferred)
- Use “testcontainers”-style ephemeral services (also OK)
- Use pre-provisioned CI services (CI only)

Example patterns (adapt to repo scripts):
```bash
# start dependencies (repo root)
docker compose up -d

# run integration suite
python -m pytest -q src/server/tests/integration
# or
npm test -- src/server/tests/integration
```

> [!IMPORTANT]
> Integration tests must be:
> - deterministic
> - hermetic (no internet calls)
> - safe to run locally
> - isolated from real/prod databases

---

## Test suite map

| Suite | Goal | Speed | Uses real services? | When it runs |
|---|---:|---:|---:|---|
| `unit/` | business rules, validators, parsers, policy input shaping | ⚡ fast | ❌ no | local + CI |
| `contract/` | OpenAPI/GraphQL schema + compatibility + example I/O | ⚡ fast | ❌ no | CI gate |
| `integration/` | DB/graph/storage/search adapters + migrations | 🐢 slower | ✅ yes | CI + opt-in local |
| `e2e/` (optional) | minimal “happy path” workflows | 🐢 slowest | ✅ yes | nightly / release |
| `security/` (optional) | redaction, authZ regressions, abuse cases | ⚠️ varies | maybe | CI gate for high-risk changes |

---

## Directory layout (recommended)

> [!NOTE]
> If your repo differs, keep the **intent** and update the folders, not the intent.

```text
src/server/tests/                                   # Server test suite (API + policy + persistence + contracts)
├─ README.md                                        # How to run (local/CI), required services, markers, and triage tips
│
├─ unit/                                            # Fast, hermetic unit tests (no services/network)
│  ├─ domain/                                       # Core domain logic (entities, value objects, invariants)
│  ├─ usecases/                                     # Application/service layer logic (ports mocked, pure decisions)
│  ├─ validation/                                   # Schema + request validation helpers (error shapes, edge cases)
│  └─ policy_input/                                 # OPA input construction/normalization (stable, deterministic)
│
├─ contract/                                        # Boundary compatibility tests (specs + snapshots)
│  ├─ openapi/                                      # OpenAPI lint + compat + endpoint conformance checks
│  ├─ graphql/                                      # GraphQL schema checks (SDL snapshot, breaking changes)
│  └─ snapshots/                                    # Normalized “known-good” spec/response snapshots (diff-friendly)
│
├─ integration/                                     # Service-backed tests (compose real dependencies)
│  ├─ db_postgis/                                   # PostGIS integration (migrations, queries, geo behavior)
│  ├─ graph_neo4j/                                  # Neo4j integration (writes/reads, constraints, traversal contracts)
│  ├─ object_store/                                 # Object store integration (artifacts, manifests, digests)
│  ├─ search_vector/                                # Vector search integration (indexing, retrieval, scoring expectations)
│  └─ opa_gateway/                                  # OPA gateway integration (default-deny, redaction, decision caching)
│
├─ e2e/                                             # End-to-end tests across the full server boundary
│  └─ smoke/                                        # Minimal happy-path coverage (startup, health, core endpoints)
│
├─ fixtures/                                        # Deterministic fixtures used across server tests (synthetic + small)
│  ├─ data/                                         # Tiny dataset/test inputs (tabular/geo/etc.)
│  ├─ catalogs/                                     # STAC/DCAT fixture artifacts (valid/invalid)
│  ├─ prov/                                         # PROV/run receipt fixtures (lineage prerequisites)
│  └─ graph/                                        # Graph fixture inputs/expected outputs (nodes/edges, constraints)
│
└─ helpers/                                         # Shared server-test utilities (deterministic; no hidden I/O)
   ├─ builders/                                     # Object/DTO builders with safe defaults + overrides
   ├─ fakes/                                        # In-memory fakes for ports/adapters (no network, predictable state)
   ├─ http/                                         # Test client wrappers + request builders + auth stubs
   └─ time/                                         # Time freezing + deterministic clock helpers (TZ-safe)
```

### Naming conventions
- Test files should clearly communicate type:
  - `*.unit.test.*`
  - `*.contract.test.*`
  - `*.integration.test.*`
  - `*.e2e.test.*`
- Prefer **feature naming** over implementation naming:
  - ✅ `focus_mode_cite_or_abstain.unit.test.ts`
  - ❌ `focusControllerPrivateMethod.test.ts`

---

## Writing tests that survive refactors

### Style: Given / When / Then
Write tests like small requirements:

- **Given** a role + a resource sensitivity,
- **When** calling an endpoint or use case,
- **Then** the policy result and output shape are correct.

### Test at the boundary you own
- ✅ Test public functions, endpoints, and ports/contracts
- ⚠️ Avoid testing private helpers directly unless they encode critical domain rules
- ❌ Don’t test third-party libraries; mock at the edges

### Determinism rules
- Freeze time (don’t rely on “now”)
- Seed randomness
- Use stable IDs
- Don’t depend on external networks or live providers

---

## Fixtures & test data governance

KFM’s tests are part of the governance surface.

> [!IMPORTANT]
> **Never commit real sensitive data** (PII, precise protected locations, restricted cultural knowledge, secrets).  
> Tests must use one of:
> - synthetic fixtures
> - fully redacted fixtures
> - *generalized* geometries (coarsened resolution) when needed

### Fixture requirements
- Small (fast to load)
- Explicitly documented
- Deterministic checksums where practical
- Clearly labeled sensitivity level

Suggested fixture header (for each fixture folder):
```text
fixtures/<name>/
  ├── README.md  # what it represents, why it exists, sensitivity classification
  └── ...
```

### Redaction regression tests (required when data is sensitive)
Add tests that prove:
- public users can only receive generalized outputs
- reviewer/admin behavior matches policy and audit rules
- “downgrade” (restricted → public) cannot happen without an approved transformation step

---

## Policy enforcement tests (OPA / fail-closed)

Policy is expected to be **default deny**.

### What to verify in server tests
Even if OPA unit tests live elsewhere, server tests must verify:

- requests with **missing auth** are denied
- requests with **missing/invalid policy input** are denied
- policy engine errors/timeouts ⇒ **deny**
- policy “allow” is required before serving restricted content

### Focus Mode “cite-or-abstain”
Minimum server behavior to test:
- if `citations[]` empty or missing ⇒ deny/abstain (per contract)
- if sensitivity checks fail ⇒ deny/abstain
- audit references are included when answers are returned (and resolvable)

---

## Contract tests (OpenAPI / GraphQL)

KFM is **contract-first**: contracts are first-class artifacts.

### What to test
- Schema linting (no missing required fields, descriptions where required)
- Backwards compatibility rules (no breaking change without version bump)
- Golden request/response examples for critical endpoints (especially Focus Mode)
- Error response shape consistency (including policy denies)

> [!TIP]
> Store example payloads as fixtures and validate them against schemas in CI.

---

## Focus Mode tests (minimum acceptance criteria)

Focus Mode is a trust-critical surface. Tests here should cover:

### 1) Evidence resolution
- Given any `citation.ref` returned in a Focus answer,
- The UI must be able to resolve it to a human-readable evidence view in a small number of calls  
  (server tests verify the resolver endpoints exist and return expected shapes).

### 2) Audit record behavior
- Every permitted Focus response yields an `audit_ref` (or equivalent)
- Audit record can be retrieved (role-appropriate redaction applies)
- Audit records are append-only and hash-linked where applicable (if implemented)

### 3) No unsourced content
- If the retrieval pipeline returns insufficient evidence, the API must abstain
- If evidence exists but is sensitive and user lacks grants, the API must abstain or return generalized info

---

## CI expectations (how these tests are used)

CI typically enforces multiple gates; server tests are only one gate.

**Common CI gates relevant to this folder**
- Unit + contract tests: required on PR
- Integration tests: required for adapter changes; otherwise on demand/nightly
- Policy tests: always required when policy changes
- Secret scanning + sensitive data scanning: always required
- Story/data validation gates: required, but live outside this folder

> [!NOTE]
> If CI is failing and you’re unsure which gate you tripped, check the pipeline job name:
> - `docs` / `stories` / `data` / `policy` / `server-tests` / `build`

---

## Debugging & troubleshooting

### Run a single test
- Python:
  ```bash
  python -m pytest -svv src/server/tests/unit/test_focus_mode.py::test_cite_or_abstain
  ```
- Node:
  ```bash
  npm test -- -t "cite-or-abstain"
  ```

### Common failures
| Symptom | Likely cause | Fix |
|---|---|---|
| Tests pass locally, fail in CI | hidden dependency (timezone, locale, ordering) | freeze time; sort results; pin locale |
| Integration tests flaky | shared state between tests | isolate DB/schema per test; transactions/cleanup |
| “Allow on error” behavior slips in | error-handling path not tested | add negative tests for timeouts/errors |
| Redaction regressions | fixtures too “clean” | add fixtures with sensitive fields + assert redaction |

---

## Change checklist (Definition of Done for server changes)

When you modify `src/server/`, ensure:

- [ ] **Contract updated first** (OpenAPI/GraphQL), with compatibility considered
- [ ] **Unit tests** added/updated for domain/use-case behavior
- [ ] **Contract tests** added/updated for new/changed endpoints
- [ ] **Policy tests** updated if authZ/sensitivity behavior changed
- [ ] **Redaction tests** added if any data could be sensitive
- [ ] **Evidence resolution** still works for any returned citations
- [ ] **Fail-closed** paths covered (missing auth, missing policy fields, policy engine down)
- [ ] **No real sensitive data** added to fixtures
- [ ] CI passes (docs/data/policy gates as applicable)

---

## “Not confirmed in repo” items (verify once, then delete this section)

The KFM design docs describe a specific stack (e.g., OPA, PostGIS, Neo4j, contract-first APIs), but **your repo may vary**.

Verify and update this README based on what exists in your repository:
- Does the server runtime use **Python (FastAPI/ASGI)**, **Node/TS**, or something else?
- Where do **API contracts** live (e.g., `src/server/contracts/`)?
- Where does **OPA policy** live (e.g., `policy/`)?
- What are the canonical **test scripts** (Makefile, package scripts, tox/nox, etc.)?

Once verified, replace the “Quick start” commands with the **exact scripts** used by this repo.

---
