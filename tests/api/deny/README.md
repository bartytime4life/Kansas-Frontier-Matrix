<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-api-deny-readme
title: tests/api/deny/ — Governed API Deny, Abstain, Error, and Leakage Test Lane
type: readme; directory-readme; negative-api-test-index; trust-membrane-proof-guardrail
version: v0.2
status: draft; canonical-test-sublane; readme-only; workflow-placeholder; executable-proof-absent; NEEDS VERIFICATION
policy_label: public
owners: OWNER_TBD — QA steward · Governed API steward · Policy steward · Runtime steward · Evidence steward · Security steward · Release steward · Docs steward
updated: 2026-07-16
current_path: tests/api/deny/README.md
truth_posture: CONFIRMED target README and prior blob, tests/api parent boundary, deny-test doctrine, TODO-only deny workflow, finite runtime outcomes, trust-membrane rule, and bounded absence of direct test modules at the pinned snapshot / UNKNOWN governed route inventory, accepted denial response profile, active fixtures, validator wiring, production behavior, and current pass state / NEEDS VERIFICATION implementation, negative fixtures, executable CI, leakage assertions, route coverage, ownership, correction coverage, and rollback proof
base_commit: 7855938a308f967a51b7dce0d023db39ca20eca0
prior_blob: d7b5a7a9ec1044f137aceb426086636b3707f604
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
  - ../../../.github/workflows/deny-test.yml
tags: [kfm, tests, api, deny, abstain, error, fail-closed, leakage, trust-membrane, governed-api, finite-outcomes, negative-tests]
notes:
  - "v0.2 replaces a generic deny-test placeholder index with an evidence-bounded executable-proof contract."
  - "The lane is canonical for negative governed API surface tests but currently contains no confirmed test module beyond this README."
  - "The deny-test workflow is TODO-only and must not be cited as executable deny coverage."
  - "This revision changes documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/api/deny/` — Governed API Deny, Abstain, Error, and Leakage Test Lane

> **Purpose.** Prove that governed API surfaces fail closed, return the correct finite non-answer outcome, and do not leak protected state when evidence, policy, rights, sensitivity, lifecycle, release, correction, runtime, or validation prerequisites are not satisfied.

![status](https://img.shields.io/badge/status-draft-yellow)
![lane](https://img.shields.io/badge/lane-negative__API__tests-blue)
![implementation](https://img.shields.io/badge/tests-README__only-orange)
![workflow](https://img.shields.io/badge/workflow-TODO__only-critical)

> [!IMPORTANT]
> `tests/api/deny/` is a **test authority lane**, not policy authority, API implementation, contract or schema authority, fixture authority, evidence authority, receipt storage, or release authority.

> [!WARNING]
> `.github/workflows/deny-test.yml` currently runs only `echo TODO ...` jobs. A green workflow result therefore proves workflow execution only; it does **not** prove public-boundary denial, RAW-leak prevention, model-runtime isolation, route coverage, response-envelope conformance, or absence of sensitive leakage.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Outcome semantics](#finite-outcome-semantics) · [Coverage](#required-deny-test-families) · [Leakage](#leakage-and-side-channel-assertions) · [Fixtures](#fixture-and-test-data-rules) · [Proof](#current-proof-and-ci-boundary) · [Authoring](#test-authoring-contract) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/api/deny/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| Direct executable files below `tests/api/deny/` | **NOT SURFACED in bounded search** | Treat the lane as README-only until recursive inventory proves otherwise. |
| `tests/api/README.md` | **CONFIRMED** | Defines the governed API test parent lane and identifies `deny/` as its negative child. |
| `docs/security/DENY_TESTS.md` | **CONFIRMED draft doctrine/catalog** | Defines fail-closed obligations and gate families, but several implementation paths remain proposed or stale. |
| `.github/workflows/deny-test.yml` | **CONFIRMED TODO-only scaffold** | Three jobs echo TODO text; green status is not executable proof. |
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

The present workflow is:

```yaml
public-boundary-deny:
  run: echo TODO public-boundary-deny

raw-leak-deny:
  run: echo TODO raw-leak-deny

model-runtime-deny:
  run: echo TODO model-runtime-deny
```

Therefore:

- workflow existence is **CONFIRMED**;
- executable deny coverage is **NOT CONFIRMED**;
- route coverage is **UNKNOWN**;
- fail-closed behavior is **UNKNOWN**;
- leakage coverage is **UNKNOWN**;
- CI should not be described as enforcing deny tests until real commands run and fail on violations.

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
python -m pytest -q tests/api/deny
python -m pytest -q tests/api
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

Do not append `|| true` to promotion-significant test commands. When no executable tests exist, record `NO TESTS COLLECTED` or fail according to the accepted bootstrap policy; do not report coverage as green.

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
- [ ] the workflow executes real tests and fails closed;
- [ ] no echo-only job is represented as proof;
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

---

## Open verification backlog

- [ ] Recursively inventory `tests/api/deny/`.
- [ ] Inventory actual governed API routes and handlers.
- [ ] Identify accepted public and semi-public response profiles.
- [ ] Resolve RuntimeResponseEnvelope, DecisionEnvelope, PolicyDecision, and HTTP mapping boundaries.
- [ ] Identify canonical fixtures and snapshot home.
- [ ] Add route-level public-boundary tests.
- [ ] Add RAW, WORK, and QUARANTINE leakage tests.
- [ ] Add direct model-runtime denial tests.
- [ ] Add exact sensitive geometry denial/generalization tests.
- [ ] Add rights, consent, and sensitivity cases.
- [ ] Add evidence-resolution and citation abstention cases.
- [ ] Add release, withdrawal, correction, supersession, and rollback cases.
- [ ] Add header, cache, search-index, tile, and generated-summary leakage checks.
- [ ] Replace echo-only workflow jobs with real fail-closed commands.
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
| `tests/api/README.md` | **CONFIRMED** | Parent API test boundary and child-lane placement | Also reports no direct API test modules confirmed |
| `docs/security/DENY_TESTS.md` | **CONFIRMED draft** | Fail-closed doctrine, gate families, and negative-test taxonomy | Contains proposed/stale implementation path claims |
| `.github/workflows/deny-test.yml` | **CONFIRMED** | Workflow name and three job families | Jobs are echo-only |
| Runtime and policy schema/contract surfaces | **CONFIRMED related evidence** | Finite-outcome and policy decision concepts | Exact API response profile remains unresolved |
| Bounded repository search | **CONFIRMED bounded result** | No direct executable file surfaced under the lane | Not a substitute for recursive tree inventory |
| Repository test execution | **NOT RUN** | — | Markdown-only API update |

[Back to top](#top)
