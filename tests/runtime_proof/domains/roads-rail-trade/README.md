<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-runtime-proof-domains-roads-rail-trade-readme
title: tests/runtime_proof/domains/roads-rail-trade/ — Roads–Rail–Trade Governed Runtime Proof Contract
type: readme; directory-readme; domain-runtime-proof-index; finite-outcome-test-contract; trust-membrane-guardrail
version: v0.2
status: draft; readme-only-in-bounded-evidence; shared-runtime-schema-present; domain-schema-absent; domain-routes-unverified; domain-workflow-stub; proof-not-closed; NEEDS VERIFICATION
policy_label: public-doc; restricted-review-when-cultural-corridor-sensitive-facility-private-access-or-operational-status-is-in-scope
owners: OWNER_TBD — QA steward · Runtime-proof steward · Roads–Rail–Trade steward · Governed API steward · Evidence steward · Policy steward · Sensitivity/rights reviewer · Release steward · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
current_path: tests/runtime_proof/domains/roads-rail-trade/README.md
truth_posture: CONFIRMED target README and prior blob, tests/runtime_proof parent and domains index, tests responsibility root, Roads–Rail–Trade API doctrine and path collision, Roads–Rail–Trade domain test index, Roads–Rail–Trade schema index with no confirmed concrete domain schemas, shared RuntimeResponseEnvelope contract/schema/validator/fixture family, finite ANSWER/ABSTAIN/DENY/ERROR enum, domain workflow stub, and bounded absence of Roads–Rail–Trade governed API route/controller/module results at the pinned snapshot / PROPOSED runtime surfaces, RoadsRailDecisionEnvelope, route names, domain payload profiles, reason-code registry, fixture families, executable runtime-proof tests, CI wiring, cache invalidation, release integration, and public-client behavior / CONFLICTED flat API_CONTRACTS.md versus api-contracts/README.md, roads-rail-trade versus transport schema slug, generic RuntimeResponseEnvelope versus proposed domain-specific envelope, and domain runtime-proof lane versus broader domain test map/API families / UNKNOWN deployed routes, runtime consumers, current pass state, production data access, public map behavior, operational status behavior, and release health / NEEDS VERIFICATION owners, accepted API-doc home, domain schema profile, route inventory, executable tests, fixtures, policy bindings, evidence resolution, CI, correction propagation, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9ab8009f9dd2a050327b146558afdf65a38d08a4
  prior_blob: 8846603f4222496c99750c9b840a75e1702ed473
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../../../domains/roads-rail-trade/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/domains/roads-rail-trade/API_CONTRACTS.md
  - ../../../../docs/domains/roads-rail-trade/api-contracts/README.md
  - ../../../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../../../docs/domains/roads-rail-trade/MAP_UI_CONTRACTS.md
  - ../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../../fixtures/contracts/v1/runtime/runtime_response_envelope/valid/README.md
  - ../../../../schemas/contracts/v1/domains/roads-rail-trade/README.md
  - ../../../../contracts/domains/roads-rail-trade/
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../release/
  - ../../../../.github/workflows/domain-roads-rail-trade.yml
tags: [kfm, tests, runtime-proof, roads-rail-trade, governed-api, finite-outcomes, runtime-response-envelope, evidence, policy, rights, sensitivity, source-role, temporal, graph-not-truth, map-not-truth, operational-status, correction, rollback, no-network, fail-closed]
notes:
  - "v0.2 replaces an aspirational runtime-proof README with a repository-grounded proof contract and explicit implementation boundary."
  - "Bounded search surfaced only this README directly under the target lane; no executable test module was confirmed."
  - "The shared RuntimeResponseEnvelope schema, validator wrapper, and minimal fixtures exist, but they do not prove a Roads–Rail–Trade route or domain payload."
  - "The Roads–Rail–Trade domain workflow is an echo-only scaffold and cannot prove validation, runtime behavior, or release readiness."
  - "This revision changes documentation only and creates, moves, deletes, or activates no route, test, fixture, schema, validator, workflow, package, policy, data, receipt, proof, or release record."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/runtime_proof/domains/roads-rail-trade/` — Roads–Rail–Trade Governed Runtime Proof Contract

> **Purpose.** Define the executable proof required before a Roads–Rail–Trade feature, layer, Evidence Drawer payload, Focus Mode answer, status statement, route relation, or transport-network projection can be presented through a governed runtime surface as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Implementation: README only" src="https://img.shields.io/badge/implementation-README__only-red">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER__ABSTAIN__DENY__ERROR-informational">
  <img alt="Workflow: stub" src="https://img.shields.io/badge/workflow-echo__only-orange">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> This lane proves runtime behavior. It does **not** own road, rail, route, corridor, crossing, facility, operator, restriction, access, legal-status, historical, graph, map, source, evidence, policy, or release truth.

> [!WARNING]
> Current repository evidence does **not** establish a Roads–Rail–Trade governed API route, domain response schema, executable runtime-proof test, domain fixture set, or CI gate. The shared runtime envelope family exists, but domain-specific runtime proof remains unimplemented in bounded evidence.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Inventory](#confirmed-repository-inventory) · [Surfaces](#runtime-surfaces-under-proof) · [Envelope](#runtime-envelope-contract) · [Outcomes](#finite-outcome-discipline) · [Domain boundaries](#roads-rail-trade-domain-boundaries) · [Time](#temporal-and-freshness-proof) · [Evidence](#evidence-citation-and-source-role-proof) · [Policy](#rights-sensitivity-and-policy-proof) · [Trust membrane](#trust-membrane-and-public-client-proof) · [Coverage](#required-test-families) · [Fixtures](#fixture-contract) · [CI](#ci-and-gate-acceptance) · [Authoring](#test-authoring-contract) · [Validation](#validation) · [Done](#definition-of-done) · [Migration](#smallest-sound-implementation-sequence) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence basis](#evidence-basis)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/runtime_proof/domains/roads-rail-trade/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| Other direct files under the target lane | **NOT SURFACED in bounded search** | Treat this child as README-only until recursive inventory proves otherwise. |
| `tests/runtime_proof/README.md` | **CONFIRMED draft parent** | Defines runtime proof around finite outcomes and trust-membrane behavior; executable depth remains unverified. |
| `tests/runtime_proof/domains/README.md` | **CONFIRMED draft index** | Indexes this child as the only surfaced domain runtime-proof lane in bounded evidence. |
| `tests/domains/roads-rail-trade/` | **CONFIRMED README-oriented domain test tree** | Documents contract, evidence, policy, and release test families; executable modules remain unverified. |
| Roads–Rail–Trade API doctrine | **CONFIRMED draft documentation** | Describes expected surfaces and finite outcomes; exact routes and implementation remain proposed or unknown. |
| Roads–Rail–Trade API documentation home | **CONFLICTED** | Both `API_CONTRACTS.md` and `api-contracts/README.md` cover the same surface. |
| Roads–Rail–Trade domain schema lane | **CONFIRMED index / no concrete domain schema confirmed** | Do not claim a domain response schema or field-complete domain object family. |
| Shared `RuntimeResponseEnvelope` contract/schema | **CONFIRMED paired / PROPOSED status** | A closed shared envelope shape exists with required fields and four finite outcomes. |
| Shared envelope validator | **CONFIRMED wrapper** | Validates shared schema shape; does not prove domain semantics, evidence resolution, policy, release, or route behavior. |
| Shared envelope fixtures | **CONFIRMED minimal coverage** | One minimal `ABSTAIN` fixture and one missing-`id` invalid case are documented. |
| Roads–Rail–Trade governed API route/controller/module | **NOT SURFACED in bounded search** | Do not invent route names or claim runtime implementation. |
| Roads–Rail–Trade domain workflow | **CONFIRMED echo-only scaffold** | A green job can only prove the echo command ran. |
| Dedicated runtime-proof workflow | **NOT SURFACED in bounded search** | Do not claim this lane runs in CI. |
| Current test pass state | **UNKNOWN** | Source inspection is not execution evidence. |
| Production runtime behavior | **UNKNOWN** | Documentation, schemas, and workflow stubs do not prove deployed behavior. |

**Authority of this README:** lane purpose, proof requirements, finite-outcome expectations, domain anti-collapse rules, fixture constraints, CI acceptance criteria, correction guidance, and rollback guidance.

The following outrank this README for their responsibilities:

- accepted Directory Rules and ADRs;
- semantic contracts;
- machine schemas;
- source registries and catalog records;
- evidence and citation records;
- policy bundles and decisions;
- executable runtime and API code;
- executable tests and validators;
- CI definitions and logs;
- release, correction, withdrawal, supersession, and rollback records;
- steward decisions.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from repository files, commit history, schema shape, or inspected implementation. |
| **PROPOSED** | A design, route, schema profile, test, fixture, or procedure not yet accepted or implemented. |
| **CONFLICTED** | Repository surfaces disagree or create competing authority. |
| **NEEDS VERIFICATION** | Checkable, but not sufficiently proven for reliance or promotion. |
| **UNKNOWN** | Not established by inspected evidence. |

[Back to top](#top)

---

<a id="placement-and-authority"></a>

## Placement and authority

### Directory Rules basis

KFM places files by primary responsibility:

```text
tests/                                      enforceability proof
tests/runtime_proof/                        governed runtime finite-outcome proof
tests/runtime_proof/domains/<domain>/       domain-bounded runtime proof
tests/domains/<domain>/                     broader domain guardrail tests
tests/fixtures/ and fixtures/               synthetic examples
apps/governed-api/                          trust-membrane runtime implementation
packages/domains/roads-rail-trade/           domain implementation helpers
contracts/                                  semantic meaning
schemas/                                    machine-checkable shape
policy/                                     admissibility and obligations
data/receipts/ and data/proofs/              emitted audit and proof records
release/                                    promotion, correction, withdrawal, rollback
```

The target is correctly under the `tests/` responsibility root and follows the currently documented runtime-proof parent layout.

### Current path class

| Field | Value |
|---|---|
| Primary responsibility | Roads–Rail–Trade governed runtime enforceability proof |
| Repository status | Present as README-only in bounded evidence |
| Placement status | `CURRENT / DRAFT` |
| Runtime implementation | Not owned here |
| Route authority | None |
| Schema authority | None |
| Policy authority | None |
| Release authority | None |
| Write posture | README guidance and future executable tests only |
| Required reviewers | QA, runtime proof, Roads–Rail–Trade, governed API, evidence, policy, sensitivity/rights, release, CI, docs |

### Relationship to broader domain tests

`tests/domains/roads-rail-trade/` and this lane must not become parallel implementations.

| Concern | Preferred proof lane |
|---|---|
| Contract meaning, identity, route membership, source role, historic precision, legal-status denial, general release and rollback behavior | `tests/domains/roads-rail-trade/` |
| Actual client-facing finite runtime envelope and trust-membrane behavior | `tests/runtime_proof/domains/roads-rail-trade/` |
| Governed API route and HTTP/envelope behavior | `tests/api/`, app-owned tests, and this lane when domain-specific runtime composition is under proof |
| Shared RuntimeResponseEnvelope schema conformance | shared runtime contract fixtures and schema tests |
| Public map/UI behavior | UI/E2E lanes, with this lane asserting runtime posture and refs |

A future test may compose lower-level domain tests, but it must not copy their authority or redefine their fixtures silently.

### Authority routing

| Concern | Owning home | This lane's role |
|---|---|---|
| Road/Rail/Trade object meaning | `contracts/domains/roads-rail-trade/` | Assert, never redefine |
| Domain machine shape | accepted Roads–Rail–Trade schema home | Validate once accepted |
| Shared runtime envelope | `contracts/runtime/` and `schemas/contracts/v1/runtime/` | Conform and test client behavior |
| Governed API implementation | `apps/governed-api/` | Exercise through bounded test interfaces |
| Domain implementation | `packages/domains/roads-rail-trade/` | Treat as system under test |
| Evidence resolution | evidence contracts, resolvers, and proof roots | Assert refs resolve or abstain |
| Policy and rights | `policy/` | Assert finite decision and obligations |
| Release state | `release/` | Assert current/corrected/withdrawn posture |
| Synthetic fixtures | `tests/fixtures/` or `fixtures/domains/roads-rail-trade/` after placement review | Consume, never treat as truth |
| Test reports | accepted QA artifact lane | Emit bounded reports, not release approval |

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Target lane

```text
tests/runtime_proof/domains/roads-rail-trade/
└── README.md
```

Bounded search did not surface an executable test module, fixture payload, helper, configuration, or child README directly under this target.

### Adjacent runtime-proof documentation

```text
tests/runtime_proof/
├── README.md
└── domains/
    ├── README.md
    └── roads-rail-trade/
        └── README.md
```

These READMEs define intended proof responsibility. They are not runtime execution evidence.

### Broader Roads–Rail–Trade test documentation

```text
tests/domains/roads-rail-trade/
├── README.md
├── contracts/
├── evidence/
├── policy/
└── release/
```

The broader domain test index documents child README families and proposed guardrails. It explicitly leaves executable test depth and pass rates unverified.

### Shared runtime envelope surfaces

```text
contracts/runtime/runtime_response_envelope.md
schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
tools/validators/validate_runtime_response_envelope.py
fixtures/contracts/v1/runtime/runtime_response_envelope/
```

The shared schema is closed and concrete, but its status is `PROPOSED`.

### Domain API and schema surfaces

```text
docs/domains/roads-rail-trade/API_CONTRACTS.md
docs/domains/roads-rail-trade/api-contracts/README.md
schemas/contracts/v1/domains/roads-rail-trade/README.md
```

Current conflicts:

- two API documentation homes cover the same responsibility;
- older documentation proposes a flat `transport` schema family;
- current schema-home guidance points to `domains/roads-rail-trade`;
- no concrete Roads–Rail–Trade `.schema.json` file was confirmed under the domain lane;
- `RoadsRailDecisionEnvelope` is documented as a proposed domain projection, not a confirmed implementation.

### CI surface

```text
.github/workflows/domain-roads-rail-trade.yml
```

The workflow currently contains three echo-only jobs:

```text
validate-roads-rail-trade
build-proof-roads-rail-trade
publish-dry-run-roads-rail-trade
```

This workflow does not execute a runtime-proof suite, validate domain schemas, call a governed API route, resolve evidence, evaluate policy, or build a release proof in its checked form.

[Back to top](#top)

---

<a id="runtime-surfaces-under-proof"></a>

## Runtime surfaces under proof

Roads–Rail–Trade API documentation describes these intended public or trust-membrane-mediated surfaces:

| Surface | Intended response | Current implementation status |
|---|---|---|
| Feature/detail resolver | Domain feature/detail response through a finite runtime envelope | Route and implementation **UNKNOWN** |
| Layer manifest resolver | Released public-safe layer descriptor or finite refusal | Route and implementation **UNKNOWN** |
| Evidence Drawer payload | Evidence-aware selected-feature projection | Route and implementation **UNKNOWN** |
| Focus Mode answer | Evidence-bounded synthesis plus finite outcome and AI receipt | Route and implementation **UNKNOWN** |
| Correction/rollback-facing state | Corrected, withdrawn, superseded, or rollback-affected client posture | Runtime wiring **UNKNOWN** |

### Route-name rule

Do not put invented HTTP paths into tests or this README.

Before binding route tests:

1. inspect actual router modules;
2. inspect OpenAPI or route registration;
3. inspect app tests;
4. pin the exact route and method;
5. record authentication/audience posture;
6. record accepted request and response schemas;
7. add negative tests for missing and unauthorized routes;
8. update this README with the evidence.

A documentation route name is not a runtime route.

### Surface anti-collapse

The following must remain separate:

```text
feature detail response
  != canonical road/rail record

layer manifest response
  != release approval

Evidence Drawer payload
  != EvidenceBundle

Focus Mode answer
  != evidence

RuntimeResponseEnvelope
  != domain payload store

PolicyDecision
  != RuntimeResponseEnvelope

test pass
  != proof closure

proof closure
  != release approval
```

[Back to top](#top)

---

<a id="runtime-envelope-contract"></a>

## Runtime envelope contract

### Confirmed shared field surface

The current shared `RuntimeResponseEnvelope` schema requires:

| Field | Confirmed schema shape | Runtime-proof expectation |
|---|---|---|
| `id` | identifier string | Stable, non-secret response identity |
| `spec_hash` | `sha256:` plus 64 lowercase hex characters | Pins contract/spec lineage |
| `version` | string | Supports compatibility and migration |
| `issued_at` | date-time string | Must reflect actual emission time |
| `outcome` | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` | Closed finite set |
| `reason_code` | string | Safe, stable, non-leaking reason |
| `evidence_refs` | array of EvidenceRef objects | Required field; semantics depend on outcome |
| `policy_state` | string | Controlled vocabulary still needs acceptance |
| `freshness` | string | Controlled vocabulary still needs acceptance |
| `correction_state` | string | Controlled vocabulary still needs acceptance |

The schema sets:

```text
additionalProperties: false
```

### Shared schema limitations

The shared schema does not currently define:

- a domain feature payload;
- a layer manifest payload;
- Evidence Drawer payload fields;
- Focus Mode answer text;
- obligations;
- release references;
- rollback references;
- citation-validation references;
- audience or authorization fields;
- route identity;
- domain object family.

Tests must not smuggle those fields into the closed envelope.

### No implicit payload rule

Because the shared schema has no payload field:

1. validate the envelope as its own object;
2. validate any domain payload against a separately accepted schema;
3. bind envelope and payload through an explicit contract or response composition;
4. test that `DENY` and `ERROR` expose no restricted payload;
5. test that `ABSTAIN` does not carry a substantive unsupported answer;
6. test that `ANSWER` payload identity and evidence refs agree.

Do not add arbitrary fields to the envelope in a fixture merely because a route needs payload data.

### Domain profile conflict

Roads–Rail–Trade API documentation proposes `RoadsRailDecisionEnvelope`, while current shared runtime schemas define `RuntimeResponseEnvelope` and `DecisionEnvelope`.

Before a domain profile is implemented, decide explicitly whether it is:

- a separate domain payload wrapped by `RuntimeResponseEnvelope`;
- a schema profile using composition;
- a compatibility alias;
- a deprecated design;
- a new object family requiring contract/schema/registry review.

Do not maintain two closed response-envelope authorities with overlapping meanings.

### Current shared fixture coverage

The confirmed positive shared fixture is a minimal `ABSTAIN` object with:

```text
reason_code: NOT_IMPLEMENTED
evidence_refs: []
policy_state: baseline
freshness: current
correction_state: none
```

The confirmed negative fixture omits `id`.

This proves only narrow schema shape behavior. It does not prove:

- a Roads–Rail–Trade response;
- domain payload validity;
- evidence resolution;
- policy evaluation;
- release eligibility;
- correction state;
- route behavior;
- client rendering;
- leakage prevention.

[Back to top](#top)

---

<a id="finite-outcome-discipline"></a>

## Finite outcome discipline

### Runtime outcomes

| Outcome | Use when | Must include or prove | Must not do |
|---|---|---|---|
| `ANSWER` | Evidence is sufficient, policy permits, the surface is release-eligible, and freshness/correction state permits response | Valid envelope, supported payload, evidence refs, safe reason/state fields, release-aware posture | Invent, overclaim, expose unreleased state, or imply operational authority |
| `ABSTAIN` | Evidence, citation, freshness, source-role support, temporal alignment, or scope is insufficient | Safe abstention reason; no substantive unsupported claim | Return low-confidence prose as an answer |
| `DENY` | Rights, sensitivity, access, policy, review, release, or public-surface rules prohibit output | Safe denial reason; no restricted payload or reconstructive hints | Leak exact geometry, private access data, or hidden fields |
| `ERROR` | Request, schema, contract, dependency, adapter, policy runtime, or infrastructure cannot evaluate safely | Bounded diagnostic code and safe client state | Emit stack traces, internal paths, credentials, or fallback claims |

### Test results are not runtime outcomes

| Test result | Meaning |
|---|---|
| pass | Observed behavior matched the expected runtime outcome and leakage posture |
| fail | Observed behavior violated the test contract |
| skip | Explicitly unavailable condition; not proof |
| expected failure | Tracked defect with owner and expiry |
| infrastructure error | Test harness could not evaluate the runtime |
| zero tests collected | Required-suite configuration failure |

A test expecting `DENY` passes when the runtime safely denies. `DENY` is not a failed test.

### Outcome exclusivity

Every response must have exactly one outcome.

Reject:

```text
ANSWER + warning-as-deny
ANSWER + hidden abstention
DENY + payload
ERROR + fallback answer
ABSTAIN + inferred route status
null outcome
unknown outcome
PARTIAL
PENDING
UNKNOWN
```

### Stable reason-code requirements

Reason codes should be:

- finite and documented;
- safe for the intended audience;
- stable enough for tests and clients;
- specific enough for correction;
- free of exact sensitive details;
- free of credentials, prompts, stack traces, database names, and internal paths;
- separate from human-facing explanatory text.

Proposed categories that require acceptance before enforcement:

```text
EVIDENCE_MISSING
EVIDENCE_STALE
SOURCE_ROLE_CONFLICT
TEMPORAL_MISALIGNMENT
RIGHTS_UNRESOLVED
SENSITIVITY_DENIED
RELEASE_MISSING
CORRECTION_PENDING
WITHDRAWN
ROLLBACK_TARGET_MISSING
SCHEMA_INVALID
CONTRACT_DRIFT
ROUTE_NOT_IMPLEMENTED
DEPENDENCY_UNAVAILABLE
```

These are test-design candidates, not a confirmed reason-code registry.

[Back to top](#top)

---

<a id="roads-rail-trade-domain-boundaries"></a>

## Roads–Rail–Trade domain boundaries

### Object and relation distinctions

Runtime proof must preserve at least these distinctions:

| Concept | Meaning boundary |
|---|---|
| Road segment | Physical or represented road segment; not automatically a route designation, access permission, legal status, or current condition |
| Rail segment | Rail network segment; not automatically an operator assignment, service status, ownership claim, or current availability |
| Route membership | Relation between a segment and a route/corridor; not segment identity |
| Corridor route | Route/corridor concept; not guaranteed current traversability |
| Historic route claim | Evidence-bounded interpretation with time and uncertainty; not modern-survey truth |
| Trade route/corridor | Historical, economic, or interpretive relation; may carry rights and cultural-sensitivity review |
| Restriction event | Time-bounded restriction evidence; not permanent legal status unless authority and time support it |
| Operator assignment | Time-scoped relation; not timeless operator truth |
| Operator status | Status assertion with source/time scope; not route availability |
| Transport facility | Transport-domain reference; critical infrastructure and adjacent-domain ownership remain separate |
| Crossing/bridge/ferry | Transport relation or facility context; does not replace Hydrology or Settlements/Infrastructure truth |
| Network edge | Derived graph projection; not canonical route, membership, or access truth |
| Public-safe route summary | Released derivative; not navigation instruction or legal advice |

### Source-role anti-collapse

Tests must reject:

```text
OSM convenience attribute -> legal designation
GNIS name -> route authority
route shield -> segment identity
historic map -> current road geometry
modeled corridor -> observed route use
graph connectivity -> legal access
operator assignment -> current service status
catalog record -> public release
map feature -> evidence closure
AI summary -> transport truth
```

### Operational and legal-status boundary

KFM runtime proof must not present Roads–Rail–Trade output as:

- turn-by-turn navigation;
- emergency routing;
- current road-closure authority;
- railroad dispatch or movement authority;
- legal access permission;
- engineering condition assessment;
- bridge-load authority;
- title, easement, or right-of-way determination;
- guaranteed route availability;
- substitute for official transportation or emergency sources.

When a user request is operationally current or safety-significant, tests should prove that the runtime:

1. narrows the claim;
2. exposes freshness and source authority;
3. redirects to the appropriate official source where policy requires;
4. abstains or denies when current authoritative support is unavailable;
5. never converts historical or contextual evidence into live guidance.

### Graph-not-truth boundary

A graph projection may support traversal analysis or visualization, but tests must prove:

- each edge resolves to source-bound objects or relations;
- derived edges are labeled as projections;
- graph version and build lineage are explicit;
- invalidation follows correction and withdrawal;
- graph reachability does not imply access, safety, legality, or current service;
- graph results do not replace RouteMembership, RoadSegment, RailSegment, restriction, or operator records.

### Map-not-truth boundary

Rendered lines, symbols, labels, popups, and network paths are carriers.

Tests must reject any runtime path that:

- treats displayed geometry as authoritative because it rendered;
- uses style visibility to substitute for redaction;
- exposes unreleased or correction-pending layers;
- serves exact restricted geometry;
- loses evidence, release, or correction references after selection;
- lets a popup replace the Evidence Drawer for material claims.

[Back to top](#top)

---

<a id="temporal-and-freshness-proof"></a>

## Temporal and freshness proof

Road, rail, restriction, operator, route, and historical claims are time-sensitive in different ways.

### Time dimensions to preserve

Use accepted vocabulary when available. At minimum, do not collapse:

- source publication time;
- observation or record time;
- validity interval;
- event start and end;
- retrieval time;
- processing time;
- release time;
- correction or withdrawal time;
- query time.

### Required temporal cases

| Scenario | Expected posture |
|---|---|
| Operator assignment queried outside its validity interval | `ABSTAIN` or bounded non-current response |
| Restriction event expired before query time | Must not appear current |
| Future-dated status record | Must not appear current |
| Historic route evidence shown as modern alignment | `DENY` or `ABSTAIN` |
| Source is stale for an operationally current question | `ABSTAIN` |
| Release exists but correction supersedes it | Corrected/superseded posture must win |
| Retrieval time is recent but observation is old | Must not relabel evidence as fresh |
| Two sources disagree across time | Preserve conflict; do not flatten into one answer |
| No accepted timezone or interval semantics | `ERROR` or `ABSTAIN`, not silent coercion |

### Freshness field proof

The shared runtime schema requires a `freshness` string but does not enforce a vocabulary.

Before runtime tests depend on exact values:

1. define the controlled vocabulary;
2. bind it to contract and policy;
3. define surface behavior for each value;
4. add positive and invalid fixtures;
5. test unknown values fail closed;
6. test client cache behavior;
7. test correction and withdrawal override freshness labels.

[Back to top](#top)

---

<a id="evidence-citation-and-source-role-proof"></a>

## Evidence, citation, and source-role proof

### Evidence requirement

A material `ANSWER` should resolve support through governed evidence interfaces.

Tests should prove:

```text
EvidenceRef
  -> resolvable EvidenceBundle or accepted evidence record
  -> source identity and role
  -> claim scope
  -> time scope
  -> rights and sensitivity posture
  -> release/correction posture
```

### Outcome-sensitive evidence rules

| Outcome | Evidence expectation |
|---|---|
| `ANSWER` | Evidence refs resolve to support the actual payload and claim scope |
| `ABSTAIN` | Empty or unresolved refs may be allowed when the reason explicitly records insufficient support |
| `DENY` | Refs may be withheld or minimized to avoid leaking restricted existence or location |
| `ERROR` | Diagnostic refs must not expose internal evidence or storage details |

### Citation proof

For public feature, Evidence Drawer, export, story, or Focus Mode surfaces, tests should verify:

- cited source identity matches supporting evidence;
- source role is visible where material;
- citation text does not overstate authority;
- citation links do not bypass the governed interface;
- withdrawn or corrected citations are invalidated;
- generated language cannot invent a citation;
- rendered labels and source properties do not count as citation proof;
- unsupported claim fragments force `ABSTAIN` or narrower scope.

### Source-family conflict

When multiple sources disagree:

- preserve each source identity;
- preserve authority and role;
- preserve time and geometry differences;
- avoid “majority vote” truth;
- use explicit conflict state;
- narrow or abstain where the conflict affects the requested claim;
- never silently upcast an aggregator or convenience source.

### Cultural and historical evidence

Oral history, treaty material, Indigenous mobility/trade evidence, archival maps, and interpretive route claims may require:

- rights review;
- cultural or sovereignty review;
- audience restrictions;
- generalized geometry;
- quotation and citation controls;
- uncertainty and interpretation labels;
- correction and withdrawal paths.

Evidence quality does not override rights or sensitivity.

[Back to top](#top)

---

<a id="rights-sensitivity-and-policy-proof"></a>

## Rights, sensitivity, and policy proof

### Fail-closed triggers

Tests should include public-safe synthetic cases for:

- unresolved rights;
- Indigenous corridor evidence without required review;
- oral-history or treaty evidence with unclear reuse rights;
- critical transport-facility detail;
- private access or parcel-linked information;
- precise cultural or historic-route geometry;
- operationally sensitive rail/facility data;
- source terms prohibiting redistribution;
- missing redaction/generalization receipt;
- missing review record;
- missing release state;
- policy runtime unavailable.

### Most-restrictive posture

A response derived from multiple inputs inherits the most restrictive applicable:

- rights;
- sensitivity;
- access;
- audience;
- release;
- correction;
- withdrawal;
- temporal;
- source-use condition.

Do not average or weaken restrictions.

### Generalized public derivatives

A generalized `ANSWER` is acceptable only when tests prove:

- exact source geometry is not exposed;
- transformation is deterministic where required;
- a transform/aggregation/redaction receipt is linked;
- resulting geometry cannot reasonably reconstruct the restricted source;
- source role and uncertainty remain visible;
- public release and review apply to the derivative;
- exact and generalized objects have distinct identities;
- cache and export paths use the derivative only.

### Denial leakage

A `DENY` response must not reveal:

- exact location;
- restricted object existence when existence itself is sensitive;
- hidden fields;
- private source names where prohibited;
- redaction parameters that aid reversal;
- internal policy expressions;
- reviewer identities when restricted;
- storage paths, credentials, or signed URLs;
- alternate endpoints that bypass the denial.

[Back to top](#top)

---

<a id="trust-membrane-and-public-client-proof"></a>

## Trust membrane and public-client proof

### Forbidden reads

Runtime tests must fail if a public or normal client path reads:

```text
data/raw/
data/work/
data/quarantine/
unpublished release candidates
canonical/internal stores
connector internals
source credentials
graph database internals
vector index internals
direct model runtime output
private review notes
```

### Allowed public path

The intended flow is:

```text
request
  -> governed API / accepted runtime interface
  -> request validation
  -> evidence resolution
  -> policy, rights, sensitivity, and access evaluation
  -> freshness and correction evaluation
  -> release-state check
  -> finite runtime envelope
  -> separately validated public-safe payload
  -> client rendering
```

### Direct-model prohibition

Focus Mode and generated summaries must prove:

- model output is interpretive;
- evidence is retrieved before answer generation;
- policy is evaluated before release;
- unsupported claims are removed or cause abstention;
- provider/model metadata is recorded in the appropriate receipt;
- chain-of-thought is not persisted or exposed;
- direct model calls from public clients are denied;
- model unavailability produces `ERROR` or a bounded non-AI path, not fabricated output.

### Public surface matrix

| Surface | Required runtime proof |
|---|---|
| Feature detail | Envelope, domain payload, evidence, source role, time, release, correction |
| Layer catalog | Released objects only; no restricted autocomplete leakage |
| Map click | Safe feature identity and route to Evidence Drawer |
| Evidence Drawer | Citation/evidence projection, limitations, policy and correction state |
| Focus Mode | Evidence-bounded answer or finite refusal; AI receipt where applicable |
| Search | Released objects only; no restricted autocomplete leakage |
| Export | Same release/policy/citation posture as screen output |
| Screenshot/story | Release/version/citation retained; no hidden sensitive layer |
| Cache | Keyed by release/correction/policy posture; invalidated on withdrawal |
| Error response | Safe reason; no internal implementation leakage |

[Back to top](#top)

---

<a id="required-test-families"></a>

## Required test families

### 1. Route and implementation discovery

- exact route and method are registered;
- route is included in OpenAPI where applicable;
- route does not exist only in documentation;
- wrong method is rejected;
- unknown route is bounded;
- required audience/authentication posture is enforced;
- route changes trigger relevant CI.

### 2. Shared runtime envelope conformance

- all required fields are present;
- `id`, `spec_hash`, and `issued_at` formats validate;
- outcome enum is closed;
- additional properties fail;
- unknown state values fail closed after vocabularies are accepted;
- envelope does not absorb domain payload fields;
- response version incompatibility is visible.

### 3. Domain payload pairing

- domain payload has an accepted contract and schema;
- payload object family is explicit;
- envelope and payload IDs/refs agree;
- `DENY` and `ERROR` carry no protected payload;
- `ABSTAIN` carries no unsupported substantive payload;
- `ANSWER` payload is schema-valid and evidence-supported;
- proposed `RoadsRailDecisionEnvelope` overlap is resolved.

### 4. Road, rail, route, and membership identity

- segment identity differs from route designation;
- route membership differs from segment identity;
- road and rail objects do not cross-type silently;
- operator assignment is time-scoped;
- display names do not become identity;
- deterministic identity survives correction and replay;
- duplicate and ambiguous matches produce bounded outcomes.

### 5. Source-role and authority

- convenience attributes do not become legal status;
- aggregator records do not become primary authority;
- historic evidence does not become current operational truth;
- modeled or inferred routes remain labeled;
- source conflict is visible;
- unsupported authority produces `ABSTAIN` or `DENY`.

### 6. Temporal and freshness behavior

- valid-time boundaries are respected;
- expired events do not appear current;
- future records do not appear current;
- stale operational evidence abstains;
- correction and withdrawal override stale caches;
- timezone/interval errors produce bounded failure;
- query time and evidence time are distinct.

### 7. Evidence and citation closure

- `ANSWER` refs resolve;
- claim scope matches evidence;
- evidence is released/admissible for the audience;
- missing or stale support abstains;
- invalid citation fails;
- generated citations fail;
- corrected/withdrawn support invalidates the answer.

### 8. Policy, rights, access, and sensitivity

- unresolved rights deny;
- cultural/Indigenous corridor review is required where applicable;
- sensitive facility detail denies or restricts;
- private access detail is not exposed;
- missing transform receipt denies generalized output;
- most-restrictive policy propagates;
- policy-runtime failure produces `ERROR`, not `ANSWER`.

### 9. Graph and derived-network proof

- graph edges resolve to source-bound records;
- graph result is labeled derived;
- graph reachability does not imply legal access or current service;
- graph version and release are pinned;
- corrected objects invalidate projections;
- graph internals are inaccessible to public clients;
- rollback restores a known graph projection.

### 10. Layer and renderer proof

- only released layers are returned;
- layer release and rollback refs are present;
- restricted geometry is transformed before tile generation;
- style hiding is not accepted as redaction;
- stale/withdrawn layer is visibly non-current;
- MapLibre output remains a carrier;
- map click routes through governed evidence.

### 11. Evidence Drawer proof

- selected object identity is stable;
- evidence refs resolve;
- source role and limitations appear;
- restricted geometry and hidden fields are absent;
- policy/freshness/correction state is visible;
- popup-only content cannot substitute for evidence;
- missing support yields `ABSTAIN`.

### 12. Focus Mode and AI proof

- question scope is domain-bounded;
- evidence is retrieved before synthesis;
- unsupported claims abstain;
- policy denial stays denial;
- AI receipt is linked where applicable;
- no direct model client is used;
- rendered feature text alone cannot support an answer;
- model/provider failure is bounded.

### 13. Operational-status and official-source safety

- historical/context layer is not presented as live navigation;
- route status carries source and valid time;
- stale status abstains;
- current safety-critical questions route to official sources as required;
- legal access and emergency routing are not inferred;
- disclaimers do not replace denial or abstention.

### 14. Error hygiene and leakage

- malformed request returns bounded `ERROR`;
- schema and contract drift are distinguishable;
- stack traces are absent;
- filesystem and database paths are absent;
- credentials and signed URLs are absent;
- exact sensitive locations are absent;
- error logs remain review-safe;
- repeated errors do not reveal hidden state.

### 15. Correction, withdrawal, supersession, and rollback

- corrected response supersedes prior identity transparently;
- withdrawal blocks current response;
- cache invalidation reaches feature, layer, search, export, story, and AI surfaces;
- rollback target exists;
- rollback restores a known prior release;
- audit refs remain;
- client cannot keep a withdrawn answer as current.

### 16. Hermetic execution

- default suite uses synthetic local fixtures;
- external network is blocked;
- no live source credentials are required;
- time is frozen or controlled;
- randomness is seeded;
- dependencies are pinned;
- zero tests collected fails;
- no `|| true` masks required proof;
- repeated runs are deterministic.

[Back to top](#top)

---

<a id="fixture-contract"></a>

## Fixture contract

### Fixture homes

Use a single reviewed fixture strategy.

Candidate homes:

```text
tests/fixtures/runtime_proof/roads-rail-trade/
fixtures/domains/roads-rail-trade/runtime/
```

The final home is **PROPOSED / NEEDS VERIFICATION**. Do not create both as equal authorities.

### Fixture requirements

Fixtures must be:

- synthetic or explicitly public-safe;
- deterministic;
- compact;
- no-network;
- free of credentials and private endpoints;
- free of exact sensitive cultural, facility, or private-access geometry;
- explicit about object family and source role;
- explicit about observed/valid/release/correction time;
- explicit about expected runtime outcome;
- explicit about expected reason category;
- paired with expected envelope and leakage assertions;
- versioned when shape changes.

### Minimum scenario matrix

| Scenario | Expected runtime outcome | Required assertion |
|---|---|---|
| Released road feature with resolved evidence | `ANSWER` | Payload/evidence/release refs agree |
| Released rail segment but stale operator status | `ABSTAIN` | No current-service claim |
| Missing evidence | `ABSTAIN` | No substantive fallback |
| Unreleased layer | `DENY` | No layer payload or URL |
| Cultural corridor without review | `DENY` | No exact geometry or reconstructive hint |
| Historic route at modern precision | `DENY` or generalized `ANSWER` | Transform receipt required for derivative |
| Route membership/source-role conflict | `ABSTAIN`, `DENY`, or bounded `ERROR` per accepted policy | No silent upcast |
| Malformed request | `ERROR` | Safe diagnostic only |
| Policy runtime unavailable | `ERROR` | No permissive fallback |
| Correction pending | finite non-current outcome | Prior response not served as current |
| Withdrawn release | `DENY` or bounded non-current response | Cache invalidated |
| Missing rollback target | `DENY` or `ERROR` | Promotion/public response blocked |
| Direct internal-store request | `DENY` | No path existence disclosure |
| Direct model request | `DENY` or `ERROR` | No model output |
| Expired restriction event | `ABSTAIN` or historical `ANSWER` | Not current |
| Graph reachability request framed as legal access | `ABSTAIN` or `DENY` | No legal-access inference |

### Forbidden fixture content

Do not use:

- real private access records;
- exact sensitive facilities;
- exact Indigenous/cultural corridor traces;
- live rail movement or dispatch information;
- unreleased source exports;
- production database identifiers;
- real credentials;
- signed URLs;
- private review notes;
- real legal-status determinations;
- real emergency-routing scenarios that could be mistaken for advice.

### Fixture anti-authority rule

A fixture proves expected behavior against a synthetic case. It does not prove:

- the real-world claim;
- source authority;
- evidence closure;
- current status;
- release approval;
- operational safety;
- legal access;
- production readiness.

[Back to top](#top)

---

<a id="ci-and-gate-acceptance"></a>

## CI and gate acceptance

### Current domain workflow

The current Roads–Rail–Trade workflow is an echo-only scaffold.

It does not currently:

- install a test environment;
- collect runtime-proof tests;
- validate shared runtime envelopes;
- validate domain payloads;
- call governed API routes;
- resolve EvidenceRefs;
- evaluate policy;
- assert leakage behavior;
- verify correction/rollback;
- emit a governed proof;
- block promotion based on runtime-proof failure.

### Required CI trigger coverage

A future runtime-proof workflow should watch, at minimum:

```text
tests/runtime_proof/domains/roads-rail-trade/**
tests/runtime_proof/**
tests/fixtures/**roads*rail*trade**
fixtures/domains/roads-rail-trade/**
apps/governed-api/**
packages/domains/roads-rail-trade/**
contracts/domains/roads-rail-trade/**
contracts/runtime/**
schemas/contracts/v1/runtime/**
schemas/contracts/v1/domains/roads-rail-trade/**
policy/domains/roads-rail-trade/**
policy/runtime/**
release/**
tools/validators/**
.github/workflows/<accepted-workflow>
```

Refine path filters only after the implementation graph is verified.

### Required CI behavior

A trusted gate should:

1. install from pinned dependency manifests;
2. run shared runtime schema fixtures;
3. run domain contract/schema fixtures;
4. run executable runtime-proof tests;
5. run route/API tests against a local deterministic app;
6. block external network;
7. fail on zero collected tests;
8. exercise every finite outcome;
9. exercise leakage assertions;
10. exercise correction, withdrawal, and rollback;
11. upload bounded QA reports;
12. preserve the primary failure;
13. emit stable reason codes;
14. produce no release approval;
15. expose the tested commit, spec hash, fixture digest, and rollback target.

### Stub-workflow rule

```text
workflow file exists
  != tests execute

echo job succeeds
  != runtime proof passes

schema fixture passes
  != domain route works

route works
  != evidence/policy/release gates close

all tests pass
  != release approval
```

### No ignored failures

Required proof commands must not use:

```text
|| true
continue-on-error: true
allowed failure without tracked expiry
empty test selection
catch-all success after exception
```

Diagnostic collection may run after failure, but it must not change the primary failure outcome.

### CI evidence hierarchy

```text
workflow present
  < workflow started
  < tests collected
  < positive and negative cases executed
  < all finite outcomes verified
  < leakage assertions verified
  < repeated deterministic pass
  < accepted promotion-gate integration
```

Never claim a higher level from a lower one.

[Back to top](#top)

---

<a id="test-authoring-contract"></a>

## Test authoring contract

Every executable test added to this lane should identify:

| Field | Requirement |
|---|---|
| Test ID | Stable and reviewable |
| Surface | Feature, layer, Evidence Drawer, Focus Mode, status, graph, correction, or other accepted surface |
| Route/interface | Exact verified implementation entry point |
| Object family | Explicit Roads–Rail–Trade or shared object |
| Fixture ID | Stable synthetic fixture reference |
| Expected outcome | One of `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Expected reason | Accepted reason code/category |
| Evidence expectation | Resolved, empty, withheld, or error posture |
| Policy expectation | Allowed, denied, restricted, or runtime-error posture |
| Freshness expectation | Accepted controlled value |
| Correction expectation | Accepted controlled value |
| Payload expectation | Present/absent and paired schema |
| Leakage assertions | Fields, paths, geometry, logs, URLs, caches, side channels |
| Release expectation | Released/current/corrected/withdrawn/blocked |
| Rollback target | Required when public state is under proof |
| Network posture | Hermetic by default |
| Cleanup | No retained sensitive or trust-bearing test output |

### Test naming

Prefer names that expose behavior:

```text
test_feature_answer_requires_resolved_evidence
test_stale_operator_status_abstains
test_unreleased_layer_denies_without_payload
test_cultural_corridor_denial_leaks_no_geometry
test_graph_reachability_does_not_imply_legal_access
test_withdrawn_release_invalidates_cached_feature
test_malformed_domain_payload_returns_safe_error
```

Avoid names that imply implementation not verified:

```text
test_production_route
test_canonical_transport_api
test_release_approved
test_live_status
```

### Assertion order

For a runtime response, assert in this order:

1. transport/HTTP behavior if applicable;
2. envelope schema;
3. exactly one finite outcome;
4. reason code;
5. payload presence/absence;
6. payload schema;
7. evidence refs;
8. policy/freshness/correction state;
9. release and rollback refs;
10. leakage absence;
11. cache/public-surface behavior;
12. receipt/report linkage.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Documentation checks for this README

- one rendered H1;
- valid heading progression;
- balanced code fences;
- valid internal navigation anchors;
- no duplicate rendered headings;
- no trailing whitespace;
- no tabs;
- no credentials, private keys, or secret-like values;
- one-file change scope;
- exact remote blob readback.

### Grounded commands after executable tests exist

Shared runtime envelope shape:

```bash
python tools/validators/validate_runtime_response_envelope.py --fixtures
```

Shared contract schema harness:

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
```

Target runtime-proof suite:

```bash
python -m pytest -q tests/runtime_proof/domains/roads-rail-trade
```

Current status of the target command:

```text
NEEDS VERIFICATION — bounded search did not surface an executable test module.
```

### Required negative validation

A credible suite must fail when:

- no tests are collected;
- an unknown outcome appears;
- a required envelope field is missing;
- a domain payload is injected into the closed envelope;
- evidence is missing for a substantive answer;
- policy denial carries a payload;
- stale status is called current;
- a graph path is called legal access;
- an unreleased layer is served;
- sensitive geometry appears in body, logs, cache, export, map, or error;
- correction/withdrawal fails to invalidate prior state;
- rollback is missing;
- public client reads an internal store;
- direct model output becomes an answer.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This runtime-proof lane is implementation-ready only when all applicable items are satisfied.

### Placement and authority completion

- [ ] Owners are assigned.
- [ ] API documentation home collision is resolved.
- [ ] Domain schema slug/home conflict is resolved or explicitly profiled.
- [ ] Runtime-proof lane remains distinct from broader domain tests.
- [ ] Fixture home is accepted.
- [ ] No parallel route, schema, fixture, or test authority remains.

### Runtime implementation

- [ ] Exact governed API routes/interfaces are verified.
- [ ] Request and response composition is documented.
- [ ] Shared envelope usage is explicit.
- [ ] Domain payload contract and schema are accepted.
- [ ] `RoadsRailDecisionEnvelope` overlap is resolved.
- [ ] Public clients use governed interfaces only.

### Test completion

- [ ] Executable tests exist in this lane.
- [ ] Every material surface has positive and negative cases.
- [ ] `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are exercised.
- [ ] Zero-test collection fails.
- [ ] Source-role, time, graph, map, AI, operational-status, rights, and sensitivity cases exist.
- [ ] Leakage is asserted across bodies, logs, headers, caches, maps, exports, search, screenshots, and AI surfaces.
- [ ] Correction, withdrawal, supersession, and rollback are exercised.

### Schemas, policy, and evidence

- [ ] Shared runtime envelope schema and fixtures pass.
- [ ] Domain payload schemas are field-complete.
- [ ] Controlled vocabularies for policy/freshness/correction are accepted.
- [ ] EvidenceRefs resolve in `ANSWER` cases.
- [ ] Policy runtime is exercised.
- [ ] Rights and sensitivity obligations are enforced.
- [ ] Domain source-role and temporal semantics are tested.

### CI and proof

- [ ] Domain workflow runs real commands instead of echo stubs.
- [ ] Dedicated runtime-proof suite runs on relevant changes.
- [ ] Default execution is hermetic and no-network.
- [ ] Required failures cannot be ignored.
- [ ] CI reports test counts and scenario counts.
- [ ] Repeated deterministic runs are demonstrated.
- [ ] Reports identify commit, spec hash, fixtures, environment, and rollback target.
- [ ] Test success is not converted into release approval.

### Release and correction

- [ ] Release state is verified before `ANSWER`.
- [ ] Corrected/withdrawn/superseded state reaches clients and caches.
- [ ] Rollback target is tested.
- [ ] Public layers, search, export, story, and AI surfaces invalidate stale state.
- [ ] Operationally current questions use accepted official-source behavior.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Phase 1 — Inventory and placement

1. recursively inventory this target;
2. inventory Roads–Rail–Trade API implementation;
3. inventory all Roads–Rail–Trade runtime and map/API tests;
4. resolve API documentation collision;
5. resolve domain payload schema home and profile;
6. select one fixture home;
7. record owners and reviewers.

### Phase 2 — Shared envelope baseline

1. run existing shared envelope fixtures;
2. add outcome-specific shared fixtures;
3. accept controlled state vocabularies or keep tests semantic and fail-closed;
4. document envelope/payload composition;
5. add no-payload-on-deny/error assertions.

### Phase 3 — Minimal domain payload

1. choose one low-risk released feature/detail object;
2. pair semantic contract and schema;
3. add synthetic positive and invalid fixtures;
4. implement a local governed interface;
5. return shared envelope plus explicit domain payload;
6. add evidence and release refs.

### Phase 4 — Four finite outcomes

Implement one deterministic case each:

```text
ANSWER   released, supported, public-safe feature
ABSTAIN  missing or stale support
DENY     policy/rights/release prohibition
ERROR    malformed request or dependency failure
```

### Phase 5 — Domain anti-collapse

Add tests for:

- route membership versus segment identity;
- historical versus current geometry;
- operator assignment/status time;
- graph reachability versus access;
- source-role conflicts;
- map/rendered text versus evidence;
- operational/current-status framing.

### Phase 6 — Sensitive and cross-lane cases

Add public-safe synthetic tests for:

- cultural/Indigenous corridor review;
- critical facility detail;
- private access context;
- generalized geometry and receipt;
- Hydrology/Settlements/Hazards cross-lane non-ownership;
- rights and source-use restrictions.

### Phase 7 — Correction and rollback

1. issue a synthetic correction;
2. supersede or withdraw a prior response;
3. invalidate cache/search/map/export/AI projections;
4. verify prior identity remains auditable;
5. execute rollback to a known safe state.

### Phase 8 — CI admission

1. replace echo-only domain workflow steps;
2. run shared and domain runtime tests;
3. enforce no-network;
4. fail on zero tests;
5. upload bounded QA reports;
6. repeat until deterministic;
7. connect to promotion only after governance review.

### Stop conditions

Stop and mark the work `NEEDS VERIFICATION` when:

- exact routes cannot be found;
- domain payload meaning is unresolved;
- schema homes conflict;
- evidence cannot resolve;
- rights or sensitivity are unclear;
- source roles conflict materially;
- operational freshness is unsupported;
- correction or rollback cannot be demonstrated;
- test execution requires live credentials;
- a public-safe fixture cannot be created;
- proposed architecture is being treated as accepted fact.

[Back to top](#top)

---

<a id="correction-and-rollback"></a>

## Correction and rollback

### Documentation correction

When this README overstates repository behavior:

1. narrow the claim;
2. identify the incorrect evidence basis;
3. update the status table and metadata;
4. link the correcting implementation or decision;
5. preserve the prior blob and PR history;
6. do not rewrite shared history.

### Test correction

When a test expectation is wrong:

1. hold promotion decisions depending on it;
2. identify affected surfaces and releases;
3. correct contract/schema/policy first when the test exposed real drift;
4. correct the test only when the expectation was wrong;
5. add a regression case;
6. rerun the complete finite-outcome matrix;
7. record correction and remaining limits.

### Fixture correction

When a fixture is unsafe or misleading:

1. remove it from active test use;
2. quarantine real or sensitive material through the governed lifecycle;
3. replace it with a synthetic public-safe fixture;
4. invalidate derived baselines and reports;
5. review caches and artifacts;
6. preserve an audit note without retaining protected data.

### Runtime correction

When a released response is wrong, stale, overprecise, or unsafe:

1. stop serving it as current;
2. issue or link correction/withdrawal state;
3. invalidate feature, layer, search, export, story, cache, and AI projections;
4. rerun evidence, policy, release, and runtime proof;
5. supersede the prior envelope;
6. retain lineage and rollback target.

### Safety rollback

Rollback is required when a change:

- enables an internal-store path;
- turns a graph or map into truth;
- weakens source-role or temporal checks;
- serves unreleased content;
- leaks sensitive geometry or access detail;
- converts operational uncertainty into advice;
- hides denial as style/filter behavior;
- removes evidence or citation requirements;
- bypasses policy;
- masks errors;
- loses correction or rollback linkage;
- makes an echo-only or empty suite appear green.

Before merge, rollback is leaving the review unmerged or restoring the prior blob through a transparent commit.

After merge, rollback is a normal revert commit or revert PR. Do not reset or rewrite shared history.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

### Placement and authority backlog

- [ ] Assign owners and CODEOWNERS.
- [ ] Resolve `API_CONTRACTS.md` versus `api-contracts/README.md`.
- [ ] Resolve `roads-rail-trade` versus `transport` schema naming.
- [ ] Decide domain payload versus envelope profile.
- [ ] Confirm fixture home.
- [ ] Inventory overlap with `tests/domains/roads-rail-trade/`.

### Runtime and API

- [ ] Find actual route/controller/module inventory.
- [ ] Inspect OpenAPI and route registration.
- [ ] Confirm authentication and audience classes.
- [ ] Confirm request schemas.
- [ ] Confirm response composition.
- [ ] Confirm cache behavior.
- [ ] Confirm client consumers.
- [ ] Confirm official-source redirect behavior for current operational questions.

### Contracts and schemas

- [ ] Create or verify domain feature/detail response contract.
- [ ] Create or verify domain payload schema.
- [ ] Resolve `RoadsRailDecisionEnvelope`.
- [ ] Add route membership and temporal schemas.
- [ ] Add controlled state vocabularies.
- [ ] Add reason-code registry.
- [ ] Add positive and negative fixtures.

### Evidence and policy

- [ ] Verify EvidenceRef resolver.
- [ ] Verify citation validation.
- [ ] Verify source-role registry bindings.
- [ ] Verify cultural/Indigenous review path.
- [ ] Verify critical-facility sensitivity rules.
- [ ] Verify rights and redistribution rules.
- [ ] Verify generalization/redaction receipts.
- [ ] Verify policy runtime failure behavior.

### Test backlog

- [ ] Add executable runtime-proof modules.
- [ ] Add four-outcome baseline.
- [ ] Add no-payload-on-deny/error tests.
- [ ] Add source-role conflict tests.
- [ ] Add temporal misalignment tests.
- [ ] Add graph-not-access tests.
- [ ] Add operational-status safety tests.
- [ ] Add Evidence Drawer tests.
- [ ] Add Focus Mode/AI tests.
- [ ] Add correction, withdrawal, cache, and rollback tests.
- [ ] Add leakage tests.
- [ ] Add no-network enforcement.

### CI

- [ ] Replace domain workflow echo steps.
- [ ] Add runtime-proof path filters.
- [ ] Run shared runtime schema fixtures.
- [ ] Run target pytest suite.
- [ ] Run local governed API integration tests.
- [ ] Fail on zero tests.
- [ ] Report collected tests and scenarios.
- [ ] Preserve primary failure.
- [ ] Verify repeated deterministic runs.
- [ ] Connect to promotion only after review.

### Release and operations

- [ ] Verify release records for domain payloads/layers.
- [ ] Verify correction and withdrawal propagation.
- [ ] Verify cache invalidation.
- [ ] Verify rollback execution.
- [ ] Verify public-client stale-state behavior.
- [ ] Verify production behavior separately from fixture proof.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | CONFIRMED | Existing lane intent and prior blob | Mostly aspirational; executable state outdated |
| `tests/runtime_proof/README.md` | CONFIRMED draft | Parent finite-outcome and trust-membrane purpose | Does not prove runtime implementation |
| `tests/runtime_proof/domains/README.md` | CONFIRMED draft | Domain child placement and current index | Child completeness and execution unverified |
| `tests/domains/roads-rail-trade/README.md` | CONFIRMED draft | Broader domain test families and anti-collapse rules | Executable depth unverified |
| Roads–Rail–Trade API docs | CONFIRMED draft / conflicted home | Intended surfaces, outcomes, domain-specific deny/abstain drivers | Routes and DTO implementation are proposed/unknown |
| Roads–Rail–Trade schema index | CONFIRMED draft | Current schema home proposal and no concrete domain schema confirmed | Does not establish domain payload shape |
| Shared RuntimeResponseEnvelope contract | CONFIRMED paired / PROPOSED | Semantic meaning and field surface | Does not prove domain route or runtime behavior |
| Shared RuntimeResponseEnvelope schema | CONFIRMED concrete / PROPOSED | Required fields, closed enum, no additional properties | No domain payload or controlled state vocabularies |
| Shared validator wrapper | CONFIRMED | Schema fixture validation entry point | Does not resolve evidence, policy, release, or client behavior |
| Shared valid fixture README | CONFIRMED | One minimal ABSTAIN fixture and narrow shape coverage | Not Roads–Rail–Trade runtime proof |
| Domain workflow | CONFIRMED echo-only scaffold | Current CI maturity boundary | Provides no executable proof |
| Bounded API code search | No Roads–Rail–Trade route/controller result surfaced | Supports route implementation uncertainty | Search-limited; recursive repo inspection remains required |
| Current-session execution | NOT RUN | Documentation-only API update | No test, validator, route, workflow, or production pass claim |

[Back to top](#top)
