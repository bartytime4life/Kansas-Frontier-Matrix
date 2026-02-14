# 🧪 KFM Test Suite (tests/)

![Governed](https://img.shields.io/badge/governed-artifacts-blue)
![Fail Closed](https://img.shields.io/badge/CI-fail--closed-critical)
![Evidence First](https://img.shields.io/badge/trust-evidence--first-success)
![Policy as Code](https://img.shields.io/badge/policy-OPA%2FRego-informational)

This folder documents **how KFM tests enforce trust guarantees** across the system:

- **Evidence-first** behavior (no evidence → abstain/refuse)
- **Fail-closed** CI gates (no merge/promotion if required governance artifacts fail validation)
- **Trust membrane** (frontend/external clients never access databases directly; only via governed APIs)
- **Sensitivity controls** (restricted/sensitive-location/aggregate-only handling must not regress)

> [!IMPORTANT]
> Tests are part of governance. If a change alters any governed artifact (policy, schemas, Story Nodes, catalogs, dataset manifests), **the matching test category must be updated/added** so CI remains deterministic and fail-closed.

---

## 📌 Table of contents

- [Principles & non-negotiables](#-principles--non-negotiables)
- [Acceptance criteria matrix](#-acceptance-criteria-matrix)
- [Test taxonomy](#-test-taxonomy)
- [Directory layout](#-directory-layout)
- [Quickstart: run tests](#-quickstart-run-tests)
- [Governed artifacts & validation](#-governed-artifacts--validation)
- [Policy tests (OPA/Rego)](#-policy-tests-oparego)
- [Contract tests (OpenAPI / API stability)](#-contract-tests-openapi--api-stability)
- [Pipeline & catalog tests (STAC/DCAT/PROV)](#-pipeline--catalog-tests-stacdcatprov)
- [Focus Mode regression tests (gold sets)](#-focus-mode-regression-tests-gold-sets)
- [UI trust membrane tests](#-ui-trust-membrane-tests)
- [Sensitivity regression suite](#-sensitivity-regression-suite)
- [Audit integrity tests](#-audit-integrity-tests)
- [CI mapping (required gates)](#-ci-mapping-required-gates)
- [Contributing rules & PR checklists](#-contributing-rules--pr-checklists)
- [Troubleshooting](#-troubleshooting)
- [References](#-references)

---

## 🧭 Principles & non-negotiables

### What tests must guarantee

1. **Fail closed**: If a required proof (schema validation, catalog validation, policy test, contract test) fails → **no merge**.
2. **Evidence-first**: Anything user-facing that asserts facts must carry resolvable evidence references, or abstain.
3. **Sensitivity & CARE/FAIR**: Tests must prevent disclosure regressions for restricted and sensitive-location data.
4. **Determinism**: Tests must be repeatable:
   - Pin tool versions where possible.
   - Use fixed fixtures/snapshots.
   - Avoid non-deterministic timestamps/randomness without seeding.
5. **Trust membrane**: UI and external clients do not connect to internal stores (PostGIS/Neo4j/etc.). Only the governed API gateway/policy boundary can.

> [!NOTE]
> If you’re uncertain which test type applies to a change, start from the [Acceptance criteria matrix](#-acceptance-criteria-matrix) and add the smallest test that prevents a regression in that category.

---

## ✅ Acceptance criteria matrix

The platform’s minimum acceptance criteria map to test types as follows:

| Subsystem | Acceptance criteria (must hold) | Primary test type(s) |
|---|---|---|
| **Pipeline** | Promotion blocked without valid catalogs + checksums (STAC/DCAT/PROV as applicable) | Integration + CI gate tests |
| **API** | OpenAPI contract stable under `/api/v1` (no breaking changes) | Contract tests |
| **Policy** | Default deny; allow only when policy conditions are satisfied (e.g., citations required) | OPA/Rego unit tests |
| **Focus Mode** | Citations resolve; abstain when missing evidence | Gold-set regression tests |
| **UI** | No direct DB calls; provenance/evidence views work | E2E + static analysis |

> [!IMPORTANT]
> The above criteria are treated as **release-blocking**. Any PR that touches the affected subsystem must include/adjust the corresponding tests.

---

## 🧩 Test taxonomy

| Category | Goal | Runs where | Typical scope |
|---|---|---|---|
| **Unit** | Pure logic correctness (domain + use-cases), no external systems | Local + CI | Fast, deterministic |
| **Integration** | Adapter correctness with real services (DB/graph/search/object store/OPA) | CI + local (containers) | Medium/slower |
| **Contract** | API compatibility and schema enforcement (`/api/v1` stability, response fields) | CI | Medium |
| **Policy** | OPA/Rego logic: default deny, cite-or-abstain, sensitivity rules | CI + local | Fast |
| **Data/Catalog validation** | STAC/DCAT/PROV schema + link correctness; checksums | CI + local | Medium |
| **Regression (gold sets)** | Prevent behavior drift (Focus Mode outputs, policy decisions, redaction) | CI | Medium/slower |
| **E2E** | Full user flows (UI ↔ API ↔ policy ↔ evidence resolver) | CI nightly / pre-release | Slowest |
| **Security checks** | SAST/dependency checks, secrets scanning, policy drift detection | CI | Medium |

---

## 🗂️ Directory layout

The exact layout can vary by implementation language, but KFM standardizes on these concepts:

```text
tests/                                      # KFM test suite (governed): unit → integration → contract → policy → E2E
├── README.md                               # (This file) test governance, how-to run, required env, CI mapping
│
├── unit/                                   # Fast, hermetic tests for domain logic + use-cases (no network/services)
│
├── integration/                            # Multi-component tests requiring real services (DB, API, queue, etc.)
│
├── contract/                               # Compatibility checks (OpenAPI schemas, backward-compat, client expectations)
│
├── policy/                                 # OPA/Rego policy tests + policy fixtures (fail-closed enforcement)
│
├── data/                                   # Catalog + dataset validation tests/fixtures (STAC/DCAT/PROV, manifests, checksums)
│
├── focus/                                  # Focus Mode eval harness (gold queries, citation checks, abstain behavior)
│
├── ui/                                     # UI quality gates: E2E flows + static analysis rules (lint, a11y, bundle checks)
│
├── security/                               # Security regression checks (secrets scanning, dependency policy, hardening tests)
│
├── fixtures/                               # Shared deterministic inputs/expected outputs used across test layers
│   ├── synthetic/                          # Safe synthetic data only (no restricted real records; reproducible generators)
│   ├── gold/                               # Gold sets (queries + expected outcomes; versioned + reviewed changes only)
│   └── snapshots/                          # Normalized “known-good” outputs (stable; diff-friendly; prevents churn)
│
└── helpers/                                # Shared test utilities (deterministic; avoid hidden time/randomness)
```

> [!NOTE]
> If your repo uses a different structure, keep this README accurate and retain the taxonomy above. CI should still enforce the same gates.

---

## 🚀 Quickstart: run tests

Because KFM can be implemented in different stacks (Go / Node / Python, etc.), we define a **tool-oriented** runbook. Use the commands that match the tooling present in your repo.

### 1) Fast local checks (no containers)

Run these before opening a PR:

- **Unit tests** (choose the one your repo uses):
  - Go: `go test ./...`
  - Node: `npm test` or `pnpm test`
  - Python: `pytest -q`

- **Policy unit tests**:
  - OPA: `opa test ./policy -v`
  - Conftest: `conftest test ./policy -p ./policy`

- **Governed document validation** (Story Nodes + governed Markdown):
  - If your repo has a validator CLI, run it (examples):
    - `./scripts/validate-docs.sh`
    - `npm run validate:docs`
    - `python -m kfm_validate docs stories`

> [!TIP]
> The “fast checks” should finish in a few minutes and catch most PR-level issues early.

### 2) Full suite (integration + contract + gold sets)

Integration tests require a local service stack (commonly via containers). Start your stack (example):

```bash
docker compose up -d --build
```

Then run:

- **Integration tests** (examples):
  - Go: `go test ./... -tags=integration`
  - Node: `npm run test:integration`
  - Python: `pytest -m integration`

- **Contract tests**:
  - OpenAPI schema validation + compatibility checks (see [Contract tests](#-contract-tests-openapi--api-stability))

- **Focus Mode gold-set regression**:
  - Run the Focus Mode evaluation harness (see [Focus Mode regression tests](#-focus-mode-regression-tests-gold-sets))

Stop services when done:

```bash
docker compose down -v
```

> [!IMPORTANT]
> If your tests require credentials (e.g., API keys), use **local env files** and CI secrets. Never commit secrets.

---

## 📜 Governed artifacts & validation

KFM treats these as governed and therefore testable:

- **Story Nodes**: schema + required headings + citations + link hygiene
- **Policy packs** (OPA/Rego): must compile + pass unit tests
- **Catalog outputs**: STAC/DCAT/PROV validation + checksums
- **OpenAPI contract**: `/api/v1` stability guarantees + non-breaking diffs
- **Evidence bundles**: resolvable refs; audit linkage; stable content hashes

### Recommended validation style

- Prefer **schema validation** over ad-hoc parsing.
- Prefer **golden fixtures** for outputs that must not drift.
- Prefer **negative tests** for forbidden outcomes (e.g., leakage of restricted fields).

---

## 🛡️ Policy tests (OPA/Rego)

Policy is enforced with a **default deny** posture; tests must prove the allow cases and deny cases.

### What to test

- **Default deny**: missing/invalid policy input → deny
- **Cite-or-abstain**: if a response has no citations → deny/abstain
- **Sensitivity gates**: restricted/sensitive-location/aggregate-only must not leak
- **Role-based access**: only authorized roles can access restricted assets

### How to run

Using OPA directly:

```bash
opa test ./policy -v
```

Using Conftest:

```bash
conftest test ./policy -p ./policy
```

### Test design rules

- Keep policy tests **table-driven** and minimal.
- Include both:
  - **Allow** tests (positive)
  - **Deny** tests (negative)
- Include tests for **missing keys** (fail-closed behavior).

---

## 📜 Contract tests (OpenAPI / API stability)

KFM’s API contract under `/api/v1` must remain stable. Contract tests enforce:

- schema validity (OpenAPI parses + validates),
- response shape invariants for core endpoints,
- and **no breaking changes** in `/api/v1`.

### Recommended contract test components

1. **OpenAPI lint/validate**
   - Ensure OpenAPI is valid and references exist.
2. **Breaking-change detection**
   - Run an OpenAPI diff against the main branch (or last release tag).
3. **Runtime contract checks**
   - Run a tool that generates requests from OpenAPI and validates responses.

### Common tool choices (pick one, pin versions)

- `schemathesis` (OpenAPI-driven runtime testing)
- `openapi-diff` style tools (breaking-change checks)
- Custom JSON Schema validators

> [!IMPORTANT]
> If you must make a breaking API change, do it in `/api/v2` (or equivalent) and keep `/api/v1` compatible.

---

## 🗺️ Pipeline & catalog tests (STAC/DCAT/PROV)

These tests ensure that promotion/publishing is blocked unless required catalogs and checksums are present and valid.

### Minimum required validations

- **STAC** (for spatial assets): collections/items validate; asset links are coherent
- **DCAT**: dataset metadata exists (license/attribution/sensitivity labels)
- **PROV**: lineage links raw inputs to processed outputs and records transformations
- **Checksums**: promoted assets have deterministic checksums recorded and verified

### Test styles

- **Schema validation tests**: run validators on fixtures
- **Golden file tests**: compare normalized output to expected snapshots
- **Integration slice tests**: ingest a fixed small slice and assert stable counts/checksums

---

## 🧠 Focus Mode regression tests (gold sets)

Focus Mode must be **evaluable** and **non-regressing**.

### What gold-set tests must assert

- For questions requiring evidence: responses contain citations and pass policy checks.
- For questions with insufficient evidence: responses **abstain** (do not hallucinate).
- Citation references are **resolvable** to evidence views (the UI can resolve a `citation.ref` efficiently).
- Outputs respect sensitivity gates and never leak restricted data.

### Suggested gold-set format

Use a structured file format that is easy to diff in PRs (YAML/JSON). Example fields:

- `id`: stable identifier
- `question`: prompt/query
- `view_state`: bbox/time range/layers context (if applicable)
- `expected`:
  - `allowed`: true/false
  - `must_abstain`: true/false
  - `min_citations`: integer
  - `deny_reasons`: list of expected policy reasons (if denied)

> [!NOTE]
> Gold sets are not “model outputs you like.” They are **regression contracts** that codify evidence + policy requirements.

---

## 🧱 UI trust membrane tests

UI must not bypass the governed API boundary.

### What to enforce

- No database connection strings in frontend code.
- No direct calls to PostGIS/Neo4j/search stores from the UI.
- All data retrieval flows:
  - UI → governed API → (policy decision + stores) → API response → UI rendering.

### Test mechanisms

- **Static analysis**:
  - Grep rules / lint rules for forbidden imports and forbidden URLs/ports.
- **E2E tests**:
  - Validate provenance/evidence panels work.
  - Validate citations render and evidence resolver endpoints are hit (not DB).

---

## 🔒 Sensitivity regression suite

KFM treats some data as sensitive and requires redaction + non-regression checks.

### Sensitivity classes (common baseline)

- **Public**: safe to publish without redaction
- **Restricted**: requires role-based access (e.g., parcel ownership)
- **Sensitive-location**: coordinates must be generalized/suppressed (e.g., archaeology, sensitive species)
- **Aggregate-only**: only publish above thresholds (e.g., small health/crime counts)

### Required regression tests

1. **Golden queries**
   - Queries that previously leaked restricted fields must fail forever.
2. **Negative tests**
   - Unauthorized roles must not receive high-precision sensitive-location output.
3. **Field-level tests**
   - Verify restricted fields (owner names, exact archaeology coordinates, small counts) are redacted/suppressed.
4. **Audit integrity**
   - Every API response includes audit reference and evidence bundle hash.

> [!IMPORTANT]
> The sensitivity suite must include **deny cases**. Passing tests must *prove* the system refuses/abstains/redacts correctly.

---

## 🧾 Audit integrity tests

Auditability is a trust requirement.

### What to test

- Responses that contain data or claims include:
  - an `audit_ref` (or equivalent audit reference)
  - an evidence bundle/content hash reference (or equivalent)
- Audit entries are:
  - present for the request
  - linked to the policy bundle/version used (if available)
  - linked to citations/evidence references

### Recommended test approach

- Add contract tests asserting required audit fields exist on responses.
- Add integration tests that fetch the audit record and validate linkage:
  - request → audit record → evidence bundle references.

---

## 🧰 CI mapping (required gates)

CI should enforce (at minimum):

1. ✅ Governed Markdown + Story Node validation
2. ✅ STAC/DCAT/PROV validation for new/changed datasets
3. ✅ OPA/Rego policy tests (default deny; cite-or-abstain)
4. ✅ OpenAPI contract tests for `/api/v1`
5. ✅ Focus Mode gold-set regression suite
6. ✅ UI trust membrane static analysis + selected E2E checks
7. ✅ Sensitivity regression suite + audit integrity tests

> [!TIP]
> Keep “fast checks” on every PR, and move heavier E2E/perf checks to nightly/pre-release—**but do not weaken the fail-closed gates** for governed artifacts.

---

## 🤝 Contributing rules & PR checklists

### PR checklist (all PRs)

- [ ] Added/updated tests matching the subsystem(s) changed
- [ ] No secrets in code/logs/fixtures
- [ ] Deterministic outputs (seed randomness, freeze time where needed)
- [ ] Link hygiene (no broken internal references)

### If your PR changes policy (OPA/Rego)

- [ ] Added/updated policy unit tests proving allow + deny behavior
- [ ] Updated sensitivity regression tests if affected
- [ ] Confirmed default-deny posture preserved

### If your PR changes OpenAPI or endpoints

- [ ] Updated contract tests
- [ ] Proved `/api/v1` remains compatible (or created `/api/v2` for breaking change)
- [ ] Updated audit integrity expectations if response shape changed

### If your PR adds/updates a dataset integration

- [ ] Added catalog fixtures (DCAT always; STAC/PROV as applicable)
- [ ] Added validator tests (schema + checksums)
- [ ] Added sensitivity labels + redaction tests if needed
- [ ] Added at least one representative API contract test query

### If your PR changes Focus Mode behavior

- [ ] Updated/added gold-set tests
- [ ] Verified abstention behavior when evidence is missing
- [ ] Verified citations remain resolvable and policy allows only with citations

---

## 🧯 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Policy tests deny everything | Missing input keys or default-deny rule hit | Add required input keys to fixtures; keep deny-by-default but prove allow cases |
| STAC/DCAT/PROV validation fails | Missing required fields, invalid geometry/time, bad links | Fix catalogs; regenerate fixtures; ensure checksums match |
| Contract tests fail on `/api/v1` | Breaking change introduced | Restore compatibility; move breaking change to `/api/v2` |
| Gold-set regressions | Behavior drift in Focus Mode or retrieval | Confirm drift is intended; update gold sets *only* with governance review for sensitive impacts |
| UI membrane test fails | Frontend attempted to call DB/service directly | Route via governed API; remove forbidden endpoints/imports |

---

## 📚 References

Internal KFM documents that define test expectations:

- **KFM Next-Gen Blueprint and Primary Guide (v1.2)** — CI minimal hardening, acceptance criteria matrix, policy-as-code patterns, Focus Mode cite-or-abstain.
- **KFM Data Source Integration Blueprint (v1.0)** — sensitivity classes, redaction as transformation, CI policy regression suite, audit integrity expectations.
- **KFM Integration Report (New Ideas 2-8-26)** — normalization notes for spec hashing and governance gaps (useful for reproducibility tests).

External standards frequently used in validation:

- STAC (OGC community standard)
- DCAT (W3C)
- PROV (W3C)
- OPA / Rego (Open Policy Agent)

---

<details>
  <summary><strong>FAQ: Why do we treat tests as governance artifacts?</strong></summary>

Because KFM’s core value is *trust*. Tests are the automated enforcement mechanism for:
- provenance completeness,
- evidence-first behavior,
- policy correctness,
- and preventing sensitivity leaks.

A “green build” is not merely “code works” — it is “the governed system still satisfies its trust contract.”

</details>
