<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-runtime-proof-readme
title: tests/runtime_proof/ — Governed Runtime Proof Root, Finite-Outcome Contract, and Placement Guardrail
type: readme; directory-readme; runtime-proof-root; finite-outcome-test-contract; trust-membrane-proof-index; migration-guardrail
version: v0.2
status: draft; canonical-runtime-proof-root; shared-envelope-schema-present; governed-api-stub-tested; domain-placement-conflicted; policy-runtime-stub; envelope-package-scaffold; no-dedicated-runtime-proof-ci; proof-not-closed; NEEDS VERIFICATION
policy_label: public-doc; restricted-review-when-sensitive-domain-or-private-runtime-state-is-in-scope
owners: OWNER_TBD — QA steward · Runtime-proof steward · Governed API steward · Runtime steward · Domain architecture steward · Evidence steward · Policy steward · Rights/sensitivity reviewer · Release steward · UI/E2E steward · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
current_path: tests/runtime_proof/README.md
truth_posture: CONFIRMED target README and prior blob, tests responsibility root, merged domain-placement index, Roads–Rail–Trade capability-first child, Flora domain-first alternate lane, RuntimeResponseEnvelope contract/schema/validator/minimal fixtures, DecisionEnvelope schema, governed-api WSGI scaffold, three registered GET routes, deterministic ABSTAIN stub, governed-api abstain and boundary tests, runtime/envelopes canonical handoff lane, packages/envelopes 0.0.0 scaffold, policy/runtime stub, root Makefile test scope, api-test workflow, validator-suite workflow, and bounded absence of a dedicated runtime-proof workflow at the pinned snapshot / PROPOSED accepted envelope profile, domain child placement winner, shared reason/state vocabularies, domain payload contracts, evidence resolution, policy execution, receipt persistence, runtime-proof fixture matrix, dedicated CI gate, correction propagation, cache invalidation, and promotion integration / CONFLICTED RuntimeResponseEnvelope versus DecisionEnvelope-shaped governed-api scaffold, contract/schema/architecture profile drift, tests/runtime_proof/domains/<domain> versus tests/domains/<domain>/runtime_proof placement, schema-shape success versus runtime-proof claims, and green generic/domain workflows versus actual runtime-proof collection / UNKNOWN exhaustive executable inventory, current pass state, production routes, runtime consumers, deployed policy/evidence/release behavior, public-client conformance, and operational health / NEEDS VERIFICATION owners, accepted ADR/profile decisions, recursive inventory, runtime-proof test collection, route coverage, fixture coverage, policy and evidence bindings, release/correction/rollback integration, and required-check status
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2ab8e92cfc76f19838de5be5e3d138d33d980bd7
  prior_blob: 3e33777d72a5fa346b82c948f9c1837d23675fc5
related:
  - ../README.md
  - ./domains/README.md
  - ./domains/roads-rail-trade/README.md
  - ../domains/flora/runtime_proof/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../tools/validators/validate_runtime_response_envelope.py
  - ../../tools/validators/validate_decision_envelope.py
  - ../../fixtures/contracts/v1/runtime/runtime_response_envelope/
  - ../../fixtures/contracts/v1/runtime/decision_envelope/
  - ../../tests/schemas/test_common_contracts.py
  - ../../runtime/envelopes/README.md
  - ../../packages/envelopes/README.md
  - ../../policy/runtime/README.md
  - ../../apps/governed-api/src/governed_api/main.py
  - ../../apps/governed-api/src/governed_api/stub.py
  - ../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../apps/governed-api/tests/test_abstain_routes.py
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../Makefile
  - ../../.github/workflows/api-test.yml
  - ../../.github/workflows/validator-suite.yml
tags: [kfm, tests, runtime-proof, governed-api, trust-membrane, finite-outcomes, answer, abstain, deny, error, runtime-response-envelope, decision-envelope, evidence, policy, freshness, correction, release, receipts, no-network, domain-placement, migration, rollback, no-parallel-authority]
notes:
  - "v0.2 replaces a planning-oriented root README with a repository-grounded runtime-proof contract and explicit implementation boundary."
  - "The governed API currently exposes three deterministic scaffold routes that return ABSTAIN and are tested against a DecisionEnvelope subset; this is useful proof of bounded scaffold behavior, not proof of the full RuntimeResponseEnvelope profile."
  - "Domain runtime-proof placement is conflicted and frozen for new children by the merged domains index."
  - "Root make test and validator-suite do not collect tests/runtime_proof; api-test exercises governed-api scaffold tests but is not a dedicated runtime-proof gate."
  - "This revision changes documentation only and creates, moves, deletes, or activates no test, fixture, route, schema, validator, workflow, package, policy, data, receipt, proof, or release record."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/runtime_proof/` — Governed Runtime Proof Root, Finite-Outcome Contract, and Placement Guardrail

> **Purpose.** Define and index the executable proof required before KFM may describe a governed runtime surface as finite-outcome, evidence-aware, policy-aware, release-aware, correction-aware, rollback-capable, and safe for a public or restricted client.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Role: runtime proof root" src="https://img.shields.io/badge/role-runtime__proof__root-purple">
  <img alt="Implementation: partial scaffold" src="https://img.shields.io/badge/implementation-partial__scaffold-orange">
  <img alt="Domain placement: conflicted" src="https://img.shields.io/badge/domain__placement-CONFLICTED-red">
  <img alt="CI: no dedicated gate" src="https://img.shields.io/badge/CI-NO__DEDICATED__GATE-lightgrey">
</p>

> [!IMPORTANT]
> `tests/runtime_proof/` is an **enforceability-proof root**. It is not runtime implementation, a governed API, a domain package, a schema or contract home, policy execution, evidence storage, receipt or proof storage, release approval, publication authority, or public truth.

> [!WARNING]
> Current repository evidence does **not** support calling runtime proof closed or promotion-ready. Shared envelope schemas, validators, minimal fixtures, governed-api scaffold tests, and boundary tests exist. However, the envelope profile is conflicted, `policy/runtime/` is a stub, domain placement is unresolved, `make test` excludes this root, and no dedicated runtime-proof workflow was surfaced.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Placement](#placement-and-authority) · [Inventory](#confirmed-repository-inventory) · [Proof model](#runtime-proof-responsibility-model) · [Profiles](#envelope-profile-and-scaffold-conflict) · [Outcomes](#finite-outcome-discipline) · [Trust membrane](#trust-membrane-invariants) · [Coverage](#required-runtime-proof-families) · [Domains](#domain-runtime-proof-placement) · [Fixtures](#fixture-and-test-data-contract) · [Network](#network-security-rights-and-sensitivity) · [CI](#ci-and-gate-acceptance) · [Authoring](#test-authoring-contract) · [Validation](#validation) · [Done](#definition-of-done) · [Migration](#smallest-sound-implementation-sequence) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/runtime_proof/README.md` | **CONFIRMED** | Root README exists; prior blob is pinned in metadata. |
| Direct executable files under `tests/runtime_proof/` | **NOT SURFACED in bounded search** | Treat the root as coordination/documentation until recursive inventory proves otherwise. |
| `tests/runtime_proof/domains/README.md` | **CONFIRMED merged v0.2** | Human routing/migration index; `INDEX_ONLY`, placement-conflicted, and frozen for new children. |
| `tests/runtime_proof/domains/roads-rail-trade/` | **CONFIRMED capability-first child** | README-only in bounded evidence; route/schema/tests/CI not closed. |
| `tests/domains/flora/runtime_proof/` | **CONFIRMED domain-first alternate** | Scaffold README; executable tests, routes, fixtures, validators, and CI remain unverified. |
| Shared `RuntimeResponseEnvelope` contract/schema | **CONFIRMED paired / status PROPOSED** | Closed shape with ten required fields and four finite outcomes. |
| Shared `DecisionEnvelope` schema | **CONFIRMED concrete / status PROPOSED** | Closed policy-style envelope with finite outcomes and required decision fields. |
| Runtime envelope validator wrappers | **CONFIRMED executable entry points** | Validate JSON Schema fixtures; do not prove runtime composition. |
| Runtime envelope fixtures | **CONFIRMED minimal** | One valid and one invalid example for the shared families; coverage is schema-only. |
| Generic schema harness | **CONFIRMED executable test code** | Discovers runtime schemas with matching fixture directories. |
| Governed API application | **CONFIRMED WSGI scaffold** | Routes registered through a local in-process application; not production deployment proof. |
| Governed API route registry | **CONFIRMED three routes** | `/bootstrap`, `/layers`, and `/evidence`. |
| Governed API route behavior | **CONFIRMED deterministic scaffold** | Registered GET routes emit `ABSTAIN` with `NOT_IMPLEMENTED`. |
| Governed API abstain tests | **CONFIRMED executable pytest module** | Exercises all registered routes and validates a DecisionEnvelope subset. |
| Governed API boundary tests | **CONFIRMED executable pytest module** | Covers 404, 405, forbidden imports, route manifest, and internal-store path literals. |
| `runtime/envelopes/` | **CONFIRMED canonical runtime handoff lane** | Coordinates runtime envelope profiles and wiring; not reusable implementation. |
| `packages/envelopes/` | **CONFIRMED `0.0.0` scaffold** | Empty initializer; no supported helper API or production consumer established. |
| `policy/runtime/` | **CONFIRMED stub** | No verified executable runtime policy bundle. |
| Root `make test` | **CONFIRMED narrow** | Runs `tests/schemas` and `tests/contracts`; excludes this root. |
| `api-test` workflow | **CONFIRMED substantive scaffold/API check** | Runs governed-api tests and the abstain-route test; not a full runtime-proof matrix. |
| `validator-suite` workflow | **CONFIRMED schema-oriented** | Runs schema validators and an EvidenceBundle fail-closed canary; not runtime proof. |
| Dedicated runtime-proof workflow | **NOT SURFACED in bounded search** | Do not claim this root is a required CI gate. |
| Production runtime behavior | **UNKNOWN** | Repository scaffolds and tests do not prove deployed behavior or operational health. |

**Authority of this README:** root routing, proof taxonomy, finite-outcome semantics, cross-lane composition, minimum fixture/test coverage, CI acceptance criteria, migration discipline, correction guidance, and rollback guidance.

The following outrank this README for their responsibilities:

- accepted Directory Rules and ADRs;
- semantic contracts and machine schemas;
- executable policy bundles and decisions;
- evidence, citations, receipts, proofs, and release records;
- runtime, package, and governed API implementation;
- executable tests, validators, workflows, and logs;
- correction, withdrawal, supersession, and rollback records;
- steward decisions.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from repository files, schema shape, tests, workflows, or commit history. |
| **PROPOSED** | A design, profile, registry, test, fixture, route, or procedure not yet accepted or implemented. |
| **CONFLICTED** | Repository surfaces disagree or create competing executable homes or object profiles. |
| **NEEDS VERIFICATION** | Checkable, but not sufficiently proven for reliance or promotion. |
| **UNKNOWN** | Not established by the inspected evidence. |

[Back to top](#top)

---

<a id="purpose-and-scope"></a>

## Purpose and scope

This root answers seven governance questions:

1. Which runtime-proof surfaces actually exist?
2. Which envelope profile is a test asserting?
3. What does each finite outcome mean?
4. Which lower-level proofs must compose before a runtime assertion is credible?
5. Which responsibilities remain outside `tests/runtime_proof/`?
6. Which tests and workflows actually collect this lane?
7. How can KFM correct, migrate, deprecate, or roll back runtime-proof behavior without losing evidence?

### In scope

- shared governed-runtime outcome and trust-membrane proof;
- envelope-profile conformance and drift detection;
- evidence-resolution and cite-or-abstain behavior;
- policy, rights, sensitivity, access, consent, and capability outcomes;
- freshness, correction, withdrawal, supersession, and rollback posture;
- public-client and restricted-client rendering permissions;
- governed API, Evidence Drawer, Focus Mode, AI, export, map, search, and cache boundary proof;
- domain runtime-proof registration and composition;
- deterministic, synthetic, no-network fixture expectations;
- CI collection, test-count, outcome-family, and negative-canary requirements;
- migration, compatibility, correction, and rollback guidance.

### Out of scope

- runtime or API implementation;
- reusable envelope package implementation;
- contracts, schemas, policy definitions, or reason-code authority;
- source registries, canonical lifecycle data, evidence, receipts, or proofs;
- release decisions or publication;
- production logs, credentials, private endpoints, or sensitive source material;
- direct model output treated as evidence;
- resolving architecture conflicts by README assertion.

[Back to top](#top)

---

<a id="placement-and-authority"></a>

## Placement and authority

### Directory Rules basis

KFM places files by primary responsibility:

```text
tests/runtime_proof/                      shared governed-runtime proof root
tests/runtime_proof/domains/              conflicted domain-child index and migration guardrail
tests/domains/<domain>/runtime_proof/     alternate domain-first runtime-proof placement
tests/api/                                route and protocol behavior
apps/governed-api/tests/                  application-owned trust-membrane tests
tests/ui/ and tests/e2e/                   client rendering and end-to-end proof
tests/schemas/ and tests/contracts/        shape and meaning proof
tests/policy/                              policy and boundary proof
fixtures/ and tests/fixtures/              synthetic examples
runtime/envelopes/                         runtime handoff and profile coordination
packages/envelopes/                        reusable helper implementation
contracts/runtime/                         semantic meaning
schemas/contracts/v1/runtime/              machine-checkable shape
policy/runtime/                            runtime admissibility and obligations
apps/governed-api/                         public/semi-public trust membrane
data/receipts/ and data/proofs/            emitted audit/proof records
release/                                   release, correction, withdrawal, rollback authority
```

The root `tests/runtime_proof/` is a valid shared capability lane under the canonical `tests/` responsibility root. The conflict is narrower: **where domain-specific runtime proof belongs**.

### Root class

| Field | Value |
|---|---|
| Primary responsibility | Shared governed-runtime enforceability proof |
| Root status | `CURRENT / DRAFT` |
| Executable depth | Partial across shared schema and governed-api application tests |
| Domain-child status | `PLACEMENT_CONFLICTED` |
| Schema authority | None |
| Contract authority | None |
| Policy authority | None |
| Runtime/API authority | None |
| Release authority | None |
| New shared tests | Allowed after profile and ownership review |
| New domain child lanes | Frozen until placement resolution |
| Required reviewers | QA, runtime proof, API/runtime, evidence, policy, rights/sensitivity, release, UI/E2E, CI, docs |

### No-parallel-authority rule

Do not create a second implementation of:

- an envelope schema;
- an envelope builder;
- evidence resolution;
- policy evaluation;
- release evaluation;
- reason-code registries;
- receipt persistence;
- domain fixtures;
- API route behavior;
- UI rendering rules.

Runtime-proof tests must call or validate owning implementations. They may use test doubles only when the substitution is explicit, deterministic, and subordinate to the owning contract.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Root and domain lanes

```text
tests/runtime_proof/
├── README.md
└── domains/
    ├── README.md
    └── roads-rail-trade/
        └── README.md

tests/domains/flora/
└── runtime_proof/
    └── README.md
```

Bounded evidence did not establish direct executable modules in these README lanes.

### Shared envelope surfaces

```text
contracts/runtime/
├── decision_envelope.md
└── runtime_response_envelope.md

schemas/contracts/v1/runtime/
├── decision_envelope.schema.json
└── runtime_response_envelope.schema.json

tools/validators/
├── validate_decision_envelope.py
└── validate_runtime_response_envelope.py

fixtures/contracts/v1/runtime/
├── decision_envelope/
└── runtime_response_envelope/
```

### Governed API scaffold inventory

```text
apps/governed-api/
├── src/governed_api/
│   ├── main.py
│   ├── stub.py
│   └── routes/
│       ├── registry.py
│       ├── bootstrap.py
│       ├── layers.py
│       └── evidence.py
└── tests/
    ├── test_abstain_routes.py
    └── test_boundary_guards.py
```

The registry contains:

```text
/bootstrap
/layers
/evidence
```

All three registered GET routes currently return a deterministic `ABSTAIN` scaffold.

### Runtime and package lanes

```text
runtime/envelopes/       canonical runtime wiring and handoff coordination
packages/envelopes/      reusable Python package scaffold, version 0.0.0
policy/runtime/          greenfield bundle stub
```

### Current proof chain

```text
shared JSON Schema + minimal fixtures
  -> common schema harness / validator wrappers
  -> governed-api stub builder
  -> WSGI route registry
  -> abstain-route and boundary tests
  -> api-test workflow
```

This chain proves bounded scaffold behavior. It does not prove policy execution, evidence resolution, release admission, correction propagation, receipt persistence, domain payloads, or public production behavior.

[Back to top](#top)

---

<a id="runtime-proof-responsibility-model"></a>

## Runtime-proof responsibility model

### Proof layers

| Layer | What it should prove | Current surfaced evidence |
|---|---|---|
| Contract | Meaning of envelope and outcomes | Draft paired contracts |
| Schema | Machine shape and finite enum | Concrete closed schemas, status PROPOSED |
| Fixture | Valid and invalid example shapes | Minimal one-valid/one-invalid coverage |
| Validator | Shape validation and stable failures | Thin wrappers over common JSON Schema runner |
| Shared runtime | Profile selection and handoff | Documentation lane; executable helpers unknown |
| Package | Reusable deterministic helpers | `0.0.0` scaffold; empty initializer |
| Policy | Allow/deny/restrict/abstain obligations | Runtime policy stub |
| Governed API | Trust-membrane serialization and route behavior | Three ABSTAIN scaffold routes |
| API tests | HTTP/WSGI and envelope behavior | Abstain and boundary tests |
| Runtime-proof root | Cross-cutting evidence/policy/release/client proof | No dedicated executable suite surfaced |
| Domain runtime proof | Domain-specific composition | Placement conflicted; README scaffolds |
| UI/E2E | Client rendering and leakage behavior | Separate test roots; not established here |
| Release/rollback | Published-state and correction behavior | Separate authority; integration unverified |

### Composition rule

A runtime-proof assertion is credible only when the required lower-level proofs are present.

```text
schema shape
  + semantic contract
  + evidence resolution
  + policy decision
  + freshness/correction state
  + release state
  + safe serialization
  + client obligation handling
  + negative leakage checks
  = runtime proof candidate
```

A pass at one layer must not be reported as closure of the entire chain.

### Proof versus authority

```text
schema-valid envelope       != evidence closure
ABSTAIN scaffold route      != accepted runtime implementation
API test pass               != policy execution proof
domain README               != executable domain test
green workflow              != runtime-proof collection
runtime-proof pass          != release approval
receipt-shaped output       != accepted receipt
release reference           != release decision
```

[Back to top](#top)

---

<a id="envelope-profile-and-scaffold-conflict"></a>

## Envelope profile and scaffold conflict

The repository currently exposes two related closed schemas and a governed-api scaffold that combines fields.

### `RuntimeResponseEnvelope`

Required schema fields:

| Field | Required |
|---|---:|
| `id` | yes |
| `spec_hash` | yes |
| `version` | yes |
| `issued_at` | yes |
| `outcome` | yes |
| `reason_code` | yes |
| `evidence_refs` | yes |
| `policy_state` | yes |
| `freshness` | yes |
| `correction_state` | yes |

The finite outcome enum is:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

Additional properties are forbidden.

### `DecisionEnvelope`

Required schema fields:

| Field | Required |
|---|---:|
| `decision_id` | yes |
| `outcome` | yes |
| `policy_family` | yes |
| `reasons` | yes |
| `obligations` | yes |
| `evaluated_at` | yes |

The schema also permits optional compatibility/scaffold fields such as `id`, `decision`, `reason_code`, `evidence_refs`, `spec_hash`, `version`, and `issued_at`.

### Current governed-api stub

The scaffold emits:

```text
id
decision_id
spec_hash
version
issued_at
evaluated_at
decision
outcome
policy_family
reason_code
reasons
obligations
evidence_refs
```

It does **not** emit the required `RuntimeResponseEnvelope` fields:

```text
policy_state
freshness
correction_state
```

The current abstain-route test therefore validates the payload against a **DecisionEnvelope subset**, not the full `RuntimeResponseEnvelope` schema.

### Safe interpretation

- The scaffold demonstrates deterministic finite `ABSTAIN` behavior.
- The API test demonstrates that every registered route returns the expected stub and matches the selected DecisionEnvelope subset.
- It does not prove the RuntimeResponseEnvelope profile.
- It does not authorize a hybrid schema.
- It does not resolve the contract/schema/architecture conflict.
- It does not establish production serialization.

### Required profile rule

Every runtime-proof test must name:

- the contract profile;
- schema `$id` or file;
- version;
- payload contract, if separate;
- policy/reason/state vocabularies;
- compatibility adapter, if any;
- expected client obligations.

Tests must fail when a response silently mixes fields from incompatible profiles.

[Back to top](#top)

---

<a id="finite-outcome-discipline"></a>

## Finite-outcome discipline

### Runtime outcomes

| Outcome | Runtime meaning | Required proof emphasis |
|---|---|---|
| `ANSWER` | A bounded response may be presented under current evidence, policy, rights, sensitivity, freshness, correction, and release constraints. | Evidence resolves; citations and payload validate; policy allows; release applies; obligations are honored. |
| `ABSTAIN` | A cited, policy-passed answer cannot responsibly be produced for the requested scope. | No claim leakage; stable reason; unresolved handles preserved; narrowing or next step is safe. |
| `DENY` | Policy, rights, sensitivity, access, consent, capability, review, or release posture forbids delivery. | Restricted payload absent; safe reason; no side-channel leakage; obligations do not become disclosure. |
| `ERROR` | The governed machinery cannot complete safely or deterministically. | Bounded diagnostic; no claim fallback; no internal paths, credentials, raw evidence, or protected detail. |

`ABSTAIN` is doctrine-aligned but ADR-0020 remains **proposed**. Tests should preserve the four-value schema enum while keeping ADR acceptance status visible.

### Test results

| Result | Meaning |
|---|---|
| pass | Observed behavior matches the expected runtime outcome and leakage posture. |
| fail | Behavior violates the test contract. |
| skip | A condition was unavailable; not proof of success. |
| expected failure | Tracked known defect with reason and expiry. |
| infrastructure error | The suite could not evaluate behavior; not product success. |
| zero tests collected | Configuration failure for a required suite. |

A test expecting `DENY`, `ABSTAIN`, or `ERROR` passes only when that negative outcome is emitted safely and without leakage.

### Forbidden outcome collapse

Tests must reject:

- `ABSTAIN` represented as blank `200 OK`;
- policy denial represented as `ABSTAIN`;
- infrastructure failure represented as `ABSTAIN`;
- missing evidence represented as `ANSWER`;
- low-confidence or partial output used as a fifth outcome;
- unknown enum values such as `PENDING`, `PARTIAL`, or `UNKNOWN`;
- UI loading state used as a runtime outcome;
- hidden warning text used instead of a finite outcome.

[Back to top](#top)

---

<a id="trust-membrane-invariants"></a>

## Trust-membrane invariants

Runtime proof must enforce these invariants:

1. Public and ordinary restricted clients use governed interfaces.
2. No public path reads RAW, WORK, QUARANTINE, unpublished candidate, canonical, or internal stores directly.
3. No browser or ordinary UI calls a model runtime or source system directly.
4. EvidenceRef must resolve through governed evidence interfaces or the result abstains.
5. Generated language, map features, graph edges, tiles, screenshots, search results, caches, and embeddings are not evidence authority.
6. Policy denial and obligations are applied before serialization and rendering.
7. Sensitive geometry or attributes are transformed upstream; style-only hiding is insufficient.
8. Stale, corrected, superseded, withdrawn, or rollback-affected state is visible and cannot silently render as current.
9. Release references are checked; they are not treated as release approval by existence alone.
10. Reason codes and diagnostics do not leak protected details.
11. Runtime proof does not write canonical lifecycle state.
12. Tests do not create production receipts, proofs, or release records.
13. Admin paths do not become normal public paths.
14. A mock adapter remains subordinate to the same evidence, policy, release, and envelope obligations.
15. Unknown or missing governance state fails closed.

### Current governed-api boundary tests

Confirmed tests currently assert:

- unknown routes return `404`;
- non-GET methods on scaffolded routes return `405`;
- forbidden renderer/model imports are absent from governed-api code;
- the route manifest equals the three expected scaffold routes;
- forbidden internal-store path literals are absent from governed-api source.

These are useful boundary checks, but they do not yet prove evidence, policy, release, correction, receipt, domain, UI, or production behavior.

[Back to top](#top)

---

<a id="required-runtime-proof-families"></a>

## Required runtime-proof families

A mature root should cover at least these families.

### 1. Envelope profile and schema

- accepted profile and version are explicit;
- required fields are present;
- unknown fields fail for closed schemas;
- finite outcome enum is closed;
- mixed-profile/hybrid envelopes fail;
- payload contract is separate and validated.

### 2. Identity, time, and integrity

- response id and decision id are deterministic or traceable;
- spec hash binds to accepted contract/config lineage;
- issued/evaluated times are valid and not rewritten;
- replay or stale envelopes are detected;
- correction creates supersession rather than silent mutation.

### 3. Evidence and citation

- `ANSWER` evidence refs resolve;
- missing or unresolved evidence yields `ABSTAIN`;
- conflicting or stale evidence is visible;
- citations match claims and payload scope;
- direct rendered/generated content cannot substitute for evidence.

### 4. Policy, rights, sensitivity, and access

- policy allow, obligations, restriction, and deny paths are explicit;
- rights and consent uncertainty fails closed;
- protected locations and attributes do not leak;
- capability and role changes invalidate prior assumptions;
- admin behavior cannot bypass normal-client policy.

### 5. Freshness, correction, and withdrawal

- freshness is evaluated against use-case requirements;
- corrected/superseded/withdrawn state reaches clients;
- caches and indexes are invalidated;
- stale public state cannot be presented as current;
- rollback target is resolvable.

### 6. Governed API route behavior

- route and method behavior are deterministic;
- request validation is bounded;
- outcome/profile matches route contract;
- payload and envelope are validated separately;
- serialization does not leak internal fields;
- errors are finite and safe.

### 7. Public-client obligations

- `ANSWER` renders citations, caveats, and required notices;
- `ABSTAIN` remains visible and does not become blank/loading;
- `DENY` does not render protected payload;
- `ERROR` does not infer truth or permission;
- correction and withdrawal override cached display.

### 8. AI and Focus Mode

- model invocation occurs only after evidence and policy checks;
- mock and real adapters use the same envelope contract;
- generated text never becomes evidence;
- AIReceipt linkage is validated where required;
- provider failure yields bounded `ERROR`, not invented fallback.

### 9. Domain composition

- domain payload contracts are accepted and separate;
- source-role and time semantics are preserved;
- domain sensitivity is inherited;
- cross-domain joins retain ownership and restrictive posture;
- domain runtime tests use one approved placement.

### 10. No-network and dependency isolation

- default proof uses local deterministic fixtures;
- unexpected network requests fail;
- external-smoke profile is explicit and non-authoritative;
- credentials and private endpoints are absent;
- dependency versions and lock state are recorded where material.

### 11. Leakage and side channels

- response body, headers, logs, stack traces, caches, URLs, search, map, tile, export, screenshot, and generated-summary surfaces are checked;
- internal paths and service names do not leak;
- exact sensitive coordinates cannot be reconstructed;
- denied payloads are not inferable from metadata or timing.

### 12. Receipts, proof, release, and rollback

- candidate receipts/proofs are distinguished from accepted records;
- subject, input, output, and digest linkage closes;
- test success does not approve release;
- correction and rollback are exercised;
- prior known-good state remains addressable.

### Negative matrix

Each material family should include:

```text
positive
invalid
ABSTAIN
DENY
ERROR
stale
conflicted
correction-pending
withdrawn
superseded
rollback
leakage canary
zero-test canary
```

[Back to top](#top)

---

<a id="domain-runtime-proof-placement"></a>

## Domain runtime-proof placement

The merged domain index records two competing layouts:

```text
tests/runtime_proof/domains/<domain>/       # capability-first
tests/domains/<domain>/runtime_proof/       # domain-first
```

Current confirmed examples:

| Domain | Placement | Status |
|---|---|---|
| Roads–Rail–Trade | capability-first | Detailed README; executable proof not established |
| Flora | domain-first | Scaffold README; executable proof not established |

### Root rule

- Do not create new domain children in either convention.
- Do not copy tests or fixtures between both paths.
- Do not claim one convention is canonical by README.
- Resolve through Directory Rules clarification or ADR.
- Preserve history, coverage, imports, workflow filters, and rollback through migration.
- Keep `tests/runtime_proof/domains/README.md` as the active placement and migration guardrail.

### Shared versus domain-specific tests

| Concern | Preferred ownership |
|---|---|
| Shared envelope schema/profile | `tests/runtime_proof/`, schema/contract tests |
| Generic evidence/policy/release composition | `tests/runtime_proof/` or shared API test lane |
| Domain object meaning and source-role rules | `tests/domains/<domain>/` |
| Domain-specific runtime composition | Chosen domain runtime-proof convention after ADR |
| HTTP protocol and route semantics | `tests/api/` or app-owned tests |
| UI rendering obligations | `tests/ui/` |
| End-to-end trust path | `tests/e2e/` |
| Domain release/rollback guardrails | Domain and release test lanes |
| Production observability | dashboards/logs/receipts, not tests |

[Back to top](#top)

---

<a id="fixture-and-test-data-contract"></a>

## Fixture and test-data contract

### Accepted fixture characteristics

Fixtures must be:

- synthetic or explicitly public-safe;
- deterministic;
- compact and reviewable;
- no-network for required proof;
- free of credentials and private endpoints;
- free of exact sensitive locations and protected personal data;
- explicit about expected outcome and reason;
- linked to contract/schema/profile;
- paired with negative cases;
- versioned when shape changes;
- distinguishable from evidence, receipts, proofs, releases, and production responses.

### Minimum shared fixture matrix

| Case | Expected outcome |
|---|---|
| accepted profile and complete evidence | `ANSWER` |
| unresolved EvidenceRef | `ABSTAIN` |
| stale evidence beyond policy | `ABSTAIN` |
| rights or sensitivity denial | `DENY` |
| unauthorized capability | `DENY` |
| malformed request or schema | `ERROR` |
| policy engine unavailable | `ERROR` |
| correction pending | bounded non-current posture |
| withdrawn release | no current `ANSWER` |
| rollback target applied | known prior safe state |
| hybrid envelope profile | validation failure |
| hidden restricted payload | test failure |
| zero tests/scenarios | configuration failure |

### Current minimal fixture boundary

The confirmed RuntimeResponseEnvelope fixtures currently demonstrate:

- one valid `ABSTAIN` object with empty evidence refs;
- one invalid object missing `id`.

That is useful schema coverage. It does not cover `ANSWER`, `DENY`, `ERROR`, evidence resolution, state vocabularies, payload profiles, policy, correction, release, or client behavior.

### Fixture anti-authority rule

A fixture may demonstrate expected shape or behavior. It does not establish:

- real-world truth;
- source authority;
- evidence closure;
- policy correctness;
- release state;
- production safety;
- current operational status;
- public publication.

[Back to top](#top)

---

<a id="network-security-rights-and-sensitivity"></a>

## Network, security, rights, and sensitivity

### Required execution profiles

| Profile | Purpose | Network posture |
|---|---|---|
| `hermetic` | Required local and pull-request proof | External network denied |
| `external-smoke` | Optional integration observation | Explicit allowlist; non-authoritative |
| `restricted-fixture` | Controlled sensitive-policy simulation | Synthetic/generalized only; access logged |
| `production-observation` | Operational monitoring | Outside default test suite; governed separately |

An external-smoke pass must never substitute for hermetic proof.

### Security requirements

- no credentials, tokens, signed URLs, or private endpoints in fixtures;
- no raw exception or stack-trace leakage;
- no filesystem, database, queue, or service topology leakage;
- no unbounded request sizes or fixture bombs;
- deterministic resource limits;
- safe reason codes;
- dependency and serializer versions recorded where material;
- logs treated as possible disclosure surfaces;
- test artifacts retained only as bounded QA material.

### Rights and sensitivity inheritance

A runtime response inherits the most restrictive applicable posture from:

- source rights;
- consent and purpose limitation;
- domain sensitivity;
- living-person/private-land concerns;
- rare-species, archaeology, cultural, infrastructure, and precise-location controls;
- release and review state;
- correction or withdrawal state.

Tests must prove that generalization or redaction cannot be reversed through alternate surfaces.

[Back to top](#top)

---

<a id="ci-and-gate-acceptance"></a>

## CI and gate acceptance

### Current repository commands

| Command or workflow | Confirmed behavior | Runtime-proof limit |
|---|---|---|
| `make schemas` | Runs common validator aggregate | Shape/fixture validation only |
| `make test` | Runs `tests/schemas` and `tests/contracts` | Does not collect `tests/runtime_proof` |
| `make governed-api-smoke` | Runs `apps/governed-api/tests` | Application scaffold/boundary proof |
| `api-test` | Runs governed-api smoke and `test_abstain_routes.py` | No evidence/policy/release/domain/UI matrix |
| `validator-suite` | Runs `make schemas` and one EvidenceBundle fail-closed canary | Not runtime-proof CI |
| domain workflows | Vary; Roads–Rail–Trade workflow is scaffolded | Green status may not mean executable runtime proof |

### Current safe conclusion

```text
schema-validation success
  != runtime-proof success

governed-api scaffold tests pass
  != accepted RuntimeResponseEnvelope profile

domain workflow green
  != domain runtime tests collected

all generic checks green
  != release approval
```

### Required dedicated gate

A trusted runtime-proof workflow should:

1. trigger on shared runtime contracts, schemas, validators, fixtures, runtime wiring, package code, governed API code, runtime-proof tests, API tests, UI obligations, and workflow changes;
2. install from accepted dependency metadata;
3. validate shared envelope schemas and negative fixtures;
4. run governed-api boundary and route tests;
5. collect shared runtime-proof tests;
6. discover the accepted domain runtime-proof convention;
7. fail when zero tests or zero cases are collected;
8. report test counts by proof family and finite outcome;
9. run hermetic no-network guards;
10. exercise evidence resolution and policy stubs/implementations explicitly;
11. test correction, withdrawal, cache invalidation, and rollback;
12. upload bounded QA reports;
13. preserve the primary failure while collecting diagnostics;
14. emit no release approval;
15. expose a rollback target.

### CI maturity ladder

```text
workflow file exists
  < workflow starts
  < expected tests are collected
  < positive and negative cases execute
  < canaries fail correctly
  < artifacts and digests verify
  < repeated runs are stable
  < required promotion integration is accepted
```

Never report a higher maturity level from a lower one.

[Back to top](#top)

---

<a id="test-authoring-contract"></a>

## Test-authoring contract

Every runtime-proof test should declare:

| Field | Requirement |
|---|---|
| Test id | Stable, reviewable identifier |
| Surface | Shared runtime, API route, domain, UI, AI, export, cache, or release |
| Profile | Contract/schema id and version |
| Payload contract | Separate contract/schema when material |
| Fixture ids | Deterministic and public-safe |
| Expected runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| Expected test result | pass/fail/skip/xfail/infrastructure error |
| Evidence posture | Resolved, missing, stale, conflicted, denied |
| Policy posture | Allow, obligations, deny, unavailable |
| Freshness/correction posture | Current, stale, corrected, withdrawn, rollback-affected |
| Release posture | Candidate, released, withdrawn, superseded |
| Leakage assertions | Body, headers, logs, cache, URLs, exports, maps, AI |
| Network profile | Hermetic or explicit external-smoke |
| Rollback target | Required when stateful or release-facing |
| Owners | QA plus relevant runtime/domain/policy/release reviewers |

### Test-body rules

Tests should:

- assert one finite outcome;
- assert stable safe reason codes;
- validate envelope and payload separately;
- verify disallowed payload absence;
- resolve evidence refs when `ANSWER` is expected;
- assert policy and release posture;
- check correction/freshness behavior;
- assert client obligations;
- avoid live network and secrets;
- fail on unrecognized profiles or outcomes;
- avoid redefining production logic inside test helpers.

### Naming and placement

Until the domain placement conflict is resolved:

- shared runtime tests may be added under an accepted shared path inside `tests/runtime_proof/`;
- new domain child directories are frozen;
- app-owned route tests remain under the app test root;
- shared schema/contract fixture tests remain in their current roots;
- a migration note is required before moving existing domain lanes.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

The following commands describe grounded verification targets. They were **not run** during this documentation-only API update.

### Inventory

```bash
find tests/runtime_proof -maxdepth 4 -type f -print | sort
find tests/domains -path '*/runtime_proof/*' -type f -print | sort
git grep -n "tests/runtime_proof"
git grep -n "RuntimeResponseEnvelope\|DecisionEnvelope"
```

### Shared schema and fixtures

```bash
python -m pytest tests/schemas/test_common_contracts.py -q
python tools/validators/validate_runtime_response_envelope.py
python tools/validators/validate_decision_envelope.py
```

### Governed API scaffold checks

```bash
PYTHONPATH=apps/governed-api/src \
  python -m pytest apps/governed-api/tests/test_abstain_routes.py -q

PYTHONPATH=apps/governed-api/src \
  python -m pytest apps/governed-api/tests/test_boundary_guards.py -q

make governed-api-smoke
```

### Runtime-proof collection

```bash
python -m pytest --collect-only tests/runtime_proof -q
python -m pytest tests/runtime_proof -q
```

A required gate should fail when collection returns zero executable tests.

### Domain placement inventory

```bash
find tests/runtime_proof/domains -mindepth 1 -maxdepth 2 -type d -print | sort
find tests/domains -mindepth 2 -maxdepth 3 -type d -name runtime_proof -print | sort
```

### Workflow inventory

```bash
git grep -n "runtime_proof\|tests/runtime_proof" .github/workflows Makefile
```

### Documentation preflight used for this revision

- one rendered H1;
- no heading-level jumps;
- balanced fenced code blocks;
- no duplicate rendered headings;
- all explicit quick-navigation anchors resolve;
- no trailing whitespace or tabs;
- no common credential or private-key patterns.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The root runtime-proof lane is mature when:

### Architecture and profiles

- [ ] An accepted profile defines RuntimeResponseEnvelope, DecisionEnvelope, payload composition, and compatibility.
- [ ] Contract/schema/architecture drift is resolved or governed by explicit adapters.
- [ ] Reason-code, policy-state, freshness, correction-state, and obligation vocabularies are accepted.
- [ ] Reusable helper ownership between `runtime/envelopes/` and `packages/envelopes/` is operationally clear.

### Shared implementation

- [ ] Envelope package exports are implemented and tested, or the package is explicitly retired.
- [ ] Runtime policy is executable or explicitly substituted by deterministic test policy.
- [ ] Evidence resolution and citation checks are wired.
- [ ] Receipt persistence and release/correction interfaces are testable.
- [ ] Governed API serializers validate the accepted profile.

### Test coverage

- [ ] Shared runtime-proof tests are executable.
- [ ] All four outcomes have positive and negative coverage.
- [ ] Hybrid profile and unknown outcome canaries fail.
- [ ] Trust-membrane, leakage, network, correction, and rollback tests exist.
- [ ] Public-client obligations are tested.
- [ ] Domain runtime-proof placement is resolved and migrated.

### CI maturity

- [ ] A dedicated workflow collects shared and domain runtime proof.
- [ ] Zero tests and zero scenarios fail.
- [ ] Test counts and outcome coverage are visible.
- [ ] Hermetic execution is required.
- [ ] External-smoke results are separated.
- [ ] The gate is required where promotion depends on runtime behavior.

### Governance and operations

- [ ] Owners and CODEOWNERS are assigned.
- [ ] Fixtures remain public-safe and non-authoritative.
- [ ] Correction, withdrawal, cache invalidation, and rollback are tested.
- [ ] Release and public-client behavior are verified separately from schema fixtures.
- [ ] Open conflicts are resolved or registered with explicit owners and deadlines.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Phase 1 — Freeze and inventory

1. Freeze new domain runtime-proof children.
2. Recursively inventory both placement patterns.
3. Inventory shared tests, app tests, fixtures, workflows, and consumers.
4. Record exact current collection and pass state.

**Stop if:** an undocumented executable lane or duplicate suite is found.

### Phase 2 — Resolve envelope profiles

1. Compare RuntimeResponseEnvelope, DecisionEnvelope, architecture prose, and API stub.
2. Select accepted profiles and versions.
3. Define payload composition and compatibility rules.
4. Define state/reason/obligation vocabularies.
5. Add ADR or accepted governance record.

**Stop if:** production consumers depend on an undocumented hybrid.

### Phase 3 — Close shared shape proof

1. Expand valid/invalid fixtures across all four outcomes.
2. Add mixed-profile and unknown-field negatives.
3. Verify validators and common harness.
4. Add deterministic profile identifiers.

**Stop if:** schema and contract semantics disagree materially.

### Phase 4 — Implement shared runtime proof

1. Add executable tests under the accepted shared root.
2. Exercise evidence, policy, freshness, correction, release, and receipt seams.
3. Add no-network and leakage canaries.
4. Fail on zero tests.

**Stop if:** tests reimplement production policy/evidence logic.

### Phase 5 — Close governed API proof

1. Bind serializers to accepted profile.
2. Validate envelope and payload separately.
3. Expand route tests beyond ABSTAIN scaffolds.
4. Test method, error, denial, correction, and leakage behavior.
5. Preserve current scaffold rollback.

**Stop if:** route behavior exposes internal stores or protected detail.

### Phase 6 — Resolve domain placement

1. Select capability-first or domain-first convention.
2. Map Roads–Rail–Trade and Flora coverage.
3. Move one lane at a time through normal commits.
4. Update imports, fixtures, docs, workflows, and CODEOWNERS atomically.
5. Leave compatibility pointers only where needed.

**Stop if:** coverage, history, or rollback cannot be preserved.

### Phase 7 — Add dedicated CI

1. Create runtime-proof workflow and path filters.
2. Run shared and accepted domain tests.
3. Record counts, outcomes, and canaries.
4. Separate hermetic and external-smoke profiles.
5. Decide required-check status.

**Stop if:** green status can occur with zero tests or skipped core families.

### Phase 8 — Integrate correction and release

1. Exercise correction, withdrawal, cache invalidation, and rollback.
2. Verify receipt/proof linkage.
3. Verify public-client state independently.
4. Run rollback drill.
5. Record remaining limitations.

**Stop if:** test output is mistaken for release approval.

[Back to top](#top)

---

<a id="correction-and-rollback"></a>

## Correction and rollback

### Documentation correction

When this README becomes stale:

1. identify the unsupported statement;
2. identify the evidence that changed;
3. narrow or relabel the claim;
4. update affected child indexes and links;
5. preserve prior blob/commit;
6. record unresolved drift;
7. do not hide implementation regression behind wording.

### Runtime-proof correction

When a test or fixture is wrong:

1. hold any claim that depended on it;
2. identify affected profiles, routes, domains, and releases;
3. preserve failing artifacts and logs;
4. correct fixture, test, implementation, or contract at the owning root;
5. add a regression case;
6. rerun the full required profile;
7. invalidate stale reports and caches;
8. preserve rollback target.

### Safety rollback triggers

Rollback is required when a change:

- weakens finite-outcome closure;
- permits `ANSWER` without evidence/policy/release support;
- hides `ABSTAIN`, `DENY`, or `ERROR`;
- exposes restricted payload or exact sensitive detail;
- creates a direct internal-store or model-runtime path;
- makes zero tests appear green;
- creates parallel domain test authority;
- silently merges incompatible envelope profiles;
- removes correction, withdrawal, or rollback visibility;
- treats test output as release approval.

Before merge, rollback is leaving the review unmerged or restoring the prior blob in a transparent commit.

After merge, rollback is a normal revert commit or revert pull request. Do not reset or rewrite shared history.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

### Inventory and placement

- [ ] Recursively inventory `tests/runtime_proof/`.
- [ ] Inventory all domain-first runtime-proof lanes.
- [ ] Inventory all app/API/UI/E2E tests that implement runtime-proof concerns.
- [ ] Resolve domain capability-first versus domain-first placement.
- [ ] Confirm CODEOWNERS and required reviewers.

### Envelope and package profiles

- [ ] Resolve RuntimeResponseEnvelope versus DecisionEnvelope profile use.
- [ ] Resolve governed-api architecture/schema drift.
- [ ] Define payload contract and profile identifiers.
- [ ] Define reason, policy, freshness, correction, and obligation vocabularies.
- [ ] Decide package/envelope implementation ownership.
- [ ] Implement or explicitly retire the `packages/envelopes` scaffold.

### Shared proof implementation

- [ ] Add direct executable tests under this root.
- [ ] Add all-four-outcome fixtures.
- [ ] Add hybrid-profile and unknown-outcome negatives.
- [ ] Add evidence-resolution and citation tests.
- [ ] Add policy execution and unavailable-policy tests.
- [ ] Add receipt, freshness, correction, withdrawal, and rollback tests.
- [ ] Add client-obligation and leakage tests.
- [ ] Add no-network guard.

### Governed API

- [ ] Verify route inventory and intended consumers.
- [ ] Bind routes to an accepted envelope profile.
- [ ] Add payload schemas.
- [ ] Expand beyond `NOT_IMPLEMENTED` ABSTAIN scaffolds.
- [ ] Verify safe error and denial serialization.
- [ ] Verify no internal-store, source, or model-runtime bypass.
- [ ] Verify production deployment separately.

### CI backlog

- [ ] Create a dedicated runtime-proof workflow.
- [ ] Add complete path filters.
- [ ] Fail on zero tests and zero scenarios.
- [ ] Report proof-family and outcome coverage.
- [ ] Separate hermetic and external-smoke profiles.
- [ ] Decide required promotion-check status.
- [ ] Inspect current promotion-gate failures separately.

### Governance and release

- [ ] Confirm ADR-0020 acceptance or replacement status.
- [ ] Confirm runtime policy ownership and implementation.
- [ ] Confirm receipt/proof destinations and retention.
- [ ] Verify correction/cache invalidation consumers.
- [ ] Verify release and rollback integration.
- [ ] Record a tested migration and rollback path.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | CONFIRMED | Existing root intent and prior blob | Stale implementation and placement claims |
| `tests/README.md` | CONFIRMED | Tests authority, runtime-proof and domain lanes, trust-spine classes | Does not resolve lane intersection |
| Merged domains index | CONFIRMED v0.2 | Placement conflict, child freeze, current inventory, CI gap | Does not select migration winner |
| Roads–Rail–Trade child README | CONFIRMED v0.2 | Capability-first child and detailed domain proof requirements | Executable route/schema/tests remain unclosed |
| Flora runtime-proof README | CONFIRMED v0.1 | Domain-first alternate lane | Scaffold; execution unverified |
| RuntimeResponseEnvelope contract/schema | CONFIRMED paired / PROPOSED | Closed client-facing field surface and finite outcomes | Does not prove runtime behavior |
| DecisionEnvelope schema | CONFIRMED concrete / PROPOSED | Policy-style finite envelope and optional scaffold fields | Profile overlap unresolved |
| Runtime validators | CONFIRMED executable wrappers | Schema/fixture validation entry points | Do not prove evidence, policy, release, or clients |
| Runtime fixtures | CONFIRMED minimal | One valid and one invalid shared example | Narrow shape-only coverage |
| Common schema test harness | CONFIRMED executable test | Runtime schemas with fixture roots are discoverable | Not runtime integration proof |
| Governed API main/registry/stub | CONFIRMED executable scaffold | Three registered routes and deterministic ABSTAIN builder | Not production or accepted profile proof |
| Governed API abstain tests | CONFIRMED executable pytest | All registered routes return expected ABSTAIN and validate DecisionEnvelope subset | No ANSWER/DENY/ERROR or full RuntimeResponseEnvelope proof |
| Governed API boundary tests | CONFIRMED executable pytest | 404/405, route manifest, forbidden imports and internal-store literals | Not evidence/policy/release/client proof |
| `runtime/envelopes/` | CONFIRMED canonical handoff lane | Runtime coordination and profile conflict | Executable helpers unknown |
| `packages/envelopes/` | CONFIRMED scaffold | Intended reusable implementation home | Empty API and no consumer |
| `policy/runtime/` | CONFIRMED stub | Runtime policy home exists | No executable policy proof |
| Root Makefile | CONFIRMED | Exact current command scope | `make test` excludes runtime proof |
| `api-test` workflow | CONFIRMED | Governed API and abstain-route checks run in CI | Not a full runtime-proof gate |
| `validator-suite` workflow | CONFIRMED | Schema validation and fail-closed evidence canary | Not runtime-proof CI |
| ADR-0020 | CONFIRMED document / PROPOSED | Cite-or-abstain and finite-outcome intent | Not accepted implementation authority |
| Current-session execution | NOT RUN | Documentation-only API update | No test, route, validator, workflow, or production pass claim |

[Back to top](#top)
