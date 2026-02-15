<!--
GOVERNED ARTIFACT NOTICE
This README defines KFM test governance. Tests are part of the trust boundary.
If you change meaning (not just phrasing), route through governance review (CODEOWNERS + CI gates).
-->

# 🧪 KFM Test Suite (`tests/`)

![Governed](https://img.shields.io/badge/governed-artifacts-critical)
![Fail-closed](https://img.shields.io/badge/fail--closed-required-111827)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-0f766e)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-enforced-16a34a)
![Policy-as-code](https://img.shields.io/badge/policy-OPA%2FRego-2563eb)
![Receipts](https://img.shields.io/badge/receipts-run__manifest%20%7C%20spec__hash-6a5acd)
![Catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-2563eb)
![Cite or abstain](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-critical)

This folder documents how KFM tests enforce trust guarantees across the system:

- evidence-first behavior (no evidence → abstain/deny)
- fail-closed CI gates (no merge/promotion if required governance artifacts fail)
- trust membrane (UI/external clients never access DBs directly)
- sensitivity controls (restricted/sensitive-location/aggregate-only must not regress)
- deterministic specs/receipts (`spec_hash`) and promotion proofs (run manifests + checksums)
- audit integrity (every governed response has `audit_ref` and resolvable evidence refs)

> [!IMPORTANT]
> Tests are part of governance. If a change alters any governed artifact (policy, contracts/schemas, Story Nodes, catalogs, receipts, dataset manifests),
> the matching test category must be updated/added so CI remains deterministic and fail-closed.

---

## 📌 Table of contents

- [Governance header](#governance-header)
- [Principles & non-negotiables](#principles--non-negotiables)
- [Acceptance criteria matrix](#acceptance-criteria-matrix)
- [Test taxonomy](#test-taxonomy)
- [Directory layout](#directory-layout)
- [Quickstart: run tests](#quickstart-run-tests)
- [Governed artifacts & validation](#governed-artifacts--validation)
- [Policy tests (OPA/Rego)](#policy-tests-oparego)
- [Receipt & promotion tests (run manifests, checksums, spec_hash)](#receipt--promotion-tests-run-manifests-checksums-spec_hash)
- [Contract tests (OpenAPI / API stability)](#contract-tests-openapi--api-stability)
- [Pipeline & catalog tests (DCAT/STAC/PROV)](#pipeline--catalog-tests-dcatstacprov)
- [Evidence resolver contract tests](#evidence-resolver-contract-tests)
- [Focus Mode regression tests (gold sets)](#focus-mode-regression-tests-gold-sets)
- [UI trust membrane tests](#ui-trust-membrane-tests)
- [Sensitivity regression suite](#sensitivity-regression-suite)
- [Audit integrity tests](#audit-integrity-tests)
- [CI mapping (required gates)](#ci-mapping-required-gates)
- [Contributing rules & PR checklists](#contributing-rules--pr-checklists)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## Governance header

| Field | Value |
|---|---|
| Document | `tests/README.md` |
| Status | **Governed** |
| Applies to | test taxonomy, required gates, fail-closed behaviors, regression baselines |
| Version | `v2.0.0-draft` |
| Effective date | 2026-02-15 |
| Owners | `.github/CODEOWNERS` *(required; if missing, treat as governance gap)* |
| Review triggers | any change affecting required gates, deny-by-default semantics, sensitivity leak protections, contract stability expectations |

---

## Principles & non-negotiables

### What tests must guarantee

1) **Fail closed**  
If a required proof fails (schema validation, receipt validation, catalog validation, policy test, contract test) → no merge and no promotion.

2) **Evidence-first**  
User-facing factual outputs must carry resolvable evidence references or abstain/deny.

3) **Sensitivity & CARE/FAIR**  
Tests must prevent disclosure regressions for restricted and sensitive-location data.

4) **Determinism**  
Tests must be repeatable:
- pin tool versions where possible
- use fixed fixtures/snapshots
- seed randomness; freeze time where needed

5) **Trust membrane**  
UI and external clients never connect to internal stores directly (PostGIS/Neo4j/search/object store). Only the governed API/policy boundary can.

> [!NOTE]
> If unsure which test applies, start from the acceptance criteria matrix and add the smallest test that prevents the regression.

---

## Acceptance criteria matrix

| Subsystem | Acceptance criteria (must hold) | Primary test type(s) |
|---|---|---|
| Promotion | promotion blocked without receipts + checksums + catalogs (DCAT always; STAC conditional; PROV required) | receipts + catalog integration tests |
| API | `/api/v1` contract stable (no breaking changes) | OpenAPI diff + contract tests |
| Policy | default deny; allow only when conditions satisfied | OPA/Rego unit + conftest regression |
| Evidence | citation refs resolvable (or deny safely) in bounded calls | evidence resolver contract tests |
| Focus Mode | cite or abstain; never bluff | gold-set regression |
| UI | no direct DB calls; evidence UX works | static analysis + E2E smoke |
| Audit | every governed response has `audit_ref` and evidence linkage | contract + integration tests |

> [!IMPORTANT]
> These criteria are release-blocking. PRs touching the subsystem must include/adjust the corresponding tests.

---

## Test taxonomy

| Category | Goal | Runs where | Typical scope |
|---|---|---|---|
| Unit | pure logic correctness (domain/use-cases), no external systems | local + CI | fast |
| Integration | adapters + real services (DB/graph/search/object store/OPA) | CI + local (containers) | medium/slower |
| Contract | API compatibility + schema enforcement (`/api/v1` stability) | CI | medium |
| Policy | OPA/Rego logic: default deny, cite-or-abstain, sensitivity rules | CI + local | fast |
| Receipts | run_manifest/run_record schema + checksum + spec_hash semantics | CI + local | fast/medium |
| Data/Catalogs | DCAT/STAC/PROV validation + cross-links + checksums | CI + local | medium |
| Regression (gold sets) | prevent behavior drift (Focus Mode, policy decisions, redaction) | CI | medium/slower |
| E2E | full user flows (UI ↔ API ↔ policy ↔ evidence) | nightly / pre-release | slowest |
| Security | dependency/secret scanning, hardening baselines | CI | medium |

---

## Directory layout

Exact layout can vary by language/tooling, but KFM standardizes these concepts:

```text
tests/
├─ README.md                      # this file
│
├─ unit/                          # hermetic unit tests (no services/network)
├─ integration/                   # service-backed integration tests (DB/OPA/etc.)
├─ contract/                      # OpenAPI validity + compatibility tests
├─ policy/                        # OPA/Rego tests + fixtures (deny-by-default)
├─ receipts/                      # run_record/run_manifest + spec_hash + checksum tests
├─ data/                          # DCAT/STAC/PROV validation fixtures + catalog/dataset checks
├─ evidence/                      # evidence resolver contract tests (ref → view, deny safely)
├─ focus/                         # Focus Mode eval harness + gold sets
├─ ui/                            # E2E UI tests + static analysis rules (trust membrane)
├─ security/                      # security regression checks (deps, secrets, baselines)
│
├─ fixtures/                      # shared deterministic fixtures
│  ├─ synthetic/                  # synthetic only (no restricted real records)
│  ├─ gold/                       # gold sets (reviewed changes only)
│  └─ snapshots/                  # normalized stable outputs (diff-friendly)
│
└─ helpers/                       # shared helpers (deterministic; no hidden time/randomness)
```

> [!NOTE]
> If your repo differs, keep this README accurate and retain the taxonomy. CI should still enforce the same gates.

---

## Quickstart: run tests

Because KFM can be implemented in different stacks (Go/Node/Python), use the commands your repo supports.

### Fast local checks (no containers)
Run before opening a PR:
- unit tests (Go/Node/Python depending on repo)
- policy tests (`opa test` and/or `conftest test`)
- docs/story validators (if present)

### Full suite (integration + contract + gold sets)
Start services (example):
```bash
docker compose up -d --build
```

Then run:
- integration tests
- contract tests (OpenAPI)
- receipts/catalog validations
- Focus Mode gold-set regression
- UI trust membrane checks (static + smoke E2E)

Stop services:
```bash
docker compose down -v
```

> [!IMPORTANT]
> Use local env files and CI secrets for credentials. Never commit secrets.

---

## Governed artifacts & validation

Governed artifacts are testable and must not drift silently:
- Story Nodes (template + citations + link hygiene)
- policy packs (OPA/Rego must compile and pass tests)
- receipts (run_record/run_manifest schema + spec_hash semantics)
- catalogs (DCAT always; STAC/PROV where applicable)
- OpenAPI contracts (`/api/v1` stability)
- evidence resolver behavior (resolvable refs or safe denial)
- audit linkage (audit_ref present, evidence refs attached)

Recommended validation style:
- prefer schema validation over ad-hoc parsing
- prefer golden fixtures for outputs that must not drift
- prefer negative tests for forbidden outcomes (leaks)

---

## Policy tests (OPA/Rego)

Policy is default deny. Tests must prove allow and deny cases.

### What to test
- default deny: missing/invalid policy input → deny
- cite-or-abstain: missing citations → deny/abstain
- sensitivity gates: restricted/sensitive-location/aggregate-only must not leak
- role-based access: only authorized roles can access restricted assets

### How to run (examples)
```bash
opa test ./policy -v
conftest test . -p policy/conftest
```

### Design rules
- table-driven tests
- include missing-keys tests (fail closed)
- include regression denies for known leak patterns

---

## Receipt & promotion tests (run manifests, checksums, spec_hash)

Promotion is blocked unless receipts and proofs validate.

### What to test
- `run_record.json` schema validity + required fields
- `run_manifest.json` schema validity (Promotion Contract receipt)
- checksums exist and match artifacts
- `spec_hash` semantics: `sha256(JCS(spec))` (RFC 8785 canonical JSON) when applicable
- catalogs referenced by receipts exist and validate

### Negative tests (required)
- missing license/sensitivity → fail promotion
- missing receipt keys → fail promotion
- checksum mismatch → fail promotion
- missing catalogs (DCAT/PROV) → fail promotion

---

## Contract tests (OpenAPI / API stability)

`/api/v1` must remain stable.

### What to test
- OpenAPI validates and references resolve
- breaking-change detection against baseline (main branch or last release tag)
- runtime contract checks for critical endpoints (catalogs, evidence resolve, Focus Mode output schema)

> [!IMPORTANT]
> Breaking changes belong in `/api/v2` (or equivalent), not `/api/v1`.

---

## Pipeline & catalog tests (DCAT/STAC/PROV)

These tests ensure promotion/publishing is blocked unless required catalogs and checksums are present and valid.

### Minimum validations
- DCAT exists and validates (license/attribution/restrictions present)
- STAC validates when spatial assets exist (collections/items/assets coherent)
- PROV validates (raw → processed lineage recorded)
- catalogs cross-link cleanly (no dangling refs)
- checksums/digests match declared artifacts

### Test styles
- schema validation against fixtures
- golden snapshot tests for normalized catalog output
- integration slice tests (tiny fixed slice → stable digests + counts)

---

## Evidence resolver contract tests

Evidence must be reviewable. Refs must resolve or deny safely.

### What to test
- `prov://`, `stac://`, `dcat://`, `doc://`, `graph://` (and optionally `oci://`) resolve to a human-readable view
- unauthorized access returns 403 (non-leaky)
- missing refs return 404
- resolver responses include required metadata (license/attribution, ids/digests where available)

### Acceptance criterion
- a citation ref can be resolved in a bounded number of calls (UI requirement); tests should enforce the server-side contract that makes this possible.

---

## Focus Mode regression tests (gold sets)

Focus Mode must be evaluable and non-regressing.

### Gold-set assertions
- evidence-required questions → citations present and policy allows
- insufficient evidence → abstain (no hallucination)
- citations resolvable via evidence resolver
- sensitivity gates respected (no restricted leakage)
- `audit_ref` always present

### Suggested gold-set format
Structured YAML/JSON:
- `id`, `question`, `view_state`
- `expected.allowed`, `expected.must_abstain`, `expected.min_citations`
- `expected.deny_reasons` for deny cases (optional)

> [!NOTE]
> Gold sets are governance contracts, not “answers you like.”

---

## UI trust membrane tests

UI must not bypass the governed API boundary.

### What to enforce
- no DB connection strings or store endpoints in frontend code
- no direct calls to PostGIS/Neo4j/search/object stores from UI
- all flows: UI → API → (policy + stores) → API → UI

### Test mechanisms
- static analysis rules (forbidden ports/hosts/imports)
- E2E smoke: evidence panels work, citations render, evidence resolver used (not DB)

---

## Sensitivity regression suite

KFM requires redaction and non-regression for sensitive outputs.

### Sensitivity classes (baseline)
- public
- restricted
- sensitive-location
- aggregate-only

### Required regression tests
1) golden deny queries (previous leak patterns must fail forever)
2) negative tests for unauthorized high-precision sensitive-location outputs
3) field-level tests for redaction/suppression
4) audit linkage checks for governed responses

> [!IMPORTANT]
> Sensitivity suite must include deny cases. Passing tests must prove refusal/redaction is correct.

---

## Audit integrity tests

Auditability is a trust requirement.

### What to test
- governed responses include `audit_ref`
- responses include evidence refs (citations) or abstain
- audit records can be fetched and link back to:
  - policy version/bundle (when available)
  - evidence refs / bundle digest (when available)

Recommended approaches:
- contract tests asserting `audit_ref` on response schemas
- integration tests that fetch audit record and validate linkage

---

## CI mapping (required gates)

CI should enforce at minimum:
1) docs/story validation
2) receipt validation + checksum verification + spec_hash semantics checks
3) DCAT/STAC/PROV validation + cross-links
4) OPA/Rego policy tests + regression denies
5) OpenAPI contract tests for `/api/v1`
6) Focus Mode gold-set regression
7) UI trust membrane static analysis + selected E2E smoke
8) sensitivity regression suite + audit integrity checks

> [!TIP]
> Keep fast checks on every PR and move heavier E2E/perf checks to nightly/pre-release—but do not weaken fail-closed gates.

---

## Contributing rules & PR checklists

### All PRs
- [ ] tests updated/added for touched subsystems
- [ ] no secrets in code/logs/fixtures
- [ ] deterministic outputs (seed randomness, freeze time)
- [ ] link hygiene (no broken internal references)

### Policy PRs
- [ ] allow + deny unit tests added/updated
- [ ] default deny preserved
- [ ] sensitivity regressions updated if affected

### OpenAPI/API PRs
- [ ] contract tests updated
- [ ] `/api/v1` compatibility proven (or create `/api/v2`)
- [ ] audit schema expectations updated if response shape changed

### Dataset integration PRs
- [ ] receipt + catalog fixtures added (DCAT always; STAC/PROV as applicable)
- [ ] checksum tests added
- [ ] sensitivity labels + redaction tests added when needed
- [ ] representative API contract test query added

### Focus Mode PRs
- [ ] gold sets updated/added (with governance review if sensitive impacts)
- [ ] abstention behavior verified
- [ ] citations resolvable verified

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Policy denies everything | missing input keys or deny-by-default triggered | fix fixtures; prove allow cases without weakening deny |
| Receipt tests fail | missing run_manifest keys/spec_hash semantics mismatch | update receipt emitter; keep fail-closed |
| Catalog tests fail | invalid DCAT/STAC/PROV or broken links | fix catalogs; regenerate normalized outputs; verify checksums |
| Contract tests fail | `/api/v1` breaking change | restore compatibility or move to `/api/v2` |
| Gold set fails | behavior drift | confirm intent; update gold set only with governance review if sensitive |
| UI membrane fails | UI trying to call stores directly | route through API gateway; remove forbidden endpoints |

---

## References

Internal KFM documents defining test expectations:
- KFM Next-Gen Blueprint & Primary Guide — CI hardening, acceptance criteria, cite-or-abstain, audit expectations
- KFM Data Source Integration Blueprint — sensitivity classes, redaction as transformation, policy regressions
- Feb-2026 integration patterns — spec_hash semantics (RFC 8785), digest pinning, acceptance harness patterns

External standards frequently used in validation:
- STAC (OGC community standard)
- DCAT (W3C)
- PROV (W3C)
- OPA/Rego (Open Policy Agent)

---

<details>
  <summary><strong>FAQ: Why treat tests as governance artifacts?</strong></summary>

Because KFM’s core value is trust. Tests are the automated enforcement mechanism for:
- provenance completeness,
- evidence-first behavior,
- policy correctness,
- and preventing sensitivity leaks.

A green build is not merely “code works”—it is “the governed system still satisfies its trust contract.”

</details>
