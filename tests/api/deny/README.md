<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-api-deny-readme
title: tests/api/deny/ — Governed API Deny, Abstain, Error, and Leakage Test Lane
type: readme; directory-readme; negative-api-test-index; trust-membrane-proof-guardrail
version: v0.3
status: draft; canonical-test-sublane; contract-and-routing-only; app-owned-five-test-companion; executable-workflow-confirmed; broader-proof-NEEDS-VERIFICATION
policy_label: public
owners: OWNER_TBD — QA steward · Governed API steward · Policy steward · Runtime steward · Evidence steward · Security steward · Release steward · Docs steward
updated: 2026-08-01
current_path: tests/api/deny/README.md
truth_posture: CONFIRMED target README and prior blob, tests/api parent boundary, deletion of two vacuous assert-true modules, five app-owned route/method/manifest/internal-store-literal/forbidden-import checks, executable local target, three-job workflow definition, finite runtime doctrine, and trust-membrane rule / UNKNOWN required-check status, complete governed route inventory, accepted denial response profile, active fixtures, production behavior, deployment state, and current hosted pass state / NEEDS VERIFICATION broader auth, policy, rights, sensitivity, evidence, runtime-payload, network, correction, rollback, and leakage coverage
base_commit: cb8a46fff89861b8f0ca57c1c29bacf1fec885a5
prior_blob: 57aab223677099be2b4178223fb08be04c8f2741
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/security/DENY_TESTS.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/truth-posture.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../../../runtime/envelopes/README.md
  - ../../../contracts/runtime/policy_decision.md
  - ../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../apps/governed-api/tests/test_boundary_guards.py
  - ../../../.github/workflows/deny-test.yml
  - ../../../Makefile
tags: [kfm, tests, api, deny, abstain, error, fail-closed, leakage, trust-membrane, governed-api, finite-outcomes, negative-tests]
notes:
  - "v0.3 removes two vacuous assert-true modules rather than preserving false-green evidence."
  - "The lane remains the negative governed API contract and routing boundary; the five current executable assertions have one owner in apps/governed-api/tests/test_boundary_guards.py."
  - "make deny-test and the read-only three-job workflow execute the same five-test set, with different local-versus-hosted process topology."
  - "The five structural checks are bounded evidence, not complete denial, policy, leakage, release, or production proof."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/api/deny/` — Governed API Deny, Abstain, Error, and Leakage Test Lane

> **Purpose.** Prove that governed API surfaces fail closed, return the correct finite non-answer outcome, and do not leak protected state when evidence, policy, rights, sensitivity, lifecycle, release, correction, runtime, or validation prerequisites are not satisfied.

![status](https://img.shields.io/badge/status-draft-yellow)
![lane](https://img.shields.io/badge/lane-negative__API__tests-blue)
![implementation](https://img.shields.io/badge/lane-contract__only-orange)
![workflow](https://img.shields.io/badge/workflow-5__bounded__guards-blue)

> [!IMPORTANT]
> `tests/api/deny/` is a **test authority lane**, not policy authority, API implementation, contract or schema authority, fixture authority, evidence authority, receipt storage, or release authority.

The current executable companion checks unknown-route `404`, unsupported-method `405`, the exact three-route scaffold manifest, forbidden internal-store **literals**, and selected MapLibre/Cesium/Ollama import prefixes. A green run does **not** prove authentication, authorization, finite `DENY` envelopes, runtime payload safety, network isolation, complete route or leakage coverage, policy/rights/sensitivity enforcement, release, deployment, or publication.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Outcome semantics](#finite-outcome-semantics) · [Coverage](#required-deny-test-families) · [Leakage](#leakage-and-side-channel-assertions) · [Fixtures](#fixture-and-test-data-rules) · [Proof](#current-proof-and-ci-boundary) · [Authoring](#test-authoring-contract) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at this revision | Safe conclusion |
|---|---|---|
| `tests/api/deny/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| Direct executable files below `tests/api/deny/` | **NONE at this revision** | Two vacuous `assert True` modules were deleted; zero collection must not be reported as passing coverage. |
| `tests/api/README.md` | **CONFIRMED** | Defines the governed API test parent lane and identifies `deny/` as its negative child. |
| `docs/security/DENY_TESTS.md` | **CONFIRMED draft doctrine/catalog** | Defines fail-closed obligations and gate families, but several implementation paths remain proposed or stale. |
| `apps/governed-api/tests/test_boundary_guards.py` | **CONFIRMED executable companion** | Owns five bounded structural/scaffold assertions; it is not complete deny-envelope or policy coverage. |
| `make deny-test` | **CONFIRMED executable local target** | Runs the five app-owned assertions in one pytest process and propagates failure. |
| `.github/workflows/deny-test.yml` | **CONFIRMED executable definition** | Three read-only jobs split the same five-test set; required-check and exact-head run state require hosted verification. |
| Governed API route inventory | **UNKNOWN** | No complete, accepted route-to-deny-test matrix is established here. |
| Canonical denial response profile | **NEEDS VERIFICATION** | Runtime, policy, and API envelope documents contain related but not automatically interchangeable vocabularies. |
| Test fixtures and snapshots | **UNKNOWN** | No accepted fixture or snapshot family is confirmed under this lane. |
| Current pass state | **UNKNOWN** | Repository source inspection is not test execution. |
| Production enforcement | **UNKNOWN** | Documentation, schemas, and CI names do not prove deployed behavior. |

**Authority of this README:** lane purpose, proof expectations, negative-case taxonomy, leakage assertions, and review discipline. Executable tests, accepted contracts and schemas, policy bundles, fixtures, validators, route implementations, workflow definitions, test reports, release records, and steward decisions outrank this document.

---

## Placement and authority

Directory Rules place enforceability proof under `tests/`. The parent API test lane is therefore the correct responsibility root for negative governed API behavior.

```text
tests/api/deny/                 negative governed API surface proof
apps/governed-api/              API implementation and route wiring
policy/                         policy rules and admissibility
contracts/                      semantic object and response meaning
schemas/                        machine-checkable shape
runtime/envelopes/              runtime envelope wiring
fixtures/                       deterministic valid and invalid examples
tools/validators/               reusable validator implementation
data/receipts/ and data/proofs/ emitted audit/proof records
release/                        promotion, correction, withdrawal, rollback authority
```

This lane must not:

- implement routes or middleware;
- define policy outcomes;
- invent response fields or enums;
- store canonical evidence, receipts, or release records;
- call RAW, WORK, QUARANTINE, canonical stores, source systems, model providers, or private services as the normal public test path;
- use real sensitive geometry, living-person data, genomic data, credentials, or private infrastructure details;
- treat a test fixture as source truth;
- treat a passing response-shape test as release approval.

### Test-layer boundary

A deny test should prove observable API behavior:

```text
synthetic governed request
  -> route / handler
  -> evidence + policy + lifecycle + release checks
  -> finite outcome
  -> safe response body
  -> no protected leakage
```

A unit test of a helper may support this lane, but it does not replace at least one route- or handler-level assertion where a public or semi-public surface exists.

---

## Finite outcome semantics

`DENY`, `ABSTAIN`, and `ERROR` are not synonyms.

| Outcome | Use when | Must not be used as |
|---|---|---|
| `DENY` | A policy, access, rights, sensitivity, consent, lifecycle, release, or governance rule forbids the requested exposure or action. | A generic substitute for missing evidence or internal exceptions. |
| `ABSTAIN` | Evidence, citation support, source authority, freshness, or bounded scope is insufficient to produce a supported answer. | A way to hide a known policy prohibition. |
| `ERROR` | Validation, dependency, configuration, adapter, envelope, or internal processing failure prevents a governed result. | A substitute for an expected policy denial. |
| restricted or redacted result | Policy permits a bounded derivative while prohibiting exact or full output. | An untracked partial `ANSWER` with omitted governance context. |

### Required outcome assertions

Every executable negative API test should assert, where the accepted response profile supports it:

- finite outcome;
- stable reason code or reason family;
- HTTP status mapping, if one is accepted;
- no answer payload on `DENY`, `ABSTAIN`, or `ERROR`;
- no protected field leakage;
- correction or release posture when material;
- evidence or policy pointers when permitted and safe;
- deterministic response shape;
- no raw exception trace, filesystem path, SQL detail, provider response, prompt, token, or model internals.

### HTTP status is not enough

The following is incomplete:

```python
assert response.status_code == 403
```

A governed deny test should also prove the accepted finite outcome and safe body. Conversely, the README does not prescribe a universal HTTP mapping until the API contract accepts one.

---

## Required deny-test families

### 1. Public trust-membrane tests

| Case | Required result |
|---|---|
| Public route attempts to read RAW data | `DENY` or hard test failure before data exposure |
| Public route attempts to read WORK or QUARANTINE | `DENY` or hard test failure |
| Public route attempts direct canonical/internal-store access | blocked and no protected body content |
| Browser/public client attempts direct model-provider access | blocked |
| Unauthenticated request reaches an administrative surface | `DENY` |
| Public route receives an unpublished candidate identifier | no candidate payload exposure |

### 2. Policy and access tests

| Case | Expected posture |
|---|---|
| Required policy decision missing | `DENY` |
| Explicit policy denial | `DENY` |
| Required role or capability absent | `DENY` |
| Requested purpose exceeds granted scope | `DENY` |
| Unknown policy version where version is required | fail closed |
| Obligation cannot be satisfied | `DENY` or accepted held/restricted state |

### 3. Rights and consent tests

| Case | Expected posture |
|---|---|
| Rights status missing or ambiguous | `DENY` or `ABSTAIN`, according to accepted contract |
| Redistribution prohibited | `DENY` |
| Consent missing for consent-dependent material | `DENY` |
| Consent revoked after prior release | deny current exposure and test correction propagation |
| Purpose limitation violated | `DENY` |
| License expired or re-review overdue | fail closed |

### 4. Sensitivity and precision tests

Synthetic cases must cover, where relevant:

- exact rare-species locations;
- exact archaeology locations;
- living-person addresses or identifiers;
- DNA or genomic material;
- private landowner details;
- vulnerable infrastructure;
- culturally sensitive or sovereignty-restricted material;
- sensitive geometry returned through vector tiles, 3D scenes, downloads, search, or generated narrative.

Expected behavior may be `DENY`, generalized geometry, redacted attributes, staged access, or another accepted restricted profile. The test must identify the accepted policy basis rather than inventing one.

### 5. Evidence and citation tests

| Case | Expected posture |
|---|---|
| `EvidenceRef` cannot resolve | `ABSTAIN` |
| EvidenceBundle is missing required source or provenance support | `ABSTAIN` or `DENY` when policy requires denial |
| Citation-required response lacks valid citation support | `ABSTAIN` |
| Source role is insufficient for the requested claim | `ABSTAIN` or `DENY` according to policy |
| Evidence is stale beyond accepted cadence | `ABSTAIN`, held, or denied |
| Generated text is the only support | `ABSTAIN` |

### 6. Lifecycle and release tests

Test that the API does not expose material as published truth when it is:

- RAW;
- in WORK;
- quarantined;
- merely processed;
- cataloged but unreleased;
- review-pending;
- held;
- withdrawn;
- superseded;
- correction-pending;
- stale-sensitive;
- missing a required release manifest, receipt, proof, or rollback target.

A file path under `data/published/` is not sufficient by itself; the accepted release state must be checked.

### 7. Runtime and envelope tests

| Case | Required posture |
|---|---|
| Model output arrives without governed envelope | `ERROR` or test failure |
| Runtime returns unknown outcome enum | schema/contract failure |
| Adapter returns provider-specific internal fields | redact or fail |
| Policy state is missing from a policy-required result | fail closed |
| Unsupported evidence is paired with `ANSWER` | test failure |
| `DENY` body includes answer payload | test failure |
| Raw stack trace or provider error leaks | test failure |

### 8. Correction and rollback tests

At least one negative route family should prove:

- withdrawn content is no longer exposed;
- superseded content is not presented as current;
- corrected identifiers or geometry do not remain in stale caches;
- revoked consent or changed sensitivity reaches the public response path;
- rollback restores the last accepted release rather than RAW or candidate state;
- denial reason and correction state remain inspectable without exposing protected content.

---

## Leakage and side-channel assertions

A denied response can still violate policy through metadata or side channels.

### Response-body leakage

Assert absence of:

- RAW, WORK, or QUARANTINE paths;
- canonical database names or internal table names;
- private object identifiers;
- source credentials or signed URLs;
- exact protected coordinates;
- private addresses;
- genomic sequences;
- policy engine internals;
- prompt text or chain-of-thought;
- provider request/response bodies;
- stack traces and local filesystem paths;
- internal service hostnames;
- unreleased titles, filenames, or catalog labels where existence itself is sensitive.

### Header and status leakage

Review:

- `Location`;
- `Link`;
- debugging headers;
- trace identifiers;
- cache headers;
- timing variation;
- response size;
- retry hints;
- exception-class names;
- internal correlation IDs.

The test should not require eliminating all diagnostics. It should verify that diagnostics follow the accepted public logging and trace contract.

### Cache and persistence leakage

Where a route uses caches or derived artifacts, test that a later denial cannot be bypassed through:

- stale browser/API caches;
- tile caches;
- search indexes;
- generated summaries;
- downloaded artifacts;
- vector stores;
- graph projections;
- public aliases;
- previously issued URLs.

---

## Fixture and test-data rules

Default deny tests must be:

- deterministic;
- offline;
- synthetic;
- minimal;
- public-safe;
- versioned;
- independently reviewable;
- free of credentials and live endpoints.

### Fixture ownership

```text
fixtures/                       reusable deterministic fixture authority
tests/api/deny/                 test code and test-scoped expectations
```

Do not create a second general fixture authority under this lane. Small inline objects are acceptable when they are test-specific and contain no sensitive material.

### Required fixture metadata

A reusable negative fixture should identify:

- fixture ID;
- object or request family;
- expected outcome;
- reason family;
- policy profile;
- evidence state;
- lifecycle/release state;
- sensitivity and rights posture;
- synthetic-data declaration;
- schema/contract version;
- expected leakage assertions.

### No live dependencies

The default suite must not require:

- internet access;
- live databases;
- live model providers;
- real credentials;
- production secrets;
- actual sensitive records;
- mutable external state.

Integration tests requiring controlled services must be separately marked and must retain deterministic negative assertions.

---

## Current proof and CI boundary

The current local and hosted selectors are:

```yaml
make deny-test:
  source: apps/governed-api/tests/test_boundary_guards.py
  tests: all 5

workflow:
  public-boundary-deny:
    tests: [unknown-route-404, non-GET-405, exact-route-manifest]

  raw-leak-deny:
    tests: [forbidden-internal-store-literal-scan]

  model-runtime-deny:
    tests: [forbidden-renderer-and-model-import-prefix-scan]
```

Therefore:

- executable five-test coverage and local/workflow test-set parity are **CONFIRMED in source**;
- local execution results must be reported for the exact revision;
- hosted run state and required-check configuration remain separate hosted facts;
- the route checks cover only scaffold routing and methods;
- the literal/import scans are bounded source checks, not runtime information-flow, payload, network, or side-channel proof;
- broader deny behavior remains **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION** as cataloged below.

### Required CI characteristics

An accepted deny-test workflow should:

1. install pinned dependencies;
2. run deterministic offline tests;
3. fail when any negative assertion fails;
4. publish bounded test reports without protected fixture contents;
5. identify the tested contract/schema/policy profile;
6. avoid `|| true`, ignored exit codes, and echo-only success;
7. cover route-level and leakage assertions;
8. run on pull requests that modify governed API, policy, envelope, release, sensitivity, evidence, or public-client boundaries;
9. retain an auditable failure signal;
10. not publish or mutate lifecycle or release state.

### Relationship to repository-wide checks

A successful `schema-validation`, `policy-test`, `api-test`, or `deny-test` workflow does not automatically prove this lane's coverage. The workflow command and collected tests must be inspected.

---

## Test authoring contract

Each test or parametrized case should declare:

| Field | Requirement |
|---|---|
| Test ID | Stable identifier |
| Route/surface | Exact handler or route under test |
| Threat or failure condition | What prerequisite is absent, invalid, prohibited, stale, or revoked |
| Expected finite outcome | `DENY`, `ABSTAIN`, `ERROR`, or accepted restricted/redacted profile |
| Expected reason | Stable code or bounded family |
| Policy/evidence basis | Accepted pointer or explicit `NEEDS VERIFICATION` during draft |
| Lifecycle/release state | Explicit when material |
| Response schema/profile | Exact accepted version |
| Leakage assertions | Protected fields, paths, identifiers, and side channels that must not appear |
| Fixture posture | Synthetic/offline declaration |
| Correction behavior | Required when withdrawal, revocation, correction, or supersession is involved |

### Example test shape

```python
def test_unresolved_evidence_abstains(client, synthetic_request):
    response = client.post("/governed/example", json=synthetic_request)

    assert response.status_code == 200  # only when accepted API contract says so
    body = response.json()
    assert body["outcome"] == "ABSTAIN"
    assert body["reason_code"] == "EVIDENCE_UNRESOLVED"
    assert "answer" not in body
    assert "data/raw/" not in response.text
    assert "Traceback" not in response.text
```

The example is illustrative. Route, status code, field names, and reason code remain **PROPOSED** until verified against accepted API contracts and implementation.

---

## Review burden

Ordinary QA review is insufficient when a test changes the expected public disclosure boundary.

Require relevant steward review when a test covers:

- living-person or genomic data;
- Indigenous, cultural, archaeological, or sovereignty-sensitive information;
- rare species or exact habitat locations;
- private landownership;
- vulnerable infrastructure;
- rights or license restrictions;
- public model/AI output;
- release, withdrawal, correction, or rollback;
- authentication, authorization, or privileged administration.

A test weakening a denial expectation must be treated as a policy- and release-significant change, not a routine snapshot update.

---

## Validation

Recommended bounded checks:

```bash
find tests/api/deny -maxdepth 5 -type f | sort
make deny-test
PYTHONPATH=apps/governed-api/src python -m pytest -q --strict-config --strict-markers \
  apps/governed-api/tests/test_boundary_guards.py
```

Workflow inspection:

```bash
sed -n '1,220p' .github/workflows/deny-test.yml
```

Static source checks may supplement, but not replace, executable tests:

```bash
git grep -nE 'data/(raw|work|quarantine)|ollama|Traceback' -- \
  apps tests/api runtime
```

Do not run `pytest tests/api/deny` and report its zero-collection exit as coverage. Do not append `|| true` to promotion-significant test commands.

---

## Definition of done

This lane is operationally complete only when:

- [ ] accepted governed API routes are inventoried;
- [ ] each public or semi-public route has required negative cases;
- [ ] an accepted response-envelope profile is pinned;
- [ ] `DENY`, `ABSTAIN`, and `ERROR` are tested distinctly;
- [ ] restricted and redacted profiles are tested where allowed;
- [ ] reusable synthetic fixtures exist in an accepted fixture home;
- [ ] response-body, header, cache, and side-channel leakage checks exist;
- [ ] rights, consent, sensitivity, evidence, lifecycle, release, correction, and rollback cases are covered where applicable;
- [ ] public clients cannot reach RAW, WORK, QUARANTINE, canonical stores, or model providers directly;
- [x] the current workflow executes five bounded tests and propagates assertion or collection failure;
- [x] no echo-only job is represented as proof;
- [ ] test reports are inspectable and public-safe;
- [ ] owners and reviewers are assigned;
- [ ] correction and rollback behavior are tested;
- [ ] CI pass state is observed from the exact implementation commit.

---

## Correction and rollback

### Correcting a test expectation

When an expected denial changes:

1. identify the accepted contract, schema, policy, ADR, release, or correction record authorizing the change;
2. update fixtures and tests together;
3. preserve the previous case when backward compatibility or regression risk exists;
4. document whether the change broadens or narrows disclosure;
5. require appropriate policy/security/release review;
6. run leakage and cache invalidation checks;
7. retain a transparent commit history.

### Documentation rollback

Before merge, leave the draft PR unmerged or restore the prior blob in a transparent follow-up commit.

After merge, revert the documentation commit or PR. Do not reset or rewrite shared history.

### Test rollback

Do not delete a failing deny test merely to recover green CI. Either:

- fix the implementation;
- fix a demonstrably incorrect test using accepted evidence;
- hold the affected release;
- document a temporary, reviewed exception with expiry and rollback.

The two deleted modules were tautological `assert True` placeholders with no inbound references; they were not failing tests or proof. Restoring them would restore false-green collection, not coverage.

---

## Open verification backlog

- [x] Inventory `tests/api/deny/` at this revision; only this README remains.
- [ ] Inventory actual governed API routes and handlers.
- [ ] Identify accepted public and semi-public response profiles.
- [ ] Resolve RuntimeResponseEnvelope, DecisionEnvelope, PolicyDecision, and HTTP mapping boundaries.
- [ ] Identify canonical fixtures and snapshot home.
- [ ] Add route-level public-boundary tests.
- [ ] Add RAW, WORK, and QUARANTINE leakage tests.
- [ ] Add behavior-level direct model-endpoint denial tests; the current import-prefix scan is structural only.
- [ ] Add exact sensitive geometry denial/generalization tests.
- [ ] Add rights, consent, and sensitivity cases.
- [ ] Add evidence-resolution and citation abstention cases.
- [ ] Add release, withdrawal, correction, supersession, and rollback cases.
- [ ] Add header, cache, search-index, tile, and generated-summary leakage checks.
- [x] Replace echo-only workflow jobs with real fail-closed commands.
- [ ] Verify workflow path filters and required-check status.
- [ ] Assign owners and CODEOWNERS.
- [ ] Record test-report and artifact retention policy.
- [ ] Verify current pass state from the exact commit.
- [ ] Add a rollback drill for a deliberately introduced leakage regression.

---

## Evidence basis

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior `tests/api/deny/README.md` | **CONFIRMED** | Existing lane intent and prior blob | Previously overstated proof purpose relative to implementation |
| `tests/api/README.md` | **CONFIRMED** | Parent API test boundary and child-lane placement | Direct lane remains contract/routing-only. |
| `docs/security/DENY_TESTS.md` | **CONFIRMED draft** | Fail-closed doctrine, gate families, and negative-test taxonomy | Most catalog families remain proposed. |
| `apps/governed-api/tests/test_boundary_guards.py` | **CONFIRMED executable** | Five route/method/manifest/literal/import assertions | No complete policy, response-envelope, payload, network, release, or production proof. |
| `Makefile` | **CONFIRMED executable definition** | Local five-test aggregate with strict pytest flags | Not hosted job isolation or required-check evidence. |
| `.github/workflows/deny-test.yml` | **CONFIRMED executable definition** | Workflow name, three jobs, and five-test selector union | Hosted exact-head result and required-check status require separate verification. |
| Runtime and policy schema/contract surfaces | **CONFIRMED related evidence** | Finite-outcome and policy decision concepts | Exact API response profile remains unresolved |
| Direct lane inventory | **CONFIRMED at base** | Two tautological modules had no inbound references and were deleted | Future branches may add distinct substantive cases. |
| Repository test execution | **NEEDS EXACT-HEAD RESULT** | Local and hosted outcomes are reported separately | A pass proves only the selected five checks. |

[Back to top](#top)
