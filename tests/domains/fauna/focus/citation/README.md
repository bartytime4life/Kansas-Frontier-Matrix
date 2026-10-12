<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/focus/citation/readme
title: Fauna Focus Citation Test Lane README
type: test-lane-readme
version: v0.2
status: draft; repository-grounded; readme-only lane at evidence snapshot
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Focus Mode steward>
  - <PLACEHOLDER — Citation/evidence steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Sensitivity reviewer>
created: 2026-07-05
updated: 2026-07-17
policy_label: public; tests; fauna; focus-mode; citation; no-network; cite-or-abstain; fail-closed
implementation_status: README contract present; executable Fauna Focus citation tests, direct citation validator, canonical report schema, Focus route, and substantive CI are not established
truth_posture: cite-or-abstain; current behavior claims are limited to the pinned evidence snapshot
responsibility_root: tests/
domain_lane: fauna
parent_lane: focus
sub_lane: citation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 7af05fc50e5a1bab28b314532b0a66d2839a229b
  target_prior_blob: 5d334e08653cf523ecc64981a64e7481df2e7aa0
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/focus/README.md
  - tests/fixtures/focus/README.md
  - docs/architecture/directory-rules.md
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/architecture/governed-ai/FOCUS_FLOW.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SENSITIVITY.md
  - contracts/ai/focus_mode_response/README.md
  - contracts/evidence/citation_validation_report.md
  - schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - schemas/contracts/v1/focus/citation_validation_report.schema.json
  - packages/citation/src/citation/README.md
  - tools/validators/citation/README.md
  - apps/governed-api/src/ai/README.md
  - apps/governed-api/tests/test_abstain_routes.py
  - apps/governed-api/src/governed_api/routes/registry.py
  - policy/focus/README.md
  - .github/workflows/citation-validation.yml
  - .github/workflows/focus-mock-test.yml
  - .github/workflows/domain-fauna.yml
  - Makefile
tags:
  - kfm
  - tests
  - fauna
  - focus-mode
  - citation
  - citation-validation
  - evidence-ref
  - evidence-bundle
  - citation-validation-report
  - ai-receipt
  - cite-or-abstain
  - sensitivity
  - no-network
  - fail-closed
notes:
  - "v0.2 preserves the v0.1 cite-or-abstain lane contract and replaces blanket implementation uncertainty with a pinned repository-grounded maturity statement."
  - "Bounded exact-path and code-index checks surfaced this README but no executable module under tests/domains/fauna/focus/citation; exhaustive absence is not claimed."
  - "CitationValidationReport has a draft semantic contract, but the evidence-family and Focus schemas are empty permissive scaffolds."
  - "The direct citation validator lane is README-only, representative executable/tests were not established, citation is absent from the shared validator aggregate, and citation-validation CI is TODO-only."
  - "The governed API has scaffolded bootstrap/layers/evidence routes with executable ABSTAIN/NOT_IMPLEMENTED tests, but no Focus route is registered."
  - "Directory Rules have duplicate live authority surfaces; both agree that this test lane belongs under tests/domains/fauna/focus/citation. The authority-path conflict remains visible and unresolved."
] -->

<a id="top"></a>

# Fauna Focus Citation Tests

> **Purpose.** Define the test contract for proving that a Fauna Focus Mode response maps every consequential claim to admissible, released evidence or returns a finite `ABSTAIN`, `DENY`, or `ERROR` outcome without leaking policy-withheld detail.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![authority: tests only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![maturity: README only](https://img.shields.io/badge/maturity-README--only-yellow)
![posture: cite or abstain](https://img.shields.io/badge/posture-cite--or--abstain-blue)
![validator: not established](https://img.shields.io/badge/validator-not--established-critical)
![network: denied by default](https://img.shields.io/badge/network-denied--by--default-informational)

**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Parent lane:** `focus/`  
**Sublane:** `citation/`  
**Current maturity:** repository-grounded README contract; executable citation tests are not established  
**Default posture:** released evidence only; cite-or-abstain; public-safe deterministic fixtures; no live source/model/network access  
**Last reviewed:** 2026-07-17

> [!IMPORTANT]
> A citation pointer is not evidence closure. `EvidenceRef`, `CitationValidationReport`, `AIReceipt`, a schema pass, and a rendered link do not replace an admissible `EvidenceBundle`, policy decision, review state, release state, correction lineage, or rollback support.

> [!CAUTION]
> This README does not claim a working Focus route, direct citation validator, field-complete citation-report schema, executable Fauna citation suite, substantive citation workflow, or production citation behavior.

## Quick navigation

[Purpose](#purpose-and-audience) · [Authority](#authority-directory-fit-and-conflicts) · [Status](#repository-grounded-status) · [Scope](#scope-and-non-scope) · [Case contract](#minimum-citation-test-case-contract) · [Scenarios](#required-scenario-families) · [Mapping](#claim-to-citation-mapping-rules) · [Proof matrix](#citation-proof-matrix) · [Fixtures](#fixtures-and-test-data) · [Network](#determinism-network-and-live-test-tiers) · [Execution](#current-execution-and-ci-surface) · [Validation](#validation-layers-and-expected-outcomes) · [Failures](#failure-interpretation) · [Limits](#what-a-passing-suite-does-not-prove) · [Review](#review-burden) · [Maintenance](#maintenance-and-fixture-updates) · [Done](#definition-of-done) · [Evidence](#evidence-ledger) · [Open](#open-verification-register) · [Rollback](#changelog-and-rollback)

---

## Purpose and audience

This directory is the Fauna Focus Mode test sublane for **citation readiness and claim-to-evidence mapping**.

It exists to prove that Fauna Focus Mode remains an interpretive surface downstream of evidence, policy, review, release, and correction controls. A response may summarize released public-safe evidence, explain bounded limitations, compare admissible sources, or expose a finite negative outcome. It must not answer from fluent generation, map properties, unreleased candidates, raw source records, private indexes, receipt metadata, or a schema that merely accepts an arbitrary object.

This lane is for:

- Fauna, Focus Mode, citation, evidence, test, sensitivity, API, and UI maintainers;
- reviewers evaluating whether a generated Fauna answer is citable, bounded, and public-safe;
- validator and schema stewards deciding when citation-report scaffolds are mature enough for enforcement;
- fixture maintainers building deterministic positive and negative cases; and
- CI reviewers interpreting what citation-related workflow results actually prove.

A mature lane should prove:

1. **Every consequential claim is mapped.** Each claim span in an `ANSWER` maps to one or more citation carriers and governed evidence references.
2. **Pointers resolve through evidence closure.** `EvidenceRef` resolution and `EvidenceBundle` admissibility are checked by the owning evidence system.
3. **Release and policy scope are enforced.** Public answers cite only evidence allowed for the current audience, purpose, time, rights, sensitivity, review, and release scope.
4. **Source roles and limitations remain visible.** Observed, regulatory, modeled, aggregate, contextual, synthetic, stale, or conflicted support is not silently flattened.
5. **Citation validation precedes emission.** A failed or unavailable citation check cannot be relabeled as an `ANSWER`.
6. **Negative outcomes are first-class.** Missing, unresolved, stale, conflicted, restricted, corrected, withdrawn, malformed, or unsafe support produces a finite non-answer.
7. **Receipts remain process memory.** `AIReceipt` can record the generation event but cannot satisfy citation or evidence closure.
8. **Default tests are deterministic and no-network.** No live model, source, index, graph, object store, or public endpoint is required.

[Back to top](#top)

---

## Authority, directory fit, and conflicts

The path is correct under the KFM responsibility-root rule:

```text
tests/domains/fauna/focus/citation/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna-specific Focus citation behavior. |
| Owning root | `tests/` — enforceability and regression proof. |
| Domain segment | `domains/fauna/` — Fauna remains a lane, not a root. |
| Parent lane | `focus/` — governed Focus behavior. |
| Sublane | `citation/` — claim/citation/evidence readiness assertions. |
| Response semantic contract | `contracts/ai/focus_mode_response/` and evidence contracts, subject to unresolved contract-home drift. |
| Citation-report meaning | `contracts/evidence/citation_validation_report.md` — draft semantic authority candidate. |
| Machine shape | Applicable schema families under `schemas/contracts/v1/`; current citation-report schemas are scaffolds. |
| Validator implementation | `tools/validators/citation/` when implemented. |
| Shared helper implementation | `packages/citation/` when implemented and bounded to helper responsibility. |
| Governed API implementation | `apps/governed-api/` when a Focus route and orchestration code exist. |
| Policy authority | `policy/focus/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`. |
| Unit-test Focus fixtures | `tests/fixtures/focus/` when payloads and consumers exist. |
| Reusable Fauna fixtures | `fixtures/domains/fauna/` when the scenario is domain-reusable and public-safe. |
| Receipts, proofs, release, correction | Their owning `data/` and `release/` lanes; never this test directory. |

### Directory Rules authority conflict

Repository evidence contains multiple Directory Rules artifacts:

- `docs/architecture/directory-rules.md`, identified by `CONTRIBUTING.md` as the newer live placement artifact; and
- `docs/doctrine/directory-rules.md`, a later-numbered presentation edition at a different path.

The placement question remains unresolved. Both inspected artifacts agree that domain-specific enforceability work belongs under `tests/` with domain and sublane segments, so this target path is not blocked. This README does not decide which Directory Rules copy is canonical.

> [!WARNING]
> This directory must not become a second citation contract, schema, validator, prompt, model, evidence, proof, receipt, policy, release, fixture-corpus, or source-data home.

[Back to top](#top)

---

## Repository-grounded status

**Evidence snapshot:** `main@7af05fc50e5a1bab28b314532b0a66d2839a229b`  
**Prior target blob:** `5d334e08653cf523ecc64981a64e7481df2e7aa0`

| Surface | Observed state | Truth posture |
|---|---|---:|
| Target README | Existing v0.1 README fetched in full and preserved as the revision baseline. | `CONFIRMED` |
| Target placement | Existing path under `tests/domains/fauna/focus/citation/`; inspected Directory Rules copies support the responsibility-root pattern. | `CONFIRMED` path / authority-copy conflict visible |
| Path-scoped instructions | No `AGENTS.md` was found at repository root, `tests/`, `tests/domains/`, `tests/domains/fauna/`, `focus/`, or this lane in the bounded preflight. | `CONFIRMED` for checked paths |
| Overlapping work | No open PR naming the target path and no matching Fauna-Focus-citation branch surfaced before branch creation. | `CONFIRMED` within search boundary |
| Executable files in this lane | Exact-path/code-index checks surfaced this README but no executable module. Exhaustive absence is not claimed. | `NOT ESTABLISHED` |
| Focus response contract | `contracts/ai/focus_mode_response/README.md` defines draft finite response semantics and requires citation validation before `ANSWER`. | `CONFIRMED` draft contract |
| Evidence citation-report contract | `contracts/evidence/citation_validation_report.md` is a draft semantic contract and explicitly not evidence closure or release authority. | `CONFIRMED` draft contract |
| Evidence citation-report schema | Exists but has `properties: {}` and `additionalProperties: true`. | `CONFIRMED` permissive scaffold |
| Focus citation-report schema | Exists but has `properties: {}` and `additionalProperties: true`. | `CONFIRMED` permissive scaffold |
| Citation validator lane | `tools/validators/citation/` is README-only in its bounded inventory; representative executable and dedicated tests were not established. | `CONFIRMED` README / implementation unestablished |
| Shared validator aggregate | Citation is absent from the documented five-entry aggregate. | `CONFIRMED` from validator README |
| Citation package | `packages/citation` is a Python `0.0.0` scaffold with empty initializer and no verified helper modules at tested paths. | `CONFIRMED` scaffold |
| Focus policy | `policy/focus/README.md` is a one-line greenfield bundle stub. | `CONFIRMED` stub |
| Governed API routes | Current registry contains bootstrap, layers, and evidence only; no Focus route is registered. | `CONFIRMED` |
| Governed API tests | Executable tests require all registered scaffold routes to return `ABSTAIN`, `NOT_IMPLEMENTED`, and no evidence refs. | `CONFIRMED` scoped behavior |
| Focus fixture lane | `tests/fixtures/focus/README.md` documents proposed fixtures; checked `answer.valid.json` and `abstain_uncited.invalid.json` paths were absent. | `CONFIRMED` README / payloads not established |
| Citation workflow | `.github/workflows/citation-validation.yml` runs only TODO echo steps. | `CONFIRMED` stub |
| Focus mock workflow | `.github/workflows/focus-mock-test.yml` runs only TODO echo steps. | `CONFIRMED` stub |
| Fauna workflow | `.github/workflows/domain-fauna.yml` remains TODO-only. | `CONFIRMED` stub |
| Root `make test` | Runs `tests/schemas` and `tests/contracts` only; this lane is not included. | `CONFIRMED` |
| Production reports, routes, metrics, and pass rates | Not established by inspected evidence. | `UNKNOWN` |

### Safe current conclusion

`tests/domains/fauna/focus/citation/` is a valid documented test responsibility lane. It is **README-only at this snapshot**. Citation-report schema acceptance currently proves almost nothing about report semantics, and successful citation-named workflows currently prove only that TODO stubs ran.

[Back to top](#top)

---

## Scope and non-scope

### In scope

This lane may contain Fauna-specific tests for:

- claim-span to citation-carrier mapping;
- citation presence, uniqueness, ordering, and stable identity where required by the accepted contract;
- `EvidenceRef` handoff and expected `EvidenceBundle` closure outcomes;
- source-role, temporal-scope, rights, sensitivity, freshness, review, release, correction, and withdrawal visibility;
- `CitationValidationReport` outcome handling once a canonical fielded profile exists;
- positive `ANSWER` behavior with released, admissible support;
- `ABSTAIN`, `DENY`, and `ERROR` behavior for missing, unresolved, restricted, malformed, or unsafe support;
- conflict-preserving answers where multiple admissible sources disagree;
- prevention of evidence substitution by map properties, generated summaries, `AIReceipt`, or schema-only acceptance;
- browser/governed-API/model boundary assertions;
- no-network deterministic fixture behavior; and
- leak checks across response text, citations, receipts, logs, traces, snapshots, and exports.

### Out of scope

This lane does not own:

- prompt templates, provider adapters, model runtime, Focus orchestration, public routes, or UI implementation;
- `CitationValidationReport`, `EvidenceRef`, `EvidenceBundle`, Focus response, or runtime-envelope meaning and schema authority;
- citation validator or evidence resolver implementation;
- policy rules, rights decisions, sensitivity classifications, source admission, review approval, release, correction, withdrawal, or rollback decisions;
- real Fauna source records, exact sensitive locations, private observer data, restricted evidence, or production model output;
- trust-bearing receipts, proofs, release manifests, catalogs, or lifecycle records;
- reusable fixture corpora better owned by verified fixture roots; or
- live network/model/source checks in the default suite.

[Back to top](#top)

---

## Minimum citation test-case contract

Every executable case added to this lane should declare its claim, support, governance context, and expected finite result.

| Field | Required content |
|---|---|
| `case_id` | Stable, descriptive identifier. |
| Request scope | Fauna question, audience, purpose, spatial/temporal scope, and selected public surface. |
| Claim spans | Exact synthetic answer claims expected to require support. |
| Citation carriers | Synthetic citation IDs/locators mapped to each claim span. |
| Evidence handoff | Expected `EvidenceRef` values and expected bundle-resolution result; no real proof payload. |
| Source roles | Observed, regulatory, modeled, aggregate, contextual, synthetic, or other accepted roles kept distinct. |
| Rights and sensitivity | Declared public-safe, generalized, restricted, denied, unknown, or review-required posture. |
| Review/release/correction state | Synthetic state that governs current admissibility. |
| Citation-report expectation | Expected pass/fail/hold/deny/abstain/error finding; field names remain profile-bound until schema adoption. |
| Runtime expectation | Exactly one of `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Reason expectation | Stable accepted reason code or bounded reason category when available. |
| Receipt expectation | Whether an AI/model invocation requires an `AIReceipt` reference; receipt is not evidence. |
| Forbidden substitution | Map properties, generated prose, receipt fields, stale releases, unresolved refs, or schema-only pass that must not support `ANSWER`. |
| Deterministic setup | Fixed time, locale, scope, seed, fixture hashes, and mock behavior. |
| Network posture | Denied by default; any live tier separately governed and excluded from default CI. |
| Cleanup and artifact safety | No secrets, sensitive payloads, production traces, or public writes. |

A case with no explicit claim-to-citation assertion is not citation proof. A TODO, skip, zero-test collection, permissive-schema pass, or receipt-only response is not a passing citation test.

[Back to top](#top)

---

## Required scenario families

| Scenario family | Example condition | Expected behavior |
|---|---|---|
| Valid released answer | Every synthetic claim maps to released, admissible evidence; policy and citation checks pass. | `ANSWER` with citations, evidence refs, limitations, and separate receipt linkage. |
| Missing citation | One or more consequential claims have no citation carrier. | `ABSTAIN` or validation failure; never fill the gap from model fluency. |
| Unresolved `EvidenceRef` | Citation exists but its evidence pointer does not resolve. | `ABSTAIN` or `ERROR` according to the accepted failure profile. |
| Incomplete bundle closure | Pointer resolves to a candidate that does not close the claim scope. | `ABSTAIN`; citation presence alone is insufficient. |
| Rights blocked | Support exists but current rights/license/use scope does not allow the answer. | `DENY` or bounded `ABSTAIN` without restricted details. |
| Sensitive detail blocked | Support would expose a protected Fauna location, identity, or reconstructive clue. | `DENY`; no exact detail in response, citation projection, logs, or receipts. |
| Unreleased or review-blocked | Evidence is candidate/unreviewed/unreleased for the public scope. | `ABSTAIN` or `DENY`; no fallback to internal content. |
| Stale support | Freshness policy blocks consequential use. | `ABSTAIN` or a narrowly allowed stale-context answer with visible state, if policy permits. |
| Conflicted support | Admissible sources disagree. | Preserve source roles and conflict in a bounded `ANSWER`, or `ABSTAIN`; never silently select. |
| Corrected/withdrawn support | Citation points to superseded or withdrawn release state. | Use current correction lineage or return a finite non-answer. |
| Malformed citation report | Report is missing required accepted fields or contains unknown outcome values. | `ERROR`/validation failure; no `ANSWER`. |
| Permissive-schema canary | Arbitrary object passes the current empty scaffold schema. | Test documents that schema pass is non-semantic and cannot authorize `ANSWER`. |
| Receipt-only canary | `AIReceipt` exists but evidence/citations are absent. | `ABSTAIN` or validation failure. |
| Map-property substitution | Generated answer cites feature properties or popup text as evidence. | `ABSTAIN`/validation failure. |
| Browser direct-model path | Client attempts to call model/index/store directly. | `DENY`/boundary failure. |
| Quarantined or unsafe fixture | Test input contains pre-public, malformed, or restricted material. | Fixture setup failure/non-render; do not move lifecycle records from this lane. |
| Adapter/runtime failure | Model or structured-output candidate fails safely. | `ERROR` or bounded `ABSTAIN`; no uncited fallback answer. |

[Back to top](#top)

---

## Claim-to-citation mapping rules

Until a field-complete schema is accepted, tests should keep mapping semantics explicit rather than inventing canonical serialized fields.

Required semantic assertions:

1. every consequential claim span in `ANSWER` has at least one declared supporting citation;
2. every citation maps to governed evidence references expected to close the claim scope;
3. a citation cannot support claims broader in geography, time, population, taxon, source role, or certainty than its evidence;
4. rights, sensitivity, release, review, correction, and audience scope are evaluated independently from citation presence;
5. source roles and conflicts remain visible;
6. quoted or paraphrased excerpts do not exceed the verified source span;
7. missing, malformed, duplicate, stale, withdrawn, or out-of-scope citation carriers produce explicit findings;
8. one citation may support multiple claims only when the mapping is declared and justified;
9. multiple citations do not automatically imply corroboration;
10. `AIReceipt`, rendered attribution, source title, URL, map property, catalog record, or schema pass is not evidence closure;
11. unknown report fields or outcome values fail closed; and
12. public citation projections contain only fields permitted for the current audience.

[Back to top](#top)

---

## Citation proof matrix

| Test concern | Required proof | Negative assertion |
|---|---|---|
| Claim coverage | Every consequential claim maps to one or more citations. | No uncited generated claim. |
| Citation identity | Citation carrier has stable test identity and expected locator/role metadata. | No ambiguous free-text source name as sole support. |
| Evidence handoff | Citation carries the expected governed `EvidenceRef` handoff. | No direct proof-store or source-record read from public/client code. |
| Bundle closure outcome | Owning resolver reports the expected claim-scope closure state. | No assumption that a valid pointer equals closure. |
| Release/currentness | Support is released, current for the claim, and not withdrawn. | No candidate or superseded support represented as current. |
| Rights/sensitivity | Citation projection and answer are admissible for current audience. | No hidden sensitive detail in citation labels, locators, logs, or receipts. |
| Source-role preservation | Regulatory, observed, modeled, aggregate, and contextual roles remain distinct. | No silent upcast to authority. |
| Conflict handling | Disagreement is visible and bounded. | No silent winner or confidence inflation. |
| Citation-report behavior | Accepted report profile produces the expected finite finding. | Current permissive schema alone cannot count as proof. |
| Runtime finite outcome | Citation/evidence/policy state maps to one finite runtime outcome. | No generic success for `ABSTAIN`, `DENY`, or `ERROR`. |
| Receipt boundary | AI/model invocation is separately receipted when required. | Receipt cannot satisfy missing citation/evidence. |
| Browser boundary | Client receives a governed envelope rather than calling model/index/store. | No browser direct-model path. |
| No-network default | Synthetic local fixtures satisfy the case. | Any unexpected external call fails the harness. |

[Back to top](#top)

---

## Fixtures and test data

Two documented fixture surfaces are relevant and must not be silently collapsed:

| Fixture surface | Intended role | Current evidence |
|---|---|---|
| `tests/fixtures/focus/` | Unit-test-scoped synthetic Focus request/response examples. | README exists; checked example payloads were absent. |
| `fixtures/domains/fauna/` | Reusable public-safe Fauna runtime/renderer/governance examples. | README and draft lanes exist; consumer alignment remains incomplete. |

A citation test should prefer the smallest owning fixture lane:

- use `tests/fixtures/focus/` for generic Focus envelope/citation behavior;
- use `fixtures/domains/fauna/` when the Fauna scenario is reusable across citation, UI, policy, or renderer tests; and
- use tiny test-local values only when they are not reusable and are easier to understand inline.

Fixture requirements:

- synthetic or explicitly public-safe;
- deterministic and no-network;
- no exact sensitive coordinates, real observer identities, private notes, restricted source payloads, or reconstruction-enabling combinations;
- explicit source role, time, rights, sensitivity, review, release, correction, and expected outcome where material;
- stable claim/citation mappings and expected findings;
- stable expected outputs when used as regression anchors;
- no production `EvidenceBundle`, receipt, policy decision, release manifest, or model output; and
- linked to an executable consumer before being counted as coverage.

If a fixture contains plausible real protected Fauna detail, stop using it, prevent logs/artifacts from spreading it, route review privately, and replace it with a synthetic or governed public-safe fixture.

[Back to top](#top)

---

## Determinism, network, and live-test tiers

### Default tier: deterministic and no-network

Default tests must not depend on:

- live source services, model providers, vector indexes, graph stores, object stores, map services, or public APIs;
- credentials, developer caches, browser profiles, production logs, or mutable upstream data;
- current time without a fixed clock;
- uncontrolled locale, timezone, seed, ordering, retry, or model sampling;
- network-installed data during the assertion phase; or
- direct source, lifecycle, release, or public-write side effects.

Unexpected network access is a test failure.

### Separate live/integration tier

A future live tier may exist only when separately named, explicitly triggered, excluded from default CI, source-terms-aware, read-only unless independently authorized, secret-safe for fork PRs, timeout/retry bounded, and unable to publish. No such Fauna Focus citation tier was established in the inspected repository.

[Back to top](#top)

---

## Current execution and CI surface

### Repository-native commands observed

| Surface | Observed behavior | Citation-lane coverage |
|---|---|---|
| `make test` | Runs `python -m pytest tests/schemas tests/contracts -q`. | Does not include this lane. |
| `make schemas` | Runs the shared schema aggregate. | Citation validator is not documented in that aggregate. |
| `make governed-api-smoke` | Runs current governed-API tests. | Tests scaffolded routes only; no Focus route is registered. |
| Governed API abstain test | Requires bootstrap/layers/evidence routes to return `ABSTAIN`, `NOT_IMPLEMENTED`, and empty evidence refs. | Confirms safe scaffold behavior, not citation validation. |
| Citation package | Python `0.0.0` scaffold with no verified helper modules at tested paths. | No executable helper coverage. |
| Direct citation validator | Not established. | No CLI, direct tests, report emission, or pass rate. |

### Workflow status

| Workflow | Current steps | Interpretation |
|---|---|---|
| `citation-validation.yml` | `echo TODO citation-resolves`; `echo TODO abstain-on-missing-evidence` | Stub only. |
| `focus-mock-test.yml` | `echo TODO mock-focus-flows`; `echo TODO finite-envelope-shape` | Stub only. |
| `domain-fauna.yml` | TODO validate/proof/publish-dry-run echoes. | Stub only. |

### Proposed future targeted command

Once executable modules and fixture consumers exist, a targeted command may take the form:

```bash
python -m pytest tests/domains/fauna/focus/citation -q
```

This is **PROPOSED**, not current behavior. It must collect intended cases, fail on zero collection/unexpected skips under the accepted harness, use no-network fixtures, and bind to accepted contracts/schemas/validators rather than reimplementing them locally.

[Back to top](#top)

---

## Validation layers and expected outcomes

| Validation layer | What it can prove for the exact test packet | Current maturity |
|---|---|---|
| Markdown/test contract review | Intended rules, authority boundaries, and expected scenarios are documented. | Available here; not executable proof. |
| Citation carrier shape | Carrier fields match an accepted schema/profile. | Canonical standalone carrier shape unestablished. |
| `EvidenceRef` shape | Pointer shape matches fielded EvidenceRef schema. | Fielded schema exists; declared direct validator path is missing. |
| `EvidenceBundle` shape | Bundle candidate matches its schema. | Executable schema wrapper exists outside citation lane. |
| Citation-report schema | Report matches accepted machine shape. | Current evidence and Focus schemas are permissive empty scaffolds. |
| Claim/citation semantic validator | Claims map to valid citation/evidence scope. | Direct validator not established. |
| Rights/sensitivity policy | Citation projection and answer are admissible. | Focus policy is a stub; domain policy behavior needs verification. |
| Governed API runtime | Finite envelope and route boundary behave correctly. | Generic scaffold routes execute; Focus route absent. |
| Browser/UI projection | Public citation display preserves finite outcome and sensitivity. | Needs implementation evidence. |
| No-network guard | No unexpected external request occurs. | Required future harness behavior. |
| CI orchestration | Repository-native citation checks run on changes. | Citation/Focus/Fauna workflows are TODO-only. |

Test reporting should distinguish:

```text
PASS | FAIL | PARTIAL | NOT RUN | NOT APPLICABLE | UNKNOWN
```

Runtime expectations use:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

A correctly produced `DENY` may make a test `PASS`. A schema `PASS` against the current empty citation-report schema must not be reported as semantic citation validation.

[Back to top](#top)

---

## Failure interpretation

| Observed result | Interpretation | Required response |
|---|---|---|
| Consequential claim lacks citation | Cite-or-abstain failure. | `ABSTAIN`/test failure; do not generate substitute support. |
| Citation exists but `EvidenceRef` is unresolved | Pointer without closure. | `ABSTAIN` or bounded `ERROR`. |
| Bundle does not close claim scope | Insufficient evidence. | `ABSTAIN`; narrow the claim if safe. |
| Rights/sensitivity/release blocks use | Admissibility failure. | `DENY` or bounded `ABSTAIN`; no restricted detail. |
| Stale, corrected, or withdrawn support represented as current | Temporal/release defect. | Fail and surface current lineage. |
| Conflicted sources silently flattened | Source-role and uncertainty defect. | Fail; preserve conflict or abstain. |
| Arbitrary report object passes permissive schema | Expected scaffold weakness. | Record non-semantic pass; do not authorize `ANSWER`. |
| `AIReceipt` used as support | Authority collapse. | Fail; receipt is process memory only. |
| Focus/browser direct-model or direct-store call | Trust-membrane violation. | Fail closed. |
| Sensitive detail appears in text, citation, log, trace, snapshot, or receipt | Security/sensitivity incident. | Stop dissemination and route private review. |
| Zero tests collected | No proof executed. | Fail or invalidate the run. |
| Test skipped or TODO workflow succeeds | Coverage gap/scaffold result. | Report `NOT RUN`/placeholder, not pass. |
| Unexpected network request | Hermeticity failure. | Fail default tier. |
| Flaky ordering, time, or model-dependent result | Determinism defect. | Fix/quarantine from authority claims; retain failure evidence. |

[Back to top](#top)

---

## What a passing suite does not prove

Even a substantive passing Fauna Focus citation suite would not, by itself, prove:

- that the cited claim is true beyond the checked evidence and scope;
- source admission, rights, sensitivity, review, policy, release, or correction approval;
- that an `EvidenceBundle` is complete for any untested claim;
- field completeness or canonical authority of current citation-report schemas;
- complete citation coverage across all Fauna questions, languages, user roles, times, or geographies;
- absence of re-identification through untested cross-domain joins;
- production Focus route deployment, model safety, telemetry safety, or branch-protection enforcement;
- publication readiness; or
- that a report, receipt, link, map property, schema pass, or workflow name is sovereign truth.

A passing test is a scoped review signal. It does not publish or approve a Fauna answer.

[Back to top](#top)

---

## Review burden

Reviewers should be able to answer:

- Does every test declare the synthetic claim spans and expected citation mapping?
- Does the test distinguish pointer shape, bundle closure, citation readiness, policy admissibility, and release state?
- Are source roles, time bounds, caveats, conflicts, corrections, and limitations preserved?
- Do missing, unresolved, denied, stale, conflicted, corrected, withdrawn, malformed, and error paths produce finite outcomes?
- Does any assertion wrongly treat the permissive schema, `AIReceipt`, map properties, rendered links, or generated prose as evidence?
- Are fixtures synthetic/public-safe, no-network, deterministic, and linked to consumers?
- Are exact sensitive details absent from response text, citation projections, logs, traces, snapshots, and receipts?
- Are tests calling canonical validators/resolvers/policies when they exist rather than redefining authority locally?
- Are TODOs, skips, absent payloads, zero collection, and workflow scaffolds reported as gaps?
- Does the PR identify workflow triggers, generated receipt, validation, rollback, and required human reviewers?

Changes affecting Fauna sensitivity, citation exposure, rights, public projections, or release behavior require the corresponding stewards. This test lane cannot approve those decisions.

[Back to top](#top)

---

## Maintenance and fixture updates

Update this README when:

- executable tests, fixtures, validators, resolver adapters, schemas, routes, or package helpers are added or moved;
- a canonical `CitationValidationReport` profile is accepted;
- citation reason/outcome vocabularies change;
- Focus policy becomes executable;
- Focus route or browser projection is implemented;
- citation, Focus, or Fauna workflows graduate from TODO stubs;
- fixture ownership between `tests/fixtures/focus/` and `fixtures/domains/fauna/` is resolved;
- supported audiences, surfaces, source roles, or sensitive-data controls change; or
- the Directory Rules authority-path conflict is resolved.

For each fixture or expected-output update:

1. identify the consuming test and claim/citation mapping;
2. verify synthetic/public-safe provenance and rights/sensitivity posture;
3. pin time, scope, ordering, seed, and expected resolver/report/runtime results;
4. update expected output intentionally;
5. run targeted and affected broader tests when available;
6. inspect logs, traces, snapshots, reports, and receipts for disclosure; and
7. document whether the update is a correction, new case, or accepted contract change.

Do not regenerate expected reports merely to make a failure disappear.

[Back to top](#top)

---

## Definition of done

This lane is mature only when repository evidence supports all applicable criteria:

- [ ] At least one executable test module exists and the targeted command collects intended cases.
- [ ] A canonical citation carrier/report semantic profile and field-complete schema are accepted or explicitly versioned.
- [ ] A direct citation validator or verified adapter exists with deterministic finite outcomes.
- [ ] Claim-span mapping, locator scope, source role, time, rights, sensitivity, release, correction, and conflict rules are executable.
- [ ] `EvidenceRef` handoff and `EvidenceBundle` closure outcomes are tested without duplicating resolver authority.
- [ ] Valid, missing-citation, unresolved-ref, incomplete-bundle, denied, stale, conflicted, corrected, withdrawn, malformed, receipt-only, direct-model, quarantined-boundary, and runtime-error scenarios execute.
- [ ] Fixtures are synthetic/public-safe, deterministic, no-network, and linked to actual consumers.
- [ ] A substantive Focus route or test harness exists where route behavior is claimed.
- [ ] TODO-only workflows are graduated to repository-native commands with reviewed triggers and permissions.
- [ ] Zero collection, unexpected skips, unexpected network access, and permissive-schema-only success cannot be misreported as proof.
- [ ] Human Fauna, Focus, citation/evidence, sensitivity, API/UI, test, and docs review is recorded where required.
- [ ] Coverage limits, rollback, correction behavior, and open authority conflicts remain documented.

At this evidence snapshot, these criteria remain open unless a separate executable artifact proves them.

[Back to top](#top)

---

## Evidence ledger

| Evidence location at pinned base | Observation supported |
|---|---|
| `tests/domains/fauna/focus/citation/README.md` | Existing v0.1 baseline and prior blob. |
| `tests/README.md` | Canonical test root, narrow root test target, and mixed maturity. |
| `tests/domains/fauna/README.md` | Parent Fauna test boundary. |
| `tests/domains/fauna/focus/README.md` | Parent Focus lane and citation child responsibility. |
| `CONTRIBUTING.md` | Branch/PR, preservation, Directory Rules conflict, validation, receipt, and rollback expectations. |
| Both Directory Rules paths | Shared target-placement rule and unresolved authority-copy conflict. |
| `docs/architecture/governed-ai/FOCUS_FLOW.md` | Required request → policy → evidence → adapter → citation → policy → envelope doctrine. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Fauna Focus citation, finite outcomes, sensitivity, and governed API boundaries. |
| `docs/domains/fauna/SENSITIVITY.md` | Deny-by-default protected-detail posture. |
| `contracts/ai/focus_mode_response/README.md` | Draft response semantics requiring validated citations for `ANSWER`. |
| `contracts/evidence/citation_validation_report.md` | Draft report meaning and non-authority boundary. |
| Evidence and Focus citation-report schemas | Empty permissive scaffold state. |
| `tools/validators/citation/README.md` | README-only direct validator lane, no direct tests/executable, absent aggregate registration, and TODO workflow. |
| `packages/citation/src/citation/README.md` | Python scaffold and no verified helper implementation at tested paths. |
| `tests/fixtures/focus/README.md` | Proposed unit-test fixture families and no verified runner. |
| Checked Focus fixture payload paths | `answer.valid.json` and `abstain_uncited.invalid.json` absent at pinned base. |
| `policy/focus/README.md` | One-line greenfield policy stub. |
| `apps/governed-api/src/ai/README.md` | AI orchestration is documented but implementation remains unverified. |
| Governed API route registry | Only bootstrap, layers, and evidence routes registered. |
| Governed API abstain test | Executable scaffold routes return `ABSTAIN / NOT_IMPLEMENTED`. |
| Citation, Focus mock, and Fauna workflows | TODO-only CI scaffolds. |
| `Makefile` | Root test targets do not execute this lane. |

[Back to top](#top)

---

## Open verification register

| Question | Status | Evidence needed |
|---|---|---|
| Are there unindexed or branch-local executable tests in this lane? | `NEEDS VERIFICATION` | Complete tree read and collection. |
| Which citation carrier and report schema/profile is canonical? | `CONFLICTED` / `NEEDS VERIFICATION` | Accepted contract/schema/ADR and migration decision. |
| When will evidence and Focus citation-report schemas become field-complete? | `PROPOSED` work | Schema, fixtures, validators, compatibility plan, tests. |
| Which validator owns claim-to-citation semantic checks? | `NEEDS VERIFICATION` | Accepted executable, registry ID, inputs, outputs, and tests. |
| Which resolver interface owns `EvidenceRef → EvidenceBundle` closure for Focus? | `NEEDS VERIFICATION` | Verified package/API integration and fixtures. |
| Which Focus route and service are canonical? | `UNKNOWN` | Implemented route registry and governed API tests. |
| Which Focus policy rules are executable? | `UNKNOWN` | Policy bundle, tests, evaluator wiring, decisions. |
| Which fixture root owns generic versus Fauna-reusable citation cases? | `NEEDS VERIFICATION` | Accepted fixture routing and consumers. |
| Which citation/Focus/Fauna checks are required by branch protection? | `UNKNOWN` | Repository ruleset evidence. |
| When do citation-validation and focus-mock workflows graduate from stubs? | `PROPOSED` work | Owners, commands, fixtures, permissions, outcomes, rollback. |
| Which Directory Rules copy becomes canonical? | `CONFLICTED` / `NEEDS VERIFICATION` | Accepted ADR and synchronized supersession/migration. |

[Back to top](#top)

---

## Changelog and rollback

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README scaffold for the Fauna Focus citation test lane. |
| 2026-07-17 | v0.2 | Repository-grounded maturity refresh; added complete citation-test profile, current contract/schema/validator/package/API/fixture/workflow evidence, scenario matrix, deterministic/no-network rules, failure interpretation, non-proof limits, maintenance, evidence ledger, and explicit authority conflicts. |

### Rollback

This is a documentation-only revision. Restore v0.1 by reverting the implementation commit or replacing this file with blob `5d334e08653cf523ecc64981a64e7481df2e7aa0`. A revert changes documentation only; it does not alter tests, fixtures, validators, packages, workflows, policy, schemas, routes, data, release state, or publication.

### Re-review triggers

Re-review on the first executable citation test, direct validator implementation, field-complete schema, Focus route, policy binding, fixture payload, substantive workflow, citation package helper, public projection change, or Directory Rules authority resolution.

[Back to top](#top)
