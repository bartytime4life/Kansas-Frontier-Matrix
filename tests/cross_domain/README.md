<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-cross-domain-readme
title: tests/cross_domain/ — Cross-Domain Enforceability Test Routing and Placement Guardrail
type: readme; directory-readme; cross-domain-test-parent-index; placement-guardrail; migration-index
version: v0.2
status: draft; surviving-cross-domain-parent; placement-conflicted; child-lane-present; executable-depth-unknown; no-parallel-authority; NEEDS VERIFICATION
policy_label: public-doc; restricted-review-when-child-sensitivity-requires
owners: OWNER_TBD — QA steward · Cross-domain architecture steward · Domain stewards for affected children · Fixture steward · Validation steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — placeholder expanded on 2026-07-05
updated: 2026-07-16
current_path: tests/cross_domain/README.md
truth_posture: CONFIRMED target README and prior blob, tests responsibility root, Domain Placement Law, cross-domain placement guidance, explicit deletion of tests/cross-domain/, surviving tests/cross_domain parent and fauna_habitat child, merged child README, and bounded absence of other surfaced children or executable files at the pinned snapshot / CONFLICTED intermediate cross_domain segment and topic naming versus tests/<topic>/ doctrine, overlapping domain-owned cross-domain test and fixture lanes, and exact long-term parent role / UNKNOWN exhaustive recursive inventory, inbound references, executable test modules, fixture payloads, accepted child registry, CI callers, pass state, production enforcement, and migration consumers / NEEDS VERIFICATION naming ADR, child registration rule, deduplication plan, fixture normalization, CI wiring, correction propagation, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 01026cd58b1e687c4f8fa3363229b9857613102b
  prior_blob: 9c6c19aaa3f0bde6dcec822c315d5fb97cc134d3
related:
  - ../README.md
  - ./fauna_habitat/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/cross-domain/multi-domain-placement.md
  - ../../docs/architecture/domain-placement-law.md
  - ../../docs/architecture/cross-domain/README.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../contracts/cross_domain/README.md
  - ../../schemas/contracts/v1/relations/README.md
  - ../../fixtures/README.md
  - ../../tools/validators/README.md
  - ../../pipelines/proofs/README.md
  - ../../release/README.md
tags: [kfm, tests, cross-domain, cross-domain-placement, enforceability, ownership, source-role, evidence, policy, sensitivity, lifecycle, release, correction, rollback, migration, no-parallel-authority]
notes:
  - "v0.2 replaces a stale compatibility index that pointed to a deleted hyphenated tree."
  - "The underscore-form parent survives in the repository, but its long-term naming and nesting remain unresolved."
  - "The only surfaced child at the pinned snapshot is fauna_habitat/, whose README is itself placement-conflicted and README-only."
  - "This revision changes documentation only and creates, moves, deletes, or activates no test, fixture, schema, contract, validator, workflow, pipeline, data, receipt, proof, policy, or release artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/cross_domain/` — Cross-Domain Enforceability Test Routing and Placement Guardrail

> **Purpose.** Route tests that genuinely span two or more KFM domains into one inspectable, non-domain-owned proof surface while preserving each domain's authority, source roles, evidence support, sensitivity posture, lifecycle state, release state, correction path, and rollback target.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="Children: one surfaced" src="https://img.shields.io/badge/children-one__surfaced-informational">
  <img alt="Implementation: needs verification" src="https://img.shields.io/badge/implementation-NEEDS__VERIFICATION-red">
</p>

> [!IMPORTANT]
> `tests/cross_domain/` is an **enforceability-proof routing lane**. It is not a new domain, a fixture authority, a contract or schema home, policy authority, validator implementation root, proof or receipt store, pipeline, runtime surface, release authority, or publication surface.

> [!WARNING]
> The repository explicitly deleted the duplicate `tests/cross-domain/` tree. Do not recreate that tree, restore its former children, or copy tests into both spellings. The surviving underscore path is current repository evidence, but deletion alone does not settle the architecture convention. Cross-domain placement doctrine still describes `tests/<topic>/...` as the general form and leaves the exact namespace open.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Inventory](#current-inventory) · [Parent responsibilities](#parent-lane-responsibilities) · [Cross-domain invariant](#cross-domain-test-invariant) · [Coverage](#required-cross-domain-test-families) · [Outcomes](#finite-system-outcomes-and-test-results) · [Fixtures](#fixture-and-test-data-boundary) · [CI](#ci-and-proof-boundary) · [Child registration](#child-lane-registration-contract) · [Migration](#placement-migration-and-deduplication) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/cross_domain/README.md` | **CONFIRMED** | Parent exists; prior blob is pinned in metadata. |
| `tests/cross_domain/fauna_habitat/README.md` | **CONFIRMED / merged v0.2** | One detailed child lane exists and is marked placement-conflicted, README-only, and sensitivity-critical. |
| Other surfaced children under `tests/cross_domain/` | **NOT SURFACED in bounded search** | Do not invent additional child inventory. |
| Direct executable tests under this parent | **NOT SURFACED in bounded search** | README presence does not establish executable proof. |
| `tests/cross-domain/` | **CONFIRMED deleted** | Former hyphenated parent and Habitat–Fauna child were removed from `main`. |
| `tests/` | **CONFIRMED canonical responsibility root** | Tests own enforceability proof, not truth or policy. |
| Domain Placement Law | **CONFIRMED rule** | Multi-domain files use the lowest common responsibility root without assigning ownership to one participating domain. |
| Cross-domain test layout | **OPEN / CONFLICTED** | `tests/<topic>/...` is the general doctrinal form; `tests/cross_domain/<topic>/...` is the surviving repository form. |
| Cross-domain child registry | **NOT CONFIRMED** | This README is the human index; no accepted machine registry was surfaced. |
| Dedicated cross-domain workflow | **NOT SURFACED in bounded search** | Do not claim this parent or its child runs in CI. |
| Current pass state | **UNKNOWN** | Repository inspection is not test execution. |
| Production enforcement | **UNKNOWN** | Documentation and test names do not prove deployed behavior. |

**Authority of this README:** parent-lane routing, placement warnings, child-index expectations, cross-domain proof invariants, review burden, migration rules, correction guidance, and rollback guidance.

The following outrank this README for their own responsibilities:

- accepted Directory Rules and ADRs;
- domain semantic contracts;
- machine schemas;
- policy bundles and policy decisions;
- executable tests and validators;
- fixture payloads;
- CI definitions and logs;
- emitted receipts and proofs;
- release, correction, withdrawal, and rollback records;
- steward decisions.

### Truth labels used here

| Label | Meaning in this document |
|---|---|
| **CONFIRMED** | Verified from current repository files, commit history, or merged pull-request evidence. |
| **PROPOSED** | A design, path, template, or procedure not established as current implementation. |
| **CONFLICTED** | Current repository evidence and placement doctrine do not resolve to one accepted answer. |
| **NEEDS VERIFICATION** | Checkable, but not sufficiently verified for promotion or reliance. |
| **UNKNOWN** | Not established by the inspected repository evidence. |

---

## Placement and authority

### Directory Rules basis

KFM places a file by its primary responsibility:

```text
tests/                            enforceability proof
fixtures/                         deterministic test examples
contracts/                        semantic meaning
schemas/                          machine-checkable shape
policy/                           allow / deny / restrict / abstain
tools/validators/                 reusable validation implementation
pipelines/                        executable orchestration
data/proofs/ and data/receipts/   emitted proof and audit records
release/                          promotion, correction, withdrawal, rollback
```

A cross-domain test remains under `tests/` because its purpose is proof. It does not move to a domain merely because one domain supplies more inputs.

The multi-domain rule requires:

1. identify that the test genuinely spans two or more domains;
2. choose the lowest common responsibility root;
3. avoid assigning the file to one participating domain;
4. use a stable cross-domain topic segment;
5. cross-link the participating domain lanes;
6. keep meaning, shape, policy, fixtures, validators, pipelines, data, and release records in their own roots.

### Current placement conflict

Current repository form:

```text
tests/cross_domain/<topic>/
```

General form in cross-domain placement doctrine:

```text
tests/<topic>/
```

Open alternative named in architecture guidance:

```text
tests/cross/<topic>/
```

Deleted duplicate form:

```text
tests/cross-domain/<topic>/       # do not recreate
```

The repository currently supports only this bounded conclusion:

- `tests/cross_domain/` is the surviving parent path;
- the parent is correctly inside `tests/`;
- the intermediate `cross_domain/` namespace is not yet accepted by a naming ADR;
- child topic naming and ordering are not yet normalized;
- the former hyphenated tree is retired and must not return without an explicit migration decision;
- new sibling paths should not be created casually while the convention is unresolved.

### Current path class

| Field | Value |
|---|---|
| Primary responsibility | Cross-domain enforceability proof routing |
| Owning root | `tests/` |
| Current repository class | Surviving parent index |
| Architectural class | `CONFLICTED / NEEDS VERIFICATION` |
| Implementation maturity | README-oriented; executable depth unknown |
| Write posture | Parent README, child indexes, migration notes, and executable tests only after placement review |
| Duplicate posture | One implementation lane per test concern |
| Public-data posture | Synthetic, redacted, generalized, deterministic, and no-network by default |
| Promotion posture | Test failure blocks promotion where the tested trust invariant is material |
| Required reviewers | QA plus all affected domain and policy/sensitivity/release stewards |

### Parent is not a domain

`cross_domain` is a routing namespace, not a KFM domain.

It must not receive:

- domain source registries;
- domain object families;
- domain contracts or schemas;
- canonical domain data;
- domain release candidates;
- domain-specific package or pipeline implementations;
- a merged "cross-domain truth" object family merely for convenience.

Each participating domain continues to own its facts. The cross-domain test proves that composition preserves those ownership boundaries.

---

## Current inventory

### Surfaced parent and child lanes

| Path | Current role | Status |
|---|---|---|
| `tests/cross_domain/README.md` | Parent routing, placement, and migration guardrail | **CONFIRMED target** |
| `tests/cross_domain/fauna_habitat/README.md` | Fauna × Habitat ownership, relation, sensitivity, geoprivacy, public-surface, correction, and rollback test contract | **CONFIRMED / README-only in bounded evidence** |

No other child lane is claimed here.

### Retired duplicate paths

The following paths were explicitly removed from `main`:

```text
tests/cross-domain/README.md
tests/cross-domain/habitat-fauna/README.md
```

Retirement implications:

- do not link new documentation to those paths;
- do not add redirects by recreating the deleted folders;
- do not copy tests from the underscore tree into the former hyphenated tree;
- update stale references through normal review;
- use commit history for lineage rather than restoring duplicate files.

### Known overlapping lanes outside this parent

| Surface | Why it overlaps | Required posture |
|---|---|---|
| `tests/domains/habitat/thin-slice.habitat-fauna.test/` | Documents Habitat–Fauna thin-slice test intent under Habitat | Treat as overlapping and placement-sensitive; do not duplicate neutral cross-domain assertions. |
| `fixtures/domains/habitat/habitat_fauna_thin_slice/` | Documents synthetic cross-domain fixture intent under Habitat | Fixture placement is conflicted; inventory before moving or copying. |
| `pipelines/proofs/habitat_fauna_thin_slice/` | Describes executable proof orchestration | System under test; not a test or fixture authority. |
| `tools/validators/habitat-fauna/` | Describes broad cross-domain validation | Validator home; executable depth remains unverified. |
| `tools/validators/geoprivacy/habitat-fauna/` | Describes sensitive-location validation | Geoprivacy validator home; not test or policy authority. |
| `schemas/contracts/v1/relations/habitat_fauna/` | Relation-schema guardrail | Machine-shape concern; currently README-oriented. |
| `schemas/contracts/v1/joins/habitat-fauna-join.schema.json` | Proposed permissive join scaffold | Not an accepted relation contract or active schema profile. |

The parent must index these relationships without absorbing their responsibilities.

### Inventory limitations

This README does not prove:

- a recursive file inventory beyond bounded search;
- that no ignored or generated files exist locally;
- executable test modules;
- fixture payload completeness;
- test collection;
- validator execution;
- CI wiring;
- current pass rates;
- release-gate integration;
- deployment behavior.

---

## Parent-lane responsibilities

`tests/cross_domain/` should do five things well.

### 1. Route cross-domain tests

A child belongs here only when its core assertion requires two or more domains and cannot truthfully be owned by one domain.

Examples:

- relation ownership across Habitat and Fauna;
- a Hydrology–Hazards regulatory-versus-observed boundary;
- Agriculture–Atmosphere smoke impact joins;
- Soil–Agriculture interpretation boundaries;
- Roads–Settlements network and infrastructure relations.

These are examples of concerns, not confirmed child paths.

### 2. Prevent parallel authority

For each concern, the parent must help reviewers identify:

- the one current test implementation lane;
- overlapping domain-owned test lanes;
- fixture homes;
- validators;
- proof pipelines;
- contracts and schemas;
- policy families;
- CI callers;
- migration status.

A child README must not imply that a duplicate path is harmless because both contain tests.

### 3. Preserve responsibility-root separation

Tests may consume or assert objects from other roots, but they do not own them.

| Concern | Owning root |
|---|---|
| Object meaning | `contracts/` |
| Machine shape | `schemas/` |
| Policy and sensitivity decisions | `policy/` |
| Deterministic examples | `fixtures/` |
| Validator implementation | `tools/validators/` |
| Proof orchestration | `pipelines/` |
| Lifecycle records | `data/` |
| Emitted receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release, correction, withdrawal, rollback | `release/` |
| Enforceability proof | `tests/` |

### 4. Maintain a truthful child index

Every child row should identify:

- scope;
- participating domains;
- implementation maturity;
- sensitivity class;
- current test command, if verified;
- fixture home;
- validator home;
- CI caller;
- placement status;
- supersession or migration state.

Unknown fields stay `UNKNOWN` or `NEEDS VERIFICATION`.

### 5. Make correction and migration visible

When paths, contracts, policies, fixtures, or release semantics change, the parent should record:

- which child is affected;
- whether tests are stale;
- whether CI still points to the correct path;
- whether snapshots or expected outputs require regeneration;
- whether public-surface leakage tests need replay;
- the rollback target.

---

## What belongs here

Appropriate contents include:

- this parent README;
- child directories for genuinely cross-domain tests after placement review;
- executable cross-domain test modules;
- test-only helpers local to one cross-domain suite when they are not reusable validators;
- child README files;
- migration and deduplication notes;
- test-only snapshot expectations when the accepted fixture rule permits them;
- pointers to domain contracts, schemas, policy, fixtures, validators, proof pipelines, receipts, proofs, release records, and correction records;
- no-network integration assertions;
- ownership, source-role, evidence, sensitivity, lifecycle, release, correction, rollback, and public-surface tests.

## What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain implementation code | accepted domain package, app, connector, or pipeline root |
| Cross-domain semantic contracts | accepted `contracts/<topic>/` or other reviewed contract home |
| Cross-domain schemas | accepted `schemas/contracts/v1/<topic>/` or reviewed schema home |
| Policy rules or geoprivacy parameters | `policy/` |
| Reusable validator implementations | `tools/validators/<topic>/` |
| Executable proof orchestration | `pipelines/proofs/<topic>/` |
| General fixture libraries | `fixtures/<topic>/` or reviewed fixture home |
| Real source records or lifecycle data | governed `data/` lifecycle roots |
| EvidenceBundles, receipts, or proof packs | governed proof and receipt roots |
| Release manifests, corrections, withdrawals, rollback cards | `release/` |
| Public API, UI, map, tile, search, graph, export, or AI implementation | governed app/package roots |
| Exact sensitive geometry or protected identifiers | never in default tests; use synthetic or public-safe derivatives |
| Live credentials, source tokens, private URLs, model-provider secrets | never in repository tests |
| Generated summaries treated as evidence or expected truth | nowhere |

### No hidden authority in helpers

A test helper under this parent must not quietly:

- make policy decisions;
- mint EvidenceBundles;
- rewrite source roles;
- normalize away domain ownership;
- choose a release state;
- publish a fixture;
- create a canonical relation identity;
- define geoprivacy thresholds;
- transform sensitive geometry without a governed policy/receipt path.

Reusable trust-bearing helper logic should graduate to its owning implementation root and be tested from here.

---

## Cross-domain test invariant

> **Composition must not collapse authority.**

A cross-domain test should demonstrate that the relation between domain-owned objects preserves all material governance dimensions.

| Dimension | Required behavior |
|---|---|
| Domain ownership | Each fact remains owned by its source domain. |
| Relation identity | The relation is a separate object or assertion, not a copied domain record. |
| Source role | Authority, observation, context, model, aggregate, regulatory, and synthetic roles remain distinguishable. |
| Evidence | Claim-bearing relations resolve EvidenceRef to EvidenceBundle or produce a finite non-answer. |
| Rights | Rights and redistribution posture propagate to the composed product. |
| Sensitivity | The resulting product inherits the most restrictive applicable posture. |
| Time | Observation, model, validity, release, and correction times remain explicit where material. |
| Lifecycle | RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED states are not skipped or collapsed. |
| Policy | Missing or denied policy state fails closed. |
| Review | Required steward review remains separate from automated validation. |
| Release | Validation and test success do not become release approval. |
| Correction | Corrected or withdrawn inputs invalidate or re-evaluate derived relations. |
| Rollback | Public and internal derivatives have explicit rollback targets where release-significant. |
| Public surfaces | API, UI, tiles, search, graph, exports, caches, embeddings, and AI summaries cannot bypass the trust membrane. |

### Anti-collapse examples

The following must not be treated as valid transformations:

```text
domain A context -> domain B fact
domain B occurrence -> domain A canonical object
modeled suitability -> observed presence
aggregate range -> exact occurrence
regulatory designation -> observation
join result -> EvidenceBundle
schema-valid relation -> policy-approved relation
validator pass -> proof closure
test pass -> release approval
redacted fixture -> unrestricted source
graph edge -> canonical truth
AI summary -> evidence
public tile -> release record
```

### Ambiguity is first-class

Many-to-many and spatial-overlap relations must not be flattened merely because a join is possible.

Tests should require one of:

- deterministic disambiguation supported by evidence;
- explicit candidate state;
- multiple relation records with confidence and provenance;
- `ABSTAIN`;
- `DENY` where ambiguity creates sensitivity or rights risk;
- `ERROR` where the relation cannot be validated safely.

---

## Required cross-domain test families

Every implemented child should select the applicable families and document omissions.

### Placement and ownership

- parent and child paths match the accepted convention;
- no duplicate test implementation exists;
- no participating domain is silently chosen as owner;
- each input object retains its owning domain;
- the relation remains separate from both inputs.

### Identity and relation direction

- deterministic relation identity is stable for the same governed inputs;
- input order and relation direction are explicit;
- reversed domain names do not create a duplicate semantic object;
- superseded identifiers resolve through a migration or correction rule;
- ambiguous joins do not mint stable truth prematurely.

### Source-role anti-collapse

- observed, modeled, regulatory, contextual, aggregate, and synthetic records remain labeled;
- an aggregator does not become original authority;
- a modeled product does not become an observation;
- source-role mismatch produces failure or a finite non-answer.

### Contract and schema conformance

- accepted relation contract exists before strict semantic assertions;
- accepted schema profile exists before strict shape assertions;
- contract and schema versions match;
- permissive scaffolds are not treated as field-complete;
- unknown additional fields are handled according to the accepted profile;
- contract/schema drift blocks promotion.

### Evidence and citation closure

- relation claims resolve all required evidence;
- missing EvidenceBundle support produces `ABSTAIN` or a hold;
- citations identify the owning sources;
- generated descriptions cannot stand in for evidence;
- evidence correction invalidates affected relation expectations.

### Rights, consent, and sensitivity

- most-restrictive posture wins;
- missing rights or consent fails closed;
- sensitive joins cannot become public merely because one side is open;
- public-safe derivatives have reviewed transforms and receipts;
- reverse inference is tested, not only direct field leakage.

### Lifecycle and release

- internal lifecycle records are not consumed as public truth;
- unreleased or held inputs cannot yield a released relation;
- withdrawn, superseded, or corrected inputs trigger re-evaluation;
- test pass does not create a ReleaseManifest;
- rollback expectations are asserted for release-significant derivatives.

### Validator and proof-harness integration

- reusable validators are invoked from their accepted homes;
- validator output is deterministic and finite;
- proof pipelines are systems under test, not test authority;
- proof receipts are not EvidenceBundles;
- zero-test collection is failure, not success;
- missing validator or proof dependencies fail clearly.

### Public-surface leakage

Where a relation reaches a public or semi-public surface, tests should cover:

- API bodies and headers;
- map popups and evidence drawers;
- vector and raster tiles;
- search results and facets;
- graph edges and triplet projections;
- downloads and exports;
- screenshots and generated reports;
- caches and stale aliases;
- embeddings and vector search;
- AI-generated answers or summaries;
- previously issued URLs after correction or withdrawal.

### No-network and deterministic execution

Default suites should:

- use synthetic or public-safe fixtures;
- avoid live network calls;
- avoid live credentials;
- pin time or use deterministic clocks where time affects the result;
- pin random seeds for transforms;
- avoid dependence on private providers;
- emit no canonical data, receipt, proof, or release record.

---

## Finite system outcomes and test results

Do not collapse KFM system outcomes into test-run results.

### System outcomes

| Outcome | Meaning |
|---|---|
| `ANSWER` | Supported, admissible, and within the tested scope. |
| `ABSTAIN` | Evidence, citation, authority, freshness, or disambiguation is insufficient. |
| `DENY` | Policy, rights, consent, sensitivity, lifecycle, release, or access forbids the result. |
| `ERROR` | Validation, dependency, configuration, schema, contract, or execution failure prevents a safe result. |

Other domain or release states such as `HOLD`, `RESTRICTED`, `GENERALIZED`, `WITHDRAWN`, or `SUPERSEDED` may exist, but a child must cite the accepted contract before asserting them.

### Test-run results

| Test result | Meaning |
|---|---|
| Pass | Observed behavior matches the governed expectation. |
| Fail | Behavior violates the expectation. |
| Skip | Test was not executed; never count as proof. |
| Expected failure | Temporary known gap with explicit issue, owner, and expiry. |
| Collection error | Suite did not run correctly; fail the gate. |
| Infrastructure error | Environment failed; do not reinterpret as a policy outcome. |
| Zero tests collected | Fail the gate for any lane claiming active coverage. |

A test that expects `DENY` should pass when the system safely denies. A failing test is not the same thing as a `DENY` result.

---

## Fixture and test-data boundary

### Default fixture posture

Cross-domain fixtures must be:

- synthetic;
- deterministic;
- minimal;
- public-safe;
- reviewable;
- no-network;
- free of live credentials;
- free of exact sensitive locations;
- explicit about domain ownership;
- explicit about source roles;
- explicit about expected evidence, policy, release, correction, and rollback states.

### Fixture authority

The parent does not settle the current fixture-path conflict.

Possible general doctrine form:

```text
fixtures/<cross-domain-topic>/
```

Current surfaced Habitat–Fauna form:

```text
fixtures/domains/habitat/habitat_fauna_thin_slice/
```

The current form is evidence, not an accepted general convention.

Before moving fixtures:

1. inventory payloads and consumers;
2. classify each fixture as single-domain or cross-domain;
3. preserve Git history;
4. update schemas, validators, tests, workflows, and docs;
5. keep expected outputs paired;
6. verify no real sensitive data is present;
7. record rollback.

### Minimum fixture matrix

An active child should include applicable cases for:

- minimal valid relation;
- missing owner reference;
- source-role mismatch;
- unsupported relation direction;
- ambiguous many-to-many join;
- missing evidence;
- missing policy;
- rights or consent denial;
- sensitivity escalation;
- missing transform receipt;
- public-surface leakage;
- stale or withdrawn input;
- correction propagation;
- rollback behavior;
- schema or contract version mismatch;
- validator dependency failure.

### Sensitive-data prohibition

Do not commit:

- exact rare-species coordinates;
- nests, dens, roosts, hibernacula, spawning or breeding sites;
- living-person identifiers;
- genomic data;
- private parcel ownership details;
- protected infrastructure locations;
- confidential cultural or sovereignty-sensitive information;
- real provider credentials or signed URLs.

Use toy geometry and toy identifiers. Do not document operational geoprivacy thresholds in public test fixtures.

---

## CI and proof boundary

### Current evidence

No dedicated executable parent-level cross-domain workflow was surfaced in the bounded review.

Therefore:

- this README does not claim CI coverage;
- a generic repository workflow name is not evidence that this parent runs;
- a green workflow with zero collected tests is not proof;
- an echo-only or placeholder job is not proof;
- a domain workflow does not automatically cover a neutral cross-domain child;
- test documentation does not establish pass rates.

### Requirements for real CI

An accepted workflow should:

1. collect the intended child suites explicitly;
2. fail if a referenced child path is missing;
3. fail on zero tests;
4. avoid `|| true` or equivalent ignored failures;
5. run offline with deterministic fixtures by default;
6. report collected and executed test counts;
7. expose skipped and expected-failure counts;
8. preserve finite system-outcome assertions;
9. run leakage and correction tests where release-significant;
10. fail promotion when trust-spine invariants fail;
11. retain logs or governed reports according to repository policy;
12. avoid creating canonical receipts, proofs, or release decisions merely from test execution.

### Proof limits

A passing cross-domain test suite proves only the scoped implementation against the scoped fixtures and environment.

It does not prove:

- all live data is safe;
- all domain pipelines are complete;
- all relation contracts are accepted;
- all schemas are mature;
- all policy bundles are correct;
- all public surfaces are covered;
- all sensitive joins are non-reconstructable;
- release approval;
- operational rollback;
- production deployment.

---

## Child-lane registration contract

Until a machine-readable registry is accepted, every child README should include the following.

```yaml
child_id: <stable-id>
path: tests/cross_domain/<topic>/
status: DRAFT | ACTIVE | HELD | SUPERSEDED | RETIRED
placement_status: CONFIRMED | PROPOSED | CONFLICTED | NEEDS_VERIFICATION
participating_domains:
  - <domain-a>
  - <domain-b>
primary_test_concern: <short responsibility statement>
implementation:
  executable_files: <verified paths or NONE_CONFIRMED>
  test_command: <verified command or NEEDS_VERIFICATION>
fixtures:
  path: <verified path or NEEDS_VERIFICATION>
validators:
  paths: []
contracts:
  paths: []
schemas:
  paths: []
policy:
  paths: []
proof_pipeline:
  path: <path or N/A>
ci:
  workflow: <verified workflow or NONE_CONFIRMED>
sensitivity:
  class: public | generalized | restricted-review | deny-default
correction:
  triggers: []
rollback:
  target: <commit, blob, or migration record>
owners:
  - <qa-steward>
  - <affected-domain-stewards>
```

### Child naming rules

Until the naming ADR is accepted:

- use existing child names rather than creating aliases;
- do not create both `domain_a_domain_b` and `domain_b_domain_a`;
- do not create both underscore and hyphen spellings;
- record the participating domains independently of directory order;
- use a stable semantic concern if a relation expands beyond two domains;
- treat renames as migration work, not cosmetic cleanup.

### Child status values

| Status | Meaning |
|---|---|
| `DRAFT` | Documented but not established as executable proof. |
| `ACTIVE` | Executable tests, fixtures, CI, owners, and review are verified. |
| `HELD` | Known conflict or safety gap prevents reliance. |
| `SUPERSEDED` | Another lane owns the concern; references are being migrated. |
| `RETIRED` | No active references or CI callers remain. |
| `NEEDS_VERIFICATION` | Implementation or placement is not proven. |

Path status and test maturity are separate. A path can be current yet conflicted, or correctly placed yet README-only.

---

## Review burden

### Ordinary review

Every parent or child documentation change requires:

- QA review;
- documentation review;
- path and link review;
- no-parallel-authority review.

### Elevated review

Add affected domain stewards when:

- object ownership is asserted;
- relation direction changes;
- source-role rules change;
- a contract or schema is introduced;
- a child is renamed or moved.

### Sensitivity review

Add sensitivity, rights, consent, cultural, or security reviewers when a child covers:

- rare species;
- archaeology;
- living persons;
- DNA or genomics;
- private parcels;
- controlled infrastructure;
- sovereignty-sensitive or culturally sensitive information;
- reconstructable location products.

### Release review

Add release and rollback stewards when:

- failures block promotion;
- public artifacts are under test;
- correction or withdrawal behavior changes;
- cache invalidation or previously issued URL behavior changes;
- a test emits release-adjacent reports.

### Separation of duties

Where maturity justifies it, the same actor should not unilaterally:

- define the relation;
- define the policy;
- implement the validator;
- author the fixtures;
- approve the test expectation;
- approve release.

---

## Placement migration and deduplication

A naming cleanup must be governed and reversible.

### Phase 1 — Freeze new variants

- Do not recreate `tests/cross-domain/`.
- Do not create `tests/cross/` or direct-topic siblings without review.
- Do not create reversed child names.
- Do not copy executable tests into overlapping domain lanes.

### Phase 2 — Inventory

Inventory:

- every parent and child path;
- executable modules;
- fixtures and snapshots;
- imports and package references;
- pytest configuration;
- Make targets;
- workflow commands;
- CODEOWNERS;
- docs links;
- schemas and contracts that declare test paths;
- validator metadata;
- proof-pipeline references;
- generated reports;
- release-gate dependencies.

### Phase 3 — Classify responsibility

For every file, decide:

- single-domain test;
- neutral cross-domain test;
- validator test;
- proof-pipeline test;
- API/UI/e2e test;
- fixture;
- reusable helper;
- documentation only.

Move only after classification.

### Phase 4 — Accept the naming rule

Record an ADR or accepted Directory Rules amendment covering:

- direct topic versus parent namespace;
- underscore versus kebab case;
- domain-order rules;
- topic naming for three or more domains;
- child registry expectations;
- redirect or compatibility policy;
- deprecation window.

### Phase 5 — Select one implementation lane

For each concern, identify:

- canonical test path;
- fixture path;
- validator path;
- contract/schema paths;
- proof pipeline;
- CI workflow;
- owners;
- rollback target.

### Phase 6 — Migrate with history

- move files transparently;
- preserve history where practical;
- update all references in the same governed change or staged migration;
- do not leave two executable copies;
- do not create symlinks without an accepted repository policy;
- keep compatibility notes only where needed and explicitly non-authoritative.

### Phase 7 — Prove parity

Run:

- old and new discovery comparison during the migration window;
- exact test-count comparison;
- expected outcome comparison;
- fixture checksum comparison;
- validator result comparison;
- no-network checks;
- leakage checks;
- correction and rollback cases;
- CI caller verification.

### Phase 8 — Retire obsolete paths

Retire a path only when:

- no executable files remain;
- no imports or workflow callers remain;
- no contract/schema metadata points to it;
- no docs or generated reports link to it;
- rollback documentation exists;
- maintainers approve removal.

### Migration stop conditions

Stop and mark `HELD` when:

- the child owner is unclear;
- two lanes contain divergent tests;
- fixtures contain real or sensitive data;
- CI callers cannot be identified;
- contract or schema identity is unresolved;
- moving the lane would weaken sensitivity or policy checks;
- test counts differ unexpectedly;
- a rename would break release or correction evidence;
- rollback cannot be demonstrated.

---

## Minimal parent maintenance procedure

When adding or revising a child:

1. verify the child path exists;
2. verify it is genuinely cross-domain;
3. verify no participating domain should own the test exclusively;
4. search for duplicate or reversed names;
5. inspect contracts, schemas, fixtures, validators, proof pipelines, and workflows;
6. classify sensitivity and rights burden;
7. identify finite expected outcomes;
8. document executable maturity honestly;
9. add the child to the inventory table;
10. run static Markdown validation;
11. run the child test suite when executable;
12. verify CI collects it;
13. record correction and rollback targets.

---

## Validation

### Documentation and inventory checks

```bash
find tests/cross_domain -maxdepth 6 -type f -print | sort
find tests -maxdepth 6 -type f \( -path '*cross*domain*' -o -path '*fauna*habitat*' -o -path '*habitat*fauna*' \) -print | sort
git grep -n -E 'tests/cross-domain|tests/cross_domain|tests/cross/|tests/fauna-habitat|tests/habitat-fauna' --
git grep -n -E 'pytest .*cross|cross_domain|cross-domain' .github Makefile pyproject.toml pytest.ini tox.ini 2>/dev/null
```

### Static README checks

- exactly one rendered H1;
- no heading-level jumps outside fenced examples;
- balanced code fences;
- unique rendered headings;
- valid internal anchors;
- no trailing whitespace or tab indentation;
- no credentials, private keys, tokens, private URLs, or sensitive coordinates;
- relative links resolve at the reviewed base.

### Executable validation

Do not publish a generic command as active until test files and collection are confirmed.

Candidate discovery:

```bash
python -m pytest --collect-only tests/cross_domain
```

Candidate execution:

```bash
python -m pytest -q tests/cross_domain
```

These commands are **NEEDS VERIFICATION** until the lane contains executable tests and repository test configuration supports it.

Required active-suite behavior:

- nonzero exit on collection failure;
- nonzero exit on zero collected tests;
- nonzero exit on assertion failure;
- no ignored failures;
- deterministic offline fixtures;
- clear skip and expected-failure reporting.

---

## Definition of done

This parent is operationally complete only when all applicable items are verified.

### Placement

- [ ] Cross-domain test naming ADR or Directory Rules amendment is accepted.
- [ ] One parent/topic convention is selected.
- [ ] Deleted and superseded paths remain retired.
- [ ] No duplicate or reversed child lane exists.
- [ ] Every child has owners and placement status.

### Inventory

- [ ] Recursive child inventory is complete.
- [ ] Executable files are identified.
- [ ] Fixture and snapshot homes are identified.
- [ ] Validator and proof-pipeline dependencies are identified.
- [ ] Contracts and schemas are linked.
- [ ] CI callers are identified.

### Proof

- [ ] Active children collect at least one test.
- [ ] Positive and negative cases exist.
- [ ] `ABSTAIN`, `DENY`, and `ERROR` cases exist where material.
- [ ] Ownership and source-role anti-collapse are tested.
- [ ] Sensitivity and reverse-inference are tested where material.
- [ ] Correction and rollback behavior is tested where release-significant.
- [ ] Test failures block the appropriate gate.

### Governance

- [ ] No child creates parallel contract, schema, policy, fixture, validator, proof, receipt, data, or release authority.
- [ ] Sensitive fixtures are synthetic and public-safe.
- [ ] Test success is not represented as release approval.
- [ ] Correction and supersession rules are documented.
- [ ] Rollback targets are verified.

Until these items close, the parent remains `DRAFT / CONFLICTED / NEEDS VERIFICATION`.

---

## Correction and rollback

### Documentation correction

Correct this README when:

- a child is added, removed, moved, or renamed;
- the naming ADR is accepted;
- a stale path is discovered;
- executable tests appear;
- CI begins collecting the parent;
- fixture or validator homes change;
- a contract/schema path is accepted;
- sensitivity or release requirements change.

A correction should identify:

- prior claim;
- corrected claim;
- evidence;
- affected children;
- affected workflows and docs;
- migration state;
- rollback target.

### Test correction

When an expected result was wrong:

1. preserve the failing evidence;
2. determine whether implementation, contract, schema, policy, fixture, or expectation is wrong;
3. avoid weakening the assertion merely to restore green CI;
4. update the owning authority first where required;
5. revise fixtures and tests transparently;
6. replay correction and rollback cases;
7. record the correction.

### Path rollback

Before merge, rollback is restoring the prior README blob in a transparent commit.

After a path migration:

- revert through normal commits or a revert PR;
- restore the prior test-discovery path if needed;
- restore workflow callers;
- restore fixture and snapshot references;
- verify exact test counts;
- do not reset or force-rewrite shared history.

### Safety rollback

If real sensitive data enters a test lane:

1. stop further distribution;
2. remove the material through the repository's governed sensitive-data response process;
3. rotate exposed credentials if any;
4. quarantine and assess derivative artifacts;
5. invalidate caches or published copies;
6. record the incident and correction without reproducing the sensitive content;
7. replace with synthetic fixtures.

---

## Open verification backlog

### Placement and naming

- [ ] Decide whether cross-domain tests use `tests/<topic>/`, `tests/cross_domain/<topic>/`, or another accepted pattern.
- [ ] Decide underscore versus kebab-case conventions.
- [ ] Decide domain-order and topic-name rules.
- [ ] Decide whether every cross-domain topic requires a parent doctrine document.
- [ ] Decide whether the surviving parent becomes canonical, transitional, or compatibility-only.
- [ ] Correct remaining references to the deleted `tests/cross-domain/` paths.

### Inventory and ownership

- [ ] Perform a recursive inventory of `tests/cross_domain/`.
- [ ] Confirm whether `fauna_habitat/` is the only child.
- [ ] Inventory overlapping tests under `tests/domains/`.
- [ ] Inventory cross-domain fixtures under domain-owned fixture trees.
- [ ] Assign parent and child owners.
- [ ] Establish a machine-readable child register if needed.

### Contracts, schemas, and validators

- [ ] Identify accepted cross-domain relation contracts.
- [ ] Resolve relation-versus-join schema placement.
- [ ] Replace permissive scaffolds before strict schema proof.
- [ ] Verify broad cross-domain validator executables.
- [ ] Verify geoprivacy validator executables.
- [ ] Verify deterministic reason and result contracts.

### Test execution and CI

- [ ] Confirm pytest or the accepted runner.
- [ ] Confirm collection of each child.
- [ ] Add fail-on-zero-tests behavior.
- [ ] Add an explicit CI caller.
- [ ] Record pass, fail, skip, and expected-failure counts.
- [ ] Add no-network enforcement.
- [ ] Add correction and rollback cases.
- [ ] Add public-surface leakage coverage where applicable.

### Fixtures and sensitivity

- [ ] Settle the cross-domain fixture home.
- [ ] Verify fixture payload inventory.
- [ ] Confirm all fixtures are synthetic and public-safe.
- [ ] Add most-restrictive sensitivity tests.
- [ ] Add reverse-inference tests.
- [ ] Confirm transform receipts and review-state fixtures without exposing policy parameters.

### Release and operations

- [ ] Identify which failures block promotion.
- [ ] Verify release, correction, withdrawal, and rollback integration.
- [ ] Verify cache and previously issued URL behavior.
- [ ] Define retention for test reports.
- [ ] Demonstrate rollback for a path migration.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior `tests/cross_domain/README.md` blob | **CONFIRMED** | Parent existed and contained stale links to the hyphenated tree. | Did not reflect deletion or merged child revision. |
| Commit deleting `tests/cross-domain/` | **CONFIRMED** | Former hyphenated parent and Habitat–Fauna child were explicitly removed. | Does not establish the final naming convention. |
| `tests/README.md` | **CONFIRMED / draft** | `tests/` is the enforceability-proof root; failures should block material promotion gates. | Does not prove this parent's executable depth. |
| Directory Rules | **CONFIRMED authority** | Files are placed by responsibility; multi-domain work does not choose one participating domain as owner. | Exact cross-domain test namespace remains open. |
| Multi-domain placement guide | **CONFIRMED document / draft** | General form `tests/<topic>/...`; exact layout is an ADR trigger. | Does not itself accept the surviving underscore form. |
| `tests/cross_domain/fauna_habitat/README.md` v0.2 | **CONFIRMED merged** | Current child purpose, placement conflict, ownership, geoprivacy, fixtures, proof, CI, correction, and rollback expectations. | Child remains README-only in bounded evidence. |
| Bounded repository search | **CONFIRMED bounded result** | Surfaced parent and one child; no dedicated CI or executable child files were established. | Search is not a recursive filesystem proof. |
| Overlapping Habitat thin-slice test README | **CONFIRMED** | A competing domain-owned cross-domain test intent exists. | No executable modules or pass state established. |
| Habitat–Fauna fixture README | **CONFIRMED** | Synthetic fixture intent and no-network posture. | No payload inventory established. |
| Habitat–Fauna proof-pipeline README | **CONFIRMED** | Proof orchestration is separate from test authority. | Executable behavior and CI remain unverified. |
| Habitat–Fauna validator READMEs | **CONFIRMED** | Broad and geoprivacy validation responsibilities are documented. | Executables and wiring remain unverified. |
| Relation-schema guardrail and join scaffold | **CONFIRMED** | Relation schema is unresolved; flat join schema is permissive and unpaired. | Does not provide an accepted active relation profile. |

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Review status | Draft parent rewrite grounded in current repository evidence |
| Implementation status | README-oriented; executable depth and CI unknown |
| Placement status | `CONFLICTED / NEEDS VERIFICATION` |
| Next review trigger | Naming ADR, new child, executable test, fixture move, validator implementation, CI wiring, contract/schema acceptance, correction, or path migration |

[Back to top](#top)
