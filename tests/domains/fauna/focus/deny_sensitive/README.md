<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/focus/deny-sensitive/readme
title: Fauna Focus Deny-Sensitive Test Lane README
type: test-lane-readme
version: v0.2
status: draft; repository-grounded; readme-only lane at evidence snapshot
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Focus Mode steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Sensitivity reviewer>
created: 2026-07-05
updated: 2026-07-17
policy_label: public; tests; fauna; focus-mode; deny-sensitive; no-network; fail-closed
implementation_status: README contract present; executable Fauna Focus denial tests, policy evaluation, Focus route, domain fixture payloads, and substantive denial CI are not established
truth_posture: cite-or-abstain; fail closed; current behavior claims are limited to the pinned evidence snapshot
responsibility_root: tests/
domain_lane: fauna
parent_lane: focus
sub_lane: deny_sensitive
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 25be8016c3b221e427a4eb18568489b07a0a88c2
  target_prior_blob: f90aec1025a101cc8f158a4780ec6c690040211d
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/focus/README.md
  - tests/domains/fauna/focus/citation/README.md
  - tests/fixtures/focus/README.md
  - docs/architecture/directory-rules.md
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/architecture/governed-ai/FOCUS_FLOW.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SENSITIVITY.md
  - policy/domains/fauna/README.md
  - policy/sensitivity/fauna/README.md
  - policy/sensitivity/fauna/deny_default.rego
  - policy/sensitivity/fauna/geoprivacy.rego
  - policy/sensitivity/fauna/sensitive_taxa_deny.rego
  - policy/sensitivity/fauna/tier_mapping.yaml
  - policy/sensitivity/fauna/geoprivacy_transforms.yaml
  - policy/sensitivity/fauna/nest_den_roost_hibernacula_spawning.yaml
  - policy/sensitivity/fauna/sensitive_taxa.yaml
  - policy/focus/README.md
  - contracts/policy/policy_decision.md
  - contracts/runtime/decision_envelope.md
  - schemas/contracts/v1/policy/policy_decision.schema.json
  - schemas/contracts/v1/runtime/decision_envelope.schema.json
  - fixtures/contracts/v1/policy/policy_decision/README.md
  - fixtures/contracts/v1/runtime/decision_envelope/README.md
  - tools/validators/validate_decision_envelope.py
  - tools/validators/_common/run_all.py
  - tests/schemas/test_common_contracts.py
  - tests/policy/test_explorer_web_adapter_boundary.py
  - apps/governed-api/tests/test_boundary_guards.py
  - apps/governed-api/tests/test_abstain_routes.py
  - apps/governed-api/src/governed_api/routes/registry.py
  - .github/workflows/policy-test.yml
  - .github/workflows/deny-test.yml
  - .github/workflows/focus-mock-test.yml
  - .github/workflows/domain-fauna.yml
  - Makefile
tags:
  - kfm
  - tests
  - fauna
  - focus-mode
  - deny-sensitive
  - policy-decision
  - decision-envelope
  - sensitivity
  - geoprivacy
  - rights
  - release
  - finite-outcome
  - ai-receipt
  - no-network
  - fail-closed
notes:
  - "v0.2 preserves the v0.1 fail-closed lane contract and replaces blanket implementation uncertainty with a pinned repository-grounded maturity statement."
  - "Bounded exact-path and code-index checks surfaced this README but no executable module under tests/domains/fauna/focus/deny_sensitive; exhaustive absence is not claimed."
  - "Fauna sensitivity policy files exist, but their README/config inputs are placeholders and the three Rego files only declare default allow false."
  - "PolicyDecision and DecisionEnvelope have fielded proposed schemas and valid/invalid fixtures; generic schema tests cover both, while the dedicated PolicyDecision validator path is absent."
  - "DecisionEnvelope has an executable JSON Schema wrapper and is included in the shared validator aggregate; this proves shape only, not Fauna policy evaluation."
  - "The governed API has generic boundary guards and scaffolded ABSTAIN/NOT_IMPLEMENTED routes, but no Focus route is registered."
  - "Policy, deny, Focus-mock, and Fauna workflows are TODO-only and do not establish denial enforcement."
  - "Directory Rules have duplicate live authority surfaces; both agree that this test lane belongs under tests/domains/fauna/focus/deny_sensitive. The authority-path conflict remains visible and unresolved."
] -->

<a id="top"></a>

# Fauna Focus Deny-Sensitive Tests

> **Purpose.** Define the test contract for proving that Fauna Focus Mode fails closed before answer emission when sensitivity, rights, review, release, correction, evidence scope, or public-safe transformation does not permit a response.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![authority: tests only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![maturity: README only](https://img.shields.io/badge/maturity-README--only-yellow)
![posture: fail closed](https://img.shields.io/badge/posture-fail--closed-blue)
![policy: scaffolded](https://img.shields.io/badge/policy-scaffolded-critical)
![network: denied by default](https://img.shields.io/badge/network-denied--by--default-informational)

**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Parent lane:** `focus/`  
**Sublane:** `deny_sensitive/`  
**Current maturity:** repository-grounded README contract; executable deny-sensitive tests are not established  
**Default posture:** policy pre-check first; finite outcomes; no hidden disclosure; public-safe deterministic fixtures; no live model/source/network access  
**Last reviewed:** 2026-07-17

> [!IMPORTANT]
> A default-deny policy scaffold is not a complete denial decision. A governed `DENY` requires the accepted policy input, evaluated policy family, finite outcome, safe reason, obligations, audit linkage, and public-safe projection defined by the owning contracts and policy implementation.

> [!CAUTION]
> This README does not claim a working Fauna sensitivity evaluator, Focus policy bundle, Focus route, deny-sensitive fixture corpus, policy-reason taxonomy, UI denial surface, or substantive denial CI.

## Quick navigation

[Purpose](#purpose-and-audience) · [Authority](#authority-directory-fit-and-conflicts) · [Status](#repository-grounded-status) · [Scope](#scope-and-non-scope) · [Case contract](#minimum-denial-test-case-contract) · [Outcomes](#finite-outcome-and-denial-semantics) · [Scenarios](#required-scenario-families) · [Proof matrix](#denial-proof-matrix) · [Fixtures](#fixtures-and-test-data) · [Network](#determinism-network-and-live-test-tiers) · [Execution](#current-execution-and-ci-surface) · [Validation](#validation-layers-and-expected-outcomes) · [Failures](#failure-interpretation) · [Limits](#what-a-passing-suite-does-not-prove) · [Review](#review-burden) · [Maintenance](#maintenance-and-fixture-updates) · [Done](#definition-of-done) · [Evidence](#evidence-ledger) · [Open](#open-verification-register) · [Rollback](#changelog-and-rollback)

---

## Purpose and audience

This directory is the Fauna Focus Mode test sublane for **sensitivity-aware denial and bounded non-answer behavior**.

It exists to prove that public Focus Mode cannot disclose, infer, reconstruct, or overstate protected Fauna information. A request that is outside the permitted audience, purpose, rights, sensitivity, review, release, correction, or transformation scope must end in a finite governed outcome before a public answer is emitted.

This lane is for:

- Fauna, Focus Mode, policy, sensitivity, test, API, UI, evidence, and release maintainers;
- reviewers deciding whether a public-safe derivative remains inside its approved disclosure boundary;
- policy and schema stewards separating policy shape from executable policy behavior;
- fixture maintainers creating deterministic denial and bounded-answer cases; and
- CI reviewers interpreting what policy- and denial-named checks actually prove.

A mature lane should prove:

1. **Policy pre-check happens before generation.** Requests that can be denied from scope, role, rights, sensitivity, review, or release metadata do not invoke a model.
2. **Finite outcomes remain distinct.** `DENY`, `ABSTAIN`, and `ERROR` are not interchangeable and never silently become `ANSWER`.
3. **Denial is reasoned and safe.** The response exposes an accepted reason category and obligations without revealing the protected fact that caused the denial.
4. **Public-safe derivatives remain bounded.** A generalized or transformed record cannot be expanded back toward exact or reconstructive detail.
5. **Evidence quality does not override policy.** Well-supported information can still be inadmissible for the requested audience or purpose.
6. **Missing evidence is not policy denial.** Evidence gaps produce `ABSTAIN` or `ERROR` according to the accepted profile; they do not invent a sensitivity finding.
7. **Receipts remain process memory.** `AIReceipt`, policy receipts, and logs may record the event but cannot replace the policy decision, evidence, review, or release state.
8. **No hidden disclosure occurs.** Answer text, denial text, citations, accessible names, logs, traces, snapshots, receipts, telemetry, cache keys, and exports remain public-safe.
9. **Default tests are deterministic and no-network.** No live model, source, index, graph, object store, geocoder, map service, or public endpoint is required.

[Back to top](#top)

---

## Authority, directory fit, and conflicts

The path is correct under the KFM responsibility-root rule:

```text
tests/domains/fauna/focus/deny_sensitive/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna-specific Focus denial and bounded-response behavior. |
| Owning root | `tests/` — enforceability and regression proof. |
| Domain segment | `domains/fauna/` — Fauna remains a lane, not a repository root. |
| Parent lane | `focus/` — governed Focus behavior. |
| Sublane | `deny_sensitive/` — sensitivity, rights, review, release, and disclosure denial cases. |
| Policy authority | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, `policy/focus/`, and applicable cross-cutting policy roots. |
| Policy decision meaning | `contracts/policy/policy_decision.md`. |
| Runtime decision meaning | `contracts/runtime/decision_envelope.md` and runtime response contracts. |
| Machine shape | Applicable policy/runtime schemas under `schemas/contracts/v1/`. |
| Governed API implementation | `apps/governed-api/` when Focus routes and policy orchestration exist. |
| Client UI implementation | `apps/explorer-web/` as a consumer of governed envelopes only. |
| Unit-test Focus fixtures | `tests/fixtures/focus/` when payloads and consumers exist. |
| Reusable Fauna fixtures | `fixtures/domains/fauna/` when scenarios are domain-reusable and public-safe. |
| Receipts, proofs, release, correction | Their owning `data/` and `release/` lanes; never this test directory. |

### Directory Rules authority conflict

Repository evidence contains multiple Directory Rules artifacts:

- `docs/architecture/directory-rules.md`, identified by `CONTRIBUTING.md` as the newer live placement artifact; and
- `docs/doctrine/directory-rules.md`, a later-numbered presentation edition at a different path.

The placement question remains unresolved. Both inspected artifacts agree that domain-specific enforceability work belongs under `tests/` with domain and sublane segments, so this target path is not blocked. This README does not decide which Directory Rules copy is canonical.

> [!WARNING]
> This directory must not become a second policy, contract, schema, evaluator, prompt, model, evidence, receipt, proof, release, fixture-corpus, or source-data home.

[Back to top](#top)

---

## Repository-grounded status

**Evidence snapshot:** `main@25be8016c3b221e427a4eb18568489b07a0a88c2`  
**Prior target blob:** `f90aec1025a101cc8f158a4780ec6c690040211d`

| Surface | Observed state | Truth posture |
|---|---|---:|
| Target README | Existing v0.1 README fetched in full and preserved as the revision baseline. | `CONFIRMED` |
| Target placement | Existing path under `tests/domains/fauna/focus/deny_sensitive/`; inspected Directory Rules copies support the responsibility-root pattern. | `CONFIRMED` path / authority-copy conflict visible |
| Path-scoped instructions | No `AGENTS.md` was found at repository root, `tests/`, or `tests/domains/fauna/focus/` in the bounded preflight. | `CONFIRMED` for checked paths |
| Overlapping work | No open PR naming the target path and no matching Fauna-Focus-deny-sensitive branch surfaced before branch creation. | `CONFIRMED` within search boundary |
| Executable files in this lane | Exact-path/code-index checks surfaced this README but no executable module. Exhaustive absence is not claimed. | `NOT ESTABLISHED` |
| Fauna domain policy README | Exists but labels itself `PROPOSED (greenfield scaffold)`. | `CONFIRMED` scaffold |
| Fauna sensitivity policy README | Exists and says it must be filled and reviewed before being treated as canonical truth. | `CONFIRMED` scaffold |
| Fauna sensitivity Rego | `deny_default.rego`, `geoprivacy.rego`, and `sensitive_taxa_deny.rego` each contain only a package declaration, scaffold comment, and `default allow := false`. | `CONFIRMED` default-deny scaffolds |
| Fauna sensitivity YAML | Tier mapping, transform, sensitive-site, and sensitive-taxa files are placeholder inventories with no operational rules. | `CONFIRMED` placeholders |
| Focus policy | `policy/focus/README.md` is a one-line greenfield bundle stub. | `CONFIRMED` stub |
| `PolicyDecision` schema | Fielded proposed schema with finite outcome and policy-family enums; valid/invalid fixtures exist and generic schema tests discover the family. | `CONFIRMED` shape / proposed status |
| Dedicated `PolicyDecision` validator | Schema declares `tools/validators/validate_policy_decision.py`, but that exact file is absent. | `CONFIRMED` missing at tested path |
| `DecisionEnvelope` schema | Fielded proposed schema with finite outcome and policy-family enums, reasons, obligations, evidence refs, and closed properties. | `CONFIRMED` shape / proposed status |
| `DecisionEnvelope` validator | Executable JSON Schema wrapper exists and is included in the shared five-validator aggregate. | `CONFIRMED` shape validator |
| Decision/policy fixtures | Minimal valid and missing-required-field invalid cases exist for both families. | `CONFIRMED` narrow shape coverage |
| Generic schema harness | `tests/schemas/test_common_contracts.py` discovers policy/runtime schema fixture families. | `CONFIRMED` executable harness |
| Governed API routes | Current registry contains bootstrap, layers, and evidence only; no Focus route is registered. | `CONFIRMED` |
| Governed API scaffold behavior | Executable tests require registered routes to return `ABSTAIN`, `NOT_IMPLEMENTED`, and empty evidence refs. | `CONFIRMED` scoped behavior |
| Generic browser/API guards | Executable tests prohibit internal-store path literals and forbidden direct runtime imports; route/method boundaries are checked. | `CONFIRMED` generic boundary coverage |
| Focus fixture lane | `tests/fixtures/focus/README.md` documents proposed denial fixtures; checked `deny_restricted.valid.json` and `deny_sensitive_geometry.valid.json` paths are absent. | `CONFIRMED` README / payloads not established |
| `make policy` | Emits `TODO: opa test policy/ -v`. | `CONFIRMED` placeholder |
| `make deny-test` | Emits `TODO: tests/api deny suite`. | `CONFIRMED` placeholder |
| `make schemas` | Runs the shared validator aggregate, including `DecisionEnvelope` but not a dedicated `PolicyDecision` validator. | `CONFIRMED` |
| `make test` | Runs schema and contract tests only; this lane is not included. | `CONFIRMED` |
| `make boundary-guards-ci` | Runs command-bearing generic policy/API boundary tests with JUnit output. | `CONFIRMED` generic enforcement |
| Policy/deny/Focus/Fauna workflows | `policy-test.yml`, `deny-test.yml`, `focus-mock-test.yml`, and `domain-fauna.yml` execute TODO echo steps. | `CONFIRMED` stubs |
| Production Focus policy evaluation, reason codes, routes, reports, and pass rates | Not established by inspected evidence. | `UNKNOWN` |

### Safe current conclusion

`tests/domains/fauna/focus/deny_sensitive/` is a valid documented test responsibility lane. It is **README-only at this snapshot**. The repository can validate the shape of proposed policy/runtime decision objects and enforce generic trust-membrane boundaries, but it does not yet prove Fauna-specific sensitivity evaluation, Focus pre-check execution, safe denial projection, or denial reason correctness.

[Back to top](#top)

---

## Scope and non-scope

### In scope

This lane may contain Fauna-specific tests for:

- sensitivity, rights, role, purpose, review, release, correction, withdrawal, embargo, and public-safe transformation pre-checks;
- exact-location, protected-site, observer-identity, private-stewardship, and re-identifying-join denials;
- finite `PolicyDecision`, `DecisionEnvelope`, and runtime response handling;
- safe denial reasons, obligations, alternatives, and accessible presentation;
- prevention of model invocation when pre-check denial is sufficient;
- public-safe derivative bounding and anti-reconstruction behavior;
- `ABSTAIN` behavior for evidence gaps distinct from policy `DENY`;
- `ERROR` behavior for unavailable or malformed evaluation paths;
- prevention of map-property, generated-summary, receipt, cache, log, or citation leakage;
- browser/governed-API/model/store boundary assertions;
- no-network deterministic fixture behavior; and
- correction, withdrawal, rollback, and supersession visibility where material.

### Out of scope

This lane does not own:

- executable policy rules, sensitivity taxonomies, geoprivacy parameters, role matrices, rights agreements, or transformation algorithms;
- `PolicyDecision`, `DecisionEnvelope`, Focus response, runtime response, or `AIReceipt` semantic and schema authority;
- Focus orchestration, routes, model adapters, public UI implementation, or policy evaluator implementation;
- source admission, evidence closure, review approval, release, correction, withdrawal, or rollback decisions;
- exact sensitive coordinates, real observer identities, restricted agency records, private stewardship details, or production evidence/model output;
- trust-bearing receipts, proofs, manifests, catalogs, or lifecycle records;
- reusable fixture corpora better owned by verified fixture roots; or
- live model/source/network checks in the default suite.

[Back to top](#top)

---

## Minimum denial test-case contract

Every executable case added to this lane should declare the policy context, expected decision, safe projection, and forbidden disclosure.

| Field | Required content |
|---|---|
| `case_id` | Stable, descriptive identifier. |
| Request scope | Fauna question, audience, role, purpose, spatial/temporal scope, selected surface, and requested precision. |
| Policy input posture | Synthetic sensitivity, rights, review, release, correction, embargo, transform, and source-role state. |
| Evidence posture | Expected released/admissible, missing, unresolved, stale, conflicted, candidate, or withdrawn state. |
| Pre-check expectation | Whether the request must terminate before evidence retrieval or model invocation. |
| Policy family | Accepted family such as `sensitivity` or `access`; do not invent unsupported serialized values. |
| Policy decision expectation | Expected finite result, safe reason category, obligations, and audit references. |
| Runtime expectation | Exactly one of `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Public-safe alternative | None, generalized answer, or bounded next action only when policy explicitly permits it. |
| Forbidden disclosure | Protected location, identity, source detail, transform parameter, inference clue, internal reason, or candidate content that must not appear. |
| Receipt/log expectation | Safe event metadata only; no protected payload or private reasoning. |
| Deterministic setup | Fixed time, role, scope, fixture hashes, expected ordering, and mock behavior. |
| Network posture | Denied by default; any live tier separately governed and excluded from default CI. |
| Cleanup and artifact safety | No credentials, mutable caches, production traces, source side effects, or public writes. |

A case with only `default allow := false` is not sufficient denial proof. The test must establish that the intended policy input produced the intended finite decision and safe public projection.

[Back to top](#top)

---

## Finite outcome and denial semantics

The runtime vocabulary is:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Workflow/control-plane processes may additionally use states such as `HOLD`, but a public runtime response must use the accepted finite runtime envelope.

| Outcome | Use in this lane | Must not do |
|---|---|---|
| `ANSWER` | Request is public-safe, evidence is admissible, and response remains inside the released/approved precision. | Expand a generalized derivative, omit material limitations, or rely on unavailable policy. |
| `ABSTAIN` | Evidence, citations, freshness, or closure are insufficient without a positive policy prohibition. | Imply that restricted data exists or guess a safe answer. |
| `DENY` | Policy prohibits the requested audience, purpose, precision, content, or access path. | Reveal the protected fact, exact reason detail, transform parameter, or restricted locator. |
| `ERROR` | Policy/runtime/schema/evaluator failure prevents a safe decision. | Downgrade to `ANSWER` or expose internal stack/configuration details. |

### Denial invariants

1. Pre-check denial occurs before model invocation when the decision can be made from governed request and policy metadata.
2. `DENY` contains a stable accepted reason category, not sensitive explanatory detail.
3. Denial obligations remain actionable but public-safe.
4. A generalized alternative is offered only when an accepted policy decision permits that representation.
5. Unknown policy, rights, sensitivity, review, or release state fails closed.
6. `ABSTAIN` is used for unsupported claims; `DENY` is used for prohibited claims.
7. Policy engine unavailability or malformed decision output produces `ERROR` unless an accepted fail-closed profile explicitly maps it otherwise.
8. Denial must remain distinguishable from HTTP authorization, source admission, lifecycle quarantine, review hold, and release withdrawal.
9. `AIReceipt`, log, trace, cache key, accessible label, citation, and export cannot carry more detail than the public decision.
10. A response cannot call the model after a pre-check `DENY` merely to generate a friendlier explanation.
11. A default-deny scaffold without evaluated inputs, reason, and obligations cannot be presented as a completed `PolicyDecision`.
12. No test may validate safety by including the protected real-world detail it is intended to hide.

[Back to top](#top)

---

## Required scenario families

| Scenario family | Example condition | Expected behavior |
|---|---|---|
| Valid public-safe answer | Public-safe generalized request; rights/review/release/evidence checks pass. | `ANSWER` within approved scope, with citations and limitations. |
| Exact sensitive-location request | User requests protected precision for a sensitive occurrence or site. | Pre-check `DENY`; no evidence/model retrieval if policy input is sufficient. |
| Generalized derivative escalation | Public derivative exists, but request asks to reverse or refine the transform. | `DENY`; no reconstruction clue or transform parameter. |
| Re-identifying join | Individually public-safe fields would combine to narrow a protected location. | `DENY` or policy hold in workflow; no joined detail. |
| Sensitive observer identity | Request asks for identity or re-identifying metadata. | `DENY`. |
| Rights unresolved | Rights/license/use scope is unknown or incompatible. | `DENY` or bounded `ABSTAIN` according to accepted policy. |
| Review missing | Content requires steward/reviewer approval that is absent. | Runtime `DENY`/`ABSTAIN`; workflow may `HOLD`. |
| Unreleased/candidate evidence | Support exists but is not released for the requested surface. | `ABSTAIN` or `DENY`; no internal fallback. |
| Evidence missing | No evidence supports an otherwise permissible question. | `ABSTAIN`, not fabricated `DENY`. |
| Stale evidence | Freshness policy blocks consequential use. | `ABSTAIN` or narrowly bounded stale-context answer if policy permits. |
| Corrected/withdrawn release | Prior support is no longer current or public. | Use current lineage or return a finite non-answer. |
| Embargo active | Time-bound release restriction remains active. | `DENY` without disclosing embargo-sensitive details. |
| Role mismatch | Authenticated or public role lacks the required access scope. | `DENY`; no role-escalation hint beyond safe guidance. |
| Purpose mismatch | Data may be allowed for one purpose but not the requested use. | `DENY` with safe purpose category. |
| Policy unavailable | Evaluator or required policy input cannot be loaded. | `ERROR` or accepted fail-closed decision; never `ANSWER`. |
| Malformed policy decision | Decision lacks required fields, enum values, or safe reasons. | Schema/semantic failure and runtime `ERROR`. |
| Default-deny scaffold canary | Rego returns default false without a reasoned policy result. | Test reports incomplete policy implementation, not substantive pass. |
| Receipt/log leakage | Denied payload appears in receipt, log, trace, snapshot, telemetry, cache key, or accessible text. | Test failure and private incident handling. |
| Direct model/store path | Browser attempts model, index, graph, object-store, source, or internal lifecycle access. | Boundary failure / `DENY`. |
| Prompt-injection request | Request attempts to override policy, expose hidden context, or change audience/precision. | `DENY`/`ABSTAIN`; untrusted text remains data. |
| Quarantined/unsafe fixture | Fixture contains pre-public or protected material. | Test setup failure/non-render; do not move lifecycle state here. |
| Live network/model attempt | Default test invokes external source/model/service. | Harness failure. |

[Back to top](#top)

---

## Denial proof matrix

| Test concern | Required proof | Negative assertion |
|---|---|---|
| Request scope | Audience, role, purpose, precision, time, and surface are explicit. | No implicit public-safe assumption. |
| Policy pre-check ordering | Denial occurs before evidence/model work when sufficient metadata exists. | No model invocation after pre-check `DENY`. |
| Policy input completeness | Sensitivity, rights, review, release, correction, and transform state are present or explicitly unknown. | No silent default to allow. |
| Policy decision shape | Required finite outcome, family, reasons, obligations, and evaluation time validate. | No arbitrary or incomplete decision object. |
| Policy semantics | Decision matches the intended synthetic policy state. | Schema shape alone is not semantic proof. |
| Runtime envelope | Policy result becomes the expected finite public outcome. | No hidden `ANSWER` fallback. |
| Safe reason | Public reason is useful and non-sensitive. | No protected fact or reconstructive clue in reason. |
| Bounded alternative | Any generalized response is explicitly allowed by policy. | No automatic precision escalation. |
| Evidence distinction | Missing evidence maps to `ABSTAIN`; prohibited use maps to `DENY`. | No conflation of evidence and policy. |
| Receipt/log safety | Event metadata is bounded and public-safe. | No denied payload in logs, traces, receipts, telemetry, or cache keys. |
| Browser/API boundary | Public client uses governed API and approved envelope. | No direct model/store/source/internal path. |
| Correction/release state | Withdrawn, superseded, or embargoed state is enforced. | No stale release represented as current. |
| No-network default | Synthetic local fixtures satisfy the case. | Any unexpected external call fails the harness. |

[Back to top](#top)

---

## Fixtures and test data

Two documented fixture surfaces are relevant and must not be silently collapsed:

| Fixture surface | Intended role | Current evidence |
|---|---|---|
| `tests/fixtures/focus/` | Unit-test-scoped synthetic Focus request/response examples. | README exists; checked denial payloads were absent. |
| `fixtures/domains/fauna/` | Reusable public-safe Fauna runtime/renderer/governance examples. | README and draft lanes exist; consumer alignment remains incomplete. |

Schema-focused fixture families also exist for:

- `fixtures/contracts/v1/policy/policy_decision/`; and
- `fixtures/contracts/v1/runtime/decision_envelope/`.

Those contract fixtures prove machine shape only. They are not Fauna sensitivity scenarios and do not prove an evaluator ran.

Fixture requirements:

- synthetic or explicitly public-safe;
- deterministic and no-network;
- no exact sensitive coordinates, real observer identities, private notes, restricted source payloads, transform parameters, or reconstruction-enabling combinations;
- explicit role, purpose, source role, time, rights, sensitivity, review, release, correction, embargo, transform, and expected outcome where material;
- explicit expected policy decision and public runtime projection;
- stable expected outputs when used as regression anchors;
- no production EvidenceBundle, policy decision, receipt, release manifest, or model output; and
- linked to an executable consumer before being counted as coverage.

If a fixture contains plausible protected Fauna detail, stop using it, prevent logs/artifacts from spreading it, route review privately, and replace it with a synthetic denial canary.

[Back to top](#top)

---

## Determinism, network, and live-test tiers

### Default tier: deterministic and no-network

Default tests must not depend on:

- live source services, model providers, vector indexes, graph stores, object stores, geocoders, map services, policy decision services, or public APIs;
- credentials, developer caches, browser profiles, production logs, or mutable upstream data;
- current time without a fixed clock;
- uncontrolled role, purpose, locale, timezone, seed, ordering, retry, or model sampling;
- network-installed data during the assertion phase; or
- direct source, lifecycle, release, or public-write side effects.

Unexpected network access is a test failure.

### Separate live/integration tier

A future live tier may exist only when separately named, explicitly triggered, excluded from default CI, source-terms-aware, read-only unless independently authorized, secret-safe for fork PRs, timeout/retry bounded, and unable to publish. No such Fauna Focus deny-sensitive tier was established in the inspected repository.

[Back to top](#top)

---

## Current execution and CI surface

### Repository-native commands observed

| Surface | Observed behavior | Deny-sensitive coverage |
|---|---|---|
| `make test` | Runs `python -m pytest tests/schemas tests/contracts -q`. | Contract/schema shape only; not this lane. |
| `make schemas` | Runs five JSON Schema validators including `DecisionEnvelope`. | No dedicated `PolicyDecision` validator; no policy semantics. |
| `make policy` | Echoes `TODO: opa test policy/ -v`. | No OPA test execution. |
| `make deny-test` | Echoes `TODO: tests/api deny suite`. | No denial suite. |
| `make governed-api-smoke` | Runs current governed-API tests. | Scaffold routes only; no Focus route. |
| `make boundary-guards-ci` | Runs generic policy/API/store/import boundary tests with JUnit. | Real generic boundary proof; not Fauna sensitivity evaluation. |
| Generic schema harness | Discovers policy/runtime valid and invalid fixture families. | Proves proposed object shape only. |
| `DecisionEnvelope` validator | Executable shared JSON Schema wrapper. | Shape only; no policy evaluation. |
| `PolicyDecision` validator | Declared by schema but missing at tested path. | Not established. |

### Workflow status

| Workflow | Current steps | Interpretation |
|---|---|---|
| `policy-test.yml` | `echo TODO opa-test`; `echo TODO policy-fixture-coverage` | Stub only. |
| `deny-test.yml` | TODO public-boundary, raw-leak, and model-runtime deny echoes. | Stub only. |
| `focus-mock-test.yml` | TODO Focus-flow and finite-envelope echoes. | Stub only. |
| `domain-fauna.yml` | TODO validate/proof/publish-dry-run echoes. | Stub only. |

### Proposed future targeted command

Once executable modules and fixture consumers exist, a targeted command may take the form:

```bash
python -m pytest tests/domains/fauna/focus/deny_sensitive -q
```

A policy-specific command may later include an accepted OPA test path, but `make policy` is currently a placeholder. Future commands must collect intended cases, fail on zero collection/unexpected skips, remain no-network, and call accepted policy/runtime implementations rather than redefining decisions locally.

[Back to top](#top)

---

## Validation layers and expected outcomes

| Validation layer | What it can prove for the exact test packet | Current maturity |
|---|---|---|
| README/test contract | Intended rules, authority boundaries, and scenario families are documented. | Available here; not executable proof. |
| `PolicyDecision` schema | Proposed decision object has required fields/enums and closed properties. | Fielded schema + generic fixtures/tests; dedicated validator absent. |
| `DecisionEnvelope` schema | Proposed runtime decision object has required fields/enums and closed properties. | Fielded schema + fixtures + validator + aggregate registration. |
| Rego parse/default | Policy files are syntactically loadable and default to no allow. | Rego files are minimal scaffolds; no direct tests established. |
| Policy semantic tests | Synthetic inputs produce correct reasoned allow/deny/abstain/error results. | Not established. |
| Focus pre-check ordering | Policy terminates before evidence/model invocation when appropriate. | No Focus route/evaluator test established. |
| Governed API runtime | Finite public envelope matches policy result. | Generic scaffold route behavior only. |
| Browser/store boundary | Client/API avoids direct internal/model/store paths. | Generic executable guards exist. |
| Safe projection/leak scan | Denial text, citations, logs, traces, receipts, telemetry, cache keys, and UI omit protected detail. | Needs dedicated fixtures/tests. |
| No-network guard | No unexpected external request occurs. | Required future harness behavior. |
| CI orchestration | Repository-native policy/denial tests run on relevant changes. | Policy/deny/Focus/Fauna workflows are TODO-only. |

Test reporting should distinguish:

```text
PASS | FAIL | PARTIAL | NOT RUN | NOT APPLICABLE | UNKNOWN
```

Runtime expectations use:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

A schema `PASS` or a Rego default of `false` must not be reported as proof that a complete, correctly reasoned, safely projected Fauna denial occurred.

[Back to top](#top)

---

## Failure interpretation

| Observed result | Interpretation | Required response |
|---|---|---|
| Sensitive request produces `ANSWER` | Policy/trust-membrane failure. | Fail closed; investigate request scope and policy binding. |
| Denial occurs only after model invocation | Ordering/data-minimization defect. | Fail; move sufficient policy pre-check earlier. |
| Missing evidence produces policy `DENY` without policy basis | Evidence/policy conflation. | Fail; use `ABSTAIN` or accepted error path. |
| Unknown sensitivity/rights/review/release produces `ANSWER` | Fail-open defect. | Fail closed. |
| Generalized derivative is expanded | Transformation/re-identification defect. | Fail and withdraw unsafe expected output. |
| Denial reason reveals protected fact or transform detail | Security/sensitivity incident. | Stop dissemination and route private review. |
| Receipt/log/trace contains denied payload | Audit/telemetry leakage. | Fail and contain artifacts. |
| Policy object passes schema but decision is semantically wrong | Shape-only pass. | Fail semantic test; schema is not policy authority. |
| `default allow := false` is treated as a complete denial | Scaffold overclaim. | Report implementation gap; require reasoned decision output. |
| Policy evaluator unavailable | Runtime safety failure. | `ERROR` or accepted fail-closed outcome; never `ANSWER`. |
| Malformed decision/envelope | Contract failure. | Reject and return bounded `ERROR`. |
| Browser calls model/index/store/source directly | Boundary violation. | Fail/deny. |
| Zero tests collected | No proof executed. | Fail or invalidate the run. |
| Test skipped or TODO workflow succeeds | Coverage gap/scaffold result. | Report `NOT RUN`/placeholder, not pass. |
| Unexpected network request | Hermeticity failure. | Fail default tier. |
| Flaky time/role/order result | Determinism defect. | Fix/quarantine from authority claims; retain failure evidence. |

[Back to top](#top)

---

## What a passing suite does not prove

Even a substantive passing Fauna Focus deny-sensitive suite would not, by itself, prove:

- that all sensitive taxa, sites, rights agreements, purposes, roles, or jurisdictions are modeled;
- correctness of untested policy inputs or source classifications;
- absence of re-identification through untested cross-domain joins;
- policy approval, review approval, release approval, or publication authority;
- field completeness or acceptance of proposed policy/runtime schemas;
- safe behavior across every client, export, log, telemetry, cache, and assistive-technology surface;
- production Focus route deployment, model safety, or branch-protection enforcement;
- that a receipt, schema pass, default-deny rule, map style, or workflow name is sovereign truth; or
- that a denied request may never be answered through a separately authorized steward-only path.

A passing test is a scoped review signal. It does not create policy, classify a real record, or publish a Fauna answer.

[Back to top](#top)

---

## Review burden

Reviewers should be able to answer:

- Does each case declare audience, role, purpose, precision, time, and surface?
- Are sensitivity, rights, review, release, correction, embargo, and transform states explicit?
- Is policy pre-check ordered before evidence/model work where possible?
- Are `DENY`, `ABSTAIN`, and `ERROR` used for the correct kinds of failure?
- Is the public reason useful without disclosing the protected fact?
- Does any generalized alternative have explicit policy support?
- Do text, citations, accessible names, receipts, logs, traces, snapshots, telemetry, cache keys, and exports avoid withheld detail?
- Are fixtures synthetic/public-safe, deterministic, no-network, and linked to consumers?
- Are tests calling canonical policy/runtime implementations when they exist rather than redefining policy locally?
- Are schema passes, default-deny scaffolds, TODOs, skips, absent payloads, and workflow names reported as limited evidence?
- Does the PR identify workflow triggers, generated receipt, validation, rollback, and required human reviewers?

Changes affecting sensitivity classification, rights, public-safe transforms, reason taxonomies, access roles, or release behavior require the corresponding stewards. This test lane cannot approve those decisions.

[Back to top](#top)

---

## Maintenance and fixture updates

Update this README when:

- executable tests, fixtures, policy rules, evaluators, schemas, routes, UI projections, or reason-code registries are added or moved;
- a canonical Focus policy bundle is accepted;
- Fauna sensitivity Rego/YAML scaffolds become operational;
- `PolicyDecision` or `DecisionEnvelope` semantics/shapes change;
- a Focus route or policy pre-check implementation is added;
- policy, deny, Focus, or Fauna workflows graduate from TODO stubs;
- fixture ownership between `tests/fixtures/focus/` and `fixtures/domains/fauna/` is resolved;
- logging/telemetry/cache disclosure rules change; or
- the Directory Rules authority-path conflict is resolved.

For each fixture or expected-output update:

1. identify the consuming test and policy scenario;
2. verify synthetic/public-safe provenance and sensitivity posture;
3. pin role, purpose, time, scope, precision, release, correction, and expected decision;
4. update expected policy and runtime outputs intentionally;
5. run targeted, schema, policy, boundary, and affected broader checks when available;
6. inspect logs, traces, snapshots, receipts, telemetry, cache keys, and UI text for disclosure; and
7. document whether the update is a correction, new scenario, or accepted policy/contract change.

Do not regenerate expected denials merely to make a failing policy test disappear.

[Back to top](#top)

---

## Definition of done

This lane is mature only when repository evidence supports all applicable criteria:

- [ ] At least one executable test module exists and the targeted command collects intended cases.
- [ ] Accepted Fauna sensitivity and Focus policy inputs/rules are operational and versioned.
- [ ] Policy tests produce reasoned finite decisions rather than default-only false results.
- [ ] `PolicyDecision` and runtime envelope schemas/contracts are accepted or explicitly versioned.
- [ ] A verified policy evaluator and Focus pre-check integration exist.
- [ ] Exact-sensitive, derivative-escalation, re-identifying-join, rights, review, release, embargo, role, purpose, evidence-gap, correction, malformed-decision, evaluator-error, leakage, direct-model, quarantined-fixture, and no-network cases execute.
- [ ] Tests distinguish `DENY`, `ABSTAIN`, `ERROR`, and workflow `HOLD`.
- [ ] Denial reasons and obligations are safe, stable, accessible, and non-reconstructive.
- [ ] No model is invoked after a sufficient pre-check denial.
- [ ] Fixtures are synthetic/public-safe, deterministic, no-network, and linked to consumers.
- [ ] Generic schema/boundary checks are supplemented by Fauna-specific policy semantics.
- [ ] TODO-only workflows are graduated to repository-native commands with reviewed triggers and permissions.
- [ ] Zero collection, unexpected skips, unexpected network access, shape-only success, and default-deny-only success cannot be misreported as proof.
- [ ] Human Fauna, Focus, policy, sensitivity, rights, API/UI, test, security, and docs review is recorded where required.
- [ ] Coverage limits, correction behavior, rollback, and open authority conflicts remain documented.

At this evidence snapshot, these criteria remain open unless a separate executable artifact proves them.

[Back to top](#top)

---

## Evidence ledger

| Evidence location at pinned base | Observation supported |
|---|---|
| `tests/domains/fauna/focus/deny_sensitive/README.md` | Existing v0.1 baseline and prior blob. |
| `tests/README.md` | Canonical test root, narrow root test target, and mixed maturity. |
| `tests/domains/fauna/README.md` | Parent Fauna test boundary. |
| `tests/domains/fauna/focus/README.md` | Parent Focus lane and deny-sensitive child responsibility. |
| `tests/domains/fauna/focus/citation/README.md` | Sibling cite-or-abstain boundary and current Focus/citation maturity. |
| `CONTRIBUTING.md` | Branch/PR, preservation, Directory Rules conflict, validation, receipt, and rollback expectations. |
| Both Directory Rules paths | Shared target-placement rule and unresolved authority-copy conflict. |
| `docs/architecture/governed-ai/FOCUS_FLOW.md` | Policy pre-check/evidence/adapter/citation/post-check/envelope doctrine. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Fauna Focus denial, geoprivacy, finite outcomes, and governed API boundaries. |
| `docs/domains/fauna/SENSITIVITY.md` | Deny-by-default protected-detail posture and non-disclosure rule. |
| Fauna domain/sensitivity policy READMEs | Explicit greenfield/scaffold status. |
| Fauna sensitivity Rego files | Default-only deny scaffolds with no evaluated rules. |
| Fauna sensitivity YAML files | Placeholder policy inventories with no operational values. |
| `policy/focus/README.md` | One-line greenfield Focus policy stub. |
| `PolicyDecision` schema/fixtures | Fielded proposed shape and narrow generic fixture coverage. |
| Missing dedicated `PolicyDecision` validator path | Direct validator implementation not established. |
| `DecisionEnvelope` schema/fixtures/validator | Fielded proposed shape, narrow fixtures, executable wrapper, aggregate registration. |
| Generic schema harness | Policy/runtime fixtures are executable shape tests. |
| Governed API route registry and abstain tests | Only bootstrap/layers/evidence routes; safe scaffold `ABSTAIN / NOT_IMPLEMENTED`. |
| Explorer/governed-API boundary guards | Generic direct-store/import/route boundary enforcement. |
| Focus fixture README and checked absent denial payloads | Proposed scenarios; no checked payload implementation. |
| Makefile | Policy/deny placeholders; real schema and generic boundary commands. |
| Policy, deny, Focus-mock, and Fauna workflows | TODO-only CI scaffolds. |

[Back to top](#top)

---

## Open verification register

| Question | Status | Evidence needed |
|---|---|---|
| Are there unindexed or branch-local executable tests in this lane? | `NEEDS VERIFICATION` | Complete tree read and test collection. |
| Which Focus/Fauna policy bundle is canonical? | `CONFLICTED` / `NEEDS VERIFICATION` | Accepted policy ownership, package names, evaluator wiring, and ADR/migration record. |
| When do Fauna sensitivity Rego/YAML scaffolds become operational? | `PROPOSED` work | Reviewed rules, safe parameters, fixtures, OPA tests, versioning, and rollback. |
| Which policy input contract is canonical for Focus pre-check? | `NEEDS VERIFICATION` | Accepted contract/schema and fixtures. |
| Is `PolicyDecision` or `DecisionEnvelope` the primary Focus denial carrier? | `NEEDS VERIFICATION` | Accepted semantic mapping and runtime/API integration. |
| When will the dedicated `PolicyDecision` validator exist? | `NEEDS VERIFICATION` | Executable path, registry/aggregate wiring, fixtures, tests, CI. |
| Which safe reason codes and obligations are accepted? | `UNKNOWN` | Policy/contract registry and public-projection review. |
| Which Focus route and service perform pre-checks? | `UNKNOWN` | Implemented route registry and governed-API tests. |
| Which fixture root owns generic versus Fauna-reusable denial cases? | `NEEDS VERIFICATION` | Accepted fixture routing and consumers. |
| Which policy/deny/Focus/Fauna checks are required by branch protection? | `UNKNOWN` | Repository ruleset evidence. |
| When do policy-test, deny-test, focus-mock-test, and domain-fauna graduate from stubs? | `PROPOSED` work | Owners, commands, fixtures, permissions, outcomes, rollback. |
| Which Directory Rules copy becomes canonical? | `CONFLICTED` / `NEEDS VERIFICATION` | Accepted ADR and synchronized supersession/migration. |

[Back to top](#top)

---

## Changelog and rollback

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README scaffold for the Fauna Focus deny-sensitive test lane. |
| 2026-07-17 | v0.2 | Repository-grounded maturity refresh; added complete denial-test profile, current policy/schema/validator/API/fixture/workflow evidence, finite outcome semantics, scenario matrix, deterministic/no-network rules, failure interpretation, non-proof limits, maintenance, evidence ledger, and explicit authority conflicts. |

### Rollback

This is a documentation-only revision. Restore v0.1 by reverting the implementation commit or replacing this file with blob `f90aec1025a101cc8f158a4780ec6c690040211d`. A revert changes documentation only; it does not alter tests, fixtures, policy, schemas, validators, routes, workflows, data, release state, or publication.

### Re-review triggers

Re-review on the first executable deny-sensitive test, operational Fauna policy rule, policy fixture, dedicated policy validator, accepted decision carrier mapping, Focus route, safe reason registry, substantive policy/deny workflow, public denial projection, or Directory Rules authority resolution.

[Back to top](#top)
