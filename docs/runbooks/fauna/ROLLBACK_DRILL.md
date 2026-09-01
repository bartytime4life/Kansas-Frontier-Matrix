<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/rollback-drill
title: Fauna — Rollback Drill
type: runbook; rehearsal-procedure; domain-lane; sensitive-domain; non-authoritative
version: v0.1
prior_version: unversioned planned-file scaffold
status: draft; repository-grounded; shared-synthetic-rehearsal-executable; fauna-integrated-and-operational-rollback-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: >-
  Fauna, release, rollback, correction, taxonomy, source, rights, sensitivity,
  geoprivacy, evidence, policy, test, operations, security, public-surface,
  and independent-review assignments remain NEEDS VERIFICATION. CODEOWNERS
  routing does not establish those authorities.
created: 2026-08-24
updated: 2026-08-24
policy_label: public-review; fauna; rollback-drill; synthetic; no-network; sensitive-location; fail-closed; non-release
current_path: docs/runbooks/fauna/ROLLBACK_DRILL.md
owning_root: docs/
responsibility: >-
  Define the bounded Fauna rollback tabletop and synthetic rehearsal procedure,
  distinguish the repository's executable shared candidate/rehearsal controls
  from unimplemented Fauna operational rollback, and produce a review handoff
  without changing source, evidence, policy, release, deployment, promotion, or
  publication state.
truth_posture: cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c3b39fb27fd7ca46c41f5b5133149f1d8cd73996
  target_prior_blob: b0fd32d2c79680f6e6c76eedd8881ea981ebbaa9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  local_runbook_index_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  fauna_rollback_runbook_blob: d8d7d3bb9c40d3de50d484e6d13640bee5baaa58
  fauna_no_network_runbook_blob: 4a8772dd1356521b11d4a568ae127acde2b2cc5e
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_card_validator_test_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  synthetic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  synthetic_rehearsal_workflow_blob: 565507371ecf1f8df3e7f688370c5700ca795529
  rollback_drill_workflow_blob: 6ce891a99b3c192da17eb8ef25757b023b686f47
  fauna_rollback_test_lane_blob: 28853dc37d00981a405613f43b1860d5500db6bb
  fauna_rollback_schema_stub_blob: 08b82778b3654ab7643a12770bdcb976eb12e9ff
  release_rollback_parent_blob: aa8b60f4d47e7b73ab3e862f1dcd498691ea4e0c
  release_rollback_fauna_blob: 7dbf5b5b93cb9a4b90b1f2270691a4069389e50f
inspection_boundary: >-
  Current-session GitHub reads of the target; accepted Directory Rules decision;
  the shared RollbackCard contract, schema, fixtures, validator, tests, helper,
  and workflows; Fauna no-network and rollback documentation; Fauna release-test,
  pipeline, data-plane, and release-review lanes; and current repository branch
  and pull-request state. Repository-native commands were not executed in a
  mounted checkout while this document was authored. No live source, protected
  wildlife payload, exact location, credential, public alias, deployed service,
  cache, catalog, tile, index, release record, or published artifact was accessed
  or changed.
related:
  - ../README.md
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/POLICY.md
  - ../../domains/fauna/RELEASE_INDEX.md
  - ./ROLLBACK_RUNBOOK.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ../rollback-rehearsal.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../fixtures/release/rollback_card/README.md
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../.github/workflows/rollback-rehearsal.yml
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../tests/domains/fauna/release/rollback/README.md
  - ../../../pipelines/rollback/fauna/README.md
  - ../../../release/rollback/README.md
  - ../../../release/rollback/fauna/README.md
  - ../../../data/rollback/fauna/README.md
tags: [kfm, fauna, rollback, drill, rehearsal, correction, geoprivacy, sensitivity, synthetic, no-network, fail-closed]
notes:
  - "This revision replaces a planned-file scaffold with a repository-grounded procedure."
  - "The shared RollbackCard candidate profile and marker-protected synthetic rehearsal are executable; they remain non-authoritative and cannot touch operational public state."
  - "A Fauna-specific integrated rollback executor, fixture family, direct test suite, accepted policy binding, release target, carrier invalidation implementation, and operational authority are not established."
  - "Current maximum result: bounded drill handoff. Actual Fauna rollback remains HOLD."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — Rollback Drill

![status](https://img.shields.io/badge/status-draft-blue)
![current](https://img.shields.io/badge/fauna%20operational%20rollback-HOLD-red)
![shared](https://img.shields.io/badge/shared%20synthetic%20rehearsal-executable-success)
![sensitivity](https://img.shields.io/badge/sensitive%20location-deny%20default-red)
![network](https://img.shields.io/badge/network-no--source--access-informational)
![authority](https://img.shields.io/badge/authority-review%20handoff%20only-orange)

> **Exercise the current shared rollback-candidate and marker-protected synthetic rehearsal controls, add a Fauna-specific fail-closed tabletop review, and stop at a bounded evidence handoff.**

> [!IMPORTANT]
> **Current disposition: the shared synthetic rehearsal is executable; an integrated or operational Fauna rollback drill is `HOLD`.** The repository contains a closed, fixture-first shared `RollbackCard` candidate profile and a deterministic temporary-root rollback/withdrawal rehearsal. It does not contain an accepted Fauna rollback executor, Fauna rollback fixture profile, actual Fauna release target, production alias, external invalidation implementation, or authorized rollback path.

> [!WARNING]
> **A drill pass is not a rollback decision.** A schema-valid candidate, green unit test, green workflow, synthetic alias change, elapsed-time measurement, report, receipt-shaped file, pull request, merge, or maintainer acknowledgement does not approve or execute rollback, correction, withdrawal, release, deployment, promotion, or publication.

> [!CAUTION]
> **Never use real or reconstructable sensitive Fauna detail in a drill.** Exact occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, aggregation sites, telemetry, movement traces, observer identity, private-land joins, steward-controlled records, transform parameters, and source credentials do not belong in scenarios, fixtures, logs, reports, issues, pull requests, screenshots, or workflow summaries.

**Quick navigation:** [Purpose](#1-purpose-scope-and-terminal-boundary) · [Authority](#2-authority-placement-and-non-effects) · [Evidence](#3-current-repository-evidence) · [Invariants](#4-rollback-and-fauna-safety-invariants) · [Roles](#5-roles-and-separation-of-duties) · [Levels](#6-drill-levels-and-current-disposition) · [Scenarios](#7-synthetic-scenario-catalog) · [Preflight](#8-preflight-and-stop-conditions) · [Executable checks](#9-shared-executable-checks) · [Procedure](#10-fauna-tabletop-and-synthetic-rehearsal-procedure) · [Invalidations](#11-carrier-and-consumer-invalidation-matrix) · [Sensitivity](#12-fauna-sensitivity-and-geoprivacy-review) · [RTO/RPO](#13-time-objectives-and-measurements) · [Outcomes](#14-finite-outcomes-and-reason-codes) · [Acceptance](#15-acceptance-matrix) · [CI](#16-hosted-ci-and-evidence-interpretation) · [Handoff](#17-drill-handoff-packet) · [Failures](#18-failure-diagnosis) · [Cleanup](#19-correction-cleanup-and-document-rollback) · [Open work](#20-current-holds-and-smallest-next-slice) · [Related](#21-related-surfaces) · [History](#22-change-log)

---

## 1. Purpose, scope, and terminal boundary

This runbook defines the strongest truthful Fauna rollback drill that the current repository evidence supports.

The bounded drill combines three distinct activities:

1. **shared candidate validation** — validate the repository's proposed, non-executing `RollbackCard` fixtures and exact negative finding sets;
2. **shared synthetic rehearsal** — exercise rollback and withdrawal against a marker-protected temporary root, including digest checks, alias replacement or withdrawal, append-only correction, complete invalidation declaration, and preservation of affected bytes; and
3. **Fauna tabletop review** — evaluate how current rights, sensitivity, geoprivacy, evidence, policy, taxonomy, and downstream public surfaces would constrain a Fauna rollback.

```text
synthetic Fauna incident
  -> declare drill hold
  -> validate shared RollbackCard candidate profile
  -> run shared marker-protected temporary-root rehearsal
  -> review Fauna target safety under current rules
  -> inventory every affected public carrier and governed consumer
  -> record blockers, measured times, and non-authority state
  -> review handoff
  -/> operational alias, source, release, deployment, promotion, or publication
```

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

This drill does not reverse that lifecycle, move files between stages, erase history, or create a second truth path. It rehearses candidate recovery behavior in synthetic state and documents what an authorized operational process would still need to prove.

### In scope

- the shared `RollbackCard` semantic contract and closed `1.0.0` JSON Schema;
- its three valid fixtures, six invalid fixtures, expected-findings manifest, validator, and unit tests;
- the shared marker-protected `tools/release/rollback_apply.py` helper and its eight isolated temporary-root tests;
- the `rollback-drill` and `rollback-rehearsal` workflow definitions and their stated non-effects;
- the accepted Fauna synthetic fixture-hygiene suite as a public-safety regression baseline;
- a no-source, no-real-location Fauna tabletop scenario;
- affected-carrier and governed-consumer inventory;
- target revalidation against current Fauna rights, sensitivity, geoprivacy, evidence, policy, taxonomy, correction, and review posture;
- measured drill timestamps and a bounded review packet.

### Out of scope

- source fetch, connector execution, source admission, rights approval, or source activation;
- real occurrences, sensitive sites, telemetry, media, EBD bytes, exact or reconstructable geometry, or private review material;
- production policy evaluation, reviewer authentication, signer custody, emergency authority, or release approval;
- an actual Fauna `ReleaseManifest`, accepted rollback target, operational `RollbackCard`, correction notice, withdrawal notice, or execution receipt;
- mutation of `data/published/`, a public alias, API route, CDN, tile service, catalog, graph, search index, vector index, AI cache, Evidence Drawer, Focus Mode response, or deployed runtime;
- release, deployment, promotion, publication, erasure, or legal/compliance action.

### Terminal boundary

The maximum result is:

```text
DRILL_HANDOFF_READY
```

That means the declared shared synthetic checks and Fauna tabletop review were completed at an exact revision, their limits are explicit, and unresolved operational blockers are ready for human review.

It never means:

```text
ROLLBACK_APPROVED
ROLLBACK_EXECUTED
PUBLIC_STATE_RESTORED
RELEASED
PUBLISHED
```

[Back to top](#top)

---

## 2. Authority, placement, and non-effects

### Directory Rules result

**`PLACE` — CONFIRMED for this same-path update.** Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes. A human operator procedure remains under `docs/runbooks/fauna/`; no responsibility root, contract, schema, policy, fixture, test, pipeline, release record, lifecycle artifact, or public carrier is created or moved.

| Responsibility | Owning surface | This runbook's posture |
|---|---|---|
| Human drill procedure | `docs/runbooks/fauna/` | own and explain |
| Shared rollback meaning | `contracts/release/rollback_card.md` | cite; do not redefine |
| Shared machine shape | `schemas/contracts/v1/release/rollback_card.schema.json` | validate candidate shape only |
| Shared candidate validator | `tools/validators/release/validate_rollback_card.py` | execute no-network fixture profile |
| Shared synthetic rehearsal | `tools/release/rollback_apply.py` | execute only through marker-protected synthetic roots |
| Shared executable proof | `tests/validators/`, `tests/release/` | run exact modules |
| Fauna fixture safety | `fixtures/domains/fauna/`, `tests/domains/fauna/`, `tools/validators/domains/fauna/` | run bounded hygiene profile |
| Fauna-specific rollback tests | `tests/domains/fauna/release/rollback/` | currently guidance-only; do not invent coverage |
| Policy and sensitivity | `policy/` responsibility lanes | inputs to future operation; not drill authority |
| Release decision and review | `release/` | no write, approval, or state transition |
| Data-plane rollback support | `data/rollback/` | draft support lane only; not decision authority |
| Public delivery | governed APIs and released public-safe carriers | no mutation or direct access |

### Important schema distinction

Two rollback-card-shaped surfaces exist and must not be collapsed:

| Surface | Current state | Allowed use in this drill |
|---|---|---|
| `schemas/contracts/v1/release/rollback_card.schema.json` | closed, fixture-first, paired with implemented validator and tests; status `PROPOSED` | **use for shared candidate validation** |
| `schemas/contracts/v1/domains/fauna/rollback_card.schema.json` | permissive `id`-only greenfield stub with `additionalProperties: true`; declared contract, fixtures, and validator are absent | **do not use as Fauna operational proof** |

The shared release profile is stronger, but it still proves only candidate shape and local consistency. It does not become Fauna policy, release authority, or an operational decision by being referenced here.

### Local boundary limitation

`docs/runbooks/fauna/README.md` is a one-byte placeholder at the pinned snapshot. This runbook therefore self-bounds its procedure and leaves the local lane index as `HOLD / NEEDS VERIFICATION`. It does not silently become the parent authority for all Fauna operations.

### Non-effects

Running or merging this runbook does not:

- create evidence, policy, review, release, rollback, correction, or publication authority;
- admit or activate a source;
- validate a real Fauna record;
- approve a prior release as safe;
- execute a production rollback;
- alter a public alias or carrier;
- invalidate an external system;
- erase or delete released history;
- satisfy independent-review or separation-of-duty requirements.

[Back to top](#top)

---

## 3. Current repository evidence

Pinned to `main@c3b39fb27fd7ca46c41f5b5133149f1d8cd73996`:

| Surface | Status | Bounded conclusion |
|---|---|---|
| Prior target | **CONFIRMED scaffold** | Twelve-line planned-file placeholder; no procedure, commands, evidence snapshot, current maturity, or handoff contract. |
| Shared `RollbackCard` contract | **CONFIRMED draft / PROPOSED** | Defines candidate rollback, withdrawal, hold, and error meaning; explicitly non-executing. |
| Shared schema | **CONFIRMED closed candidate profile** | `RollbackCard` `1.0.0`, finite vocabularies, required invalidations, false governance flags, `release_ref: null`. |
| Shared validator | **CONFIRMED executable** | No-network candidate shape and local-consistency validation; does not resolve references or execute policy. |
| Shared fixtures and tests | **CONFIRMED executable** | Three valid candidates, six invalid candidates, expected findings, and non-vacuous validator tests. |
| Shared synthetic helper | **CONFIRMED executable and synthetic-only** | Requires a marker-protected root and `synthetic: true`; plan is no-write; apply affects only the synthetic root. |
| Shared rehearsal tests | **CONFIRMED executable** | Eight tests cover deterministic plan, rollback, withdrawal, history preservation, complete invalidations, target/digest failure, marker enforcement, and non-synthetic denial. |
| `rollback-rehearsal` workflow | **CONFIRMED command-bearing** | Runs the shared rehearsal test on its path-filtered scope; does not trigger from this Fauna document alone unless another matched path changes or it is dispatched. |
| `rollback-drill` workflow | **CONFIRMED readiness workflow** | Runs on pull requests, validates the shared candidate/rehearsal controls, and keeps production rollback and alias verification as explicit holds. |
| Fauna fixture-hygiene profile | **CONFIRMED executable** | Two positive and five negative synthetic fixtures with eight deterministic tests; proves fixture safety only. |
| Fauna direct rollback test lane | **CONFIRMED guidance-only** | `tests/domains/fauna/release/rollback/` contains README guidance and `.gitkeep`, not executable Fauna rollback tests. |
| Fauna rollback schema | **CONFIRMED permissive stub** | `id`-only, open object, no existing paired contract, fixture root, or validator at declared paths. |
| Fauna rollback pipeline/adapters | **UNKNOWN / documentation-only** | `pipelines/rollback/fauna/README.md` states executable depth is unknown and target-specific spec/tests were absent at its checkpoint. |
| Release rollback lanes | **CONFIRMED draft guidance** | Parent and Fauna review READMEs exist; no actual accepted Fauna rollback record or operational authority is established. |
| Published alias and external invalidation | **HOLD / UNKNOWN** | Workflow source expects no governed published aliases and an alias auditor placeholder; exact-head execution and any deployed state remain separate evidence. |
| Owners and stewards | **NEEDS VERIFICATION** | `@bartytime4life` is the verified GitHub route; functional and independent authorities are not assigned. |
| Operational Fauna rollback | **HOLD** | No accepted target, executor, policy binding, external invalidation, post-rollback proof, or public-state mutation path is established. |

### What is executable now

```text
shared RollbackCard fixture validation
shared marker-protected synthetic rollback/withdrawal rehearsal
Fauna synthetic public-safe fixture hygiene
Fauna tabletop analysis
```

### What remains unproved

```text
real Fauna release discovery
current-vs-target manifest resolution
current-policy target admission
Fauna policy evaluation
authorized decision/signature flow
external alias mutation
external cache/tile/catalog/index invalidation
public UI/API verification
post-rollback proof
operational RTO/RPO
```

Repository-native commands were not run in a mounted checkout while this revision was authored. Command availability and file content are confirmed; local and hosted outcomes must be collected at the exact drill revision.

[Back to top](#top)

---

## 4. Rollback and Fauna safety invariants

Every drill must preserve these rules.

### Lifecycle and history

- `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED` remains intact.
- Rollback is a governed release transition, not a reverse file move.
- The affected release, manifests, artifacts, receipts, proofs, review records, and correction lineage remain inspectable.
- Rollback is not erasure. A lawful removal process, where applicable, is separate.
- A prior release is not safe merely because it was previously published.

### Target safety

The proposed target must be re-evaluated under **current** applicable rules:

- source role and source availability;
- rights and redistribution posture;
- taxonomic identity and supersession;
- evidence resolution and contradiction state;
- sensitivity and geoprivacy;
- policy version and result;
- review state;
- artifact integrity;
- correction and withdrawal state;
- current downstream reconstruction risk.

If the prior target cannot pass current requirements, the drill outcome must be a hold, denial, or withdrawal/forward-correction recommendation—not a forced rollback.

### Fauna sensitivity

- Exact or reconstructable sensitive locations fail closed.
- Sensitive geometry is transformed or withheld before any public carrier; client-side styling is not a control.
- A rollback must not restore older, more precise, differently joined, or less protected derivatives.
- Logs and reports use safe reason codes and paths, never protected values.
- Cross-domain joins with habitat, hydrology, land, infrastructure, imagery, time, or telemetry must be considered.
- A generalized historical product can still be unsafe if current external data makes it reconstructable.

### Evidence and AI

- `EvidenceRef` must resolve to `EvidenceBundle` before consequential claims are treated as supported.
- Maps, tiles, catalogs, graphs, search indexes, vector indexes, dashboards, scenes, summaries, and model output are downstream carriers.
- Focus Mode and AI must not answer from a revoked or withdrawn release.
- An AI cache hit or generated summary cannot approve rollback or prove target safety.
- Cite-or-abstain remains the public truth posture.

### Complete invalidation

The shared candidate and rehearsal profiles name nine invalidation classes:

```text
API_CACHE
CDN
TILES
CATALOG
TRIPLETS
SEARCH_INDEX
VECTOR_INDEX
AI_CACHE
DOWNSTREAM_DERIVATIVES
```

A drill that omits one is incomplete. The shared rehearsal records the complete set inside a synthetic root; it does not execute those invalidations against external systems.

### Drill non-authority

- Initial state is `HOLD`.
- No scenario may use a real release or protected record.
- The synthetic marker and `synthetic: true` are mandatory.
- The drill must record `public_state_mutated: false` for real KFM state.
- A green result is bounded evidence, not approval.

[Back to top](#top)

---

## 5. Roles and separation of duties

The operational roles below are required design responsibilities. Their named assignments remain `NEEDS VERIFICATION`.

| Role | Drill responsibility | May not self-grant |
|---|---|---|
| Drill coordinator | freeze scope, revision, scenario, clock, and terminal boundary | release or rollback authority |
| Fauna domain steward | review biological meaning, taxonomic continuity, and domain impact | rights or policy waiver |
| Sensitivity/geoprivacy reviewer | assess exact/reconstructable location risk and target transforms | source or release approval |
| Evidence steward | verify support references and contradiction state | manufacture evidence from summaries |
| Policy/rights reviewer | assess current rights, terms, access, and policy posture | waive missing authority |
| Release/rollback steward | own decision handoff and accepted release objects | treat drill report as decision |
| Operations owner | inventory aliases, caches, tiles, catalogs, indexes, and deployed consumers | execute undeclared mutation |
| Security observer | verify synthetic/no-network boundary, path safety, and log safety | approve protected-data exposure |
| Independent reviewer | challenge target, evidence, invalidations, measurements, and claims | merge review with execution |
| Scribe | record safe timestamps, commands, digests, outcomes, and blockers | store protected values |

### Current route

- `@bartytime4life` is the verified repository review route.
- No current evidence assigns the functional roles above.
- A tabletop may have one participant perform multiple simulated roles, but the handoff must record that separation of duties was **not** proven.
- A real rollback may not inherit authority from a tabletop role-play, CODEOWNERS routing, pull-request approval, or repository ownership.

### Minimum operational separation

Before any real Fauna rollback, at least these duties must be independently accountable:

1. target proposal;
2. Fauna sensitivity/geoprivacy review;
3. evidence/policy validation;
4. release decision;
5. execution;
6. post-execution verification.

The exact organizational assignment remains an open governance decision.

[Back to top](#top)

---

## 6. Drill levels and current disposition

| Level | Name | What it exercises | Current state | Maximum claim |
|---:|---|---|---|---|
| 0 | `TABLETOP` | synthetic incident, target questions, carrier inventory, roles, timestamps, blockers | **AVAILABLE** | procedure completed |
| 1 | `SHARED_CANDIDATE_PROFILE` | shared schema, three valid fixtures, six exact negative cases | **EXECUTABLE** | candidate shape/local consistency |
| 2 | `SHARED_SYNTHETIC_REHEARSAL` | marker-protected temporary alias rollback/withdrawal, digest and preservation checks | **EXECUTABLE** | synthetic helper behavior |
| 3 | `FAUNA_INTEGRATED_REHEARSAL` | Fauna-specific candidate, current-policy target check, governed consumers, public-safe outputs | **HOLD** | none until implemented |
| 4 | `OPERATIONAL_ROLLBACK` | authorized real release transition and external invalidation | **DENY / HOLD** | unavailable |

### Accepted scope for this runbook version

A complete run under this document may perform Levels 0–2 and produce a `DRILL_HANDOFF_READY` packet. It must explicitly report Levels 3–4 as held.

### Why Level 2 is not Level 3

The shared helper operates on a test-created directory with:

- a synthetic marker file;
- toy release IDs;
- local text artifacts;
- local manifest JSON;
- a local `published/current.json`;
- local correction and invalidation JSON;
- no source, policy engine, reviewer, release service, public API, map, CDN, or deployment.

That is valuable executable proof of deterministic mechanics. It is not an integrated Fauna release system.

[Back to top](#top)

---

## 7. Synthetic scenario catalog

Use only toy identifiers and withheld spatial support. Do not derive a scenario from a real sensitive occurrence.

### Scenario A — sensitivity discovery

```text
trigger: SENSITIVITY_DISCOVERY
affected: release:synthetic:fauna:v2
candidate target: release:synthetic:fauna:v1
```

Questions:

- Would the older target restore more precise or reconstructable material?
- Are current geoprivacy, rights, policy, and review records resolvable?
- Do map, API, search, vector, AI, and downstream derivatives all have invalidation paths?
- Is withdrawal safer than restoring the target?

Expected tabletop result: `HOLD_FOR_POLICY`, `HOLD_FOR_TARGET`, or `WITHDRAWAL_CANDIDATE` unless current support is complete. No real target is evaluated.

### Scenario B — target integrity failure

Synthetic target artifact bytes are changed after the manifest digest is established.

Expected shared result:

```text
HOLD
ARTIFACT_DIGEST_MISMATCH
```

No alias change is permitted.

### Scenario C — no safe prior release

The synthetic affected release must be removed from current use, but no admissible prior target is available.

Expected candidate posture:

```text
WITHDRAWAL_CANDIDATE
target.mode: WITHDRAWAL
target.release_ref: null
```

A withdrawal is not erasure. The affected release remains in audit history.

### Scenario D — incomplete invalidation inventory

One or more of the nine required invalidation classes is omitted.

Expected shared result:

```text
HOLD
INVALIDATION_SET_INCOMPLETE
```

Do not narrow the set merely because a consumer is not yet implemented; record that consumer as absent, not applicable with evidence, or `NEEDS VERIFICATION`.

### Scenario E — non-synthetic input

The scenario sets `synthetic: false` or the workspace lacks the exact marker.

Expected shared result:

```text
HOLD
NON_SYNTHETIC_INPUT_DENIED
```

or:

```text
HOLD
SYNTHETIC_MARKER_MISSING
```

### Scenario F — stale governed consumer

A toy map or Focus Mode response is described as referencing the affected synthetic release after the simulated transition.

Expected tabletop response:

- the carrier/consumer is marked stale or unavailable;
- the old evidence path is not treated as current;
- AI answer caches are invalidated;
- the Evidence Drawer would show correction/withdrawal state;
- the scenario remains held until an executable consumer check exists.

### Scenario G — deterministic replay

The same plan is evaluated twice against the same synthetic root.

Expected shared result:

- byte-identical plan report;
- no correction directory during plan mode;
- no real public mutation;
- stable reason code and invalidation set.

### Recommended rotation

Run at least:

- Scenario A for Fauna-specific tabletop pressure;
- Scenario B or D for fail-closed behavior;
- Scenario C for withdrawal;
- Scenario G for determinism.

The shared unit module already exercises B–G mechanics. The Fauna tabletop adds A and consumer interpretation.

[Back to top](#top)

---

## 8. Preflight and stop conditions

Run from a clean checkout or isolated worktree at the exact intended revision.

```bash
git rev-parse HEAD
git status --short
```

Record the exact SHA. A dirty tree is not automatically forbidden, but unexplained changes in any required path are a `HOLD`.

### Required paths

```text
docs/runbooks/fauna/ROLLBACK_DRILL.md
docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
contracts/release/rollback_card.md
schemas/contracts/v1/release/rollback_card.schema.json
tools/validators/release/validate_rollback_card.py
tests/validators/test_validate_rollback_card.py
fixtures/release/rollback_card/README.md
tools/release/rollback_apply.py
tests/release/test_synthetic_rollback_rehearsal.py
.github/workflows/rollback-rehearsal.yml
.github/workflows/rollback-drill.yml
tests/domains/fauna/test_fauna_smoke.py
tests/domains/fauna/release/rollback/README.md
```

### Environment

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC
```

The shared `RollbackCard` validator and its tests require the repository's declared Python test dependencies, including `jsonschema`. Use the locked or repository-native installation route; do not install an unpinned package merely to make the drill green.

### Credential and data preflight

- Remove source tokens, API keys, cloud credentials, model credentials, and unrelated secrets.
- Do not mount production data, release stores, object stores, databases, indexes, or public-service credentials.
- Do not copy a real Fauna payload into a temporary root.
- Do not use real coordinates, even as an invalid example.
- Do not use a mutable production alias, URL, bucket, endpoint, or branch as the affected or target identity.
- Confirm the helper's target root is created by the test or is an explicitly disposable synthetic root with the exact marker.
- Confirm no overlapping pull request owns the target document or the executable controls being cited.

### Stop before execution when

- the exact repository SHA is unknown;
- any scenario or fixture may contain protected or reconstructable detail;
- a live source, production store, or credential is required;
- the shared helper lacks its exact synthetic marker guard;
- the scenario is not explicitly synthetic;
- the candidate target equals the affected release;
- the target identity or digest is missing;
- the complete invalidation set is unknown;
- the current rights/sensitivity/policy question cannot be posed without revealing protected information;
- the direct Fauna test lane is mistaken for executable coverage;
- expected results were copied from an older SHA without rerun;
- the branch head changes after evidence collection.

### Stop after execution when

- a test reports zero collected tests;
- any negative fixture unexpectedly passes;
- any positive fixture unexpectedly fails;
- any output echoes protected values;
- a helper touches a path outside the synthetic root;
- the affected synthetic bytes change;
- a report claims real public state changed;
- any workflow or human response is being interpreted as operational authority.

[Back to top](#top)

---

## 9. Shared executable checks

Run these checks from the repository root at the frozen revision.

### 9.1 Shared RollbackCard fixture profile

```bash
python tools/validators/release/validate_rollback_card.py --fixtures
```

Expected bounded result:

- three valid fixtures emit `PASS`;
- six invalid fixtures emit `FAIL` with their exact expected finding sets;
- process exits `0`;
- no `FIXTURE_POLARITY_ERROR`;
- no authority, policy evaluation, review completion, rollback execution, public mutation, release reference, or publication is created.

Then run the validator unit module:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

Expected bounded result: the schema, metadata, valid/invalid polarity, CLI profile, duplicate-key rejection, non-finite-number rejection, and missing-file failure tests pass.

### 9.2 Shared synthetic rollback rehearsal

```bash
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

Expected bounded result: eight tests pass.

The module verifies:

- deterministic no-write plan;
- synthetic rollback alias change;
- synthetic withdrawal;
- affected manifest/artifact retention;
- append-only correction output;
- complete invalidation record;
- non-synthetic denial;
- incomplete-invalidation denial;
- missing-target denial;
- digest-mismatch denial;
- missing-marker denial.

The unit module is the preferred entry point because it creates and destroys its own temporary roots. Do not use `--apply` against an ad hoc or non-disposable path.

### 9.3 Fauna fixture-safety baseline

```bash
python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Expected bounded result: eight tests pass against the accepted seven-file synthetic fixture inventory.

This proves only Fauna fixture hygiene. It does not validate a Fauna rollback target, policy decision, release record, carrier, or public state.

### 9.4 Static changed-area checks

```bash
git diff --check
git diff -- docs/runbooks/fauna/ROLLBACK_DRILL.md
```

For this documentation-only slice, the shared executable paths should normally be unchanged. Any executable delta expands the review boundary and requires separate validation.

### Evidence labels

| Check | A green result proves | A green result does not prove |
|---|---|---|
| RollbackCard fixtures | proposed candidate shape and local consistency | target safety or approval |
| RollbackCard tests | validator behavior at one SHA | operational execution |
| Synthetic rehearsal tests | isolated temporary-root mechanics | public alias mutation |
| Fauna smoke tests | synthetic fixture hygiene | rollback or release |
| Markdown/static checks | document integrity | doctrine acceptance or implementation |
| Hosted workflow | command status at exact head | human review, release, deployment, or publication |

[Back to top](#top)

---

## 10. Fauna tabletop and synthetic rehearsal procedure

### Step 1 — Freeze the authority and evidence snapshot

Record:

- base and head SHA;
- current target blob;
- shared contract/schema/validator/helper/test blobs;
- scenario ID;
- participant roles;
- start time in UTC;
- declared drill level;
- explicit `public_state_mutated: false`;
- explicit `synthetic_workspace_only: true`.

Do not begin with a floating branch name as the evidence identity.

### Step 2 — Declare the initial hold

The first drill state is:

```text
HOLD_FOR_REVIEW
```

The hold prevents a scenario from being interpreted as permission to restore a target.

### Step 3 — Select a synthetic scenario

Use one scenario from [§7](#7-synthetic-scenario-catalog). Use only toy release identifiers and non-spatial artifact bytes.

Recommended primary tabletop:

```text
scenario_id: rehearsal:fauna:sensitivity-discovery:001
trigger: SENSITIVITY_DISCOVERY
affected_release_ref: release:synthetic:fauna:v2
candidate_target_ref: release:synthetic:fauna:v1
```

This is explanatory drill data, not a repository `RollbackCard` instance.

### Step 4 — State the proposed recovery mode

Choose one candidate posture:

- `ROLLBACK_CANDIDATE`;
- `WITHDRAWAL_CANDIDATE`;
- `HOLD`;
- `ERROR`.

Do not jump directly to rollback because a prior target exists.

### Step 5 — Run the shared candidate profile

Execute [§9.1](#91-shared-rollbackcard-fixture-profile).

If the shared profile fails, stop. Do not weaken the schema, omit negative fixtures, reorder expectations, or bypass the validator to continue the tabletop.

### Step 6 — Run the shared synthetic rehearsal

Execute [§9.2](#92-shared-synthetic-rollback-rehearsal).

Record:

- test count;
- exit status;
- whether plan mode remained no-write;
- whether rollback and withdrawal cases retained affected bytes;
- whether every invalidation class was present;
- fail-closed reason codes exercised.

No custom apply run is required for this document-only drill. The unit module's disposable roots are the accepted bounded execution surface.

### Step 7 — Run the Fauna fixture-safety baseline

Execute [§9.3](#93-fauna-fixture-safety-baseline).

If the accepted Fauna fixtures fail, classify the failure before proceeding. A rollback drill must not claim public-safety readiness while the bounded Fauna hygiene baseline is red.

### Step 8 — Re-evaluate the synthetic target under current Fauna rules

For the tabletop target, answer each question as:

```text
PASS
HOLD
DENY
NOT_APPLICABLE_WITH_EVIDENCE
UNKNOWN
```

| Gate | Tabletop question |
|---|---|
| Identity | Is the target distinct, immutable, and digest-bound? |
| Source role | Would the target preserve observation/model/aggregate/context distinctions? |
| Rights | Are target rights and redistribution permissions current and resolvable? |
| Taxonomy | Are taxon identities and crosswalks current, non-conflicted, and reviewable? |
| Evidence | Do claim-support references resolve without contradiction or withdrawal? |
| Sensitivity | Could target bytes or joins expose exact/reconstructable sensitive locations? |
| Geoprivacy | Are current transforms, receipts, caveats, and review support appropriate? |
| Policy | Is there an accepted current policy result for the target and audience? |
| Review | Are required functional and independent reviews complete? |
| Correction | Is the affected release linked to a correction/withdrawal/supersession path? |
| Integrity | Do manifest and artifact digests match? |
| Time | Are validity, publication, correction, and effective times coherent? |
| Consumers | Is every public carrier and governed consumer inventoried? |
| Recovery | Is post-transition validation and rollback-of-rollback/forward-fix defined? |

Under current repository evidence, several gates remain `HOLD` or `UNKNOWN`. Record that truthfully; do not fabricate passing references.

### Step 9 — Build the affected-carrier inventory

Use [§11](#11-carrier-and-consumer-invalidation-matrix).

Every class must be:

- identified with a synthetic or bounded pointer;
- marked implemented, absent, held, or unknown;
- assigned an expected safe post-transition state;
- assigned a verification method;
- assigned an accountable owner or `NEEDS VERIFICATION`.

### Step 10 — Simulate consumer behavior

For each conceptual consumer, record the required behavior:

- governed API: affected release is not served as current;
- map layer: old carrier is absent, stale, or visibly withdrawn;
- Evidence Drawer: correction and evidence status are visible;
- search/graph/vector: affected references are invalidated or marked stale;
- Focus Mode: answer narrows, abstains, or denies rather than citing withdrawn support;
- AI cache: affected generated answer is not reused;
- export/story/dashboard: affected derivative is withdrawn or superseded.

These are tabletop expectations. Current implementation remains `HOLD / NEEDS VERIFICATION`.

### Step 11 — Verify history preservation

Confirm the shared rehearsal proves that:

- affected synthetic manifest bytes remain;
- affected synthetic artifact bytes remain;
- correction output is appended;
- alias state changes only inside the marked temporary root;
- invalidation intent is recorded;
- no real KFM state changes.

### Step 12 — Measure drill time

Record the timestamps in [§13](#13-time-objectives-and-measurements). Do not compare against an invented target.

### Step 13 — Replay the plan

The shared test executes the same plan twice and expects deterministic equality. Record whether the exact-head test passed.

A real operational replay contract remains unproved.

### Step 14 — Assign the terminal drill outcome

Use [§14](#14-finite-outcomes-and-reason-codes).

For the current maturity, a successful Levels 0–2 run will normally end as:

```text
DRILL_HANDOFF_READY
fauna_integrated_rehearsal: HOLD_FOR_RUNTIME
operational_rollback: HOLD_FOR_AUTHORITY
public_state_mutated: false
```

### Step 15 — Close and hand off

Produce the packet in [§17](#17-drill-handoff-packet), clean up disposable state, and stop. Do not convert the packet into a release or rollback record.

[Back to top](#top)

---

## 11. Carrier and consumer invalidation matrix

The shared helper requires all nine invalidation classes. The table below adds Fauna-specific review questions.

| Class | Fauna-facing risk | Required tabletop evidence | Current execution status |
|---|---|---|---|
| `API_CACHE` | stale occurrence/range/evidence payload remains current | route/profile inventory, cache key/release binding, expected unavailable/superseded state | `UNKNOWN / HOLD` |
| `CDN` | old tile, export, image, or document remains reachable | artifact URLs or surrogate keys, purge plan, verification method | `UNKNOWN / HOLD` |
| `TILES` | old PMTiles/MVT/raster product exposes outdated or unsafe detail | layer/artifact manifest, source-layer identity, sensitivity transform binding | `UNKNOWN / HOLD` |
| `CATALOG` | catalog still advertises withdrawn release | catalog item and release-state transition expectation | `UNKNOWN / HOLD` |
| `TRIPLETS` | graph projection keeps affected claims linked as current | projection version, invalidation/rebuild expectation, evidence state | `UNKNOWN / HOLD` |
| `SEARCH_INDEX` | search returns affected taxa, sites, or summaries | index version, release binding, stale-result behavior | `UNKNOWN / HOLD` |
| `VECTOR_INDEX` | semantic retrieval supplies withdrawn support to AI | index build identity, source release binding, deletion/rebuild or tombstone plan | `UNKNOWN / HOLD` |
| `AI_CACHE` | cached answer cites affected evidence | cache key/evidence refs, invalidation expectation, abstain/deny fallback | `UNKNOWN / HOLD` |
| `DOWNSTREAM_DERIVATIVES` | maps, dashboards, exports, stories, reports, screenshots, or partner copies remain misleading | complete derivative/consumer inventory and notification/correction plan | `UNKNOWN / HOLD` |

### Required additional consumer checks

These do not replace the nine classes:

- governed API response envelope;
- MapLibre layer/source/style state;
- Evidence Drawer bundle/correction state;
- Focus Mode bounded response state;
- export and download surfaces;
- public status/correction notice;
- external mirrors or partner copies, where any exist;
- accessibility and low-connectivity copies;
- operational dashboards and support runbooks.

### Absence is evidence-sensitive

Do not mark a class `NOT_APPLICABLE` merely because no implementation was found in one search. Use:

```text
ABSENT_AT_PINNED_REPOSITORY_SNAPSHOT
UNKNOWN_IN_DEPLOYMENT
```

when deployment evidence is unavailable.

### Synthetic helper limitation

The helper writes one local invalidation JSON containing the complete class list. It does not contact, purge, rebuild, disable, or verify any external carrier. Treat its result as deterministic invalidation-plan evidence only.

[Back to top](#top)

---

## 12. Fauna sensitivity and geoprivacy review

### Protected detail must stay outside the drill

Do not place any of the following in the drill packet:

- precise coordinates or geometry;
- coordinate-like free text;
- source URLs that reveal a private endpoint or location;
- nest, den, roost, hibernacula, breeding, spawning, aggregation, telemetry, or movement detail;
- observer or landowner identity;
- collection notes or media metadata that can reveal place;
- geoprivacy seeds, offsets, masks, radii, thresholds, or reviewer-only methods;
- restricted source identifiers that can be joined back to place.

Use toy references and public-safe reason codes.

### Older is not safer

A prior release may be less safe because it:

- predates a sensitivity discovery;
- uses a superseded transform;
- carries more precise geometry;
- lacks an explicit withholding caveat;
- predates a current rights restriction;
- references a withdrawn source;
- uses an obsolete taxonomic identity;
- can now be reconstructed through newer public joins;
- lacks correction, review, or rollback support required today.

The target must therefore pass current review, not historical policy.

### Transform and receipt posture

A synthetic redaction or geoprivacy reference may be used only as a clearly labeled toy pointer. It does not prove:

- a transform was executed;
- the transform is safe;
- the parameters are current;
- a reviewer approved it;
- a public release is permitted.

Operational use requires the owning transform, receipt, policy, evidence, review, and release records.

### Public-safe failure reporting

A fail-closed result should reveal:

- stable reason code;
- bounded field or object path;
- audience-safe corrective action;
- whether retry is permitted.

It must not reveal the protected value that caused the failure.

### Cross-domain reconstruction

The tabletop must ask whether a generalized Fauna output becomes identifying when combined with:

- habitat;
- hydrology;
- land or parcel context;
- infrastructure and access;
- imagery;
- observation time;
- weather;
- telemetry or movement;
- archival narrative.

If reconstruction resistance is unproved, use `HOLD_FOR_POLICY` or `DENY`.

[Back to top](#top)

---

## 13. Time objectives and measurements

No accepted Fauna rollback RTO or RPO target was verified at the pinned snapshot. Record measured values without inventing objectives.

### Required timestamps

| Field | Meaning |
|---|---|
| `incident_declared_at` | synthetic issue enters drill hold |
| `scope_frozen_at` | exact revision, scenario, and terminal boundary fixed |
| `candidate_validated_at` | shared RollbackCard profile completes |
| `rehearsal_completed_at` | shared synthetic test module completes |
| `fauna_review_completed_at` | tabletop target and carrier review completes |
| `safe_state_expected_at` | tabletop predicts all affected consumers would be safe |
| `handoff_completed_at` | bounded packet delivered |
| `replay_completed_at` | deterministic replay evidence collected |

All timestamps must be timezone-aware and recorded in UTC.

### Measured drill RTO

```text
measured_drill_rto =
  handoff_completed_at - incident_declared_at
```

This is the time to a reviewable synthetic handoff, not time to restore production.

A future operational RTO would require a separately accepted definition, start event, safe-state definition, instrumentation, owner, and target.

### Measured recovery-point posture

Record:

- affected synthetic release identity and time;
- candidate target identity and time;
- difference in supported data currency;
- claims, corrections, or coverage that would be lost or superseded;
- whether withdrawal avoids restoring stale or unsafe content.

Do not compress that into a single number if the releases have different spatial, temporal, taxonomic, or evidentiary coverage.

### Clock integrity

Record:

- wall-clock source;
- timezone;
- monotonic duration where available;
- workflow start/end times;
- pauses awaiting human review separately from execution time.

### Performance result labels

Use:

```text
MEASURED
NOT_MEASURED
TARGET_UNKNOWN
TARGET_MET
TARGET_MISSED
```

`TARGET_MET` is forbidden until an accepted target exists.

[Back to top](#top)

---

## 14. Finite outcomes and reason codes

### Shared candidate dispositions

The current `RollbackCard` profile permits:

| Disposition | Meaning |
|---|---|
| `ROLLBACK_CANDIDATE` | proposes a distinct prior release |
| `WITHDRAWAL_CANDIDATE` | proposes withdrawal without a prior target |
| `HOLD` | records an unresolved or blocked posture |
| `ERROR` | records an invalid or failed candidate evaluation |

These are candidate values, not drill or operational completion states.

### Drill outcomes

| Outcome | Meaning |
|---|---|
| `DRILL_HANDOFF_READY` | Levels 0–2 completed at an exact revision; limitations and holds are explicit |
| `HOLD_FOR_TARGET` | no distinct, immutable, currently admissible target |
| `HOLD_FOR_EVIDENCE` | support references are missing, unresolved, contradicted, or withdrawn |
| `HOLD_FOR_POLICY` | rights, sensitivity, geoprivacy, or policy posture is incomplete |
| `HOLD_FOR_REVIEW` | required functional or independent review is incomplete |
| `HOLD_FOR_CARRIER_INVENTORY` | downstream consumer or invalidation scope is incomplete |
| `HOLD_FOR_RUNTIME` | required Fauna adapter, executor, alias, or invalidator is absent or unproved |
| `HOLD_FOR_AUTHORITY` | no accountable operational decision/execution authority |
| `DENY` | request or target is prohibited or would expose protected material |
| `ERROR` | integrity, parsing, dependency, execution, or evidence-capture failure |
| `NO_ACTION` | no recovery transition is supported by the drill evidence |

### Shared fail-closed reason codes exercised

The synthetic helper and shared candidate validator include stable reasons such as:

```text
NON_SYNTHETIC_INPUT_DENIED
SYNTHETIC_MARKER_MISSING
INVALIDATION_SET_INCOMPLETE
REQUIRED_FILE_MISSING
ARTIFACT_DIGEST_MISMATCH
CURRENT_ALIAS_DIGEST_MISMATCH
TARGET_MANIFEST_DIGEST_MISMATCH
TARGET_EQUALS_AFFECTED
HISTORY_MUTATED
GOVERNANCE_BOUNDARY_VIOLATION
TARGET_RELEASE_REQUIRED
CORRECTION_NOTICE_REQUIRED
DECISION_BEFORE_DETECTION
EFFECTIVE_BEFORE_DECISION
```

Do not reuse an internal message as a public reason if it reveals sensitive detail.

### Prohibited completion language

Do not emit:

```text
ROLLBACK_COMPLETE
PRODUCTION_SAFE
POLICY_APPROVED
RELEASE_APPROVED
PUBLICATION_RESTORED
```

unless a future accepted operational process and post-transition proof support those exact claims.

[Back to top](#top)

---

## 15. Acceptance matrix

### Levels 0–2 acceptance

| Requirement | Evidence | Required result |
|---|---|---|
| Exact revision frozen | SHA and clean/explained tree | `PASS` |
| Synthetic/no-network boundary | environment, no credentials, test-created roots | `PASS` |
| No protected detail | scenario and output review | `PASS` |
| Shared RollbackCard fixtures | validator `--fixtures` | `PASS` |
| Shared validator tests | exact unittest module | `PASS`, non-vacuous |
| Shared synthetic rehearsal | exact unittest module | eight tests pass |
| Fauna fixture hygiene | exact Fauna smoke module | eight tests pass |
| Complete invalidation classes | shared scenario/report and tabletop matrix | all nine present |
| Affected history preserved | shared rehearsal assertions | `PASS` |
| Target-current-policy review | tabletop matrix | blockers explicit |
| Consumer inventory | matrix | no silent omissions |
| Real public mutation | report and scope | `false` |
| Authority created | report and scope | `false` |
| Measured times | timestamp record | present or `NOT_MEASURED` |
| Exact-head CI | workflow/check inventory | current and classified |
| Operational levels | final packet | explicitly held |

### Current blocked acceptance

The following cannot truthfully pass under the pinned evidence:

| Requirement | Current state |
|---|---|
| Accepted Fauna rollback contract/profile | `HOLD` |
| Fauna rollback fixtures and direct executable tests | `HOLD` |
| Accepted Fauna rollback pipeline/adapter | `HOLD` |
| Actual affected and prior `ReleaseManifest` | `HOLD / UNKNOWN` |
| Current-policy target evaluator | `HOLD` |
| Authenticated reviewer and signer path | `HOLD` |
| External alias mutation | `HOLD` |
| External cache/tile/catalog/index invalidation | `HOLD` |
| Public API/map/Evidence Drawer/Focus Mode post-check | `HOLD` |
| Post-rollback proof and execution receipt | `HOLD` |
| Accepted operational RTO/RPO | `UNKNOWN` |

### Definition of done for this document

This documentation slice is complete when:

- the scaffold is replaced by this bounded procedure;
- current executable and held surfaces are distinguished;
- commands match repository entry points;
- sensitive-detail rules are explicit;
- the operational hold is visible;
- review, merge, release, deployment, promotion, and publication remain separate.

[Back to top](#top)

---

## 16. Hosted CI and evidence interpretation

### `rollback-drill`

`.github/workflows/rollback-drill.yml` runs on pull requests and preserves the stable job names:

```text
simulate-rollback
verify-published-aliases
```

At the pinned definition it:

- installs declared repository test dependencies;
- confirms the production rollback pipeline remains a placeholder;
- confirms the generic legacy validator entry point delegates to the canonical
  release validator with byte-identical fixture output;
- validates the stronger release-scoped `RollbackCard` fixture profile;
- runs the non-vacuous shared synthetic rehearsal tests;
- confirms direct domain drill material remains guidance-only where expected;
- inspects rollback-card placeholder inventory;
- holds production rollback;
- holds published-alias verification while the auditor and governed aliases remain unimplemented.

A green `rollback-drill` check therefore proves the current bounded readiness/hold assertions at the tested SHA. It does not prove a production rollback.

### `rollback-rehearsal`

`.github/workflows/rollback-rehearsal.yml` is path-filtered to the shared helper, test, fixture, workflow, and shared runbook paths. A change only to this Fauna document may not trigger it.

Do not report it as passing unless a run exists at the exact head. The same test module may still be exercised by `rollback-drill`.

### Fauna workflow

The Fauna domain workflow may run according to its current trigger/path configuration. Report the exact job and SHA rather than assuming coverage from the document's location.

### Exact-head rule

For every hosted result:

1. record workflow and job name;
2. record tested SHA;
3. record conclusion and completion time;
4. distinguish a real execution from an explicit hold assertion;
5. classify failure as `INTRODUCED`, `INHERITED`, `INFRASTRUCTURE`, or `NEEDS VERIFICATION`;
6. rerun after every head change.

A green check on an older head is stale evidence.

### Evidence axes remain separate

| Axis | Example | Does not prove |
|---|---|---|
| bytes | document exists at commit | correctness |
| local check | unit module passes | hosted execution |
| hosted check | job passes at head | human review |
| review | reviewer approves PR | release decision |
| merge | bytes enter `main` | deployment or promotion |
| synthetic apply | temp alias changes | public mutation |
| operational release | future governed transition | publication unless separately authorized |

[Back to top](#top)

---

## 17. Drill handoff packet

Use a value-safe packet such as:

```yaml
runbook: docs/runbooks/fauna/ROLLBACK_DRILL.md
runbook_version: v0.1
base_sha: <immutable base>
head_sha: <immutable head>
scenario_id: rehearsal:fauna:sensitivity-discovery:001
scenario_class: synthetic
drill_levels_attempted: [TABLETOP, SHARED_CANDIDATE_PROFILE, SHARED_SYNTHETIC_REHEARSAL]
affected_release_ref: release:synthetic:fauna:v2
candidate_target_ref: release:synthetic:fauna:v1
candidate_disposition: HOLD
drill_outcome: DRILL_HANDOFF_READY
fauna_integrated_rehearsal: HOLD_FOR_RUNTIME
operational_rollback: HOLD_FOR_AUTHORITY
public_state_mutated: false
authority_created: false
synthetic_workspace_only: true
network_source_access: false
protected_detail_present: false
commands:
  rollback_card_fixtures: python tools/validators/release/validate_rollback_card.py --fixtures
  rollback_card_tests: python -m unittest discover --start-directory tests/validators --pattern test_validate_rollback_card.py --verbose
  synthetic_rehearsal: python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
  fauna_fixture_hygiene: python -m unittest discover --start-directory tests/domains/fauna --pattern test_fauna_smoke.py --verbose
results:
  rollback_card_fixtures: PASS | FAIL | NOT_RUN
  rollback_card_tests: PASS | FAIL | NOT_RUN
  synthetic_rehearsal: PASS | FAIL | NOT_RUN
  fauna_fixture_hygiene: PASS | FAIL | NOT_RUN
invalidations:
  - API_CACHE
  - CDN
  - TILES
  - CATALOG
  - TRIPLETS
  - SEARCH_INDEX
  - VECTOR_INDEX
  - AI_CACHE
  - DOWNSTREAM_DERIVATIVES
timestamps:
  incident_declared_at: <UTC>
  scope_frozen_at: <UTC>
  handoff_completed_at: <UTC>
measurements:
  measured_drill_rto: <duration or NOT_MEASURED>
  operational_rto_target: TARGET_UNKNOWN
  operational_rpo_target: TARGET_UNKNOWN
review:
  repository_route: "@bartytime4life"
  fauna_steward: NEEDS_VERIFICATION
  sensitivity_reviewer: NEEDS_VERIFICATION
  evidence_policy_reviewer: NEEDS_VERIFICATION
  release_rollback_steward: NEEDS_VERIFICATION
  independent_reviewer: NEEDS_VERIFICATION
hosted_checks:
  exact_head: <sha>
  status: <per-job results>
open_blockers:
  - <safe blocker code and next evidence>
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
```

### Packet rules

- Never include protected values.
- Do not place the packet in a release, proof, receipt, or published lane unless its owning contract explicitly admits it.
- A Markdown handoff is not a `RollbackCard` instance.
- A JSON file resembling the schema is not an approved decision.
- Keep command output and workflow logs bounded and value-safe.
- Record `NOT_RUN`, `UNKNOWN`, and `NEEDS_VERIFICATION` rather than guessing.

[Back to top](#top)

---

## 18. Failure diagnosis

| Symptom | Likely meaning | Required response |
|---|---|---|
| `jsonschema` import fails | declared test environment not installed or drifted | `ERROR`; use repository-native locked install, do not unpin |
| shared valid fixture fails | contract/schema/validator drift | stop and reconcile exact profile |
| shared invalid fixture passes | fail-closed regression | `FAIL`; do not delete or weaken fixture |
| `FIXTURE_POLARITY_ERROR` | expected finding set differs | inspect semantic change; no bypass |
| `Ran 0 tests` | vacuous command or discovery failure | `ERROR`; correct entry point |
| `NON_SYNTHETIC_INPUT_DENIED` | scenario is not explicitly synthetic | `DENY`; do not override |
| marker failure | root is not accepted as disposable synthetic state | `DENY`; use test-created root |
| digest mismatch | artifact, alias, or manifest differs from expected bytes | `HOLD_FOR_TARGET`; investigate |
| incomplete invalidations | one or more carrier classes omitted | `HOLD_FOR_CARRIER_INVENTORY` |
| history mutation | affected bytes changed | stop, preserve evidence, diagnose helper/environment |
| Fauna smoke failure | fixture-hygiene regression or drift | stop; classify before drill handoff |
| protected value appears in output | log-safety failure or exposure | stop, contain output, follow correction/incident process |
| target would restore greater precision | current target is unsafe | `DENY` or withdrawal/forward correction |
| policy/evidence reference unresolved | support closure missing | `HOLD_FOR_EVIDENCE` or `HOLD_FOR_POLICY` |
| hosted head differs | stale CI evidence | rerun at new head |
| unrelated check fails | inherited or infrastructure failure possible | compare base/head and classify truthfully |
| green hold workflow | current absence/guardrail assertion passed | do not reinterpret as operational readiness |

### Never repair a drill by

- using a real release because synthetic data is inconvenient;
- removing a negative test;
- weakening a closed schema;
- omitting an invalidation class;
- changing expected digests to match tampered bytes without explanation;
- storing exact sensitive detail in a report;
- marking unknown consumers not applicable;
- converting a hold to pass for schedule reasons;
- treating generated text as review or evidence.

[Back to top](#top)

---

## 19. Correction, cleanup, and document rollback

### Disposable-state cleanup

The accepted shared unit module uses temporary directories and cleans them in test teardown.

For any separately authorized synthetic workspace:

- verify the exact synthetic marker;
- keep it outside repository lifecycle, release, and public paths;
- retain only value-safe result summaries required for review;
- remove the disposable workspace after review evidence is captured;
- do not retain toy aliases where they can be mistaken for operational state.

### If the drill discovers a real issue

Stop the drill. Preserve value-safe evidence and route the issue through:

- [Fauna Rollback Runbook](./ROLLBACK_RUNBOOK.md);
- the applicable correction/withdrawal process;
- rights, sensitivity, geoprivacy, evidence, policy, security, and release review.

Do not continue a tabletop as a substitute for containment or authorized correction.

### Correction of a drill packet

If a packet contains a factual error:

1. mark it superseded or corrected;
2. identify the exact prior packet;
3. state the correction without adding protected detail;
4. preserve lineage;
5. rerun affected checks if the error changes the conclusion.

### Rollback of this documentation change

Revert the feature-branch commit or pull request that updates this file.

That rollback:

- restores the prior documentation bytes;
- does not alter the shared schema, validator, helper, tests, workflows, source state, release state, public aliases, or published artifacts;
- does not reverse a real rollback;
- does not erase review history.

[Back to top](#top)

---

## 20. Current holds and smallest next slice

### Current holds

1. **Local runbook boundary** — `docs/runbooks/fauna/README.md` remains a one-byte placeholder.
2. **Fauna schema authority** — the domain rollback schema is a permissive greenfield stub and conflicts in maturity with the stronger shared release profile.
3. **Missing Fauna contract/profile** — the domain schema's declared contract, fixture root, and validator paths are absent.
4. **Missing direct Fauna tests** — the established `tests/domains/fauna/release/rollback/` lane has no executable tests.
5. **Pipeline authority** — the Fauna rollback adapter/pipeline is documentation-only or unproved; the production rollback pipeline remains a placeholder.
6. **Actual release identity** — no accepted affected and target Fauna manifests were verified.
7. **Current policy target check** — no accepted evaluator binds Fauna target evidence, rights, sensitivity, geoprivacy, taxonomy, and review.
8. **Operational aliases** — no accepted public alias profile or executable auditor is proven.
9. **External invalidation** — no executor or receipt proves all nine carrier invalidations.
10. **Governed consumers** — API, map, Evidence Drawer, Focus Mode, search, graph, vector, export, and AI post-transition checks are unproved.
11. **Authority and separation** — functional roles and independent review are unassigned.
12. **RTO/RPO** — no accepted objectives or operational measurement path.
13. **Path convergence** — `release/rollback/`, `release/correction/rollback/`, `release/rollback_cards/`, and data-plane rollback support retain documented boundary questions.

### Smallest next executable Fauna slice — PROPOSED

The smallest coherent follow-up is one no-network, synthetic, non-publishing Fauna adapter test that reuses the shared controls rather than inventing a second rollback engine.

Proposed acceptance boundary:

1. perform a placement check against Directory Rules and the existing direct Fauna rollback test lane;
2. define one toy sensitivity-discovery scenario with no geometry and no real source identity;
3. validate a shared `RollbackCard` candidate or a narrowly defined Fauna adapter over that shared profile;
4. run only in a marker-protected temporary root;
5. require all nine invalidation classes;
6. assert target revalidation returns `HOLD` when current Fauna policy/evidence support is unresolved;
7. assert protected values never appear in output;
8. assert affected history is retained;
9. assert no real public state, release, source, policy, review, deployment, promotion, or publication changes;
10. wire an exact, non-vacuous test command and path-scoped hosted check.

The follow-up should not:

- create an actual Fauna release;
- activate eBird, GBIF, iNaturalist, telemetry, media, or another source;
- introduce exact location fixtures;
- bypass the shared release contract;
- admit a production alias;
- implement external invalidation;
- claim operational readiness.

### Graduation sequence

```text
shared synthetic mechanics
  -> one Fauna adapter fixture/test
  -> current-policy target assessment
  -> governed consumer inventory
  -> mirror-only carrier rehearsal
  -> independent review and separation of duties
  -> operational proposal
```

Each arrow is a separate reviewable transition.

[Back to top](#top)

---

## 21. Related surfaces

### Governing and domain documents

- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Fauna domain README](../../domains/fauna/README.md)
- [Fauna sensitivity](../../domains/fauna/SENSITIVITY.md)
- [Fauna policy](../../domains/fauna/POLICY.md)
- [Fauna release index](../../domains/fauna/RELEASE_INDEX.md)

### Runbooks

- [Fauna rollback](./ROLLBACK_RUNBOOK.md)
- [Fauna no-network tests](./NO_NETWORK_TEST_RUNBOOK.md)
- [Shared synthetic rollback rehearsal](../rollback-rehearsal.md)

### Shared contracts and proof

- [`RollbackCard` contract](../../../contracts/release/rollback_card.md)
- [`RollbackCard` schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Candidate validator](../../../tools/validators/release/validate_rollback_card.py)
- [Validator tests](../../../tests/validators/test_validate_rollback_card.py)
- [Candidate fixtures](../../../fixtures/release/rollback_card/README.md)
- [Synthetic rehearsal helper](../../../tools/release/rollback_apply.py)
- [Synthetic rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)

### Fauna and release lanes

- [Direct Fauna rollback test lane](../../../tests/domains/fauna/release/rollback/README.md)
- [Fauna rollback pipeline guidance](../../../pipelines/rollback/fauna/README.md)
- [Release rollback parent](../../../release/rollback/README.md)
- [Release rollback Fauna lane](../../../release/rollback/fauna/README.md)
- [Data-plane Fauna rollback support](../../../data/rollback/fauna/README.md)

### Workflows

- [Rollback rehearsal](../../../.github/workflows/rollback-rehearsal.yml)
- [Rollback drill readiness](../../../.github/workflows/rollback-drill.yml)

[Back to top](#top)

---

## 22. Change log

| Version | Date | Change |
|---|---|---|
| Unversioned scaffold | prior to 2026-08-24 | Planned-file placeholder sourced from the Fauna missing/planned register. |
| `v0.1` | 2026-08-24 | Replaced scaffold with repository-grounded Levels 0–2 drill procedure; documented shared executable candidate/rehearsal controls, Fauna fail-closed tabletop, exact commands, invalidation matrix, measurements, finite outcomes, handoff, cleanup, operational holds, and smallest next slice. |

---

**Current final disposition**

```text
shared_candidate_profile: EXECUTABLE / NON-AUTHORITATIVE
shared_synthetic_rehearsal: EXECUTABLE / SYNTHETIC-ONLY
fauna_tabletop: AVAILABLE
fauna_integrated_rehearsal: HOLD
fauna_operational_rollback: HOLD / DENY-BY-DEFAULT
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
```

[Back to top](#top)
