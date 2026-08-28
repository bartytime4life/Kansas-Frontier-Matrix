<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-cross-domain-fauna-habitat-readme
title: tests/cross_domain/fauna_habitat/ — Fauna × Habitat Cross-Domain Test and Geoprivacy Proof Lane
type: readme; directory-readme; cross-domain-test-index; ownership-guardrail; geoprivacy-proof-contract
version: v0.2
status: draft; surviving-cross-domain-path; placement-conflicted; readme-only; executable-proof-absent; sensitivity-critical; NEEDS VERIFICATION
policy_label: public-doc; restricted-review-when-sensitive
owners: OWNER_TBD — QA steward · Cross-domain steward · Fauna steward · Habitat steward · Sensitivity reviewer · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — placeholder expanded on 2026-07-05
updated: 2026-07-16
current_path: tests/cross_domain/fauna_habitat/README.md
truth_posture: CONFIRMED target README and prior blob, explicit deletion of tests/cross-domain/, surviving tests/cross_domain parent and child paths, tests responsibility root, cross-domain lowest-common-root doctrine, Habitat/Fauna ownership and sensitivity doctrine, Habitat-Fauna join schema scaffold, relation-schema guardrail, proof-pipeline README, Habitat-owned thin-slice test README, synthetic fixture README, broad and geoprivacy validator READMEs, and absence of the checked habitat_assignment contract path at the pinned snapshot / CONFLICTED target nesting and naming versus tests/<topic>/ doctrine, cross-domain fixture placement under Habitat, and overlapping Habitat-owned thin-slice test lane / UNKNOWN executable test modules, fixture payloads, validator executables, accepted relation contract, active schema profile, CI caller, pass state, release integration, and production behavior / NEEDS VERIFICATION path decision, parent README correction, object identity, negative fixtures, executable validators, CI, correction cascade, migration, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 30e4c9d1a2c890fc82db4f6c95554e5c9823d3c1
  prior_blob: e85b5f16dff7530b1219231233adffc5b4b3e540
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/architecture/cross-domain/multi-domain-placement.md
  - ../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md
  - ../../../schemas/contracts/v1/relations/habitat_fauna/README.md
  - ../../../schemas/contracts/v1/joins/habitat-fauna-join.schema.json
  - ../../../pipelines/proofs/habitat_fauna_thin_slice/README.md
  - ../../../fixtures/domains/habitat/habitat_fauna_thin_slice/README.md
  - ../../domains/habitat/thin-slice.habitat-fauna.test/README.md
  - ../../../tools/validators/habitat-fauna/README.md
  - ../../../tools/validators/geoprivacy/habitat-fauna/README.md
tags: [kfm, tests, cross-domain, fauna, habitat, geoprivacy, sensitivity, ownership, evidence, policy, release, correction, rollback, fail-closed]
notes:
  - "v0.2 replaces a stale compatibility redirect with a repository-grounded cross-domain test and geoprivacy proof contract."
  - "The hyphenated tests/cross-domain tree was explicitly deleted at the pinned snapshot; that deletion does not by itself accept the underscore nesting convention."
  - "This revision changes documentation only and creates, moves, deletes, or activates no test, fixture, schema, contract, validator, workflow, data, or release artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/cross_domain/fauna_habitat/` — Fauna × Habitat Cross-Domain Test and Geoprivacy Proof Lane

> **Purpose.** Define the negative and positive enforceability proofs required when Fauna-owned evidence is related to Habitat-owned context, without collapsing ownership, weakening source roles, leaking sensitive locations, bypassing evidence and policy gates, or treating a test pass as proof closure or release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="Implementation: README only" src="https://img.shields.io/badge/implementation-README__only-red">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
</p>

> [!IMPORTANT]
> This lane may prove cross-domain behavior; it does not own Fauna truth, Habitat truth, relation meaning, schema shape, geoprivacy parameters, policy decisions, EvidenceBundles, receipts, proof artifacts, release decisions, public API behavior, or published layers.

> [!WARNING]
> The repository explicitly deleted `tests/cross-domain/` at the pinned snapshot, leaving this underscore-form path as the surviving neutral cross-domain test path. That repository fact does **not** settle the architectural convention. Current cross-domain placement doctrine says tests should use the lowest common responsibility root under `tests/<topic>/...`, while the dedicated cross-domain layout remains an open decision. Treat this path as **current and reviewable, but placement-conflicted**.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Ownership](#domain-ownership-and-relation-boundary) · [Sensitivity](#sensitivity-and-geoprivacy-invariants) · [Coverage](#required-test-families) · [Outcomes](#finite-outcomes-and-test-results) · [Fixtures](#fixture-and-test-data-contract) · [Proof](#current-implementation-and-proof-boundary) · [Authoring](#test-authoring-contract) · [Migration](#placement-migration-and-deduplication) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/cross_domain/fauna_habitat/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| Other direct files below this target | **NOT SURFACED in bounded search** | Treat the lane as README-only until recursive inventory proves otherwise. |
| `tests/cross_domain/README.md` | **CONFIRMED but stale** | It still points to the deleted hyphenated tree and requires separate correction. |
| `tests/cross-domain/` | **CONFIRMED deleted** | The prior parent and Habitat-Fauna child READMEs were removed from `main`. |
| `tests/` | **CONFIRMED canonical responsibility root** | Tests prove enforceability; they do not own policy, truth, fixtures, or release. |
| Cross-domain placement doctrine | **CONFIRMED rule / naming OPEN** | Multi-domain tests belong at the lowest common test root without choosing one domain; exact topic layout remains unresolved. |
| `tests/domains/habitat/thin-slice.habitat-fauna.test/` | **CONFIRMED README-only overlapping lane** | Habitat-owned placement for a cross-domain test is architecturally suspect and must not become a second implementation authority. |
| Habitat-Fauna fixture lane | **CONFIRMED README-oriented / placement conflicted** | Synthetic fixture intent exists under Habitat, but payload inventory and cross-domain placement are unverified. |
| Habitat-Fauna proof pipeline | **CONFIRMED README-only proof-harness lane** | Executable proof behavior, receipts, CI, and pass state remain unverified. |
| Relation schema lane | **CONFIRMED README-only guardrail** | No schema file was surfaced directly under `relations/habitat_fauna/`. |
| Flat join schema | **CONFIRMED permissive scaffold** | `habitat-fauna-join.schema.json` has empty properties, allows additional properties, and has no paired contract. |
| Checked HabitatAssignment contract | **ABSENT at exact path** | `contracts/domains/fauna/habitat_assignment.md` is proposed in prose but was not found. |
| Broad Habitat-Fauna validator lane | **CONFIRMED README / executable UNKNOWN** | No executable is established by the README. |
| Habitat-Fauna geoprivacy validator lane | **CONFIRMED README / executable UNKNOWN** | No executable, policy bundle, fixture set, or CI wiring is established. |
| Dedicated cross-domain CI | **NOT SURFACED in bounded search** | Do not claim this lane runs in CI. |
| Current test pass state | **UNKNOWN** | Source inspection is not execution evidence. |
| Production behavior | **UNKNOWN** | Documentation and path presence do not prove deployed enforcement. |

**Authority of this README:** lane purpose, placement warning, test taxonomy, expected outcomes, fixture constraints, leakage checks, review burden, migration guardrails, and rollback guidance. Executable tests, accepted contracts and schemas, policy bundles, validators, fixtures, proof receipts, CI results, release records, correction records, and steward decisions outrank this document.

---

## Placement and authority

### Directory Rules basis

KFM places files by primary responsibility:

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

For a file that spans multiple domains, the Domain Placement Law requires the lowest common responsibility root **without choosing one domain as owner**.

Current doctrine gives the general target:

```text
tests/<cross-domain-topic>/...
```

It leaves the exact cross-domain namespace open:

```text
tests/fauna-habitat/...           possible direct topic form
tests/cross_domain/fauna_habitat/ current surviving repository form
tests/cross/<topic>/...           open layout question in architecture docs
```

Therefore:

- the target is correctly under `tests/`;
- the target does not choose `tests/domains/habitat/` or `tests/domains/fauna/`;
- the intermediate `cross_domain/` segment and `fauna_habitat` spelling remain **NEEDS VERIFICATION**;
- the deletion of `tests/cross-domain/` removes a duplicate tree but does not constitute an accepted naming ADR;
- no new cross-domain test path should be created until the naming decision is recorded.

### Current path class

| Field | Value |
|---|---|
| Responsibility | Cross-domain enforceability proof |
| Current repository role | Surviving cross-domain Habitat-Fauna README lane |
| Authority status | `CONFLICTED / NEEDS VERIFICATION` |
| Implementation status | README-only in bounded evidence |
| Write posture | Documentation and future executable tests only after placement review |
| Duplicate posture | Do not recreate `tests/cross-domain/` or duplicate tests under Habitat and neutral lanes |
| Required reviewers | QA, cross-domain, Fauna, Habitat, sensitivity, evidence, policy, release, docs |

### Adjacent lane routing

| Concern | Owning home | This lane's role |
|---|---|---|
| Neutral Fauna × Habitat cross-domain assertions | accepted cross-domain test topic under `tests/` | Primary test intent documented here |
| Habitat-only behavior | `tests/domains/habitat/` | Link and compose; do not duplicate |
| Fauna-only behavior | `tests/domains/fauna/` | Link and compose; do not duplicate |
| Proof orchestration | `pipelines/proofs/habitat_fauna_thin_slice/` | System under test; not reimplemented here |
| Broad cross-domain validation | `tools/validators/habitat-fauna/` | Invoke or assert outputs once executable |
| Sensitive-location validation | `tools/validators/geoprivacy/habitat-fauna/` | Invoke or assert outputs once executable |
| Relation meaning | accepted cross-domain contract home | Reference only; current contract is unresolved |
| Relation machine shape | accepted relation/join schema home | Validate once an accepted schema exists |
| Test examples | accepted `fixtures/<topic>/` or explicitly governed current fixture lane | Consume synthetic inputs; do not create truth |
| Evidence and receipts | `data/proofs/`, `data/receipts/` | Assert pointers and behavior; do not store canonical records here |
| Release/correction/rollback | `release/` | Assert gate behavior; do not decide state |

---

## Domain ownership and relation boundary

### Core ownership invariant

> **A relation is not an ownership transfer.**

Fauna and Habitat retain distinct authority:

| Object or claim | Owning domain | Cross-domain test requirement |
|---|---|---|
| Taxon identity | Fauna | Habitat must not redefine or mint taxon truth. |
| Occurrence evidence | Fauna | Habitat context may cite it only through governed relations and sensitivity rules. |
| Sensitive site or exact occurrence geometry | Fauna | Deny by default; never included in default public-safe fixtures. |
| Range, monitoring, telemetry, seasonal occurrence | Fauna | Preserve source role, time, sensitivity, and uncertainty. |
| Habitat patch | Habitat | Fauna may cite the released public-safe reference; it does not copy the patch into Fauna truth. |
| Land-cover observation | Habitat | Remains Habitat-owned context and must not become occurrence evidence. |
| Ecological system or ecoregion context | Habitat | Context only; does not establish species presence. |
| Suitability model or habitat quality | Habitat | Modeled support; never relabeled as observed occurrence or regulatory designation. |
| Connectivity edge or corridor | Habitat | Derived landscape support; does not prove animal movement. |
| Habitat assignment | Cross-domain relation | Must reference both owners, preserve evidence, and remain separate from either canonical object. |

### Relation anti-collapse rules

The following transformations must fail:

```text
HabitatPatch -> Fauna Occurrence
Fauna Occurrence -> HabitatPatch
SuitabilityModel -> observed presence
RangePolygon -> exact occurrence
SensitiveSite -> public habitat label
Habitat assignment -> taxonomic authority
Join result -> EvidenceBundle
Test pass -> proof closure
Proof pass -> release approval
Redaction check -> policy decision
Public-safe derivative -> unrestricted source geometry
Graph edge -> canonical relation truth
AI summary -> evidence
```

### Source-role preservation

Tests must retain distinctions among:

- observed occurrence;
- modeled suitability;
- regulatory designation;
- aggregate or range context;
- administrative or stewardship context;
- candidate relation;
- synthetic fixture.

A relation that silently upgrades a model to observation, context to authority, candidate to released fact, or synthetic fixture to evidence must fail.

### Direction and citation

A valid relation should be directional and explicit:

```text
Fauna-owned subject reference
  -> relation type + method + evidence + time + sensitivity
  -> Habitat-owned object reference
```

or the reverse, when the semantic contract requires it.

Tests must reject:

- directionless relation blobs;
- copied owner fields presented as local truth;
- missing source object versions;
- missing relation method or confidence posture where material;
- silent many-to-many flattening;
- duplicate relation identity without reconciliation.

---

## Sensitivity and geoprivacy invariants

### Most-restrictive result rule

Habitat's dominant sensitivity risk is join-induced. A public Habitat object can become sensitive when combined with Fauna occurrence or site information.

The test rule is:

> The resulting product inherits the most restrictive applicable sensitivity, rights, policy, and release posture of any input or derivation.

Tests must not assume:

```text
public Habitat input + restricted Fauna input = public join
```

The default is fail-closed until an approved public-safe derivative is supported by policy, review, evidence, and receipts.

### Protected categories

Default tests must treat these as sensitive or potentially re-identifying:

- exact sensitive occurrence geometry;
- nests, dens, roosts, hibernacula, spawning, breeding, and aggregation sites;
- detailed telemetry or movement paths;
- steward-controlled and rights-restricted records;
- reverse-engineerable density, hotspot, corridor, suitability, or uncertainty products;
- private-parcel or named-party joins;
- controlled-source ecological records;
- outputs that reveal sensitive locations through combination rather than a direct field.

This README intentionally contains no exact coordinates, real identifiers, generalization distances, thresholds, or redaction parameters.

### Public-safe derivative gate

A public-safe derivative requires all material support to be testable:

| Requirement | Test posture |
|---|---|
| Binding policy decision | Present and applicable to subject, purpose, audience, and surface |
| Review state | Approved by the required steward/reviewer |
| Transform identity | Named, versioned, deterministic, and reproducible |
| Receipt | RedactionReceipt, AggregationReceipt, or accepted equivalent |
| Evidence | EvidenceRefs resolve to admissible support |
| Geometry safety | Output cannot reconstruct protected geometry within the tested threat model |
| Surface safety | Map, tile, API, export, search, graph, screenshot, embedding, and AI outputs remain safe |
| Release state | Released derivative is distinct from restricted source |
| Correction path | Published derivative can be corrected, withdrawn, and cache-invalidated |
| Rollback target | Previous safe state or full withdrawal is identified |

### Reverse-inference tests

Tests must cover leakage even when the protected value is absent from the main response:

- map tiles and tile metadata;
- search indexes and autocomplete;
- graph neighbors and edge density;
- model outputs and uncertainty surfaces;
- screenshots and thumbnails;
- cache keys and public aliases;
- exports and downloadable summaries;
- vector embeddings and retrieval snippets;
- AI-generated descriptions;
- error messages and debug traces;
- previously issued URLs after correction or withdrawal.

A product that omits an exact point but makes it practically recoverable still fails.

---

## Required test families

### 1. Placement and duplicate-lane tests

Prove that:

- only the accepted cross-domain test path executes;
- deleted or deprecated aliases are not reintroduced;
- the Habitat-owned thin-slice README does not become a second implementation lane;
- imports, CI globs, and fixture pointers resolve to the accepted path;
- parent README indexes are corrected after migration.

### 2. Domain ownership tests

Prove that:

- Habitat-owned objects remain Habitat references;
- Fauna-owned objects remain Fauna references;
- joins store relation fields rather than copied canonical payloads;
- write attempts against the non-owning domain fail;
- correction of an owner object propagates through relation invalidation or re-evaluation.

### 3. Relation identity and ambiguity tests

Cover:

- deterministic relation identity;
- directionality;
- duplicate relations;
- conflicting source versions;
- many-to-many ambiguity;
- spatial overlap without semantic support;
- temporal mismatch;
- uncertain classification;
- stale supporting objects.

Ambiguous relations should `ABSTAIN`, hold, or fail validation rather than flattening to a confident assignment.

### 4. Source-role tests

Reject:

- suitability treated as observed occurrence;
- range treated as exact occurrence;
- regulatory habitat treated as species presence;
- context treated as legal authority;
- aggregate products treated as raw observations;
- synthetic fixtures treated as evidence.

### 5. Contract and schema tests

An accepted relation profile must eventually prove:

- a paired semantic contract exists;
- the schema has stable identity and meaningful fields;
- required domain refs, relation type, time, method, evidence, policy, sensitivity, and release fields are constrained where material;
- additional properties are governed;
- invalid references and owner mismatches fail;
- the current empty permissive join scaffold is not promoted as active.

### 6. Evidence tests

Cover:

- resolvable EvidenceRef to EvidenceBundle;
- missing EvidenceBundle;
- evidence supporting only one side of the relation;
- unsupported inference from co-location;
- stale evidence;
- contradictory evidence;
- source authority mismatch;
- citation-safe public projection.

Missing or inadequate support should yield `ABSTAIN`, not an invented relation.

### 7. Policy and review tests

Cover:

- missing policy state;
- explicit deny;
- reviewer-required state;
- purpose or audience mismatch;
- consent or rights restrictions where applicable;
- most-restrictive policy propagation;
- public versus reviewer versus restricted surface behavior.

Missing or denying policy should yield `DENY` or an accepted restricted outcome.

### 8. Geoprivacy tests

Cover:

- sensitive occurrence joined to public Habitat object without transform;
- transform without receipt;
- receipt without matching transform digest or policy;
- non-deterministic transform;
- transform that remains reverse-engineerable;
- map-safe output but unsafe export or search result;
- safe body but unsafe cache, tile, graph, screenshot, or AI summary;
- correction that leaves old precise artifacts reachable.

### 9. Lifecycle and release tests

Cover:

- RAW, WORK, QUARANTINE, or unpublished candidates used as public relation inputs;
- missing review state;
- missing release manifest;
- withdrawn or superseded owner object;
- correction-pending relation;
- stale public derivative;
- missing rollback target;
- public cache not invalidated after withdrawal.

### 10. Proof-harness boundary tests

Prove that:

- the proof pipeline uses fixture-safe or release-approved inputs;
- proof outputs land in accepted proof/receipt homes;
- proof receipts do not become EvidenceBundles;
- proof pass does not publish;
- missing gates produce blockers;
- no-network mode is enforced by default;
- public clients never read proof internals or lifecycle stores.

### 11. API, UI, tile, and AI surface tests

Prove that every supported surface:

- reads through governed interfaces;
- uses only released public-safe derivatives;
- preserves finite outcomes and caveats;
- does not expose protected geometry or internal refs;
- does not turn absence of evidence into confident text;
- reflects corrections, withdrawals, and supersession.

### 12. Correction and rollback tests

Cover:

- Fauna correction invalidating a Habitat assignment;
- Habitat correction invalidating relation outputs;
- sensitivity escalation after release;
- policy or rights change;
- transform defect;
- receipt mismatch;
- source withdrawal;
- rollback to a prior public-safe derivative;
- full withdrawal when no safe rollback exists.

---

## Finite outcomes and test results

### Runtime or policy outcomes

Use accepted finite system outcomes without inventing new meanings:

| Outcome | Use |
|---|---|
| `ANSWER` | Relation is supported and the requested representation is permitted. |
| `ABSTAIN` | Evidence, identity, ambiguity, freshness, or scope is insufficient. |
| `DENY` | Policy, rights, sensitivity, audience, purpose, lifecycle, or release state forbids the request. |
| `ERROR` | Validation, schema, dependency, adapter, configuration, or processing failure prevents safe evaluation. |

Restricted or redacted responses are representation classes, not automatic substitutes for one of the finite outcomes. Their relationship to an accepted response envelope must be explicit.

### Test-run results

Do not confuse system outcomes with test framework results:

| Test result | Meaning |
|---|---|
| pass | Observed behavior matched the declared expectation. |
| fail | Behavior violated the declared cross-domain invariant. |
| skip | Test was intentionally not executed with a documented reason; not proof. |
| xfail | Known defect is tracked; not acceptable promotion evidence unless the gate explicitly permits it. |
| error | Test infrastructure failed; system behavior is unknown. |

A test expecting `DENY` **passes** only when the system returns the accepted deny profile and leaks nothing protected.

---

## Fixture and test-data contract

### Current fixture evidence

The repository contains a fixture README at:

```text
fixtures/domains/habitat/habitat_fauna_thin_slice/
```

That lane documents synthetic cross-domain proof-support intent but no payload inventory was verified. Its placement under Habitat conflicts with the neutral cross-domain placement rule and must not silently become fixture authority.

### Interim fixture posture

Until fixture placement is accepted:

- use only existing reviewed synthetic fixtures;
- do not create duplicate fixture families under multiple paths;
- document the consuming test and expected outcome;
- keep fixture identity, owner, and sensitivity explicit;
- avoid real or source-derived protected geometry;
- do not use realistic values that could act as exposure guidance;
- use deterministic toy digests, timestamps, identifiers, and generalized geometry;
- keep valid, invalid, denied, abstaining, error, correction, and rollback cases separate.

### Minimum fixture matrix

| Scenario | Expected system posture |
|---|---|
| Valid public-safe relation with resolved support | `ANSWER` or accepted relation success |
| Habitat object copied as Fauna truth | validation failure |
| Fauna occurrence copied as Habitat truth | validation failure |
| Missing relation contract/profile | `ERROR` or validation failure |
| Missing EvidenceBundle | `ABSTAIN` |
| Ambiguous many-to-many join | `ABSTAIN` |
| Sensitive join without policy | `DENY` |
| Sensitive join without transform receipt | `DENY` |
| Transform still reverse-engineerable | `DENY` or validation failure |
| Unreleased owner object | `DENY` |
| Corrected or withdrawn owner object | `DENY` / `ABSTAIN` plus invalidation |
| Proof receipt used as EvidenceBundle | validation failure |
| Public client reads lifecycle store | validation failure |
| Model output presented as observed occurrence | validation failure |
| Rollback target missing for released derivative | release blocker |

### Fixture anti-authority rule

A fixture may demonstrate a shape or behavior. It cannot establish:

- real species presence;
- habitat suitability;
- source authority;
- evidence closure;
- policy approval;
- sensitivity tier;
- geoprivacy safety;
- release approval;
- correction completion;
- rollback readiness.

---

## Current implementation and proof boundary

### Confirmed implementation depth

At the pinned snapshot:

- this target is README-only in bounded search;
- the deleted hyphenated lane contained no confirmed test modules;
- the Habitat-owned thin-slice lane is README-only;
- the fixture lane is README-oriented with no verified payload inventory;
- the proof pipeline is documented but executable behavior remains unverified;
- the neutral relation-schema lane is README-only;
- the existing join schema is an empty permissive scaffold;
- the checked HabitatAssignment contract path is absent;
- broad and geoprivacy validator lanes are README-only and explicitly do not confirm executables;
- no dedicated cross-domain test workflow was surfaced.

### What documentation can prove

Documentation can prove:

- intended responsibility;
- required invariants;
- expected failure modes;
- review and migration requirements;
- known gaps and conflicts.

Documentation cannot prove:

- importable test modules;
- fixture validity;
- validator behavior;
- CI execution;
- geoprivacy safety;
- release blocking;
- runtime or public-client behavior;
- current pass rates.

### CI acceptance characteristics

A future CI job for this lane should:

1. run the accepted cross-domain path only;
2. fail when no tests are collected;
3. run offline with network denied by default;
4. use deterministic synthetic fixtures;
5. exercise positive and negative cases;
6. assert `ABSTAIN`, `DENY`, and `ERROR` paths;
7. check protected-field and reverse-inference leakage;
8. invoke accepted broad and geoprivacy validators;
9. validate relation contracts and schemas;
10. produce a reviewable test report;
11. block promotion for material failures;
12. avoid `|| true`, ignored exit codes, and echo-only jobs.

A workflow name or green placeholder job is not proof.

---

## Test authoring contract

Each executable test or test group should identify:

```yaml
test_id: <stable-id>
status: DRAFT | ACTIVE | HELD | SUPERSEDED | RETIRED
path: <accepted-test-path>
owners:
  fauna: <owner>
  habitat: <owner>
  qa: <owner>
  sensitivity: <owner-if-material>
scope:
  relation_type: <accepted-type>
  fauna_object_family: <family>
  habitat_object_family: <family>
fixture_refs:
  - <synthetic-fixture>
expected:
  system_outcome: ANSWER | ABSTAIN | DENY | ERROR
  test_result: pass
support:
  fauna_contract: <path-or-NEEDS-VERIFICATION>
  habitat_contract: <path-or-NEEDS-VERIFICATION>
  relation_contract: <path-or-NEEDS-VERIFICATION>
  relation_schema: <path-or-NEEDS-VERIFICATION>
  policy: <path-or-NEEDS-VERIFICATION>
  validator: <path-or-NEEDS-VERIFICATION>
  evidence_fixture: <path-or-NEEDS-VERIFICATION>
  receipt_fixture: <path-or-NEEDS-VERIFICATION>
leakage_assertions:
  - <protected-field-or-surface>
release_assertions:
  correction: <expectation>
  rollback: <expectation>
```

### Required assertion groups

A material cross-domain test should assert:

- response or relation shape;
- expected finite outcome;
- stable reason code or finding;
- owner refs remain distinct;
- source roles remain visible;
- evidence support is sufficient or abstention occurs;
- sensitivity and policy propagate correctly;
- protected data is absent from all observed surfaces;
- release/correction/rollback behavior is correct;
- no lifecycle or proof-store bypass occurs.

### Review burden

| Change | Minimum review |
|---|---|
| README clarification | QA or docs maintainer |
| New ownership or relation test | QA + Fauna + Habitat |
| Sensitive-location case | QA + Fauna + Habitat + sensitivity/geoprivacy reviewer |
| Policy outcome expectation | Policy steward |
| New fixture shape | Fixture + affected domain stewards |
| New schema or contract expectation | Contract + schema stewards |
| Release/correction/rollback expectation | Release steward |
| Path migration or naming change | Architecture/directory steward; ADR or migration record as required |
| CI promotion gate | QA + release + security reviewers |

---

## Placement migration and deduplication

### Current conflict set

The repository currently carries or recently carried:

```text
tests/cross_domain/fauna_habitat/                 surviving neutral path
tests/cross_domain/README.md                      stale parent index
tests/cross-domain/                               deleted duplicate tree
tests/domains/habitat/thin-slice.habitat-fauna.test/
                                                  overlapping Habitat-owned README lane
fixtures/domains/habitat/habitat_fauna_thin_slice/
                                                  cross-domain fixture under Habitat
```

### Migration sequence

Do not perform a folder rename or copy without this sequence:

1. **Inventory** every README, test module, fixture, import, workflow glob, documentation link, and generated report reference.
2. **Classify** each artifact as neutral cross-domain, Habitat-only, Fauna-only, fixture, validator, schema, contract, proof orchestration, or generated output.
3. **Choose** the accepted cross-domain topic and naming convention through the governing review process.
4. **Select** one neutral cross-domain test implementation path.
5. **Move or rewrite** domain-owned tests to their domain lanes and neutral assertions to the accepted cross-domain lane.
6. **Resolve fixtures** into one accepted fixture home, preserving lineage and expected-output references.
7. **Update** validators, contracts, schemas, imports, CI, docs, and parent indexes atomically or through a staged migration.
8. **Retain redirects** only where useful and mark them non-executable.
9. **Run both positive and negative suites** against the migrated path.
10. **Remove deprecated execution paths** only after consumer and CI verification.
11. **Record rollback** to the previous tree and restore links if migration fails.

### Stop conditions

Stop migration when:

- a test's ownership cannot be classified;
- unique content exists in more than one lane;
- an accepted relation contract is missing;
- fixture lineage is unclear;
- CI or imports still reference a deprecated path;
- protected fixture content is discovered;
- rollback cannot restore the previous runnable state.

---

## Validation

### Documentation validation

This README should maintain:

- one rendered H1;
- valid heading hierarchy;
- balanced code fences;
- resolvable internal navigation;
- no duplicate rendered headings;
- no trailing whitespace;
- no credentials, secrets, exact protected locations, or geoprivacy parameters.

### Repository checks

Recommended checks after executable tests are added:

```bash
find tests/cross_domain/fauna_habitat -maxdepth 5 -type f | sort
find tests/domains/habitat/thin-slice.habitat-fauna.test -maxdepth 5 -type f | sort
find fixtures/domains/habitat/habitat_fauna_thin_slice -maxdepth 5 -type f | sort
find pipelines/proofs/habitat_fauna_thin_slice -maxdepth 5 -type f | sort
pytest -q tests/cross_domain/fauna_habitat
```

Additional checks should be added only after the accepted paths and runners are verified.

**Status for this README revision:** documentation checks only. Repository tests and validators were **not run**.

### Negative checks

Validation should fail if:

- no tests are collected;
- a deleted or deprecated path is still the only CI target;
- cross-domain tests are duplicated under multiple authorities;
- fixtures contain real protected data;
- relation tests pass without evidence or policy assertions;
- geoprivacy tests check only response bodies and ignore other surfaces;
- test failure is ignored;
- a test pass is used as release approval.

---

## Definition of done

This lane is not implementation-complete until all applicable items are verified:

- [ ] Cross-domain test path and naming convention are accepted.
- [ ] `tests/cross_domain/README.md` is corrected to current repository state.
- [ ] One executable neutral Fauna × Habitat test lane exists.
- [ ] Overlapping Habitat-owned thin-slice tests are classified and deduplicated.
- [ ] Fixture placement is accepted and payload inventory is verified.
- [ ] A paired relation semantic contract exists.
- [ ] A meaningful closed relation schema or accepted profile exists.
- [ ] Relation identity, direction, time, source role, evidence, sensitivity, policy, release, correction, and rollback semantics are testable.
- [ ] Broad Habitat-Fauna validator executable exists.
- [ ] Geoprivacy validator executable exists.
- [ ] Positive, invalid, abstain, deny, error, correction, and rollback fixtures exist.
- [ ] Reverse-inference and multi-surface leakage tests exist.
- [ ] Proof-harness integration test exists without live network access.
- [ ] CI runs the accepted path and fails on zero collection.
- [ ] Material failures block promotion.
- [ ] Owners and review burden are recorded.
- [ ] Test reports are inspectable and retained under an accepted report lane.
- [ ] Correction and rollback of test expectations and released derivatives are covered.

---

## Correction and rollback

### Documentation correction

If a statement in this README becomes wrong:

1. update the statement with current repository evidence;
2. preserve the prior claim in version control;
3. label the corrected implementation state accurately;
4. update links and affected parent indexes;
5. do not use documentation correction to change policy or release state.

### Test correction

When a test expectation changes:

- identify whether the change is a bug fix, contract change, policy change, schema change, source-role correction, sensitivity correction, or release correction;
- update the owning artifact first;
- update fixtures and tests together;
- preserve the former expected behavior where regression history matters;
- require the appropriate domain, policy, sensitivity, and release review.

### Path rollback

Before merging a future path migration:

- preserve the prior branch or commit;
- record the prior paths and imports;
- confirm the old suite can be restored;
- avoid force pushes or history rewrites;
- keep one executable authority at every migration stage.

If a migration breaks test discovery, fixtures, imports, CI, links, or rollback:

- restore the prior executable path through a revert;
- restore parent indexes and CI globs;
- keep the failed migration evidence;
- correct the migration plan before retrying.

### README rollback target

For this documentation revision, restore prior blob:

```text
e85b5f16dff7530b1219231233adffc5b4b3e540
```

or revert the documentation commit/PR after merge. Do not reset shared history.

---

## Open verification backlog

### Placement and ownership

- [ ] Decide whether cross-domain tests use `tests/<topic>/`, `tests/cross_domain/<topic>/`, or another accepted pattern.
- [ ] Decide whether `fauna_habitat` or `habitat_fauna` is the stable topic identity.
- [ ] Correct `tests/cross_domain/README.md`, which references deleted paths.
- [ ] Classify the Habitat-owned thin-slice test lane as domain-only, compatibility, migration source, or duplicate.
- [ ] Resolve cross-domain fixture placement currently under Habitat.
- [ ] Record the path decision in Directory Rules, an ADR, or an accepted migration note.

### Contracts and schemas

- [ ] Define or verify the relation semantic contract.
- [ ] Decide relation lane versus join lane schema authority.
- [ ] Replace or retire the empty permissive join scaffold.
- [ ] Define deterministic relation identity and direction.
- [ ] Define required temporal, evidence, policy, sensitivity, review, release, correction, and rollback fields.
- [ ] Verify schema registry records and consumers.

### Tests, fixtures, and validators

- [ ] Inventory executable files under all overlapping lanes.
- [ ] Create deterministic public-safe fixture payloads.
- [ ] Create ownership, role, evidence, ambiguity, policy, geoprivacy, leakage, lifecycle, release, correction, and rollback tests.
- [ ] Verify broad Habitat-Fauna validator executable.
- [ ] Verify geoprivacy validator executable.
- [ ] Verify proof-pipeline executable and no-network mode.
- [ ] Establish CI and fail-on-zero-tests behavior.
- [ ] Record pass rates and test reports.

### Sensitivity and release

- [ ] Verify binding policy paths and accepted sensitivity vocabulary.
- [ ] Verify transform receipt schemas and validation.
- [ ] Test every public surface for reverse inference.
- [ ] Verify cache and previously issued URL invalidation.
- [ ] Verify correction propagation from both owning domains.
- [ ] Verify withdrawal and rollback behavior.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Current target README | **CONFIRMED** | Prior compatibility role and stale hyphenated pointer | Did not reflect deletion or current overlap |
| Commit deleting `tests/cross-domain/` | **CONFIRMED** | Hyphenated tree no longer exists at pinned snapshot | Does not establish final naming doctrine |
| `tests/cross_domain/README.md` | **CONFIRMED stale** | Surviving parent path | Still references deleted lanes |
| Directory Rules and multi-domain placement doc | **CONFIRMED doctrine / layout open** | Lowest common responsibility root; no picked domain owner | Exact cross-domain test namespace unresolved |
| Fauna cross-lane relations | **CONFIRMED draft doctrine-derived register** | Owner-publishes/consumer-cites, most-restrictive sensitivity, EvidenceBundle support | Concrete relation implementation remains proposed |
| Habitat sensitivity profile | **CONFIRMED draft profile** | Join-induced sensitivity and product-level disposition | Binding policy parameters remain outside doc |
| Fauna sensitivity profile | **CONFIRMED draft profile** | Deny-by-default sensitive occurrence and geoprivacy posture | Tier persistence and parameters remain proposed |
| Relation schema README | **CONFIRMED guardrail** | Neutral relation placement and overlap awareness | No direct relation schemas confirmed |
| Join schema | **CONFIRMED scaffold** | Existing schema path and permissive shape | No meaningful fields or contract |
| Proof-pipeline README | **CONFIRMED draft** | Proof-harness responsibility and anti-collapse rules | Executable behavior and CI unverified |
| Habitat thin-slice test README | **CONFIRMED draft** | Overlapping test intent and boundary | No modules or pass state established |
| Habitat-Fauna fixture README | **CONFIRMED draft** | Synthetic fixture intent | Payload inventory and placement unresolved |
| Broad validator README | **CONFIRMED draft** | Proposed cross-domain validation responsibilities | No executable confirmed |
| Geoprivacy validator README | **CONFIRMED draft** | Proposed sensitive-location checks | No executable, policy binding, or CI confirmed |
| Exact HabitatAssignment contract fetch | **ABSENT at checked path** | Proposed contract is not current evidence | Another contract path may exist; exhaustive search not proven |

---

<p align="right"><a href="#top">Back to top</a></p>
