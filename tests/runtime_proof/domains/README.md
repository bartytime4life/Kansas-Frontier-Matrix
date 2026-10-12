<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-runtime-proof-domains-readme
title: tests/runtime_proof/domains/ — Domain Runtime-Proof Placement, Registration, and Finite-Outcome Guardrail
type: readme; directory-readme; domain-runtime-proof-index; placement-guardrail; finite-outcome-test-contract; migration-index
version: v0.2
status: draft; current-repository-index; one-direct-child; alternate-domain-first-lane-present; placement-conflicted; index-only; frozen-for-new-children; executable-depth-unverified; no-dedicated-ci; NEEDS VERIFICATION
policy_label: public-doc; restricted-review-when-child-domain-sensitivity-requires
owners: OWNER_TBD — QA steward · Runtime-proof steward · Domain architecture steward · Governed API steward · Evidence steward · Policy steward · Rights/sensitivity reviewer · Release steward · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
current_path: tests/runtime_proof/domains/README.md
truth_posture: CONFIRMED target README and prior blob, tests responsibility root, tests/runtime_proof parent, merged Roads–Rail–Trade child, alternate Flora runtime-proof lane under tests/domains/flora, shared RuntimeResponseEnvelope contract/schema/validator/minimal fixtures, root Makefile test scope, validator-suite workflow scope, and bounded absence of other surfaced children or a dedicated runtime-proof workflow at the pinned snapshot / PROPOSED accepted domain runtime-proof placement, child registration mechanism, executable test matrix, fixture profiles, route bindings, reason-code vocabulary, CI gate, migration winner, compatibility redirects, and machine registry / CONFLICTED tests/runtime_proof/domains/<domain> capability-first placement versus tests/domains/<domain>/runtime_proof domain-first placement / UNKNOWN exhaustive recursive child inventory, executable modules outside bounded search, current pass state, route coverage, production behavior, public-client conformance, and release integration / NEEDS VERIFICATION owners, Directory Rules or ADR resolution, complete inventory, consumer graph, workflow triggers, test collection, fixture coverage, evidence resolution, correction propagation, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b902a5c34165ac55d2bb46b470f21e4002cf505f
  prior_blob: 0264e3a335a13dee0fc7aa6accd20b0c87af0cfd
related:
  - ../../README.md
  - ../README.md
  - ./roads-rail-trade/README.md
  - ../../domains/flora/runtime_proof/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/architecture/domain-placement-law.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../fixtures/contracts/v1/runtime/runtime_response_envelope/valid/README.md
  - ../../../fixtures/contracts/v1/runtime/runtime_response_envelope/invalid/README.md
  - ../../../tests/domains/README.md
  - ../../../Makefile
  - ../../../.github/workflows/validator-suite.yml
  - ../../../.github/workflows/domain-roads-rail-trade.yml
tags: [kfm, tests, runtime-proof, domains, placement, finite-outcomes, runtime-response-envelope, answer, abstain, deny, error, evidence, policy, release, correction, rollback, no-network, synthetic-fixtures, migration, no-parallel-authority]
notes:
  - "v0.2 replaces a narrow aspirational index with a repository-grounded placement, child-registration, CI, migration, and rollback guardrail."
  - "The direct child roads-rail-trade/ is merged and README-only in bounded evidence."
  - "A Flora runtime-proof README exists under tests/domains/flora/runtime_proof/, creating a capability-first versus domain-first placement conflict."
  - "This parent is INDEX_ONLY and FROZEN_FOR_NEW_CHILDREN until Directory Rules or an ADR selects one executable placement convention."
  - "This revision changes documentation only and creates, moves, deletes, or activates no test, fixture, route, schema, validator, workflow, package, policy, data, receipt, proof, or release record."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/runtime_proof/domains/` — Domain Runtime-Proof Placement, Registration, and Finite-Outcome Guardrail

> **Purpose.** Keep domain-bounded runtime proof inspectable and non-duplicative while KFM resolves whether executable domain runtime tests belong in a capability-first tree (`tests/runtime_proof/domains/<domain>/`) or inside each domain test package (`tests/domains/<domain>/runtime_proof/`).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Role: index only" src="https://img.shields.io/badge/role-INDEX__ONLY-purple">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="New children: frozen" src="https://img.shields.io/badge/new__children-FROZEN-red">
  <img alt="CI: not dedicated" src="https://img.shields.io/badge/CI-NOT__DEDICATED-lightgrey">
</p>

> [!IMPORTANT]
> This directory is a **human routing and migration index**. It is not a runtime implementation, governed API route, domain package, fixture authority, contract or schema home, policy authority, evidence store, receipt or proof store, release authority, publication surface, or machine registry.

> [!WARNING]
> Repository evidence currently supports two competing executable placements:
>
> ```text
> tests/runtime_proof/domains/<domain>/       # capability-first
> tests/domains/<domain>/runtime_proof/       # domain-first
> ```
>
> Do not create a new child in either pattern, copy a test suite between them, or declare one canonical by README assertion. Resolve the convention through Directory Rules clarification or an ADR-backed migration.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Placement](#placement-and-authority) · [Inventory](#current-repository-inventory) · [Registration](#child-lane-registration-contract) · [Envelope](#shared-runtime-envelope-baseline) · [Outcomes](#finite-outcome-discipline) · [Composition](#cross-lane-composition) · [Coverage](#required-domain-runtime-proof-families) · [Fixtures](#fixture-and-test-data-contract) · [Network](#network-rights-and-sensitivity-boundary) · [CI](#ci-and-gate-acceptance) · [Review](#review-burden) · [Migration](#placement-resolution-and-migration) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/runtime_proof/domains/README.md` | **CONFIRMED** | Parent exists; prior blob is pinned in metadata. |
| Direct child `roads-rail-trade/` | **CONFIRMED merged v0.2** | Detailed child README exists; bounded evidence classifies it as README-only and not CI-closed. |
| Other direct children under this parent | **NOT SURFACED in bounded search** | Do not invent a broader direct-child inventory. |
| `tests/domains/flora/runtime_proof/` | **CONFIRMED alternate placement** | Flora runtime-proof README exists under the domain-first tree and identifies itself as a scaffold. |
| Other domain-first runtime-proof lanes | **NOT SURFACED in bounded search** | Flora is the only alternate lane confirmed in this update. |
| Direct executable files in this parent | **NOT SURFACED in bounded search** | This parent is an index, not executable proof. |
| Direct executable files in the confirmed child lanes | **NOT ESTABLISHED** | README presence does not prove collection or execution. |
| `tests/runtime_proof/README.md` | **CONFIRMED draft parent** | Names finite-outcome and abstain proof; executable depth remains unverified. |
| `tests/README.md` | **CONFIRMED canonical test root** | Separately lists `tests/runtime_proof/` and `tests/domains/<domain>/`, producing the unresolved intersection documented here. |
| Shared `RuntimeResponseEnvelope` contract/schema | **CONFIRMED paired / schema status PROPOSED** | A closed shared envelope shape exists with four finite outcomes. |
| Shared envelope validator | **CONFIRMED executable wrapper** | Proves JSON Schema shape when invoked; does not prove domain semantics or runtime behavior. |
| Shared envelope fixture family | **CONFIRMED minimal** | One minimal valid `ABSTAIN` case and one missing-`id` invalid case are documented. |
| Root `make test` | **CONFIRMED narrow** | Runs `tests/schemas` and `tests/contracts`; it does not collect this parent or its children. |
| `validator-suite` workflow | **CONFIRMED schema-oriented** | Runs `make schemas` plus one fail-closed evidence-bundle check; it is not runtime-proof CI. |
| Dedicated domain runtime-proof workflow | **NOT SURFACED in bounded search** | Do not claim this parent or either child convention runs as a required gate. |
| Current test pass state | **UNKNOWN** | Repository inspection is not execution evidence. |
| Production runtime behavior | **UNKNOWN** | Documentation, schema fixtures, and workflow presence do not prove deployed behavior. |

**Authority of this README:** parent-lane routing, placement warnings, child-index expectations, shared finite-outcome invariants, minimum proof coverage, migration discipline, correction guidance, and rollback guidance.

The following outrank this README for their own responsibilities:

- accepted Directory Rules and ADRs;
- semantic contracts;
- machine schemas;
- policy bundles and decisions;
- source registries, catalog records, evidence, receipts, and proofs;
- executable runtime and governed API code;
- executable tests and validators;
- CI definitions and logs;
- release, correction, withdrawal, supersession, and rollback records;
- steward decisions.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from repository files, commit history, schema shape, or inspected implementation. |
| **PROPOSED** | A design, convention, registry, test, fixture, or procedure not yet accepted or implemented. |
| **CONFLICTED** | Two repository or doctrine surfaces point to incompatible executable homes or responsibilities. |
| **NEEDS VERIFICATION** | Checkable, but not sufficiently proven for reliance or promotion. |
| **UNKNOWN** | Not established by the inspected evidence. |

[Back to top](#top)

---

<a id="purpose-and-scope"></a>

## Purpose and scope

This parent exists to answer five governance questions:

1. Which domain runtime-proof lanes are actually present?
2. Which placement convention does each lane use?
3. What shared finite-outcome contract must every child respect?
4. How must child tests compose domain, API, evidence, policy, release, UI, and rollback proof without copying authority?
5. How can KFM migrate to one executable convention without losing history, coverage, or rollback?

### In scope

- a human-readable child index;
- placement status and compatibility warnings;
- registration requirements for new or migrated child lanes;
- shared `RuntimeResponseEnvelope` expectations;
- finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` semantics;
- cross-lane composition rules;
- minimum fixture and negative-test coverage;
- no-network, rights, sensitivity, and leakage rules;
- CI acceptance requirements;
- migration, correction, deprecation, and rollback procedures.

### Out of scope

- implementing governed API routes;
- implementing domain packages;
- defining domain contracts or schemas;
- creating policy rules or reason-code authority;
- storing fixture collections, runtime responses, logs, screenshots, evidence, receipts, proofs, or releases;
- treating a child README as executable proof;
- selecting an architecture winner without the required governance decision.

[Back to top](#top)

---

<a id="placement-and-authority"></a>

## Placement and authority

### Directory Rules basis

KFM places files by primary responsibility:

```text
tests/                              enforceability proof
tests/runtime_proof/                shared finite-outcome and trust-membrane proof
tests/domains/<domain>/             domain-owned test package
apps/governed-api/                  trust-membrane runtime implementation
packages/domains/<domain>/          domain implementation
contracts/                          semantic meaning
schemas/                            machine-checkable shape
policy/                             admissibility and obligations
fixtures/ and tests/fixtures/       synthetic test examples
data/receipts/ and data/proofs/     emitted audit and proof records
release/                            promotion, correction, withdrawal, rollback
```

Both disputed runtime-proof placements remain beneath the correct `tests/` responsibility root. The conflict is narrower: **which second-level organizing principle owns the executable domain runtime suite?**

### Competing placement models

| Model | Path | Strength | Risk |
|---|---|---|---|
| Capability-first | `tests/runtime_proof/domains/<domain>/` | Centralizes finite-outcome conventions, shared harnesses, and cross-domain comparison. | Can duplicate or fragment the domain's broader test package. |
| Domain-first | `tests/domains/<domain>/runtime_proof/` | Keeps all domain tests under one steward-owned package and aligns with `tests/domains/<domain>/`. | Can duplicate shared runtime harnesses and make parent-wide coverage harder to inspect. |
| Index-plus-executable split | Parent index in one path, tests in the other | Could preserve navigation while avoiding duplicate code. | Requires explicit compatibility semantics; otherwise two homes appear authoritative. |

### Current interim classification

| Field | Value |
|---|---|
| Parent role | `INDEX_ONLY` |
| Placement state | `CONFLICTED` |
| New-child posture | `FROZEN_FOR_NEW_CHILDREN` |
| Existing direct child | Preserve in place until migration decision |
| Existing domain-first lane | Preserve in place until migration decision |
| Executable authority | None granted by this README |
| Machine registry | Not confirmed |
| Required decision | Directory Rules clarification or ADR-backed placement/migration decision |

### Interim no-drift rule

Until the placement decision is accepted:

1. do not create another domain child under this parent;
2. do not create another `tests/domains/<domain>/runtime_proof/` lane;
3. do not copy tests or fixtures between the two patterns;
4. do not rename or delete either confirmed lane;
5. do not make workflow filters depend on an unaccepted new path;
6. record proposed additions in the verification backlog instead;
7. keep shared finite-outcome helpers outside domain children when they are genuinely reusable.

This freeze does not prohibit correcting documentation, fixing an existing executable test in place, or adding a regression test required to close a defect in an already established child. Such a change must remain scoped and must not create a second authority home.

[Back to top](#top)

---

<a id="current-repository-inventory"></a>

## Current repository inventory

### Parent and direct child

```text
tests/runtime_proof/
├── README.md
└── domains/
    ├── README.md                         # this file
    └── roads-rail-trade/
        └── README.md
```

Bounded search did not surface another direct child or a direct executable file under this parent.

### Alternate domain-first lane

```text
tests/domains/
└── flora/
    └── runtime_proof/
        └── README.md
```

The Flora README states that executable tests, fixtures, runtime envelopes, validators, routes, and CI remain unverified. It also asks whether shared finite-outcome tests should live under `tests/runtime_proof/`.

### Child posture index

| Domain | Current path | Pattern | Document status | Executable status | CI status | Parent action |
|---|---|---|---|---|---|---|
| Roads–Rail–Trade | `tests/runtime_proof/domains/roads-rail-trade/` | Capability-first | Detailed v0.2 README merged | README-only in bounded evidence | Domain workflow is echo-only; no dedicated runtime-proof gate | Index and preserve; do not duplicate |
| Flora | `tests/domains/flora/runtime_proof/` | Domain-first | Draft v0.1 scaffold | Unknown / not verified | No dedicated runtime-proof gate surfaced | Cross-link as alternate placement; do not copy |
| Other domains | Not surfaced | Unknown | Unknown | Unknown | Unknown | Do not invent or pre-create |

### Shared runtime proof surfaces

```text
contracts/runtime/runtime_response_envelope.md
schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
tools/validators/validate_runtime_response_envelope.py
fixtures/contracts/v1/runtime/runtime_response_envelope/
├── valid/
└── invalid/
```

These shared surfaces establish a shape and validator baseline. They do not establish any domain route, domain payload, evidence resolution, policy decision, release state, UI behavior, or production enforcement.

[Back to top](#top)

---

<a id="child-lane-registration-contract"></a>

## Child-lane registration contract

No accepted machine-readable child registry was surfaced. Until one is accepted, this README is the human index.

A child may be listed as implementation-bearing only when its README records all fields below.

### Required registration fields

| Field | Requirement |
|---|---|
| Domain id | Accepted domain segment and display name |
| Exact path | Current executable path, not a proposed alternative |
| Placement model | `capability-first`, `domain-first`, or `compatibility-index` |
| Status | One finite child status from the table below |
| Owners | Domain, runtime-proof, governed API, evidence, policy, release, CI, and docs reviewers |
| Runtime surfaces | Named surface categories; route names only when verified |
| Shared envelope | Accepted contract/schema version and validator |
| Domain payload | Paired contract/schema, or explicit absence |
| Fixture roots | Exact valid, invalid, deny, abstain, error, correction, and rollback fixture locations |
| Executable commands | Repository-native commands that collect non-zero tests |
| CI workflow | Workflow name, trigger paths, required status, and artifact behavior |
| Trust boundaries | Internal-store, direct-model, source-role, rights, sensitivity, and release prohibitions |
| Correction path | How corrected or withdrawn runtime state reaches tests and clients |
| Rollback target | Prior known-good tests, fixtures, runtime version, and public state |
| Evidence basis | Current commit/file evidence supporting implementation claims |

### Finite child statuses

| Status | Meaning |
|---|---|
| `DOCUMENTED_ONLY` | README exists; executable tests are not confirmed. |
| `EXECUTABLE_UNWIRED` | Tests exist and collect locally, but required CI is not established. |
| `EXECUTABLE_WIRED` | Tests collect in required CI with negative canaries and bounded artifacts. |
| `MIGRATION_PENDING` | Child is moving to the accepted placement and has a compatibility plan. |
| `COMPATIBILITY_INDEX` | Path is retained only to redirect and preserve history; no duplicate tests live here. |
| `DEPRECATED` | No new use; consumers are migrating and a removal window is recorded. |
| `RETIRED` | Inbound references are closed, history is preserved, and the accepted replacement is active. |
| `CONFLICTED` | Placement, ownership, or authority remains unresolved. |

A child must not be marked `EXECUTABLE_WIRED` merely because a general repository workflow is green. The workflow must collect that child, exercise its negative canaries, and fail when zero tests run.

### Registration update rule

When a child changes status:

1. update the child README;
2. update this parent index;
3. update the accepted machine registry if one exists later;
4. update workflow paths and commands;
5. update fixtures and expected outcomes;
6. update correction and rollback references;
7. preserve the prior status in a changelog or migration record.

[Back to top](#top)

---

<a id="shared-runtime-envelope-baseline"></a>

## Shared runtime envelope baseline

The confirmed shared `RuntimeResponseEnvelope` schema currently requires:

```text
id
spec_hash
version
issued_at
outcome
reason_code
evidence_refs
policy_state
freshness
correction_state
```

It also:

- closes `outcome` to `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- rejects additional properties;
- requires a SHA-256-shaped `spec_hash`;
- references the shared `EvidenceRef` schema;
- names a shared validator and fixture root;
- remains marked `PROPOSED`.

### Parent invariant

Every domain runtime-proof child must either:

1. validate the shared envelope directly; or
2. validate an accepted domain profile that composes the shared envelope without weakening its required fields or finite outcome set.

A domain-specific payload must not be smuggled into the closed shared envelope through undocumented fields. Use a separately paired payload contract/schema and an explicit reference or composition rule.

### Shape proof is not runtime proof

A passing shared fixture proves only that JSON matches the schema.

It does not prove:

- the route exists;
- the payload is semantically valid;
- evidence refs resolve;
- cited evidence supports the claim;
- policy evaluation is correct;
- rights and sensitivity obligations were applied;
- release state permits public use;
- correction state is current;
- clients obey the outcome;
- caches, exports, maps, or AI surfaces are safe.

### Shared baseline test requirements

The parent expects shared coverage for:

- all required fields;
- closed outcome enum;
- invalid outcome rejection;
- digest pattern;
- date-time validation;
- additional-property rejection;
- EvidenceRef shape;
- safe reason-code behavior;
- state-field controlled vocabularies once accepted;
- correction and supersession transitions;
- backward-compatible version handling.

Domain children should consume these shared tests or fixtures rather than copy them.

[Back to top](#top)

---

<a id="finite-outcome-discipline"></a>

## Finite outcome discipline

### System outcomes

| Outcome | Required meaning | Required child assertion |
|---|---|---|
| `ANSWER` | The runtime may present a substantive, evidence-supported, policy-permitted, release-aware result. | Evidence resolves; payload validates; obligations are applied; public client receives only allowed fields. |
| `ABSTAIN` | Evidence, citation support, freshness, scope, or context is insufficient for a supported answer. | No substantive claim or inferred answer leaks through payload, reason, metadata, map, export, or AI text. |
| `DENY` | Policy, rights, sensitivity, consent, access, review, or release posture forbids delivery. | Restricted payload is absent; denial is visible and safe; no side-channel reveals the protected answer. |
| `ERROR` | Validation, adapter, contract, dependency, configuration, or infrastructure failure prevents safe completion. | Error is finite and safe; no fallback claim, internal path, credential, stack trace, or hidden source detail leaks. |

### Test results

| Test result | Meaning |
|---|---|
| pass | Observed behavior matches the expected system outcome and leakage posture. |
| fail | Observed behavior violates the test contract. |
| skip | A declared prerequisite is unavailable; it is not proof of success. |
| expected failure | A tracked defect remains open with an owner and expiry. |
| infrastructure error | The suite could not evaluate behavior; product behavior is not proven. |
| zero tests collected | Configuration failure for a required child lane. |

A test expecting `DENY` passes when the system denies safely. A runtime `ERROR` is not automatically a failed test if `ERROR` is the expected bounded outcome. Conversely, a green test that merely checks HTTP status without validating the finite outcome and leakage posture is insufficient.

### Forbidden outcome collapse

Children must reject or normalize unregistered public outcomes such as:

```text
PARTIAL
PENDING
UNKNOWN
SUCCESS
FAILED
ACCEPTED
HOLD
```

Internal validation, promotion, correction, or workflow systems may use other finite vocabularies, but public runtime responses must map deliberately to the shared four-outcome contract.

[Back to top](#top)

---

<a id="cross-lane-composition"></a>

## Cross-lane composition

Domain runtime proof is an integration seam. It must compose other test responsibilities without copying their authority.

| Concern | Primary proof home | Domain runtime child's responsibility |
|---|---|---|
| Shared envelope shape | `tests/schemas/`, runtime contract fixtures, validator tests | Validate emitted envelope and version compatibility |
| Domain object meaning | `tests/domains/<domain>/contracts/` or equivalent | Assert emitted payload uses accepted semantics |
| Domain schema shape | domain schema tests | Validate payload or payload reference |
| Source-role behavior | domain source/evidence tests | Prove runtime does not upcast convenience/context sources |
| Evidence resolution | evidence resolver and domain evidence tests | Prove `ANSWER` resolves support or returns `ABSTAIN` |
| Policy and sensitivity | policy tests | Prove finite `DENY`/obligation behavior |
| Governed API route | `tests/api/` and app-owned tests | Prove transport plus domain composition |
| Public client rendering | UI/E2E tests | Prove client obeys outcome and does not leak |
| Release/correction/rollback | release tests | Prove runtime reflects current governed state |
| Domain runtime integration | one accepted domain runtime-proof lane | Prove the end-to-end bounded composition |

### No-parallel-test-authority rule

Do not implement the same assertion independently in:

```text
tests/runtime_proof/domains/<domain>/
tests/domains/<domain>/runtime_proof/
tests/api/
tests/ui/
tests/e2e/
```

Instead:

- keep low-level assertions in their owning lanes;
- expose reusable fixtures/helpers through accepted test utilities;
- make runtime-proof integration tests call those surfaces;
- make UI/E2E tests verify client-visible behavior;
- retain one owner for each assertion and link dependents.

### Shared helper boundary

A helper is shared only when it is domain-neutral and reusable across at least two accepted children. Shared helpers should not live in a domain child. Their accepted test utility location remains **NEEDS VERIFICATION** and must follow Directory Rules before creation.

[Back to top](#top)

---

<a id="required-domain-runtime-proof-families"></a>

## Required domain runtime-proof families

Every mature child should cover the families below where material.

### 1. Envelope and versioning

- valid shared envelope;
- missing required field;
- unknown outcome;
- additional-property rejection;
- schema-version mismatch;
- stale or unsupported client version;
- `spec_hash` mismatch.

### 2. Domain payload

- valid domain payload;
- payload schema failure;
- semantic contract drift;
- envelope/payload identity mismatch;
- payload reference not found;
- shared-envelope field used as hidden payload storage.

### 3. Evidence and citation

- resolvable evidence for `ANSWER`;
- missing evidence produces `ABSTAIN`;
- stale evidence produces `ABSTAIN` or a bounded stale response;
- citation does not support the claim;
- source-role conflict blocks or narrows output;
- generated language cannot replace EvidenceBundle support.

### 4. Policy, rights, and sensitivity

- allow;
- allow with obligations;
- deny;
- unresolved rights;
- missing review;
- consent or purpose limitation where applicable;
- exact sensitive geometry or attributes;
- safe generalization/redaction plus receipt;
- reason-code side-channel leakage.

### 5. Lifecycle and release

- PUBLISHED/released current state;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or candidate state blocked from public current;
- missing release reference;
- withdrawn state;
- superseded state;
- correction pending;
- rollback affected;
- stale client cache.

### 6. Trust membrane

- no direct internal-store read;
- no direct source-system call;
- no direct model-runtime call;
- no admin shortcut on normal public path;
- no canonical database identifiers in response;
- no private endpoint or credential leakage;
- governed API is the normal client path.

### 7. Public surfaces

- API response;
- map feature and popup;
- Evidence Drawer;
- Focus Mode or governed AI;
- search;
- graph projection;
- screenshot and export;
- cached response;
- URL and browser history;
- generated summary.

### 8. Temporal behavior

- source time;
- observation/event time;
- valid time;
- retrieval time;
- processing time;
- release time;
- correction time;
- expiry and freshness;
- event-boundary behavior.

### 9. Negative-state integrity

- `ABSTAIN` with no claim;
- `DENY` with no restricted payload;
- `ERROR` with no internal detail;
- malformed request;
- dependency unavailable;
- policy runtime unavailable;
- evidence resolver unavailable;
- correction resolver unavailable;
- zero test collection.

### 10. Correction and rollback

- corrected evidence changes runtime posture;
- withdrawn release stops current delivery;
- superseded payload is not served as current;
- caches and search indexes invalidate;
- rollback restores known prior behavior;
- audit links preserve old and new identities.

A child may add stricter domain-specific families. It may not weaken these shared minimums.

[Back to top](#top)

---

<a id="fixture-and-test-data-contract"></a>

## Fixture and test-data contract

### Fixture homes

| Fixture class | Preferred home |
|---|---|
| Shared RuntimeResponseEnvelope shape fixtures | `fixtures/contracts/v1/runtime/runtime_response_envelope/` |
| Reusable domain fixtures | `fixtures/domains/<domain>/` after placement review |
| Unit-test-scoped examples | `tests/fixtures/` or child-local inline values when truly minimal |
| Invalid shared cases | paired shared `invalid/` fixture lane |
| UI/E2E-specific test carriers | accepted UI/E2E fixture lanes |

### Minimum domain fixture matrix

| Case | Expected outcome |
|---|---|
| supported released answer | `ANSWER` |
| missing evidence | `ABSTAIN` |
| stale/conflicted support | `ABSTAIN` or explicitly bounded stale posture |
| policy denial | `DENY` |
| rights/sensitivity denial | `DENY` |
| missing release | `DENY` |
| malformed request | `ERROR` |
| schema mismatch | `ERROR` |
| dependency failure | `ERROR` |
| corrected state | bounded current/corrected outcome |
| withdrawn state | `DENY` or safe unavailable posture |
| rollback state | restored known prior behavior |
| leakage canary | no protected value appears anywhere |
| zero-result/empty-domain case | finite non-invented outcome |

### Fixture requirements

Fixtures must be:

- synthetic or explicitly public-safe;
- deterministic;
- compact and reviewable;
- no-network by default;
- free of credentials, private endpoints, production prompts, and production logs;
- free of exact protected locations and private identities;
- explicit about expected system outcome and expected test result;
- linked to accepted contracts and schemas;
- versioned when shape changes;
- paired with negative cases;
- safe to retain in a public repository.

### Fixture anti-authority rule

A fixture demonstrates expected shape or behavior. It does not establish:

- source authority;
- real-world truth;
- evidence closure;
- policy correctness;
- current release state;
- public publication;
- production safety;
- legal or operational advice.

### Canary requirements

At least one canary should prove each major fail-closed mechanism is live:

- invalid outcome is rejected;
- missing evidence cannot answer;
- denied content does not leak;
- direct store access is blocked;
- unexpected network access fails;
- stale/withdrawn content is not served current;
- zero collected tests fail the gate.

[Back to top](#top)

---

<a id="network-rights-and-sensitivity-boundary"></a>

## Network, rights, and sensitivity boundary

### Default execution profile

Domain runtime proof is **hermetic by default**:

- no live source APIs;
- no external tile/style/glyph/CDN calls;
- no production governed API;
- no model provider;
- no private database;
- no cloud secret;
- no current operational feed;
- no mutable remote fixture.

A separately named external-smoke profile may be useful, but it must be optional, allowlisted, non-authoritative, and unable to substitute for hermetic proof.

### Sensitive-domain inheritance

A child inherits the most restrictive applicable posture from:

- its domain;
- the source;
- joined domains;
- living-person or private-party context;
- cultural or sovereignty review;
- exact-location risk;
- infrastructure exposure;
- licensing and rights;
- release state.

This parent does not define sensitivity thresholds or generalization distances.

### Leakage surfaces

Tests should inspect:

- response body;
- headers;
- reason codes;
- error metadata;
- stack traces;
- logs;
- URLs;
- cache keys;
- map feature properties;
- tiles and style JSON;
- search indexes;
- graph projections;
- exports and screenshots;
- Evidence Drawer payloads;
- Focus Mode or AI text.

### Fail-safe rule

When rights, sensitivity, evidence, release, or correction posture cannot be resolved safely, the expected public runtime result is a bounded `ABSTAIN`, `DENY`, or `ERROR`—never a guessed `ANSWER`.

[Back to top](#top)

---

<a id="ci-and-gate-acceptance"></a>

## CI and gate acceptance

### Current CI boundary

Current evidence shows:

- `make test` collects only `tests/schemas` and `tests/contracts`;
- `validator-suite` runs schema validation and one evidence-bundle fail-closed check;
- no dedicated runtime-proof workflow was surfaced;
- the Roads–Rail–Trade domain workflow is echo-only;
- README and link checks may run, but they do not execute domain runtime proof.

Therefore:

```text
README exists                         != executable proof
workflow exists                       != tests collected
echo job succeeds                     != runtime behavior proven
shared schema fixture passes          != domain route works
domain workflow is green              != domain runtime proof is green
all runtime-proof tests pass          != release approval
```

### Required future gate behavior

An accepted domain runtime-proof gate should:

1. trigger on the accepted child path;
2. also trigger on shared runtime contracts, schemas, validators, and fixtures;
3. trigger on relevant domain contracts, schemas, policy, API/runtime, release, and fixture paths;
4. install from pinned dependency metadata;
5. run with external network disabled;
6. collect at least one positive and one negative test per required material family;
7. fail when zero tests are collected;
8. validate the shared envelope and domain payload separately;
9. exercise `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
10. verify no-leak behavior;
11. verify correction, withdrawal, cache invalidation, and rollback;
12. emit bounded QA artifacts;
13. preserve the primary failure when diagnostics are collected;
14. report exact child, fixture, schema, contract, and runtime versions;
15. remain separate from release approval.

### Trigger behavior during migration

Until placement is resolved, a future workflow that must cover both existing children may watch both confirmed paths. That temporary dual watch must be documented as migration support, not evidence that both paths are canonical.

### CI evidence hierarchy

```text
README present
  < test file present
  < test collected locally
  < workflow triggered
  < expected tests collected in CI
  < negative canaries fail correctly
  < repeated stable runs
  < correction and rollback proven
  < accepted promotion-gate integration
```

Never claim a higher maturity from a lower signal.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

### Required reviewers

A placement or child-status change should involve:

- QA/test steward;
- runtime-proof steward;
- affected domain steward;
- governed API steward;
- evidence/citation steward;
- policy steward;
- rights/sensitivity reviewer when applicable;
- release/correction/rollback steward;
- CI steward;
- docs steward.

### Higher-burden changes

Require explicit architecture or governance review when a change:

- selects the canonical executable placement;
- moves or deletes an existing child;
- creates a machine registry;
- changes the finite outcome vocabulary;
- weakens shared envelope requirements;
- changes fixture authority;
- permits network access in a required profile;
- changes sensitive-data posture;
- makes runtime proof a promotion requirement;
- alters correction or rollback semantics.

### Reviewer questions

1. Is there exactly one executable child for the domain?
2. Does the child compose shared proof instead of copying it?
3. Does `ANSWER` require evidence, policy, and release support?
4. Are `ABSTAIN`, `DENY`, and `ERROR` tested as first-class outcomes?
5. Can any response, log, cache, map, export, or AI surface leak protected content?
6. Does CI collect the intended tests and fail on zero collection?
7. Is correction and rollback observable?
8. Is the path decision supported by Directory Rules or an ADR?

[Back to top](#top)

---

<a id="placement-resolution-and-migration"></a>

## Placement resolution and migration

### Decision required

The final convention must select one executable placement:

```text
A. tests/runtime_proof/domains/<domain>/
B. tests/domains/<domain>/runtime_proof/
```

The decision should state:

- which path is executable authority;
- whether the other path remains a human compatibility index;
- where shared runtime-proof helpers live;
- how domain owners are assigned;
- how workflows discover children;
- how fixtures are referenced;
- how history and links are preserved;
- how rollback works.

### Decision criteria

| Criterion | Capability-first | Domain-first |
|---|---:|---:|
| Shared finite-outcome visibility | Strong | Requires parent aggregation |
| Domain ownership visibility | Requires cross-links | Strong |
| Avoiding duplicate domain fixtures | Moderate risk | Stronger |
| Shared harness reuse | Strong | Requires shared helper imports |
| Domain package navigation | Weaker | Strong |
| Cross-domain consistency review | Strong | Requires registry/index |
| Migration cost from current state | Roads child already present | Flora lane already present |

This README does not choose a winner.

### Eight-phase migration

#### Phase 1 — Freeze and inventory

- freeze new children;
- enumerate both patterns recursively;
- inventory executable files, fixtures, helpers, workflows, and inbound references;
- identify duplicate assertions and divergent semantics.

#### Phase 2 — Decide placement

- issue Directory Rules clarification or accept an ADR;
- name the canonical executable path;
- define compatibility-index behavior;
- assign owners.

#### Phase 3 — Define shared contracts

- confirm RuntimeResponseEnvelope version;
- confirm domain payload composition;
- confirm state and reason-code vocabularies;
- confirm fixture and validator homes.

#### Phase 4 — Select implementation per domain

- identify the stronger existing lane;
- merge unique coverage into the selected lane;
- do not copy files blindly;
- preserve commit history where practical.

#### Phase 5 — Wire CI

- update workflow paths and commands atomically;
- fail on zero tests;
- run hermetic and negative canaries;
- record exact versions and artifacts.

#### Phase 6 — Add compatibility index

- replace the losing executable path with a small redirect/index;
- remove duplicate tests and fixtures;
- preserve migration and rollback references;
- update parent and root READMEs.

#### Phase 7 — Verify consumers

- update docs, workflows, CODEOWNERS, scripts, test commands, dashboards, and release gates;
- verify no inbound reference still treats the old path as executable;
- verify correction and rollback documentation.

#### Phase 8 — Deprecate and retire

- announce a deprecation window;
- retain compatibility until consumers are migrated;
- retire only after inbound references and CI usage are zero;
- preserve history through normal commits.

### Migration stop conditions

Stop and require review if:

- two paths would contain executable tests for the same domain;
- unique coverage cannot be mapped safely;
- fixture authority is unclear;
- the shared envelope or domain payload is unresolved;
- workflow collection cannot be proven;
- sensitive fixtures might move into a less controlled lane;
- correction or rollback references would break;
- a proposed deletion lacks an inbound-reference inventory.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Documentation checks

The README should pass:

- one rendered H1;
- no heading-level jumps;
- balanced fenced blocks;
- unique rendered headings;
- valid internal navigation anchors;
- no trailing whitespace or tabs;
- no secret-like or private-key material;
- correct relative links for confirmed paths.

### Repository inspection commands

These commands are verification aids, not claims that they were run in this update:

```bash
find tests/runtime_proof/domains -maxdepth 4 -type f -print | sort
find tests/domains -path '*/runtime_proof/*' -type f -print | sort
git grep -n 'tests/runtime_proof/domains'
git grep -n 'tests/domains/.*/runtime_proof'
git grep -n 'pytest tests/runtime_proof'
git grep -n 'runtime_proof' .github/workflows Makefile pyproject.toml
```

### Shared envelope validation

```bash
python tools/validators/validate_runtime_response_envelope.py \
  fixtures/contracts/v1/runtime/runtime_response_envelope/valid/valid_1.json
```

A shape pass is not domain runtime proof.

### Future child execution

After placement and executable tests are accepted:

```bash
python -m pytest -q <accepted-domain-runtime-proof-path>
```

The command must fail if no tests are collected.

### Required validation record

A child promotion record should capture:

- commit SHA;
- child path;
- test count;
- outcome-family coverage;
- fixture digests;
- shared envelope version and hash;
- domain contract/schema versions;
- policy and release fixture versions;
- network profile;
- runtime/API version;
- correction/rollback scenario results;
- known limitations.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This parent is mature when:

- [ ] Directory Rules or an ADR selects one executable placement.
- [ ] The alternate placement is explicitly a compatibility index or retired.
- [ ] A complete child inventory is verified.
- [ ] Every indexed child has one finite registration status.
- [ ] No domain has executable tests in both patterns.
- [ ] Shared RuntimeResponseEnvelope version and validator are accepted.
- [ ] Domain payload composition rules are accepted.
- [ ] Shared reason/state vocabularies are accepted or explicitly versioned.
- [ ] Positive, invalid, `ABSTAIN`, `DENY`, `ERROR`, correction, and rollback fixtures exist.
- [ ] Required CI collects non-zero tests for every `EXECUTABLE_WIRED` child.
- [ ] Required tests are hermetic.
- [ ] Leakage canaries cover response, log, cache, map, export, search, and AI surfaces where material.
- [ ] Correction, withdrawal, supersession, cache invalidation, and rollback are tested.
- [ ] Parent, child, root-test, workflow, CODEOWNERS, and runbook links agree.
- [ ] Documentation does not overstate production behavior.
- [ ] A transparent rollback target exists for the placement migration.

Until then, this parent remains `INDEX_ONLY / CONFLICTED / NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="correction-and-rollback"></a>

## Correction and rollback

### Documentation correction

When this index is wrong:

1. identify the incorrect child, path, status, or implementation claim;
2. inspect current repository evidence;
3. narrow the claim;
4. update the child README and this parent together when needed;
5. record the correction in normal commit history;
6. do not rewrite shared history.

### Child implementation correction

When a child test or fixture is wrong:

1. hold reliance on the affected proof;
2. identify domains, routes, releases, and clients affected;
3. preserve the failing fixture and diagnostics;
4. correct the owning test/fixture/contract/schema/policy surface;
5. add a regression case;
6. rerun shared and domain proof;
7. invalidate stale QA artifacts and dashboards;
8. record remaining uncertainty.

### Placement rollback

A placement migration must name a rollback target that restores:

- prior executable path;
- prior workflow commands and filters;
- prior fixture references;
- prior CODEOWNERS;
- prior parent/child links;
- prior dashboards or required checks.

Rollback must be a normal revert or follow-up commit. Do not reset or force-rewrite shared history.

### Safety rollback triggers

Rollback or hold is required if a change:

- creates duplicate executable authority;
- causes zero tests to appear green;
- weakens finite outcomes;
- allows a claim on `ABSTAIN`, `DENY`, or `ERROR`;
- bypasses evidence, policy, release, or correction gates;
- exposes sensitive detail;
- enables unexpected network access;
- breaks correction or rollback propagation;
- makes an old path silently stop running.

### Current README rollback

Before merge, leave the review unmerged or restore prior blob:

```text
0264e3a335a13dee0fc7aa6accd20b0c87af0cfd
```

After merge, revert the implementation commit or pull request through normal Git history.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

### Placement and inventory

- [ ] Recursively inventory both placement patterns.
- [ ] Confirm whether any unindexed runtime-proof children exist.
- [ ] Resolve capability-first versus domain-first placement.
- [ ] Decide whether this parent remains an index after migration.
- [ ] Confirm CODEOWNERS and reviewer assignments.
- [ ] Identify every inbound link and workflow consumer.

### Shared runtime contract

- [ ] Confirm RuntimeResponseEnvelope acceptance status and version.
- [ ] Confirm EvidenceRef resolution behavior.
- [ ] Define controlled vocabularies for policy, freshness, and correction state.
- [ ] Define safe reason-code registry and leakage constraints.
- [ ] Define domain payload composition.
- [ ] Add broader positive and negative shared fixtures.

### Child implementation

- [ ] Verify Roads–Rail–Trade executable inventory.
- [ ] Verify Flora executable inventory.
- [ ] Decide migration winner for each confirmed lane.
- [ ] Add domain-specific payload, evidence, policy, release, and client tests.
- [ ] Add correction, withdrawal, cache, and rollback tests.
- [ ] Add no-network and leakage canaries.

### CI

- [ ] Create or identify a dedicated runtime-proof workflow.
- [ ] Add accepted child discovery.
- [ ] Add shared contract/schema/validator triggers.
- [ ] Fail on zero tests.
- [ ] Record test counts and outcome-family coverage.
- [ ] Separate hermetic and external-smoke profiles.
- [ ] Verify current pass/fail state from logs.
- [ ] Decide whether runtime proof becomes a required promotion check.

### Governance and release

- [ ] Confirm child status registry strategy.
- [ ] Confirm correction and deprecation procedure.
- [ ] Confirm migration compatibility window.
- [ ] Verify release/correction/rollback consumers.
- [ ] Verify public-client behavior independently from fixture proof.
- [ ] Record a tested placement rollback.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | CONFIRMED | Existing parent intent and prior blob | Narrow, aspirational, and unaware of alternate placement |
| `tests/README.md` | CONFIRMED | `tests/` authority, separate runtime-proof and domain lanes, trust-spine classes | Does not resolve their intersection |
| `tests/runtime_proof/README.md` | CONFIRMED draft | Capability-first domain-child model and finite-outcome rules | Executable depth and CI unverified |
| Merged Roads–Rail–Trade child README | CONFIRMED v0.2 | One direct child, detailed proof contract, README-only status, workflow gap | Domain route/schema/tests remain unimplemented in bounded evidence |
| Flora domain-first runtime-proof README | CONFIRMED v0.1 | Alternate executable placement and domain-first rationale | Scaffold; tests/routes/CI unverified |
| Shared RuntimeResponseEnvelope contract | CONFIRMED paired / PROPOSED | Semantic boundary and required field intent | Not route, payload, evidence, policy, or release proof |
| Shared RuntimeResponseEnvelope schema | CONFIRMED concrete / PROPOSED | Required fields, four outcomes, closed object | State vocabularies and domain payload are not defined |
| Shared validator wrapper | CONFIRMED executable wrapper | Shared JSON Schema invocation | Does not prove runtime composition |
| Shared fixture READMEs | CONFIRMED minimal | One valid `ABSTAIN` shape and one missing-`id` invalid case | Not domain runtime proof |
| Root Makefile | CONFIRMED | `make test` excludes runtime-proof paths | Does not prove other ad hoc commands are absent |
| `validator-suite` workflow | CONFIRMED | Schema-oriented CI scope | Not domain runtime-proof CI |
| Bounded workflow search | No dedicated runtime-proof workflow surfaced | Supports CI uncertainty | Search-limited; recursive workflow inventory remains required |
| Directory Rules | CONFIRMED doctrine | Responsibility-root placement and no-parallel-authority posture | Does not choose between the two nested test conventions |
| Current-session execution | NOT RUN | Documentation-only repository update | No test, route, validator, workflow, or production pass claim |

[Back to top](#top)
