<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-air-readme
title: tests/domains/air/ — Air Slug Compatibility Test Guardrail
type: readme; directory-readme; domain-test-compatibility-lane; slug-conflict-guardrail; non-authoritative
version: v0.2
status: draft; repository-grounded; compatibility-only; direct-lane-readme-only; preferred-atmosphere-lane-confirmed; executable-tests-not-established; slug-adr-open; ci-todo-only; not-for-life-safety
owners: OWNER_TBD — Atmosphere/Air steward · Test steward · QA steward · Directory-governance steward · Contract steward · Schema steward · Fixture steward · Policy steward · Evidence steward · Release steward · Security reviewer · CI steward · Docs steward
created: NEEDS VERIFICATION — compatibility stub existed before v0.2
updated: 2026-07-16
supersedes: v0.1 nine-line Air compatibility README
policy_label: "public-review; tests; air; atmosphere; compatibility-only; slug-drift; redirect-to-atmosphere; no-executable-tests-here; no-network-default; synthetic-only; evidence-aware; policy-aware; release-gated; correction-aware; rollback-aware; not-emergency-alerting; no-truth-authority; no-publication-authority"
current_path: tests/domains/air/README.md
truth_posture: >
  CONFIRMED target v0.1 compatibility README and prior blob; canonical tests responsibility
  root; tests/domains parent classification of compatibility lanes; preferred Atmosphere test
  parent at tests/domains/atmosphere; Atmosphere canonical-path registry preferring atmosphere
  while marking air versus atmosphere ADR-class; policy/domains/air and pipeline_specs/air
  compatibility guardrails; pipelines/domains/air alias-candidate documentation; TODO-only
  domain-atmosphere workflow; current Makefile test target excluding domain test lanes; generated
  receipt schema; bounded search returning only this README under tests/domains/air; no matching
  open pull request or task branch; and no path-scoped AGENTS.md at the checked root/tests/tests-domains/
  tests-domains-air paths / PROPOSED this path remain a documentation-only compatibility and
  migration guardrail, redirect all executable Atmosphere/Air domain tests to tests/domains/atmosphere,
  reject duplicate test, fixture, policy, contract, schema, evidence, release, or public-surface
  authority under the air slug, and expose finite REDIRECT/HOLD/ABSTAIN/DENY/ERROR outcomes /
  CONFLICTED continued repository presence of both air and atmosphere segments across policy,
  pipeline specifications, executable pipeline documentation, contracts, and tests while the
  canonical-path registry says new work should use atmosphere until ADR resolution /
  UNKNOWN exhaustive unindexed or differently named files, dynamic test generation, current
  collected Atmosphere test inventory, fixture payloads, active policy bundles, canonical slug
  decision, branch-protection significance, runtime consumers, public route aliases, release
  manifests, and production use / NEEDS VERIFICATION owners, CODEOWNERS, accepted ADR or lane-register
  decision, complete air/atmosphere inventory, migration/deprecation map, executable alias tests,
  fixture identity, reason-code vocabulary, CI ownership, promotion-gate adoption, correction
  propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ba141d8ee7092427936161ad7b954fc449036601
  prior_blob: 810432ee7db80d18ff8d0aa1b1885239d6622536
  preferred_test_lane: tests/domains/atmosphere/
  compatibility_test_lane: tests/domains/air/
  direct_lane_indexed_files:
    - tests/domains/air/README.md
  checked_absent_paths:
    - AGENTS.md
    - tests/AGENTS.md
    - tests/domains/AGENTS.md
    - tests/domains/air/AGENTS.md
  related_repository_blobs:
    tests_domains_parent: d84d692e15cc1882e4eff9771c091e8a6a872911
    atmosphere_test_parent: 6474cc33c3bdd668fd8713e06e94f7dacda97b6b
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    atmosphere_canonical_paths: 97296d516792ad3bc2bc1f18d03e2518e367d28a
    atmosphere_domain_readme: 005421a9a3851d8ddc64e79a6ad3653d65d57f78
    air_policy_guardrail: 1531b955ebc8474dae384e896117d0e265405e76
    air_pipeline_spec_guardrail: 16a5096d5edcad9bbba51c87ef5f5d5521c2a0d6
    air_pipeline_alias: 75bcd81d996c93595492e61860a34b3c8f6dfe51
    atmosphere_workflow: a3c6a21db798b02202c87f76bfba5f45c5f08c9b
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    generated_receipt_schema: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  bounded_inventory_note: >
    Indexed search and named-path probes establish only the checked snapshot. They do not prove
    permanent absence from history, forks, ignored files, generated workspaces, dynamic test
    generation, Git LFS, external stores, or differently named paths.
related:
  - ../README.md
  - ../atmosphere/README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../policy/domains/air/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../pipeline_specs/air/README.md
  - ../../../pipeline_specs/atmosphere/README.md
  - ../../../pipelines/domains/air/README.md
  - ../../../pipelines/domains/atmosphere/README.md
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../Makefile
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, tests, air, atmosphere, compatibility, slug-drift, alias, redirect, migration, no-network, fail-closed, evidence, policy, release, correction, rollback, official-authority-redirect]
notes:
  - "This revision changes only tests/domains/air/README.md; a generated provenance receipt is paired separately."
  - "The Air test path remains a compatibility guardrail and must not receive executable tests while the domain slug remains unresolved."
  - "New Atmosphere/Air domain tests belong under tests/domains/atmosphere/ unless an accepted ADR explicitly selects or authorizes the air segment."
  - "No test, fixture, contract, schema, policy, validator, pipeline, workflow, source record, lifecycle object, receipt/proof instance, release object, runtime behavior, alerting behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/air/` — Air Slug Compatibility Test Guardrail

> **One-line purpose.** Preserve an inspectable compatibility boundary for the unresolved `air` domain slug, redirect executable Atmosphere/Air tests to [`tests/domains/atmosphere/`](../atmosphere/README.md), and prevent alias paths from becoming duplicate test, fixture, policy, evidence, release, or public authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Authority: compatibility only" src="https://img.shields.io/badge/authority-compatibility__only-orange">
  <img alt="Preferred lane: atmosphere" src="https://img.shields.io/badge/preferred-tests%2Fdomains%2Fatmosphere%2F-success">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="ADR: required" src="https://img.shields.io/badge/slug__ADR-required-critical">
  <img alt="Emergency authority: official issuer" src="https://img.shields.io/badge/emergency__authority-official__issuer-red">
</p>

> [!IMPORTANT]
> **This directory is a compatibility guardrail, not a second Atmosphere test package.** Path presence, README completeness, imported aliases, or a green test run must not activate `air` as a canonical domain segment. Until an accepted ADR or governing lane register resolves the naming decision, new executable domain tests belong under `tests/domains/atmosphere/`.

> [!CAUTION]
> **Current executable coverage is not established here.** Bounded repository search surfaced only this README under `tests/domains/air/`. The preferred Atmosphere parent and several child READMEs are present, but their executable tests, fixtures, validators, policy bundles, and substantive CI coverage remain verification-bound.

> [!WARNING]
> **KFM is not an emergency-alerting or life-safety issuing authority.** Air-quality, weather, smoke, aerosol, model, forecast, and advisory tests may prove source-role, knowledge-character, evidence, caveat, and official-authority-redirection boundaries. They must not convert KFM into the issuer of warnings, protective actions, or emergency instructions.

**Quick links:** [Purpose](#purpose) · [Status](#current-evidence-and-maturity) · [Authority](#authority-and-directory-rules-basis) · [Slug](#slug-conflict-and-compatibility-contract) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Redirect](#redirect-and-migration-behavior) · [Atmosphere lane](#preferred-atmosphere-test-surface) · [Invariants](#compatibility-invariants) · [Cases](#required-case-matrix) · [Outcomes](#finite-outcomes-and-reason-code-posture) · [Network](#no-network-rights-and-sensitive-test-data) · [Commands](#deterministic-inventory-and-execution-commands) · [Failures](#failure-interpretation) · [Passing](#what-a-passing-check-does-not-prove) · [CI](#ci-and-promotion-boundary) · [Review](#review-burden-and-change-discipline) · [Migration](#adr-migration-correction-and-rollback) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Changelog](#changelog-correction-and-rollback)

---

## Purpose

`tests/domains/air/` exists because the repository contains a historical or proposed `air` domain segment while current Directory Rules and Atmosphere placement documentation prefer `atmosphere` for new domain lanes.

Its durable question is:

> Can the repository preserve the `air` alias as an inspectable compatibility surface without allowing it to create duplicate test discovery, fixture authority, contract/schema/policy meaning, source identity, evidence behavior, release semantics, public routes, or life-safety claims?

This path should support only these functions:

1. document the unresolved `air` versus `atmosphere` naming conflict;
2. redirect contributors and test discovery toward the preferred Atmosphere lane;
3. define tests that a future migration or alias strategy must pass;
4. prevent duplicate collection and divergent expectations across both slugs;
5. preserve historical references long enough for reviewed migration, correction, or deprecation;
6. keep evidence, policy, release, correction, and rollback semantics unchanged by slug choice.

It is not a place to implement Atmosphere behavior while governance remains unresolved.

[Back to top](#top)

---

## Current evidence and maturity

### Safe conclusion

The repository contains both `tests/domains/air/` and `tests/domains/atmosphere/`, but their roles are not equivalent:

- `tests/domains/air/` is confirmed as a README-only compatibility stub at the pinned snapshot.
- `tests/domains/atmosphere/` is the preferred domain test parent in current repository documentation.
- the parent `tests/domains/README.md` indexes `atmosphere/` as a domain package and states that compatibility lanes must document their canonical relationship and avoid parallel authority;
- Atmosphere canonical-path documentation says new work should use `atmosphere/` until an ADR resolves the segment;
- `policy/domains/air/` and `pipeline_specs/air/` already define their `air` paths as compatibility or slug-conflict guardrails;
- `pipelines/domains/air/` records itself as an alias candidate or transitional lane;
- the `domain-atmosphere` workflow runs TODO echo commands and does not establish substantive Atmosphere test enforcement;
- `make test` currently runs only `tests/schemas` and `tests/contracts`, not either Atmosphere domain lane.

### Maturity matrix

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `tests/domains/air/` | **CONFIRMED README-only** | Compatibility documentation exists; no executable direct-lane test surfaced. |
| `tests/domains/atmosphere/` | **CONFIRMED parent README / scaffold** | Preferred test parent exists; executable coverage remains unestablished. |
| Atmosphere child test lanes | **README-backed scaffolds** | Schema, source-role, knowledge-character, unit, policy-deny, and no-network responsibilities are documented; implementation remains verification-bound. |
| `docs/domains/atmosphere/CANONICAL_PATHS.md` | **CONFIRMED draft registry** | Uses `atmosphere` for new paths and treats `air` as ADR-class drift. |
| `policy/domains/air/` | **CONFIRMED compatibility guardrail** | Must not become a second active policy authority. |
| `pipeline_specs/air/` | **CONFIRMED compatibility guardrail** | No active Air specification established by bounded evidence. |
| `pipelines/domains/air/` | **CONFIRMED alias-candidate README** | Canonical executable slug remains unresolved. |
| Domain workflow | **CONFIRMED TODO-only** | Green status cannot prove test, evidence, policy, proof, or release behavior. |
| Default Make target | **CONFIRMED excludes domain lanes** | `make test` does not execute `tests/domains/air/` or `tests/domains/atmosphere/`. |
| Canonical slug decision | **CONFLICTED / NEEDS VERIFICATION** | No accepted ADR or lane-register decision was verified. |
| Runtime and public aliases | **UNKNOWN** | No active route, loader, test-discovery alias, or release mapping is claimed here. |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from repository files or bounded connector search at the pinned snapshot. |
| `PROPOSED` | A safe compatibility, test, migration, or validation design not established as implemented authority. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently verified to act as fact. |
| `CONFLICTED` | Repository surfaces disagree or coexist without a governing decision. |

[Back to top](#top)

---

## Authority and Directory Rules basis

### Responsibility root

Directory Rules place enforceability proof under `tests/` and domain-specific tests under `tests/domains/<domain>/`. The target therefore has the correct **responsibility root** but an unresolved **domain segment**.

```text
tests/                         = canonical enforceability root
tests/domains/atmosphere/      = preferred Atmosphere test lane pending ADR
tests/domains/air/             = compatibility and migration guardrail only
```

### Authority split

| Concern | Authority home | Relationship of this path |
|---|---|---|
| Atmosphere/Air test implementation | `tests/domains/atmosphere/` until ADR resolution | Redirect target; executable tests should live there. |
| Test-domain parent index | `tests/domains/README.md` | Classifies domain and compatibility lanes. |
| Human-facing domain placement | `docs/domains/atmosphere/CANONICAL_PATHS.md` | Records `air` versus `atmosphere` as ADR-class. |
| Atmosphere object meaning | `contracts/domains/atmosphere/` or ADR-accepted home | Referenced; never defined here. |
| Atmosphere machine shape | `schemas/contracts/v1/domains/atmosphere/` or ADR-accepted home | Referenced; never authored here. |
| Atmosphere policy | `policy/domains/atmosphere/` or ADR-accepted home | Tested elsewhere; not defined here. |
| Source identity and rights | `data/registry/sources/atmosphere/` and policy roots | Not owned here. |
| Reusable fixtures | `fixtures/domains/atmosphere/` or ADR-accepted home | Must not be duplicated under the alias. |
| Validators | `tools/validators/` | Called by tests; not implemented here. |
| Lifecycle data, receipts, proofs | `data/` responsibility lanes | Never stored here. |
| Release, correction, rollback | `release/` | Never decided here. |
| Public API/UI/map/AI behavior | governed application and package roots | May be tested from canonical lanes; not served here. |

> [!IMPORTANT]
> A README can document a conflict. It cannot choose the canonical slug, activate test discovery, authorize a migration, or make an alias authoritative.

### ADR trigger

Choosing `air` as canonical, activating both slugs, or creating parallel schema, contract, policy, source, registry, release, proof, or receipt homes is ADR-class under Directory Rules. This update makes no such decision.

[Back to top](#top)

---

## Slug conflict and compatibility contract

### Current posture

Until an accepted ADR or governing domain-lane register resolves the choice:

- use `atmosphere` for new domain test paths;
- keep `tests/domains/air/` documentation-only;
- do not add executable `test_*.py`, `conftest.py`, fixtures, snapshots, generated outputs, policy bundles, schemas, contracts, or source records here;
- do not configure pytest, build tools, CI, import aliases, package discovery, or release tooling to collect both domains as independent suites;
- preserve existing references long enough to migrate them through reviewed, reversible change;
- record any exception as `CONFLICTED` and link the governing ADR or migration record.

### Compatibility-lane contract

| Rule | Required behavior |
|---|---|
| Documentation only | This directory contains this README and, only when needed, migration/deprecation notes approved by reviewers. |
| Redirect new work | Contributors are directed to `tests/domains/atmosphere/`. |
| No duplicate collection | A test case must not run once under `air` and again under `atmosphere`. |
| No duplicate fixture home | Reusable Atmosphere fixtures remain in one accepted lane. |
| No semantic fork | Slug choice must not change object meaning, source role, knowledge character, units, time, evidence, caveats, policy, or release rules. |
| No silent alias activation | Path existence or importability must not select `air` as canonical. |
| Preserve correction lineage | Historical references are migrated with explicit mapping and rollback. |
| Fail closed | Unresolved authority returns `REDIRECT`, `HOLD`, `ABSTAIN`, `DENY`, or `ERROR`; never implicit `ALLOW`. |

### Disallowed collapses

```text
README presence                    -> active test package
compatibility path                 -> canonical domain
same test under two slugs          -> broader coverage
green TODO workflow                -> executable enforcement
valid schema                       -> valid evidence or policy
AQI                                -> pollutant concentration
AOD                                -> PM2.5 observation
model or forecast                  -> observation
low-cost sensor value              -> regulatory observation
advisory context                   -> official warning
passing test                       -> release approval
generated explanation              -> evidence
```

[Back to top](#top)

---

## What belongs here

Only compatibility-governance documentation belongs in this path while the slug remains unresolved:

- this README;
- a short migration map, deprecation notice, or redirect note when approved in the same change as the governing decision;
- references to the accepted ADR, drift entry, lane-register decision, correction notice, or rollback plan;
- documentation of a bounded alias test that lives in the canonical test lane;
- history-preserving notes needed to explain why the directory remains present.

Any future additional file must answer all of these questions:

1. Why can it not live under `tests/domains/atmosphere/`?
2. Which accepted ADR authorizes the `air` path?
3. Does it create duplicate test collection or fixture ownership?
4. How is migration and rollback handled?
5. Which reviewer owns the compatibility period?
6. When does the file expire or become removable?

If those questions cannot be answered, do not add the file.

[Back to top](#top)

---

## What does not belong here

| Excluded material | Correct home or action |
|---|---|
| Executable Atmosphere/Air domain tests | `tests/domains/atmosphere/` until ADR resolution. |
| `conftest.py`, pytest plugins, test-discovery hooks, aliases | Canonical test tooling or the accepted Atmosphere lane. |
| Reusable fixtures or snapshots | `fixtures/domains/atmosphere/` or ADR-accepted fixture home. |
| Tiny local examples used by executable tests | Keep beside the canonical test, not in the alias directory. |
| Semantic contracts | `contracts/domains/atmosphere/` or ADR-accepted home. |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/` or ADR-accepted home. |
| Policy modules or bundles | `policy/domains/atmosphere/` or ADR-accepted home. |
| Source descriptors and source registry entries | `data/registry/sources/atmosphere/` or accepted source home. |
| Validator implementation | `tools/validators/` or accepted validator package. |
| Pipeline code or specifications | `pipelines/domains/atmosphere/`, `pipeline_specs/atmosphere/`, or ADR-accepted homes. |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED data | `data/` lifecycle lanes. |
| Receipts, proofs, catalog records, release records | Their owning `data/` or `release/` roots. |
| Public API, map, tile, export, screenshot, report, search, graph, or AI output | Governed application/artifact lanes after release. |
| Real credentials, private endpoints, production logs, or sensitive payloads | Never in this documentation lane. |
| Emergency advisories, protective actions, or life-safety instructions | Official issuing authority; KFM may redirect and cite context only. |

[Back to top](#top)

---

## Redirect and migration behavior

### Contributor redirect

A contributor attempting to add a test under this path should receive a safe, inspectable response:

```text
REDIRECT
preferred_path: tests/domains/atmosphere/
reason_code: AIR_ALIAS_REDIRECT_REQUIRED
required_action: move proposed test to the preferred Atmosphere lane or cite an accepted ADR
```

The redirect must not silently move files, rewrite history, or create duplicate copies.

### Discovery redirect

Test-discovery and CI configuration should select one canonical lane. Until the slug is resolved:

- include `tests/domains/atmosphere/` when domain tests are explicitly enabled;
- exclude `tests/domains/air/` from executable discovery;
- treat executable files discovered under `air/` as a validation failure or migration hold;
- detect duplicate node IDs, parametrization IDs, snapshots, fixture IDs, report keys, and coverage paths across both slugs.

### Migration sequence

A safe migration or alias strategy should include:

1. accepted ADR or governing lane-register decision;
2. complete inventory of `air` and `atmosphere` paths across all responsibility roots;
3. source-of-truth path map and compatibility window;
4. collision checks for test IDs, schema IDs, contract IDs, source IDs, fixture IDs, release IDs, and public routes;
5. history-preserving operations where files move;
6. redirect or deprecation behavior with explicit expiry;
7. updated CI, CODEOWNERS, registries, docs, imports, release maps, correction paths, and rollback references;
8. positive and negative migration tests;
9. generated receipt and human review;
10. rollback rehearsal before compatibility removal.

### No automatic cleanup

This README does not authorize deletion of the alias directory. Removal is a governed migration decision and should preserve reviewable lineage.

[Back to top](#top)

---

## Preferred Atmosphere test surface

Current repository documentation identifies [`tests/domains/atmosphere/`](../atmosphere/README.md) as the domain test parent.

### Documented child responsibilities

| Child responsibility | Preferred location | Current documentation posture |
|---|---|---|
| Schema conformance | `tests/domains/atmosphere/schema/` | README/scaffold; executable coverage NEEDS VERIFICATION. |
| Source-role anti-collapse | `tests/domains/atmosphere/source-role/` | README/scaffold; executable coverage NEEDS VERIFICATION. |
| Knowledge-character boundaries | `tests/domains/atmosphere/knowledge-character/` | README/scaffold; executable coverage NEEDS VERIFICATION. |
| Unit normalization | `tests/domains/atmosphere/unit-normalization/` | README/scaffold; executable coverage NEEDS VERIFICATION. |
| Policy denial | `tests/domains/atmosphere/policy-deny/` | README/scaffold; executable policy and fixtures NEEDS VERIFICATION. |
| No-network fixtures | `tests/domains/atmosphere/no-network-fixtures/` | Documentation posture; fixture inventory NEEDS VERIFICATION. |
| No-network behavior | `tests/domains/atmosphere/no-network/` | Documentation posture; enforcement NEEDS VERIFICATION. |

### Domain distinctions those tests must preserve

- `AQI` is report or index context, not pollutant concentration.
- `AOD` is aerosol optical depth context, not PM2.5 measurement.
- modeled and forecast fields are not observations.
- advisory context is not official warning authority.
- low-cost sensor values require calibration, caveat, confidence, limitation, and correction posture.
- source, observed, valid, issue, retrieval, processing, release, and correction times remain distinct where material.
- units, averaging periods, methods, quality flags, and no-data semantics remain explicit.
- evidence-dependent statements resolve support or abstain.
- passing tests remain subordinate to policy, review, release, correction, and rollback.

This compatibility README does not duplicate those test specifications. It points to their preferred home and tests the alias boundary around them.

[Back to top](#top)

---

## Compatibility invariants

| Invariant | Required behavior | Failure outcome |
|---|---|---|
| Single test authority | Only one domain slug is executable for a given Atmosphere test family. | `FAIL` / `HOLD`. |
| Single fixture authority | Reusable fixture IDs and payloads have one accepted home. | `FAIL` / `REDIRECT`. |
| Stable object meaning | `air` and `atmosphere` aliases cannot change contract semantics. | `DENY` / validation failure. |
| Stable source role | Alias mapping cannot upcast context, modeled, aggregate, advisory, or low-cost sensor material into observation or authority. | `DENY` / `ABSTAIN`. |
| Stable knowledge character | AQI, AOD, smoke, forecast, observation, and advisory distinctions survive alias resolution. | `DENY` / validation failure. |
| Stable temporal scope | Alias mapping preserves time kinds and stale/correction state. | `ABSTAIN` / validation failure. |
| Stable evidence | EvidenceRef and EvidenceBundle identifiers do not fork by slug. | `HOLD` / `ABSTAIN`. |
| Stable policy | The same request cannot receive different policy outcomes solely because a path uses `air` or `atmosphere`. | `ERROR` / `HOLD`. |
| Stable release identity | Release, correction, withdrawal, supersession, and rollback references use the accepted canonical identity. | promotion block. |
| No public alias leakage | Public URLs, tiles, exports, reports, screenshots, search results, graph edges, or AI answers cannot expose unresolved internal slug drift as truth. | `DENY` / `ERROR`. |
| Official-authority boundary | Advisory or hazard context redirects to the official issuing authority. | `DENY` / `REDIRECT`. |
| No-network default | Compatibility checks use local synthetic inventory and do not call live services. | `ERROR`. |

[Back to top](#top)

---

## Required case matrix

A future executable compatibility suite should include both positive controls and failure cases.

| Case | Input condition | Expected result | Why |
|---|---|---|---|
| Preferred-lane positive control | Test exists only under `atmosphere/` and has no alias duplicate. | `PASS`. | Confirms ordinary canonical placement. |
| Air README only | Alias directory contains only this guardrail README. | `PASS`. | Confirms documentation-only compatibility posture. |
| Executable file under Air | `test_*.py`, `conftest.py`, plugin, or runner config appears under `air/` without ADR support. | `FAIL` / `HOLD`. | Prevents silent activation. |
| Duplicate test body | Equivalent tests exist under both slugs. | `FAIL`. | Prevents double collection and divergent maintenance. |
| Duplicate test ID | Same node ID, parametrization ID, case ID, or snapshot key appears under both slugs. | `FAIL`. | Prevents ambiguous reports. |
| Duplicate fixture ID | Same reusable fixture is copied under both slugs. | `FAIL` / `REDIRECT`. | Preserves fixture authority. |
| Alias-only import | Code imports an Air test helper that has no ADR-approved compatibility contract. | `REDIRECT` / `HOLD`. | Prevents hidden canonicalization. |
| Conflicting expectations | Same payload passes in one slug and fails in the other. | `ERROR` / `HOLD`. | Reveals semantic fork. |
| Conflicting policy result | Same request receives `ALLOW` under one slug and `DENY` under the other. | `ERROR` / promotion block. | Policy cannot depend on unresolved path naming. |
| Evidence fork | Same claim resolves different EvidenceBundle identifiers by slug. | `HOLD` / `ABSTAIN`. | Evidence identity must remain stable. |
| Release slug mismatch | Candidate, manifest, correction, or rollback references both slugs inconsistently. | promotion block. | Release lineage must be unambiguous. |
| AQI as concentration | Alias transform relabels AQI as pollutant concentration. | `DENY`. | Knowledge-character collapse. |
| AOD as PM2.5 | Alias transform relabels AOD as measured PM2.5. | `DENY`. | Source/knowledge collapse. |
| Model as observation | Forecast/model field is exposed as observed measurement. | `DENY` / `ABSTAIN`. | Evidence character is wrong. |
| Advisory as warning | KFM alias route issues life-safety instruction. | `DENY` / `REDIRECT`. | Official authority boundary. |
| Network attempt | Alias test performs DNS, HTTP, socket, cloud, model, map-service, or source call. | `ERROR`. | Default suite must be deterministic. |
| Missing ADR | Migration or activation is attempted without accepted decision. | `HOLD` / `REDIRECT`. | Governance prerequisite absent. |
| Accepted migration | ADR, inventory, history-preserving move, tests, receipts, and rollback are present. | scoped `PASS`. | Confirms governed transition, not automatic publication. |
| Rollback rehearsal | Migration can restore prior paths and references without evidence or release loss. | `PASS` or `ERROR` with safe reason. | Preserves reversibility. |

### Fixture rules for these cases

Compatibility cases should use path manifests and synthetic metadata, not real atmospheric measurements. A minimal case may list:

- synthetic path;
- synthetic file role;
- canonical slug expectation;
- test/fixture/schema/policy/release identifier;
- expected finite outcome;
- safe reason code;
- migration or ADR reference when applicable.

Do not copy real source data into this alias lane to test path routing.

[Back to top](#top)

---

## Finite outcomes and reason-code posture

### Layered outcomes

| Layer | Outcomes | Boundary |
|---|---|---|
| Test runner | pass, fail, skip, error according to the framework | Framework result only. |
| Compatibility validator | `PASS`, `REDIRECT`, `HOLD`, `FAIL`, `ERROR` | Path and migration result; not policy or release authority. |
| Policy/public boundary | `ALLOW`, `RESTRICT`, `ABSTAIN`, `DENY`, `ERROR` | Must come from governing policy/runtime, not this README. |
| Migration workflow | `PROPOSED`, `NEEDS_REVIEW`, `APPROVED`, `BLOCKED`, `ROLLED_BACK`, `ERROR` | Review state; not publication. |

### Proposed safe reason codes

| Reason code | Meaning |
|---|---|
| `AIR_SLUG_UNRESOLVED` | No accepted decision establishes the canonical segment. |
| `AIR_ALIAS_REDIRECT_REQUIRED` | New work must use the preferred Atmosphere lane. |
| `AIR_EXECUTABLE_FILE_FORBIDDEN` | Executable test material appeared under the compatibility path without authorization. |
| `AIR_DUPLICATE_TEST_AUTHORITY` | Equivalent test ownership exists under both slugs. |
| `AIR_DUPLICATE_FIXTURE_HOME` | Reusable fixture ownership is duplicated. |
| `AIR_TEST_ID_COLLISION` | Test, case, snapshot, or report identity collides across slugs. |
| `AIR_SEMANTIC_FORK` | Alias selection changes object meaning or test expectation. |
| `AIR_POLICY_DIVERGENCE` | Alias selection changes a policy result. |
| `AIR_EVIDENCE_FORK` | Alias selection changes evidence identity or closure. |
| `AIR_RELEASE_SLUG_MISMATCH` | Release/correction/rollback lineage uses inconsistent slugs. |
| `AIR_ADR_REQUIRED` | Activation, migration, or canonicalization lacks an accepted ADR. |
| `AIR_MIGRATION_INCOMPLETE` | Inventory, redirects, tests, receipts, or rollback are incomplete. |
| `AIR_OFFICIAL_AUTHORITY_REDIRECT` | Emergency or advisory request must redirect to the official issuer. |
| `AIR_NETWORK_ACCESS_FORBIDDEN` | A default compatibility test attempted a live call. |
| `AIR_TEST_DISCOVERY_EMPTY` | A command collected no meaningful tests and cannot be reported as pass. |
| `AIR_UNEXPECTED_ERROR` | Tooling or repository inspection failed safely. |

Reason codes should not contain sensitive payloads, credentials, private endpoints, or internal policy details.

[Back to top](#top)

---

## No-network, rights, and sensitive test data

### Default execution posture

Compatibility checks should operate on repository paths, metadata, synthetic manifests, and local configuration only. They must not:

- resolve DNS or open sockets;
- call EPA, AirNow, NOAA, NWS, NASA, ECMWF, OpenAQ-like, sensor, smoke, weather, climate, map, release, or model services;
- load credentials, tokens, private endpoints, or developer-local caches;
- write public artifacts or lifecycle records;
- call a live AI provider;
- mutate release, alias, registry, or public-route state.

### Sensitive and high-consequence material

Even path tests can leak or normalize unsafe assumptions. Fixtures and logs must not include:

- exact non-public sensor or infrastructure locations;
- private endpoints or source credentials;
- proprietary observation feeds;
- restricted low-cost sensor identifiers tied to private parties;
- real emergency-response or protective-action instructions;
- unreviewed vulnerability, infrastructure, or operational details;
- production EvidenceBundles, receipts, proofs, release manifests, rollback cards, or audit records.

Use synthetic identifiers such as `fixture://air-alias/example-001` and obvious mock markers.

### Life-safety rule

A compatibility test may verify that KFM returns an official-authority redirect. It must not embed or approve operational instructions. Current conditions, warnings, and protective actions remain the responsibility of the official issuing source.

[Back to top](#top)

---

## Deterministic inventory and execution commands

### Safe inventory commands

```bash
find tests/domains/air tests/domains/atmosphere -maxdepth 5 -type f 2>/dev/null | sort
find fixtures/domains/air fixtures/domains/atmosphere -maxdepth 5 -type f 2>/dev/null | sort
find contracts schemas policy pipelines pipeline_specs data release docs -maxdepth 7 -type f 2>/dev/null \
  | grep -E '/(air|atmosphere)/' \
  | sort
find docs/adr docs/registers control_plane -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'air|atmosphere|alias|drift|deprecat|migration' \
  | sort
```

These commands inventory paths. They do not decide which path is authoritative.

### Current repository-native commands

```bash
make test
make schemas
```

Inspected behavior:

- `make test` runs `python -m pytest tests/schemas tests/contracts -q`; it does not execute either Atmosphere domain lane.
- `make schemas` runs the shared schema validator orchestrator; it does not establish Air/Atmosphere alias or domain-test coverage.

### Diagnostic domain command

```bash
python -m pytest tests/domains/atmosphere -q
```

This is a diagnostic candidate only. It is not an accepted green gate until test collection, fixture coverage, validator/policy dependencies, expected outcomes, CI ownership, and pass significance are verified.

Do not use:

```bash
python -m pytest tests/domains/air -q
```

as evidence of coverage. The direct lane is README-only in bounded evidence. A no-tests-collected or documentation-only result is a gap, not a pass.

### Future alias-guard command

A mature repository may add a stable command such as:

```bash
make test-atmosphere-alias-guard
```

It should inspect both slugs without collecting the compatibility path as an independent test package.

[Back to top](#top)

---

## Failure interpretation

| Observed result | Interpretation | Required action |
|---|---|---|
| No executable files under `air/` | Expected compatibility posture. | Keep guardrail and verify Atmosphere coverage separately. |
| No Atmosphere tests collected | Coverage gap. | Do not label pass; implement scoped canonical tests. |
| Executable file appears under `air/` | Unauthorized activation or migration drift. | `HOLD`; move or justify through ADR. |
| Same test collected twice | Duplicate authority. | Fail and remove one executable source. |
| Same fixture copied twice | Fixture-authority drift. | Fail; select one canonical fixture and migrate references. |
| Same case differs by slug | Semantic or policy fork. | `ERROR` / `HOLD`; investigate before release. |
| Workflow succeeds on TODO echo | Scaffold success only. | Do not describe as substantive validation. |
| Workflow fails on unrelated prerequisite | Repository prerequisite or infrastructure issue. | Record accurately; do not broaden this README change automatically. |
| Public route exposes both slugs | Compatibility leakage. | `DENY` or staged redirect until reviewed. |
| Migration has no rollback | Irreversible governance change. | Block migration. |
| Error output leaks sensitive material | Security failure. | Minimize, redact, quarantine, and review. |

An alias guard should prefer honest failure over silent normalization.

[Back to top](#top)

---

## What a passing check does not prove

A passing compatibility check does **not** prove that:

- `air` or `atmosphere` has been accepted as the canonical slug;
- Atmosphere schemas or contracts are complete;
- policy bundles are active or correct;
- source descriptors, rights, licenses, endpoints, or source roles are verified;
- observations, AQI, AOD, smoke, forecast, climate, or advisory claims are scientifically valid;
- fixtures represent real source truth;
- executable Atmosphere domain tests have meaningful coverage;
- validators, evidence resolution, catalog closure, release, correction, withdrawal, or rollback work in production;
- CI checks are required by branch protection;
- public API, map, tile, export, search, graph, report, screenshot, or AI behavior is safe;
- KFM is authorized to issue emergency or life-safety information;
- a release or publication decision has occurred.

Passing means only that the bounded alias expectation behaved as asserted against the checked repository state and synthetic inputs.

[Back to top](#top)

---

## CI and promotion boundary

### Inspected workflow

| Workflow | Trigger | Inspected behavior | Substantive proof? |
|---|---|---|---|
| `domain-atmosphere` | pull request and push to `main` | Checkout plus TODO echo steps for validate, proof build, and publish dry run. | No. |

### Requirements before CI can enforce this guardrail

1. one accepted canonical slug or explicit alias strategy;
2. a complete path inventory and migration map;
3. executable alias-guard tests in a canonical test/tool lane;
4. deterministic synthetic fixtures or path manifests;
5. duplicate collection and fixture-ID checks;
6. policy/evidence/release identity consistency checks where applicable;
7. no-network enforcement;
8. safe, structured failure output;
9. retained reports without sensitive data;
10. workflow path filters and required-check status verified;
11. correction and rollback procedures tested;
12. owners and CODEOWNERS established.

### Promotion rule

A green alias guard may support repository hygiene review. It cannot approve a domain slug, migrate files, activate policy, admit a source, promote lifecycle material, approve a release, or publish a public alias.

[Back to top](#top)

---

## Review burden and change discipline

Changes to this README require at least:

- Atmosphere/Air domain review;
- test/QA review;
- Directory Rules or architecture review;
- docs review.

Changes that activate, migrate, deprecate, delete, or redirect executable behavior also require the relevant schema, contract, fixture, policy, source, evidence, pipeline, release, security, and CI owners.

### Smallest-change rule

This compatibility README should remain narrow. Do not use it to solve the slug conflict by prose. Prefer:

1. inventory;
2. ADR or lane-register decision;
3. migration plan;
4. executable guard;
5. reviewed move or alias implementation;
6. rollback rehearsal;
7. deprecation closeout.

### Workflow-trigger threat preflight

A pull request touching this file may trigger repository workflows. Reviewers should confirm that workflows:

- use least-privilege permissions;
- do not expose secrets to untrusted code;
- do not auto-publish or mutate release state;
- do not treat TODO echo success as promotion proof;
- do not infer slug authority from the changed path.

[Back to top](#top)

---

## ADR, migration, correction, and rollback

### ADR decision scope

The governing decision should specify:

- canonical domain segment: `atmosphere`, `air`, or an explicit alias strategy;
- which responsibility roots are affected;
- public and internal identifier policy;
- test, fixture, schema, contract, policy, source, evidence, release, and route migration rules;
- compatibility window and removal criteria;
- correction and rollback behavior;
- steward ownership and review requirements.

### Migration acceptance matrix

| Criterion | Required result |
|---|---|
| Full path inventory | `PASS` |
| Canonical slug decision | `PASS` |
| Duplicate test/fixture IDs | none |
| Semantic and policy parity | `PASS` |
| Evidence and release identity parity | `PASS` |
| Import and public-route mapping | reviewed |
| History preservation | `PASS` |
| Correction propagation | `PASS` or documented non-applicability |
| Rollback rehearsal | `PASS` |
| Human review | approved |

### Correction path

If this README misstates current repository evidence:

1. identify the exact claim and pinned snapshot;
2. replace or narrow the claim using current evidence;
3. update the evidence snapshot and ledger;
4. update the generated receipt;
5. update linked compatibility docs if the correction is cross-root;
6. record the correction in the changelog;
7. keep activation and public use on hold until material corrections propagate.

### Rollback path

This documentation revision is reversible by restoring the prior blob:

```text
810432ee7db80d18ff8d0aa1b1885239d6622536
```

Rollback should also remove the paired generated receipt through a reviewed Git change. It does not alter tests, fixtures, source data, schemas, policy, pipelines, releases, routes, or public state because this revision changes none of them.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Accepted canonical domain segment | `NEEDS VERIFICATION` | Accepted ADR or governing domain-lane register. |
| Complete `air` and `atmosphere` path inventory | `NEEDS VERIFICATION` | Recursive tree at pinned commit plus generated/ignored path review. |
| Executable test files under either domain lane | `UNKNOWN` beyond bounded checks | Full recursive inventory and pytest collection report. |
| Reusable fixture payload inventory | `NEEDS VERIFICATION` | Fixture manifest and consumer map. |
| Active policy bundle and package namespace | `UNKNOWN` | Bundle manifest, evaluator query, tests, CI. |
| Canonical schema and contract aliases | `CONFLICTED` | ADR, registry, migration record, validator parity. |
| Source descriptor and registry identity behavior | `UNKNOWN` | Source registry records and resolver tests. |
| EvidenceRef/EvidenceBundle alias behavior | `UNKNOWN` | Resolver tests and identity contract. |
| Release/correction/rollback slug behavior | `UNKNOWN` | Release manifests, correction/rollback tests, route mapping. |
| Public API/UI/map alias behavior | `UNKNOWN` | Route registry, integration tests, released manifests. |
| CI alias-guard job | `NOT ESTABLISHED` | Workflow with substantive command and retained report. |
| Branch-protection requirement | `UNKNOWN` | Repository ruleset or protection evidence. |
| Owners and CODEOWNERS | `NEEDS VERIFICATION` | Accepted ownership records. |
| Compatibility expiration/removal criteria | `NEEDS VERIFICATION` | ADR migration plan and deprecation register. |
| Rollback automation | `UNKNOWN` | Tested rollback command and receipt. |

Open items are not permission to guess. They are blockers or scoped follow-up work.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `tests/domains/air/README.md` prior blob | `CONFIRMED` | Target existed as a nine-line compatibility stub directing work to Atmosphere. | Does not prove executable behavior. |
| `tests/domains/README.md` | `CONFIRMED` | Atmosphere is indexed as a domain package; compatibility lanes must avoid parallel authority. | Does not list every path or executable test. |
| `tests/domains/atmosphere/README.md` | `CONFIRMED scaffold` | Preferred Atmosphere parent, documented child responsibilities, no-network and finite-outcome posture. | Executable coverage remains unverified. |
| Atmosphere policy-deny child README | `CONFIRMED scaffold` | Negative, fail-closed, evidence, policy, and official-authority boundaries. | Policy bundle and tests remain unverified. |
| `docs/doctrine/directory-rules.md` | `CONFIRMED doctrine` | Tests own enforceability; domains are segments; parallel authority and unresolved placement require ADR/drift handling. | Does not choose the current slug by itself beyond doctrine preference. |
| `docs/domains/atmosphere/README.md` | `CONFIRMED draft domain doc` | Atmosphere/Air scope, anti-collapse rules, preferred lane map, slug conflict. | Current runtime/source/release maturity remains unverified. |
| `docs/domains/atmosphere/CANONICAL_PATHS.md` | `CONFIRMED draft registry` | Uses `atmosphere` for new paths and treats `air` as ADR-class drift. | Registry itself is draft and needs accepted governance decision. |
| `policy/domains/air/README.md` | `CONFIRMED guardrail` | Air policy path is compatibility-only and must not activate. | Does not prove policy enforcement. |
| `pipeline_specs/air/README.md` | `CONFIRMED guardrail` | Air spec path is compatibility-only; Atmosphere is preferred. | No active spec or parser is established. |
| `pipelines/domains/air/README.md` | `CONFIRMED alias-candidate doc` | Executable slug remains unresolved; avoid parallel authority. | Does not prove executable pipeline behavior. |
| `.github/workflows/domain-atmosphere.yml` | `CONFIRMED TODO scaffold` | PR/push triggers exist; jobs only echo TODO. | Green status is not substantive proof. |
| `Makefile` | `CONFIRMED` | Default `make test` excludes domain test lanes. | Does not describe all CI or ad hoc commands. |
| Generated receipt schema | `CONFIRMED` | Defines provenance fields and validation vocabulary for this AI-authored README. | Receipt records generation; it does not approve merge or release. |
| Bounded repository search | `CONFIRMED performed` | Surfaced only this README in the direct Air test lane and no matching open PR/branch. | Not an exhaustive recursive or historical proof. |

[Back to top](#top)

---

## Changelog, correction, and rollback

### v0.2 — 2026-07-16

- replaced the nine-line compatibility stub with a repository-grounded compatibility-test guardrail;
- retained the original instruction to use `tests/domains/atmosphere/` for implementation work;
- added Directory Rules and ADR basis;
- documented the direct lane as README-only in bounded evidence;
- mapped related Air compatibility surfaces in policy, pipeline specs, and pipelines;
- added alias invariants, duplicate-authority checks, case matrix, finite outcomes, reason codes, no-network posture, and official-authority redirect requirements;
- documented current Makefile and TODO-only workflow limits;
- added migration, correction, rollback, evidence, and open-verification controls;
- created no executable tests or authority-bearing artifacts.

### What did not change

- No test collection or executable code.
- No fixture or source payload.
- No contract, schema, policy, validator, connector, pipeline, pipeline specification, workflow, lifecycle record, catalog record, evidence object, receipt/proof instance, release object, public route, map layer, UI behavior, export, search, graph, or AI behavior.
- No canonical slug decision, migration, deletion, source activation, promotion, release, correction, withdrawal, rollback execution, or publication.

### Human review

Human review remains pending. The generated receipt documents provenance and validation; it is not approval.

---

**Last reviewed:** 2026-07-16  
**Implementation posture:** compatibility documentation only; executable Air test coverage is not established  
**Preferred lane:** `tests/domains/atmosphere/`  
**Canonical slug:** `CONFLICTED / NEEDS VERIFICATION`  
**Publication posture:** no release, alert, or publication authority

[Back to top](#top)
