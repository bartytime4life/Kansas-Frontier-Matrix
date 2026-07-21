# Fauna compatibility fixtures

> **One-line purpose.** `fixtures/fauna/` is a transitional compatibility and routing lane for synthetic Fauna fixture references; reusable Fauna payloads belong under `fixtures/domains/fauna/`, and test-local wrappers belong under `tests/fixtures/domains/fauna/`.

**Path:** `fixtures/fauna/`  
**Authority level:** compatibility / transitional fixture lane under the canonical `fixtures/` responsibility root  
**Document status:** draft, repository-grounded directory README  
**Truth posture:** cite-or-abstain; filenames, examples, and passing checks do not create Fauna truth or implementation proof  
**Default for new payloads:** do not add them here; use the canonical reusable or test-local lane  
**Last reviewed:** 2026-07-21

## Quick navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does NOT belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs](#adrs)
- [Last reviewed](#last-reviewed)
- [Compatibility and migration contract](#compatibility-and-migration-contract)
- [Fauna sensitivity contract](#fauna-sensitivity-contract)
- [Fixture-home decision matrix](#fixture-home-decision-matrix)
- [Scenario and outcome matrix](#scenario-and-outcome-matrix)
- [Naming and pairing](#naming-and-pairing)
- [Maintenance, correction, and rollback](#maintenance-correction-and-rollback)
- [Verification status](#verification-status)

## Purpose

`fixtures/fauna/` exists to preserve a clear landing page for older or ambiguous references that point to a top-level Fauna fixture path.

It does **not** own the reusable Fauna fixture corpus. The canonical reusable lane is [`fixtures/domains/fauna/`](../domains/fauna/README.md), which already documents domain-owned valid, invalid, golden, layer, stale-source, sensitive-denial, and synthetic fixture families.

Use this compatibility lane only to:

- route readers and tooling toward the canonical Fauna fixture homes;
- document a bounded migration from an older path;
- record compatibility behavior while downstream references are being updated;
- explain why no new payload should be added here;
- preserve safe correction and rollback guidance for path migration.

This lane must never evolve into a second independent Fauna fixture authority.

## Authority level

`fixtures/fauna/` is **compatibility / transitional and non-authoritative**.

| Concern | Owning surface | Compatibility-lane role |
|---|---|---|
| Fauna doctrine and domain boundaries | `docs/domains/fauna/` | Cite and route; do not redefine. |
| Canonical reusable Fauna fixtures | `fixtures/domains/fauna/` | Redirect all new reusable payloads and expected outputs there. |
| Test-local wrappers and expectations | `tests/fixtures/domains/fauna/` | Redirect test-owned wrappers there. |
| Executable Fauna tests | `tests/domains/fauna/` | Do not place executable tests here. |
| Object meaning | `contracts/domains/fauna/` | Fixture examples may illustrate meaning but do not define it. |
| Machine shape | `schemas/contracts/v1/domains/fauna/` | Fixture examples may exercise schemas but do not establish them. |
| Policy and geoprivacy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | May model expected outcomes; cannot decide them. |
| Validator routing | `tools/validators/domains/fauna/` and documented shared validator lanes | Link to consumers; do not implement validation here. |
| Source registry | `data/registry/sources/fauna/` | Never create source authority from a fixture. |
| Lifecycle, proofs, receipts, and release | `data/`, `data/proofs/`, `data/receipts/`, `release/` | Never store real lifecycle or trust-bearing artifacts here. |

A compatibility path can preserve links and migration context. It cannot become canonical merely because it is older, convenient, or widely referenced.

## Status

| Surface | Status | Evidence-bounded interpretation |
|---|---|---|
| `fixtures/fauna/README.md` | **CONFIRMED** | The target README exists on the inspected base commit. |
| Parent classification | **CONFIRMED** | `fixtures/README.md` classifies `fixtures/fauna/` as a Fauna compatibility/staging lane and prefers domain-owned fixture lanes. |
| Canonical reusable lane | **CONFIRMED** | `fixtures/domains/fauna/README.md` exists and documents the reusable Fauna fixture boundary. |
| Test-local wrapper lane | **CONFIRMED** | `tests/fixtures/domains/fauna/README.md` exists and distinguishes test-local wrappers from reusable payloads. |
| Executable-test parent | **CONFIRMED file / scaffold status** | `tests/domains/fauna/README.md` exists; its own metadata says executable tests and enforcement remain unverified. |
| Direct inventory under `fixtures/fauna/` | **CONFIRMED bounded search: README only** | Repository code search returned only this README at the indexed snapshot. Treat exhaustive inventory as NEEDS VERIFICATION because indexes may lag or omit generated/ignored files. |
| Fauna validator implementation | **NEEDS VERIFICATION** | Validator READMEs exist, but executable coverage, fixture consumption, reports, and CI wiring are not established by this README. |
| Branch-protection and required-check enforcement | **UNKNOWN** | Repository settings are outside this README's evidence boundary. |

## What belongs here

Because this is a compatibility lane, accepted content is intentionally narrow:

- this README;
- a migration or deprecation note that identifies the canonical replacement path;
- a small redirect manifest only when an existing consumer requires one and the synchronization rule is documented;
- compatibility documentation that maps an old identifier or path to `fixtures/domains/fauna/`;
- a temporary inventory of legacy files while a reviewed move is in progress;
- rollback notes for a path migration.

Any compatibility file added here must identify:

1. its canonical source;
2. why the compatibility copy is still required;
3. how it is synchronized;
4. who consumes it;
5. its removal or review condition;
6. its sensitivity and rights posture;
7. its rollback path.

## What does NOT belong here

Do not add new reusable Fauna payloads to this lane.

The following are prohibited:

- canonical valid, invalid, golden, layer, stale-source, sensitive-denial, or synthetic Fauna fixtures;
- real source records, live API responses, source exports, scraped material, field observations, telemetry, eDNA, acoustic detections, mortality reports, disease reports, or conservation-status exports;
- exact or reconstructive locations for nests, dens, roosts, hibernacula, spawning sites, breeding sites, aggregation sites, private parcels, or steward-controlled records;
- real observer names, contact details, collection notes, source-system identifiers, or timestamps that could reveal a real occurrence;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data;
- actual `SourceDescriptor`, `EvidenceBundle`, `RunReceipt`, `RedactionReceipt`, proof pack, `PolicyDecision`, review record, release manifest, rollback card, correction notice, or withdrawal notice;
- contracts, schemas, policy rules, validators, tests, connector code, pipeline code, application code, or release tooling;
- public API material, public map material, public tiles, direct model output, or published artifacts;
- an independently edited mirror of a fixture stored under `fixtures/domains/fauna/`;
- filenames or prose that label a synthetic example as `real`, `production`, `final`, `official`, or `authoritative`.

When a file has a clear Fauna owner, put it under the canonical domain fixture lane instead of extending this compatibility surface.

## Inputs

Accepted inputs to this lane are limited to:

- repository-grounded migration findings;
- links or references that still point to `fixtures/fauna/`;
- canonical-path decisions from Directory Rules and Fauna documentation;
- a reviewed inventory of legacy files discovered under this path;
- synchronization or deprecation requirements from a named consumer;
- correction and rollback instructions for compatibility-path changes.

Do not use real animal records as migration examples. Use path names, toy identifiers, or redacted metadata only.

## Outputs

This lane may emit only compatibility-oriented documentation or routing metadata:

- a canonical-path pointer to `fixtures/domains/fauna/`;
- a test-local pointer to `tests/fixtures/domains/fauna/`;
- a migration checklist;
- a deprecation or compatibility note;
- a bounded legacy inventory;
- a rollback note.

It must not emit:

- reusable fixtures;
- executable test results;
- validation reports;
- policy decisions;
- proof or release artifacts;
- public-safe derivatives presented as approved;
- any object that could be mistaken for taxonomic, occurrence, range, or sensitive-site truth.

## Validation

### Required documentation checks

Before accepting a change to this lane, verify:

- exactly one H1 is present;
- relative links resolve;
- the compatibility classification remains explicit;
- every new file names its canonical source and consumer;
- no new reusable payload is introduced;
- no sensitive or reconstructive detail is present;
- no fixture is duplicated without a synchronization rule;
- the canonical reusable lane remains `fixtures/domains/fauna/`;
- test-local wrappers remain under `tests/fixtures/domains/fauna/`;
- executable tests remain under `tests/domains/fauna/`;
- changes do not claim source authority, EvidenceBundle closure, policy approval, release state, or publication.

### Consumer validation

No executable consumer is confirmed for `fixtures/fauna/` itself. A future compatibility file must identify the exact consumer that still requires the old path.

A passing link check or fixture test proves only the checked behavior. It does not prove:

- source accuracy or freshness;
- taxonomic correctness;
- occurrence truth;
- geoprivacy completeness;
- rights or redistribution permission;
- policy completeness;
- release approval;
- public safety outside the tested case;
- production runtime behavior.

### Migration validation

Before moving or deleting a compatibility file:

1. search code, docs, workflows, tests, manifests, and generated indexes for inbound references;
2. verify the canonical replacement exists;
3. update references in the same change when practical;
4. preserve history with a normal Git move when content is relocated;
5. verify the old path is no longer required;
6. document rollback;
7. avoid leaving two independently editable copies.

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life` at the inspected base. CODEOWNERS is a review-routing mechanism, not proof that review occurred.

Additional domain review is warranted when a change affects:

- taxonomy or conservation status;
- occurrence, range, migration, mortality, disease, or invasive-species semantics;
- sensitive-species location handling or geoprivacy;
- source rights or redistribution;
- policy outcomes or finite response envelopes;
- public map, Evidence Drawer, Focus Mode, API, export, or AI behavior;
- correction, revocation, rollback, or release semantics.

Do not add unverified role names or teams to executable CODEOWNERS entries.

## Related folders

Verified related files and lanes:

- [`../README.md`](../README.md) — parent runtime and synthetic fixture boundary.
- [`../domains/fauna/README.md`](../domains/fauna/README.md) — canonical reusable Fauna fixture lane.
- [`../ecology/README.md`](../ecology/README.md) — cross-domain ecology fixture boundary.
- [`../../tests/fixtures/domains/fauna/README.md`](../../tests/fixtures/domains/fauna/README.md) — test-local Fauna wrapper lane.
- [`../../tests/domains/fauna/README.md`](../../tests/domains/fauna/README.md) — executable Fauna test parent.
- [`../../docs/domains/fauna/README.md`](../../docs/domains/fauna/README.md) — Fauna domain boundary and sensitivity posture.
- [`../../docs/domains/fauna/CANONICAL_PATHS.md`](../../docs/domains/fauna/CANONICAL_PATHS.md) — doctrine-derived Fauna path register.
- [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) — canonical placement doctrine.
- [`../../tools/validators/fauna/README.md`](../../tools/validators/fauna/README.md) — broad Fauna validator routing index; executable behavior remains bounded.
- [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) — current GitHub review-routing evidence.

## ADRs

No target-specific accepted ADR was verified for `fixtures/fauna/`.

This README aligns an existing compatibility path with:

- Directory Rules' canonical `fixtures/domains/<domain>/` pattern;
- the parent fixture README's compatibility/staging classification;
- the Fauna canonical-path register;
- the existing reusable and test-local Fauna fixture lanes.

A new ADR is not required for this documentation-only clarification because it does not add, remove, or rename a canonical root; change a lifecycle phase; or create a parallel authority home.

An ADR or explicit migration decision is required before a future change would:

- make `fixtures/fauna/` a permanent independently edited mirror;
- reverse the canonical `fixtures/domains/fauna/` placement;
- create another reusable Fauna fixture home;
- change the test-local versus reusable fixture split;
- alter a KFM invariant or authority boundary.

## Last reviewed

**2026-07-21**

Review this README again when:

- a file other than this README is discovered under `fixtures/fauna/`;
- an inbound consumer still requires this path;
- the canonical reusable fixture lane changes;
- a migration or deletion PR is proposed;
- the fixture-home distinction is changed by ADR;
- more than six months have passed.

## Compatibility and migration contract

### Default state

`fixtures/fauna/` is a **frozen compatibility lane** for new payloads.

New reusable Fauna fixtures go to:

```text
fixtures/domains/fauna/
```

New test-local Fauna wrappers go to:

```text
tests/fixtures/domains/fauna/
```

New executable Fauna tests go to:

```text
tests/domains/fauna/
```

### If legacy files are found here

Do not silently copy them into the canonical lane. For each file:

1. inspect content, sensitivity, rights, and consumers;
2. classify it as reusable fixture, test-local wrapper, generated artifact, lifecycle data, or prohibited material;
3. quarantine any real, rights-unclear, or sensitive material;
4. select the correct canonical destination;
5. move with history when safe;
6. update references;
7. add a migration note;
8. verify no divergent copy remains;
9. document rollback.

### Retention conditions

Keep a compatibility file only while a verified consumer requires the old path. A compatibility file must not outlive its documented consumer without renewed review.

## Fauna sensitivity contract

Fauna fixtures are deny-by-default for exact sensitive occurrence information.

Never include real or reverse-engineerable detail for:

- sensitive taxa;
- nests, dens, roosts, hibernacula, spawning, breeding, or aggregation sites;
- telemetry tracks or movement paths;
- observer identities or private contact details;
- collection notes or steward-only records;
- parcel-level or timestamp combinations that can reveal a protected location;
- restricted disease, mortality, or invasive-species records;
- raw eDNA or acoustic detections tied to a real site.

For synthetic cases:

- prefer no geometry;
- otherwise use unmistakably toy or generalized geometry;
- label artificial values;
- preserve the difference between exact source records and public-safe derivatives;
- preserve source roles;
- make expected policy outcome explicit;
- include no operational transform threshold unless it is clearly synthetic and owned by a test contract.

A range polygon is not occurrence truth. A modeled habitat or suitability surface is not an observation. A generalized derivative is not the source record. A map feature is not evidence authority.

## Fixture-home decision matrix

| Need | Correct home | Reason |
|---|---|---|
| Reusable Fauna runtime or documentation fixture | `fixtures/domains/fauna/` | Canonical domain-owned fixture lane. |
| Test-specific wrapper or expectation manifest | `tests/fixtures/domains/fauna/` | Test-local and owned by named tests. |
| Executable Fauna test | `tests/domains/fauna/` | Enforceability proof. |
| Cross-domain Habitat × Fauna or ecology scenario | `fixtures/ecology/` or the owning domain thin-slice lane | Use the lowest common responsibility boundary. |
| Compatibility redirect from an old top-level Fauna path | `fixtures/fauna/` | This lane's bounded purpose. |
| Schema | `schemas/contracts/v1/domains/fauna/` | Machine shape authority. |
| Contract | `contracts/domains/fauna/` | Semantic meaning. |
| Policy or geoprivacy rule | `policy/domains/fauna/` or `policy/sensitivity/fauna/` | Admissibility authority. |
| Validator implementation | accepted `tools/validators/` lane | Executable checking logic. |
| Real source or lifecycle material | governed `data/` or quarantine lane | Fixtures are not lifecycle data. |
| Release, proof, receipt, correction, or rollback record | owning trust-bearing root | Compatibility fixtures cannot authorize state. |

## Scenario and outcome matrix

| Scenario | Expected posture | Correct location |
|---|---|---|
| Synthetic non-sensitive occurrence | Valid or review-ready | `fixtures/domains/fauna/valid/` or object-specific canonical lane. |
| Unsupported taxonomy or missing source role | Validation failure or `ABSTAIN` | `fixtures/domains/fauna/invalid/`. |
| Exact sensitive location appears | `DENY`, blocked render, or validation failure | `fixtures/domains/fauna/sensitive_deny/`. |
| Source is stale or superseded | Stale, hold, `ABSTAIN`, or review-required | `fixtures/domains/fauna/stale_source/`. |
| Stable expected output | Deterministic expected output, never release state | `fixtures/domains/fauna/golden/`. |
| Layer-shaped renderer example | Renderer-safe, generalized, or denied | `fixtures/domains/fauna/layers/`. |
| Test-specific wrapper around a reusable fixture | Pass, fail, deny, or abstain expectation | `tests/fixtures/domains/fauna/`. |
| Cross-domain ecology presentation | Context-only or bounded finite outcome | `fixtures/ecology/` when no single domain owns the scenario. |
| Legacy path redirect | Compatibility only | `fixtures/fauna/`. |
| Unexpected consumer or validator failure | `ERROR` | Owning test or validator report; do not create a payload here. |

## Naming and pairing

In the canonical fixture lane, prefer names that reveal scenario and role:

```text
<scenario>.input.json
<scenario>.expected.json
<scenario>.valid.json
<scenario>.invalid.json
<scenario>.geojson
<scenario>.md
```

In this compatibility lane, prefer routing names such as:

```text
README.md
MIGRATION.md
DEPRECATION.md
compatibility-map.yaml
```

A compatibility map must identify canonical destinations and must not copy substantive payload content.

Avoid names that imply authority or release:

```text
real.json
production.json
official.json
authoritative.json
final.json
published.json
```

## Maintenance, correction, and rollback

- Keep this README synchronized with the parent fixture index and canonical Fauna fixture README.
- Do not add child lanes here for scenarios already owned by `fixtures/domains/fauna/`.
- Remove stale inbound links as part of migration work.
- Record any retained compatibility file, consumer, synchronization rule, and review date.
- Treat sensitive or real material found here as a governance incident, not a documentation cleanup.
- Route prohibited material to quarantine or its correct authority root.
- Preserve correction history for any public or shared artifact affected by a path mistake.

### Rollback

For this README, rollback is a normal revert to the previous content.

For a future file migration:

- revert the move and reference updates together;
- restore the prior path only if it is still safe and needed;
- do not restore sensitive or prohibited content to a fixture lane;
- retain any incident, correction, or withdrawal record required by the event.

## Verification status

| Acceptance item | Status | Evidence or limit |
|---|---|---|
| Target file read from immutable base | **PASS** | `fixtures/fauna/README.md` fetched from the pinned base commit. |
| Parent compatibility classification | **PASS** | `fixtures/README.md` explicitly identifies `fixtures/fauna/` as compatibility/staging. |
| Canonical reusable lane | **PASS** | `fixtures/domains/fauna/README.md` inspected. |
| Test-local wrapper lane | **PASS** | `tests/fixtures/domains/fauna/README.md` inspected. |
| Executable-test parent | **PASS for file presence / scaffold only** | `tests/domains/fauna/README.md` inspected; implementation remains unverified. |
| Fauna domain and canonical-path doctrine | **PASS** | `docs/domains/fauna/README.md` and `CANONICAL_PATHS.md` inspected. |
| Review route | **PASS** | `.github/CODEOWNERS` routes `/fixtures/` to `@bartytime4life`. |
| Direct indexed inventory | **PASS, bounded** | Code search returned only `fixtures/fauna/README.md` at the indexed snapshot. |
| Exhaustive filesystem inventory | **NEEDS VERIFICATION** | Search indexes may omit generated, ignored, or unindexed content. |
| Executable consumer for `fixtures/fauna/` | **NOT FOUND / NEEDS VERIFICATION** | No consumer was confirmed for the compatibility path itself. |
| Validator implementation and fixture coverage | **NEEDS VERIFICATION** | Validator indexes exist; executable coverage and CI binding are not established here. |
| Sensitive-data review | **NOT APPLICABLE to this README-only change** | Repeat for every future payload or compatibility manifest. |
